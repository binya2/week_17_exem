from mongo_connection import insert_data_from_json
from kafka_publisher import process_seed_data

if "__main__" == __name__:
    insert_data_from_json("suspicious_customers_orders.json")
    process_seed_data()
