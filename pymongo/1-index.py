from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client.pymongo
userCollection = db.users
print(client.server_info())

user = {"nome": "Marco", "cognome": "Verdi"}
result = userCollection.insert_one(user)
print(result.inserted_id)

#oppure si può fare così
#user = userCollection.insert_one({"_id": "1", "nome": "Marco", "cognome": "Verdi"})
#print(user.inserted_id)

users = [
    {"nome": "Marco", "cognome": "Verdi", "eta": 23},
    {"nome": "Anna", "cognome": "Marco", "eta": 18},
    {"nome": "Giovanni", "cognome": "Rossi", "eta": 30, "squadra": "Inter"},
    {"nome": "Turi", "cognome": "Zazzamita", "eta": 17}, 
    {"nome": "Alessio", "cognome": "Stigliano", "eta": 17}
]

result = userCollection.insert_many(users)
print(result.inserted_ids)

