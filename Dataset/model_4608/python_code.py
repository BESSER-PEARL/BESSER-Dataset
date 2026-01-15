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
class LineKind(Enum):
    LINE_SOLID = "LINE_SOLID"
    LINE_DASH = "LINE_DASH"
    LINE_DOT = "LINE_DOT"
    LINE_DASHDOT = "LINE_DASHDOT"
    LINE_DASHDOTDOT = "LINE_DASHDOTDOT"
    LINE_CUSTOM = "LINE_CUSTOM"
class FontStyle(Enum):
    NORMAL = "NORMAL"
    BOLD = "BOLD"
    ITALIC = "ITALIC"
class Alignment(Enum):
    BEGINNING = "BEGINNING"
    CENTER = "CENTER"
    END = "END"
    FILL = "FILL"


############################################
# Definition of Classes
############################################

class Layout:

    pass
class gmfgraph_StackLayout(Layout):

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
    def majorSpacing(self) -> int:
        return self.__majorSpacing

    @majorSpacing.setter
    def majorSpacing(self, majorSpacing: int):
        self.__majorSpacing = majorSpacing

    @property
    def minorSpacing(self) -> int:
        return self.__minorSpacing

    @minorSpacing.setter
    def minorSpacing(self, minorSpacing: int):
        self.__minorSpacing = minorSpacing

    @property
    def vertical(self) -> bool:
        return self.__vertical

    @vertical.setter
    def vertical(self, vertical: bool):
        self.__vertical = vertical

    @property
    def matchMinorSize(self) -> bool:
        return self.__matchMinorSize

    @matchMinorSize.setter
    def matchMinorSize(self, matchMinorSize: bool):
        self.__matchMinorSize = matchMinorSize

    @property
    def minorAlignment(self) -> str:
        return self.__minorAlignment

    @minorAlignment.setter
    def minorAlignment(self, minorAlignment: str):
        self.__minorAlignment = minorAlignment

class gmfgraph_GridLayout(Layout):

    def __init__(self, numColumns: int, equalWidth: bool, gmfgraph_GridLayout: "gmfgraph_Dimension" = None, gmfgraph_GridLayout100: "gmfgraph_Dimension" = None):
        self.numColumns = numColumns
        self.equalWidth = equalWidth
        self.gmfgraph_GridLayout = gmfgraph_GridLayout
        self.gmfgraph_GridLayout100 = gmfgraph_GridLayout100
        
    @property
    def equalWidth(self) -> bool:
        return self.__equalWidth

    @equalWidth.setter
    def equalWidth(self, equalWidth: bool):
        self.__equalWidth = equalWidth

    @property
    def numColumns(self) -> int:
        return self.__numColumns

    @numColumns.setter
    def numColumns(self, numColumns: int):
        self.__numColumns = numColumns

    @property
    def gmfgraph_GridLayout100(self):
        return self.__gmfgraph_GridLayout100

    @gmfgraph_GridLayout100.setter
    def gmfgraph_GridLayout100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_GridLayout__gmfgraph_GridLayout100", None)
        self.__gmfgraph_GridLayout100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_Dimension101"):
                opp_val = getattr(old_value, "gmfgraph_Dimension101", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_Dimension101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Dimension101"):
                opp_val = getattr(value, "gmfgraph_Dimension101", None)
                setattr(value, "gmfgraph_Dimension101", self)

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
            if hasattr(old_value, "gmfgraph_Dimension98"):
                opp_val = getattr(old_value, "gmfgraph_Dimension98", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_Dimension98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Dimension98"):
                opp_val = getattr(value, "gmfgraph_Dimension98", None)
                setattr(value, "gmfgraph_Dimension98", self)

class gmfgraph_XYLayout(Layout):

    pass
class gmfgraph_BorderLayout(Layout):

    pass
class gmfgraph_Layout(ABC):

    pass
class LayoutData:

    pass
class gmfgraph_BorderLayoutData(LayoutData):

    def __init__(self, alignment: str, vertical: bool):
        self.alignment = alignment
        self.vertical = vertical
        
    @property
    def alignment(self) -> str:
        return self.__alignment

    @alignment.setter
    def alignment(self, alignment: str):
        self.__alignment = alignment

    @property
    def vertical(self) -> bool:
        return self.__vertical

    @vertical.setter
    def vertical(self, vertical: bool):
        self.__vertical = vertical

class gmfgraph_GridLayoutData(LayoutData):

    def __init__(self, grabExcessHorizontalSpace: bool, grabExcessVerticalSpace: bool, horizontalSpan: int, horizontalIndent: int, verticalAlignment: str, horizontalAlignment: str, verticalSpan: int, gmfgraph_GridLayoutData: "gmfgraph_Dimension" = None):
        self.grabExcessHorizontalSpace = grabExcessHorizontalSpace
        self.grabExcessVerticalSpace = grabExcessVerticalSpace
        self.horizontalSpan = horizontalSpan
        self.horizontalIndent = horizontalIndent
        self.verticalAlignment = verticalAlignment
        self.horizontalAlignment = horizontalAlignment
        self.verticalSpan = verticalSpan
        self.gmfgraph_GridLayoutData = gmfgraph_GridLayoutData
        
    @property
    def verticalSpan(self) -> int:
        return self.__verticalSpan

    @verticalSpan.setter
    def verticalSpan(self, verticalSpan: int):
        self.__verticalSpan = verticalSpan

    @property
    def verticalAlignment(self) -> str:
        return self.__verticalAlignment

    @verticalAlignment.setter
    def verticalAlignment(self, verticalAlignment: str):
        self.__verticalAlignment = verticalAlignment

    @property
    def grabExcessHorizontalSpace(self) -> bool:
        return self.__grabExcessHorizontalSpace

    @grabExcessHorizontalSpace.setter
    def grabExcessHorizontalSpace(self, grabExcessHorizontalSpace: bool):
        self.__grabExcessHorizontalSpace = grabExcessHorizontalSpace

    @property
    def horizontalSpan(self) -> int:
        return self.__horizontalSpan

    @horizontalSpan.setter
    def horizontalSpan(self, horizontalSpan: int):
        self.__horizontalSpan = horizontalSpan

    @property
    def horizontalAlignment(self) -> str:
        return self.__horizontalAlignment

    @horizontalAlignment.setter
    def horizontalAlignment(self, horizontalAlignment: str):
        self.__horizontalAlignment = horizontalAlignment

    @property
    def horizontalIndent(self) -> int:
        return self.__horizontalIndent

    @horizontalIndent.setter
    def horizontalIndent(self, horizontalIndent: int):
        self.__horizontalIndent = horizontalIndent

    @property
    def grabExcessVerticalSpace(self) -> bool:
        return self.__grabExcessVerticalSpace

    @grabExcessVerticalSpace.setter
    def grabExcessVerticalSpace(self, grabExcessVerticalSpace: bool):
        self.__grabExcessVerticalSpace = grabExcessVerticalSpace

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
            if hasattr(old_value, "gmfgraph_Dimension93"):
                opp_val = getattr(old_value, "gmfgraph_Dimension93", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_Dimension93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Dimension93"):
                opp_val = getattr(value, "gmfgraph_Dimension93", None)
                setattr(value, "gmfgraph_Dimension93", self)

class gmfgraph_XYLayoutData(LayoutData):

    pass
class gmfgraph_Layoutable(ABC):

    pass
class gmfgraph_LayoutData(ABC):

    pass
class Border:

    pass
class gmfgraph_MarginBorder(Border):

    pass
class gmfgraph_CompoundBorder(Border):

    pass
class gmfgraph_LineBorder(Border):

    def __init__(self, width: int, gmfgraph_LineBorder: "gmfgraph_Color" = None):
        self.width = width
        self.gmfgraph_LineBorder = gmfgraph_LineBorder
        
    @property
    def width(self) -> int:
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
            if hasattr(old_value, "gmfgraph_Color83"):
                opp_val = getattr(old_value, "gmfgraph_Color83", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_Color83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Color83"):
                opp_val = getattr(value, "gmfgraph_Color83", None)
                setattr(value, "gmfgraph_Color83", self)

class CustomClass:

    pass
class gmfgraph_CustomBorder(Border, CustomClass):

    pass
class gmfgraph_CustomLayout(Layout, CustomClass):

    pass
class gmfgraph_CustomLayoutData(LayoutData, CustomClass):

    pass
class Font:

    pass
class gmfgraph_BasicFont(Font):

    def __init__(self, faceName: str, height: int, style: str):
        self.faceName = faceName
        self.height = height
        self.style = style
        
    @property
    def faceName(self) -> str:
        return self.__faceName

    @faceName.setter
    def faceName(self, faceName: str):
        self.__faceName = faceName

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

class Color:

    pass
class gmfgraph_ConstantColor(Color):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class gmfgraph_RGBColor(Color):

    def __init__(self, red: int, green: int, blue: int):
        self.red = red
        self.green = green
        self.blue = blue
        
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

    @property
    def green(self) -> int:
        return self.__green

    @green.setter
    def green(self, green: int):
        self.__green = green

class CustomFigure:

    pass
class Shape:

    pass
class gmfgraph_RoundedRectangle(Shape):

    def __init__(self, cornerWidth: int, cornerHeight: int):
        self.cornerWidth = cornerWidth
        self.cornerHeight = cornerHeight
        
    @property
    def cornerWidth(self) -> int:
        return self.__cornerWidth

    @cornerWidth.setter
    def cornerWidth(self, cornerWidth: int):
        self.__cornerWidth = cornerWidth

    @property
    def cornerHeight(self) -> int:
        return self.__cornerHeight

    @cornerHeight.setter
    def cornerHeight(self, cornerHeight: int):
        self.__cornerHeight = cornerHeight

class gmfgraph_FigureAccessor:

    def __init__(self, accessor: str, gmfgraph_FigureAccessor: "gmfgraph_RealFigure" = None, gmfgraph_FigureAccessor81: "gmfgraph_CustomFigure" = None):
        self.accessor = accessor
        self.gmfgraph_FigureAccessor = gmfgraph_FigureAccessor
        self.gmfgraph_FigureAccessor81 = gmfgraph_FigureAccessor81
        
    @property
    def accessor(self) -> str:
        return self.__accessor

    @accessor.setter
    def accessor(self, accessor: str):
        self.__accessor = accessor

    @property
    def gmfgraph_FigureAccessor81(self):
        return self.__gmfgraph_FigureAccessor81

    @gmfgraph_FigureAccessor81.setter
    def gmfgraph_FigureAccessor81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_FigureAccessor__gmfgraph_FigureAccessor81", None)
        self.__gmfgraph_FigureAccessor81 = value
        
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
            if hasattr(old_value, "gmfgraph_RealFigure79"):
                opp_val = getattr(old_value, "gmfgraph_RealFigure79", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_RealFigure79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_RealFigure79"):
                opp_val = getattr(value, "gmfgraph_RealFigure79", None)
                setattr(value, "gmfgraph_RealFigure79", self)

class gmfgraph_CustomAttribute:

    def __init__(self, name: str, value: str, directAccess: bool, multiStatementValue: bool, gmfgraph_CustomAttribute: "gmfgraph_CustomClass" = None):
        self.name = name
        self.value = value
        self.directAccess = directAccess
        self.multiStatementValue = multiStatementValue
        self.gmfgraph_CustomAttribute = gmfgraph_CustomAttribute
        
    @property
    def multiStatementValue(self) -> bool:
        return self.__multiStatementValue

    @multiStatementValue.setter
    def multiStatementValue(self, multiStatementValue: bool):
        self.__multiStatementValue = multiStatementValue

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def directAccess(self) -> bool:
        return self.__directAccess

    @directAccess.setter
    def directAccess(self, directAccess: bool):
        self.__directAccess = directAccess

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
            if hasattr(old_value, "gmfgraph_CustomClass"):
                opp_val = getattr(old_value, "gmfgraph_CustomClass", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_CustomClass"):
                opp_val = getattr(value, "gmfgraph_CustomClass", None)
                if opp_val is None:
                    setattr(value, "gmfgraph_CustomClass", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class gmfgraph_CustomClass(ABC):

    def __init__(self, qualifiedClassName: str, gmfgraph_CustomClass: set["gmfgraph_CustomAttribute"] = None):
        self.qualifiedClassName = qualifiedClassName
        self.gmfgraph_CustomClass = gmfgraph_CustomClass if gmfgraph_CustomClass is not None else set()
        
    @property
    def qualifiedClassName(self) -> str:
        return self.__qualifiedClassName

    @qualifiedClassName.setter
    def qualifiedClassName(self, qualifiedClassName: str):
        self.__qualifiedClassName = qualifiedClassName

    @property
    def gmfgraph_CustomClass(self):
        return self.__gmfgraph_CustomClass

    @gmfgraph_CustomClass.setter
    def gmfgraph_CustomClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_CustomClass__gmfgraph_CustomClass", None)
        self.__gmfgraph_CustomClass = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gmfgraph_CustomAttribute"):
                    opp_val = getattr(item, "gmfgraph_CustomAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "gmfgraph_CustomAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gmfgraph_CustomAttribute"):
                    opp_val = getattr(item, "gmfgraph_CustomAttribute", None)
                    
                    setattr(item, "gmfgraph_CustomAttribute", self)
                    

class DecorationFigure:

    pass
class gmfgraph_CustomDecoration(CustomFigure, DecorationFigure):

    pass
class ConnectionFigure:

    pass
class gmfgraph_CustomConnection(CustomFigure, ConnectionFigure):

    pass
class Polygon:

    pass
class gmfgraph_PolygonDecoration(Polygon, DecorationFigure):

    pass
class gmfgraph_ScalablePolygon(Polygon):

    pass
class Polyline:

    pass
class gmfgraph_PolylineConnection(ConnectionFigure, Polyline):

    pass
class gmfgraph_PolylineDecoration(Polyline, DecorationFigure):

    pass
class gmfgraph_Polygon(Polyline):

    pass
class gmfgraph_Polyline(Shape):

    pass
class gmfgraph_Ellipse(Shape):

    pass
class gmfgraph_Rectangle(Shape):

    pass
class RealFigure:

    pass
class gmfgraph_Label(RealFigure):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class gmfgraph_Shape(RealFigure):

    def __init__(self, outline: bool, fill: bool, lineWidth: int, lineKind: str, xorFill: bool, xorOutline: bool, gmfgraph_Shape: set["gmfgraph_Figure"] = None):
        self.outline = outline
        self.fill = fill
        self.lineWidth = lineWidth
        self.lineKind = lineKind
        self.xorFill = xorFill
        self.xorOutline = xorOutline
        self.gmfgraph_Shape = gmfgraph_Shape if gmfgraph_Shape is not None else set()
        
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
    def fill(self) -> bool:
        return self.__fill

    @fill.setter
    def fill(self, fill: bool):
        self.__fill = fill

    @property
    def xorFill(self) -> bool:
        return self.__xorFill

    @xorFill.setter
    def xorFill(self, xorFill: bool):
        self.__xorFill = xorFill

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
                if hasattr(item, "gmfgraph_Figure70"):
                    opp_val = getattr(item, "gmfgraph_Figure70", None)
                    
                    if opp_val == self:
                        setattr(item, "gmfgraph_Figure70", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gmfgraph_Figure70"):
                    opp_val = getattr(item, "gmfgraph_Figure70", None)
                    
                    setattr(item, "gmfgraph_Figure70", self)
                    

class gmfgraph_CustomFigure(RealFigure, CustomClass):

    pass
class gmfgraph_DecorationFigure(RealFigure):

    pass
class gmfgraph_LabeledContainer(RealFigure):

    pass
class gmfgraph_ConnectionFigure(RealFigure):

    pass
class AbstractFigure:

    pass
class gmfgraph_FigureRef(AbstractFigure):

    pass
class Figure:

    pass
class gmfgraph_AbstractFigure(Figure):

    pass
class gmfgraph_Point:

    def __init__(self, x: int, y: int, gmfgraph_Point: "gmfgraph_Figure" = None, gmfgraph_Point55: "gmfgraph_Figure" = None, gmfgraph_Point72: "gmfgraph_Polyline" = None, gmfgraph_Point105: "gmfgraph_XYLayoutData" = None):
        self.x = x
        self.y = y
        self.gmfgraph_Point = gmfgraph_Point
        self.gmfgraph_Point55 = gmfgraph_Point55
        self.gmfgraph_Point72 = gmfgraph_Point72
        self.gmfgraph_Point105 = gmfgraph_Point105
        
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

    @property
    def gmfgraph_Point72(self):
        return self.__gmfgraph_Point72

    @gmfgraph_Point72.setter
    def gmfgraph_Point72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Point__gmfgraph_Point72", None)
        self.__gmfgraph_Point72 = value
        
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
            if hasattr(old_value, "gmfgraph_Figure52"):
                opp_val = getattr(old_value, "gmfgraph_Figure52", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_Figure52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Figure52"):
                opp_val = getattr(value, "gmfgraph_Figure52", None)
                setattr(value, "gmfgraph_Figure52", self)

    @property
    def gmfgraph_Point105(self):
        return self.__gmfgraph_Point105

    @gmfgraph_Point105.setter
    def gmfgraph_Point105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Point__gmfgraph_Point105", None)
        self.__gmfgraph_Point105 = value
        
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

    @property
    def gmfgraph_Point55(self):
        return self.__gmfgraph_Point55

    @gmfgraph_Point55.setter
    def gmfgraph_Point55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Point__gmfgraph_Point55", None)
        self.__gmfgraph_Point55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_Figure54"):
                opp_val = getattr(old_value, "gmfgraph_Figure54", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_Figure54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Figure54"):
                opp_val = getattr(value, "gmfgraph_Figure54", None)
                setattr(value, "gmfgraph_Figure54", self)

class gmfgraph_Border(ABC):

    pass
class gmfgraph_Insets:

    def __init__(self, bottom: int, right: int, top: int, left: int, gmfgraph_Insets: "gmfgraph_Figure" = None, gmfgraph_Insets85: "gmfgraph_MarginBorder" = None):
        self.bottom = bottom
        self.right = right
        self.top = top
        self.left = left
        self.gmfgraph_Insets = gmfgraph_Insets
        self.gmfgraph_Insets85 = gmfgraph_Insets85
        
    @property
    def top(self) -> int:
        return self.__top

    @top.setter
    def top(self, top: int):
        self.__top = top

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
    def gmfgraph_Insets85(self):
        return self.__gmfgraph_Insets85

    @gmfgraph_Insets85.setter
    def gmfgraph_Insets85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Insets__gmfgraph_Insets85", None)
        self.__gmfgraph_Insets85 = value
        
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
            if hasattr(old_value, "gmfgraph_Figure48"):
                opp_val = getattr(old_value, "gmfgraph_Figure48", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_Figure48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Figure48"):
                opp_val = getattr(value, "gmfgraph_Figure48", None)
                setattr(value, "gmfgraph_Figure48", self)

class gmfgraph_Font(ABC):

    pass
class gmfgraph_Color(ABC):

    pass
class Layoutable:

    pass
class gmfgraph_Figure(Layoutable):

    pass
class gmfgraph_Dimension:

    def __init__(self, dx: int, dy: int, gmfgraph_Dimension: "gmfgraph_DefaultSizeFacet" = None, gmfgraph_Dimension38: "gmfgraph_Figure" = None, gmfgraph_Dimension41: "gmfgraph_Figure" = None, gmfgraph_Dimension44: "gmfgraph_Figure" = None, gmfgraph_Dimension93: "gmfgraph_GridLayoutData" = None, gmfgraph_Dimension98: "gmfgraph_GridLayout" = None, gmfgraph_Dimension101: "gmfgraph_GridLayout" = None, gmfgraph_Dimension103: "gmfgraph_BorderLayout" = None, gmfgraph_Dimension108: "gmfgraph_XYLayoutData" = None):
        self.dx = dx
        self.dy = dy
        self.gmfgraph_Dimension = gmfgraph_Dimension
        self.gmfgraph_Dimension38 = gmfgraph_Dimension38
        self.gmfgraph_Dimension41 = gmfgraph_Dimension41
        self.gmfgraph_Dimension44 = gmfgraph_Dimension44
        self.gmfgraph_Dimension93 = gmfgraph_Dimension93
        self.gmfgraph_Dimension98 = gmfgraph_Dimension98
        self.gmfgraph_Dimension101 = gmfgraph_Dimension101
        self.gmfgraph_Dimension103 = gmfgraph_Dimension103
        self.gmfgraph_Dimension108 = gmfgraph_Dimension108
        
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

    @property
    def gmfgraph_Dimension98(self):
        return self.__gmfgraph_Dimension98

    @gmfgraph_Dimension98.setter
    def gmfgraph_Dimension98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Dimension__gmfgraph_Dimension98", None)
        self.__gmfgraph_Dimension98 = value
        
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
    def gmfgraph_Dimension38(self):
        return self.__gmfgraph_Dimension38

    @gmfgraph_Dimension38.setter
    def gmfgraph_Dimension38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Dimension__gmfgraph_Dimension38", None)
        self.__gmfgraph_Dimension38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_Figure37"):
                opp_val = getattr(old_value, "gmfgraph_Figure37", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_Figure37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Figure37"):
                opp_val = getattr(value, "gmfgraph_Figure37", None)
                setattr(value, "gmfgraph_Figure37", self)

    @property
    def gmfgraph_Dimension103(self):
        return self.__gmfgraph_Dimension103

    @gmfgraph_Dimension103.setter
    def gmfgraph_Dimension103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Dimension__gmfgraph_Dimension103", None)
        self.__gmfgraph_Dimension103 = value
        
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
    def gmfgraph_Dimension108(self):
        return self.__gmfgraph_Dimension108

    @gmfgraph_Dimension108.setter
    def gmfgraph_Dimension108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Dimension__gmfgraph_Dimension108", None)
        self.__gmfgraph_Dimension108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_XYLayoutData107"):
                opp_val = getattr(old_value, "gmfgraph_XYLayoutData107", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_XYLayoutData107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_XYLayoutData107"):
                opp_val = getattr(value, "gmfgraph_XYLayoutData107", None)
                setattr(value, "gmfgraph_XYLayoutData107", self)

    @property
    def gmfgraph_Dimension41(self):
        return self.__gmfgraph_Dimension41

    @gmfgraph_Dimension41.setter
    def gmfgraph_Dimension41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Dimension__gmfgraph_Dimension41", None)
        self.__gmfgraph_Dimension41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_Figure40"):
                opp_val = getattr(old_value, "gmfgraph_Figure40", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_Figure40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Figure40"):
                opp_val = getattr(value, "gmfgraph_Figure40", None)
                setattr(value, "gmfgraph_Figure40", self)

    @property
    def gmfgraph_Dimension44(self):
        return self.__gmfgraph_Dimension44

    @gmfgraph_Dimension44.setter
    def gmfgraph_Dimension44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Dimension__gmfgraph_Dimension44", None)
        self.__gmfgraph_Dimension44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_Figure43"):
                opp_val = getattr(old_value, "gmfgraph_Figure43", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_Figure43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Figure43"):
                opp_val = getattr(value, "gmfgraph_Figure43", None)
                setattr(value, "gmfgraph_Figure43", self)

    @property
    def gmfgraph_Dimension101(self):
        return self.__gmfgraph_Dimension101

    @gmfgraph_Dimension101.setter
    def gmfgraph_Dimension101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Dimension__gmfgraph_Dimension101", None)
        self.__gmfgraph_Dimension101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_GridLayout100"):
                opp_val = getattr(old_value, "gmfgraph_GridLayout100", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_GridLayout100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_GridLayout100"):
                opp_val = getattr(value, "gmfgraph_GridLayout100", None)
                setattr(value, "gmfgraph_GridLayout100", self)

    @property
    def gmfgraph_Dimension93(self):
        return self.__gmfgraph_Dimension93

    @gmfgraph_Dimension93.setter
    def gmfgraph_Dimension93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Dimension__gmfgraph_Dimension93", None)
        self.__gmfgraph_Dimension93 = value
        
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

class VisualFacet:

    pass
class gmfgraph_AlignmentFacet(VisualFacet):

    def __init__(self, alignment: str):
        self.alignment = alignment
        
    @property
    def alignment(self) -> str:
        return self.__alignment

    @alignment.setter
    def alignment(self, alignment: str):
        self.__alignment = alignment

class gmfgraph_GradientFacet(VisualFacet):

    def __init__(self, direction: str):
        self.direction = direction
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

class gmfgraph_LabelOffsetFacet(VisualFacet):

    def __init__(self, y: int, x: int):
        self.y = y
        self.x = x
        
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

class gmfgraph_DefaultSizeFacet(VisualFacet):

    pass
class gmfgraph_GeneralFacet(VisualFacet):

    def __init__(self, identifier: str, data: str):
        self.identifier = identifier
        self.data = data
        
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

class Node:

    pass
class gmfgraph_ChildAccess:

    def __init__(self, accessor: str, gmfgraph_ChildAccess: "gmfgraph_Node" = None, gmfgraph_ChildAccess21: "gmfgraph_Compartment" = None, gmfgraph_ChildAccess24: "gmfgraph_DiagramLabel" = None, gmfgraph_ChildAccess27: "gmfgraph_DiagramLabel" = None, accessors: "gmfgraph_FigureDescriptor" = None, gmfgraph_ChildAccess62: "gmfgraph_Figure" = None, ChildAccess: "gmfgraph_FigureDescriptor" = None):
        self.accessor = accessor
        self.gmfgraph_ChildAccess = gmfgraph_ChildAccess
        self.gmfgraph_ChildAccess21 = gmfgraph_ChildAccess21
        self.gmfgraph_ChildAccess24 = gmfgraph_ChildAccess24
        self.gmfgraph_ChildAccess27 = gmfgraph_ChildAccess27
        self.accessors = accessors
        self.gmfgraph_ChildAccess62 = gmfgraph_ChildAccess62
        self.ChildAccess = ChildAccess
        
    @property
    def accessor(self) -> str:
        return self.__accessor

    @accessor.setter
    def accessor(self, accessor: str):
        self.__accessor = accessor

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
            if hasattr(old_value, "gmfgraph_Node18"):
                opp_val = getattr(old_value, "gmfgraph_Node18", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_Node18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Node18"):
                opp_val = getattr(value, "gmfgraph_Node18", None)
                setattr(value, "gmfgraph_Node18", self)

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

    @property
    def gmfgraph_ChildAccess24(self):
        return self.__gmfgraph_ChildAccess24

    @gmfgraph_ChildAccess24.setter
    def gmfgraph_ChildAccess24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_ChildAccess__gmfgraph_ChildAccess24", None)
        self.__gmfgraph_ChildAccess24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_DiagramLabel23"):
                opp_val = getattr(old_value, "gmfgraph_DiagramLabel23", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_DiagramLabel23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_DiagramLabel23"):
                opp_val = getattr(value, "gmfgraph_DiagramLabel23", None)
                setattr(value, "gmfgraph_DiagramLabel23", self)

    @property
    def gmfgraph_ChildAccess62(self):
        return self.__gmfgraph_ChildAccess62

    @gmfgraph_ChildAccess62.setter
    def gmfgraph_ChildAccess62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_ChildAccess__gmfgraph_ChildAccess62", None)
        self.__gmfgraph_ChildAccess62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_Figure63"):
                opp_val = getattr(old_value, "gmfgraph_Figure63", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_Figure63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Figure63"):
                opp_val = getattr(value, "gmfgraph_Figure63", None)
                setattr(value, "gmfgraph_Figure63", self)

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
    def gmfgraph_ChildAccess21(self):
        return self.__gmfgraph_ChildAccess21

    @gmfgraph_ChildAccess21.setter
    def gmfgraph_ChildAccess21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_ChildAccess__gmfgraph_ChildAccess21", None)
        self.__gmfgraph_ChildAccess21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_Compartment20"):
                opp_val = getattr(old_value, "gmfgraph_Compartment20", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_Compartment20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Compartment20"):
                opp_val = getattr(value, "gmfgraph_Compartment20", None)
                setattr(value, "gmfgraph_Compartment20", self)

    @property
    def gmfgraph_ChildAccess27(self):
        return self.__gmfgraph_ChildAccess27

    @gmfgraph_ChildAccess27.setter
    def gmfgraph_ChildAccess27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_ChildAccess__gmfgraph_ChildAccess27", None)
        self.__gmfgraph_ChildAccess27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_DiagramLabel26"):
                opp_val = getattr(old_value, "gmfgraph_DiagramLabel26", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_DiagramLabel26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_DiagramLabel26"):
                opp_val = getattr(value, "gmfgraph_DiagramLabel26", None)
                setattr(value, "gmfgraph_DiagramLabel26", self)

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
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class gmfgraph_RealFigure(AbstractFigure):

    def __init__(self, name: str, gmfgraph_RealFigure: "gmfgraph_FigureGallery" = None, gmfgraph_RealFigure65: set["gmfgraph_Figure"] = None, gmfgraph_RealFigure68: "gmfgraph_FigureRef" = None, gmfgraph_RealFigure79: "gmfgraph_FigureAccessor" = None):
        self.name = name
        self.gmfgraph_RealFigure = gmfgraph_RealFigure
        self.gmfgraph_RealFigure65 = gmfgraph_RealFigure65 if gmfgraph_RealFigure65 is not None else set()
        self.gmfgraph_RealFigure68 = gmfgraph_RealFigure68
        self.gmfgraph_RealFigure79 = gmfgraph_RealFigure79
        
    @property
    def name(self) -> str:
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
    def gmfgraph_RealFigure79(self):
        return self.__gmfgraph_RealFigure79

    @gmfgraph_RealFigure79.setter
    def gmfgraph_RealFigure79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_RealFigure__gmfgraph_RealFigure79", None)
        self.__gmfgraph_RealFigure79 = value
        
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
    def gmfgraph_RealFigure65(self):
        return self.__gmfgraph_RealFigure65

    @gmfgraph_RealFigure65.setter
    def gmfgraph_RealFigure65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_RealFigure__gmfgraph_RealFigure65", None)
        self.__gmfgraph_RealFigure65 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gmfgraph_Figure66"):
                    opp_val = getattr(item, "gmfgraph_Figure66", None)
                    
                    if opp_val == self:
                        setattr(item, "gmfgraph_Figure66", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gmfgraph_Figure66"):
                    opp_val = getattr(item, "gmfgraph_Figure66", None)
                    
                    setattr(item, "gmfgraph_Figure66", self)
                    

    @property
    def gmfgraph_RealFigure68(self):
        return self.__gmfgraph_RealFigure68

    @gmfgraph_RealFigure68.setter
    def gmfgraph_RealFigure68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_RealFigure__gmfgraph_RealFigure68", None)
        self.__gmfgraph_RealFigure68 = value
        
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

    def __init__(self, elementIcon: bool, external: bool, gmfgraph_DiagramLabel: "gmfgraph_Canvas" = None, gmfgraph_DiagramLabel23: "gmfgraph_ChildAccess" = None, gmfgraph_DiagramLabel26: "gmfgraph_ChildAccess" = None):
        self.elementIcon = elementIcon
        self.external = external
        self.gmfgraph_DiagramLabel = gmfgraph_DiagramLabel
        self.gmfgraph_DiagramLabel23 = gmfgraph_DiagramLabel23
        self.gmfgraph_DiagramLabel26 = gmfgraph_DiagramLabel26
        
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
    def gmfgraph_DiagramLabel26(self):
        return self.__gmfgraph_DiagramLabel26

    @gmfgraph_DiagramLabel26.setter
    def gmfgraph_DiagramLabel26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_DiagramLabel__gmfgraph_DiagramLabel26", None)
        self.__gmfgraph_DiagramLabel26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_ChildAccess27"):
                opp_val = getattr(old_value, "gmfgraph_ChildAccess27", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_ChildAccess27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_ChildAccess27"):
                opp_val = getattr(value, "gmfgraph_ChildAccess27", None)
                setattr(value, "gmfgraph_ChildAccess27", self)

    @property
    def gmfgraph_DiagramLabel23(self):
        return self.__gmfgraph_DiagramLabel23

    @gmfgraph_DiagramLabel23.setter
    def gmfgraph_DiagramLabel23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_DiagramLabel__gmfgraph_DiagramLabel23", None)
        self.__gmfgraph_DiagramLabel23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_ChildAccess24"):
                opp_val = getattr(old_value, "gmfgraph_ChildAccess24", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_ChildAccess24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_ChildAccess24"):
                opp_val = getattr(value, "gmfgraph_ChildAccess24", None)
                setattr(value, "gmfgraph_ChildAccess24", self)

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

class gmfgraph_Compartment(DiagramElement):

    def __init__(self, collapsible: bool, needsTitle: bool, gmfgraph_Compartment: "gmfgraph_Canvas" = None, gmfgraph_Compartment20: "gmfgraph_ChildAccess" = None):
        self.collapsible = collapsible
        self.needsTitle = needsTitle
        self.gmfgraph_Compartment = gmfgraph_Compartment
        self.gmfgraph_Compartment20 = gmfgraph_Compartment20
        
    @property
    def needsTitle(self) -> bool:
        return self.__needsTitle

    @needsTitle.setter
    def needsTitle(self, needsTitle: bool):
        self.__needsTitle = needsTitle

    @property
    def collapsible(self) -> bool:
        return self.__collapsible

    @collapsible.setter
    def collapsible(self, collapsible: bool):
        self.__collapsible = collapsible

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

    @property
    def gmfgraph_Compartment20(self):
        return self.__gmfgraph_Compartment20

    @gmfgraph_Compartment20.setter
    def gmfgraph_Compartment20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Compartment__gmfgraph_Compartment20", None)
        self.__gmfgraph_Compartment20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_ChildAccess21"):
                opp_val = getattr(old_value, "gmfgraph_ChildAccess21", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_ChildAccess21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_ChildAccess21"):
                opp_val = getattr(value, "gmfgraph_ChildAccess21", None)
                setattr(value, "gmfgraph_ChildAccess21", self)

class gmfgraph_Connection(DiagramElement):

    pass
class gmfgraph_Node(AbstractNode):

    def __init__(self, resizeConstraint: str, affixedParentSide: str, gmfgraph_Node: "gmfgraph_Canvas" = None, gmfgraph_Node18: "gmfgraph_ChildAccess" = None):
        self.resizeConstraint = resizeConstraint
        self.affixedParentSide = affixedParentSide
        self.gmfgraph_Node = gmfgraph_Node
        self.gmfgraph_Node18 = gmfgraph_Node18
        
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
    def gmfgraph_Node18(self):
        return self.__gmfgraph_Node18

    @gmfgraph_Node18.setter
    def gmfgraph_Node18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Node__gmfgraph_Node18", None)
        self.__gmfgraph_Node18 = value
        
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
class gmfgraph_FigureDescriptor(Identity):

    pass
class gmfgraph_FigureGallery(Identity):

    def __init__(self, implementationBundle: str, gmfgraph_FigureGallery: "gmfgraph_Canvas" = None, gmfgraph_FigureGallery10: set["gmfgraph_RealFigure"] = None, gmfgraph_FigureGallery12: set["gmfgraph_FigureDescriptor"] = None):
        self.implementationBundle = implementationBundle
        self.gmfgraph_FigureGallery = gmfgraph_FigureGallery
        self.gmfgraph_FigureGallery10 = gmfgraph_FigureGallery10 if gmfgraph_FigureGallery10 is not None else set()
        self.gmfgraph_FigureGallery12 = gmfgraph_FigureGallery12 if gmfgraph_FigureGallery12 is not None else set()
        
    @property
    def implementationBundle(self) -> str:
        return self.__implementationBundle

    @implementationBundle.setter
    def implementationBundle(self, implementationBundle: str):
        self.__implementationBundle = implementationBundle

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

class gmfgraph_Canvas(Identity):

    pass