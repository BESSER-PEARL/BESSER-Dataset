from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class LineStyle(Enum):
    SOLID = "SOLID"
    DASH = "DASH"
    DOT = "DOT"
class CSS2FontWeight(Enum):
    NORMAL = "NORMAL"
    BOLD = "BOLD"
    BOLDER = "BOLDER"
    LIGHTER = "LIGHTER"
class CSS2FontStyle(Enum):
    NORMAL = "NORMAL"
    ITALIC = "ITALIC"
    OBLIQUE = "OBLIQUE"
class LineShape(Enum):
    LINE = "LINE"
    CURVE = "CURVE"
class FontDecoration(Enum):
    UNDERLINE = "UNDERLINE"
    OVERLINE = "OVERLINE"
    LINETHROUGH = "LINETHROUGH"
class PNType(Enum):
    SYMNET = "SYMNET"
    COREMODEL = "COREMODEL"
    PTNET = "PTNET"
    HLPN = "HLPN"
    PTHLPN = "PTHLPN"
class FontAlign(Enum):
    LEFT = "LEFT"
    CENTER = "CENTER"
    RIGHT = "RIGHT"
class Gradient(Enum):
    HORIZONTAL = "HORIZONTAL"
    VERTICAL = "VERTICAL"
    DIAGONAL = "DIAGONAL"
class CSS2FontSize(Enum):
    XXSMALL = "XXSMALL"
    XSMALL = "XSMALL"
    SMALL = "SMALL"
    MEDIUM = "MEDIUM"
    LARGE = "LARGE"
    XLARGE = "XLARGE"
    XXLARGE = "XXLARGE"
class CSS2FontFamily(Enum):
    VERDANA = "VERDANA"
    ARIAL = "ARIAL"
    TIMES = "TIMES"
    GEORGIA = "GEORGIA"
    TREBUCHET = "TREBUCHET"
class CSS2Color(Enum):
    BLUE = "BLUE"
    FUCHSIA = "FUCHSIA"
    GRAY = "GRAY"
    GREEN = "GREEN"
    LIME = "LIME"
    MAROON = "MAROON"
    NAVY = "NAVY"
    OLIVE = "OLIVE"
    ORANGE = "ORANGE"
    PURPLE = "PURPLE"
    RED = "RED"
    AQUA = "AQUA"
    BLACK = "BLACK"
    SILVER = "SILVER"
    TEAL = "TEAL"
    WHITE = "WHITE"
    YELLOW = "YELLOW"


############################################
# Definition of Classes
############################################

class hlcorestructure_Declarations:

    pass
class hlcorestructure_Term:

    pass
class HLCoreAnnotation:

    pass
class hlcorestructure_Sort:

    pass
class hlcorestructure_Condition(HLCoreAnnotation):

    pass
class Label:

    pass
class hlcorestructure_Attribute(Label):

    pass
class hlcorestructure_HLMarking(HLCoreAnnotation):

    pass
class hlcorestructure_Type(HLCoreAnnotation):

    pass
class PlaceNode:

    pass
class hlcorestructure_Place(PlaceNode):

    pass
class TransitionNode:

    pass
class hlcorestructure_RefTransition(TransitionNode):

    pass
class hlcorestructure_Transition(TransitionNode):

    pass
class hlcorestructure_RefPlace(PlaceNode):

    pass
class Node:

    pass
class hlcorestructure_TransitionNode(Node):

    pass
class hlcorestructure_PlaceNode(Node):

    pass
class hlcorestructure_HLAnnotation(HLCoreAnnotation):

    pass
class hlcorestructure_Annotation(Label):

    pass
class hlcorestructure_Font:

    def __init__(self, align: str, decoration: str, family: str, rotation: str, size: str, style: str, weight: str, Font: "hlcorestructure_AnnotationGraphics" = None, font: "hlcorestructure_AnnotationGraphics" = None):
        self.align = align
        self.decoration = decoration
        self.family = family
        self.rotation = rotation
        self.size = size
        self.style = style
        self.weight = weight
        self.Font = Font
        self.font = font
        
    @property
    def rotation(self) -> str:
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation: str):
        self.__rotation = rotation

    @property
    def decoration(self) -> str:
        return self.__decoration

    @decoration.setter
    def decoration(self, decoration: str):
        self.__decoration = decoration

    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

    @property
    def family(self) -> str:
        return self.__family

    @family.setter
    def family(self, family: str):
        self.__family = family

    @property
    def weight(self) -> str:
        return self.__weight

    @weight.setter
    def weight(self, weight: str):
        self.__weight = weight

    @property
    def align(self) -> str:
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align

    @property
    def style(self) -> str:
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
        old_value = getattr(self, f"_hlcorestructure_Font__font", None)
        self.__font = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AnnotationGraphics94"):
                opp_val = getattr(old_value, "AnnotationGraphics94", None)
                if opp_val == self:
                    setattr(old_value, "AnnotationGraphics94", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AnnotationGraphics94"):
                opp_val = getattr(value, "AnnotationGraphics94", None)
                setattr(value, "AnnotationGraphics94", self)

    @property
    def Font(self):
        return self.__Font

    @Font.setter
    def Font(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlcorestructure_Font__Font", None)
        self.__Font = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containerAnnotationGraphics58"):
                opp_val = getattr(old_value, "containerAnnotationGraphics58", None)
                if opp_val == self:
                    setattr(old_value, "containerAnnotationGraphics58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containerAnnotationGraphics58"):
                opp_val = getattr(value, "containerAnnotationGraphics58", None)
                setattr(value, "containerAnnotationGraphics58", self)

class Coordinate:

    pass
class hlcorestructure_Offset(Coordinate):

    pass
class hlcorestructure_Coordinate(ABC):

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

class hlcorestructure_Graphics(ABC):

    pass
class hlcorestructure_Line:

    def __init__(self, width: str, color: str, shape: str, style: str, Line: "hlcorestructure_NodeGraphics" = None, Line56: "hlcorestructure_AnnotationGraphics" = None, line: "hlcorestructure_NodeGraphics" = None, line68: "hlcorestructure_ArcGraphics" = None, Line77: "hlcorestructure_ArcGraphics" = None, line71: "hlcorestructure_AnnotationGraphics" = None):
        self.width = width
        self.color = color
        self.shape = shape
        self.style = style
        self.Line = Line
        self.Line56 = Line56
        self.line = line
        self.line68 = line68
        self.Line77 = Line77
        self.line71 = line71
        
    @property
    def shape(self) -> str:
        return self.__shape

    @shape.setter
    def shape(self, shape: str):
        self.__shape = shape

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def line68(self):
        return self.__line68

    @line68.setter
    def line68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlcorestructure_Line__line68", None)
        self.__line68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ArcGraphics69"):
                opp_val = getattr(old_value, "ArcGraphics69", None)
                if opp_val == self:
                    setattr(old_value, "ArcGraphics69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ArcGraphics69"):
                opp_val = getattr(value, "ArcGraphics69", None)
                setattr(value, "ArcGraphics69", self)

    @property
    def Line77(self):
        return self.__Line77

    @Line77.setter
    def Line77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlcorestructure_Line__Line77", None)
        self.__Line77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containerArcGraphics76"):
                opp_val = getattr(old_value, "containerArcGraphics76", None)
                if opp_val == self:
                    setattr(old_value, "containerArcGraphics76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containerArcGraphics76"):
                opp_val = getattr(value, "containerArcGraphics76", None)
                setattr(value, "containerArcGraphics76", self)

    @property
    def Line56(self):
        return self.__Line56

    @Line56.setter
    def Line56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlcorestructure_Line__Line56", None)
        self.__Line56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containerAnnotationGraphics55"):
                opp_val = getattr(old_value, "containerAnnotationGraphics55", None)
                if opp_val == self:
                    setattr(old_value, "containerAnnotationGraphics55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containerAnnotationGraphics55"):
                opp_val = getattr(value, "containerAnnotationGraphics55", None)
                setattr(value, "containerAnnotationGraphics55", self)

    @property
    def Line(self):
        return self.__Line

    @Line.setter
    def Line(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlcorestructure_Line__Line", None)
        self.__Line = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containerNodeGraphics39"):
                opp_val = getattr(old_value, "containerNodeGraphics39", None)
                if opp_val == self:
                    setattr(old_value, "containerNodeGraphics39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containerNodeGraphics39"):
                opp_val = getattr(value, "containerNodeGraphics39", None)
                setattr(value, "containerNodeGraphics39", self)

    @property
    def line(self):
        return self.__line

    @line.setter
    def line(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlcorestructure_Line__line", None)
        self.__line = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NodeGraphics66"):
                opp_val = getattr(old_value, "NodeGraphics66", None)
                if opp_val == self:
                    setattr(old_value, "NodeGraphics66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NodeGraphics66"):
                opp_val = getattr(value, "NodeGraphics66", None)
                setattr(value, "NodeGraphics66", self)

    @property
    def line71(self):
        return self.__line71

    @line71.setter
    def line71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlcorestructure_Line__line71", None)
        self.__line71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AnnotationGraphics72"):
                opp_val = getattr(old_value, "AnnotationGraphics72", None)
                if opp_val == self:
                    setattr(old_value, "AnnotationGraphics72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AnnotationGraphics72"):
                opp_val = getattr(value, "AnnotationGraphics72", None)
                setattr(value, "AnnotationGraphics72", self)

class hlcorestructure_Fill:

    def __init__(self, color: str, gradientcolor: str, gradientrotation: str, image: str, Fill: "hlcorestructure_NodeGraphics" = None, Fill53: "hlcorestructure_AnnotationGraphics" = None, fill: "hlcorestructure_NodeGraphics" = None, fill63: "hlcorestructure_AnnotationGraphics" = None):
        self.color = color
        self.gradientcolor = gradientcolor
        self.gradientrotation = gradientrotation
        self.image = image
        self.Fill = Fill
        self.Fill53 = Fill53
        self.fill = fill
        self.fill63 = fill63
        
    @property
    def gradientcolor(self) -> str:
        return self.__gradientcolor

    @gradientcolor.setter
    def gradientcolor(self, gradientcolor: str):
        self.__gradientcolor = gradientcolor

    @property
    def image(self) -> str:
        return self.__image

    @image.setter
    def image(self, image: str):
        self.__image = image

    @property
    def gradientrotation(self) -> str:
        return self.__gradientrotation

    @gradientrotation.setter
    def gradientrotation(self, gradientrotation: str):
        self.__gradientrotation = gradientrotation

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def Fill(self):
        return self.__Fill

    @Fill.setter
    def Fill(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlcorestructure_Fill__Fill", None)
        self.__Fill = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containerNodeGraphics"):
                opp_val = getattr(old_value, "containerNodeGraphics", None)
                if opp_val == self:
                    setattr(old_value, "containerNodeGraphics", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containerNodeGraphics"):
                opp_val = getattr(value, "containerNodeGraphics", None)
                setattr(value, "containerNodeGraphics", self)

    @property
    def fill(self):
        return self.__fill

    @fill.setter
    def fill(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlcorestructure_Fill__fill", None)
        self.__fill = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NodeGraphics61"):
                opp_val = getattr(old_value, "NodeGraphics61", None)
                if opp_val == self:
                    setattr(old_value, "NodeGraphics61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NodeGraphics61"):
                opp_val = getattr(value, "NodeGraphics61", None)
                setattr(value, "NodeGraphics61", self)

    @property
    def Fill53(self):
        return self.__Fill53

    @Fill53.setter
    def Fill53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlcorestructure_Fill__Fill53", None)
        self.__Fill53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containerAnnotationGraphics52"):
                opp_val = getattr(old_value, "containerAnnotationGraphics52", None)
                if opp_val == self:
                    setattr(old_value, "containerAnnotationGraphics52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containerAnnotationGraphics52"):
                opp_val = getattr(value, "containerAnnotationGraphics52", None)
                setattr(value, "containerAnnotationGraphics52", self)

    @property
    def fill63(self):
        return self.__fill63

    @fill63.setter
    def fill63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlcorestructure_Fill__fill63", None)
        self.__fill63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AnnotationGraphics64"):
                opp_val = getattr(old_value, "AnnotationGraphics64", None)
                if opp_val == self:
                    setattr(old_value, "AnnotationGraphics64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AnnotationGraphics64"):
                opp_val = getattr(value, "AnnotationGraphics64", None)
                setattr(value, "AnnotationGraphics64", self)

class Graphics:

    pass
class hlcorestructure_ArcGraphics(Graphics):

    pass
class hlcorestructure_AnnotationGraphics(Graphics):

    pass
class hlcorestructure_AnyObject(ABC):

    pass
class hlcorestructure_Label(ABC):

    pass
class hlcorestructure_Dimension(Coordinate):

    pass
class hlcorestructure_Position(Coordinate):

    pass
class hlcorestructure_NodeGraphics(Graphics):

    pass
class Annotation:

    pass
class hlcorestructure_HLCoreAnnotation(Annotation):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class PnObject:

    pass
class hlcorestructure_Arc(PnObject):

    pass
class hlcorestructure_Node(PnObject):

    pass
class hlcorestructure_Declaration(HLCoreAnnotation):

    pass
class hlcorestructure_PnObject(ABC):

    def __init__(self, id: str, PnObject: "hlcorestructure_Page" = None, containerPnObject: set["hlcorestructure_ToolInfo"] = None, objects: "hlcorestructure_Page" = None, containerNamePnObject: "hlcorestructure_Name" = None, PnObject24: "hlcorestructure_Name" = None, PnObject29: "hlcorestructure_ToolInfo" = None):
        self.id = id
        self.PnObject = PnObject
        self.containerPnObject = containerPnObject if containerPnObject is not None else set()
        self.objects = objects
        self.containerNamePnObject = containerNamePnObject
        self.PnObject24 = PnObject24
        self.PnObject29 = PnObject29
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def PnObject24(self):
        return self.__PnObject24

    @PnObject24.setter
    def PnObject24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlcorestructure_PnObject__PnObject24", None)
        self.__PnObject24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "name23"):
                opp_val = getattr(old_value, "name23", None)
                if opp_val == self:
                    setattr(old_value, "name23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "name23"):
                opp_val = getattr(value, "name23", None)
                setattr(value, "name23", self)

    @property
    def PnObject29(self):
        return self.__PnObject29

    @PnObject29.setter
    def PnObject29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlcorestructure_PnObject__PnObject29", None)
        self.__PnObject29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "toolspecifics28"):
                opp_val = getattr(old_value, "toolspecifics28", None)
                if opp_val == self:
                    setattr(old_value, "toolspecifics28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "toolspecifics28"):
                opp_val = getattr(value, "toolspecifics28", None)
                setattr(value, "toolspecifics28", self)

    @property
    def objects(self):
        return self.__objects

    @objects.setter
    def objects(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlcorestructure_PnObject__objects", None)
        self.__objects = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Page19"):
                opp_val = getattr(old_value, "Page19", None)
                if opp_val == self:
                    setattr(old_value, "Page19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Page19"):
                opp_val = getattr(value, "Page19", None)
                setattr(value, "Page19", self)

    @property
    def PnObject(self):
        return self.__PnObject

    @PnObject.setter
    def PnObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlcorestructure_PnObject__PnObject", None)
        self.__PnObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containerPage"):
                opp_val = getattr(old_value, "containerPage", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containerPage"):
                opp_val = getattr(value, "containerPage", None)
                if opp_val is None:
                    setattr(value, "containerPage", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def containerPnObject(self):
        return self.__containerPnObject

    @containerPnObject.setter
    def containerPnObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlcorestructure_PnObject__containerPnObject", None)
        self.__containerPnObject = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ToolInfo17"):
                    opp_val = getattr(item, "ToolInfo17", None)
                    
                    if opp_val == self:
                        setattr(item, "ToolInfo17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ToolInfo17"):
                    opp_val = getattr(item, "ToolInfo17", None)
                    
                    setattr(item, "ToolInfo17", self)
                    

    @property
    def containerNamePnObject(self):
        return self.__containerNamePnObject

    @containerNamePnObject.setter
    def containerNamePnObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlcorestructure_PnObject__containerNamePnObject", None)
        self.__containerNamePnObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Name15"):
                opp_val = getattr(old_value, "Name15", None)
                if opp_val == self:
                    setattr(old_value, "Name15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Name15"):
                opp_val = getattr(value, "Name15", None)
                setattr(value, "Name15", self)

class hlcorestructure_Page(PnObject):

    pass
class hlcorestructure_ToolInfo:

    def __init__(self, formattedXMLBuffer: str, toolInfoGrammarURI: str, tool: str, version: str, ToolInfo: "hlcorestructure_PetriNet" = None, ToolInfo17: "hlcorestructure_PnObject" = None, toolspecifics: "hlcorestructure_PetriNet" = None, toolspecifics28: "hlcorestructure_PnObject" = None, toolspecifics31: "hlcorestructure_Label" = None, containerToolInfo: "hlcorestructure_AnyObject" = None, ToolInfo34: "hlcorestructure_Label" = None, ToolInfo107: "hlcorestructure_AnyObject" = None):
        self.formattedXMLBuffer = formattedXMLBuffer
        self.toolInfoGrammarURI = toolInfoGrammarURI
        self.tool = tool
        self.version = version
        self.ToolInfo = ToolInfo
        self.ToolInfo17 = ToolInfo17
        self.toolspecifics = toolspecifics
        self.toolspecifics28 = toolspecifics28
        self.toolspecifics31 = toolspecifics31
        self.containerToolInfo = containerToolInfo
        self.ToolInfo34 = ToolInfo34
        self.ToolInfo107 = ToolInfo107
        
    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def formattedXMLBuffer(self) -> str:
        return self.__formattedXMLBuffer

    @formattedXMLBuffer.setter
    def formattedXMLBuffer(self, formattedXMLBuffer: str):
        self.__formattedXMLBuffer = formattedXMLBuffer

    @property
    def tool(self) -> str:
        return self.__tool

    @tool.setter
    def tool(self, tool: str):
        self.__tool = tool

    @property
    def toolInfoGrammarURI(self) -> str:
        return self.__toolInfoGrammarURI

    @toolInfoGrammarURI.setter
    def toolInfoGrammarURI(self, toolInfoGrammarURI: str):
        self.__toolInfoGrammarURI = toolInfoGrammarURI

    @property
    def toolspecifics(self):
        return self.__toolspecifics

    @toolspecifics.setter
    def toolspecifics(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlcorestructure_ToolInfo__toolspecifics", None)
        self.__toolspecifics = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet26"):
                opp_val = getattr(old_value, "PetriNet26", None)
                if opp_val == self:
                    setattr(old_value, "PetriNet26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet26"):
                opp_val = getattr(value, "PetriNet26", None)
                setattr(value, "PetriNet26", self)

    @property
    def ToolInfo34(self):
        return self.__ToolInfo34

    @ToolInfo34.setter
    def ToolInfo34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlcorestructure_ToolInfo__ToolInfo34", None)
        self.__ToolInfo34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containerLabel"):
                opp_val = getattr(old_value, "containerLabel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containerLabel"):
                opp_val = getattr(value, "containerLabel", None)
                if opp_val is None:
                    setattr(value, "containerLabel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def containerToolInfo(self):
        return self.__containerToolInfo

    @containerToolInfo.setter
    def containerToolInfo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlcorestructure_ToolInfo__containerToolInfo", None)
        self.__containerToolInfo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AnyObject"):
                opp_val = getattr(old_value, "AnyObject", None)
                if opp_val == self:
                    setattr(old_value, "AnyObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AnyObject"):
                opp_val = getattr(value, "AnyObject", None)
                setattr(value, "AnyObject", self)

    @property
    def toolspecifics28(self):
        return self.__toolspecifics28

    @toolspecifics28.setter
    def toolspecifics28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlcorestructure_ToolInfo__toolspecifics28", None)
        self.__toolspecifics28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PnObject29"):
                opp_val = getattr(old_value, "PnObject29", None)
                if opp_val == self:
                    setattr(old_value, "PnObject29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PnObject29"):
                opp_val = getattr(value, "PnObject29", None)
                setattr(value, "PnObject29", self)

    @property
    def ToolInfo17(self):
        return self.__ToolInfo17

    @ToolInfo17.setter
    def ToolInfo17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlcorestructure_ToolInfo__ToolInfo17", None)
        self.__ToolInfo17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containerPnObject"):
                opp_val = getattr(old_value, "containerPnObject", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containerPnObject"):
                opp_val = getattr(value, "containerPnObject", None)
                if opp_val is None:
                    setattr(value, "containerPnObject", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ToolInfo107(self):
        return self.__ToolInfo107

    @ToolInfo107.setter
    def ToolInfo107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlcorestructure_ToolInfo__ToolInfo107", None)
        self.__ToolInfo107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "toolInfoModel"):
                opp_val = getattr(old_value, "toolInfoModel", None)
                if opp_val == self:
                    setattr(old_value, "toolInfoModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "toolInfoModel"):
                opp_val = getattr(value, "toolInfoModel", None)
                setattr(value, "toolInfoModel", self)

    @property
    def ToolInfo(self):
        return self.__ToolInfo

    @ToolInfo.setter
    def ToolInfo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlcorestructure_ToolInfo__ToolInfo", None)
        self.__ToolInfo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containerPetriNet4"):
                opp_val = getattr(old_value, "containerPetriNet4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containerPetriNet4"):
                opp_val = getattr(value, "containerPetriNet4", None)
                if opp_val is None:
                    setattr(value, "containerPetriNet4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def toolspecifics31(self):
        return self.__toolspecifics31

    @toolspecifics31.setter
    def toolspecifics31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlcorestructure_ToolInfo__toolspecifics31", None)
        self.__toolspecifics31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Label"):
                opp_val = getattr(old_value, "Label", None)
                if opp_val == self:
                    setattr(old_value, "Label", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Label"):
                opp_val = getattr(value, "Label", None)
                setattr(value, "Label", self)

class hlcorestructure_Name(Annotation):

    def __init__(self, text: str, Name: "hlcorestructure_PetriNet" = None, Name15: "hlcorestructure_PnObject" = None, name: "hlcorestructure_PetriNet" = None, name23: "hlcorestructure_PnObject" = None):
        self.text = text
        self.Name = Name
        self.Name15 = Name15
        self.name = name
        self.name23 = name23
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def Name15(self):
        return self.__Name15

    @Name15.setter
    def Name15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlcorestructure_Name__Name15", None)
        self.__Name15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containerNamePnObject"):
                opp_val = getattr(old_value, "containerNamePnObject", None)
                if opp_val == self:
                    setattr(old_value, "containerNamePnObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containerNamePnObject"):
                opp_val = getattr(value, "containerNamePnObject", None)
                setattr(value, "containerNamePnObject", self)

    @property
    def name23(self):
        return self.__name23

    @name23.setter
    def name23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlcorestructure_Name__name23", None)
        self.__name23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PnObject24"):
                opp_val = getattr(old_value, "PnObject24", None)
                if opp_val == self:
                    setattr(old_value, "PnObject24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PnObject24"):
                opp_val = getattr(value, "PnObject24", None)
                setattr(value, "PnObject24", self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlcorestructure_Name__name", None)
        self.__name = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet21"):
                opp_val = getattr(old_value, "PetriNet21", None)
                if opp_val == self:
                    setattr(old_value, "PetriNet21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet21"):
                opp_val = getattr(value, "PetriNet21", None)
                setattr(value, "PetriNet21", self)

    @property
    def Name(self):
        return self.__Name

    @Name.setter
    def Name(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlcorestructure_Name__Name", None)
        self.__Name = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containerNamePetriNet"):
                opp_val = getattr(old_value, "containerNamePetriNet", None)
                if opp_val == self:
                    setattr(old_value, "containerNamePetriNet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containerNamePetriNet"):
                opp_val = getattr(value, "containerNamePetriNet", None)
                setattr(value, "containerNamePetriNet", self)

class hlcorestructure_PetriNetDoc:

    def __init__(self, xmlns: str, containerPetriNetDoc: set["hlcorestructure_PetriNet"] = None, PetriNetDoc: "hlcorestructure_PetriNet" = None):
        self.xmlns = xmlns
        self.containerPetriNetDoc = containerPetriNetDoc if containerPetriNetDoc is not None else set()
        self.PetriNetDoc = PetriNetDoc
        
    @property
    def xmlns(self) -> str:
        return self.__xmlns

    @xmlns.setter
    def xmlns(self, xmlns: str):
        self.__xmlns = xmlns

    @property
    def PetriNetDoc(self):
        return self.__PetriNetDoc

    @PetriNetDoc.setter
    def PetriNetDoc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlcorestructure_PetriNetDoc__PetriNetDoc", None)
        self.__PetriNetDoc = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nets"):
                opp_val = getattr(old_value, "nets", None)
                if opp_val == self:
                    setattr(old_value, "nets", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nets"):
                opp_val = getattr(value, "nets", None)
                setattr(value, "nets", self)

    @property
    def containerPetriNetDoc(self):
        return self.__containerPetriNetDoc

    @containerPetriNetDoc.setter
    def containerPetriNetDoc(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlcorestructure_PetriNetDoc__containerPetriNetDoc", None)
        self.__containerPetriNetDoc = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PetriNet"):
                    opp_val = getattr(item, "PetriNet", None)
                    
                    if opp_val == self:
                        setattr(item, "PetriNet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PetriNet"):
                    opp_val = getattr(item, "PetriNet", None)
                    
                    setattr(item, "PetriNet", self)
                    

class hlcorestructure_PetriNet:

    def __init__(self, id: str, type: str, PetriNet: "hlcorestructure_PetriNetDoc" = None, containerNamePetriNet: "hlcorestructure_Name" = None, containerPetriNet4: set["hlcorestructure_ToolInfo"] = None, containerPetriNet: set["hlcorestructure_Page"] = None, PetriNet9: "hlcorestructure_Page" = None, nets: "hlcorestructure_PetriNetDoc" = None, containerDeclarationPetriNet: set["hlcorestructure_Declaration"] = None, PetriNet21: "hlcorestructure_Name" = None, PetriNet26: "hlcorestructure_ToolInfo" = None, PetriNet122: "hlcorestructure_Declaration" = None):
        self.id = id
        self.type = type
        self.PetriNet = PetriNet
        self.containerNamePetriNet = containerNamePetriNet
        self.containerPetriNet4 = containerPetriNet4 if containerPetriNet4 is not None else set()
        self.containerPetriNet = containerPetriNet if containerPetriNet is not None else set()
        self.PetriNet9 = PetriNet9
        self.nets = nets
        self.containerDeclarationPetriNet = containerDeclarationPetriNet if containerDeclarationPetriNet is not None else set()
        self.PetriNet21 = PetriNet21
        self.PetriNet26 = PetriNet26
        self.PetriNet122 = PetriNet122
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def containerPetriNet4(self):
        return self.__containerPetriNet4

    @containerPetriNet4.setter
    def containerPetriNet4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlcorestructure_PetriNet__containerPetriNet4", None)
        self.__containerPetriNet4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ToolInfo"):
                    opp_val = getattr(item, "ToolInfo", None)
                    
                    if opp_val == self:
                        setattr(item, "ToolInfo", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ToolInfo"):
                    opp_val = getattr(item, "ToolInfo", None)
                    
                    setattr(item, "ToolInfo", self)
                    

    @property
    def PetriNet26(self):
        return self.__PetriNet26

    @PetriNet26.setter
    def PetriNet26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlcorestructure_PetriNet__PetriNet26", None)
        self.__PetriNet26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "toolspecifics"):
                opp_val = getattr(old_value, "toolspecifics", None)
                if opp_val == self:
                    setattr(old_value, "toolspecifics", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "toolspecifics"):
                opp_val = getattr(value, "toolspecifics", None)
                setattr(value, "toolspecifics", self)

    @property
    def PetriNet122(self):
        return self.__PetriNet122

    @PetriNet122.setter
    def PetriNet122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlcorestructure_PetriNet__PetriNet122", None)
        self.__PetriNet122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "declaration"):
                opp_val = getattr(old_value, "declaration", None)
                if opp_val == self:
                    setattr(old_value, "declaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "declaration"):
                opp_val = getattr(value, "declaration", None)
                setattr(value, "declaration", self)

    @property
    def containerNamePetriNet(self):
        return self.__containerNamePetriNet

    @containerNamePetriNet.setter
    def containerNamePetriNet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlcorestructure_PetriNet__containerNamePetriNet", None)
        self.__containerNamePetriNet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Name"):
                opp_val = getattr(old_value, "Name", None)
                if opp_val == self:
                    setattr(old_value, "Name", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Name"):
                opp_val = getattr(value, "Name", None)
                setattr(value, "Name", self)

    @property
    def PetriNet(self):
        return self.__PetriNet

    @PetriNet.setter
    def PetriNet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlcorestructure_PetriNet__PetriNet", None)
        self.__PetriNet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containerPetriNetDoc"):
                opp_val = getattr(old_value, "containerPetriNetDoc", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containerPetriNetDoc"):
                opp_val = getattr(value, "containerPetriNetDoc", None)
                if opp_val is None:
                    setattr(value, "containerPetriNetDoc", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def nets(self):
        return self.__nets

    @nets.setter
    def nets(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlcorestructure_PetriNet__nets", None)
        self.__nets = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNetDoc"):
                opp_val = getattr(old_value, "PetriNetDoc", None)
                if opp_val == self:
                    setattr(old_value, "PetriNetDoc", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNetDoc"):
                opp_val = getattr(value, "PetriNetDoc", None)
                setattr(value, "PetriNetDoc", self)

    @property
    def containerPetriNet(self):
        return self.__containerPetriNet

    @containerPetriNet.setter
    def containerPetriNet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlcorestructure_PetriNet__containerPetriNet", None)
        self.__containerPetriNet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Page"):
                    opp_val = getattr(item, "Page", None)
                    
                    if opp_val == self:
                        setattr(item, "Page", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Page"):
                    opp_val = getattr(item, "Page", None)
                    
                    setattr(item, "Page", self)
                    

    @property
    def containerDeclarationPetriNet(self):
        return self.__containerDeclarationPetriNet

    @containerDeclarationPetriNet.setter
    def containerDeclarationPetriNet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlcorestructure_PetriNet__containerDeclarationPetriNet", None)
        self.__containerDeclarationPetriNet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Declaration"):
                    opp_val = getattr(item, "Declaration", None)
                    
                    if opp_val == self:
                        setattr(item, "Declaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Declaration"):
                    opp_val = getattr(item, "Declaration", None)
                    
                    setattr(item, "Declaration", self)
                    

    @property
    def PetriNet21(self):
        return self.__PetriNet21

    @PetriNet21.setter
    def PetriNet21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlcorestructure_PetriNet__PetriNet21", None)
        self.__PetriNet21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "name"):
                opp_val = getattr(old_value, "name", None)
                if opp_val == self:
                    setattr(old_value, "name", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "name"):
                opp_val = getattr(value, "name", None)
                setattr(value, "name", self)

    @property
    def PetriNet9(self):
        return self.__PetriNet9

    @PetriNet9.setter
    def PetriNet9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hlcorestructure_PetriNet__PetriNet9", None)
        self.__PetriNet9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pages"):
                opp_val = getattr(old_value, "pages", None)
                if opp_val == self:
                    setattr(old_value, "pages", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pages"):
                opp_val = getattr(value, "pages", None)
                setattr(value, "pages", self)
