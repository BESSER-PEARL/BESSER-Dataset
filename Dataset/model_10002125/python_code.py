from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Bewegungssensor:

    def __init__(self, bewegungssensorID: int):
        self.bewegungssensorID = bewegungssensorID
        
        pass
    @property
    def bewegungssensorID(self):
        return self.__bewegungssensorID
    @bewegungssensorID.setter
    def bewegungssensorID(self, bewegungssensorID: int):
        self.__bewegungssensorID = bewegungssensorID



class Fenstersensor:

    def __init__(self, fenstersensorID: int):
        self.fenstersensorID = fenstersensorID
        
        pass
    @property
    def fenstersensorID(self):
        return self.__fenstersensorID
    @fenstersensorID.setter
    def fenstersensorID(self, fenstersensorID: int):
        self.__fenstersensorID = fenstersensorID



class T_rsensor:

    def __init__(self, t_rsensorID: int):
        self.t_rsensorID = t_rsensorID
        
        pass
    @property
    def t_rsensorID(self):
        return self.__t_rsensorID
    @t_rsensorID.setter
    def t_rsensorID(self, t_rsensorID: int):
        self.__t_rsensorID = t_rsensorID



class Sensoren:

    def __init__(self, sensorID: int):
        self.sensorID = sensorID
        
        pass
    @property
    def sensorID(self):
        return self.__sensorID
    @sensorID.setter
    def sensorID(self, sensorID: int):
        self.__sensorID = sensorID

