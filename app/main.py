from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Sport Pro API")

class Sport(BaseModel):
    id: int
    name: str
    category: str
    is_olympic: bool = False

sports_db = [
    {"id": 1, "name": "Football", "category": "Team", "is_olympic": True},
    {"id": 2, "name": "Cricket", "category": "Team", "is_olympic": False},
]

@app.get("/")
def read_root():
    return {"message": "FastAPI is active!", "docs_url": "/docs"}

@app.get("/sports", response_model=List[Sport])
def list_sports():
    return sports_db

@app.post("/sports", status_code=201)
def create_sport(sport: Sport):
    if any(s['id'] == sport.id for s in sports_db):
        raise HTTPException(status_code=400, detail="Sport ID already exists")
    sports_db.append(sport.dict())
    return sport
