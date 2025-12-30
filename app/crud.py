from sqlalchemy.orm import Session
from . import models, schemas

def get_sport(db: Session, sport_id: int):
    return db.query(models.SportItem).filter(models.SportItem.id == sport_id).first()

def get_all_sports(db: Session):
    return db.query(models.SportItem).all()

def create_sport(db: Session, sport: schemas.SportCreate):
    new_sport = models.SportItem(
        name=sport.name, 
        players_count=sport.players_count, 
        description=sport.description
    )
    db.add(new_sport)
    db.commit()
    db.refresh(new_sport)
    return new_sport
