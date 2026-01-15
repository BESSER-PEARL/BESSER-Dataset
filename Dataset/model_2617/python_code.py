from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class DLayout(Enum):
    none = "none"
    free = "free"
    horizontal = "horizontal"
    vertical = "vertical"
class DLine(Enum):
    solid = "solid"
    dash = "dash"
    dot = "dot"
    dashdot = "dashdot"
    dashdotdot = "dashdotdot"
    custom = "custom"
class DColor(Enum):
    white = "white"
    black = "black"
    lightGray = "lightGray"
    gray = "gray"
    darkGray = "darkGray"
    lightGreen = "lightGreen"
    darkGreen = "darkGreen"
    cyan = "cyan"
    lightBlue = "lightBlue"
    blue = "blue"
    darkBlue = "darkBlue"
    red = "red"
    orange = "orange"
    yellow = "yellow"
    green = "green"
class DFontStyle(Enum):
    normal = "normal"
    bold = "bold"
    italic = "italic"
class DShape(Enum):
    rectangle = "rectangle"
    roundedRectangle = "roundedRectangle"
    ellipse = "ellipse"
    dot = "dot"
    custom = "custom"
    arrow = "arrow"
    triangle = "triangle"
class DDirection(Enum):
    none = "none"
    left = "left"
    right = "right"
    bidirectional = "bidirectional"
class DFontName(Enum):
    arial = "arial"
    courier = "courier"
    times = "times"
class DAlignment(Enum):
    fill = "fill"
    beginning = "beginning"
    center = "center"
    end = "end"


############################################
# Definition of Classes
############################################

class DNodeEdgeStyle:

    pass
class diastyle_DEdgeStyle(DNodeEdgeStyle):

    def __init__(self, arrowDirection: str, arrowSize: int, shape: str):
        self.arrowDirection = arrowDirection
        self.arrowSize = arrowSize
        self.shape = shape
        
    @property
    def arrowSize(self) -> int:
        return self.__arrowSize

    @arrowSize.setter
    def arrowSize(self, arrowSize: int):
        self.__arrowSize = arrowSize

    @property
    def shape(self) -> str:
        return self.__shape

    @shape.setter
    def shape(self, shape: str):
        self.__shape = shape

    @property
    def arrowDirection(self) -> str:
        return self.__arrowDirection

    @arrowDirection.setter
    def arrowDirection(self, arrowDirection: str):
        self.__arrowDirection = arrowDirection

class diastyle_DNodeStyle(DNodeEdgeStyle):

    def __init__(self, radius: int, shape: str, sizeY: int, figure: str, shapeData: str, layout: str, sizeX: int):
        self.radius = radius
        self.shape = shape
        self.sizeY = sizeY
        self.figure = figure
        self.shapeData = shapeData
        self.layout = layout
        self.sizeX = sizeX
        
    @property
    def sizeX(self) -> int:
        return self.__sizeX

    @sizeX.setter
    def sizeX(self, sizeX: int):
        self.__sizeX = sizeX

    @property
    def radius(self) -> int:
        return self.__radius

    @radius.setter
    def radius(self, radius: int):
        self.__radius = radius

    @property
    def sizeY(self) -> int:
        return self.__sizeY

    @sizeY.setter
    def sizeY(self, sizeY: int):
        self.__sizeY = sizeY

    @property
    def figure(self) -> str:
        return self.__figure

    @figure.setter
    def figure(self, figure: str):
        self.__figure = figure

    @property
    def shapeData(self) -> str:
        return self.__shapeData

    @shapeData.setter
    def shapeData(self, shapeData: str):
        self.__shapeData = shapeData

    @property
    def shape(self) -> str:
        return self.__shape

    @shape.setter
    def shape(self, shape: str):
        self.__shape = shape

    @property
    def layout(self) -> str:
        return self.__layout

    @layout.setter
    def layout(self, layout: str):
        self.__layout = layout

class diastyle_DGraphElement:

    pass
class diastyle_DStyleBridge:

    def __init__(self, name: str, diastyle_DStyleBridge: "diastyle_DGraphElement" = None, diastyle_DStyleBridge6: "diastyle_DBaseStyle" = None):
        self.name = name
        self.diastyle_DStyleBridge = diastyle_DStyleBridge
        self.diastyle_DStyleBridge6 = diastyle_DStyleBridge6
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def diastyle_DStyleBridge6(self):
        return self.__diastyle_DStyleBridge6

    @diastyle_DStyleBridge6.setter
    def diastyle_DStyleBridge6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diastyle_DStyleBridge__diastyle_DStyleBridge6", None)
        self.__diastyle_DStyleBridge6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diastyle_DBaseStyle5"):
                opp_val = getattr(old_value, "diastyle_DBaseStyle5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diastyle_DBaseStyle5"):
                opp_val = getattr(value, "diastyle_DBaseStyle5", None)
                if opp_val is None:
                    setattr(value, "diastyle_DBaseStyle5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def diastyle_DStyleBridge(self):
        return self.__diastyle_DStyleBridge

    @diastyle_DStyleBridge.setter
    def diastyle_DStyleBridge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diastyle_DStyleBridge__diastyle_DStyleBridge", None)
        self.__diastyle_DStyleBridge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diastyle_DGraphElement"):
                opp_val = getattr(old_value, "diastyle_DGraphElement", None)
                if opp_val == self:
                    setattr(old_value, "diastyle_DGraphElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diastyle_DGraphElement"):
                opp_val = getattr(value, "diastyle_DGraphElement", None)
                setattr(value, "diastyle_DGraphElement", self)

class diastyle_DGraph:

    pass
class diastyle_DBaseStyle(ABC):

    def __init__(self, name: str, color: str, parentName: str, diastyle_DBaseStyle: "diastyle_DStyle" = None, diastyle_DBaseStyle5: set["diastyle_DStyleBridge"] = None, diastyle_DBaseStyle9: "diastyle_DBaseStyle" = None, diastyle_DBaseStyle7: "diastyle_DBaseStyle" = None):
        self.name = name
        self.color = color
        self.parentName = parentName
        self.diastyle_DBaseStyle = diastyle_DBaseStyle
        self.diastyle_DBaseStyle5 = diastyle_DBaseStyle5 if diastyle_DBaseStyle5 is not None else set()
        self.diastyle_DBaseStyle9 = diastyle_DBaseStyle9
        self.diastyle_DBaseStyle7 = diastyle_DBaseStyle7
        
    @property
    def parentName(self) -> str:
        return self.__parentName

    @parentName.setter
    def parentName(self, parentName: str):
        self.__parentName = parentName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def diastyle_DBaseStyle9(self):
        return self.__diastyle_DBaseStyle9

    @diastyle_DBaseStyle9.setter
    def diastyle_DBaseStyle9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diastyle_DBaseStyle__diastyle_DBaseStyle9", None)
        self.__diastyle_DBaseStyle9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diastyle_DBaseStyle7"):
                opp_val = getattr(old_value, "diastyle_DBaseStyle7", None)
                if opp_val == self:
                    setattr(old_value, "diastyle_DBaseStyle7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diastyle_DBaseStyle7"):
                opp_val = getattr(value, "diastyle_DBaseStyle7", None)
                setattr(value, "diastyle_DBaseStyle7", self)

    @property
    def diastyle_DBaseStyle(self):
        return self.__diastyle_DBaseStyle

    @diastyle_DBaseStyle.setter
    def diastyle_DBaseStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diastyle_DBaseStyle__diastyle_DBaseStyle", None)
        self.__diastyle_DBaseStyle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diastyle_DStyle"):
                opp_val = getattr(old_value, "diastyle_DStyle", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diastyle_DStyle"):
                opp_val = getattr(value, "diastyle_DStyle", None)
                if opp_val is None:
                    setattr(value, "diastyle_DStyle", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def diastyle_DBaseStyle5(self):
        return self.__diastyle_DBaseStyle5

    @diastyle_DBaseStyle5.setter
    def diastyle_DBaseStyle5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diastyle_DBaseStyle__diastyle_DBaseStyle5", None)
        self.__diastyle_DBaseStyle5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diastyle_DStyleBridge6"):
                    opp_val = getattr(item, "diastyle_DStyleBridge6", None)
                    
                    if opp_val == self:
                        setattr(item, "diastyle_DStyleBridge6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diastyle_DStyleBridge6"):
                    opp_val = getattr(item, "diastyle_DStyleBridge6", None)
                    
                    setattr(item, "diastyle_DStyleBridge6", self)
                    

    @property
    def diastyle_DBaseStyle7(self):
        return self.__diastyle_DBaseStyle7

    @diastyle_DBaseStyle7.setter
    def diastyle_DBaseStyle7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diastyle_DBaseStyle__diastyle_DBaseStyle7", None)
        self.__diastyle_DBaseStyle7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diastyle_DBaseStyle9"):
                opp_val = getattr(old_value, "diastyle_DBaseStyle9", None)
                if opp_val == self:
                    setattr(old_value, "diastyle_DBaseStyle9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diastyle_DBaseStyle9"):
                opp_val = getattr(value, "diastyle_DBaseStyle9", None)
                setattr(value, "diastyle_DBaseStyle9", self)

class DBaseStyle:

    pass
class diastyle_DNestingEdgeStyle(DBaseStyle):

    pass
class EModelElement:

    pass
class diastyle_DStyle(EModelElement):

    def __init__(self, styleHandler: str, diastyle_DStyle: set["diastyle_DBaseStyle"] = None, diastyle_DStyle2: "diastyle_DGraph" = None):
        self.styleHandler = styleHandler
        self.diastyle_DStyle = diastyle_DStyle if diastyle_DStyle is not None else set()
        self.diastyle_DStyle2 = diastyle_DStyle2
        
    @property
    def styleHandler(self) -> str:
        return self.__styleHandler

    @styleHandler.setter
    def styleHandler(self, styleHandler: str):
        self.__styleHandler = styleHandler

    @property
    def diastyle_DStyle(self):
        return self.__diastyle_DStyle

    @diastyle_DStyle.setter
    def diastyle_DStyle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diastyle_DStyle__diastyle_DStyle", None)
        self.__diastyle_DStyle = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diastyle_DBaseStyle"):
                    opp_val = getattr(item, "diastyle_DBaseStyle", None)
                    
                    if opp_val == self:
                        setattr(item, "diastyle_DBaseStyle", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diastyle_DBaseStyle"):
                    opp_val = getattr(item, "diastyle_DBaseStyle", None)
                    
                    setattr(item, "diastyle_DBaseStyle", self)
                    

    @property
    def diastyle_DStyle2(self):
        return self.__diastyle_DStyle2

    @diastyle_DStyle2.setter
    def diastyle_DStyle2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diastyle_DStyle__diastyle_DStyle2", None)
        self.__diastyle_DStyle2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diastyle_DGraph"):
                opp_val = getattr(old_value, "diastyle_DGraph", None)
                if opp_val == self:
                    setattr(old_value, "diastyle_DGraph", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diastyle_DGraph"):
                opp_val = getattr(value, "diastyle_DGraph", None)
                setattr(value, "diastyle_DGraph", self)

    def getIcon(self, element: str) -> str:
        # TODO: Implement getIcon method
        pass

    def getFigure(self, element: str) -> str:
        # TODO: Implement getFigure method
        pass

    def getBackgroundColor(self, element: str) -> str:
        # TODO: Implement getBackgroundColor method
        pass

class diastyle_DNodeEdgeStyle(DBaseStyle, EModelElement):

    def __init__(self, line: str, lineWidth: int, fontName: str, fontStyle: str, fontSize: int, fontColor: str, textAlignment: str, icon: str):
        self.line = line
        self.lineWidth = lineWidth
        self.fontName = fontName
        self.fontStyle = fontStyle
        self.fontSize = fontSize
        self.fontColor = fontColor
        self.textAlignment = textAlignment
        self.icon = icon
        
    @property
    def fontStyle(self) -> str:
        return self.__fontStyle

    @fontStyle.setter
    def fontStyle(self, fontStyle: str):
        self.__fontStyle = fontStyle

    @property
    def lineWidth(self) -> int:
        return self.__lineWidth

    @lineWidth.setter
    def lineWidth(self, lineWidth: int):
        self.__lineWidth = lineWidth

    @property
    def fontSize(self) -> int:
        return self.__fontSize

    @fontSize.setter
    def fontSize(self, fontSize: int):
        self.__fontSize = fontSize

    @property
    def fontColor(self) -> str:
        return self.__fontColor

    @fontColor.setter
    def fontColor(self, fontColor: str):
        self.__fontColor = fontColor

    @property
    def fontName(self) -> str:
        return self.__fontName

    @fontName.setter
    def fontName(self, fontName: str):
        self.__fontName = fontName

    @property
    def textAlignment(self) -> str:
        return self.__textAlignment

    @textAlignment.setter
    def textAlignment(self, textAlignment: str):
        self.__textAlignment = textAlignment

    @property
    def icon(self) -> str:
        return self.__icon

    @icon.setter
    def icon(self, icon: str):
        self.__icon = icon

    @property
    def line(self) -> str:
        return self.__line

    @line.setter
    def line(self, line: str):
        self.__line = line
