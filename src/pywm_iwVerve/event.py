from .param import Param

class Event:
    def __init__(self, eventIndex: int =-1, params: 'dict[str, str]' =None, events: 'list[Event]' =None) -> None:
        self.eventIndex = eventIndex
        self.params = params
        if params is None:
            self.params = {}
        self.events = events
        if events is None:
            self.events = []

    def __repr__(self) -> str:
        return self.serialize()

    def serialize(self) -> str:
        out = f'<event eventIndex="{self.eventIndex}">'
        for key, val in self.params.items():
            out += f'<param key="{key}" val="{val}">'
        for e in self.events:
            out += e.serialize()
        out += '</event>'
        return out