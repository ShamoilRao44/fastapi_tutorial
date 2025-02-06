from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import database, models, schemas, utils, oauth2

router = APIRouter(prefix='/auth', tags=['Authentication'])

@router.post('/', status_code=status.HTTP_200_OK)
async def login(user_cred: schemas.LoginUser, db:Session=Depends(database.get_db)):

    user = db.query(models.User).filter(models.User.email == user_cred.email).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid Credentials')
    
    if not utils.verifyPassword(user_cred.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid Credentials')
    
    access_token = oauth2.create_jwt_token({"u_id":user.u_id})
    
    return {
        "token":access_token,
        "token_type":"bearer"
    }