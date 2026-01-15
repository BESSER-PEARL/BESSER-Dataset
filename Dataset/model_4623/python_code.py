from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Orientation(Enum):
    HORIZONTAL = "HORIZONTAL"
    VERTICAL = "VERTICAL"
    LEFT_DIAGONAL = "LEFT_DIAGONAL"
    RIGHT_DIAGONAL = "RIGHT_DIAGONAL"
class LineTextureType(Enum):
    INVISIBLE = "INVISIBLE"
    SOLID = "SOLID"
    DASH = "DASH"
    DOT = "DOT"
    DASHDOT = "DASHDOT"
    DASHDOTDOT = "DASHDOTDOT"
    DOUBLE = "DOUBLE"
class FillTextureType(Enum):
    NONE = "NONE"
    STRIP = "STRIP"
    DASH = "DASH"
    DOT = "DOT"
    DASHDOT = "DASHDOT"
    DASHDOTDOT = "DASHDOTDOT"
class IconType(Enum):
    CROSS = "CROSS"
    ARROW = "ARROW"
    LETTER = "LETTER"
class DefinitionType(Enum):
    GRAPHICAL = "GRAPHICAL"
    TEXTUAL = "TEXTUAL"
    HYBRID = "HYBRID"
class AudienceType(Enum):
    EXPERT = "EXPERT"
    BEGINNER = "BEGINNER"
    BOTH = "BOTH"
class Color(Enum):
    RED = "RED"
    ORANGE = "ORANGE"
    YELLOW = "YELLOW"
    GREEN = "GREEN"
    LIGHT_GREEN = "LIGHT_GREEN"
    DARK_GREEN = "DARK_GREEN"
    CYAN = "CYAN"
    LIGHT_BLUE = "LIGHT_BLUE"
    BLUE = "BLUE"
    DARK_BLUE = "DARK_BLUE"
    WHITE = "WHITE"
    BLACK = "BLACK"
    LIGHT_GRAY = "LIGHT_GRAY"
    GRAY = "GRAY"
    DARK_GRAY = "DARK_GRAY"
class Layout(Enum):
    HORIZONTAL = "HORIZONTAL"
    VERTICAL = "VERTICAL"
    UNKNOWN = "UNKNOWN"


############################################
# Definition of Classes
############################################

class Style:

    pass
class notation_Style(ABC):

    pass
class Value:

    pass
class notation_ReferenceValue(Value):

    pass
class notation_AttributeValue(Value):

    pass
class TextualElement:

    pass
class notation_Value(TextualElement):

    pass
class notation_Keyword(TextualElement):

    pass
class notation_Token(TextualElement):

    pass
class notation_Point:

    def __init__(self, x: int, y: int, notation_Point: "notation_Polyline" = None):
        self.x = x
        self.y = y
        self.notation_Point = notation_Point
        
    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x

    @property
    def notation_Point(self):
        return self.__notation_Point

    @notation_Point.setter
    def notation_Point(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_Point__notation_Point", None)
        self.__notation_Point = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "notation_Polyline"):
                opp_val = getattr(old_value, "notation_Polyline", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "notation_Polyline"):
                opp_val = getattr(value, "notation_Polyline", None)
                if opp_val is None:
                    setattr(value, "notation_Polyline", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Figure:

    pass
class notation_Square(Figure):

    pass
class notation_Cylinder(Figure):

    pass
class notation_Circle(Figure):

    pass
class notation_Diamond(Figure):

    pass
class notation_Roundtangle(Figure):

    pass
class notation_Polyline(Figure):

    pass
class notation_Cube(Figure):

    pass
class notation_Triangle(Figure):

    pass
class notation_Rectangle(Figure):

    pass
class notation_LineStyle(Style):

    def __init__(self, thickness: float, color: str, orientation: str, length: float, brightness: int, texture: str, notation_LineStyle: "notation_Line" = None):
        self.thickness = thickness
        self.color = color
        self.orientation = orientation
        self.length = length
        self.brightness = brightness
        self.texture = texture
        self.notation_LineStyle = notation_LineStyle
        
    @property
    def length(self) -> float:
        return self.__length

    @length.setter
    def length(self, length: float):
        self.__length = length

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def thickness(self) -> float:
        return self.__thickness

    @thickness.setter
    def thickness(self, thickness: float):
        self.__thickness = thickness

    @property
    def texture(self) -> str:
        return self.__texture

    @texture.setter
    def texture(self, texture: str):
        self.__texture = texture

    @property
    def brightness(self) -> int:
        return self.__brightness

    @brightness.setter
    def brightness(self, brightness: int):
        self.__brightness = brightness

    @property
    def orientation(self) -> str:
        return self.__orientation

    @orientation.setter
    def orientation(self, orientation: str):
        self.__orientation = orientation

    @property
    def notation_LineStyle(self):
        return self.__notation_LineStyle

    @notation_LineStyle.setter
    def notation_LineStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_LineStyle__notation_LineStyle", None)
        self.__notation_LineStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "notation_Line"):
                opp_val = getattr(old_value, "notation_Line", None)
                if opp_val == self:
                    setattr(old_value, "notation_Line", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "notation_Line"):
                opp_val = getattr(value, "notation_Line", None)
                setattr(value, "notation_Line", self)

class notation_TextualContainment:

    def __init__(self, layout: str, notation_TextualContainment: "notation_Label" = None, notation_TextualContainment32: set["notation_TextualElement"] = None):
        self.layout = layout
        self.notation_TextualContainment = notation_TextualContainment
        self.notation_TextualContainment32 = notation_TextualContainment32 if notation_TextualContainment32 is not None else set()
        
    @property
    def layout(self) -> str:
        return self.__layout

    @layout.setter
    def layout(self, layout: str):
        self.__layout = layout

    @property
    def notation_TextualContainment32(self):
        return self.__notation_TextualContainment32

    @notation_TextualContainment32.setter
    def notation_TextualContainment32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_TextualContainment__notation_TextualContainment32", None)
        self.__notation_TextualContainment32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "notation_TextualElement"):
                    opp_val = getattr(item, "notation_TextualElement", None)
                    
                    if opp_val == self:
                        setattr(item, "notation_TextualElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "notation_TextualElement"):
                    opp_val = getattr(item, "notation_TextualElement", None)
                    
                    setattr(item, "notation_TextualElement", self)
                    

    @property
    def notation_TextualContainment(self):
        return self.__notation_TextualContainment

    @notation_TextualContainment.setter
    def notation_TextualContainment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_TextualContainment__notation_TextualContainment", None)
        self.__notation_TextualContainment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "notation_Label20"):
                opp_val = getattr(old_value, "notation_Label20", None)
                if opp_val == self:
                    setattr(old_value, "notation_Label20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "notation_Label20"):
                opp_val = getattr(value, "notation_Label20", None)
                setattr(value, "notation_Label20", self)

class notation_TextStyle(Style):

    def __init__(self, fontSize: int, fontName: str, bold: bool, italic: bool, underlined: bool, fontColor: str, notation_TextStyle: "notation_Label" = None):
        self.fontSize = fontSize
        self.fontName = fontName
        self.bold = bold
        self.italic = italic
        self.underlined = underlined
        self.fontColor = fontColor
        self.notation_TextStyle = notation_TextStyle
        
    @property
    def fontName(self) -> str:
        return self.__fontName

    @fontName.setter
    def fontName(self, fontName: str):
        self.__fontName = fontName

    @property
    def italic(self) -> bool:
        return self.__italic

    @italic.setter
    def italic(self, italic: bool):
        self.__italic = italic

    @property
    def fontSize(self) -> int:
        return self.__fontSize

    @fontSize.setter
    def fontSize(self, fontSize: int):
        self.__fontSize = fontSize

    @property
    def underlined(self) -> bool:
        return self.__underlined

    @underlined.setter
    def underlined(self, underlined: bool):
        self.__underlined = underlined

    @property
    def bold(self) -> bool:
        return self.__bold

    @bold.setter
    def bold(self, bold: bool):
        self.__bold = bold

    @property
    def fontColor(self) -> str:
        return self.__fontColor

    @fontColor.setter
    def fontColor(self, fontColor: str):
        self.__fontColor = fontColor

    @property
    def notation_TextStyle(self):
        return self.__notation_TextStyle

    @notation_TextStyle.setter
    def notation_TextStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_TextStyle__notation_TextStyle", None)
        self.__notation_TextStyle = value
        
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

class notation_IconStyle(Style):

    def __init__(self, width: float, height: float, orientation: str, brightness: int, color: str, notation_IconStyle: "notation_Icon" = None):
        self.width = width
        self.height = height
        self.orientation = orientation
        self.brightness = brightness
        self.color = color
        self.notation_IconStyle = notation_IconStyle
        
    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, width: float):
        self.__width = width

    @property
    def brightness(self) -> int:
        return self.__brightness

    @brightness.setter
    def brightness(self, brightness: int):
        self.__brightness = brightness

    @property
    def height(self) -> float:
        return self.__height

    @height.setter
    def height(self, height: float):
        self.__height = height

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def orientation(self) -> str:
        return self.__orientation

    @orientation.setter
    def orientation(self, orientation: str):
        self.__orientation = orientation

    @property
    def notation_IconStyle(self):
        return self.__notation_IconStyle

    @notation_IconStyle.setter
    def notation_IconStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_IconStyle__notation_IconStyle", None)
        self.__notation_IconStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "notation_Icon"):
                opp_val = getattr(old_value, "notation_Icon", None)
                if opp_val == self:
                    setattr(old_value, "notation_Icon", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "notation_Icon"):
                opp_val = getattr(value, "notation_Icon", None)
                setattr(value, "notation_Icon", self)

class GraphicalElement:

    pass
class notation_Image(GraphicalElement):

    def __init__(self, path: str, notation_Image: "notation_GraphicalElement" = None):
        self.path = path
        self.notation_Image = notation_Image
        
    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

    @property
    def notation_Image(self):
        return self.__notation_Image

    @notation_Image.setter
    def notation_Image(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_Image__notation_Image", None)
        self.__notation_Image = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "notation_GraphicalElement12"):
                opp_val = getattr(old_value, "notation_GraphicalElement12", None)
                if opp_val == self:
                    setattr(old_value, "notation_GraphicalElement12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "notation_GraphicalElement12"):
                opp_val = getattr(value, "notation_GraphicalElement12", None)
                setattr(value, "notation_GraphicalElement12", self)

class notation_Icon(GraphicalElement):

    def __init__(self, iconType: str, notation_Icon: "notation_IconStyle" = None):
        self.iconType = iconType
        self.notation_Icon = notation_Icon
        
    @property
    def iconType(self) -> str:
        return self.__iconType

    @iconType.setter
    def iconType(self, iconType: str):
        self.__iconType = iconType

    @property
    def notation_Icon(self):
        return self.__notation_Icon

    @notation_Icon.setter
    def notation_Icon(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_Icon__notation_Icon", None)
        self.__notation_Icon = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "notation_IconStyle"):
                opp_val = getattr(old_value, "notation_IconStyle", None)
                if opp_val == self:
                    setattr(old_value, "notation_IconStyle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "notation_IconStyle"):
                opp_val = getattr(value, "notation_IconStyle", None)
                setattr(value, "notation_IconStyle", self)

class notation_Composite(GraphicalElement):

    def __init__(self, layout: str, notation_Composite: set["notation_GraphicalElement"] = None, notation_Composite16: "notation_GraphicalElement" = None):
        self.layout = layout
        self.notation_Composite = notation_Composite if notation_Composite is not None else set()
        self.notation_Composite16 = notation_Composite16
        
    @property
    def layout(self) -> str:
        return self.__layout

    @layout.setter
    def layout(self, layout: str):
        self.__layout = layout

    @property
    def notation_Composite(self):
        return self.__notation_Composite

    @notation_Composite.setter
    def notation_Composite(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_Composite__notation_Composite", None)
        self.__notation_Composite = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "notation_GraphicalElement14"):
                    opp_val = getattr(item, "notation_GraphicalElement14", None)
                    
                    if opp_val == self:
                        setattr(item, "notation_GraphicalElement14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "notation_GraphicalElement14"):
                    opp_val = getattr(item, "notation_GraphicalElement14", None)
                    
                    setattr(item, "notation_GraphicalElement14", self)
                    

    @property
    def notation_Composite16(self):
        return self.__notation_Composite16

    @notation_Composite16.setter
    def notation_Composite16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_Composite__notation_Composite16", None)
        self.__notation_Composite16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "notation_GraphicalElement17"):
                opp_val = getattr(old_value, "notation_GraphicalElement17", None)
                if opp_val == self:
                    setattr(old_value, "notation_GraphicalElement17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "notation_GraphicalElement17"):
                opp_val = getattr(value, "notation_GraphicalElement17", None)
                setattr(value, "notation_GraphicalElement17", self)

class notation_Line(GraphicalElement):

    pass
class notation_Label(GraphicalElement):

    pass
class notation_SyntaxOf(GraphicalElement):

    pass
class notation_FigureContainment:

    def __init__(self, layout: str, notation_FigureContainment: "notation_Figure" = None, notation_FigureContainment28: set["notation_GraphicalElement"] = None):
        self.layout = layout
        self.notation_FigureContainment = notation_FigureContainment
        self.notation_FigureContainment28 = notation_FigureContainment28 if notation_FigureContainment28 is not None else set()
        
    @property
    def layout(self) -> str:
        return self.__layout

    @layout.setter
    def layout(self, layout: str):
        self.__layout = layout

    @property
    def notation_FigureContainment(self):
        return self.__notation_FigureContainment

    @notation_FigureContainment.setter
    def notation_FigureContainment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_FigureContainment__notation_FigureContainment", None)
        self.__notation_FigureContainment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "notation_Figure26"):
                opp_val = getattr(old_value, "notation_Figure26", None)
                if opp_val == self:
                    setattr(old_value, "notation_Figure26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "notation_Figure26"):
                opp_val = getattr(value, "notation_Figure26", None)
                setattr(value, "notation_Figure26", self)

    @property
    def notation_FigureContainment28(self):
        return self.__notation_FigureContainment28

    @notation_FigureContainment28.setter
    def notation_FigureContainment28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_FigureContainment__notation_FigureContainment28", None)
        self.__notation_FigureContainment28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "notation_GraphicalElement29"):
                    opp_val = getattr(item, "notation_GraphicalElement29", None)
                    
                    if opp_val == self:
                        setattr(item, "notation_GraphicalElement29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "notation_GraphicalElement29"):
                    opp_val = getattr(item, "notation_GraphicalElement29", None)
                    
                    setattr(item, "notation_GraphicalElement29", self)
                    

class notation_BorderStyle(Style):

    def __init__(self, thickness: float, color: str, texture: str, notation_BorderStyle: "notation_Figure" = None):
        self.thickness = thickness
        self.color = color
        self.texture = texture
        self.notation_BorderStyle = notation_BorderStyle
        
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def thickness(self) -> float:
        return self.__thickness

    @thickness.setter
    def thickness(self, thickness: float):
        self.__thickness = thickness

    @property
    def texture(self) -> str:
        return self.__texture

    @texture.setter
    def texture(self, texture: str):
        self.__texture = texture

    @property
    def notation_BorderStyle(self):
        return self.__notation_BorderStyle

    @notation_BorderStyle.setter
    def notation_BorderStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_BorderStyle__notation_BorderStyle", None)
        self.__notation_BorderStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "notation_Figure24"):
                opp_val = getattr(old_value, "notation_Figure24", None)
                if opp_val == self:
                    setattr(old_value, "notation_Figure24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "notation_Figure24"):
                opp_val = getattr(value, "notation_Figure24", None)
                setattr(value, "notation_Figure24", self)

class notation_FigureStyle(Style):

    def __init__(self, fillTexture: str, fillOrientation: str, fillTextureColor: str, width: float, height: float, orientation: str, brightness: int, fillColor: str, notation_FigureStyle: "notation_Figure" = None):
        self.fillTexture = fillTexture
        self.fillOrientation = fillOrientation
        self.fillTextureColor = fillTextureColor
        self.width = width
        self.height = height
        self.orientation = orientation
        self.brightness = brightness
        self.fillColor = fillColor
        self.notation_FigureStyle = notation_FigureStyle
        
    @property
    def height(self) -> float:
        return self.__height

    @height.setter
    def height(self, height: float):
        self.__height = height

    @property
    def fillTextureColor(self) -> str:
        return self.__fillTextureColor

    @fillTextureColor.setter
    def fillTextureColor(self, fillTextureColor: str):
        self.__fillTextureColor = fillTextureColor

    @property
    def fillOrientation(self) -> str:
        return self.__fillOrientation

    @fillOrientation.setter
    def fillOrientation(self, fillOrientation: str):
        self.__fillOrientation = fillOrientation

    @property
    def brightness(self) -> int:
        return self.__brightness

    @brightness.setter
    def brightness(self, brightness: int):
        self.__brightness = brightness

    @property
    def orientation(self) -> str:
        return self.__orientation

    @orientation.setter
    def orientation(self, orientation: str):
        self.__orientation = orientation

    @property
    def fillColor(self) -> str:
        return self.__fillColor

    @fillColor.setter
    def fillColor(self, fillColor: str):
        self.__fillColor = fillColor

    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, width: float):
        self.__width = width

    @property
    def fillTexture(self) -> str:
        return self.__fillTexture

    @fillTexture.setter
    def fillTexture(self, fillTexture: str):
        self.__fillTexture = fillTexture

    @property
    def notation_FigureStyle(self):
        return self.__notation_FigureStyle

    @notation_FigureStyle.setter
    def notation_FigureStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_FigureStyle__notation_FigureStyle", None)
        self.__notation_FigureStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "notation_Figure"):
                opp_val = getattr(old_value, "notation_Figure", None)
                if opp_val == self:
                    setattr(old_value, "notation_Figure", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "notation_Figure"):
                opp_val = getattr(value, "notation_Figure", None)
                setattr(value, "notation_Figure", self)

class notation_Figure(GraphicalElement):

    pass
class IDElement:

    pass
class notation_TextualElement(IDElement):

    pass
class notation_IDElement:

    def __init__(self, ID: str):
        self.ID = ID
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

class notation_DiagramElement(IDElement):

    pass
class notation_DiagramDefinition:

    def __init__(self, Legend: str, Level: int, allowChunks: bool, targetedAudience: str, notation_DiagramDefinition: "notation_NotationDefinition" = None, notation_DiagramDefinition2: set["notation_DiagramElement"] = None):
        self.Legend = Legend
        self.Level = Level
        self.allowChunks = allowChunks
        self.targetedAudience = targetedAudience
        self.notation_DiagramDefinition = notation_DiagramDefinition
        self.notation_DiagramDefinition2 = notation_DiagramDefinition2 if notation_DiagramDefinition2 is not None else set()
        
    @property
    def Level(self) -> int:
        return self.__Level

    @Level.setter
    def Level(self, Level: int):
        self.__Level = Level

    @property
    def targetedAudience(self) -> str:
        return self.__targetedAudience

    @targetedAudience.setter
    def targetedAudience(self, targetedAudience: str):
        self.__targetedAudience = targetedAudience

    @property
    def allowChunks(self) -> bool:
        return self.__allowChunks

    @allowChunks.setter
    def allowChunks(self, allowChunks: bool):
        self.__allowChunks = allowChunks

    @property
    def Legend(self) -> str:
        return self.__Legend

    @Legend.setter
    def Legend(self, Legend: str):
        self.__Legend = Legend

    @property
    def notation_DiagramDefinition2(self):
        return self.__notation_DiagramDefinition2

    @notation_DiagramDefinition2.setter
    def notation_DiagramDefinition2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_DiagramDefinition__notation_DiagramDefinition2", None)
        self.__notation_DiagramDefinition2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "notation_DiagramElement"):
                    opp_val = getattr(item, "notation_DiagramElement", None)
                    
                    if opp_val == self:
                        setattr(item, "notation_DiagramElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "notation_DiagramElement"):
                    opp_val = getattr(item, "notation_DiagramElement", None)
                    
                    setattr(item, "notation_DiagramElement", self)
                    

    @property
    def notation_DiagramDefinition(self):
        return self.__notation_DiagramDefinition

    @notation_DiagramDefinition.setter
    def notation_DiagramDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_DiagramDefinition__notation_DiagramDefinition", None)
        self.__notation_DiagramDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "notation_NotationDefinition"):
                opp_val = getattr(old_value, "notation_NotationDefinition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "notation_NotationDefinition"):
                opp_val = getattr(value, "notation_NotationDefinition", None)
                if opp_val is None:
                    setattr(value, "notation_NotationDefinition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class notation_NotationDefinition:

    def __init__(self, Type: str, notation_NotationDefinition: set["notation_DiagramDefinition"] = None):
        self.Type = Type
        self.notation_NotationDefinition = notation_NotationDefinition if notation_NotationDefinition is not None else set()
        
    @property
    def Type(self) -> str:
        return self.__Type

    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def notation_NotationDefinition(self):
        return self.__notation_NotationDefinition

    @notation_NotationDefinition.setter
    def notation_NotationDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_NotationDefinition__notation_NotationDefinition", None)
        self.__notation_NotationDefinition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "notation_DiagramDefinition"):
                    opp_val = getattr(item, "notation_DiagramDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "notation_DiagramDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "notation_DiagramDefinition"):
                    opp_val = getattr(item, "notation_DiagramDefinition", None)
                    
                    setattr(item, "notation_DiagramDefinition", self)
                    

class Relation:

    pass
class notation_Link(Relation):

    pass
class notation_Compartment(Relation):

    def __init__(self, layout: str, notation_Compartment: "notation_Node" = None):
        self.layout = layout
        self.notation_Compartment = notation_Compartment
        
    @property
    def layout(self) -> str:
        return self.__layout

    @layout.setter
    def layout(self, layout: str):
        self.__layout = layout

    @property
    def notation_Compartment(self):
        return self.__notation_Compartment

    @notation_Compartment.setter
    def notation_Compartment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_notation_Compartment__notation_Compartment", None)
        self.__notation_Compartment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "notation_Node5"):
                opp_val = getattr(old_value, "notation_Node5", None)
                if opp_val == self:
                    setattr(old_value, "notation_Node5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "notation_Node5"):
                opp_val = getattr(value, "notation_Node5", None)
                setattr(value, "notation_Node5", self)

class notation_GraphicalElement(IDElement):

    pass
class DiagramElement:

    pass
class notation_Relation(DiagramElement):

    pass
class notation_Node(DiagramElement):

    pass