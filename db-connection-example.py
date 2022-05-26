from pymongo import MongoClient

DB_CONNECTION_STRING = "mongodb+srv://jesus:cisco@arquitecturadesoftware.ddie5.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(DB_CONNECTION_STRING)

db = client.arquitecturadesoftware
empresa_equipo1 = db.empresa_equipo1
clientes_equipo1 = db.clientes_equipo1
empleados_equipo1 = db.empleados_equipo1

# CREATE OBJECT TO USE IN 'INSERT'
""" 
nueva_empresa = {
    "id": 1,
    "nombre": "Big Dick Destroyer"
} 
"""
# DO THE ACTUAL INSERTION IN DB
# empresa_equipo1.insert_one(nueva_empresa)

# SEARCH IN TABLE BY SOME ATTRIBUTES IN THE OBJECT OF THE CLASS
print(empresa_equipo1.find_one({ "nombre": "Big Dick Destroyer" }))