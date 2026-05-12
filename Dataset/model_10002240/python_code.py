from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Train:

    def __init__(self, trucks: int, type: str):
        self.trucks = trucks
        self.type = type
        
        pass
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def trucks(self):
        return self.__trucks
    @trucks.setter
    def trucks(self, trucks: int):
        self.__trucks = trucks



class Car1:

    def __init__(self, doors: int, helmSide: str):
        self.doors = doors
        self.helmSide = helmSide
        
        pass
    @property
    def helmSide(self):
        return self.__helmSide
    @helmSide.setter
    def helmSide(self, helmSide: str):
        self.__helmSide = helmSide

    @property
    def doors(self):
        return self.__doors
    @doors.setter
    def doors(self, doors: int):
        self.__doors = doors



class Airplane:

    def __init__(self, maxCarryingWeight: int, maxAttitude: int):
        self.maxCarryingWeight = maxCarryingWeight
        self.maxAttitude = maxAttitude
        
        pass
    @property
    def maxAttitude(self):
        return self.__maxAttitude
    @maxAttitude.setter
    def maxAttitude(self, maxAttitude: int):
        self.__maxAttitude = maxAttitude

    @property
    def maxCarryingWeight(self):
        return self.__maxCarryingWeight
    @maxCarryingWeight.setter
    def maxCarryingWeight(self, maxCarryingWeight: int):
        self.__maxCarryingWeight = maxCarryingWeight



class Boat:

    def __init__(self, maxCarryingWeight: int):
        self.maxCarryingWeight = maxCarryingWeight
        
        pass
    @property
    def maxCarryingWeight(self):
        return self.__maxCarryingWeight
    @maxCarryingWeight.setter
    def maxCarryingWeight(self, maxCarryingWeight: int):
        self.__maxCarryingWeight = maxCarryingWeight



class Vehicle:

    def __init__(self, brand: str, price: str, engine: str):
        self.brand = brand
        self.price = price
        self.engine = engine
        
        pass
    @property
    def brand(self):
        return self.__brand
    @brand.setter
    def brand(self, brand: str):
        self.__brand = brand

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: str):
        self.__price = price

    @property
    def engine(self):
        return self.__engine
    @engine.setter
    def engine(self, engine: str):
        self.__engine = engine



class Car:

    def __init__(self, model: str, engine: str, wheels: str, doors: int, width: int, length: int, height: int):
        self.model = model
        self.engine = engine
        self.wheels = wheels
        self.doors = doors
        self.width = width
        self.length = length
        self.height = height
        
        pass
    @property
    def doors(self):
        return self.__doors
    @doors.setter
    def doors(self, doors: int):
        self.__doors = doors

    @property
    def wheels(self):
        return self.__wheels
    @wheels.setter
    def wheels(self, wheels: str):
        self.__wheels = wheels

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, width: int):
        self.__width = width

    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self, model: str):
        self.__model = model

    @property
    def length(self):
        return self.__length
    @length.setter
    def length(self, length: int):
        self.__length = length

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, height: int):
        self.__height = height

    @property
    def engine(self):
        return self.__engine
    @engine.setter
    def engine(self, engine: str):
        self.__engine = engine

