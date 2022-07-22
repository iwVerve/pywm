# pywannamaker
A python package for parsing and serializing I Wanna Maker maps from and back to their XML format.

## Usage
Importing the `pywm` module imports all required submodules.

### Opening maps
Several functions load and parse a map.

- `pywm.parseFile` does so from a file object or file path.
- `pywm.parseLocal` opens a map with the provided name in the actual game maps folder (specified in config.py).
- `pywm.parseString` opens a map from the provided string.

Worth noting is that each of these functions can correctly open any non-param element, meaning you can e.g. store individual objects in files.

### Saving
- `Map.serialize` returns the map string.
- `Map.save` saves the map to the provided file path.
- `Map.saveLocal` saves the name in the game maps folder with the provided name

### Object structure
- `Map`
    - `properties: Properties`
    - `objects: [Object]`
- `Properties`
    - `name: str`
    - `version: str`
    - `tileset: str`
    - `tileset2: str`
    - `bg: str`
    - `spikes: str`
    - `spikes2: str`
    - `width: str`
    - `height: str`
    - `colors: str`
    - `scroll_mode: str`
    - `music: str`
- `Object`
    - `type: int`
    - `x: int`
    - `y: int`
    - `sprite_angle: int`
    - `params: dict[str, str]`
    - `events: [Event]`
    - `children: [Object]`
    - `linked: [Object]`
- `Event`
    - `event_index: int`
    - `params: dict[str, str]`
    - `events: [Event]`

### Examples
```
m = pywm.Map()
m.saveLocal('empty.map')
```
Creates a new map and saves it.

```
m = pywm.parseLocal('input.map')
for o in m.objects:
    o.x = float(m.properties.width) - o.x
```
Mirrors a level horizontally

```
from pywm import Object, Event, ObjectType, EventType, ActionType
cannon = Object(ObjectType.CANNON, 400, 304)
onmetronome = Event(EventType.ONMETRONOMETICK)
onmetronome.params['frames'] = 25
onmetronome.events.append(Event(ActionType.FIRECANNON))
cannon.events.append(onmetronome)
```
Creates a new cannon object, and gives it an On metronome -> Fire event.