from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os
import models

class State(BaseModel, Base):
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state", cascade="all, delete, delete-orphan")
    else:
        @property
        def cities(self):
            return [city for city in models.storage.all("City").values() if city.state_id == self.id]
        
    def __str__(self):
        return f"[State] ({self.id}) {self.__dict__}"
    
    @property
    def cities(self):
        """return the list of city objects from storage linked to the current state"""
        from models import storage
        from models.city import City
        #Get all city objects from storage
        all_cities = storage.all(City)
        #Filter cities that belong to the current state
        state_cities = []
        for city in all_cities.values():
            if city.state_id == self.id:
                state_cities.append(city)
        return state_cities


