from sqlalchemy import Column, Integer, String, Decimal, ForeignKey, Date
from sqlalchemy.orm import relationship
from .database import Base

class Team(Base):
    __tablename__ = "teams"

    team_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    city = Column(String(100))

    players = relationship("Player", back_populates="team", cascade="all, delete")
    home_matches = relationship("Match", foreign_keys="Match.home_team_id", back_populates="home_team")
    away_matches = relationship("Match", foreign_keys="Match.away_team_id", back_populates="away_team")

class Player(Base):
    __tablename__ = "players"

    player_id = Column(Integer, primary_key=True, index=True)
    team_id = Column(Integer, ForeignKey("teams.team_id", ondelete="CASCADE"))
    full_name = Column(String(100), nullable=False)
    position = Column(String(50))
    salary = Column(Numeric(12, 2))

    team = relationship("Team", back_populates="players")
    goals = relationship("Goal", back_populates="player", cascade="all, delete")

class Match(Base):
    __tablename__ = "matches"

    match_id = Column(Integer, primary_key=True, index=True)
    home_team_id = Column(Integer, ForeignKey("teams.team_id", ondelete="CASCADE"))
    away_team_id = Column(Integer, ForeignKey("teams.team_id", ondelete="CASCADE"))
    match_date = Column(Date)
    stadium = Column(String(100))

    home_team = relationship("Team", foreign_keys=[home_team_id], back_populates="home_matches")
    away_team = relationship("Team", foreign_keys=[away_team_id], back_populates="away_matches")
    goals = relationship("Goal", back_populates="match", cascade="all, delete")

class Goal(Base):
    __tablename__ = "goals"

    goal_id = Column(Integer, primary_key=True, index=True)
    match_id = Column(Integer, ForeignKey("matches.match_id", ondelete="CASCADE"))
    player_id = Column(Integer, ForeignKey("players.player_id", ondelete="CASCADE"))
    goal_minute = Column(Integer)

    match = relationship("Match", back_populates="goals")
    player = relationship("Player", back_populates="goals")
