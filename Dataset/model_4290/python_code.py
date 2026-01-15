from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class GameType(Enum):
    ACTION = "ACTION"
    RPG = "RPG"
    FPS = "FPS"
    STRATEGIC = "STRATEGIC"
    COMBAT = "COMBAT"


############################################
# Definition of Classes
############################################

class gametournament_QualificationPhase:

    def __init__(self, gametournament_QualificationPhase8: set["gametournament_Pool"] = None, gametournament_QualificationPhase14: "gametournament_FinalPhase" = None, gametournament_QualificationPhase: "gametournament_Tournament" = None):
        self.gametournament_QualificationPhase8 = gametournament_QualificationPhase8 if gametournament_QualificationPhase8 is not None else set()
        self.gametournament_QualificationPhase14 = gametournament_QualificationPhase14
        self.gametournament_QualificationPhase = gametournament_QualificationPhase
        
    @property
    def gametournament_QualificationPhase(self):
        return self.__gametournament_QualificationPhase

    @gametournament_QualificationPhase.setter
    def gametournament_QualificationPhase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gametournament_QualificationPhase__gametournament_QualificationPhase", None)
        self.__gametournament_QualificationPhase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gametournament_Tournament6"):
                opp_val = getattr(old_value, "gametournament_Tournament6", None)
                if opp_val == self:
                    setattr(old_value, "gametournament_Tournament6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gametournament_Tournament6"):
                opp_val = getattr(value, "gametournament_Tournament6", None)
                setattr(value, "gametournament_Tournament6", self)

    @property
    def gametournament_QualificationPhase14(self):
        return self.__gametournament_QualificationPhase14

    @gametournament_QualificationPhase14.setter
    def gametournament_QualificationPhase14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gametournament_QualificationPhase__gametournament_QualificationPhase14", None)
        self.__gametournament_QualificationPhase14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gametournament_FinalPhase13"):
                opp_val = getattr(old_value, "gametournament_FinalPhase13", None)
                if opp_val == self:
                    setattr(old_value, "gametournament_FinalPhase13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gametournament_FinalPhase13"):
                opp_val = getattr(value, "gametournament_FinalPhase13", None)
                setattr(value, "gametournament_FinalPhase13", self)

    @property
    def gametournament_QualificationPhase8(self):
        return self.__gametournament_QualificationPhase8

    @gametournament_QualificationPhase8.setter
    def gametournament_QualificationPhase8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gametournament_QualificationPhase__gametournament_QualificationPhase8", None)
        self.__gametournament_QualificationPhase8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gametournament_Pool"):
                    opp_val = getattr(item, "gametournament_Pool", None)
                    
                    if opp_val == self:
                        setattr(item, "gametournament_Pool", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gametournament_Pool"):
                    opp_val = getattr(item, "gametournament_Pool", None)
                    
                    setattr(item, "gametournament_Pool", self)
                    

    def createPools(self) -> str:
        # TODO: Implement createPools method
        pass

class gametournament_FinalPhase:

    pass
class gametournament_Gamer:

    def __init__(self, firstName: str, lastName: str, pseudo: str, victories: int, matches: int, gametournament_Gamer11: "gametournament_FinalPhase" = None, gametournament_Gamer17: "gametournament_Pool" = None, gametournament_Gamer20: "gametournament_Pool" = None, gametournament_Gamer: "gametournament_Tournament" = None):
        self.firstName = firstName
        self.lastName = lastName
        self.pseudo = pseudo
        self.victories = victories
        self.matches = matches
        self.gametournament_Gamer11 = gametournament_Gamer11
        self.gametournament_Gamer17 = gametournament_Gamer17
        self.gametournament_Gamer20 = gametournament_Gamer20
        self.gametournament_Gamer = gametournament_Gamer
        
    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def pseudo(self) -> str:
        return self.__pseudo

    @pseudo.setter
    def pseudo(self, pseudo: str):
        self.__pseudo = pseudo

    @property
    def matches(self) -> int:
        return self.__matches

    @matches.setter
    def matches(self, matches: int):
        self.__matches = matches

    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def victories(self) -> int:
        return self.__victories

    @victories.setter
    def victories(self, victories: int):
        self.__victories = victories

    @property
    def gametournament_Gamer20(self):
        return self.__gametournament_Gamer20

    @gametournament_Gamer20.setter
    def gametournament_Gamer20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gametournament_Gamer__gametournament_Gamer20", None)
        self.__gametournament_Gamer20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gametournament_Pool19"):
                opp_val = getattr(old_value, "gametournament_Pool19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gametournament_Pool19"):
                opp_val = getattr(value, "gametournament_Pool19", None)
                if opp_val is None:
                    setattr(value, "gametournament_Pool19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gametournament_Gamer(self):
        return self.__gametournament_Gamer

    @gametournament_Gamer.setter
    def gametournament_Gamer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gametournament_Gamer__gametournament_Gamer", None)
        self.__gametournament_Gamer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gametournament_Tournament2"):
                opp_val = getattr(old_value, "gametournament_Tournament2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gametournament_Tournament2"):
                opp_val = getattr(value, "gametournament_Tournament2", None)
                if opp_val is None:
                    setattr(value, "gametournament_Tournament2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gametournament_Gamer11(self):
        return self.__gametournament_Gamer11

    @gametournament_Gamer11.setter
    def gametournament_Gamer11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gametournament_Gamer__gametournament_Gamer11", None)
        self.__gametournament_Gamer11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gametournament_FinalPhase10"):
                opp_val = getattr(old_value, "gametournament_FinalPhase10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gametournament_FinalPhase10"):
                opp_val = getattr(value, "gametournament_FinalPhase10", None)
                if opp_val is None:
                    setattr(value, "gametournament_FinalPhase10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gametournament_Gamer17(self):
        return self.__gametournament_Gamer17

    @gametournament_Gamer17.setter
    def gametournament_Gamer17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gametournament_Gamer__gametournament_Gamer17", None)
        self.__gametournament_Gamer17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gametournament_Pool16"):
                opp_val = getattr(old_value, "gametournament_Pool16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gametournament_Pool16"):
                opp_val = getattr(value, "gametournament_Pool16", None)
                if opp_val is None:
                    setattr(value, "gametournament_Pool16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class gametournament_Game:

    def __init__(self, name: str, type: str, gametournament_Game: "gametournament_Tournament" = None):
        self.name = name
        self.type = type
        self.gametournament_Game = gametournament_Game
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def gametournament_Game(self):
        return self.__gametournament_Game

    @gametournament_Game.setter
    def gametournament_Game(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gametournament_Game__gametournament_Game", None)
        self.__gametournament_Game = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gametournament_Tournament"):
                opp_val = getattr(old_value, "gametournament_Tournament", None)
                if opp_val == self:
                    setattr(old_value, "gametournament_Tournament", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gametournament_Tournament"):
                opp_val = getattr(value, "gametournament_Tournament", None)
                setattr(value, "gametournament_Tournament", self)

class gametournament_Pool:

    def __init__(self, gametournament_Pool: "gametournament_QualificationPhase" = None, gametournament_Pool16: set["gametournament_Gamer"] = None, gametournament_Pool19: set["gametournament_Gamer"] = None):
        self.gametournament_Pool = gametournament_Pool
        self.gametournament_Pool16 = gametournament_Pool16 if gametournament_Pool16 is not None else set()
        self.gametournament_Pool19 = gametournament_Pool19 if gametournament_Pool19 is not None else set()
        
    @property
    def gametournament_Pool16(self):
        return self.__gametournament_Pool16

    @gametournament_Pool16.setter
    def gametournament_Pool16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gametournament_Pool__gametournament_Pool16", None)
        self.__gametournament_Pool16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gametournament_Gamer17"):
                    opp_val = getattr(item, "gametournament_Gamer17", None)
                    
                    if opp_val == self:
                        setattr(item, "gametournament_Gamer17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gametournament_Gamer17"):
                    opp_val = getattr(item, "gametournament_Gamer17", None)
                    
                    setattr(item, "gametournament_Gamer17", self)
                    

    @property
    def gametournament_Pool(self):
        return self.__gametournament_Pool

    @gametournament_Pool.setter
    def gametournament_Pool(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gametournament_Pool__gametournament_Pool", None)
        self.__gametournament_Pool = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gametournament_QualificationPhase8"):
                opp_val = getattr(old_value, "gametournament_QualificationPhase8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gametournament_QualificationPhase8"):
                opp_val = getattr(value, "gametournament_QualificationPhase8", None)
                if opp_val is None:
                    setattr(value, "gametournament_QualificationPhase8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gametournament_Pool19(self):
        return self.__gametournament_Pool19

    @gametournament_Pool19.setter
    def gametournament_Pool19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gametournament_Pool__gametournament_Pool19", None)
        self.__gametournament_Pool19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gametournament_Gamer20"):
                    opp_val = getattr(item, "gametournament_Gamer20", None)
                    
                    if opp_val == self:
                        setattr(item, "gametournament_Gamer20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gametournament_Gamer20"):
                    opp_val = getattr(item, "gametournament_Gamer20", None)
                    
                    setattr(item, "gametournament_Gamer20", self)
                    

    def generateClassment(self):
        # TODO: Implement generateClassment method
        pass

class gametournament_Tournament:

    def __init__(self, name: str, location: str, startDate: date, endDate: date, prize: int, gametournament_Tournament: "gametournament_Game" = None, gametournament_Tournament2: set["gametournament_Gamer"] = None, gametournament_Tournament4: "gametournament_FinalPhase" = None, gametournament_Tournament6: "gametournament_QualificationPhase" = None):
        self.name = name
        self.location = location
        self.startDate = startDate
        self.endDate = endDate
        self.prize = prize
        self.gametournament_Tournament = gametournament_Tournament
        self.gametournament_Tournament2 = gametournament_Tournament2 if gametournament_Tournament2 is not None else set()
        self.gametournament_Tournament4 = gametournament_Tournament4
        self.gametournament_Tournament6 = gametournament_Tournament6
        
    @property
    def endDate(self) -> date:
        return self.__endDate

    @endDate.setter
    def endDate(self, endDate: date):
        self.__endDate = endDate

    @property
    def prize(self) -> int:
        return self.__prize

    @prize.setter
    def prize(self, prize: int):
        self.__prize = prize

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def startDate(self) -> date:
        return self.__startDate

    @startDate.setter
    def startDate(self, startDate: date):
        self.__startDate = startDate

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def gametournament_Tournament6(self):
        return self.__gametournament_Tournament6

    @gametournament_Tournament6.setter
    def gametournament_Tournament6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gametournament_Tournament__gametournament_Tournament6", None)
        self.__gametournament_Tournament6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gametournament_QualificationPhase"):
                opp_val = getattr(old_value, "gametournament_QualificationPhase", None)
                if opp_val == self:
                    setattr(old_value, "gametournament_QualificationPhase", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gametournament_QualificationPhase"):
                opp_val = getattr(value, "gametournament_QualificationPhase", None)
                setattr(value, "gametournament_QualificationPhase", self)

    @property
    def gametournament_Tournament2(self):
        return self.__gametournament_Tournament2

    @gametournament_Tournament2.setter
    def gametournament_Tournament2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gametournament_Tournament__gametournament_Tournament2", None)
        self.__gametournament_Tournament2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gametournament_Gamer"):
                    opp_val = getattr(item, "gametournament_Gamer", None)
                    
                    if opp_val == self:
                        setattr(item, "gametournament_Gamer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gametournament_Gamer"):
                    opp_val = getattr(item, "gametournament_Gamer", None)
                    
                    setattr(item, "gametournament_Gamer", self)
                    

    @property
    def gametournament_Tournament4(self):
        return self.__gametournament_Tournament4

    @gametournament_Tournament4.setter
    def gametournament_Tournament4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gametournament_Tournament__gametournament_Tournament4", None)
        self.__gametournament_Tournament4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gametournament_FinalPhase"):
                opp_val = getattr(old_value, "gametournament_FinalPhase", None)
                if opp_val == self:
                    setattr(old_value, "gametournament_FinalPhase", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gametournament_FinalPhase"):
                opp_val = getattr(value, "gametournament_FinalPhase", None)
                setattr(value, "gametournament_FinalPhase", self)

    @property
    def gametournament_Tournament(self):
        return self.__gametournament_Tournament

    @gametournament_Tournament.setter
    def gametournament_Tournament(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gametournament_Tournament__gametournament_Tournament", None)
        self.__gametournament_Tournament = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gametournament_Game"):
                opp_val = getattr(old_value, "gametournament_Game", None)
                if opp_val == self:
                    setattr(old_value, "gametournament_Game", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gametournament_Game"):
                opp_val = getattr(value, "gametournament_Game", None)
                setattr(value, "gametournament_Game", self)
