from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class CardTitle(Enum):
    pass
class CardSuit(Enum):
    pass

############################################
# Definition of Classes
############################################










class Game:

    def __init__(self, winner: Player, player1: set["Player"] = None, dealer2: "Dealer" = None):
        self.winner = winner
        self.player1 = player1 if player1 is not None else set()
        self.dealer2 = dealer2
        
        pass
    @property
    def winner(self):
        return self.__winner
    @winner.setter
    def winner(self, winner: Player):
        self.__winner = winner

    @property
    def player1(self):
        return self.__player1
    @player1.setter
    def player1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Game__player1", None)
        self.__player1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "game0"):
                    opp_val = getattr(item, "game0", None)
                    
                    if opp_val == self:
                        setattr(item, "game0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "game0"):
                    opp_val = getattr(item, "game0", None)
                    
                    setattr(item, "game0", self)
                    

    @property
    def dealer2(self):
        return self.__dealer2
    @dealer2.setter
    def dealer2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Game__dealer2", None)
        self.__dealer2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "game3"):
                opp_val = getattr(old_value, "game3", None)
                if opp_val == self:
                    setattr(old_value, "game3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "game3"):
                opp_val = getattr(value, "game3", None)
                setattr(value, "game3", self)



class HandValue:

    pass


class Dealer:

    def __init__(self, name: str, cards: Cards, game3: "Game" = None, deck10: "Deck" = None):
        self.name = name
        self.cards = cards
        self.game3 = game3
        self.deck10 = deck10
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cards(self):
        return self.__cards
    @cards.setter
    def cards(self, cards: Cards):
        self.__cards = cards

    @property
    def game3(self):
        return self.__game3
    @game3.setter
    def game3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Dealer__game3", None)
        self.__game3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dealer2"):
                opp_val = getattr(old_value, "dealer2", None)
                if opp_val == self:
                    setattr(old_value, "dealer2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dealer2"):
                opp_val = getattr(value, "dealer2", None)
                setattr(value, "dealer2", self)

    @property
    def deck10(self):
        return self.__deck10
    @deck10.setter
    def deck10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Dealer__deck10", None)
        self.__deck10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dealer11"):
                opp_val = getattr(old_value, "dealer11", None)
                if opp_val == self:
                    setattr(old_value, "dealer11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dealer11"):
                opp_val = getattr(value, "dealer11", None)
                setattr(value, "dealer11", self)



class Hand:

    def __init__(self, value: HandValue, player6: "Player" = None, handValue9: "HandValue" = None, cards12: set["Cards"] = None):
        self.value = value
        self.player6 = player6
        self.handValue9 = handValue9
        self.cards12 = cards12 if cards12 is not None else set()
        
        pass
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value: HandValue):
        self.__value = value

    @property
    def player6(self):
        return self.__player6
    @player6.setter
    def player6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hand__player6", None)
        self.__player6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hand7"):
                opp_val = getattr(old_value, "hand7", None)
                if opp_val == self:
                    setattr(old_value, "hand7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hand7"):
                opp_val = getattr(value, "hand7", None)
                setattr(value, "hand7", self)

    @property
    def cards12(self):
        return self.__cards12
    @cards12.setter
    def cards12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hand__cards12", None)
        self.__cards12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hand13"):
                    opp_val = getattr(item, "hand13", None)
                    
                    if opp_val == self:
                        setattr(item, "hand13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hand13"):
                    opp_val = getattr(item, "hand13", None)
                    
                    setattr(item, "hand13", self)
                    

    @property
    def handValue9(self):
        return self.__handValue9
    @handValue9.setter
    def handValue9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hand__handValue9", None)
        self.__handValue9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hand8"):
                opp_val = getattr(old_value, "hand8", None)
                if opp_val == self:
                    setattr(old_value, "hand8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hand8"):
                opp_val = getattr(value, "hand8", None)
                setattr(value, "hand8", self)



class Player:

    def __init__(self, name: str, game0: "Game" = None, hand7: "Hand" = None):
        self.name = name
        self.game0 = game0
        self.hand7 = hand7
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def hand7(self):
        return self.__hand7
    @hand7.setter
    def hand7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__hand7", None)
        self.__hand7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player6"):
                opp_val = getattr(old_value, "player6", None)
                if opp_val == self:
                    setattr(old_value, "player6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player6"):
                opp_val = getattr(value, "player6", None)
                setattr(value, "player6", self)

    @property
    def game0(self):
        return self.__game0
    @game0.setter
    def game0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__game0", None)
        self.__game0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player1"):
                opp_val = getattr(old_value, "player1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player1"):
                opp_val = getattr(value, "player1", None)
                if opp_val is None:
                    setattr(value, "player1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Cards:

    def __init__(self, value: int, suit: CardSuit, title: CardTitle, deck5: "Deck" = None, hand13: "Hand" = None):
        self.value = value
        self.suit = suit
        self.title = title
        self.deck5 = deck5
        self.hand13 = hand13
        
        pass
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: CardSuit):
        self.__suit = suit

    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, title: CardTitle):
        self.__title = title

    @property
    def deck5(self):
        return self.__deck5
    @deck5.setter
    def deck5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cards__deck5", None)
        self.__deck5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cards4"):
                opp_val = getattr(old_value, "cards4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cards4"):
                opp_val = getattr(value, "cards4", None)
                if opp_val is None:
                    setattr(value, "cards4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def hand13(self):
        return self.__hand13
    @hand13.setter
    def hand13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cards__hand13", None)
        self.__hand13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cards12"):
                opp_val = getattr(old_value, "cards12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cards12"):
                opp_val = getattr(value, "cards12", None)
                if opp_val is None:
                    setattr(value, "cards12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Deck:

    pass
