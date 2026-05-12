from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class StyleType(Enum):
    sttsolid = "sttsolid"
    sttdash = "sttdash"
    sttdot = "sttdot"
class RotationType(Enum):
    rtvertical = "rtvertical"
    rthorizontal = "rthorizontal"
    rtdiagonal = "rtdiagonal"
class AlignType(Enum):
    atleft = "atleft"
    atcenter = "atcenter"
    atright = "atright"
class ShapeType(Enum):
    shtline = "shtline"
    shtcurve = "shtcurve"
class DecorationType(Enum):
    dtunderligne = "dtunderligne"
    dtoverligne = "dtoverligne"
    dtlinethrough = "dtlinethrough"


############################################
# Definition of Classes
############################################

class PNML_Font:

    def __init__(self, family: str, style: str, weight: str, size: str, decoration: str, align: str, rotation: str, font: "AnnotationGraphics" = None):
        self.family = family
        self.style = style
        self.weight = weight
        self.size = size
        self.decoration = decoration
        self.align = align
        self.rotation = rotation
        self.font = font
        
        pass
    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight: str):
        self.__weight = weight


    @property
    def decoration(self):
        return self.__decoration

    @decoration.setter
    def decoration(self, decoration: str):
        self.__decoration = decoration


    @property
    def style(self):
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style


    @property
    def align(self):
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align


    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size


    @property
    def rotation(self):
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation: str):
        self.__rotation = rotation


    @property
    def family(self):
        return self.__family

    @family.setter
    def family(self, family: str):
        self.__family = family


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
            if hasattr(old_value, "AnnotationGraphics179"):
                opp_val = getattr(old_value, "AnnotationGraphics179", None)
                if opp_val == self:
                    setattr(old_value, "AnnotationGraphics179", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AnnotationGraphics179"):
                opp_val = getattr(value, "AnnotationGraphics179", None)
                setattr(value, "AnnotationGraphics179", self)

class Color:

    pass
class PNML_Fill:

    def __init__(self, gradientrotation: str, fill166: "AnnotationGraphics" = None, PNML_Fill: "Color" = None, PNML_Fill155: "Color" = None, PNML_Fill158: "URI" = None, fill: "NodeGraphics" = None, fill163: "EdgeGraphics" = None):
        self.gradientrotation = gradientrotation
        self.fill166 = fill166
        self.PNML_Fill = PNML_Fill
        self.PNML_Fill155 = PNML_Fill155
        self.PNML_Fill158 = PNML_Fill158
        self.fill = fill
        self.fill163 = fill163
        
        pass
    @property
    def gradientrotation(self):
        return self.__gradientrotation

    @gradientrotation.setter
    def gradientrotation(self, gradientrotation: str):
        self.__gradientrotation = gradientrotation


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
    def fill(self):
        return self.__fill

    @fill.setter
    def fill(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PNML_Fill__fill", None)
        self.__fill = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NodeGraphics161"):
                opp_val = getattr(old_value, "NodeGraphics161", None)
                if opp_val == self:
                    setattr(old_value, "NodeGraphics161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NodeGraphics161"):
                opp_val = getattr(value, "NodeGraphics161", None)
                setattr(value, "NodeGraphics161", self)

    @property
    def PNML_Fill155(self):
        return self.__PNML_Fill155

    @PNML_Fill155.setter
    def PNML_Fill155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PNML_Fill__PNML_Fill155", None)
        self.__PNML_Fill155 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Color156"):
                opp_val = getattr(old_value, "Color156", None)
                if opp_val == self:
                    setattr(old_value, "Color156", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Color156"):
                opp_val = getattr(value, "Color156", None)
                setattr(value, "Color156", self)

    @property
    def fill166(self):
        return self.__fill166

    @fill166.setter
    def fill166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PNML_Fill__fill166", None)
        self.__fill166 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AnnotationGraphics167"):
                opp_val = getattr(old_value, "AnnotationGraphics167", None)
                if opp_val == self:
                    setattr(old_value, "AnnotationGraphics167", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AnnotationGraphics167"):
                opp_val = getattr(value, "AnnotationGraphics167", None)
                setattr(value, "AnnotationGraphics167", self)

    @property
    def fill163(self):
        return self.__fill163

    @fill163.setter
    def fill163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PNML_Fill__fill163", None)
        self.__fill163 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EdgeGraphics164"):
                opp_val = getattr(old_value, "EdgeGraphics164", None)
                if opp_val == self:
                    setattr(old_value, "EdgeGraphics164", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EdgeGraphics164"):
                opp_val = getattr(value, "EdgeGraphics164", None)
                setattr(value, "EdgeGraphics164", self)

    @property
    def PNML_Fill158(self):
        return self.__PNML_Fill158

    @PNML_Fill158.setter
    def PNML_Fill158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PNML_Fill__PNML_Fill158", None)
        self.__PNML_Fill158 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "URI159"):
                opp_val = getattr(old_value, "URI159", None)
                if opp_val == self:
                    setattr(old_value, "URI159", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "URI159"):
                opp_val = getattr(value, "URI159", None)
                setattr(value, "URI159", self)

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
            if hasattr(old_value, "NodeGraphics152"):
                opp_val = getattr(old_value, "NodeGraphics152", None)
                if opp_val == self:
                    setattr(old_value, "NodeGraphics152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NodeGraphics152"):
                opp_val = getattr(value, "NodeGraphics152", None)
                setattr(value, "NodeGraphics152", self)

class PNML_Line:

    def __init__(self, width: str, shape: str, style: str, PNML_Line: "Color" = None, line: "NodeGraphics" = None, line173: "EdgeGraphics" = None, line176: "AnnotationGraphics" = None):
        self.width = width
        self.shape = shape
        self.style = style
        self.PNML_Line = PNML_Line
        self.line = line
        self.line173 = line173
        self.line176 = line176
        
        pass
    @property
    def shape(self):
        return self.__shape

    @shape.setter
    def shape(self, shape: str):
        self.__shape = shape


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width


    @property
    def style(self):
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style


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
            if hasattr(old_value, "Color169"):
                opp_val = getattr(old_value, "Color169", None)
                if opp_val == self:
                    setattr(old_value, "Color169", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Color169"):
                opp_val = getattr(value, "Color169", None)
                setattr(value, "Color169", self)

    @property
    def line173(self):
        return self.__line173

    @line173.setter
    def line173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PNML_Line__line173", None)
        self.__line173 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EdgeGraphics174"):
                opp_val = getattr(old_value, "EdgeGraphics174", None)
                if opp_val == self:
                    setattr(old_value, "EdgeGraphics174", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EdgeGraphics174"):
                opp_val = getattr(value, "EdgeGraphics174", None)
                setattr(value, "EdgeGraphics174", self)

    @property
    def line176(self):
        return self.__line176

    @line176.setter
    def line176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PNML_Line__line176", None)
        self.__line176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AnnotationGraphics177"):
                opp_val = getattr(old_value, "AnnotationGraphics177", None)
                if opp_val == self:
                    setattr(old_value, "AnnotationGraphics177", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AnnotationGraphics177"):
                opp_val = getattr(value, "AnnotationGraphics177", None)
                setattr(value, "AnnotationGraphics177", self)

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
            if hasattr(old_value, "NodeGraphics171"):
                opp_val = getattr(old_value, "NodeGraphics171", None)
                if opp_val == self:
                    setattr(old_value, "NodeGraphics171", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NodeGraphics171"):
                opp_val = getattr(value, "NodeGraphics171", None)
                setattr(value, "NodeGraphics171", self)

class Font:

    pass
class Offset:

    pass
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


class Graphics:

    pass
class PNML_NodeGraphics(Graphics):

    pass
class PNML_AnnotationGraphics(Graphics):

    pass
class PNML_PageGraphics(Graphics):

    pass
class PNML_NetGraphics(Graphics):

    pass
class PNML_Graphics(ABC):

    pass
class InitialMarking:

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
class PNML_ImportNode:

    pass
class ImportNode:

    pass
class NCName:

    pass
class Instance:

    pass
class LabeledElement:

    pass
class Inscription:

    pass
class EdgeGraphics:

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

class NetContentElement:

    pass
class PNML_Transition(NetContentElement):

    pass
class PNML_Place(NetContentElement):

    pass
class Place:

    pass
class PNML_InitialMarking(LabeledElement):

    pass
class PageGraphics:

    pass
class PNML_Inscription(LabeledElement):

    pass
class PNML_Name(LabeledElement):

    pass
class Name:

    pass
class NetGraphics:

    pass
class ToolSpecific:

    pass
class AnnotationGraphics:

    pass
class Label:

    pass
class PNML_LabeledElement(ABC):

    pass
class Arc:

    pass
class AnyElement:

    pass
class PNML_ToolSpecific:

    def __init__(self, tool: str, version: str, PNML_ToolSpecific: set["AnyElement"] = None, tools: "NetElement" = None, tools43: "Arc" = None, tools45: "Node" = None, tools48: "Page" = None):
        self.tool = tool
        self.version = version
        self.PNML_ToolSpecific = PNML_ToolSpecific if PNML_ToolSpecific is not None else set()
        self.tools = tools
        self.tools43 = tools43
        self.tools45 = tools45
        self.tools48 = tools48
        
        pass
    @property
    def tool(self):
        return self.__tool

    @tool.setter
    def tool(self, tool: str):
        self.__tool = tool


    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version


    @property
    def tools43(self):
        return self.__tools43

    @tools43.setter
    def tools43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PNML_ToolSpecific__tools43", None)
        self.__tools43 = value
        
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
    def tools48(self):
        return self.__tools48

    @tools48.setter
    def tools48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PNML_ToolSpecific__tools48", None)
        self.__tools48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Page49"):
                opp_val = getattr(old_value, "Page49", None)
                if opp_val == self:
                    setattr(old_value, "Page49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Page49"):
                opp_val = getattr(value, "Page49", None)
                setattr(value, "Page49", self)

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
            if hasattr(old_value, "NetElement41"):
                opp_val = getattr(old_value, "NetElement41", None)
                if opp_val == self:
                    setattr(old_value, "NetElement41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NetElement41"):
                opp_val = getattr(value, "NetElement41", None)
                setattr(value, "NetElement41", self)

    @property
    def tools45(self):
        return self.__tools45

    @tools45.setter
    def tools45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PNML_ToolSpecific__tools45", None)
        self.__tools45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Node46"):
                opp_val = getattr(old_value, "Node46", None)
                if opp_val == self:
                    setattr(old_value, "Node46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Node46"):
                opp_val = getattr(value, "Node46", None)
                setattr(value, "Node46", self)

class Page:

    pass
class PNML_NetContent(ABC):

    pass
class Module:

    pass
class NetElement:

    pass
class Reference:

    pass
class Node:

    pass
class PNML_Reference(Node):

    pass
class PNML_Interface:

    pass
class PNMLDocument:

    pass
class NetContent:

    pass
class PNML_NetContentElement(NetContent):

    pass
class PNML_ReferenceTransition(Reference, NetContent):

    pass
class PNML_ReferencePlace(Reference, NetContent):

    pass
class Interface:

    pass
class IdedElement:

    pass
class PNML_NetElement(IdedElement):

    pass
class PNML_Node(IdedElement):

    pass
class PNML_Arc(IdedElement, NetContent):

    pass
class PNML_Instance(IdedElement, NetContent):

    pass
class PNML_Page(IdedElement, NetContent):

    pass
class PNML_Module(IdedElement):

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


class URI:

    pass
class PNML_PNMLDocument:

    pass
class PNML_NCName:

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


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

