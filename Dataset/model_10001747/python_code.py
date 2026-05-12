from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class RAM:

    pass


class Cache:

    def __init__(self, chunck: str):
        self.chunck = chunck
        
        pass
    @property
    def chunck(self):
        return self.__chunck
    @chunck.setter
    def chunck(self, chunck: str):
        self.__chunck = chunck



class Memory_Interface:

    pass


class Processor:

    pass
