import os
from . import config
from .properties import Properties
from .object import Object

class Map:
    def __init__(self, properties: Properties =Properties(), objects: 'list[Object]' =None) -> None:
        self.properties = properties
        self.objects = objects
        if objects is None:
            self.objects = []

    def __repr__(self) -> str:
        return self.serialize()

    def save(self, path) -> None:
        f = open(path, "w")
        f.write(self.serialize())
        f.close()

    def saveLocal(self, name) -> None:
        self.save(f'{config.local_path}{name}')

    def serialize(self) -> str:
        out = '<sfm_map>'
        self.properties.version = 90
        out += self.properties.serialize(len(self.objects))
        out += '<objects>'
        for o in self.objects:
            out += o.serialize(0)
        out += '</objects></sfm_map>'
        return out