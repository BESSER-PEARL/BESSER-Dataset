from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Color(Enum):
    pass
class List_Pieces_(Enum):
    pass

############################################
# Definition of Classes
############################################










class List:

    pass


class Player:

    def __init__(self, name: str, color: Color, pieces: List_Pieces_):
        self.name = name
        self.color = color
        self.pieces = pieces
        
        pass
    @property
    def pieces(self):
        return self.__pieces
    @pieces.setter
    def pieces(self, pieces: List_Pieces_):
        self.__pieces = pieces

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color: Color):
        self.__color = color



class Board:

    def __init__(self, whitePlayer: Player, blackPlayer: Player, spots: str, currentPlayer: Player, isCheck: bool, isCheckMate: bool, isStaleMate: bool):
        self.whitePlayer = whitePlayer
        self.blackPlayer = blackPlayer
        self.spots = spots
        self.currentPlayer = currentPlayer
        self.isCheck = isCheck
        self.isCheckMate = isCheckMate
        self.isStaleMate = isStaleMate
        
        pass
    @property
    def spots(self):
        return self.__spots
    @spots.setter
    def spots(self, spots: str):
        self.__spots = spots

    @property
    def whitePlayer(self):
        return self.__whitePlayer
    @whitePlayer.setter
    def whitePlayer(self, whitePlayer: Player):
        self.__whitePlayer = whitePlayer

    @property
    def blackPlayer(self):
        return self.__blackPlayer
    @blackPlayer.setter
    def blackPlayer(self, blackPlayer: Player):
        self.__blackPlayer = blackPlayer

    @property
    def isCheckMate(self):
        return self.__isCheckMate
    @isCheckMate.setter
    def isCheckMate(self, isCheckMate: bool):
        self.__isCheckMate = isCheckMate

    @property
    def isStaleMate(self):
        return self.__isStaleMate
    @isStaleMate.setter
    def isStaleMate(self, isStaleMate: bool):
        self.__isStaleMate = isStaleMate

    @property
    def isCheck(self):
        return self.__isCheck
    @isCheck.setter
    def isCheck(self, isCheck: bool):
        self.__isCheck = isCheck

    @property
    def currentPlayer(self):
        return self.__currentPlayer
    @currentPlayer.setter
    def currentPlayer(self, currentPlayer: Player):
        self.__currentPlayer = currentPlayer



class T:

    pass


class Spot:

    def __init__(self, x: int, y: int, piece: Piece):
        self.x = x
        self.y = y
        self.piece = piece
        
        pass
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y: int):
        self.__y = y

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x: int):
        self.__x = x

    @property
    def piece(self):
        return self.__piece
    @piece.setter
    def piece(self, piece: Piece):
        self.__piece = piece



class Knight:

    pass


class Queen:

    pass


class King:

    pass


class Bishop:

    pass


class Rook:

    pass


class Pawn:

    pass


class Piece:

    def __init__(self, x: int, y: int, color: Color):
        self.x = x
        self.y = y
        self.color = color
        
        pass
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x: int):
        self.__x = x

    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color: Color):
        self.__color = color

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y: int):
        self.__y = y

