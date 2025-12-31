from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    yield db
    db.close()

@app.get("/teams/", response_model=List[schemas.TeamResponse])
def read_teams(db: Session = Depends(get_db)):
    return crud.get_teams(db)

@app.post("/teams/", response_model=schemas.TeamResponse)
def create_team(team: schemas.TeamCreate, db: Session = Depends(get_db)):
    return crud.create_team(db=db, team=team)
    
