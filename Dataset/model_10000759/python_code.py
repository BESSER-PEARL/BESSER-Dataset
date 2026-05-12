from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################










class ArrPrint:

    pass


class Print:

    pass


class Documents:

    def __init__(self, file: str, data: Json, file_name: str, tab_counter: int):
        self.file = file
        self.data = data
        self.file_name = file_name
        self.tab_counter = tab_counter
        
        pass
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data: Json):
        self.__data = data

    @property
    def file(self):
        return self.__file
    @file.setter
    def file(self, file: str):
        self.__file = file

    @property
    def file_name(self):
        return self.__file_name
    @file_name.setter
    def file_name(self, file_name: str):
        self.__file_name = file_name

    @property
    def tab_counter(self):
        return self.__tab_counter
    @tab_counter.setter
    def tab_counter(self, tab_counter: int):
        self.__tab_counter = tab_counter



class Json:

    def __init__(self, values: Value):
        self.values = values
        
        pass
    @property
    def values(self):
        return self.__values
    @values.setter
    def values(self, values: Value):
        self.__values = values



class Visitor:

    pass


class Array:

    def __init__(self, data: Value):
        self.data = data
        
        pass
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data: Value):
        self.__data = data



class Number:

    def __init__(self, data: int):
        self.data = data
        
        pass
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data: int):
        self.__data = data



class Bool:

    def __init__(self, data: bool):
        self.data = data
        
        pass
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data: bool):
        self.__data = data



class String:

    def __init__(self, data: String):
        self.data = data
        
        pass
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, data: String):
        self.__data = data



class Value(ABC):

    def __init__(self, attribute: str):
        self.attribute = attribute
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute



class Null:

    pass
