from fastapi import Depends, status, HTTPException,APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas
from typing import List
from ..database import get_db

router = APIRouter(prefix="/posts", tags=['Posts'])

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schemas.fetchPostResponse])
async def get_posts(db: Session=Depends(get_db)):
   
    posts = db.query(models.Post).all()

    return posts

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.fetchPostResponse)
async def create_post(post: schemas.CreateUpdatePost, db:Session=Depends(get_db)):
    
    new_post = models.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post

@router.get("/{id}", response_model=schemas.fetchPostResponse)
async def get_single_post(id:int,db:Session=Depends(get_db)):
    
    post = db.query(models.Post).filter(models.Post.id == id).first()
    
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Post not found"
            )
        
    
    return post

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
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

@router.put("/{id}", response_model=schemas.fetchPostResponse)
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