from pymongo import MongoClient
from pprint import pprint
import setup.data_loading


closuresDB = setup.data_loading.load_basic_data()

# $project pipeline stage { $project: { <specification(s)> } }
# 1 denotes include field, _id is added by default, can exclude it by providing 0
projectFields = {"$project": {"_id": 0, "ERC_ID": 1, "ROAD_CLOSURE_TYPE": 1, "INCIDENT_TYPE": 1,
                              "CLOSED_ROAD_NAME": 1}}


# $sort pipeline stage { $sort: { <field1>: <sort order>, <field2>: <sort order> ... } }
# -1 denotes descending, 1 ascending
sortBy = {"$sort": {"ERC_ID": -1}}


# $limit pipeline stage { $limit: <positive integer> }
limitDocs = {"$limit": 100}


# $Group pipeline stage { $group: { _id: <expression>, <field1>: { <accumulator1> : <expression1> }, ... } }
# group the road closures by the ROAD CLOSURE TYPE and  Incident Type add 1 for each occurrence
groupClosureType = {"$group": {"_id":   {"closure_type": "$ROAD_CLOSURE_TYPE", "incident_type": "$INCIDENT_TYPE"},
                               "total": {"$sum": 1}}}


pipeLine = [projectFields, sortBy, limitDocs, groupClosureType]
cursor = closuresDB.roadClosures.aggregate(pipeLine)
result = list(cursor)
#pprint(result)


# groupBy null can  be used too
groupByNull = {"$group": {"_id": "null", "noOfGroups": {"$sum": 1}}}

# wer are not applying the groupClosureType.
pipeLine = [projectFields, sortBy, limitDocs, groupByNull]
cursor = closuresDB.roadClosures.aggregate(pipeLine)
result = list(cursor)
#pprint(result)

pipeLine = [projectFields, sortBy, limitDocs, groupClosureType, groupByNull]
cursor = closuresDB.roadClosures.aggregate(pipeLine)
result = list(cursor)
#pprint(result)
