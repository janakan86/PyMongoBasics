from pymongo import MongoClient
from pprint import pprint
from bson.code import Code
import setup.data_loading


closuresDB = setup.data_loading.load_basic_data()

# just to check whether the load worked
findOne = closuresDB.roadClosures.find_one({"OBJECTID": "2264"})
# pprint(findOne)


# Example 1
# Retrieve the road closure due to bad weather and list down the roads that were closed
# and the total of distance of closures for each road.

map_function = Code("""
                    function (){
                        emit( this.CLOSED_ROAD_NAME, this.INCIDENT_DISTANCE);
                    }
            """)

reduce_function = Code("""
                    function (key, values){
                        return Array.sum(values);
                    }
            """)


# JS command - closuresDB.roadClosures.map_reduce
# (mapper, reducer, {out:"myresult", query: {INCIDENT_TYPE : Weather}}
result = closuresDB.roadClosures.map_reduce(map_function, reduce_function,
                                            out="myresult", query={"INCIDENT_TYPE": "Weather"})

for doc in result.find():
    pprint(doc)



