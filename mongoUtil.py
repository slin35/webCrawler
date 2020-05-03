import requests
from pymongo import MongoClient

class DBConnector:
    def __init__(self):
        print('Establishing MongoDB connection...', end = '')
        client = MongoClient("mongodb://localhost:27017/")
        print('done.')

        self._db = client["urldb"]
        self._collection = self._db["urls"]

    def insert_url(self, dict):
        self._collection.insert(dict)
