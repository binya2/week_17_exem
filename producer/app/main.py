from mongo_connection import insert_data_from_json

if "__main__" == __name__:
    insert_data_from_json("suspicious_customers_orders.json")