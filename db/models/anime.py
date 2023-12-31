from pydantic import BaseModel
from typing import Optional


class Anime(BaseModel):
    id: Optional[str]
    name: str
    description: str
    episodes: int
    season: str
    genres: str
    image_url: str


class AnimeToCreate(BaseModel):
    name: str
    description: str
    episodes: int
    season: str
    genres: str
    image_url: str


class TotalAnimesPages(BaseModel):
    total_animes: int
    total_pages: int
