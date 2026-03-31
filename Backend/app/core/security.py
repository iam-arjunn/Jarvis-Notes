from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
import hashlib

SECRET_KEY = "Ares2009@007"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



def preprocess(password: str):
    return hashlib.sha256(password.encode()).hexdigest()

def hash_password(password: str):
    processed = preprocess(password)[:72]
    return pwd_context.hash(processed)

def verify_password(plain, hashed):
    processed = preprocess(plain)[:72]
    return pwd_context.verify(processed, hashed)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(hours=2)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)