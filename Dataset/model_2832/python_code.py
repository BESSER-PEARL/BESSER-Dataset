from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ColorConstants(Enum):
    white = "white"
    black = "black"
    lightGray = "lightGray"
    gray = "gray"
    darkGray = "darkGray"
    red = "red"
    orange = "orange"
    yellow = "yellow"
    green = "green"
    lightGreen = "lightGreen"
    darkGreen = "darkGreen"
    cyan = "cyan"
    lightBlue = "lightBlue"
    blue = "blue"
    darkBlue = "darkBlue"
class Alignment(Enum):
    BEGINNING = "BEGINNING"
    CENTER = "CENTER"
    END = "END"
    FILL = "FILL"
class LineKind(Enum):
    LINE_SOLID = "LINE_SOLID"
    LINE_CUSTOM = "LINE_CUSTOM"
    LINE_DASH = "LINE_DASH"
    LINE_DOT = "LINE_DOT"
    LINE_DASHDOT = "LINE_DASHDOT"
    LINE_DASHDOTDOT = "LINE_DASHDOTDOT"
class Language(Enum):
    ocl = "ocl"
    java = "java"
    regexp = "regexp"
    nregexp = "nregexp"
    literal = "literal"
class Severity(Enum):
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
class FontStyle(Enum):
    NORMAL = "NORMAL"
    BOLD = "BOLD"
    ITALIC = "ITALIC"
class ActionKind(Enum):
    CREATE = "CREATE"
    PROPCHANGE = "PROPCHANGE"
    MODIFY = "MODIFY"
    PROCESS = "PROCESS"
    CUSTOM = "CUSTOM"
class LabelTextAccessMethod(Enum):
    MESSAGE_FORMAT = "MESSAGE_FORMAT"
    NATIVE = "NATIVE"
    REGEXP = "REGEXP"
    PRINTF = "PRINTF"
class SVGPropertyType(Enum):
    STRING = "STRING"
    COLOR = "COLOR"
    FLOAT = "FLOAT"
class AppearanceStyle(Enum):
    Font = "Font"
    Fill = "Fill"
    Line = "Line"
class Direction(Enum):
    NONE = "NONE"
    NORTH = "NORTH"
    SOUTH = "SOUTH"
    WEST = "WEST"
    EAST = "EAST"
    NORTH_EAST = "NORTH_EAST"
    NORTH_WEST = "NORTH_WEST"
    SOUTH_EAST = "SOUTH_EAST"
    SOUTH_WEST = "SOUTH_WEST"
    NORTH_SOUTH = "NORTH_SOUTH"
    EAST_WEST = "EAST_WEST"
    NSEW = "NSEW"
class StandardToolKind(Enum):
    SELECT = "SELECT"
    SELECT_PAN = "SELECT_PAN"
    MARQUEE = "MARQUEE"
    ZOOM_PAN = "ZOOM_PAN"
    ZOOM_IN = "ZOOM_IN"
    ZOOM_OUT = "ZOOM_OUT"


############################################
# Definition of Classes
############################################

class gmf_all_gmfgraph_PinOwner(ABC):

    pass
class Rectangle2D:

    pass
class gmf_all_gmfgraph_Rectangle2D:

    def __init__(self, x: float, y: float, width: float, height: float):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, width: float):
        self.__width = width

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y

    @property
    def height(self) -> float:
        return self.__height

    @height.setter
    def height(self, height: float):
        self.__height = height

class gmf_all_gmfgraph_SVGProperty:

    def __init__(self, query: str, attribute: str, type: str, getter: str, setter: str, callSuper: bool):
        self.query = query
        self.attribute = attribute
        self.type = type
        self.getter = getter
        self.setter = setter
        self.callSuper = callSuper
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def callSuper(self) -> bool:
        return self.__callSuper

    @callSuper.setter
    def callSuper(self, callSuper: bool):
        self.__callSuper = callSuper

    @property
    def attribute(self) -> str:
        return self.__attribute

    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def query(self) -> str:
        return self.__query

    @query.setter
    def query(self, query: str):
        self.__query = query

    @property
    def getter(self) -> str:
        return self.__getter

    @getter.setter
    def getter(self, getter: str):
        self.__getter = getter

    @property
    def setter(self) -> str:
        return self.__setter

    @setter.setter
    def setter(self, setter: str):
        self.__setter = setter

class SVGProperty:

    pass
class gmfgraph_Layout:

    pass
class gmf_all_gmfgraph_Layout(ABC):

    pass
class gmf_all_gmfgraph_Layoutable(ABC):

    pass
class LayoutData:

    pass
class gmf_all_gmfgraph_XYLayoutData(LayoutData):

    pass
class gmf_all_gmfgraph_BorderLayoutData(LayoutData):

    def __init__(self, alignment: str, vertical: bool, gmfgraph285: "gmf_all_gmfgraph_Layoutable"):
        self.alignment = alignment
        self.vertical = vertical
        
    @property
    def vertical(self) -> bool:
        return self.__vertical

    @vertical.setter
    def vertical(self, vertical: bool):
        self.__vertical = vertical

    @property
    def alignment(self) -> str:
        return self.__alignment

    @alignment.setter
    def alignment(self, alignment: str):
        self.__alignment = alignment

class gmf_all_gmfgraph_GridLayoutData(LayoutData):

    def __init__(self, grabExcessHorizontalSpace: bool, grabExcessVerticalSpace: bool, verticalSpan: int, horizontalSpan: int, horizontalIndent: int, verticalAlignment: str, horizontalAlignment: str, gmf_all_gmfgraph_GridLayoutData: "Dimension" = None, gmfgraph285: "gmf_all_gmfgraph_Layoutable"):
        self.grabExcessHorizontalSpace = grabExcessHorizontalSpace
        self.grabExcessVerticalSpace = grabExcessVerticalSpace
        self.verticalSpan = verticalSpan
        self.horizontalSpan = horizontalSpan
        self.horizontalIndent = horizontalIndent
        self.verticalAlignment = verticalAlignment
        self.horizontalAlignment = horizontalAlignment
        self.gmf_all_gmfgraph_GridLayoutData = gmf_all_gmfgraph_GridLayoutData
        
    @property
    def grabExcessHorizontalSpace(self) -> bool:
        return self.__grabExcessHorizontalSpace

    @grabExcessHorizontalSpace.setter
    def grabExcessHorizontalSpace(self, grabExcessHorizontalSpace: bool):
        self.__grabExcessHorizontalSpace = grabExcessHorizontalSpace

    @property
    def grabExcessVerticalSpace(self) -> bool:
        return self.__grabExcessVerticalSpace

    @grabExcessVerticalSpace.setter
    def grabExcessVerticalSpace(self, grabExcessVerticalSpace: bool):
        self.__grabExcessVerticalSpace = grabExcessVerticalSpace

    @property
    def verticalAlignment(self) -> str:
        return self.__verticalAlignment

    @verticalAlignment.setter
    def verticalAlignment(self, verticalAlignment: str):
        self.__verticalAlignment = verticalAlignment

    @property
    def horizontalAlignment(self) -> str:
        return self.__horizontalAlignment

    @horizontalAlignment.setter
    def horizontalAlignment(self, horizontalAlignment: str):
        self.__horizontalAlignment = horizontalAlignment

    @property
    def verticalSpan(self) -> int:
        return self.__verticalSpan

    @verticalSpan.setter
    def verticalSpan(self, verticalSpan: int):
        self.__verticalSpan = verticalSpan

    @property
    def horizontalIndent(self) -> int:
        return self.__horizontalIndent

    @horizontalIndent.setter
    def horizontalIndent(self, horizontalIndent: int):
        self.__horizontalIndent = horizontalIndent

    @property
    def horizontalSpan(self) -> int:
        return self.__horizontalSpan

    @horizontalSpan.setter
    def horizontalSpan(self, horizontalSpan: int):
        self.__horizontalSpan = horizontalSpan

    @property
    def gmf_all_gmfgraph_GridLayoutData(self):
        return self.__gmf_all_gmfgraph_GridLayoutData

    @gmf_all_gmfgraph_GridLayoutData.setter
    def gmf_all_gmfgraph_GridLayoutData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_gmfgraph_GridLayoutData__gmf_all_gmfgraph_GridLayoutData", None)
        self.__gmf_all_gmfgraph_GridLayoutData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Dimension283"):
                opp_val = getattr(old_value, "Dimension283", None)
                if opp_val == self:
                    setattr(old_value, "Dimension283", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Dimension283"):
                opp_val = getattr(value, "Dimension283", None)
                setattr(value, "Dimension283", self)

class gmfgraph_LayoutData:

    pass
class gmf_all_gmfgraph_LayoutData(ABC):

    pass
class gmfgraph_Border:

    pass
class gmf_all_gmfgraph_Border(ABC):

    pass
class gmfgraph_CustomFigure:

    pass
class gmf_all_gmfgraph_Insets:

    def __init__(self, top: int, left: int, bottom: int, right: int):
        self.top = top
        self.left = left
        self.bottom = bottom
        self.right = right
        
    @property
    def left(self) -> int:
        return self.__left

    @left.setter
    def left(self, left: int):
        self.__left = left

    @property
    def bottom(self) -> int:
        return self.__bottom

    @bottom.setter
    def bottom(self, bottom: int):
        self.__bottom = bottom

    @property
    def right(self) -> int:
        return self.__right

    @right.setter
    def right(self, right: int):
        self.__right = right

    @property
    def top(self) -> int:
        return self.__top

    @top.setter
    def top(self, top: int):
        self.__top = top

class gmf_all_gmfgraph_Dimension:

    def __init__(self, dx: int, dy: int):
        self.dx = dx
        self.dy = dy
        
    @property
    def dx(self) -> int:
        return self.__dx

    @dx.setter
    def dx(self, dx: int):
        self.__dx = dx

    @property
    def dy(self) -> int:
        return self.__dy

    @dy.setter
    def dy(self, dy: int):
        self.__dy = dy

class gmf_all_gmfgraph_Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        
    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x

    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y

class gmf_all_gmfgraph_Font(ABC):

    pass
class gmf_all_gmfgraph_Color(ABC):

    pass
class FigureAccessor:

    pass
class gmfgraph_CustomClass:

    pass
class gmf_all_gmfgraph_CustomLayout(gmfgraph_Layout, gmfgraph_CustomClass):

    pass
class gmf_all_gmfgraph_CustomBorder(gmfgraph_Border, gmfgraph_CustomClass):

    pass
class gmf_all_gmfgraph_CustomLayoutData(gmfgraph_LayoutData, gmfgraph_CustomClass):

    pass
class gmfgraph_RealFigure:

    pass
class gmf_all_gmfgraph_CustomFigure(gmfgraph_RealFigure, gmfgraph_CustomClass):

    pass
class gmf_all_gmfgraph_FigureAccessor:

    def __init__(self, accessor: str, gmf_all_gmfgraph_FigureAccessor: "RealFigure" = None):
        self.accessor = accessor
        self.gmf_all_gmfgraph_FigureAccessor = gmf_all_gmfgraph_FigureAccessor
        
    @property
    def accessor(self) -> str:
        return self.__accessor

    @accessor.setter
    def accessor(self, accessor: str):
        self.__accessor = accessor

    @property
    def gmf_all_gmfgraph_FigureAccessor(self):
        return self.__gmf_all_gmfgraph_FigureAccessor

    @gmf_all_gmfgraph_FigureAccessor.setter
    def gmf_all_gmfgraph_FigureAccessor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_gmfgraph_FigureAccessor__gmf_all_gmfgraph_FigureAccessor", None)
        self.__gmf_all_gmfgraph_FigureAccessor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RealFigure267"):
                opp_val = getattr(old_value, "RealFigure267", None)
                if opp_val == self:
                    setattr(old_value, "RealFigure267", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RealFigure267"):
                opp_val = getattr(value, "RealFigure267", None)
                setattr(value, "RealFigure267", self)

class gmf_all_gmfgraph_CustomAttribute:

    def __init__(self, name: str, value: str, directAccess: bool, multiStatementValue: bool):
        self.name = name
        self.value = value
        self.directAccess = directAccess
        self.multiStatementValue = multiStatementValue
        
    @property
    def directAccess(self) -> bool:
        return self.__directAccess

    @directAccess.setter
    def directAccess(self, directAccess: bool):
        self.__directAccess = directAccess

    @property
    def multiStatementValue(self) -> bool:
        return self.__multiStatementValue

    @multiStatementValue.setter
    def multiStatementValue(self, multiStatementValue: bool):
        self.__multiStatementValue = multiStatementValue

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class CustomAttributeOwner:

    pass
class gmf_all_gmfgraph_CustomClass(CustomAttributeOwner):

    def __init__(self, qualifiedClassName: str):
        self.qualifiedClassName = qualifiedClassName
        
    @property
    def qualifiedClassName(self) -> str:
        return self.__qualifiedClassName

    @qualifiedClassName.setter
    def qualifiedClassName(self, qualifiedClassName: str):
        self.__qualifiedClassName = qualifiedClassName

class CustomAttribute:

    pass
class gmf_all_gmfgraph_CustomAttributeOwner(ABC):

    pass
class gmfgraph_Polygon:

    pass
class gmfgraph_DecorationFigure:

    pass
class gmf_all_gmfgraph_PolygonDecoration(gmfgraph_Polygon, gmfgraph_DecorationFigure):

    pass
class gmf_all_gmfgraph_CustomDecoration(gmfgraph_DecorationFigure, gmfgraph_CustomFigure):

    pass
class DecorationFigure:

    pass
class gmfgraph_ConnectionFigure:

    pass
class gmf_all_gmfgraph_CustomConnection(gmfgraph_ConnectionFigure, gmfgraph_CustomFigure):

    pass
class gmfgraph_Polyline:

    pass
class gmf_all_gmfgraph_PolylineDecoration(gmfgraph_DecorationFigure, gmfgraph_Polyline):

    pass
class gmf_all_gmfgraph_PolylineConnection(gmfgraph_ConnectionFigure, gmfgraph_Polyline):

    pass
class Polygon:

    pass
class gmf_all_gmfgraph_ScalablePolygon(Polygon):

    pass
class Polyline:

    pass
class gmf_all_gmfgraph_Polygon(Polyline):

    pass
class Shape:

    pass
class gmf_all_gmfgraph_Polyline(Shape):

    pass
class gmf_all_gmfgraph_Ellipse(Shape):

    pass
class gmf_all_gmfgraph_RoundedRectangle(Shape):

    def __init__(self, cornerWidth: int, cornerHeight: int):
        self.cornerWidth = cornerWidth
        self.cornerHeight = cornerHeight
        
    @property
    def cornerHeight(self) -> int:
        return self.__cornerHeight

    @cornerHeight.setter
    def cornerHeight(self, cornerHeight: int):
        self.__cornerHeight = cornerHeight

    @property
    def cornerWidth(self) -> int:
        return self.__cornerWidth

    @cornerWidth.setter
    def cornerWidth(self, cornerWidth: int):
        self.__cornerWidth = cornerWidth

class gmf_all_gmfgraph_Rectangle(Shape):

    pass
class Figure:

    pass
class gmf_all_gmfgraph_AbstractFigure(Figure):

    pass
class AbstractFigure:

    pass
class gmf_all_gmfgraph_FigureRef(AbstractFigure):

    pass
class gmfgraph_CustomAttributeOwner:

    pass
class gmfgraph_PinOwner:

    pass
class gmfgraph_AbstractFigure:

    pass
class gmf_all_gmfgraph_RealFigure(gmfgraph_CustomAttributeOwner, gmfgraph_PinOwner, gmfgraph_AbstractFigure):

    def __init__(self, name: str, gmf_all_gmfgraph_RealFigure: set["Figure"] = None):
        self.name = name
        self.gmf_all_gmfgraph_RealFigure = gmf_all_gmfgraph_RealFigure if gmf_all_gmfgraph_RealFigure is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def gmf_all_gmfgraph_RealFigure(self):
        return self.__gmf_all_gmfgraph_RealFigure

    @gmf_all_gmfgraph_RealFigure.setter
    def gmf_all_gmfgraph_RealFigure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_gmfgraph_RealFigure__gmf_all_gmfgraph_RealFigure", None)
        self.__gmf_all_gmfgraph_RealFigure = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Figure254"):
                    opp_val = getattr(item, "Figure254", None)
                    
                    if opp_val == self:
                        setattr(item, "Figure254", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Figure254"):
                    opp_val = getattr(item, "Figure254", None)
                    
                    setattr(item, "Figure254", self)
                    

class gmf_all_gmfgraph_ChildAccess:

    def __init__(self, accessor: str, FigureDescriptor249: "FigureDescriptor" = None, gmf_all_gmfgraph_ChildAccess: "Figure" = None):
        self.accessor = accessor
        self.FigureDescriptor249 = FigureDescriptor249
        self.gmf_all_gmfgraph_ChildAccess = gmf_all_gmfgraph_ChildAccess
        
    @property
    def accessor(self) -> str:
        return self.__accessor

    @accessor.setter
    def accessor(self, accessor: str):
        self.__accessor = accessor

    @property
    def gmf_all_gmfgraph_ChildAccess(self):
        return self.__gmf_all_gmfgraph_ChildAccess

    @gmf_all_gmfgraph_ChildAccess.setter
    def gmf_all_gmfgraph_ChildAccess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_gmfgraph_ChildAccess__gmf_all_gmfgraph_ChildAccess", None)
        self.__gmf_all_gmfgraph_ChildAccess = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Figure252"):
                opp_val = getattr(old_value, "Figure252", None)
                if opp_val == self:
                    setattr(old_value, "Figure252", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Figure252"):
                opp_val = getattr(value, "Figure252", None)
                setattr(value, "Figure252", self)

    @property
    def FigureDescriptor249(self):
        return self.__FigureDescriptor249

    @FigureDescriptor249.setter
    def FigureDescriptor249(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_gmfgraph_ChildAccess__FigureDescriptor249", None)
        self.__FigureDescriptor249 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph250"):
                opp_val = getattr(old_value, "gmfgraph250", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph250", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph250"):
                opp_val = getattr(value, "gmfgraph250", None)
                setattr(value, "gmfgraph250", self)

class Point:

    pass
class Insets:

    pass
class Font:

    pass
class gmf_all_gmfgraph_BasicFont(Font):

    def __init__(self, faceName: str, height: int, style: str, Font: "gmf_all_gmfgraph_Figure"):
        self.faceName = faceName
        self.height = height
        self.style = style
        
    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height

    @property
    def faceName(self) -> str:
        return self.__faceName

    @faceName.setter
    def faceName(self, faceName: str):
        self.__faceName = faceName

class Color:

    pass
class gmf_all_gmfgraph_ConstantColor(Color):

    def __init__(self, value: str, Color: "gmf_all_gmfgraph_Figure", Color223: "gmf_all_gmfgraph_Figure", Color272: "gmf_all_gmfgraph_LineBorder"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class gmf_all_gmfgraph_RGBColor(Color):

    def __init__(self, red: int, green: int, blue: int, Color: "gmf_all_gmfgraph_Figure", Color223: "gmf_all_gmfgraph_Figure", Color272: "gmf_all_gmfgraph_LineBorder"):
        self.red = red
        self.green = green
        self.blue = blue
        
    @property
    def green(self) -> int:
        return self.__green

    @green.setter
    def green(self, green: int):
        self.__green = green

    @property
    def red(self) -> int:
        return self.__red

    @red.setter
    def red(self, red: int):
        self.__red = red

    @property
    def blue(self) -> int:
        return self.__blue

    @blue.setter
    def blue(self, blue: int):
        self.__blue = blue

class Layoutable:

    pass
class gmf_all_gmfgraph_Figure(Layoutable):

    pass
class Dimension:

    pass
class RealFigure:

    pass
class gmf_all_gmfgraph_InvisibleRectangle(RealFigure):

    pass
class gmf_all_gmfgraph_ConnectionFigure(RealFigure):

    pass
class gmf_all_gmfgraph_Label(RealFigure):

    def __init__(self, text: str, RealFigure256: "gmf_all_gmfgraph_FigureRef", RealFigure267: "gmf_all_gmfgraph_FigureAccessor", RealFigure: "gmf_all_gmfgraph_FigureGallery"):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class gmf_all_gmfgraph_DecorationFigure(RealFigure):

    pass
class gmf_all_gmfgraph_LabeledContainer(RealFigure):

    pass
class gmf_all_gmfgraph_SVGFigure(RealFigure):

    def __init__(self, documentURI: str, noCanvasWidth: bool, noCanvasHeight: bool, gmf_all_gmfgraph_SVGFigure: set["SVGProperty"] = None, gmf_all_gmfgraph_SVGFigure304: "Rectangle2D" = None, RealFigure256: "gmf_all_gmfgraph_FigureRef", RealFigure267: "gmf_all_gmfgraph_FigureAccessor", RealFigure: "gmf_all_gmfgraph_FigureGallery"):
        self.documentURI = documentURI
        self.noCanvasWidth = noCanvasWidth
        self.noCanvasHeight = noCanvasHeight
        self.gmf_all_gmfgraph_SVGFigure = gmf_all_gmfgraph_SVGFigure if gmf_all_gmfgraph_SVGFigure is not None else set()
        self.gmf_all_gmfgraph_SVGFigure304 = gmf_all_gmfgraph_SVGFigure304
        
    @property
    def noCanvasHeight(self) -> bool:
        return self.__noCanvasHeight

    @noCanvasHeight.setter
    def noCanvasHeight(self, noCanvasHeight: bool):
        self.__noCanvasHeight = noCanvasHeight

    @property
    def noCanvasWidth(self) -> bool:
        return self.__noCanvasWidth

    @noCanvasWidth.setter
    def noCanvasWidth(self, noCanvasWidth: bool):
        self.__noCanvasWidth = noCanvasWidth

    @property
    def documentURI(self) -> str:
        return self.__documentURI

    @documentURI.setter
    def documentURI(self, documentURI: str):
        self.__documentURI = documentURI

    @property
    def gmf_all_gmfgraph_SVGFigure(self):
        return self.__gmf_all_gmfgraph_SVGFigure

    @gmf_all_gmfgraph_SVGFigure.setter
    def gmf_all_gmfgraph_SVGFigure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_gmfgraph_SVGFigure__gmf_all_gmfgraph_SVGFigure", None)
        self.__gmf_all_gmfgraph_SVGFigure = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SVGProperty"):
                    opp_val = getattr(item, "SVGProperty", None)
                    
                    if opp_val == self:
                        setattr(item, "SVGProperty", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SVGProperty"):
                    opp_val = getattr(item, "SVGProperty", None)
                    
                    setattr(item, "SVGProperty", self)
                    

    @property
    def gmf_all_gmfgraph_SVGFigure304(self):
        return self.__gmf_all_gmfgraph_SVGFigure304

    @gmf_all_gmfgraph_SVGFigure304.setter
    def gmf_all_gmfgraph_SVGFigure304(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_gmfgraph_SVGFigure__gmf_all_gmfgraph_SVGFigure304", None)
        self.__gmf_all_gmfgraph_SVGFigure304 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Rectangle2D"):
                opp_val = getattr(old_value, "Rectangle2D", None)
                if opp_val == self:
                    setattr(old_value, "Rectangle2D", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Rectangle2D"):
                opp_val = getattr(value, "Rectangle2D", None)
                setattr(value, "Rectangle2D", self)

class gmf_all_gmfgraph_VerticalLabel(RealFigure):

    def __init__(self, text: str, RealFigure256: "gmf_all_gmfgraph_FigureRef", RealFigure267: "gmf_all_gmfgraph_FigureAccessor", RealFigure: "gmf_all_gmfgraph_FigureGallery"):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class gmf_all_gmfgraph_Shape(RealFigure):

    def __init__(self, outline: bool, fill: bool, lineWidth: int, lineKind: str, xorFill: bool, xorOutline: bool, gmf_all_gmfgraph_Shape: set["Figure"] = None, RealFigure256: "gmf_all_gmfgraph_FigureRef", RealFigure267: "gmf_all_gmfgraph_FigureAccessor", RealFigure: "gmf_all_gmfgraph_FigureGallery"):
        self.outline = outline
        self.fill = fill
        self.lineWidth = lineWidth
        self.lineKind = lineKind
        self.xorFill = xorFill
        self.xorOutline = xorOutline
        self.gmf_all_gmfgraph_Shape = gmf_all_gmfgraph_Shape if gmf_all_gmfgraph_Shape is not None else set()
        
    @property
    def lineKind(self) -> str:
        return self.__lineKind

    @lineKind.setter
    def lineKind(self, lineKind: str):
        self.__lineKind = lineKind

    @property
    def lineWidth(self) -> int:
        return self.__lineWidth

    @lineWidth.setter
    def lineWidth(self, lineWidth: int):
        self.__lineWidth = lineWidth

    @property
    def outline(self) -> bool:
        return self.__outline

    @outline.setter
    def outline(self, outline: bool):
        self.__outline = outline

    @property
    def xorOutline(self) -> bool:
        return self.__xorOutline

    @xorOutline.setter
    def xorOutline(self, xorOutline: bool):
        self.__xorOutline = xorOutline

    @property
    def xorFill(self) -> bool:
        return self.__xorFill

    @xorFill.setter
    def xorFill(self, xorFill: bool):
        self.__xorFill = xorFill

    @property
    def fill(self) -> bool:
        return self.__fill

    @fill.setter
    def fill(self, fill: bool):
        self.__fill = fill

    @property
    def gmf_all_gmfgraph_Shape(self):
        return self.__gmf_all_gmfgraph_Shape

    @gmf_all_gmfgraph_Shape.setter
    def gmf_all_gmfgraph_Shape(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_gmfgraph_Shape__gmf_all_gmfgraph_Shape", None)
        self.__gmf_all_gmfgraph_Shape = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Figure258"):
                    opp_val = getattr(item, "Figure258", None)
                    
                    if opp_val == self:
                        setattr(item, "Figure258", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Figure258"):
                    opp_val = getattr(item, "Figure258", None)
                    
                    setattr(item, "Figure258", self)
                    

class gmf_all_gmfgraph_VisualFacet(ABC):

    pass
class ChildAccess:

    pass
class AbstractNode:

    pass
class gmf_all_gmfgraph_Node(AbstractNode):

    def __init__(self, resizeConstraint: str, affixedParentSide: str, gmf_all_gmfgraph_Node: "ChildAccess" = None):
        self.resizeConstraint = resizeConstraint
        self.affixedParentSide = affixedParentSide
        self.gmf_all_gmfgraph_Node = gmf_all_gmfgraph_Node
        
    @property
    def affixedParentSide(self) -> str:
        return self.__affixedParentSide

    @affixedParentSide.setter
    def affixedParentSide(self, affixedParentSide: str):
        self.__affixedParentSide = affixedParentSide

    @property
    def resizeConstraint(self) -> str:
        return self.__resizeConstraint

    @resizeConstraint.setter
    def resizeConstraint(self, resizeConstraint: str):
        self.__resizeConstraint = resizeConstraint

    @property
    def gmf_all_gmfgraph_Node(self):
        return self.__gmf_all_gmfgraph_Node

    @gmf_all_gmfgraph_Node.setter
    def gmf_all_gmfgraph_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_gmfgraph_Node__gmf_all_gmfgraph_Node", None)
        self.__gmf_all_gmfgraph_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ChildAccess"):
                opp_val = getattr(old_value, "ChildAccess", None)
                if opp_val == self:
                    setattr(old_value, "ChildAccess", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ChildAccess"):
                opp_val = getattr(value, "ChildAccess", None)
                setattr(value, "ChildAccess", self)

class DiagramElement:

    pass
class gmf_all_gmfgraph_Compartment(DiagramElement):

    def __init__(self, collapsible: bool, needsTitle: bool, gmf_all_gmfgraph_Compartment: "ChildAccess" = None):
        self.collapsible = collapsible
        self.needsTitle = needsTitle
        self.gmf_all_gmfgraph_Compartment = gmf_all_gmfgraph_Compartment
        
    @property
    def collapsible(self) -> bool:
        return self.__collapsible

    @collapsible.setter
    def collapsible(self, collapsible: bool):
        self.__collapsible = collapsible

    @property
    def needsTitle(self) -> bool:
        return self.__needsTitle

    @needsTitle.setter
    def needsTitle(self, needsTitle: bool):
        self.__needsTitle = needsTitle

    @property
    def gmf_all_gmfgraph_Compartment(self):
        return self.__gmf_all_gmfgraph_Compartment

    @gmf_all_gmfgraph_Compartment.setter
    def gmf_all_gmfgraph_Compartment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_gmfgraph_Compartment__gmf_all_gmfgraph_Compartment", None)
        self.__gmf_all_gmfgraph_Compartment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ChildAccess210"):
                opp_val = getattr(old_value, "ChildAccess210", None)
                if opp_val == self:
                    setattr(old_value, "ChildAccess210", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ChildAccess210"):
                opp_val = getattr(value, "ChildAccess210", None)
                setattr(value, "ChildAccess210", self)

class gmf_all_gmfgraph_Connection(DiagramElement):

    pass
class gmf_all_gmfgraph_AbstractNode(DiagramElement):

    pass
class VisualFacet:

    pass
class gmf_all_gmfgraph_GeneralFacet(VisualFacet):

    def __init__(self, data: str, identifier: str, VisualFacet: "gmf_all_gmfgraph_DiagramElement"):
        self.data = data
        self.identifier = identifier
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def data(self) -> str:
        return self.__data

    @data.setter
    def data(self, data: str):
        self.__data = data

class gmf_all_gmfgraph_DefaultSizeFacet(VisualFacet):

    pass
class gmf_all_gmfgraph_LabelOffsetFacet(VisualFacet):

    def __init__(self, x: int, y: int, VisualFacet: "gmf_all_gmfgraph_DiagramElement"):
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

class gmf_all_gmfgraph_GradientFacet(VisualFacet):

    def __init__(self, direction: str, VisualFacet: "gmf_all_gmfgraph_DiagramElement"):
        self.direction = direction
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

class gmf_all_gmfgraph_AlignmentFacet(VisualFacet):

    def __init__(self, alignment: str, VisualFacet: "gmf_all_gmfgraph_DiagramElement"):
        self.alignment = alignment
        
    @property
    def alignment(self) -> str:
        return self.__alignment

    @alignment.setter
    def alignment(self, alignment: str):
        self.__alignment = alignment

class gmf_all_gmfgraph_Identity(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Layout:

    pass
class gmf_all_gmfgraph_FlowLayout(Layout):

    def __init__(self, forceSingleLine: bool, majorAlignment: str, minorAlignment: str, majorSpacing: int, minorSpacing: int, vertical: bool, matchMinorSize: bool, Layout: "gmf_all_gmfgraph_FigureGallery", Layout289: "gmf_all_gmfgraph_LayoutRef", Layout287: "gmf_all_gmfgraph_Layoutable"):
        self.forceSingleLine = forceSingleLine
        self.majorAlignment = majorAlignment
        self.minorAlignment = minorAlignment
        self.majorSpacing = majorSpacing
        self.minorSpacing = minorSpacing
        self.vertical = vertical
        self.matchMinorSize = matchMinorSize
        
    @property
    def minorAlignment(self) -> str:
        return self.__minorAlignment

    @minorAlignment.setter
    def minorAlignment(self, minorAlignment: str):
        self.__minorAlignment = minorAlignment

    @property
    def majorSpacing(self) -> int:
        return self.__majorSpacing

    @majorSpacing.setter
    def majorSpacing(self, majorSpacing: int):
        self.__majorSpacing = majorSpacing

    @property
    def forceSingleLine(self) -> bool:
        return self.__forceSingleLine

    @forceSingleLine.setter
    def forceSingleLine(self, forceSingleLine: bool):
        self.__forceSingleLine = forceSingleLine

    @property
    def majorAlignment(self) -> str:
        return self.__majorAlignment

    @majorAlignment.setter
    def majorAlignment(self, majorAlignment: str):
        self.__majorAlignment = majorAlignment

    @property
    def minorSpacing(self) -> int:
        return self.__minorSpacing

    @minorSpacing.setter
    def minorSpacing(self, minorSpacing: int):
        self.__minorSpacing = minorSpacing

    @property
    def matchMinorSize(self) -> bool:
        return self.__matchMinorSize

    @matchMinorSize.setter
    def matchMinorSize(self, matchMinorSize: bool):
        self.__matchMinorSize = matchMinorSize

    @property
    def vertical(self) -> bool:
        return self.__vertical

    @vertical.setter
    def vertical(self, vertical: bool):
        self.__vertical = vertical

class gmf_all_gmfgraph_BorderLayout(Layout):

    pass
class gmf_all_gmfgraph_XYLayout(Layout):

    pass
class gmf_all_gmfgraph_LayoutRef(Layout):

    pass
class gmf_all_gmfgraph_GridLayout(Layout):

    def __init__(self, numColumns: int, equalWidth: bool, gmf_all_gmfgraph_GridLayout: "Dimension" = None, gmf_all_gmfgraph_GridLayout293: "Dimension" = None, Layout: "gmf_all_gmfgraph_FigureGallery", Layout289: "gmf_all_gmfgraph_LayoutRef", Layout287: "gmf_all_gmfgraph_Layoutable"):
        self.numColumns = numColumns
        self.equalWidth = equalWidth
        self.gmf_all_gmfgraph_GridLayout = gmf_all_gmfgraph_GridLayout
        self.gmf_all_gmfgraph_GridLayout293 = gmf_all_gmfgraph_GridLayout293
        
    @property
    def numColumns(self) -> int:
        return self.__numColumns

    @numColumns.setter
    def numColumns(self, numColumns: int):
        self.__numColumns = numColumns

    @property
    def equalWidth(self) -> bool:
        return self.__equalWidth

    @equalWidth.setter
    def equalWidth(self, equalWidth: bool):
        self.__equalWidth = equalWidth

    @property
    def gmf_all_gmfgraph_GridLayout293(self):
        return self.__gmf_all_gmfgraph_GridLayout293

    @gmf_all_gmfgraph_GridLayout293.setter
    def gmf_all_gmfgraph_GridLayout293(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_gmfgraph_GridLayout__gmf_all_gmfgraph_GridLayout293", None)
        self.__gmf_all_gmfgraph_GridLayout293 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Dimension294"):
                opp_val = getattr(old_value, "Dimension294", None)
                if opp_val == self:
                    setattr(old_value, "Dimension294", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Dimension294"):
                opp_val = getattr(value, "Dimension294", None)
                setattr(value, "Dimension294", self)

    @property
    def gmf_all_gmfgraph_GridLayout(self):
        return self.__gmf_all_gmfgraph_GridLayout

    @gmf_all_gmfgraph_GridLayout.setter
    def gmf_all_gmfgraph_GridLayout(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_gmfgraph_GridLayout__gmf_all_gmfgraph_GridLayout", None)
        self.__gmf_all_gmfgraph_GridLayout = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Dimension291"):
                opp_val = getattr(old_value, "Dimension291", None)
                if opp_val == self:
                    setattr(old_value, "Dimension291", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Dimension291"):
                opp_val = getattr(value, "Dimension291", None)
                setattr(value, "Dimension291", self)

class gmf_all_gmfgraph_CenterLayout(Layout):

    pass
class gmf_all_gmfgraph_StackLayout(Layout):

    pass
class Border:

    pass
class gmf_all_gmfgraph_LineBorder(Border):

    def __init__(self, width: int, gmf_all_gmfgraph_LineBorder: "Color" = None, Border279: "gmf_all_gmfgraph_CompoundBorder", Border239: "gmf_all_gmfgraph_Figure", Border270: "gmf_all_gmfgraph_BorderRef", Border: "gmf_all_gmfgraph_FigureGallery", Border276: "gmf_all_gmfgraph_CompoundBorder"):
        self.width = width
        self.gmf_all_gmfgraph_LineBorder = gmf_all_gmfgraph_LineBorder
        
    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width

    @property
    def gmf_all_gmfgraph_LineBorder(self):
        return self.__gmf_all_gmfgraph_LineBorder

    @gmf_all_gmfgraph_LineBorder.setter
    def gmf_all_gmfgraph_LineBorder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_gmfgraph_LineBorder__gmf_all_gmfgraph_LineBorder", None)
        self.__gmf_all_gmfgraph_LineBorder = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Color272"):
                opp_val = getattr(old_value, "Color272", None)
                if opp_val == self:
                    setattr(old_value, "Color272", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Color272"):
                opp_val = getattr(value, "Color272", None)
                setattr(value, "Color272", self)

class gmf_all_gmfgraph_CompoundBorder(Border):

    pass
class gmf_all_gmfgraph_MarginBorder(Border):

    pass
class gmf_all_gmfgraph_BorderRef(Border):

    pass
class FigureDescriptor:

    pass
class tooldef_ContributionItem:

    pass
class FigureGallery:

    pass
class Identity:

    pass
class gmf_all_gmfgraph_DiagramElement(Identity):

    pass
class gmf_all_gmfgraph_FigureGallery(Identity):

    def __init__(self, implementationBundle: str, gmf_all_gmfgraph_FigureGallery199: set["FigureDescriptor"] = None, gmf_all_gmfgraph_FigureGallery201: set["Border"] = None, gmf_all_gmfgraph_FigureGallery203: set["Layout"] = None, gmf_all_gmfgraph_FigureGallery: set["RealFigure"] = None):
        self.implementationBundle = implementationBundle
        self.gmf_all_gmfgraph_FigureGallery199 = gmf_all_gmfgraph_FigureGallery199 if gmf_all_gmfgraph_FigureGallery199 is not None else set()
        self.gmf_all_gmfgraph_FigureGallery201 = gmf_all_gmfgraph_FigureGallery201 if gmf_all_gmfgraph_FigureGallery201 is not None else set()
        self.gmf_all_gmfgraph_FigureGallery203 = gmf_all_gmfgraph_FigureGallery203 if gmf_all_gmfgraph_FigureGallery203 is not None else set()
        self.gmf_all_gmfgraph_FigureGallery = gmf_all_gmfgraph_FigureGallery if gmf_all_gmfgraph_FigureGallery is not None else set()
        
    @property
    def implementationBundle(self) -> str:
        return self.__implementationBundle

    @implementationBundle.setter
    def implementationBundle(self, implementationBundle: str):
        self.__implementationBundle = implementationBundle

    @property
    def gmf_all_gmfgraph_FigureGallery(self):
        return self.__gmf_all_gmfgraph_FigureGallery

    @gmf_all_gmfgraph_FigureGallery.setter
    def gmf_all_gmfgraph_FigureGallery(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_gmfgraph_FigureGallery__gmf_all_gmfgraph_FigureGallery", None)
        self.__gmf_all_gmfgraph_FigureGallery = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RealFigure"):
                    opp_val = getattr(item, "RealFigure", None)
                    
                    if opp_val == self:
                        setattr(item, "RealFigure", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RealFigure"):
                    opp_val = getattr(item, "RealFigure", None)
                    
                    setattr(item, "RealFigure", self)
                    

    @property
    def gmf_all_gmfgraph_FigureGallery203(self):
        return self.__gmf_all_gmfgraph_FigureGallery203

    @gmf_all_gmfgraph_FigureGallery203.setter
    def gmf_all_gmfgraph_FigureGallery203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_gmfgraph_FigureGallery__gmf_all_gmfgraph_FigureGallery203", None)
        self.__gmf_all_gmfgraph_FigureGallery203 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Layout"):
                    opp_val = getattr(item, "Layout", None)
                    
                    if opp_val == self:
                        setattr(item, "Layout", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Layout"):
                    opp_val = getattr(item, "Layout", None)
                    
                    setattr(item, "Layout", self)
                    

    @property
    def gmf_all_gmfgraph_FigureGallery199(self):
        return self.__gmf_all_gmfgraph_FigureGallery199

    @gmf_all_gmfgraph_FigureGallery199.setter
    def gmf_all_gmfgraph_FigureGallery199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_gmfgraph_FigureGallery__gmf_all_gmfgraph_FigureGallery199", None)
        self.__gmf_all_gmfgraph_FigureGallery199 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FigureDescriptor"):
                    opp_val = getattr(item, "FigureDescriptor", None)
                    
                    if opp_val == self:
                        setattr(item, "FigureDescriptor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FigureDescriptor"):
                    opp_val = getattr(item, "FigureDescriptor", None)
                    
                    setattr(item, "FigureDescriptor", self)
                    

    @property
    def gmf_all_gmfgraph_FigureGallery201(self):
        return self.__gmf_all_gmfgraph_FigureGallery201

    @gmf_all_gmfgraph_FigureGallery201.setter
    def gmf_all_gmfgraph_FigureGallery201(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_gmfgraph_FigureGallery__gmf_all_gmfgraph_FigureGallery201", None)
        self.__gmf_all_gmfgraph_FigureGallery201 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Border"):
                    opp_val = getattr(item, "Border", None)
                    
                    if opp_val == self:
                        setattr(item, "Border", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Border"):
                    opp_val = getattr(item, "Border", None)
                    
                    setattr(item, "Border", self)
                    

class gmf_all_gmfgraph_Pin(Identity):

    def __init__(self):
        
    def getOperationType(self) -> str:
        # TODO: Implement getOperationType method
        pass

    def getOperationName(self) -> str:
        # TODO: Implement getOperationName method
        pass

class gmf_all_gmfgraph_FigureDescriptor(Identity):

    pass
class gmf_all_gmfgraph_Canvas(Identity):

    pass
class gmf_all_tooldef_StyleSelector(ABC):

    def __init__(self):
        
    def isOk(self, style: str) -> bool:
        # TODO: Implement isOk method
        pass

class gmf_all_tooldef_Image(ABC):

    pass
class ToolContainer:

    pass
class gmf_all_tooldef_ToolGroup(ToolContainer):

    def __init__(self, collapsible: bool, stack: bool, gmf_all_tooldef_ToolGroup: "AbstractTool" = None):
        self.collapsible = collapsible
        self.stack = stack
        self.gmf_all_tooldef_ToolGroup = gmf_all_tooldef_ToolGroup
        
    @property
    def collapsible(self) -> bool:
        return self.__collapsible

    @collapsible.setter
    def collapsible(self, collapsible: bool):
        self.__collapsible = collapsible

    @property
    def stack(self) -> bool:
        return self.__stack

    @stack.setter
    def stack(self, stack: bool):
        self.__stack = stack

    @property
    def gmf_all_tooldef_ToolGroup(self):
        return self.__gmf_all_tooldef_ToolGroup

    @gmf_all_tooldef_ToolGroup.setter
    def gmf_all_tooldef_ToolGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_tooldef_ToolGroup__gmf_all_tooldef_ToolGroup", None)
        self.__gmf_all_tooldef_ToolGroup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractTool174"):
                opp_val = getattr(old_value, "AbstractTool174", None)
                if opp_val == self:
                    setattr(old_value, "AbstractTool174", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractTool174"):
                opp_val = getattr(value, "AbstractTool174", None)
                setattr(value, "AbstractTool174", self)

class ContributionItem:

    pass
class gmf_all_tooldef_MenuAction(ContributionItem):

    def __init__(self, kind: str, hotKey: str):
        self.kind = kind
        self.hotKey = hotKey
        
    @property
    def hotKey(self) -> str:
        return self.__hotKey

    @hotKey.setter
    def hotKey(self, hotKey: str):
        self.__hotKey = hotKey

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

class tooldef_PredefinedItem:

    pass
class tooldef_Menu:

    pass
class gmf_all_tooldef_PopupMenu(tooldef_ContributionItem, tooldef_Menu):

    def __init__(self, iD: str):
        self.iD = iD
        
    @property
    def iD(self) -> str:
        return self.__iD

    @iD.setter
    def iD(self, iD: str):
        self.__iD = iD

class gmf_all_tooldef_PredefinedMenu(tooldef_Menu, tooldef_PredefinedItem):

    pass
class ItemBase:

    pass
class gmf_all_tooldef_ContributionItem(ItemBase):

    def __init__(self, title: str, gmf_all_tooldef_ContributionItem: "Image" = None, ItemBase: "gmf_all_tooldef_Menu", ItemBase181: "gmf_all_tooldef_ItemRef"):
        self.title = title
        self.gmf_all_tooldef_ContributionItem = gmf_all_tooldef_ContributionItem
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def gmf_all_tooldef_ContributionItem(self):
        return self.__gmf_all_tooldef_ContributionItem

    @gmf_all_tooldef_ContributionItem.setter
    def gmf_all_tooldef_ContributionItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_tooldef_ContributionItem__gmf_all_tooldef_ContributionItem", None)
        self.__gmf_all_tooldef_ContributionItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Image179"):
                opp_val = getattr(old_value, "Image179", None)
                if opp_val == self:
                    setattr(old_value, "Image179", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Image179"):
                opp_val = getattr(value, "Image179", None)
                setattr(value, "Image179", self)

class gmf_all_tooldef_Separator(ItemBase):

    def __init__(self, name: str, ItemBase: "gmf_all_tooldef_Menu", ItemBase181: "gmf_all_tooldef_ItemRef"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class gmf_all_tooldef_PredefinedItem(ItemBase):

    def __init__(self, identifier: str, ItemBase: "gmf_all_tooldef_Menu", ItemBase181: "gmf_all_tooldef_ItemRef"):
        self.identifier = identifier
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

class gmf_all_tooldef_ItemRef(ItemBase):

    pass
class gmf_all_tooldef_Menu(ABC):

    pass
class gmf_all_tooldef_ItemBase(ABC):

    pass
class gmf_all_tooldef_Palette(ToolContainer):

    pass
class Image:

    pass
class gmf_all_tooldef_BundleImage(Image):

    def __init__(self, path: str, bundle: str, Image179: "gmf_all_tooldef_ContributionItem", Image: "gmf_all_tooldef_AbstractTool", Image170: "gmf_all_tooldef_AbstractTool"):
        self.path = path
        self.bundle = bundle
        
    @property
    def bundle(self) -> str:
        return self.__bundle

    @bundle.setter
    def bundle(self, bundle: str):
        self.__bundle = bundle

    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

class gmf_all_tooldef_DefaultImage(Image):

    pass
class gmf_all_tooldef_AbstractTool(ABC):

    def __init__(self, title: str, description: str, gmf_all_tooldef_AbstractTool: "Image" = None, gmf_all_tooldef_AbstractTool169: "Image" = None):
        self.title = title
        self.description = description
        self.gmf_all_tooldef_AbstractTool = gmf_all_tooldef_AbstractTool
        self.gmf_all_tooldef_AbstractTool169 = gmf_all_tooldef_AbstractTool169
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def gmf_all_tooldef_AbstractTool(self):
        return self.__gmf_all_tooldef_AbstractTool

    @gmf_all_tooldef_AbstractTool.setter
    def gmf_all_tooldef_AbstractTool(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_tooldef_AbstractTool__gmf_all_tooldef_AbstractTool", None)
        self.__gmf_all_tooldef_AbstractTool = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Image"):
                opp_val = getattr(old_value, "Image", None)
                if opp_val == self:
                    setattr(old_value, "Image", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Image"):
                opp_val = getattr(value, "Image", None)
                setattr(value, "Image", self)

    @property
    def gmf_all_tooldef_AbstractTool169(self):
        return self.__gmf_all_tooldef_AbstractTool169

    @gmf_all_tooldef_AbstractTool169.setter
    def gmf_all_tooldef_AbstractTool169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_tooldef_AbstractTool__gmf_all_tooldef_AbstractTool169", None)
        self.__gmf_all_tooldef_AbstractTool169 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Image170"):
                opp_val = getattr(old_value, "Image170", None)
                if opp_val == self:
                    setattr(old_value, "Image170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Image170"):
                opp_val = getattr(value, "Image170", None)
                setattr(value, "Image170", self)

class Menu:

    pass
class gmf_all_tooldef_Toolbar(Menu):

    pass
class gmf_all_tooldef_ContextMenu(Menu):

    pass
class gmf_all_tooldef_MainMenu(Menu):

    def __init__(self, title: str, Menu: "gmf_all_tooldef_ToolRegistry"):
        self.title = title
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

class MenuAction:

    pass
class gmf_all_tooldef_ToolRegistry:

    pass
class Pin:

    pass
class gmf_all_gmfgraph_ColorPin(Pin):

    def __init__(self, backgroundNotForeground: bool, Pin: "gmf_all_mappings_VisualEffectMapping", Pin306: "gmf_all_gmfgraph_PinOwner"):
        self.backgroundNotForeground = backgroundNotForeground
        
    @property
    def backgroundNotForeground(self) -> bool:
        return self.__backgroundNotForeground

    @backgroundNotForeground.setter
    def backgroundNotForeground(self, backgroundNotForeground: bool):
        self.__backgroundNotForeground = backgroundNotForeground

class gmf_all_gmfgraph_CustomPin(Pin):

    def __init__(self, customOperationName: str, customOperationType: str, Pin: "gmf_all_mappings_VisualEffectMapping", Pin306: "gmf_all_gmfgraph_PinOwner"):
        self.customOperationName = customOperationName
        self.customOperationType = customOperationType
        
    @property
    def customOperationName(self) -> str:
        return self.__customOperationName

    @customOperationName.setter
    def customOperationName(self, customOperationName: str):
        self.__customOperationName = customOperationName

    @property
    def customOperationType(self) -> str:
        return self.__customOperationType

    @customOperationType.setter
    def customOperationType(self, customOperationType: str):
        self.__customOperationType = customOperationType

class gmf_all_gmfgraph_VisiblePin(Pin):

    pass
class gmf_all_mappings_VisualEffectMapping:

    def __init__(self, oclExpression: str, gmf_all_mappings_VisualEffectMapping: "Pin" = None, MappingEntry159: "MappingEntry" = None):
        self.oclExpression = oclExpression
        self.gmf_all_mappings_VisualEffectMapping = gmf_all_mappings_VisualEffectMapping
        self.MappingEntry159 = MappingEntry159
        
    @property
    def oclExpression(self) -> str:
        return self.__oclExpression

    @oclExpression.setter
    def oclExpression(self, oclExpression: str):
        self.__oclExpression = oclExpression

    @property
    def gmf_all_mappings_VisualEffectMapping(self):
        return self.__gmf_all_mappings_VisualEffectMapping

    @gmf_all_mappings_VisualEffectMapping.setter
    def gmf_all_mappings_VisualEffectMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_mappings_VisualEffectMapping__gmf_all_mappings_VisualEffectMapping", None)
        self.__gmf_all_mappings_VisualEffectMapping = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Pin"):
                opp_val = getattr(old_value, "Pin", None)
                if opp_val == self:
                    setattr(old_value, "Pin", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Pin"):
                opp_val = getattr(value, "Pin", None)
                setattr(value, "Pin", self)

    @property
    def MappingEntry159(self):
        return self.__MappingEntry159

    @MappingEntry159.setter
    def MappingEntry159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_mappings_VisualEffectMapping__MappingEntry159", None)
        self.__MappingEntry159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mappings160"):
                opp_val = getattr(old_value, "mappings160", None)
                if opp_val == self:
                    setattr(old_value, "mappings160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mappings160"):
                opp_val = getattr(value, "mappings160", None)
                setattr(value, "mappings160", self)

class gmf_all_mappings_Measurable(ABC):

    pass
class gmf_all_mappings_Auditable(ABC):

    pass
class Measurable:

    pass
class MetricRule:

    pass
class gmf_all_mappings_MetricContainer:

    pass
class mappings_Measurable:

    pass
class mappings_Auditable:

    pass
class gmf_all_mappings_NotationElementTarget(mappings_Measurable, mappings_Auditable):

    pass
class gmf_all_mappings_DiagramElementTarget(mappings_Measurable, mappings_Auditable):

    pass
class gmf_all_mappings_DomainElementTarget(mappings_Measurable, mappings_Auditable):

    pass
class Auditable:

    pass
class gmf_all_mappings_AuditedMetricTarget(Auditable):

    pass
class gmf_all_mappings_DomainAttributeTarget(Auditable):

    def __init__(self, nullAsError: bool, gmf_all_mappings_DomainAttributeTarget: "mappings_gmf_all_EAttribute" = None, Auditable: "gmf_all_mappings_AuditRule"):
        self.nullAsError = nullAsError
        self.gmf_all_mappings_DomainAttributeTarget = gmf_all_mappings_DomainAttributeTarget
        
    @property
    def nullAsError(self) -> bool:
        return self.__nullAsError

    @nullAsError.setter
    def nullAsError(self, nullAsError: bool):
        self.__nullAsError = nullAsError

    @property
    def gmf_all_mappings_DomainAttributeTarget(self):
        return self.__gmf_all_mappings_DomainAttributeTarget

    @gmf_all_mappings_DomainAttributeTarget.setter
    def gmf_all_mappings_DomainAttributeTarget(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_mappings_DomainAttributeTarget__gmf_all_mappings_DomainAttributeTarget", None)
        self.__gmf_all_mappings_DomainAttributeTarget = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mappings_gmf_all_EAttribute141"):
                opp_val = getattr(old_value, "mappings_gmf_all_EAttribute141", None)
                if opp_val == self:
                    setattr(old_value, "mappings_gmf_all_EAttribute141", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mappings_gmf_all_EAttribute141"):
                opp_val = getattr(value, "mappings_gmf_all_EAttribute141", None)
                setattr(value, "mappings_gmf_all_EAttribute141", self)

class RuleBase:

    pass
class gmf_all_mappings_MetricRule(RuleBase):

    def __init__(self, key: str, lowLimit: str, highLimit: str, gmf_all_mappings_MetricRule: "ValueExpression" = None, gmf_all_mappings_MetricRule151: "Measurable" = None, MetricContainer153: "MetricContainer" = None):
        self.key = key
        self.lowLimit = lowLimit
        self.highLimit = highLimit
        self.gmf_all_mappings_MetricRule = gmf_all_mappings_MetricRule
        self.gmf_all_mappings_MetricRule151 = gmf_all_mappings_MetricRule151
        self.MetricContainer153 = MetricContainer153
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def lowLimit(self) -> str:
        return self.__lowLimit

    @lowLimit.setter
    def lowLimit(self, lowLimit: str):
        self.__lowLimit = lowLimit

    @property
    def highLimit(self) -> str:
        return self.__highLimit

    @highLimit.setter
    def highLimit(self, highLimit: str):
        self.__highLimit = highLimit

    @property
    def gmf_all_mappings_MetricRule(self):
        return self.__gmf_all_mappings_MetricRule

    @gmf_all_mappings_MetricRule.setter
    def gmf_all_mappings_MetricRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_mappings_MetricRule__gmf_all_mappings_MetricRule", None)
        self.__gmf_all_mappings_MetricRule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ValueExpression149"):
                opp_val = getattr(old_value, "ValueExpression149", None)
                if opp_val == self:
                    setattr(old_value, "ValueExpression149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ValueExpression149"):
                opp_val = getattr(value, "ValueExpression149", None)
                setattr(value, "ValueExpression149", self)

    @property
    def MetricContainer153(self):
        return self.__MetricContainer153

    @MetricContainer153.setter
    def MetricContainer153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_mappings_MetricRule__MetricContainer153", None)
        self.__MetricContainer153 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mappings154"):
                opp_val = getattr(old_value, "mappings154", None)
                if opp_val == self:
                    setattr(old_value, "mappings154", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mappings154"):
                opp_val = getattr(value, "mappings154", None)
                setattr(value, "mappings154", self)

    @property
    def gmf_all_mappings_MetricRule151(self):
        return self.__gmf_all_mappings_MetricRule151

    @gmf_all_mappings_MetricRule151.setter
    def gmf_all_mappings_MetricRule151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_mappings_MetricRule__gmf_all_mappings_MetricRule151", None)
        self.__gmf_all_mappings_MetricRule151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Measurable"):
                opp_val = getattr(old_value, "Measurable", None)
                if opp_val == self:
                    setattr(old_value, "Measurable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Measurable"):
                opp_val = getattr(value, "Measurable", None)
                setattr(value, "Measurable", self)

class gmf_all_mappings_AuditRule(RuleBase):

    def __init__(self, id: str, severity: str, useInLiveMode: bool, message: str, gmf_all_mappings_AuditRule: "Constraint" = None, gmf_all_mappings_AuditRule134: "Auditable" = None, AuditContainer136: "AuditContainer" = None):
        self.id = id
        self.severity = severity
        self.useInLiveMode = useInLiveMode
        self.message = message
        self.gmf_all_mappings_AuditRule = gmf_all_mappings_AuditRule
        self.gmf_all_mappings_AuditRule134 = gmf_all_mappings_AuditRule134
        self.AuditContainer136 = AuditContainer136
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def useInLiveMode(self) -> bool:
        return self.__useInLiveMode

    @useInLiveMode.setter
    def useInLiveMode(self, useInLiveMode: bool):
        self.__useInLiveMode = useInLiveMode

    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def severity(self) -> str:
        return self.__severity

    @severity.setter
    def severity(self, severity: str):
        self.__severity = severity

    @property
    def AuditContainer136(self):
        return self.__AuditContainer136

    @AuditContainer136.setter
    def AuditContainer136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_mappings_AuditRule__AuditContainer136", None)
        self.__AuditContainer136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mappings137"):
                opp_val = getattr(old_value, "mappings137", None)
                if opp_val == self:
                    setattr(old_value, "mappings137", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mappings137"):
                opp_val = getattr(value, "mappings137", None)
                setattr(value, "mappings137", self)

    @property
    def gmf_all_mappings_AuditRule134(self):
        return self.__gmf_all_mappings_AuditRule134

    @gmf_all_mappings_AuditRule134.setter
    def gmf_all_mappings_AuditRule134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_mappings_AuditRule__gmf_all_mappings_AuditRule134", None)
        self.__gmf_all_mappings_AuditRule134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Auditable"):
                opp_val = getattr(old_value, "Auditable", None)
                if opp_val == self:
                    setattr(old_value, "Auditable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Auditable"):
                opp_val = getattr(value, "Auditable", None)
                setattr(value, "Auditable", self)

    @property
    def gmf_all_mappings_AuditRule(self):
        return self.__gmf_all_mappings_AuditRule

    @gmf_all_mappings_AuditRule.setter
    def gmf_all_mappings_AuditRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_mappings_AuditRule__gmf_all_mappings_AuditRule", None)
        self.__gmf_all_mappings_AuditRule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Constraint132"):
                opp_val = getattr(old_value, "Constraint132", None)
                if opp_val == self:
                    setattr(old_value, "Constraint132", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Constraint132"):
                opp_val = getattr(value, "Constraint132", None)
                setattr(value, "Constraint132", self)

class gmf_all_mappings_RuleBase(ABC):

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

class AuditRule:

    pass
class gmf_all_mappings_AuditContainer:

    def __init__(self, id: str, name: str, description: str, AuditContainer124: "AuditContainer" = None, AuditRule: set["AuditRule"] = None, AuditContainer129: set["AuditContainer"] = None):
        self.id = id
        self.name = name
        self.description = description
        self.AuditContainer124 = AuditContainer124
        self.AuditRule = AuditRule if AuditRule is not None else set()
        self.AuditContainer129 = AuditContainer129 if AuditContainer129 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def AuditRule(self):
        return self.__AuditRule

    @AuditRule.setter
    def AuditRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_mappings_AuditContainer__AuditRule", None)
        self.__AuditRule = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mappings127"):
                    opp_val = getattr(item, "mappings127", None)
                    
                    if opp_val == self:
                        setattr(item, "mappings127", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mappings127"):
                    opp_val = getattr(item, "mappings127", None)
                    
                    setattr(item, "mappings127", self)
                    

    @property
    def AuditContainer129(self):
        return self.__AuditContainer129

    @AuditContainer129.setter
    def AuditContainer129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_mappings_AuditContainer__AuditContainer129", None)
        self.__AuditContainer129 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mappings130"):
                    opp_val = getattr(item, "mappings130", None)
                    
                    if opp_val == self:
                        setattr(item, "mappings130", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mappings130"):
                    opp_val = getattr(item, "mappings130", None)
                    
                    setattr(item, "mappings130", self)
                    

    @property
    def AuditContainer124(self):
        return self.__AuditContainer124

    @AuditContainer124.setter
    def AuditContainer124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_mappings_AuditContainer__AuditContainer124", None)
        self.__AuditContainer124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mappings125"):
                opp_val = getattr(old_value, "mappings125", None)
                if opp_val == self:
                    setattr(old_value, "mappings125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mappings125"):
                opp_val = getattr(value, "mappings125", None)
                setattr(value, "mappings125", self)

class gmf_all_mappings_AppearanceSteward(ABC):

    pass
class AbstractTool:

    pass
class gmf_all_tooldef_CreationTool(AbstractTool):

    pass
class gmf_all_tooldef_GenericTool(AbstractTool):

    def __init__(self, toolClass: str, AbstractTool172: "gmf_all_tooldef_ToolContainer", AbstractTool: "gmf_all_mappings_ToolOwner", AbstractTool176: "gmf_all_tooldef_Palette", AbstractTool174: "gmf_all_tooldef_ToolGroup"):
        self.toolClass = toolClass
        
    @property
    def toolClass(self) -> str:
        return self.__toolClass

    @toolClass.setter
    def toolClass(self, toolClass: str):
        self.__toolClass = toolClass

class gmf_all_tooldef_StandardTool(AbstractTool):

    def __init__(self, toolKind: str, AbstractTool172: "gmf_all_tooldef_ToolContainer", AbstractTool: "gmf_all_mappings_ToolOwner", AbstractTool176: "gmf_all_tooldef_Palette", AbstractTool174: "gmf_all_tooldef_ToolGroup"):
        self.toolKind = toolKind
        
    @property
    def toolKind(self) -> str:
        return self.__toolKind

    @toolKind.setter
    def toolKind(self, toolKind: str):
        self.__toolKind = toolKind

class gmf_all_tooldef_ToolContainer(AbstractTool):

    pass
class gmf_all_tooldef_PaletteSeparator(AbstractTool):

    pass
class gmf_all_mappings_ToolOwner(ABC):

    pass
class ContextMenu:

    pass
class gmf_all_mappings_MenuOwner(ABC):

    pass
class FeatureSeqInitializer:

    pass
class gmf_all_mappings_FeatureInitializer(ABC):

    pass
class ReferenceNewElementSpec:

    pass
class FeatureInitializer:

    pass
class gmf_all_mappings_FeatureValueSpec(FeatureInitializer):

    pass
class gmf_all_mappings_ReferenceNewElementSpec(FeatureInitializer):

    pass
class gmf_all_mappings_ElementInitializer(ABC):

    pass
class gmf_all_mappings_ValueExpression:

    def __init__(self, body: str, language: str, langName: str):
        self.body = body
        self.language = language
        self.langName = langName
        
    @property
    def body(self) -> str:
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body

    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def langName(self) -> str:
        return self.__langName

    @langName.setter
    def langName(self, langName: str):
        self.__langName = langName

class gmf_all_mappings_LinkConstraints:

    pass
class ValueExpression:

    pass
class gmf_all_mappings_Constraint(ValueExpression):

    pass
class Canvas:

    pass
class gmf_all_mappings_CanvasMapping:

    pass
class mappings_gmf_all_EAttribute:

    pass
class MappingEntry:

    pass
class DiagramLabel:

    pass
class gmf_all_mappings_LabelMapping:

    def __init__(self, readOnly: bool, gmf_all_mappings_LabelMapping: "DiagramLabel" = None, MappingEntry: "MappingEntry" = None):
        self.readOnly = readOnly
        self.gmf_all_mappings_LabelMapping = gmf_all_mappings_LabelMapping
        self.MappingEntry = MappingEntry
        
    @property
    def readOnly(self) -> bool:
        return self.__readOnly

    @readOnly.setter
    def readOnly(self, readOnly: bool):
        self.__readOnly = readOnly

    @property
    def MappingEntry(self):
        return self.__MappingEntry

    @MappingEntry.setter
    def MappingEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_mappings_LabelMapping__MappingEntry", None)
        self.__MappingEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mappings74"):
                opp_val = getattr(old_value, "mappings74", None)
                if opp_val == self:
                    setattr(old_value, "mappings74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mappings74"):
                opp_val = getattr(value, "mappings74", None)
                setattr(value, "mappings74", self)

    @property
    def gmf_all_mappings_LabelMapping(self):
        return self.__gmf_all_mappings_LabelMapping

    @gmf_all_mappings_LabelMapping.setter
    def gmf_all_mappings_LabelMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_mappings_LabelMapping__gmf_all_mappings_LabelMapping", None)
        self.__gmf_all_mappings_LabelMapping = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DiagramLabel"):
                opp_val = getattr(old_value, "DiagramLabel", None)
                if opp_val == self:
                    setattr(old_value, "DiagramLabel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagramLabel"):
                opp_val = getattr(value, "DiagramLabel", None)
                setattr(value, "DiagramLabel", self)

class Toolbar:

    pass
class MainMenu:

    pass
class Palette:

    pass
class mappings_gmf_all_EPackage:

    pass
class Node:

    pass
class gmf_all_gmfgraph_DiagramLabel(Node):

    def __init__(self, elementIcon: bool, external: bool, gmf_all_gmfgraph_DiagramLabel: "ChildAccess" = None, gmf_all_gmfgraph_DiagramLabel214: "ChildAccess" = None, Node187: "gmf_all_gmfgraph_Canvas", Node: "gmf_all_mappings_NodeMapping"):
        self.elementIcon = elementIcon
        self.external = external
        self.gmf_all_gmfgraph_DiagramLabel = gmf_all_gmfgraph_DiagramLabel
        self.gmf_all_gmfgraph_DiagramLabel214 = gmf_all_gmfgraph_DiagramLabel214
        
    @property
    def external(self) -> bool:
        return self.__external

    @external.setter
    def external(self, external: bool):
        self.__external = external

    @property
    def elementIcon(self) -> bool:
        return self.__elementIcon

    @elementIcon.setter
    def elementIcon(self, elementIcon: bool):
        self.__elementIcon = elementIcon

    @property
    def gmf_all_gmfgraph_DiagramLabel214(self):
        return self.__gmf_all_gmfgraph_DiagramLabel214

    @gmf_all_gmfgraph_DiagramLabel214.setter
    def gmf_all_gmfgraph_DiagramLabel214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_gmfgraph_DiagramLabel__gmf_all_gmfgraph_DiagramLabel214", None)
        self.__gmf_all_gmfgraph_DiagramLabel214 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ChildAccess215"):
                opp_val = getattr(old_value, "ChildAccess215", None)
                if opp_val == self:
                    setattr(old_value, "ChildAccess215", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ChildAccess215"):
                opp_val = getattr(value, "ChildAccess215", None)
                setattr(value, "ChildAccess215", self)

    @property
    def gmf_all_gmfgraph_DiagramLabel(self):
        return self.__gmf_all_gmfgraph_DiagramLabel

    @gmf_all_gmfgraph_DiagramLabel.setter
    def gmf_all_gmfgraph_DiagramLabel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_gmfgraph_DiagramLabel__gmf_all_gmfgraph_DiagramLabel", None)
        self.__gmf_all_gmfgraph_DiagramLabel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ChildAccess212"):
                opp_val = getattr(old_value, "ChildAccess212", None)
                if opp_val == self:
                    setattr(old_value, "ChildAccess212", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ChildAccess212"):
                opp_val = getattr(value, "ChildAccess212", None)
                setattr(value, "ChildAccess212", self)

class mappings_AppearanceSteward:

    pass
class LinkConstraints:

    pass
class mappings_gmf_all_EStructuralFeature:

    pass
class Connection:

    pass
class mappings_NeedsContainment:

    pass
class Compartment:

    pass
class gmf_all_mappings_CompartmentMapping:

    pass
class ChildReference:

    pass
class mappings_gmf_all_EReference:

    pass
class gmf_all_mappings_NeedsContainment(ABC):

    pass
class mappings_ToolOwner:

    pass
class mappings_MenuOwner:

    pass
class mappings_MappingEntry:

    pass
class gmf_all_mappings_LinkMapping(mappings_ToolOwner, mappings_MenuOwner, mappings_MappingEntry, mappings_NeedsContainment, mappings_AppearanceSteward):

    pass
class gmf_all_mappings_NodeMapping(mappings_MappingEntry, mappings_AppearanceSteward, mappings_MenuOwner, mappings_ToolOwner):

    pass
class CompartmentMapping:

    pass
class NodeReference:

    pass
class gmf_all_mappings_TopNodeReference(NodeReference):

    pass
class gmf_all_mappings_ChildReference(NodeReference):

    pass
class NodeMapping:

    pass
class NeedsContainment:

    pass
class gmf_all_mappings_NodeReference(NeedsContainment):

    pass
class VisualEffectMapping:

    pass
class LabelMapping:

    pass
class gmf_all_mappings_DesignLabelMapping(LabelMapping):

    pass
class gmf_all_mappings_FeatureLabelMapping(LabelMapping):

    def __init__(self, viewPattern: str, editorPattern: str, editPattern: str, viewMethod: str, editMethod: str, gmf_all_mappings_FeatureLabelMapping: set["mappings_gmf_all_EAttribute"] = None, gmf_all_mappings_FeatureLabelMapping77: set["mappings_gmf_all_EAttribute"] = None, mappings: "gmf_all_mappings_MappingEntry"):
        self.viewPattern = viewPattern
        self.editorPattern = editorPattern
        self.editPattern = editPattern
        self.viewMethod = viewMethod
        self.editMethod = editMethod
        self.gmf_all_mappings_FeatureLabelMapping = gmf_all_mappings_FeatureLabelMapping if gmf_all_mappings_FeatureLabelMapping is not None else set()
        self.gmf_all_mappings_FeatureLabelMapping77 = gmf_all_mappings_FeatureLabelMapping77 if gmf_all_mappings_FeatureLabelMapping77 is not None else set()
        
    @property
    def editMethod(self) -> str:
        return self.__editMethod

    @editMethod.setter
    def editMethod(self, editMethod: str):
        self.__editMethod = editMethod

    @property
    def editPattern(self) -> str:
        return self.__editPattern

    @editPattern.setter
    def editPattern(self, editPattern: str):
        self.__editPattern = editPattern

    @property
    def viewPattern(self) -> str:
        return self.__viewPattern

    @viewPattern.setter
    def viewPattern(self, viewPattern: str):
        self.__viewPattern = viewPattern

    @property
    def editorPattern(self) -> str:
        return self.__editorPattern

    @editorPattern.setter
    def editorPattern(self, editorPattern: str):
        self.__editorPattern = editorPattern

    @property
    def viewMethod(self) -> str:
        return self.__viewMethod

    @viewMethod.setter
    def viewMethod(self, viewMethod: str):
        self.__viewMethod = viewMethod

    @property
    def gmf_all_mappings_FeatureLabelMapping(self):
        return self.__gmf_all_mappings_FeatureLabelMapping

    @gmf_all_mappings_FeatureLabelMapping.setter
    def gmf_all_mappings_FeatureLabelMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_mappings_FeatureLabelMapping__gmf_all_mappings_FeatureLabelMapping", None)
        self.__gmf_all_mappings_FeatureLabelMapping = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mappings_gmf_all_EAttribute"):
                    opp_val = getattr(item, "mappings_gmf_all_EAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "mappings_gmf_all_EAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mappings_gmf_all_EAttribute"):
                    opp_val = getattr(item, "mappings_gmf_all_EAttribute", None)
                    
                    setattr(item, "mappings_gmf_all_EAttribute", self)
                    

    @property
    def gmf_all_mappings_FeatureLabelMapping77(self):
        return self.__gmf_all_mappings_FeatureLabelMapping77

    @gmf_all_mappings_FeatureLabelMapping77.setter
    def gmf_all_mappings_FeatureLabelMapping77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_mappings_FeatureLabelMapping__gmf_all_mappings_FeatureLabelMapping77", None)
        self.__gmf_all_mappings_FeatureLabelMapping77 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mappings_gmf_all_EAttribute78"):
                    opp_val = getattr(item, "mappings_gmf_all_EAttribute78", None)
                    
                    if opp_val == self:
                        setattr(item, "mappings_gmf_all_EAttribute78", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mappings_gmf_all_EAttribute78"):
                    opp_val = getattr(item, "mappings_gmf_all_EAttribute78", None)
                    
                    setattr(item, "mappings_gmf_all_EAttribute78", self)
                    

class gmf_all_mappings_OclChoiceLabelMapping(LabelMapping):

    pass
class gmf_all_mappings_ExpressionLabelMapping(LabelMapping):

    pass
class ElementInitializer:

    pass
class gmf_all_mappings_FeatureSeqInitializer(ElementInitializer):

    pass
class Constraint:

    pass
class mappings_gmf_all_EClass:

    pass
class gmf_all_mappings_MappingEntry(ABC):

    def __init__(self, gmf_all_mappings_MappingEntry: "mappings_gmf_all_EClass" = None, gmf_all_mappings_MappingEntry13: "Constraint" = None, gmf_all_mappings_MappingEntry15: "ElementInitializer" = None, LabelMapping: set["LabelMapping"] = None, gmf_all_mappings_MappingEntry18: set["CanvasMapping"] = None, VisualEffectMapping: set["VisualEffectMapping"] = None):
        self.gmf_all_mappings_MappingEntry = gmf_all_mappings_MappingEntry
        self.gmf_all_mappings_MappingEntry13 = gmf_all_mappings_MappingEntry13
        self.gmf_all_mappings_MappingEntry15 = gmf_all_mappings_MappingEntry15
        self.LabelMapping = LabelMapping if LabelMapping is not None else set()
        self.gmf_all_mappings_MappingEntry18 = gmf_all_mappings_MappingEntry18 if gmf_all_mappings_MappingEntry18 is not None else set()
        self.VisualEffectMapping = VisualEffectMapping if VisualEffectMapping is not None else set()
        
    @property
    def gmf_all_mappings_MappingEntry15(self):
        return self.__gmf_all_mappings_MappingEntry15

    @gmf_all_mappings_MappingEntry15.setter
    def gmf_all_mappings_MappingEntry15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_mappings_MappingEntry__gmf_all_mappings_MappingEntry15", None)
        self.__gmf_all_mappings_MappingEntry15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ElementInitializer"):
                opp_val = getattr(old_value, "ElementInitializer", None)
                if opp_val == self:
                    setattr(old_value, "ElementInitializer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ElementInitializer"):
                opp_val = getattr(value, "ElementInitializer", None)
                setattr(value, "ElementInitializer", self)

    @property
    def LabelMapping(self):
        return self.__LabelMapping

    @LabelMapping.setter
    def LabelMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_mappings_MappingEntry__LabelMapping", None)
        self.__LabelMapping = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mappings"):
                    opp_val = getattr(item, "mappings", None)
                    
                    if opp_val == self:
                        setattr(item, "mappings", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mappings"):
                    opp_val = getattr(item, "mappings", None)
                    
                    setattr(item, "mappings", self)
                    

    @property
    def gmf_all_mappings_MappingEntry18(self):
        return self.__gmf_all_mappings_MappingEntry18

    @gmf_all_mappings_MappingEntry18.setter
    def gmf_all_mappings_MappingEntry18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_mappings_MappingEntry__gmf_all_mappings_MappingEntry18", None)
        self.__gmf_all_mappings_MappingEntry18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CanvasMapping19"):
                    opp_val = getattr(item, "CanvasMapping19", None)
                    
                    if opp_val == self:
                        setattr(item, "CanvasMapping19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CanvasMapping19"):
                    opp_val = getattr(item, "CanvasMapping19", None)
                    
                    setattr(item, "CanvasMapping19", self)
                    

    @property
    def gmf_all_mappings_MappingEntry13(self):
        return self.__gmf_all_mappings_MappingEntry13

    @gmf_all_mappings_MappingEntry13.setter
    def gmf_all_mappings_MappingEntry13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_mappings_MappingEntry__gmf_all_mappings_MappingEntry13", None)
        self.__gmf_all_mappings_MappingEntry13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Constraint"):
                opp_val = getattr(old_value, "Constraint", None)
                if opp_val == self:
                    setattr(old_value, "Constraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Constraint"):
                opp_val = getattr(value, "Constraint", None)
                setattr(value, "Constraint", self)

    @property
    def VisualEffectMapping(self):
        return self.__VisualEffectMapping

    @VisualEffectMapping.setter
    def VisualEffectMapping(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_mappings_MappingEntry__VisualEffectMapping", None)
        self.__VisualEffectMapping = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mappings21"):
                    opp_val = getattr(item, "mappings21", None)
                    
                    if opp_val == self:
                        setattr(item, "mappings21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mappings21"):
                    opp_val = getattr(item, "mappings21", None)
                    
                    setattr(item, "mappings21", self)
                    

    @property
    def gmf_all_mappings_MappingEntry(self):
        return self.__gmf_all_mappings_MappingEntry

    @gmf_all_mappings_MappingEntry.setter
    def gmf_all_mappings_MappingEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_mappings_MappingEntry__gmf_all_mappings_MappingEntry", None)
        self.__gmf_all_mappings_MappingEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mappings_gmf_all_EClass"):
                opp_val = getattr(old_value, "mappings_gmf_all_EClass", None)
                if opp_val == self:
                    setattr(old_value, "mappings_gmf_all_EClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mappings_gmf_all_EClass"):
                opp_val = getattr(value, "mappings_gmf_all_EClass", None)
                setattr(value, "mappings_gmf_all_EClass", self)

    def getDomainContext(self) -> str:
        # TODO: Implement getDomainContext method
        pass

class MetricContainer:

    pass
class AuditContainer:

    pass
class StyleSelector:

    pass
class gmf_all_tooldef_GenericStyleSelector(StyleSelector):

    def __init__(self, values: str, StyleSelector122: "gmf_all_mappings_AppearanceSteward", StyleSelector: "gmf_all_mappings_Mapping"):
        self.values = values
        
    @property
    def values(self) -> str:
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values

class CanvasMapping:

    pass
class LinkMapping:

    pass
class TopNodeReference:

    pass
class gmf_all_mappings_Mapping:

    pass