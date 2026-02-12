from mongo_connection import insert_data_from_json
from kafka_publisher import process_seed_data

if __name__ == "__main__":
    insert_data_from_json("suspicious_customers_orders.json")
    process_seed_data("customer")
    process_seed_data("order")
