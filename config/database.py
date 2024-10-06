from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres.exuurgyrxqtroniyuirl:[YOUR-PASSWORD]@aws-0-us-west-1.pooler.supabase.com:5432/postgres"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres.vnwasszoxxvhuyuzhacj:724$gabTske(:)@aws-0-us-west-1.pooler.supabase.com:6543/postgres"

engine = create_engine(
  SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

