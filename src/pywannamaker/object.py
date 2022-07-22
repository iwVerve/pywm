from math import dist, atan2, degrees
from typing import Optional
from .event import Event
from .enum import ObjectType

class Object:
    def __init__(self, type: int =ObjectType.BLOCK, x: int =0, y: int =0, sprite_angle: int =0, params: 'dict[str, str]' =None, events: 'list[Event]' =None, children: 'list[Object]' =None, linked: 'list[Object]' =None) -> None:
        self.type = type
        self.x = x
        self.y = y
        self.sprite_angle = sprite_angle
        self.params = params
        if params is None:
            self.params = {}
        self.events = events
        if events is None:
            self.events = []
        self.children = children
        if children is None:
            self.children = []
        self.linked = linked
        if linked is None:
            self.linked = []

    def __repr__(self) -> str:
        return self.serialize()

    def serialize(self, object_type: int =0, parent: Optional['Object'] =None) -> str:
        tag = 'object' if object_type == 0 else 'obj' if object_type == 1 else 'global_obj'
        out = f'<{tag} type="{self.type}" x="{self.x}" y="{self.y}" sprite_angle="{self.sprite_angle}"'
        if object_type == 2:
            distance = dist([self.x, self.y], [parent.x, parent.y])
            angle = degrees(atan2(parent.x - self.x, parent.y - self.y)) + 90
            out += f' slot_distance="{distance}" slot_angle="{angle}"'
        out += '>'
        for key, val in self.params.items():
            out += f'<param key="{key}" val="{val}">'
        for e in self.events:
            out += e.serialize()
        for c in self.children:
            out += c.serialize(1)
        for l in self.linked:
            out += l.serialize(2, self)
        out += f'</{tag}>'
        return out