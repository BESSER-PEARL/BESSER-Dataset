from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class TournamentType(Enum):
    Pro = "Pro"
    Amateur = "Amateur"


############################################
# Definition of Classes
############################################

class bowling_Game:

    def __init__(self, frames: int, bowling_Game5: "bowling_Player" = None, bowling_Game: "bowling_Matchup" = None):
        self.frames = frames
        self.bowling_Game5 = bowling_Game5
        self.bowling_Game = bowling_Game
        
    @property
    def frames(self) -> int:
        return self.__frames

    @frames.setter
    def frames(self, frames: int):
        self.__frames = frames

    @property
    def bowling_Game5(self):
        return self.__bowling_Game5

    @bowling_Game5.setter
    def bowling_Game5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Game__bowling_Game5", None)
        self.__bowling_Game5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bowling_Player6"):
                opp_val = getattr(old_value, "bowling_Player6", None)
                if opp_val == self:
                    setattr(old_value, "bowling_Player6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bowling_Player6"):
                opp_val = getattr(value, "bowling_Player6", None)
                setattr(value, "bowling_Player6", self)

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
            if hasattr(old_value, "bowling_Matchup3"):
                opp_val = getattr(old_value, "bowling_Matchup3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bowling_Matchup3"):
                opp_val = getattr(value, "bowling_Matchup3", None)
                if opp_val is None:
                    setattr(value, "bowling_Matchup3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bowling_Lane:

    def __init__(self, number: int, bowling_Lane: "bowling_Alley" = None):
        self.number = number
        self.bowling_Lane = bowling_Lane
        
    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def bowling_Lane(self):
        return self.__bowling_Lane

    @bowling_Lane.setter
    def bowling_Lane(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Lane__bowling_Lane", None)
        self.__bowling_Lane = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bowling_Alley13"):
                opp_val = getattr(old_value, "bowling_Alley13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bowling_Alley13"):
                opp_val = getattr(value, "bowling_Alley13", None)
                if opp_val is None:
                    setattr(value, "bowling_Alley13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bowling_Alley:

    def __init__(self, name: str, bowling_Alley: set["bowling_League"] = None, bowling_Alley10: set["bowling_Tournament"] = None, bowling_Alley13: set["bowling_Lane"] = None):
        self.name = name
        self.bowling_Alley = bowling_Alley if bowling_Alley is not None else set()
        self.bowling_Alley10 = bowling_Alley10 if bowling_Alley10 is not None else set()
        self.bowling_Alley13 = bowling_Alley13 if bowling_Alley13 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bowling_Alley10(self):
        return self.__bowling_Alley10

    @bowling_Alley10.setter
    def bowling_Alley10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Alley__bowling_Alley10", None)
        self.__bowling_Alley10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bowling_Tournament11"):
                    opp_val = getattr(item, "bowling_Tournament11", None)
                    
                    if opp_val == self:
                        setattr(item, "bowling_Tournament11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bowling_Tournament11"):
                    opp_val = getattr(item, "bowling_Tournament11", None)
                    
                    setattr(item, "bowling_Tournament11", self)
                    

    @property
    def bowling_Alley13(self):
        return self.__bowling_Alley13

    @bowling_Alley13.setter
    def bowling_Alley13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Alley__bowling_Alley13", None)
        self.__bowling_Alley13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bowling_Lane"):
                    opp_val = getattr(item, "bowling_Lane", None)
                    
                    if opp_val == self:
                        setattr(item, "bowling_Lane", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bowling_Lane"):
                    opp_val = getattr(item, "bowling_Lane", None)
                    
                    setattr(item, "bowling_Lane", self)
                    

    @property
    def bowling_Alley(self):
        return self.__bowling_Alley

    @bowling_Alley.setter
    def bowling_Alley(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Alley__bowling_Alley", None)
        self.__bowling_Alley = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bowling_League8"):
                    opp_val = getattr(item, "bowling_League8", None)
                    
                    if opp_val == self:
                        setattr(item, "bowling_League8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bowling_League8"):
                    opp_val = getattr(item, "bowling_League8", None)
                    
                    setattr(item, "bowling_League8", self)
                    

class bowling_Matchup:

    def __init__(self, name: str, bowling_Matchup: "bowling_Tournament" = None, bowling_Matchup3: set["bowling_Game"] = None):
        self.name = name
        self.bowling_Matchup = bowling_Matchup
        self.bowling_Matchup3 = bowling_Matchup3 if bowling_Matchup3 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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

    @property
    def bowling_Matchup3(self):
        return self.__bowling_Matchup3

    @bowling_Matchup3.setter
    def bowling_Matchup3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Matchup__bowling_Matchup3", None)
        self.__bowling_Matchup3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bowling_Game"):
                    opp_val = getattr(item, "bowling_Game", None)
                    
                    if opp_val == self:
                        setattr(item, "bowling_Game", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bowling_Game"):
                    opp_val = getattr(item, "bowling_Game", None)
                    
                    setattr(item, "bowling_Game", self)
                    

class bowling_Tournament:

    def __init__(self, name: str, type: str, bowling_Tournament: set["bowling_Matchup"] = None, bowling_Tournament11: "bowling_Alley" = None):
        self.name = name
        self.type = type
        self.bowling_Tournament = bowling_Tournament if bowling_Tournament is not None else set()
        self.bowling_Tournament11 = bowling_Tournament11
        
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
    def bowling_Tournament11(self):
        return self.__bowling_Tournament11

    @bowling_Tournament11.setter
    def bowling_Tournament11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Tournament__bowling_Tournament11", None)
        self.__bowling_Tournament11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bowling_Alley10"):
                opp_val = getattr(old_value, "bowling_Alley10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bowling_Alley10"):
                opp_val = getattr(value, "bowling_Alley10", None)
                if opp_val is None:
                    setattr(value, "bowling_Alley10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bowling_League:

    def __init__(self, name: str, bowling_League: set["bowling_Player"] = None, bowling_League8: "bowling_Alley" = None):
        self.name = name
        self.bowling_League = bowling_League if bowling_League is not None else set()
        self.bowling_League8 = bowling_League8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bowling_League8(self):
        return self.__bowling_League8

    @bowling_League8.setter
    def bowling_League8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_League__bowling_League8", None)
        self.__bowling_League8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bowling_Alley"):
                opp_val = getattr(old_value, "bowling_Alley", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bowling_Alley"):
                opp_val = getattr(value, "bowling_Alley", None)
                if opp_val is None:
                    setattr(value, "bowling_Alley", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
                    

class bowling_Player:

    def __init__(self, name: str, dateOfBirth: date, height: float, isProfessional: bool, bowling_Player: "bowling_League" = None, bowling_Player6: "bowling_Game" = None):
        self.name = name
        self.dateOfBirth = dateOfBirth
        self.height = height
        self.isProfessional = isProfessional
        self.bowling_Player = bowling_Player
        self.bowling_Player6 = bowling_Player6
        
    @property
    def height(self) -> float:
        return self.__height

    @height.setter
    def height(self, height: float):
        self.__height = height

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isProfessional(self) -> bool:
        return self.__isProfessional

    @isProfessional.setter
    def isProfessional(self, isProfessional: bool):
        self.__isProfessional = isProfessional

    @property
    def dateOfBirth(self) -> date:
        return self.__dateOfBirth

    @dateOfBirth.setter
    def dateOfBirth(self, dateOfBirth: date):
        self.__dateOfBirth = dateOfBirth

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
            if hasattr(old_value, "bowling_Game5"):
                opp_val = getattr(old_value, "bowling_Game5", None)
                if opp_val == self:
                    setattr(old_value, "bowling_Game5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bowling_Game5"):
                opp_val = getattr(value, "bowling_Game5", None)
                setattr(value, "bowling_Game5", self)
