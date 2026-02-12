import json
from pathlib import Path

from pymongo import MongoClient

from congif import mongo_config

mongodb_client = MongoClient(mongo_config.MONGODB_URL)
db = mongodb_client["test"]
collection = db["wekk_17_exem"]
collection.drop()


def insert_data_from_json(file_path):
    try:
        file_path = Path(__file__).resolve().parent / file_path
        with open(file_path, "r") as f:
            data = json.load(f)
            if isinstance(data, list):
                collection.insert_many(data)
            else:
                collection.insert_one(data)
        print("Data inserted successfully.")
    except Exception as e:
        print(f"Error inserting data: {e}")


def get_n_documents(t,s,l):
    return collection.find({"type":t}).sort(f"{t}Number").skip(s).limit(l).to_list(length=30)
