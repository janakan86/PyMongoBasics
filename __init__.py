from pymongo import MongoClient
import data_loading
import properties
import json


# read CSV File and convert it to a JSON
data_loading.load_csv_data()

# open JSON file for processing
jsonFile = data_loading.open_json_file()
jsonData = json.load(jsonFile)

# connect to MongoDB
client = MongoClient(properties.mongoDB_url)


# create / access a DB called Closures
closuresDB = client.Closures

# drop the collection called roadClosures if exists
closuresDB.roadClosures.drop()





