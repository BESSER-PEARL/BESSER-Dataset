from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Library:

    pass
class schoollibrary_SchoolLibrary(Library):

    def __init__(self, location: str):
        self.location = location
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

class Asset:

    pass
class Book:

    pass
class schoollibrary_SchoolBook(Book, Asset):

    pass
class schoollibrary_Asset:

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value
