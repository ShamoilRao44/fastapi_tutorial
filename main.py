from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "My name is Shamoil Rao."}

@app.get("/posts")
async def get_posts():
    return {"data":"These are all the posts."}

@app.post("/createposts")
async def create_post(payload: dict = Body(...)):
    return {
        "msg":"post created successfully.", 
        "data": {
            "title": payload["title"], 
            "content": payload["content"]
            }
        }
