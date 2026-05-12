from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class STATE(Enum):
    pass
class Player(Enum):
    pass

############################################
# Definition of Classes
############################################










class Queen:

    pass


class King:

    pass


class Knight:

    pass


class Bishop:

    pass


class Rook:

    pass


class Pawn:

    pass


class Piece(ABC):

    def __init__(self, Name: str):
        self.Name = Name
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

