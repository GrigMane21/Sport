from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class TeamBase(BaseModel):
    name: str
    city: Optional[str] = None

class TeamCreate(TeamBase):
    pass

class TeamResponse(TeamBase):
    team_id: int
    class Config:
        from_attributes = True

class PlayerBase(BaseModel):
    full_name: str
    position: Optional[str] = None
    salary: float
    team_id: int

class PlayerCreate(PlayerBase):
    pass

class PlayerResponse(PlayerBase):
    player_id: int
    class Config:
        from_attributes = True
