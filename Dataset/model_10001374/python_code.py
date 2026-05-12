from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class C2:

    pass


class C1:

    def __init__(self, vv1: int):
        self.vv1 = vv1
        
        pass
    @property
    def vv1(self):
        return self.__vv1
    @vv1.setter
    def vv1(self, vv1: int):
        self.__vv1 = vv1

