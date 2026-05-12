from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class T:

    pass


class Class:

    def __init__(self, test1: bool):
        self.test1 = test1
        
        pass
    @property
    def test1(self):
        return self.__test1
    @test1.setter
    def test1(self, test1: bool):
        self.__test1 = test1

