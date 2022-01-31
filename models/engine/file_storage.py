#!/usr/bin/python3
"""file_storage module containing file_storage class """
import os


class FileStorage:
    """
    FileStorage class: contains methods to serialize objects to JSON
    and to deserialize JSON files to objects
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        Returns __objects dictionary
        """
        return type(self).__objects

    def new(self, obj):
        """
        Sets obj value in __objects dict with key <obj class name>.id
        """
        objects_value = obj
        objects_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        type(self).__objects[objects_key] = objects_value

    def save(self):
        """
        Serializes __objects dict to JSON.
        Writes File to __file_path.
        """
        from json import dump as jdu
        from models.base_model import BaseModel

        dict_to_serial = type(self).__objects.copy()
        with open(type(self).__file_path, "w+") as File:
            for key, value in dict_to_serial.items():
                value_as_dict = value.to_dict()
                dict_to_serial[key] = value_as_dict
            jdu(dict_to_serial, File)

    def reload(self):
        """
        If the JSON file exists, deserializes it.
        Opens file in read-only mode.
        Converts the string reps back to objects.
        """
        from json import load as jlo
        from models.base_model import BaseModel
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User

        new_dict = {}
        cl = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
              "Place": Place, "Review": Review, "State": State, "User": User}
        if os.path.isfile(type(self).__file_path) is True:
            with open(type(self).__file_path, 'r') as File:
                nd = jlo(File)
            for key in nd:
                type(self).__objects[key] = cl[nd[key]["__class__"]](**nd[key])
