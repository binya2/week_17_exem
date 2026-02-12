from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    KAFKA_TOPIC: str = Field(default="documents", serialization_alias="kafka_topic")


settings = Settings()


class KafkaConsumerConfig(BaseSettings):
    KAFKA_BOOTSTRAP_SERVERS: str = Field(default="localhost:9092", serialization_alias="bootstrap.servers")
    KAFKA_GROUP_ID: str = Field(default="consumer-group", serialization_alias="group.id")
    KAFKA_AUTO_OFFSET_RESET: str = Field(default="earliest", serialization_alias="auto.offset.reset")


kafka_consumer_config = KafkaConsumerConfig()


class MysqlConfig(BaseSettings):
    MYSQL_HOST: str = Field(default="localhost", serialization_alias="host")
    MYSQL_PORT: int = Field(default=3306, serialization_alias="port")
    MYSQL_USER: str = Field(default="root", serialization_alias="user")
    MYSQL_ROOT_PASSWORD: str = Field(default="root_password", serialization_alias="password")

mysql_config = MysqlConfig()