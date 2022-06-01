from pymongo import MongoClient
import datetime

DB_CONNECTION_STRING = "mongodb+srv://jesus:cisco@arquitecturadesoftware.ddie5.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(DB_CONNECTION_STRING)

db = client.arquitecturadesoftware
empresa = db.empresa
clientes = db.clientes
empleados = db.empleados

# CREATE OBJECT TO USE IN 'INSERT'
""" 
empresa_1 = {
    "id": 1,
    "nombre": "Big Dick Destroyer"
} 
"""
# DO THE ACTUAL INSERTION IN DB
# empresa.insert_one(empresa_1)

# SEARCH IN TABLE BY SOME ATTRIBUTES IN THE OBJECT OF THE CLASS
print(empresa.find_one({ "id": 1 }))