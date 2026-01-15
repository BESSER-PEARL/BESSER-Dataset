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

class bowlingTournament_Matchup:

    pass
class bowlingTournament_Tournament:

    def __init__(self, type: str, bowlingTournament_Tournament: set["bowlingTournament_Matchup"] = None, bowlingTournament_Tournament3: set["bowlingTournament_League"] = None):
        self.type = type
        self.bowlingTournament_Tournament = bowlingTournament_Tournament if bowlingTournament_Tournament is not None else set()
        self.bowlingTournament_Tournament3 = bowlingTournament_Tournament3 if bowlingTournament_Tournament3 is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def bowlingTournament_Tournament(self):
        return self.__bowlingTournament_Tournament

    @bowlingTournament_Tournament.setter
    def bowlingTournament_Tournament(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowlingTournament_Tournament__bowlingTournament_Tournament", None)
        self.__bowlingTournament_Tournament = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bowlingTournament_Matchup"):
                    opp_val = getattr(item, "bowlingTournament_Matchup", None)
                    
                    if opp_val == self:
                        setattr(item, "bowlingTournament_Matchup", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bowlingTournament_Matchup"):
                    opp_val = getattr(item, "bowlingTournament_Matchup", None)
                    
                    setattr(item, "bowlingTournament_Matchup", self)
                    

    @property
    def bowlingTournament_Tournament3(self):
        return self.__bowlingTournament_Tournament3

    @bowlingTournament_Tournament3.setter
    def bowlingTournament_Tournament3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowlingTournament_Tournament__bowlingTournament_Tournament3", None)
        self.__bowlingTournament_Tournament3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bowlingTournament_League4"):
                    opp_val = getattr(item, "bowlingTournament_League4", None)
                    
                    if opp_val == self:
                        setattr(item, "bowlingTournament_League4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bowlingTournament_League4"):
                    opp_val = getattr(item, "bowlingTournament_League4", None)
                    
                    setattr(item, "bowlingTournament_League4", self)
                    

class bowlingTournament_Player:

    def __init__(self, name: str, dateOfBirth: date, height: float, isProfessional: bool, bowlingTournament_Player7: "bowlingTournament_Game" = None, bowlingTournament_Player: "bowlingTournament_League" = None):
        self.name = name
        self.dateOfBirth = dateOfBirth
        self.height = height
        self.isProfessional = isProfessional
        self.bowlingTournament_Player7 = bowlingTournament_Player7
        self.bowlingTournament_Player = bowlingTournament_Player
        
    @property
    def height(self) -> float:
        return self.__height

    @height.setter
    def height(self, height: float):
        self.__height = height

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
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bowlingTournament_Player7(self):
        return self.__bowlingTournament_Player7

    @bowlingTournament_Player7.setter
    def bowlingTournament_Player7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowlingTournament_Player__bowlingTournament_Player7", None)
        self.__bowlingTournament_Player7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bowlingTournament_Game"):
                opp_val = getattr(old_value, "bowlingTournament_Game", None)
                if opp_val == self:
                    setattr(old_value, "bowlingTournament_Game", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bowlingTournament_Game"):
                opp_val = getattr(value, "bowlingTournament_Game", None)
                setattr(value, "bowlingTournament_Game", self)

    @property
    def bowlingTournament_Player(self):
        return self.__bowlingTournament_Player

    @bowlingTournament_Player.setter
    def bowlingTournament_Player(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowlingTournament_Player__bowlingTournament_Player", None)
        self.__bowlingTournament_Player = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bowlingTournament_League"):
                opp_val = getattr(old_value, "bowlingTournament_League", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bowlingTournament_League"):
                opp_val = getattr(value, "bowlingTournament_League", None)
                if opp_val is None:
                    setattr(value, "bowlingTournament_League", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bowlingTournament_Game:

    def __init__(self, frames: int, Game: "bowlingTournament_Matchup" = None, bowlingTournament_Game: "bowlingTournament_Player" = None, games: "bowlingTournament_Matchup" = None):
        self.frames = frames
        self.Game = Game
        self.bowlingTournament_Game = bowlingTournament_Game
        self.games = games
        
    @property
    def frames(self) -> int:
        return self.__frames

    @frames.setter
    def frames(self, frames: int):
        self.__frames = frames

    @property
    def games(self):
        return self.__games

    @games.setter
    def games(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowlingTournament_Game__games", None)
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
    def Game(self):
        return self.__Game

    @Game.setter
    def Game(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowlingTournament_Game__Game", None)
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
    def bowlingTournament_Game(self):
        return self.__bowlingTournament_Game

    @bowlingTournament_Game.setter
    def bowlingTournament_Game(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowlingTournament_Game__bowlingTournament_Game", None)
        self.__bowlingTournament_Game = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bowlingTournament_Player7"):
                opp_val = getattr(old_value, "bowlingTournament_Player7", None)
                if opp_val == self:
                    setattr(old_value, "bowlingTournament_Player7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bowlingTournament_Player7"):
                opp_val = getattr(value, "bowlingTournament_Player7", None)
                setattr(value, "bowlingTournament_Player7", self)

class bowlingTournament_League:

    def __init__(self, name: str, bowlingTournament_League: set["bowlingTournament_Player"] = None, bowlingTournament_League4: "bowlingTournament_Tournament" = None):
        self.name = name
        self.bowlingTournament_League = bowlingTournament_League if bowlingTournament_League is not None else set()
        self.bowlingTournament_League4 = bowlingTournament_League4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bowlingTournament_League(self):
        return self.__bowlingTournament_League

    @bowlingTournament_League.setter
    def bowlingTournament_League(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowlingTournament_League__bowlingTournament_League", None)
        self.__bowlingTournament_League = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bowlingTournament_Player"):
                    opp_val = getattr(item, "bowlingTournament_Player", None)
                    
                    if opp_val == self:
                        setattr(item, "bowlingTournament_Player", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bowlingTournament_Player"):
                    opp_val = getattr(item, "bowlingTournament_Player", None)
                    
                    setattr(item, "bowlingTournament_Player", self)
                    

    @property
    def bowlingTournament_League4(self):
        return self.__bowlingTournament_League4

    @bowlingTournament_League4.setter
    def bowlingTournament_League4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowlingTournament_League__bowlingTournament_League4", None)
        self.__bowlingTournament_League4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bowlingTournament_Tournament3"):
                opp_val = getattr(old_value, "bowlingTournament_Tournament3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bowlingTournament_Tournament3"):
                opp_val = getattr(value, "bowlingTournament_Tournament3", None)
                if opp_val is None:
                    setattr(value, "bowlingTournament_Tournament3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
