from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class TournamentType(Enum):
    Amateur = "Amateur"
    Pro = "Pro"


############################################
# Definition of Classes
############################################

class bowling_Tournament:

    def __init__(self, title: str, type: str, tournament17: "bowling_Playerlist" = None, Tournament: "bowling_Matchup" = None, Tournament13: "bowling_Playerlist" = None, tournament: set["bowling_Matchup"] = None):
        self.title = title
        self.type = type
        self.tournament17 = tournament17
        self.Tournament = Tournament
        self.Tournament13 = Tournament13
        self.tournament = tournament if tournament is not None else set()
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def tournament(self):
        return self.__tournament

    @tournament.setter
    def tournament(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Tournament__tournament", None)
        self.__tournament = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Matchup15"):
                    opp_val = getattr(item, "Matchup15", None)
                    
                    if opp_val == self:
                        setattr(item, "Matchup15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Matchup15"):
                    opp_val = getattr(item, "Matchup15", None)
                    
                    setattr(item, "Matchup15", self)
                    

    @property
    def Tournament(self):
        return self.__Tournament

    @Tournament.setter
    def Tournament(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Tournament__Tournament", None)
        self.__Tournament = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "matchups"):
                opp_val = getattr(old_value, "matchups", None)
                if opp_val == self:
                    setattr(old_value, "matchups", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "matchups"):
                opp_val = getattr(value, "matchups", None)
                setattr(value, "matchups", self)

    @property
    def Tournament13(self):
        return self.__Tournament13

    @Tournament13.setter
    def Tournament13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Tournament__Tournament13", None)
        self.__Tournament13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "playerlist12"):
                opp_val = getattr(old_value, "playerlist12", None)
                if opp_val == self:
                    setattr(old_value, "playerlist12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "playerlist12"):
                opp_val = getattr(value, "playerlist12", None)
                setattr(value, "playerlist12", self)

    @property
    def tournament17(self):
        return self.__tournament17

    @tournament17.setter
    def tournament17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Tournament__tournament17", None)
        self.__tournament17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Playerlist18"):
                opp_val = getattr(old_value, "Playerlist18", None)
                if opp_val == self:
                    setattr(old_value, "Playerlist18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Playerlist18"):
                opp_val = getattr(value, "Playerlist18", None)
                setattr(value, "Playerlist18", self)

class bowling_Matchup:

    pass
class bowling_Player:

    def __init__(self, streetnumber: int, city: str, dateOfBirth: date, height: float, isProfessional: bool, firstname: str, lastname: str, street: str, player: set["bowling_Game"] = None, player2: "bowling_Playerlist" = None, Player: "bowling_Game" = None, Player10: "bowling_Playerlist" = None):
        self.streetnumber = streetnumber
        self.city = city
        self.dateOfBirth = dateOfBirth
        self.height = height
        self.isProfessional = isProfessional
        self.firstname = firstname
        self.lastname = lastname
        self.street = street
        self.player = player if player is not None else set()
        self.player2 = player2
        self.Player = Player
        self.Player10 = Player10
        
    @property
    def lastname(self) -> str:
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname

    @property
    def firstname(self) -> str:
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname

    @property
    def height(self) -> float:
        return self.__height

    @height.setter
    def height(self, height: float):
        self.__height = height

    @property
    def isProfessional(self) -> bool:
        return self.__isProfessional

    @isProfessional.setter
    def isProfessional(self, isProfessional: bool):
        self.__isProfessional = isProfessional

    @property
    def street(self) -> str:
        return self.__street

    @street.setter
    def street(self, street: str):
        self.__street = street

    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def dateOfBirth(self) -> date:
        return self.__dateOfBirth

    @dateOfBirth.setter
    def dateOfBirth(self, dateOfBirth: date):
        self.__dateOfBirth = dateOfBirth

    @property
    def streetnumber(self) -> int:
        return self.__streetnumber

    @streetnumber.setter
    def streetnumber(self, streetnumber: int):
        self.__streetnumber = streetnumber

    @property
    def Player(self):
        return self.__Player

    @Player.setter
    def Player(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Player__Player", None)
        self.__Player = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game"):
                opp_val = getattr(old_value, "game", None)
                if opp_val == self:
                    setattr(old_value, "game", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game"):
                opp_val = getattr(value, "game", None)
                setattr(value, "game", self)

    @property
    def player2(self):
        return self.__player2

    @player2.setter
    def player2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Player__player2", None)
        self.__player2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Playerlist"):
                opp_val = getattr(old_value, "Playerlist", None)
                if opp_val == self:
                    setattr(old_value, "Playerlist", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Playerlist"):
                opp_val = getattr(value, "Playerlist", None)
                setattr(value, "Playerlist", self)

    @property
    def player(self):
        return self.__player

    @player.setter
    def player(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Player__player", None)
        self.__player = value if value is not None else set()
        
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
    def Player10(self):
        return self.__Player10

    @Player10.setter
    def Player10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Player__Player10", None)
        self.__Player10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "playerlist"):
                opp_val = getattr(old_value, "playerlist", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "playerlist"):
                opp_val = getattr(value, "playerlist", None)
                if opp_val is None:
                    setattr(value, "playerlist", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bowling_Playerlist:

    def __init__(self, name: str, Playerlist: "bowling_Player" = None, Playerlist18: "bowling_Tournament" = None, playerlist: set["bowling_Player"] = None, playerlist12: "bowling_Tournament" = None):
        self.name = name
        self.Playerlist = Playerlist
        self.Playerlist18 = Playerlist18
        self.playerlist = playerlist if playerlist is not None else set()
        self.playerlist12 = playerlist12
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Playerlist18(self):
        return self.__Playerlist18

    @Playerlist18.setter
    def Playerlist18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Playerlist__Playerlist18", None)
        self.__Playerlist18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tournament17"):
                opp_val = getattr(old_value, "tournament17", None)
                if opp_val == self:
                    setattr(old_value, "tournament17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tournament17"):
                opp_val = getattr(value, "tournament17", None)
                setattr(value, "tournament17", self)

    @property
    def Playerlist(self):
        return self.__Playerlist

    @Playerlist.setter
    def Playerlist(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Playerlist__Playerlist", None)
        self.__Playerlist = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player2"):
                opp_val = getattr(old_value, "player2", None)
                if opp_val == self:
                    setattr(old_value, "player2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player2"):
                opp_val = getattr(value, "player2", None)
                setattr(value, "player2", self)

    @property
    def playerlist12(self):
        return self.__playerlist12

    @playerlist12.setter
    def playerlist12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Playerlist__playerlist12", None)
        self.__playerlist12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Tournament13"):
                opp_val = getattr(old_value, "Tournament13", None)
                if opp_val == self:
                    setattr(old_value, "Tournament13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Tournament13"):
                opp_val = getattr(value, "Tournament13", None)
                setattr(value, "Tournament13", self)

    @property
    def playerlist(self):
        return self.__playerlist

    @playerlist.setter
    def playerlist(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Playerlist__playerlist", None)
        self.__playerlist = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Player10"):
                    opp_val = getattr(item, "Player10", None)
                    
                    if opp_val == self:
                        setattr(item, "Player10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Player10"):
                    opp_val = getattr(item, "Player10", None)
                    
                    setattr(item, "Player10", self)
                    

class bowling_Game:

    def __init__(self, date: date, frames: int, Game: "bowling_Player" = None, game: "bowling_Player" = None, game5: "bowling_Matchup" = None, Game7: "bowling_Matchup" = None):
        self.date = date
        self.frames = frames
        self.Game = Game
        self.game = game
        self.game5 = game5
        self.Game7 = Game7
        
    @property
    def frames(self) -> int:
        return self.__frames

    @frames.setter
    def frames(self, frames: int):
        self.__frames = frames

    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def game(self):
        return self.__game

    @game.setter
    def game(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Game__game", None)
        self.__game = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Player"):
                opp_val = getattr(old_value, "Player", None)
                if opp_val == self:
                    setattr(old_value, "Player", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Player"):
                opp_val = getattr(value, "Player", None)
                setattr(value, "Player", self)

    @property
    def Game7(self):
        return self.__Game7

    @Game7.setter
    def Game7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Game__Game7", None)
        self.__Game7 = value
        
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
    def Game(self):
        return self.__Game

    @Game.setter
    def Game(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Game__Game", None)
        self.__Game = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player"):
                opp_val = getattr(old_value, "player", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player"):
                opp_val = getattr(value, "player", None)
                if opp_val is None:
                    setattr(value, "player", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def game5(self):
        return self.__game5

    @game5.setter
    def game5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bowling_Game__game5", None)
        self.__game5 = value
        
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
