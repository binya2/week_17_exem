import json

from pymongo import MongoClient

mongodb_client = MongoClient("mongodb://localhost:27017/")
db = mongodb_client["test"]
collection = db["wekk_17_exem"]
collection.drop()

def insert_data_from_json(file_path):
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
            if isinstance(data, list):
                collection.insert_many(data)
            else:
                collection.insert_one(data)
        print("Data inserted successfully.")
    except Exception as e:
        print(f"Error inserting data: {e}")


def get_n_documents(n):
    return collection.find().limit(n)