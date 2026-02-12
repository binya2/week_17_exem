from consumer.app.mysql_connection import init_db
from kafka_consumer import consumer_run

if __name__ == "__main__":
    init_db()
    consumer_run()

