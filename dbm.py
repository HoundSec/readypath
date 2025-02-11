from pymongo import MongoClient
from datetime import datetime, timezone
from os import getenv

class DBM:
    def __init__(self):
        # Initialize connection to MongoDB and create 'URLs' collection if not exists.
        self.client = MongoClient(getenv("MONGO_URI",default="mongodb://mongo:27017/"))
        self.db = self.client["readypath"]  # Database name
        self.collection = self.db["URLs"]  # Collection name

        # Ensure 'token' field has a unique index
        self.collection.create_index("token", unique=True)

    def get_url(self, token):
        data = self.collection.find_one(
                    {"token": token},
                    {"_id": 0, "url": 1},
                    collation={"locale": "en", "strength": 2}
                )
        return data["url"] if data else None

    def token_exists(self, token):
        # Check if a given token already exists in the collection.
        return self.collection.count_documents({"token": token}) > 0

    def insert_data(self, url, token, ip_address):
        document = {
            "url": url,
            "token": token,
            "ip_address": ip_address,
            "date_created": datetime.now(timezone.utc)
        }
        self.collection.insert_one(document)

    def get_whole_document(self, token):
        # Fetch the entire record associated with a given token.
        return self.collection.find_one({"token": token}, {"_id": 0})
