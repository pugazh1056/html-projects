# main.py

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import models, schemas
from database import engine, get_db

# Create all tables in database
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI
app = FastAPI(title="AI News Assistant Backend")

# Enable CORS so frontend can access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or your frontend URL
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root route
@app.get("/")
def root():
    return {"message": "Backend is running!"}

# POST route to add news
@app.post("/news/", response_model=schemas.NewsItemResponse)
def create_news(news: schemas.NewsItemCreate, db: Session = Depends(get_db)):
    db_news = models.NewsItem(title=news.title, content=news.content)
    db.add(db_news)
    db.commit()
    db.refresh(db_news)
    return db_news

# GET route to fetch all news
@app.get("/news/", response_model=list[schemas.NewsItemResponse])
def get_news(db: Session = Depends(get_db)):
    news_list = db.query(models.NewsItem).all()
    return news_list
