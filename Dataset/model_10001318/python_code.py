from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class cards_Suit(Enum):
    pass

############################################
# Definition of Classes
############################################










class main_Play:

    def __init__(self, players: str, plv: players_PlayerVersionGUI, gb: game_GameBoardGUI, cd: cards_CardsGUI):
        self.players = players
        self.plv = plv
        self.gb = gb
        self.cd = cd
        
        pass
    @property
    def players(self):
        return self.__players
    @players.setter
    def players(self, players: str):
        self.__players = players

    @property
    def gb(self):
        return self.__gb
    @gb.setter
    def gb(self, gb: game_GameBoardGUI):
        self.__gb = gb

    @property
    def cd(self):
        return self.__cd
    @cd.setter
    def cd(self, cd: cards_CardsGUI):
        self.__cd = cd

    @property
    def plv(self):
        return self.__plv
    @plv.setter
    def plv(self, plv: players_PlayerVersionGUI):
        self.__plv = plv



class game_GameBoardGUI:

    pass


class game_Ranker:

    def __init__(self, hand: cards_PokerHand, highValue: int):
        self.hand = hand
        self.highValue = highValue
        
        pass
    @property
    def hand(self):
        return self.__hand
    @hand.setter
    def hand(self, hand: cards_PokerHand):
        self.__hand = hand

    @property
    def highValue(self):
        return self.__highValue
    @highValue.setter
    def highValue(self, highValue: int):
        self.__highValue = highValue



class players_Person:

    def __init__(self, name: str, accountNumber: str):
        self.name = name
        self.accountNumber = accountNumber
        
        pass
    @property
    def accountNumber(self):
        return self.__accountNumber
    @accountNumber.setter
    def accountNumber(self, accountNumber: str):
        self.__accountNumber = accountNumber

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name



class players_PlayerVersionGUI:

    pass


class players_Player:

    def __init__(self, hand: cards_PokerHand, hasFolded: bool, curentChips: int):
        self.hand = hand
        self.hasFolded = hasFolded
        self.curentChips = curentChips
        
        pass
    @property
    def hasFolded(self):
        return self.__hasFolded
    @hasFolded.setter
    def hasFolded(self, hasFolded: bool):
        self.__hasFolded = hasFolded

    @property
    def hand(self):
        return self.__hand
    @hand.setter
    def hand(self, hand: cards_PokerHand):
        self.__hand = hand

    @property
    def curentChips(self):
        return self.__curentChips
    @curentChips.setter
    def curentChips(self, curentChips: int):
        self.__curentChips = curentChips



class cards_PokerHandInterface_Interface:

    pass


class cards_CardsGUI:

    pass


class cards_Deck:

    def __init__(self, cards: str, remain: int):
        self.cards = cards
        self.remain = remain
        
        pass
    @property
    def remain(self):
        return self.__remain
    @remain.setter
    def remain(self, remain: int):
        self.__remain = remain

    @property
    def cards(self):
        return self.__cards
    @cards.setter
    def cards(self, cards: str):
        self.__cards = cards



class cards_PokerHand:

    def __init__(self, hand: str, rank: int):
        self.hand = hand
        self.rank = rank
        
        pass
    @property
    def hand(self):
        return self.__hand
    @hand.setter
    def hand(self, hand: str):
        self.__hand = hand

    @property
    def rank(self):
        return self.__rank
    @rank.setter
    def rank(self, rank: int):
        self.__rank = rank



class cards_Card:

    def __init__(self, rank: int, suit: cards_Suit):
        self.rank = rank
        self.suit = suit
        
        pass
    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: cards_Suit):
        self.__suit = suit

    @property
    def rank(self):
        return self.__rank
    @rank.setter
    def rank(self, rank: int):
        self.__rank = rank

