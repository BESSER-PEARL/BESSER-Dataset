from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class CSS2FontSize(Enum):
    XXSMALL = "XXSMALL"
    XSMALL = "XSMALL"
    SMALL = "SMALL"
    MEDIUM = "MEDIUM"
    LARGE = "LARGE"
    XLARGE = "XLARGE"
    XXLARGE = "XXLARGE"
class Gradient(Enum):
    HORIZONTAL = "HORIZONTAL"
    VERTICAL = "VERTICAL"
    DIAGONAL = "DIAGONAL"
class CSS2FontStyle(Enum):
    NORMAL = "NORMAL"
    ITALIC = "ITALIC"
    OBLIQUE = "OBLIQUE"
class PNType(Enum):
    PTNET = "PTNET"
    COREMODEL = "COREMODEL"
    SYMNET = "SYMNET"
    HLPN = "HLPN"
class LineStyle(Enum):
    SOLID = "SOLID"
    DASH = "DASH"
    DOT = "DOT"
class CSS2FontWeight(Enum):
    NORMAL = "NORMAL"
    BOLD = "BOLD"
    BOLDER = "BOLDER"
    LIGHTER = "LIGHTER"
class CSS2FontFamily(Enum):
    TREBUCHET = "TREBUCHET"
    VERDANA = "VERDANA"
    ARIAL = "ARIAL"
    TIMES = "TIMES"
    GEORGIA = "GEORGIA"
class FontAlign(Enum):
    LEFT = "LEFT"
    CENTER = "CENTER"
    RIGHT = "RIGHT"
class LineShape(Enum):
    LINE = "LINE"
    CURVE = "CURVE"
class FontDecoration(Enum):
    UNDERLINE = "UNDERLINE"
    OVERLINE = "OVERLINE"
    LINETHROUGH = "LINETHROUGH"
class CSS2Color(Enum):
    AQUA = "AQUA"
    BLACK = "BLACK"
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
    SILVER = "SILVER"
    TEAL = "TEAL"
    WHITE = "WHITE"
    YELLOW = "YELLOW"


############################################
# Definition of Classes
############################################

class PlaceNode:

    pass
class ptnet_RefPlace(PlaceNode):

    pass
class Label:

    pass
class ptnet_Attribute(Label):

    pass
class TransitionNode:

    pass
class ptnet_RefTransition(TransitionNode):

    pass
class ptnet_Transition(TransitionNode):

    pass
class Node:

    pass
class ptnet_TransitionNode(Node):

    pass
class ptnet_PlaceNode(Node):

    pass
class ptnet_Annotation(Label):

    pass
class ptnet_Font:

    def __init__(self, align: str, decoration: str, family: str, rotation: str, size: str, style: str, weight: str, Font: "ptnet_AnnotationGraphics" = None, font: "ptnet_AnnotationGraphics" = None):
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
    def family(self) -> str:
        return self.__family

    @family.setter
    def family(self, family: str):
        self.__family = family

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

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
    def align(self) -> str:
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align

    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

    @property
    def font(self):
        return self.__font

    @font.setter
    def font(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnet_Font__font", None)
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
        old_value = getattr(self, f"_ptnet_Font__Font", None)
        self.__Font = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containerAnnotationGraphics57"):
                opp_val = getattr(old_value, "containerAnnotationGraphics57", None)
                if opp_val == self:
                    setattr(old_value, "containerAnnotationGraphics57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containerAnnotationGraphics57"):
                opp_val = getattr(value, "containerAnnotationGraphics57", None)
                setattr(value, "containerAnnotationGraphics57", self)

class ptnet_AnyObject(ABC):

    pass
class ptnet_Label(ABC):

    pass
class Coordinate:

    pass
class ptnet_Offset(Coordinate):

    pass
class ptnet_Coordinate(ABC):

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

class ptnet_Graphics(ABC):

    pass
class ptnet_Line:

    def __init__(self, style: str, color: str, shape: str, width: str, Line: "ptnet_NodeGraphics" = None, Line55: "ptnet_AnnotationGraphics" = None, line67: "ptnet_ArcGraphics" = None, line70: "ptnet_AnnotationGraphics" = None, Line76: "ptnet_ArcGraphics" = None, line: "ptnet_NodeGraphics" = None):
        self.style = style
        self.color = color
        self.shape = shape
        self.width = width
        self.Line = Line
        self.Line55 = Line55
        self.line67 = line67
        self.line70 = line70
        self.Line76 = Line76
        self.line = line
        
    @property
    def shape(self) -> str:
        return self.__shape

    @shape.setter
    def shape(self, shape: str):
        self.__shape = shape

    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def line(self):
        return self.__line

    @line.setter
    def line(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnet_Line__line", None)
        self.__line = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NodeGraphics65"):
                opp_val = getattr(old_value, "NodeGraphics65", None)
                if opp_val == self:
                    setattr(old_value, "NodeGraphics65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NodeGraphics65"):
                opp_val = getattr(value, "NodeGraphics65", None)
                setattr(value, "NodeGraphics65", self)

    @property
    def Line(self):
        return self.__Line

    @Line.setter
    def Line(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnet_Line__Line", None)
        self.__Line = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containerNodeGraphics38"):
                opp_val = getattr(old_value, "containerNodeGraphics38", None)
                if opp_val == self:
                    setattr(old_value, "containerNodeGraphics38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containerNodeGraphics38"):
                opp_val = getattr(value, "containerNodeGraphics38", None)
                setattr(value, "containerNodeGraphics38", self)

    @property
    def line67(self):
        return self.__line67

    @line67.setter
    def line67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnet_Line__line67", None)
        self.__line67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ArcGraphics68"):
                opp_val = getattr(old_value, "ArcGraphics68", None)
                if opp_val == self:
                    setattr(old_value, "ArcGraphics68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ArcGraphics68"):
                opp_val = getattr(value, "ArcGraphics68", None)
                setattr(value, "ArcGraphics68", self)

    @property
    def Line76(self):
        return self.__Line76

    @Line76.setter
    def Line76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnet_Line__Line76", None)
        self.__Line76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containerArcGraphics75"):
                opp_val = getattr(old_value, "containerArcGraphics75", None)
                if opp_val == self:
                    setattr(old_value, "containerArcGraphics75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containerArcGraphics75"):
                opp_val = getattr(value, "containerArcGraphics75", None)
                setattr(value, "containerArcGraphics75", self)

    @property
    def Line55(self):
        return self.__Line55

    @Line55.setter
    def Line55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnet_Line__Line55", None)
        self.__Line55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containerAnnotationGraphics54"):
                opp_val = getattr(old_value, "containerAnnotationGraphics54", None)
                if opp_val == self:
                    setattr(old_value, "containerAnnotationGraphics54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containerAnnotationGraphics54"):
                opp_val = getattr(value, "containerAnnotationGraphics54", None)
                setattr(value, "containerAnnotationGraphics54", self)

    @property
    def line70(self):
        return self.__line70

    @line70.setter
    def line70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnet_Line__line70", None)
        self.__line70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AnnotationGraphics71"):
                opp_val = getattr(old_value, "AnnotationGraphics71", None)
                if opp_val == self:
                    setattr(old_value, "AnnotationGraphics71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AnnotationGraphics71"):
                opp_val = getattr(value, "AnnotationGraphics71", None)
                setattr(value, "AnnotationGraphics71", self)

class ptnet_Fill:

    def __init__(self, color: str, gradientcolor: str, gradientrotation: str, image: str, Fill: "ptnet_NodeGraphics" = None, fill: "ptnet_NodeGraphics" = None, fill62: "ptnet_AnnotationGraphics" = None, Fill52: "ptnet_AnnotationGraphics" = None):
        self.color = color
        self.gradientcolor = gradientcolor
        self.gradientrotation = gradientrotation
        self.image = image
        self.Fill = Fill
        self.fill = fill
        self.fill62 = fill62
        self.Fill52 = Fill52
        
    @property
    def gradientrotation(self) -> str:
        return self.__gradientrotation

    @gradientrotation.setter
    def gradientrotation(self, gradientrotation: str):
        self.__gradientrotation = gradientrotation

    @property
    def image(self) -> str:
        return self.__image

    @image.setter
    def image(self, image: str):
        self.__image = image

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def gradientcolor(self) -> str:
        return self.__gradientcolor

    @gradientcolor.setter
    def gradientcolor(self, gradientcolor: str):
        self.__gradientcolor = gradientcolor

    @property
    def fill62(self):
        return self.__fill62

    @fill62.setter
    def fill62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnet_Fill__fill62", None)
        self.__fill62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AnnotationGraphics63"):
                opp_val = getattr(old_value, "AnnotationGraphics63", None)
                if opp_val == self:
                    setattr(old_value, "AnnotationGraphics63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AnnotationGraphics63"):
                opp_val = getattr(value, "AnnotationGraphics63", None)
                setattr(value, "AnnotationGraphics63", self)

    @property
    def fill(self):
        return self.__fill

    @fill.setter
    def fill(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnet_Fill__fill", None)
        self.__fill = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "NodeGraphics60"):
                opp_val = getattr(old_value, "NodeGraphics60", None)
                if opp_val == self:
                    setattr(old_value, "NodeGraphics60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "NodeGraphics60"):
                opp_val = getattr(value, "NodeGraphics60", None)
                setattr(value, "NodeGraphics60", self)

    @property
    def Fill(self):
        return self.__Fill

    @Fill.setter
    def Fill(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnet_Fill__Fill", None)
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
    def Fill52(self):
        return self.__Fill52

    @Fill52.setter
    def Fill52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnet_Fill__Fill52", None)
        self.__Fill52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containerAnnotationGraphics51"):
                opp_val = getattr(old_value, "containerAnnotationGraphics51", None)
                if opp_val == self:
                    setattr(old_value, "containerAnnotationGraphics51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containerAnnotationGraphics51"):
                opp_val = getattr(value, "containerAnnotationGraphics51", None)
                setattr(value, "containerAnnotationGraphics51", self)

class ptnet_Dimension(Coordinate):

    pass
class ptnet_Position(Coordinate):

    pass
class Graphics:

    pass
class ptnet_AnnotationGraphics(Graphics):

    pass
class ptnet_ArcGraphics(Graphics):

    pass
class ptnet_PnObject(ABC):

    def __init__(self, id: str, PnObject: "ptnet_Page" = None, containerNamePnObject: "ptnet_Name" = None, containerPnObject: set["ptnet_ToolInfo"] = None, objects: "ptnet_Page" = None, PnObject23: "ptnet_Name" = None, PnObject28: "ptnet_ToolInfo" = None):
        self.id = id
        self.PnObject = PnObject
        self.containerNamePnObject = containerNamePnObject
        self.containerPnObject = containerPnObject if containerPnObject is not None else set()
        self.objects = objects
        self.PnObject23 = PnObject23
        self.PnObject28 = PnObject28
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def containerPnObject(self):
        return self.__containerPnObject

    @containerPnObject.setter
    def containerPnObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnet_PnObject__containerPnObject", None)
        self.__containerPnObject = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ToolInfo16"):
                    opp_val = getattr(item, "ToolInfo16", None)
                    
                    if opp_val == self:
                        setattr(item, "ToolInfo16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ToolInfo16"):
                    opp_val = getattr(item, "ToolInfo16", None)
                    
                    setattr(item, "ToolInfo16", self)
                    

    @property
    def PnObject(self):
        return self.__PnObject

    @PnObject.setter
    def PnObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnet_PnObject__PnObject", None)
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
    def PnObject23(self):
        return self.__PnObject23

    @PnObject23.setter
    def PnObject23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnet_PnObject__PnObject23", None)
        self.__PnObject23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "name22"):
                opp_val = getattr(old_value, "name22", None)
                if opp_val == self:
                    setattr(old_value, "name22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "name22"):
                opp_val = getattr(value, "name22", None)
                setattr(value, "name22", self)

    @property
    def containerNamePnObject(self):
        return self.__containerNamePnObject

    @containerNamePnObject.setter
    def containerNamePnObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnet_PnObject__containerNamePnObject", None)
        self.__containerNamePnObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Name14"):
                opp_val = getattr(old_value, "Name14", None)
                if opp_val == self:
                    setattr(old_value, "Name14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Name14"):
                opp_val = getattr(value, "Name14", None)
                setattr(value, "Name14", self)

    @property
    def objects(self):
        return self.__objects

    @objects.setter
    def objects(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnet_PnObject__objects", None)
        self.__objects = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Page18"):
                opp_val = getattr(old_value, "Page18", None)
                if opp_val == self:
                    setattr(old_value, "Page18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Page18"):
                opp_val = getattr(value, "Page18", None)
                setattr(value, "Page18", self)

    @property
    def PnObject28(self):
        return self.__PnObject28

    @PnObject28.setter
    def PnObject28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnet_PnObject__PnObject28", None)
        self.__PnObject28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "toolspecifics27"):
                opp_val = getattr(old_value, "toolspecifics27", None)
                if opp_val == self:
                    setattr(old_value, "toolspecifics27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "toolspecifics27"):
                opp_val = getattr(value, "toolspecifics27", None)
                setattr(value, "toolspecifics27", self)

class PnObject:

    pass
class ptnet_Node(PnObject):

    pass
class ptnet_ToolInfo:

    def __init__(self, tool: str, version: str, formattedXMLBuffer: str, toolInfoGrammarURI: str, ToolInfo16: "ptnet_PnObject" = None, ToolInfo: "ptnet_PetriNet" = None, ToolInfo33: "ptnet_Label" = None, toolspecifics: "ptnet_PetriNet" = None, toolspecifics27: "ptnet_PnObject" = None, toolspecifics30: "ptnet_Label" = None, containerToolInfo: "ptnet_AnyObject" = None, ToolInfo104: "ptnet_AnyObject" = None):
        self.tool = tool
        self.version = version
        self.formattedXMLBuffer = formattedXMLBuffer
        self.toolInfoGrammarURI = toolInfoGrammarURI
        self.ToolInfo16 = ToolInfo16
        self.ToolInfo = ToolInfo
        self.ToolInfo33 = ToolInfo33
        self.toolspecifics = toolspecifics
        self.toolspecifics27 = toolspecifics27
        self.toolspecifics30 = toolspecifics30
        self.containerToolInfo = containerToolInfo
        self.ToolInfo104 = ToolInfo104
        
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
    def ToolInfo(self):
        return self.__ToolInfo

    @ToolInfo.setter
    def ToolInfo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnet_ToolInfo__ToolInfo", None)
        self.__ToolInfo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containerPetriNet6"):
                opp_val = getattr(old_value, "containerPetriNet6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containerPetriNet6"):
                opp_val = getattr(value, "containerPetriNet6", None)
                if opp_val is None:
                    setattr(value, "containerPetriNet6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def toolspecifics30(self):
        return self.__toolspecifics30

    @toolspecifics30.setter
    def toolspecifics30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnet_ToolInfo__toolspecifics30", None)
        self.__toolspecifics30 = value
        
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
    def toolspecifics27(self):
        return self.__toolspecifics27

    @toolspecifics27.setter
    def toolspecifics27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnet_ToolInfo__toolspecifics27", None)
        self.__toolspecifics27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PnObject28"):
                opp_val = getattr(old_value, "PnObject28", None)
                if opp_val == self:
                    setattr(old_value, "PnObject28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PnObject28"):
                opp_val = getattr(value, "PnObject28", None)
                setattr(value, "PnObject28", self)

    @property
    def containerToolInfo(self):
        return self.__containerToolInfo

    @containerToolInfo.setter
    def containerToolInfo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnet_ToolInfo__containerToolInfo", None)
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
    def ToolInfo16(self):
        return self.__ToolInfo16

    @ToolInfo16.setter
    def ToolInfo16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnet_ToolInfo__ToolInfo16", None)
        self.__ToolInfo16 = value
        
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
    def ToolInfo104(self):
        return self.__ToolInfo104

    @ToolInfo104.setter
    def ToolInfo104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnet_ToolInfo__ToolInfo104", None)
        self.__ToolInfo104 = value
        
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
    def ToolInfo33(self):
        return self.__ToolInfo33

    @ToolInfo33.setter
    def ToolInfo33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnet_ToolInfo__ToolInfo33", None)
        self.__ToolInfo33 = value
        
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
    def toolspecifics(self):
        return self.__toolspecifics

    @toolspecifics.setter
    def toolspecifics(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnet_ToolInfo__toolspecifics", None)
        self.__toolspecifics = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet25"):
                opp_val = getattr(old_value, "PetriNet25", None)
                if opp_val == self:
                    setattr(old_value, "PetriNet25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet25"):
                opp_val = getattr(value, "PetriNet25", None)
                setattr(value, "PetriNet25", self)

class ptnet_NodeGraphics(Graphics):

    pass
class ptnet_Arc(PnObject):

    pass
class ptnet_Place(PlaceNode):

    pass
class Annotation:

    pass
class ptnet_Name(Annotation):

    def __init__(self, text: str, Name14: "ptnet_PnObject" = None, name: "ptnet_PetriNet" = None, name22: "ptnet_PnObject" = None, Name: "ptnet_PetriNet" = None):
        self.text = text
        self.Name14 = Name14
        self.name = name
        self.name22 = name22
        self.Name = Name
        
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
        old_value = getattr(self, f"_ptnet_Name__name", None)
        self.__name = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PetriNet20"):
                opp_val = getattr(old_value, "PetriNet20", None)
                if opp_val == self:
                    setattr(old_value, "PetriNet20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PetriNet20"):
                opp_val = getattr(value, "PetriNet20", None)
                setattr(value, "PetriNet20", self)

    @property
    def Name(self):
        return self.__Name

    @Name.setter
    def Name(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnet_Name__Name", None)
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

    @property
    def Name14(self):
        return self.__Name14

    @Name14.setter
    def Name14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnet_Name__Name14", None)
        self.__Name14 = value
        
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
    def name22(self):
        return self.__name22

    @name22.setter
    def name22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnet_Name__name22", None)
        self.__name22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PnObject23"):
                opp_val = getattr(old_value, "PnObject23", None)
                if opp_val == self:
                    setattr(old_value, "PnObject23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PnObject23"):
                opp_val = getattr(value, "PnObject23", None)
                setattr(value, "PnObject23", self)

class ptnet_PTArcAnnotation(Annotation):

    def __init__(self, text: str, inscription: "ptnet_Arc" = None, PTArcAnnotation: "ptnet_Arc" = None):
        self.text = text
        self.inscription = inscription
        self.PTArcAnnotation = PTArcAnnotation
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def PTArcAnnotation(self):
        return self.__PTArcAnnotation

    @PTArcAnnotation.setter
    def PTArcAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnet_PTArcAnnotation__PTArcAnnotation", None)
        self.__PTArcAnnotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containerArc86"):
                opp_val = getattr(old_value, "containerArc86", None)
                if opp_val == self:
                    setattr(old_value, "containerArc86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containerArc86"):
                opp_val = getattr(value, "containerArc86", None)
                setattr(value, "containerArc86", self)

    @property
    def inscription(self):
        return self.__inscription

    @inscription.setter
    def inscription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnet_PTArcAnnotation__inscription", None)
        self.__inscription = value
        
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

class ptnet_Page(PnObject):

    pass
class ptnet_PetriNet:

    def __init__(self, id: str, type: str, PetriNet: "ptnet_PetriNetDoc" = None, containerPetriNet: set["ptnet_Page"] = None, PetriNet10: "ptnet_Page" = None, PetriNet20: "ptnet_Name" = None, containerNamePetriNet: "ptnet_Name" = None, containerPetriNet6: set["ptnet_ToolInfo"] = None, nets: "ptnet_PetriNetDoc" = None, PetriNet25: "ptnet_ToolInfo" = None):
        self.id = id
        self.type = type
        self.PetriNet = PetriNet
        self.containerPetriNet = containerPetriNet if containerPetriNet is not None else set()
        self.PetriNet10 = PetriNet10
        self.PetriNet20 = PetriNet20
        self.containerNamePetriNet = containerNamePetriNet
        self.containerPetriNet6 = containerPetriNet6 if containerPetriNet6 is not None else set()
        self.nets = nets
        self.PetriNet25 = PetriNet25
        
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
    def nets(self):
        return self.__nets

    @nets.setter
    def nets(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnet_PetriNet__nets", None)
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
        old_value = getattr(self, f"_ptnet_PetriNet__containerPetriNet", None)
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
    def PetriNet(self):
        return self.__PetriNet

    @PetriNet.setter
    def PetriNet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnet_PetriNet__PetriNet", None)
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
        old_value = getattr(self, f"_ptnet_PetriNet__containerNamePetriNet", None)
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
    def containerPetriNet6(self):
        return self.__containerPetriNet6

    @containerPetriNet6.setter
    def containerPetriNet6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnet_PetriNet__containerPetriNet6", None)
        self.__containerPetriNet6 = value if value is not None else set()
        
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
    def PetriNet25(self):
        return self.__PetriNet25

    @PetriNet25.setter
    def PetriNet25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnet_PetriNet__PetriNet25", None)
        self.__PetriNet25 = value
        
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
    def PetriNet20(self):
        return self.__PetriNet20

    @PetriNet20.setter
    def PetriNet20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnet_PetriNet__PetriNet20", None)
        self.__PetriNet20 = value
        
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
    def PetriNet10(self):
        return self.__PetriNet10

    @PetriNet10.setter
    def PetriNet10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnet_PetriNet__PetriNet10", None)
        self.__PetriNet10 = value
        
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

class ptnet_PetriNetDoc:

    def __init__(self, xmlns: str, containerPetriNetDoc: set["ptnet_PetriNet"] = None, PetriNetDoc: "ptnet_PetriNet" = None):
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
        old_value = getattr(self, f"_ptnet_PetriNetDoc__PetriNetDoc", None)
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
        old_value = getattr(self, f"_ptnet_PetriNetDoc__containerPetriNetDoc", None)
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
                    

class ptnet_PTMarking(Annotation):

    def __init__(self, text: str, initialMarking: "ptnet_Place" = None, PTMarking: "ptnet_Place" = None):
        self.text = text
        self.initialMarking = initialMarking
        self.PTMarking = PTMarking
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def initialMarking(self):
        return self.__initialMarking

    @initialMarking.setter
    def initialMarking(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnet_PTMarking__initialMarking", None)
        self.__initialMarking = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Place"):
                opp_val = getattr(old_value, "Place", None)
                if opp_val == self:
                    setattr(old_value, "Place", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Place"):
                opp_val = getattr(value, "Place", None)
                setattr(value, "Place", self)

    @property
    def PTMarking(self):
        return self.__PTMarking

    @PTMarking.setter
    def PTMarking(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ptnet_PTMarking__PTMarking", None)
        self.__PTMarking = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containerPlace"):
                opp_val = getattr(old_value, "containerPlace", None)
                if opp_val == self:
                    setattr(old_value, "containerPlace", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containerPlace"):
                opp_val = getattr(value, "containerPlace", None)
                setattr(value, "containerPlace", self)
