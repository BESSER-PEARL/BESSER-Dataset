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


class IncomeTax:

    def __init__(self, taxRate: float, board9: "Board1" = None):
        self.taxRate = taxRate
        self.board9 = board9
        
        pass
    @property
    def taxRate(self):
        return self.__taxRate
    @taxRate.setter
    def taxRate(self, taxRate: float):
        self.__taxRate = taxRate

    @property
    def board9(self):
        return self.__board9
    @board9.setter
    def board9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_IncomeTax__board9", None)
        self.__board9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incomeTax8"):
                opp_val = getattr(old_value, "incomeTax8", None)
                if opp_val == self:
                    setattr(old_value, "incomeTax8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incomeTax8"):
                opp_val = getattr(value, "incomeTax8", None)
                setattr(value, "incomeTax8", self)



class PlayerIcon:

    def __init__(self, icon: str, boardGUI4: "BoardGUI" = None):
        self.icon = icon
        self.boardGUI4 = boardGUI4
        
        pass
    @property
    def icon(self):
        return self.__icon
    @icon.setter
    def icon(self, icon: str):
        self.__icon = icon

    @property
    def boardGUI4(self):
        return self.__boardGUI4
    @boardGUI4.setter
    def boardGUI4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PlayerIcon__boardGUI4", None)
        self.__boardGUI4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "playerIcon5"):
                opp_val = getattr(old_value, "playerIcon5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "playerIcon5"):
                opp_val = getattr(value, "playerIcon5", None)
                if opp_val is None:
                    setattr(value, "playerIcon5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class JFrame:

    pass


class BoardGUI:

    def __init__(self, frame: JFrame, playerIcon5: set["PlayerIcon"] = None, board16: "Board1" = None):
        self.frame = frame
        self.playerIcon5 = playerIcon5 if playerIcon5 is not None else set()
        self.board16 = board16
        
        pass
    @property
    def frame(self):
        return self.__frame
    @frame.setter
    def frame(self, frame: JFrame):
        self.__frame = frame

    @property
    def playerIcon5(self):
        return self.__playerIcon5
    @playerIcon5.setter
    def playerIcon5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BoardGUI__playerIcon5", None)
        self.__playerIcon5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "boardGUI4"):
                    opp_val = getattr(item, "boardGUI4", None)
                    
                    if opp_val == self:
                        setattr(item, "boardGUI4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "boardGUI4"):
                    opp_val = getattr(item, "boardGUI4", None)
                    
                    setattr(item, "boardGUI4", self)
                    

    @property
    def board16(self):
        return self.__board16
    @board16.setter
    def board16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BoardGUI__board16", None)
        self.__board16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "boardGUI17"):
                opp_val = getattr(old_value, "boardGUI17", None)
                if opp_val == self:
                    setattr(old_value, "boardGUI17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "boardGUI17"):
                opp_val = getattr(value, "boardGUI17", None)
                setattr(value, "boardGUI17", self)



class Chance:

    def __init__(self, amount: Random, board15: "Board1" = None):
        self.amount = amount
        self.board15 = board15
        
        pass
    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: Random):
        self.__amount = amount

    @property
    def board15(self):
        return self.__board15
    @board15.setter
    def board15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Chance__board15", None)
        self.__board15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "chance14"):
                opp_val = getattr(old_value, "chance14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "chance14"):
                opp_val = getattr(value, "chance14", None)
                if opp_val is None:
                    setattr(value, "chance14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Jail:

    def __init__(self, JailPosition: int, jailFine: int, board13: "Board1" = None):
        self.JailPosition = JailPosition
        self.jailFine = jailFine
        self.board13 = board13
        
        pass
    @property
    def JailPosition(self):
        return self.__JailPosition
    @JailPosition.setter
    def JailPosition(self, JailPosition: int):
        self.__JailPosition = JailPosition

    @property
    def jailFine(self):
        return self.__jailFine
    @jailFine.setter
    def jailFine(self, jailFine: int):
        self.__jailFine = jailFine

    @property
    def board13(self):
        return self.__board13
    @board13.setter
    def board13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Jail__board13", None)
        self.__board13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jail12"):
                opp_val = getattr(old_value, "jail12", None)
                if opp_val == self:
                    setattr(old_value, "jail12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jail12"):
                opp_val = getattr(value, "jail12", None)
                setattr(value, "jail12", self)



class AIPlayer:

    pass


class Dice:

    def __init__(self, firstValue: int, secondValue: int, randomNumber: Random, board11: "Board1" = None):
        self.firstValue = firstValue
        self.secondValue = secondValue
        self.randomNumber = randomNumber
        self.board11 = board11
        
        pass
    @property
    def randomNumber(self):
        return self.__randomNumber
    @randomNumber.setter
    def randomNumber(self, randomNumber: Random):
        self.__randomNumber = randomNumber

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
    def board11(self):
        return self.__board11
    @board11.setter
    def board11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Dice__board11", None)
        self.__board11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dice10"):
                opp_val = getattr(old_value, "dice10", None)
                if opp_val == self:
                    setattr(old_value, "dice10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dice10"):
                opp_val = getattr(value, "dice10", None)
                setattr(value, "dice10", self)



class Board1:

    def __init__(self, boardSize: int, player2: set["Player"] = None, freeParking6: "FreeParking" = None, incomeTax8: "IncomeTax" = None, dice10: "Dice" = None, jail12: "Jail" = None, chance14: set["Chance"] = None, boardGUI17: "BoardGUI" = None):
        self.boardSize = boardSize
        self.player2 = player2 if player2 is not None else set()
        self.freeParking6 = freeParking6
        self.incomeTax8 = incomeTax8
        self.dice10 = dice10
        self.jail12 = jail12
        self.chance14 = chance14 if chance14 is not None else set()
        self.boardGUI17 = boardGUI17
        
        pass
    @property
    def boardSize(self):
        return self.__boardSize
    @boardSize.setter
    def boardSize(self, boardSize: int):
        self.__boardSize = boardSize

    @property
    def chance14(self):
        return self.__chance14
    @chance14.setter
    def chance14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Board1__chance14", None)
        self.__chance14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "board15"):
                    opp_val = getattr(item, "board15", None)
                    
                    if opp_val == self:
                        setattr(item, "board15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "board15"):
                    opp_val = getattr(item, "board15", None)
                    
                    setattr(item, "board15", self)
                    

    @property
    def boardGUI17(self):
        return self.__boardGUI17
    @boardGUI17.setter
    def boardGUI17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Board1__boardGUI17", None)
        self.__boardGUI17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "board16"):
                opp_val = getattr(old_value, "board16", None)
                if opp_val == self:
                    setattr(old_value, "board16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "board16"):
                opp_val = getattr(value, "board16", None)
                setattr(value, "board16", self)

    @property
    def freeParking6(self):
        return self.__freeParking6
    @freeParking6.setter
    def freeParking6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Board1__freeParking6", None)
        self.__freeParking6 = value
        
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

    @property
    def jail12(self):
        return self.__jail12
    @jail12.setter
    def jail12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Board1__jail12", None)
        self.__jail12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "board13"):
                opp_val = getattr(old_value, "board13", None)
                if opp_val == self:
                    setattr(old_value, "board13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "board13"):
                opp_val = getattr(value, "board13", None)
                setattr(value, "board13", self)

    @property
    def dice10(self):
        return self.__dice10
    @dice10.setter
    def dice10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Board1__dice10", None)
        self.__dice10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "board11"):
                opp_val = getattr(old_value, "board11", None)
                if opp_val == self:
                    setattr(old_value, "board11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "board11"):
                opp_val = getattr(value, "board11", None)
                setattr(value, "board11", self)

    @property
    def incomeTax8(self):
        return self.__incomeTax8
    @incomeTax8.setter
    def incomeTax8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Board1__incomeTax8", None)
        self.__incomeTax8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "board9"):
                opp_val = getattr(old_value, "board9", None)
                if opp_val == self:
                    setattr(old_value, "board9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "board9"):
                opp_val = getattr(value, "board9", None)
                setattr(value, "board9", self)

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

    def __init__(self, isRetire: bool, isAI: bool, isBankrupt: bool, board: Board, rand: Random, INITIAL_MONEY: int, INITIAL_POSITION: int, PASS_GO_MONEY: int, name: str, money: Money, position: int, property1: Property, inJail: bool, board3: "Board1" = None, money1: "Money" = None):
        self.isRetire = isRetire
        self.isAI = isAI
        self.isBankrupt = isBankrupt
        self.board = board
        self.rand = rand
        self.INITIAL_MONEY = INITIAL_MONEY
        self.INITIAL_POSITION = INITIAL_POSITION
        self.PASS_GO_MONEY = PASS_GO_MONEY
        self.name = name
        self.money = money
        self.position = position
        self.property1 = property1
        self.inJail = inJail
        self.board3 = board3
        self.money1 = money1
        
        pass
    @property
    def isRetire(self):
        return self.__isRetire
    @isRetire.setter
    def isRetire(self, isRetire: bool):
        self.__isRetire = isRetire

    @property
    def INITIAL_MONEY(self):
        return self.__INITIAL_MONEY
    @INITIAL_MONEY.setter
    def INITIAL_MONEY(self, INITIAL_MONEY: int):
        self.__INITIAL_MONEY = INITIAL_MONEY

    @property
    def board(self):
        return self.__board
    @board.setter
    def board(self, board: Board):
        self.__board = board

    @property
    def property1(self):
        return self.__property1
    @property1.setter
    def property1(self, property1: Property):
        self.__property1 = property1

    @property
    def PASS_GO_MONEY(self):
        return self.__PASS_GO_MONEY
    @PASS_GO_MONEY.setter
    def PASS_GO_MONEY(self, PASS_GO_MONEY: int):
        self.__PASS_GO_MONEY = PASS_GO_MONEY

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
    def rand(self):
        return self.__rand
    @rand.setter
    def rand(self, rand: Random):
        self.__rand = rand

    @property
    def isAI(self):
        return self.__isAI
    @isAI.setter
    def isAI(self, isAI: bool):
        self.__isAI = isAI

    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self, money: Money):
        self.__money = money

    @property
    def inJail(self):
        return self.__inJail
    @inJail.setter
    def inJail(self, inJail: bool):
        self.__inJail = inJail

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, position: int):
        self.__position = position

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

