from xmlrpc.client import Boolean
from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def bcrypt(password: str) -> str:
        return pwd_cxt.hash(password)

    def verify(password:str, hashed_password:str) -> Boolean:
        return pwd_cxt.verify(password,hashed_password)

# class 