from pydantic import BaseModel
from datetime import datetime

class postBase(BaseModel):
    title: str
    content: str
    published: bool = True

class CreateUpdatePost(postBase):
    pass

class fetchPostResponse(postBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode=True