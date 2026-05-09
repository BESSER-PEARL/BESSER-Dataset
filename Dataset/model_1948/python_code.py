from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Asset:

    pass
class schoollibrary_Asset:

    def __init__(self, value: float):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value


class Library:

    pass
class schoollibrary_SchoolLibrary(Library):

    def __init__(self, location: str):
        self.location = location
        
        pass
    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location


class Book:

    pass
class schoollibrary_SchoolBook(Asset, Book):

    pass