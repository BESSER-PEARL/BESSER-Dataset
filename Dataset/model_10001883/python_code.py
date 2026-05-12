from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################










class Test:

    pass


class TestStand:

    def __init__(self, carToBeTested: Car):
        self.carToBeTested = carToBeTested
        
        pass
    @property
    def carToBeTested(self):
        return self.__carToBeTested
    @carToBeTested.setter
    def carToBeTested(self, carToBeTested: Car):
        self.__carToBeTested = carToBeTested



class M6:

    def __init__(self, manufacturer: str, color: str, engine: Engine):
        self.manufacturer = manufacturer
        self.color = color
        self.engine = engine
        
        pass
    @property
    def engine(self):
        return self.__engine
    @engine.setter
    def engine(self, engine: Engine):
        self.__engine = engine

    @property
    def manufacturer(self):
        return self.__manufacturer
    @manufacturer.setter
    def manufacturer(self, manufacturer: str):
        self.__manufacturer = manufacturer

    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color: str):
        self.__color = color



class Engine:

    def __init__(self, type: str, efficiencyCoefficient: int, engineSpeed: int):
        self.type = type
        self.efficiencyCoefficient = efficiencyCoefficient
        self.engineSpeed = engineSpeed
        
        pass
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def efficiencyCoefficient(self):
        return self.__efficiencyCoefficient
    @efficiencyCoefficient.setter
    def efficiencyCoefficient(self, efficiencyCoefficient: int):
        self.__efficiencyCoefficient = efficiencyCoefficient

    @property
    def engineSpeed(self):
        return self.__engineSpeed
    @engineSpeed.setter
    def engineSpeed(self, engineSpeed: int):
        self.__engineSpeed = engineSpeed



class Tennis:

    def __init__(self, manufacturer: str, color: str, engine: Engine):
        self.manufacturer = manufacturer
        self.color = color
        self.engine = engine
        
        pass
    @property
    def manufacturer(self):
        return self.__manufacturer
    @manufacturer.setter
    def manufacturer(self, manufacturer: str):
        self.__manufacturer = manufacturer

    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def engine(self):
        return self.__engine
    @engine.setter
    def engine(self, engine: Engine):
        self.__engine = engine



class Car(ABC):

    pass
