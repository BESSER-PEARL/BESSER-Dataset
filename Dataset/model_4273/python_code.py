from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class TournamentType(Enum):
    Pro = "Pro"
    Amateur = "Amateur"
class Gender(Enum):
    Female = "Female"
    Male = "Male"


############################################
# Definition of Classes
############################################

class bowling_Merchandise:

    def __init__(self, name: str, price: str, serialNumber: str, bowling_Merchandise: "bowling_Fan" = None, bowling_Merchandise35: "bowling_Fan" = None):
        self.name = name
        self.price = price
        self.serialNumber = serialNumber
        self.bowling_Merchandise = bowling_Merchandise
        self.bowling_Merchandise35 = bowling_Merchandise35
        
    @property
    def price(self) -> str:
        return self.__price

    @price.setter
    def price(self, price: str):
        self.__price = price

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def serialNumber(self) -> str:
        return self.__serialNumber

    @serialNumber.setter
    def serialNumber(self, serialNumber: str):
        self.__serialNumber = serialNumber

    @property
    def bowling_Merchandise35(self):
        return self.__bowling_Merchandise35

    @bowling_Merchandise35.setter
    def bowling_Merchandise35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Merchandise__bowling_Merchandise35", None)
        self.__bowling_Merchandise35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bowling_Fan34"):
                opp_val = getattr(old_value, "bowling_Fan34", None)
                if opp_val == self:
                    setattr(old_value, "bowling_Fan34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bowling_Fan34"):
                opp_val = getattr(value, "bowling_Fan34", None)
                setattr(value, "bowling_Fan34", self)

    @property
    def bowling_Merchandise(self):
        return self.__bowling_Merchandise

    @bowling_Merchandise.setter
    def bowling_Merchandise(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Merchandise__bowling_Merchandise", None)
        self.__bowling_Merchandise = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bowling_Fan32"):
                opp_val = getattr(old_value, "bowling_Fan32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bowling_Fan32"):
                opp_val = getattr(value, "bowling_Fan32", None)
                if opp_val is None:
                    setattr(value, "bowling_Fan32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bowling_Fan:

    def __init__(self, name: str, dateOfBirth: date, hasSeasonTicket: bool, eMails: str, gender: str, numberOfTournamentsVisited: int, moneySpentOnTickets: float, bowling_Fan: "bowling_Player" = None, bowling_Fan32: set["bowling_Merchandise"] = None, bowling_Fan34: "bowling_Merchandise" = None, bowling_Fan37: set["bowling_Tournament"] = None):
        self.name = name
        self.dateOfBirth = dateOfBirth
        self.hasSeasonTicket = hasSeasonTicket
        self.eMails = eMails
        self.gender = gender
        self.numberOfTournamentsVisited = numberOfTournamentsVisited
        self.moneySpentOnTickets = moneySpentOnTickets
        self.bowling_Fan = bowling_Fan
        self.bowling_Fan32 = bowling_Fan32 if bowling_Fan32 is not None else set()
        self.bowling_Fan34 = bowling_Fan34
        self.bowling_Fan37 = bowling_Fan37 if bowling_Fan37 is not None else set()
        
    @property
    def hasSeasonTicket(self) -> bool:
        return self.__hasSeasonTicket

    @hasSeasonTicket.setter
    def hasSeasonTicket(self, hasSeasonTicket: bool):
        self.__hasSeasonTicket = hasSeasonTicket

    @property
    def moneySpentOnTickets(self) -> float:
        return self.__moneySpentOnTickets

    @moneySpentOnTickets.setter
    def moneySpentOnTickets(self, moneySpentOnTickets: float):
        self.__moneySpentOnTickets = moneySpentOnTickets

    @property
    def gender(self) -> str:
        return self.__gender

    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender

    @property
    def eMails(self) -> str:
        return self.__eMails

    @eMails.setter
    def eMails(self, eMails: str):
        self.__eMails = eMails

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def numberOfTournamentsVisited(self) -> int:
        return self.__numberOfTournamentsVisited

    @numberOfTournamentsVisited.setter
    def numberOfTournamentsVisited(self, numberOfTournamentsVisited: int):
        self.__numberOfTournamentsVisited = numberOfTournamentsVisited

    @property
    def dateOfBirth(self) -> date:
        return self.__dateOfBirth

    @dateOfBirth.setter
    def dateOfBirth(self, dateOfBirth: date):
        self.__dateOfBirth = dateOfBirth

    @property
    def bowling_Fan(self):
        return self.__bowling_Fan

    @bowling_Fan.setter
    def bowling_Fan(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Fan__bowling_Fan", None)
        self.__bowling_Fan = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bowling_Player30"):
                opp_val = getattr(old_value, "bowling_Player30", None)
                if opp_val == self:
                    setattr(old_value, "bowling_Player30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bowling_Player30"):
                opp_val = getattr(value, "bowling_Player30", None)
                setattr(value, "bowling_Player30", self)

    @property
    def bowling_Fan32(self):
        return self.__bowling_Fan32

    @bowling_Fan32.setter
    def bowling_Fan32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Fan__bowling_Fan32", None)
        self.__bowling_Fan32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bowling_Merchandise"):
                    opp_val = getattr(item, "bowling_Merchandise", None)
                    
                    if opp_val == self:
                        setattr(item, "bowling_Merchandise", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bowling_Merchandise"):
                    opp_val = getattr(item, "bowling_Merchandise", None)
                    
                    setattr(item, "bowling_Merchandise", self)
                    

    @property
    def bowling_Fan37(self):
        return self.__bowling_Fan37

    @bowling_Fan37.setter
    def bowling_Fan37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Fan__bowling_Fan37", None)
        self.__bowling_Fan37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bowling_Tournament38"):
                    opp_val = getattr(item, "bowling_Tournament38", None)
                    
                    if opp_val == self:
                        setattr(item, "bowling_Tournament38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bowling_Tournament38"):
                    opp_val = getattr(item, "bowling_Tournament38", None)
                    
                    setattr(item, "bowling_Tournament38", self)
                    

    @property
    def bowling_Fan34(self):
        return self.__bowling_Fan34

    @bowling_Fan34.setter
    def bowling_Fan34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Fan__bowling_Fan34", None)
        self.__bowling_Fan34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bowling_Merchandise35"):
                opp_val = getattr(old_value, "bowling_Merchandise35", None)
                if opp_val == self:
                    setattr(old_value, "bowling_Merchandise35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bowling_Merchandise35"):
                opp_val = getattr(value, "bowling_Merchandise35", None)
                setattr(value, "bowling_Merchandise35", self)

class bowling_Area:

    pass
class bowling_Referee:

    def __init__(self, dateOfBirth: str, bowling_Referee: "bowling_League" = None, bowling_Referee20: "bowling_RefereeToGamesMap" = None):
        self.dateOfBirth = dateOfBirth
        self.bowling_Referee = bowling_Referee
        self.bowling_Referee20 = bowling_Referee20
        
    @property
    def dateOfBirth(self) -> str:
        return self.__dateOfBirth

    @dateOfBirth.setter
    def dateOfBirth(self, dateOfBirth: str):
        self.__dateOfBirth = dateOfBirth

    @property
    def bowling_Referee20(self):
        return self.__bowling_Referee20

    @bowling_Referee20.setter
    def bowling_Referee20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Referee__bowling_Referee20", None)
        self.__bowling_Referee20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bowling_RefereeToGamesMap19"):
                opp_val = getattr(old_value, "bowling_RefereeToGamesMap19", None)
                if opp_val == self:
                    setattr(old_value, "bowling_RefereeToGamesMap19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bowling_RefereeToGamesMap19"):
                opp_val = getattr(value, "bowling_RefereeToGamesMap19", None)
                setattr(value, "bowling_RefereeToGamesMap19", self)

    @property
    def bowling_Referee(self):
        return self.__bowling_Referee

    @bowling_Referee.setter
    def bowling_Referee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Referee__bowling_Referee", None)
        self.__bowling_Referee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bowling_League17"):
                opp_val = getattr(old_value, "bowling_League17", None)
                if opp_val == self:
                    setattr(old_value, "bowling_League17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bowling_League17"):
                opp_val = getattr(value, "bowling_League17", None)
                setattr(value, "bowling_League17", self)

class bowling_Game:

    def __init__(self, frames: int, Game: "bowling_Matchup" = None, games: "bowling_Matchup" = None, bowling_Game: "bowling_Player" = None, bowling_Game23: "bowling_RefereeToGamesMap" = None):
        self.frames = frames
        self.Game = Game
        self.games = games
        self.bowling_Game = bowling_Game
        self.bowling_Game23 = bowling_Game23
        
    @property
    def frames(self) -> int:
        return self.__frames

    @frames.setter
    def frames(self, frames: int):
        self.__frames = frames

    @property
    def Game(self):
        return self.__Game

    @Game.setter
    def Game(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Game__Game", None)
        self.__Game = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "matchup"):
                opp_val = getattr(old_value, "matchup", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "matchup"):
                opp_val = getattr(value, "matchup", None)
                if opp_val is None:
                    setattr(value, "matchup", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def games(self):
        return self.__games

    @games.setter
    def games(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Game__games", None)
        self.__games = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Matchup"):
                opp_val = getattr(old_value, "Matchup", None)
                if opp_val == self:
                    setattr(old_value, "Matchup", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Matchup"):
                opp_val = getattr(value, "Matchup", None)
                setattr(value, "Matchup", self)

    @property
    def bowling_Game23(self):
        return self.__bowling_Game23

    @bowling_Game23.setter
    def bowling_Game23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Game__bowling_Game23", None)
        self.__bowling_Game23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bowling_RefereeToGamesMap22"):
                opp_val = getattr(old_value, "bowling_RefereeToGamesMap22", None)
                if opp_val == self:
                    setattr(old_value, "bowling_RefereeToGamesMap22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bowling_RefereeToGamesMap22"):
                opp_val = getattr(value, "bowling_RefereeToGamesMap22", None)
                setattr(value, "bowling_RefereeToGamesMap22", self)

    @property
    def bowling_Game(self):
        return self.__bowling_Game

    @bowling_Game.setter
    def bowling_Game(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Game__bowling_Game", None)
        self.__bowling_Game = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bowling_Player12"):
                opp_val = getattr(old_value, "bowling_Player12", None)
                if opp_val == self:
                    setattr(old_value, "bowling_Player12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bowling_Player12"):
                opp_val = getattr(value, "bowling_Player12", None)
                setattr(value, "bowling_Player12", self)

class bowling_RefereeToGamesMap:

    pass
class bowling_PlayerToPointsMap:

    def __init__(self, value: str, bowling_PlayerToPointsMap: "bowling_Tournament" = None, bowling_PlayerToPointsMap14: "bowling_Player" = None):
        self.value = value
        self.bowling_PlayerToPointsMap = bowling_PlayerToPointsMap
        self.bowling_PlayerToPointsMap14 = bowling_PlayerToPointsMap14
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def bowling_PlayerToPointsMap(self):
        return self.__bowling_PlayerToPointsMap

    @bowling_PlayerToPointsMap.setter
    def bowling_PlayerToPointsMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_PlayerToPointsMap__bowling_PlayerToPointsMap", None)
        self.__bowling_PlayerToPointsMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bowling_Tournament3"):
                opp_val = getattr(old_value, "bowling_Tournament3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bowling_Tournament3"):
                opp_val = getattr(value, "bowling_Tournament3", None)
                if opp_val is None:
                    setattr(value, "bowling_Tournament3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bowling_PlayerToPointsMap14(self):
        return self.__bowling_PlayerToPointsMap14

    @bowling_PlayerToPointsMap14.setter
    def bowling_PlayerToPointsMap14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_PlayerToPointsMap__bowling_PlayerToPointsMap14", None)
        self.__bowling_PlayerToPointsMap14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bowling_Player15"):
                opp_val = getattr(old_value, "bowling_Player15", None)
                if opp_val == self:
                    setattr(old_value, "bowling_Player15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bowling_Player15"):
                opp_val = getattr(value, "bowling_Player15", None)
                setattr(value, "bowling_Player15", self)

class bowling_Matchup:

    def __init__(self, nrSpectators: str, bowling_Matchup: "bowling_Tournament" = None, matchup: set["bowling_Game"] = None, Matchup: "bowling_Game" = None):
        self.nrSpectators = nrSpectators
        self.bowling_Matchup = bowling_Matchup
        self.matchup = matchup if matchup is not None else set()
        self.Matchup = Matchup
        
    @property
    def nrSpectators(self) -> str:
        return self.__nrSpectators

    @nrSpectators.setter
    def nrSpectators(self, nrSpectators: str):
        self.__nrSpectators = nrSpectators

    @property
    def matchup(self):
        return self.__matchup

    @matchup.setter
    def matchup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Matchup__matchup", None)
        self.__matchup = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Game"):
                    opp_val = getattr(item, "Game", None)
                    
                    if opp_val == self:
                        setattr(item, "Game", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Game"):
                    opp_val = getattr(item, "Game", None)
                    
                    setattr(item, "Game", self)
                    

    @property
    def Matchup(self):
        return self.__Matchup

    @Matchup.setter
    def Matchup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Matchup__Matchup", None)
        self.__Matchup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "games"):
                opp_val = getattr(old_value, "games", None)
                if opp_val == self:
                    setattr(old_value, "games", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "games"):
                opp_val = getattr(value, "games", None)
                setattr(value, "games", self)

    @property
    def bowling_Matchup(self):
        return self.__bowling_Matchup

    @bowling_Matchup.setter
    def bowling_Matchup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Matchup__bowling_Matchup", None)
        self.__bowling_Matchup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bowling_Tournament"):
                opp_val = getattr(old_value, "bowling_Tournament", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bowling_Tournament"):
                opp_val = getattr(value, "bowling_Tournament", None)
                if opp_val is None:
                    setattr(value, "bowling_Tournament", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bowling_Tournament:

    def __init__(self, type: str, priceMoney: float, receivesTrophy: bool, matchDays: date, bowling_Tournament28: "bowling_Area" = None, bowling_Tournament: set["bowling_Matchup"] = None, bowling_Tournament3: set["bowling_PlayerToPointsMap"] = None, bowling_Tournament5: set["bowling_Player"] = None, bowling_Tournament8: set["bowling_RefereeToGamesMap"] = None, bowling_Tournament38: "bowling_Fan" = None):
        self.type = type
        self.priceMoney = priceMoney
        self.receivesTrophy = receivesTrophy
        self.matchDays = matchDays
        self.bowling_Tournament28 = bowling_Tournament28
        self.bowling_Tournament = bowling_Tournament if bowling_Tournament is not None else set()
        self.bowling_Tournament3 = bowling_Tournament3 if bowling_Tournament3 is not None else set()
        self.bowling_Tournament5 = bowling_Tournament5 if bowling_Tournament5 is not None else set()
        self.bowling_Tournament8 = bowling_Tournament8 if bowling_Tournament8 is not None else set()
        self.bowling_Tournament38 = bowling_Tournament38
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def receivesTrophy(self) -> bool:
        return self.__receivesTrophy

    @receivesTrophy.setter
    def receivesTrophy(self, receivesTrophy: bool):
        self.__receivesTrophy = receivesTrophy

    @property
    def matchDays(self) -> date:
        return self.__matchDays

    @matchDays.setter
    def matchDays(self, matchDays: date):
        self.__matchDays = matchDays

    @property
    def priceMoney(self) -> float:
        return self.__priceMoney

    @priceMoney.setter
    def priceMoney(self, priceMoney: float):
        self.__priceMoney = priceMoney

    @property
    def bowling_Tournament5(self):
        return self.__bowling_Tournament5

    @bowling_Tournament5.setter
    def bowling_Tournament5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Tournament__bowling_Tournament5", None)
        self.__bowling_Tournament5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bowling_Player6"):
                    opp_val = getattr(item, "bowling_Player6", None)
                    
                    if opp_val == self:
                        setattr(item, "bowling_Player6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bowling_Player6"):
                    opp_val = getattr(item, "bowling_Player6", None)
                    
                    setattr(item, "bowling_Player6", self)
                    

    @property
    def bowling_Tournament38(self):
        return self.__bowling_Tournament38

    @bowling_Tournament38.setter
    def bowling_Tournament38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Tournament__bowling_Tournament38", None)
        self.__bowling_Tournament38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bowling_Fan37"):
                opp_val = getattr(old_value, "bowling_Fan37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bowling_Fan37"):
                opp_val = getattr(value, "bowling_Fan37", None)
                if opp_val is None:
                    setattr(value, "bowling_Fan37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bowling_Tournament3(self):
        return self.__bowling_Tournament3

    @bowling_Tournament3.setter
    def bowling_Tournament3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Tournament__bowling_Tournament3", None)
        self.__bowling_Tournament3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bowling_PlayerToPointsMap"):
                    opp_val = getattr(item, "bowling_PlayerToPointsMap", None)
                    
                    if opp_val == self:
                        setattr(item, "bowling_PlayerToPointsMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bowling_PlayerToPointsMap"):
                    opp_val = getattr(item, "bowling_PlayerToPointsMap", None)
                    
                    setattr(item, "bowling_PlayerToPointsMap", self)
                    

    @property
    def bowling_Tournament(self):
        return self.__bowling_Tournament

    @bowling_Tournament.setter
    def bowling_Tournament(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Tournament__bowling_Tournament", None)
        self.__bowling_Tournament = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bowling_Matchup"):
                    opp_val = getattr(item, "bowling_Matchup", None)
                    
                    if opp_val == self:
                        setattr(item, "bowling_Matchup", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bowling_Matchup"):
                    opp_val = getattr(item, "bowling_Matchup", None)
                    
                    setattr(item, "bowling_Matchup", self)
                    

    @property
    def bowling_Tournament8(self):
        return self.__bowling_Tournament8

    @bowling_Tournament8.setter
    def bowling_Tournament8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Tournament__bowling_Tournament8", None)
        self.__bowling_Tournament8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bowling_RefereeToGamesMap"):
                    opp_val = getattr(item, "bowling_RefereeToGamesMap", None)
                    
                    if opp_val == self:
                        setattr(item, "bowling_RefereeToGamesMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bowling_RefereeToGamesMap"):
                    opp_val = getattr(item, "bowling_RefereeToGamesMap", None)
                    
                    setattr(item, "bowling_RefereeToGamesMap", self)
                    

    @property
    def bowling_Tournament28(self):
        return self.__bowling_Tournament28

    @bowling_Tournament28.setter
    def bowling_Tournament28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Tournament__bowling_Tournament28", None)
        self.__bowling_Tournament28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bowling_Area27"):
                opp_val = getattr(old_value, "bowling_Area27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bowling_Area27"):
                opp_val = getattr(value, "bowling_Area27", None)
                if opp_val is None:
                    setattr(value, "bowling_Area27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bowling_Player:

    def __init__(self, name: str, dateOfBirth: date, height: float, isProfessional: bool, eMails: str, numberOfVictories: int, playedTournamentTypes: str, winLossRatio: str, gender: str, bowling_Player: "bowling_League" = None, bowling_Player6: "bowling_Tournament" = None, bowling_Player12: "bowling_Game" = None, bowling_Player15: "bowling_PlayerToPointsMap" = None, bowling_Player30: "bowling_Fan" = None):
        self.name = name
        self.dateOfBirth = dateOfBirth
        self.height = height
        self.isProfessional = isProfessional
        self.eMails = eMails
        self.numberOfVictories = numberOfVictories
        self.playedTournamentTypes = playedTournamentTypes
        self.winLossRatio = winLossRatio
        self.gender = gender
        self.bowling_Player = bowling_Player
        self.bowling_Player6 = bowling_Player6
        self.bowling_Player12 = bowling_Player12
        self.bowling_Player15 = bowling_Player15
        self.bowling_Player30 = bowling_Player30
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def eMails(self) -> str:
        return self.__eMails

    @eMails.setter
    def eMails(self, eMails: str):
        self.__eMails = eMails

    @property
    def dateOfBirth(self) -> date:
        return self.__dateOfBirth

    @dateOfBirth.setter
    def dateOfBirth(self, dateOfBirth: date):
        self.__dateOfBirth = dateOfBirth

    @property
    def isProfessional(self) -> bool:
        return self.__isProfessional

    @isProfessional.setter
    def isProfessional(self, isProfessional: bool):
        self.__isProfessional = isProfessional

    @property
    def height(self) -> float:
        return self.__height

    @height.setter
    def height(self, height: float):
        self.__height = height

    @property
    def playedTournamentTypes(self) -> str:
        return self.__playedTournamentTypes

    @playedTournamentTypes.setter
    def playedTournamentTypes(self, playedTournamentTypes: str):
        self.__playedTournamentTypes = playedTournamentTypes

    @property
    def gender(self) -> str:
        return self.__gender

    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender

    @property
    def winLossRatio(self) -> str:
        return self.__winLossRatio

    @winLossRatio.setter
    def winLossRatio(self, winLossRatio: str):
        self.__winLossRatio = winLossRatio

    @property
    def numberOfVictories(self) -> int:
        return self.__numberOfVictories

    @numberOfVictories.setter
    def numberOfVictories(self, numberOfVictories: int):
        self.__numberOfVictories = numberOfVictories

    @property
    def bowling_Player6(self):
        return self.__bowling_Player6

    @bowling_Player6.setter
    def bowling_Player6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Player__bowling_Player6", None)
        self.__bowling_Player6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bowling_Tournament5"):
                opp_val = getattr(old_value, "bowling_Tournament5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bowling_Tournament5"):
                opp_val = getattr(value, "bowling_Tournament5", None)
                if opp_val is None:
                    setattr(value, "bowling_Tournament5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bowling_Player12(self):
        return self.__bowling_Player12

    @bowling_Player12.setter
    def bowling_Player12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Player__bowling_Player12", None)
        self.__bowling_Player12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bowling_Game"):
                opp_val = getattr(old_value, "bowling_Game", None)
                if opp_val == self:
                    setattr(old_value, "bowling_Game", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bowling_Game"):
                opp_val = getattr(value, "bowling_Game", None)
                setattr(value, "bowling_Game", self)

    @property
    def bowling_Player30(self):
        return self.__bowling_Player30

    @bowling_Player30.setter
    def bowling_Player30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Player__bowling_Player30", None)
        self.__bowling_Player30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bowling_Fan"):
                opp_val = getattr(old_value, "bowling_Fan", None)
                if opp_val == self:
                    setattr(old_value, "bowling_Fan", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bowling_Fan"):
                opp_val = getattr(value, "bowling_Fan", None)
                setattr(value, "bowling_Fan", self)

    @property
    def bowling_Player15(self):
        return self.__bowling_Player15

    @bowling_Player15.setter
    def bowling_Player15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Player__bowling_Player15", None)
        self.__bowling_Player15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bowling_PlayerToPointsMap14"):
                opp_val = getattr(old_value, "bowling_PlayerToPointsMap14", None)
                if opp_val == self:
                    setattr(old_value, "bowling_PlayerToPointsMap14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bowling_PlayerToPointsMap14"):
                opp_val = getattr(value, "bowling_PlayerToPointsMap14", None)
                setattr(value, "bowling_PlayerToPointsMap14", self)

    @property
    def bowling_Player(self):
        return self.__bowling_Player

    @bowling_Player.setter
    def bowling_Player(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Player__bowling_Player", None)
        self.__bowling_Player = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bowling_League"):
                opp_val = getattr(old_value, "bowling_League", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bowling_League"):
                opp_val = getattr(value, "bowling_League", None)
                if opp_val is None:
                    setattr(value, "bowling_League", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def validate(self, context: str, chain: str) -> bool:
        # TODO: Implement validate method
        pass

class bowling_League:

    def __init__(self, name: str, bowling_League: set["bowling_Player"] = None, bowling_League17: "bowling_Referee" = None):
        self.name = name
        self.bowling_League = bowling_League if bowling_League is not None else set()
        self.bowling_League17 = bowling_League17
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bowling_League17(self):
        return self.__bowling_League17

    @bowling_League17.setter
    def bowling_League17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_League__bowling_League17", None)
        self.__bowling_League17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bowling_Referee"):
                opp_val = getattr(old_value, "bowling_Referee", None)
                if opp_val == self:
                    setattr(old_value, "bowling_Referee", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bowling_Referee"):
                opp_val = getattr(value, "bowling_Referee", None)
                setattr(value, "bowling_Referee", self)

    @property
    def bowling_League(self):
        return self.__bowling_League

    @bowling_League.setter
    def bowling_League(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_League__bowling_League", None)
        self.__bowling_League = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bowling_Player"):
                    opp_val = getattr(item, "bowling_Player", None)
                    
                    if opp_val == self:
                        setattr(item, "bowling_Player", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bowling_Player"):
                    opp_val = getattr(item, "bowling_Player", None)
                    
                    setattr(item, "bowling_Player", self)
                    
