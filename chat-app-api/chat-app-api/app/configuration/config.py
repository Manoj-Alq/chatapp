from fastapi import FastAPI,APIRouter, Depends
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy import create_engine, Column, Integer, String, Boolean,TIMESTAMP,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, defer
from sqlalchemy.orm import session


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:12345@localhost/chatapp"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
conn=engine.raw_connection()  
cur=conn.cursor()
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#swwagger setup
app = FastAPI(
    title="Chat App API",)
app.mount("/api/v1/",app)

#middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)