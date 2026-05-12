from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class BlackJack_Card:

    def __init__(self, value: int, color: str, rank: int, hand6: set["BlackJack_Hand"] = None):
        self.value = value
        self.color = color
        self.rank = rank
        self.hand6 = hand6 if hand6 is not None else set()
        
        pass
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def rank(self):
        return self.__rank
    @rank.setter
    def rank(self, rank: int):
        self.__rank = rank

    @property
    def hand6(self):
        return self.__hand6
    @hand6.setter
    def hand6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BlackJack_Card__hand6", None)
        self.__hand6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "card7"):
                    opp_val = getattr(item, "card7", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "card7"):
                    opp_val = getattr(item, "card7", None)
                    
                    if opp_val is None:
                        setattr(item, "card7", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class BlackJack_Game:

    def __init__(self, win_loose: bool, house0: "BlackJack_House" = None, player2: set["BlackJack_Player"] = None):
        self.win_loose = win_loose
        self.house0 = house0
        self.player2 = player2 if player2 is not None else set()
        
        pass
    @property
    def win_loose(self):
        return self.__win_loose
    @win_loose.setter
    def win_loose(self, win_loose: bool):
        self.__win_loose = win_loose

    @property
    def player2(self):
        return self.__player2
    @player2.setter
    def player2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BlackJack_Game__player2", None)
        self.__player2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Game_Player_13"):
                    opp_val = getattr(item, "Game_Player_13", None)
                    
                    if opp_val == self:
                        setattr(item, "Game_Player_13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Game_Player_13"):
                    opp_val = getattr(item, "Game_Player_13", None)
                    
                    setattr(item, "Game_Player_13", self)
                    

    @property
    def house0(self):
        return self.__house0
    @house0.setter
    def house0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BlackJack_Game__house0", None)
        self.__house0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game1"):
                opp_val = getattr(old_value, "game1", None)
                if opp_val == self:
                    setattr(old_value, "game1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game1"):
                opp_val = getattr(value, "game1", None)
                setattr(value, "game1", self)



class BlackJack_House:

    pass


class BlackJack_Player:

    def __init__(self, limit: int, Game_Player_13: "BlackJack_Game" = None):
        self.limit = limit
        self.Game_Player_13 = Game_Player_13
        
        pass
    @property
    def limit(self):
        return self.__limit
    @limit.setter
    def limit(self, limit: int):
        self.__limit = limit

    @property
    def Game_Player_13(self):
        return self.__Game_Player_13
    @Game_Player_13.setter
    def Game_Player_13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BlackJack_Player__Game_Player_13", None)
        self.__Game_Player_13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player2"):
                opp_val = getattr(old_value, "player2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player2"):
                opp_val = getattr(value, "player2", None)
                if opp_val is None:
                    setattr(value, "player2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class BlackJack_Deck:

    def __init__(self, nextItem: int, game4: "BlackJack_House" = None):
        self.nextItem = nextItem
        self.game4 = game4
        
        pass
    @property
    def nextItem(self):
        return self.__nextItem
    @nextItem.setter
    def nextItem(self, nextItem: int):
        self.__nextItem = nextItem

    @property
    def game4(self):
        return self.__game4
    @game4.setter
    def game4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BlackJack_Deck__game4", None)
        self.__game4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deck5"):
                opp_val = getattr(old_value, "deck5", None)
                if opp_val == self:
                    setattr(old_value, "deck5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deck5"):
                opp_val = getattr(value, "deck5", None)
                setattr(value, "deck5", self)



class BlackJack_Generic_Player:

    def __init__(self, valueOfHand: int):
        self.valueOfHand = valueOfHand
        
        pass
    @property
    def valueOfHand(self):
        return self.__valueOfHand
    @valueOfHand.setter
    def valueOfHand(self, valueOfHand: int):
        self.__valueOfHand = valueOfHand



class BlackJack_Hand:

    def __init__(self, ArrayList: BlackJack_Card, card7: set["BlackJack_Card"] = None):
        self.ArrayList = ArrayList
        self.card7 = card7 if card7 is not None else set()
        
        pass
    @property
    def ArrayList(self):
        return self.__ArrayList
    @ArrayList.setter
    def ArrayList(self, ArrayList: BlackJack_Card):
        self.__ArrayList = ArrayList

    @property
    def card7(self):
        return self.__card7
    @card7.setter
    def card7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BlackJack_Hand__card7", None)
        self.__card7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hand6"):
                    opp_val = getattr(item, "hand6", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hand6"):
                    opp_val = getattr(item, "hand6", None)
                    
                    if opp_val is None:
                        setattr(item, "hand6", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

