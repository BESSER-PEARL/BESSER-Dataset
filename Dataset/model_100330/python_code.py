from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class RotationType(Enum):
    rtvertical = "rtvertical"
    rthorizontal = "rthorizontal"
    rtdiagonal = "rtdiagonal"
class StyleType(Enum):
    sttsolid = "sttsolid"
    sttdash = "sttdash"
    sttdot = "sttdot"
class ShapeType(Enum):
    shtline = "shtline"
    shtcurve = "shtcurve"
class AlignType(Enum):
    atleft = "atleft"
    atcenter = "atcenter"
    atright = "atright"
class DecorationType(Enum):
    dtunderligne = "dtunderligne"
    dtoverligne = "dtoverligne"
    dtlinethrough = "dtlinethrough"


############################################
# Definition of Classes
############################################

class PNML_Font:

    def __init__(self, rotation: str, family: str, style: str, weight: str, size: str, decoration: str, align: str, font: "AnnotationGraphics" = None):
        self.rotation = rotation
        self.family = family
        self.style = style
        self.weight = weight
        self.size = size
        self.decoration = decoration
        self.align = align
        self.font = font
        
        pass
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size


    @property
    def style(self):
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style


    @property
    def decoration(self):
        return self.__decoration

    @decoration.setter
    def decoration(self, decoration: str):
        self.__decoration = decoration


    @property
    def align(self):
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align


    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight: str):
        self.__weight = weight


    @property
    def family(self):
        return self.__family

    @family.setter
    def family(self, family: str):
        self.__family = family


    @property
    def rotation(self):
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation: str):
        self.__rotation = rotation


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
            if hasattr(old_value, "AnnotationGraphics141"):
                opp_val = getattr(old_value, "AnnotationGraphics141", None)
                if opp_val == self:
                    setattr(old_value, "AnnotationGraphics141", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AnnotationGraphics141"):
                opp_val = getattr(value, "AnnotationGraphics141", None)
                setattr(value, "AnnotationGraphics141", self)

class PNML_Line:

    def __init__(self, width: str, shape: str, style: str, PNML_Line: "Color" = None, line: "NodeGraphics" = None, line135: "EdgeGraphics" = None, line138: "AnnotationGraphics" = None):
        self.width = width
        self.shape = shape
        self.style = style
        self.PNML_Line = PNML_Line
        self.line = line
        self.line135 = line135
        self.line138 = line138
        
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
    def line(self):
        return self.__line

    @line.setter
    def line(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PNML_Line__line", None)
        self.__line = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NodeGraphics133"):
                opp_val = getattr(old_value, "NodeGraphics133", None)
                if opp_val == self:
                    setattr(old_value, "NodeGraphics133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NodeGraphics133"):
                opp_val = getattr(value, "NodeGraphics133", None)
                setattr(value, "NodeGraphics133", self)

    @property
    def line135(self):
        return self.__line135

    @line135.setter
    def line135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PNML_Line__line135", None)
        self.__line135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EdgeGraphics136"):
                opp_val = getattr(old_value, "EdgeGraphics136", None)
                if opp_val == self:
                    setattr(old_value, "EdgeGraphics136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EdgeGraphics136"):
                opp_val = getattr(value, "EdgeGraphics136", None)
                setattr(value, "EdgeGraphics136", self)

    @property
    def line138(self):
        return self.__line138

    @line138.setter
    def line138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PNML_Line__line138", None)
        self.__line138 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AnnotationGraphics139"):
                opp_val = getattr(old_value, "AnnotationGraphics139", None)
                if opp_val == self:
                    setattr(old_value, "AnnotationGraphics139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AnnotationGraphics139"):
                opp_val = getattr(value, "AnnotationGraphics139", None)
                setattr(value, "AnnotationGraphics139", self)

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
            if hasattr(old_value, "Color131"):
                opp_val = getattr(old_value, "Color131", None)
                if opp_val == self:
                    setattr(old_value, "Color131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Color131"):
                opp_val = getattr(value, "Color131", None)
                setattr(value, "Color131", self)

class Color:

    pass
class PNML_Fill:

    def __init__(self, gradientrotation: str, PNML_Fill: "Color" = None, PNML_Fill117: "Color" = None, PNML_Fill120: "URI" = None, fill: "NodeGraphics" = None, fill125: "EdgeGraphics" = None, fill128: "AnnotationGraphics" = None):
        self.gradientrotation = gradientrotation
        self.PNML_Fill = PNML_Fill
        self.PNML_Fill117 = PNML_Fill117
        self.PNML_Fill120 = PNML_Fill120
        self.fill = fill
        self.fill125 = fill125
        self.fill128 = fill128
        
        pass
    @property
    def gradientrotation(self):
        return self.__gradientrotation

    @gradientrotation.setter
    def gradientrotation(self, gradientrotation: str):
        self.__gradientrotation = gradientrotation


    @property
    def fill128(self):
        return self.__fill128

    @fill128.setter
    def fill128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PNML_Fill__fill128", None)
        self.__fill128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AnnotationGraphics129"):
                opp_val = getattr(old_value, "AnnotationGraphics129", None)
                if opp_val == self:
                    setattr(old_value, "AnnotationGraphics129", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AnnotationGraphics129"):
                opp_val = getattr(value, "AnnotationGraphics129", None)
                setattr(value, "AnnotationGraphics129", self)

    @property
    def PNML_Fill117(self):
        return self.__PNML_Fill117

    @PNML_Fill117.setter
    def PNML_Fill117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PNML_Fill__PNML_Fill117", None)
        self.__PNML_Fill117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Color118"):
                opp_val = getattr(old_value, "Color118", None)
                if opp_val == self:
                    setattr(old_value, "Color118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Color118"):
                opp_val = getattr(value, "Color118", None)
                setattr(value, "Color118", self)

    @property
    def PNML_Fill120(self):
        return self.__PNML_Fill120

    @PNML_Fill120.setter
    def PNML_Fill120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PNML_Fill__PNML_Fill120", None)
        self.__PNML_Fill120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "URI121"):
                opp_val = getattr(old_value, "URI121", None)
                if opp_val == self:
                    setattr(old_value, "URI121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "URI121"):
                opp_val = getattr(value, "URI121", None)
                setattr(value, "URI121", self)

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
    def fill125(self):
        return self.__fill125

    @fill125.setter
    def fill125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PNML_Fill__fill125", None)
        self.__fill125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EdgeGraphics126"):
                opp_val = getattr(old_value, "EdgeGraphics126", None)
                if opp_val == self:
                    setattr(old_value, "EdgeGraphics126", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EdgeGraphics126"):
                opp_val = getattr(value, "EdgeGraphics126", None)
                setattr(value, "EdgeGraphics126", self)

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
            if hasattr(old_value, "NodeGraphics123"):
                opp_val = getattr(old_value, "NodeGraphics123", None)
                if opp_val == self:
                    setattr(old_value, "NodeGraphics123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NodeGraphics123"):
                opp_val = getattr(value, "NodeGraphics123", None)
                setattr(value, "NodeGraphics123", self)

class PNML_Dimension:

    def __init__(self, width: str, height: str, dimension: "NodeGraphics" = None):
        self.width = width
        self.height = height
        self.dimension = dimension
        
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
            if hasattr(old_value, "NodeGraphics114"):
                opp_val = getattr(old_value, "NodeGraphics114", None)
                if opp_val == self:
                    setattr(old_value, "NodeGraphics114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NodeGraphics114"):
                opp_val = getattr(value, "NodeGraphics114", None)
                setattr(value, "NodeGraphics114", self)

class Coordinate:

    pass
class PNML_Position(Coordinate):

    pass
class PNML_Coordinate(ABC):

    def __init__(self, x: str, y: str):
        self.x = x
        self.y = y
        
        pass
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x


    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y


class Font:

    pass
class Offset:

    pass
class PNML_Offset(Coordinate):

    pass
class Line:

    pass
class Fill:

    pass
class Dimension:

    pass
class Position:

    pass
class Graphics:

    pass
class PNML_PageGraphics(Graphics):

    pass
class PNML_NodeGraphics(Graphics):

    pass
class PNML_EdgeGraphics(Graphics):

    pass
class PNML_AnnotationGraphics(Graphics):

    pass
class PNML_NetGraphics(Graphics):

    pass
class PNML_Graphics(ABC):

    pass
class InitialMarking:

    pass
class Reference:

    pass
class PageGraphics:

    pass
class Inscription:

    pass
class EdgeGraphics:

    pass
class NodeGraphics:

    pass
class Place:

    pass
class LabeledElement:

    pass
class PNML_Name(LabeledElement):

    pass
class PNML_InitialMarking(LabeledElement):

    pass
class PNML_Inscription(LabeledElement):

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
class NetContentElement:

    pass
class PNML_Place(NetContentElement):

    pass
class PNML_Transition(NetContentElement):

    pass
class Node:

    pass
class PNML_Reference(Node):

    pass
class Arc:

    pass
class AnyElement:

    pass
class PNML_ToolSpecific:

    def __init__(self, tool: str, version: str, tools24: "Node" = None, tools26: "Page" = None, PNML_ToolSpecific: set["AnyElement"] = None, tools: "NetElement" = None, tools22: "Arc" = None):
        self.tool = tool
        self.version = version
        self.tools24 = tools24
        self.tools26 = tools26
        self.PNML_ToolSpecific = PNML_ToolSpecific if PNML_ToolSpecific is not None else set()
        self.tools = tools
        self.tools22 = tools22
        
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
    def tools26(self):
        return self.__tools26

    @tools26.setter
    def tools26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PNML_ToolSpecific__tools26", None)
        self.__tools26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Page27"):
                opp_val = getattr(old_value, "Page27", None)
                if opp_val == self:
                    setattr(old_value, "Page27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Page27"):
                opp_val = getattr(value, "Page27", None)
                setattr(value, "Page27", self)

    @property
    def tools24(self):
        return self.__tools24

    @tools24.setter
    def tools24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PNML_ToolSpecific__tools24", None)
        self.__tools24 = value
        
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
    def tools22(self):
        return self.__tools22

    @tools22.setter
    def tools22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PNML_ToolSpecific__tools22", None)
        self.__tools22 = value
        
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
            if hasattr(old_value, "NetElement20"):
                opp_val = getattr(old_value, "NetElement20", None)
                if opp_val == self:
                    setattr(old_value, "NetElement20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NetElement20"):
                opp_val = getattr(value, "NetElement20", None)
                setattr(value, "NetElement20", self)

class Page:

    pass
class PNML_NetContent(ABC):

    pass
class Name:

    pass
class NetGraphics:

    pass
class ToolSpecific:

    pass
class Label:

    pass
class PNML_LabeledElement(ABC):

    pass
class IdedElement:

    pass
class PNML_Node(IdedElement):

    pass
class PNML_NetElement(IdedElement):

    pass
class NetElement:

    pass
class URI:

    pass
class PNML_PNMLDocument:

    pass
class NetContent:

    pass
class PNML_Page(IdedElement, NetContent):

    pass
class PNML_NetContentElement(NetContent):

    pass
class PNML_Arc(IdedElement, NetContent):

    pass
class PNML_ReferencePlace(NetContent, Reference):

    pass
class PNML_ReferenceTransition(NetContent, Reference):

    pass
class PNMLDocument:

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
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


class PNML_Color:

    pass