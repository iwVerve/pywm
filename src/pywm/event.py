class Event:
    def __init__(self, event_index: int =-1, params: 'dict[str, str]' =None, events: 'list[Event]' =None) -> None:
        self.event_index = event_index
        self.params = params
        if params is None:
            self.params = {}
        self.events = events
        if events is None:
            self.events = []

    def __repr__(self) -> str:
        return self.serialize()

    def serialize(self) -> str:
        out = f'<event eventIndex="{self.event_index}">'
        for key, val in self.params.items():
            out += f'<param key="{key}" val="{val}">'
        for e in self.events:
            out += e.serialize()
        out += '</event>'
        return out