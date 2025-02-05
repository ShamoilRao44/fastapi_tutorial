from fastapi import Depends, FastAPI, status, HTTPException
from typing import List
from sqlalchemy.orm import Session
from . import models, schemas, utils
from .database import engine, get_db

models.Base.metadata.create_all(bind = engine)

app = FastAPI()




@app.get("/")
async def root():
    return {"message": "This is a social media application"}

@app.get("/posts", status_code=status.HTTP_200_OK, response_model=List[schemas.fetchPostResponse])
async def get_posts(db: Session=Depends(get_db)):
   
    posts = db.query(models.Post).all()

    return posts

@app.post("/posts", status_code=status.HTTP_201_CREATED, response_model=schemas.fetchPostResponse)
async def create_post(post: schemas.CreateUpdatePost, db:Session=Depends(get_db)):
    
    new_post = models.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post

@app.get("/posts/{id}", response_model=schemas.fetchPostResponse)
async def get_single_post(id:int,db:Session=Depends(get_db)):
    
    post = db.query(models.Post).filter(models.Post.id == id).first()
    
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Post not found"
            )
        
    
    return post

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id:int, db:Session=Depends(get_db)):

    postQuery = db.query(models.Post).filter(models.Post.id == id)

    if postQuery.first() == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"The post with id {id} does not exist!"
            )
    
    postQuery.delete(synchronize_session=False)
    db.commit()
        

    return 

@app.put("/posts/{id}", response_model=schemas.fetchPostResponse)
async def update_post(id:int, post:schemas.CreateUpdatePost, db:Session = Depends(get_db)):

    postQuery = db.query(models.Post).filter(models.Post.id == id)

    if postQuery.first() == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"The post with id {id} does not exist!"
            )
    
    postQuery.update(post.model_dump())
    db.commit()

    return postQuery.first()

@app.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.UserResponse)
def createUser(user:schemas.CreateUser, db:Session=Depends(get_db)):

    user.password =utils.appHash(user.password)

    newUser = models.User(**user.model_dump())
    db.add(newUser)
    db.commit()
    db.refresh(newUser)

    return newUser

@app.get("/users", status_code=status.HTTP_200_OK, response_model=List[schemas.UserResponse])
def fetchAllUsers(db: Session=Depends(get_db)):

    users=db.query(models.User).all()

    return users

@app.get("/users/{id}", status_code=status.HTTP_200_OK, response_model=schemas.UserResponse)
def fetchSingleUser(id: int, db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.u_id == id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User does not Exist'
        )
    
    return user
    
