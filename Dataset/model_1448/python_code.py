from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class GSeverity(Enum):
    error = "error"
    warning = "warning"
    info = "info"


############################################
# Definition of Classes
############################################

class graph_GAlignable:

    pass
class graph_GIssue:

    def __init__(self, severity: str, message: str, graph_GIssue: "graph_GIssueMarker" = None):
        self.severity = severity
        self.message = message
        self.graph_GIssue = graph_GIssue
        
        pass
    @property
    def severity(self):
        return self.__severity

    @severity.setter
    def severity(self, severity: str):
        self.__severity = severity


    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message


    @property
    def graph_GIssue(self):
        return self.__graph_GIssue

    @graph_GIssue.setter
    def graph_GIssue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_GIssue__graph_GIssue", None)
        self.__graph_GIssue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_GIssueMarker"):
                opp_val = getattr(old_value, "graph_GIssueMarker", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_GIssueMarker"):
                opp_val = getattr(value, "graph_GIssueMarker", None)
                if opp_val is None:
                    setattr(value, "graph_GIssueMarker", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class GAlignable:

    pass
class graph_GLayouting(ABC):

    def __init__(self, layout: str, graph_GLayouting: set["graph_StringToObjectMapEntry"] = None):
        self.layout = layout
        self.graph_GLayouting = graph_GLayouting if graph_GLayouting is not None else set()
        
        pass
    @property
    def layout(self):
        return self.__layout

    @layout.setter
    def layout(self, layout: str):
        self.__layout = layout


    @property
    def graph_GLayouting(self):
        return self.__graph_GLayouting

    @graph_GLayouting.setter
    def graph_GLayouting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_GLayouting__graph_GLayouting", None)
        self.__graph_GLayouting = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graph_StringToObjectMapEntry20"):
                    opp_val = getattr(item, "graph_StringToObjectMapEntry20", None)
                    
                    if opp_val == self:
                        setattr(item, "graph_StringToObjectMapEntry20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graph_StringToObjectMapEntry20"):
                    opp_val = getattr(item, "graph_StringToObjectMapEntry20", None)
                    
                    setattr(item, "graph_StringToObjectMapEntry20", self)
                    

class graph_GEdgePlacement:

    def __init__(self, position: str, offset: str, side: str, rotate: bool, graph_GEdgePlacement: "graph_GEdgeLayoutable" = None):
        self.position = position
        self.offset = offset
        self.side = side
        self.rotate = rotate
        self.graph_GEdgePlacement = graph_GEdgePlacement
        
        pass
    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, side: str):
        self.__side = side


    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position


    @property
    def offset(self):
        return self.__offset

    @offset.setter
    def offset(self, offset: str):
        self.__offset = offset


    @property
    def rotate(self):
        return self.__rotate

    @rotate.setter
    def rotate(self, rotate: bool):
        self.__rotate = rotate


    @property
    def graph_GEdgePlacement(self):
        return self.__graph_GEdgePlacement

    @graph_GEdgePlacement.setter
    def graph_GEdgePlacement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_GEdgePlacement__graph_GEdgePlacement", None)
        self.__graph_GEdgePlacement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_GEdgeLayoutable"):
                opp_val = getattr(old_value, "graph_GEdgeLayoutable", None)
                if opp_val == self:
                    setattr(old_value, "graph_GEdgeLayoutable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_GEdgeLayoutable"):
                opp_val = getattr(value, "graph_GEdgeLayoutable", None)
                setattr(value, "graph_GEdgeLayoutable", self)

class graph_GEdgeLayoutable(ABC):

    pass
class graph_GDimension:

    def __init__(self, width: float, height: float, graph_GDimension: "graph_GBoundsAware" = None):
        self.width = width
        self.height = height
        self.graph_GDimension = graph_GDimension
        
        pass
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: float):
        self.__height = height


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: float):
        self.__width = width


    @property
    def graph_GDimension(self):
        return self.__graph_GDimension

    @graph_GDimension.setter
    def graph_GDimension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_GDimension__graph_GDimension", None)
        self.__graph_GDimension = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_GBoundsAware17"):
                opp_val = getattr(old_value, "graph_GBoundsAware17", None)
                if opp_val == self:
                    setattr(old_value, "graph_GBoundsAware17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_GBoundsAware17"):
                opp_val = getattr(value, "graph_GBoundsAware17", None)
                setattr(value, "graph_GBoundsAware17", self)

class graph_GBoundsAware(ABC):

    pass
class graph_GModelElement(ABC):

    def __init__(self, trace: str, type: str, id: str, cssClasses: str, GModelElement4: "graph_GModelElement" = None, children: "graph_GModelElement" = None, GModelElement: "graph_GModelElement" = None, parent: set["graph_GModelElement"] = None, graph_GModelElement: "graph_GEdge" = None, graph_GModelElement12: "graph_GEdge" = None):
        self.trace = trace
        self.type = type
        self.id = id
        self.cssClasses = cssClasses
        self.GModelElement4 = GModelElement4
        self.children = children
        self.GModelElement = GModelElement
        self.parent = parent if parent is not None else set()
        self.graph_GModelElement = graph_GModelElement
        self.graph_GModelElement12 = graph_GModelElement12
        
        pass
    @property
    def cssClasses(self):
        return self.__cssClasses

    @cssClasses.setter
    def cssClasses(self, cssClasses: str):
        self.__cssClasses = cssClasses


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def trace(self):
        return self.__trace

    @trace.setter
    def trace(self, trace: str):
        self.__trace = trace


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def GModelElement4(self):
        return self.__GModelElement4

    @GModelElement4.setter
    def GModelElement4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_GModelElement__GModelElement4", None)
        self.__GModelElement4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "children"):
                opp_val = getattr(old_value, "children", None)
                if opp_val == self:
                    setattr(old_value, "children", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "children"):
                opp_val = getattr(value, "children", None)
                setattr(value, "children", self)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_GModelElement__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GModelElement"):
                    opp_val = getattr(item, "GModelElement", None)
                    
                    if opp_val == self:
                        setattr(item, "GModelElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GModelElement"):
                    opp_val = getattr(item, "GModelElement", None)
                    
                    setattr(item, "GModelElement", self)
                    

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_GModelElement__children", None)
        self.__children = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GModelElement4"):
                opp_val = getattr(old_value, "GModelElement4", None)
                if opp_val == self:
                    setattr(old_value, "GModelElement4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GModelElement4"):
                opp_val = getattr(value, "GModelElement4", None)
                setattr(value, "GModelElement4", self)

    @property
    def GModelElement(self):
        return self.__GModelElement

    @GModelElement.setter
    def GModelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_GModelElement__GModelElement", None)
        self.__GModelElement = value
        
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
    def graph_GModelElement(self):
        return self.__graph_GModelElement

    @graph_GModelElement.setter
    def graph_GModelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_GModelElement__graph_GModelElement", None)
        self.__graph_GModelElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_GEdge9"):
                opp_val = getattr(old_value, "graph_GEdge9", None)
                if opp_val == self:
                    setattr(old_value, "graph_GEdge9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_GEdge9"):
                opp_val = getattr(value, "graph_GEdge9", None)
                setattr(value, "graph_GEdge9", self)

    @property
    def graph_GModelElement12(self):
        return self.__graph_GModelElement12

    @graph_GModelElement12.setter
    def graph_GModelElement12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_GModelElement__graph_GModelElement12", None)
        self.__graph_GModelElement12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_GEdge11"):
                opp_val = getattr(old_value, "graph_GEdge11", None)
                if opp_val == self:
                    setattr(old_value, "graph_GEdge11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_GEdge11"):
                opp_val = getattr(value, "graph_GEdge11", None)
                setattr(value, "graph_GEdge11", self)

class graph_GPoint:

    def __init__(self, x: float, y: float, graph_GPoint: "graph_GEdge" = None, graph_GPoint15: "graph_GBoundsAware" = None, graph_GPoint22: "graph_GAlignable" = None):
        self.x = x
        self.y = y
        self.graph_GPoint = graph_GPoint
        self.graph_GPoint15 = graph_GPoint15
        self.graph_GPoint22 = graph_GPoint22
        
        pass
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x


    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y


    @property
    def graph_GPoint(self):
        return self.__graph_GPoint

    @graph_GPoint.setter
    def graph_GPoint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_GPoint__graph_GPoint", None)
        self.__graph_GPoint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_GEdge"):
                opp_val = getattr(old_value, "graph_GEdge", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_GEdge"):
                opp_val = getattr(value, "graph_GEdge", None)
                if opp_val is None:
                    setattr(value, "graph_GEdge", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graph_GPoint22(self):
        return self.__graph_GPoint22

    @graph_GPoint22.setter
    def graph_GPoint22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_GPoint__graph_GPoint22", None)
        self.__graph_GPoint22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_GAlignable"):
                opp_val = getattr(old_value, "graph_GAlignable", None)
                if opp_val == self:
                    setattr(old_value, "graph_GAlignable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_GAlignable"):
                opp_val = getattr(value, "graph_GAlignable", None)
                setattr(value, "graph_GAlignable", self)

    @property
    def graph_GPoint15(self):
        return self.__graph_GPoint15

    @graph_GPoint15.setter
    def graph_GPoint15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_GPoint__graph_GPoint15", None)
        self.__graph_GPoint15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_GBoundsAware"):
                opp_val = getattr(old_value, "graph_GBoundsAware", None)
                if opp_val == self:
                    setattr(old_value, "graph_GBoundsAware", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_GBoundsAware"):
                opp_val = getattr(value, "graph_GBoundsAware", None)
                setattr(value, "graph_GBoundsAware", self)

class GLayouting:

    pass
class GEdgeLayoutable:

    pass
class GShapeElement:

    pass
class graph_GButton(GShapeElement):

    def __init__(self, enabled: bool):
        self.enabled = enabled
        
        pass
    @property
    def enabled(self):
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled: bool):
        self.__enabled = enabled


class graph_GIssueMarker(GShapeElement):

    pass
class graph_GCompartment(GShapeElement, GLayouting):

    pass
class graph_GLabel(GAlignable, GShapeElement, GEdgeLayoutable):

    def __init__(self, text: str):
        self.text = text
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


class graph_GPort(GShapeElement):

    pass
class graph_GNode(GShapeElement, GEdgeLayoutable, GLayouting):

    pass
class graph_GBounds:

    def __init__(self, x: float, y: float, width: float, height: float, graph_GBounds: "graph_GModelRoot" = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.graph_GBounds = graph_GBounds
        
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
    def graph_GBounds(self):
        return self.__graph_GBounds

    @graph_GBounds.setter
    def graph_GBounds(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_GBounds__graph_GBounds", None)
        self.__graph_GBounds = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_GModelRoot"):
                opp_val = getattr(old_value, "graph_GModelRoot", None)
                if opp_val == self:
                    setattr(old_value, "graph_GModelRoot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_GModelRoot"):
                opp_val = getattr(value, "graph_GModelRoot", None)
                setattr(value, "graph_GModelRoot", self)

class graph_StringToObjectMapEntry:

    def __init__(self, key: str, value: str, graph_StringToObjectMapEntry: "graph_GGraph" = None, graph_StringToObjectMapEntry20: "graph_GLayouting" = None):
        self.key = key
        self.value = value
        self.graph_StringToObjectMapEntry = graph_StringToObjectMapEntry
        self.graph_StringToObjectMapEntry20 = graph_StringToObjectMapEntry20
        
        pass
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def graph_StringToObjectMapEntry(self):
        return self.__graph_StringToObjectMapEntry

    @graph_StringToObjectMapEntry.setter
    def graph_StringToObjectMapEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_StringToObjectMapEntry__graph_StringToObjectMapEntry", None)
        self.__graph_StringToObjectMapEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_GGraph"):
                opp_val = getattr(old_value, "graph_GGraph", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_GGraph"):
                opp_val = getattr(value, "graph_GGraph", None)
                if opp_val is None:
                    setattr(value, "graph_GGraph", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def graph_StringToObjectMapEntry20(self):
        return self.__graph_StringToObjectMapEntry20

    @graph_StringToObjectMapEntry20.setter
    def graph_StringToObjectMapEntry20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_StringToObjectMapEntry__graph_StringToObjectMapEntry20", None)
        self.__graph_StringToObjectMapEntry20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_GLayouting"):
                opp_val = getattr(old_value, "graph_GLayouting", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_GLayouting"):
                opp_val = getattr(value, "graph_GLayouting", None)
                if opp_val is None:
                    setattr(value, "graph_GLayouting", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class GModelRoot:

    pass
class graph_GHtmlRoot(GModelRoot):

    def __init__(self, classes: str):
        self.classes = classes
        
        pass
    @property
    def classes(self):
        return self.__classes

    @classes.setter
    def classes(self, classes: str):
        self.__classes = classes


class GBoundsAware:

    pass
class graph_GGraph(GBoundsAware, GModelRoot):

    pass
class GModelElement:

    pass
class graph_GPreRenderedElement(GModelElement):

    def __init__(self, code: str):
        self.code = code
        
        pass
    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code


class graph_GEdge(GModelElement):

    def __init__(self, sourceId: str, targetId: str, routerKind: str, graph_GEdge: set["graph_GPoint"] = None, graph_GEdge9: "graph_GModelElement" = None, graph_GEdge11: "graph_GModelElement" = None):
        self.sourceId = sourceId
        self.targetId = targetId
        self.routerKind = routerKind
        self.graph_GEdge = graph_GEdge if graph_GEdge is not None else set()
        self.graph_GEdge9 = graph_GEdge9
        self.graph_GEdge11 = graph_GEdge11
        
        pass
    @property
    def routerKind(self):
        return self.__routerKind

    @routerKind.setter
    def routerKind(self, routerKind: str):
        self.__routerKind = routerKind


    @property
    def sourceId(self):
        return self.__sourceId

    @sourceId.setter
    def sourceId(self, sourceId: str):
        self.__sourceId = sourceId


    @property
    def targetId(self):
        return self.__targetId

    @targetId.setter
    def targetId(self, targetId: str):
        self.__targetId = targetId


    @property
    def graph_GEdge(self):
        return self.__graph_GEdge

    @graph_GEdge.setter
    def graph_GEdge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_GEdge__graph_GEdge", None)
        self.__graph_GEdge = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "graph_GPoint"):
                    opp_val = getattr(item, "graph_GPoint", None)
                    
                    if opp_val == self:
                        setattr(item, "graph_GPoint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "graph_GPoint"):
                    opp_val = getattr(item, "graph_GPoint", None)
                    
                    setattr(item, "graph_GPoint", self)
                    

    @property
    def graph_GEdge9(self):
        return self.__graph_GEdge9

    @graph_GEdge9.setter
    def graph_GEdge9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_GEdge__graph_GEdge9", None)
        self.__graph_GEdge9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_GModelElement"):
                opp_val = getattr(old_value, "graph_GModelElement", None)
                if opp_val == self:
                    setattr(old_value, "graph_GModelElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_GModelElement"):
                opp_val = getattr(value, "graph_GModelElement", None)
                setattr(value, "graph_GModelElement", self)

    @property
    def graph_GEdge11(self):
        return self.__graph_GEdge11

    @graph_GEdge11.setter
    def graph_GEdge11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_GEdge__graph_GEdge11", None)
        self.__graph_GEdge11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_GModelElement12"):
                opp_val = getattr(old_value, "graph_GModelElement12", None)
                if opp_val == self:
                    setattr(old_value, "graph_GModelElement12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_GModelElement12"):
                opp_val = getattr(value, "graph_GModelElement12", None)
                setattr(value, "graph_GModelElement12", self)

class graph_GModelRoot(GModelElement):

    def __init__(self, revision: int, graph_GModelRoot: "graph_GBounds" = None):
        self.revision = revision
        self.graph_GModelRoot = graph_GModelRoot
        
        pass
    @property
    def revision(self):
        return self.__revision

    @revision.setter
    def revision(self, revision: int):
        self.__revision = revision


    @property
    def graph_GModelRoot(self):
        return self.__graph_GModelRoot

    @graph_GModelRoot.setter
    def graph_GModelRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_GModelRoot__graph_GModelRoot", None)
        self.__graph_GModelRoot = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_GBounds"):
                opp_val = getattr(old_value, "graph_GBounds", None)
                if opp_val == self:
                    setattr(old_value, "graph_GBounds", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_GBounds"):
                opp_val = getattr(value, "graph_GBounds", None)
                setattr(value, "graph_GBounds", self)

class graph_GShapeElement(GModelElement, GBoundsAware):

    pass