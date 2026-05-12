from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Enumeration(Enum):
    pass

############################################
# Definition of Classes
############################################










class Room:

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name



class SessionType:

    def __init__(self, id: int, name: str, color: str):
        self.id = id
        self.name = name
        self.color = color
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color: str):
        self.__color = color



class Session:

    def __init__(self, id: int, start: str, end: str, type: SessionType, name: str, room: Room, Events: Event):
        self.id = id
        self.start = start
        self.end = end
        self.type = type
        self.name = name
        self.room = room
        self.Events = Events
        
        pass
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: SessionType):
        self.__type = type

    @property
    def end(self):
        return self.__end
    @end.setter
    def end(self, end: str):
        self.__end = end

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def room(self):
        return self.__room
    @room.setter
    def room(self, room: Room):
        self.__room = room

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def start(self):
        return self.__start
    @start.setter
    def start(self, start: str):
        self.__start = start

    @property
    def Events(self):
        return self.__Events
    @Events.setter
    def Events(self, Events: Event):
        self.__Events = Events



class Serie:

    def __init__(self, Events: Event):
        self.Events = Events
        
        pass
    @property
    def Events(self):
        return self.__Events
    @Events.setter
    def Events(self, Events: Event):
        self.__Events = Events



class Event:

    def __init__(self, id: int, acronym: str, name: str, edition: int, attribute: str):
        self.id = id
        self.acronym = acronym
        self.name = name
        self.edition = edition
        self.attribute = attribute
        
        pass
    @property
    def acronym(self):
        return self.__acronym
    @acronym.setter
    def acronym(self, acronym: str):
        self.__acronym = acronym

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def edition(self):
        return self.__edition
    @edition.setter
    def edition(self, edition: int):
        self.__edition = edition

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

