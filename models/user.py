from database.connection import get_users_collection
from bson import ObjectId

def create_user(email, password, name):
    """Create a new user"""
    users_collection = get_users_collection()
    user = {
        "email": email,
        "password": password,
        "name": name
    }
    result = users_collection.insert_one(user)
    return result.inserted_id

def get_user_by_email(email):
    """Get user by email"""
    users_collection = get_users_collection()
    return users_collection.find_one({"email": email})

def get_user_by_id(user_id):
    """Get user by ID"""
    users_collection = get_users_collection()
    try:
        return users_collection.find_one({"_id": ObjectId(user_id)})
    except:
        return None

def update_user(user_id, data):
    """Update user data"""
    users_collection = get_users_collection()
    try:
        users_collection.update_one(
            {"_id": ObjectId(user_id)},
            {"$set": data}
        )
    except:
        pass
