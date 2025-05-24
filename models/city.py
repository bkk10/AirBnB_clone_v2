from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship  # ✅ add this

class City(BaseModel, Base):
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    
    # ✅ correct relationship reference
    places = relationship("Place", back_populates="city", cascade="all, delete, delete-orphan")

    def __str__(self):
        return f"[City] ({self.id}) {self.__dict__}"
