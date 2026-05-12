from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Game_PlantationType(Enum):
    pass

############################################
# Definition of Classes
############################################










class Game_GoodZone:

    def __init__(self, Stackable: bool, Pieces: Good):
        self.Stackable = Stackable
        self.Pieces = Pieces
        
        pass
    @property
    def Stackable(self):
        return self.__Stackable
    @Stackable.setter
    def Stackable(self, Stackable: bool):
        self.__Stackable = Stackable

    @property
    def Pieces(self):
        return self.__Pieces
    @Pieces.setter
    def Pieces(self, Pieces: Good):
        self.__Pieces = Pieces



class Game_IBoard_Interface:

    pass


class Game_IColonistBoard_Interface:

    pass


class Game_Plantation:

    def __init__(self, Type: Game_PlantationType, ColonistZone: Game_ColonistZone, HasProduced: bool):
        self.Type = Type
        self.ColonistZone = ColonistZone
        self.HasProduced = HasProduced
        
        pass
    @property
    def HasProduced(self):
        return self.__HasProduced
    @HasProduced.setter
    def HasProduced(self, HasProduced: bool):
        self.__HasProduced = HasProduced

    @property
    def ColonistZone(self):
        return self.__ColonistZone
    @ColonistZone.setter
    def ColonistZone(self, ColonistZone: Game_ColonistZone):
        self.__ColonistZone = ColonistZone

    @property
    def Type(self):
        return self.__Type
    @Type.setter
    def Type(self, Type: Game_PlantationType):
        self.__Type = Type



class Game_PlantationSupply:

    pass


class Game_PlayerBoard:

    def __init__(self, PlayerID: int, ColonistZone: Game_ColonistZone):
        self.PlayerID = PlayerID
        self.ColonistZone = ColonistZone
        
        pass
    @property
    def ColonistZone(self):
        return self.__ColonistZone
    @ColonistZone.setter
    def ColonistZone(self, ColonistZone: Game_ColonistZone):
        self.__ColonistZone = ColonistZone

    @property
    def PlayerID(self):
        return self.__PlayerID
    @PlayerID.setter
    def PlayerID(self, PlayerID: int):
        self.__PlayerID = PlayerID



class Game_Building:

    def __init__(self, Type: str, Cost: int, VictoryPoints: int, Size: int, ColonistZones: Game_ColonistZone, MaxColonists: int, HasProduced: bool):
        self.Type = Type
        self.Cost = Cost
        self.VictoryPoints = VictoryPoints
        self.Size = Size
        self.ColonistZones = ColonistZones
        self.MaxColonists = MaxColonists
        self.HasProduced = HasProduced
        
        pass
    @property
    def ColonistZones(self):
        return self.__ColonistZones
    @ColonistZones.setter
    def ColonistZones(self, ColonistZones: Game_ColonistZone):
        self.__ColonistZones = ColonistZones

    @property
    def HasProduced(self):
        return self.__HasProduced
    @HasProduced.setter
    def HasProduced(self, HasProduced: bool):
        self.__HasProduced = HasProduced

    @property
    def Cost(self):
        return self.__Cost
    @Cost.setter
    def Cost(self, Cost: int):
        self.__Cost = Cost

    @property
    def Type(self):
        return self.__Type
    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def Size(self):
        return self.__Size
    @Size.setter
    def Size(self, Size: int):
        self.__Size = Size

    @property
    def VictoryPoints(self):
        return self.__VictoryPoints
    @VictoryPoints.setter
    def VictoryPoints(self, VictoryPoints: int):
        self.__VictoryPoints = VictoryPoints

    @property
    def MaxColonists(self):
        return self.__MaxColonists
    @MaxColonists.setter
    def MaxColonists(self, MaxColonists: int):
        self.__MaxColonists = MaxColonists



class Game_ColonistZone:

    def __init__(self, Stackable: bool, Pieces: Colonist, MaxColonists: int):
        self.Stackable = Stackable
        self.Pieces = Pieces
        self.MaxColonists = MaxColonists
        
        pass
    @property
    def MaxColonists(self):
        return self.__MaxColonists
    @MaxColonists.setter
    def MaxColonists(self, MaxColonists: int):
        self.__MaxColonists = MaxColonists

    @property
    def Stackable(self):
        return self.__Stackable
    @Stackable.setter
    def Stackable(self, Stackable: bool):
        self.__Stackable = Stackable

    @property
    def Pieces(self):
        return self.__Pieces
    @Pieces.setter
    def Pieces(self, Pieces: Colonist):
        self.__Pieces = Pieces



class Game_ShippingShip:

    def __init__(self, Size: int):
        self.Size = Size
        
        pass
    @property
    def Size(self):
        return self.__Size
    @Size.setter
    def Size(self, Size: int):
        self.__Size = Size



class Game_ColonistShip:

    def __init__(self, ColonistZone: Game_ColonistZone, Num_Colonists: int):
        self.ColonistZone = ColonistZone
        self.Num_Colonists = Num_Colonists
        
        pass
    @property
    def Num_Colonists(self):
        return self.__Num_Colonists
    @Num_Colonists.setter
    def Num_Colonists(self, Num_Colonists: int):
        self.__Num_Colonists = Num_Colonists

    @property
    def ColonistZone(self):
        return self.__ColonistZone
    @ColonistZone.setter
    def ColonistZone(self, ColonistZone: Game_ColonistZone):
        self.__ColonistZone = ColonistZone



class Game_SupplyBoard:

    pass


class Game_TradingHouse:

    pass


class Doubloon:

    pass


class VictoryPoint:

    pass


class Governor:

    pass


class Role:

    pass


class Good:

    pass


class Colonist:

    pass


class Piece:

    pass
