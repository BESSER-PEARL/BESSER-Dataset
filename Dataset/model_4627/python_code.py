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
    BOTTOM = "BOTTOM"
class GridAlignment(Enum):
    CENTER = "CENTER"
    FILL = "FILL"
    BEGINNING = "BEGINNING"
    END = "END"
class SystemCursorType(Enum):
    ARROW = "ARROW"
    HAND = "HAND"
class Orientation(Enum):
    NORTH = "NORTH"
    SOUTH = "SOUTH"
    EAST = "EAST"
    WEST = "WEST"


############################################
# Definition of Classes
############################################

class Container:

    pass
class VisualInterface_GridContainer(Container):

    def __init__(self, horizontalSpacing: int, verticalSpacing: int, marginWidth: int, marginHeight: int, columns: int, equalWidth: bool, VisualInterface_GridContainer: set["VisualInterface_GridChild"] = None):
        self.horizontalSpacing = horizontalSpacing
        self.verticalSpacing = verticalSpacing
        self.marginWidth = marginWidth
        self.marginHeight = marginHeight
        self.columns = columns
        self.equalWidth = equalWidth
        self.VisualInterface_GridContainer = VisualInterface_GridContainer if VisualInterface_GridContainer is not None else set()
        
    @property
    def equalWidth(self) -> bool:
        return self.__equalWidth

    @equalWidth.setter
    def equalWidth(self, equalWidth: bool):
        self.__equalWidth = equalWidth

    @property
    def columns(self) -> int:
        return self.__columns

    @columns.setter
    def columns(self, columns: int):
        self.__columns = columns

    @property
    def marginHeight(self) -> int:
        return self.__marginHeight

    @marginHeight.setter
    def marginHeight(self, marginHeight: int):
        self.__marginHeight = marginHeight

    @property
    def marginWidth(self) -> int:
        return self.__marginWidth

    @marginWidth.setter
    def marginWidth(self, marginWidth: int):
        self.__marginWidth = marginWidth

    @property
    def horizontalSpacing(self) -> int:
        return self.__horizontalSpacing

    @horizontalSpacing.setter
    def horizontalSpacing(self, horizontalSpacing: int):
        self.__horizontalSpacing = horizontalSpacing

    @property
    def verticalSpacing(self) -> int:
        return self.__verticalSpacing

    @verticalSpacing.setter
    def verticalSpacing(self, verticalSpacing: int):
        self.__verticalSpacing = verticalSpacing

    @property
    def VisualInterface_GridContainer(self):
        return self.__VisualInterface_GridContainer

    @VisualInterface_GridContainer.setter
    def VisualInterface_GridContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_VisualInterface_GridContainer__VisualInterface_GridContainer", None)
        self.__VisualInterface_GridContainer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VisualInterface_GridChild"):
                    opp_val = getattr(item, "VisualInterface_GridChild", None)
                    
                    if opp_val == self:
                        setattr(item, "VisualInterface_GridChild", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VisualInterface_GridChild"):
                    opp_val = getattr(item, "VisualInterface_GridChild", None)
                    
                    setattr(item, "VisualInterface_GridChild", self)
                    

class VisualInterface_StackContainer(Container):

    pass
class VisualInterface_BorderContainer(Container):

    def __init__(self, verticalSpacing: int, horizontalSpacing: int, VisualInterface_BorderContainer: set["VisualInterface_BorderChild"] = None):
        self.verticalSpacing = verticalSpacing
        self.horizontalSpacing = horizontalSpacing
        self.VisualInterface_BorderContainer = VisualInterface_BorderContainer if VisualInterface_BorderContainer is not None else set()
        
    @property
    def verticalSpacing(self) -> int:
        return self.__verticalSpacing

    @verticalSpacing.setter
    def verticalSpacing(self, verticalSpacing: int):
        self.__verticalSpacing = verticalSpacing

    @property
    def horizontalSpacing(self) -> int:
        return self.__horizontalSpacing

    @horizontalSpacing.setter
    def horizontalSpacing(self, horizontalSpacing: int):
        self.__horizontalSpacing = horizontalSpacing

    @property
    def VisualInterface_BorderContainer(self):
        return self.__VisualInterface_BorderContainer

    @VisualInterface_BorderContainer.setter
    def VisualInterface_BorderContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_VisualInterface_BorderContainer__VisualInterface_BorderContainer", None)
        self.__VisualInterface_BorderContainer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VisualInterface_BorderChild"):
                    opp_val = getattr(item, "VisualInterface_BorderChild", None)
                    
                    if opp_val == self:
                        setattr(item, "VisualInterface_BorderChild", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VisualInterface_BorderChild"):
                    opp_val = getattr(item, "VisualInterface_BorderChild", None)
                    
                    setattr(item, "VisualInterface_BorderChild", self)
                    

class VisualInterface_XYContainer(Container):

    pass
class Cursor:

    pass
class VisualInterface_SystemCursor(Cursor):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class VisualInterface_Connection:

    pass
class VisualInterface_Dimension:

    def __init__(self, width: float, height: float, VisualInterface_Dimension14: "VisualInterface_XYChild" = None, VisualInterface_Dimension: "VisualInterface_Symbol" = None, VisualInterface_Dimension20: "VisualInterface_Figure" = None):
        self.width = width
        self.height = height
        self.VisualInterface_Dimension14 = VisualInterface_Dimension14
        self.VisualInterface_Dimension = VisualInterface_Dimension
        self.VisualInterface_Dimension20 = VisualInterface_Dimension20
        
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
    def VisualInterface_Dimension20(self):
        return self.__VisualInterface_Dimension20

    @VisualInterface_Dimension20.setter
    def VisualInterface_Dimension20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_VisualInterface_Dimension__VisualInterface_Dimension20", None)
        self.__VisualInterface_Dimension20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VisualInterface_Figure"):
                opp_val = getattr(old_value, "VisualInterface_Figure", None)
                if opp_val == self:
                    setattr(old_value, "VisualInterface_Figure", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VisualInterface_Figure"):
                opp_val = getattr(value, "VisualInterface_Figure", None)
                setattr(value, "VisualInterface_Figure", self)

    @property
    def VisualInterface_Dimension14(self):
        return self.__VisualInterface_Dimension14

    @VisualInterface_Dimension14.setter
    def VisualInterface_Dimension14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_VisualInterface_Dimension__VisualInterface_Dimension14", None)
        self.__VisualInterface_Dimension14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VisualInterface_XYChild13"):
                opp_val = getattr(old_value, "VisualInterface_XYChild13", None)
                if opp_val == self:
                    setattr(old_value, "VisualInterface_XYChild13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VisualInterface_XYChild13"):
                opp_val = getattr(value, "VisualInterface_XYChild13", None)
                setattr(value, "VisualInterface_XYChild13", self)

    @property
    def VisualInterface_Dimension(self):
        return self.__VisualInterface_Dimension

    @VisualInterface_Dimension.setter
    def VisualInterface_Dimension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_VisualInterface_Dimension__VisualInterface_Dimension", None)
        self.__VisualInterface_Dimension = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VisualInterface_Symbol6"):
                opp_val = getattr(old_value, "VisualInterface_Symbol6", None)
                if opp_val == self:
                    setattr(old_value, "VisualInterface_Symbol6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VisualInterface_Symbol6"):
                opp_val = getattr(value, "VisualInterface_Symbol6", None)
                setattr(value, "VisualInterface_Symbol6", self)

class VisualInterface_Position:

    def __init__(self, x: float, y: float, VisualInterface_Position: "VisualInterface_XYChild" = None, VisualInterface_Position18: "VisualInterface_Line" = None):
        self.x = x
        self.y = y
        self.VisualInterface_Position = VisualInterface_Position
        self.VisualInterface_Position18 = VisualInterface_Position18
        
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
    def VisualInterface_Position(self):
        return self.__VisualInterface_Position

    @VisualInterface_Position.setter
    def VisualInterface_Position(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_VisualInterface_Position__VisualInterface_Position", None)
        self.__VisualInterface_Position = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VisualInterface_XYChild"):
                opp_val = getattr(old_value, "VisualInterface_XYChild", None)
                if opp_val == self:
                    setattr(old_value, "VisualInterface_XYChild", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VisualInterface_XYChild"):
                opp_val = getattr(value, "VisualInterface_XYChild", None)
                setattr(value, "VisualInterface_XYChild", self)

    @property
    def VisualInterface_Position18(self):
        return self.__VisualInterface_Position18

    @VisualInterface_Position18.setter
    def VisualInterface_Position18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_VisualInterface_Position__VisualInterface_Position18", None)
        self.__VisualInterface_Position18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VisualInterface_Line"):
                opp_val = getattr(old_value, "VisualInterface_Line", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VisualInterface_Line"):
                opp_val = getattr(value, "VisualInterface_Line", None)
                if opp_val is None:
                    setattr(value, "VisualInterface_Line", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Child:

    pass
class VisualInterface_BorderChild(Child):

    def __init__(self, alignment: str, VisualInterface_BorderChild: "VisualInterface_BorderContainer" = None):
        self.alignment = alignment
        self.VisualInterface_BorderChild = VisualInterface_BorderChild
        
    @property
    def alignment(self) -> str:
        return self.__alignment

    @alignment.setter
    def alignment(self, alignment: str):
        self.__alignment = alignment

    @property
    def VisualInterface_BorderChild(self):
        return self.__VisualInterface_BorderChild

    @VisualInterface_BorderChild.setter
    def VisualInterface_BorderChild(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_VisualInterface_BorderChild__VisualInterface_BorderChild", None)
        self.__VisualInterface_BorderChild = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VisualInterface_BorderContainer"):
                opp_val = getattr(old_value, "VisualInterface_BorderContainer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VisualInterface_BorderContainer"):
                opp_val = getattr(value, "VisualInterface_BorderContainer", None)
                if opp_val is None:
                    setattr(value, "VisualInterface_BorderContainer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class VisualInterface_GridChild(Child):

    def __init__(self, horizontalAlignment: str, verticalAlignment: str, grabHorizontalSpace: bool, grabVerticalSpace: bool, spanCols: int, spanRows: str, widthHint: str, heightHint: str, VisualInterface_GridChild: "VisualInterface_GridContainer" = None):
        self.horizontalAlignment = horizontalAlignment
        self.verticalAlignment = verticalAlignment
        self.grabHorizontalSpace = grabHorizontalSpace
        self.grabVerticalSpace = grabVerticalSpace
        self.spanCols = spanCols
        self.spanRows = spanRows
        self.widthHint = widthHint
        self.heightHint = heightHint
        self.VisualInterface_GridChild = VisualInterface_GridChild
        
    @property
    def verticalAlignment(self) -> str:
        return self.__verticalAlignment

    @verticalAlignment.setter
    def verticalAlignment(self, verticalAlignment: str):
        self.__verticalAlignment = verticalAlignment

    @property
    def heightHint(self) -> str:
        return self.__heightHint

    @heightHint.setter
    def heightHint(self, heightHint: str):
        self.__heightHint = heightHint

    @property
    def horizontalAlignment(self) -> str:
        return self.__horizontalAlignment

    @horizontalAlignment.setter
    def horizontalAlignment(self, horizontalAlignment: str):
        self.__horizontalAlignment = horizontalAlignment

    @property
    def spanCols(self) -> int:
        return self.__spanCols

    @spanCols.setter
    def spanCols(self, spanCols: int):
        self.__spanCols = spanCols

    @property
    def spanRows(self) -> str:
        return self.__spanRows

    @spanRows.setter
    def spanRows(self, spanRows: str):
        self.__spanRows = spanRows

    @property
    def widthHint(self) -> str:
        return self.__widthHint

    @widthHint.setter
    def widthHint(self, widthHint: str):
        self.__widthHint = widthHint

    @property
    def grabVerticalSpace(self) -> bool:
        return self.__grabVerticalSpace

    @grabVerticalSpace.setter
    def grabVerticalSpace(self, grabVerticalSpace: bool):
        self.__grabVerticalSpace = grabVerticalSpace

    @property
    def grabHorizontalSpace(self) -> bool:
        return self.__grabHorizontalSpace

    @grabHorizontalSpace.setter
    def grabHorizontalSpace(self, grabHorizontalSpace: bool):
        self.__grabHorizontalSpace = grabHorizontalSpace

    @property
    def VisualInterface_GridChild(self):
        return self.__VisualInterface_GridChild

    @VisualInterface_GridChild.setter
    def VisualInterface_GridChild(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_VisualInterface_GridChild__VisualInterface_GridChild", None)
        self.__VisualInterface_GridChild = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VisualInterface_GridContainer"):
                opp_val = getattr(old_value, "VisualInterface_GridContainer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VisualInterface_GridContainer"):
                opp_val = getattr(value, "VisualInterface_GridContainer", None)
                if opp_val is None:
                    setattr(value, "VisualInterface_GridContainer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class VisualInterface_XYChild(Child):

    pass
class VisualInterface_Child:

    def __init__(self, name: str, VisualInterface_Child: "VisualInterface_Primitive" = None):
        self.name = name
        self.VisualInterface_Child = VisualInterface_Child
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def VisualInterface_Child(self):
        return self.__VisualInterface_Child

    @VisualInterface_Child.setter
    def VisualInterface_Child(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_VisualInterface_Child__VisualInterface_Child", None)
        self.__VisualInterface_Child = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VisualInterface_Primitive10"):
                opp_val = getattr(old_value, "VisualInterface_Primitive10", None)
                if opp_val == self:
                    setattr(old_value, "VisualInterface_Primitive10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VisualInterface_Primitive10"):
                opp_val = getattr(value, "VisualInterface_Primitive10", None)
                setattr(value, "VisualInterface_Primitive10", self)

class Shape:

    pass
class VisualInterface_Arc(Shape):

    def __init__(self, start: int, length: int):
        self.start = start
        self.length = length
        
    @property
    def start(self) -> int:
        return self.__start

    @start.setter
    def start(self, start: int):
        self.__start = start

    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length

class VisualInterface_Ellipse(Shape):

    pass
class VisualInterface_Line(Shape):

    pass
class VisualInterface_Rectangle(Shape):

    pass
class Figure:

    pass
class VisualInterface_Image(Figure):

    def __init__(self, uri: str):
        self.uri = uri
        
    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

class VisualInterface_Text(Figure):

    def __init__(self, text: str, labelAlignment: str, iconAlignment: str, textAlignment: str, textPlacement: str, fontName: str, fontSize: int, fontBold: bool, fontItalic: bool):
        self.text = text
        self.labelAlignment = labelAlignment
        self.iconAlignment = iconAlignment
        self.textAlignment = textAlignment
        self.textPlacement = textPlacement
        self.fontName = fontName
        self.fontSize = fontSize
        self.fontBold = fontBold
        self.fontItalic = fontItalic
        
    @property
    def fontItalic(self) -> bool:
        return self.__fontItalic

    @fontItalic.setter
    def fontItalic(self, fontItalic: bool):
        self.__fontItalic = fontItalic

    @property
    def fontBold(self) -> bool:
        return self.__fontBold

    @fontBold.setter
    def fontBold(self, fontBold: bool):
        self.__fontBold = fontBold

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def fontSize(self) -> int:
        return self.__fontSize

    @fontSize.setter
    def fontSize(self, fontSize: int):
        self.__fontSize = fontSize

    @property
    def textAlignment(self) -> str:
        return self.__textAlignment

    @textAlignment.setter
    def textAlignment(self, textAlignment: str):
        self.__textAlignment = textAlignment

    @property
    def fontName(self) -> str:
        return self.__fontName

    @fontName.setter
    def fontName(self, fontName: str):
        self.__fontName = fontName

    @property
    def labelAlignment(self) -> str:
        return self.__labelAlignment

    @labelAlignment.setter
    def labelAlignment(self, labelAlignment: str):
        self.__labelAlignment = labelAlignment

    @property
    def textPlacement(self) -> str:
        return self.__textPlacement

    @textPlacement.setter
    def textPlacement(self, textPlacement: str):
        self.__textPlacement = textPlacement

    @property
    def iconAlignment(self) -> str:
        return self.__iconAlignment

    @iconAlignment.setter
    def iconAlignment(self, iconAlignment: str):
        self.__iconAlignment = iconAlignment

class VisualInterface_FigureContainer(Figure):

    pass
class VisualInterface_Shape(Figure):

    def __init__(self, lineWidth: float, antialias: str, alpha: str, fill: bool, outline: bool):
        self.lineWidth = lineWidth
        self.antialias = antialias
        self.alpha = alpha
        self.fill = fill
        self.outline = outline
        
    @property
    def lineWidth(self) -> float:
        return self.__lineWidth

    @lineWidth.setter
    def lineWidth(self, lineWidth: float):
        self.__lineWidth = lineWidth

    @property
    def alpha(self) -> str:
        return self.__alpha

    @alpha.setter
    def alpha(self, alpha: str):
        self.__alpha = alpha

    @property
    def antialias(self) -> str:
        return self.__antialias

    @antialias.setter
    def antialias(self, antialias: str):
        self.__antialias = antialias

    @property
    def outline(self) -> bool:
        return self.__outline

    @outline.setter
    def outline(self, outline: bool):
        self.__outline = outline

    @property
    def fill(self) -> bool:
        return self.__fill

    @fill.setter
    def fill(self, fill: bool):
        self.__fill = fill

class Primitive:

    pass
class VisualInterface_Figure(Primitive):

    def __init__(self, foregroundColor: str, backgroundColor: str, onClick: str, onDoubleClick: str, visible: bool, border: str, opaque: str, toolTip: str, VisualInterface_Figure: "VisualInterface_Dimension" = None, VisualInterface_Figure22: "VisualInterface_Cursor" = None):
        self.foregroundColor = foregroundColor
        self.backgroundColor = backgroundColor
        self.onClick = onClick
        self.onDoubleClick = onDoubleClick
        self.visible = visible
        self.border = border
        self.opaque = opaque
        self.toolTip = toolTip
        self.VisualInterface_Figure = VisualInterface_Figure
        self.VisualInterface_Figure22 = VisualInterface_Figure22
        
    @property
    def border(self) -> str:
        return self.__border

    @border.setter
    def border(self, border: str):
        self.__border = border

    @property
    def toolTip(self) -> str:
        return self.__toolTip

    @toolTip.setter
    def toolTip(self, toolTip: str):
        self.__toolTip = toolTip

    @property
    def foregroundColor(self) -> str:
        return self.__foregroundColor

    @foregroundColor.setter
    def foregroundColor(self, foregroundColor: str):
        self.__foregroundColor = foregroundColor

    @property
    def onClick(self) -> str:
        return self.__onClick

    @onClick.setter
    def onClick(self, onClick: str):
        self.__onClick = onClick

    @property
    def backgroundColor(self) -> str:
        return self.__backgroundColor

    @backgroundColor.setter
    def backgroundColor(self, backgroundColor: str):
        self.__backgroundColor = backgroundColor

    @property
    def onDoubleClick(self) -> str:
        return self.__onDoubleClick

    @onDoubleClick.setter
    def onDoubleClick(self, onDoubleClick: str):
        self.__onDoubleClick = onDoubleClick

    @property
    def visible(self) -> bool:
        return self.__visible

    @visible.setter
    def visible(self, visible: bool):
        self.__visible = visible

    @property
    def opaque(self) -> str:
        return self.__opaque

    @opaque.setter
    def opaque(self, opaque: str):
        self.__opaque = opaque

    @property
    def VisualInterface_Figure(self):
        return self.__VisualInterface_Figure

    @VisualInterface_Figure.setter
    def VisualInterface_Figure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_VisualInterface_Figure__VisualInterface_Figure", None)
        self.__VisualInterface_Figure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VisualInterface_Dimension20"):
                opp_val = getattr(old_value, "VisualInterface_Dimension20", None)
                if opp_val == self:
                    setattr(old_value, "VisualInterface_Dimension20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VisualInterface_Dimension20"):
                opp_val = getattr(value, "VisualInterface_Dimension20", None)
                setattr(value, "VisualInterface_Dimension20", self)

    @property
    def VisualInterface_Figure22(self):
        return self.__VisualInterface_Figure22

    @VisualInterface_Figure22.setter
    def VisualInterface_Figure22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_VisualInterface_Figure__VisualInterface_Figure22", None)
        self.__VisualInterface_Figure22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VisualInterface_Cursor23"):
                opp_val = getattr(old_value, "VisualInterface_Cursor23", None)
                if opp_val == self:
                    setattr(old_value, "VisualInterface_Cursor23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VisualInterface_Cursor23"):
                opp_val = getattr(value, "VisualInterface_Cursor23", None)
                setattr(value, "VisualInterface_Cursor23", self)

class VisualInterface_SymbolReference(Primitive):

    def __init__(self, uri: str, zoom: str, onCreateProperties: str, VisualInterface_SymbolReference: set["VisualInterface_StringToStringMap"] = None):
        self.uri = uri
        self.zoom = zoom
        self.onCreateProperties = onCreateProperties
        self.VisualInterface_SymbolReference = VisualInterface_SymbolReference if VisualInterface_SymbolReference is not None else set()
        
    @property
    def onCreateProperties(self) -> str:
        return self.__onCreateProperties

    @onCreateProperties.setter
    def onCreateProperties(self, onCreateProperties: str):
        self.__onCreateProperties = onCreateProperties

    @property
    def zoom(self) -> str:
        return self.__zoom

    @zoom.setter
    def zoom(self, zoom: str):
        self.__zoom = zoom

    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

    @property
    def VisualInterface_SymbolReference(self):
        return self.__VisualInterface_SymbolReference

    @VisualInterface_SymbolReference.setter
    def VisualInterface_SymbolReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_VisualInterface_SymbolReference__VisualInterface_SymbolReference", None)
        self.__VisualInterface_SymbolReference = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VisualInterface_StringToStringMap25"):
                    opp_val = getattr(item, "VisualInterface_StringToStringMap25", None)
                    
                    if opp_val == self:
                        setattr(item, "VisualInterface_StringToStringMap25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VisualInterface_StringToStringMap25"):
                    opp_val = getattr(item, "VisualInterface_StringToStringMap25", None)
                    
                    setattr(item, "VisualInterface_StringToStringMap25", self)
                    

class VisualInterface_Container(Primitive):

    pass
class VisualInterface_Cursor(ABC):

    pass
class VisualInterface_StringToStringMap:

    def __init__(self, key: str, value: str, VisualInterface_StringToStringMap: "VisualInterface_Symbol" = None, VisualInterface_StringToStringMap25: "VisualInterface_SymbolReference" = None):
        self.key = key
        self.value = value
        self.VisualInterface_StringToStringMap = VisualInterface_StringToStringMap
        self.VisualInterface_StringToStringMap25 = VisualInterface_StringToStringMap25
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def VisualInterface_StringToStringMap25(self):
        return self.__VisualInterface_StringToStringMap25

    @VisualInterface_StringToStringMap25.setter
    def VisualInterface_StringToStringMap25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_VisualInterface_StringToStringMap__VisualInterface_StringToStringMap25", None)
        self.__VisualInterface_StringToStringMap25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VisualInterface_SymbolReference"):
                opp_val = getattr(old_value, "VisualInterface_SymbolReference", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VisualInterface_SymbolReference"):
                opp_val = getattr(value, "VisualInterface_SymbolReference", None)
                if opp_val is None:
                    setattr(value, "VisualInterface_SymbolReference", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def VisualInterface_StringToStringMap(self):
        return self.__VisualInterface_StringToStringMap

    @VisualInterface_StringToStringMap.setter
    def VisualInterface_StringToStringMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_VisualInterface_StringToStringMap__VisualInterface_StringToStringMap", None)
        self.__VisualInterface_StringToStringMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VisualInterface_Symbol2"):
                opp_val = getattr(old_value, "VisualInterface_Symbol2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VisualInterface_Symbol2"):
                opp_val = getattr(value, "VisualInterface_Symbol2", None)
                if opp_val is None:
                    setattr(value, "VisualInterface_Symbol2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class VisualInterface_Primitive(ABC):

    def __init__(self, name: str, VisualInterface_Primitive: "VisualInterface_Symbol" = None, VisualInterface_Primitive10: "VisualInterface_Child" = None, VisualInterface_Primitive29: "VisualInterface_FigureContainer" = None, VisualInterface_Primitive37: "VisualInterface_StackContainer" = None, VisualInterface_Primitive32: "VisualInterface_Connection" = None, VisualInterface_Primitive35: "VisualInterface_Connection" = None):
        self.name = name
        self.VisualInterface_Primitive = VisualInterface_Primitive
        self.VisualInterface_Primitive10 = VisualInterface_Primitive10
        self.VisualInterface_Primitive29 = VisualInterface_Primitive29
        self.VisualInterface_Primitive37 = VisualInterface_Primitive37
        self.VisualInterface_Primitive32 = VisualInterface_Primitive32
        self.VisualInterface_Primitive35 = VisualInterface_Primitive35
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def VisualInterface_Primitive32(self):
        return self.__VisualInterface_Primitive32

    @VisualInterface_Primitive32.setter
    def VisualInterface_Primitive32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_VisualInterface_Primitive__VisualInterface_Primitive32", None)
        self.__VisualInterface_Primitive32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VisualInterface_Connection31"):
                opp_val = getattr(old_value, "VisualInterface_Connection31", None)
                if opp_val == self:
                    setattr(old_value, "VisualInterface_Connection31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VisualInterface_Connection31"):
                opp_val = getattr(value, "VisualInterface_Connection31", None)
                setattr(value, "VisualInterface_Connection31", self)

    @property
    def VisualInterface_Primitive29(self):
        return self.__VisualInterface_Primitive29

    @VisualInterface_Primitive29.setter
    def VisualInterface_Primitive29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_VisualInterface_Primitive__VisualInterface_Primitive29", None)
        self.__VisualInterface_Primitive29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VisualInterface_FigureContainer"):
                opp_val = getattr(old_value, "VisualInterface_FigureContainer", None)
                if opp_val == self:
                    setattr(old_value, "VisualInterface_FigureContainer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VisualInterface_FigureContainer"):
                opp_val = getattr(value, "VisualInterface_FigureContainer", None)
                setattr(value, "VisualInterface_FigureContainer", self)

    @property
    def VisualInterface_Primitive35(self):
        return self.__VisualInterface_Primitive35

    @VisualInterface_Primitive35.setter
    def VisualInterface_Primitive35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_VisualInterface_Primitive__VisualInterface_Primitive35", None)
        self.__VisualInterface_Primitive35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VisualInterface_Connection34"):
                opp_val = getattr(old_value, "VisualInterface_Connection34", None)
                if opp_val == self:
                    setattr(old_value, "VisualInterface_Connection34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VisualInterface_Connection34"):
                opp_val = getattr(value, "VisualInterface_Connection34", None)
                setattr(value, "VisualInterface_Connection34", self)

    @property
    def VisualInterface_Primitive10(self):
        return self.__VisualInterface_Primitive10

    @VisualInterface_Primitive10.setter
    def VisualInterface_Primitive10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_VisualInterface_Primitive__VisualInterface_Primitive10", None)
        self.__VisualInterface_Primitive10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VisualInterface_Child"):
                opp_val = getattr(old_value, "VisualInterface_Child", None)
                if opp_val == self:
                    setattr(old_value, "VisualInterface_Child", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VisualInterface_Child"):
                opp_val = getattr(value, "VisualInterface_Child", None)
                setattr(value, "VisualInterface_Child", self)

    @property
    def VisualInterface_Primitive37(self):
        return self.__VisualInterface_Primitive37

    @VisualInterface_Primitive37.setter
    def VisualInterface_Primitive37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_VisualInterface_Primitive__VisualInterface_Primitive37", None)
        self.__VisualInterface_Primitive37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VisualInterface_StackContainer"):
                opp_val = getattr(old_value, "VisualInterface_StackContainer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VisualInterface_StackContainer"):
                opp_val = getattr(value, "VisualInterface_StackContainer", None)
                if opp_val is None:
                    setattr(value, "VisualInterface_StackContainer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def VisualInterface_Primitive(self):
        return self.__VisualInterface_Primitive

    @VisualInterface_Primitive.setter
    def VisualInterface_Primitive(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_VisualInterface_Primitive__VisualInterface_Primitive", None)
        self.__VisualInterface_Primitive = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VisualInterface_Symbol"):
                opp_val = getattr(old_value, "VisualInterface_Symbol", None)
                if opp_val == self:
                    setattr(old_value, "VisualInterface_Symbol", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VisualInterface_Symbol"):
                opp_val = getattr(value, "VisualInterface_Symbol", None)
                setattr(value, "VisualInterface_Symbol", self)

class VisualInterface_Symbol:

    def __init__(self, onInit: str, onDispose: str, onUpdate: str, scriptModules: str, backgroundColor: str, VisualInterface_Symbol: "VisualInterface_Primitive" = None, VisualInterface_Symbol2: set["VisualInterface_StringToStringMap"] = None, VisualInterface_Symbol4: "VisualInterface_Cursor" = None, VisualInterface_Symbol6: "VisualInterface_Dimension" = None, VisualInterface_Symbol8: set["VisualInterface_Connection"] = None):
        self.onInit = onInit
        self.onDispose = onDispose
        self.onUpdate = onUpdate
        self.scriptModules = scriptModules
        self.backgroundColor = backgroundColor
        self.VisualInterface_Symbol = VisualInterface_Symbol
        self.VisualInterface_Symbol2 = VisualInterface_Symbol2 if VisualInterface_Symbol2 is not None else set()
        self.VisualInterface_Symbol4 = VisualInterface_Symbol4
        self.VisualInterface_Symbol6 = VisualInterface_Symbol6
        self.VisualInterface_Symbol8 = VisualInterface_Symbol8 if VisualInterface_Symbol8 is not None else set()
        
    @property
    def scriptModules(self) -> str:
        return self.__scriptModules

    @scriptModules.setter
    def scriptModules(self, scriptModules: str):
        self.__scriptModules = scriptModules

    @property
    def onUpdate(self) -> str:
        return self.__onUpdate

    @onUpdate.setter
    def onUpdate(self, onUpdate: str):
        self.__onUpdate = onUpdate

    @property
    def onDispose(self) -> str:
        return self.__onDispose

    @onDispose.setter
    def onDispose(self, onDispose: str):
        self.__onDispose = onDispose

    @property
    def onInit(self) -> str:
        return self.__onInit

    @onInit.setter
    def onInit(self, onInit: str):
        self.__onInit = onInit

    @property
    def backgroundColor(self) -> str:
        return self.__backgroundColor

    @backgroundColor.setter
    def backgroundColor(self, backgroundColor: str):
        self.__backgroundColor = backgroundColor

    @property
    def VisualInterface_Symbol4(self):
        return self.__VisualInterface_Symbol4

    @VisualInterface_Symbol4.setter
    def VisualInterface_Symbol4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_VisualInterface_Symbol__VisualInterface_Symbol4", None)
        self.__VisualInterface_Symbol4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VisualInterface_Cursor"):
                opp_val = getattr(old_value, "VisualInterface_Cursor", None)
                if opp_val == self:
                    setattr(old_value, "VisualInterface_Cursor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VisualInterface_Cursor"):
                opp_val = getattr(value, "VisualInterface_Cursor", None)
                setattr(value, "VisualInterface_Cursor", self)

    @property
    def VisualInterface_Symbol8(self):
        return self.__VisualInterface_Symbol8

    @VisualInterface_Symbol8.setter
    def VisualInterface_Symbol8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_VisualInterface_Symbol__VisualInterface_Symbol8", None)
        self.__VisualInterface_Symbol8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VisualInterface_Connection"):
                    opp_val = getattr(item, "VisualInterface_Connection", None)
                    
                    if opp_val == self:
                        setattr(item, "VisualInterface_Connection", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VisualInterface_Connection"):
                    opp_val = getattr(item, "VisualInterface_Connection", None)
                    
                    setattr(item, "VisualInterface_Connection", self)
                    

    @property
    def VisualInterface_Symbol2(self):
        return self.__VisualInterface_Symbol2

    @VisualInterface_Symbol2.setter
    def VisualInterface_Symbol2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_VisualInterface_Symbol__VisualInterface_Symbol2", None)
        self.__VisualInterface_Symbol2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VisualInterface_StringToStringMap"):
                    opp_val = getattr(item, "VisualInterface_StringToStringMap", None)
                    
                    if opp_val == self:
                        setattr(item, "VisualInterface_StringToStringMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VisualInterface_StringToStringMap"):
                    opp_val = getattr(item, "VisualInterface_StringToStringMap", None)
                    
                    setattr(item, "VisualInterface_StringToStringMap", self)
                    

    @property
    def VisualInterface_Symbol6(self):
        return self.__VisualInterface_Symbol6

    @VisualInterface_Symbol6.setter
    def VisualInterface_Symbol6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_VisualInterface_Symbol__VisualInterface_Symbol6", None)
        self.__VisualInterface_Symbol6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VisualInterface_Dimension"):
                opp_val = getattr(old_value, "VisualInterface_Dimension", None)
                if opp_val == self:
                    setattr(old_value, "VisualInterface_Dimension", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VisualInterface_Dimension"):
                opp_val = getattr(value, "VisualInterface_Dimension", None)
                setattr(value, "VisualInterface_Dimension", self)

    @property
    def VisualInterface_Symbol(self):
        return self.__VisualInterface_Symbol

    @VisualInterface_Symbol.setter
    def VisualInterface_Symbol(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_VisualInterface_Symbol__VisualInterface_Symbol", None)
        self.__VisualInterface_Symbol = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VisualInterface_Primitive"):
                opp_val = getattr(old_value, "VisualInterface_Primitive", None)
                if opp_val == self:
                    setattr(old_value, "VisualInterface_Primitive", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VisualInterface_Primitive"):
                opp_val = getattr(value, "VisualInterface_Primitive", None)
                setattr(value, "VisualInterface_Primitive", self)
