from pydantic import BaseModel, Field

class CommentBase(BaseModel):
  content: str = Field(min_length=10, max_length=500)

class CommentCreate(CommentBase):
  post_id: int
  user_id: int | None  = None

class Comment(CommentBase):
  id: int
  user_id: int
  post_id: int
  
  class Config:
    orm_mode = True
