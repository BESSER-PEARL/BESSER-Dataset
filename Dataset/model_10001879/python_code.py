from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class C3:

    def __init__(self, Integer_k: int, long_m: str):
        self.Integer_k = Integer_k
        self.long_m = long_m
        
        pass
    @property
    def long_m(self):
        return self.__long_m
    @long_m.setter
    def long_m(self, long_m: str):
        self.__long_m = long_m

    @property
    def Integer_k(self):
        return self.__Integer_k
    @Integer_k.setter
    def Integer_k(self, Integer_k: int):
        self.__Integer_k = Integer_k



class C2:

    pass


class C1:

    pass


class S1:

    def __init__(self, static_int_v1: str, double_v2: str):
        self.static_int_v1 = static_int_v1
        self.double_v2 = double_v2
        
        pass
    @property
    def static_int_v1(self):
        return self.__static_int_v1
    @static_int_v1.setter
    def static_int_v1(self, static_int_v1: str):
        self.__static_int_v1 = static_int_v1

    @property
    def double_v2(self):
        return self.__double_v2
    @double_v2.setter
    def double_v2(self, double_v2: str):
        self.__double_v2 = double_v2

