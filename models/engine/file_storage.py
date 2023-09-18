#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex


class FileStorage:
    """This is the 'file storage' class"""
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of all objects"""
        if cls is None:
            return FileStorage.__objects
        else:
            cls_name = cls.__name__
            filtered_objects = {}
            for key, obj in FileStorage.__objects.items():
                if obj.__class__.__name__ == cls_name:
                    filtered_objects[key] = obj
            return filtered_objects

    def new(self, obj):
        """Saves a new object"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file"""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                loaded_data = json.load(file)
                for key, value in loaded_data.items():
                    class_name = value["__class__"]
                    obj = models.classes[class_name](**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes an object from __objects"""
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]

