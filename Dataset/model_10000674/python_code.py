from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class List_User_S_(Enum):
    pass
class List_Card_(Enum):
    pass

############################################
# Definition of Classes
############################################










class dutycalls_contoller_HomeControl:

    pass


class dutycalls_contoller_Dealer_Control:

    def __init__(self, cardCount: int, userid: int):
        self.cardCount = cardCount
        self.userid = userid
        
        pass
    @property
    def cardCount(self):
        return self.__cardCount
    @cardCount.setter
    def cardCount(self, cardCount: int):
        self.__cardCount = cardCount

    @property
    def userid(self):
        return self.__userid
    @userid.setter
    def userid(self, userid: int):
        self.__userid = userid



class dutycalls_model_User_S:

    def __init__(self, id: int):
        self.id = id
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id



class dutycalls_model_Value:

    pass


class dutycalls_model_Suit:

    pass


class dutycalls_model_WildHand:

    pass


class dutycalls_model_GameType:

    pass


class dutycalls_model_PokerHand:

    pass


class dutycalls_model_PlayerHand:

    pass


class dutycalls_model_Card:

    pass


class dutycalls_model_Deck:

    pass


class dutycalls_model_BestHand:

    def __init__(self, handValue: int):
        self.handValue = handValue
        
        pass
    @property
    def handValue(self):
        return self.__handValue
    @handValue.setter
    def handValue(self, handValue: int):
        self.__handValue = handValue



class dutycalls_model_Dealer_SINGLEPLAYER:

    def __init__(self, allIn: bool, bet: int, deck: dutycalls_model_Deck, main_userList: List_User_S_, openBet: int, tableValue: int, userList: List_User_S_):
        self.allIn = allIn
        self.bet = bet
        self.deck = deck
        self.main_userList = main_userList
        self.openBet = openBet
        self.tableValue = tableValue
        self.userList = userList
        
        pass
    @property
    def allIn(self):
        return self.__allIn
    @allIn.setter
    def allIn(self, allIn: bool):
        self.__allIn = allIn

    @property
    def openBet(self):
        return self.__openBet
    @openBet.setter
    def openBet(self, openBet: int):
        self.__openBet = openBet

    @property
    def userList(self):
        return self.__userList
    @userList.setter
    def userList(self, userList: List_User_S_):
        self.__userList = userList

    @property
    def bet(self):
        return self.__bet
    @bet.setter
    def bet(self, bet: int):
        self.__bet = bet

    @property
    def deck(self):
        return self.__deck
    @deck.setter
    def deck(self, deck: dutycalls_model_Deck):
        self.__deck = deck

    @property
    def tableValue(self):
        return self.__tableValue
    @tableValue.setter
    def tableValue(self, tableValue: int):
        self.__tableValue = tableValue

    @property
    def main_userList(self):
        return self.__main_userList
    @main_userList.setter
    def main_userList(self, main_userList: List_User_S_):
        self.__main_userList = main_userList



class dutycalls_model_AIUser:

    pass


class dutycalls_view_User:

    pass


class dutycalls_view_WaitingForPlayer:

    pass


class dutycalls_view_PokerTable:

    pass


class dutycalls_view_JoinGame:

    pass


class dutycalls_view_Instructions:

    pass


class dutycalls_view_Home:

    pass


class dutycalls_view_About:

    pass
