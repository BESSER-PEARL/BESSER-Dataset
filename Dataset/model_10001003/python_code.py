from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class PowerUps:

    def __init__(self, locations: str, speciliaty: str, points: int):
        self.locations = locations
        self.speciliaty = speciliaty
        self.points = points
        
        pass
    @property
    def points(self):
        return self.__points
    @points.setter
    def points(self, points: int):
        self.__points = points

    @property
    def locations(self):
        return self.__locations
    @locations.setter
    def locations(self, locations: str):
        self.__locations = locations

    @property
    def speciliaty(self):
        return self.__speciliaty
    @speciliaty.setter
    def speciliaty(self, speciliaty: str):
        self.__speciliaty = speciliaty



class GameMap:

    def __init__(self, walls: str, transitions: str, poerups: str):
        self.walls = walls
        self.transitions = transitions
        self.poerups = poerups
        
        pass
    @property
    def transitions(self):
        return self.__transitions
    @transitions.setter
    def transitions(self, transitions: str):
        self.__transitions = transitions

    @property
    def walls(self):
        return self.__walls
    @walls.setter
    def walls(self, walls: str):
        self.__walls = walls

    @property
    def poerups(self):
        return self.__poerups
    @poerups.setter
    def poerups(self, poerups: str):
        self.__poerups = poerups



class Monster:

    def __init__(self, location: str, type: str, specilization: str, lives: int):
        self.location = location
        self.type = type
        self.specilization = specilization
        self.lives = lives
        
        pass
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def specilization(self):
        return self.__specilization
    @specilization.setter
    def specilization(self, specilization: str):
        self.__specilization = specilization

    @property
    def lives(self):
        return self.__lives
    @lives.setter
    def lives(self, lives: int):
        self.__lives = lives

    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self, location: str):
        self.__location = location



class Game:

    def __init__(self, Timer: int):
        self.Timer = Timer
        
        pass
    @property
    def Timer(self):
        return self.__Timer
    @Timer.setter
    def Timer(self, Timer: int):
        self.__Timer = Timer



class BomberMan:

    def __init__(self, points: int, lives: int, location: str):
        self.points = points
        self.lives = lives
        self.location = location
        
        pass
    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def points(self):
        return self.__points
    @points.setter
    def points(self, points: int):
        self.__points = points

    @property
    def lives(self):
        return self.__lives
    @lives.setter
    def lives(self, lives: int):
        self.__lives = lives

