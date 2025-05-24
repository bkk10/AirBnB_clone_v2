from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from datetime import datetime
import models
import uuid


Base = declarative_base()

class BaseModel:
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel instance"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.fromisoformat(value) if isinstance(value, str) else value)
                    else:
                        setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.utcnow()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.utcnow()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def save(self):
        """Update updated_at and save instance"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Return dict of instance including class name but without _sa_instance_state"""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        # convert datetime to isoformat string
        if 'created_at' in dictionary:
            dictionary['created_at'] = dictionary['created_at'].isoformat()
        if 'updated_at' in dictionary:
            dictionary['updated_at'] = dictionary['updated_at'].isoformat()
        dictionary.pop('_sa_instance_state', None)
        return dictionary

    def delete(self):
        """Delete the current instance from storage"""
        models.storage.delete(self)
