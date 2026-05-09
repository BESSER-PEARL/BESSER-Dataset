from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class KnownColor(Enum):
    green = "green"
    navy = "navy"
    blue = "blue"
    aqua = "aqua"
    teal = "teal"
    black = "black"
    silver = "silver"
    gray = "gray"
    maroon = "maroon"
    red = "red"
    orange = "orange"
    yellow = "yellow"
    olive = "olive"
    purple = "purple"
    fuchsia = "fuchsia"
    white = "white"
    lime = "lime"


############################################
# Definition of Classes
############################################

class dc_Dimension:

    def __init__(self, width: str, height: str):
        self.width = width
        self.height = height
        
        pass
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width


    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height


    def nonNegativeWidth(self, dc_context, dc_diagnostics) :
        # TODO: Implement nonNegativeWidth method
        pass

    def nonNegativeHeight(self, dc_diagnostics, dc_context) :
        # TODO: Implement nonNegativeHeight method
        pass

class dc_Point:

    def __init__(self, x: str, y: str):
        self.x = x
        self.y = y
        
        pass
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y


    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x


class dc_Bounds:

    def __init__(self, x: str, y: str, width: str, height: str):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        pass
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x


    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width


    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y


    def nonNegativeWidth(self, dc_diagnostics, dc_context) :
        # TODO: Implement nonNegativeWidth method
        pass

    def nonNegativeHeight(self, dc_context, dc_diagnostics) :
        # TODO: Implement nonNegativeHeight method
        pass
