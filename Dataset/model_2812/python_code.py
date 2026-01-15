from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class VAlign(Enum):
    TOP = "TOP"
    MIDDLE = "MIDDLE"
    BOTTOM = "BOTTOM"
class TextType(Enum):
    default = "default"
    multiline = "multiline"
class AnchorPredefiniedEnum(Enum):
    center = "center"
    corners = "corners"
class ConnectionStyle(Enum):
    freeform = "freeform"
    manhatten = "manhatten"
class HAlign(Enum):
    LEFT = "LEFT"
    CENTER = "CENTER"
    RIGHT = "RIGHT"
class CompartmentLayout(Enum):
    FIXED = "FIXED"
    VERTICAL = "VERTICAL"
    HORIZONTAL = "HORIZONTAL"
    FIT = "FIT"


############################################
# Definition of Classes
############################################

class shape_Point:

    def __init__(self, xcor: str, ycor: str, curveBefore: int, curveAfter: int, shape_Point: "shape_LineLayout" = None, shape_Point98: "shape_PolyLineLayout" = None):
        self.xcor = xcor
        self.ycor = ycor
        self.curveBefore = curveBefore
        self.curveAfter = curveAfter
        self.shape_Point = shape_Point
        self.shape_Point98 = shape_Point98
        
    @property
    def xcor(self) -> str:
        return self.__xcor

    @xcor.setter
    def xcor(self, xcor: str):
        self.__xcor = xcor

    @property
    def curveBefore(self) -> int:
        return self.__curveBefore

    @curveBefore.setter
    def curveBefore(self, curveBefore: int):
        self.__curveBefore = curveBefore

    @property
    def curveAfter(self) -> int:
        return self.__curveAfter

    @curveAfter.setter
    def curveAfter(self, curveAfter: int):
        self.__curveAfter = curveAfter

    @property
    def ycor(self) -> str:
        return self.__ycor

    @ycor.setter
    def ycor(self, ycor: str):
        self.__ycor = ycor

    @property
    def shape_Point(self):
        return self.__shape_Point

    @shape_Point.setter
    def shape_Point(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shape_Point__shape_Point", None)
        self.__shape_Point = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shape_LineLayout92"):
                opp_val = getattr(old_value, "shape_LineLayout92", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shape_LineLayout92"):
                opp_val = getattr(value, "shape_LineLayout92", None)
                if opp_val is None:
                    setattr(value, "shape_LineLayout92", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def shape_Point98(self):
        return self.__shape_Point98

    @shape_Point98.setter
    def shape_Point98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shape_Point__shape_Point98", None)
        self.__shape_Point98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shape_PolyLineLayout97"):
                opp_val = getattr(old_value, "shape_PolyLineLayout97", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shape_PolyLineLayout97"):
                opp_val = getattr(value, "shape_PolyLineLayout97", None)
                if opp_val is None:
                    setattr(value, "shape_PolyLineLayout97", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class shape_CommonLayout:

    def __init__(self, xcor: int, ycor: int, width: int, heigth: int, shape_CommonLayout: "shape_RectangleEllipseLayout" = None, shape_CommonLayout104: "shape_RoundedRectangleLayout" = None, shape_CommonLayout110: "shape_TextLayout" = None):
        self.xcor = xcor
        self.ycor = ycor
        self.width = width
        self.heigth = heigth
        self.shape_CommonLayout = shape_CommonLayout
        self.shape_CommonLayout104 = shape_CommonLayout104
        self.shape_CommonLayout110 = shape_CommonLayout110
        
    @property
    def heigth(self) -> int:
        return self.__heigth

    @heigth.setter
    def heigth(self, heigth: int):
        self.__heigth = heigth

    @property
    def xcor(self) -> int:
        return self.__xcor

    @xcor.setter
    def xcor(self, xcor: int):
        self.__xcor = xcor

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width

    @property
    def ycor(self) -> int:
        return self.__ycor

    @ycor.setter
    def ycor(self, ycor: int):
        self.__ycor = ycor

    @property
    def shape_CommonLayout(self):
        return self.__shape_CommonLayout

    @shape_CommonLayout.setter
    def shape_CommonLayout(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shape_CommonLayout__shape_CommonLayout", None)
        self.__shape_CommonLayout = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shape_RectangleEllipseLayout87"):
                opp_val = getattr(old_value, "shape_RectangleEllipseLayout87", None)
                if opp_val == self:
                    setattr(old_value, "shape_RectangleEllipseLayout87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shape_RectangleEllipseLayout87"):
                opp_val = getattr(value, "shape_RectangleEllipseLayout87", None)
                setattr(value, "shape_RectangleEllipseLayout87", self)

    @property
    def shape_CommonLayout104(self):
        return self.__shape_CommonLayout104

    @shape_CommonLayout104.setter
    def shape_CommonLayout104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shape_CommonLayout__shape_CommonLayout104", None)
        self.__shape_CommonLayout104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shape_RoundedRectangleLayout103"):
                opp_val = getattr(old_value, "shape_RoundedRectangleLayout103", None)
                if opp_val == self:
                    setattr(old_value, "shape_RoundedRectangleLayout103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shape_RoundedRectangleLayout103"):
                opp_val = getattr(value, "shape_RoundedRectangleLayout103", None)
                setattr(value, "shape_RoundedRectangleLayout103", self)

    @property
    def shape_CommonLayout110(self):
        return self.__shape_CommonLayout110

    @shape_CommonLayout110.setter
    def shape_CommonLayout110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shape_CommonLayout__shape_CommonLayout110", None)
        self.__shape_CommonLayout110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shape_TextLayout109"):
                opp_val = getattr(old_value, "shape_TextLayout109", None)
                if opp_val == self:
                    setattr(old_value, "shape_TextLayout109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shape_TextLayout109"):
                opp_val = getattr(value, "shape_TextLayout109", None)
                setattr(value, "shape_TextLayout109", self)

class shape_CompartmentPolygon:

    pass
class shape_CompartmentRoundedRectangle:

    pass
class CompartmentShape:

    pass
class shape_CompartmentEllipse(CompartmentShape):

    pass
class shape_CompartmentRectangle(CompartmentShape):

    pass
class shape_CompartmentShape:

    pass
class shape_Compartment:

    def __init__(self, compartmentLayout: str, shape_Compartment: "shape_CompartmentShape" = None):
        self.compartmentLayout = compartmentLayout
        self.shape_Compartment = shape_Compartment
        
    @property
    def compartmentLayout(self) -> str:
        return self.__compartmentLayout

    @compartmentLayout.setter
    def compartmentLayout(self, compartmentLayout: str):
        self.__compartmentLayout = compartmentLayout

    @property
    def shape_Compartment(self):
        return self.__shape_Compartment

    @shape_Compartment.setter
    def shape_Compartment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shape_Compartment__shape_Compartment", None)
        self.__shape_Compartment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shape_CompartmentShape"):
                opp_val = getattr(old_value, "shape_CompartmentShape", None)
                if opp_val == self:
                    setattr(old_value, "shape_CompartmentShape", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shape_CompartmentShape"):
                opp_val = getattr(value, "shape_CompartmentShape", None)
                setattr(value, "shape_CompartmentShape", self)

class Shape:

    pass
class shape_Text(Shape):

    def __init__(self, texttype: str, shape_Text: "shape_TextLayout" = None, shape_Text61: "shape_TextBody" = None):
        self.texttype = texttype
        self.shape_Text = shape_Text
        self.shape_Text61 = shape_Text61
        
    @property
    def texttype(self) -> str:
        return self.__texttype

    @texttype.setter
    def texttype(self, texttype: str):
        self.__texttype = texttype

    @property
    def shape_Text61(self):
        return self.__shape_Text61

    @shape_Text61.setter
    def shape_Text61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shape_Text__shape_Text61", None)
        self.__shape_Text61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shape_TextBody62"):
                opp_val = getattr(old_value, "shape_TextBody62", None)
                if opp_val == self:
                    setattr(old_value, "shape_TextBody62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shape_TextBody62"):
                opp_val = getattr(value, "shape_TextBody62", None)
                setattr(value, "shape_TextBody62", self)

    @property
    def shape_Text(self):
        return self.__shape_Text

    @shape_Text.setter
    def shape_Text(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shape_Text__shape_Text", None)
        self.__shape_Text = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shape_TextLayout59"):
                opp_val = getattr(old_value, "shape_TextLayout59", None)
                if opp_val == self:
                    setattr(old_value, "shape_TextLayout59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shape_TextLayout59"):
                opp_val = getattr(value, "shape_TextLayout59", None)
                setattr(value, "shape_TextLayout59", self)

class shape_Ellipse(Shape):

    pass
class shape_Polygon(Shape):

    pass
class shape_Polyline(Shape):

    pass
class shape_Rectangle(Shape):

    pass
class shape_Line(Shape):

    pass
class shape_TextBody:

    def __init__(self, value: str, shape_TextBody: "shape_CDText" = None, shape_TextBody65: "shape_CompartmentInfo" = None, shape_TextBody62: "shape_Text" = None, shape_TextBody85: "shape_Description" = None, shape_TextBody72: "shape_CompartmentShape" = None, shape_TextBody77: "shape_CompartmentRoundedRectangle" = None, shape_TextBody82: "shape_CompartmentPolygon" = None):
        self.value = value
        self.shape_TextBody = shape_TextBody
        self.shape_TextBody65 = shape_TextBody65
        self.shape_TextBody62 = shape_TextBody62
        self.shape_TextBody85 = shape_TextBody85
        self.shape_TextBody72 = shape_TextBody72
        self.shape_TextBody77 = shape_TextBody77
        self.shape_TextBody82 = shape_TextBody82
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def shape_TextBody62(self):
        return self.__shape_TextBody62

    @shape_TextBody62.setter
    def shape_TextBody62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shape_TextBody__shape_TextBody62", None)
        self.__shape_TextBody62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shape_Text61"):
                opp_val = getattr(old_value, "shape_Text61", None)
                if opp_val == self:
                    setattr(old_value, "shape_Text61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shape_Text61"):
                opp_val = getattr(value, "shape_Text61", None)
                setattr(value, "shape_Text61", self)

    @property
    def shape_TextBody65(self):
        return self.__shape_TextBody65

    @shape_TextBody65.setter
    def shape_TextBody65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shape_TextBody__shape_TextBody65", None)
        self.__shape_TextBody65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shape_CompartmentInfo64"):
                opp_val = getattr(old_value, "shape_CompartmentInfo64", None)
                if opp_val == self:
                    setattr(old_value, "shape_CompartmentInfo64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shape_CompartmentInfo64"):
                opp_val = getattr(value, "shape_CompartmentInfo64", None)
                setattr(value, "shape_CompartmentInfo64", self)

    @property
    def shape_TextBody(self):
        return self.__shape_TextBody

    @shape_TextBody.setter
    def shape_TextBody(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shape_TextBody__shape_TextBody", None)
        self.__shape_TextBody = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shape_CDText28"):
                opp_val = getattr(old_value, "shape_CDText28", None)
                if opp_val == self:
                    setattr(old_value, "shape_CDText28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shape_CDText28"):
                opp_val = getattr(value, "shape_CDText28", None)
                setattr(value, "shape_CDText28", self)

    @property
    def shape_TextBody72(self):
        return self.__shape_TextBody72

    @shape_TextBody72.setter
    def shape_TextBody72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shape_TextBody__shape_TextBody72", None)
        self.__shape_TextBody72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shape_CompartmentShape71"):
                opp_val = getattr(old_value, "shape_CompartmentShape71", None)
                if opp_val == self:
                    setattr(old_value, "shape_CompartmentShape71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shape_CompartmentShape71"):
                opp_val = getattr(value, "shape_CompartmentShape71", None)
                setattr(value, "shape_CompartmentShape71", self)

    @property
    def shape_TextBody85(self):
        return self.__shape_TextBody85

    @shape_TextBody85.setter
    def shape_TextBody85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shape_TextBody__shape_TextBody85", None)
        self.__shape_TextBody85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shape_Description84"):
                opp_val = getattr(old_value, "shape_Description84", None)
                if opp_val == self:
                    setattr(old_value, "shape_Description84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shape_Description84"):
                opp_val = getattr(value, "shape_Description84", None)
                setattr(value, "shape_Description84", self)

    @property
    def shape_TextBody82(self):
        return self.__shape_TextBody82

    @shape_TextBody82.setter
    def shape_TextBody82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shape_TextBody__shape_TextBody82", None)
        self.__shape_TextBody82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shape_CompartmentPolygon81"):
                opp_val = getattr(old_value, "shape_CompartmentPolygon81", None)
                if opp_val == self:
                    setattr(old_value, "shape_CompartmentPolygon81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shape_CompartmentPolygon81"):
                opp_val = getattr(value, "shape_CompartmentPolygon81", None)
                setattr(value, "shape_CompartmentPolygon81", self)

    @property
    def shape_TextBody77(self):
        return self.__shape_TextBody77

    @shape_TextBody77.setter
    def shape_TextBody77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shape_TextBody__shape_TextBody77", None)
        self.__shape_TextBody77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shape_CompartmentRoundedRectangle76"):
                opp_val = getattr(old_value, "shape_CompartmentRoundedRectangle76", None)
                if opp_val == self:
                    setattr(old_value, "shape_CompartmentRoundedRectangle76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shape_CompartmentRoundedRectangle76"):
                opp_val = getattr(value, "shape_CompartmentRoundedRectangle76", None)
                setattr(value, "shape_CompartmentRoundedRectangle76", self)

class shape_TextLayout:

    def __init__(self, hAlign: str, vAlign: str, shape_TextLayout: "shape_CDText" = None, shape_TextLayout59: "shape_Text" = None, shape_TextLayout109: "shape_CommonLayout" = None, shape_TextLayout112: "shape_ShapestyleLayout" = None):
        self.hAlign = hAlign
        self.vAlign = vAlign
        self.shape_TextLayout = shape_TextLayout
        self.shape_TextLayout59 = shape_TextLayout59
        self.shape_TextLayout109 = shape_TextLayout109
        self.shape_TextLayout112 = shape_TextLayout112
        
    @property
    def hAlign(self) -> str:
        return self.__hAlign

    @hAlign.setter
    def hAlign(self, hAlign: str):
        self.__hAlign = hAlign

    @property
    def vAlign(self) -> str:
        return self.__vAlign

    @vAlign.setter
    def vAlign(self, vAlign: str):
        self.__vAlign = vAlign

    @property
    def shape_TextLayout112(self):
        return self.__shape_TextLayout112

    @shape_TextLayout112.setter
    def shape_TextLayout112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shape_TextLayout__shape_TextLayout112", None)
        self.__shape_TextLayout112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shape_ShapestyleLayout113"):
                opp_val = getattr(old_value, "shape_ShapestyleLayout113", None)
                if opp_val == self:
                    setattr(old_value, "shape_ShapestyleLayout113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shape_ShapestyleLayout113"):
                opp_val = getattr(value, "shape_ShapestyleLayout113", None)
                setattr(value, "shape_ShapestyleLayout113", self)

    @property
    def shape_TextLayout59(self):
        return self.__shape_TextLayout59

    @shape_TextLayout59.setter
    def shape_TextLayout59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shape_TextLayout__shape_TextLayout59", None)
        self.__shape_TextLayout59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shape_Text"):
                opp_val = getattr(old_value, "shape_Text", None)
                if opp_val == self:
                    setattr(old_value, "shape_Text", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shape_Text"):
                opp_val = getattr(value, "shape_Text", None)
                setattr(value, "shape_Text", self)

    @property
    def shape_TextLayout(self):
        return self.__shape_TextLayout

    @shape_TextLayout.setter
    def shape_TextLayout(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shape_TextLayout__shape_TextLayout", None)
        self.__shape_TextLayout = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shape_CDText"):
                opp_val = getattr(old_value, "shape_CDText", None)
                if opp_val == self:
                    setattr(old_value, "shape_CDText", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shape_CDText"):
                opp_val = getattr(value, "shape_CDText", None)
                setattr(value, "shape_CDText", self)

    @property
    def shape_TextLayout109(self):
        return self.__shape_TextLayout109

    @shape_TextLayout109.setter
    def shape_TextLayout109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shape_TextLayout__shape_TextLayout109", None)
        self.__shape_TextLayout109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shape_CommonLayout110"):
                opp_val = getattr(old_value, "shape_CommonLayout110", None)
                if opp_val == self:
                    setattr(old_value, "shape_CommonLayout110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shape_CommonLayout110"):
                opp_val = getattr(value, "shape_CommonLayout110", None)
                setattr(value, "shape_CommonLayout110", self)

class shape_RoundedRectangleLayout:

    def __init__(self, curveWidth: int, curveHeight: int, shape_RoundedRectangleLayout41: "shape_RoundedRectangle" = None, shape_RoundedRectangleLayout: "shape_CDRoundedRectangle" = None, shape_RoundedRectangleLayout74: "shape_CompartmentRoundedRectangle" = None, shape_RoundedRectangleLayout103: "shape_CommonLayout" = None, shape_RoundedRectangleLayout106: "shape_ShapestyleLayout" = None):
        self.curveWidth = curveWidth
        self.curveHeight = curveHeight
        self.shape_RoundedRectangleLayout41 = shape_RoundedRectangleLayout41
        self.shape_RoundedRectangleLayout = shape_RoundedRectangleLayout
        self.shape_RoundedRectangleLayout74 = shape_RoundedRectangleLayout74
        self.shape_RoundedRectangleLayout103 = shape_RoundedRectangleLayout103
        self.shape_RoundedRectangleLayout106 = shape_RoundedRectangleLayout106
        
    @property
    def curveHeight(self) -> int:
        return self.__curveHeight

    @curveHeight.setter
    def curveHeight(self, curveHeight: int):
        self.__curveHeight = curveHeight

    @property
    def curveWidth(self) -> int:
        return self.__curveWidth

    @curveWidth.setter
    def curveWidth(self, curveWidth: int):
        self.__curveWidth = curveWidth

    @property
    def shape_RoundedRectangleLayout103(self):
        return self.__shape_RoundedRectangleLayout103

    @shape_RoundedRectangleLayout103.setter
    def shape_RoundedRectangleLayout103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shape_RoundedRectangleLayout__shape_RoundedRectangleLayout103", None)
        self.__shape_RoundedRectangleLayout103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shape_CommonLayout104"):
                opp_val = getattr(old_value, "shape_CommonLayout104", None)
                if opp_val == self:
                    setattr(old_value, "shape_CommonLayout104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shape_CommonLayout104"):
                opp_val = getattr(value, "shape_CommonLayout104", None)
                setattr(value, "shape_CommonLayout104", self)

    @property
    def shape_RoundedRectangleLayout106(self):
        return self.__shape_RoundedRectangleLayout106

    @shape_RoundedRectangleLayout106.setter
    def shape_RoundedRectangleLayout106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shape_RoundedRectangleLayout__shape_RoundedRectangleLayout106", None)
        self.__shape_RoundedRectangleLayout106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shape_ShapestyleLayout107"):
                opp_val = getattr(old_value, "shape_ShapestyleLayout107", None)
                if opp_val == self:
                    setattr(old_value, "shape_ShapestyleLayout107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shape_ShapestyleLayout107"):
                opp_val = getattr(value, "shape_ShapestyleLayout107", None)
                setattr(value, "shape_ShapestyleLayout107", self)

    @property
    def shape_RoundedRectangleLayout74(self):
        return self.__shape_RoundedRectangleLayout74

    @shape_RoundedRectangleLayout74.setter
    def shape_RoundedRectangleLayout74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shape_RoundedRectangleLayout__shape_RoundedRectangleLayout74", None)
        self.__shape_RoundedRectangleLayout74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shape_CompartmentRoundedRectangle"):
                opp_val = getattr(old_value, "shape_CompartmentRoundedRectangle", None)
                if opp_val == self:
                    setattr(old_value, "shape_CompartmentRoundedRectangle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shape_CompartmentRoundedRectangle"):
                opp_val = getattr(value, "shape_CompartmentRoundedRectangle", None)
                setattr(value, "shape_CompartmentRoundedRectangle", self)

    @property
    def shape_RoundedRectangleLayout(self):
        return self.__shape_RoundedRectangleLayout

    @shape_RoundedRectangleLayout.setter
    def shape_RoundedRectangleLayout(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shape_RoundedRectangleLayout__shape_RoundedRectangleLayout", None)
        self.__shape_RoundedRectangleLayout = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shape_CDRoundedRectangle"):
                opp_val = getattr(old_value, "shape_CDRoundedRectangle", None)
                if opp_val == self:
                    setattr(old_value, "shape_CDRoundedRectangle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shape_CDRoundedRectangle"):
                opp_val = getattr(value, "shape_CDRoundedRectangle", None)
                setattr(value, "shape_CDRoundedRectangle", self)

    @property
    def shape_RoundedRectangleLayout41(self):
        return self.__shape_RoundedRectangleLayout41

    @shape_RoundedRectangleLayout41.setter
    def shape_RoundedRectangleLayout41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shape_RoundedRectangleLayout__shape_RoundedRectangleLayout41", None)
        self.__shape_RoundedRectangleLayout41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shape_RoundedRectangle"):
                opp_val = getattr(old_value, "shape_RoundedRectangle", None)
                if opp_val == self:
                    setattr(old_value, "shape_RoundedRectangle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shape_RoundedRectangle"):
                opp_val = getattr(value, "shape_RoundedRectangle", None)
                setattr(value, "shape_RoundedRectangle", self)

class shape_RoundedRectangle(Shape):

    pass
class shape_CompartmentInfo:

    def __init__(self, spacing: int, margin: int, invisible: bool, compartmentLayout: str, stretchH: str, stretchV: str, shape_CompartmentInfo: "shape_Rectangle" = None, shape_CompartmentInfo64: "shape_TextBody" = None, shape_CompartmentInfo51: "shape_Ellipse" = None):
        self.spacing = spacing
        self.margin = margin
        self.invisible = invisible
        self.compartmentLayout = compartmentLayout
        self.stretchH = stretchH
        self.stretchV = stretchV
        self.shape_CompartmentInfo = shape_CompartmentInfo
        self.shape_CompartmentInfo64 = shape_CompartmentInfo64
        self.shape_CompartmentInfo51 = shape_CompartmentInfo51
        
    @property
    def stretchH(self) -> str:
        return self.__stretchH

    @stretchH.setter
    def stretchH(self, stretchH: str):
        self.__stretchH = stretchH

    @property
    def stretchV(self) -> str:
        return self.__stretchV

    @stretchV.setter
    def stretchV(self, stretchV: str):
        self.__stretchV = stretchV

    @property
    def invisible(self) -> bool:
        return self.__invisible

    @invisible.setter
    def invisible(self, invisible: bool):
        self.__invisible = invisible

    @property
    def margin(self) -> int:
        return self.__margin

    @margin.setter
    def margin(self, margin: int):
        self.__margin = margin

    @property
    def spacing(self) -> int:
        return self.__spacing

    @spacing.setter
    def spacing(self, spacing: int):
        self.__spacing = spacing

    @property
    def compartmentLayout(self) -> str:
        return self.__compartmentLayout

    @compartmentLayout.setter
    def compartmentLayout(self, compartmentLayout: str):
        self.__compartmentLayout = compartmentLayout

    @property
    def shape_CompartmentInfo64(self):
        return self.__shape_CompartmentInfo64

    @shape_CompartmentInfo64.setter
    def shape_CompartmentInfo64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shape_CompartmentInfo__shape_CompartmentInfo64", None)
        self.__shape_CompartmentInfo64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shape_TextBody65"):
                opp_val = getattr(old_value, "shape_TextBody65", None)
                if opp_val == self:
                    setattr(old_value, "shape_TextBody65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shape_TextBody65"):
                opp_val = getattr(value, "shape_TextBody65", None)
                setattr(value, "shape_TextBody65", self)

    @property
    def shape_CompartmentInfo(self):
        return self.__shape_CompartmentInfo

    @shape_CompartmentInfo.setter
    def shape_CompartmentInfo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shape_CompartmentInfo__shape_CompartmentInfo", None)
        self.__shape_CompartmentInfo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shape_Rectangle"):
                opp_val = getattr(old_value, "shape_Rectangle", None)
                if opp_val == self:
                    setattr(old_value, "shape_Rectangle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shape_Rectangle"):
                opp_val = getattr(value, "shape_Rectangle", None)
                setattr(value, "shape_Rectangle", self)

    @property
    def shape_CompartmentInfo51(self):
        return self.__shape_CompartmentInfo51

    @shape_CompartmentInfo51.setter
    def shape_CompartmentInfo51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shape_CompartmentInfo__shape_CompartmentInfo51", None)
        self.__shape_CompartmentInfo51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shape_Ellipse"):
                opp_val = getattr(old_value, "shape_Ellipse", None)
                if opp_val == self:
                    setattr(old_value, "shape_Ellipse", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shape_Ellipse"):
                opp_val = getattr(value, "shape_Ellipse", None)
                setattr(value, "shape_Ellipse", self)

class ShapeConnection:

    pass
class shape_CDPolygon(ShapeConnection):

    pass
class shape_CDEllipse(ShapeConnection):

    pass
class shape_CDText(ShapeConnection):

    def __init__(self, texttype: str, shape_CDText: "shape_TextLayout" = None, shape_CDText28: "shape_TextBody" = None):
        self.texttype = texttype
        self.shape_CDText = shape_CDText
        self.shape_CDText28 = shape_CDText28
        
    @property
    def texttype(self) -> str:
        return self.__texttype

    @texttype.setter
    def texttype(self, texttype: str):
        self.__texttype = texttype

    @property
    def shape_CDText(self):
        return self.__shape_CDText

    @shape_CDText.setter
    def shape_CDText(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shape_CDText__shape_CDText", None)
        self.__shape_CDText = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shape_TextLayout"):
                opp_val = getattr(old_value, "shape_TextLayout", None)
                if opp_val == self:
                    setattr(old_value, "shape_TextLayout", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shape_TextLayout"):
                opp_val = getattr(value, "shape_TextLayout", None)
                setattr(value, "shape_TextLayout", self)

    @property
    def shape_CDText28(self):
        return self.__shape_CDText28

    @shape_CDText28.setter
    def shape_CDText28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shape_CDText__shape_CDText28", None)
        self.__shape_CDText28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shape_TextBody"):
                opp_val = getattr(old_value, "shape_TextBody", None)
                if opp_val == self:
                    setattr(old_value, "shape_TextBody", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shape_TextBody"):
                opp_val = getattr(value, "shape_TextBody", None)
                setattr(value, "shape_TextBody", self)

class shape_CDLine(ShapeConnection):

    pass
class AnchorPositionPos:

    pass
class shape_AnchorFixPointPosition(AnchorPositionPos):

    def __init__(self, xcor: int, ycor: int):
        self.xcor = xcor
        self.ycor = ycor
        
    @property
    def xcor(self) -> int:
        return self.__xcor

    @xcor.setter
    def xcor(self, xcor: int):
        self.__xcor = xcor

    @property
    def ycor(self) -> int:
        return self.__ycor

    @ycor.setter
    def ycor(self, ycor: int):
        self.__ycor = ycor

class shape_AnchorRelativePosition(AnchorPositionPos):

    def __init__(self, xoffset: str, yoffset: str):
        self.xoffset = xoffset
        self.yoffset = yoffset
        
    @property
    def yoffset(self) -> str:
        return self.__yoffset

    @yoffset.setter
    def yoffset(self, yoffset: str):
        self.__yoffset = yoffset

    @property
    def xoffset(self) -> str:
        return self.__xoffset

    @xoffset.setter
    def xoffset(self, xoffset: str):
        self.__xoffset = xoffset

class shape_AnchorPositionPos:

    pass
class shape_AnchorPosition:

    pass
class AnchorType:

    pass
class shape_AnchorManual(AnchorType):

    pass
class shape_AnchorPredefinied(AnchorType):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class shape_AnchorType:

    pass
class shape_CDRoundedRectangle(ShapeConnection):

    pass
class shape_RectangleEllipseLayout:

    pass
class shape_CDRectangle(ShapeConnection):

    pass
class shape_PolyLineLayout:

    pass
class shape_CDPolyline(ShapeConnection):

    pass
class shape_LineLayout:

    pass
class shape_Shape:

    def __init__(self, style: str, shape_Shape: "shape_ShapeDefinition" = None, shape_Shape39: "shape_Rectangle" = None, shape_Shape44: "shape_RoundedRectangle" = None, shape_Shape49: "shape_Polygon" = None, shape_Shape57: "shape_Ellipse" = None):
        self.style = style
        self.shape_Shape = shape_Shape
        self.shape_Shape39 = shape_Shape39
        self.shape_Shape44 = shape_Shape44
        self.shape_Shape49 = shape_Shape49
        self.shape_Shape57 = shape_Shape57
        
    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def shape_Shape39(self):
        return self.__shape_Shape39

    @shape_Shape39.setter
    def shape_Shape39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shape_Shape__shape_Shape39", None)
        self.__shape_Shape39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shape_Rectangle38"):
                opp_val = getattr(old_value, "shape_Rectangle38", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shape_Rectangle38"):
                opp_val = getattr(value, "shape_Rectangle38", None)
                if opp_val is None:
                    setattr(value, "shape_Rectangle38", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def shape_Shape(self):
        return self.__shape_Shape

    @shape_Shape.setter
    def shape_Shape(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shape_Shape__shape_Shape", None)
        self.__shape_Shape = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shape_ShapeDefinition6"):
                opp_val = getattr(old_value, "shape_ShapeDefinition6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shape_ShapeDefinition6"):
                opp_val = getattr(value, "shape_ShapeDefinition6", None)
                if opp_val is None:
                    setattr(value, "shape_ShapeDefinition6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def shape_Shape57(self):
        return self.__shape_Shape57

    @shape_Shape57.setter
    def shape_Shape57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shape_Shape__shape_Shape57", None)
        self.__shape_Shape57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shape_Ellipse56"):
                opp_val = getattr(old_value, "shape_Ellipse56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shape_Ellipse56"):
                opp_val = getattr(value, "shape_Ellipse56", None)
                if opp_val is None:
                    setattr(value, "shape_Ellipse56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def shape_Shape49(self):
        return self.__shape_Shape49

    @shape_Shape49.setter
    def shape_Shape49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shape_Shape__shape_Shape49", None)
        self.__shape_Shape49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shape_Polygon48"):
                opp_val = getattr(old_value, "shape_Polygon48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shape_Polygon48"):
                opp_val = getattr(value, "shape_Polygon48", None)
                if opp_val is None:
                    setattr(value, "shape_Polygon48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def shape_Shape44(self):
        return self.__shape_Shape44

    @shape_Shape44.setter
    def shape_Shape44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shape_Shape__shape_Shape44", None)
        self.__shape_Shape44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shape_RoundedRectangle43"):
                opp_val = getattr(old_value, "shape_RoundedRectangle43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shape_RoundedRectangle43"):
                opp_val = getattr(value, "shape_RoundedRectangle43", None)
                if opp_val is None:
                    setattr(value, "shape_RoundedRectangle43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class shape_ShapeLayout:

    def __init__(self, minwidth: int, minheight: int, maxwidth: int, maxheight: int, stretchH: str, stretchV: str, proportional: str, shape_ShapeLayout: "shape_ShapeDefinition" = None):
        self.minwidth = minwidth
        self.minheight = minheight
        self.maxwidth = maxwidth
        self.maxheight = maxheight
        self.stretchH = stretchH
        self.stretchV = stretchV
        self.proportional = proportional
        self.shape_ShapeLayout = shape_ShapeLayout
        
    @property
    def stretchH(self) -> str:
        return self.__stretchH

    @stretchH.setter
    def stretchH(self, stretchH: str):
        self.__stretchH = stretchH

    @property
    def stretchV(self) -> str:
        return self.__stretchV

    @stretchV.setter
    def stretchV(self, stretchV: str):
        self.__stretchV = stretchV

    @property
    def maxheight(self) -> int:
        return self.__maxheight

    @maxheight.setter
    def maxheight(self, maxheight: int):
        self.__maxheight = maxheight

    @property
    def maxwidth(self) -> int:
        return self.__maxwidth

    @maxwidth.setter
    def maxwidth(self, maxwidth: int):
        self.__maxwidth = maxwidth

    @property
    def minwidth(self) -> int:
        return self.__minwidth

    @minwidth.setter
    def minwidth(self, minwidth: int):
        self.__minwidth = minwidth

    @property
    def proportional(self) -> str:
        return self.__proportional

    @proportional.setter
    def proportional(self, proportional: str):
        self.__proportional = proportional

    @property
    def minheight(self) -> int:
        return self.__minheight

    @minheight.setter
    def minheight(self, minheight: int):
        self.__minheight = minheight

    @property
    def shape_ShapeLayout(self):
        return self.__shape_ShapeLayout

    @shape_ShapeLayout.setter
    def shape_ShapeLayout(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shape_ShapeLayout__shape_ShapeLayout", None)
        self.__shape_ShapeLayout = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shape_ShapeDefinition"):
                opp_val = getattr(old_value, "shape_ShapeDefinition", None)
                if opp_val == self:
                    setattr(old_value, "shape_ShapeDefinition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shape_ShapeDefinition"):
                opp_val = getattr(value, "shape_ShapeDefinition", None)
                setattr(value, "shape_ShapeDefinition", self)

class shape_PlacingDefinition:

    def __init__(self, offset: str, distance: int, angle: int, shape_PlacingDefinition12: "shape_ShapeConnection" = None, shape_PlacingDefinition: "shape_ConnectionDefinition" = None):
        self.offset = offset
        self.distance = distance
        self.angle = angle
        self.shape_PlacingDefinition12 = shape_PlacingDefinition12
        self.shape_PlacingDefinition = shape_PlacingDefinition
        
    @property
    def offset(self) -> str:
        return self.__offset

    @offset.setter
    def offset(self, offset: str):
        self.__offset = offset

    @property
    def angle(self) -> int:
        return self.__angle

    @angle.setter
    def angle(self, angle: int):
        self.__angle = angle

    @property
    def distance(self) -> int:
        return self.__distance

    @distance.setter
    def distance(self, distance: int):
        self.__distance = distance

    @property
    def shape_PlacingDefinition(self):
        return self.__shape_PlacingDefinition

    @shape_PlacingDefinition.setter
    def shape_PlacingDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shape_PlacingDefinition__shape_PlacingDefinition", None)
        self.__shape_PlacingDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shape_ConnectionDefinition3"):
                opp_val = getattr(old_value, "shape_ConnectionDefinition3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shape_ConnectionDefinition3"):
                opp_val = getattr(value, "shape_ConnectionDefinition3", None)
                if opp_val is None:
                    setattr(value, "shape_ConnectionDefinition3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def shape_PlacingDefinition12(self):
        return self.__shape_PlacingDefinition12

    @shape_PlacingDefinition12.setter
    def shape_PlacingDefinition12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shape_PlacingDefinition__shape_PlacingDefinition12", None)
        self.__shape_PlacingDefinition12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shape_ShapeConnection"):
                opp_val = getattr(old_value, "shape_ShapeConnection", None)
                if opp_val == self:
                    setattr(old_value, "shape_ShapeConnection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shape_ShapeConnection"):
                opp_val = getattr(value, "shape_ShapeConnection", None)
                setattr(value, "shape_ShapeConnection", self)

class shape_ShapestyleLayout:

    pass
class ShapeContainerElement:

    pass
class shape_ShapeDefinition(ShapeContainerElement):

    pass
class shape_ConnectionDefinition(ShapeContainerElement):

    def __init__(self, connectionStyle: str, shape_ConnectionDefinition: "shape_ShapestyleLayout" = None, shape_ConnectionDefinition3: set["shape_PlacingDefinition"] = None):
        self.connectionStyle = connectionStyle
        self.shape_ConnectionDefinition = shape_ConnectionDefinition
        self.shape_ConnectionDefinition3 = shape_ConnectionDefinition3 if shape_ConnectionDefinition3 is not None else set()
        
    @property
    def connectionStyle(self) -> str:
        return self.__connectionStyle

    @connectionStyle.setter
    def connectionStyle(self, connectionStyle: str):
        self.__connectionStyle = connectionStyle

    @property
    def shape_ConnectionDefinition3(self):
        return self.__shape_ConnectionDefinition3

    @shape_ConnectionDefinition3.setter
    def shape_ConnectionDefinition3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shape_ConnectionDefinition__shape_ConnectionDefinition3", None)
        self.__shape_ConnectionDefinition3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shape_PlacingDefinition"):
                    opp_val = getattr(item, "shape_PlacingDefinition", None)
                    
                    if opp_val == self:
                        setattr(item, "shape_PlacingDefinition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shape_PlacingDefinition"):
                    opp_val = getattr(item, "shape_PlacingDefinition", None)
                    
                    setattr(item, "shape_PlacingDefinition", self)
                    

    @property
    def shape_ConnectionDefinition(self):
        return self.__shape_ConnectionDefinition

    @shape_ConnectionDefinition.setter
    def shape_ConnectionDefinition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shape_ConnectionDefinition__shape_ConnectionDefinition", None)
        self.__shape_ConnectionDefinition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shape_ShapestyleLayout"):
                opp_val = getattr(old_value, "shape_ShapestyleLayout", None)
                if opp_val == self:
                    setattr(old_value, "shape_ShapestyleLayout", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shape_ShapestyleLayout"):
                opp_val = getattr(value, "shape_ShapestyleLayout", None)
                setattr(value, "shape_ShapestyleLayout", self)

class shape_ShapeContainerElement:

    def __init__(self, name: str, style: str, shape_ShapeContainerElement: "shape_ShapeContainer" = None):
        self.name = name
        self.style = style
        self.shape_ShapeContainerElement = shape_ShapeContainerElement
        
    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def shape_ShapeContainerElement(self):
        return self.__shape_ShapeContainerElement

    @shape_ShapeContainerElement.setter
    def shape_ShapeContainerElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shape_ShapeContainerElement__shape_ShapeContainerElement", None)
        self.__shape_ShapeContainerElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shape_ShapeContainer"):
                opp_val = getattr(old_value, "shape_ShapeContainer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shape_ShapeContainer"):
                opp_val = getattr(value, "shape_ShapeContainer", None)
                if opp_val is None:
                    setattr(value, "shape_ShapeContainer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class shape_ShapeContainer:

    pass
class shape_ShapeConnection:

    def __init__(self, style: str, shape_ShapeConnection: "shape_PlacingDefinition" = None):
        self.style = style
        self.shape_ShapeConnection = shape_ShapeConnection
        
    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def shape_ShapeConnection(self):
        return self.__shape_ShapeConnection

    @shape_ShapeConnection.setter
    def shape_ShapeConnection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shape_ShapeConnection__shape_ShapeConnection", None)
        self.__shape_ShapeConnection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shape_PlacingDefinition12"):
                opp_val = getattr(old_value, "shape_PlacingDefinition12", None)
                if opp_val == self:
                    setattr(old_value, "shape_PlacingDefinition12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shape_PlacingDefinition12"):
                opp_val = getattr(value, "shape_PlacingDefinition12", None)
                setattr(value, "shape_PlacingDefinition12", self)

class shape_Anchor:

    pass
class shape_Description:

    def __init__(self, style: str, hAlign: str, vAlign: str, shape_Description: "shape_ShapeDefinition" = None, shape_Description84: "shape_TextBody" = None):
        self.style = style
        self.hAlign = hAlign
        self.vAlign = vAlign
        self.shape_Description = shape_Description
        self.shape_Description84 = shape_Description84
        
    @property
    def vAlign(self) -> str:
        return self.__vAlign

    @vAlign.setter
    def vAlign(self, vAlign: str):
        self.__vAlign = vAlign

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def hAlign(self) -> str:
        return self.__hAlign

    @hAlign.setter
    def hAlign(self, hAlign: str):
        self.__hAlign = hAlign

    @property
    def shape_Description(self):
        return self.__shape_Description

    @shape_Description.setter
    def shape_Description(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shape_Description__shape_Description", None)
        self.__shape_Description = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shape_ShapeDefinition8"):
                opp_val = getattr(old_value, "shape_ShapeDefinition8", None)
                if opp_val == self:
                    setattr(old_value, "shape_ShapeDefinition8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shape_ShapeDefinition8"):
                opp_val = getattr(value, "shape_ShapeDefinition8", None)
                setattr(value, "shape_ShapeDefinition8", self)

    @property
    def shape_Description84(self):
        return self.__shape_Description84

    @shape_Description84.setter
    def shape_Description84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shape_Description__shape_Description84", None)
        self.__shape_Description84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shape_TextBody85"):
                opp_val = getattr(old_value, "shape_TextBody85", None)
                if opp_val == self:
                    setattr(old_value, "shape_TextBody85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shape_TextBody85"):
                opp_val = getattr(value, "shape_TextBody85", None)
                setattr(value, "shape_TextBody85", self)
