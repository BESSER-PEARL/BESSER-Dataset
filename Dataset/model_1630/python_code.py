from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class LineShape(Enum):
    line = "line"
    curve = "curve"


############################################
# Definition of Classes
############################################

class pnmlcoremodel_ID(ABC):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class ToolInfo:

    pass
class pnmlcoremodel_ToolInfoText(ToolInfo):

    def __init__(self, info: str):
        self.info = info
        
    @property
    def info(self) -> str:
        return self.__info

    @info.setter
    def info(self, info: str):
        self.__info = info

class PetriNetType:

    pass
class pnmlcoremodel_EmptyType(PetriNetType):

    pass
class pnmlcoremodel_Fill:

    def __init__(self, color: str, image: str, gradientColor: str, gradientrotation: str, pnmlcoremodel_Fill: "pnmlcoremodel_NodeGraphics" = None, pnmlcoremodel_Fill64: "pnmlcoremodel_AnnotationGraphics" = None):
        self.color = color
        self.image = image
        self.gradientColor = gradientColor
        self.gradientrotation = gradientrotation
        self.pnmlcoremodel_Fill = pnmlcoremodel_Fill
        self.pnmlcoremodel_Fill64 = pnmlcoremodel_Fill64
        
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

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
    def gradientColor(self) -> str:
        return self.__gradientColor

    @gradientColor.setter
    def gradientColor(self, gradientColor: str):
        self.__gradientColor = gradientColor

    @property
    def pnmlcoremodel_Fill(self):
        return self.__pnmlcoremodel_Fill

    @pnmlcoremodel_Fill.setter
    def pnmlcoremodel_Fill(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_Fill__pnmlcoremodel_Fill", None)
        self.__pnmlcoremodel_Fill = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pnmlcoremodel_NodeGraphics62"):
                opp_val = getattr(old_value, "pnmlcoremodel_NodeGraphics62", None)
                if opp_val == self:
                    setattr(old_value, "pnmlcoremodel_NodeGraphics62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pnmlcoremodel_NodeGraphics62"):
                opp_val = getattr(value, "pnmlcoremodel_NodeGraphics62", None)
                setattr(value, "pnmlcoremodel_NodeGraphics62", self)

    @property
    def pnmlcoremodel_Fill64(self):
        return self.__pnmlcoremodel_Fill64

    @pnmlcoremodel_Fill64.setter
    def pnmlcoremodel_Fill64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_Fill__pnmlcoremodel_Fill64", None)
        self.__pnmlcoremodel_Fill64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pnmlcoremodel_AnnotationGraphics"):
                opp_val = getattr(old_value, "pnmlcoremodel_AnnotationGraphics", None)
                if opp_val == self:
                    setattr(old_value, "pnmlcoremodel_AnnotationGraphics", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pnmlcoremodel_AnnotationGraphics"):
                opp_val = getattr(value, "pnmlcoremodel_AnnotationGraphics", None)
                setattr(value, "pnmlcoremodel_AnnotationGraphics", self)

class pnmlcoremodel_Font:

    def __init__(self, style: str, weight: str, size: str, decoration: str, align: str, rotation: float, family: str, pnmlcoremodel_Font: "pnmlcoremodel_AnnotationGraphics" = None):
        self.style = style
        self.weight = weight
        self.size = size
        self.decoration = decoration
        self.align = align
        self.rotation = rotation
        self.family = family
        self.pnmlcoremodel_Font = pnmlcoremodel_Font
        
    @property
    def decoration(self) -> str:
        return self.__decoration

    @decoration.setter
    def decoration(self, decoration: str):
        self.__decoration = decoration

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
    def rotation(self) -> float:
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation: float):
        self.__rotation = rotation

    @property
    def family(self) -> str:
        return self.__family

    @family.setter
    def family(self, family: str):
        self.__family = family

    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

    @property
    def pnmlcoremodel_Font(self):
        return self.__pnmlcoremodel_Font

    @pnmlcoremodel_Font.setter
    def pnmlcoremodel_Font(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_Font__pnmlcoremodel_Font", None)
        self.__pnmlcoremodel_Font = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pnmlcoremodel_AnnotationGraphics72"):
                opp_val = getattr(old_value, "pnmlcoremodel_AnnotationGraphics72", None)
                if opp_val == self:
                    setattr(old_value, "pnmlcoremodel_AnnotationGraphics72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pnmlcoremodel_AnnotationGraphics72"):
                opp_val = getattr(value, "pnmlcoremodel_AnnotationGraphics72", None)
                setattr(value, "pnmlcoremodel_AnnotationGraphics72", self)

class Label:

    pass
class pnmlcoremodel_Attribute(Label):

    pass
class pnmlcoremodel_Coordinate:

    def __init__(self, x: float, y: float, pnmlcoremodel_Coordinate: "pnmlcoremodel_ArcGraphics" = None, pnmlcoremodel_Coordinate54: "pnmlcoremodel_NodeGraphics" = None, pnmlcoremodel_Coordinate70: "pnmlcoremodel_AnnotationGraphics" = None, pnmlcoremodel_Coordinate57: "pnmlcoremodel_NodeGraphics" = None):
        self.x = x
        self.y = y
        self.pnmlcoremodel_Coordinate = pnmlcoremodel_Coordinate
        self.pnmlcoremodel_Coordinate54 = pnmlcoremodel_Coordinate54
        self.pnmlcoremodel_Coordinate70 = pnmlcoremodel_Coordinate70
        self.pnmlcoremodel_Coordinate57 = pnmlcoremodel_Coordinate57
        
    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x

    @property
    def pnmlcoremodel_Coordinate54(self):
        return self.__pnmlcoremodel_Coordinate54

    @pnmlcoremodel_Coordinate54.setter
    def pnmlcoremodel_Coordinate54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_Coordinate__pnmlcoremodel_Coordinate54", None)
        self.__pnmlcoremodel_Coordinate54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pnmlcoremodel_NodeGraphics"):
                opp_val = getattr(old_value, "pnmlcoremodel_NodeGraphics", None)
                if opp_val == self:
                    setattr(old_value, "pnmlcoremodel_NodeGraphics", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pnmlcoremodel_NodeGraphics"):
                opp_val = getattr(value, "pnmlcoremodel_NodeGraphics", None)
                setattr(value, "pnmlcoremodel_NodeGraphics", self)

    @property
    def pnmlcoremodel_Coordinate(self):
        return self.__pnmlcoremodel_Coordinate

    @pnmlcoremodel_Coordinate.setter
    def pnmlcoremodel_Coordinate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_Coordinate__pnmlcoremodel_Coordinate", None)
        self.__pnmlcoremodel_Coordinate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pnmlcoremodel_ArcGraphics52"):
                opp_val = getattr(old_value, "pnmlcoremodel_ArcGraphics52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pnmlcoremodel_ArcGraphics52"):
                opp_val = getattr(value, "pnmlcoremodel_ArcGraphics52", None)
                if opp_val is None:
                    setattr(value, "pnmlcoremodel_ArcGraphics52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pnmlcoremodel_Coordinate70(self):
        return self.__pnmlcoremodel_Coordinate70

    @pnmlcoremodel_Coordinate70.setter
    def pnmlcoremodel_Coordinate70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_Coordinate__pnmlcoremodel_Coordinate70", None)
        self.__pnmlcoremodel_Coordinate70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pnmlcoremodel_AnnotationGraphics69"):
                opp_val = getattr(old_value, "pnmlcoremodel_AnnotationGraphics69", None)
                if opp_val == self:
                    setattr(old_value, "pnmlcoremodel_AnnotationGraphics69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pnmlcoremodel_AnnotationGraphics69"):
                opp_val = getattr(value, "pnmlcoremodel_AnnotationGraphics69", None)
                setattr(value, "pnmlcoremodel_AnnotationGraphics69", self)

    @property
    def pnmlcoremodel_Coordinate57(self):
        return self.__pnmlcoremodel_Coordinate57

    @pnmlcoremodel_Coordinate57.setter
    def pnmlcoremodel_Coordinate57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_Coordinate__pnmlcoremodel_Coordinate57", None)
        self.__pnmlcoremodel_Coordinate57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pnmlcoremodel_NodeGraphics56"):
                opp_val = getattr(old_value, "pnmlcoremodel_NodeGraphics56", None)
                if opp_val == self:
                    setattr(old_value, "pnmlcoremodel_NodeGraphics56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pnmlcoremodel_NodeGraphics56"):
                opp_val = getattr(value, "pnmlcoremodel_NodeGraphics56", None)
                setattr(value, "pnmlcoremodel_NodeGraphics56", self)

class pnmlcoremodel_Line:

    def __init__(self, shape: str, color: str, width: float, style: str, pnmlcoremodel_Line: "pnmlcoremodel_ArcGraphics" = None, pnmlcoremodel_Line67: "pnmlcoremodel_AnnotationGraphics" = None, pnmlcoremodel_Line60: "pnmlcoremodel_NodeGraphics" = None):
        self.shape = shape
        self.color = color
        self.width = width
        self.style = style
        self.pnmlcoremodel_Line = pnmlcoremodel_Line
        self.pnmlcoremodel_Line67 = pnmlcoremodel_Line67
        self.pnmlcoremodel_Line60 = pnmlcoremodel_Line60
        
    @property
    def shape(self) -> str:
        return self.__shape

    @shape.setter
    def shape(self, shape: str):
        self.__shape = shape

    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, width: float):
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
    def pnmlcoremodel_Line60(self):
        return self.__pnmlcoremodel_Line60

    @pnmlcoremodel_Line60.setter
    def pnmlcoremodel_Line60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_Line__pnmlcoremodel_Line60", None)
        self.__pnmlcoremodel_Line60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pnmlcoremodel_NodeGraphics59"):
                opp_val = getattr(old_value, "pnmlcoremodel_NodeGraphics59", None)
                if opp_val == self:
                    setattr(old_value, "pnmlcoremodel_NodeGraphics59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pnmlcoremodel_NodeGraphics59"):
                opp_val = getattr(value, "pnmlcoremodel_NodeGraphics59", None)
                setattr(value, "pnmlcoremodel_NodeGraphics59", self)

    @property
    def pnmlcoremodel_Line(self):
        return self.__pnmlcoremodel_Line

    @pnmlcoremodel_Line.setter
    def pnmlcoremodel_Line(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_Line__pnmlcoremodel_Line", None)
        self.__pnmlcoremodel_Line = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pnmlcoremodel_ArcGraphics"):
                opp_val = getattr(old_value, "pnmlcoremodel_ArcGraphics", None)
                if opp_val == self:
                    setattr(old_value, "pnmlcoremodel_ArcGraphics", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pnmlcoremodel_ArcGraphics"):
                opp_val = getattr(value, "pnmlcoremodel_ArcGraphics", None)
                setattr(value, "pnmlcoremodel_ArcGraphics", self)

    @property
    def pnmlcoremodel_Line67(self):
        return self.__pnmlcoremodel_Line67

    @pnmlcoremodel_Line67.setter
    def pnmlcoremodel_Line67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_Line__pnmlcoremodel_Line67", None)
        self.__pnmlcoremodel_Line67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pnmlcoremodel_AnnotationGraphics66"):
                opp_val = getattr(old_value, "pnmlcoremodel_AnnotationGraphics66", None)
                if opp_val == self:
                    setattr(old_value, "pnmlcoremodel_AnnotationGraphics66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pnmlcoremodel_AnnotationGraphics66"):
                opp_val = getattr(value, "pnmlcoremodel_AnnotationGraphics66", None)
                setattr(value, "pnmlcoremodel_AnnotationGraphics66", self)

class Graphics:

    pass
class pnmlcoremodel_AnnotationGraphics(Graphics):

    pass
class pnmlcoremodel_NodeGraphics(Graphics):

    pass
class pnmlcoremodel_ArcGraphics(Graphics):

    pass
class TransitionNode:

    pass
class pnmlcoremodel_Transition(TransitionNode):

    pass
class pnmlcoremodel_RefTransition(TransitionNode):

    pass
class PlaceNode:

    pass
class pnmlcoremodel_RefPlace(PlaceNode):

    pass
class pnmlcoremodel_Place(PlaceNode):

    pass
class pnmlcoremodel_Graphics(ABC):

    pass
class pnmlcoremodel_LabelProxy:

    def __init__(self, text: str, pnmlcoremodel_LabelProxy29: "pnmlcoremodel_Label" = None, pnmlcoremodel_LabelProxy31: "pnmlcoremodel_Object" = None, pnmlcoremodel_LabelProxy: "pnmlcoremodel_Page" = None):
        self.text = text
        self.pnmlcoremodel_LabelProxy29 = pnmlcoremodel_LabelProxy29
        self.pnmlcoremodel_LabelProxy31 = pnmlcoremodel_LabelProxy31
        self.pnmlcoremodel_LabelProxy = pnmlcoremodel_LabelProxy
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def pnmlcoremodel_LabelProxy31(self):
        return self.__pnmlcoremodel_LabelProxy31

    @pnmlcoremodel_LabelProxy31.setter
    def pnmlcoremodel_LabelProxy31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_LabelProxy__pnmlcoremodel_LabelProxy31", None)
        self.__pnmlcoremodel_LabelProxy31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pnmlcoremodel_Object32"):
                opp_val = getattr(old_value, "pnmlcoremodel_Object32", None)
                if opp_val == self:
                    setattr(old_value, "pnmlcoremodel_Object32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pnmlcoremodel_Object32"):
                opp_val = getattr(value, "pnmlcoremodel_Object32", None)
                setattr(value, "pnmlcoremodel_Object32", self)

    @property
    def pnmlcoremodel_LabelProxy(self):
        return self.__pnmlcoremodel_LabelProxy

    @pnmlcoremodel_LabelProxy.setter
    def pnmlcoremodel_LabelProxy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_LabelProxy__pnmlcoremodel_LabelProxy", None)
        self.__pnmlcoremodel_LabelProxy = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pnmlcoremodel_Page16"):
                opp_val = getattr(old_value, "pnmlcoremodel_Page16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pnmlcoremodel_Page16"):
                opp_val = getattr(value, "pnmlcoremodel_Page16", None)
                if opp_val is None:
                    setattr(value, "pnmlcoremodel_Page16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pnmlcoremodel_LabelProxy29(self):
        return self.__pnmlcoremodel_LabelProxy29

    @pnmlcoremodel_LabelProxy29.setter
    def pnmlcoremodel_LabelProxy29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_LabelProxy__pnmlcoremodel_LabelProxy29", None)
        self.__pnmlcoremodel_LabelProxy29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pnmlcoremodel_Label"):
                opp_val = getattr(old_value, "pnmlcoremodel_Label", None)
                if opp_val == self:
                    setattr(old_value, "pnmlcoremodel_Label", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pnmlcoremodel_Label"):
                opp_val = getattr(value, "pnmlcoremodel_Label", None)
                setattr(value, "pnmlcoremodel_Label", self)

class Object:

    pass
class pnmlcoremodel_Arc(Object):

    pass
class pnmlcoremodel_Node(Object):

    pass
class pnmlcoremodel_Label(ABC):

    pass
class pnmlcoremodel_Name(Label):

    def __init__(self, text: str, pnmlcoremodel_Name: "pnmlcoremodel_PetriNet" = None, pnmlcoremodel_Name19: "pnmlcoremodel_Object" = None):
        self.text = text
        self.pnmlcoremodel_Name = pnmlcoremodel_Name
        self.pnmlcoremodel_Name19 = pnmlcoremodel_Name19
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def pnmlcoremodel_Name19(self):
        return self.__pnmlcoremodel_Name19

    @pnmlcoremodel_Name19.setter
    def pnmlcoremodel_Name19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_Name__pnmlcoremodel_Name19", None)
        self.__pnmlcoremodel_Name19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pnmlcoremodel_Object18"):
                opp_val = getattr(old_value, "pnmlcoremodel_Object18", None)
                if opp_val == self:
                    setattr(old_value, "pnmlcoremodel_Object18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pnmlcoremodel_Object18"):
                opp_val = getattr(value, "pnmlcoremodel_Object18", None)
                setattr(value, "pnmlcoremodel_Object18", self)

    @property
    def pnmlcoremodel_Name(self):
        return self.__pnmlcoremodel_Name

    @pnmlcoremodel_Name.setter
    def pnmlcoremodel_Name(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_Name__pnmlcoremodel_Name", None)
        self.__pnmlcoremodel_Name = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pnmlcoremodel_PetriNet4"):
                opp_val = getattr(old_value, "pnmlcoremodel_PetriNet4", None)
                if opp_val == self:
                    setattr(old_value, "pnmlcoremodel_PetriNet4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pnmlcoremodel_PetriNet4"):
                opp_val = getattr(value, "pnmlcoremodel_PetriNet4", None)
                setattr(value, "pnmlcoremodel_PetriNet4", self)

class pnmlcoremodel_PetriNetType(ABC):

    pass
class ID:

    pass
class pnmlcoremodel_PetriNet(ID):

    pass
class pnmlcoremodel_PageLabelProxy:

    def __init__(self, text: str, pnmlcoremodel_PageLabelProxy: "pnmlcoremodel_Page" = None, pnmlcoremodel_PageLabelProxy74: "pnmlcoremodel_Label" = None):
        self.text = text
        self.pnmlcoremodel_PageLabelProxy = pnmlcoremodel_PageLabelProxy
        self.pnmlcoremodel_PageLabelProxy74 = pnmlcoremodel_PageLabelProxy74
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def pnmlcoremodel_PageLabelProxy74(self):
        return self.__pnmlcoremodel_PageLabelProxy74

    @pnmlcoremodel_PageLabelProxy74.setter
    def pnmlcoremodel_PageLabelProxy74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_PageLabelProxy__pnmlcoremodel_PageLabelProxy74", None)
        self.__pnmlcoremodel_PageLabelProxy74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pnmlcoremodel_Label75"):
                opp_val = getattr(old_value, "pnmlcoremodel_Label75", None)
                if opp_val == self:
                    setattr(old_value, "pnmlcoremodel_Label75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pnmlcoremodel_Label75"):
                opp_val = getattr(value, "pnmlcoremodel_Label75", None)
                setattr(value, "pnmlcoremodel_Label75", self)

    @property
    def pnmlcoremodel_PageLabelProxy(self):
        return self.__pnmlcoremodel_PageLabelProxy

    @pnmlcoremodel_PageLabelProxy.setter
    def pnmlcoremodel_PageLabelProxy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_PageLabelProxy__pnmlcoremodel_PageLabelProxy", None)
        self.__pnmlcoremodel_PageLabelProxy = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pnmlcoremodel_Page14"):
                opp_val = getattr(old_value, "pnmlcoremodel_Page14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pnmlcoremodel_Page14"):
                opp_val = getattr(value, "pnmlcoremodel_Page14", None)
                if opp_val is None:
                    setattr(value, "pnmlcoremodel_Page14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class pnmlcoremodel_Object(ID):

    pass
class Node:

    pass
class pnmlcoremodel_PlaceNode(Node):

    pass
class pnmlcoremodel_TransitionNode(Node):

    pass
class pnmlcoremodel_AnyType:

    pass
class pnmlcoremodel_ToolInfo(ABC):

    def __init__(self, tool: str, version: str, pnmlcoremodel_ToolInfo: "pnmlcoremodel_PetriNet" = None, pnmlcoremodel_ToolInfo22: "pnmlcoremodel_Object" = None, pnmlcoremodel_ToolInfo43: "pnmlcoremodel_Label" = None):
        self.tool = tool
        self.version = version
        self.pnmlcoremodel_ToolInfo = pnmlcoremodel_ToolInfo
        self.pnmlcoremodel_ToolInfo22 = pnmlcoremodel_ToolInfo22
        self.pnmlcoremodel_ToolInfo43 = pnmlcoremodel_ToolInfo43
        
    @property
    def tool(self) -> str:
        return self.__tool

    @tool.setter
    def tool(self, tool: str):
        self.__tool = tool

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def pnmlcoremodel_ToolInfo22(self):
        return self.__pnmlcoremodel_ToolInfo22

    @pnmlcoremodel_ToolInfo22.setter
    def pnmlcoremodel_ToolInfo22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_ToolInfo__pnmlcoremodel_ToolInfo22", None)
        self.__pnmlcoremodel_ToolInfo22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pnmlcoremodel_Object21"):
                opp_val = getattr(old_value, "pnmlcoremodel_Object21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pnmlcoremodel_Object21"):
                opp_val = getattr(value, "pnmlcoremodel_Object21", None)
                if opp_val is None:
                    setattr(value, "pnmlcoremodel_Object21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pnmlcoremodel_ToolInfo43(self):
        return self.__pnmlcoremodel_ToolInfo43

    @pnmlcoremodel_ToolInfo43.setter
    def pnmlcoremodel_ToolInfo43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_ToolInfo__pnmlcoremodel_ToolInfo43", None)
        self.__pnmlcoremodel_ToolInfo43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pnmlcoremodel_Label42"):
                opp_val = getattr(old_value, "pnmlcoremodel_Label42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pnmlcoremodel_Label42"):
                opp_val = getattr(value, "pnmlcoremodel_Label42", None)
                if opp_val is None:
                    setattr(value, "pnmlcoremodel_Label42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pnmlcoremodel_ToolInfo(self):
        return self.__pnmlcoremodel_ToolInfo

    @pnmlcoremodel_ToolInfo.setter
    def pnmlcoremodel_ToolInfo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pnmlcoremodel_ToolInfo__pnmlcoremodel_ToolInfo", None)
        self.__pnmlcoremodel_ToolInfo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pnmlcoremodel_PetriNet8"):
                opp_val = getattr(old_value, "pnmlcoremodel_PetriNet8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pnmlcoremodel_PetriNet8"):
                opp_val = getattr(value, "pnmlcoremodel_PetriNet8", None)
                if opp_val is None:
                    setattr(value, "pnmlcoremodel_PetriNet8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class pnmlcoremodel_Page(Node):

    pass
class pnmlcoremodel_PetriNetDoc:

    pass