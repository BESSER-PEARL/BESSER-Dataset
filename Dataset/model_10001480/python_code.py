from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class color(Enum):
    pass
class PieceType(Enum):
    pass

############################################
# Definition of Classes
############################################










class BoardView:

    pass


class BoardViewInterface_Interface:

    pass


class BoardValidatorInterface_Interface:

    pass


class ChessGame:

    pass


class Player:

    pass


class BoardValidator:

    pass


class ChessGameController:

    def __init__(self, attribute: str, attribute2: str):
        self.attribute = attribute
        self.attribute2 = attribute2
        
        pass
    @property
    def attribute2(self):
        return self.__attribute2
    @attribute2.setter
    def attribute2(self, attribute2: str):
        self.__attribute2 = attribute2

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute



class ChessBoard:

    pass


class Queen:

    pass


class Pawn:

    pass


class Knigh:

    pass


class King:

    pass


class Rook:

    pass


class Bishop:

    pass


class Piece:

    def __init__(self, attribute: str, chessBoard1: "ChessBoard" = None):
        self.attribute = attribute
        self.chessBoard1 = chessBoard1
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def chessBoard1(self):
        return self.__chessBoard1
    @chessBoard1.setter
    def chessBoard1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Piece__chessBoard1", None)
        self.__chessBoard1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "piece0"):
                opp_val = getattr(old_value, "piece0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "piece0"):
                opp_val = getattr(value, "piece0", None)
                if opp_val is None:
                    setattr(value, "piece0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Position:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        
        pass
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x: int):
        self.__x = x

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y: int):
        self.__y = y



class Square:

    def __init__(self, position: Position, piece: Piece):
        self.position = position
        self.piece = piece
        
        pass
    @property
    def piece(self):
        return self.__piece
    @piece.setter
    def piece(self, piece: Piece):
        self.__piece = piece

    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, position: Position):
        self.__position = position



class ChessBoardInterface_Interface:

    pass
