from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Property(Enum):
    pass

############################################
# Definition of Classes
############################################










class FreeParking:

    pass


class AIPlayer:

    pass


class Dice:

    def __init__(self, firstValue: int, secondValue: int, randomNumber: Random, board7: "Board1" = None):
        self.firstValue = firstValue
        self.secondValue = secondValue
        self.randomNumber = randomNumber
        self.board7 = board7
        
        pass
    @property
    def secondValue(self):
        return self.__secondValue
    @secondValue.setter
    def secondValue(self, secondValue: int):
        self.__secondValue = secondValue

    @property
    def firstValue(self):
        return self.__firstValue
    @firstValue.setter
    def firstValue(self, firstValue: int):
        self.__firstValue = firstValue

    @property
    def randomNumber(self):
        return self.__randomNumber
    @randomNumber.setter
    def randomNumber(self, randomNumber: Random):
        self.__randomNumber = randomNumber

    @property
    def board7(self):
        return self.__board7
    @board7.setter
    def board7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Dice__board7", None)
        self.__board7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dice6"):
                opp_val = getattr(old_value, "dice6", None)
                if opp_val == self:
                    setattr(old_value, "dice6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dice6"):
                opp_val = getattr(value, "dice6", None)
                setattr(value, "dice6", self)



class Board1:

    def __init__(self, boardSize: int, freeParking4: "FreeParking" = None, dice6: "Dice" = None, player2: set["Player"] = None):
        self.boardSize = boardSize
        self.freeParking4 = freeParking4
        self.dice6 = dice6
        self.player2 = player2 if player2 is not None else set()
        
        pass
    @property
    def boardSize(self):
        return self.__boardSize
    @boardSize.setter
    def boardSize(self, boardSize: int):
        self.__boardSize = boardSize

    @property
    def freeParking4(self):
        return self.__freeParking4
    @freeParking4.setter
    def freeParking4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Board1__freeParking4", None)
        self.__freeParking4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "board5"):
                opp_val = getattr(old_value, "board5", None)
                if opp_val == self:
                    setattr(old_value, "board5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "board5"):
                opp_val = getattr(value, "board5", None)
                setattr(value, "board5", self)

    @property
    def player2(self):
        return self.__player2
    @player2.setter
    def player2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Board1__player2", None)
        self.__player2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "board3"):
                    opp_val = getattr(item, "board3", None)
                    
                    if opp_val == self:
                        setattr(item, "board3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "board3"):
                    opp_val = getattr(item, "board3", None)
                    
                    setattr(item, "board3", self)
                    

    @property
    def dice6(self):
        return self.__dice6
    @dice6.setter
    def dice6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Board1__dice6", None)
        self.__dice6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "board7"):
                opp_val = getattr(old_value, "board7", None)
                if opp_val == self:
                    setattr(old_value, "board7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "board7"):
                opp_val = getattr(value, "board7", None)
                setattr(value, "board7", self)



class Money:

    def __init__(self, money: int, player0: "Player" = None):
        self.money = money
        self.player0 = player0
        
        pass
    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self, money: int):
        self.__money = money

    @property
    def player0(self):
        return self.__player0
    @player0.setter
    def player0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Money__player0", None)
        self.__player0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "money1"):
                opp_val = getattr(old_value, "money1", None)
                if opp_val == self:
                    setattr(old_value, "money1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "money1"):
                opp_val = getattr(value, "money1", None)
                setattr(value, "money1", self)



class Board:

    pass


class Random:

    pass


class Class:

    pass


class Player:

    def __init__(self, board: Board, rand: Random, INITIAL_MONEY: int, INITIAL_POSITION: int, PASS_GO_MONEY: int, name: str, money: Money, position: int, property1: str, isRetire: bool, isAI: bool, isBankrupt: bool, money1: "Money" = None, board3: "Board1" = None):
        self.board = board
        self.rand = rand
        self.INITIAL_MONEY = INITIAL_MONEY
        self.INITIAL_POSITION = INITIAL_POSITION
        self.PASS_GO_MONEY = PASS_GO_MONEY
        self.name = name
        self.money = money
        self.position = position
        self.property1 = property1
        self.isRetire = isRetire
        self.isAI = isAI
        self.isBankrupt = isBankrupt
        self.money1 = money1
        self.board3 = board3
        
        pass
    @property
    def isRetire(self):
        return self.__isRetire
    @isRetire.setter
    def isRetire(self, isRetire: bool):
        self.__isRetire = isRetire

    @property
    def PASS_GO_MONEY(self):
        return self.__PASS_GO_MONEY
    @PASS_GO_MONEY.setter
    def PASS_GO_MONEY(self, PASS_GO_MONEY: int):
        self.__PASS_GO_MONEY = PASS_GO_MONEY

    @property
    def isAI(self):
        return self.__isAI
    @isAI.setter
    def isAI(self, isAI: bool):
        self.__isAI = isAI

    @property
    def INITIAL_POSITION(self):
        return self.__INITIAL_POSITION
    @INITIAL_POSITION.setter
    def INITIAL_POSITION(self, INITIAL_POSITION: int):
        self.__INITIAL_POSITION = INITIAL_POSITION

    @property
    def isBankrupt(self):
        return self.__isBankrupt
    @isBankrupt.setter
    def isBankrupt(self, isBankrupt: bool):
        self.__isBankrupt = isBankrupt

    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, position: int):
        self.__position = position

    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self, money: Money):
        self.__money = money

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def property1(self):
        return self.__property1
    @property1.setter
    def property1(self, property1: str):
        self.__property1 = property1

    @property
    def INITIAL_MONEY(self):
        return self.__INITIAL_MONEY
    @INITIAL_MONEY.setter
    def INITIAL_MONEY(self, INITIAL_MONEY: int):
        self.__INITIAL_MONEY = INITIAL_MONEY

    @property
    def rand(self):
        return self.__rand
    @rand.setter
    def rand(self, rand: Random):
        self.__rand = rand

    @property
    def board(self):
        return self.__board
    @board.setter
    def board(self, board: Board):
        self.__board = board

    @property
    def board3(self):
        return self.__board3
    @board3.setter
    def board3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__board3", None)
        self.__board3 = value
        
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

    @property
    def money1(self):
        return self.__money1
    @money1.setter
    def money1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Player__money1", None)
        self.__money1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "player0"):
                opp_val = getattr(old_value, "player0", None)
                if opp_val == self:
                    setattr(old_value, "player0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "player0"):
                opp_val = getattr(value, "player0", None)
                setattr(value, "player0", self)

