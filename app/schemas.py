from pydantic import BaseModel

class SportCreate(BaseModel):
    name: str
    players_count: int
    description: str

class SportResponse(SportCreate):
    id: int

    class Config:
        from_attributes = True
