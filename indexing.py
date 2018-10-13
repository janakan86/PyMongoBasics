from pymongo import MongoClient
from pprint import pprint
import setup.data_loading


closuresDB = setup.data_loading.load_basic_data()


# find a single document
findOne = closuresDB.roadClosures.find_one({"OBJECTID": "2264"})
pprint(findOne)
