from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class AnchorDirection(Enum):
    INCOMING = "INCOMING"
    OUTGOING = "OUTGOING"
class TextAlignValue(Enum):
    CENTER = "CENTER"
    RIGHT = "RIGHT"
    LEFT = "LEFT"
class Operator(Enum):
    EQUAL = "EQUAL"
    DIFFERENT = "DIFFERENT"
class LineType(Enum):
    SOLID = "SOLID"
    DASH = "DASH"
    DOT = "DOT"
class DefaultColor(Enum):
    MAROON = "MAROON"
    YELLOW = "YELLOW"
    OLIVE = "OLIVE"
    LIME = "LIME"
    GREEN = "GREEN"
    AQUA = "AQUA"
    WHITE = "WHITE"
    TEAL = "TEAL"
    SILVER = "SILVER"
    BLUE = "BLUE"
    GRAY = "GRAY"
    NAVY = "NAVY"
    BLACK = "BLACK"
    FUCHSIA = "FUCHSIA"
    RED = "RED"
    PURPLE = "PURPLE"
class BooleanLiteral(Enum):
    TRUE = "TRUE"
    FALSE = "FALSE"


############################################
# Definition of Classes
############################################

class model_TextPart:

    def __init__(self, text: str, editable: bool, model_TextPart: "model_TextValue" = None, model_TextPart57: "model_EAttribute" = None):
        self.text = text
        self.editable = editable
        self.model_TextPart = model_TextPart
        self.model_TextPart57 = model_TextPart57
        
    @property
    def editable(self) -> bool:
        return self.__editable

    @editable.setter
    def editable(self, editable: bool):
        self.__editable = editable

    @property
    def text(self) -> str:
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
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class model_BooleanValue(Value):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class model_StringValue(Value):

    def __init__(self, null: bool, value: str):
        self.null = null
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def null(self) -> bool:
        return self.__null

    @null.setter
    def null(self, null: bool):
        self.__null = null

class model_IntValue(Value):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class model_DoubleValue(Value):

    def __init__(self, valueInt: int, valueDecimal: int):
        self.valueInt = valueInt
        self.valueDecimal = valueDecimal
        
    @property
    def valueInt(self) -> int:
        return self.__valueInt

    @valueInt.setter
    def valueInt(self, valueInt: int):
        self.__valueInt = valueInt

    @property
    def valueDecimal(self) -> int:
        return self.__valueDecimal

    @valueDecimal.setter
    def valueDecimal(self, valueDecimal: int):
        self.__valueDecimal = valueDecimal

class ConnectableElement:

    pass
class model_Invisible(ConnectableElement):

    pass
class model_Image(ConnectableElement):

    def __init__(self, imageId: str):
        self.imageId = imageId
        
    @property
    def imageId(self) -> str:
        return self.__imageId

    @imageId.setter
    def imageId(self, imageId: str):
        self.__imageId = imageId

class model_Ellipse(ConnectableElement):

    def __init__(self, ellipse: bool, circle: bool):
        self.ellipse = ellipse
        self.circle = circle
        
    @property
    def circle(self) -> bool:
        return self.__circle

    @circle.setter
    def circle(self, circle: bool):
        self.__circle = circle

    @property
    def ellipse(self) -> bool:
        return self.__ellipse

    @ellipse.setter
    def ellipse(self, ellipse: bool):
        self.__ellipse = ellipse

class model_Label(ConnectableElement):

    pass
class model_Rectangle(ConnectableElement):

    def __init__(self, square: bool, rectangle: bool):
        self.square = square
        self.rectangle = rectangle
        
    @property
    def square(self) -> bool:
        return self.__square

    @square.setter
    def square(self, square: bool):
        self.__square = square

    @property
    def rectangle(self) -> bool:
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
        
    @property
    def polyline(self) -> bool:
        return self.__polyline

    @polyline.setter
    def polyline(self, polyline: bool):
        self.__polyline = polyline

    @property
    def polygon(self) -> bool:
        return self.__polygon

    @polygon.setter
    def polygon(self, polygon: bool):
        self.__polygon = polygon

class model_Custom(ConnectableElement):

    pass
class model_Rhombus(ConnectableElement):

    pass
class model_Color:

    def __init__(self, default: str, model_Color: "model_CustomColor" = None, model_Color54: "model_ColorFeature" = None):
        self.default = default
        self.model_Color = model_Color
        self.model_Color54 = model_Color54
        
    @property
    def default(self) -> str:
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

class Feature:

    pass
class model_Position(Feature):

    def __init__(self, x: int, xRelative: bool, y: int, yRelative: bool):
        self.x = x
        self.xRelative = xRelative
        self.y = y
        self.yRelative = yRelative
        
    @property
    def xRelative(self) -> bool:
        return self.__xRelative

    @xRelative.setter
    def xRelative(self, xRelative: bool):
        self.__xRelative = xRelative

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x

    @property
    def yRelative(self) -> bool:
        return self.__yRelative

    @yRelative.setter
    def yRelative(self, yRelative: bool):
        self.__yRelative = yRelative

    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y

class model_Point(Feature):

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        
    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x

class model_LineStyle(Feature):

    def __init__(self, style: str, manhattan: bool):
        self.style = style
        self.manhattan = manhattan
        
    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def manhattan(self) -> bool:
        return self.__manhattan

    @manhattan.setter
    def manhattan(self, manhattan: bool):
        self.__manhattan = manhattan

class model_Corner(Feature):

    def __init__(self, angle: int):
        self.angle = angle
        
    @property
    def angle(self) -> int:
        return self.__angle

    @angle.setter
    def angle(self, angle: int):
        self.__angle = angle

class model_Transparency(Feature):

    def __init__(self, percent: int):
        self.percent = percent
        
    @property
    def percent(self) -> int:
        return self.__percent

    @percent.setter
    def percent(self, percent: int):
        self.__percent = percent

class model_TextAlign(Feature):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class model_FontProperties(Feature):

    def __init__(self, face: str, size: int, bold: bool, italics: bool):
        self.face = face
        self.size = size
        self.bold = bold
        self.italics = italics
        
    @property
    def italics(self) -> bool:
        return self.__italics

    @italics.setter
    def italics(self, italics: bool):
        self.__italics = italics

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def bold(self) -> bool:
        return self.__bold

    @bold.setter
    def bold(self, bold: bool):
        self.__bold = bold

    @property
    def face(self) -> str:
        return self.__face

    @face.setter
    def face(self, face: str):
        self.__face = face

class model_Visible(Feature):

    pass
class model_ColorFeature(Feature):

    def __init__(self, type: str, model_ColorFeature: "model_Color" = None):
        self.type = type
        self.model_ColorFeature = model_ColorFeature
        
    @property
    def type(self) -> str:
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

class model_Layout(Feature):

    def __init__(self, vertical: bool, horizontal: bool, margin: int):
        self.vertical = vertical
        self.horizontal = horizontal
        self.margin = margin
        
    @property
    def vertical(self) -> bool:
        return self.__vertical

    @vertical.setter
    def vertical(self, vertical: bool):
        self.__vertical = vertical

    @property
    def horizontal(self) -> bool:
        return self.__horizontal

    @horizontal.setter
    def horizontal(self, horizontal: bool):
        self.__horizontal = horizontal

    @property
    def margin(self) -> int:
        return self.__margin

    @margin.setter
    def margin(self, margin: int):
        self.__margin = margin

class model_LineWidth(Feature):

    def __init__(self, width: int):
        self.width = width
        
    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width

class model_TextValue(Feature):

    pass
class model_Size(Feature):

    def __init__(self, width: int, widthRelative: bool, height: int, heightRelative: bool, resizable: bool):
        self.width = width
        self.widthRelative = widthRelative
        self.height = height
        self.heightRelative = heightRelative
        self.resizable = resizable
        
    @property
    def widthRelative(self) -> bool:
        return self.__widthRelative

    @widthRelative.setter
    def widthRelative(self, widthRelative: bool):
        self.__widthRelative = widthRelative

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height

    @property
    def resizable(self) -> bool:
        return self.__resizable

    @resizable.setter
    def resizable(self, resizable: bool):
        self.__resizable = resizable

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width

    @property
    def heightRelative(self) -> bool:
        return self.__heightRelative

    @heightRelative.setter
    def heightRelative(self, heightRelative: bool):
        self.__heightRelative = heightRelative

class model_Anchor(Feature):

    def __init__(self, direction: str, max: int, model_Anchor: "model_EReference" = None):
        self.direction = direction
        self.max = max
        self.model_Anchor = model_Anchor
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def max(self) -> int:
        return self.__max

    @max.setter
    def max(self, max: int):
        self.__max = max

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

class model_Decorator:

    pass
class model_EReference:

    pass
class model_CustomColor:

    def __init__(self, name: str, R: int, G: int, B: int, model_CustomColor: "model_Colors" = None, model_CustomColor41: "model_Color" = None):
        self.name = name
        self.R = R
        self.G = G
        self.B = B
        self.model_CustomColor = model_CustomColor
        self.model_CustomColor41 = model_CustomColor41
        
    @property
    def B(self) -> int:
        return self.__B

    @B.setter
    def B(self, B: int):
        self.__B = B

    @property
    def G(self) -> int:
        return self.__G

    @G.setter
    def G(self, G: int):
        self.__G = G

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def R(self) -> int:
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

class FeatureContainer:

    pass
class model_Arrow(FeatureContainer):

    pass
class model_Line(FeatureContainer):

    def __init__(self, horizontal: bool, vertical: bool):
        self.horizontal = horizontal
        self.vertical = vertical
        
    @property
    def horizontal(self) -> bool:
        return self.__horizontal

    @horizontal.setter
    def horizontal(self, horizontal: bool):
        self.__horizontal = horizontal

    @property
    def vertical(self) -> bool:
        return self.__vertical

    @vertical.setter
    def vertical(self, vertical: bool):
        self.__vertical = vertical

class model_EAttribute:

    pass
class model_FeatureContainer:

    pass
class model_FeatureConditional:

    def __init__(self, operator: str, model_FeatureConditional22: "model_Value" = None, model_FeatureConditional: "model_Feature" = None, model_FeatureConditional20: "model_EAttribute" = None):
        self.operator = operator
        self.model_FeatureConditional22 = model_FeatureConditional22
        self.model_FeatureConditional = model_FeatureConditional
        self.model_FeatureConditional20 = model_FeatureConditional20
        
    @property
    def operator(self) -> str:
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

class model_Feature:

    pass
class model_Contains(Feature):

    pass
class model_ConnectableElement(FeatureContainer):

    pass
class DiagramElement:

    pass
class model_Link(FeatureContainer, DiagramElement):

    def __init__(self, reference: bool, complex: bool, model_Link: "model_EReference" = None, model_Link26: "model_EReference" = None, model_Link29: "model_EReference" = None, model_Link32: set["model_Decorator"] = None):
        self.reference = reference
        self.complex = complex
        self.model_Link = model_Link
        self.model_Link26 = model_Link26
        self.model_Link29 = model_Link29
        self.model_Link32 = model_Link32 if model_Link32 is not None else set()
        
    @property
    def reference(self) -> bool:
        return self.__reference

    @reference.setter
    def reference(self, reference: bool):
        self.__reference = reference

    @property
    def complex(self) -> bool:
        return self.__complex

    @complex.setter
    def complex(self, complex: bool):
        self.__complex = complex

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

class model_Node(DiagramElement):

    pass
class model_Value:

    pass
class model_CustomFigure:

    def __init__(self, name: str, model_CustomFigure: "model_XDiagram" = None, model_CustomFigure46: "model_ConnectableElement" = None, model_CustomFigure49: "model_Custom" = None):
        self.name = name
        self.model_CustomFigure = model_CustomFigure
        self.model_CustomFigure46 = model_CustomFigure46
        self.model_CustomFigure49 = model_CustomFigure49
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
class model_Diagram:

    pass
class model_MetaModel:

    def __init__(self, plugin: str, ecorePath: str, model_MetaModel: "model_XDiagram" = None):
        self.plugin = plugin
        self.ecorePath = ecorePath
        self.model_MetaModel = model_MetaModel
        
    @property
    def ecorePath(self) -> str:
        return self.__ecorePath

    @ecorePath.setter
    def ecorePath(self, ecorePath: str):
        self.__ecorePath = ecorePath

    @property
    def plugin(self) -> str:
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
class model_EClass:

    pass
class model_ImportStatement:

    def __init__(self, importedNamespace: str):
        self.importedNamespace = importedNamespace
        
    @property
    def importedNamespace(self) -> str:
        return self.__importedNamespace

    @importedNamespace.setter
    def importedNamespace(self, importedNamespace: str):
        self.__importedNamespace = importedNamespace
