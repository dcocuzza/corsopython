from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb://localhost:27017")
db = client.pymongo
userCollection = db.users
print(client.server_info())

print()

query = {"nome": "Marco"}
value = {"$set": {"nome": "Reginaldo"}}
result = userCollection.update_one(query, value) #il primo valore è il filtro mentre il secondo nome è ciò che vogliamo settare
print(result.upserted_id) #da none perché ritorna l'id quando il documento che vogliamo modificare non esite e lo crea

print()

query = {"_id": ObjectId('651140d710bd7a944ee05ee8')}
value = {"$set": {"nome": "Saro", "eta": 20}}
result = userCollection.update_one(query, value)
print(result.upserted_id)

print()

query = {"eta": {"$gt": 25}}
value = {"$set": {"nome": "Leonardo"}}
result = userCollection.update_many(query, value)
print(result.upserted_id)
