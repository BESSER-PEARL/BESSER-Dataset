from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class KnownColor(Enum):
    maroon = "maroon"
    red = "red"
    orange = "orange"
    yellow = "yellow"
    olive = "olive"
    white = "white"
    lime = "lime"
    green = "green"
    navy = "navy"
    blue = "blue"
    aqua = "aqua"
    teal = "teal"
    black = "black"
    purple = "purple"
    silver = "silver"
    fuchsia = "fuchsia"
    gray = "gray"


############################################
# Definition of Classes
############################################

class dc_Bounds:

    def __init__(self, x: str, y: str, width: str, height: str):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    @property
    def x(self) -> str:
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x

    @property
    def y(self) -> str:
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y

    @property
    def height(self) -> str:
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height

    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    def nonNegativeWidth(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement nonNegativeWidth method
        pass

    def nonNegativeHeight(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement nonNegativeHeight method
        pass

class dc_Dimension:

    def __init__(self, width: str, height: str):
        self.width = width
        self.height = height
        
    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def height(self) -> str:
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height

    def nonNegativeWidth(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement nonNegativeWidth method
        pass

    def nonNegativeHeight(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement nonNegativeHeight method
        pass

class dc_Point:

    def __init__(self, x: str, y: str):
        self.x = x
        self.y = y
        
    @property
    def y(self) -> str:
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y

    @property
    def x(self) -> str:
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x
