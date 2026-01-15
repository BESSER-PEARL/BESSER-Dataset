from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class BookCategory(Enum):


############################################
# Definition of Classes
############################################

class extlibrary_Borrower:

    pass
class extlibrary_Borrowable(ABC):

    pass
class extlibrary_Item(ABC):

    pass
class extlibrary_Book:

    pass