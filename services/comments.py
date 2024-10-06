import models
import schemas

from sqlalchemy.orm import Session

def get_comment(db: Session, comment_id: int):
  return db.query(models.comments.Comment).filter(models.comments.Comment.id == comment_id)

def get_comments_post(db: Session, post_id: int, limit=10):
  return db.query(models.comments.Comment).filter(models.comments.Comment.post_id == post_id).limit(limit)

def create_comment(db: Session, comment: schemas.CommentCreate):
  new_comment: models.comments.Comment = models.comments.Comment(
    content=comment.content,
    user_id=comment.user_id,
    post_id=comment.post_id
  )
  db.add(new_comment)
  db.commit()
  db.refresh(new_comment)
  return new_comment

def delete_comment(db: Session, comment_id: int):
  post = get_comment(db, comment_id=comment_id)
  if post:
    db.delete(post)
    db.commit()
  return post

