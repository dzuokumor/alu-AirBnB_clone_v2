#!/usr/bin/python3
"""This is the file storage class for AirBnB"""

import warnings
import json
import shlex
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review

warnings.filterwarnings("ignore", category=FutureWarning, module="pep8")


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances.
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Returns a dictionary of all objects of a given class
        (or all if cls is None).
        """
        dic = {}
        if cls:
            for key, obj in self.__objects.items():
                if obj.__class__ == cls:
                    dic[key] = obj
        else:
            dic = self.__objects
        return dic

    def new(self, obj):
        """Sets __objects to given obj."""
        if obj:
            class_name = type(obj).__name__
            key = "{}.{}".format(class_name, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serialize the __objects to a JSON file."""
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name = value["__class__"]
                    class_obj = globals()[class_name]
                    self.__objects[key] = class_obj(**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """Calls reload to refresh the objects in memory."""
        self.reload()
