import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "rasoi_guru_db")

_client = None
_db = None
_connection_error = None

def get_client():
    """Get MongoDB client with lazy connection"""
    global _client, _connection_error
    if _client is None and _connection_error is None:
        try:
            _client = MongoClient(
                MONGO_URI, 
                serverSelectionTimeoutMS=3000,
                connectTimeoutMS=3000,
                retryWrites=False
            )
            _client.admin.command("ping")
        except Exception as e:
            _connection_error = str(e)
            _client = None
    return _client

def get_db():
    """Get database with lazy connection"""
    global _db
    if _db is None:
        client = get_client()
        if client is not None:
            _db = client[DB_NAME]
    return _db

class PlaceholderCollection:
    """Placeholder for when MongoDB is not available"""
    def __init__(self, name):
        self.name = name
    
    def find(self, *args, **kwargs):
        return []
    
    def find_one(self, *args, **kwargs):
        return None
    
    def insert_one(self, *args, **kwargs):
        class Result:
            inserted_id = None
        return Result()
    
    def update_one(self, *args, **kwargs):
        pass
    
    def delete_one(self, *args, **kwargs):
        pass
    
    def create_index(self, *args, **kwargs):
        pass

def get_users_collection():
    db = get_db()
    if db is not None:
        try:
            col = db["users"]
            col.create_index("email", unique=True)
            return col
        except:
            pass
    return PlaceholderCollection("users")

def get_recipes_collection():
    db = get_db()
    if db is not None:
        try:
            col = db["recipes"]
            col.create_index("name")
            col.create_index("category")
            return col
        except:
            pass
    return PlaceholderCollection("recipes")

def get_meal_plans_collection():
    db = get_db()
    if db is not None:
        try:
            return db["meal_plans"]
        except:
            pass
    return PlaceholderCollection("meal_plans")

def get_favorites_collection():
    db = get_db()
    if db is not None:
        try:
            return db["favorites"]
        except:
            pass
    return PlaceholderCollection("favorites")
