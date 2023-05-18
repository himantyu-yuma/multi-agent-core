import logging

from pymongo.errors import OperationFailure
from pymongo.mongo_client import MongoClient

logger = logging.getLogger(__name__)

DEFAULT_CONNECTION_STRING = (
    "mongodb://root:root@mongo:27017/messages?authSource=admin"
)


class MongoDB:
    def __init__(
        self,
        collection_name="data",
        connection_string: str = DEFAULT_CONNECTION_STRING,
    ):
        try:
            self.client = MongoClient(connection_string)
            self.db = self.client.get_default_database()
        except OperationFailure as error:
            logger.error(error)

        self.collection = self.db.get_collection(collection_name)

    def ping(self):
        try:
            self.client.admin.command("ping")
            print("You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

    def insert_one(self, data):
        return self.collection.insert_one(data)

    def close_connection(self):
        self.client.close()

    def find_one(self, query):
        return self.collection.find_one(filter=query)

    def find_many(self, query):
        return self.collection.find(filter=query)
