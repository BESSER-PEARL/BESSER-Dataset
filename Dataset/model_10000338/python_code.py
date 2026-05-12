from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class candyCrushPackage_SwapDirection(Enum):
    pass

############################################
# Definition of Classes
############################################










class Color_external:

    pass


class candyCrushPackage_ActionListener_Interface:

    pass


class candyCrushPackage_JPanel:

    pass


class candyCrushPackage_JFrame:

    pass


class candyCrushPackage_CandyButton:

    def __init__(self, button: str, image: str, x: int, y: int, image4: "ImageIcon_external" = None, button6: "JButton_external" = None, board13: "candyCrushPackage_Board" = None):
        self.button = button
        self.image = image
        self.x = x
        self.y = y
        self.image4 = image4
        self.button6 = button6
        self.board13 = board13
        
        pass
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x: int):
        self.__x = x

    @property
    def button(self):
        return self.__button
    @button.setter
    def button(self, button: str):
        self.__button = button

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y: int):
        self.__y = y

    @property
    def image(self):
        return self.__image
    @image.setter
    def image(self, image: str):
        self.__image = image

    @property
    def board13(self):
        return self.__board13
    @board13.setter
    def board13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_candyCrushPackage_CandyButton__board13", None)
        self.__board13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "candiesButtons12"):
                opp_val = getattr(old_value, "candiesButtons12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "candiesButtons12"):
                opp_val = getattr(value, "candiesButtons12", None)
                if opp_val is None:
                    setattr(value, "candiesButtons12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def image4(self):
        return self.__image4
    @image4.setter
    def image4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_candyCrushPackage_CandyButton__image4", None)
        self.__image4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "candyButton5"):
                opp_val = getattr(old_value, "candyButton5", None)
                if opp_val == self:
                    setattr(old_value, "candyButton5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "candyButton5"):
                opp_val = getattr(value, "candyButton5", None)
                setattr(value, "candyButton5", self)

    @property
    def button6(self):
        return self.__button6
    @button6.setter
    def button6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_candyCrushPackage_CandyButton__button6", None)
        self.__button6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "candyButton7"):
                opp_val = getattr(old_value, "candyButton7", None)
                if opp_val == self:
                    setattr(old_value, "candyButton7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "candyButton7"):
                opp_val = getattr(value, "candyButton7", None)
                setattr(value, "candyButton7", self)



class candyCrushPackage_ColorBombCandy:

    pass


class candyCrushPackage_WrappedCandy:

    def __init__(self, selfCrushRange: int):
        self.selfCrushRange = selfCrushRange
        
        pass
    @property
    def selfCrushRange(self):
        return self.__selfCrushRange
    @selfCrushRange.setter
    def selfCrushRange(self, selfCrushRange: int):
        self.__selfCrushRange = selfCrushRange



class candyCrushPackage_StrippedCandy:

    def __init__(self, isHorizontal: bool):
        self.isHorizontal = isHorizontal
        
        pass
    @property
    def isHorizontal(self):
        return self.__isHorizontal
    @isHorizontal.setter
    def isHorizontal(self, isHorizontal: bool):
        self.__isHorizontal = isHorizontal



class candyCrushPackage_Board:

    def __init__(self, BOARD_HEIGHT: int, SIZE: int, candyWidth: int, candyHeight: int, delay: int, moveDistance: int, baseScorePerCandy: int, movesPerGame: int, gameScore: int, scorePerCandy: str, dropTimer: str, swapTimer: str, crushTimer: str, selfCrushTimer: str, cascadeTimer: str, dropTimerCount: int, swapTimerCount: int, crushTimerCount: int, selfCrushTimerCount: int, isFirstPressed: bool, isSwapBack: bool, movesLeft: int, firstPressedCandy: candyCrushPackage_Candy, secondPressedCandy: candyCrushPackage_Candy, selfCrushCandy: candyCrushPackage_Candy, swapDirection: candyCrushPackage_SwapDirection, HORIZONTAL_GAP: int, VERTICAL_GAP: int, BOARD_WIDTH: int, game3: "candyCrushPackage_Game" = None, candies10: set["candyCrushPackage_Candy"] = None, candiesButtons12: set["candyCrushPackage_CandyButton"] = None):
        self.BOARD_HEIGHT = BOARD_HEIGHT
        self.SIZE = SIZE
        self.candyWidth = candyWidth
        self.candyHeight = candyHeight
        self.delay = delay
        self.moveDistance = moveDistance
        self.baseScorePerCandy = baseScorePerCandy
        self.movesPerGame = movesPerGame
        self.gameScore = gameScore
        self.scorePerCandy = scorePerCandy
        self.dropTimer = dropTimer
        self.swapTimer = swapTimer
        self.crushTimer = crushTimer
        self.selfCrushTimer = selfCrushTimer
        self.cascadeTimer = cascadeTimer
        self.dropTimerCount = dropTimerCount
        self.swapTimerCount = swapTimerCount
        self.crushTimerCount = crushTimerCount
        self.selfCrushTimerCount = selfCrushTimerCount
        self.isFirstPressed = isFirstPressed
        self.isSwapBack = isSwapBack
        self.movesLeft = movesLeft
        self.firstPressedCandy = firstPressedCandy
        self.secondPressedCandy = secondPressedCandy
        self.selfCrushCandy = selfCrushCandy
        self.swapDirection = swapDirection
        self.HORIZONTAL_GAP = HORIZONTAL_GAP
        self.VERTICAL_GAP = VERTICAL_GAP
        self.BOARD_WIDTH = BOARD_WIDTH
        self.game3 = game3
        self.candies10 = candies10 if candies10 is not None else set()
        self.candiesButtons12 = candiesButtons12 if candiesButtons12 is not None else set()
        
        pass
    @property
    def movesLeft(self):
        return self.__movesLeft
    @movesLeft.setter
    def movesLeft(self, movesLeft: int):
        self.__movesLeft = movesLeft

    @property
    def BOARD_WIDTH(self):
        return self.__BOARD_WIDTH
    @BOARD_WIDTH.setter
    def BOARD_WIDTH(self, BOARD_WIDTH: int):
        self.__BOARD_WIDTH = BOARD_WIDTH

    @property
    def VERTICAL_GAP(self):
        return self.__VERTICAL_GAP
    @VERTICAL_GAP.setter
    def VERTICAL_GAP(self, VERTICAL_GAP: int):
        self.__VERTICAL_GAP = VERTICAL_GAP

    @property
    def candyHeight(self):
        return self.__candyHeight
    @candyHeight.setter
    def candyHeight(self, candyHeight: int):
        self.__candyHeight = candyHeight

    @property
    def HORIZONTAL_GAP(self):
        return self.__HORIZONTAL_GAP
    @HORIZONTAL_GAP.setter
    def HORIZONTAL_GAP(self, HORIZONTAL_GAP: int):
        self.__HORIZONTAL_GAP = HORIZONTAL_GAP

    @property
    def SIZE(self):
        return self.__SIZE
    @SIZE.setter
    def SIZE(self, SIZE: int):
        self.__SIZE = SIZE

    @property
    def crushTimer(self):
        return self.__crushTimer
    @crushTimer.setter
    def crushTimer(self, crushTimer: str):
        self.__crushTimer = crushTimer

    @property
    def dropTimerCount(self):
        return self.__dropTimerCount
    @dropTimerCount.setter
    def dropTimerCount(self, dropTimerCount: int):
        self.__dropTimerCount = dropTimerCount

    @property
    def firstPressedCandy(self):
        return self.__firstPressedCandy
    @firstPressedCandy.setter
    def firstPressedCandy(self, firstPressedCandy: candyCrushPackage_Candy):
        self.__firstPressedCandy = firstPressedCandy

    @property
    def candyWidth(self):
        return self.__candyWidth
    @candyWidth.setter
    def candyWidth(self, candyWidth: int):
        self.__candyWidth = candyWidth

    @property
    def selfCrushTimer(self):
        return self.__selfCrushTimer
    @selfCrushTimer.setter
    def selfCrushTimer(self, selfCrushTimer: str):
        self.__selfCrushTimer = selfCrushTimer

    @property
    def swapDirection(self):
        return self.__swapDirection
    @swapDirection.setter
    def swapDirection(self, swapDirection: candyCrushPackage_SwapDirection):
        self.__swapDirection = swapDirection

    @property
    def secondPressedCandy(self):
        return self.__secondPressedCandy
    @secondPressedCandy.setter
    def secondPressedCandy(self, secondPressedCandy: candyCrushPackage_Candy):
        self.__secondPressedCandy = secondPressedCandy

    @property
    def dropTimer(self):
        return self.__dropTimer
    @dropTimer.setter
    def dropTimer(self, dropTimer: str):
        self.__dropTimer = dropTimer

    @property
    def cascadeTimer(self):
        return self.__cascadeTimer
    @cascadeTimer.setter
    def cascadeTimer(self, cascadeTimer: str):
        self.__cascadeTimer = cascadeTimer

    @property
    def swapTimerCount(self):
        return self.__swapTimerCount
    @swapTimerCount.setter
    def swapTimerCount(self, swapTimerCount: int):
        self.__swapTimerCount = swapTimerCount

    @property
    def selfCrushCandy(self):
        return self.__selfCrushCandy
    @selfCrushCandy.setter
    def selfCrushCandy(self, selfCrushCandy: candyCrushPackage_Candy):
        self.__selfCrushCandy = selfCrushCandy

    @property
    def selfCrushTimerCount(self):
        return self.__selfCrushTimerCount
    @selfCrushTimerCount.setter
    def selfCrushTimerCount(self, selfCrushTimerCount: int):
        self.__selfCrushTimerCount = selfCrushTimerCount

    @property
    def baseScorePerCandy(self):
        return self.__baseScorePerCandy
    @baseScorePerCandy.setter
    def baseScorePerCandy(self, baseScorePerCandy: int):
        self.__baseScorePerCandy = baseScorePerCandy

    @property
    def isFirstPressed(self):
        return self.__isFirstPressed
    @isFirstPressed.setter
    def isFirstPressed(self, isFirstPressed: bool):
        self.__isFirstPressed = isFirstPressed

    @property
    def scorePerCandy(self):
        return self.__scorePerCandy
    @scorePerCandy.setter
    def scorePerCandy(self, scorePerCandy: str):
        self.__scorePerCandy = scorePerCandy

    @property
    def isSwapBack(self):
        return self.__isSwapBack
    @isSwapBack.setter
    def isSwapBack(self, isSwapBack: bool):
        self.__isSwapBack = isSwapBack

    @property
    def movesPerGame(self):
        return self.__movesPerGame
    @movesPerGame.setter
    def movesPerGame(self, movesPerGame: int):
        self.__movesPerGame = movesPerGame

    @property
    def gameScore(self):
        return self.__gameScore
    @gameScore.setter
    def gameScore(self, gameScore: int):
        self.__gameScore = gameScore

    @property
    def delay(self):
        return self.__delay
    @delay.setter
    def delay(self, delay: int):
        self.__delay = delay

    @property
    def moveDistance(self):
        return self.__moveDistance
    @moveDistance.setter
    def moveDistance(self, moveDistance: int):
        self.__moveDistance = moveDistance

    @property
    def swapTimer(self):
        return self.__swapTimer
    @swapTimer.setter
    def swapTimer(self, swapTimer: str):
        self.__swapTimer = swapTimer

    @property
    def BOARD_HEIGHT(self):
        return self.__BOARD_HEIGHT
    @BOARD_HEIGHT.setter
    def BOARD_HEIGHT(self, BOARD_HEIGHT: int):
        self.__BOARD_HEIGHT = BOARD_HEIGHT

    @property
    def crushTimerCount(self):
        return self.__crushTimerCount
    @crushTimerCount.setter
    def crushTimerCount(self, crushTimerCount: int):
        self.__crushTimerCount = crushTimerCount

    @property
    def game3(self):
        return self.__game3
    @game3.setter
    def game3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_candyCrushPackage_Board__game3", None)
        self.__game3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "board2"):
                opp_val = getattr(old_value, "board2", None)
                if opp_val == self:
                    setattr(old_value, "board2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "board2"):
                opp_val = getattr(value, "board2", None)
                setattr(value, "board2", self)

    @property
    def candiesButtons12(self):
        return self.__candiesButtons12
    @candiesButtons12.setter
    def candiesButtons12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_candyCrushPackage_Board__candiesButtons12", None)
        self.__candiesButtons12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "board13"):
                    opp_val = getattr(item, "board13", None)
                    
                    if opp_val == self:
                        setattr(item, "board13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "board13"):
                    opp_val = getattr(item, "board13", None)
                    
                    setattr(item, "board13", self)
                    

    @property
    def candies10(self):
        return self.__candies10
    @candies10.setter
    def candies10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_candyCrushPackage_Board__candies10", None)
        self.__candies10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "board11"):
                    opp_val = getattr(item, "board11", None)
                    
                    if opp_val == self:
                        setattr(item, "board11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "board11"):
                    opp_val = getattr(item, "board11", None)
                    
                    setattr(item, "board11", self)
                    



class candyCrushPackage_Menu:

    def __init__(self, menuBGColor: str, buttonBGColor: str, highScoreLabel: str, movesLabel: str, game1: "candyCrushPackage_Game" = None, color14: "Color_external" = None):
        self.menuBGColor = menuBGColor
        self.buttonBGColor = buttonBGColor
        self.highScoreLabel = highScoreLabel
        self.movesLabel = movesLabel
        self.game1 = game1
        self.color14 = color14
        
        pass
    @property
    def highScoreLabel(self):
        return self.__highScoreLabel
    @highScoreLabel.setter
    def highScoreLabel(self, highScoreLabel: str):
        self.__highScoreLabel = highScoreLabel

    @property
    def buttonBGColor(self):
        return self.__buttonBGColor
    @buttonBGColor.setter
    def buttonBGColor(self, buttonBGColor: str):
        self.__buttonBGColor = buttonBGColor

    @property
    def movesLabel(self):
        return self.__movesLabel
    @movesLabel.setter
    def movesLabel(self, movesLabel: str):
        self.__movesLabel = movesLabel

    @property
    def menuBGColor(self):
        return self.__menuBGColor
    @menuBGColor.setter
    def menuBGColor(self, menuBGColor: str):
        self.__menuBGColor = menuBGColor

    @property
    def color14(self):
        return self.__color14
    @color14.setter
    def color14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_candyCrushPackage_Menu__color14", None)
        self.__color14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "menu15"):
                opp_val = getattr(old_value, "menu15", None)
                if opp_val == self:
                    setattr(old_value, "menu15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "menu15"):
                opp_val = getattr(value, "menu15", None)
                setattr(value, "menu15", self)

    @property
    def game1(self):
        return self.__game1
    @game1.setter
    def game1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_candyCrushPackage_Menu__game1", None)
        self.__game1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "menu0"):
                opp_val = getattr(old_value, "menu0", None)
                if opp_val == self:
                    setattr(old_value, "menu0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "menu0"):
                opp_val = getattr(value, "menu0", None)
                setattr(value, "menu0", self)



class candyCrushPackage_Game:

    def __init__(self, SEP: str, IMAGES_PATH: str, SOUNDS_PATH: str, WINDOW_WIDTH: int, WINDOW_HEIGHT: int, playerName: str, score: int, menu0: "candyCrushPackage_Menu" = None, board2: "candyCrushPackage_Board" = None):
        self.SEP = SEP
        self.IMAGES_PATH = IMAGES_PATH
        self.SOUNDS_PATH = SOUNDS_PATH
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT
        self.playerName = playerName
        self.score = score
        self.menu0 = menu0
        self.board2 = board2
        
        pass
    @property
    def playerName(self):
        return self.__playerName
    @playerName.setter
    def playerName(self, playerName: str):
        self.__playerName = playerName

    @property
    def SOUNDS_PATH(self):
        return self.__SOUNDS_PATH
    @SOUNDS_PATH.setter
    def SOUNDS_PATH(self, SOUNDS_PATH: str):
        self.__SOUNDS_PATH = SOUNDS_PATH

    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, score: int):
        self.__score = score

    @property
    def SEP(self):
        return self.__SEP
    @SEP.setter
    def SEP(self, SEP: str):
        self.__SEP = SEP

    @property
    def WINDOW_HEIGHT(self):
        return self.__WINDOW_HEIGHT
    @WINDOW_HEIGHT.setter
    def WINDOW_HEIGHT(self, WINDOW_HEIGHT: int):
        self.__WINDOW_HEIGHT = WINDOW_HEIGHT

    @property
    def IMAGES_PATH(self):
        return self.__IMAGES_PATH
    @IMAGES_PATH.setter
    def IMAGES_PATH(self, IMAGES_PATH: str):
        self.__IMAGES_PATH = IMAGES_PATH

    @property
    def WINDOW_WIDTH(self):
        return self.__WINDOW_WIDTH
    @WINDOW_WIDTH.setter
    def WINDOW_WIDTH(self, WINDOW_WIDTH: int):
        self.__WINDOW_WIDTH = WINDOW_WIDTH

    @property
    def board2(self):
        return self.__board2
    @board2.setter
    def board2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_candyCrushPackage_Game__board2", None)
        self.__board2 = value
        
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

    @property
    def menu0(self):
        return self.__menu0
    @menu0.setter
    def menu0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_candyCrushPackage_Game__menu0", None)
        self.__menu0 = value
        
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



class candyCrushPackage_RegularCandy:

    def __init__(self, selfCrush: bool, selfCrushRange: int):
        self.selfCrush = selfCrush
        self.selfCrushRange = selfCrushRange
        
        pass
    @property
    def selfCrush(self):
        return self.__selfCrush
    @selfCrush.setter
    def selfCrush(self, selfCrush: bool):
        self.__selfCrush = selfCrush

    @property
    def selfCrushRange(self):
        return self.__selfCrushRange
    @selfCrushRange.setter
    def selfCrushRange(self, selfCrushRange: int):
        self.__selfCrushRange = selfCrushRange



class candyCrushPackage_Visited_Interface:

    pass


class candyCrushPackage_Visitor_Interface:

    pass


class candyCrushPackage_Candy(ABC):

    def __init__(self, color: int, row: int, col: int, board8: set["candyCrushPackage_Candy"] = None, candy9: "candyCrushPackage_Candy" = None, board11: "candyCrushPackage_Board" = None):
        self.color = color
        self.row = row
        self.col = col
        self.board8 = board8 if board8 is not None else set()
        self.candy9 = candy9
        self.board11 = board11
        
        pass
    @property
    def row(self):
        return self.__row
    @row.setter
    def row(self, row: int):
        self.__row = row

    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color: int):
        self.__color = color

    @property
    def col(self):
        return self.__col
    @col.setter
    def col(self, col: int):
        self.__col = col

    @property
    def board8(self):
        return self.__board8
    @board8.setter
    def board8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_candyCrushPackage_Candy__board8", None)
        self.__board8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "candy9"):
                    opp_val = getattr(item, "candy9", None)
                    
                    if opp_val == self:
                        setattr(item, "candy9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "candy9"):
                    opp_val = getattr(item, "candy9", None)
                    
                    setattr(item, "candy9", self)
                    

    @property
    def board11(self):
        return self.__board11
    @board11.setter
    def board11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_candyCrushPackage_Candy__board11", None)
        self.__board11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "candies10"):
                opp_val = getattr(old_value, "candies10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "candies10"):
                opp_val = getattr(value, "candies10", None)
                if opp_val is None:
                    setattr(value, "candies10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def candy9(self):
        return self.__candy9
    @candy9.setter
    def candy9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_candyCrushPackage_Candy__candy9", None)
        self.__candy9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "board8"):
                opp_val = getattr(old_value, "board8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "board8"):
                opp_val = getattr(value, "board8", None)
                if opp_val is None:
                    setattr(value, "board8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class JButton_external:

    pass


class ImageIcon_external:

    pass
