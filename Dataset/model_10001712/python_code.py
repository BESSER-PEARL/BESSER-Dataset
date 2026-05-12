from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Coach:

    def __init__(self, numberOfSeats: int, seatsFilled: int):
        self.numberOfSeats = numberOfSeats
        self.seatsFilled = seatsFilled
        
        pass
    @property
    def seatsFilled(self):
        return self.__seatsFilled
    @seatsFilled.setter
    def seatsFilled(self, seatsFilled: int):
        self.__seatsFilled = seatsFilled

    @property
    def numberOfSeats(self):
        return self.__numberOfSeats
    @numberOfSeats.setter
    def numberOfSeats(self, numberOfSeats: int):
        self.__numberOfSeats = numberOfSeats



class FirstClass:

    def __init__(self, numberOfSeats: int, seatsFilled: int):
        self.numberOfSeats = numberOfSeats
        self.seatsFilled = seatsFilled
        
        pass
    @property
    def numberOfSeats(self):
        return self.__numberOfSeats
    @numberOfSeats.setter
    def numberOfSeats(self, numberOfSeats: int):
        self.__numberOfSeats = numberOfSeats

    @property
    def seatsFilled(self):
        return self.__seatsFilled
    @seatsFilled.setter
    def seatsFilled(self, seatsFilled: int):
        self.__seatsFilled = seatsFilled



class PassengerTrain:

    def __init__(self, Origin: str, Stops: str, numberOfPassengers: int):
        self.Origin = Origin
        self.Stops = Stops
        self.numberOfPassengers = numberOfPassengers
        
        pass
    @property
    def numberOfPassengers(self):
        return self.__numberOfPassengers
    @numberOfPassengers.setter
    def numberOfPassengers(self, numberOfPassengers: int):
        self.__numberOfPassengers = numberOfPassengers

    @property
    def Origin(self):
        return self.__Origin
    @Origin.setter
    def Origin(self, Origin: str):
        self.__Origin = Origin

    @property
    def Stops(self):
        return self.__Stops
    @Stops.setter
    def Stops(self, Stops: str):
        self.__Stops = Stops



class CargoTrain:

    def __init__(self, Origin: str, Stops: str, Containers: str):
        self.Origin = Origin
        self.Stops = Stops
        self.Containers = Containers
        
        pass
    @property
    def Stops(self):
        return self.__Stops
    @Stops.setter
    def Stops(self, Stops: str):
        self.__Stops = Stops

    @property
    def Origin(self):
        return self.__Origin
    @Origin.setter
    def Origin(self, Origin: str):
        self.__Origin = Origin

    @property
    def Containers(self):
        return self.__Containers
    @Containers.setter
    def Containers(self, Containers: str):
        self.__Containers = Containers



class Train:

    def __init__(self, Power: str, Manufacturer: str, Cars: str, Operator: str):
        self.Power = Power
        self.Manufacturer = Manufacturer
        self.Cars = Cars
        self.Operator = Operator
        
        pass
    @property
    def Operator(self):
        return self.__Operator
    @Operator.setter
    def Operator(self, Operator: str):
        self.__Operator = Operator

    @property
    def Manufacturer(self):
        return self.__Manufacturer
    @Manufacturer.setter
    def Manufacturer(self, Manufacturer: str):
        self.__Manufacturer = Manufacturer

    @property
    def Power(self):
        return self.__Power
    @Power.setter
    def Power(self, Power: str):
        self.__Power = Power

    @property
    def Cars(self):
        return self.__Cars
    @Cars.setter
    def Cars(self, Cars: str):
        self.__Cars = Cars

