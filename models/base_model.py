#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime


class BaseModel:
    """A base class for all hbnb models"""
    metadata = None

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if not kwargs:
            # If no kwargs are passed, generate new values
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            # Use 'get' to handle missing 'updated_at' and 'created_at'
            self.id = kwargs.get('id', str(uuid.uuid4()))  # default if 'id' is missing
            self.created_at = datetime.strptime(kwargs.get('created_at', datetime.now().isoformat()),
                                                 '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = datetime.strptime(kwargs.get('updated_at', datetime.now().isoformat()),
                                                 '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']  # Remove the class name if present in kwargs
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
