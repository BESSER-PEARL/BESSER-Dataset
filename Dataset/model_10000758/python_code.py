from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Theme(Enum):
    pass
class CarProperties(Enum):
    pass
class TankProperties(Enum):
    pass

############################################
# Definition of Classes
############################################










class Score:

    pass


class Theme1:

    def __init__(self, name: str, year: int, deck6: set["Deck"] = None, game12: "Game" = None):
        self.name = name
        self.year = year
        self.deck6 = deck6 if deck6 is not None else set()
        self.game12 = game12
        
        pass
    @property
    def year(self):
        return self.__year
    @year.setter
    def year(self, year: int):
        self.__year = year

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def game12(self):
        return self.__game12
    @game12.setter
    def game12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Theme1__game12", None)
        self.__game12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "theme13"):
                opp_val = getattr(old_value, "theme13", None)
                if opp_val == self:
                    setattr(old_value, "theme13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "theme13"):
                opp_val = getattr(value, "theme13", None)
                setattr(value, "theme13", self)

    @property
    def deck6(self):
        return self.__deck6
    @deck6.setter
    def deck6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Theme1__deck6", None)
        self.__deck6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "theme7"):
                    opp_val = getattr(item, "theme7", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "theme7"):
                    opp_val = getattr(item, "theme7", None)
                    
                    if opp_val is None:
                        setattr(item, "theme7", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Card:

    def __init__(self, theme: Theme, ID: str, group9: set["Group"] = None):
        self.theme = theme
        self.ID = ID
        self.group9 = group9 if group9 is not None else set()
        
        pass
    @property
    def theme(self):
        return self.__theme
    @theme.setter
    def theme(self, theme: Theme):
        self.__theme = theme

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def group9(self):
        return self.__group9
    @group9.setter
    def group9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Card__group9", None)
        self.__group9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "card8"):
                    opp_val = getattr(item, "card8", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "card8"):
                    opp_val = getattr(item, "card8", None)
                    
                    if opp_val is None:
                        setattr(item, "card8", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Player(ABC):

    def __init__(self, name: str, avatar0: "Avatar" = None, games3: set["Game"] = None, score10: "Score" = None):
        self.name = name
        self.avatar0 = avatar0
        self.games3 = games3 if games3 is not None else set()
        self.score10 = score10
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def avatar0(self):
        return self.__avatar0
    @avatar0.setter
    def avatar0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__avatar0", None)
        self.__avatar0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "players1"):
                opp_val = getattr(old_value, "players1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "players1"):
                opp_val = getattr(value, "players1", None)
                if opp_val is None:
                    setattr(value, "players1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def score10(self):
        return self.__score10
    @score10.setter
    def score10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__score10", None)
        self.__score10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player11"):
                opp_val = getattr(old_value, "player11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player11"):
                opp_val = getattr(value, "player11", None)
                if opp_val is None:
                    setattr(value, "player11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def games3(self):
        return self.__games3
    @games3.setter
    def games3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__games3", None)
        self.__games3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "players2"):
                    opp_val = getattr(item, "players2", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "players2"):
                    opp_val = getattr(item, "players2", None)
                    
                    if opp_val is None:
                        setattr(item, "players2", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Game(ABC):

    def __init__(self, name: str, players2: set["Player"] = None, theme13: "Theme1" = None):
        self.name = name
        self.players2 = players2 if players2 is not None else set()
        self.theme13 = theme13
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def players2(self):
        return self.__players2
    @players2.setter
    def players2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Game__players2", None)
        self.__players2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "games3"):
                    opp_val = getattr(item, "games3", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "games3"):
                    opp_val = getattr(item, "games3", None)
                    
                    if opp_val is None:
                        setattr(item, "games3", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def theme13(self):
        return self.__theme13
    @theme13.setter
    def theme13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Game__theme13", None)
        self.__theme13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game12"):
                opp_val = getattr(old_value, "game12", None)
                if opp_val == self:
                    setattr(old_value, "game12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game12"):
                opp_val = getattr(value, "game12", None)
                setattr(value, "game12", self)



class Avatar:

    pass


class Group:

    def __init__(self, name: str, ID: int, deck5: set["Deck"] = None, card8: set["Card"] = None):
        self.name = name
        self.ID = ID
        self.deck5 = deck5 if deck5 is not None else set()
        self.card8 = card8 if card8 is not None else set()
        
        pass
    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def card8(self):
        return self.__card8
    @card8.setter
    def card8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Group__card8", None)
        self.__card8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "group9"):
                    opp_val = getattr(item, "group9", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "group9"):
                    opp_val = getattr(item, "group9", None)
                    
                    if opp_val is None:
                        setattr(item, "group9", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def deck5(self):
        return self.__deck5
    @deck5.setter
    def deck5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Group__deck5", None)
        self.__deck5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "group4"):
                    opp_val = getattr(item, "group4", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "group4"):
                    opp_val = getattr(item, "group4", None)
                    
                    if opp_val is None:
                        setattr(item, "group4", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Deck:

    pass
