from distutils.log import debug
from imp import reload
from fastapi import FastAPI
import uvicorn

from database import engine, Base
from api import users
import authentication

Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(authentication.router)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, debug=True)