from configuration.config import *
from .user_model import *
from utils.security import hash_password
from utils.handlers import response_handler, error_handler

def create_user(db,user):
    user.password = hash_password(user.password)
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return response_handler(201,"user created successfully",True)

def get_users_service(db):
    return db.query(User).options(defer(User.password)).all()

def get_user_service(id,db):
    return db.query(User).options(defer(User.password)).filter(User.id == id).first()