# db/client.py
from pymongo import MongoClient

# Cambia la URI según corresponda: 'mongodb://localhost:27017' o la URI de MongoDB Atlas
MONGO_URI = "mongodb://localhost:27017"
client = MongoClient(MONGO_URI)

# Nombre de la base de datos
db = client["to_do_database"]


if __name__ == "__main__":
    # Esto intentará obtener la lista de bases de datos para verificar la conexión
    print("Bases de datos disponibles:", client.list_database_names())
