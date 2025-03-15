import pymongo

connection_string = "mongodb+srv://localhost:8487"

def create_db(connection_string, db_name):
    client = pymongo.MongoClient(connection_string)
    db = client[db_name]
    return db

def create_collection(db, collection_name):
    collection = db[collection_name]
    return collection


if __name__ == "__main__":
    db = create_db(connection_string, "test_db")
    collection = create_collection(db, "test_collection")
    print("Database and collection created successfully")