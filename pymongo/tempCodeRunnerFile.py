from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb://localhost:27017")
db = client.pymongo
userCollection = db.users
print(client.server_info())

print()