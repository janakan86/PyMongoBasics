# Project Title
PyMongoBasics

## Description
Contains examples for beginners who would like to learn using PyMongo to work with Mongo DB. 
The examples makes use of publicly available road closure data from the State of Victoria, Australia

### Prerequisites
The following software needs to be installed in your machine

```
Mongo DB
Python
PyMongo Package
```

## Running the examples

* Make sure the Mongo Daemon is up and running 

* Set the URL of the running mongo in the properties. py
```
 mongoDB_url = 'mongodb://localhost:27017'
```

* execute any of the following python scripts.
1. basics.py
2. aggregate.py
3. map_reduce.py
4. indexing.py

Each of the above scripts would load the sample data from a CSV file into MongoDB (if not already loaded) and run the examples.
