from datetime import datetime
from pydantic import BaseModel, Field

class PostBase(BaseModel):
  content: str = Field(min_length=10, max_length=500)
  localization: str = Field(min_length=10, max_legth=30)
  alert_type: int

class PostCreate(PostBase):
  user_id: int | None = None

class Post(PostBase):
  id: int

  class Config:
    orm_mode = True
  

