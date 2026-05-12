from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class DecorationType(Enum):
    dtunderligne = "dtunderligne"
    dtoverligne = "dtoverligne"
    dtlinethrough = "dtlinethrough"
class StyleType(Enum):
    sttsolid = "sttsolid"
    sttdash = "sttdash"
    sttdot = "sttdot"
class ShapeType(Enum):
    shtline = "shtline"
    shtcurve = "shtcurve"
class RotationType(Enum):
    rtvertical = "rtvertical"
    rthorizontal = "rthorizontal"
    rtdiagonal = "rtdiagonal"
class AlignType(Enum):
    atleft = "atleft"
    atcenter = "atcenter"
    atright = "atright"


############################################
# Definition of Classes
############################################

class Place:

    pass
class Inscription:

    pass
class EdgeGraphics:

    pass
class NetContentElement:

    pass
class AnyElement:

    pass
class PNML_ToolSpecific:

    def __init__(self, tool: str, version: str, tools20: "Arc" = None, tools22: "Node" = None, PNML_ToolSpecific: set["AnyElement"] = None, tools: "NetElement" = None):
        self.tool = tool
        self.version = version
        self.tools20 = tools20
        self.tools22 = tools22
        self.PNML_ToolSpecific = PNML_ToolSpecific if PNML_ToolSpecific is not None else set()
        self.tools = tools
        
        pass
    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def tool(self):
        return self.__tool

    @tool.setter
    def tool(self, tool: str):
        self.__tool = tool


    @property
    def PNML_ToolSpecific(self):
        return self.__PNML_ToolSpecific

    @PNML_ToolSpecific.setter
    def PNML_ToolSpecific(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PNML_ToolSpecific__PNML_ToolSpecific", None)
        self.__PNML_ToolSpecific = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AnyElement"):
                    opp_val = getattr(item, "AnyElement", None)
                    
                    if opp_val == self:
                        setattr(item, "AnyElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AnyElement"):
                    opp_val = getattr(item, "AnyElement", None)
                    
                    setattr(item, "AnyElement", self)
                    

    @property
    def tools(self):
        return self.__tools

    @tools.setter
    def tools(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PNML_ToolSpecific__tools", None)
        self.__tools = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NetElement18"):
                opp_val = getattr(old_value, "NetElement18", None)
                if opp_val == self:
                    setattr(old_value, "NetElement18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NetElement18"):
                opp_val = getattr(value, "NetElement18", None)
                setattr(value, "NetElement18", self)

    @property
    def tools22(self):
        return self.__tools22

    @tools22.setter
    def tools22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PNML_ToolSpecific__tools22", None)
        self.__tools22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node"):
                opp_val = getattr(old_value, "Node", None)
                if opp_val == self:
                    setattr(old_value, "Node", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node"):
                opp_val = getattr(value, "Node", None)
                setattr(value, "Node", self)

    @property
    def tools20(self):
        return self.__tools20

    @tools20.setter
    def tools20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PNML_ToolSpecific__tools20", None)
        self.__tools20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Arc"):
                opp_val = getattr(old_value, "Arc", None)
                if opp_val == self:
                    setattr(old_value, "Arc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Arc"):
                opp_val = getattr(value, "Arc", None)
                setattr(value, "Arc", self)

class LabeledElement:

    pass
class PNML_Name(LabeledElement):

    pass
class PNML_Inscription(LabeledElement):

    pass
class PNML_InitialMarking(LabeledElement):

    pass
class PNML_Label:

    def __init__(self, text: str, labels: "LabeledElement" = None):
        self.text = text
        self.labels = labels
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def labels(self):
        return self.__labels

    @labels.setter
    def labels(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PNML_Label__labels", None)
        self.__labels = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LabeledElement"):
                opp_val = getattr(old_value, "LabeledElement", None)
                if opp_val == self:
                    setattr(old_value, "LabeledElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LabeledElement"):
                opp_val = getattr(value, "LabeledElement", None)
                setattr(value, "LabeledElement", self)

class AnnotationGraphics:

    pass
class Label:

    pass
class PNML_LabeledElement(ABC):

    pass
class Node:

    pass
class Arc:

    pass
class NetElement:

    pass
class URI:

    pass
class PNML_PNMLDocument:

    pass
class PNML_NetContent(ABC):

    pass
class Name:

    pass
class NetGraphics:

    pass
class ToolSpecific:

    pass
class NetContent:

    pass
class PNML_NetContentElement(NetContent):

    pass
class PNMLDocument:

    pass
class IdedElement:

    pass
class PNML_Arc(NetContent, IdedElement):

    pass
class PNML_Node(IdedElement):

    pass
class PNML_NetElement(IdedElement):

    pass
class PNML_IdedElement(ABC):

    def __init__(self, id: str):
        self.id = id
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


class PNML_AnyElement:

    def __init__(self, name: str, text: str):
        self.name = name
        self.text = text
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class PNML_Color:

    pass
class PNML_URI:

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class PNML_Font:

    def __init__(self, weight: str, size: str, decoration: str, align: str, rotation: str, family: str, style: str, font: "AnnotationGraphics" = None):
        self.weight = weight
        self.size = size
        self.decoration = decoration
        self.align = align
        self.rotation = rotation
        self.family = family
        self.style = style
        self.font = font
        
        pass
    @property
    def decoration(self):
        return self.__decoration

    @decoration.setter
    def decoration(self, decoration: str):
        self.__decoration = decoration


    @property
    def family(self):
        return self.__family

    @family.setter
    def family(self, family: str):
        self.__family = family


    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size


    @property
    def align(self):
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align


    @property
    def rotation(self):
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation: str):
        self.__rotation = rotation


    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight: str):
        self.__weight = weight


    @property
    def style(self):
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style


    @property
    def font(self):
        return self.__font

    @font.setter
    def font(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PNML_Font__font", None)
        self.__font = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AnnotationGraphics125"):
                opp_val = getattr(old_value, "AnnotationGraphics125", None)
                if opp_val == self:
                    setattr(old_value, "AnnotationGraphics125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AnnotationGraphics125"):
                opp_val = getattr(value, "AnnotationGraphics125", None)
                setattr(value, "AnnotationGraphics125", self)

class PNML_Dimension:

    def __init__(self, width: str, height: str, dimension: "NodeGraphics" = None):
        self.width = width
        self.height = height
        self.dimension = dimension
        
        pass
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
    def dimension(self):
        return self.__dimension

    @dimension.setter
    def dimension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PNML_Dimension__dimension", None)
        self.__dimension = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NodeGraphics98"):
                opp_val = getattr(old_value, "NodeGraphics98", None)
                if opp_val == self:
                    setattr(old_value, "NodeGraphics98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NodeGraphics98"):
                opp_val = getattr(value, "NodeGraphics98", None)
                setattr(value, "NodeGraphics98", self)

class PNML_Line:

    def __init__(self, width: str, shape: str, style: str, PNML_Line: "Color" = None, line: "NodeGraphics" = None, line119: "EdgeGraphics" = None, line122: "AnnotationGraphics" = None):
        self.width = width
        self.shape = shape
        self.style = style
        self.PNML_Line = PNML_Line
        self.line = line
        self.line119 = line119
        self.line122 = line122
        
        pass
    @property
    def shape(self):
        return self.__shape

    @shape.setter
    def shape(self, shape: str):
        self.__shape = shape


    @property
    def style(self):
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width


    @property
    def PNML_Line(self):
        return self.__PNML_Line

    @PNML_Line.setter
    def PNML_Line(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PNML_Line__PNML_Line", None)
        self.__PNML_Line = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Color115"):
                opp_val = getattr(old_value, "Color115", None)
                if opp_val == self:
                    setattr(old_value, "Color115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Color115"):
                opp_val = getattr(value, "Color115", None)
                setattr(value, "Color115", self)

    @property
    def line122(self):
        return self.__line122

    @line122.setter
    def line122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PNML_Line__line122", None)
        self.__line122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AnnotationGraphics123"):
                opp_val = getattr(old_value, "AnnotationGraphics123", None)
                if opp_val == self:
                    setattr(old_value, "AnnotationGraphics123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AnnotationGraphics123"):
                opp_val = getattr(value, "AnnotationGraphics123", None)
                setattr(value, "AnnotationGraphics123", self)

    @property
    def line119(self):
        return self.__line119

    @line119.setter
    def line119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PNML_Line__line119", None)
        self.__line119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EdgeGraphics120"):
                opp_val = getattr(old_value, "EdgeGraphics120", None)
                if opp_val == self:
                    setattr(old_value, "EdgeGraphics120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EdgeGraphics120"):
                opp_val = getattr(value, "EdgeGraphics120", None)
                setattr(value, "EdgeGraphics120", self)

    @property
    def line(self):
        return self.__line

    @line.setter
    def line(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PNML_Line__line", None)
        self.__line = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NodeGraphics117"):
                opp_val = getattr(old_value, "NodeGraphics117", None)
                if opp_val == self:
                    setattr(old_value, "NodeGraphics117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NodeGraphics117"):
                opp_val = getattr(value, "NodeGraphics117", None)
                setattr(value, "NodeGraphics117", self)

class Color:

    pass
class PNML_Fill:

    def __init__(self, gradientrotation: str, PNML_Fill: "Color" = None, PNML_Fill101: "Color" = None, PNML_Fill104: "URI" = None, fill: "NodeGraphics" = None, fill109: "EdgeGraphics" = None, fill112: "AnnotationGraphics" = None):
        self.gradientrotation = gradientrotation
        self.PNML_Fill = PNML_Fill
        self.PNML_Fill101 = PNML_Fill101
        self.PNML_Fill104 = PNML_Fill104
        self.fill = fill
        self.fill109 = fill109
        self.fill112 = fill112
        
        pass
    @property
    def gradientrotation(self):
        return self.__gradientrotation

    @gradientrotation.setter
    def gradientrotation(self, gradientrotation: str):
        self.__gradientrotation = gradientrotation


    @property
    def PNML_Fill101(self):
        return self.__PNML_Fill101

    @PNML_Fill101.setter
    def PNML_Fill101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PNML_Fill__PNML_Fill101", None)
        self.__PNML_Fill101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Color102"):
                opp_val = getattr(old_value, "Color102", None)
                if opp_val == self:
                    setattr(old_value, "Color102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Color102"):
                opp_val = getattr(value, "Color102", None)
                setattr(value, "Color102", self)

    @property
    def fill109(self):
        return self.__fill109

    @fill109.setter
    def fill109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PNML_Fill__fill109", None)
        self.__fill109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EdgeGraphics110"):
                opp_val = getattr(old_value, "EdgeGraphics110", None)
                if opp_val == self:
                    setattr(old_value, "EdgeGraphics110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EdgeGraphics110"):
                opp_val = getattr(value, "EdgeGraphics110", None)
                setattr(value, "EdgeGraphics110", self)

    @property
    def PNML_Fill104(self):
        return self.__PNML_Fill104

    @PNML_Fill104.setter
    def PNML_Fill104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PNML_Fill__PNML_Fill104", None)
        self.__PNML_Fill104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "URI105"):
                opp_val = getattr(old_value, "URI105", None)
                if opp_val == self:
                    setattr(old_value, "URI105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "URI105"):
                opp_val = getattr(value, "URI105", None)
                setattr(value, "URI105", self)

    @property
    def fill(self):
        return self.__fill

    @fill.setter
    def fill(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PNML_Fill__fill", None)
        self.__fill = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NodeGraphics107"):
                opp_val = getattr(old_value, "NodeGraphics107", None)
                if opp_val == self:
                    setattr(old_value, "NodeGraphics107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NodeGraphics107"):
                opp_val = getattr(value, "NodeGraphics107", None)
                setattr(value, "NodeGraphics107", self)

    @property
    def PNML_Fill(self):
        return self.__PNML_Fill

    @PNML_Fill.setter
    def PNML_Fill(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PNML_Fill__PNML_Fill", None)
        self.__PNML_Fill = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Color"):
                opp_val = getattr(old_value, "Color", None)
                if opp_val == self:
                    setattr(old_value, "Color", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Color"):
                opp_val = getattr(value, "Color", None)
                setattr(value, "Color", self)

    @property
    def fill112(self):
        return self.__fill112

    @fill112.setter
    def fill112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PNML_Fill__fill112", None)
        self.__fill112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AnnotationGraphics113"):
                opp_val = getattr(old_value, "AnnotationGraphics113", None)
                if opp_val == self:
                    setattr(old_value, "AnnotationGraphics113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AnnotationGraphics113"):
                opp_val = getattr(value, "AnnotationGraphics113", None)
                setattr(value, "AnnotationGraphics113", self)

class Coordinate:

    pass
class PNML_Offset(Coordinate):

    pass
class PNML_Position(Coordinate):

    pass
class PNML_Coordinate(ABC):

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


class Font:

    pass
class Offset:

    pass
class Graphics:

    pass
class PNML_NodeGraphics(Graphics):

    pass
class PNML_AnnotationGraphics(Graphics):

    pass
class PNML_NetGraphics(Graphics):

    pass
class PNML_Graphics(ABC):

    pass
class PNML_Transition(NetContentElement):

    pass
class InitialMarking:

    pass
class PNML_Place(NetContentElement):

    pass
class NodeGraphics:

    pass
class PNML_EdgeGraphics(Graphics):

    pass
class Line:

    pass
class Fill:

    pass
class Dimension:

    pass
class Position:

    pass