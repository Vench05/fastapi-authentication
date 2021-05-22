from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from schemas.users import User, UserShow
from database import get_db
from models.User import Users
from hashing import Hash
from authentication import get_current_user

router = APIRouter(
    tags=['USER'],
    prefix='/users'
)


@router.post('/', response_model=UserShow)
def create(request: User, db: Session = Depends(get_db)):
    request.password = Hash.bcrypt(request.password)
    new_user = Users(**request.dict())
    print(new_user)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get('/', response_model=List[UserShow])
def get_users(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    users = db.query(Users).all()
    return users


@router.get("/{id}", response_model=UserShow)
def get_user(id:int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    user = db.query(Users).get(id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User id:{id} not found')
    return user
