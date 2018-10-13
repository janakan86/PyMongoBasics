import setup.properties
from pymongo import MongoClient
import json
import csv


def load_csv_data():
    # open road closures CSV file
    file = open(setup.properties.input_file_path)

    # Change each field name to the appropriate field name. I know, so difficult.
    reader = csv.DictReader(file, fieldnames= setup.properties.csv_columns)

    # Parse the CSV into JSON
    jsonData = json.dumps([row for row in reader])

    # write CSV data into a JSON file
    jsonFile = open(setup.properties.output_file_path, 'w')
    jsonFile.write(jsonData)
    jsonFile.close()


def open_json_file():
    return open(setup.properties.output_file_path, "r")


def load_basic_data():
    # connect to MongoDB
    client = MongoClient(setup.properties.mongoDB_url)

    # create / access a DB called Closures
    closuresDB = client.Closures

    if closuresDB.roadClosures.count()== 0 :
        # read CSV File and convert it to a JSON
        load_csv_data()

        # open JSON file for processing
        jsonFile = open_json_file()
        jsonData = json.load(jsonFile)

        for element in jsonData:
            closuresDB.roadClosures.insert_one(element)

    return closuresDB