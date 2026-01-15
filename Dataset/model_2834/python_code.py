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


############################################
# Definition of Classes
############################################

class Layout:

    pass
class gmfgraph_FlowLayout(Layout):

    def __init__(self, forceSingleLine: bool, majorAlignment: str, minorAlignment: str, majorSpacing: int, minorSpacing: int, vertical: bool, matchMinorSize: bool):
        self.forceSingleLine = forceSingleLine
        self.majorAlignment = majorAlignment
        self.minorAlignment = minorAlignment
        self.majorSpacing = majorSpacing
        self.minorSpacing = minorSpacing
        self.vertical = vertical
        self.matchMinorSize = matchMinorSize
        
    @property
    def vertical(self) -> bool:
        return self.__vertical

    @vertical.setter
    def vertical(self, vertical: bool):
        self.__vertical = vertical

    @property
    def minorSpacing(self) -> int:
        return self.__minorSpacing

    @minorSpacing.setter
    def minorSpacing(self, minorSpacing: int):
        self.__minorSpacing = minorSpacing

    @property
    def majorAlignment(self) -> str:
        return self.__majorAlignment

    @majorAlignment.setter
    def majorAlignment(self, majorAlignment: str):
        self.__majorAlignment = majorAlignment

    @property
    def minorAlignment(self) -> str:
        return self.__minorAlignment

    @minorAlignment.setter
    def minorAlignment(self, minorAlignment: str):
        self.__minorAlignment = minorAlignment

    @property
    def matchMinorSize(self) -> bool:
        return self.__matchMinorSize

    @matchMinorSize.setter
    def matchMinorSize(self, matchMinorSize: bool):
        self.__matchMinorSize = matchMinorSize

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

class gmfgraph_BorderLayout(Layout):

    pass
class gmfgraph_GridLayout(Layout):

    def __init__(self, numColumns: int, equalWidth: bool, gmfgraph_GridLayout: "gmfgraph_Dimension" = None, gmfgraph_GridLayout80: "gmfgraph_Dimension" = None):
        self.numColumns = numColumns
        self.equalWidth = equalWidth
        self.gmfgraph_GridLayout = gmfgraph_GridLayout
        self.gmfgraph_GridLayout80 = gmfgraph_GridLayout80
        
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
    def gmfgraph_GridLayout80(self):
        return self.__gmfgraph_GridLayout80

    @gmfgraph_GridLayout80.setter
    def gmfgraph_GridLayout80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_GridLayout__gmfgraph_GridLayout80", None)
        self.__gmfgraph_GridLayout80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_Dimension81"):
                opp_val = getattr(old_value, "gmfgraph_Dimension81", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_Dimension81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Dimension81"):
                opp_val = getattr(value, "gmfgraph_Dimension81", None)
                setattr(value, "gmfgraph_Dimension81", self)

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
            if hasattr(old_value, "gmfgraph_Dimension78"):
                opp_val = getattr(old_value, "gmfgraph_Dimension78", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_Dimension78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Dimension78"):
                opp_val = getattr(value, "gmfgraph_Dimension78", None)
                setattr(value, "gmfgraph_Dimension78", self)

class gmfgraph_Layout(ABC):

    pass
class gmfgraph_StackLayout(Layout):

    pass
class gmfgraph_XYLayout(Layout):

    pass
class LayoutData:

    pass
class gmfgraph_XYLayoutData(LayoutData):

    pass
class gmfgraph_Layoutable(ABC):

    pass
class gmfgraph_LayoutData(ABC):

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

    def __init__(self, grabExcessHorizontalSpace: bool, grabExcessVerticalSpace: bool, verticalAlignment: str, horizontalAlignment: str, verticalSpan: int, horizontalSpan: int, horizontalIndent: int, gmfgraph_GridLayoutData: "gmfgraph_Dimension" = None):
        self.grabExcessHorizontalSpace = grabExcessHorizontalSpace
        self.grabExcessVerticalSpace = grabExcessVerticalSpace
        self.verticalAlignment = verticalAlignment
        self.horizontalAlignment = horizontalAlignment
        self.verticalSpan = verticalSpan
        self.horizontalSpan = horizontalSpan
        self.horizontalIndent = horizontalIndent
        self.gmfgraph_GridLayoutData = gmfgraph_GridLayoutData
        
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
    def horizontalAlignment(self) -> str:
        return self.__horizontalAlignment

    @horizontalAlignment.setter
    def horizontalAlignment(self, horizontalAlignment: str):
        self.__horizontalAlignment = horizontalAlignment

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
    def gmfgraph_GridLayoutData(self):
        return self.__gmfgraph_GridLayoutData

    @gmfgraph_GridLayoutData.setter
    def gmfgraph_GridLayoutData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_GridLayoutData__gmfgraph_GridLayoutData", None)
        self.__gmfgraph_GridLayoutData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_Dimension74"):
                opp_val = getattr(old_value, "gmfgraph_Dimension74", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_Dimension74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Dimension74"):
                opp_val = getattr(value, "gmfgraph_Dimension74", None)
                setattr(value, "gmfgraph_Dimension74", self)

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

class Border:

    pass
class gmfgraph_CompoundBorder(Border):

    pass
class gmfgraph_MarginBorder(Border):

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
            if hasattr(old_value, "gmfgraph_Color64"):
                opp_val = getattr(old_value, "gmfgraph_Color64", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_Color64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Color64"):
                opp_val = getattr(value, "gmfgraph_Color64", None)
                setattr(value, "gmfgraph_Color64", self)

class gmfgraph_CustomAttribute:

    def __init__(self, name: str, value: str, directAccess: bool, multiStatementValue: bool, gmfgraph_CustomAttribute: "gmfgraph_CustomClass" = None):
        self.name = name
        self.value = value
        self.directAccess = directAccess
        self.multiStatementValue = multiStatementValue
        self.gmfgraph_CustomAttribute = gmfgraph_CustomAttribute
        
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

    def __init__(self, qualifiedClassName: str, bundleName: str, gmfgraph_CustomClass: set["gmfgraph_CustomAttribute"] = None):
        self.qualifiedClassName = qualifiedClassName
        self.bundleName = bundleName
        self.gmfgraph_CustomClass = gmfgraph_CustomClass if gmfgraph_CustomClass is not None else set()
        
    @property
    def bundleName(self) -> str:
        return self.__bundleName

    @bundleName.setter
    def bundleName(self, bundleName: str):
        self.__bundleName = bundleName

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
    def green(self) -> int:
        return self.__green

    @green.setter
    def green(self, green: int):
        self.__green = green

    @property
    def blue(self) -> int:
        return self.__blue

    @blue.setter
    def blue(self, blue: int):
        self.__blue = blue

class CustomFigure:

    pass
class gmfgraph_CustomDecoration(CustomFigure, DecorationFigure):

    pass
class CustomClass:

    pass
class gmfgraph_CustomLayout(Layout, CustomClass):

    pass
class gmfgraph_CustomBorder(Border, CustomClass):

    pass
class gmfgraph_CustomLayoutData(LayoutData, CustomClass):

    pass
class Shape:

    pass
class gmfgraph_RoundedRectangle(Shape):

    def __init__(self, cornerHeight: int, cornerWidth: int):
        self.cornerHeight = cornerHeight
        self.cornerWidth = cornerWidth
        
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

class gmfgraph_Rectangle(Shape):

    pass
class ConnectionFigure:

    pass
class gmfgraph_CustomConnection(ConnectionFigure, CustomFigure):

    pass
class Polygon:

    pass
class gmfgraph_PolygonDecoration(Polygon, DecorationFigure):

    pass
class gmfgraph_ScalablePolygon(Polygon):

    pass
class Polyline:

    pass
class gmfgraph_PolylineDecoration(Polyline, DecorationFigure):

    pass
class gmfgraph_PolylineConnection(ConnectionFigure, Polyline):

    pass
class gmfgraph_Polygon(Polyline):

    pass
class gmfgraph_Polyline(Shape):

    pass
class gmfgraph_Ellipse(Shape):

    pass
class gmfgraph_Insets:

    def __init__(self, top: int, left: int, bottom: int, right: int, gmfgraph_Insets: "gmfgraph_Figure" = None, gmfgraph_Insets66: "gmfgraph_MarginBorder" = None):
        self.top = top
        self.left = left
        self.bottom = bottom
        self.right = right
        self.gmfgraph_Insets = gmfgraph_Insets
        self.gmfgraph_Insets66 = gmfgraph_Insets66
        
    @property
    def left(self) -> int:
        return self.__left

    @left.setter
    def left(self, left: int):
        self.__left = left

    @property
    def top(self) -> int:
        return self.__top

    @top.setter
    def top(self, top: int):
        self.__top = top

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
    def gmfgraph_Insets66(self):
        return self.__gmfgraph_Insets66

    @gmfgraph_Insets66.setter
    def gmfgraph_Insets66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Insets__gmfgraph_Insets66", None)
        self.__gmfgraph_Insets66 = value
        
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
            if hasattr(old_value, "gmfgraph_Figure40"):
                opp_val = getattr(old_value, "gmfgraph_Figure40", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_Figure40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Figure40"):
                opp_val = getattr(value, "gmfgraph_Figure40", None)
                setattr(value, "gmfgraph_Figure40", self)

class gmfgraph_Font(ABC):

    pass
class gmfgraph_Color(ABC):

    pass
class FigureHandle:

    pass
class gmfgraph_FigureAccessor(FigureHandle):

    def __init__(self, accessor: str, gmfgraph_FigureAccessor62: "gmfgraph_CustomFigure" = None, gmfgraph_FigureAccessor: "gmfgraph_CustomFigure" = None):
        self.accessor = accessor
        self.gmfgraph_FigureAccessor62 = gmfgraph_FigureAccessor62
        self.gmfgraph_FigureAccessor = gmfgraph_FigureAccessor
        
    @property
    def accessor(self) -> str:
        return self.__accessor

    @accessor.setter
    def accessor(self, accessor: str):
        self.__accessor = accessor

    @property
    def gmfgraph_FigureAccessor62(self):
        return self.__gmfgraph_FigureAccessor62

    @gmfgraph_FigureAccessor62.setter
    def gmfgraph_FigureAccessor62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_FigureAccessor__gmfgraph_FigureAccessor62", None)
        self.__gmfgraph_FigureAccessor62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_CustomFigure61"):
                opp_val = getattr(old_value, "gmfgraph_CustomFigure61", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_CustomFigure61"):
                opp_val = getattr(value, "gmfgraph_CustomFigure61", None)
                if opp_val is None:
                    setattr(value, "gmfgraph_CustomFigure61", set([self]))
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
            if hasattr(old_value, "gmfgraph_CustomFigure"):
                opp_val = getattr(old_value, "gmfgraph_CustomFigure", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_CustomFigure", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_CustomFigure"):
                opp_val = getattr(value, "gmfgraph_CustomFigure", None)
                setattr(value, "gmfgraph_CustomFigure", self)

class FigureMarker:

    pass
class Figure:

    pass
class gmfgraph_LabeledContainer(Figure):

    pass
class gmfgraph_Shape(Figure):

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
    def xorOutline(self) -> bool:
        return self.__xorOutline

    @xorOutline.setter
    def xorOutline(self, xorOutline: bool):
        self.__xorOutline = xorOutline

    @property
    def outline(self) -> bool:
        return self.__outline

    @outline.setter
    def outline(self, outline: bool):
        self.__outline = outline

    @property
    def lineWidth(self) -> int:
        return self.__lineWidth

    @lineWidth.setter
    def lineWidth(self, lineWidth: int):
        self.__lineWidth = lineWidth

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
                if hasattr(item, "gmfgraph_Figure51"):
                    opp_val = getattr(item, "gmfgraph_Figure51", None)
                    
                    if opp_val == self:
                        setattr(item, "gmfgraph_Figure51", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gmfgraph_Figure51"):
                    opp_val = getattr(item, "gmfgraph_Figure51", None)
                    
                    setattr(item, "gmfgraph_Figure51", self)
                    

class gmfgraph_Label(Figure):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class gmfgraph_DecorationFigure(Figure):

    pass
class gmfgraph_CustomFigure(Figure, CustomClass):

    pass
class gmfgraph_ConnectionFigure(Figure):

    pass
class gmfgraph_FigureRef(FigureMarker):

    pass
class gmfgraph_Point:

    def __init__(self, x: int, y: int, gmfgraph_Point: "gmfgraph_Figure" = None, gmfgraph_Point47: "gmfgraph_Figure" = None, gmfgraph_Point53: "gmfgraph_Polyline" = None, gmfgraph_Point85: "gmfgraph_XYLayoutData" = None):
        self.x = x
        self.y = y
        self.gmfgraph_Point = gmfgraph_Point
        self.gmfgraph_Point47 = gmfgraph_Point47
        self.gmfgraph_Point53 = gmfgraph_Point53
        self.gmfgraph_Point85 = gmfgraph_Point85
        
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
    def gmfgraph_Point53(self):
        return self.__gmfgraph_Point53

    @gmfgraph_Point53.setter
    def gmfgraph_Point53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Point__gmfgraph_Point53", None)
        self.__gmfgraph_Point53 = value
        
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
    def gmfgraph_Point47(self):
        return self.__gmfgraph_Point47

    @gmfgraph_Point47.setter
    def gmfgraph_Point47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Point__gmfgraph_Point47", None)
        self.__gmfgraph_Point47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_Figure46"):
                opp_val = getattr(old_value, "gmfgraph_Figure46", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_Figure46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Figure46"):
                opp_val = getattr(value, "gmfgraph_Figure46", None)
                setattr(value, "gmfgraph_Figure46", self)

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
    def gmfgraph_Point85(self):
        return self.__gmfgraph_Point85

    @gmfgraph_Point85.setter
    def gmfgraph_Point85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Point__gmfgraph_Point85", None)
        self.__gmfgraph_Point85 = value
        
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

class gmfgraph_Border(ABC):

    pass
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
class Layoutable:

    pass
class gmfgraph_FigureMarker(Layoutable):

    pass
class gmfgraph_Dimension:

    def __init__(self, dx: int, dy: int, gmfgraph_Dimension: "gmfgraph_DefaultSizeFacet" = None, gmfgraph_Dimension30: "gmfgraph_Figure" = None, gmfgraph_Dimension33: "gmfgraph_Figure" = None, gmfgraph_Dimension36: "gmfgraph_Figure" = None, gmfgraph_Dimension74: "gmfgraph_GridLayoutData" = None, gmfgraph_Dimension88: "gmfgraph_XYLayoutData" = None, gmfgraph_Dimension78: "gmfgraph_GridLayout" = None, gmfgraph_Dimension81: "gmfgraph_GridLayout" = None, gmfgraph_Dimension83: "gmfgraph_BorderLayout" = None):
        self.dx = dx
        self.dy = dy
        self.gmfgraph_Dimension = gmfgraph_Dimension
        self.gmfgraph_Dimension30 = gmfgraph_Dimension30
        self.gmfgraph_Dimension33 = gmfgraph_Dimension33
        self.gmfgraph_Dimension36 = gmfgraph_Dimension36
        self.gmfgraph_Dimension74 = gmfgraph_Dimension74
        self.gmfgraph_Dimension88 = gmfgraph_Dimension88
        self.gmfgraph_Dimension78 = gmfgraph_Dimension78
        self.gmfgraph_Dimension81 = gmfgraph_Dimension81
        self.gmfgraph_Dimension83 = gmfgraph_Dimension83
        
    @property
    def dy(self) -> int:
        return self.__dy

    @dy.setter
    def dy(self, dy: int):
        self.__dy = dy

    @property
    def dx(self) -> int:
        return self.__dx

    @dx.setter
    def dx(self, dx: int):
        self.__dx = dx

    @property
    def gmfgraph_Dimension36(self):
        return self.__gmfgraph_Dimension36

    @gmfgraph_Dimension36.setter
    def gmfgraph_Dimension36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Dimension__gmfgraph_Dimension36", None)
        self.__gmfgraph_Dimension36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_Figure35"):
                opp_val = getattr(old_value, "gmfgraph_Figure35", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_Figure35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Figure35"):
                opp_val = getattr(value, "gmfgraph_Figure35", None)
                setattr(value, "gmfgraph_Figure35", self)

    @property
    def gmfgraph_Dimension30(self):
        return self.__gmfgraph_Dimension30

    @gmfgraph_Dimension30.setter
    def gmfgraph_Dimension30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Dimension__gmfgraph_Dimension30", None)
        self.__gmfgraph_Dimension30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_Figure29"):
                opp_val = getattr(old_value, "gmfgraph_Figure29", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_Figure29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Figure29"):
                opp_val = getattr(value, "gmfgraph_Figure29", None)
                setattr(value, "gmfgraph_Figure29", self)

    @property
    def gmfgraph_Dimension83(self):
        return self.__gmfgraph_Dimension83

    @gmfgraph_Dimension83.setter
    def gmfgraph_Dimension83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Dimension__gmfgraph_Dimension83", None)
        self.__gmfgraph_Dimension83 = value
        
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
    def gmfgraph_Dimension33(self):
        return self.__gmfgraph_Dimension33

    @gmfgraph_Dimension33.setter
    def gmfgraph_Dimension33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Dimension__gmfgraph_Dimension33", None)
        self.__gmfgraph_Dimension33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_Figure32"):
                opp_val = getattr(old_value, "gmfgraph_Figure32", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_Figure32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Figure32"):
                opp_val = getattr(value, "gmfgraph_Figure32", None)
                setattr(value, "gmfgraph_Figure32", self)

    @property
    def gmfgraph_Dimension88(self):
        return self.__gmfgraph_Dimension88

    @gmfgraph_Dimension88.setter
    def gmfgraph_Dimension88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Dimension__gmfgraph_Dimension88", None)
        self.__gmfgraph_Dimension88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_XYLayoutData87"):
                opp_val = getattr(old_value, "gmfgraph_XYLayoutData87", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_XYLayoutData87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_XYLayoutData87"):
                opp_val = getattr(value, "gmfgraph_XYLayoutData87", None)
                setattr(value, "gmfgraph_XYLayoutData87", self)

    @property
    def gmfgraph_Dimension81(self):
        return self.__gmfgraph_Dimension81

    @gmfgraph_Dimension81.setter
    def gmfgraph_Dimension81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Dimension__gmfgraph_Dimension81", None)
        self.__gmfgraph_Dimension81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_GridLayout80"):
                opp_val = getattr(old_value, "gmfgraph_GridLayout80", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_GridLayout80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_GridLayout80"):
                opp_val = getattr(value, "gmfgraph_GridLayout80", None)
                setattr(value, "gmfgraph_GridLayout80", self)

    @property
    def gmfgraph_Dimension74(self):
        return self.__gmfgraph_Dimension74

    @gmfgraph_Dimension74.setter
    def gmfgraph_Dimension74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Dimension__gmfgraph_Dimension74", None)
        self.__gmfgraph_Dimension74 = value
        
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
    def gmfgraph_Dimension78(self):
        return self.__gmfgraph_Dimension78

    @gmfgraph_Dimension78.setter
    def gmfgraph_Dimension78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Dimension__gmfgraph_Dimension78", None)
        self.__gmfgraph_Dimension78 = value
        
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

class gmfgraph_DefaultSizeFacet(VisualFacet):

    pass
class gmfgraph_LabelOffsetFacet(VisualFacet):

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

class gmfgraph_GradientFacet(VisualFacet):

    def __init__(self, direction: str):
        self.direction = direction
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

class gmfgraph_DiagramLabel(Node):

    def __init__(self, elementIcon: bool, gmfgraph_DiagramLabel: "gmfgraph_Canvas" = None):
        self.elementIcon = elementIcon
        self.gmfgraph_DiagramLabel = gmfgraph_DiagramLabel
        
    @property
    def elementIcon(self) -> bool:
        return self.__elementIcon

    @elementIcon.setter
    def elementIcon(self, elementIcon: bool):
        self.__elementIcon = elementIcon

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

class Identity:

    pass
class gmfgraph_Figure(Identity, FigureMarker, FigureHandle):

    pass
class gmfgraph_FigureGallery(Identity):

    def __init__(self, implementationBundle: str, gmfgraph_FigureGallery: "gmfgraph_Canvas" = None, gmfgraph_FigureGallery10: set["gmfgraph_Figure"] = None):
        self.implementationBundle = implementationBundle
        self.gmfgraph_FigureGallery = gmfgraph_FigureGallery
        self.gmfgraph_FigureGallery10 = gmfgraph_FigureGallery10 if gmfgraph_FigureGallery10 is not None else set()
        
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
                if hasattr(item, "gmfgraph_Figure"):
                    opp_val = getattr(item, "gmfgraph_Figure", None)
                    
                    if opp_val == self:
                        setattr(item, "gmfgraph_Figure", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gmfgraph_Figure"):
                    opp_val = getattr(item, "gmfgraph_Figure", None)
                    
                    setattr(item, "gmfgraph_Figure", self)
                    

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
class DiagramElement:

    pass
class gmfgraph_Compartment(DiagramElement):

    def __init__(self, collapsible: bool, needsTitle: bool, gmfgraph_Compartment: "gmfgraph_Canvas" = None):
        self.collapsible = collapsible
        self.needsTitle = needsTitle
        self.gmfgraph_Compartment = gmfgraph_Compartment
        
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

class gmfgraph_Node(DiagramElement):

    def __init__(self, resizeConstraint: str, affixedParentSide: str, gmfgraph_Node: "gmfgraph_Canvas" = None, gmfgraph_Node14: "gmfgraph_Figure" = None):
        self.resizeConstraint = resizeConstraint
        self.affixedParentSide = affixedParentSide
        self.gmfgraph_Node = gmfgraph_Node
        self.gmfgraph_Node14 = gmfgraph_Node14
        
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
    def gmfgraph_Node14(self):
        return self.__gmfgraph_Node14

    @gmfgraph_Node14.setter
    def gmfgraph_Node14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Node__gmfgraph_Node14", None)
        self.__gmfgraph_Node14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_Figure15"):
                opp_val = getattr(old_value, "gmfgraph_Figure15", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_Figure15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Figure15"):
                opp_val = getattr(value, "gmfgraph_Figure15", None)
                setattr(value, "gmfgraph_Figure15", self)

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

class gmfgraph_Connection(DiagramElement):

    pass
class gmfgraph_VisualFacet(ABC):

    pass
class gmfgraph_FigureHandle(ABC):

    pass
class gmfgraph_DiagramElement(Identity):

    def __init__(self, referencingElements: "gmfgraph_FigureHandle" = None, gmfgraph_DiagramElement: set["gmfgraph_VisualFacet"] = None, DiagramElement: "gmfgraph_FigureHandle" = None):
        self.referencingElements = referencingElements
        self.gmfgraph_DiagramElement = gmfgraph_DiagramElement if gmfgraph_DiagramElement is not None else set()
        self.DiagramElement = DiagramElement
        
    @property
    def referencingElements(self):
        return self.__referencingElements

    @referencingElements.setter
    def referencingElements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_DiagramElement__referencingElements", None)
        self.__referencingElements = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FigureHandle"):
                opp_val = getattr(old_value, "FigureHandle", None)
                if opp_val == self:
                    setattr(old_value, "FigureHandle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FigureHandle"):
                opp_val = getattr(value, "FigureHandle", None)
                setattr(value, "FigureHandle", self)

    @property
    def DiagramElement(self):
        return self.__DiagramElement

    @DiagramElement.setter
    def DiagramElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_DiagramElement__DiagramElement", None)
        self.__DiagramElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "figure"):
                opp_val = getattr(old_value, "figure", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "figure"):
                opp_val = getattr(value, "figure", None)
                if opp_val is None:
                    setattr(value, "figure", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gmfgraph_DiagramElement(self):
        return self.__gmfgraph_DiagramElement

    @gmfgraph_DiagramElement.setter
    def gmfgraph_DiagramElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_DiagramElement__gmfgraph_DiagramElement", None)
        self.__gmfgraph_DiagramElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gmfgraph_VisualFacet"):
                    opp_val = getattr(item, "gmfgraph_VisualFacet", None)
                    
                    if opp_val == self:
                        setattr(item, "gmfgraph_VisualFacet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gmfgraph_VisualFacet"):
                    opp_val = getattr(item, "gmfgraph_VisualFacet", None)
                    
                    setattr(item, "gmfgraph_VisualFacet", self)
                    

    def find(self, facetClass: str) -> str:
        # TODO: Implement find method
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
