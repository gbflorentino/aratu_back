from models.users import User
from schemas.users import UserCreate

from sqlalchemy.orm import  Session

def get_user(db: Session, user_id: int):
  return db.query(User).filter(User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
  return db.query(User).filter(User.username == username).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
  return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate):
  new_user: User = User(
    username=user.username,
    hashed_password=user.password,
    name=user.name,
    bio=user.bio
  )
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user

def update_user(db: Session, user_id: int, username: str):
    user: User = get_user(db, user_id=user_id)
    if user:
      if username:
        user.username = username
      db.commit()
    return user

def delete_user(db: Session, user_id: str):
  user: User = get_user(db, user_id=user_id)
  if user:
    db.delete(user)
    db.commit()
  return user