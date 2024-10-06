from datetime import datetime
from pydantic import BaseModel, Field

from schemas.posts import Post

class UserBase(BaseModel):
  username: str = Field(min_length=5, max_length=20)
  name: str = Field(min_length=5, max_length=20)
  bio: str = Field(min_length=10, max_lenght=256)

class UserCreate(UserBase):
  password: str = Field(min_length=5, max_length=30)  

class User(UserBase):
  id: int
  is_verified: bool = Field(default=False)
  creation_date: datetime
  posts: list[Post] = []

  class Config:
    orm_mode = True


