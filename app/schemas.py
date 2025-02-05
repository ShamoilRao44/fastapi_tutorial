import email
from pydantic import BaseModel, EmailStr
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

class CreateUser(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    u_id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode=True