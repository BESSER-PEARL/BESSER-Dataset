from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class BookCategory(Enum):
    Encyclopedia = "Encyclopedia"
    Dictionary = "Dictionary"


############################################
# Definition of Classes
############################################

class extlibrary_Borrower:

    pass
class extlibrary_Borrowable(ABC):

    pass
class extlibrary_Book:

    def __init__(self, title: str):
        self.title = title
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title
