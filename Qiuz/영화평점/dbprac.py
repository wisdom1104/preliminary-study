from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.xqvw0op.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta


doc = {
    'name':'babo',
    'age':27
}

db.users.insert_one(doc)