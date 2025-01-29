from fastapi import FastAPI, Response, status, HTTPException
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

def findPost(id:int):
    for p in my_posts:
        if p["id"] == id:
            return p

def indexOfPost(id:int):
    for i in range(len(my_posts)):
        if my_posts[i]["id"] == id:
            return i


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

@app.get("/posts/{id}")
async def get_single_post(id:int, response:Response):
    print(id)
    post = findPost(id)

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"detail": "Post not found"}
    
    return {
        "msg":"Post fetched succesfully",
        "data":post
        }

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id:int):
    index = indexOfPost(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The post with id {id} does not exist!")
        
    my_posts.pop(index)

    return 