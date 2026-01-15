from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

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
class FontStyle(Enum):
    NORMAL = "NORMAL"
    BOLD = "BOLD"
    ITALIC = "ITALIC"


############################################
# Definition of Classes
############################################

class Figure:

    pass
class gmfgraph_AbstractFigure(Figure):

    pass
class LayoutData:

    pass
class gmfgraph_XYLayoutData(LayoutData):

    pass
class gmfgraph_GridLayoutData(LayoutData):

    def __init__(self, horizontalAlignment: str, verticalSpan: int, horizontalSpan: int, horizontalIndent: int, grabExcessHorizontalSpace: bool, grabExcessVerticalSpace: bool, verticalAlignment: str, gmfgraph_GridLayoutData: "gmfgraph_Dimension" = None):
        self.horizontalAlignment = horizontalAlignment
        self.verticalSpan = verticalSpan
        self.horizontalSpan = horizontalSpan
        self.horizontalIndent = horizontalIndent
        self.grabExcessHorizontalSpace = grabExcessHorizontalSpace
        self.grabExcessVerticalSpace = grabExcessVerticalSpace
        self.verticalAlignment = verticalAlignment
        self.gmfgraph_GridLayoutData = gmfgraph_GridLayoutData
        
    @property
    def grabExcessVerticalSpace(self) -> bool:
        return self.__grabExcessVerticalSpace

    @grabExcessVerticalSpace.setter
    def grabExcessVerticalSpace(self, grabExcessVerticalSpace: bool):
        self.__grabExcessVerticalSpace = grabExcessVerticalSpace

    @property
    def grabExcessHorizontalSpace(self) -> bool:
        return self.__grabExcessHorizontalSpace

    @grabExcessHorizontalSpace.setter
    def grabExcessHorizontalSpace(self, grabExcessHorizontalSpace: bool):
        self.__grabExcessHorizontalSpace = grabExcessHorizontalSpace

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
    def verticalAlignment(self) -> str:
        return self.__verticalAlignment

    @verticalAlignment.setter
    def verticalAlignment(self, verticalAlignment: str):
        self.__verticalAlignment = verticalAlignment

    @property
    def horizontalSpan(self) -> int:
        return self.__horizontalSpan

    @horizontalSpan.setter
    def horizontalSpan(self, horizontalSpan: int):
        self.__horizontalSpan = horizontalSpan

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
            if hasattr(old_value, "gmfgraph_Dimension85"):
                opp_val = getattr(old_value, "gmfgraph_Dimension85", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_Dimension85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Dimension85"):
                opp_val = getattr(value, "gmfgraph_Dimension85", None)
                setattr(value, "gmfgraph_Dimension85", self)

class gmfgraph_Layoutable(ABC):

    pass
class gmfgraph_LayoutData(ABC):

    pass
class Layout:

    pass
class gmfgraph_XYLayout(Layout):

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
    def matchMinorSize(self) -> bool:
        return self.__matchMinorSize

    @matchMinorSize.setter
    def matchMinorSize(self, matchMinorSize: bool):
        self.__matchMinorSize = matchMinorSize

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

class gmfgraph_LayoutRef(Layout):

    pass
class gmfgraph_GridLayout(Layout):

    def __init__(self, numColumns: int, equalWidth: bool, gmfgraph_GridLayout: "gmfgraph_Dimension" = None, gmfgraph_GridLayout92: "gmfgraph_Dimension" = None):
        self.numColumns = numColumns
        self.equalWidth = equalWidth
        self.gmfgraph_GridLayout = gmfgraph_GridLayout
        self.gmfgraph_GridLayout92 = gmfgraph_GridLayout92
        
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
    def gmfgraph_GridLayout(self):
        return self.__gmfgraph_GridLayout

    @gmfgraph_GridLayout.setter
    def gmfgraph_GridLayout(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_GridLayout__gmfgraph_GridLayout", None)
        self.__gmfgraph_GridLayout = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_Dimension90"):
                opp_val = getattr(old_value, "gmfgraph_Dimension90", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_Dimension90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Dimension90"):
                opp_val = getattr(value, "gmfgraph_Dimension90", None)
                setattr(value, "gmfgraph_Dimension90", self)

    @property
    def gmfgraph_GridLayout92(self):
        return self.__gmfgraph_GridLayout92

    @gmfgraph_GridLayout92.setter
    def gmfgraph_GridLayout92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_GridLayout__gmfgraph_GridLayout92", None)
        self.__gmfgraph_GridLayout92 = value
        
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

class gmfgraph_BorderLayout(Layout):

    pass
class gmfgraph_StackLayout(Layout):

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

class Border:

    pass
class gmfgraph_BorderRef(Border):

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
            if hasattr(old_value, "gmfgraph_Color75"):
                opp_val = getattr(old_value, "gmfgraph_Color75", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_Color75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Color75"):
                opp_val = getattr(value, "gmfgraph_Color75", None)
                setattr(value, "gmfgraph_Color75", self)

class Font:

    pass
class gmfgraph_BasicFont(Font):

    def __init__(self, faceName: str, height: int, style: str):
        self.faceName = faceName
        self.height = height
        self.style = style
        
    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def faceName(self) -> str:
        return self.__faceName

    @faceName.setter
    def faceName(self, faceName: str):
        self.__faceName = faceName

class gmfgraph_CompoundBorder(Border):

    pass
class gmfgraph_MarginBorder(Border):

    pass
class CustomClass:

    pass
class gmfgraph_CustomBorder(Border, CustomClass):

    pass
class gmfgraph_CustomLayoutData(LayoutData, CustomClass):

    pass
class gmfgraph_CustomLayout(CustomClass, Layout):

    pass
class gmfgraph_FigureAccessor:

    def __init__(self, accessor: str, gmfgraph_FigureAccessor: "gmfgraph_RealFigure" = None, gmfgraph_FigureAccessor73: "gmfgraph_CustomFigure" = None):
        self.accessor = accessor
        self.gmfgraph_FigureAccessor = gmfgraph_FigureAccessor
        self.gmfgraph_FigureAccessor73 = gmfgraph_FigureAccessor73
        
    @property
    def accessor(self) -> str:
        return self.__accessor

    @accessor.setter
    def accessor(self, accessor: str):
        self.__accessor = accessor

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
            if hasattr(old_value, "gmfgraph_RealFigure71"):
                opp_val = getattr(old_value, "gmfgraph_RealFigure71", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_RealFigure71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_RealFigure71"):
                opp_val = getattr(value, "gmfgraph_RealFigure71", None)
                setattr(value, "gmfgraph_RealFigure71", self)

    @property
    def gmfgraph_FigureAccessor73(self):
        return self.__gmfgraph_FigureAccessor73

    @gmfgraph_FigureAccessor73.setter
    def gmfgraph_FigureAccessor73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_FigureAccessor__gmfgraph_FigureAccessor73", None)
        self.__gmfgraph_FigureAccessor73 = value
        
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

class gmfgraph_CustomAttribute:

    def __init__(self, name: str, value: str, directAccess: bool, multiStatementValue: bool, gmfgraph_CustomAttribute: "gmfgraph_CustomClass" = None):
        self.name = name
        self.value = value
        self.directAccess = directAccess
        self.multiStatementValue = multiStatementValue
        self.gmfgraph_CustomAttribute = gmfgraph_CustomAttribute
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def directAccess(self) -> bool:
        return self.__directAccess

    @directAccess.setter
    def directAccess(self, directAccess: bool):
        self.__directAccess = directAccess

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def multiStatementValue(self) -> bool:
        return self.__multiStatementValue

    @multiStatementValue.setter
    def multiStatementValue(self, multiStatementValue: bool):
        self.__multiStatementValue = multiStatementValue

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
                    

class Polygon:

    pass
class gmfgraph_ScalablePolygon(Polygon):

    pass
class DecorationFigure:

    pass
class gmfgraph_PolygonDecoration(Polygon, DecorationFigure):

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
class RealFigure:

    pass
class gmfgraph_CustomFigure(RealFigure, CustomClass):

    pass
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
    def xorFill(self) -> bool:
        return self.__xorFill

    @xorFill.setter
    def xorFill(self, xorFill: bool):
        self.__xorFill = xorFill

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
    def outline(self) -> bool:
        return self.__outline

    @outline.setter
    def outline(self, outline: bool):
        self.__outline = outline

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
                if hasattr(item, "gmfgraph_Figure62"):
                    opp_val = getattr(item, "gmfgraph_Figure62", None)
                    
                    if opp_val == self:
                        setattr(item, "gmfgraph_Figure62", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gmfgraph_Figure62"):
                    opp_val = getattr(item, "gmfgraph_Figure62", None)
                    
                    setattr(item, "gmfgraph_Figure62", self)
                    

class gmfgraph_DecorationFigure(RealFigure):

    pass
class gmfgraph_LabeledContainer(RealFigure):

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

class gmfgraph_ConnectionFigure(RealFigure):

    pass
class ConnectionFigure:

    pass
class gmfgraph_CustomConnection(ConnectionFigure, CustomFigure):

    pass
class Polyline:

    pass
class gmfgraph_PolylineDecoration(Polyline, DecorationFigure):

    pass
class gmfgraph_PolylineConnection(Polyline, ConnectionFigure):

    pass
class gmfgraph_Polygon(Polyline):

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

class gmfgraph_Ellipse(Shape):

    pass
class gmfgraph_Polyline(Shape):

    pass
class gmfgraph_Rectangle(Shape):

    pass
class gmfgraph_Color(ABC):

    pass
class Layoutable:

    pass
class gmfgraph_Figure(Layoutable):

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

class AbstractFigure:

    pass
class gmfgraph_FigureRef(AbstractFigure):

    pass
class gmfgraph_Point:

    def __init__(self, x: int, y: int, gmfgraph_Point: "gmfgraph_Figure" = None, gmfgraph_Point55: "gmfgraph_Figure" = None, gmfgraph_Point64: "gmfgraph_Polyline" = None, gmfgraph_Point97: "gmfgraph_XYLayoutData" = None):
        self.x = x
        self.y = y
        self.gmfgraph_Point = gmfgraph_Point
        self.gmfgraph_Point55 = gmfgraph_Point55
        self.gmfgraph_Point64 = gmfgraph_Point64
        self.gmfgraph_Point97 = gmfgraph_Point97
        
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

    @property
    def gmfgraph_Point97(self):
        return self.__gmfgraph_Point97

    @gmfgraph_Point97.setter
    def gmfgraph_Point97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Point__gmfgraph_Point97", None)
        self.__gmfgraph_Point97 = value
        
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
    def gmfgraph_Point64(self):
        return self.__gmfgraph_Point64

    @gmfgraph_Point64.setter
    def gmfgraph_Point64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Point__gmfgraph_Point64", None)
        self.__gmfgraph_Point64 = value
        
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

class gmfgraph_Insets:

    def __init__(self, top: int, left: int, bottom: int, right: int, gmfgraph_Insets: "gmfgraph_Figure" = None, gmfgraph_Insets77: "gmfgraph_MarginBorder" = None):
        self.top = top
        self.left = left
        self.bottom = bottom
        self.right = right
        self.gmfgraph_Insets = gmfgraph_Insets
        self.gmfgraph_Insets77 = gmfgraph_Insets77
        
    @property
    def right(self) -> int:
        return self.__right

    @right.setter
    def right(self, right: int):
        self.__right = right

    @property
    def bottom(self) -> int:
        return self.__bottom

    @bottom.setter
    def bottom(self, bottom: int):
        self.__bottom = bottom

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
    def gmfgraph_Insets77(self):
        return self.__gmfgraph_Insets77

    @gmfgraph_Insets77.setter
    def gmfgraph_Insets77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Insets__gmfgraph_Insets77", None)
        self.__gmfgraph_Insets77 = value
        
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
            if hasattr(old_value, "gmfgraph_Figure47"):
                opp_val = getattr(old_value, "gmfgraph_Figure47", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_Figure47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Figure47"):
                opp_val = getattr(value, "gmfgraph_Figure47", None)
                setattr(value, "gmfgraph_Figure47", self)

class gmfgraph_Font(ABC):

    pass
class gmfgraph_Dimension:

    def __init__(self, dx: int, dy: int, gmfgraph_Dimension: "gmfgraph_Figure" = None, gmfgraph_Dimension40: "gmfgraph_Figure" = None, gmfgraph_Dimension43: "gmfgraph_Figure" = None, gmfgraph_Dimension85: "gmfgraph_GridLayoutData" = None, gmfgraph_Dimension102: "gmfgraph_DefaultSizeFacet" = None, gmfgraph_Dimension90: "gmfgraph_GridLayout" = None, gmfgraph_Dimension93: "gmfgraph_GridLayout" = None, gmfgraph_Dimension95: "gmfgraph_BorderLayout" = None, gmfgraph_Dimension100: "gmfgraph_XYLayoutData" = None):
        self.dx = dx
        self.dy = dy
        self.gmfgraph_Dimension = gmfgraph_Dimension
        self.gmfgraph_Dimension40 = gmfgraph_Dimension40
        self.gmfgraph_Dimension43 = gmfgraph_Dimension43
        self.gmfgraph_Dimension85 = gmfgraph_Dimension85
        self.gmfgraph_Dimension102 = gmfgraph_Dimension102
        self.gmfgraph_Dimension90 = gmfgraph_Dimension90
        self.gmfgraph_Dimension93 = gmfgraph_Dimension93
        self.gmfgraph_Dimension95 = gmfgraph_Dimension95
        self.gmfgraph_Dimension100 = gmfgraph_Dimension100
        
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
    def gmfgraph_Dimension(self):
        return self.__gmfgraph_Dimension

    @gmfgraph_Dimension.setter
    def gmfgraph_Dimension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Dimension__gmfgraph_Dimension", None)
        self.__gmfgraph_Dimension = value
        
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
    def gmfgraph_Dimension40(self):
        return self.__gmfgraph_Dimension40

    @gmfgraph_Dimension40.setter
    def gmfgraph_Dimension40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Dimension__gmfgraph_Dimension40", None)
        self.__gmfgraph_Dimension40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_Figure39"):
                opp_val = getattr(old_value, "gmfgraph_Figure39", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_Figure39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Figure39"):
                opp_val = getattr(value, "gmfgraph_Figure39", None)
                setattr(value, "gmfgraph_Figure39", self)

    @property
    def gmfgraph_Dimension102(self):
        return self.__gmfgraph_Dimension102

    @gmfgraph_Dimension102.setter
    def gmfgraph_Dimension102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Dimension__gmfgraph_Dimension102", None)
        self.__gmfgraph_Dimension102 = value
        
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
    def gmfgraph_Dimension93(self):
        return self.__gmfgraph_Dimension93

    @gmfgraph_Dimension93.setter
    def gmfgraph_Dimension93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Dimension__gmfgraph_Dimension93", None)
        self.__gmfgraph_Dimension93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_GridLayout92"):
                opp_val = getattr(old_value, "gmfgraph_GridLayout92", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_GridLayout92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_GridLayout92"):
                opp_val = getattr(value, "gmfgraph_GridLayout92", None)
                setattr(value, "gmfgraph_GridLayout92", self)

    @property
    def gmfgraph_Dimension90(self):
        return self.__gmfgraph_Dimension90

    @gmfgraph_Dimension90.setter
    def gmfgraph_Dimension90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Dimension__gmfgraph_Dimension90", None)
        self.__gmfgraph_Dimension90 = value
        
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
    def gmfgraph_Dimension43(self):
        return self.__gmfgraph_Dimension43

    @gmfgraph_Dimension43.setter
    def gmfgraph_Dimension43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Dimension__gmfgraph_Dimension43", None)
        self.__gmfgraph_Dimension43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_Figure42"):
                opp_val = getattr(old_value, "gmfgraph_Figure42", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_Figure42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Figure42"):
                opp_val = getattr(value, "gmfgraph_Figure42", None)
                setattr(value, "gmfgraph_Figure42", self)

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
            if hasattr(old_value, "gmfgraph_XYLayoutData99"):
                opp_val = getattr(old_value, "gmfgraph_XYLayoutData99", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_XYLayoutData99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_XYLayoutData99"):
                opp_val = getattr(value, "gmfgraph_XYLayoutData99", None)
                setattr(value, "gmfgraph_XYLayoutData99", self)

    @property
    def gmfgraph_Dimension95(self):
        return self.__gmfgraph_Dimension95

    @gmfgraph_Dimension95.setter
    def gmfgraph_Dimension95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Dimension__gmfgraph_Dimension95", None)
        self.__gmfgraph_Dimension95 = value
        
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
    def gmfgraph_Dimension85(self):
        return self.__gmfgraph_Dimension85

    @gmfgraph_Dimension85.setter
    def gmfgraph_Dimension85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_Dimension__gmfgraph_Dimension85", None)
        self.__gmfgraph_Dimension85 = value
        
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

class gmfgraph_Identity(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class gmfgraph_Layout(ABC):

    pass
class gmfgraph_Border(ABC):

    pass
class gmfgraph_RealFigure(AbstractFigure):

    def __init__(self, name: str, gmfgraph_RealFigure: "gmfgraph_FigureGallery" = None, gmfgraph_RealFigure60: "gmfgraph_FigureRef" = None, gmfgraph_RealFigure71: "gmfgraph_FigureAccessor" = None, gmfgraph_RealFigure104: set["gmfgraph_Figure"] = None):
        self.name = name
        self.gmfgraph_RealFigure = gmfgraph_RealFigure
        self.gmfgraph_RealFigure60 = gmfgraph_RealFigure60
        self.gmfgraph_RealFigure71 = gmfgraph_RealFigure71
        self.gmfgraph_RealFigure104 = gmfgraph_RealFigure104 if gmfgraph_RealFigure104 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def gmfgraph_RealFigure104(self):
        return self.__gmfgraph_RealFigure104

    @gmfgraph_RealFigure104.setter
    def gmfgraph_RealFigure104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_RealFigure__gmfgraph_RealFigure104", None)
        self.__gmfgraph_RealFigure104 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gmfgraph_Figure105"):
                    opp_val = getattr(item, "gmfgraph_Figure105", None)
                    
                    if opp_val == self:
                        setattr(item, "gmfgraph_Figure105", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gmfgraph_Figure105"):
                    opp_val = getattr(item, "gmfgraph_Figure105", None)
                    
                    setattr(item, "gmfgraph_Figure105", self)
                    

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
    def gmfgraph_RealFigure60(self):
        return self.__gmfgraph_RealFigure60

    @gmfgraph_RealFigure60.setter
    def gmfgraph_RealFigure60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_RealFigure__gmfgraph_RealFigure60", None)
        self.__gmfgraph_RealFigure60 = value
        
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

    @property
    def gmfgraph_RealFigure71(self):
        return self.__gmfgraph_RealFigure71

    @gmfgraph_RealFigure71.setter
    def gmfgraph_RealFigure71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_RealFigure__gmfgraph_RealFigure71", None)
        self.__gmfgraph_RealFigure71 = value
        
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

class Node:

    pass
class gmfgraph_DiagramLabel(Node):

    def __init__(self, elementIcon: bool, external: bool, gmfgraph_DiagramLabel: "gmfgraph_Canvas" = None, gmfgraph_DiagramLabel27: "gmfgraph_ChildAccess" = None, gmfgraph_DiagramLabel30: "gmfgraph_ChildAccess" = None):
        self.elementIcon = elementIcon
        self.external = external
        self.gmfgraph_DiagramLabel = gmfgraph_DiagramLabel
        self.gmfgraph_DiagramLabel27 = gmfgraph_DiagramLabel27
        self.gmfgraph_DiagramLabel30 = gmfgraph_DiagramLabel30
        
    @property
    def elementIcon(self) -> bool:
        return self.__elementIcon

    @elementIcon.setter
    def elementIcon(self, elementIcon: bool):
        self.__elementIcon = elementIcon

    @property
    def external(self) -> bool:
        return self.__external

    @external.setter
    def external(self, external: bool):
        self.__external = external

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

class DiagramElement:

    pass
class gmfgraph_AbstractNode(DiagramElement):

    pass
class gmfgraph_Compartment(DiagramElement):

    def __init__(self, collapsible: bool, needsTitle: bool, gmfgraph_Compartment24: "gmfgraph_ChildAccess" = None, gmfgraph_Compartment: "gmfgraph_Canvas" = None):
        self.collapsible = collapsible
        self.needsTitle = needsTitle
        self.gmfgraph_Compartment24 = gmfgraph_Compartment24
        self.gmfgraph_Compartment = gmfgraph_Compartment
        
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

class gmfgraph_ChildAccess:

    def __init__(self, accessor: str, gmfgraph_ChildAccess: "gmfgraph_Node" = None, gmfgraph_ChildAccess25: "gmfgraph_Compartment" = None, gmfgraph_ChildAccess28: "gmfgraph_DiagramLabel" = None, gmfgraph_ChildAccess31: "gmfgraph_DiagramLabel" = None, ChildAccess: "gmfgraph_FigureDescriptor" = None, accessors: "gmfgraph_FigureDescriptor" = None, gmfgraph_ChildAccess113: "gmfgraph_Figure" = None):
        self.accessor = accessor
        self.gmfgraph_ChildAccess = gmfgraph_ChildAccess
        self.gmfgraph_ChildAccess25 = gmfgraph_ChildAccess25
        self.gmfgraph_ChildAccess28 = gmfgraph_ChildAccess28
        self.gmfgraph_ChildAccess31 = gmfgraph_ChildAccess31
        self.ChildAccess = ChildAccess
        self.accessors = accessors
        self.gmfgraph_ChildAccess113 = gmfgraph_ChildAccess113
        
    @property
    def accessor(self) -> str:
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
            if hasattr(old_value, "owner110"):
                opp_val = getattr(old_value, "owner110", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner110"):
                opp_val = getattr(value, "owner110", None)
                if opp_val is None:
                    setattr(value, "owner110", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gmfgraph_ChildAccess113(self):
        return self.__gmfgraph_ChildAccess113

    @gmfgraph_ChildAccess113.setter
    def gmfgraph_ChildAccess113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmfgraph_ChildAccess__gmfgraph_ChildAccess113", None)
        self.__gmfgraph_ChildAccess113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gmfgraph_Figure114"):
                opp_val = getattr(old_value, "gmfgraph_Figure114", None)
                if opp_val == self:
                    setattr(old_value, "gmfgraph_Figure114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gmfgraph_Figure114"):
                opp_val = getattr(value, "gmfgraph_Figure114", None)
                setattr(value, "gmfgraph_Figure114", self)

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

class AbstractNode:

    pass
class gmfgraph_VisualFacet(ABC):

    pass
class gmfgraph_Connection(DiagramElement):

    pass
class gmfgraph_Node(AbstractNode):

    def __init__(self, resizeConstraint: str, affixedParentSide: str, gmfgraph_Node: "gmfgraph_Canvas" = None, gmfgraph_Node22: "gmfgraph_ChildAccess" = None):
        self.resizeConstraint = resizeConstraint
        self.affixedParentSide = affixedParentSide
        self.gmfgraph_Node = gmfgraph_Node
        self.gmfgraph_Node22 = gmfgraph_Node22
        
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
class gmfgraph_FigureGallery(Identity):

    def __init__(self, implementationBundle: str, gmfgraph_FigureGallery: "gmfgraph_Canvas" = None, gmfgraph_FigureGallery10: set["gmfgraph_RealFigure"] = None, gmfgraph_FigureGallery12: set["gmfgraph_FigureDescriptor"] = None, gmfgraph_FigureGallery14: set["gmfgraph_Border"] = None, gmfgraph_FigureGallery16: set["gmfgraph_Layout"] = None):
        self.implementationBundle = implementationBundle
        self.gmfgraph_FigureGallery = gmfgraph_FigureGallery
        self.gmfgraph_FigureGallery10 = gmfgraph_FigureGallery10 if gmfgraph_FigureGallery10 is not None else set()
        self.gmfgraph_FigureGallery12 = gmfgraph_FigureGallery12 if gmfgraph_FigureGallery12 is not None else set()
        self.gmfgraph_FigureGallery14 = gmfgraph_FigureGallery14 if gmfgraph_FigureGallery14 is not None else set()
        self.gmfgraph_FigureGallery16 = gmfgraph_FigureGallery16 if gmfgraph_FigureGallery16 is not None else set()
        
    @property
    def implementationBundle(self) -> str:
        return self.__implementationBundle

    @implementationBundle.setter
    def implementationBundle(self, implementationBundle: str):
        self.__implementationBundle = implementationBundle

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

class gmfgraph_FigureDescriptor(Identity):

    pass
class gmfgraph_DiagramElement(Identity):

    pass
class gmfgraph_Canvas(Identity):

    pass