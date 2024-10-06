import models
import schemas

from sqlalchemy.orm import  Session

def get_posts(db: Session, skip: int = 0, limit: int = 100):
  return db.query(models.posts.Post).offset(skip).limit(limit).all()

def get_post(db: Session, post_id: int):
  return db.query(models.posts.Post).filter(models.posts.Post.id == post_id)
  
def get_user_post(db: Session, user_id: str, limit=10):
  return db.query(models.posts.Post).filter(models.posts.Post.user_id == user_id).limit()

def create_post(db: Session, post: schemas.PostCreate):
  new_post: models.posts.Post = models.posts.Post(
    content=post.content,
    localization=post.localization,
    alert_type=post.alert_type,
    user_id=post.user_id
  )
  db.add(new_post)
  db.commit()
  db.refresh(new_post)
  return new_post

def delete_post(db: Session, post_id: int):
  post = get_post(db, post_id=post_id)
  if post:
    db.delete(post)
    db.commit()
  return post

