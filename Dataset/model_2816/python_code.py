from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Alignment(Enum):
    LEFT = "LEFT"
    CENTER = "CENTER"
    RIGHT = "RIGHT"
    TOP = "TOP"
    MIDDLE = "MIDDLE"
    BOTTOM = "BOTTOM"
class Orientation(Enum):
    HORIZONTAL = "HORIZONTAL"
    VERTICAL = "VERTICAL"
class Direction(Enum):
    NORTH = "NORTH"
    SOUTH = "SOUTH"
    EAST = "EAST"
    WEST = "WEST"


############################################
# Definition of Classes
############################################

class ColoredLabeledBorder:

    pass
class draw2d_TitleBarBorder(ColoredLabeledBorder):

    pass
class draw2d_GroupBoxBorder(ColoredLabeledBorder):

    pass
class LabeledBorder:

    pass
class draw2d_ColoredLabeledBorder(LabeledBorder):

    pass
class draw2d_FrameBorder(LabeledBorder):

    pass
class Border:

    pass
class draw2d_FlowBorder(Border):

    def __init__(self, rightMargin: int, topMargin: int, bottomMargin: int, leftMargin: int):
        self.rightMargin = rightMargin
        self.topMargin = topMargin
        self.bottomMargin = bottomMargin
        self.leftMargin = leftMargin
        
    @property
    def leftMargin(self) -> int:
        return self.__leftMargin

    @leftMargin.setter
    def leftMargin(self, leftMargin: int):
        self.__leftMargin = leftMargin

    @property
    def rightMargin(self) -> int:
        return self.__rightMargin

    @rightMargin.setter
    def rightMargin(self, rightMargin: int):
        self.__rightMargin = rightMargin

    @property
    def topMargin(self) -> int:
        return self.__topMargin

    @topMargin.setter
    def topMargin(self, topMargin: int):
        self.__topMargin = topMargin

    @property
    def bottomMargin(self) -> int:
        return self.__bottomMargin

    @bottomMargin.setter
    def bottomMargin(self, bottomMargin: int):
        self.__bottomMargin = bottomMargin

class draw2d_LabeledBorder(Border):

    def __init__(self, label: str, draw2d_LabeledBorder: "draw2d_Font" = None):
        self.label = label
        self.draw2d_LabeledBorder = draw2d_LabeledBorder
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def draw2d_LabeledBorder(self):
        return self.__draw2d_LabeledBorder

    @draw2d_LabeledBorder.setter
    def draw2d_LabeledBorder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_draw2d_LabeledBorder__draw2d_LabeledBorder", None)
        self.__draw2d_LabeledBorder = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "draw2d_Font21"):
                opp_val = getattr(old_value, "draw2d_Font21", None)
                if opp_val == self:
                    setattr(old_value, "draw2d_Font21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "draw2d_Font21"):
                opp_val = getattr(value, "draw2d_Font21", None)
                setattr(value, "draw2d_Font21", self)

class ConnectionAnchor:

    pass
class draw2d_XYAnchor(ConnectionAnchor):

    def __init__(self, location: str):
        self.location = location
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

class draw2d_ConnectionAnchor(ABC):

    pass
class Polyline:

    pass
class draw2d_Polygon(Polyline):

    pass
class PointListShape:

    pass
class draw2d_PolylineShape(PointListShape):

    def __init__(self, tolerance: int):
        self.tolerance = tolerance
        
    @property
    def tolerance(self) -> int:
        return self.__tolerance

    @tolerance.setter
    def tolerance(self, tolerance: int):
        self.__tolerance = tolerance

class draw2d_PolygonShape(PointListShape):

    pass
class draw2d_Polyline(PointListShape):

    def __init__(self, tolerance: int):
        self.tolerance = tolerance
        
    @property
    def tolerance(self) -> int:
        return self.__tolerance

    @tolerance.setter
    def tolerance(self, tolerance: int):
        self.__tolerance = tolerance

class Shape:

    pass
class draw2d_Triangle(Shape):

    def __init__(self, orientation: str, direction: str):
        self.orientation = orientation
        self.direction = direction
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def orientation(self) -> str:
        return self.__orientation

    @orientation.setter
    def orientation(self, orientation: str):
        self.__orientation = orientation

class draw2d_PointListShape(Shape):

    def __init__(self, pointList: int):
        self.pointList = pointList
        
    @property
    def pointList(self) -> int:
        return self.__pointList

    @pointList.setter
    def pointList(self, pointList: int):
        self.__pointList = pointList

class draw2d_Ellipse(Shape):

    pass
class draw2d_RoundedRectangle(Shape):

    def __init__(self, cornerDimensions: str):
        self.cornerDimensions = cornerDimensions
        
    @property
    def cornerDimensions(self) -> str:
        return self.__cornerDimensions

    @cornerDimensions.setter
    def cornerDimensions(self, cornerDimensions: str):
        self.__cornerDimensions = cornerDimensions

class draw2d_RectangleFigure(Shape):

    pass
class draw2d_Color:

    pass
class Figure:

    pass
class draw2d_Shape(Figure):

    def __init__(self, fill: bool, fillXOR: bool, outline: bool, outlineXOR: bool, alpha: str, antialias: str, lineDash: float, lineDashOffset: float, lineMiterLimit: float, lineWidthFloat: float, lineStyle: str, lineCap: str, lineJoin: str):
        self.fill = fill
        self.fillXOR = fillXOR
        self.outline = outline
        self.outlineXOR = outlineXOR
        self.alpha = alpha
        self.antialias = antialias
        self.lineDash = lineDash
        self.lineDashOffset = lineDashOffset
        self.lineMiterLimit = lineMiterLimit
        self.lineWidthFloat = lineWidthFloat
        self.lineStyle = lineStyle
        self.lineCap = lineCap
        self.lineJoin = lineJoin
        
    @property
    def antialias(self) -> str:
        return self.__antialias

    @antialias.setter
    def antialias(self, antialias: str):
        self.__antialias = antialias

    @property
    def fill(self) -> bool:
        return self.__fill

    @fill.setter
    def fill(self, fill: bool):
        self.__fill = fill

    @property
    def lineStyle(self) -> str:
        return self.__lineStyle

    @lineStyle.setter
    def lineStyle(self, lineStyle: str):
        self.__lineStyle = lineStyle

    @property
    def lineDash(self) -> float:
        return self.__lineDash

    @lineDash.setter
    def lineDash(self, lineDash: float):
        self.__lineDash = lineDash

    @property
    def lineMiterLimit(self) -> float:
        return self.__lineMiterLimit

    @lineMiterLimit.setter
    def lineMiterLimit(self, lineMiterLimit: float):
        self.__lineMiterLimit = lineMiterLimit

    @property
    def lineJoin(self) -> str:
        return self.__lineJoin

    @lineJoin.setter
    def lineJoin(self, lineJoin: str):
        self.__lineJoin = lineJoin

    @property
    def lineWidthFloat(self) -> float:
        return self.__lineWidthFloat

    @lineWidthFloat.setter
    def lineWidthFloat(self, lineWidthFloat: float):
        self.__lineWidthFloat = lineWidthFloat

    @property
    def lineCap(self) -> str:
        return self.__lineCap

    @lineCap.setter
    def lineCap(self, lineCap: str):
        self.__lineCap = lineCap

    @property
    def alpha(self) -> str:
        return self.__alpha

    @alpha.setter
    def alpha(self, alpha: str):
        self.__alpha = alpha

    @property
    def outlineXOR(self) -> bool:
        return self.__outlineXOR

    @outlineXOR.setter
    def outlineXOR(self, outlineXOR: bool):
        self.__outlineXOR = outlineXOR

    @property
    def outline(self) -> bool:
        return self.__outline

    @outline.setter
    def outline(self, outline: bool):
        self.__outline = outline

    @property
    def lineDashOffset(self) -> float:
        return self.__lineDashOffset

    @lineDashOffset.setter
    def lineDashOffset(self, lineDashOffset: float):
        self.__lineDashOffset = lineDashOffset

    @property
    def fillXOR(self) -> bool:
        return self.__fillXOR

    @fillXOR.setter
    def fillXOR(self, fillXOR: bool):
        self.__fillXOR = fillXOR

class draw2d_BlockFlow(Figure):

    def __init__(self, orientation: str):
        self.orientation = orientation
        
    @property
    def orientation(self) -> str:
        return self.__orientation

    @orientation.setter
    def orientation(self, orientation: str):
        self.__orientation = orientation

class draw2d_ImageFigure(Figure):

    def __init__(self, image: str):
        self.image = image
        
    @property
    def image(self) -> str:
        return self.__image

    @image.setter
    def image(self, image: str):
        self.__image = image

class draw2d_Label(Figure):

    def __init__(self, text: str, textAlignment: str, textPlacement: str, icon: str, iconAlignment: str, iconTextGap: int):
        self.text = text
        self.textAlignment = textAlignment
        self.textPlacement = textPlacement
        self.icon = icon
        self.iconAlignment = iconAlignment
        self.iconTextGap = iconTextGap
        
    @property
    def iconTextGap(self) -> int:
        return self.__iconTextGap

    @iconTextGap.setter
    def iconTextGap(self, iconTextGap: int):
        self.__iconTextGap = iconTextGap

    @property
    def iconAlignment(self) -> str:
        return self.__iconAlignment

    @iconAlignment.setter
    def iconAlignment(self, iconAlignment: str):
        self.__iconAlignment = iconAlignment

    @property
    def icon(self) -> str:
        return self.__icon

    @icon.setter
    def icon(self, icon: str):
        self.__icon = icon

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def textAlignment(self) -> str:
        return self.__textAlignment

    @textAlignment.setter
    def textAlignment(self, textAlignment: str):
        self.__textAlignment = textAlignment

    @property
    def textPlacement(self) -> str:
        return self.__textPlacement

    @textPlacement.setter
    def textPlacement(self, textPlacement: str):
        self.__textPlacement = textPlacement

class draw2d_Border(ABC):

    def __init__(self, opaque: bool, draw2d_Border: "draw2d_Figure" = None):
        self.opaque = opaque
        self.draw2d_Border = draw2d_Border
        
    @property
    def opaque(self) -> bool:
        return self.__opaque

    @opaque.setter
    def opaque(self, opaque: bool):
        self.__opaque = opaque

    @property
    def draw2d_Border(self):
        return self.__draw2d_Border

    @draw2d_Border.setter
    def draw2d_Border(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_draw2d_Border__draw2d_Border", None)
        self.__draw2d_Border = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "draw2d_Figure17"):
                opp_val = getattr(old_value, "draw2d_Figure17", None)
                if opp_val == self:
                    setattr(old_value, "draw2d_Figure17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "draw2d_Figure17"):
                opp_val = getattr(value, "draw2d_Figure17", None)
                setattr(value, "draw2d_Figure17", self)

class draw2d_Font:

    pass
class draw2d_Figure:

    def __init__(self, enabled: bool, visible: bool, opaque: bool, focusTraversable: bool, bounds: str, minimumSize: str, preferredSize: str, maximumSize: str, draw2d_Figure: "draw2d_Draw2DCanvas" = None, Figure: "draw2d_Figure" = None, parent: set["draw2d_Figure"] = None, Figure5: "draw2d_Figure" = None, children: "draw2d_Figure" = None, draw2d_Figure8: "draw2d_Figure" = None, draw2d_Figure6: "draw2d_Figure" = None, draw2d_Figure12: "draw2d_Color" = None, draw2d_Figure15: "draw2d_Font" = None, draw2d_Figure17: "draw2d_Border" = None, draw2d_Figure10: "draw2d_Color" = None, draw2d_Figure19: "draw2d_ConnectionAnchor" = None):
        self.enabled = enabled
        self.visible = visible
        self.opaque = opaque
        self.focusTraversable = focusTraversable
        self.bounds = bounds
        self.minimumSize = minimumSize
        self.preferredSize = preferredSize
        self.maximumSize = maximumSize
        self.draw2d_Figure = draw2d_Figure
        self.Figure = Figure
        self.parent = parent if parent is not None else set()
        self.Figure5 = Figure5
        self.children = children
        self.draw2d_Figure8 = draw2d_Figure8
        self.draw2d_Figure6 = draw2d_Figure6
        self.draw2d_Figure12 = draw2d_Figure12
        self.draw2d_Figure15 = draw2d_Figure15
        self.draw2d_Figure17 = draw2d_Figure17
        self.draw2d_Figure10 = draw2d_Figure10
        self.draw2d_Figure19 = draw2d_Figure19
        
    @property
    def opaque(self) -> bool:
        return self.__opaque

    @opaque.setter
    def opaque(self, opaque: bool):
        self.__opaque = opaque

    @property
    def maximumSize(self) -> str:
        return self.__maximumSize

    @maximumSize.setter
    def maximumSize(self, maximumSize: str):
        self.__maximumSize = maximumSize

    @property
    def minimumSize(self) -> str:
        return self.__minimumSize

    @minimumSize.setter
    def minimumSize(self, minimumSize: str):
        self.__minimumSize = minimumSize

    @property
    def bounds(self) -> str:
        return self.__bounds

    @bounds.setter
    def bounds(self, bounds: str):
        self.__bounds = bounds

    @property
    def focusTraversable(self) -> bool:
        return self.__focusTraversable

    @focusTraversable.setter
    def focusTraversable(self, focusTraversable: bool):
        self.__focusTraversable = focusTraversable

    @property
    def preferredSize(self) -> str:
        return self.__preferredSize

    @preferredSize.setter
    def preferredSize(self, preferredSize: str):
        self.__preferredSize = preferredSize

    @property
    def visible(self) -> bool:
        return self.__visible

    @visible.setter
    def visible(self, visible: bool):
        self.__visible = visible

    @property
    def enabled(self) -> bool:
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled: bool):
        self.__enabled = enabled

    @property
    def draw2d_Figure8(self):
        return self.__draw2d_Figure8

    @draw2d_Figure8.setter
    def draw2d_Figure8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_draw2d_Figure__draw2d_Figure8", None)
        self.__draw2d_Figure8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "draw2d_Figure6"):
                opp_val = getattr(old_value, "draw2d_Figure6", None)
                if opp_val == self:
                    setattr(old_value, "draw2d_Figure6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "draw2d_Figure6"):
                opp_val = getattr(value, "draw2d_Figure6", None)
                setattr(value, "draw2d_Figure6", self)

    @property
    def Figure5(self):
        return self.__Figure5

    @Figure5.setter
    def Figure5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_draw2d_Figure__Figure5", None)
        self.__Figure5 = value
        
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
    def Figure(self):
        return self.__Figure

    @Figure.setter
    def Figure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_draw2d_Figure__Figure", None)
        self.__Figure = value
        
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
    def draw2d_Figure17(self):
        return self.__draw2d_Figure17

    @draw2d_Figure17.setter
    def draw2d_Figure17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_draw2d_Figure__draw2d_Figure17", None)
        self.__draw2d_Figure17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "draw2d_Border"):
                opp_val = getattr(old_value, "draw2d_Border", None)
                if opp_val == self:
                    setattr(old_value, "draw2d_Border", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "draw2d_Border"):
                opp_val = getattr(value, "draw2d_Border", None)
                setattr(value, "draw2d_Border", self)

    @property
    def draw2d_Figure6(self):
        return self.__draw2d_Figure6

    @draw2d_Figure6.setter
    def draw2d_Figure6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_draw2d_Figure__draw2d_Figure6", None)
        self.__draw2d_Figure6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "draw2d_Figure8"):
                opp_val = getattr(old_value, "draw2d_Figure8", None)
                if opp_val == self:
                    setattr(old_value, "draw2d_Figure8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "draw2d_Figure8"):
                opp_val = getattr(value, "draw2d_Figure8", None)
                setattr(value, "draw2d_Figure8", self)

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_draw2d_Figure__children", None)
        self.__children = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Figure5"):
                opp_val = getattr(old_value, "Figure5", None)
                if opp_val == self:
                    setattr(old_value, "Figure5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Figure5"):
                opp_val = getattr(value, "Figure5", None)
                setattr(value, "Figure5", self)

    @property
    def draw2d_Figure19(self):
        return self.__draw2d_Figure19

    @draw2d_Figure19.setter
    def draw2d_Figure19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_draw2d_Figure__draw2d_Figure19", None)
        self.__draw2d_Figure19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "draw2d_ConnectionAnchor"):
                opp_val = getattr(old_value, "draw2d_ConnectionAnchor", None)
                if opp_val == self:
                    setattr(old_value, "draw2d_ConnectionAnchor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "draw2d_ConnectionAnchor"):
                opp_val = getattr(value, "draw2d_ConnectionAnchor", None)
                setattr(value, "draw2d_ConnectionAnchor", self)

    @property
    def draw2d_Figure15(self):
        return self.__draw2d_Figure15

    @draw2d_Figure15.setter
    def draw2d_Figure15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_draw2d_Figure__draw2d_Figure15", None)
        self.__draw2d_Figure15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "draw2d_Font"):
                opp_val = getattr(old_value, "draw2d_Font", None)
                if opp_val == self:
                    setattr(old_value, "draw2d_Font", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "draw2d_Font"):
                opp_val = getattr(value, "draw2d_Font", None)
                setattr(value, "draw2d_Font", self)

    @property
    def draw2d_Figure10(self):
        return self.__draw2d_Figure10

    @draw2d_Figure10.setter
    def draw2d_Figure10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_draw2d_Figure__draw2d_Figure10", None)
        self.__draw2d_Figure10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "draw2d_Color"):
                opp_val = getattr(old_value, "draw2d_Color", None)
                if opp_val == self:
                    setattr(old_value, "draw2d_Color", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "draw2d_Color"):
                opp_val = getattr(value, "draw2d_Color", None)
                setattr(value, "draw2d_Color", self)

    @property
    def draw2d_Figure12(self):
        return self.__draw2d_Figure12

    @draw2d_Figure12.setter
    def draw2d_Figure12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_draw2d_Figure__draw2d_Figure12", None)
        self.__draw2d_Figure12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "draw2d_Color13"):
                opp_val = getattr(old_value, "draw2d_Color13", None)
                if opp_val == self:
                    setattr(old_value, "draw2d_Color13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "draw2d_Color13"):
                opp_val = getattr(value, "draw2d_Color13", None)
                setattr(value, "draw2d_Color13", self)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_draw2d_Figure__parent", None)
        self.__parent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Figure"):
                    opp_val = getattr(item, "Figure", None)
                    
                    if opp_val == self:
                        setattr(item, "Figure", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Figure"):
                    opp_val = getattr(item, "Figure", None)
                    
                    setattr(item, "Figure", self)
                    

    @property
    def draw2d_Figure(self):
        return self.__draw2d_Figure

    @draw2d_Figure.setter
    def draw2d_Figure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_draw2d_Figure__draw2d_Figure", None)
        self.__draw2d_Figure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "draw2d_Draw2DCanvas"):
                opp_val = getattr(old_value, "draw2d_Draw2DCanvas", None)
                if opp_val == self:
                    setattr(old_value, "draw2d_Draw2DCanvas", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "draw2d_Draw2DCanvas"):
                opp_val = getattr(value, "draw2d_Draw2DCanvas", None)
                setattr(value, "draw2d_Draw2DCanvas", self)

class Canvas:

    pass
class draw2d_Draw2DCanvas(Canvas):

    pass