from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
from . import models
from .database import engine

models.Base.metadata.create_all(bind = engine)

app = FastAPI()

try:
    conn = psycopg2.connect(host='localhost', database ='fastapi_tutorial', 
                            user = 'Shamoil', password = 'Shampg2344!', cursor_factory=RealDictCursor,)
    cursor = conn.cursor()
except Exception as error:
    print(error)



class Post(BaseModel):
    title: str
    content: str
    published: bool = True


@app.get("/")
async def root():
    return {"message": "This is a social media application"}

@app.get("/posts")
async def get_posts():
    cursor.execute("""Select * from posts order by post_id;""")
    posts = cursor.fetchall()

    return {"data": posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_post(post: Post):
    cursor.execute("""INSERT INTO posts(title, content, published) VALUES (%s,%s,%s) RETURNING *""",
                   (post.title,post.content, post.published))
    post=cursor.fetchone()
    conn.commit()
    return {
        "msg":"post created successfully.", 
        "data": post #return post_dict
        }

@app.get("/posts/{id}")
async def get_single_post(id:int,):
    cursor.execute("""Select * from posts where post_id = %s""", (str(id)),)
    post = cursor.fetchone()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Post not found"
            )
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"detail": "Post not found"}
    
    return {
        "msg":"Post fetched succesfully",
        "data":post
        }

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id:int):

    cursor.execute("""DELETE FROM posts where post_id = %s returning *""", (str(id)))
    post = cursor.fetchone()
    print(post)
    conn.commit()

    if post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"The post with id {id} does not exist!"
            )
        

    return 

@app.put("/posts/{id}")
async def update_post(id:int, post:Post):

    cursor.execute("""Update posts set title = %s, content = %s, published=%s where post_id = %s returning *""",
                   (post.title, post.content,post.published,str(id),),
                   )
    upd_post = cursor.fetchone()

    conn.commit()

    if upd_post == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"The post with id {id} does not exist!"
            )
    
   

    return {
        "msg":"Post updated successfully",
        "data":upd_post
    }