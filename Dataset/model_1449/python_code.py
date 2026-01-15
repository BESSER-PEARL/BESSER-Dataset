from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class GSide(Enum):
    left = "left"
    right = "right"
    top = "top"
    bottom = "bottom"
    on = "on"
class GSeverity(Enum):
    error = "error"
    warning = "warning"
    info = "info"


############################################
# Definition of Classes
############################################

class graph_GAlignable:

    pass
class graph_GLayouting(ABC):

    def __init__(self, layout: str, graph_GLayouting: "graph_GLayoutOptions" = None):
        self.layout = layout
        self.graph_GLayouting = graph_GLayouting
        
    @property
    def layout(self) -> str:
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
        self.__graph_GLayouting = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_GLayoutOptions22"):
                opp_val = getattr(old_value, "graph_GLayoutOptions22", None)
                if opp_val == self:
                    setattr(old_value, "graph_GLayoutOptions22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_GLayoutOptions22"):
                opp_val = getattr(value, "graph_GLayoutOptions22", None)
                setattr(value, "graph_GLayoutOptions22", self)

class graph_GEdgePlacement:

    def __init__(self, position: str, offset: str, side: str, graph_GEdgePlacement: "graph_GEdgeLayoutable" = None):
        self.position = position
        self.offset = offset
        self.side = side
        self.graph_GEdgePlacement = graph_GEdgePlacement
        
    @property
    def position(self) -> str:
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position

    @property
    def side(self) -> str:
        return self.__side

    @side.setter
    def side(self, side: str):
        self.__side = side

    @property
    def offset(self) -> str:
        return self.__offset

    @offset.setter
    def offset(self, offset: str):
        self.__offset = offset

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
class GAlignable:

    pass
class graph_GDimension:

    def __init__(self, width: float, height: float, graph_GDimension: "graph_GBoundsAware" = None):
        self.width = width
        self.height = height
        self.graph_GDimension = graph_GDimension
        
    @property
    def height(self) -> float:
        return self.__height

    @height.setter
    def height(self, height: float):
        self.__height = height

    @property
    def width(self) -> float:
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
            if hasattr(old_value, "graph_GBoundsAware19"):
                opp_val = getattr(old_value, "graph_GBoundsAware19", None)
                if opp_val == self:
                    setattr(old_value, "graph_GBoundsAware19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_GBoundsAware19"):
                opp_val = getattr(value, "graph_GBoundsAware19", None)
                setattr(value, "graph_GBoundsAware19", self)

class graph_GBoundsAware(ABC):

    pass
class graph_GIssue:

    def __init__(self, severity: str, message: str, graph_GIssue: "graph_GIssueMarker" = None):
        self.severity = severity
        self.message = message
        self.graph_GIssue = graph_GIssue
        
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

class graph_GPoint:

    def __init__(self, x: float, y: float, graph_GPoint: "graph_GEdge" = None, graph_GPoint17: "graph_GBoundsAware" = None, graph_GPoint24: "graph_GAlignable" = None):
        self.x = x
        self.y = y
        self.graph_GPoint = graph_GPoint
        self.graph_GPoint17 = graph_GPoint17
        self.graph_GPoint24 = graph_GPoint24
        
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
    def graph_GPoint24(self):
        return self.__graph_GPoint24

    @graph_GPoint24.setter
    def graph_GPoint24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_GPoint__graph_GPoint24", None)
        self.__graph_GPoint24 = value
        
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
    def graph_GPoint17(self):
        return self.__graph_GPoint17

    @graph_GPoint17.setter
    def graph_GPoint17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_GPoint__graph_GPoint17", None)
        self.__graph_GPoint17 = value
        
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
class graph_GPort(GShapeElement):

    pass
class graph_GLabel(GEdgeLayoutable, GAlignable, GShapeElement):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class graph_GCompartment(GLayouting, GShapeElement):

    pass
class graph_GButton(GShapeElement):

    def __init__(self, enabled: bool):
        self.enabled = enabled
        
    @property
    def enabled(self) -> bool:
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled: bool):
        self.__enabled = enabled

class graph_GIssueMarker(GShapeElement):

    pass
class graph_GNode(GLayouting, GEdgeLayoutable, GShapeElement):

    pass
class graph_GBounds:

    def __init__(self, x: float, y: float, width: float, height: float, graph_GBounds: "graph_GModelRoot" = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.graph_GBounds = graph_GBounds
        
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

    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, width: float):
        self.__width = width

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

class graph_GLayoutOptions:

    def __init__(self, paddingLeft: str, paddingRight: str, paddingTop: str, paddingBottom: str, paddingFactor: str, resizeContainer: bool, vGap: str, hGap: str, vAlign: str, hAlign: str, minWidth: str, minHeight: str, graph_GLayoutOptions: "graph_GGraph" = None, graph_GLayoutOptions22: "graph_GLayouting" = None):
        self.paddingLeft = paddingLeft
        self.paddingRight = paddingRight
        self.paddingTop = paddingTop
        self.paddingBottom = paddingBottom
        self.paddingFactor = paddingFactor
        self.resizeContainer = resizeContainer
        self.vGap = vGap
        self.hGap = hGap
        self.vAlign = vAlign
        self.hAlign = hAlign
        self.minWidth = minWidth
        self.minHeight = minHeight
        self.graph_GLayoutOptions = graph_GLayoutOptions
        self.graph_GLayoutOptions22 = graph_GLayoutOptions22
        
    @property
    def paddingBottom(self) -> str:
        return self.__paddingBottom

    @paddingBottom.setter
    def paddingBottom(self, paddingBottom: str):
        self.__paddingBottom = paddingBottom

    @property
    def vAlign(self) -> str:
        return self.__vAlign

    @vAlign.setter
    def vAlign(self, vAlign: str):
        self.__vAlign = vAlign

    @property
    def vGap(self) -> str:
        return self.__vGap

    @vGap.setter
    def vGap(self, vGap: str):
        self.__vGap = vGap

    @property
    def minHeight(self) -> str:
        return self.__minHeight

    @minHeight.setter
    def minHeight(self, minHeight: str):
        self.__minHeight = minHeight

    @property
    def paddingRight(self) -> str:
        return self.__paddingRight

    @paddingRight.setter
    def paddingRight(self, paddingRight: str):
        self.__paddingRight = paddingRight

    @property
    def hGap(self) -> str:
        return self.__hGap

    @hGap.setter
    def hGap(self, hGap: str):
        self.__hGap = hGap

    @property
    def resizeContainer(self) -> bool:
        return self.__resizeContainer

    @resizeContainer.setter
    def resizeContainer(self, resizeContainer: bool):
        self.__resizeContainer = resizeContainer

    @property
    def paddingLeft(self) -> str:
        return self.__paddingLeft

    @paddingLeft.setter
    def paddingLeft(self, paddingLeft: str):
        self.__paddingLeft = paddingLeft

    @property
    def minWidth(self) -> str:
        return self.__minWidth

    @minWidth.setter
    def minWidth(self, minWidth: str):
        self.__minWidth = minWidth

    @property
    def paddingTop(self) -> str:
        return self.__paddingTop

    @paddingTop.setter
    def paddingTop(self, paddingTop: str):
        self.__paddingTop = paddingTop

    @property
    def hAlign(self) -> str:
        return self.__hAlign

    @hAlign.setter
    def hAlign(self, hAlign: str):
        self.__hAlign = hAlign

    @property
    def paddingFactor(self) -> str:
        return self.__paddingFactor

    @paddingFactor.setter
    def paddingFactor(self, paddingFactor: str):
        self.__paddingFactor = paddingFactor

    @property
    def graph_GLayoutOptions22(self):
        return self.__graph_GLayoutOptions22

    @graph_GLayoutOptions22.setter
    def graph_GLayoutOptions22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_GLayoutOptions__graph_GLayoutOptions22", None)
        self.__graph_GLayoutOptions22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_GLayouting"):
                opp_val = getattr(old_value, "graph_GLayouting", None)
                if opp_val == self:
                    setattr(old_value, "graph_GLayouting", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_GLayouting"):
                opp_val = getattr(value, "graph_GLayouting", None)
                setattr(value, "graph_GLayouting", self)

    @property
    def graph_GLayoutOptions(self):
        return self.__graph_GLayoutOptions

    @graph_GLayoutOptions.setter
    def graph_GLayoutOptions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_GLayoutOptions__graph_GLayoutOptions", None)
        self.__graph_GLayoutOptions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_GGraph"):
                opp_val = getattr(old_value, "graph_GGraph", None)
                if opp_val == self:
                    setattr(old_value, "graph_GGraph", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_GGraph"):
                opp_val = getattr(value, "graph_GGraph", None)
                setattr(value, "graph_GGraph", self)

class GModelRoot:

    pass
class graph_GHtmlRoot(GModelRoot):

    def __init__(self, classes: str):
        self.classes = classes
        
    @property
    def classes(self) -> str:
        return self.__classes

    @classes.setter
    def classes(self, classes: str):
        self.__classes = classes

class GBoundsAware:

    pass
class graph_GGraph(GModelRoot, GBoundsAware):

    pass
class GModelElement:

    pass
class graph_GModelRoot(GModelElement):

    def __init__(self, revision: int, graph_GModelRoot: "graph_GBounds" = None):
        self.revision = revision
        self.graph_GModelRoot = graph_GModelRoot
        
    @property
    def revision(self) -> int:
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

class graph_GEdge(GModelElement):

    def __init__(self, sourceId: str, targetId: str, graph_GEdge: set["graph_GPoint"] = None, graph_GEdge11: "graph_GModelElement" = None, graph_GEdge13: "graph_GModelElement" = None):
        self.sourceId = sourceId
        self.targetId = targetId
        self.graph_GEdge = graph_GEdge if graph_GEdge is not None else set()
        self.graph_GEdge11 = graph_GEdge11
        self.graph_GEdge13 = graph_GEdge13
        
    @property
    def targetId(self) -> str:
        return self.__targetId

    @targetId.setter
    def targetId(self, targetId: str):
        self.__targetId = targetId

    @property
    def sourceId(self) -> str:
        return self.__sourceId

    @sourceId.setter
    def sourceId(self, sourceId: str):
        self.__sourceId = sourceId

    @property
    def graph_GEdge13(self):
        return self.__graph_GEdge13

    @graph_GEdge13.setter
    def graph_GEdge13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_GEdge__graph_GEdge13", None)
        self.__graph_GEdge13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_GModelElement14"):
                opp_val = getattr(old_value, "graph_GModelElement14", None)
                if opp_val == self:
                    setattr(old_value, "graph_GModelElement14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_GModelElement14"):
                opp_val = getattr(value, "graph_GModelElement14", None)
                setattr(value, "graph_GModelElement14", self)

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
                    

class graph_GPreRenderedElement(GModelElement):

    def __init__(self, code: str):
        self.code = code
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

class graph_GShapeElement(GBoundsAware, GModelElement):

    pass
class graph_GModelElement(ABC):

    def __init__(self, id: str, trace: str, type: str, cssClasses: str, 6: "graph_GModelElement" = None, 5: "graph_GModelElement" = None, 2: "graph_GModelElement" = None, : set["graph_GModelElement"] = None, graph_GModelElement: "graph_GEdge" = None, graph_GModelElement14: "graph_GEdge" = None):
        self.id = id
        self.trace = trace
        self.type = type
        self.cssClasses = cssClasses
        self.6 = 6
        self.5 = 5
        self.2 = 2
        self. =  if  is not None else set()
        self.graph_GModelElement = graph_GModelElement
        self.graph_GModelElement14 = graph_GModelElement14
        
    @property
    def cssClasses(self) -> str:
        return self.__cssClasses

    @cssClasses.setter
    def cssClasses(self, cssClasses: str):
        self.__cssClasses = cssClasses

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def trace(self) -> str:
        return self.__trace

    @trace.setter
    def trace(self, trace: str):
        self.__trace = trace

    @property
    def 6(self):
        return self.__6

    @6.setter
    def 6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_GModelElement__6", None)
        self.__6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "5"):
                opp_val = getattr(old_value, "5", None)
                if opp_val == self:
                    setattr(old_value, "5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "5"):
                opp_val = getattr(value, "5", None)
                setattr(value, "5", self)

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
            if hasattr(old_value, "graph_GEdge11"):
                opp_val = getattr(old_value, "graph_GEdge11", None)
                if opp_val == self:
                    setattr(old_value, "graph_GEdge11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_GEdge11"):
                opp_val = getattr(value, "graph_GEdge11", None)
                setattr(value, "graph_GEdge11", self)

    @property
    def 5(self):
        return self.__5

    @5.setter
    def 5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_GModelElement__5", None)
        self.__5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "6"):
                opp_val = getattr(old_value, "6", None)
                if opp_val == self:
                    setattr(old_value, "6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "6"):
                opp_val = getattr(value, "6", None)
                setattr(value, "6", self)

    @property
    def (self):
        return self.__

    @.setter
    def (self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_GModelElement__", None)
        self.__ = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "2"):
                    opp_val = getattr(item, "2", None)
                    
                    if opp_val == self:
                        setattr(item, "2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "2"):
                    opp_val = getattr(item, "2", None)
                    
                    setattr(item, "2", self)
                    

    @property
    def graph_GModelElement14(self):
        return self.__graph_GModelElement14

    @graph_GModelElement14.setter
    def graph_GModelElement14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_GModelElement__graph_GModelElement14", None)
        self.__graph_GModelElement14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph_GEdge13"):
                opp_val = getattr(old_value, "graph_GEdge13", None)
                if opp_val == self:
                    setattr(old_value, "graph_GEdge13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph_GEdge13"):
                opp_val = getattr(value, "graph_GEdge13", None)
                setattr(value, "graph_GEdge13", self)

    @property
    def 2(self):
        return self.__2

    @2.setter
    def 2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_graph_GModelElement__2", None)
        self.__2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, ""):
                opp_val = getattr(old_value, "", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, ""):
                opp_val = getattr(value, "", None)
                if opp_val is None:
                    setattr(value, "", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
