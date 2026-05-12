from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################










class SUIT_external:

    pass


class RANK_external:

    pass


class Role_external:

    pass


class PlayerView:

    pass


class PokerTableView:

    pass


class StandardDeck:

    pass


class T:

    pass


class GameRound:

    pass


class __abstract___BaseDeck(ABC):

    pass


class PokerTable:

    pass


class PlayCard:

    pass


class Player:

    def __init__(self, stack: int, bid: int, role12: set["Role_external"] = None, pokerTable19: "PokerTable" = None, kortti0: set["PlayCard"] = None, Table3: "PokerTable" = None):
        self.stack = stack
        self.bid = bid
        self.role12 = role12 if role12 is not None else set()
        self.pokerTable19 = pokerTable19
        self.kortti0 = kortti0 if kortti0 is not None else set()
        self.Table3 = Table3
        
        pass
    @property
    def stack(self):
        return self.__stack
    @stack.setter
    def stack(self, stack: int):
        self.__stack = stack

    @property
    def bid(self):
        return self.__bid
    @bid.setter
    def bid(self, bid: int):
        self.__bid = bid

    @property
    def role12(self):
        return self.__role12
    @role12.setter
    def role12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__role12", None)
        self.__role12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "player13"):
                    opp_val = getattr(item, "player13", None)
                    
                    if opp_val == self:
                        setattr(item, "player13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "player13"):
                    opp_val = getattr(item, "player13", None)
                    
                    setattr(item, "player13", self)
                    

    @property
    def pokerTable19(self):
        return self.__pokerTable19
    @pokerTable19.setter
    def pokerTable19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__pokerTable19", None)
        self.__pokerTable19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Active18"):
                opp_val = getattr(old_value, "Active18", None)
                if opp_val == self:
                    setattr(old_value, "Active18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Active18"):
                opp_val = getattr(value, "Active18", None)
                setattr(value, "Active18", self)

    @property
    def Table3(self):
        return self.__Table3
    @Table3.setter
    def Table3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__Table3", None)
        self.__Table3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pelaaja2"):
                opp_val = getattr(old_value, "pelaaja2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pelaaja2"):
                opp_val = getattr(value, "pelaaja2", None)
                if opp_val is None:
                    setattr(value, "pelaaja2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def kortti0(self):
        return self.__kortti0
    @kortti0.setter
    def kortti0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__kortti0", None)
        self.__kortti0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pelaaja1"):
                    opp_val = getattr(item, "pelaaja1", None)
                    
                    if opp_val == self:
                        setattr(item, "pelaaja1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pelaaja1"):
                    opp_val = getattr(item, "pelaaja1", None)
                    
                    setattr(item, "pelaaja1", self)
                    

