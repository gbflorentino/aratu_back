import schemas
import services

from typing import Annotated

from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from dependencies import get_db
from services.auth import get_password_hash, generate_token, get_current_user
from schemas.token import Token
from config.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/users/", response_model=schemas.users.User, tags=["user"])
async def create_user(user: schemas.users.UserCreate, db: Session = Depends(get_db)):
  db_user = services.users.get_user_by_username(db, username=user.username)
  if db_user:
    raise HTTPException(status_code=400, detail="O usuário já está registrado")
  user.password = get_password_hash(password=user.password)
  print(user.password)
  return services.users.create_user(db=db, user=user)

@app.get("/users/{user_id}", response_model=schemas.users.User, tags=["user"])
async def read_user(user_id: int, db: Session = Depends(get_db)):
  db_user = services.get_user(db, user_id=user_id)
  if db_user is None:
    raise HTTPException(status_code=404, detail="Usuario não encontrado")
  
@app.get("/users/", response_model=list[schemas.users.User], tags=["user"])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
  users = services.get_users(db, skip=skip, limit=limit)
  print(users)
  return users

@app.post("/posts/", response_model=schemas.posts.Post, tags=["posts"])
async def create_post_for_user(
  post: schemas.posts.PostCreate,
  current_user: schemas.users.User = Depends(get_current_user),
  db: Session = Depends(get_db)  
):
  return services.posts.create_post(db=db, post=post)

@app.get("/posts/", response_model=list[schemas.posts.Post], tags=["posts"])
async def read_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
  posts = services.posts.get_posts(db, skip=skip)
  return posts

@app.post("/posts/{post_id}/comments", response_model=schemas.comments.Comment, tags=["comments"])
async def creatte_comment_for_post(
  post_id: int,
  comment: schemas.comments.CommentCreate,
  current_user: schemas.users.User = Depends(get_current_user),
  db: Session = Depends(get_db)  
):
  comment.post_id = post_id
  return services.comments.create_comment(db=db, comment=comment)

@app.get("/posts/{post_id}/comments", response_model=list[schemas.comments.Comment], tags=["comments"])
async def read_comments(post_id: int, db: Session = Depends(get_db)):
  comments = services.comments.get_comments_post(db, post_id=post_id)
  return comments

@app.post("/token", tags=["jwt token"])
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db)
) -> Token:
    access_token, user_id = generate_token(
      db=db,
      username=form_data.username,
      password=form_data.password
    )
    return Token(user_id=user_id, access_token=access_token, token_type="bearer")
