from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database import get_db
from models.User import Users
from hashing import Hash
from schemas import tokens
import Token

router = APIRouter(
    tags=['Authentication'],
)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


@router.post('/login', response_model=tokens.Token)
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(Users).filter(Users.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid Username or Password')
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid Username or Password')
    data = {
        'id': user.id,
        'username': user.email,
    }
    access_token = Token.create_access_token(data)
    return {
        'access_token': access_token,
        'token_type': 'bearer'
    }

# async def get_current_user(data: str = Depends(oauth2_scheme)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     return 

async def get_current_user(token: str = Depends(oauth2_scheme)):
    print(token)
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return Token.verify_token(token, credentials_exception)
    # user = db.query(Users).get(token_data['id'])
    # if user is None:
    #     raise credentials_exception
    # return user