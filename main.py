from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange


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
    post_dict = post.model_dump() #Convert model into dictionary.
    post_dict['id'] = randrange(3,1000000) #Add a key named id and assign it a random integer between 3 and 1 million.
    my_posts.append(post_dict) #add post_dict to my_posts List
    return {
        "msg":"post created successfully.", 
        "data": post_dict #return post_dict
        }
