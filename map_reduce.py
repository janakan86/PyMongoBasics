from pymongo import MongoClient
from pprint import pprint
import setup.data_loading


closuresDB = setup.data_loading.load_basic_data()

# just to check whether the load worked
findOne = closuresDB.roadClosures.find_one({"OBJECTID": "2264"})
pprint(findOne)
