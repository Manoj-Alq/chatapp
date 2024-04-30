from pydantic import BaseModel

class Registeruser(BaseModel):
    nickname:str
    username:str
    email:str
    password:str