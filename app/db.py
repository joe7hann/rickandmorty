from pymongo import MongoClient

client = MongoClient('localhost', 27017)
#client = MongoClient('localhost', 27017, username='root', password='root')

#vamos a conectarnos a una db
db = client["ricky_and_morty"]