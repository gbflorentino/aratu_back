import datetime

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Float, DateTime
from sqlalchemy.orm import relationship

from config.database import Base

class User(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True, autoincrement=True)  
  username = Column(String, unique=True, index=True)
  name = Column(String, index=True)
  hashed_password = Column(String)
  is_verified = Column(Boolean, default=False)
  #profile_picture = Column(Integer)
  bio = Column(Text)
  creation_date = Column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))
  
  posts = relationship("Post", back_populates="user")
  comments = relationship("Comment", back_populates="user")
  

  