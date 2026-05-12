from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Elevator:

    def __init__(self, Floor: int):
        self.Floor = Floor
        
        pass
    @property
    def Floor(self):
        return self.__Floor
    @Floor.setter
    def Floor(self, Floor: int):
        self.__Floor = Floor

