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
class FontAlign(Enum):
    LEFT = "LEFT"
    CENTER = "CENTER"
    RIGHT = "RIGHT"
class CSS2FontFamily(Enum):
    VERDANA = "VERDANA"
    ARIAL = "ARIAL"
    TIMES = "TIMES"
    GEORGIA = "GEORGIA"
    TREBUCHET = "TREBUCHET"
class CSS2Color(Enum):
    AQUA = "AQUA"
    OLIVE = "OLIVE"
    ORANGE = "ORANGE"
    PURPLE = "PURPLE"
    RED = "RED"
    SILVER = "SILVER"
    TEAL = "TEAL"
    WHITE = "WHITE"
    YELLOW = "YELLOW"
    BLACK = "BLACK"
    BLUE = "BLUE"
    FUCHSIA = "FUCHSIA"
    GRAY = "GRAY"
    GREEN = "GREEN"
    LIME = "LIME"
    MAROON = "MAROON"
    NAVY = "NAVY"
class CSS2FontWeight(Enum):
    NORMAL = "NORMAL"
    BOLD = "BOLD"
    BOLDER = "BOLDER"
    LIGHTER = "LIGHTER"
class CSS2FontStyle(Enum):
    NORMAL = "NORMAL"
    ITALIC = "ITALIC"
    OBLIQUE = "OBLIQUE"
class Gradient(Enum):
    HORIZONTAL = "HORIZONTAL"
    VERTICAL = "VERTICAL"
    DIAGONAL = "DIAGONAL"
class CSS2FontSize(Enum):
    MEDIUM = "MEDIUM"
    LARGE = "LARGE"
    XLARGE = "XLARGE"
    XXLARGE = "XXLARGE"
    XXSMALL = "XXSMALL"
    XSMALL = "XSMALL"
    SMALL = "SMALL"
class PNType(Enum):
    COREMODEL = "COREMODEL"
    PTNET = "PTNET"
    SYMNET = "SYMNET"
    HLPN = "HLPN"
class LineShape(Enum):
    LINE = "LINE"
    CURVE = "CURVE"
class FontDecoration(Enum):
    UNDERLINE = "UNDERLINE"
    OVERLINE = "OVERLINE"
    LINETHROUGH = "LINETHROUGH"


############################################
# Definition of Classes
############################################

class Label:

    pass
class pnmlcoremodel_Attribute(Label):

    pass
class Node:

    pass
class pnmlcoremodel_TransitionNode(Node):

    pass
class pnmlcoremodel_PlaceNode(Node):

    pass
class TransitionNode:

    pass
class pnmlcoremodel_Transition(TransitionNode):

    pass
class PlaceNode:

    pass
class pnmlcoremodel_RefPlace(PlaceNode):

    pass
class pnmlcoremodel_Place(PlaceNode):

    pass
class pnmlcoremodel_RefTransition(TransitionNode):

    pass
class pnmlcoremodel_Annotation(Label):

    pass
class pnmlcoremodel_Font:

    def __init__(self, align: str, decoration: str, family: str, rotation: str, size: str, style: str, weight: str, Font: "pnmlcoremodel_AnnotationGraphics" = None, font: "pnmlcoremodel_AnnotationGraphics" = None):
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
    def family(self) -> str:
        return self.__family

    @family.setter
    def family(self, family: str):
        self.__family = family

    @property
    def align(self) -> str:
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align

    @property
    def weight(self) -> str:
        return self.__weight

    @weight.setter
    def weight(self, weight: str):
        self.__weight = weight

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
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def rotation(self) -> str:
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation: str):
        self.__rotation = rotation

    @property
    def Font(self):
        return self.__Font

    @Font.setter
    def Font(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_Font__Font", None)
        self.__Font = value
        
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
    def font(self):
        return self.__font

    @font.setter
    def font(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_Font__font", None)
        self.__font = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AnnotationGraphics89"):
                opp_val = getattr(old_value, "AnnotationGraphics89", None)
                if opp_val == self:
                    setattr(old_value, "AnnotationGraphics89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AnnotationGraphics89"):
                opp_val = getattr(value, "AnnotationGraphics89", None)
                setattr(value, "AnnotationGraphics89", self)

class pnmlcoremodel_Graphics(ABC):

    pass
class Coordinate:

    pass
class pnmlcoremodel_Offset(Coordinate):

    pass
class pnmlcoremodel_Coordinate(ABC):

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

class Graphics:

    pass
class pnmlcoremodel_AnnotationGraphics(Graphics):

    pass
class pnmlcoremodel_ArcGraphics(Graphics):

    pass
class pnmlcoremodel_AnyObject(ABC):

    pass
class pnmlcoremodel_Line:

    def __init__(self, style: str, color: str, shape: str, width: str, Line: "pnmlcoremodel_NodeGraphics" = None, Line53: "pnmlcoremodel_AnnotationGraphics" = None, line65: "pnmlcoremodel_ArcGraphics" = None, line68: "pnmlcoremodel_AnnotationGraphics" = None, line: "pnmlcoremodel_NodeGraphics" = None, Line74: "pnmlcoremodel_ArcGraphics" = None):
        self.style = style
        self.color = color
        self.shape = shape
        self.width = width
        self.Line = Line
        self.Line53 = Line53
        self.line65 = line65
        self.line68 = line68
        self.line = line
        self.Line74 = Line74
        
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def shape(self) -> str:
        return self.__shape

    @shape.setter
    def shape(self, shape: str):
        self.__shape = shape

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def line65(self):
        return self.__line65

    @line65.setter
    def line65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_Line__line65", None)
        self.__line65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ArcGraphics66"):
                opp_val = getattr(old_value, "ArcGraphics66", None)
                if opp_val == self:
                    setattr(old_value, "ArcGraphics66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ArcGraphics66"):
                opp_val = getattr(value, "ArcGraphics66", None)
                setattr(value, "ArcGraphics66", self)

    @property
    def Line(self):
        return self.__Line

    @Line.setter
    def Line(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_Line__Line", None)
        self.__Line = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containerNodeGraphics36"):
                opp_val = getattr(old_value, "containerNodeGraphics36", None)
                if opp_val == self:
                    setattr(old_value, "containerNodeGraphics36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containerNodeGraphics36"):
                opp_val = getattr(value, "containerNodeGraphics36", None)
                setattr(value, "containerNodeGraphics36", self)

    @property
    def line(self):
        return self.__line

    @line.setter
    def line(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_Line__line", None)
        self.__line = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NodeGraphics63"):
                opp_val = getattr(old_value, "NodeGraphics63", None)
                if opp_val == self:
                    setattr(old_value, "NodeGraphics63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NodeGraphics63"):
                opp_val = getattr(value, "NodeGraphics63", None)
                setattr(value, "NodeGraphics63", self)

    @property
    def Line74(self):
        return self.__Line74

    @Line74.setter
    def Line74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_Line__Line74", None)
        self.__Line74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containerArcGraphics73"):
                opp_val = getattr(old_value, "containerArcGraphics73", None)
                if opp_val == self:
                    setattr(old_value, "containerArcGraphics73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containerArcGraphics73"):
                opp_val = getattr(value, "containerArcGraphics73", None)
                setattr(value, "containerArcGraphics73", self)

    @property
    def Line53(self):
        return self.__Line53

    @Line53.setter
    def Line53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_Line__Line53", None)
        self.__Line53 = value
        
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
    def line68(self):
        return self.__line68

    @line68.setter
    def line68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_Line__line68", None)
        self.__line68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AnnotationGraphics69"):
                opp_val = getattr(old_value, "AnnotationGraphics69", None)
                if opp_val == self:
                    setattr(old_value, "AnnotationGraphics69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AnnotationGraphics69"):
                opp_val = getattr(value, "AnnotationGraphics69", None)
                setattr(value, "AnnotationGraphics69", self)

class pnmlcoremodel_Fill:

    def __init__(self, gradientcolor: str, gradientrotation: str, image: str, color: str, Fill: "pnmlcoremodel_NodeGraphics" = None, Fill50: "pnmlcoremodel_AnnotationGraphics" = None, fill: "pnmlcoremodel_NodeGraphics" = None, fill60: "pnmlcoremodel_AnnotationGraphics" = None):
        self.gradientcolor = gradientcolor
        self.gradientrotation = gradientrotation
        self.image = image
        self.color = color
        self.Fill = Fill
        self.Fill50 = Fill50
        self.fill = fill
        self.fill60 = fill60
        
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
    def gradientcolor(self) -> str:
        return self.__gradientcolor

    @gradientcolor.setter
    def gradientcolor(self, gradientcolor: str):
        self.__gradientcolor = gradientcolor

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
        old_value = getattr(self, f"_pnmlcoremodel_Fill__Fill", None)
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
        old_value = getattr(self, f"_pnmlcoremodel_Fill__fill", None)
        self.__fill = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NodeGraphics58"):
                opp_val = getattr(old_value, "NodeGraphics58", None)
                if opp_val == self:
                    setattr(old_value, "NodeGraphics58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NodeGraphics58"):
                opp_val = getattr(value, "NodeGraphics58", None)
                setattr(value, "NodeGraphics58", self)

    @property
    def fill60(self):
        return self.__fill60

    @fill60.setter
    def fill60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_Fill__fill60", None)
        self.__fill60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AnnotationGraphics61"):
                opp_val = getattr(old_value, "AnnotationGraphics61", None)
                if opp_val == self:
                    setattr(old_value, "AnnotationGraphics61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AnnotationGraphics61"):
                opp_val = getattr(value, "AnnotationGraphics61", None)
                setattr(value, "AnnotationGraphics61", self)

    @property
    def Fill50(self):
        return self.__Fill50

    @Fill50.setter
    def Fill50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_Fill__Fill50", None)
        self.__Fill50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containerAnnotationGraphics49"):
                opp_val = getattr(old_value, "containerAnnotationGraphics49", None)
                if opp_val == self:
                    setattr(old_value, "containerAnnotationGraphics49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containerAnnotationGraphics49"):
                opp_val = getattr(value, "containerAnnotationGraphics49", None)
                setattr(value, "containerAnnotationGraphics49", self)

class pnmlcoremodel_Dimension(Coordinate):

    pass
class pnmlcoremodel_Position(Coordinate):

    pass
class pnmlcoremodel_Label(ABC):

    pass
class pnmlcoremodel_NodeGraphics(Graphics):

    pass
class pnmlcoremodel_PnObject(ABC):

    def __init__(self, id: str, containerNamePnObject: "pnmlcoremodel_Name" = None, containerPnObject: set["pnmlcoremodel_ToolInfo"] = None, objects: "pnmlcoremodel_Page" = None, PnObject: "pnmlcoremodel_Page" = None, PnObject26: "pnmlcoremodel_ToolInfo" = None, PnObject21: "pnmlcoremodel_Name" = None):
        self.id = id
        self.containerNamePnObject = containerNamePnObject
        self.containerPnObject = containerPnObject if containerPnObject is not None else set()
        self.objects = objects
        self.PnObject = PnObject
        self.PnObject26 = PnObject26
        self.PnObject21 = PnObject21
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def PnObject26(self):
        return self.__PnObject26

    @PnObject26.setter
    def PnObject26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_PnObject__PnObject26", None)
        self.__PnObject26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "toolspecifics25"):
                opp_val = getattr(old_value, "toolspecifics25", None)
                if opp_val == self:
                    setattr(old_value, "toolspecifics25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "toolspecifics25"):
                opp_val = getattr(value, "toolspecifics25", None)
                setattr(value, "toolspecifics25", self)

    @property
    def PnObject21(self):
        return self.__PnObject21

    @PnObject21.setter
    def PnObject21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_PnObject__PnObject21", None)
        self.__PnObject21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "name20"):
                opp_val = getattr(old_value, "name20", None)
                if opp_val == self:
                    setattr(old_value, "name20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "name20"):
                opp_val = getattr(value, "name20", None)
                setattr(value, "name20", self)

    @property
    def containerNamePnObject(self):
        return self.__containerNamePnObject

    @containerNamePnObject.setter
    def containerNamePnObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_PnObject__containerNamePnObject", None)
        self.__containerNamePnObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Name12"):
                opp_val = getattr(old_value, "Name12", None)
                if opp_val == self:
                    setattr(old_value, "Name12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Name12"):
                opp_val = getattr(value, "Name12", None)
                setattr(value, "Name12", self)

    @property
    def objects(self):
        return self.__objects

    @objects.setter
    def objects(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_PnObject__objects", None)
        self.__objects = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Page16"):
                opp_val = getattr(old_value, "Page16", None)
                if opp_val == self:
                    setattr(old_value, "Page16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Page16"):
                opp_val = getattr(value, "Page16", None)
                setattr(value, "Page16", self)

    @property
    def containerPnObject(self):
        return self.__containerPnObject

    @containerPnObject.setter
    def containerPnObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_PnObject__containerPnObject", None)
        self.__containerPnObject = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ToolInfo14"):
                    opp_val = getattr(item, "ToolInfo14", None)
                    
                    if opp_val == self:
                        setattr(item, "ToolInfo14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ToolInfo14"):
                    opp_val = getattr(item, "ToolInfo14", None)
                    
                    setattr(item, "ToolInfo14", self)
                    

    @property
    def PnObject(self):
        return self.__PnObject

    @PnObject.setter
    def PnObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_PnObject__PnObject", None)
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

class Annotation:

    pass
class pnmlcoremodel_ToolInfo:

    def __init__(self, tool: str, version: str, formattedXMLBuffer: str, toolInfoGrammarURI: str, ToolInfo: "pnmlcoremodel_PetriNet" = None, ToolInfo14: "pnmlcoremodel_PnObject" = None, toolspecifics: "pnmlcoremodel_PetriNet" = None, toolspecifics25: "pnmlcoremodel_PnObject" = None, toolspecifics28: "pnmlcoremodel_Label" = None, containerToolInfo: "pnmlcoremodel_AnyObject" = None, ToolInfo31: "pnmlcoremodel_Label" = None, ToolInfo98: "pnmlcoremodel_AnyObject" = None):
        self.tool = tool
        self.version = version
        self.formattedXMLBuffer = formattedXMLBuffer
        self.toolInfoGrammarURI = toolInfoGrammarURI
        self.ToolInfo = ToolInfo
        self.ToolInfo14 = ToolInfo14
        self.toolspecifics = toolspecifics
        self.toolspecifics25 = toolspecifics25
        self.toolspecifics28 = toolspecifics28
        self.containerToolInfo = containerToolInfo
        self.ToolInfo31 = ToolInfo31
        self.ToolInfo98 = ToolInfo98
        
    @property
    def formattedXMLBuffer(self) -> str:
        return self.__formattedXMLBuffer

    @formattedXMLBuffer.setter
    def formattedXMLBuffer(self, formattedXMLBuffer: str):
        self.__formattedXMLBuffer = formattedXMLBuffer

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def toolInfoGrammarURI(self) -> str:
        return self.__toolInfoGrammarURI

    @toolInfoGrammarURI.setter
    def toolInfoGrammarURI(self, toolInfoGrammarURI: str):
        self.__toolInfoGrammarURI = toolInfoGrammarURI

    @property
    def tool(self) -> str:
        return self.__tool

    @tool.setter
    def tool(self, tool: str):
        self.__tool = tool

    @property
    def toolspecifics28(self):
        return self.__toolspecifics28

    @toolspecifics28.setter
    def toolspecifics28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_ToolInfo__toolspecifics28", None)
        self.__toolspecifics28 = value
        
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

    @property
    def toolspecifics25(self):
        return self.__toolspecifics25

    @toolspecifics25.setter
    def toolspecifics25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_ToolInfo__toolspecifics25", None)
        self.__toolspecifics25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PnObject26"):
                opp_val = getattr(old_value, "PnObject26", None)
                if opp_val == self:
                    setattr(old_value, "PnObject26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PnObject26"):
                opp_val = getattr(value, "PnObject26", None)
                setattr(value, "PnObject26", self)

    @property
    def containerToolInfo(self):
        return self.__containerToolInfo

    @containerToolInfo.setter
    def containerToolInfo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_ToolInfo__containerToolInfo", None)
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
    def toolspecifics(self):
        return self.__toolspecifics

    @toolspecifics.setter
    def toolspecifics(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_ToolInfo__toolspecifics", None)
        self.__toolspecifics = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet23"):
                opp_val = getattr(old_value, "PetriNet23", None)
                if opp_val == self:
                    setattr(old_value, "PetriNet23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet23"):
                opp_val = getattr(value, "PetriNet23", None)
                setattr(value, "PetriNet23", self)

    @property
    def ToolInfo(self):
        return self.__ToolInfo

    @ToolInfo.setter
    def ToolInfo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_ToolInfo__ToolInfo", None)
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
    def ToolInfo98(self):
        return self.__ToolInfo98

    @ToolInfo98.setter
    def ToolInfo98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_ToolInfo__ToolInfo98", None)
        self.__ToolInfo98 = value
        
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
    def ToolInfo31(self):
        return self.__ToolInfo31

    @ToolInfo31.setter
    def ToolInfo31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_ToolInfo__ToolInfo31", None)
        self.__ToolInfo31 = value
        
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
    def ToolInfo14(self):
        return self.__ToolInfo14

    @ToolInfo14.setter
    def ToolInfo14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_ToolInfo__ToolInfo14", None)
        self.__ToolInfo14 = value
        
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

class pnmlcoremodel_Name(Annotation):

    def __init__(self, text: str, Name: "pnmlcoremodel_PetriNet" = None, Name12: "pnmlcoremodel_PnObject" = None, name: "pnmlcoremodel_PetriNet" = None, name20: "pnmlcoremodel_PnObject" = None):
        self.text = text
        self.Name = Name
        self.Name12 = Name12
        self.name = name
        self.name20 = name20
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_Name__name", None)
        self.__name = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet18"):
                opp_val = getattr(old_value, "PetriNet18", None)
                if opp_val == self:
                    setattr(old_value, "PetriNet18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet18"):
                opp_val = getattr(value, "PetriNet18", None)
                setattr(value, "PetriNet18", self)

    @property
    def name20(self):
        return self.__name20

    @name20.setter
    def name20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_Name__name20", None)
        self.__name20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PnObject21"):
                opp_val = getattr(old_value, "PnObject21", None)
                if opp_val == self:
                    setattr(old_value, "PnObject21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PnObject21"):
                opp_val = getattr(value, "PnObject21", None)
                setattr(value, "PnObject21", self)

    @property
    def Name12(self):
        return self.__Name12

    @Name12.setter
    def Name12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_Name__Name12", None)
        self.__Name12 = value
        
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
    def Name(self):
        return self.__Name

    @Name.setter
    def Name(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_Name__Name", None)
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

class PnObject:

    pass
class pnmlcoremodel_Node(PnObject):

    pass
class pnmlcoremodel_Arc(PnObject):

    pass
class pnmlcoremodel_Page(PnObject):

    pass
class pnmlcoremodel_PetriNetDoc:

    def __init__(self, xmlns: str, containerPetriNetDoc: set["pnmlcoremodel_PetriNet"] = None, PetriNetDoc: "pnmlcoremodel_PetriNet" = None):
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
        old_value = getattr(self, f"_pnmlcoremodel_PetriNetDoc__PetriNetDoc", None)
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
        old_value = getattr(self, f"_pnmlcoremodel_PetriNetDoc__containerPetriNetDoc", None)
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
                    

class pnmlcoremodel_PetriNet:

    def __init__(self, id: str, type: str, PetriNet: "pnmlcoremodel_PetriNetDoc" = None, nets: "pnmlcoremodel_PetriNetDoc" = None, containerPetriNet: set["pnmlcoremodel_Page"] = None, containerNamePetriNet: "pnmlcoremodel_Name" = None, containerPetriNet4: set["pnmlcoremodel_ToolInfo"] = None, PetriNet8: "pnmlcoremodel_Page" = None, PetriNet23: "pnmlcoremodel_ToolInfo" = None, PetriNet18: "pnmlcoremodel_Name" = None):
        self.id = id
        self.type = type
        self.PetriNet = PetriNet
        self.nets = nets
        self.containerPetriNet = containerPetriNet if containerPetriNet is not None else set()
        self.containerNamePetriNet = containerNamePetriNet
        self.containerPetriNet4 = containerPetriNet4 if containerPetriNet4 is not None else set()
        self.PetriNet8 = PetriNet8
        self.PetriNet23 = PetriNet23
        self.PetriNet18 = PetriNet18
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def containerPetriNet(self):
        return self.__containerPetriNet

    @containerPetriNet.setter
    def containerPetriNet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_PetriNet__containerPetriNet", None)
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
    def nets(self):
        return self.__nets

    @nets.setter
    def nets(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_PetriNet__nets", None)
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
    def PetriNet(self):
        return self.__PetriNet

    @PetriNet.setter
    def PetriNet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_PetriNet__PetriNet", None)
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
    def containerNamePetriNet(self):
        return self.__containerNamePetriNet

    @containerNamePetriNet.setter
    def containerNamePetriNet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_PetriNet__containerNamePetriNet", None)
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
    def PetriNet18(self):
        return self.__PetriNet18

    @PetriNet18.setter
    def PetriNet18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_PetriNet__PetriNet18", None)
        self.__PetriNet18 = value
        
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
    def PetriNet8(self):
        return self.__PetriNet8

    @PetriNet8.setter
    def PetriNet8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_PetriNet__PetriNet8", None)
        self.__PetriNet8 = value
        
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

    @property
    def PetriNet23(self):
        return self.__PetriNet23

    @PetriNet23.setter
    def PetriNet23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_PetriNet__PetriNet23", None)
        self.__PetriNet23 = value
        
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
    def containerPetriNet4(self):
        return self.__containerPetriNet4

    @containerPetriNet4.setter
    def containerPetriNet4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_PetriNet__containerPetriNet4", None)
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
                    
