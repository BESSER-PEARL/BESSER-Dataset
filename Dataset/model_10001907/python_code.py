from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Package_Class:

    def __init__(self, attribute: str):
        self.attribute = attribute
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

