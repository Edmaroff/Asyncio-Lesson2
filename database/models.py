from sqlalchemy import ARRAY, Column, Integer, String
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase


class Base(AsyncAttrs, DeclarativeBase):
    pass


class People(Base):
    __tablename__ = "swapi_people"

    people_id = Column(Integer, primary_key=True, autoincrement=False)
    birth_year = Column(String)
    eye_color = Column(String)
    gender = Column(String)
    hair_color = Column(String)
    height = Column(String)
    homeworld = Column(String)
    mass = Column(String)
    name = Column(String)
    skin_color = Column(String)
    films = Column(ARRAY(String))
    species = Column(ARRAY(String))
    starships = Column(ARRAY(String))
    vehicles = Column(ARRAY(String))
