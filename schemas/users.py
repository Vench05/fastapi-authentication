from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    first_name: Optional[str] 
    last_name: Optional[str] 
    email:str
    password:str


class UserShow(BaseModel):
    id:int
    first_name:str
    last_name:str
    email:str
    class Config():
        orm_mode = True