from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb://localhost:27017")
db = client.pymongo
userCollection = db.users
print(client.server_info())

print()

query = {"_id": ObjectId('651180522432faf158727b31')}
result = userCollection.delete_one(query)
print(result.deleted_count)

query = {"eta": {"$gt": 25}}
result = userCollection.delete_many(query)
print()
print(result.deleted_count)

'''
Per cancellare tutti i documenti andare su MongoCompass e lanciare ad uno ad uno i seguenti comandi:
use pymongo
db.users
db.users.deleteMany({})
'''