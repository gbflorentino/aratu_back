import datetime

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Float, DateTime
from sqlalchemy.orm import relationship

from config.database import Base

class Post(Base):
  __tablename__ = "posts"

  id = Column(Integer, primary_key=True, autoincrement=True)
  content = Column(Text, index=True)
  likes = Column(Integer, default=0)
  localization = Column(String, index=True)
  creation_date = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))
  alert_type = Column(Integer)
  user_id = Column(Integer, ForeignKey("users.id"))
  
  user = relationship("User", back_populates="posts")
  comments = relationship("Comment", back_populates="post")