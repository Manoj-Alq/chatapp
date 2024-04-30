from passlib.context import CryptContext
pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str):
    """to bcrypt password"""
    return pwd_cxt.hash(password)

def verify(plain_password,hashed_password):
    """to hashing password"""   
    return pwd_cxt.verify(plain_password,hashed_password)