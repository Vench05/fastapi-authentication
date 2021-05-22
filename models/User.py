from sqlalchemy import Column, String, Integer
from database import Base


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    password = Column(String)