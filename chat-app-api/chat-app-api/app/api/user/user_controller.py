from .user_service import *

def user_create_controller(db,user):
    return create_user(db,user)

def get_users_controller(db):
    return get_users_service(db)

def get_user_controller(id,db):
    try:
        user = get_user_service(id,db)

        if user is None:
            return error_handler(404,"user not found")
        
        return user
    except Exception as e:
        return e
    