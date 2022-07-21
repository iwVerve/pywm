class Param:
    def __init__(self, key: str ="key", value: str ="0") -> None:
        self.key = key
        self.value = value

    def __repr__(self) -> str:
        return self.serialize()
    
    def serialize(self) -> str:
        return f'<param key="{self.key}" val="{self.value}">'