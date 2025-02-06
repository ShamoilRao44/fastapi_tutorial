from fastapi import Depends, status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, utils
from typing import List
from ..database import get_db

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
def createUser(user:schemas.CreateUser, db:Session=Depends(get_db)):

    user.password =utils.appHash(user.password)

    newUser = models.User(**user.model_dump())
    db.add(newUser)
    db.commit()
    db.refresh(newUser)

    return newUser

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.UserResponse])
def fetchAllUsers(db: Session=Depends(get_db)):

    users=db.query(models.User).all()

    return users

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.UserResponse)
def fetchSingleUser(id: int, db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.u_id == id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User does not Exist'
        )
    
    return user
