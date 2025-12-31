from sqlalchemy.orm import Session
from . import models, schemas

def get_teams(db: Session):
    return db.query(models.Team).all()

def create_team(db: Session, team: schemas.TeamCreate):
    db_team = models.Team(name=team.name, city=team.city)
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team

def get_players(db: Session):
    return db.query(models.Player).all()

def create_player(db: Session, player: schemas.PlayerCreate):
    db_player = models.Player(
        full_name=player.full_name,
        position=player.position,
        salary=player.salary,
        team_id=player.team_id
    )
    db.add(db_player)
    db.commit()
    db.refresh(db_player)
    return db_player
