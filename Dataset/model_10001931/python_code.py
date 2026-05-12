from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Chips_ChipDeductResult(Enum):
    pass
class Cards_Suit(Enum):
    pass
class Ranker_Ranking(Enum):
    pass
class Player_PlayerStatus(Enum):
    pass
class Cards_CardRank(Enum):
    pass

############################################
# Definition of Classes
############################################










class DiscardableArray_DealableArray:

    pass


class DiscardableArray_DiscardableArray_Interface:

    pass


class Player_Player:

    def __init__(self, chips: Chips_ChipStash, status: Player_PlayerStatus, card1: set["Cards_Card"] = None):
        self.chips = chips
        self.status = status
        self.card1 = card1 if card1 is not None else set()
        
        pass
    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: Player_PlayerStatus):
        self.__status = status

    @property
    def chips(self):
        return self.__chips
    @chips.setter
    def chips(self, chips: Chips_ChipStash):
        self.__chips = chips

    @property
    def card1(self):
        return self.__card1
    @card1.setter
    def card1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player_Player__card1", None)
        self.__card1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "player0"):
                    opp_val = getattr(item, "player0", None)
                    
                    if opp_val == self:
                        setattr(item, "player0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "player0"):
                    opp_val = getattr(item, "player0", None)
                    
                    setattr(item, "player0", self)
                    



class Ranker_Rank:

    pass


class Gameplay_GameInitializer:

    pass


class Gameplay_Game:

    def __init__(self, players: Player_Player, pot: Chips_Pot, deck: str, round: int):
        self.players = players
        self.pot = pot
        self.deck = deck
        self.round = round
        
        pass
    @property
    def players(self):
        return self.__players
    @players.setter
    def players(self, players: Player_Player):
        self.__players = players

    @property
    def round(self):
        return self.__round
    @round.setter
    def round(self, round: int):
        self.__round = round

    @property
    def deck(self):
        return self.__deck
    @deck.setter
    def deck(self, deck: str):
        self.__deck = deck

    @property
    def pot(self):
        return self.__pot
    @pot.setter
    def pot(self, pot: Chips_Pot):
        self.__pot = pot



class Chips_Pot:

    pass


class Chips_ChipStash:

    pass


class Chips_Chip:

    def __init__(self, value: int, chipStash2: set["Chips_ChipStash"] = None):
        self.value = value
        self.chipStash2 = chipStash2 if chipStash2 is not None else set()
        
        pass
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def chipStash2(self):
        return self.__chipStash2
    @chipStash2.setter
    def chipStash2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Chips_Chip__chipStash2", None)
        self.__chipStash2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "chip3"):
                    opp_val = getattr(item, "chip3", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "chip3"):
                    opp_val = getattr(item, "chip3", None)
                    
                    if opp_val is None:
                        setattr(item, "chip3", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Cards_Card:

    def __init__(self, rank: Cards_CardRank, suit: Cards_Suit, player0: "Player_Player" = None):
        self.rank = rank
        self.suit = suit
        self.player0 = player0
        
        pass
    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: Cards_Suit):
        self.__suit = suit

    @property
    def rank(self):
        return self.__rank
    @rank.setter
    def rank(self, rank: Cards_CardRank):
        self.__rank = rank

    @property
    def player0(self):
        return self.__player0
    @player0.setter
    def player0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cards_Card__player0", None)
        self.__player0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "card1"):
                opp_val = getattr(old_value, "card1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card1"):
                opp_val = getattr(value, "card1", None)
                if opp_val is None:
                    setattr(value, "card1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

