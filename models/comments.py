import datetime

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Float, DateTime
from sqlalchemy.orm import relationship

from config.database import Base

class Comment(Base):
  __tablename__ = "comments"

  id = Column(Integer, primary_key=True, autoincrement=True)
  content = Column(Text, index=True)
  likes = Column(Integer, default=0)
  creation_date = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))
  user_id = Column(Integer, ForeignKey("users.id"))
  post_id = Column(Integer, ForeignKey("posts.id"))
  
  user = relationship("User", back_populates="comments")
  post = relationship("Post", back_populates="comments")