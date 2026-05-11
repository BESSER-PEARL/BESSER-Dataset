from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class AppearanceStyle(Enum):
    Line = "Line"
    Font = "Font"
    Fill = "Fill"
class StandardToolKind(Enum):
    SELECT = "SELECT"
    SELECT_PAN = "SELECT_PAN"
    MARQUEE = "MARQUEE"
    ZOOM_PAN = "ZOOM_PAN"
    ZOOM_IN = "ZOOM_IN"
    ZOOM_OUT = "ZOOM_OUT"
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
class Language(Enum):
    ocl = "ocl"
    java = "java"
    regexp = "regexp"
    nregexp = "nregexp"
    literal = "literal"
class Alignment(Enum):
    BEGINNING = "BEGINNING"
    CENTER = "CENTER"
    END = "END"
    FILL = "FILL"
class SVGPropertyType(Enum):
    STRING = "STRING"
    COLOR = "COLOR"
    FLOAT = "FLOAT"
class FontStyle(Enum):
    NORMAL = "NORMAL"
    BOLD = "BOLD"
    ITALIC = "ITALIC"
class LabelTextAccessMethod(Enum):
    MESSAGE_FORMAT = "MESSAGE_FORMAT"
    NATIVE = "NATIVE"
    REGEXP = "REGEXP"
    PRINTF = "PRINTF"
class Severity(Enum):
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
class LineKind(Enum):
    LINE_DOT = "LINE_DOT"
    LINE_DASHDOT = "LINE_DASHDOT"
    LINE_DASHDOTDOT = "LINE_DASHDOTDOT"
    LINE_CUSTOM = "LINE_CUSTOM"
    LINE_SOLID = "LINE_SOLID"
    LINE_DASH = "LINE_DASH"
class ActionKind(Enum):
    CREATE = "CREATE"
    PROPCHANGE = "PROPCHANGE"
    MODIFY = "MODIFY"
    PROCESS = "PROCESS"
    CUSTOM = "CUSTOM"


############################################
# Definition of Classes
############################################

class Node:

    pass
class mappings_AppearanceSteward:

    pass
class mappings_ToolOwner:

    pass
class mappings_MenuOwner:

    pass
class mappings_MappingEntry:

    pass
class gmf_all_mappings_NodeMapping(mappings_ToolOwner, mappings_MappingEntry, mappings_AppearanceSteward, mappings_MenuOwner):

    pass
class LabelMapping:

    pass
class ElementInitializer:

    pass
class Constraint:

    pass
class mappings_gmf_all_EClass:

    pass
class gmf_all_mappings_MappingEntry(ABC):

    def __init__(self, gmf_all_mappings_MappingEntry18: set["CanvasMapping"] = None, parentMapEntry: set["VisualEffectMapping"] = None, gmf_all_mappings_MappingEntry: "mappings_gmf_all_EClass" = None, gmf_all_mappings_MappingEntry13: "Constraint" = None, gmf_all_mappings_MappingEntry15: "ElementInitializer" = None, mapEntry: set["LabelMapping"] = None):
        self.gmf_all_mappings_MappingEntry18 = gmf_all_mappings_MappingEntry18 if gmf_all_mappings_MappingEntry18 is not None else set()
        self.parentMapEntry = parentMapEntry if parentMapEntry is not None else set()
        self.gmf_all_mappings_MappingEntry = gmf_all_mappings_MappingEntry
        self.gmf_all_mappings_MappingEntry13 = gmf_all_mappings_MappingEntry13
        self.gmf_all_mappings_MappingEntry15 = gmf_all_mappings_MappingEntry15
        self.mapEntry = mapEntry if mapEntry is not None else set()
        
        pass
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
    def mapEntry(self):
        return self.__mapEntry

    @mapEntry.setter
    def mapEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_mappings_MappingEntry__mapEntry", None)
        self.__mapEntry = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LabelMapping"):
                    opp_val = getattr(item, "LabelMapping", None)
                    
                    if opp_val == self:
                        setattr(item, "LabelMapping", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LabelMapping"):
                    opp_val = getattr(item, "LabelMapping", None)
                    
                    setattr(item, "LabelMapping", self)
                    

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

    @property
    def parentMapEntry(self):
        return self.__parentMapEntry

    @parentMapEntry.setter
    def parentMapEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_mappings_MappingEntry__parentMapEntry", None)
        self.__parentMapEntry = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VisualEffectMapping"):
                    opp_val = getattr(item, "VisualEffectMapping", None)
                    
                    if opp_val == self:
                        setattr(item, "VisualEffectMapping", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VisualEffectMapping"):
                    opp_val = getattr(item, "VisualEffectMapping", None)
                    
                    setattr(item, "VisualEffectMapping", self)
                    

    def getDomainContext(self) :
        # TODO: Implement getDomainContext method
        pass

class gmf_all_gmfgraph_PinOwner(ABC):

    pass
class gmf_all_gmfgraph_SVGProperty:

    def __init__(self, query: str, attribute: str, type: str, getter: str, setter: str, callSuper: bool):
        self.query = query
        self.attribute = attribute
        self.type = type
        self.getter = getter
        self.setter = setter
        self.callSuper = callSuper
        
        pass
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
    def callSuper(self):
        return self.__callSuper

    @callSuper.setter
    def callSuper(self, callSuper: bool):
        self.__callSuper = callSuper


    @property
    def query(self):
        return self.__query

    @query.setter
    def query(self, query: str):
        self.__query = query


    @property
    def getter(self):
        return self.__getter

    @getter.setter
    def getter(self, getter: str):
        self.__getter = getter


    @property
    def attribute(self):
        return self.__attribute

    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute


class Rectangle2D:

    pass
class SVGProperty:

    pass
class gmf_all_gmfgraph_Rectangle2D:

    def __init__(self, x: float, y: float, width: float, height: float):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        pass
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: float):
        self.__width = width


    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x


    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: float):
        self.__height = height


class gmfgraph_Layout:

    pass
class gmf_all_gmfgraph_Layout(ABC):

    pass
class gmf_all_gmfgraph_Layoutable(ABC):

    pass
class LayoutData:

    pass
class gmf_all_gmfgraph_BorderLayoutData(LayoutData):

    def __init__(self, alignment: str, vertical: bool, LayoutData: "gmf_all_gmfgraph_Layoutable" = None):
        self.alignment = alignment
        self.vertical = vertical
        
        pass
    @property
    def vertical(self):
        return self.__vertical

    @vertical.setter
    def vertical(self, vertical: bool):
        self.__vertical = vertical


    @property
    def alignment(self):
        return self.__alignment

    @alignment.setter
    def alignment(self, alignment: str):
        self.__alignment = alignment


class gmf_all_gmfgraph_XYLayoutData(LayoutData):

    pass
class gmf_all_gmfgraph_GridLayoutData(LayoutData):

    def __init__(self, grabExcessHorizontalSpace: bool, grabExcessVerticalSpace: bool, verticalAlignment: str, horizontalAlignment: str, verticalSpan: int, horizontalSpan: int, horizontalIndent: int, gmf_all_gmfgraph_GridLayoutData: "Dimension" = None, LayoutData: "gmf_all_gmfgraph_Layoutable" = None):
        self.grabExcessHorizontalSpace = grabExcessHorizontalSpace
        self.grabExcessVerticalSpace = grabExcessVerticalSpace
        self.verticalAlignment = verticalAlignment
        self.horizontalAlignment = horizontalAlignment
        self.verticalSpan = verticalSpan
        self.horizontalSpan = horizontalSpan
        self.horizontalIndent = horizontalIndent
        self.gmf_all_gmfgraph_GridLayoutData = gmf_all_gmfgraph_GridLayoutData
        
        pass
    @property
    def grabExcessVerticalSpace(self):
        return self.__grabExcessVerticalSpace

    @grabExcessVerticalSpace.setter
    def grabExcessVerticalSpace(self, grabExcessVerticalSpace: bool):
        self.__grabExcessVerticalSpace = grabExcessVerticalSpace


    @property
    def verticalSpan(self):
        return self.__verticalSpan

    @verticalSpan.setter
    def verticalSpan(self, verticalSpan: int):
        self.__verticalSpan = verticalSpan


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
    def gmf_all_gmfgraph_GridLayoutData(self):
        return self.__gmf_all_gmfgraph_GridLayoutData

    @gmf_all_gmfgraph_GridLayoutData.setter
    def gmf_all_gmfgraph_GridLayoutData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_gmfgraph_GridLayoutData__gmf_all_gmfgraph_GridLayoutData", None)
        self.__gmf_all_gmfgraph_GridLayoutData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Dimension263"):
                opp_val = getattr(old_value, "Dimension263", None)
                if opp_val == self:
                    setattr(old_value, "Dimension263", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Dimension263"):
                opp_val = getattr(value, "Dimension263", None)
                setattr(value, "Dimension263", self)

class gmfgraph_Border:

    pass
class gmf_all_gmfgraph_Border(ABC):

    pass
class gmfgraph_LayoutData:

    pass
class gmf_all_gmfgraph_LayoutData(ABC):

    pass
class gmf_all_gmfgraph_Point:

    def __init__(self, y: int, x: int):
        self.y = y
        self.x = x
        
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


class gmf_all_gmfgraph_Font(ABC):

    pass
class gmf_all_gmfgraph_Color(ABC):

    pass
class gmfgraph_CustomFigure:

    pass
class FigureAccessor:

    pass
class gmf_all_gmfgraph_Insets:

    def __init__(self, top: int, left: int, bottom: int, right: int):
        self.top = top
        self.left = left
        self.bottom = bottom
        self.right = right
        
        pass
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
    def left(self):
        return self.__left

    @left.setter
    def left(self, left: int):
        self.__left = left


class gmf_all_gmfgraph_Dimension:

    def __init__(self, dx: int, dy: int):
        self.dx = dx
        self.dy = dy
        
        pass
    @property
    def dy(self):
        return self.__dy

    @dy.setter
    def dy(self, dy: int):
        self.__dy = dy


    @property
    def dx(self):
        return self.__dx

    @dx.setter
    def dx(self, dx: int):
        self.__dx = dx


class gmf_all_gmfgraph_FigureAccessor:

    def __init__(self, accessor: str, gmf_all_gmfgraph_FigureAccessor: "RealFigure" = None):
        self.accessor = accessor
        self.gmf_all_gmfgraph_FigureAccessor = gmf_all_gmfgraph_FigureAccessor
        
        pass
    @property
    def accessor(self):
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
            if hasattr(old_value, "RealFigure248"):
                opp_val = getattr(old_value, "RealFigure248", None)
                if opp_val == self:
                    setattr(old_value, "RealFigure248", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RealFigure248"):
                opp_val = getattr(value, "RealFigure248", None)
                setattr(value, "RealFigure248", self)

class gmf_all_gmfgraph_CustomAttribute:

    def __init__(self, name: str, value: str, directAccess: bool, multiStatementValue: bool):
        self.name = name
        self.value = value
        self.directAccess = directAccess
        self.multiStatementValue = multiStatementValue
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def directAccess(self):
        return self.__directAccess

    @directAccess.setter
    def directAccess(self, directAccess: bool):
        self.__directAccess = directAccess


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def multiStatementValue(self):
        return self.__multiStatementValue

    @multiStatementValue.setter
    def multiStatementValue(self, multiStatementValue: bool):
        self.__multiStatementValue = multiStatementValue


class CustomAttributeOwner:

    pass
class gmf_all_gmfgraph_CustomClass(CustomAttributeOwner):

    def __init__(self, qualifiedClassName: str):
        self.qualifiedClassName = qualifiedClassName
        
        pass
    @property
    def qualifiedClassName(self):
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
class gmf_all_gmfgraph_CustomDecoration(gmfgraph_CustomFigure, gmfgraph_DecorationFigure):

    pass
class gmf_all_gmfgraph_PolygonDecoration(gmfgraph_Polygon, gmfgraph_DecorationFigure):

    pass
class DecorationFigure:

    pass
class gmfgraph_ConnectionFigure:

    pass
class gmf_all_gmfgraph_CustomConnection(gmfgraph_ConnectionFigure, gmfgraph_CustomFigure):

    pass
class gmfgraph_Polyline:

    pass
class gmf_all_gmfgraph_PolylineDecoration(gmfgraph_Polyline, gmfgraph_DecorationFigure):

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
class gmfgraph_CustomClass:

    pass
class gmf_all_gmfgraph_CustomBorder(gmfgraph_Border, gmfgraph_CustomClass):

    pass
class gmf_all_gmfgraph_CustomLayout(gmfgraph_CustomClass, gmfgraph_Layout):

    pass
class gmf_all_gmfgraph_CustomLayoutData(gmfgraph_LayoutData, gmfgraph_CustomClass):

    pass
class gmfgraph_RealFigure:

    pass
class gmf_all_gmfgraph_CustomFigure(gmfgraph_RealFigure, gmfgraph_CustomClass):

    pass
class Shape:

    pass
class gmf_all_gmfgraph_RoundedRectangle(Shape):

    def __init__(self, cornerWidth: int, cornerHeight: int):
        self.cornerWidth = cornerWidth
        self.cornerHeight = cornerHeight
        
        pass
    @property
    def cornerHeight(self):
        return self.__cornerHeight

    @cornerHeight.setter
    def cornerHeight(self, cornerHeight: int):
        self.__cornerHeight = cornerHeight


    @property
    def cornerWidth(self):
        return self.__cornerWidth

    @cornerWidth.setter
    def cornerWidth(self, cornerWidth: int):
        self.__cornerWidth = cornerWidth


class gmf_all_gmfgraph_Rectangle(Shape):

    pass
class AbstractFigure:

    pass
class gmf_all_gmfgraph_FigureRef(AbstractFigure):

    pass
class gmf_all_gmfgraph_Polyline(Shape):

    pass
class gmf_all_gmfgraph_Ellipse(Shape):

    pass
class gmf_all_gmfgraph_ChildAccess:

    def __init__(self, accessor: str, accessors: "FigureDescriptor" = None, gmf_all_gmfgraph_ChildAccess: "Figure" = None):
        self.accessor = accessor
        self.accessors = accessors
        self.gmf_all_gmfgraph_ChildAccess = gmf_all_gmfgraph_ChildAccess
        
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
        old_value = getattr(self, f"_gmf_all_gmfgraph_ChildAccess__accessors", None)
        self.__accessors = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FigureDescriptor231"):
                opp_val = getattr(old_value, "FigureDescriptor231", None)
                if opp_val == self:
                    setattr(old_value, "FigureDescriptor231", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FigureDescriptor231"):
                opp_val = getattr(value, "FigureDescriptor231", None)
                setattr(value, "FigureDescriptor231", self)

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
            if hasattr(old_value, "Figure233"):
                opp_val = getattr(old_value, "Figure233", None)
                if opp_val == self:
                    setattr(old_value, "Figure233", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Figure233"):
                opp_val = getattr(value, "Figure233", None)
                setattr(value, "Figure233", self)

class Figure:

    pass
class gmf_all_gmfgraph_AbstractFigure(Figure):

    pass
class Point:

    pass
class Insets:

    pass
class Font:

    pass
class gmf_all_gmfgraph_BasicFont(Font):

    def __init__(self, faceName: str, height: int, style: str, Font: "gmf_all_gmfgraph_Figure" = None):
        self.faceName = faceName
        self.height = height
        self.style = style
        
        pass
    @property
    def faceName(self):
        return self.__faceName

    @faceName.setter
    def faceName(self, faceName: str):
        self.__faceName = faceName


    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height


    @property
    def style(self):
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style


class Color:

    pass
class gmf_all_gmfgraph_ConstantColor(Color):

    def __init__(self, value: str, Color: "gmf_all_gmfgraph_Figure" = None, Color205: "gmf_all_gmfgraph_Figure" = None, Color253: "gmf_all_gmfgraph_LineBorder" = None):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class gmf_all_gmfgraph_RGBColor(Color):

    def __init__(self, red: int, green: int, blue: int, Color: "gmf_all_gmfgraph_Figure" = None, Color205: "gmf_all_gmfgraph_Figure" = None, Color253: "gmf_all_gmfgraph_LineBorder" = None):
        self.red = red
        self.green = green
        self.blue = blue
        
        pass
    @property
    def green(self):
        return self.__green

    @green.setter
    def green(self, green: int):
        self.__green = green


    @property
    def red(self):
        return self.__red

    @red.setter
    def red(self, red: int):
        self.__red = red


    @property
    def blue(self):
        return self.__blue

    @blue.setter
    def blue(self, blue: int):
        self.__blue = blue


class gmfgraph_CustomAttributeOwner:

    pass
class gmfgraph_PinOwner:

    pass
class gmfgraph_AbstractFigure:

    pass
class gmf_all_gmfgraph_RealFigure(gmfgraph_CustomAttributeOwner, gmfgraph_AbstractFigure, gmfgraph_PinOwner):

    def __init__(self, name: str, gmf_all_gmfgraph_RealFigure: set["Figure"] = None):
        self.name = name
        self.gmf_all_gmfgraph_RealFigure = gmf_all_gmfgraph_RealFigure if gmf_all_gmfgraph_RealFigure is not None else set()
        
        pass
    @property
    def name(self):
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
                if hasattr(item, "Figure235"):
                    opp_val = getattr(item, "Figure235", None)
                    
                    if opp_val == self:
                        setattr(item, "Figure235", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Figure235"):
                    opp_val = getattr(item, "Figure235", None)
                    
                    setattr(item, "Figure235", self)
                    

class Dimension:

    pass
class gmf_all_gmfgraph_VisualFacet(ABC):

    pass
class gmf_all_gmfgraph_DiagramLabel(Node):

    def __init__(self, elementIcon: bool, external: bool, gmf_all_gmfgraph_DiagramLabel: "ChildAccess" = None, gmf_all_gmfgraph_DiagramLabel196: "ChildAccess" = None, Node169: "gmf_all_gmfgraph_Canvas" = None, Node: "gmf_all_mappings_NodeMapping" = None):
        self.elementIcon = elementIcon
        self.external = external
        self.gmf_all_gmfgraph_DiagramLabel = gmf_all_gmfgraph_DiagramLabel
        self.gmf_all_gmfgraph_DiagramLabel196 = gmf_all_gmfgraph_DiagramLabel196
        
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
    def gmf_all_gmfgraph_DiagramLabel(self):
        return self.__gmf_all_gmfgraph_DiagramLabel

    @gmf_all_gmfgraph_DiagramLabel.setter
    def gmf_all_gmfgraph_DiagramLabel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_gmfgraph_DiagramLabel__gmf_all_gmfgraph_DiagramLabel", None)
        self.__gmf_all_gmfgraph_DiagramLabel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ChildAccess194"):
                opp_val = getattr(old_value, "ChildAccess194", None)
                if opp_val == self:
                    setattr(old_value, "ChildAccess194", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ChildAccess194"):
                opp_val = getattr(value, "ChildAccess194", None)
                setattr(value, "ChildAccess194", self)

    @property
    def gmf_all_gmfgraph_DiagramLabel196(self):
        return self.__gmf_all_gmfgraph_DiagramLabel196

    @gmf_all_gmfgraph_DiagramLabel196.setter
    def gmf_all_gmfgraph_DiagramLabel196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_gmfgraph_DiagramLabel__gmf_all_gmfgraph_DiagramLabel196", None)
        self.__gmf_all_gmfgraph_DiagramLabel196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ChildAccess197"):
                opp_val = getattr(old_value, "ChildAccess197", None)
                if opp_val == self:
                    setattr(old_value, "ChildAccess197", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ChildAccess197"):
                opp_val = getattr(value, "ChildAccess197", None)
                setattr(value, "ChildAccess197", self)

class ChildAccess:

    pass
class Layoutable:

    pass
class gmf_all_gmfgraph_Figure(Layoutable):

    pass
class VisualFacet:

    pass
class gmf_all_gmfgraph_GeneralFacet(VisualFacet):

    def __init__(self, identifier: str, data: str, VisualFacet: "gmf_all_gmfgraph_DiagramElement" = None):
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


class gmf_all_gmfgraph_GradientFacet(VisualFacet):

    def __init__(self, direction: str, VisualFacet: "gmf_all_gmfgraph_DiagramElement" = None):
        self.direction = direction
        
        pass
    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction


class gmf_all_gmfgraph_LabelOffsetFacet(VisualFacet):

    def __init__(self, x: int, y: int, VisualFacet: "gmf_all_gmfgraph_DiagramElement" = None):
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


class gmf_all_gmfgraph_DefaultSizeFacet(VisualFacet):

    pass
class gmf_all_gmfgraph_AlignmentFacet(VisualFacet):

    def __init__(self, alignment: str, VisualFacet: "gmf_all_gmfgraph_DiagramElement" = None):
        self.alignment = alignment
        
        pass
    @property
    def alignment(self):
        return self.__alignment

    @alignment.setter
    def alignment(self, alignment: str):
        self.__alignment = alignment


class gmf_all_gmfgraph_Identity(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class Layout:

    pass
class gmf_all_gmfgraph_LayoutRef(Layout):

    pass
class gmf_all_gmfgraph_GridLayout(Layout):

    def __init__(self, numColumns: int, equalWidth: bool, gmf_all_gmfgraph_GridLayout: "Dimension" = None, gmf_all_gmfgraph_GridLayout273: "Dimension" = None, Layout269: "gmf_all_gmfgraph_LayoutRef" = None, Layout: "gmf_all_gmfgraph_FigureGallery" = None, Layout267: "gmf_all_gmfgraph_Layoutable" = None):
        self.numColumns = numColumns
        self.equalWidth = equalWidth
        self.gmf_all_gmfgraph_GridLayout = gmf_all_gmfgraph_GridLayout
        self.gmf_all_gmfgraph_GridLayout273 = gmf_all_gmfgraph_GridLayout273
        
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
    def gmf_all_gmfgraph_GridLayout273(self):
        return self.__gmf_all_gmfgraph_GridLayout273

    @gmf_all_gmfgraph_GridLayout273.setter
    def gmf_all_gmfgraph_GridLayout273(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_gmfgraph_GridLayout__gmf_all_gmfgraph_GridLayout273", None)
        self.__gmf_all_gmfgraph_GridLayout273 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Dimension274"):
                opp_val = getattr(old_value, "Dimension274", None)
                if opp_val == self:
                    setattr(old_value, "Dimension274", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Dimension274"):
                opp_val = getattr(value, "Dimension274", None)
                setattr(value, "Dimension274", self)

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
            if hasattr(old_value, "Dimension271"):
                opp_val = getattr(old_value, "Dimension271", None)
                if opp_val == self:
                    setattr(old_value, "Dimension271", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Dimension271"):
                opp_val = getattr(value, "Dimension271", None)
                setattr(value, "Dimension271", self)

class gmf_all_gmfgraph_FlowLayout(Layout):

    def __init__(self, vertical: bool, matchMinorSize: bool, forceSingleLine: bool, majorAlignment: str, minorAlignment: str, majorSpacing: int, minorSpacing: int, Layout269: "gmf_all_gmfgraph_LayoutRef" = None, Layout: "gmf_all_gmfgraph_FigureGallery" = None, Layout267: "gmf_all_gmfgraph_Layoutable" = None):
        self.vertical = vertical
        self.matchMinorSize = matchMinorSize
        self.forceSingleLine = forceSingleLine
        self.majorAlignment = majorAlignment
        self.minorAlignment = minorAlignment
        self.majorSpacing = majorSpacing
        self.minorSpacing = minorSpacing
        
        pass
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
    def majorAlignment(self):
        return self.__majorAlignment

    @majorAlignment.setter
    def majorAlignment(self, majorAlignment: str):
        self.__majorAlignment = majorAlignment


    @property
    def majorSpacing(self):
        return self.__majorSpacing

    @majorSpacing.setter
    def majorSpacing(self, majorSpacing: int):
        self.__majorSpacing = majorSpacing


    @property
    def vertical(self):
        return self.__vertical

    @vertical.setter
    def vertical(self, vertical: bool):
        self.__vertical = vertical


    @property
    def matchMinorSize(self):
        return self.__matchMinorSize

    @matchMinorSize.setter
    def matchMinorSize(self, matchMinorSize: bool):
        self.__matchMinorSize = matchMinorSize


    @property
    def minorAlignment(self):
        return self.__minorAlignment

    @minorAlignment.setter
    def minorAlignment(self, minorAlignment: str):
        self.__minorAlignment = minorAlignment


class gmf_all_gmfgraph_CenterLayout(Layout):

    pass
class gmf_all_gmfgraph_StackLayout(Layout):

    pass
class gmf_all_gmfgraph_BorderLayout(Layout):

    pass
class gmf_all_gmfgraph_XYLayout(Layout):

    pass
class Border:

    pass
class gmf_all_gmfgraph_LineBorder(Border):

    def __init__(self, width: int, gmf_all_gmfgraph_LineBorder: "Color" = None, Border260: "gmf_all_gmfgraph_CompoundBorder" = None, Border221: "gmf_all_gmfgraph_Figure" = None, Border251: "gmf_all_gmfgraph_BorderRef" = None, Border: "gmf_all_gmfgraph_FigureGallery" = None, Border257: "gmf_all_gmfgraph_CompoundBorder" = None):
        self.width = width
        self.gmf_all_gmfgraph_LineBorder = gmf_all_gmfgraph_LineBorder
        
        pass
    @property
    def width(self):
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
            if hasattr(old_value, "Color253"):
                opp_val = getattr(old_value, "Color253", None)
                if opp_val == self:
                    setattr(old_value, "Color253", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Color253"):
                opp_val = getattr(value, "Color253", None)
                setattr(value, "Color253", self)

class gmf_all_gmfgraph_BorderRef(Border):

    pass
class gmf_all_gmfgraph_MarginBorder(Border):

    pass
class gmf_all_gmfgraph_CompoundBorder(Border):

    pass
class FigureDescriptor:

    pass
class RealFigure:

    pass
class gmf_all_gmfgraph_LabeledContainer(RealFigure):

    pass
class gmf_all_gmfgraph_DecorationFigure(RealFigure):

    pass
class gmf_all_gmfgraph_InvisibleRectangle(RealFigure):

    pass
class gmf_all_gmfgraph_ConnectionFigure(RealFigure):

    pass
class gmf_all_gmfgraph_Label(RealFigure):

    def __init__(self, text: str, RealFigure248: "gmf_all_gmfgraph_FigureAccessor" = None, RealFigure237: "gmf_all_gmfgraph_FigureRef" = None, RealFigure: "gmf_all_gmfgraph_FigureGallery" = None):
        self.text = text
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


class gmf_all_gmfgraph_Shape(RealFigure):

    def __init__(self, outline: bool, fill: bool, lineWidth: int, lineKind: str, xorFill: bool, xorOutline: bool, gmf_all_gmfgraph_Shape: set["Figure"] = None, RealFigure248: "gmf_all_gmfgraph_FigureAccessor" = None, RealFigure237: "gmf_all_gmfgraph_FigureRef" = None, RealFigure: "gmf_all_gmfgraph_FigureGallery" = None):
        self.outline = outline
        self.fill = fill
        self.lineWidth = lineWidth
        self.lineKind = lineKind
        self.xorFill = xorFill
        self.xorOutline = xorOutline
        self.gmf_all_gmfgraph_Shape = gmf_all_gmfgraph_Shape if gmf_all_gmfgraph_Shape is not None else set()
        
        pass
    @property
    def xorFill(self):
        return self.__xorFill

    @xorFill.setter
    def xorFill(self, xorFill: bool):
        self.__xorFill = xorFill


    @property
    def lineKind(self):
        return self.__lineKind

    @lineKind.setter
    def lineKind(self, lineKind: str):
        self.__lineKind = lineKind


    @property
    def xorOutline(self):
        return self.__xorOutline

    @xorOutline.setter
    def xorOutline(self, xorOutline: bool):
        self.__xorOutline = xorOutline


    @property
    def fill(self):
        return self.__fill

    @fill.setter
    def fill(self, fill: bool):
        self.__fill = fill


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
                if hasattr(item, "Figure239"):
                    opp_val = getattr(item, "Figure239", None)
                    
                    if opp_val == self:
                        setattr(item, "Figure239", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Figure239"):
                    opp_val = getattr(item, "Figure239", None)
                    
                    setattr(item, "Figure239", self)
                    

class gmf_all_gmfgraph_SVGFigure(RealFigure):

    def __init__(self, documentURI: str, noCanvasWidth: bool, noCanvasHeight: bool, gmf_all_gmfgraph_SVGFigure: set["SVGProperty"] = None, gmf_all_gmfgraph_SVGFigure284: "Rectangle2D" = None, RealFigure248: "gmf_all_gmfgraph_FigureAccessor" = None, RealFigure237: "gmf_all_gmfgraph_FigureRef" = None, RealFigure: "gmf_all_gmfgraph_FigureGallery" = None):
        self.documentURI = documentURI
        self.noCanvasWidth = noCanvasWidth
        self.noCanvasHeight = noCanvasHeight
        self.gmf_all_gmfgraph_SVGFigure = gmf_all_gmfgraph_SVGFigure if gmf_all_gmfgraph_SVGFigure is not None else set()
        self.gmf_all_gmfgraph_SVGFigure284 = gmf_all_gmfgraph_SVGFigure284
        
        pass
    @property
    def documentURI(self):
        return self.__documentURI

    @documentURI.setter
    def documentURI(self, documentURI: str):
        self.__documentURI = documentURI


    @property
    def noCanvasWidth(self):
        return self.__noCanvasWidth

    @noCanvasWidth.setter
    def noCanvasWidth(self, noCanvasWidth: bool):
        self.__noCanvasWidth = noCanvasWidth


    @property
    def noCanvasHeight(self):
        return self.__noCanvasHeight

    @noCanvasHeight.setter
    def noCanvasHeight(self, noCanvasHeight: bool):
        self.__noCanvasHeight = noCanvasHeight


    @property
    def gmf_all_gmfgraph_SVGFigure284(self):
        return self.__gmf_all_gmfgraph_SVGFigure284

    @gmf_all_gmfgraph_SVGFigure284.setter
    def gmf_all_gmfgraph_SVGFigure284(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_gmfgraph_SVGFigure__gmf_all_gmfgraph_SVGFigure284", None)
        self.__gmf_all_gmfgraph_SVGFigure284 = value
        
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
                    

class gmf_all_gmfgraph_VerticalLabel(RealFigure):

    def __init__(self, text: str, RealFigure248: "gmf_all_gmfgraph_FigureAccessor" = None, RealFigure237: "gmf_all_gmfgraph_FigureRef" = None, RealFigure: "gmf_all_gmfgraph_FigureGallery" = None):
        self.text = text
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


class FigureGallery:

    pass
class AbstractNode:

    pass
class gmf_all_gmfgraph_Node(AbstractNode):

    def __init__(self, resizeConstraint: str, affixedParentSide: str, gmf_all_gmfgraph_Node: "ChildAccess" = None):
        self.resizeConstraint = resizeConstraint
        self.affixedParentSide = affixedParentSide
        self.gmf_all_gmfgraph_Node = gmf_all_gmfgraph_Node
        
        pass
    @property
    def resizeConstraint(self):
        return self.__resizeConstraint

    @resizeConstraint.setter
    def resizeConstraint(self, resizeConstraint: str):
        self.__resizeConstraint = resizeConstraint


    @property
    def affixedParentSide(self):
        return self.__affixedParentSide

    @affixedParentSide.setter
    def affixedParentSide(self, affixedParentSide: str):
        self.__affixedParentSide = affixedParentSide


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
class gmf_all_gmfgraph_Connection(DiagramElement):

    pass
class gmf_all_gmfgraph_Compartment(DiagramElement):

    def __init__(self, collapsible: bool, needsTitle: bool, gmf_all_gmfgraph_Compartment: "ChildAccess" = None):
        self.collapsible = collapsible
        self.needsTitle = needsTitle
        self.gmf_all_gmfgraph_Compartment = gmf_all_gmfgraph_Compartment
        
        pass
    @property
    def collapsible(self):
        return self.__collapsible

    @collapsible.setter
    def collapsible(self, collapsible: bool):
        self.__collapsible = collapsible


    @property
    def needsTitle(self):
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
            if hasattr(old_value, "ChildAccess192"):
                opp_val = getattr(old_value, "ChildAccess192", None)
                if opp_val == self:
                    setattr(old_value, "ChildAccess192", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ChildAccess192"):
                opp_val = getattr(value, "ChildAccess192", None)
                setattr(value, "ChildAccess192", self)

class gmf_all_gmfgraph_AbstractNode(DiagramElement):

    pass
class gmf_all_tooldef_StyleSelector(ABC):

    def __init__(self):
        
        pass
    def isOk(self, gmf_all_style) :
        # TODO: Implement isOk method
        pass

class gmf_all_tooldef_Image(ABC):

    pass
class tooldef_ContributionItem:

    pass
class Identity:

    pass
class gmf_all_gmfgraph_Pin(Identity):

    def __init__(self):
        
        pass
    def getOperationType(self) :
        # TODO: Implement getOperationType method
        pass

    def getOperationName(self) :
        # TODO: Implement getOperationName method
        pass

class gmf_all_gmfgraph_FigureDescriptor(Identity):

    pass
class gmf_all_gmfgraph_DiagramElement(Identity):

    pass
class gmf_all_gmfgraph_FigureGallery(Identity):

    def __init__(self, implementationBundle: str, gmf_all_gmfgraph_FigureGallery185: set["Layout"] = None, gmf_all_gmfgraph_FigureGallery: set["RealFigure"] = None, gmf_all_gmfgraph_FigureGallery181: set["FigureDescriptor"] = None, gmf_all_gmfgraph_FigureGallery183: set["Border"] = None):
        self.implementationBundle = implementationBundle
        self.gmf_all_gmfgraph_FigureGallery185 = gmf_all_gmfgraph_FigureGallery185 if gmf_all_gmfgraph_FigureGallery185 is not None else set()
        self.gmf_all_gmfgraph_FigureGallery = gmf_all_gmfgraph_FigureGallery if gmf_all_gmfgraph_FigureGallery is not None else set()
        self.gmf_all_gmfgraph_FigureGallery181 = gmf_all_gmfgraph_FigureGallery181 if gmf_all_gmfgraph_FigureGallery181 is not None else set()
        self.gmf_all_gmfgraph_FigureGallery183 = gmf_all_gmfgraph_FigureGallery183 if gmf_all_gmfgraph_FigureGallery183 is not None else set()
        
        pass
    @property
    def implementationBundle(self):
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
    def gmf_all_gmfgraph_FigureGallery185(self):
        return self.__gmf_all_gmfgraph_FigureGallery185

    @gmf_all_gmfgraph_FigureGallery185.setter
    def gmf_all_gmfgraph_FigureGallery185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_gmfgraph_FigureGallery__gmf_all_gmfgraph_FigureGallery185", None)
        self.__gmf_all_gmfgraph_FigureGallery185 = value if value is not None else set()
        
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
    def gmf_all_gmfgraph_FigureGallery181(self):
        return self.__gmf_all_gmfgraph_FigureGallery181

    @gmf_all_gmfgraph_FigureGallery181.setter
    def gmf_all_gmfgraph_FigureGallery181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_gmfgraph_FigureGallery__gmf_all_gmfgraph_FigureGallery181", None)
        self.__gmf_all_gmfgraph_FigureGallery181 = value if value is not None else set()
        
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
    def gmf_all_gmfgraph_FigureGallery183(self):
        return self.__gmf_all_gmfgraph_FigureGallery183

    @gmf_all_gmfgraph_FigureGallery183.setter
    def gmf_all_gmfgraph_FigureGallery183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_gmfgraph_FigureGallery__gmf_all_gmfgraph_FigureGallery183", None)
        self.__gmf_all_gmfgraph_FigureGallery183 = value if value is not None else set()
        
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
                    

class gmf_all_gmfgraph_Canvas(Identity):

    pass
class tooldef_PredefinedItem:

    pass
class tooldef_Menu:

    pass
class gmf_all_tooldef_PopupMenu(tooldef_ContributionItem, tooldef_Menu):

    def __init__(self, iD: str):
        self.iD = iD
        
        pass
    @property
    def iD(self):
        return self.__iD

    @iD.setter
    def iD(self, iD: str):
        self.__iD = iD


class gmf_all_tooldef_PredefinedMenu(tooldef_Menu, tooldef_PredefinedItem):

    pass
class ItemBase:

    pass
class gmf_all_tooldef_ContributionItem(ItemBase):

    def __init__(self, title: str, gmf_all_tooldef_ContributionItem: "Image" = None, ItemBase163: "gmf_all_tooldef_ItemRef" = None, ItemBase: "gmf_all_tooldef_Menu" = None):
        self.title = title
        self.gmf_all_tooldef_ContributionItem = gmf_all_tooldef_ContributionItem
        
        pass
    @property
    def title(self):
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
            if hasattr(old_value, "Image161"):
                opp_val = getattr(old_value, "Image161", None)
                if opp_val == self:
                    setattr(old_value, "Image161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Image161"):
                opp_val = getattr(value, "Image161", None)
                setattr(value, "Image161", self)

class gmf_all_tooldef_Separator(ItemBase):

    def __init__(self, name: str, ItemBase163: "gmf_all_tooldef_ItemRef" = None, ItemBase: "gmf_all_tooldef_Menu" = None):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class gmf_all_tooldef_PredefinedItem(ItemBase):

    def __init__(self, identifier: str, ItemBase163: "gmf_all_tooldef_ItemRef" = None, ItemBase: "gmf_all_tooldef_Menu" = None):
        self.identifier = identifier
        
        pass
    @property
    def identifier(self):
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier


class gmf_all_tooldef_Menu(ABC):

    pass
class gmf_all_tooldef_ItemBase(ABC):

    pass
class gmf_all_tooldef_ItemRef(ItemBase):

    pass
class ContributionItem:

    pass
class gmf_all_tooldef_MenuAction(ContributionItem):

    def __init__(self, kind: str, hotKey: str):
        self.kind = kind
        self.hotKey = hotKey
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def hotKey(self):
        return self.__hotKey

    @hotKey.setter
    def hotKey(self, hotKey: str):
        self.__hotKey = hotKey


class Image:

    pass
class gmf_all_tooldef_BundleImage(Image):

    def __init__(self, path: str, bundle: str, Image152: "gmf_all_tooldef_AbstractTool" = None, Image: "gmf_all_tooldef_AbstractTool" = None, Image161: "gmf_all_tooldef_ContributionItem" = None):
        self.path = path
        self.bundle = bundle
        
        pass
    @property
    def bundle(self):
        return self.__bundle

    @bundle.setter
    def bundle(self, bundle: str):
        self.__bundle = bundle


    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path


class gmf_all_tooldef_DefaultImage(Image):

    pass
class gmf_all_tooldef_AbstractTool(ABC):

    def __init__(self, title: str, description: str, gmf_all_tooldef_AbstractTool: "Image" = None, gmf_all_tooldef_AbstractTool151: "Image" = None):
        self.title = title
        self.description = description
        self.gmf_all_tooldef_AbstractTool = gmf_all_tooldef_AbstractTool
        self.gmf_all_tooldef_AbstractTool151 = gmf_all_tooldef_AbstractTool151
        
        pass
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


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
    def gmf_all_tooldef_AbstractTool151(self):
        return self.__gmf_all_tooldef_AbstractTool151

    @gmf_all_tooldef_AbstractTool151.setter
    def gmf_all_tooldef_AbstractTool151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_tooldef_AbstractTool__gmf_all_tooldef_AbstractTool151", None)
        self.__gmf_all_tooldef_AbstractTool151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Image152"):
                opp_val = getattr(old_value, "Image152", None)
                if opp_val == self:
                    setattr(old_value, "Image152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Image152"):
                opp_val = getattr(value, "Image152", None)
                setattr(value, "Image152", self)

class Menu:

    pass
class gmf_all_tooldef_ContextMenu(Menu):

    pass
class gmf_all_tooldef_MainMenu(Menu):

    def __init__(self, title: str, Menu: "gmf_all_tooldef_ToolRegistry" = None):
        self.title = title
        
        pass
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


class gmf_all_tooldef_Toolbar(Menu):

    pass
class MenuAction:

    pass
class gmf_all_tooldef_ToolRegistry:

    pass
class Pin:

    pass
class gmf_all_gmfgraph_CustomPin(Pin):

    def __init__(self, customOperationName: str, customOperationType: str, Pin: "gmf_all_mappings_VisualEffectMapping" = None, Pin286: "gmf_all_gmfgraph_PinOwner" = None):
        self.customOperationName = customOperationName
        self.customOperationType = customOperationType
        
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


class gmf_all_gmfgraph_VisiblePin(Pin):

    pass
class gmf_all_gmfgraph_ColorPin(Pin):

    def __init__(self, backgroundNotForeground: bool, Pin: "gmf_all_mappings_VisualEffectMapping" = None, Pin286: "gmf_all_gmfgraph_PinOwner" = None):
        self.backgroundNotForeground = backgroundNotForeground
        
        pass
    @property
    def backgroundNotForeground(self):
        return self.__backgroundNotForeground

    @backgroundNotForeground.setter
    def backgroundNotForeground(self, backgroundNotForeground: bool):
        self.__backgroundNotForeground = backgroundNotForeground


class gmf_all_mappings_VisualEffectMapping:

    def __init__(self, oclExpression: str, gmf_all_mappings_VisualEffectMapping: "Pin" = None, visualEffects: "MappingEntry" = None):
        self.oclExpression = oclExpression
        self.gmf_all_mappings_VisualEffectMapping = gmf_all_mappings_VisualEffectMapping
        self.visualEffects = visualEffects
        
        pass
    @property
    def oclExpression(self):
        return self.__oclExpression

    @oclExpression.setter
    def oclExpression(self, oclExpression: str):
        self.__oclExpression = oclExpression


    @property
    def visualEffects(self):
        return self.__visualEffects

    @visualEffects.setter
    def visualEffects(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_mappings_VisualEffectMapping__visualEffects", None)
        self.__visualEffects = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MappingEntry142"):
                opp_val = getattr(old_value, "MappingEntry142", None)
                if opp_val == self:
                    setattr(old_value, "MappingEntry142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MappingEntry142"):
                opp_val = getattr(value, "MappingEntry142", None)
                setattr(value, "MappingEntry142", self)

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

class gmf_all_mappings_Measurable(ABC):

    pass
class gmf_all_mappings_Auditable(ABC):

    pass
class ToolContainer:

    pass
class gmf_all_tooldef_Palette(ToolContainer):

    pass
class gmf_all_tooldef_ToolGroup(ToolContainer):

    def __init__(self, collapsible: bool, stack: bool, gmf_all_tooldef_ToolGroup: "AbstractTool" = None):
        self.collapsible = collapsible
        self.stack = stack
        self.gmf_all_tooldef_ToolGroup = gmf_all_tooldef_ToolGroup
        
        pass
    @property
    def stack(self):
        return self.__stack

    @stack.setter
    def stack(self, stack: bool):
        self.__stack = stack


    @property
    def collapsible(self):
        return self.__collapsible

    @collapsible.setter
    def collapsible(self, collapsible: bool):
        self.__collapsible = collapsible


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
            if hasattr(old_value, "AbstractTool156"):
                opp_val = getattr(old_value, "AbstractTool156", None)
                if opp_val == self:
                    setattr(old_value, "AbstractTool156", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractTool156"):
                opp_val = getattr(value, "AbstractTool156", None)
                setattr(value, "AbstractTool156", self)

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
class gmf_all_mappings_DiagramElementTarget(mappings_Measurable, mappings_Auditable):

    pass
class gmf_all_mappings_NotationElementTarget(mappings_Measurable, mappings_Auditable):

    pass
class gmf_all_mappings_DomainElementTarget(mappings_Auditable, mappings_Measurable):

    pass
class Auditable:

    pass
class gmf_all_mappings_AuditedMetricTarget(Auditable):

    pass
class RuleBase:

    pass
class gmf_all_mappings_MetricRule(RuleBase):

    def __init__(self, key: str, lowLimit: str, highLimit: str, gmf_all_mappings_MetricRule: "ValueExpression" = None, gmf_all_mappings_MetricRule135: "Measurable" = None, metrics: "MetricContainer" = None):
        self.key = key
        self.lowLimit = lowLimit
        self.highLimit = highLimit
        self.gmf_all_mappings_MetricRule = gmf_all_mappings_MetricRule
        self.gmf_all_mappings_MetricRule135 = gmf_all_mappings_MetricRule135
        self.metrics = metrics
        
        pass
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    @property
    def lowLimit(self):
        return self.__lowLimit

    @lowLimit.setter
    def lowLimit(self, lowLimit: str):
        self.__lowLimit = lowLimit


    @property
    def highLimit(self):
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
            if hasattr(old_value, "ValueExpression133"):
                opp_val = getattr(old_value, "ValueExpression133", None)
                if opp_val == self:
                    setattr(old_value, "ValueExpression133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ValueExpression133"):
                opp_val = getattr(value, "ValueExpression133", None)
                setattr(value, "ValueExpression133", self)

    @property
    def metrics(self):
        return self.__metrics

    @metrics.setter
    def metrics(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_mappings_MetricRule__metrics", None)
        self.__metrics = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MetricContainer137"):
                opp_val = getattr(old_value, "MetricContainer137", None)
                if opp_val == self:
                    setattr(old_value, "MetricContainer137", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MetricContainer137"):
                opp_val = getattr(value, "MetricContainer137", None)
                setattr(value, "MetricContainer137", self)

    @property
    def gmf_all_mappings_MetricRule135(self):
        return self.__gmf_all_mappings_MetricRule135

    @gmf_all_mappings_MetricRule135.setter
    def gmf_all_mappings_MetricRule135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_mappings_MetricRule__gmf_all_mappings_MetricRule135", None)
        self.__gmf_all_mappings_MetricRule135 = value
        
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

    def __init__(self, id: str, severity: str, useInLiveMode: bool, message: str, gmf_all_mappings_AuditRule: "Constraint" = None, gmf_all_mappings_AuditRule119: "Auditable" = None, audits: "AuditContainer" = None):
        self.id = id
        self.severity = severity
        self.useInLiveMode = useInLiveMode
        self.message = message
        self.gmf_all_mappings_AuditRule = gmf_all_mappings_AuditRule
        self.gmf_all_mappings_AuditRule119 = gmf_all_mappings_AuditRule119
        self.audits = audits
        
        pass
    @property
    def useInLiveMode(self):
        return self.__useInLiveMode

    @useInLiveMode.setter
    def useInLiveMode(self, useInLiveMode: bool):
        self.__useInLiveMode = useInLiveMode


    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message


    @property
    def severity(self):
        return self.__severity

    @severity.setter
    def severity(self, severity: str):
        self.__severity = severity


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def gmf_all_mappings_AuditRule119(self):
        return self.__gmf_all_mappings_AuditRule119

    @gmf_all_mappings_AuditRule119.setter
    def gmf_all_mappings_AuditRule119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_mappings_AuditRule__gmf_all_mappings_AuditRule119", None)
        self.__gmf_all_mappings_AuditRule119 = value
        
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
    def audits(self):
        return self.__audits

    @audits.setter
    def audits(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_mappings_AuditRule__audits", None)
        self.__audits = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AuditContainer121"):
                opp_val = getattr(old_value, "AuditContainer121", None)
                if opp_val == self:
                    setattr(old_value, "AuditContainer121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AuditContainer121"):
                opp_val = getattr(value, "AuditContainer121", None)
                setattr(value, "AuditContainer121", self)

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
            if hasattr(old_value, "Constraint117"):
                opp_val = getattr(old_value, "Constraint117", None)
                if opp_val == self:
                    setattr(old_value, "Constraint117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Constraint117"):
                opp_val = getattr(value, "Constraint117", None)
                setattr(value, "Constraint117", self)

class gmf_all_mappings_RuleBase(ABC):

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        
        pass
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class gmf_all_mappings_DomainAttributeTarget(Auditable):

    def __init__(self, nullAsError: bool, gmf_all_mappings_DomainAttributeTarget: "mappings_gmf_all_EAttribute" = None, Auditable: "gmf_all_mappings_AuditRule" = None):
        self.nullAsError = nullAsError
        self.gmf_all_mappings_DomainAttributeTarget = gmf_all_mappings_DomainAttributeTarget
        
        pass
    @property
    def nullAsError(self):
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
            if hasattr(old_value, "mappings_gmf_all_EAttribute125"):
                opp_val = getattr(old_value, "mappings_gmf_all_EAttribute125", None)
                if opp_val == self:
                    setattr(old_value, "mappings_gmf_all_EAttribute125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mappings_gmf_all_EAttribute125"):
                opp_val = getattr(value, "mappings_gmf_all_EAttribute125", None)
                setattr(value, "mappings_gmf_all_EAttribute125", self)

class gmf_all_mappings_AuditContainer:

    def __init__(self, description: str, id: str, name: str, childContainers: "AuditContainer" = None, container: set["AuditRule"] = None, parentContainer: set["AuditContainer"] = None):
        self.description = description
        self.id = id
        self.name = name
        self.childContainers = childContainers
        self.container = container if container is not None else set()
        self.parentContainer = parentContainer if parentContainer is not None else set()
        
        pass
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def container(self):
        return self.__container

    @container.setter
    def container(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_mappings_AuditContainer__container", None)
        self.__container = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AuditRule"):
                    opp_val = getattr(item, "AuditRule", None)
                    
                    if opp_val == self:
                        setattr(item, "AuditRule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AuditRule"):
                    opp_val = getattr(item, "AuditRule", None)
                    
                    setattr(item, "AuditRule", self)
                    

    @property
    def parentContainer(self):
        return self.__parentContainer

    @parentContainer.setter
    def parentContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_mappings_AuditContainer__parentContainer", None)
        self.__parentContainer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AuditContainer115"):
                    opp_val = getattr(item, "AuditContainer115", None)
                    
                    if opp_val == self:
                        setattr(item, "AuditContainer115", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AuditContainer115"):
                    opp_val = getattr(item, "AuditContainer115", None)
                    
                    setattr(item, "AuditContainer115", self)
                    

    @property
    def childContainers(self):
        return self.__childContainers

    @childContainers.setter
    def childContainers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_mappings_AuditContainer__childContainers", None)
        self.__childContainers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AuditContainer112"):
                opp_val = getattr(old_value, "AuditContainer112", None)
                if opp_val == self:
                    setattr(old_value, "AuditContainer112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AuditContainer112"):
                opp_val = getattr(value, "AuditContainer112", None)
                setattr(value, "AuditContainer112", self)

class gmf_all_mappings_AppearanceSteward(ABC):

    pass
class AbstractTool:

    pass
class gmf_all_tooldef_ToolContainer(AbstractTool):

    pass
class gmf_all_tooldef_StandardTool(AbstractTool):

    def __init__(self, toolKind: str, AbstractTool154: "gmf_all_tooldef_ToolContainer" = None, AbstractTool: "gmf_all_mappings_ToolOwner" = None, AbstractTool156: "gmf_all_tooldef_ToolGroup" = None, AbstractTool158: "gmf_all_tooldef_Palette" = None):
        self.toolKind = toolKind
        
        pass
    @property
    def toolKind(self):
        return self.__toolKind

    @toolKind.setter
    def toolKind(self, toolKind: str):
        self.__toolKind = toolKind


class gmf_all_tooldef_CreationTool(AbstractTool):

    pass
class gmf_all_tooldef_PaletteSeparator(AbstractTool):

    pass
class gmf_all_tooldef_GenericTool(AbstractTool):

    def __init__(self, toolClass: str, AbstractTool154: "gmf_all_tooldef_ToolContainer" = None, AbstractTool: "gmf_all_mappings_ToolOwner" = None, AbstractTool156: "gmf_all_tooldef_ToolGroup" = None, AbstractTool158: "gmf_all_tooldef_Palette" = None):
        self.toolClass = toolClass
        
        pass
    @property
    def toolClass(self):
        return self.__toolClass

    @toolClass.setter
    def toolClass(self, toolClass: str):
        self.__toolClass = toolClass


class gmf_all_mappings_ToolOwner(ABC):

    pass
class ContextMenu:

    pass
class gmf_all_mappings_MenuOwner(ABC):

    pass
class FeatureSeqInitializer:

    pass
class AuditRule:

    pass
class ReferenceNewElementSpec:

    pass
class FeatureInitializer:

    pass
class gmf_all_mappings_ReferenceNewElementSpec(FeatureInitializer):

    pass
class gmf_all_mappings_FeatureValueSpec(FeatureInitializer):

    pass
class gmf_all_mappings_FeatureSeqInitializer(ElementInitializer):

    pass
class gmf_all_mappings_ElementInitializer(ABC):

    pass
class gmf_all_mappings_ValueExpression:

    def __init__(self, body: str, language: str, langName: str):
        self.body = body
        self.language = language
        self.langName = langName
        
        pass
    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language


    @property
    def langName(self):
        return self.__langName

    @langName.setter
    def langName(self, langName: str):
        self.__langName = langName


    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, body: str):
        self.__body = body


class gmf_all_mappings_FeatureInitializer(ABC):

    pass
class gmf_all_mappings_LinkConstraints:

    pass
class gmf_all_mappings_ExpressionLabelMapping(LabelMapping):

    pass
class gmf_all_mappings_DesignLabelMapping(LabelMapping):

    pass
class gmf_all_mappings_OclChoiceLabelMapping(LabelMapping):

    pass
class mappings_gmf_all_EAttribute:

    pass
class gmf_all_mappings_FeatureLabelMapping(LabelMapping):

    def __init__(self, viewPattern: str, editorPattern: str, editPattern: str, viewMethod: str, editMethod: str, gmf_all_mappings_FeatureLabelMapping: set["mappings_gmf_all_EAttribute"] = None, gmf_all_mappings_FeatureLabelMapping70: set["mappings_gmf_all_EAttribute"] = None, LabelMapping: "gmf_all_mappings_MappingEntry" = None):
        self.viewPattern = viewPattern
        self.editorPattern = editorPattern
        self.editPattern = editPattern
        self.viewMethod = viewMethod
        self.editMethod = editMethod
        self.gmf_all_mappings_FeatureLabelMapping = gmf_all_mappings_FeatureLabelMapping if gmf_all_mappings_FeatureLabelMapping is not None else set()
        self.gmf_all_mappings_FeatureLabelMapping70 = gmf_all_mappings_FeatureLabelMapping70 if gmf_all_mappings_FeatureLabelMapping70 is not None else set()
        
        pass
    @property
    def viewPattern(self):
        return self.__viewPattern

    @viewPattern.setter
    def viewPattern(self, viewPattern: str):
        self.__viewPattern = viewPattern


    @property
    def editorPattern(self):
        return self.__editorPattern

    @editorPattern.setter
    def editorPattern(self, editorPattern: str):
        self.__editorPattern = editorPattern


    @property
    def editMethod(self):
        return self.__editMethod

    @editMethod.setter
    def editMethod(self, editMethod: str):
        self.__editMethod = editMethod


    @property
    def viewMethod(self):
        return self.__viewMethod

    @viewMethod.setter
    def viewMethod(self, viewMethod: str):
        self.__viewMethod = viewMethod


    @property
    def editPattern(self):
        return self.__editPattern

    @editPattern.setter
    def editPattern(self, editPattern: str):
        self.__editPattern = editPattern


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
    def gmf_all_mappings_FeatureLabelMapping70(self):
        return self.__gmf_all_mappings_FeatureLabelMapping70

    @gmf_all_mappings_FeatureLabelMapping70.setter
    def gmf_all_mappings_FeatureLabelMapping70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_mappings_FeatureLabelMapping__gmf_all_mappings_FeatureLabelMapping70", None)
        self.__gmf_all_mappings_FeatureLabelMapping70 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mappings_gmf_all_EAttribute71"):
                    opp_val = getattr(item, "mappings_gmf_all_EAttribute71", None)
                    
                    if opp_val == self:
                        setattr(item, "mappings_gmf_all_EAttribute71", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mappings_gmf_all_EAttribute71"):
                    opp_val = getattr(item, "mappings_gmf_all_EAttribute71", None)
                    
                    setattr(item, "mappings_gmf_all_EAttribute71", self)
                    

class MappingEntry:

    pass
class DiagramLabel:

    pass
class gmf_all_mappings_LabelMapping:

    def __init__(self, readOnly: bool, labelMappings: "MappingEntry" = None, gmf_all_mappings_LabelMapping: "DiagramLabel" = None):
        self.readOnly = readOnly
        self.labelMappings = labelMappings
        self.gmf_all_mappings_LabelMapping = gmf_all_mappings_LabelMapping
        
        pass
    @property
    def readOnly(self):
        return self.__readOnly

    @readOnly.setter
    def readOnly(self, readOnly: bool):
        self.__readOnly = readOnly


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

    @property
    def labelMappings(self):
        return self.__labelMappings

    @labelMappings.setter
    def labelMappings(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gmf_all_mappings_LabelMapping__labelMappings", None)
        self.__labelMappings = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MappingEntry"):
                opp_val = getattr(old_value, "MappingEntry", None)
                if opp_val == self:
                    setattr(old_value, "MappingEntry", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MappingEntry"):
                opp_val = getattr(value, "MappingEntry", None)
                setattr(value, "MappingEntry", self)

class Toolbar:

    pass
class MainMenu:

    pass
class ValueExpression:

    pass
class gmf_all_mappings_Constraint(ValueExpression):

    pass
class Canvas:

    pass
class gmf_all_mappings_CanvasMapping:

    pass
class LinkConstraints:

    pass
class mappings_gmf_all_EStructuralFeature:

    pass
class Connection:

    pass
class mappings_NeedsContainment:

    pass
class gmf_all_mappings_LinkMapping(mappings_NeedsContainment, mappings_MappingEntry, mappings_ToolOwner, mappings_MenuOwner, mappings_AppearanceSteward):

    pass
class Compartment:

    pass
class gmf_all_mappings_CompartmentMapping:

    pass
class ChildReference:

    pass
class Palette:

    pass
class mappings_gmf_all_EPackage:

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
class MetricContainer:

    pass
class AuditContainer:

    pass
class StyleSelector:

    pass
class gmf_all_tooldef_GenericStyleSelector(StyleSelector):

    def __init__(self, values: str, StyleSelector: "gmf_all_mappings_Mapping" = None, StyleSelector110: "gmf_all_mappings_AppearanceSteward" = None):
        self.values = values
        
        pass
    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values


class CanvasMapping:

    pass
class LinkMapping:

    pass
class mappings_gmf_all_EReference:

    pass
class gmf_all_mappings_NeedsContainment(ABC):

    pass
class VisualEffectMapping:

    pass
class TopNodeReference:

    pass
class gmf_all_mappings_Mapping:

    pass