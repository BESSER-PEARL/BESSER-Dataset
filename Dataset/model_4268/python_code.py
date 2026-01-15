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

class bowling_League:

    def __init__(self, name: str, bowling_League: set["bowling_Player"] = None):
        self.name = name
        self.bowling_League = bowling_League if bowling_League is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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

    def __init__(self, name: str, dateOfBirth: date, height: float, isProfessional: bool, bowling_Player: "bowling_League" = None, bowling_Player5: "bowling_Game" = None):
        self.name = name
        self.dateOfBirth = dateOfBirth
        self.height = height
        self.isProfessional = isProfessional
        self.bowling_Player = bowling_Player
        self.bowling_Player5 = bowling_Player5
        
    @property
    def dateOfBirth(self) -> date:
        return self.__dateOfBirth

    @dateOfBirth.setter
    def dateOfBirth(self, dateOfBirth: date):
        self.__dateOfBirth = dateOfBirth

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
    def height(self) -> float:
        return self.__height

    @height.setter
    def height(self, height: float):
        self.__height = height

    @property
    def bowling_Player5(self):
        return self.__bowling_Player5

    @bowling_Player5.setter
    def bowling_Player5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Player__bowling_Player5", None)
        self.__bowling_Player5 = value
        
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

class bowling_Game:

    def __init__(self, frames: int, Game: "bowling_Matchup" = None, games: "bowling_Matchup" = None, bowling_Game: "bowling_Player" = None):
        self.frames = frames
        self.Game = Game
        self.games = games
        self.bowling_Game = bowling_Game
        
    @property
    def frames(self) -> int:
        return self.__frames

    @frames.setter
    def frames(self, frames: int):
        self.__frames = frames

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
            if hasattr(old_value, "bowling_Player5"):
                opp_val = getattr(old_value, "bowling_Player5", None)
                if opp_val == self:
                    setattr(old_value, "bowling_Player5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bowling_Player5"):
                opp_val = getattr(value, "bowling_Player5", None)
                setattr(value, "bowling_Player5", self)

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

class bowling_Matchup:

    def __init__(self, name: str, bowling_Matchup: "bowling_Tournament" = None, matchup: set["bowling_Game"] = None, Matchup: "bowling_Game" = None):
        self.name = name
        self.bowling_Matchup = bowling_Matchup
        self.matchup = matchup if matchup is not None else set()
        self.Matchup = Matchup
        
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
                    

class bowling_Tournament:

    def __init__(self, name: str, type: str, bowling_Tournament: set["bowling_Matchup"] = None):
        self.name = name
        self.type = type
        self.bowling_Tournament = bowling_Tournament if bowling_Tournament is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
                    
