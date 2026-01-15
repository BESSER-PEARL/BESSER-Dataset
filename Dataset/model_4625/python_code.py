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
class SystemCursorType(Enum):
    ARROW = "ARROW"
    HAND = "HAND"
class GridAlignment(Enum):
    CENTER = "CENTER"
    FILL = "FILL"
    BEGINNING = "BEGINNING"
    END = "END"
class Orientation(Enum):
    NORTH = "NORTH"
    SOUTH = "SOUTH"
    EAST = "EAST"
    WEST = "WEST"


############################################
# Definition of Classes
############################################

class Cursor:

    pass
class model_SystemCursor(Cursor):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class Shape:

    pass
class model_Arc(Shape):

    def __init__(self, start: int, length: int):
        self.start = start
        self.length = length
        
    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length

    @property
    def start(self) -> int:
        return self.__start

    @start.setter
    def start(self, start: int):
        self.__start = start

class model_Polygon(Shape):

    pass
class model_RoundedRectangle(Shape):

    pass
class model_Ellipse(Shape):

    pass
class model_Rectangle(Shape):

    pass
class model_Line(Shape):

    pass
class Container:

    pass
class model_GridContainer(Container):

    def __init__(self, columns: int, equalWidth: bool, horizontalSpacing: int, verticalSpacing: int, marginWidth: int, marginHeight: int, model_GridContainer: set["model_GridChild"] = None):
        self.columns = columns
        self.equalWidth = equalWidth
        self.horizontalSpacing = horizontalSpacing
        self.verticalSpacing = verticalSpacing
        self.marginWidth = marginWidth
        self.marginHeight = marginHeight
        self.model_GridContainer = model_GridContainer if model_GridContainer is not None else set()
        
    @property
    def equalWidth(self) -> bool:
        return self.__equalWidth

    @equalWidth.setter
    def equalWidth(self, equalWidth: bool):
        self.__equalWidth = equalWidth

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
    def marginHeight(self) -> int:
        return self.__marginHeight

    @marginHeight.setter
    def marginHeight(self, marginHeight: int):
        self.__marginHeight = marginHeight

    @property
    def verticalSpacing(self) -> int:
        return self.__verticalSpacing

    @verticalSpacing.setter
    def verticalSpacing(self, verticalSpacing: int):
        self.__verticalSpacing = verticalSpacing

    @property
    def columns(self) -> int:
        return self.__columns

    @columns.setter
    def columns(self, columns: int):
        self.__columns = columns

    @property
    def model_GridContainer(self):
        return self.__model_GridContainer

    @model_GridContainer.setter
    def model_GridContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_GridContainer__model_GridContainer", None)
        self.__model_GridContainer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_GridChild"):
                    opp_val = getattr(item, "model_GridChild", None)
                    
                    if opp_val == self:
                        setattr(item, "model_GridChild", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_GridChild"):
                    opp_val = getattr(item, "model_GridChild", None)
                    
                    setattr(item, "model_GridChild", self)
                    

class model_BorderContainer(Container):

    def __init__(self, verticalSpacing: int, horizontalSpacing: int, model_BorderContainer: set["model_BorderChild"] = None):
        self.verticalSpacing = verticalSpacing
        self.horizontalSpacing = horizontalSpacing
        self.model_BorderContainer = model_BorderContainer if model_BorderContainer is not None else set()
        
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
    def model_BorderContainer(self):
        return self.__model_BorderContainer

    @model_BorderContainer.setter
    def model_BorderContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_BorderContainer__model_BorderContainer", None)
        self.__model_BorderContainer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_BorderChild"):
                    opp_val = getattr(item, "model_BorderChild", None)
                    
                    if opp_val == self:
                        setattr(item, "model_BorderChild", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_BorderChild"):
                    opp_val = getattr(item, "model_BorderChild", None)
                    
                    setattr(item, "model_BorderChild", self)
                    

class model_StackContainer(Container):

    pass
class model_XYContainer(Container):

    pass
class model_Position:

    def __init__(self, x: float, y: float, model_Position: "model_XYChild" = None, model_Position18: "model_Line" = None, model_Position39: "model_Polygon" = None):
        self.x = x
        self.y = y
        self.model_Position = model_Position
        self.model_Position18 = model_Position18
        self.model_Position39 = model_Position39
        
    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x

    @property
    def model_Position(self):
        return self.__model_Position

    @model_Position.setter
    def model_Position(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Position__model_Position", None)
        self.__model_Position = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_XYChild"):
                opp_val = getattr(old_value, "model_XYChild", None)
                if opp_val == self:
                    setattr(old_value, "model_XYChild", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_XYChild"):
                opp_val = getattr(value, "model_XYChild", None)
                setattr(value, "model_XYChild", self)

    @property
    def model_Position39(self):
        return self.__model_Position39

    @model_Position39.setter
    def model_Position39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Position__model_Position39", None)
        self.__model_Position39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Polygon"):
                opp_val = getattr(old_value, "model_Polygon", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Polygon"):
                opp_val = getattr(value, "model_Polygon", None)
                if opp_val is None:
                    setattr(value, "model_Polygon", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Position18(self):
        return self.__model_Position18

    @model_Position18.setter
    def model_Position18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Position__model_Position18", None)
        self.__model_Position18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Line"):
                opp_val = getattr(old_value, "model_Line", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Line"):
                opp_val = getattr(value, "model_Line", None)
                if opp_val is None:
                    setattr(value, "model_Line", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Child:

    pass
class model_GridChild(Child):

    def __init__(self, horizontalAlignment: str, verticalAlignment: str, grabHorizontalSpace: bool, grabVerticalSpace: bool, spanCols: int, spanRows: str, widthHint: str, heightHint: str, model_GridChild: "model_GridContainer" = None):
        self.horizontalAlignment = horizontalAlignment
        self.verticalAlignment = verticalAlignment
        self.grabHorizontalSpace = grabHorizontalSpace
        self.grabVerticalSpace = grabVerticalSpace
        self.spanCols = spanCols
        self.spanRows = spanRows
        self.widthHint = widthHint
        self.heightHint = heightHint
        self.model_GridChild = model_GridChild
        
    @property
    def grabVerticalSpace(self) -> bool:
        return self.__grabVerticalSpace

    @grabVerticalSpace.setter
    def grabVerticalSpace(self, grabVerticalSpace: bool):
        self.__grabVerticalSpace = grabVerticalSpace

    @property
    def widthHint(self) -> str:
        return self.__widthHint

    @widthHint.setter
    def widthHint(self, widthHint: str):
        self.__widthHint = widthHint

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
    def grabHorizontalSpace(self) -> bool:
        return self.__grabHorizontalSpace

    @grabHorizontalSpace.setter
    def grabHorizontalSpace(self, grabHorizontalSpace: bool):
        self.__grabHorizontalSpace = grabHorizontalSpace

    @property
    def spanCols(self) -> int:
        return self.__spanCols

    @spanCols.setter
    def spanCols(self, spanCols: int):
        self.__spanCols = spanCols

    @property
    def heightHint(self) -> str:
        return self.__heightHint

    @heightHint.setter
    def heightHint(self, heightHint: str):
        self.__heightHint = heightHint

    @property
    def spanRows(self) -> str:
        return self.__spanRows

    @spanRows.setter
    def spanRows(self, spanRows: str):
        self.__spanRows = spanRows

    @property
    def model_GridChild(self):
        return self.__model_GridChild

    @model_GridChild.setter
    def model_GridChild(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_GridChild__model_GridChild", None)
        self.__model_GridChild = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_GridContainer"):
                opp_val = getattr(old_value, "model_GridContainer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_GridContainer"):
                opp_val = getattr(value, "model_GridContainer", None)
                if opp_val is None:
                    setattr(value, "model_GridContainer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_BorderChild(Child):

    def __init__(self, alignment: str, model_BorderChild: "model_BorderContainer" = None):
        self.alignment = alignment
        self.model_BorderChild = model_BorderChild
        
    @property
    def alignment(self) -> str:
        return self.__alignment

    @alignment.setter
    def alignment(self, alignment: str):
        self.__alignment = alignment

    @property
    def model_BorderChild(self):
        return self.__model_BorderChild

    @model_BorderChild.setter
    def model_BorderChild(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_BorderChild__model_BorderChild", None)
        self.__model_BorderChild = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_BorderContainer"):
                opp_val = getattr(old_value, "model_BorderContainer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_BorderContainer"):
                opp_val = getattr(value, "model_BorderContainer", None)
                if opp_val is None:
                    setattr(value, "model_BorderContainer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_XYChild(Child):

    pass
class model_Child:

    def __init__(self, name: str, model_Child: "model_Primitive" = None):
        self.name = name
        self.model_Child = model_Child
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_Child(self):
        return self.__model_Child

    @model_Child.setter
    def model_Child(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Child__model_Child", None)
        self.__model_Child = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Primitive10"):
                opp_val = getattr(old_value, "model_Primitive10", None)
                if opp_val == self:
                    setattr(old_value, "model_Primitive10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Primitive10"):
                opp_val = getattr(value, "model_Primitive10", None)
                setattr(value, "model_Primitive10", self)

class model_Symbol:

    def __init__(self, onInit: str, onDispose: str, onUpdate: str, scriptModules: str, backgroundColor: str, backgroundImage: str, model_Symbol: "model_Primitive" = None, model_Symbol2: set["model_StringToStringMap"] = None, model_Symbol4: "model_Cursor" = None, model_Symbol6: "model_Dimension" = None, model_Symbol8: set["model_Connection"] = None):
        self.onInit = onInit
        self.onDispose = onDispose
        self.onUpdate = onUpdate
        self.scriptModules = scriptModules
        self.backgroundColor = backgroundColor
        self.backgroundImage = backgroundImage
        self.model_Symbol = model_Symbol
        self.model_Symbol2 = model_Symbol2 if model_Symbol2 is not None else set()
        self.model_Symbol4 = model_Symbol4
        self.model_Symbol6 = model_Symbol6
        self.model_Symbol8 = model_Symbol8 if model_Symbol8 is not None else set()
        
    @property
    def scriptModules(self) -> str:
        return self.__scriptModules

    @scriptModules.setter
    def scriptModules(self, scriptModules: str):
        self.__scriptModules = scriptModules

    @property
    def onDispose(self) -> str:
        return self.__onDispose

    @onDispose.setter
    def onDispose(self, onDispose: str):
        self.__onDispose = onDispose

    @property
    def backgroundImage(self) -> str:
        return self.__backgroundImage

    @backgroundImage.setter
    def backgroundImage(self, backgroundImage: str):
        self.__backgroundImage = backgroundImage

    @property
    def backgroundColor(self) -> str:
        return self.__backgroundColor

    @backgroundColor.setter
    def backgroundColor(self, backgroundColor: str):
        self.__backgroundColor = backgroundColor

    @property
    def onInit(self) -> str:
        return self.__onInit

    @onInit.setter
    def onInit(self, onInit: str):
        self.__onInit = onInit

    @property
    def onUpdate(self) -> str:
        return self.__onUpdate

    @onUpdate.setter
    def onUpdate(self, onUpdate: str):
        self.__onUpdate = onUpdate

    @property
    def model_Symbol8(self):
        return self.__model_Symbol8

    @model_Symbol8.setter
    def model_Symbol8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Symbol__model_Symbol8", None)
        self.__model_Symbol8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Connection"):
                    opp_val = getattr(item, "model_Connection", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Connection", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Connection"):
                    opp_val = getattr(item, "model_Connection", None)
                    
                    setattr(item, "model_Connection", self)
                    

    @property
    def model_Symbol4(self):
        return self.__model_Symbol4

    @model_Symbol4.setter
    def model_Symbol4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Symbol__model_Symbol4", None)
        self.__model_Symbol4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Cursor"):
                opp_val = getattr(old_value, "model_Cursor", None)
                if opp_val == self:
                    setattr(old_value, "model_Cursor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Cursor"):
                opp_val = getattr(value, "model_Cursor", None)
                setattr(value, "model_Cursor", self)

    @property
    def model_Symbol(self):
        return self.__model_Symbol

    @model_Symbol.setter
    def model_Symbol(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Symbol__model_Symbol", None)
        self.__model_Symbol = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Primitive"):
                opp_val = getattr(old_value, "model_Primitive", None)
                if opp_val == self:
                    setattr(old_value, "model_Primitive", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Primitive"):
                opp_val = getattr(value, "model_Primitive", None)
                setattr(value, "model_Primitive", self)

    @property
    def model_Symbol6(self):
        return self.__model_Symbol6

    @model_Symbol6.setter
    def model_Symbol6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Symbol__model_Symbol6", None)
        self.__model_Symbol6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Dimension"):
                opp_val = getattr(old_value, "model_Dimension", None)
                if opp_val == self:
                    setattr(old_value, "model_Dimension", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Dimension"):
                opp_val = getattr(value, "model_Dimension", None)
                setattr(value, "model_Dimension", self)

    @property
    def model_Symbol2(self):
        return self.__model_Symbol2

    @model_Symbol2.setter
    def model_Symbol2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Symbol__model_Symbol2", None)
        self.__model_Symbol2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_StringToStringMap"):
                    opp_val = getattr(item, "model_StringToStringMap", None)
                    
                    if opp_val == self:
                        setattr(item, "model_StringToStringMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_StringToStringMap"):
                    opp_val = getattr(item, "model_StringToStringMap", None)
                    
                    setattr(item, "model_StringToStringMap", self)
                    

class Figure:

    pass
class model_Text(Figure):

    def __init__(self, fontBold: bool, fontItalic: bool, alpha: str, text: str, labelAlignment: str, iconAlignment: str, textAlignment: str, textPlacement: str, fontName: str, fontSize: int):
        self.fontBold = fontBold
        self.fontItalic = fontItalic
        self.alpha = alpha
        self.text = text
        self.labelAlignment = labelAlignment
        self.iconAlignment = iconAlignment
        self.textAlignment = textAlignment
        self.textPlacement = textPlacement
        self.fontName = fontName
        self.fontSize = fontSize
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def fontItalic(self) -> bool:
        return self.__fontItalic

    @fontItalic.setter
    def fontItalic(self, fontItalic: bool):
        self.__fontItalic = fontItalic

    @property
    def labelAlignment(self) -> str:
        return self.__labelAlignment

    @labelAlignment.setter
    def labelAlignment(self, labelAlignment: str):
        self.__labelAlignment = labelAlignment

    @property
    def alpha(self) -> str:
        return self.__alpha

    @alpha.setter
    def alpha(self, alpha: str):
        self.__alpha = alpha

    @property
    def textPlacement(self) -> str:
        return self.__textPlacement

    @textPlacement.setter
    def textPlacement(self, textPlacement: str):
        self.__textPlacement = textPlacement

    @property
    def fontName(self) -> str:
        return self.__fontName

    @fontName.setter
    def fontName(self, fontName: str):
        self.__fontName = fontName

    @property
    def fontBold(self) -> bool:
        return self.__fontBold

    @fontBold.setter
    def fontBold(self, fontBold: bool):
        self.__fontBold = fontBold

    @property
    def textAlignment(self) -> str:
        return self.__textAlignment

    @textAlignment.setter
    def textAlignment(self, textAlignment: str):
        self.__textAlignment = textAlignment

    @property
    def iconAlignment(self) -> str:
        return self.__iconAlignment

    @iconAlignment.setter
    def iconAlignment(self, iconAlignment: str):
        self.__iconAlignment = iconAlignment

    @property
    def fontSize(self) -> int:
        return self.__fontSize

    @fontSize.setter
    def fontSize(self, fontSize: int):
        self.__fontSize = fontSize

class model_Image(Figure):

    def __init__(self, uri: str, imageAlignment: str):
        self.uri = uri
        self.imageAlignment = imageAlignment
        
    @property
    def imageAlignment(self) -> str:
        return self.__imageAlignment

    @imageAlignment.setter
    def imageAlignment(self, imageAlignment: str):
        self.__imageAlignment = imageAlignment

    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

class model_FigureContainer(Figure):

    pass
class model_Shape(Figure):

    def __init__(self, lineWidth: float, antialias: str, alpha: str, fill: bool, outline: bool):
        self.lineWidth = lineWidth
        self.antialias = antialias
        self.alpha = alpha
        self.fill = fill
        self.outline = outline
        
    @property
    def antialias(self) -> str:
        return self.__antialias

    @antialias.setter
    def antialias(self, antialias: str):
        self.__antialias = antialias

    @property
    def alpha(self) -> str:
        return self.__alpha

    @alpha.setter
    def alpha(self, alpha: str):
        self.__alpha = alpha

    @property
    def outline(self) -> bool:
        return self.__outline

    @outline.setter
    def outline(self, outline: bool):
        self.__outline = outline

    @property
    def lineWidth(self) -> float:
        return self.__lineWidth

    @lineWidth.setter
    def lineWidth(self, lineWidth: float):
        self.__lineWidth = lineWidth

    @property
    def fill(self) -> bool:
        return self.__fill

    @fill.setter
    def fill(self, fill: bool):
        self.__fill = fill

class Primitive:

    pass
class model_SymbolReference(Primitive):

    def __init__(self, uri: str, zoom: str, onCreateProperties: str, model_SymbolReference: set["model_StringToStringMap"] = None):
        self.uri = uri
        self.zoom = zoom
        self.onCreateProperties = onCreateProperties
        self.model_SymbolReference = model_SymbolReference if model_SymbolReference is not None else set()
        
    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

    @property
    def zoom(self) -> str:
        return self.__zoom

    @zoom.setter
    def zoom(self, zoom: str):
        self.__zoom = zoom

    @property
    def onCreateProperties(self) -> str:
        return self.__onCreateProperties

    @onCreateProperties.setter
    def onCreateProperties(self, onCreateProperties: str):
        self.__onCreateProperties = onCreateProperties

    @property
    def model_SymbolReference(self):
        return self.__model_SymbolReference

    @model_SymbolReference.setter
    def model_SymbolReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_SymbolReference__model_SymbolReference", None)
        self.__model_SymbolReference = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_StringToStringMap25"):
                    opp_val = getattr(item, "model_StringToStringMap25", None)
                    
                    if opp_val == self:
                        setattr(item, "model_StringToStringMap25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_StringToStringMap25"):
                    opp_val = getattr(item, "model_StringToStringMap25", None)
                    
                    setattr(item, "model_StringToStringMap25", self)
                    

class model_Figure(Primitive):

    def __init__(self, foregroundColor: str, backgroundColor: str, onMouseHover: str, onMouseDrag: str, onClick: str, onDoubleClick: str, visible: bool, border: str, opaque: str, toolTip: str, onMouseIn: str, onMouseOut: str, onMouseMove: str, model_Figure: "model_Dimension" = None, model_Figure22: "model_Cursor" = None):
        self.foregroundColor = foregroundColor
        self.backgroundColor = backgroundColor
        self.onMouseHover = onMouseHover
        self.onMouseDrag = onMouseDrag
        self.onClick = onClick
        self.onDoubleClick = onDoubleClick
        self.visible = visible
        self.border = border
        self.opaque = opaque
        self.toolTip = toolTip
        self.onMouseIn = onMouseIn
        self.onMouseOut = onMouseOut
        self.onMouseMove = onMouseMove
        self.model_Figure = model_Figure
        self.model_Figure22 = model_Figure22
        
    @property
    def onDoubleClick(self) -> str:
        return self.__onDoubleClick

    @onDoubleClick.setter
    def onDoubleClick(self, onDoubleClick: str):
        self.__onDoubleClick = onDoubleClick

    @property
    def onMouseIn(self) -> str:
        return self.__onMouseIn

    @onMouseIn.setter
    def onMouseIn(self, onMouseIn: str):
        self.__onMouseIn = onMouseIn

    @property
    def onMouseDrag(self) -> str:
        return self.__onMouseDrag

    @onMouseDrag.setter
    def onMouseDrag(self, onMouseDrag: str):
        self.__onMouseDrag = onMouseDrag

    @property
    def opaque(self) -> str:
        return self.__opaque

    @opaque.setter
    def opaque(self, opaque: str):
        self.__opaque = opaque

    @property
    def visible(self) -> bool:
        return self.__visible

    @visible.setter
    def visible(self, visible: bool):
        self.__visible = visible

    @property
    def border(self) -> str:
        return self.__border

    @border.setter
    def border(self, border: str):
        self.__border = border

    @property
    def onClick(self) -> str:
        return self.__onClick

    @onClick.setter
    def onClick(self, onClick: str):
        self.__onClick = onClick

    @property
    def onMouseMove(self) -> str:
        return self.__onMouseMove

    @onMouseMove.setter
    def onMouseMove(self, onMouseMove: str):
        self.__onMouseMove = onMouseMove

    @property
    def backgroundColor(self) -> str:
        return self.__backgroundColor

    @backgroundColor.setter
    def backgroundColor(self, backgroundColor: str):
        self.__backgroundColor = backgroundColor

    @property
    def onMouseHover(self) -> str:
        return self.__onMouseHover

    @onMouseHover.setter
    def onMouseHover(self, onMouseHover: str):
        self.__onMouseHover = onMouseHover

    @property
    def onMouseOut(self) -> str:
        return self.__onMouseOut

    @onMouseOut.setter
    def onMouseOut(self, onMouseOut: str):
        self.__onMouseOut = onMouseOut

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
    def model_Figure(self):
        return self.__model_Figure

    @model_Figure.setter
    def model_Figure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Figure__model_Figure", None)
        self.__model_Figure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Dimension20"):
                opp_val = getattr(old_value, "model_Dimension20", None)
                if opp_val == self:
                    setattr(old_value, "model_Dimension20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Dimension20"):
                opp_val = getattr(value, "model_Dimension20", None)
                setattr(value, "model_Dimension20", self)

    @property
    def model_Figure22(self):
        return self.__model_Figure22

    @model_Figure22.setter
    def model_Figure22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Figure__model_Figure22", None)
        self.__model_Figure22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Cursor23"):
                opp_val = getattr(old_value, "model_Cursor23", None)
                if opp_val == self:
                    setattr(old_value, "model_Cursor23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Cursor23"):
                opp_val = getattr(value, "model_Cursor23", None)
                setattr(value, "model_Cursor23", self)

class model_Container(Primitive):

    pass
class model_Connection:

    pass
class model_Dimension:

    def __init__(self, width: float, height: float, model_Dimension: "model_Symbol" = None, model_Dimension14: "model_XYChild" = None, model_Dimension20: "model_Figure" = None, model_Dimension41: "model_RoundedRectangle" = None):
        self.width = width
        self.height = height
        self.model_Dimension = model_Dimension
        self.model_Dimension14 = model_Dimension14
        self.model_Dimension20 = model_Dimension20
        self.model_Dimension41 = model_Dimension41
        
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
    def model_Dimension14(self):
        return self.__model_Dimension14

    @model_Dimension14.setter
    def model_Dimension14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Dimension__model_Dimension14", None)
        self.__model_Dimension14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_XYChild13"):
                opp_val = getattr(old_value, "model_XYChild13", None)
                if opp_val == self:
                    setattr(old_value, "model_XYChild13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_XYChild13"):
                opp_val = getattr(value, "model_XYChild13", None)
                setattr(value, "model_XYChild13", self)

    @property
    def model_Dimension(self):
        return self.__model_Dimension

    @model_Dimension.setter
    def model_Dimension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Dimension__model_Dimension", None)
        self.__model_Dimension = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Symbol6"):
                opp_val = getattr(old_value, "model_Symbol6", None)
                if opp_val == self:
                    setattr(old_value, "model_Symbol6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Symbol6"):
                opp_val = getattr(value, "model_Symbol6", None)
                setattr(value, "model_Symbol6", self)

    @property
    def model_Dimension41(self):
        return self.__model_Dimension41

    @model_Dimension41.setter
    def model_Dimension41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Dimension__model_Dimension41", None)
        self.__model_Dimension41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_RoundedRectangle"):
                opp_val = getattr(old_value, "model_RoundedRectangle", None)
                if opp_val == self:
                    setattr(old_value, "model_RoundedRectangle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_RoundedRectangle"):
                opp_val = getattr(value, "model_RoundedRectangle", None)
                setattr(value, "model_RoundedRectangle", self)

    @property
    def model_Dimension20(self):
        return self.__model_Dimension20

    @model_Dimension20.setter
    def model_Dimension20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Dimension__model_Dimension20", None)
        self.__model_Dimension20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Figure"):
                opp_val = getattr(old_value, "model_Figure", None)
                if opp_val == self:
                    setattr(old_value, "model_Figure", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Figure"):
                opp_val = getattr(value, "model_Figure", None)
                setattr(value, "model_Figure", self)

class model_Cursor(ABC):

    pass
class model_StringToStringMap:

    def __init__(self, key: str, value: str, model_StringToStringMap: "model_Symbol" = None, model_StringToStringMap25: "model_SymbolReference" = None):
        self.key = key
        self.value = value
        self.model_StringToStringMap = model_StringToStringMap
        self.model_StringToStringMap25 = model_StringToStringMap25
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def model_StringToStringMap25(self):
        return self.__model_StringToStringMap25

    @model_StringToStringMap25.setter
    def model_StringToStringMap25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_StringToStringMap__model_StringToStringMap25", None)
        self.__model_StringToStringMap25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_SymbolReference"):
                opp_val = getattr(old_value, "model_SymbolReference", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_SymbolReference"):
                opp_val = getattr(value, "model_SymbolReference", None)
                if opp_val is None:
                    setattr(value, "model_SymbolReference", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_StringToStringMap(self):
        return self.__model_StringToStringMap

    @model_StringToStringMap.setter
    def model_StringToStringMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_StringToStringMap__model_StringToStringMap", None)
        self.__model_StringToStringMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Symbol2"):
                opp_val = getattr(old_value, "model_Symbol2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Symbol2"):
                opp_val = getattr(value, "model_Symbol2", None)
                if opp_val is None:
                    setattr(value, "model_Symbol2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_Primitive(ABC):

    def __init__(self, name: str, model_Primitive: "model_Symbol" = None, model_Primitive10: "model_Child" = None, model_Primitive29: "model_FigureContainer" = None, model_Primitive32: "model_Connection" = None, model_Primitive35: "model_Connection" = None, model_Primitive37: "model_StackContainer" = None):
        self.name = name
        self.model_Primitive = model_Primitive
        self.model_Primitive10 = model_Primitive10
        self.model_Primitive29 = model_Primitive29
        self.model_Primitive32 = model_Primitive32
        self.model_Primitive35 = model_Primitive35
        self.model_Primitive37 = model_Primitive37
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_Primitive32(self):
        return self.__model_Primitive32

    @model_Primitive32.setter
    def model_Primitive32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Primitive__model_Primitive32", None)
        self.__model_Primitive32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Connection31"):
                opp_val = getattr(old_value, "model_Connection31", None)
                if opp_val == self:
                    setattr(old_value, "model_Connection31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Connection31"):
                opp_val = getattr(value, "model_Connection31", None)
                setattr(value, "model_Connection31", self)

    @property
    def model_Primitive37(self):
        return self.__model_Primitive37

    @model_Primitive37.setter
    def model_Primitive37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Primitive__model_Primitive37", None)
        self.__model_Primitive37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_StackContainer"):
                opp_val = getattr(old_value, "model_StackContainer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_StackContainer"):
                opp_val = getattr(value, "model_StackContainer", None)
                if opp_val is None:
                    setattr(value, "model_StackContainer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Primitive35(self):
        return self.__model_Primitive35

    @model_Primitive35.setter
    def model_Primitive35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Primitive__model_Primitive35", None)
        self.__model_Primitive35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Connection34"):
                opp_val = getattr(old_value, "model_Connection34", None)
                if opp_val == self:
                    setattr(old_value, "model_Connection34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Connection34"):
                opp_val = getattr(value, "model_Connection34", None)
                setattr(value, "model_Connection34", self)

    @property
    def model_Primitive29(self):
        return self.__model_Primitive29

    @model_Primitive29.setter
    def model_Primitive29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Primitive__model_Primitive29", None)
        self.__model_Primitive29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_FigureContainer"):
                opp_val = getattr(old_value, "model_FigureContainer", None)
                if opp_val == self:
                    setattr(old_value, "model_FigureContainer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_FigureContainer"):
                opp_val = getattr(value, "model_FigureContainer", None)
                setattr(value, "model_FigureContainer", self)

    @property
    def model_Primitive(self):
        return self.__model_Primitive

    @model_Primitive.setter
    def model_Primitive(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Primitive__model_Primitive", None)
        self.__model_Primitive = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Symbol"):
                opp_val = getattr(old_value, "model_Symbol", None)
                if opp_val == self:
                    setattr(old_value, "model_Symbol", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Symbol"):
                opp_val = getattr(value, "model_Symbol", None)
                setattr(value, "model_Symbol", self)

    @property
    def model_Primitive10(self):
        return self.__model_Primitive10

    @model_Primitive10.setter
    def model_Primitive10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Primitive__model_Primitive10", None)
        self.__model_Primitive10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Child"):
                opp_val = getattr(old_value, "model_Child", None)
                if opp_val == self:
                    setattr(old_value, "model_Child", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Child"):
                opp_val = getattr(value, "model_Child", None)
                setattr(value, "model_Child", self)
