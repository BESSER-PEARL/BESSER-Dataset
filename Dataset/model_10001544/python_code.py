from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Integer_external:

    pass


class BlackjackGame:

    pass


class Player:

    def __init__(self, name: str, blackjackGame3: "BlackjackGame" = None, hand6: "Hand" = None):
        self.name = name
        self.blackjackGame3 = blackjackGame3
        self.hand6 = hand6
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def hand6(self):
        return self.__hand6
    @hand6.setter
    def hand6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__hand6", None)
        self.__hand6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player7"):
                opp_val = getattr(old_value, "player7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player7"):
                opp_val = getattr(value, "player7", None)
                if opp_val is None:
                    setattr(value, "player7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def blackjackGame3(self):
        return self.__blackjackGame3
    @blackjackGame3.setter
    def blackjackGame3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__blackjackGame3", None)
        self.__blackjackGame3 = value
        
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



class Hand:

    def __init__(self, handValue: int, player7: set["Player"] = None):
        self.handValue = handValue
        self.player7 = player7 if player7 is not None else set()
        
        pass
    @property
    def handValue(self):
        return self.__handValue
    @handValue.setter
    def handValue(self, handValue: int):
        self.__handValue = handValue

    @property
    def player7(self):
        return self.__player7
    @player7.setter
    def player7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hand__player7", None)
        self.__player7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hand6"):
                    opp_val = getattr(item, "hand6", None)
                    
                    if opp_val == self:
                        setattr(item, "hand6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hand6"):
                    opp_val = getattr(item, "hand6", None)
                    
                    setattr(item, "hand6", self)
                    



class Dealer:

    def __init__(self, handValue: int, handLimit: int, hand1: "Integer_external" = None, blackjackGame5: "BlackjackGame" = None):
        self.handValue = handValue
        self.handLimit = handLimit
        self.hand1 = hand1
        self.blackjackGame5 = blackjackGame5
        
        pass
    @property
    def handValue(self):
        return self.__handValue
    @handValue.setter
    def handValue(self, handValue: int):
        self.__handValue = handValue

    @property
    def handLimit(self):
        return self.__handLimit
    @handLimit.setter
    def handLimit(self, handLimit: int):
        self.__handLimit = handLimit

    @property
    def blackjackGame5(self):
        return self.__blackjackGame5
    @blackjackGame5.setter
    def blackjackGame5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Dealer__blackjackGame5", None)
        self.__blackjackGame5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dealer4"):
                opp_val = getattr(old_value, "dealer4", None)
                if opp_val == self:
                    setattr(old_value, "dealer4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dealer4"):
                opp_val = getattr(value, "dealer4", None)
                setattr(value, "dealer4", self)

    @property
    def hand1(self):
        return self.__hand1
    @hand1.setter
    def hand1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Dealer__hand1", None)
        self.__hand1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dealer0"):
                opp_val = getattr(old_value, "dealer0", None)
                if opp_val == self:
                    setattr(old_value, "dealer0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dealer0"):
                opp_val = getattr(value, "dealer0", None)
                setattr(value, "dealer0", self)



class Cards:

    def __init__(self, cardName: str, cardValue: int):
        self.cardName = cardName
        self.cardValue = cardValue
        
        pass
    @property
    def cardValue(self):
        return self.__cardValue
    @cardValue.setter
    def cardValue(self, cardValue: int):
        self.__cardValue = cardValue

    @property
    def cardName(self):
        return self.__cardName
    @cardName.setter
    def cardName(self, cardName: str):
        self.__cardName = cardName



class Deck:

    def __init__(self, size: int, deckArray: int, association2_111: "_Interface" = None):
        self.size = size
        self.deckArray = deckArray
        self.association2_111 = association2_111
        
        pass
    @property
    def deckArray(self):
        return self.__deckArray
    @deckArray.setter
    def deckArray(self, deckArray: int):
        self.__deckArray = deckArray

    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def association2_111(self):
        return self.__association2_111
    @association2_111.setter
    def association2_111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deck__association2_111", None)
        self.__association2_111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deck10"):
                opp_val = getattr(old_value, "deck10", None)
                if opp_val == self:
                    setattr(old_value, "deck10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deck10"):
                opp_val = getattr(value, "deck10", None)
                setattr(value, "deck10", self)



class _Interface:

    pass
