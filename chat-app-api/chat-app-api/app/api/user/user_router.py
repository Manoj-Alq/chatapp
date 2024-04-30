from .user_controller import *
from .user_schema import Registeruser

router = APIRouter()

@router.post("/create",)
def create_user_router(user:Registeruser,db:session=Depends(get_db)):
    return user_create_controller(db,user)

@router.get("/get_users",)
def get_users_router(db:session=Depends(get_db)):
    return get_users_controller(db)

@router.get("/get_user/{id}",)
def get_users_router(id:int,db:session=Depends(get_db)):
    return get_user_controller(id,db)