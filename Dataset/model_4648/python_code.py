from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class LineStyle(Enum):
    SOLID = "SOLID"
    DASH = "DASH"
    DOT = "DOT"
    DASHDOT = "DASHDOT"
    DASHDOTDOT = "DASHDOTDOT"
    LINE_CUSTOM = "LINE_CUSTOM"
class RulerUnit(Enum):
    INCHES = "INCHES"
    CENTIMETERS = "CENTIMETERS"
    PIXELS = "PIXELS"
class Alignment(Enum):
    LEFT = "LEFT"
    CENTER = "CENTER"
    RIGHT = "RIGHT"
    TOP = "TOP"
    BOTTOM = "BOTTOM"


############################################
# Definition of Classes
############################################

class di_ElementEntry:

    def __init__(self, value: str, di_ElementEntry: "di_Guide" = None, di_ElementEntry34: "di_View" = None):
        self.value = value
        self.di_ElementEntry = di_ElementEntry
        self.di_ElementEntry34 = di_ElementEntry34
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def di_ElementEntry34(self):
        return self.__di_ElementEntry34

    @di_ElementEntry34.setter
    def di_ElementEntry34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_ElementEntry__di_ElementEntry34", None)
        self.__di_ElementEntry34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_View35"):
                opp_val = getattr(old_value, "di_View35", None)
                if opp_val == self:
                    setattr(old_value, "di_View35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_View35"):
                opp_val = getattr(value, "di_View35", None)
                setattr(value, "di_View35", self)

    @property
    def di_ElementEntry(self):
        return self.__di_ElementEntry

    @di_ElementEntry.setter
    def di_ElementEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_ElementEntry__di_ElementEntry", None)
        self.__di_ElementEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_Guide"):
                opp_val = getattr(old_value, "di_Guide", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_Guide"):
                opp_val = getattr(value, "di_Guide", None)
                if opp_val is None:
                    setattr(value, "di_Guide", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class di_Guide:

    def __init__(self, position: int, Guide: "di_Ruler" = None, guides: "di_Ruler" = None, di_Guide: set["di_ElementEntry"] = None):
        self.position = position
        self.Guide = Guide
        self.guides = guides
        self.di_Guide = di_Guide if di_Guide is not None else set()
        
    @property
    def position(self) -> int:
        return self.__position

    @position.setter
    def position(self, position: int):
        self.__position = position

    @property
    def guides(self):
        return self.__guides

    @guides.setter
    def guides(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Guide__guides", None)
        self.__guides = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Ruler"):
                opp_val = getattr(old_value, "Ruler", None)
                if opp_val == self:
                    setattr(old_value, "Ruler", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Ruler"):
                opp_val = getattr(value, "Ruler", None)
                setattr(value, "Ruler", self)

    @property
    def Guide(self):
        return self.__Guide

    @Guide.setter
    def Guide(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Guide__Guide", None)
        self.__Guide = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ruler"):
                opp_val = getattr(old_value, "ruler", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ruler"):
                opp_val = getattr(value, "ruler", None)
                if opp_val is None:
                    setattr(value, "ruler", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def di_Guide(self):
        return self.__di_Guide

    @di_Guide.setter
    def di_Guide(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Guide__di_Guide", None)
        self.__di_Guide = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "di_ElementEntry"):
                    opp_val = getattr(item, "di_ElementEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "di_ElementEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "di_ElementEntry"):
                    opp_val = getattr(item, "di_ElementEntry", None)
                    
                    setattr(item, "di_ElementEntry", self)
                    

class Shape:

    pass
class di_GradientShape(Shape):

    def __init__(self, usingGradient: bool, gradientColor: int, verticalGradient: bool):
        self.usingGradient = usingGradient
        self.gradientColor = gradientColor
        self.verticalGradient = verticalGradient
        
    @property
    def gradientColor(self) -> int:
        return self.__gradientColor

    @gradientColor.setter
    def gradientColor(self, gradientColor: int):
        self.__gradientColor = gradientColor

    @property
    def usingGradient(self) -> bool:
        return self.__usingGradient

    @usingGradient.setter
    def usingGradient(self, usingGradient: bool):
        self.__usingGradient = usingGradient

    @property
    def verticalGradient(self) -> bool:
        return self.__verticalGradient

    @verticalGradient.setter
    def verticalGradient(self, verticalGradient: bool):
        self.__verticalGradient = verticalGradient

class Line:

    pass
class Node:

    pass
class di_Grid:

    def __init__(self, color: int, spacing: int, style: str, di_Grid: "di_Diagram" = None):
        self.color = color
        self.spacing = spacing
        self.style = style
        self.di_Grid = di_Grid
        
    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def spacing(self) -> int:
        return self.__spacing

    @spacing.setter
    def spacing(self, spacing: int):
        self.__spacing = spacing

    @property
    def color(self) -> int:
        return self.__color

    @color.setter
    def color(self, color: int):
        self.__color = color

    @property
    def di_Grid(self):
        return self.__di_Grid

    @di_Grid.setter
    def di_Grid(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Grid__di_Grid", None)
        self.__di_Grid = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_Diagram18"):
                opp_val = getattr(old_value, "di_Diagram18", None)
                if opp_val == self:
                    setattr(old_value, "di_Diagram18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_Diagram18"):
                opp_val = getattr(value, "di_Diagram18", None)
                setattr(value, "di_Diagram18", self)

class di_Ruler:

    def __init__(self, unit: str, di_Ruler: "di_Diagram" = None, di_Ruler16: "di_Diagram" = None, ruler: set["di_Guide"] = None, Ruler: "di_Guide" = None):
        self.unit = unit
        self.di_Ruler = di_Ruler
        self.di_Ruler16 = di_Ruler16
        self.ruler = ruler if ruler is not None else set()
        self.Ruler = Ruler
        
    @property
    def unit(self) -> str:
        return self.__unit

    @unit.setter
    def unit(self, unit: str):
        self.__unit = unit

    @property
    def ruler(self):
        return self.__ruler

    @ruler.setter
    def ruler(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Ruler__ruler", None)
        self.__ruler = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Guide"):
                    opp_val = getattr(item, "Guide", None)
                    
                    if opp_val == self:
                        setattr(item, "Guide", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Guide"):
                    opp_val = getattr(item, "Guide", None)
                    
                    setattr(item, "Guide", self)
                    

    @property
    def Ruler(self):
        return self.__Ruler

    @Ruler.setter
    def Ruler(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Ruler__Ruler", None)
        self.__Ruler = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "guides"):
                opp_val = getattr(old_value, "guides", None)
                if opp_val == self:
                    setattr(old_value, "guides", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "guides"):
                opp_val = getattr(value, "guides", None)
                setattr(value, "guides", self)

    @property
    def di_Ruler16(self):
        return self.__di_Ruler16

    @di_Ruler16.setter
    def di_Ruler16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Ruler__di_Ruler16", None)
        self.__di_Ruler16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_Diagram15"):
                opp_val = getattr(old_value, "di_Diagram15", None)
                if opp_val == self:
                    setattr(old_value, "di_Diagram15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_Diagram15"):
                opp_val = getattr(value, "di_Diagram15", None)
                setattr(value, "di_Diagram15", self)

    @property
    def di_Ruler(self):
        return self.__di_Ruler

    @di_Ruler.setter
    def di_Ruler(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Ruler__di_Ruler", None)
        self.__di_Ruler = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_Diagram13"):
                opp_val = getattr(old_value, "di_Diagram13", None)
                if opp_val == self:
                    setattr(old_value, "di_Diagram13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_Diagram13"):
                opp_val = getattr(value, "di_Diagram13", None)
                setattr(value, "di_Diagram13", self)

class di_Comment(Shape):

    pass
class Container:

    pass
class di_Diagram(Container):

    def __init__(self, rulers: str, snapToGrid: bool, snapToGeometry: bool, di_Diagram: set["di_Comment"] = None, di_Diagram11: set["di_CommentLink"] = None, di_Diagram13: "di_Ruler" = None, di_Diagram15: "di_Ruler" = None, di_Diagram18: "di_Grid" = None):
        self.rulers = rulers
        self.snapToGrid = snapToGrid
        self.snapToGeometry = snapToGeometry
        self.di_Diagram = di_Diagram if di_Diagram is not None else set()
        self.di_Diagram11 = di_Diagram11 if di_Diagram11 is not None else set()
        self.di_Diagram13 = di_Diagram13
        self.di_Diagram15 = di_Diagram15
        self.di_Diagram18 = di_Diagram18
        
    @property
    def snapToGeometry(self) -> bool:
        return self.__snapToGeometry

    @snapToGeometry.setter
    def snapToGeometry(self, snapToGeometry: bool):
        self.__snapToGeometry = snapToGeometry

    @property
    def snapToGrid(self) -> bool:
        return self.__snapToGrid

    @snapToGrid.setter
    def snapToGrid(self, snapToGrid: bool):
        self.__snapToGrid = snapToGrid

    @property
    def rulers(self) -> str:
        return self.__rulers

    @rulers.setter
    def rulers(self, rulers: str):
        self.__rulers = rulers

    @property
    def di_Diagram15(self):
        return self.__di_Diagram15

    @di_Diagram15.setter
    def di_Diagram15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Diagram__di_Diagram15", None)
        self.__di_Diagram15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_Ruler16"):
                opp_val = getattr(old_value, "di_Ruler16", None)
                if opp_val == self:
                    setattr(old_value, "di_Ruler16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_Ruler16"):
                opp_val = getattr(value, "di_Ruler16", None)
                setattr(value, "di_Ruler16", self)

    @property
    def di_Diagram18(self):
        return self.__di_Diagram18

    @di_Diagram18.setter
    def di_Diagram18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Diagram__di_Diagram18", None)
        self.__di_Diagram18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_Grid"):
                opp_val = getattr(old_value, "di_Grid", None)
                if opp_val == self:
                    setattr(old_value, "di_Grid", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_Grid"):
                opp_val = getattr(value, "di_Grid", None)
                setattr(value, "di_Grid", self)

    @property
    def di_Diagram(self):
        return self.__di_Diagram

    @di_Diagram.setter
    def di_Diagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Diagram__di_Diagram", None)
        self.__di_Diagram = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "di_Comment"):
                    opp_val = getattr(item, "di_Comment", None)
                    
                    if opp_val == self:
                        setattr(item, "di_Comment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "di_Comment"):
                    opp_val = getattr(item, "di_Comment", None)
                    
                    setattr(item, "di_Comment", self)
                    

    @property
    def di_Diagram13(self):
        return self.__di_Diagram13

    @di_Diagram13.setter
    def di_Diagram13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Diagram__di_Diagram13", None)
        self.__di_Diagram13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_Ruler"):
                opp_val = getattr(old_value, "di_Ruler", None)
                if opp_val == self:
                    setattr(old_value, "di_Ruler", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_Ruler"):
                opp_val = getattr(value, "di_Ruler", None)
                setattr(value, "di_Ruler", self)

    @property
    def di_Diagram11(self):
        return self.__di_Diagram11

    @di_Diagram11.setter
    def di_Diagram11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Diagram__di_Diagram11", None)
        self.__di_Diagram11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "di_CommentLink"):
                    opp_val = getattr(item, "di_CommentLink", None)
                    
                    if opp_val == self:
                        setattr(item, "di_CommentLink", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "di_CommentLink"):
                    opp_val = getattr(item, "di_CommentLink", None)
                    
                    setattr(item, "di_CommentLink", self)
                    

class di_Line(Node):

    def __init__(self, color: int, width: int, sourceAnchor: str, targetAnchor: str, sourceNode: str, targetNode: str, style: str, lineDash: int, di_Line: "di_Container" = None):
        self.color = color
        self.width = width
        self.sourceAnchor = sourceAnchor
        self.targetAnchor = targetAnchor
        self.sourceNode = sourceNode
        self.targetNode = targetNode
        self.style = style
        self.lineDash = lineDash
        self.di_Line = di_Line
        
    @property
    def lineDash(self) -> int:
        return self.__lineDash

    @lineDash.setter
    def lineDash(self, lineDash: int):
        self.__lineDash = lineDash

    @property
    def sourceAnchor(self) -> str:
        return self.__sourceAnchor

    @sourceAnchor.setter
    def sourceAnchor(self, sourceAnchor: str):
        self.__sourceAnchor = sourceAnchor

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def targetNode(self) -> str:
        return self.__targetNode

    @targetNode.setter
    def targetNode(self, targetNode: str):
        self.__targetNode = targetNode

    @property
    def color(self) -> int:
        return self.__color

    @color.setter
    def color(self, color: int):
        self.__color = color

    @property
    def sourceNode(self) -> str:
        return self.__sourceNode

    @sourceNode.setter
    def sourceNode(self, sourceNode: str):
        self.__sourceNode = sourceNode

    @property
    def targetAnchor(self) -> str:
        return self.__targetAnchor

    @targetAnchor.setter
    def targetAnchor(self, targetAnchor: str):
        self.__targetAnchor = targetAnchor

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width

    @property
    def di_Line(self):
        return self.__di_Line

    @di_Line.setter
    def di_Line(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Line__di_Line", None)
        self.__di_Line = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_Container8"):
                opp_val = getattr(old_value, "di_Container8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_Container8"):
                opp_val = getattr(value, "di_Container8", None)
                if opp_val is None:
                    setattr(value, "di_Container8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class di_Shape(Node, Container):

    def __init__(self, background: int, foreground: int, bounds: str, di_Shape: "di_Container" = None):
        self.background = background
        self.foreground = foreground
        self.bounds = bounds
        self.di_Shape = di_Shape
        
    @property
    def foreground(self) -> int:
        return self.__foreground

    @foreground.setter
    def foreground(self, foreground: int):
        self.__foreground = foreground

    @property
    def background(self) -> int:
        return self.__background

    @background.setter
    def background(self, background: int):
        self.__background = background

    @property
    def bounds(self) -> str:
        return self.__bounds

    @bounds.setter
    def bounds(self, bounds: str):
        self.__bounds = bounds

    @property
    def di_Shape(self):
        return self.__di_Shape

    @di_Shape.setter
    def di_Shape(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Shape__di_Shape", None)
        self.__di_Shape = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_Container"):
                opp_val = getattr(old_value, "di_Container", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_Container"):
                opp_val = getattr(value, "di_Container", None)
                if opp_val is None:
                    setattr(value, "di_Container", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class di_Connector(Line):

    pass
class di_CommentLink(Line):

    pass
class View:

    pass
class di_Container(View):

    def __init__(self, allLines: str, allShapes: str, di_Container: set["di_Shape"] = None, di_Container8: set["di_Line"] = None):
        self.allLines = allLines
        self.allShapes = allShapes
        self.di_Container = di_Container if di_Container is not None else set()
        self.di_Container8 = di_Container8 if di_Container8 is not None else set()
        
    @property
    def allLines(self) -> str:
        return self.__allLines

    @allLines.setter
    def allLines(self, allLines: str):
        self.__allLines = allLines

    @property
    def allShapes(self) -> str:
        return self.__allShapes

    @allShapes.setter
    def allShapes(self, allShapes: str):
        self.__allShapes = allShapes

    @property
    def di_Container8(self):
        return self.__di_Container8

    @di_Container8.setter
    def di_Container8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Container__di_Container8", None)
        self.__di_Container8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "di_Line"):
                    opp_val = getattr(item, "di_Line", None)
                    
                    if opp_val == self:
                        setattr(item, "di_Line", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "di_Line"):
                    opp_val = getattr(item, "di_Line", None)
                    
                    setattr(item, "di_Line", self)
                    

    @property
    def di_Container(self):
        return self.__di_Container

    @di_Container.setter
    def di_Container(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Container__di_Container", None)
        self.__di_Container = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "di_Shape"):
                    opp_val = getattr(item, "di_Shape", None)
                    
                    if opp_val == self:
                        setattr(item, "di_Shape", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "di_Shape"):
                    opp_val = getattr(item, "di_Shape", None)
                    
                    setattr(item, "di_Shape", self)
                    

class di_Node(View):

    def __init__(self, allOutgoingLines: str, allIncomingLines: str, source: set["di_CommentLink"] = None, source3: set["di_Connector"] = None, target: set["di_Connector"] = None, Node: "di_Connector" = None, Node21: "di_Connector" = None, Node28: "di_CommentLink" = None):
        self.allOutgoingLines = allOutgoingLines
        self.allIncomingLines = allIncomingLines
        self.source = source if source is not None else set()
        self.source3 = source3 if source3 is not None else set()
        self.target = target if target is not None else set()
        self.Node = Node
        self.Node21 = Node21
        self.Node28 = Node28
        
    @property
    def allOutgoingLines(self) -> str:
        return self.__allOutgoingLines

    @allOutgoingLines.setter
    def allOutgoingLines(self, allOutgoingLines: str):
        self.__allOutgoingLines = allOutgoingLines

    @property
    def allIncomingLines(self) -> str:
        return self.__allIncomingLines

    @allIncomingLines.setter
    def allIncomingLines(self, allIncomingLines: str):
        self.__allIncomingLines = allIncomingLines

    @property
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Node__Node", None)
        self.__Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incomingLines"):
                opp_val = getattr(old_value, "incomingLines", None)
                if opp_val == self:
                    setattr(old_value, "incomingLines", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incomingLines"):
                opp_val = getattr(value, "incomingLines", None)
                setattr(value, "incomingLines", self)

    @property
    def Node21(self):
        return self.__Node21

    @Node21.setter
    def Node21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Node__Node21", None)
        self.__Node21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoingLines"):
                opp_val = getattr(old_value, "outgoingLines", None)
                if opp_val == self:
                    setattr(old_value, "outgoingLines", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoingLines"):
                opp_val = getattr(value, "outgoingLines", None)
                setattr(value, "outgoingLines", self)

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Node__target", None)
        self.__target = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Connector5"):
                    opp_val = getattr(item, "Connector5", None)
                    
                    if opp_val == self:
                        setattr(item, "Connector5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Connector5"):
                    opp_val = getattr(item, "Connector5", None)
                    
                    setattr(item, "Connector5", self)
                    

    @property
    def Node28(self):
        return self.__Node28

    @Node28.setter
    def Node28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Node__Node28", None)
        self.__Node28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "commentLinks"):
                opp_val = getattr(old_value, "commentLinks", None)
                if opp_val == self:
                    setattr(old_value, "commentLinks", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "commentLinks"):
                opp_val = getattr(value, "commentLinks", None)
                setattr(value, "commentLinks", self)

    @property
    def source3(self):
        return self.__source3

    @source3.setter
    def source3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Node__source3", None)
        self.__source3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Connector"):
                    opp_val = getattr(item, "Connector", None)
                    
                    if opp_val == self:
                        setattr(item, "Connector", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Connector"):
                    opp_val = getattr(item, "Connector", None)
                    
                    setattr(item, "Connector", self)
                    

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_Node__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CommentLink"):
                    opp_val = getattr(item, "CommentLink", None)
                    
                    if opp_val == self:
                        setattr(item, "CommentLink", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CommentLink"):
                    opp_val = getattr(item, "CommentLink", None)
                    
                    setattr(item, "CommentLink", self)
                    

class di_EObject:

    pass
class di_View(ABC):

    def __init__(self, label: str, id: str, di_View: "di_EObject" = None, di_View35: "di_ElementEntry" = None):
        self.label = label
        self.id = id
        self.di_View = di_View
        self.di_View35 = di_View35
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def di_View(self):
        return self.__di_View

    @di_View.setter
    def di_View(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_View__di_View", None)
        self.__di_View = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_EObject"):
                opp_val = getattr(old_value, "di_EObject", None)
                if opp_val == self:
                    setattr(old_value, "di_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_EObject"):
                opp_val = getattr(value, "di_EObject", None)
                setattr(value, "di_EObject", self)

    @property
    def di_View35(self):
        return self.__di_View35

    @di_View35.setter
    def di_View35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_View__di_View35", None)
        self.__di_View35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_ElementEntry34"):
                opp_val = getattr(old_value, "di_ElementEntry34", None)
                if opp_val == self:
                    setattr(old_value, "di_ElementEntry34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_ElementEntry34"):
                opp_val = getattr(value, "di_ElementEntry34", None)
                setattr(value, "di_ElementEntry34", self)
