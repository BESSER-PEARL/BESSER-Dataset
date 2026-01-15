from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Color(Enum):
    BLACK = "BLACK"
    RED = "RED"
    GREEN = "GREEN"
    BLUE = "BLUE"


############################################
# Definition of Classes
############################################

class notation_Definition:

    pass
class notation_EReference:

    pass
class Value:

    pass
class notation_ReferenceValue(Value):

    pass
class notation_AttributeValue(Value):

    pass
class notation_EAttribute:

    pass
class TextualElement:

    pass
class notation_Keyword(TextualElement):

    pass
class notation_Value(TextualElement):

    def __init__(self, separator: str, notation_Value: "notation_EAttribute" = None):
        self.separator = separator
        self.notation_Value = notation_Value
        
    @property
    def separator(self) -> str:
        return self.__separator

    @separator.setter
    def separator(self, separator: str):
        self.__separator = separator

    @property
    def notation_Value(self):
        return self.__notation_Value

    @notation_Value.setter
    def notation_Value(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_Value__notation_Value", None)
        self.__notation_Value = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "notation_EAttribute"):
                opp_val = getattr(old_value, "notation_EAttribute", None)
                if opp_val == self:
                    setattr(old_value, "notation_EAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "notation_EAttribute"):
                opp_val = getattr(value, "notation_EAttribute", None)
                setattr(value, "notation_EAttribute", self)

class notation_Token(TextualElement):

    pass
class Figure:

    pass
class notation_Rectangle(Figure):

    pass
class GraphicalElement:

    pass
class notation_Line(GraphicalElement):

    pass
class notation_Label(GraphicalElement):

    pass
class notation_Figure(GraphicalElement):

    pass
class NotationElement:

    pass
class notation_SyntaxOf(NotationElement):

    pass
class notation_TextualElement(NotationElement):

    def __init__(self, fill: str, notation_TextualElement: "notation_Label" = None):
        self.fill = fill
        self.notation_TextualElement = notation_TextualElement
        
    @property
    def fill(self) -> str:
        return self.__fill

    @fill.setter
    def fill(self, fill: str):
        self.__fill = fill

    @property
    def notation_TextualElement(self):
        return self.__notation_TextualElement

    @notation_TextualElement.setter
    def notation_TextualElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_TextualElement__notation_TextualElement", None)
        self.__notation_TextualElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "notation_Label"):
                opp_val = getattr(old_value, "notation_Label", None)
                if opp_val == self:
                    setattr(old_value, "notation_Label", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "notation_Label"):
                opp_val = getattr(value, "notation_Label", None)
                setattr(value, "notation_Label", self)

class notation_Composite(NotationElement):

    pass
class notation_GraphicalElement(NotationElement):

    def __init__(self, x: int, y: int, height: int, width: int, fill: str, stroke: str):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.fill = fill
        self.stroke = stroke
        
    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width

    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y

    @property
    def stroke(self) -> str:
        return self.__stroke

    @stroke.setter
    def stroke(self, stroke: str):
        self.__stroke = stroke

    @property
    def fill(self) -> str:
        return self.__fill

    @fill.setter
    def fill(self, fill: str):
        self.__fill = fill

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height

class IdElement:

    pass
class notation_NotationElement(IdElement):

    pass
class notation_IdElement(ABC):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id
