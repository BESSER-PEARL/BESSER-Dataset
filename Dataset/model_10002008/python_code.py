from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################










class genmymodelreverse_javax_swing_JFrame:

    pass


class genmymodelreverse_javax_swing_Timer:

    pass


class genmymodelreverse_javax_swing_JPanel:

    pass


class genmymodelreverse_java_awt_event_KeyEvent:

    pass


class genmymodelreverse_java_awt_event_KeyAdapter(ABC):

    pass


class genmymodelreverse_java_awt_event_ActionListener_Interface(ABC):

    pass


class genmymodelreverse_java_awt_event_ActionEvent:

    pass


class genmymodelreverse_java_awt_Graphics(ABC):

    pass


class genmymodelreverse_java_nio_charset_Charset(ABC):

    pass


class genmymodelreverse_java_io_IOException:

    pass


class genmymodelreverse_java_awt_Image(ABC):

    pass


class snake_Main:

    def __init__(self, serialVersionUID: int):
        self.serialVersionUID = serialVersionUID
        
        pass
    @property
    def serialVersionUID(self):
        return self.__serialVersionUID
    @serialVersionUID.setter
    def serialVersionUID(self, serialVersionUID: int):
        self.__serialVersionUID = serialVersionUID



class snake_TAdapter:

    pass


class snake_GameScene:

    def __init__(self, serialVersionUID: int, B_WIDTH: int, B_HEIGHT: int, DOT_SIZE: int, ALL_DOTS: int, RAND_POS: int, DELAY: int, x: str, y: str, bodyLength: int, apple_x: int, apple_y: int, myScore: int, level: int, leftDirection: bool, rightDirection: bool, upDirection: bool, downDirection: bool, inGame: bool, timer: genmymodelreverse_javax_swing_Timer, bodySegment: genmymodelreverse_java_awt_Image, apple: genmymodelreverse_java_awt_Image, head: genmymodelreverse_java_awt_Image, bg: genmymodelreverse_java_awt_Image):
        self.serialVersionUID = serialVersionUID
        self.B_WIDTH = B_WIDTH
        self.B_HEIGHT = B_HEIGHT
        self.DOT_SIZE = DOT_SIZE
        self.ALL_DOTS = ALL_DOTS
        self.RAND_POS = RAND_POS
        self.DELAY = DELAY
        self.x = x
        self.y = y
        self.bodyLength = bodyLength
        self.apple_x = apple_x
        self.apple_y = apple_y
        self.myScore = myScore
        self.level = level
        self.leftDirection = leftDirection
        self.rightDirection = rightDirection
        self.upDirection = upDirection
        self.downDirection = downDirection
        self.inGame = inGame
        self.timer = timer
        self.bodySegment = bodySegment
        self.apple = apple
        self.head = head
        self.bg = bg
        
        pass
    @property
    def level(self):
        return self.__level
    @level.setter
    def level(self, level: int):
        self.__level = level

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x: str):
        self.__x = x

    @property
    def leftDirection(self):
        return self.__leftDirection
    @leftDirection.setter
    def leftDirection(self, leftDirection: bool):
        self.__leftDirection = leftDirection

    @property
    def inGame(self):
        return self.__inGame
    @inGame.setter
    def inGame(self, inGame: bool):
        self.__inGame = inGame

    @property
    def head(self):
        return self.__head
    @head.setter
    def head(self, head: genmymodelreverse_java_awt_Image):
        self.__head = head

    @property
    def upDirection(self):
        return self.__upDirection
    @upDirection.setter
    def upDirection(self, upDirection: bool):
        self.__upDirection = upDirection

    @property
    def downDirection(self):
        return self.__downDirection
    @downDirection.setter
    def downDirection(self, downDirection: bool):
        self.__downDirection = downDirection

    @property
    def apple_y(self):
        return self.__apple_y
    @apple_y.setter
    def apple_y(self, apple_y: int):
        self.__apple_y = apple_y

    @property
    def apple(self):
        return self.__apple
    @apple.setter
    def apple(self, apple: genmymodelreverse_java_awt_Image):
        self.__apple = apple

    @property
    def bodyLength(self):
        return self.__bodyLength
    @bodyLength.setter
    def bodyLength(self, bodyLength: int):
        self.__bodyLength = bodyLength

    @property
    def B_WIDTH(self):
        return self.__B_WIDTH
    @B_WIDTH.setter
    def B_WIDTH(self, B_WIDTH: int):
        self.__B_WIDTH = B_WIDTH

    @property
    def bg(self):
        return self.__bg
    @bg.setter
    def bg(self, bg: genmymodelreverse_java_awt_Image):
        self.__bg = bg

    @property
    def serialVersionUID(self):
        return self.__serialVersionUID
    @serialVersionUID.setter
    def serialVersionUID(self, serialVersionUID: int):
        self.__serialVersionUID = serialVersionUID

    @property
    def RAND_POS(self):
        return self.__RAND_POS
    @RAND_POS.setter
    def RAND_POS(self, RAND_POS: int):
        self.__RAND_POS = RAND_POS

    @property
    def apple_x(self):
        return self.__apple_x
    @apple_x.setter
    def apple_x(self, apple_x: int):
        self.__apple_x = apple_x

    @property
    def rightDirection(self):
        return self.__rightDirection
    @rightDirection.setter
    def rightDirection(self, rightDirection: bool):
        self.__rightDirection = rightDirection

    @property
    def B_HEIGHT(self):
        return self.__B_HEIGHT
    @B_HEIGHT.setter
    def B_HEIGHT(self, B_HEIGHT: int):
        self.__B_HEIGHT = B_HEIGHT

    @property
    def ALL_DOTS(self):
        return self.__ALL_DOTS
    @ALL_DOTS.setter
    def ALL_DOTS(self, ALL_DOTS: int):
        self.__ALL_DOTS = ALL_DOTS

    @property
    def timer(self):
        return self.__timer
    @timer.setter
    def timer(self, timer: genmymodelreverse_javax_swing_Timer):
        self.__timer = timer

    @property
    def myScore(self):
        return self.__myScore
    @myScore.setter
    def myScore(self, myScore: int):
        self.__myScore = myScore

    @property
    def bodySegment(self):
        return self.__bodySegment
    @bodySegment.setter
    def bodySegment(self, bodySegment: genmymodelreverse_java_awt_Image):
        self.__bodySegment = bodySegment

    @property
    def DOT_SIZE(self):
        return self.__DOT_SIZE
    @DOT_SIZE.setter
    def DOT_SIZE(self, DOT_SIZE: int):
        self.__DOT_SIZE = DOT_SIZE

    @property
    def DELAY(self):
        return self.__DELAY
    @DELAY.setter
    def DELAY(self, DELAY: int):
        self.__DELAY = DELAY

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y: str):
        self.__y = y



class snake_Backgrounds:

    def __init__(self, backgrounds: genmymodelreverse_java_awt_Image):
        self.backgrounds = backgrounds
        
        pass
    @property
    def backgrounds(self):
        return self.__backgrounds
    @backgrounds.setter
    def backgrounds(self, backgrounds: genmymodelreverse_java_awt_Image):
        self.__backgrounds = backgrounds

