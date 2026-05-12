from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Ticket:

    def __init__(self, id: str):
        self.id = id
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id



class ValleyParking:

    pass


class spot:

    def __init__(self, size: int, id: str, parkedVehicle: Vehicle_Interface):
        self.size = size
        self.id = id
        self.parkedVehicle = parkedVehicle
        
        pass
    @property
    def parkedVehicle(self):
        return self.__parkedVehicle
    @parkedVehicle.setter
    def parkedVehicle(self, parkedVehicle: Vehicle_Interface):
        self.__parkedVehicle = parkedVehicle

    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id



class XL:

    pass


class large:

    pass


class medium:

    pass


class small:

    pass


class Vehicle_Interface:

    pass
