from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

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

@app.put("/sports/{sport_id}")
def update_sport(sport_id: int, updated_sport: Sport):
    for index, sport in enumerate(sports_db):
        if sport["id"] == sport_id:
            sports_db[index] = updated_sport.dict()
            return {"message": "Sport updated successfully"}
    raise HTTPException(status_code=404, detail="Sport not found")

@app.delete("/sports/{sport_id}")
def delete_sport(sport_id: int):
    for index, sport in enumerate(sports_db):
        if sport["id"] == sport_id:
            sports_db.pop(index)
            return {"message": "Sport deleted successfully"}
    raise HTTPException(status_code=404, detail="Sport not found")
