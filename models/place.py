#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship


place_amenity = Table("place_amenity",
                          Base.metadata,
                          Column("place_id", String(60), ForeignKey("places.id"), primary_key=True, nullable=False),
                          Column("amenity_id", String(60), ForeignKey("amenities.id"), primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    user = relationship("User", back_populates="places")
    city = relationship("City", back_populates="places")
    reviews = relationship("Review", back_populates="place", cascade="all, delete, delete-orphan")
    amenities = relationship("Amenity", secondary="place_amenity",  viewonly=False)

        # Only if using FileStorage
    amenity_ids = []

    @property
    def amenities(self):
        """Return list of Amenity instances based on amenity_ids"""
        from models import storage
        from models.amenity import Amenity
        return [amenity for amenity in storage.all(Amenity).values()
                if amenity.id in self.amenity_ids]

    @amenities.setter
    def amenities(self, obj):
        """Add only Amenity objects to amenity_ids"""
        from models.amenity import Amenity
        if isinstance(obj, Amenity):
            if obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)

