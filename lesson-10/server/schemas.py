from pydantic import BaseModel
from typing import List, Optional

class PostBase(BaseModel):
    title: str
    body: str
    user_id: int

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int

    class Config:
        orm_mode = True

class CommentBase(BaseModel):
    name: str
    email: str
    body: str
    post_id: int

class CommentCreate(CommentBase):
    pass

class Comment(CommentBase):
    id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
    website: Optional[str] = None

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
