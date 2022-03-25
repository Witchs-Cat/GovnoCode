import os, asyncio
from pymongo import MongoClient

class MongoDb:
    def __init__(self):
        self._client = MongoClient("")#вставить хуй
        self._database = self._client["SelfBot"]
        self._invited_users_collection = self._database["InvitedUsers"]
        self._ignored_users_collection = self._database["IgnoredUsers"]
        self._ignored_guilds_collection = self._database["IgnoredGuilds"]

        self.ignored_users = MongoCollection(self._ignored_users_collection)
        self.ignored_guilds = MongoCollection(self._ignored_guilds_collection)
        self.invited_users = MongoCollection(self._invited_users_collection)


class MongoCollection:
    def __init__(self, collection):
        self._collection = collection

    def add(self, _id):
        self._collection.insert_one({"_id" : _id })

    def any(self, _id):
        result = self._collection.find_one({"_id" : _id})
        return result != None

    def any_common(self, *_ids):
        result = self._collection.find()
        for element in result:
            if element["_id"] in _ids:
                return True
        return False

