import json
from time import sleep
from confluent_kafka import Producer

from mongo_connection import get_n_documents

from congif import settings, kafka_producer_config

producer = Producer(kafka_producer_config.model_dump(by_alias=True))


def serialize_doc(doc: dict):
    if doc and "_id" in doc:
        doc["_id"] = doc["_id"].__str__()
    return doc


def serialize_docs(docs: list[dict]):
    return [serialize_doc(doc) for doc in docs]


def process_seed_data(types: str):
    s = 0
    l = 30
    t = types
    documents = get_n_documents(t, s, l)
    while len(documents) > 0:
        documents = serialize_docs(documents)
        for document in documents:
            try:
                value = json.dumps(document).encode("utf-8")
                send_document(value)
                sleep(0.5)
            except Exception as e:
                print(f"Error sending document: {e}")
        s = l
        l += 30
        documents = get_n_documents(t, s, l)
    print("Data sent successfully.")

def send_document(value):
    producer.produce(
        topic=settings.KAFKA_TOPIC,
        value=value,
    )
    producer.flush()
