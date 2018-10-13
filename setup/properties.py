mongoDB_url = 'mongodb://localhost:27017'

input_file_path = 'setup/Road_closures.csv'
output_file_path = 'setup/parsedRoadClosures.json'

csv_columns = ("OBJECTID", "ERC_ID", "OBJECTID_1", "ERC_ID_1", "INCIDENT_TYPE",
               "INCIDENT_STATUS", "COMMS_COMMENT", "ROAD_CLOSURE_TYPE",
               "DECLARED_ROAD_NUMBER", "DECLARED_ROAD_NAME", "DECLARED_ROAD_DIRECTION",
               "CLOSED_ROAD_NAME", "CLOSED_ROAD_SRNS", "CLOSED_ROAD_RMA_CLASS",
               "CLOSED_ROAD_LGA", "CLOSED_ROAD_VR_REGION", "CLOSED_ROAD_SES_REGION",
               "CLOSED_ROAD_TRAM", "CLOSED_ROAD_BUS", "INCIDENT_DISTANCE",
               "INCIDENT_DIRECTION",
               "INCIDENT_INT_ROAD_NAME", "INCIDENT_LOCALITY", "INCIDENT_MELWAY",
               "INCIDENT_VCSD",
               "START_INT_ROAD_NAME", "START_INT_LOCALITY", "END_INT_ROAD_NAME",
               "END_INT_LOCALITY",
               "DT_CREATED", "DT_UPDATED", "DT_PUBLISH_UNTIL", "DT_LAST_LN_UPDATE",
               "POINT_TYPE")
