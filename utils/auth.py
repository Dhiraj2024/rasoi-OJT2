import bcrypt

def hash_password(password):
    """Hash a password using bcrypt"""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

def verify_password(password, hashed_password):
    """Verify password against hashed password"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

def serialize_user(user):
    """Convert user document to serializable format"""
    if user:
        user["_id"] = str(user["_id"])
        user.pop("password", None)
    return user