from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

my_posts = [
    {"title":"post 1", "content":"Content of post 1", "id": 1},
    {"title":"post 2", "content":"Content of post 2", "id": 2},
    ]

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[float] = None

@app.get("/")
async def root():
    return {"message": "This is a social media application"}

@app.get("/posts")
async def get_posts():
    return {"data": my_posts}

@app.post("/posts")
async def create_post(post: Post):
    return {
        "msg":"post created successfully.", 
        "data": post
        }
