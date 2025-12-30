from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        print("Database connection error")
    
    db.close()

@app.get("/sports/", response_model=list[schemas.SportResponse])
def read_sports(db: Session = Depends(get_db)):
    return crud.get_all_sports(db)

@app.post("/sports/", response_model=schemas.SportResponse)
def add_sport(sport: schemas.SportCreate, db: Session = Depends(get_db)):
    return crud.create_sport(db=db, sport=sport)

    
