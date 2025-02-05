from fastapi import Depends, FastAPI, status, HTTPException
from typing import List
from sqlalchemy.orm import Session
from . import models, schemas
from .database import engine, get_db

models.Base.metadata.create_all(bind = engine)

app = FastAPI()




@app.get("/")
async def root():
    return {"message": "This is a social media application"}

@app.get("/posts", response_model=List[schemas.fetchPostResponse])
async def get_posts(db: Session=Depends(get_db)):
    # cursor.execute("""Select * from posts order by post_id;""")
    # posts = cursor.fetchall()

    posts = db.query(models.Post).all()

    return posts

@app.post("/posts", status_code=status.HTTP_201_CREATED, response_model=schemas.fetchPostResponse)
async def create_post(post: schemas.CreateUpdatePost, db:Session=Depends(get_db)):
    # cursor.execute("""INSERT INTO posts(title, content, published) VALUES (%s,%s,%s) RETURNING *""",
    #                (post.title,post.content, post.published))
    # post=cursor.fetchone()
    # conn.commit()
    new_post = models.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@app.get("/posts/{id}", response_model=schemas.fetchPostResponse)
async def get_single_post(id:int,db:Session=Depends(get_db)):
    # cursor.execute("""Select * from posts where post_id = %s""", (str(id)),)
    # post = cursor.fetchone()

    post = db.query(models.Post).filter(models.Post.id == id).first()
    
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Post not found"
            )
        
    
    return post

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id:int, db:Session=Depends(get_db)):

    # cursor.execute("""DELETE FROM posts where post_id = %s returning *""", (str(id)))
    # post = cursor.fetchone()
    # conn.commit()

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

    # cursor.execute("""Update posts set title = %s, content = %s, published=%s where post_id = %s returning *""",
    #                (post.title, post.content,post.published,str(id),),
    #                )
    # upd_post = cursor.fetchone()

    # conn.commit()

    postQuery = db.query(models.Post).filter(models.Post.id == id)

    if postQuery.first() == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"The post with id {id} does not exist!"
            )
    
    postQuery.update(post.model_dump())
    db.commit()
    return postQuery.first()