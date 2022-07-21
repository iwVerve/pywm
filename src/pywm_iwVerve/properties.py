class Properties:
    def __init__(self, name: str ='', version: int =90, tileset: int =0, tileset2: int =0, bg: int =0, spikes: int =0, spikes2: int =0, width: int =800, height: int =608, colors: str ='5A0200000600000005000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000', scroll_mode: int =0, music: int =0) -> None:
        self.name = name
        self.version = version
        self.tileset = tileset
        self.tileset2 = tileset2
        self.bg = bg
        self.spikes = spikes
        self.spikes2 = spikes2
        self.width = width
        self.height = height
        self.colors = colors
        self.scroll_mode = scroll_mode
        self.music = music

    def __repr__(self) -> str:
        return self.serialize()

    def serialize(self, num_objects: int =0) -> str:
        out = '<head>'
        out += f'<name>{self.name}</name>'
        out += f'<version>{self.version}</version>'
        out += f'<tileset>{self.tileset}</tileset>'
        out += f'<tileset2>{self.tileset2}</tileset2>'
        out += f'<bg>{self.bg}</bg>'
        out += f'<spikes>{self.spikes}</spikes>'
        out += f'<spikes2>{self.spikes2}</spikes2>'
        out += f'<width>{self.width}</width>'
        out += f'<height>{self.height}</height>'
        out += f'<colors>{self.colors}</colors>'
        out += f'<scroll_mode>{self.scroll_mode}</scroll_mode>'
        out += f'<music>{self.music}</music>'
        out += f'<num_objects>{num_objects}</num_objects>'
        out += '</head>'
        return out