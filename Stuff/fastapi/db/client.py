from pymongo import MongoClient

# db_client = MongoClient().local

db_client = MongoClient(
    "mongodb+srv://test:test@cluster0.nntxmos.mongodb.net/?retryWrites=true&w=majority").test
