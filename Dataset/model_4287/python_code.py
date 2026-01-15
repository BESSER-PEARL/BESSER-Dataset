from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class WeightKind(Enum):
    pounds = "pounds"
    kilograms = "kilograms"
class ForwardPositionKind(Enum):
    left_wing = "left_wing"
    right_wing = "right_wing"
    center = "center"
class HeightKind(Enum):
    inches = "inches"
    centimeters = "centimeters"
class ShotKind(Enum):
    left = "left"
    right = "right"
class DefencePositionKind(Enum):
    left_defence = "left_defence"
    right_defence = "right_defence"


############################################
# Definition of Classes
############################################

class hockeyleague_HockeyleagueObject(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class hockeyleague_GoalieStats:

    def __init__(self, year: str, gamesPlayedIn: int, minutesPlayedIn: int, goalsAgainstAverage: float, wins: int, losses: int, ties: int, emptyNetGoals: int, shutouts: int, goalsAgainst: int, saves: int, penaltyMinutes: int, goals: int, assists: int, points: int, hockeyleague_GoalieStats: "hockeyleague_Goalie" = None, hockeyleague_GoalieStats5: "hockeyleague_Team" = None):
        self.year = year
        self.gamesPlayedIn = gamesPlayedIn
        self.minutesPlayedIn = minutesPlayedIn
        self.goalsAgainstAverage = goalsAgainstAverage
        self.wins = wins
        self.losses = losses
        self.ties = ties
        self.emptyNetGoals = emptyNetGoals
        self.shutouts = shutouts
        self.goalsAgainst = goalsAgainst
        self.saves = saves
        self.penaltyMinutes = penaltyMinutes
        self.goals = goals
        self.assists = assists
        self.points = points
        self.hockeyleague_GoalieStats = hockeyleague_GoalieStats
        self.hockeyleague_GoalieStats5 = hockeyleague_GoalieStats5
        
    @property
    def year(self) -> str:
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year

    @property
    def wins(self) -> int:
        return self.__wins

    @wins.setter
    def wins(self, wins: int):
        self.__wins = wins

    @property
    def gamesPlayedIn(self) -> int:
        return self.__gamesPlayedIn

    @gamesPlayedIn.setter
    def gamesPlayedIn(self, gamesPlayedIn: int):
        self.__gamesPlayedIn = gamesPlayedIn

    @property
    def emptyNetGoals(self) -> int:
        return self.__emptyNetGoals

    @emptyNetGoals.setter
    def emptyNetGoals(self, emptyNetGoals: int):
        self.__emptyNetGoals = emptyNetGoals

    @property
    def saves(self) -> int:
        return self.__saves

    @saves.setter
    def saves(self, saves: int):
        self.__saves = saves

    @property
    def penaltyMinutes(self) -> int:
        return self.__penaltyMinutes

    @penaltyMinutes.setter
    def penaltyMinutes(self, penaltyMinutes: int):
        self.__penaltyMinutes = penaltyMinutes

    @property
    def shutouts(self) -> int:
        return self.__shutouts

    @shutouts.setter
    def shutouts(self, shutouts: int):
        self.__shutouts = shutouts

    @property
    def goalsAgainst(self) -> int:
        return self.__goalsAgainst

    @goalsAgainst.setter
    def goalsAgainst(self, goalsAgainst: int):
        self.__goalsAgainst = goalsAgainst

    @property
    def assists(self) -> int:
        return self.__assists

    @assists.setter
    def assists(self, assists: int):
        self.__assists = assists

    @property
    def points(self) -> int:
        return self.__points

    @points.setter
    def points(self, points: int):
        self.__points = points

    @property
    def goalsAgainstAverage(self) -> float:
        return self.__goalsAgainstAverage

    @goalsAgainstAverage.setter
    def goalsAgainstAverage(self, goalsAgainstAverage: float):
        self.__goalsAgainstAverage = goalsAgainstAverage

    @property
    def goals(self) -> int:
        return self.__goals

    @goals.setter
    def goals(self, goals: int):
        self.__goals = goals

    @property
    def losses(self) -> int:
        return self.__losses

    @losses.setter
    def losses(self, losses: int):
        self.__losses = losses

    @property
    def ties(self) -> int:
        return self.__ties

    @ties.setter
    def ties(self, ties: int):
        self.__ties = ties

    @property
    def minutesPlayedIn(self) -> int:
        return self.__minutesPlayedIn

    @minutesPlayedIn.setter
    def minutesPlayedIn(self, minutesPlayedIn: int):
        self.__minutesPlayedIn = minutesPlayedIn

    @property
    def hockeyleague_GoalieStats5(self):
        return self.__hockeyleague_GoalieStats5

    @hockeyleague_GoalieStats5.setter
    def hockeyleague_GoalieStats5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hockeyleague_GoalieStats__hockeyleague_GoalieStats5", None)
        self.__hockeyleague_GoalieStats5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hockeyleague_Team"):
                opp_val = getattr(old_value, "hockeyleague_Team", None)
                if opp_val == self:
                    setattr(old_value, "hockeyleague_Team", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hockeyleague_Team"):
                opp_val = getattr(value, "hockeyleague_Team", None)
                setattr(value, "hockeyleague_Team", self)

    @property
    def hockeyleague_GoalieStats(self):
        return self.__hockeyleague_GoalieStats

    @hockeyleague_GoalieStats.setter
    def hockeyleague_GoalieStats(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hockeyleague_GoalieStats__hockeyleague_GoalieStats", None)
        self.__hockeyleague_GoalieStats = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hockeyleague_Goalie"):
                opp_val = getattr(old_value, "hockeyleague_Goalie", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hockeyleague_Goalie"):
                opp_val = getattr(value, "hockeyleague_Goalie", None)
                if opp_val is None:
                    setattr(value, "hockeyleague_Goalie", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class hockeyleague_PlayerStats:

    def __init__(self, year: str, gamesPlayedIn: int, goals: int, assists: int, points: int, plusMinus: int, penaltyMinutes: int, powerPlayGoals: int, shortHandedGoals: int, gameWinningGoals: int, shots: int, shotPercentage: float, hockeyleague_PlayerStats: "hockeyleague_Defence" = None, hockeyleague_PlayerStats2: "hockeyleague_Forward" = None, hockeyleague_PlayerStats9: "hockeyleague_Team" = None):
        self.year = year
        self.gamesPlayedIn = gamesPlayedIn
        self.goals = goals
        self.assists = assists
        self.points = points
        self.plusMinus = plusMinus
        self.penaltyMinutes = penaltyMinutes
        self.powerPlayGoals = powerPlayGoals
        self.shortHandedGoals = shortHandedGoals
        self.gameWinningGoals = gameWinningGoals
        self.shots = shots
        self.shotPercentage = shotPercentage
        self.hockeyleague_PlayerStats = hockeyleague_PlayerStats
        self.hockeyleague_PlayerStats2 = hockeyleague_PlayerStats2
        self.hockeyleague_PlayerStats9 = hockeyleague_PlayerStats9
        
    @property
    def shots(self) -> int:
        return self.__shots

    @shots.setter
    def shots(self, shots: int):
        self.__shots = shots

    @property
    def shotPercentage(self) -> float:
        return self.__shotPercentage

    @shotPercentage.setter
    def shotPercentage(self, shotPercentage: float):
        self.__shotPercentage = shotPercentage

    @property
    def powerPlayGoals(self) -> int:
        return self.__powerPlayGoals

    @powerPlayGoals.setter
    def powerPlayGoals(self, powerPlayGoals: int):
        self.__powerPlayGoals = powerPlayGoals

    @property
    def year(self) -> str:
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year

    @property
    def plusMinus(self) -> int:
        return self.__plusMinus

    @plusMinus.setter
    def plusMinus(self, plusMinus: int):
        self.__plusMinus = plusMinus

    @property
    def assists(self) -> int:
        return self.__assists

    @assists.setter
    def assists(self, assists: int):
        self.__assists = assists

    @property
    def gamesPlayedIn(self) -> int:
        return self.__gamesPlayedIn

    @gamesPlayedIn.setter
    def gamesPlayedIn(self, gamesPlayedIn: int):
        self.__gamesPlayedIn = gamesPlayedIn

    @property
    def penaltyMinutes(self) -> int:
        return self.__penaltyMinutes

    @penaltyMinutes.setter
    def penaltyMinutes(self, penaltyMinutes: int):
        self.__penaltyMinutes = penaltyMinutes

    @property
    def gameWinningGoals(self) -> int:
        return self.__gameWinningGoals

    @gameWinningGoals.setter
    def gameWinningGoals(self, gameWinningGoals: int):
        self.__gameWinningGoals = gameWinningGoals

    @property
    def shortHandedGoals(self) -> int:
        return self.__shortHandedGoals

    @shortHandedGoals.setter
    def shortHandedGoals(self, shortHandedGoals: int):
        self.__shortHandedGoals = shortHandedGoals

    @property
    def goals(self) -> int:
        return self.__goals

    @goals.setter
    def goals(self, goals: int):
        self.__goals = goals

    @property
    def points(self) -> int:
        return self.__points

    @points.setter
    def points(self, points: int):
        self.__points = points

    @property
    def hockeyleague_PlayerStats9(self):
        return self.__hockeyleague_PlayerStats9

    @hockeyleague_PlayerStats9.setter
    def hockeyleague_PlayerStats9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hockeyleague_PlayerStats__hockeyleague_PlayerStats9", None)
        self.__hockeyleague_PlayerStats9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hockeyleague_Team10"):
                opp_val = getattr(old_value, "hockeyleague_Team10", None)
                if opp_val == self:
                    setattr(old_value, "hockeyleague_Team10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hockeyleague_Team10"):
                opp_val = getattr(value, "hockeyleague_Team10", None)
                setattr(value, "hockeyleague_Team10", self)

    @property
    def hockeyleague_PlayerStats2(self):
        return self.__hockeyleague_PlayerStats2

    @hockeyleague_PlayerStats2.setter
    def hockeyleague_PlayerStats2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hockeyleague_PlayerStats__hockeyleague_PlayerStats2", None)
        self.__hockeyleague_PlayerStats2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hockeyleague_Forward"):
                opp_val = getattr(old_value, "hockeyleague_Forward", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hockeyleague_Forward"):
                opp_val = getattr(value, "hockeyleague_Forward", None)
                if opp_val is None:
                    setattr(value, "hockeyleague_Forward", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def hockeyleague_PlayerStats(self):
        return self.__hockeyleague_PlayerStats

    @hockeyleague_PlayerStats.setter
    def hockeyleague_PlayerStats(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hockeyleague_PlayerStats__hockeyleague_PlayerStats", None)
        self.__hockeyleague_PlayerStats = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hockeyleague_Defence"):
                opp_val = getattr(old_value, "hockeyleague_Defence", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hockeyleague_Defence"):
                opp_val = getattr(value, "hockeyleague_Defence", None)
                if opp_val is None:
                    setattr(value, "hockeyleague_Defence", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Player:

    pass
class hockeyleague_Forward(Player):

    def __init__(self, position: str, hockeyleague_Forward: set["hockeyleague_PlayerStats"] = None, hockeyleague_Forward13: "hockeyleague_Team" = None):
        self.position = position
        self.hockeyleague_Forward = hockeyleague_Forward if hockeyleague_Forward is not None else set()
        self.hockeyleague_Forward13 = hockeyleague_Forward13
        
    @property
    def position(self) -> str:
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position

    @property
    def hockeyleague_Forward13(self):
        return self.__hockeyleague_Forward13

    @hockeyleague_Forward13.setter
    def hockeyleague_Forward13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hockeyleague_Forward__hockeyleague_Forward13", None)
        self.__hockeyleague_Forward13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hockeyleague_Team12"):
                opp_val = getattr(old_value, "hockeyleague_Team12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hockeyleague_Team12"):
                opp_val = getattr(value, "hockeyleague_Team12", None)
                if opp_val is None:
                    setattr(value, "hockeyleague_Team12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def hockeyleague_Forward(self):
        return self.__hockeyleague_Forward

    @hockeyleague_Forward.setter
    def hockeyleague_Forward(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hockeyleague_Forward__hockeyleague_Forward", None)
        self.__hockeyleague_Forward = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hockeyleague_PlayerStats2"):
                    opp_val = getattr(item, "hockeyleague_PlayerStats2", None)
                    
                    if opp_val == self:
                        setattr(item, "hockeyleague_PlayerStats2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hockeyleague_PlayerStats2"):
                    opp_val = getattr(item, "hockeyleague_PlayerStats2", None)
                    
                    setattr(item, "hockeyleague_PlayerStats2", self)
                    

class hockeyleague_Goalie(Player):

    pass
class hockeyleague_Defence(Player):

    def __init__(self, position: str, hockeyleague_Defence: set["hockeyleague_PlayerStats"] = None, hockeyleague_Defence16: "hockeyleague_Team" = None):
        self.position = position
        self.hockeyleague_Defence = hockeyleague_Defence if hockeyleague_Defence is not None else set()
        self.hockeyleague_Defence16 = hockeyleague_Defence16
        
    @property
    def position(self) -> str:
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position

    @property
    def hockeyleague_Defence(self):
        return self.__hockeyleague_Defence

    @hockeyleague_Defence.setter
    def hockeyleague_Defence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hockeyleague_Defence__hockeyleague_Defence", None)
        self.__hockeyleague_Defence = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hockeyleague_PlayerStats"):
                    opp_val = getattr(item, "hockeyleague_PlayerStats", None)
                    
                    if opp_val == self:
                        setattr(item, "hockeyleague_PlayerStats", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hockeyleague_PlayerStats"):
                    opp_val = getattr(item, "hockeyleague_PlayerStats", None)
                    
                    setattr(item, "hockeyleague_PlayerStats", self)
                    

    @property
    def hockeyleague_Defence16(self):
        return self.__hockeyleague_Defence16

    @hockeyleague_Defence16.setter
    def hockeyleague_Defence16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hockeyleague_Defence__hockeyleague_Defence16", None)
        self.__hockeyleague_Defence16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hockeyleague_Team15"):
                opp_val = getattr(old_value, "hockeyleague_Team15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hockeyleague_Team15"):
                opp_val = getattr(value, "hockeyleague_Team15", None)
                if opp_val is None:
                    setattr(value, "hockeyleague_Team15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class HockeyleagueObject:

    pass
class hockeyleague_Arena(HockeyleagueObject):

    def __init__(self, address: str, capacity: int, hockeyleague_Arena: "hockeyleague_Team" = None):
        self.address = address
        self.capacity = capacity
        self.hockeyleague_Arena = hockeyleague_Arena
        
    @property
    def capacity(self) -> int:
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity: int):
        self.__capacity = capacity

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def hockeyleague_Arena(self):
        return self.__hockeyleague_Arena

    @hockeyleague_Arena.setter
    def hockeyleague_Arena(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hockeyleague_Arena__hockeyleague_Arena", None)
        self.__hockeyleague_Arena = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hockeyleague_Team21"):
                opp_val = getattr(old_value, "hockeyleague_Team21", None)
                if opp_val == self:
                    setattr(old_value, "hockeyleague_Team21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hockeyleague_Team21"):
                opp_val = getattr(value, "hockeyleague_Team21", None)
                setattr(value, "hockeyleague_Team21", self)

class hockeyleague_Team(HockeyleagueObject):

    pass
class hockeyleague_Player(HockeyleagueObject):

    def __init__(self, shot: str, birthdate: str, birthplace: str, number: int, heightMesurement: str, heightValue: int, weightMesurement: str, weightValue: int):
        self.shot = shot
        self.birthdate = birthdate
        self.birthplace = birthplace
        self.number = number
        self.heightMesurement = heightMesurement
        self.heightValue = heightValue
        self.weightMesurement = weightMesurement
        self.weightValue = weightValue
        
    @property
    def birthdate(self) -> str:
        return self.__birthdate

    @birthdate.setter
    def birthdate(self, birthdate: str):
        self.__birthdate = birthdate

    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def birthplace(self) -> str:
        return self.__birthplace

    @birthplace.setter
    def birthplace(self, birthplace: str):
        self.__birthplace = birthplace

    @property
    def heightValue(self) -> int:
        return self.__heightValue

    @heightValue.setter
    def heightValue(self, heightValue: int):
        self.__heightValue = heightValue

    @property
    def weightValue(self) -> int:
        return self.__weightValue

    @weightValue.setter
    def weightValue(self, weightValue: int):
        self.__weightValue = weightValue

    @property
    def weightMesurement(self) -> str:
        return self.__weightMesurement

    @weightMesurement.setter
    def weightMesurement(self, weightMesurement: str):
        self.__weightMesurement = weightMesurement

    @property
    def shot(self) -> str:
        return self.__shot

    @shot.setter
    def shot(self, shot: str):
        self.__shot = shot

    @property
    def heightMesurement(self) -> str:
        return self.__heightMesurement

    @heightMesurement.setter
    def heightMesurement(self, heightMesurement: str):
        self.__heightMesurement = heightMesurement

class hockeyleague_League(HockeyleagueObject):

    def __init__(self, headoffice: str, hockeyleague_League: set["hockeyleague_Team"] = None):
        self.headoffice = headoffice
        self.hockeyleague_League = hockeyleague_League if hockeyleague_League is not None else set()
        
    @property
    def headoffice(self) -> str:
        return self.__headoffice

    @headoffice.setter
    def headoffice(self, headoffice: str):
        self.__headoffice = headoffice

    @property
    def hockeyleague_League(self):
        return self.__hockeyleague_League

    @hockeyleague_League.setter
    def hockeyleague_League(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hockeyleague_League__hockeyleague_League", None)
        self.__hockeyleague_League = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hockeyleague_Team7"):
                    opp_val = getattr(item, "hockeyleague_Team7", None)
                    
                    if opp_val == self:
                        setattr(item, "hockeyleague_Team7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hockeyleague_Team7"):
                    opp_val = getattr(item, "hockeyleague_Team7", None)
                    
                    setattr(item, "hockeyleague_Team7", self)
                    
