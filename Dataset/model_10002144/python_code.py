from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class PieceColor(Enum):
    pass
class ParkingSpotType(Enum):
    pass

############################################
# Definition of Classes
############################################










class Slot:

    def __init__(self, piece: Piece, Occupied: bool):
        self.piece = piece
        self.Occupied = Occupied
        
        pass
    @property
    def piece(self):
        return self.__piece
    @piece.setter
    def piece(self, piece: Piece):
        self.__piece = piece

    @property
    def Occupied(self):
        return self.__Occupied
    @Occupied.setter
    def Occupied(self, Occupied: bool):
        self.__Occupied = Occupied



class Pawn:

    def __init__(self, pieceColor: str):
        self.pieceColor = pieceColor
        
        pass
    @property
    def pieceColor(self):
        return self.__pieceColor
    @pieceColor.setter
    def pieceColor(self, pieceColor: str):
        self.__pieceColor = pieceColor



class King:

    def __init__(self, pieceColor: str):
        self.pieceColor = pieceColor
        
        pass
    @property
    def pieceColor(self):
        return self.__pieceColor
    @pieceColor.setter
    def pieceColor(self, pieceColor: str):
        self.__pieceColor = pieceColor



class Queen:

    def __init__(self, pieceColor: str):
        self.pieceColor = pieceColor
        
        pass
    @property
    def pieceColor(self):
        return self.__pieceColor
    @pieceColor.setter
    def pieceColor(self, pieceColor: str):
        self.__pieceColor = pieceColor



class Rook:

    def __init__(self, pieceColor: str):
        self.pieceColor = pieceColor
        
        pass
    @property
    def pieceColor(self):
        return self.__pieceColor
    @pieceColor.setter
    def pieceColor(self, pieceColor: str):
        self.__pieceColor = pieceColor



class Bishop:

    def __init__(self, pieceColor: str):
        self.pieceColor = pieceColor
        
        pass
    @property
    def pieceColor(self):
        return self.__pieceColor
    @pieceColor.setter
    def pieceColor(self, pieceColor: str):
        self.__pieceColor = pieceColor



class Knight:

    def __init__(self, pieceColor: str):
        self.pieceColor = pieceColor
        
        pass
    @property
    def pieceColor(self):
        return self.__pieceColor
    @pieceColor.setter
    def pieceColor(self, pieceColor: str):
        self.__pieceColor = pieceColor



class Piece:

    def __init__(self, pieceColor: PieceColor):
        self.pieceColor = pieceColor
        
        pass
    @property
    def pieceColor(self):
        return self.__pieceColor
    @pieceColor.setter
    def pieceColor(self, pieceColor: PieceColor):
        self.__pieceColor = pieceColor



class Chess:

    def __init__(self, board: str):
        self.board = board
        
        pass
    @property
    def board(self):
        return self.__board
    @board.setter
    def board(self, board: str):
        self.__board = board



class Level:

    def __init__(self, parkingSpots: str, levelId: int, numofSpots: int, parkingLot1: "ParkingLot" = None, parkingSpot2: set["ParkingSpot"] = None):
        self.parkingSpots = parkingSpots
        self.levelId = levelId
        self.numofSpots = numofSpots
        self.parkingLot1 = parkingLot1
        self.parkingSpot2 = parkingSpot2 if parkingSpot2 is not None else set()
        
        pass
    @property
    def parkingSpots(self):
        return self.__parkingSpots
    @parkingSpots.setter
    def parkingSpots(self, parkingSpots: str):
        self.__parkingSpots = parkingSpots

    @property
    def levelId(self):
        return self.__levelId
    @levelId.setter
    def levelId(self, levelId: int):
        self.__levelId = levelId

    @property
    def numofSpots(self):
        return self.__numofSpots
    @numofSpots.setter
    def numofSpots(self, numofSpots: int):
        self.__numofSpots = numofSpots

    @property
    def parkingLot1(self):
        return self.__parkingLot1
    @parkingLot1.setter
    def parkingLot1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Level__parkingLot1", None)
        self.__parkingLot1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "level0"):
                opp_val = getattr(old_value, "level0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "level0"):
                opp_val = getattr(value, "level0", None)
                if opp_val is None:
                    setattr(value, "level0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def parkingSpot2(self):
        return self.__parkingSpot2
    @parkingSpot2.setter
    def parkingSpot2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Level__parkingSpot2", None)
        self.__parkingSpot2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "level3"):
                    opp_val = getattr(item, "level3", None)
                    
                    if opp_val == self:
                        setattr(item, "level3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "level3"):
                    opp_val = getattr(item, "level3", None)
                    
                    setattr(item, "level3", self)
                    



class ParkingSpot:

    def __init__(self, parkingSpotId: int, spotType: ParkingSpotType, occupied: bool, level3: "Level" = None):
        self.parkingSpotId = parkingSpotId
        self.spotType = spotType
        self.occupied = occupied
        self.level3 = level3
        
        pass
    @property
    def occupied(self):
        return self.__occupied
    @occupied.setter
    def occupied(self, occupied: bool):
        self.__occupied = occupied

    @property
    def parkingSpotId(self):
        return self.__parkingSpotId
    @parkingSpotId.setter
    def parkingSpotId(self, parkingSpotId: int):
        self.__parkingSpotId = parkingSpotId

    @property
    def spotType(self):
        return self.__spotType
    @spotType.setter
    def spotType(self, spotType: ParkingSpotType):
        self.__spotType = spotType

    @property
    def level3(self):
        return self.__level3
    @level3.setter
    def level3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ParkingSpot__level3", None)
        self.__level3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parkingSpot2"):
                opp_val = getattr(old_value, "parkingSpot2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parkingSpot2"):
                opp_val = getattr(value, "parkingSpot2", None)
                if opp_val is None:
                    setattr(value, "parkingSpot2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class ParkingLot:

    def __init__(self, levels: str, spotsOccupied: int, hours: str, numOfLevels: int, capacity: int, level0: set["Level"] = None):
        self.levels = levels
        self.spotsOccupied = spotsOccupied
        self.hours = hours
        self.numOfLevels = numOfLevels
        self.capacity = capacity
        self.level0 = level0 if level0 is not None else set()
        
        pass
    @property
    def capacity(self):
        return self.__capacity
    @capacity.setter
    def capacity(self, capacity: int):
        self.__capacity = capacity

    @property
    def numOfLevels(self):
        return self.__numOfLevels
    @numOfLevels.setter
    def numOfLevels(self, numOfLevels: int):
        self.__numOfLevels = numOfLevels

    @property
    def spotsOccupied(self):
        return self.__spotsOccupied
    @spotsOccupied.setter
    def spotsOccupied(self, spotsOccupied: int):
        self.__spotsOccupied = spotsOccupied

    @property
    def levels(self):
        return self.__levels
    @levels.setter
    def levels(self, levels: str):
        self.__levels = levels

    @property
    def hours(self):
        return self.__hours
    @hours.setter
    def hours(self, hours: str):
        self.__hours = hours

    @property
    def level0(self):
        return self.__level0
    @level0.setter
    def level0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ParkingLot__level0", None)
        self.__level0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "parkingLot1"):
                    opp_val = getattr(item, "parkingLot1", None)
                    
                    if opp_val == self:
                        setattr(item, "parkingLot1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "parkingLot1"):
                    opp_val = getattr(item, "parkingLot1", None)
                    
                    setattr(item, "parkingLot1", self)
                    

