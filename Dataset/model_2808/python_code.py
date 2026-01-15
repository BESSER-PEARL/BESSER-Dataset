from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class CSOrientation(Enum):
    VERTICAL = "VERTICAL"
    HORIZONTAL = "HORIZONTAL"
class CSFitType(Enum):
    AUTO_EXPAND = "AUTO_EXPAND"
    FIT_TO_CHILDREN = "FIT_TO_CHILDREN"


############################################
# Definition of Classes
############################################

class cs_EClass:

    pass
class cs_CSPoint:

    def __init__(self, x: float, y: float, cs_CSPoint: "cs_CSShape" = None):
        self.x = x
        self.y = y
        self.cs_CSPoint = cs_CSPoint
        
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
    def cs_CSPoint(self):
        return self.__cs_CSPoint

    @cs_CSPoint.setter
    def cs_CSPoint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cs_CSPoint__cs_CSPoint", None)
        self.__cs_CSPoint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cs_CSShape25"):
                opp_val = getattr(old_value, "cs_CSShape25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cs_CSShape25"):
                opp_val = getattr(value, "cs_CSShape25", None)
                if opp_val is None:
                    setattr(value, "cs_CSShape25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class CSNode:

    pass
class cs_CSTemplateDescription(CSNode):

    def __init__(self, scale: float, cs_CSTemplateDescription: "cs_EClass" = None, cs_CSTemplateDescription28: "cs_EClass" = None, cs_CSTemplateDescription31: "cs_EStructuralFeature" = None, cs_CSTemplateDescription34: "cs_CSElement" = None):
        self.scale = scale
        self.cs_CSTemplateDescription = cs_CSTemplateDescription
        self.cs_CSTemplateDescription28 = cs_CSTemplateDescription28
        self.cs_CSTemplateDescription31 = cs_CSTemplateDescription31
        self.cs_CSTemplateDescription34 = cs_CSTemplateDescription34
        
    @property
    def scale(self) -> float:
        return self.__scale

    @scale.setter
    def scale(self, scale: float):
        self.__scale = scale

    @property
    def cs_CSTemplateDescription34(self):
        return self.__cs_CSTemplateDescription34

    @cs_CSTemplateDescription34.setter
    def cs_CSTemplateDescription34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cs_CSTemplateDescription__cs_CSTemplateDescription34", None)
        self.__cs_CSTemplateDescription34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cs_CSElement35"):
                opp_val = getattr(old_value, "cs_CSElement35", None)
                if opp_val == self:
                    setattr(old_value, "cs_CSElement35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cs_CSElement35"):
                opp_val = getattr(value, "cs_CSElement35", None)
                setattr(value, "cs_CSElement35", self)

    @property
    def cs_CSTemplateDescription31(self):
        return self.__cs_CSTemplateDescription31

    @cs_CSTemplateDescription31.setter
    def cs_CSTemplateDescription31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cs_CSTemplateDescription__cs_CSTemplateDescription31", None)
        self.__cs_CSTemplateDescription31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cs_EStructuralFeature32"):
                opp_val = getattr(old_value, "cs_EStructuralFeature32", None)
                if opp_val == self:
                    setattr(old_value, "cs_EStructuralFeature32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cs_EStructuralFeature32"):
                opp_val = getattr(value, "cs_EStructuralFeature32", None)
                setattr(value, "cs_EStructuralFeature32", self)

    @property
    def cs_CSTemplateDescription28(self):
        return self.__cs_CSTemplateDescription28

    @cs_CSTemplateDescription28.setter
    def cs_CSTemplateDescription28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cs_CSTemplateDescription__cs_CSTemplateDescription28", None)
        self.__cs_CSTemplateDescription28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cs_EClass29"):
                opp_val = getattr(old_value, "cs_EClass29", None)
                if opp_val == self:
                    setattr(old_value, "cs_EClass29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cs_EClass29"):
                opp_val = getattr(value, "cs_EClass29", None)
                setattr(value, "cs_EClass29", self)

    @property
    def cs_CSTemplateDescription(self):
        return self.__cs_CSTemplateDescription

    @cs_CSTemplateDescription.setter
    def cs_CSTemplateDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cs_CSTemplateDescription__cs_CSTemplateDescription", None)
        self.__cs_CSTemplateDescription = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cs_EClass"):
                opp_val = getattr(old_value, "cs_EClass", None)
                if opp_val == self:
                    setattr(old_value, "cs_EClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cs_EClass"):
                opp_val = getattr(value, "cs_EClass", None)
                setattr(value, "cs_EClass", self)

class cs_CSText(CSNode):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class cs_CSConnectionEnd:

    def __init__(self, tipType: int, cs_CSConnectionEnd: "cs_CSConnection" = None, cs_CSConnectionEnd37: "cs_CSNode" = None, cs_CSConnectionEnd40: "cs_EStructuralFeature" = None, cs_CSConnectionEnd43: "cs_EStructuralFeature" = None):
        self.tipType = tipType
        self.cs_CSConnectionEnd = cs_CSConnectionEnd
        self.cs_CSConnectionEnd37 = cs_CSConnectionEnd37
        self.cs_CSConnectionEnd40 = cs_CSConnectionEnd40
        self.cs_CSConnectionEnd43 = cs_CSConnectionEnd43
        
    @property
    def tipType(self) -> int:
        return self.__tipType

    @tipType.setter
    def tipType(self, tipType: int):
        self.__tipType = tipType

    @property
    def cs_CSConnectionEnd37(self):
        return self.__cs_CSConnectionEnd37

    @cs_CSConnectionEnd37.setter
    def cs_CSConnectionEnd37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cs_CSConnectionEnd__cs_CSConnectionEnd37", None)
        self.__cs_CSConnectionEnd37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cs_CSNode38"):
                opp_val = getattr(old_value, "cs_CSNode38", None)
                if opp_val == self:
                    setattr(old_value, "cs_CSNode38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cs_CSNode38"):
                opp_val = getattr(value, "cs_CSNode38", None)
                setattr(value, "cs_CSNode38", self)

    @property
    def cs_CSConnectionEnd(self):
        return self.__cs_CSConnectionEnd

    @cs_CSConnectionEnd.setter
    def cs_CSConnectionEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cs_CSConnectionEnd__cs_CSConnectionEnd", None)
        self.__cs_CSConnectionEnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cs_CSConnection23"):
                opp_val = getattr(old_value, "cs_CSConnection23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cs_CSConnection23"):
                opp_val = getattr(value, "cs_CSConnection23", None)
                if opp_val is None:
                    setattr(value, "cs_CSConnection23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cs_CSConnectionEnd43(self):
        return self.__cs_CSConnectionEnd43

    @cs_CSConnectionEnd43.setter
    def cs_CSConnectionEnd43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cs_CSConnectionEnd__cs_CSConnectionEnd43", None)
        self.__cs_CSConnectionEnd43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cs_EStructuralFeature44"):
                opp_val = getattr(old_value, "cs_EStructuralFeature44", None)
                if opp_val == self:
                    setattr(old_value, "cs_EStructuralFeature44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cs_EStructuralFeature44"):
                opp_val = getattr(value, "cs_EStructuralFeature44", None)
                setattr(value, "cs_EStructuralFeature44", self)

    @property
    def cs_CSConnectionEnd40(self):
        return self.__cs_CSConnectionEnd40

    @cs_CSConnectionEnd40.setter
    def cs_CSConnectionEnd40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cs_CSConnectionEnd__cs_CSConnectionEnd40", None)
        self.__cs_CSConnectionEnd40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cs_EStructuralFeature41"):
                opp_val = getattr(old_value, "cs_EStructuralFeature41", None)
                if opp_val == self:
                    setattr(old_value, "cs_EStructuralFeature41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cs_EStructuralFeature41"):
                opp_val = getattr(value, "cs_EStructuralFeature41", None)
                setattr(value, "cs_EStructuralFeature41", self)

class cs_CSLayout:

    pass
class cs_EStructuralFeature:

    pass
class cs_EObject:

    pass
class cs_CSTransform:

    def __init__(self, m11: float, m12: float, m20: float, m21: float, m22: float, m00: float, m01: float, m02: float, m10: float, cs_CSTransform: "cs_CSElement" = None):
        self.m11 = m11
        self.m12 = m12
        self.m20 = m20
        self.m21 = m21
        self.m22 = m22
        self.m00 = m00
        self.m01 = m01
        self.m02 = m02
        self.m10 = m10
        self.cs_CSTransform = cs_CSTransform
        
    @property
    def m21(self) -> float:
        return self.__m21

    @m21.setter
    def m21(self, m21: float):
        self.__m21 = m21

    @property
    def m20(self) -> float:
        return self.__m20

    @m20.setter
    def m20(self, m20: float):
        self.__m20 = m20

    @property
    def m11(self) -> float:
        return self.__m11

    @m11.setter
    def m11(self, m11: float):
        self.__m11 = m11

    @property
    def m12(self) -> float:
        return self.__m12

    @m12.setter
    def m12(self, m12: float):
        self.__m12 = m12

    @property
    def m02(self) -> float:
        return self.__m02

    @m02.setter
    def m02(self, m02: float):
        self.__m02 = m02

    @property
    def m00(self) -> float:
        return self.__m00

    @m00.setter
    def m00(self, m00: float):
        self.__m00 = m00

    @property
    def m10(self) -> float:
        return self.__m10

    @m10.setter
    def m10(self, m10: float):
        self.__m10 = m10

    @property
    def m01(self) -> float:
        return self.__m01

    @m01.setter
    def m01(self, m01: float):
        self.__m01 = m01

    @property
    def m22(self) -> float:
        return self.__m22

    @m22.setter
    def m22(self, m22: float):
        self.__m22 = m22

    @property
    def cs_CSTransform(self):
        return self.__cs_CSTransform

    @cs_CSTransform.setter
    def cs_CSTransform(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cs_CSTransform__cs_CSTransform", None)
        self.__cs_CSTransform = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cs_CSElement14"):
                opp_val = getattr(old_value, "cs_CSElement14", None)
                if opp_val == self:
                    setattr(old_value, "cs_CSElement14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cs_CSElement14"):
                opp_val = getattr(value, "cs_CSElement14", None)
                setattr(value, "cs_CSElement14", self)

class cs_CSColor:

    def __init__(self, r: float, g: float, b: float, a: float, cs_CSColor: "cs_CSElement" = None, cs_CSColor10: "cs_CSElement" = None):
        self.r = r
        self.g = g
        self.b = b
        self.a = a
        self.cs_CSColor = cs_CSColor
        self.cs_CSColor10 = cs_CSColor10
        
    @property
    def r(self) -> float:
        return self.__r

    @r.setter
    def r(self, r: float):
        self.__r = r

    @property
    def g(self) -> float:
        return self.__g

    @g.setter
    def g(self, g: float):
        self.__g = g

    @property
    def a(self) -> float:
        return self.__a

    @a.setter
    def a(self, a: float):
        self.__a = a

    @property
    def b(self) -> float:
        return self.__b

    @b.setter
    def b(self, b: float):
        self.__b = b

    @property
    def cs_CSColor(self):
        return self.__cs_CSColor

    @cs_CSColor.setter
    def cs_CSColor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cs_CSColor__cs_CSColor", None)
        self.__cs_CSColor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cs_CSElement7"):
                opp_val = getattr(old_value, "cs_CSElement7", None)
                if opp_val == self:
                    setattr(old_value, "cs_CSElement7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cs_CSElement7"):
                opp_val = getattr(value, "cs_CSElement7", None)
                setattr(value, "cs_CSElement7", self)

    @property
    def cs_CSColor10(self):
        return self.__cs_CSColor10

    @cs_CSColor10.setter
    def cs_CSColor10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cs_CSColor__cs_CSColor10", None)
        self.__cs_CSColor10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cs_CSElement9"):
                opp_val = getattr(old_value, "cs_CSElement9", None)
                if opp_val == self:
                    setattr(old_value, "cs_CSElement9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cs_CSElement9"):
                opp_val = getattr(value, "cs_CSElement9", None)
                setattr(value, "cs_CSElement9", self)

class cs_CSStroke:

    def __init__(self, width: float, join: int, cap: int, miterlimit: float, dash: float, dash_phase: float, cs_CSStroke: "cs_CSElement" = None):
        self.width = width
        self.join = join
        self.cap = cap
        self.miterlimit = miterlimit
        self.dash = dash
        self.dash_phase = dash_phase
        self.cs_CSStroke = cs_CSStroke
        
    @property
    def dash_phase(self) -> float:
        return self.__dash_phase

    @dash_phase.setter
    def dash_phase(self, dash_phase: float):
        self.__dash_phase = dash_phase

    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, width: float):
        self.__width = width

    @property
    def cap(self) -> int:
        return self.__cap

    @cap.setter
    def cap(self, cap: int):
        self.__cap = cap

    @property
    def join(self) -> int:
        return self.__join

    @join.setter
    def join(self, join: int):
        self.__join = join

    @property
    def dash(self) -> float:
        return self.__dash

    @dash.setter
    def dash(self, dash: float):
        self.__dash = dash

    @property
    def miterlimit(self) -> float:
        return self.__miterlimit

    @miterlimit.setter
    def miterlimit(self, miterlimit: float):
        self.__miterlimit = miterlimit

    @property
    def cs_CSStroke(self):
        return self.__cs_CSStroke

    @cs_CSStroke.setter
    def cs_CSStroke(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cs_CSStroke__cs_CSStroke", None)
        self.__cs_CSStroke = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cs_CSElement"):
                opp_val = getattr(old_value, "cs_CSElement", None)
                if opp_val == self:
                    setattr(old_value, "cs_CSElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cs_CSElement"):
                opp_val = getattr(value, "cs_CSElement", None)
                setattr(value, "cs_CSElement", self)

class ENamedElement:

    pass
class cs_CSShape(ENamedElement):

    def __init__(self, closed: bool, cs_CSShape: "cs_CSElement" = None, cs_CSShape25: set["cs_CSPoint"] = None):
        self.closed = closed
        self.cs_CSShape = cs_CSShape
        self.cs_CSShape25 = cs_CSShape25 if cs_CSShape25 is not None else set()
        
    @property
    def closed(self) -> bool:
        return self.__closed

    @closed.setter
    def closed(self, closed: bool):
        self.__closed = closed

    @property
    def cs_CSShape25(self):
        return self.__cs_CSShape25

    @cs_CSShape25.setter
    def cs_CSShape25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cs_CSShape__cs_CSShape25", None)
        self.__cs_CSShape25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cs_CSPoint"):
                    opp_val = getattr(item, "cs_CSPoint", None)
                    
                    if opp_val == self:
                        setattr(item, "cs_CSPoint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cs_CSPoint"):
                    opp_val = getattr(item, "cs_CSPoint", None)
                    
                    setattr(item, "cs_CSPoint", self)
                    

    @property
    def cs_CSShape(self):
        return self.__cs_CSShape

    @cs_CSShape.setter
    def cs_CSShape(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cs_CSShape__cs_CSShape", None)
        self.__cs_CSShape = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cs_CSElement12"):
                opp_val = getattr(old_value, "cs_CSElement12", None)
                if opp_val == self:
                    setattr(old_value, "cs_CSElement12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cs_CSElement12"):
                opp_val = getattr(value, "cs_CSElement12", None)
                setattr(value, "cs_CSElement12", self)

class cs_CSElement(ENamedElement):

    def __init__(self, selectable: str, draggable: bool, resizable: bool, templateRoot: bool, minZoom: str, maxZoom: str, cs_CSElement: "cs_CSStroke" = None, cs_CSElement7: "cs_CSColor" = None, CSElement: "cs_CSElement" = None, parent: set["cs_CSElement"] = None, CSElement5: "cs_CSElement" = None, children: "cs_CSElement" = None, cs_CSElement9: "cs_CSColor" = None, cs_CSElement12: "cs_CSShape" = None, cs_CSElement14: "cs_CSTransform" = None, cs_CSElement16: "cs_EObject" = None, cs_CSElement18: set["cs_EStructuralFeature"] = None, cs_CSElement20: "cs_CSLayout" = None, cs_CSElement35: "cs_CSTemplateDescription" = None):
        self.selectable = selectable
        self.draggable = draggable
        self.resizable = resizable
        self.templateRoot = templateRoot
        self.minZoom = minZoom
        self.maxZoom = maxZoom
        self.cs_CSElement = cs_CSElement
        self.cs_CSElement7 = cs_CSElement7
        self.CSElement = CSElement
        self.parent = parent if parent is not None else set()
        self.CSElement5 = CSElement5
        self.children = children
        self.cs_CSElement9 = cs_CSElement9
        self.cs_CSElement12 = cs_CSElement12
        self.cs_CSElement14 = cs_CSElement14
        self.cs_CSElement16 = cs_CSElement16
        self.cs_CSElement18 = cs_CSElement18 if cs_CSElement18 is not None else set()
        self.cs_CSElement20 = cs_CSElement20
        self.cs_CSElement35 = cs_CSElement35
        
    @property
    def templateRoot(self) -> bool:
        return self.__templateRoot

    @templateRoot.setter
    def templateRoot(self, templateRoot: bool):
        self.__templateRoot = templateRoot

    @property
    def selectable(self) -> str:
        return self.__selectable

    @selectable.setter
    def selectable(self, selectable: str):
        self.__selectable = selectable

    @property
    def maxZoom(self) -> str:
        return self.__maxZoom

    @maxZoom.setter
    def maxZoom(self, maxZoom: str):
        self.__maxZoom = maxZoom

    @property
    def draggable(self) -> bool:
        return self.__draggable

    @draggable.setter
    def draggable(self, draggable: bool):
        self.__draggable = draggable

    @property
    def minZoom(self) -> str:
        return self.__minZoom

    @minZoom.setter
    def minZoom(self, minZoom: str):
        self.__minZoom = minZoom

    @property
    def resizable(self) -> bool:
        return self.__resizable

    @resizable.setter
    def resizable(self, resizable: bool):
        self.__resizable = resizable

    @property
    def CSElement5(self):
        return self.__CSElement5

    @CSElement5.setter
    def CSElement5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cs_CSElement__CSElement5", None)
        self.__CSElement5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "children"):
                opp_val = getattr(old_value, "children", None)
                if opp_val == self:
                    setattr(old_value, "children", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "children"):
                opp_val = getattr(value, "children", None)
                setattr(value, "children", self)

    @property
    def cs_CSElement12(self):
        return self.__cs_CSElement12

    @cs_CSElement12.setter
    def cs_CSElement12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cs_CSElement__cs_CSElement12", None)
        self.__cs_CSElement12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cs_CSShape"):
                opp_val = getattr(old_value, "cs_CSShape", None)
                if opp_val == self:
                    setattr(old_value, "cs_CSShape", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cs_CSShape"):
                opp_val = getattr(value, "cs_CSShape", None)
                setattr(value, "cs_CSShape", self)

    @property
    def cs_CSElement35(self):
        return self.__cs_CSElement35

    @cs_CSElement35.setter
    def cs_CSElement35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cs_CSElement__cs_CSElement35", None)
        self.__cs_CSElement35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cs_CSTemplateDescription34"):
                opp_val = getattr(old_value, "cs_CSTemplateDescription34", None)
                if opp_val == self:
                    setattr(old_value, "cs_CSTemplateDescription34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cs_CSTemplateDescription34"):
                opp_val = getattr(value, "cs_CSTemplateDescription34", None)
                setattr(value, "cs_CSTemplateDescription34", self)

    @property
    def cs_CSElement14(self):
        return self.__cs_CSElement14

    @cs_CSElement14.setter
    def cs_CSElement14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cs_CSElement__cs_CSElement14", None)
        self.__cs_CSElement14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cs_CSTransform"):
                opp_val = getattr(old_value, "cs_CSTransform", None)
                if opp_val == self:
                    setattr(old_value, "cs_CSTransform", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cs_CSTransform"):
                opp_val = getattr(value, "cs_CSTransform", None)
                setattr(value, "cs_CSTransform", self)

    @property
    def cs_CSElement16(self):
        return self.__cs_CSElement16

    @cs_CSElement16.setter
    def cs_CSElement16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cs_CSElement__cs_CSElement16", None)
        self.__cs_CSElement16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cs_EObject"):
                opp_val = getattr(old_value, "cs_EObject", None)
                if opp_val == self:
                    setattr(old_value, "cs_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cs_EObject"):
                opp_val = getattr(value, "cs_EObject", None)
                setattr(value, "cs_EObject", self)

    @property
    def CSElement(self):
        return self.__CSElement

    @CSElement.setter
    def CSElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cs_CSElement__CSElement", None)
        self.__CSElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent"):
                opp_val = getattr(old_value, "parent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent"):
                opp_val = getattr(value, "parent", None)
                if opp_val is None:
                    setattr(value, "parent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cs_CSElement(self):
        return self.__cs_CSElement

    @cs_CSElement.setter
    def cs_CSElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cs_CSElement__cs_CSElement", None)
        self.__cs_CSElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cs_CSStroke"):
                opp_val = getattr(old_value, "cs_CSStroke", None)
                if opp_val == self:
                    setattr(old_value, "cs_CSStroke", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cs_CSStroke"):
                opp_val = getattr(value, "cs_CSStroke", None)
                setattr(value, "cs_CSStroke", self)

    @property
    def cs_CSElement20(self):
        return self.__cs_CSElement20

    @cs_CSElement20.setter
    def cs_CSElement20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cs_CSElement__cs_CSElement20", None)
        self.__cs_CSElement20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cs_CSLayout"):
                opp_val = getattr(old_value, "cs_CSLayout", None)
                if opp_val == self:
                    setattr(old_value, "cs_CSLayout", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cs_CSLayout"):
                opp_val = getattr(value, "cs_CSLayout", None)
                setattr(value, "cs_CSLayout", self)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cs_CSElement__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CSElement"):
                    opp_val = getattr(item, "CSElement", None)
                    
                    if opp_val == self:
                        setattr(item, "CSElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CSElement"):
                    opp_val = getattr(item, "CSElement", None)
                    
                    setattr(item, "CSElement", self)
                    

    @property
    def cs_CSElement9(self):
        return self.__cs_CSElement9

    @cs_CSElement9.setter
    def cs_CSElement9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cs_CSElement__cs_CSElement9", None)
        self.__cs_CSElement9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cs_CSColor10"):
                opp_val = getattr(old_value, "cs_CSColor10", None)
                if opp_val == self:
                    setattr(old_value, "cs_CSColor10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cs_CSColor10"):
                opp_val = getattr(value, "cs_CSColor10", None)
                setattr(value, "cs_CSColor10", self)

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cs_CSElement__children", None)
        self.__children = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CSElement5"):
                opp_val = getattr(old_value, "CSElement5", None)
                if opp_val == self:
                    setattr(old_value, "CSElement5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CSElement5"):
                opp_val = getattr(value, "CSElement5", None)
                setattr(value, "CSElement5", self)

    @property
    def cs_CSElement18(self):
        return self.__cs_CSElement18

    @cs_CSElement18.setter
    def cs_CSElement18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cs_CSElement__cs_CSElement18", None)
        self.__cs_CSElement18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cs_EStructuralFeature"):
                    opp_val = getattr(item, "cs_EStructuralFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "cs_EStructuralFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cs_EStructuralFeature"):
                    opp_val = getattr(item, "cs_EStructuralFeature", None)
                    
                    setattr(item, "cs_EStructuralFeature", self)
                    

    @property
    def cs_CSElement7(self):
        return self.__cs_CSElement7

    @cs_CSElement7.setter
    def cs_CSElement7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cs_CSElement__cs_CSElement7", None)
        self.__cs_CSElement7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cs_CSColor"):
                opp_val = getattr(old_value, "cs_CSColor", None)
                if opp_val == self:
                    setattr(old_value, "cs_CSColor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cs_CSColor"):
                opp_val = getattr(value, "cs_CSColor", None)
                setattr(value, "cs_CSColor", self)

class CSElement:

    pass
class cs_CSConnection(CSElement):

    pass
class cs_CSNode(CSElement):

    def __init__(self, height: str, width: str, x: str, y: str, horizontalAlign: str, verticalAlign: str, widthRatioToParent: str, heightRatioToParent: str, minHeight: str, maxHeight: str, minWidth: str, maxWidth: str, cs_CSNode: set["cs_CSConnection"] = None, cs_CSNode38: "cs_CSConnectionEnd" = None):
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.horizontalAlign = horizontalAlign
        self.verticalAlign = verticalAlign
        self.widthRatioToParent = widthRatioToParent
        self.heightRatioToParent = heightRatioToParent
        self.minHeight = minHeight
        self.maxHeight = maxHeight
        self.minWidth = minWidth
        self.maxWidth = maxWidth
        self.cs_CSNode = cs_CSNode if cs_CSNode is not None else set()
        self.cs_CSNode38 = cs_CSNode38
        
    @property
    def height(self) -> str:
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height

    @property
    def verticalAlign(self) -> str:
        return self.__verticalAlign

    @verticalAlign.setter
    def verticalAlign(self, verticalAlign: str):
        self.__verticalAlign = verticalAlign

    @property
    def horizontalAlign(self) -> str:
        return self.__horizontalAlign

    @horizontalAlign.setter
    def horizontalAlign(self, horizontalAlign: str):
        self.__horizontalAlign = horizontalAlign

    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def minWidth(self) -> str:
        return self.__minWidth

    @minWidth.setter
    def minWidth(self, minWidth: str):
        self.__minWidth = minWidth

    @property
    def maxWidth(self) -> str:
        return self.__maxWidth

    @maxWidth.setter
    def maxWidth(self, maxWidth: str):
        self.__maxWidth = maxWidth

    @property
    def maxHeight(self) -> str:
        return self.__maxHeight

    @maxHeight.setter
    def maxHeight(self, maxHeight: str):
        self.__maxHeight = maxHeight

    @property
    def x(self) -> str:
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x

    @property
    def minHeight(self) -> str:
        return self.__minHeight

    @minHeight.setter
    def minHeight(self, minHeight: str):
        self.__minHeight = minHeight

    @property
    def heightRatioToParent(self) -> str:
        return self.__heightRatioToParent

    @heightRatioToParent.setter
    def heightRatioToParent(self, heightRatioToParent: str):
        self.__heightRatioToParent = heightRatioToParent

    @property
    def y(self) -> str:
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y

    @property
    def widthRatioToParent(self) -> str:
        return self.__widthRatioToParent

    @widthRatioToParent.setter
    def widthRatioToParent(self, widthRatioToParent: str):
        self.__widthRatioToParent = widthRatioToParent

    @property
    def cs_CSNode(self):
        return self.__cs_CSNode

    @cs_CSNode.setter
    def cs_CSNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cs_CSNode__cs_CSNode", None)
        self.__cs_CSNode = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cs_CSConnection"):
                    opp_val = getattr(item, "cs_CSConnection", None)
                    
                    if opp_val == self:
                        setattr(item, "cs_CSConnection", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cs_CSConnection"):
                    opp_val = getattr(item, "cs_CSConnection", None)
                    
                    setattr(item, "cs_CSConnection", self)
                    

    @property
    def cs_CSNode38(self):
        return self.__cs_CSNode38

    @cs_CSNode38.setter
    def cs_CSNode38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cs_CSNode__cs_CSNode38", None)
        self.__cs_CSNode38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cs_CSConnectionEnd37"):
                opp_val = getattr(old_value, "cs_CSConnectionEnd37", None)
                if opp_val == self:
                    setattr(old_value, "cs_CSConnectionEnd37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cs_CSConnectionEnd37"):
                opp_val = getattr(value, "cs_CSConnectionEnd37", None)
                setattr(value, "cs_CSConnectionEnd37", self)

class cs_CSRoot(CSElement):

    pass