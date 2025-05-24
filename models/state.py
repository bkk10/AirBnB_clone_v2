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

