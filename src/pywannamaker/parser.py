import os
from . import config
from .event import Event
from .object import Object
from .properties import Properties
from .map import Map

from typing import Union, Optional
from xml.dom.minidom import Element, parse as parseXml, parseString as parseXmlString, Document

def get_params(node: Element) -> 'dict[str, str]':
    params = {}
    for param in node.getElementsByTagName('param'):
        key = param.getAttribute('key') if param.hasAttribute('key') else ''
        value = param.getAttribute('val') if param.hasAttribute('val') else ''
        params[key] = value
    return params

def parse(node: Element) -> Optional[Union[Map, Properties, Object, Event]]:
    tag_name = node.tagName
    if tag_name == 'sfm_map':
        p = parse(node.childNodes[0])
        o = parse(node.childNodes[1])
        return Map(p, o)
    elif tag_name == 'head':
        p_name, p_version, p_tileset, p_tileset2, p_bg, p_spikes, p_spikes2, p_width, p_height, p_colors, p_scroll_mode, p_music = \
            [node.getElementsByTagName(p_tag_name)[0].childNodes[0].nodeValue for p_tag_name in \
            ['name', 'version', 'tileset', 'tileset2', 'bg', 'spikes', 'spikes2', 'width', 'height', 'colors', 'scroll_mode', 'music']]
        return Properties(p_name, p_version, p_tileset, p_tileset2, p_bg, p_spikes, p_spikes2, p_width, p_height, p_colors, p_scroll_mode, p_music)
    elif tag_name == 'objects':
        objects = []
        for n in node.childNodes:
            objects.append(parse(n))
        return objects
    elif tag_name == 'object' or tag_name == 'obj' or tag_name == 'global_obj':
        x = float(node.getAttribute('x')) if node.hasAttribute('x') else 0
        y = float(node.getAttribute('y')) if node.hasAttribute('y') else 0
        object_type = int(node.getAttribute('type')) if node.hasAttribute('type') else 0
        sprite_angle = int(node.getAttribute('sprite_angle')) if node.hasAttribute('sprite_angle') else 0
        name = ''
        if node.getElementsByTagName('name'):
            name = node.getElementsByTagName('name')[0].childNodes[0].nodeValue
        params = get_params(node)
        events = []
        children = []
        linked = []
        for n in node.childNodes:
            o = parse(n)
            if n.tagName == 'event':
                events.append(o)
            elif n.tagName == 'obj':
                children.append(o)
            elif n.tagName == 'global_obj':
                linked.append(o)
        return Object(object_type, x, y, sprite_angle, name, params, events, children, linked)
    elif tag_name == 'event':
        event_index = node.getAttribute('eventIndex') if node.hasAttribute('eventIndex') else '0'
        params = get_params(node)
        events = []
        for n in node.childNodes:
            o = parse(n)
            if n.tagName == 'event':
                events.append(o)
        return Event(event_index, params, events)

def parseFile(file_or_path) -> Optional[Union[Map, Properties, Object, Event]]:
    return parse(parseXml(file_or_path).childNodes[0])

def parseLocal(name) -> Optional[Union[Map, Properties, Object, Event]]:
    return parseFile(f'{config.local_path}{name}')

def parseString(string: str) -> Optional[Union[Map, Properties, Object, Event]]:
    return parse(parseXmlString(string).childNodes[0])