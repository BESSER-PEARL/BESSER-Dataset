from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class BooleanLiteral(Enum):
    TRUE = "TRUE"
    FALSE = "FALSE"
class AnchorDirection(Enum):
    INCOMING = "INCOMING"
    OUTGOING = "OUTGOING"
class LineType(Enum):
    SOLID = "SOLID"
    DASH = "DASH"
    DOT = "DOT"
class DefaultColor(Enum):
    BLUE = "BLUE"
    NAVY = "NAVY"
    FUCHSIA = "FUCHSIA"
    PURPLE = "PURPLE"
    WHITE = "WHITE"
    SILVER = "SILVER"
    GRAY = "GRAY"
    BLACK = "BLACK"
    RED = "RED"
    MAROON = "MAROON"
    YELLOW = "YELLOW"
    OLIVE = "OLIVE"
    LIME = "LIME"
    GREEN = "GREEN"
    AQUA = "AQUA"
    TEAL = "TEAL"
class Operator(Enum):
    EQUAL = "EQUAL"
    DIFFERENT = "DIFFERENT"
class TextAlignValue(Enum):
    LEFT = "LEFT"
    CENTER = "CENTER"
    RIGHT = "RIGHT"


############################################
# Definition of Classes
############################################

class model_TextPart:

    def __init__(self, text: str, editable: bool, model_TextPart: "model_TextValue" = None, model_TextPart57: "model_EAttribute" = None):
        self.text = text
        self.editable = editable
        self.model_TextPart = model_TextPart
        self.model_TextPart57 = model_TextPart57
        
        pass
    @property
    def editable(self):
        return self.__editable

    @editable.setter
    def editable(self, editable: bool):
        self.__editable = editable


    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def model_TextPart(self):
        return self.__model_TextPart

    @model_TextPart.setter
    def model_TextPart(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TextPart__model_TextPart", None)
        self.__model_TextPart = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_TextValue"):
                opp_val = getattr(old_value, "model_TextValue", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_TextValue"):
                opp_val = getattr(value, "model_TextValue", None)
                if opp_val is None:
                    setattr(value, "model_TextValue", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_TextPart57(self):
        return self.__model_TextPart57

    @model_TextPart57.setter
    def model_TextPart57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TextPart__model_TextPart57", None)
        self.__model_TextPart57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_EAttribute58"):
                opp_val = getattr(old_value, "model_EAttribute58", None)
                if opp_val == self:
                    setattr(old_value, "model_EAttribute58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_EAttribute58"):
                opp_val = getattr(value, "model_EAttribute58", None)
                setattr(value, "model_EAttribute58", self)

class Value:

    pass
class model_EnumValue(Value):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class model_BooleanValue(Value):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class model_DoubleValue(Value):

    def __init__(self, valueInt: int, valueDecimal: int):
        self.valueInt = valueInt
        self.valueDecimal = valueDecimal
        
        pass
    @property
    def valueInt(self):
        return self.__valueInt

    @valueInt.setter
    def valueInt(self, valueInt: int):
        self.__valueInt = valueInt


    @property
    def valueDecimal(self):
        return self.__valueDecimal

    @valueDecimal.setter
    def valueDecimal(self, valueDecimal: int):
        self.__valueDecimal = valueDecimal


class model_StringValue(Value):

    def __init__(self, null: bool, value: str):
        self.null = null
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def null(self):
        return self.__null

    @null.setter
    def null(self, null: bool):
        self.__null = null


class model_IntValue(Value):

    def __init__(self, value: int):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


class model_CustomColor:

    def __init__(self, R: int, G: int, B: int, name: str, model_CustomColor41: "model_Color" = None, model_CustomColor: "model_Colors" = None):
        self.R = R
        self.G = G
        self.B = B
        self.name = name
        self.model_CustomColor41 = model_CustomColor41
        self.model_CustomColor = model_CustomColor
        
        pass
    @property
    def B(self):
        return self.__B

    @B.setter
    def B(self, B: int):
        self.__B = B


    @property
    def G(self):
        return self.__G

    @G.setter
    def G(self, G: int):
        self.__G = G


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def R(self):
        return self.__R

    @R.setter
    def R(self, R: int):
        self.__R = R


    @property
    def model_CustomColor41(self):
        return self.__model_CustomColor41

    @model_CustomColor41.setter
    def model_CustomColor41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_CustomColor__model_CustomColor41", None)
        self.__model_CustomColor41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Color"):
                opp_val = getattr(old_value, "model_Color", None)
                if opp_val == self:
                    setattr(old_value, "model_Color", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Color"):
                opp_val = getattr(value, "model_Color", None)
                setattr(value, "model_Color", self)

    @property
    def model_CustomColor(self):
        return self.__model_CustomColor

    @model_CustomColor.setter
    def model_CustomColor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_CustomColor__model_CustomColor", None)
        self.__model_CustomColor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Colors39"):
                opp_val = getattr(old_value, "model_Colors39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Colors39"):
                opp_val = getattr(value, "model_Colors39", None)
                if opp_val is None:
                    setattr(value, "model_Colors39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Feature:

    pass
class model_Transparency(Feature):

    def __init__(self, percent: int):
        self.percent = percent
        
        pass
    @property
    def percent(self):
        return self.__percent

    @percent.setter
    def percent(self, percent: int):
        self.__percent = percent


class model_TextValue(Feature):

    pass
class model_TextAlign(Feature):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class model_Corner(Feature):

    def __init__(self, angle: int):
        self.angle = angle
        
        pass
    @property
    def angle(self):
        return self.__angle

    @angle.setter
    def angle(self, angle: int):
        self.__angle = angle


class model_Layout(Feature):

    def __init__(self, vertical: bool, horizontal: bool, margin: int):
        self.vertical = vertical
        self.horizontal = horizontal
        self.margin = margin
        
        pass
    @property
    def horizontal(self):
        return self.__horizontal

    @horizontal.setter
    def horizontal(self, horizontal: bool):
        self.__horizontal = horizontal


    @property
    def margin(self):
        return self.__margin

    @margin.setter
    def margin(self, margin: int):
        self.__margin = margin


    @property
    def vertical(self):
        return self.__vertical

    @vertical.setter
    def vertical(self, vertical: bool):
        self.__vertical = vertical


class model_Position(Feature):

    def __init__(self, xRelative: bool, y: int, yRelative: bool, x: int):
        self.xRelative = xRelative
        self.y = y
        self.yRelative = yRelative
        self.x = x
        
        pass
    @property
    def xRelative(self):
        return self.__xRelative

    @xRelative.setter
    def xRelative(self, xRelative: bool):
        self.__xRelative = xRelative


    @property
    def yRelative(self):
        return self.__yRelative

    @yRelative.setter
    def yRelative(self, yRelative: bool):
        self.__yRelative = yRelative


    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y


    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x


class model_LineStyle(Feature):

    def __init__(self, style: str, manhattan: bool):
        self.style = style
        self.manhattan = manhattan
        
        pass
    @property
    def manhattan(self):
        return self.__manhattan

    @manhattan.setter
    def manhattan(self, manhattan: bool):
        self.__manhattan = manhattan


    @property
    def style(self):
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style


class model_Point(Feature):

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        
        pass
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y


    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x


class model_Size(Feature):

    def __init__(self, width: int, widthRelative: bool, height: int, heightRelative: bool, resizable: bool):
        self.width = width
        self.widthRelative = widthRelative
        self.height = height
        self.heightRelative = heightRelative
        self.resizable = resizable
        
        pass
    @property
    def resizable(self):
        return self.__resizable

    @resizable.setter
    def resizable(self, resizable: bool):
        self.__resizable = resizable


    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height


    @property
    def widthRelative(self):
        return self.__widthRelative

    @widthRelative.setter
    def widthRelative(self, widthRelative: bool):
        self.__widthRelative = widthRelative


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width


    @property
    def heightRelative(self):
        return self.__heightRelative

    @heightRelative.setter
    def heightRelative(self, heightRelative: bool):
        self.__heightRelative = heightRelative


class model_FontProperties(Feature):

    def __init__(self, face: str, size: int, bold: bool, italics: bool):
        self.face = face
        self.size = size
        self.bold = bold
        self.italics = italics
        
        pass
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size


    @property
    def italics(self):
        return self.__italics

    @italics.setter
    def italics(self, italics: bool):
        self.__italics = italics


    @property
    def face(self):
        return self.__face

    @face.setter
    def face(self, face: str):
        self.__face = face


    @property
    def bold(self):
        return self.__bold

    @bold.setter
    def bold(self, bold: bool):
        self.__bold = bold


class model_ColorFeature(Feature):

    def __init__(self, type: str, model_ColorFeature: "model_Color" = None):
        self.type = type
        self.model_ColorFeature = model_ColorFeature
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def model_ColorFeature(self):
        return self.__model_ColorFeature

    @model_ColorFeature.setter
    def model_ColorFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ColorFeature__model_ColorFeature", None)
        self.__model_ColorFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Color54"):
                opp_val = getattr(old_value, "model_Color54", None)
                if opp_val == self:
                    setattr(old_value, "model_Color54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Color54"):
                opp_val = getattr(value, "model_Color54", None)
                setattr(value, "model_Color54", self)

class model_LineWidth(Feature):

    def __init__(self, width: int):
        self.width = width
        
        pass
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width


class model_Visible(Feature):

    pass
class model_Anchor(Feature):

    def __init__(self, direction: str, max: int, model_Anchor: "model_EReference" = None):
        self.direction = direction
        self.max = max
        self.model_Anchor = model_Anchor
        
        pass
    @property
    def max(self):
        return self.__max

    @max.setter
    def max(self, max: int):
        self.__max = max


    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction


    @property
    def model_Anchor(self):
        return self.__model_Anchor

    @model_Anchor.setter
    def model_Anchor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Anchor__model_Anchor", None)
        self.__model_Anchor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_EReference37"):
                opp_val = getattr(old_value, "model_EReference37", None)
                if opp_val == self:
                    setattr(old_value, "model_EReference37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_EReference37"):
                opp_val = getattr(value, "model_EReference37", None)
                setattr(value, "model_EReference37", self)

class ConnectableElement:

    pass
class model_Ellipse(ConnectableElement):

    def __init__(self, ellipse: bool, circle: bool):
        self.ellipse = ellipse
        self.circle = circle
        
        pass
    @property
    def circle(self):
        return self.__circle

    @circle.setter
    def circle(self, circle: bool):
        self.__circle = circle


    @property
    def ellipse(self):
        return self.__ellipse

    @ellipse.setter
    def ellipse(self, ellipse: bool):
        self.__ellipse = ellipse


class model_Invisible(ConnectableElement):

    pass
class model_Rhombus(ConnectableElement):

    pass
class model_Image(ConnectableElement):

    def __init__(self, imageId: str):
        self.imageId = imageId
        
        pass
    @property
    def imageId(self):
        return self.__imageId

    @imageId.setter
    def imageId(self, imageId: str):
        self.__imageId = imageId


class model_Label(ConnectableElement):

    pass
class model_Rectangle(ConnectableElement):

    def __init__(self, rectangle: bool, square: bool):
        self.rectangle = rectangle
        self.square = square
        
        pass
    @property
    def square(self):
        return self.__square

    @square.setter
    def square(self, square: bool):
        self.__square = square


    @property
    def rectangle(self):
        return self.__rectangle

    @rectangle.setter
    def rectangle(self, rectangle: bool):
        self.__rectangle = rectangle


class model_Triangle(ConnectableElement):

    pass
class model_Polyline(ConnectableElement):

    def __init__(self, polygon: bool, polyline: bool):
        self.polygon = polygon
        self.polyline = polyline
        
        pass
    @property
    def polyline(self):
        return self.__polyline

    @polyline.setter
    def polyline(self, polyline: bool):
        self.__polyline = polyline


    @property
    def polygon(self):
        return self.__polygon

    @polygon.setter
    def polygon(self, polygon: bool):
        self.__polygon = polygon


class model_Custom(ConnectableElement):

    pass
class model_Color:

    def __init__(self, default: str, model_Color: "model_CustomColor" = None, model_Color54: "model_ColorFeature" = None):
        self.default = default
        self.model_Color = model_Color
        self.model_Color54 = model_Color54
        
        pass
    @property
    def default(self):
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default


    @property
    def model_Color(self):
        return self.__model_Color

    @model_Color.setter
    def model_Color(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Color__model_Color", None)
        self.__model_Color = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_CustomColor41"):
                opp_val = getattr(old_value, "model_CustomColor41", None)
                if opp_val == self:
                    setattr(old_value, "model_CustomColor41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_CustomColor41"):
                opp_val = getattr(value, "model_CustomColor41", None)
                setattr(value, "model_CustomColor41", self)

    @property
    def model_Color54(self):
        return self.__model_Color54

    @model_Color54.setter
    def model_Color54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Color__model_Color54", None)
        self.__model_Color54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ColorFeature"):
                opp_val = getattr(old_value, "model_ColorFeature", None)
                if opp_val == self:
                    setattr(old_value, "model_ColorFeature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ColorFeature"):
                opp_val = getattr(value, "model_ColorFeature", None)
                setattr(value, "model_ColorFeature", self)

class model_Contains(Feature):

    pass
class model_EClass:

    pass
class model_ImportStatement:

    def __init__(self, importedNamespace: str):
        self.importedNamespace = importedNamespace
        
        pass
    @property
    def importedNamespace(self):
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace


class model_CustomFigure:

    def __init__(self, name: str, model_CustomFigure: "model_XDiagram" = None, model_CustomFigure46: "model_ConnectableElement" = None, model_CustomFigure49: "model_Custom" = None):
        self.name = name
        self.model_CustomFigure = model_CustomFigure
        self.model_CustomFigure46 = model_CustomFigure46
        self.model_CustomFigure49 = model_CustomFigure49
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def model_CustomFigure49(self):
        return self.__model_CustomFigure49

    @model_CustomFigure49.setter
    def model_CustomFigure49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_CustomFigure__model_CustomFigure49", None)
        self.__model_CustomFigure49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Custom"):
                opp_val = getattr(old_value, "model_Custom", None)
                if opp_val == self:
                    setattr(old_value, "model_Custom", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Custom"):
                opp_val = getattr(value, "model_Custom", None)
                setattr(value, "model_Custom", self)

    @property
    def model_CustomFigure46(self):
        return self.__model_CustomFigure46

    @model_CustomFigure46.setter
    def model_CustomFigure46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_CustomFigure__model_CustomFigure46", None)
        self.__model_CustomFigure46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ConnectableElement47"):
                opp_val = getattr(old_value, "model_ConnectableElement47", None)
                if opp_val == self:
                    setattr(old_value, "model_ConnectableElement47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ConnectableElement47"):
                opp_val = getattr(value, "model_ConnectableElement47", None)
                setattr(value, "model_ConnectableElement47", self)

    @property
    def model_CustomFigure(self):
        return self.__model_CustomFigure

    @model_CustomFigure.setter
    def model_CustomFigure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_CustomFigure__model_CustomFigure", None)
        self.__model_CustomFigure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_XDiagram8"):
                opp_val = getattr(old_value, "model_XDiagram8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_XDiagram8"):
                opp_val = getattr(value, "model_XDiagram8", None)
                if opp_val is None:
                    setattr(value, "model_XDiagram8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_DiagramElement:

    pass
class model_Colors:

    pass
class model_Decorator:

    pass
class model_EReference:

    pass
class FeatureContainer:

    pass
class model_Arrow(FeatureContainer):

    pass
class model_Line(FeatureContainer):

    def __init__(self, vertical: bool, horizontal: bool):
        self.vertical = vertical
        self.horizontal = horizontal
        
        pass
    @property
    def horizontal(self):
        return self.__horizontal

    @horizontal.setter
    def horizontal(self, horizontal: bool):
        self.__horizontal = horizontal


    @property
    def vertical(self):
        return self.__vertical

    @vertical.setter
    def vertical(self, vertical: bool):
        self.__vertical = vertical


class model_ConnectableElement(FeatureContainer):

    pass
class DiagramElement:

    pass
class model_Link(DiagramElement, FeatureContainer):

    def __init__(self, reference: bool, complex: bool, model_Link: "model_EReference" = None, model_Link26: "model_EReference" = None, model_Link29: "model_EReference" = None, model_Link32: set["model_Decorator"] = None):
        self.reference = reference
        self.complex = complex
        self.model_Link = model_Link
        self.model_Link26 = model_Link26
        self.model_Link29 = model_Link29
        self.model_Link32 = model_Link32 if model_Link32 is not None else set()
        
        pass
    @property
    def complex(self):
        return self.__complex

    @complex.setter
    def complex(self, complex: bool):
        self.__complex = complex


    @property
    def reference(self):
        return self.__reference

    @reference.setter
    def reference(self, reference: bool):
        self.__reference = reference


    @property
    def model_Link29(self):
        return self.__model_Link29

    @model_Link29.setter
    def model_Link29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Link__model_Link29", None)
        self.__model_Link29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_EReference30"):
                opp_val = getattr(old_value, "model_EReference30", None)
                if opp_val == self:
                    setattr(old_value, "model_EReference30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_EReference30"):
                opp_val = getattr(value, "model_EReference30", None)
                setattr(value, "model_EReference30", self)

    @property
    def model_Link26(self):
        return self.__model_Link26

    @model_Link26.setter
    def model_Link26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Link__model_Link26", None)
        self.__model_Link26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_EReference27"):
                opp_val = getattr(old_value, "model_EReference27", None)
                if opp_val == self:
                    setattr(old_value, "model_EReference27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_EReference27"):
                opp_val = getattr(value, "model_EReference27", None)
                setattr(value, "model_EReference27", self)

    @property
    def model_Link(self):
        return self.__model_Link

    @model_Link.setter
    def model_Link(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Link__model_Link", None)
        self.__model_Link = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_EReference"):
                opp_val = getattr(old_value, "model_EReference", None)
                if opp_val == self:
                    setattr(old_value, "model_EReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_EReference"):
                opp_val = getattr(value, "model_EReference", None)
                setattr(value, "model_EReference", self)

    @property
    def model_Link32(self):
        return self.__model_Link32

    @model_Link32.setter
    def model_Link32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Link__model_Link32", None)
        self.__model_Link32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Decorator"):
                    opp_val = getattr(item, "model_Decorator", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Decorator", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Decorator"):
                    opp_val = getattr(item, "model_Decorator", None)
                    
                    setattr(item, "model_Decorator", self)
                    

class model_Node(DiagramElement):

    pass
class model_Value:

    pass
class model_EAttribute:

    pass
class model_FeatureContainer:

    pass
class model_FeatureConditional:

    def __init__(self, operator: str, model_FeatureConditional: "model_Feature" = None, model_FeatureConditional20: "model_EAttribute" = None, model_FeatureConditional22: "model_Value" = None):
        self.operator = operator
        self.model_FeatureConditional = model_FeatureConditional
        self.model_FeatureConditional20 = model_FeatureConditional20
        self.model_FeatureConditional22 = model_FeatureConditional22
        
        pass
    @property
    def operator(self):
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator


    @property
    def model_FeatureConditional22(self):
        return self.__model_FeatureConditional22

    @model_FeatureConditional22.setter
    def model_FeatureConditional22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_FeatureConditional__model_FeatureConditional22", None)
        self.__model_FeatureConditional22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Value"):
                opp_val = getattr(old_value, "model_Value", None)
                if opp_val == self:
                    setattr(old_value, "model_Value", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Value"):
                opp_val = getattr(value, "model_Value", None)
                setattr(value, "model_Value", self)

    @property
    def model_FeatureConditional20(self):
        return self.__model_FeatureConditional20

    @model_FeatureConditional20.setter
    def model_FeatureConditional20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_FeatureConditional__model_FeatureConditional20", None)
        self.__model_FeatureConditional20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_EAttribute"):
                opp_val = getattr(old_value, "model_EAttribute", None)
                if opp_val == self:
                    setattr(old_value, "model_EAttribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_EAttribute"):
                opp_val = getattr(value, "model_EAttribute", None)
                setattr(value, "model_EAttribute", self)

    @property
    def model_FeatureConditional(self):
        return self.__model_FeatureConditional

    @model_FeatureConditional.setter
    def model_FeatureConditional(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_FeatureConditional__model_FeatureConditional", None)
        self.__model_FeatureConditional = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Feature"):
                opp_val = getattr(old_value, "model_Feature", None)
                if opp_val == self:
                    setattr(old_value, "model_Feature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Feature"):
                opp_val = getattr(value, "model_Feature", None)
                setattr(value, "model_Feature", self)

class model_Feature:

    pass
class model_Diagram:

    pass
class model_MetaModel:

    def __init__(self, plugin: str, ecorePath: str, model_MetaModel: "model_XDiagram" = None):
        self.plugin = plugin
        self.ecorePath = ecorePath
        self.model_MetaModel = model_MetaModel
        
        pass
    @property
    def ecorePath(self):
        return self.__ecorePath

    @ecorePath.setter
    def ecorePath(self, ecorePath: str):
        self.__ecorePath = ecorePath


    @property
    def plugin(self):
        return self.__plugin

    @plugin.setter
    def plugin(self, plugin: str):
        self.__plugin = plugin


    @property
    def model_MetaModel(self):
        return self.__model_MetaModel

    @model_MetaModel.setter
    def model_MetaModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_MetaModel__model_MetaModel", None)
        self.__model_MetaModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_XDiagram"):
                opp_val = getattr(old_value, "model_XDiagram", None)
                if opp_val == self:
                    setattr(old_value, "model_XDiagram", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_XDiagram"):
                opp_val = getattr(value, "model_XDiagram", None)
                setattr(value, "model_XDiagram", self)

class model_XDiagram:

    pass