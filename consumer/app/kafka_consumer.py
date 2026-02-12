import json

from confluent_kafka import Consumer

from congif import settings, kafka_consumer_config
from mysql_connection import insert_customer, insert_order

consumer_config = kafka_consumer_config.model_dump(by_alias=True)
consumer = Consumer(consumer_config)


def consumer_run():
    consumer.subscribe([settings.KAFKA_TOPIC])
    print(f"🟢 Consumer is running and subscribed to {settings.KAFKA_TOPIC} topic")
    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                print("❌ Error:", msg.error())
                continue
            value = msg.value().decode("utf-8")
            schema = json.loads(value)

            types = schema.get("type")
            schema.pop("type", None)
            schema.pop("_id", None)
            if types == "customer":
                insert_customer(schema)
            elif types == "order":
                insert_order(schema)
            else:
                print("Invalid message type")


    except KeyboardInterrupt:
        print("\n🔴 Stopping consumer")
    finally:
        consumer.close()
