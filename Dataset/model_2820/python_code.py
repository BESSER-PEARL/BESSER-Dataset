from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Alignment(Enum):
    CENTER = "CENTER"
    LEFT = "LEFT"
    TOP = "TOP"
    RIGHT = "RIGHT"
    BOTTOM = "BOTTOM"
    MIDDLE = "MIDDLE"
    UNSPECIFIED = "UNSPECIFIED"


############################################
# Definition of Classes
############################################

class sofiagraphics_Gesture:

    pass
class sofiagraphics_Color:

    def __init__(self, r: float, g: float, b: float, a: float, sofiagraphics_Color34: "sofiagraphics_Style" = None, sofiagraphics_Color37: "sofiagraphics_Style" = None, sofiagraphics_Color: "sofiagraphics_Scene" = None):
        self.r = r
        self.g = g
        self.b = b
        self.a = a
        self.sofiagraphics_Color34 = sofiagraphics_Color34
        self.sofiagraphics_Color37 = sofiagraphics_Color37
        self.sofiagraphics_Color = sofiagraphics_Color
        
    @property
    def b(self) -> float:
        return self.__b

    @b.setter
    def b(self, b: float):
        self.__b = b

    @property
    def r(self) -> float:
        return self.__r

    @r.setter
    def r(self, r: float):
        self.__r = r

    @property
    def a(self) -> float:
        return self.__a

    @a.setter
    def a(self, a: float):
        self.__a = a

    @property
    def g(self) -> float:
        return self.__g

    @g.setter
    def g(self, g: float):
        self.__g = g

    @property
    def sofiagraphics_Color34(self):
        return self.__sofiagraphics_Color34

    @sofiagraphics_Color34.setter
    def sofiagraphics_Color34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sofiagraphics_Color__sofiagraphics_Color34", None)
        self.__sofiagraphics_Color34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sofiagraphics_Style33"):
                opp_val = getattr(old_value, "sofiagraphics_Style33", None)
                if opp_val == self:
                    setattr(old_value, "sofiagraphics_Style33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sofiagraphics_Style33"):
                opp_val = getattr(value, "sofiagraphics_Style33", None)
                setattr(value, "sofiagraphics_Style33", self)

    @property
    def sofiagraphics_Color37(self):
        return self.__sofiagraphics_Color37

    @sofiagraphics_Color37.setter
    def sofiagraphics_Color37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sofiagraphics_Color__sofiagraphics_Color37", None)
        self.__sofiagraphics_Color37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sofiagraphics_Style36"):
                opp_val = getattr(old_value, "sofiagraphics_Style36", None)
                if opp_val == self:
                    setattr(old_value, "sofiagraphics_Style36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sofiagraphics_Style36"):
                opp_val = getattr(value, "sofiagraphics_Style36", None)
                setattr(value, "sofiagraphics_Style36", self)

    @property
    def sofiagraphics_Color(self):
        return self.__sofiagraphics_Color

    @sofiagraphics_Color.setter
    def sofiagraphics_Color(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sofiagraphics_Color__sofiagraphics_Color", None)
        self.__sofiagraphics_Color = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sofiagraphics_Scene26"):
                opp_val = getattr(old_value, "sofiagraphics_Scene26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sofiagraphics_Scene26"):
                opp_val = getattr(value, "sofiagraphics_Scene26", None)
                if opp_val is None:
                    setattr(value, "sofiagraphics_Scene26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sofiagraphics_Scene:

    pass
class sofiagraphics_Widget(ABC):

    def __init__(self, gestureOnly: bool, portYPosition: float, sofiagraphics_Widget: "sofiagraphics_Style" = None, Widget5: "sofiagraphics_Widget" = None, parent: set["sofiagraphics_Widget"] = None, sofiagraphics_Widget7: "sofiagraphics_Point" = None, sofiagraphics_Widget9: "sofiagraphics_Dimension" = None, Widget: "sofiagraphics_Widget" = None, child: "sofiagraphics_Widget" = None, sofiagraphics_Widget40: "sofiagraphics_Gesture" = None, sofiagraphics_Widget15: "sofiagraphics_Scene" = None, sofiagraphics_Widget18: "sofiagraphics_Scene" = None):
        self.gestureOnly = gestureOnly
        self.portYPosition = portYPosition
        self.sofiagraphics_Widget = sofiagraphics_Widget
        self.Widget5 = Widget5
        self.parent = parent if parent is not None else set()
        self.sofiagraphics_Widget7 = sofiagraphics_Widget7
        self.sofiagraphics_Widget9 = sofiagraphics_Widget9
        self.Widget = Widget
        self.child = child
        self.sofiagraphics_Widget40 = sofiagraphics_Widget40
        self.sofiagraphics_Widget15 = sofiagraphics_Widget15
        self.sofiagraphics_Widget18 = sofiagraphics_Widget18
        
    @property
    def portYPosition(self) -> float:
        return self.__portYPosition

    @portYPosition.setter
    def portYPosition(self, portYPosition: float):
        self.__portYPosition = portYPosition

    @property
    def gestureOnly(self) -> bool:
        return self.__gestureOnly

    @gestureOnly.setter
    def gestureOnly(self, gestureOnly: bool):
        self.__gestureOnly = gestureOnly

    @property
    def sofiagraphics_Widget15(self):
        return self.__sofiagraphics_Widget15

    @sofiagraphics_Widget15.setter
    def sofiagraphics_Widget15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sofiagraphics_Widget__sofiagraphics_Widget15", None)
        self.__sofiagraphics_Widget15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sofiagraphics_Scene"):
                opp_val = getattr(old_value, "sofiagraphics_Scene", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sofiagraphics_Scene"):
                opp_val = getattr(value, "sofiagraphics_Scene", None)
                if opp_val is None:
                    setattr(value, "sofiagraphics_Scene", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sofiagraphics_Widget7(self):
        return self.__sofiagraphics_Widget7

    @sofiagraphics_Widget7.setter
    def sofiagraphics_Widget7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sofiagraphics_Widget__sofiagraphics_Widget7", None)
        self.__sofiagraphics_Widget7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sofiagraphics_Point"):
                opp_val = getattr(old_value, "sofiagraphics_Point", None)
                if opp_val == self:
                    setattr(old_value, "sofiagraphics_Point", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sofiagraphics_Point"):
                opp_val = getattr(value, "sofiagraphics_Point", None)
                setattr(value, "sofiagraphics_Point", self)

    @property
    def Widget5(self):
        return self.__Widget5

    @Widget5.setter
    def Widget5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sofiagraphics_Widget__Widget5", None)
        self.__Widget5 = value
        
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
    def sofiagraphics_Widget18(self):
        return self.__sofiagraphics_Widget18

    @sofiagraphics_Widget18.setter
    def sofiagraphics_Widget18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sofiagraphics_Widget__sofiagraphics_Widget18", None)
        self.__sofiagraphics_Widget18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sofiagraphics_Scene17"):
                opp_val = getattr(old_value, "sofiagraphics_Scene17", None)
                if opp_val == self:
                    setattr(old_value, "sofiagraphics_Scene17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sofiagraphics_Scene17"):
                opp_val = getattr(value, "sofiagraphics_Scene17", None)
                setattr(value, "sofiagraphics_Scene17", self)

    @property
    def sofiagraphics_Widget40(self):
        return self.__sofiagraphics_Widget40

    @sofiagraphics_Widget40.setter
    def sofiagraphics_Widget40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sofiagraphics_Widget__sofiagraphics_Widget40", None)
        self.__sofiagraphics_Widget40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sofiagraphics_Gesture39"):
                opp_val = getattr(old_value, "sofiagraphics_Gesture39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sofiagraphics_Gesture39"):
                opp_val = getattr(value, "sofiagraphics_Gesture39", None)
                if opp_val is None:
                    setattr(value, "sofiagraphics_Gesture39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def child(self):
        return self.__child

    @child.setter
    def child(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sofiagraphics_Widget__child", None)
        self.__child = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Widget"):
                opp_val = getattr(old_value, "Widget", None)
                if opp_val == self:
                    setattr(old_value, "Widget", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Widget"):
                opp_val = getattr(value, "Widget", None)
                setattr(value, "Widget", self)

    @property
    def Widget(self):
        return self.__Widget

    @Widget.setter
    def Widget(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sofiagraphics_Widget__Widget", None)
        self.__Widget = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "child"):
                opp_val = getattr(old_value, "child", None)
                if opp_val == self:
                    setattr(old_value, "child", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "child"):
                opp_val = getattr(value, "child", None)
                setattr(value, "child", self)

    @property
    def sofiagraphics_Widget(self):
        return self.__sofiagraphics_Widget

    @sofiagraphics_Widget.setter
    def sofiagraphics_Widget(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sofiagraphics_Widget__sofiagraphics_Widget", None)
        self.__sofiagraphics_Widget = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sofiagraphics_Style"):
                opp_val = getattr(old_value, "sofiagraphics_Style", None)
                if opp_val == self:
                    setattr(old_value, "sofiagraphics_Style", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sofiagraphics_Style"):
                opp_val = getattr(value, "sofiagraphics_Style", None)
                setattr(value, "sofiagraphics_Style", self)

    @property
    def sofiagraphics_Widget9(self):
        return self.__sofiagraphics_Widget9

    @sofiagraphics_Widget9.setter
    def sofiagraphics_Widget9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sofiagraphics_Widget__sofiagraphics_Widget9", None)
        self.__sofiagraphics_Widget9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sofiagraphics_Dimension"):
                opp_val = getattr(old_value, "sofiagraphics_Dimension", None)
                if opp_val == self:
                    setattr(old_value, "sofiagraphics_Dimension", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sofiagraphics_Dimension"):
                opp_val = getattr(value, "sofiagraphics_Dimension", None)
                setattr(value, "sofiagraphics_Dimension", self)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sofiagraphics_Widget__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Widget5"):
                    opp_val = getattr(item, "Widget5", None)
                    
                    if opp_val == self:
                        setattr(item, "Widget5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Widget5"):
                    opp_val = getattr(item, "Widget5", None)
                    
                    setattr(item, "Widget5", self)
                    

class sofiagraphics_Dimension:

    def __init__(self, width: float, height: float, wrelative: bool, hrelative: bool, noresize: bool, sofiagraphics_Dimension: "sofiagraphics_Widget" = None, sofiagraphics_Dimension11: "sofiagraphics_RoundedRectangle" = None, sofiagraphics_Dimension24: "sofiagraphics_Scene" = None):
        self.width = width
        self.height = height
        self.wrelative = wrelative
        self.hrelative = hrelative
        self.noresize = noresize
        self.sofiagraphics_Dimension = sofiagraphics_Dimension
        self.sofiagraphics_Dimension11 = sofiagraphics_Dimension11
        self.sofiagraphics_Dimension24 = sofiagraphics_Dimension24
        
    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, width: float):
        self.__width = width

    @property
    def wrelative(self) -> bool:
        return self.__wrelative

    @wrelative.setter
    def wrelative(self, wrelative: bool):
        self.__wrelative = wrelative

    @property
    def hrelative(self) -> bool:
        return self.__hrelative

    @hrelative.setter
    def hrelative(self, hrelative: bool):
        self.__hrelative = hrelative

    @property
    def height(self) -> float:
        return self.__height

    @height.setter
    def height(self, height: float):
        self.__height = height

    @property
    def noresize(self) -> bool:
        return self.__noresize

    @noresize.setter
    def noresize(self, noresize: bool):
        self.__noresize = noresize

    @property
    def sofiagraphics_Dimension11(self):
        return self.__sofiagraphics_Dimension11

    @sofiagraphics_Dimension11.setter
    def sofiagraphics_Dimension11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sofiagraphics_Dimension__sofiagraphics_Dimension11", None)
        self.__sofiagraphics_Dimension11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sofiagraphics_RoundedRectangle"):
                opp_val = getattr(old_value, "sofiagraphics_RoundedRectangle", None)
                if opp_val == self:
                    setattr(old_value, "sofiagraphics_RoundedRectangle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sofiagraphics_RoundedRectangle"):
                opp_val = getattr(value, "sofiagraphics_RoundedRectangle", None)
                setattr(value, "sofiagraphics_RoundedRectangle", self)

    @property
    def sofiagraphics_Dimension(self):
        return self.__sofiagraphics_Dimension

    @sofiagraphics_Dimension.setter
    def sofiagraphics_Dimension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sofiagraphics_Dimension__sofiagraphics_Dimension", None)
        self.__sofiagraphics_Dimension = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sofiagraphics_Widget9"):
                opp_val = getattr(old_value, "sofiagraphics_Widget9", None)
                if opp_val == self:
                    setattr(old_value, "sofiagraphics_Widget9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sofiagraphics_Widget9"):
                opp_val = getattr(value, "sofiagraphics_Widget9", None)
                setattr(value, "sofiagraphics_Widget9", self)

    @property
    def sofiagraphics_Dimension24(self):
        return self.__sofiagraphics_Dimension24

    @sofiagraphics_Dimension24.setter
    def sofiagraphics_Dimension24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sofiagraphics_Dimension__sofiagraphics_Dimension24", None)
        self.__sofiagraphics_Dimension24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sofiagraphics_Scene23"):
                opp_val = getattr(old_value, "sofiagraphics_Scene23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sofiagraphics_Scene23"):
                opp_val = getattr(value, "sofiagraphics_Scene23", None)
                if opp_val is None:
                    setattr(value, "sofiagraphics_Scene23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sofiagraphics_Point:

    def __init__(self, x: float, y: float, xrelative: bool, yrelative: bool, sofiagraphics_Point: "sofiagraphics_Widget" = None, sofiagraphics_Point13: "sofiagraphics_Polyline" = None, sofiagraphics_Point21: "sofiagraphics_Scene" = None):
        self.x = x
        self.y = y
        self.xrelative = xrelative
        self.yrelative = yrelative
        self.sofiagraphics_Point = sofiagraphics_Point
        self.sofiagraphics_Point13 = sofiagraphics_Point13
        self.sofiagraphics_Point21 = sofiagraphics_Point21
        
    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x

    @property
    def xrelative(self) -> bool:
        return self.__xrelative

    @xrelative.setter
    def xrelative(self, xrelative: bool):
        self.__xrelative = xrelative

    @property
    def yrelative(self) -> bool:
        return self.__yrelative

    @yrelative.setter
    def yrelative(self, yrelative: bool):
        self.__yrelative = yrelative

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y

    @property
    def sofiagraphics_Point(self):
        return self.__sofiagraphics_Point

    @sofiagraphics_Point.setter
    def sofiagraphics_Point(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sofiagraphics_Point__sofiagraphics_Point", None)
        self.__sofiagraphics_Point = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sofiagraphics_Widget7"):
                opp_val = getattr(old_value, "sofiagraphics_Widget7", None)
                if opp_val == self:
                    setattr(old_value, "sofiagraphics_Widget7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sofiagraphics_Widget7"):
                opp_val = getattr(value, "sofiagraphics_Widget7", None)
                setattr(value, "sofiagraphics_Widget7", self)

    @property
    def sofiagraphics_Point13(self):
        return self.__sofiagraphics_Point13

    @sofiagraphics_Point13.setter
    def sofiagraphics_Point13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sofiagraphics_Point__sofiagraphics_Point13", None)
        self.__sofiagraphics_Point13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sofiagraphics_Polyline"):
                opp_val = getattr(old_value, "sofiagraphics_Polyline", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sofiagraphics_Polyline"):
                opp_val = getattr(value, "sofiagraphics_Polyline", None)
                if opp_val is None:
                    setattr(value, "sofiagraphics_Polyline", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sofiagraphics_Point21(self):
        return self.__sofiagraphics_Point21

    @sofiagraphics_Point21.setter
    def sofiagraphics_Point21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sofiagraphics_Point__sofiagraphics_Point21", None)
        self.__sofiagraphics_Point21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sofiagraphics_Scene20"):
                opp_val = getattr(old_value, "sofiagraphics_Scene20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sofiagraphics_Scene20"):
                opp_val = getattr(value, "sofiagraphics_Scene20", None)
                if opp_val is None:
                    setattr(value, "sofiagraphics_Scene20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Rectangle:

    pass
class sofiagraphics_RoundedRectangle(Rectangle):

    pass
class Widget:

    pass
class sofiagraphics_Text(Widget):

    def __init__(self, text: str, halign: str, valign: str, attributeName: str):
        self.text = text
        self.halign = halign
        self.valign = valign
        self.attributeName = attributeName
        
    @property
    def valign(self) -> str:
        return self.__valign

    @valign.setter
    def valign(self, valign: str):
        self.__valign = valign

    @property
    def attributeName(self) -> str:
        return self.__attributeName

    @attributeName.setter
    def attributeName(self, attributeName: str):
        self.__attributeName = attributeName

    @property
    def halign(self) -> str:
        return self.__halign

    @halign.setter
    def halign(self, halign: str):
        self.__halign = halign

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class sofiagraphics_Ellipse(Widget):

    pass
class sofiagraphics_Polyline(Widget):

    pass
class sofiagraphics_Rectangle(Widget):

    pass
class sofiagraphics_Style:

    def __init__(self, filled: bool, lineWidth: float, sofiagraphics_Style: "sofiagraphics_Widget" = None, sofiagraphics_Style33: "sofiagraphics_Color" = None, sofiagraphics_Style36: "sofiagraphics_Color" = None, sofiagraphics_Style29: "sofiagraphics_Scene" = None):
        self.filled = filled
        self.lineWidth = lineWidth
        self.sofiagraphics_Style = sofiagraphics_Style
        self.sofiagraphics_Style33 = sofiagraphics_Style33
        self.sofiagraphics_Style36 = sofiagraphics_Style36
        self.sofiagraphics_Style29 = sofiagraphics_Style29
        
    @property
    def lineWidth(self) -> float:
        return self.__lineWidth

    @lineWidth.setter
    def lineWidth(self, lineWidth: float):
        self.__lineWidth = lineWidth

    @property
    def filled(self) -> bool:
        return self.__filled

    @filled.setter
    def filled(self, filled: bool):
        self.__filled = filled

    @property
    def sofiagraphics_Style36(self):
        return self.__sofiagraphics_Style36

    @sofiagraphics_Style36.setter
    def sofiagraphics_Style36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sofiagraphics_Style__sofiagraphics_Style36", None)
        self.__sofiagraphics_Style36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sofiagraphics_Color37"):
                opp_val = getattr(old_value, "sofiagraphics_Color37", None)
                if opp_val == self:
                    setattr(old_value, "sofiagraphics_Color37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sofiagraphics_Color37"):
                opp_val = getattr(value, "sofiagraphics_Color37", None)
                setattr(value, "sofiagraphics_Color37", self)

    @property
    def sofiagraphics_Style(self):
        return self.__sofiagraphics_Style

    @sofiagraphics_Style.setter
    def sofiagraphics_Style(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sofiagraphics_Style__sofiagraphics_Style", None)
        self.__sofiagraphics_Style = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sofiagraphics_Widget"):
                opp_val = getattr(old_value, "sofiagraphics_Widget", None)
                if opp_val == self:
                    setattr(old_value, "sofiagraphics_Widget", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sofiagraphics_Widget"):
                opp_val = getattr(value, "sofiagraphics_Widget", None)
                setattr(value, "sofiagraphics_Widget", self)

    @property
    def sofiagraphics_Style29(self):
        return self.__sofiagraphics_Style29

    @sofiagraphics_Style29.setter
    def sofiagraphics_Style29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sofiagraphics_Style__sofiagraphics_Style29", None)
        self.__sofiagraphics_Style29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sofiagraphics_Scene28"):
                opp_val = getattr(old_value, "sofiagraphics_Scene28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sofiagraphics_Scene28"):
                opp_val = getattr(value, "sofiagraphics_Scene28", None)
                if opp_val is None:
                    setattr(value, "sofiagraphics_Scene28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sofiagraphics_Style33(self):
        return self.__sofiagraphics_Style33

    @sofiagraphics_Style33.setter
    def sofiagraphics_Style33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sofiagraphics_Style__sofiagraphics_Style33", None)
        self.__sofiagraphics_Style33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sofiagraphics_Color34"):
                opp_val = getattr(old_value, "sofiagraphics_Color34", None)
                if opp_val == self:
                    setattr(old_value, "sofiagraphics_Color34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sofiagraphics_Color34"):
                opp_val = getattr(value, "sofiagraphics_Color34", None)
                setattr(value, "sofiagraphics_Color34", self)
