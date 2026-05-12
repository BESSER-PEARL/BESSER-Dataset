from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Money_PlayerMoney:

    def __init__(self, numofplayers: str, totalmoney: str):
        self.numofplayers = numofplayers
        self.totalmoney = totalmoney
        
        pass
    @property
    def totalmoney(self):
        return self.__totalmoney
    @totalmoney.setter
    def totalmoney(self, totalmoney: str):
        self.__totalmoney = totalmoney

    @property
    def numofplayers(self):
        return self.__numofplayers
    @numofplayers.setter
    def numofplayers(self, numofplayers: str):
        self.__numofplayers = numofplayers



class GUI_Interface:

    pass


class Comparable_Interface:

    pass


class Main_StartGame:

    def __init__(self, hand: str, handsize: int, scanner: str, deck: str, player: str):
        self.hand = hand
        self.handsize = handsize
        self.scanner = scanner
        self.deck = deck
        self.player = player
        
        pass
    @property
    def player(self):
        return self.__player
    @player.setter
    def player(self, player: str):
        self.__player = player

    @property
    def scanner(self):
        return self.__scanner
    @scanner.setter
    def scanner(self, scanner: str):
        self.__scanner = scanner

    @property
    def handsize(self):
        return self.__handsize
    @handsize.setter
    def handsize(self, handsize: int):
        self.__handsize = handsize

    @property
    def deck(self):
        return self.__deck
    @deck.setter
    def deck(self, deck: str):
        self.__deck = deck

    @property
    def hand(self):
        return self.__hand
    @hand.setter
    def hand(self, hand: str):
        self.__hand = hand



class Player_Players:

    pass


class Game_EvaluateHand:

    def __init__(self, card: str):
        self.card = card
        
        pass
    @property
    def card(self):
        return self.__card
    @card.setter
    def card(self, card: str):
        self.__card = card



class Game_Display:

    def __init__(self, card: str, money: str):
        self.card = card
        self.money = money
        
        pass
    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self, money: str):
        self.__money = money

    @property
    def card(self):
        return self.__card
    @card.setter
    def card(self, card: str):
        self.__card = card



class Game_Ranking:

    def __init__(self, card: str):
        self.card = card
        
        pass
    @property
    def card(self):
        return self.__card
    @card.setter
    def card(self, card: str):
        self.__card = card



class Card_Cards:

    def __init__(self, suit: int, rank: int):
        self.suit = suit
        self.rank = rank
        
        pass
    @property
    def rank(self):
        return self.__rank
    @rank.setter
    def rank(self, rank: int):
        self.__rank = rank

    @property
    def suit(self):
        return self.__suit
    @suit.setter
    def suit(self, suit: int):
        self.__suit = suit



class Card_Deck:

    def __init__(self, decksize: int, shuffletimes: int, handsize: int, remainder: int, deck: str, random: str):
        self.decksize = decksize
        self.shuffletimes = shuffletimes
        self.handsize = handsize
        self.remainder = remainder
        self.deck = deck
        self.random = random
        
        pass
    @property
    def deck(self):
        return self.__deck
    @deck.setter
    def deck(self, deck: str):
        self.__deck = deck

    @property
    def handsize(self):
        return self.__handsize
    @handsize.setter
    def handsize(self, handsize: int):
        self.__handsize = handsize

    @property
    def shuffletimes(self):
        return self.__shuffletimes
    @shuffletimes.setter
    def shuffletimes(self, shuffletimes: int):
        self.__shuffletimes = shuffletimes

    @property
    def decksize(self):
        return self.__decksize
    @decksize.setter
    def decksize(self, decksize: int):
        self.__decksize = decksize

    @property
    def random(self):
        return self.__random
    @random.setter
    def random(self, random: str):
        self.__random = random

    @property
    def remainder(self):
        return self.__remainder
    @remainder.setter
    def remainder(self, remainder: int):
        self.__remainder = remainder

