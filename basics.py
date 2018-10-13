from pymongo import MongoClient
from pprint import pprint
import setup.data_loading
import setup.properties
import json

# read CSV File and convert it to a JSON
setup.data_loading.load_csv_data()

# open JSON file for processing
jsonFile = setup.data_loading.open_json_file()
jsonData = json.load(jsonFile)

# connect to MongoDB
client = MongoClient(setup.properties.mongoDB_url)


# create / access a DB called Closures
closuresDB = client.Closures

# drop the collection called roadClosures if exists
closuresDB.roadClosures.drop()

# insert a single document
closuresDB.roadClosures.insert_one(jsonData[1])


# upsert all the documents in the JSON file
# this JSON file starts with a square bracket.Therefore keys() will not work at root level,
# therefore need to iterate elements.
# Check if docs exist with same OBJECTID, if so replace, otherwise insert.
for element in jsonData:
    closuresDB.roadClosures.update({"OBJECTID": element["OBJECTID"]}, element, upsert=True)

# find a single document
findOne = closuresDB.roadClosures.find_one({"OBJECTID": "2264"})
pprint(findOne)

# find multiple documents. This returns a cursor
findMany = closuresDB.roadClosures.find({"CLOSED_ROAD_NAME": "WANGARATTA ROAD"})
print('Number of closures in Wangaratta ', findMany.count())




# create a index


# sort results

# projection


# play around with aggregates

# map reduce





