from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb://localhost:27017")
db = client.pymongo
userCollection = db.users
print(client.server_info())

print()

result = userCollection.find_one() #trova il primo
print(result)

print()

result = userCollection.find()
for user in result:
    print(user)

print()

result = userCollection.find({}, {"_id": 0, "nome": 1}) #stiamo dicendo che non vogliamo l'id(se non lo specifichiamo lo manda sempre) e che vogliamo il nome
for user in result:
    print(user)

print()

result = userCollection.find({}, {"nome": 0}) #manda tutto tranne il nome
for user in result:
    print(user)

print()

result = userCollection.find({"_id": ObjectId("6511461376c62d18db7e07bb")})
for user in result:
    print(user)

print()

query = {"eta": {"$gt": 25}}
result = userCollection.find(query)
for user in result:
    print(user)

print()

query = {"cognome": {"$regex": "^R"}}
result = userCollection.find(query)
for user in result:
    print(user)

print()

result = userCollection.find().sort("eta", 1) #1 = crescente
for user in result:
    print(user)

print()

result = userCollection.find().sort("eta", -1) #-1 = decrescente
for user in result:
    print(user)

print()

result = userCollection.find().sort("eta", -1).limit(3) #-1 = decrescente
for user in result:
    print(user)