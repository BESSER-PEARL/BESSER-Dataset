from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class FontStyle(Enum):
    NORMAL = "NORMAL"
    BOLD = "BOLD"
    ITALIC = "ITALIC"
class Direction(Enum):
    SOUTH_EAST = "SOUTH_EAST"
    SOUTH_WEST = "SOUTH_WEST"
    NORTH_SOUTH = "NORTH_SOUTH"
    EAST_WEST = "EAST_WEST"
    NSEW = "NSEW"
    NONE = "NONE"
    NORTH = "NORTH"
    SOUTH = "SOUTH"
    WEST = "WEST"
    EAST = "EAST"
    NORTH_EAST = "NORTH_EAST"
    NORTH_WEST = "NORTH_WEST"
class LineKind(Enum):
    LINE_SOLID = "LINE_SOLID"
    LINE_DASH = "LINE_DASH"
    LINE_DOT = "LINE_DOT"
    LINE_DASHDOT = "LINE_DASHDOT"
    LINE_DASHDOTDOT = "LINE_DASHDOTDOT"
    LINE_CUSTOM = "LINE_CUSTOM"
class SVGPropertyType(Enum):
    STRING = "STRING"
    COLOR = "COLOR"
    FLOAT = "FLOAT"
class Alignment(Enum):
    BEGINNING = "BEGINNING"
    CENTER = "CENTER"
    END = "END"
    FILL = "FILL"
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


############################################
# Definition of Classes
############################################

class Pin:

    pass
class gmfgraph_CustomPin(Pin):

    def __init__(self, customOperationType: str, customOperationName: str):
        self.customOperationType = customOperationType
        self.customOperationName = customOperationName
        
        pass
    @property
    def customOperationType(self):
        return self.__customOperationType

    @customOperationType.setter
    def customOperationType(self, customOperationType: str):
        self.__customOperationType = customOperationType


    @property
    def customOperationName(self):
        return self.__customOperationName

    @customOperationName.setter
    def customOperationName(self, customOperationName: str):
        self.__customOperationName = customOperationName


class gmfgraph_PinOwner(ABC):

    pass
class gmfgraph_VisiblePin(Pin):

    pass
class gmfgraph_ColorPin(Pin):

    def __init__(self, backgroundNotForeground: bool):
        self.backgroundNotForeground = backgroundNotForeground
        
        pass
    @property
    def backgroundNotForeground(self):
        return self.__backgroundNotForeground

    @backgroundNotForeground.setter
    def backgroundNotForeground(self, backgroundNotForeground: bool):
        self.__backgroundNotForeground = backgroundNotForeground


class gmfgraph_Rectangle2D:

    def __init__(self, x: float, y: float, width: float, height: float, gmfgraph_Rectangle2D: "gmfgraph_SVGFigure" = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.gmfgraph_Rectangle2D = gmfgraph_Rectangle2D
        
        pass
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: float):
        self.__height = height


    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: float):
        self.__width = width


    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y


    @property
    def gmfgraph_Rectangle2D(self):
        return self.__gmfgraph_Rectangle2D

    @gmfgraph_Rectangle2D.setter
    def gmfgraph_Rectangle2D(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Rectangle2D__gmfgraph_Rectangle2D", None)
        self.__gmfgraph_Rectangle2D = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_SVGFigure121"):
                opp_val = getattr(old_value, "gmfgraph_SVGFigure121", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_SVGFigure121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_SVGFigure121"):
                opp_val = getattr(value, "gmfgraph_SVGFigure121", None)
                setattr(value, "gmfgraph_SVGFigure121", self)

class gmfgraph_SVGProperty:

    def __init__(self, query: str, attribute: str, type: str, getter: str, setter: str, callSuper: bool, gmfgraph_SVGProperty: "gmfgraph_SVGFigure" = None):
        self.query = query
        self.attribute = attribute
        self.type = type
        self.getter = getter
        self.setter = setter
        self.callSuper = callSuper
        self.gmfgraph_SVGProperty = gmfgraph_SVGProperty
        
        pass
    @property
    def getter(self):
        return self.__getter

    @getter.setter
    def getter(self, getter: str):
        self.__getter = getter


    @property
    def callSuper(self):
        return self.__callSuper

    @callSuper.setter
    def callSuper(self, callSuper: bool):
        self.__callSuper = callSuper


    @property
    def attribute(self):
        return self.__attribute

    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute


    @property
    def query(self):
        return self.__query

    @query.setter
    def query(self, query: str):
        self.__query = query


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def setter(self):
        return self.__setter

    @setter.setter
    def setter(self, setter: str):
        self.__setter = setter


    @property
    def gmfgraph_SVGProperty(self):
        return self.__gmfgraph_SVGProperty

    @gmfgraph_SVGProperty.setter
    def gmfgraph_SVGProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_SVGProperty__gmfgraph_SVGProperty", None)
        self.__gmfgraph_SVGProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_SVGFigure"):
                opp_val = getattr(old_value, "gmfgraph_SVGFigure", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_SVGFigure"):
                opp_val = getattr(value, "gmfgraph_SVGFigure", None)
                if opp_val is None:
                    setattr(value, "gmfgraph_SVGFigure", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Layout:

    pass
class gmfgraph_CenterLayout(Layout):

    pass
class gmfgraph_FlowLayout(Layout):

    def __init__(self, vertical: bool, matchMinorSize: bool, forceSingleLine: bool, majorAlignment: str, minorAlignment: str, majorSpacing: int, minorSpacing: int):
        self.vertical = vertical
        self.matchMinorSize = matchMinorSize
        self.forceSingleLine = forceSingleLine
        self.majorAlignment = majorAlignment
        self.minorAlignment = minorAlignment
        self.majorSpacing = majorSpacing
        self.minorSpacing = minorSpacing
        
        pass
    @property
    def majorAlignment(self):
        return self.__majorAlignment

    @majorAlignment.setter
    def majorAlignment(self, majorAlignment: str):
        self.__majorAlignment = majorAlignment


    @property
    def vertical(self):
        return self.__vertical

    @vertical.setter
    def vertical(self, vertical: bool):
        self.__vertical = vertical


    @property
    def forceSingleLine(self):
        return self.__forceSingleLine

    @forceSingleLine.setter
    def forceSingleLine(self, forceSingleLine: bool):
        self.__forceSingleLine = forceSingleLine


    @property
    def minorSpacing(self):
        return self.__minorSpacing

    @minorSpacing.setter
    def minorSpacing(self, minorSpacing: int):
        self.__minorSpacing = minorSpacing


    @property
    def minorAlignment(self):
        return self.__minorAlignment

    @minorAlignment.setter
    def minorAlignment(self, minorAlignment: str):
        self.__minorAlignment = minorAlignment


    @property
    def matchMinorSize(self):
        return self.__matchMinorSize

    @matchMinorSize.setter
    def matchMinorSize(self, matchMinorSize: bool):
        self.__matchMinorSize = matchMinorSize


    @property
    def majorSpacing(self):
        return self.__majorSpacing

    @majorSpacing.setter
    def majorSpacing(self, majorSpacing: int):
        self.__majorSpacing = majorSpacing


class gmfgraph_GridLayout(Layout):

    def __init__(self, numColumns: int, equalWidth: bool, gmfgraph_GridLayout: "gmfgraph_Dimension" = None, gmfgraph_GridLayout110: "gmfgraph_Dimension" = None):
        self.numColumns = numColumns
        self.equalWidth = equalWidth
        self.gmfgraph_GridLayout = gmfgraph_GridLayout
        self.gmfgraph_GridLayout110 = gmfgraph_GridLayout110
        
        pass
    @property
    def numColumns(self):
        return self.__numColumns

    @numColumns.setter
    def numColumns(self, numColumns: int):
        self.__numColumns = numColumns


    @property
    def equalWidth(self):
        return self.__equalWidth

    @equalWidth.setter
    def equalWidth(self, equalWidth: bool):
        self.__equalWidth = equalWidth


    @property
    def gmfgraph_GridLayout(self):
        return self.__gmfgraph_GridLayout

    @gmfgraph_GridLayout.setter
    def gmfgraph_GridLayout(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_GridLayout__gmfgraph_GridLayout", None)
        self.__gmfgraph_GridLayout = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_Dimension108"):
                opp_val = getattr(old_value, "gmfgraph_Dimension108", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_Dimension108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Dimension108"):
                opp_val = getattr(value, "gmfgraph_Dimension108", None)
                setattr(value, "gmfgraph_Dimension108", self)

    @property
    def gmfgraph_GridLayout110(self):
        return self.__gmfgraph_GridLayout110

    @gmfgraph_GridLayout110.setter
    def gmfgraph_GridLayout110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_GridLayout__gmfgraph_GridLayout110", None)
        self.__gmfgraph_GridLayout110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_Dimension111"):
                opp_val = getattr(old_value, "gmfgraph_Dimension111", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_Dimension111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Dimension111"):
                opp_val = getattr(value, "gmfgraph_Dimension111", None)
                setattr(value, "gmfgraph_Dimension111", self)

class gmfgraph_XYLayout(Layout):

    pass
class gmfgraph_StackLayout(Layout):

    pass
class gmfgraph_BorderLayout(Layout):

    pass
class gmfgraph_LayoutRef(Layout):

    pass
class LayoutData:

    pass
class gmfgraph_BorderLayoutData(LayoutData):

    def __init__(self, alignment: str, vertical: bool):
        self.alignment = alignment
        self.vertical = vertical
        
        pass
    @property
    def alignment(self):
        return self.__alignment

    @alignment.setter
    def alignment(self, alignment: str):
        self.__alignment = alignment


    @property
    def vertical(self):
        return self.__vertical

    @vertical.setter
    def vertical(self, vertical: bool):
        self.__vertical = vertical


class gmfgraph_XYLayoutData(LayoutData):

    pass
class gmfgraph_GridLayoutData(LayoutData):

    def __init__(self, grabExcessHorizontalSpace: bool, grabExcessVerticalSpace: bool, verticalAlignment: str, horizontalAlignment: str, verticalSpan: int, horizontalSpan: int, horizontalIndent: int, gmfgraph_GridLayoutData: "gmfgraph_Dimension" = None):
        self.grabExcessHorizontalSpace = grabExcessHorizontalSpace
        self.grabExcessVerticalSpace = grabExcessVerticalSpace
        self.verticalAlignment = verticalAlignment
        self.horizontalAlignment = horizontalAlignment
        self.verticalSpan = verticalSpan
        self.horizontalSpan = horizontalSpan
        self.horizontalIndent = horizontalIndent
        self.gmfgraph_GridLayoutData = gmfgraph_GridLayoutData
        
        pass
    @property
    def verticalSpan(self):
        return self.__verticalSpan

    @verticalSpan.setter
    def verticalSpan(self, verticalSpan: int):
        self.__verticalSpan = verticalSpan


    @property
    def horizontalSpan(self):
        return self.__horizontalSpan

    @horizontalSpan.setter
    def horizontalSpan(self, horizontalSpan: int):
        self.__horizontalSpan = horizontalSpan


    @property
    def grabExcessHorizontalSpace(self):
        return self.__grabExcessHorizontalSpace

    @grabExcessHorizontalSpace.setter
    def grabExcessHorizontalSpace(self, grabExcessHorizontalSpace: bool):
        self.__grabExcessHorizontalSpace = grabExcessHorizontalSpace


    @property
    def grabExcessVerticalSpace(self):
        return self.__grabExcessVerticalSpace

    @grabExcessVerticalSpace.setter
    def grabExcessVerticalSpace(self, grabExcessVerticalSpace: bool):
        self.__grabExcessVerticalSpace = grabExcessVerticalSpace


    @property
    def horizontalIndent(self):
        return self.__horizontalIndent

    @horizontalIndent.setter
    def horizontalIndent(self, horizontalIndent: int):
        self.__horizontalIndent = horizontalIndent


    @property
    def verticalAlignment(self):
        return self.__verticalAlignment

    @verticalAlignment.setter
    def verticalAlignment(self, verticalAlignment: str):
        self.__verticalAlignment = verticalAlignment


    @property
    def horizontalAlignment(self):
        return self.__horizontalAlignment

    @horizontalAlignment.setter
    def horizontalAlignment(self, horizontalAlignment: str):
        self.__horizontalAlignment = horizontalAlignment


    @property
    def gmfgraph_GridLayoutData(self):
        return self.__gmfgraph_GridLayoutData

    @gmfgraph_GridLayoutData.setter
    def gmfgraph_GridLayoutData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_GridLayoutData__gmfgraph_GridLayoutData", None)
        self.__gmfgraph_GridLayoutData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_Dimension100"):
                opp_val = getattr(old_value, "gmfgraph_Dimension100", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_Dimension100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Dimension100"):
                opp_val = getattr(value, "gmfgraph_Dimension100", None)
                setattr(value, "gmfgraph_Dimension100", self)

class gmfgraph_Layoutable(ABC):

    pass
class gmfgraph_LayoutData(ABC):

    pass
class Border:

    pass
class gmfgraph_LineBorder(Border):

    def __init__(self, width: int, gmfgraph_LineBorder: "gmfgraph_Color" = None):
        self.width = width
        self.gmfgraph_LineBorder = gmfgraph_LineBorder
        
        pass
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width


    @property
    def gmfgraph_LineBorder(self):
        return self.__gmfgraph_LineBorder

    @gmfgraph_LineBorder.setter
    def gmfgraph_LineBorder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_LineBorder__gmfgraph_LineBorder", None)
        self.__gmfgraph_LineBorder = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_Color90"):
                opp_val = getattr(old_value, "gmfgraph_Color90", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_Color90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Color90"):
                opp_val = getattr(value, "gmfgraph_Color90", None)
                setattr(value, "gmfgraph_Color90", self)

class gmfgraph_MarginBorder(Border):

    pass
class gmfgraph_CompoundBorder(Border):

    pass
class gmfgraph_BorderRef(Border):

    pass
class Font:

    pass
class gmfgraph_BasicFont(Font):

    def __init__(self, height: int, style: str, faceName: str):
        self.height = height
        self.style = style
        self.faceName = faceName
        
        pass
    @property
    def style(self):
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style


    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height


    @property
    def faceName(self):
        return self.__faceName

    @faceName.setter
    def faceName(self, faceName: str):
        self.__faceName = faceName


class Color:

    pass
class gmfgraph_RGBColor(Color):

    def __init__(self, blue: int, red: int, green: int):
        self.blue = blue
        self.red = red
        self.green = green
        
        pass
    @property
    def green(self):
        return self.__green

    @green.setter
    def green(self, green: int):
        self.__green = green


    @property
    def blue(self):
        return self.__blue

    @blue.setter
    def blue(self, blue: int):
        self.__blue = blue


    @property
    def red(self):
        return self.__red

    @red.setter
    def red(self, red: int):
        self.__red = red


class gmfgraph_ConstantColor(Color):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class gmfgraph_FigureAccessor:

    def __init__(self, accessor: str, gmfgraph_FigureAccessor: "gmfgraph_RealFigure" = None, gmfgraph_FigureAccessor86: "gmfgraph_CustomFigure" = None):
        self.accessor = accessor
        self.gmfgraph_FigureAccessor = gmfgraph_FigureAccessor
        self.gmfgraph_FigureAccessor86 = gmfgraph_FigureAccessor86
        
        pass
    @property
    def accessor(self):
        return self.__accessor

    @accessor.setter
    def accessor(self, accessor: str):
        self.__accessor = accessor


    @property
    def gmfgraph_FigureAccessor86(self):
        return self.__gmfgraph_FigureAccessor86

    @gmfgraph_FigureAccessor86.setter
    def gmfgraph_FigureAccessor86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_FigureAccessor__gmfgraph_FigureAccessor86", None)
        self.__gmfgraph_FigureAccessor86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_CustomFigure"):
                opp_val = getattr(old_value, "gmfgraph_CustomFigure", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_CustomFigure"):
                opp_val = getattr(value, "gmfgraph_CustomFigure", None)
                if opp_val is None:
                    setattr(value, "gmfgraph_CustomFigure", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gmfgraph_FigureAccessor(self):
        return self.__gmfgraph_FigureAccessor

    @gmfgraph_FigureAccessor.setter
    def gmfgraph_FigureAccessor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_FigureAccessor__gmfgraph_FigureAccessor", None)
        self.__gmfgraph_FigureAccessor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_RealFigure84"):
                opp_val = getattr(old_value, "gmfgraph_RealFigure84", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_RealFigure84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_RealFigure84"):
                opp_val = getattr(value, "gmfgraph_RealFigure84", None)
                setattr(value, "gmfgraph_RealFigure84", self)

class CustomFigure:

    pass
class CustomClass:

    pass
class gmfgraph_CustomLayout(CustomClass, Layout):

    pass
class gmfgraph_CustomBorder(CustomClass, Border):

    pass
class gmfgraph_CustomLayoutData(CustomClass, LayoutData):

    pass
class ConnectionFigure:

    pass
class gmfgraph_CustomConnection(CustomFigure, ConnectionFigure):

    pass
class Polygon:

    pass
class gmfgraph_ScalablePolygon(Polygon):

    pass
class Polyline:

    pass
class gmfgraph_PolylineConnection(Polyline, ConnectionFigure):

    pass
class gmfgraph_Polygon(Polyline):

    pass
class gmfgraph_CustomAttribute:

    def __init__(self, name: str, value: str, directAccess: bool, multiStatementValue: bool, gmfgraph_CustomAttribute: "gmfgraph_CustomAttributeOwner" = None):
        self.name = name
        self.value = value
        self.directAccess = directAccess
        self.multiStatementValue = multiStatementValue
        self.gmfgraph_CustomAttribute = gmfgraph_CustomAttribute
        
        pass
    @property
    def directAccess(self):
        return self.__directAccess

    @directAccess.setter
    def directAccess(self, directAccess: bool):
        self.__directAccess = directAccess


    @property
    def multiStatementValue(self):
        return self.__multiStatementValue

    @multiStatementValue.setter
    def multiStatementValue(self, multiStatementValue: bool):
        self.__multiStatementValue = multiStatementValue


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def gmfgraph_CustomAttribute(self):
        return self.__gmfgraph_CustomAttribute

    @gmfgraph_CustomAttribute.setter
    def gmfgraph_CustomAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_CustomAttribute__gmfgraph_CustomAttribute", None)
        self.__gmfgraph_CustomAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_CustomAttributeOwner"):
                opp_val = getattr(old_value, "gmfgraph_CustomAttributeOwner", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_CustomAttributeOwner"):
                opp_val = getattr(value, "gmfgraph_CustomAttributeOwner", None)
                if opp_val is None:
                    setattr(value, "gmfgraph_CustomAttributeOwner", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class gmfgraph_CustomAttributeOwner(ABC):

    pass
class DecorationFigure:

    pass
class gmfgraph_CustomDecoration(CustomFigure, DecorationFigure):

    pass
class gmfgraph_PolygonDecoration(Polygon, DecorationFigure):

    pass
class gmfgraph_PolylineDecoration(Polyline, DecorationFigure):

    pass
class RealFigure:

    pass
class gmfgraph_SVGFigure(RealFigure):

    def __init__(self, documentURI: str, noCanvasWidth: bool, noCanvasHeight: bool, gmfgraph_SVGFigure: set["gmfgraph_SVGProperty"] = None, gmfgraph_SVGFigure121: "gmfgraph_Rectangle2D" = None):
        self.documentURI = documentURI
        self.noCanvasWidth = noCanvasWidth
        self.noCanvasHeight = noCanvasHeight
        self.gmfgraph_SVGFigure = gmfgraph_SVGFigure if gmfgraph_SVGFigure is not None else set()
        self.gmfgraph_SVGFigure121 = gmfgraph_SVGFigure121
        
        pass
    @property
    def documentURI(self):
        return self.__documentURI

    @documentURI.setter
    def documentURI(self, documentURI: str):
        self.__documentURI = documentURI


    @property
    def noCanvasHeight(self):
        return self.__noCanvasHeight

    @noCanvasHeight.setter
    def noCanvasHeight(self, noCanvasHeight: bool):
        self.__noCanvasHeight = noCanvasHeight


    @property
    def noCanvasWidth(self):
        return self.__noCanvasWidth

    @noCanvasWidth.setter
    def noCanvasWidth(self, noCanvasWidth: bool):
        self.__noCanvasWidth = noCanvasWidth


    @property
    def gmfgraph_SVGFigure121(self):
        return self.__gmfgraph_SVGFigure121

    @gmfgraph_SVGFigure121.setter
    def gmfgraph_SVGFigure121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_SVGFigure__gmfgraph_SVGFigure121", None)
        self.__gmfgraph_SVGFigure121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_Rectangle2D"):
                opp_val = getattr(old_value, "gmfgraph_Rectangle2D", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_Rectangle2D", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Rectangle2D"):
                opp_val = getattr(value, "gmfgraph_Rectangle2D", None)
                setattr(value, "gmfgraph_Rectangle2D", self)

    @property
    def gmfgraph_SVGFigure(self):
        return self.__gmfgraph_SVGFigure

    @gmfgraph_SVGFigure.setter
    def gmfgraph_SVGFigure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_SVGFigure__gmfgraph_SVGFigure", None)
        self.__gmfgraph_SVGFigure = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gmfgraph_SVGProperty"):
                    opp_val = getattr(item, "gmfgraph_SVGProperty", None)
                    
                    if opp_val == self:
                        setattr(item, "gmfgraph_SVGProperty", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gmfgraph_SVGProperty"):
                    opp_val = getattr(item, "gmfgraph_SVGProperty", None)
                    
                    setattr(item, "gmfgraph_SVGProperty", self)
                    

class gmfgraph_Shape(RealFigure):

    def __init__(self, outline: bool, fill: bool, lineWidth: int, lineKind: str, xorFill: bool, xorOutline: bool, gmfgraph_Shape: set["gmfgraph_Figure"] = None):
        self.outline = outline
        self.fill = fill
        self.lineWidth = lineWidth
        self.lineKind = lineKind
        self.xorFill = xorFill
        self.xorOutline = xorOutline
        self.gmfgraph_Shape = gmfgraph_Shape if gmfgraph_Shape is not None else set()
        
        pass
    @property
    def lineKind(self):
        return self.__lineKind

    @lineKind.setter
    def lineKind(self, lineKind: str):
        self.__lineKind = lineKind


    @property
    def xorFill(self):
        return self.__xorFill

    @xorFill.setter
    def xorFill(self, xorFill: bool):
        self.__xorFill = xorFill


    @property
    def lineWidth(self):
        return self.__lineWidth

    @lineWidth.setter
    def lineWidth(self, lineWidth: int):
        self.__lineWidth = lineWidth


    @property
    def outline(self):
        return self.__outline

    @outline.setter
    def outline(self, outline: bool):
        self.__outline = outline


    @property
    def fill(self):
        return self.__fill

    @fill.setter
    def fill(self, fill: bool):
        self.__fill = fill


    @property
    def xorOutline(self):
        return self.__xorOutline

    @xorOutline.setter
    def xorOutline(self, xorOutline: bool):
        self.__xorOutline = xorOutline


    @property
    def gmfgraph_Shape(self):
        return self.__gmfgraph_Shape

    @gmfgraph_Shape.setter
    def gmfgraph_Shape(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Shape__gmfgraph_Shape", None)
        self.__gmfgraph_Shape = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gmfgraph_Figure75"):
                    opp_val = getattr(item, "gmfgraph_Figure75", None)
                    
                    if opp_val == self:
                        setattr(item, "gmfgraph_Figure75", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gmfgraph_Figure75"):
                    opp_val = getattr(item, "gmfgraph_Figure75", None)
                    
                    setattr(item, "gmfgraph_Figure75", self)
                    

class gmfgraph_CustomFigure(CustomClass, RealFigure):

    pass
class gmfgraph_LabeledContainer(RealFigure):

    pass
class gmfgraph_DecorationFigure(RealFigure):

    pass
class gmfgraph_Label(RealFigure):

    def __init__(self, text: str):
        self.text = text
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


class gmfgraph_ConnectionFigure(RealFigure):

    pass
class gmfgraph_InvisibleRectangle(RealFigure):

    pass
class Shape:

    pass
class gmfgraph_RoundedRectangle(Shape):

    def __init__(self, cornerWidth: int, cornerHeight: int):
        self.cornerWidth = cornerWidth
        self.cornerHeight = cornerHeight
        
        pass
    @property
    def cornerWidth(self):
        return self.__cornerWidth

    @cornerWidth.setter
    def cornerWidth(self, cornerWidth: int):
        self.__cornerWidth = cornerWidth


    @property
    def cornerHeight(self):
        return self.__cornerHeight

    @cornerHeight.setter
    def cornerHeight(self, cornerHeight: int):
        self.__cornerHeight = cornerHeight


class gmfgraph_Polyline(Shape):

    pass
class gmfgraph_Ellipse(Shape):

    pass
class gmfgraph_Rectangle(Shape):

    pass
class gmfgraph_VerticalLabel(RealFigure):

    def __init__(self, text: str):
        self.text = text
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


class CustomAttributeOwner:

    pass
class gmfgraph_CustomClass(CustomAttributeOwner):

    def __init__(self, qualifiedClassName: str):
        self.qualifiedClassName = qualifiedClassName
        
        pass
    @property
    def qualifiedClassName(self):
        return self.__qualifiedClassName

    @qualifiedClassName.setter
    def qualifiedClassName(self, qualifiedClassName: str):
        self.__qualifiedClassName = qualifiedClassName


class PinOwner:

    pass
class AbstractFigure:

    pass
class gmfgraph_FigureRef(AbstractFigure):

    pass
class gmfgraph_Color(ABC):

    pass
class Layoutable:

    pass
class gmfgraph_Figure(Layoutable):

    pass
class Figure:

    pass
class gmfgraph_AbstractFigure(Figure):

    pass
class gmfgraph_Point:

    def __init__(self, x: int, y: int, gmfgraph_Point77: "gmfgraph_Polyline" = None, gmfgraph_Point: "gmfgraph_Figure" = None, gmfgraph_Point60: "gmfgraph_Figure" = None, gmfgraph_Point115: "gmfgraph_XYLayoutData" = None):
        self.x = x
        self.y = y
        self.gmfgraph_Point77 = gmfgraph_Point77
        self.gmfgraph_Point = gmfgraph_Point
        self.gmfgraph_Point60 = gmfgraph_Point60
        self.gmfgraph_Point115 = gmfgraph_Point115
        
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


    @property
    def gmfgraph_Point60(self):
        return self.__gmfgraph_Point60

    @gmfgraph_Point60.setter
    def gmfgraph_Point60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Point__gmfgraph_Point60", None)
        self.__gmfgraph_Point60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_Figure59"):
                opp_val = getattr(old_value, "gmfgraph_Figure59", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_Figure59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Figure59"):
                opp_val = getattr(value, "gmfgraph_Figure59", None)
                setattr(value, "gmfgraph_Figure59", self)

    @property
    def gmfgraph_Point77(self):
        return self.__gmfgraph_Point77

    @gmfgraph_Point77.setter
    def gmfgraph_Point77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Point__gmfgraph_Point77", None)
        self.__gmfgraph_Point77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_Polyline"):
                opp_val = getattr(old_value, "gmfgraph_Polyline", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Polyline"):
                opp_val = getattr(value, "gmfgraph_Polyline", None)
                if opp_val is None:
                    setattr(value, "gmfgraph_Polyline", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gmfgraph_Point(self):
        return self.__gmfgraph_Point

    @gmfgraph_Point.setter
    def gmfgraph_Point(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Point__gmfgraph_Point", None)
        self.__gmfgraph_Point = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_Figure57"):
                opp_val = getattr(old_value, "gmfgraph_Figure57", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_Figure57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Figure57"):
                opp_val = getattr(value, "gmfgraph_Figure57", None)
                setattr(value, "gmfgraph_Figure57", self)

    @property
    def gmfgraph_Point115(self):
        return self.__gmfgraph_Point115

    @gmfgraph_Point115.setter
    def gmfgraph_Point115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Point__gmfgraph_Point115", None)
        self.__gmfgraph_Point115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_XYLayoutData"):
                opp_val = getattr(old_value, "gmfgraph_XYLayoutData", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_XYLayoutData", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_XYLayoutData"):
                opp_val = getattr(value, "gmfgraph_XYLayoutData", None)
                setattr(value, "gmfgraph_XYLayoutData", self)

class gmfgraph_Insets:

    def __init__(self, top: int, left: int, bottom: int, right: int, gmfgraph_Insets92: "gmfgraph_MarginBorder" = None, gmfgraph_Insets: "gmfgraph_Figure" = None):
        self.top = top
        self.left = left
        self.bottom = bottom
        self.right = right
        self.gmfgraph_Insets92 = gmfgraph_Insets92
        self.gmfgraph_Insets = gmfgraph_Insets
        
        pass
    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left: int):
        self.__left = left


    @property
    def bottom(self):
        return self.__bottom

    @bottom.setter
    def bottom(self, bottom: int):
        self.__bottom = bottom


    @property
    def top(self):
        return self.__top

    @top.setter
    def top(self, top: int):
        self.__top = top


    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right: int):
        self.__right = right


    @property
    def gmfgraph_Insets92(self):
        return self.__gmfgraph_Insets92

    @gmfgraph_Insets92.setter
    def gmfgraph_Insets92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Insets__gmfgraph_Insets92", None)
        self.__gmfgraph_Insets92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_MarginBorder"):
                opp_val = getattr(old_value, "gmfgraph_MarginBorder", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_MarginBorder", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_MarginBorder"):
                opp_val = getattr(value, "gmfgraph_MarginBorder", None)
                setattr(value, "gmfgraph_MarginBorder", self)

    @property
    def gmfgraph_Insets(self):
        return self.__gmfgraph_Insets

    @gmfgraph_Insets.setter
    def gmfgraph_Insets(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Insets__gmfgraph_Insets", None)
        self.__gmfgraph_Insets = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_Figure52"):
                opp_val = getattr(old_value, "gmfgraph_Figure52", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_Figure52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Figure52"):
                opp_val = getattr(value, "gmfgraph_Figure52", None)
                setattr(value, "gmfgraph_Figure52", self)

class gmfgraph_Font(ABC):

    pass
class gmfgraph_Dimension:

    def __init__(self, dx: int, dy: int, gmfgraph_Dimension: "gmfgraph_DefaultSizeFacet" = None, gmfgraph_Dimension48: "gmfgraph_Figure" = None, gmfgraph_Dimension42: "gmfgraph_Figure" = None, gmfgraph_Dimension45: "gmfgraph_Figure" = None, gmfgraph_Dimension108: "gmfgraph_GridLayout" = None, gmfgraph_Dimension111: "gmfgraph_GridLayout" = None, gmfgraph_Dimension100: "gmfgraph_GridLayoutData" = None, gmfgraph_Dimension118: "gmfgraph_XYLayoutData" = None, gmfgraph_Dimension113: "gmfgraph_BorderLayout" = None):
        self.dx = dx
        self.dy = dy
        self.gmfgraph_Dimension = gmfgraph_Dimension
        self.gmfgraph_Dimension48 = gmfgraph_Dimension48
        self.gmfgraph_Dimension42 = gmfgraph_Dimension42
        self.gmfgraph_Dimension45 = gmfgraph_Dimension45
        self.gmfgraph_Dimension108 = gmfgraph_Dimension108
        self.gmfgraph_Dimension111 = gmfgraph_Dimension111
        self.gmfgraph_Dimension100 = gmfgraph_Dimension100
        self.gmfgraph_Dimension118 = gmfgraph_Dimension118
        self.gmfgraph_Dimension113 = gmfgraph_Dimension113
        
        pass
    @property
    def dx(self):
        return self.__dx

    @dx.setter
    def dx(self, dx: int):
        self.__dx = dx


    @property
    def dy(self):
        return self.__dy

    @dy.setter
    def dy(self, dy: int):
        self.__dy = dy


    @property
    def gmfgraph_Dimension111(self):
        return self.__gmfgraph_Dimension111

    @gmfgraph_Dimension111.setter
    def gmfgraph_Dimension111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Dimension__gmfgraph_Dimension111", None)
        self.__gmfgraph_Dimension111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_GridLayout110"):
                opp_val = getattr(old_value, "gmfgraph_GridLayout110", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_GridLayout110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_GridLayout110"):
                opp_val = getattr(value, "gmfgraph_GridLayout110", None)
                setattr(value, "gmfgraph_GridLayout110", self)

    @property
    def gmfgraph_Dimension45(self):
        return self.__gmfgraph_Dimension45

    @gmfgraph_Dimension45.setter
    def gmfgraph_Dimension45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Dimension__gmfgraph_Dimension45", None)
        self.__gmfgraph_Dimension45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_Figure44"):
                opp_val = getattr(old_value, "gmfgraph_Figure44", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_Figure44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Figure44"):
                opp_val = getattr(value, "gmfgraph_Figure44", None)
                setattr(value, "gmfgraph_Figure44", self)

    @property
    def gmfgraph_Dimension(self):
        return self.__gmfgraph_Dimension

    @gmfgraph_Dimension.setter
    def gmfgraph_Dimension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Dimension__gmfgraph_Dimension", None)
        self.__gmfgraph_Dimension = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_DefaultSizeFacet"):
                opp_val = getattr(old_value, "gmfgraph_DefaultSizeFacet", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_DefaultSizeFacet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_DefaultSizeFacet"):
                opp_val = getattr(value, "gmfgraph_DefaultSizeFacet", None)
                setattr(value, "gmfgraph_DefaultSizeFacet", self)

    @property
    def gmfgraph_Dimension48(self):
        return self.__gmfgraph_Dimension48

    @gmfgraph_Dimension48.setter
    def gmfgraph_Dimension48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Dimension__gmfgraph_Dimension48", None)
        self.__gmfgraph_Dimension48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_Figure47"):
                opp_val = getattr(old_value, "gmfgraph_Figure47", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_Figure47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Figure47"):
                opp_val = getattr(value, "gmfgraph_Figure47", None)
                setattr(value, "gmfgraph_Figure47", self)

    @property
    def gmfgraph_Dimension118(self):
        return self.__gmfgraph_Dimension118

    @gmfgraph_Dimension118.setter
    def gmfgraph_Dimension118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Dimension__gmfgraph_Dimension118", None)
        self.__gmfgraph_Dimension118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_XYLayoutData117"):
                opp_val = getattr(old_value, "gmfgraph_XYLayoutData117", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_XYLayoutData117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_XYLayoutData117"):
                opp_val = getattr(value, "gmfgraph_XYLayoutData117", None)
                setattr(value, "gmfgraph_XYLayoutData117", self)

    @property
    def gmfgraph_Dimension108(self):
        return self.__gmfgraph_Dimension108

    @gmfgraph_Dimension108.setter
    def gmfgraph_Dimension108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Dimension__gmfgraph_Dimension108", None)
        self.__gmfgraph_Dimension108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_GridLayout"):
                opp_val = getattr(old_value, "gmfgraph_GridLayout", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_GridLayout", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_GridLayout"):
                opp_val = getattr(value, "gmfgraph_GridLayout", None)
                setattr(value, "gmfgraph_GridLayout", self)

    @property
    def gmfgraph_Dimension113(self):
        return self.__gmfgraph_Dimension113

    @gmfgraph_Dimension113.setter
    def gmfgraph_Dimension113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Dimension__gmfgraph_Dimension113", None)
        self.__gmfgraph_Dimension113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_BorderLayout"):
                opp_val = getattr(old_value, "gmfgraph_BorderLayout", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_BorderLayout", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_BorderLayout"):
                opp_val = getattr(value, "gmfgraph_BorderLayout", None)
                setattr(value, "gmfgraph_BorderLayout", self)

    @property
    def gmfgraph_Dimension100(self):
        return self.__gmfgraph_Dimension100

    @gmfgraph_Dimension100.setter
    def gmfgraph_Dimension100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Dimension__gmfgraph_Dimension100", None)
        self.__gmfgraph_Dimension100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_GridLayoutData"):
                opp_val = getattr(old_value, "gmfgraph_GridLayoutData", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_GridLayoutData", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_GridLayoutData"):
                opp_val = getattr(value, "gmfgraph_GridLayoutData", None)
                setattr(value, "gmfgraph_GridLayoutData", self)

    @property
    def gmfgraph_Dimension42(self):
        return self.__gmfgraph_Dimension42

    @gmfgraph_Dimension42.setter
    def gmfgraph_Dimension42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Dimension__gmfgraph_Dimension42", None)
        self.__gmfgraph_Dimension42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_Figure41"):
                opp_val = getattr(old_value, "gmfgraph_Figure41", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_Figure41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Figure41"):
                opp_val = getattr(value, "gmfgraph_Figure41", None)
                setattr(value, "gmfgraph_Figure41", self)

class gmfgraph_ChildAccess:

    def __init__(self, accessor: str, ChildAccess: "gmfgraph_FigureDescriptor" = None, accessors: "gmfgraph_FigureDescriptor" = None, gmfgraph_ChildAccess67: "gmfgraph_Figure" = None, gmfgraph_ChildAccess: "gmfgraph_Node" = None, gmfgraph_ChildAccess25: "gmfgraph_Compartment" = None, gmfgraph_ChildAccess28: "gmfgraph_DiagramLabel" = None, gmfgraph_ChildAccess31: "gmfgraph_DiagramLabel" = None):
        self.accessor = accessor
        self.ChildAccess = ChildAccess
        self.accessors = accessors
        self.gmfgraph_ChildAccess67 = gmfgraph_ChildAccess67
        self.gmfgraph_ChildAccess = gmfgraph_ChildAccess
        self.gmfgraph_ChildAccess25 = gmfgraph_ChildAccess25
        self.gmfgraph_ChildAccess28 = gmfgraph_ChildAccess28
        self.gmfgraph_ChildAccess31 = gmfgraph_ChildAccess31
        
        pass
    @property
    def accessor(self):
        return self.__accessor

    @accessor.setter
    def accessor(self, accessor: str):
        self.__accessor = accessor


    @property
    def accessors(self):
        return self.__accessors

    @accessors.setter
    def accessors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_ChildAccess__accessors", None)
        self.__accessors = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FigureDescriptor"):
                opp_val = getattr(old_value, "FigureDescriptor", None)
                if opp_val == self:
                    setattr(old_value, "FigureDescriptor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FigureDescriptor"):
                opp_val = getattr(value, "FigureDescriptor", None)
                setattr(value, "FigureDescriptor", self)

    @property
    def gmfgraph_ChildAccess(self):
        return self.__gmfgraph_ChildAccess

    @gmfgraph_ChildAccess.setter
    def gmfgraph_ChildAccess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_ChildAccess__gmfgraph_ChildAccess", None)
        self.__gmfgraph_ChildAccess = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_Node22"):
                opp_val = getattr(old_value, "gmfgraph_Node22", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_Node22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Node22"):
                opp_val = getattr(value, "gmfgraph_Node22", None)
                setattr(value, "gmfgraph_Node22", self)

    @property
    def gmfgraph_ChildAccess67(self):
        return self.__gmfgraph_ChildAccess67

    @gmfgraph_ChildAccess67.setter
    def gmfgraph_ChildAccess67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_ChildAccess__gmfgraph_ChildAccess67", None)
        self.__gmfgraph_ChildAccess67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_Figure68"):
                opp_val = getattr(old_value, "gmfgraph_Figure68", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_Figure68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Figure68"):
                opp_val = getattr(value, "gmfgraph_Figure68", None)
                setattr(value, "gmfgraph_Figure68", self)

    @property
    def gmfgraph_ChildAccess31(self):
        return self.__gmfgraph_ChildAccess31

    @gmfgraph_ChildAccess31.setter
    def gmfgraph_ChildAccess31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_ChildAccess__gmfgraph_ChildAccess31", None)
        self.__gmfgraph_ChildAccess31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_DiagramLabel30"):
                opp_val = getattr(old_value, "gmfgraph_DiagramLabel30", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_DiagramLabel30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_DiagramLabel30"):
                opp_val = getattr(value, "gmfgraph_DiagramLabel30", None)
                setattr(value, "gmfgraph_DiagramLabel30", self)

    @property
    def gmfgraph_ChildAccess28(self):
        return self.__gmfgraph_ChildAccess28

    @gmfgraph_ChildAccess28.setter
    def gmfgraph_ChildAccess28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_ChildAccess__gmfgraph_ChildAccess28", None)
        self.__gmfgraph_ChildAccess28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_DiagramLabel27"):
                opp_val = getattr(old_value, "gmfgraph_DiagramLabel27", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_DiagramLabel27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_DiagramLabel27"):
                opp_val = getattr(value, "gmfgraph_DiagramLabel27", None)
                setattr(value, "gmfgraph_DiagramLabel27", self)

    @property
    def gmfgraph_ChildAccess25(self):
        return self.__gmfgraph_ChildAccess25

    @gmfgraph_ChildAccess25.setter
    def gmfgraph_ChildAccess25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_ChildAccess__gmfgraph_ChildAccess25", None)
        self.__gmfgraph_ChildAccess25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_Compartment24"):
                opp_val = getattr(old_value, "gmfgraph_Compartment24", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_Compartment24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Compartment24"):
                opp_val = getattr(value, "gmfgraph_Compartment24", None)
                setattr(value, "gmfgraph_Compartment24", self)

    @property
    def ChildAccess(self):
        return self.__ChildAccess

    @ChildAccess.setter
    def ChildAccess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_ChildAccess__ChildAccess", None)
        self.__ChildAccess = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner"):
                opp_val = getattr(old_value, "owner", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner"):
                opp_val = getattr(value, "owner", None)
                if opp_val is None:
                    setattr(value, "owner", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class AbstractNode:

    pass
class DiagramElement:

    pass
class gmfgraph_AbstractNode(DiagramElement):

    pass
class gmfgraph_VisualFacet(ABC):

    pass
class gmfgraph_Identity(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class VisualFacet:

    pass
class gmfgraph_AlignmentFacet(VisualFacet):

    def __init__(self, alignment: str):
        self.alignment = alignment
        
        pass
    @property
    def alignment(self):
        return self.__alignment

    @alignment.setter
    def alignment(self, alignment: str):
        self.__alignment = alignment


class gmfgraph_GradientFacet(VisualFacet):

    def __init__(self, direction: str):
        self.direction = direction
        
        pass
    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction


class gmfgraph_LabelOffsetFacet(VisualFacet):

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        
        pass
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x


    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y


class gmfgraph_DefaultSizeFacet(VisualFacet):

    pass
class gmfgraph_GeneralFacet(VisualFacet):

    def __init__(self, identifier: str, data: str):
        self.identifier = identifier
        self.data = data
        
        pass
    @property
    def identifier(self):
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier


    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data: str):
        self.__data = data


class Node:

    pass
class gmfgraph_Connection(DiagramElement):

    pass
class gmfgraph_Node(AbstractNode):

    def __init__(self, resizeConstraint: str, affixedParentSide: str, gmfgraph_Node: "gmfgraph_Canvas" = None, gmfgraph_Node22: "gmfgraph_ChildAccess" = None):
        self.resizeConstraint = resizeConstraint
        self.affixedParentSide = affixedParentSide
        self.gmfgraph_Node = gmfgraph_Node
        self.gmfgraph_Node22 = gmfgraph_Node22
        
        pass
    @property
    def affixedParentSide(self):
        return self.__affixedParentSide

    @affixedParentSide.setter
    def affixedParentSide(self, affixedParentSide: str):
        self.__affixedParentSide = affixedParentSide


    @property
    def resizeConstraint(self):
        return self.__resizeConstraint

    @resizeConstraint.setter
    def resizeConstraint(self, resizeConstraint: str):
        self.__resizeConstraint = resizeConstraint


    @property
    def gmfgraph_Node(self):
        return self.__gmfgraph_Node

    @gmfgraph_Node.setter
    def gmfgraph_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Node__gmfgraph_Node", None)
        self.__gmfgraph_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_Canvas2"):
                opp_val = getattr(old_value, "gmfgraph_Canvas2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Canvas2"):
                opp_val = getattr(value, "gmfgraph_Canvas2", None)
                if opp_val is None:
                    setattr(value, "gmfgraph_Canvas2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gmfgraph_Node22(self):
        return self.__gmfgraph_Node22

    @gmfgraph_Node22.setter
    def gmfgraph_Node22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Node__gmfgraph_Node22", None)
        self.__gmfgraph_Node22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_ChildAccess"):
                opp_val = getattr(old_value, "gmfgraph_ChildAccess", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_ChildAccess", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_ChildAccess"):
                opp_val = getattr(value, "gmfgraph_ChildAccess", None)
                setattr(value, "gmfgraph_ChildAccess", self)

class Identity:

    pass
class gmfgraph_DiagramElement(Identity):

    pass
class gmfgraph_FigureGallery(Identity):

    def __init__(self, implementationBundle: str, gmfgraph_FigureGallery10: set["gmfgraph_RealFigure"] = None, gmfgraph_FigureGallery12: set["gmfgraph_FigureDescriptor"] = None, gmfgraph_FigureGallery14: set["gmfgraph_Border"] = None, gmfgraph_FigureGallery16: set["gmfgraph_Layout"] = None, gmfgraph_FigureGallery: "gmfgraph_Canvas" = None):
        self.implementationBundle = implementationBundle
        self.gmfgraph_FigureGallery10 = gmfgraph_FigureGallery10 if gmfgraph_FigureGallery10 is not None else set()
        self.gmfgraph_FigureGallery12 = gmfgraph_FigureGallery12 if gmfgraph_FigureGallery12 is not None else set()
        self.gmfgraph_FigureGallery14 = gmfgraph_FigureGallery14 if gmfgraph_FigureGallery14 is not None else set()
        self.gmfgraph_FigureGallery16 = gmfgraph_FigureGallery16 if gmfgraph_FigureGallery16 is not None else set()
        self.gmfgraph_FigureGallery = gmfgraph_FigureGallery
        
        pass
    @property
    def implementationBundle(self):
        return self.__implementationBundle

    @implementationBundle.setter
    def implementationBundle(self, implementationBundle: str):
        self.__implementationBundle = implementationBundle


    @property
    def gmfgraph_FigureGallery(self):
        return self.__gmfgraph_FigureGallery

    @gmfgraph_FigureGallery.setter
    def gmfgraph_FigureGallery(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_FigureGallery__gmfgraph_FigureGallery", None)
        self.__gmfgraph_FigureGallery = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_Canvas"):
                opp_val = getattr(old_value, "gmfgraph_Canvas", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Canvas"):
                opp_val = getattr(value, "gmfgraph_Canvas", None)
                if opp_val is None:
                    setattr(value, "gmfgraph_Canvas", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gmfgraph_FigureGallery14(self):
        return self.__gmfgraph_FigureGallery14

    @gmfgraph_FigureGallery14.setter
    def gmfgraph_FigureGallery14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_FigureGallery__gmfgraph_FigureGallery14", None)
        self.__gmfgraph_FigureGallery14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gmfgraph_Border"):
                    opp_val = getattr(item, "gmfgraph_Border", None)
                    
                    if opp_val == self:
                        setattr(item, "gmfgraph_Border", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gmfgraph_Border"):
                    opp_val = getattr(item, "gmfgraph_Border", None)
                    
                    setattr(item, "gmfgraph_Border", self)
                    

    @property
    def gmfgraph_FigureGallery10(self):
        return self.__gmfgraph_FigureGallery10

    @gmfgraph_FigureGallery10.setter
    def gmfgraph_FigureGallery10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_FigureGallery__gmfgraph_FigureGallery10", None)
        self.__gmfgraph_FigureGallery10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gmfgraph_RealFigure"):
                    opp_val = getattr(item, "gmfgraph_RealFigure", None)
                    
                    if opp_val == self:
                        setattr(item, "gmfgraph_RealFigure", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gmfgraph_RealFigure"):
                    opp_val = getattr(item, "gmfgraph_RealFigure", None)
                    
                    setattr(item, "gmfgraph_RealFigure", self)
                    

    @property
    def gmfgraph_FigureGallery16(self):
        return self.__gmfgraph_FigureGallery16

    @gmfgraph_FigureGallery16.setter
    def gmfgraph_FigureGallery16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_FigureGallery__gmfgraph_FigureGallery16", None)
        self.__gmfgraph_FigureGallery16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gmfgraph_Layout"):
                    opp_val = getattr(item, "gmfgraph_Layout", None)
                    
                    if opp_val == self:
                        setattr(item, "gmfgraph_Layout", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gmfgraph_Layout"):
                    opp_val = getattr(item, "gmfgraph_Layout", None)
                    
                    setattr(item, "gmfgraph_Layout", self)
                    

    @property
    def gmfgraph_FigureGallery12(self):
        return self.__gmfgraph_FigureGallery12

    @gmfgraph_FigureGallery12.setter
    def gmfgraph_FigureGallery12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_FigureGallery__gmfgraph_FigureGallery12", None)
        self.__gmfgraph_FigureGallery12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gmfgraph_FigureDescriptor"):
                    opp_val = getattr(item, "gmfgraph_FigureDescriptor", None)
                    
                    if opp_val == self:
                        setattr(item, "gmfgraph_FigureDescriptor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gmfgraph_FigureDescriptor"):
                    opp_val = getattr(item, "gmfgraph_FigureDescriptor", None)
                    
                    setattr(item, "gmfgraph_FigureDescriptor", self)
                    

class gmfgraph_Pin(Identity):

    def __init__(self, gmfgraph_Pin: "gmfgraph_PinOwner" = None):
        self.gmfgraph_Pin = gmfgraph_Pin
        
        pass
    @property
    def gmfgraph_Pin(self):
        return self.__gmfgraph_Pin

    @gmfgraph_Pin.setter
    def gmfgraph_Pin(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Pin__gmfgraph_Pin", None)
        self.__gmfgraph_Pin = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_PinOwner"):
                opp_val = getattr(old_value, "gmfgraph_PinOwner", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_PinOwner"):
                opp_val = getattr(value, "gmfgraph_PinOwner", None)
                if opp_val is None:
                    setattr(value, "gmfgraph_PinOwner", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getOperationType(self) :
        # TODO: Implement getOperationType method
        pass

    def getOperationName(self) :
        # TODO: Implement getOperationName method
        pass

class gmfgraph_Canvas(Identity):

    pass
class gmfgraph_Layout(ABC):

    pass
class gmfgraph_Border(ABC):

    pass
class gmfgraph_FigureDescriptor(Identity):

    pass
class gmfgraph_RealFigure(PinOwner, CustomAttributeOwner, AbstractFigure):

    def __init__(self, name: str, gmfgraph_RealFigure: "gmfgraph_FigureGallery" = None, gmfgraph_RealFigure70: set["gmfgraph_Figure"] = None, gmfgraph_RealFigure73: "gmfgraph_FigureRef" = None, gmfgraph_RealFigure84: "gmfgraph_FigureAccessor" = None):
        self.name = name
        self.gmfgraph_RealFigure = gmfgraph_RealFigure
        self.gmfgraph_RealFigure70 = gmfgraph_RealFigure70 if gmfgraph_RealFigure70 is not None else set()
        self.gmfgraph_RealFigure73 = gmfgraph_RealFigure73
        self.gmfgraph_RealFigure84 = gmfgraph_RealFigure84
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def gmfgraph_RealFigure(self):
        return self.__gmfgraph_RealFigure

    @gmfgraph_RealFigure.setter
    def gmfgraph_RealFigure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_RealFigure__gmfgraph_RealFigure", None)
        self.__gmfgraph_RealFigure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_FigureGallery10"):
                opp_val = getattr(old_value, "gmfgraph_FigureGallery10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_FigureGallery10"):
                opp_val = getattr(value, "gmfgraph_FigureGallery10", None)
                if opp_val is None:
                    setattr(value, "gmfgraph_FigureGallery10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gmfgraph_RealFigure84(self):
        return self.__gmfgraph_RealFigure84

    @gmfgraph_RealFigure84.setter
    def gmfgraph_RealFigure84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_RealFigure__gmfgraph_RealFigure84", None)
        self.__gmfgraph_RealFigure84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_FigureAccessor"):
                opp_val = getattr(old_value, "gmfgraph_FigureAccessor", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_FigureAccessor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_FigureAccessor"):
                opp_val = getattr(value, "gmfgraph_FigureAccessor", None)
                setattr(value, "gmfgraph_FigureAccessor", self)

    @property
    def gmfgraph_RealFigure70(self):
        return self.__gmfgraph_RealFigure70

    @gmfgraph_RealFigure70.setter
    def gmfgraph_RealFigure70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_RealFigure__gmfgraph_RealFigure70", None)
        self.__gmfgraph_RealFigure70 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gmfgraph_Figure71"):
                    opp_val = getattr(item, "gmfgraph_Figure71", None)
                    
                    if opp_val == self:
                        setattr(item, "gmfgraph_Figure71", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gmfgraph_Figure71"):
                    opp_val = getattr(item, "gmfgraph_Figure71", None)
                    
                    setattr(item, "gmfgraph_Figure71", self)
                    

    @property
    def gmfgraph_RealFigure73(self):
        return self.__gmfgraph_RealFigure73

    @gmfgraph_RealFigure73.setter
    def gmfgraph_RealFigure73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_RealFigure__gmfgraph_RealFigure73", None)
        self.__gmfgraph_RealFigure73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_FigureRef"):
                opp_val = getattr(old_value, "gmfgraph_FigureRef", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_FigureRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_FigureRef"):
                opp_val = getattr(value, "gmfgraph_FigureRef", None)
                setattr(value, "gmfgraph_FigureRef", self)

class gmfgraph_DiagramLabel(Node):

    def __init__(self, elementIcon: bool, external: bool, gmfgraph_DiagramLabel: "gmfgraph_Canvas" = None, gmfgraph_DiagramLabel27: "gmfgraph_ChildAccess" = None, gmfgraph_DiagramLabel30: "gmfgraph_ChildAccess" = None):
        self.elementIcon = elementIcon
        self.external = external
        self.gmfgraph_DiagramLabel = gmfgraph_DiagramLabel
        self.gmfgraph_DiagramLabel27 = gmfgraph_DiagramLabel27
        self.gmfgraph_DiagramLabel30 = gmfgraph_DiagramLabel30
        
        pass
    @property
    def external(self):
        return self.__external

    @external.setter
    def external(self, external: bool):
        self.__external = external


    @property
    def elementIcon(self):
        return self.__elementIcon

    @elementIcon.setter
    def elementIcon(self, elementIcon: bool):
        self.__elementIcon = elementIcon


    @property
    def gmfgraph_DiagramLabel30(self):
        return self.__gmfgraph_DiagramLabel30

    @gmfgraph_DiagramLabel30.setter
    def gmfgraph_DiagramLabel30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_DiagramLabel__gmfgraph_DiagramLabel30", None)
        self.__gmfgraph_DiagramLabel30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_ChildAccess31"):
                opp_val = getattr(old_value, "gmfgraph_ChildAccess31", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_ChildAccess31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_ChildAccess31"):
                opp_val = getattr(value, "gmfgraph_ChildAccess31", None)
                setattr(value, "gmfgraph_ChildAccess31", self)

    @property
    def gmfgraph_DiagramLabel(self):
        return self.__gmfgraph_DiagramLabel

    @gmfgraph_DiagramLabel.setter
    def gmfgraph_DiagramLabel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_DiagramLabel__gmfgraph_DiagramLabel", None)
        self.__gmfgraph_DiagramLabel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_Canvas8"):
                opp_val = getattr(old_value, "gmfgraph_Canvas8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Canvas8"):
                opp_val = getattr(value, "gmfgraph_Canvas8", None)
                if opp_val is None:
                    setattr(value, "gmfgraph_Canvas8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gmfgraph_DiagramLabel27(self):
        return self.__gmfgraph_DiagramLabel27

    @gmfgraph_DiagramLabel27.setter
    def gmfgraph_DiagramLabel27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_DiagramLabel__gmfgraph_DiagramLabel27", None)
        self.__gmfgraph_DiagramLabel27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_ChildAccess28"):
                opp_val = getattr(old_value, "gmfgraph_ChildAccess28", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_ChildAccess28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_ChildAccess28"):
                opp_val = getattr(value, "gmfgraph_ChildAccess28", None)
                setattr(value, "gmfgraph_ChildAccess28", self)

class gmfgraph_Compartment(DiagramElement):

    def __init__(self, collapsible: bool, needsTitle: bool, gmfgraph_Compartment: "gmfgraph_Canvas" = None, gmfgraph_Compartment24: "gmfgraph_ChildAccess" = None):
        self.collapsible = collapsible
        self.needsTitle = needsTitle
        self.gmfgraph_Compartment = gmfgraph_Compartment
        self.gmfgraph_Compartment24 = gmfgraph_Compartment24
        
        pass
    @property
    def needsTitle(self):
        return self.__needsTitle

    @needsTitle.setter
    def needsTitle(self, needsTitle: bool):
        self.__needsTitle = needsTitle


    @property
    def collapsible(self):
        return self.__collapsible

    @collapsible.setter
    def collapsible(self, collapsible: bool):
        self.__collapsible = collapsible


    @property
    def gmfgraph_Compartment24(self):
        return self.__gmfgraph_Compartment24

    @gmfgraph_Compartment24.setter
    def gmfgraph_Compartment24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Compartment__gmfgraph_Compartment24", None)
        self.__gmfgraph_Compartment24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_ChildAccess25"):
                opp_val = getattr(old_value, "gmfgraph_ChildAccess25", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_ChildAccess25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_ChildAccess25"):
                opp_val = getattr(value, "gmfgraph_ChildAccess25", None)
                setattr(value, "gmfgraph_ChildAccess25", self)

    @property
    def gmfgraph_Compartment(self):
        return self.__gmfgraph_Compartment

    @gmfgraph_Compartment.setter
    def gmfgraph_Compartment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Compartment__gmfgraph_Compartment", None)
        self.__gmfgraph_Compartment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_Canvas6"):
                opp_val = getattr(old_value, "gmfgraph_Canvas6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Canvas6"):
                opp_val = getattr(value, "gmfgraph_Canvas6", None)
                if opp_val is None:
                    setattr(value, "gmfgraph_Canvas6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
