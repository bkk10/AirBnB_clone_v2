#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Table
from sqlalchemy import MetaData

class Amenity(BaseModel, Base):
    """ Amenity class to store amenity information """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)

    place_amenity = Table("place_amenity",
                          Base.metadata,
                          Column("place_id", String(60), ForeignKey("places.id"), primary_key=True, nullable=False),
                          Column("amenity_id", String(60), ForeignKey("amenities.id"), primary_key=True, nullable=False))

