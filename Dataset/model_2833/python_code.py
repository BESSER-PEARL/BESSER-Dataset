from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class IconSize(Enum):
    Small = "Small"
    Medium = "Medium"
    Large = "Large"
    XLarge = "XLarge"
    XXL = "XXL"
    Custom = "Custom"
class LineStyle(Enum):
    Solid = "Solid"
    Dotted = "Dotted"
    Dashed = "Dashed"
class Rotation90(Enum):
    _0 = "_0"
    _90 = "_90"
    _180 = "_180"
    _270 = "_270"
class ShapeType(Enum):
    Ellipse = "Ellipse"
    Rectangle = "Rectangle"
    RoundedRectangle = "RoundedRectangle"
    RoundRectangle = "RoundRectangle"
    Diamond = "Diamond"
    Star = "Star"
    Parallelogram = "Parallelogram"
    Triangle = "Triangle"
    RightTriangle = "RightTriangle"
class Theme(Enum):
    Default = "Default"
    Clean = "Clean"
    Sketch = "Sketch"
class TextAlignment(Enum):
    Left = "Left"
    Center = "Center"
    Right = "Right"
class ChartType(Enum):
    Pie = "Pie"
    Line = "Line"
    Bar = "Bar"
    Column = "Column"
class BorderStyle(Enum):
    None = "None"
    Solid = "Solid"
    SolidRounded = "SolidRounded"
    DashedRounded = "DashedRounded"
class State(Enum):
    Normal = "Normal"
    Disabled = "Disabled"
    Selected = "Selected"
    Focused = "Focused"
class Position(Enum):
    Top = "Top"
    Bottom = "Bottom"
    Left = "Left"
    Right = "Right"
    TopLeft = "TopLeft"
    TopRight = "TopRight"
    BottomLeft = "BottomLeft"
    BottomRight = "BottomRight"
class ResizeMode(Enum):
    Both = "Both"
    Horizontal = "Horizontal"
    Vertical = "Vertical"
    None = "None"
class ButtonStyle(Enum):
    Round = "Round"
    PointRight = "PointRight"
    PointLeft = "PointLeft"
    Square = "Square"


############################################
# Definition of Classes
############################################

class ItemOverrides:

    pass
class model_overrides_WidgetContainerOverrides(ABC):

    pass
class model_overrides_Reference(ABC):

    def __init__(self, ref: str):
        self.ref = ref
        
    @property
    def ref(self) -> str:
        return self.__ref

    @ref.setter
    def ref(self, ref: str):
        self.__ref = ref

class overrides_model_EObject:

    pass
class overrides_Operation:

    pass
class model_overrides_Operation(ABC):

    pass
class model_overrides_StringToStringMap:

    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
        
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

class Reference:

    pass
class model_overrides_ItemOverrides(Reference):

    def __init__(self, text: str, link: str, noLink: bool):
        self.text = text
        self.link = link
        self.noLink = noLink
        
    @property
    def link(self) -> str:
        return self.__link

    @link.setter
    def link(self, link: str):
        self.__link = link

    @property
    def noLink(self) -> bool:
        return self.__noLink

    @noLink.setter
    def noLink(self, noLink: bool):
        self.__noLink = noLink

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class model_overrides_FontOverrides:

    def __init__(self, size: str, bold: str, italic: str, underline: str):
        self.size = size
        self.bold = bold
        self.italic = italic
        self.underline = underline
        
    @property
    def bold(self) -> str:
        return self.__bold

    @bold.setter
    def bold(self, bold: str):
        self.__bold = bold

    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

    @property
    def underline(self) -> str:
        return self.__underline

    @underline.setter
    def underline(self, underline: str):
        self.__underline = underline

    @property
    def italic(self) -> str:
        return self.__italic

    @italic.setter
    def italic(self, italic: str):
        self.__italic = italic

class Operation:

    pass
class model_overrides_Insert(Operation):

    def __init__(self, newIndex: int, model_overrides_Insert: "overrides_model_EObject" = None, Operation33: "model_overrides_WidgetContainerOverrides", Operation: "model_overrides_WidgetOverrides"):
        self.newIndex = newIndex
        self.model_overrides_Insert = model_overrides_Insert
        
    @property
    def newIndex(self) -> int:
        return self.__newIndex

    @newIndex.setter
    def newIndex(self, newIndex: int):
        self.__newIndex = newIndex

    @property
    def model_overrides_Insert(self):
        return self.__model_overrides_Insert

    @model_overrides_Insert.setter
    def model_overrides_Insert(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_overrides_Insert__model_overrides_Insert", None)
        self.__model_overrides_Insert = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "overrides_model_EObject"):
                opp_val = getattr(old_value, "overrides_model_EObject", None)
                if opp_val == self:
                    setattr(old_value, "overrides_model_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "overrides_model_EObject"):
                opp_val = getattr(value, "overrides_model_EObject", None)
                setattr(value, "overrides_model_EObject", self)

class FontOverrides:

    pass
class StringToStringMap:

    pass
class Storyboard:

    pass
class overrides_Reference:

    pass
class model_overrides_Delete(overrides_Operation, overrides_Reference):

    pass
class model_overrides_Move(overrides_Operation, overrides_Reference):

    def __init__(self, newIndex: int):
        self.newIndex = newIndex
        
    @property
    def newIndex(self) -> int:
        return self.__newIndex

    @newIndex.setter
    def newIndex(self, newIndex: int):
        self.__newIndex = newIndex

class overrides_WidgetContainerOverrides:

    pass
class model_overrides_WidgetOverrides(overrides_WidgetContainerOverrides, overrides_Reference):

    def __init__(self, x: str, y: str, width: str, height: str, text: str, noText: bool, link: str, noLink: bool, src: str, model_overrides_WidgetOverrides: set["StringToStringMap"] = None, model_overrides_WidgetOverrides26: "FontOverrides" = None, model_overrides_WidgetOverrides30: set["Operation"] = None, model_overrides_WidgetOverrides28: set["ItemOverrides"] = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.noText = noText
        self.link = link
        self.noLink = noLink
        self.src = src
        self.model_overrides_WidgetOverrides = model_overrides_WidgetOverrides if model_overrides_WidgetOverrides is not None else set()
        self.model_overrides_WidgetOverrides26 = model_overrides_WidgetOverrides26
        self.model_overrides_WidgetOverrides30 = model_overrides_WidgetOverrides30 if model_overrides_WidgetOverrides30 is not None else set()
        self.model_overrides_WidgetOverrides28 = model_overrides_WidgetOverrides28 if model_overrides_WidgetOverrides28 is not None else set()
        
    @property
    def x(self) -> str:
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x

    @property
    def y(self) -> str:
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y

    @property
    def noText(self) -> bool:
        return self.__noText

    @noText.setter
    def noText(self, noText: bool):
        self.__noText = noText

    @property
    def height(self) -> str:
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height

    @property
    def link(self) -> str:
        return self.__link

    @link.setter
    def link(self, link: str):
        self.__link = link

    @property
    def width(self) -> str:
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width

    @property
    def noLink(self) -> bool:
        return self.__noLink

    @noLink.setter
    def noLink(self, noLink: bool):
        self.__noLink = noLink

    @property
    def src(self) -> str:
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def model_overrides_WidgetOverrides26(self):
        return self.__model_overrides_WidgetOverrides26

    @model_overrides_WidgetOverrides26.setter
    def model_overrides_WidgetOverrides26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_overrides_WidgetOverrides__model_overrides_WidgetOverrides26", None)
        self.__model_overrides_WidgetOverrides26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FontOverrides"):
                opp_val = getattr(old_value, "FontOverrides", None)
                if opp_val == self:
                    setattr(old_value, "FontOverrides", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FontOverrides"):
                opp_val = getattr(value, "FontOverrides", None)
                setattr(value, "FontOverrides", self)

    @property
    def model_overrides_WidgetOverrides30(self):
        return self.__model_overrides_WidgetOverrides30

    @model_overrides_WidgetOverrides30.setter
    def model_overrides_WidgetOverrides30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_overrides_WidgetOverrides__model_overrides_WidgetOverrides30", None)
        self.__model_overrides_WidgetOverrides30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Operation"):
                    opp_val = getattr(item, "Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Operation"):
                    opp_val = getattr(item, "Operation", None)
                    
                    setattr(item, "Operation", self)
                    

    @property
    def model_overrides_WidgetOverrides28(self):
        return self.__model_overrides_WidgetOverrides28

    @model_overrides_WidgetOverrides28.setter
    def model_overrides_WidgetOverrides28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_overrides_WidgetOverrides__model_overrides_WidgetOverrides28", None)
        self.__model_overrides_WidgetOverrides28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ItemOverrides"):
                    opp_val = getattr(item, "ItemOverrides", None)
                    
                    if opp_val == self:
                        setattr(item, "ItemOverrides", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ItemOverrides"):
                    opp_val = getattr(item, "ItemOverrides", None)
                    
                    setattr(item, "ItemOverrides", self)
                    

    @property
    def model_overrides_WidgetOverrides(self):
        return self.__model_overrides_WidgetOverrides

    @model_overrides_WidgetOverrides.setter
    def model_overrides_WidgetOverrides(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_overrides_WidgetOverrides__model_overrides_WidgetOverrides", None)
        self.__model_overrides_WidgetOverrides = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StringToStringMap"):
                    opp_val = getattr(item, "StringToStringMap", None)
                    
                    if opp_val == self:
                        setattr(item, "StringToStringMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StringToStringMap"):
                    opp_val = getattr(item, "StringToStringMap", None)
                    
                    setattr(item, "StringToStringMap", self)
                    

class WidgetOverrides:

    pass
class WidgetContainerOverrides:

    pass
class model_overrides_Overrides(WidgetContainerOverrides):

    pass
class story_model_Screen:

    pass
class model_story_Panel:

    def __init__(self, id: str, x: int, y: int, model_story_Panel: "story_model_Screen" = None, model_story_Panel22: "Storyboard" = None):
        self.id = id
        self.x = x
        self.y = y
        self.model_story_Panel = model_story_Panel
        self.model_story_Panel22 = model_story_Panel22
        
    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x

    @property
    def model_story_Panel(self):
        return self.__model_story_Panel

    @model_story_Panel.setter
    def model_story_Panel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_story_Panel__model_story_Panel", None)
        self.__model_story_Panel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "story_model_Screen"):
                opp_val = getattr(old_value, "story_model_Screen", None)
                if opp_val == self:
                    setattr(old_value, "story_model_Screen", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "story_model_Screen"):
                opp_val = getattr(value, "story_model_Screen", None)
                setattr(value, "story_model_Screen", self)

    @property
    def model_story_Panel22(self):
        return self.__model_story_Panel22

    @model_story_Panel22.setter
    def model_story_Panel22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_story_Panel__model_story_Panel22", None)
        self.__model_story_Panel22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Storyboard"):
                opp_val = getattr(old_value, "Storyboard", None)
                if opp_val == self:
                    setattr(old_value, "Storyboard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Storyboard"):
                opp_val = getattr(value, "Storyboard", None)
                setattr(value, "Storyboard", self)

class model_story_Storyboard:

    pass
class model_NoteSupport(ABC):

    def __init__(self, note: str):
        self.note = note
        
    @property
    def note(self) -> str:
        return self.__note

    @note.setter
    def note(self, note: str):
        self.__note = note

class model_AnnotationSupport(ABC):

    pass
class Panel:

    pass
class model_Frame(Panel):

    pass
class model_VisibleSupport(ABC):

    def __init__(self, visible: bool):
        self.visible = visible
        
    @property
    def visible(self) -> bool:
        return self.__visible

    @visible.setter
    def visible(self, visible: bool):
        self.__visible = visible

class model_LineHeightSupport(ABC):

    def __init__(self, lineHeight: str):
        self.lineHeight = lineHeight
        
    @property
    def lineHeight(self) -> str:
        return self.__lineHeight

    @lineHeight.setter
    def lineHeight(self, lineHeight: str):
        self.__lineHeight = lineHeight

class model_FlipSupport(ABC):

    def __init__(self, hFlip: bool, vFlip: bool):
        self.hFlip = hFlip
        self.vFlip = vFlip
        
    @property
    def vFlip(self) -> bool:
        return self.__vFlip

    @vFlip.setter
    def vFlip(self, vFlip: bool):
        self.__vFlip = vFlip

    @property
    def hFlip(self) -> bool:
        return self.__hFlip

    @hFlip.setter
    def hFlip(self, hFlip: bool):
        self.__hFlip = hFlip

class model_SkinSupport(ABC):

    def __init__(self, skin: str):
        self.skin = skin
        
    @property
    def skin(self) -> str:
        return self.__skin

    @skin.setter
    def skin(self, skin: str):
        self.__skin = skin

class model_RotationSupport(ABC):

    def __init__(self, rotation: str):
        self.rotation = rotation
        
    @property
    def rotation(self) -> str:
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation: str):
        self.__rotation = rotation

class model_LineStyleSupport(ABC):

    def __init__(self, lineStyle: str):
        self.lineStyle = lineStyle
        
    @property
    def lineStyle(self) -> str:
        return self.__lineStyle

    @lineStyle.setter
    def lineStyle(self, lineStyle: str):
        self.__lineStyle = lineStyle

class model_ColorAlternativeSupport(ABC):

    def __init__(self, alternative: str):
        self.alternative = alternative
        
    @property
    def alternative(self) -> str:
        return self.__alternative

    @alternative.setter
    def alternative(self, alternative: str):
        self.__alternative = alternative

class model_NameSupport(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class model_LinkSupport(ABC):

    def __init__(self, link: str):
        self.link = link
        
    @property
    def link(self) -> str:
        return self.__link

    @link.setter
    def link(self, link: str):
        self.__link = link

class model_ItemSupport(ABC):

    pass
class model_ListSupport(ABC):

    def __init__(self, rowHeight: int, horizontalLines: bool):
        self.rowHeight = rowHeight
        self.horizontalLines = horizontalLines
        
    @property
    def rowHeight(self) -> int:
        return self.__rowHeight

    @rowHeight.setter
    def rowHeight(self, rowHeight: int):
        self.__rowHeight = rowHeight

    @property
    def horizontalLines(self) -> bool:
        return self.__horizontalLines

    @horizontalLines.setter
    def horizontalLines(self, horizontalLines: bool):
        self.__horizontalLines = horizontalLines

class model_BorderStyleSupport(ABC):

    def __init__(self, border: str):
        self.border = border
        
    @property
    def border(self) -> str:
        return self.__border

    @border.setter
    def border(self, border: str):
        self.__border = border

class model_ValueSupport(ABC):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class model_IconSupport(ABC):

    def __init__(self, icon: str, iconRotation: str):
        self.icon = icon
        self.iconRotation = iconRotation
        
    @property
    def iconRotation(self) -> str:
        return self.__iconRotation

    @iconRotation.setter
    def iconRotation(self, iconRotation: str):
        self.__iconRotation = iconRotation

    @property
    def icon(self) -> str:
        return self.__icon

    @icon.setter
    def icon(self, icon: str):
        self.__icon = icon

class model_StateSupport(ABC):

    def __init__(self, state: str):
        self.state = state
        
    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    def isValidState(self, state: str) -> bool:
        # TODO: Implement isValidState method
        pass

class model_BorderSupport(ABC):

    def __init__(self, border: bool):
        self.border = border
        
    @property
    def border(self) -> bool:
        return self.__border

    @border.setter
    def border(self, border: bool):
        self.__border = border

class model_BooleanSelectionSupport(ABC):

    def __init__(self, selected: bool):
        self.selected = selected
        
    @property
    def selected(self) -> bool:
        return self.__selected

    @selected.setter
    def selected(self, selected: bool):
        self.__selected = selected

class model_TextAlignmentSupport(ABC):

    def __init__(self, textAlignment: str):
        self.textAlignment = textAlignment
        
    @property
    def textAlignment(self) -> str:
        return self.__textAlignment

    @textAlignment.setter
    def textAlignment(self, textAlignment: str):
        self.__textAlignment = textAlignment

class AnnotationSupport:

    pass
class model_SelectionSupport(ABC):

    def __init__(self, selection: str):
        self.selection = selection
        
    @property
    def selection(self) -> str:
        return self.__selection

    @selection.setter
    def selection(self, selection: str):
        self.__selection = selection

    def doSelect(self):
        # TODO: Implement doSelect method
        pass

class model_ColorAlphaSupport(ABC):

    def __init__(self, alpha: int):
        self.alpha = alpha
        
    @property
    def alpha(self) -> int:
        return self.__alpha

    @alpha.setter
    def alpha(self, alpha: int):
        self.__alpha = alpha

class model_ColorBorderSupport(ABC):

    def __init__(self, borderColor: str):
        self.borderColor = borderColor
        
    @property
    def borderColor(self) -> str:
        return self.__borderColor

    @borderColor.setter
    def borderColor(self, borderColor: str):
        self.__borderColor = borderColor

class model_ColorBackgroundSupport(ABC):

    def __init__(self, background: str):
        self.background = background
        
    @property
    def background(self) -> str:
        return self.__background

    @background.setter
    def background(self, background: str):
        self.__background = background

class model_ColorForegroundSupport(ABC):

    def __init__(self, foreground: str):
        self.foreground = foreground
        
    @property
    def foreground(self) -> str:
        return self.__foreground

    @foreground.setter
    def foreground(self, foreground: str):
        self.__foreground = foreground

class model_FontSupport(ABC):

    pass
class FlipSupport:

    pass
class Overrides:

    pass
class model_Font:

    def __init__(self, size: str, bold: str, italic: str, underline: str, model_Font: "model_FontSupport" = None):
        self.size = size
        self.bold = bold
        self.italic = italic
        self.underline = underline
        self.model_Font = model_Font
        
    @property
    def underline(self) -> str:
        return self.__underline

    @underline.setter
    def underline(self, underline: str):
        self.__underline = underline

    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

    @property
    def italic(self) -> str:
        return self.__italic

    @italic.setter
    def italic(self, italic: str):
        self.__italic = italic

    @property
    def bold(self) -> str:
        return self.__bold

    @bold.setter
    def bold(self, bold: str):
        self.__bold = bold

    @property
    def model_Font(self):
        return self.__model_Font

    @model_Font.setter
    def model_Font(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Font__model_Font", None)
        self.__model_Font = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_FontSupport"):
                opp_val = getattr(old_value, "model_FontSupport", None)
                if opp_val == self:
                    setattr(old_value, "model_FontSupport", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_FontSupport"):
                opp_val = getattr(value, "model_FontSupport", None)
                setattr(value, "model_FontSupport", self)

class ColorAlternativeSupport:

    pass
class ItemSupport:

    pass
class model_TextLinksSupport(ItemSupport):

    pass
class LineStyleSupport:

    pass
class ValueSupport:

    pass
class model_VerticalScrollbarSupport(ValueSupport):

    def __init__(self, verticalScrollbar: bool):
        self.verticalScrollbar = verticalScrollbar
        
    @property
    def verticalScrollbar(self) -> bool:
        return self.__verticalScrollbar

    @verticalScrollbar.setter
    def verticalScrollbar(self, verticalScrollbar: bool):
        self.__verticalScrollbar = verticalScrollbar

class DoubleClickSupport:

    pass
class VerticalScrollbarSupport:

    pass
class ListSupport:

    pass
class BorderSupport:

    pass
class BorderStyleSupport:

    pass
class LineHeightSupport:

    pass
class SelectionSupport:

    pass
class ColorAlphaSupport:

    pass
class ColorBorderSupport:

    pass
class TextInputSupport:

    pass
class TextLinksSupport:

    pass
class RotationSupport:

    pass
class IconPositionSupport:

    pass
class ColorForegroundSupport:

    pass
class model_WidgetContainer(ABC):

    pass
class VisibleSupport:

    pass
class BooleanSelectionSupport:

    pass
class ClickSupport:

    pass
class SkinSupport:

    pass
class TextAlignmentSupport:

    pass
class LinkSupport:

    pass
class model_Item(ClickSupport, VisibleSupport, LinkSupport):

    def __init__(self, x: int, y: int, width: int, height: int, text: str, model_Item: "model_ItemSupport" = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.model_Item = model_Item
        
    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height

    @property
    def model_Item(self):
        return self.__model_Item

    @model_Item.setter
    def model_Item(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Item__model_Item", None)
        self.__model_Item = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ItemSupport"):
                opp_val = getattr(old_value, "model_ItemSupport", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ItemSupport"):
                opp_val = getattr(value, "model_ItemSupport", None)
                if opp_val is None:
                    setattr(value, "model_ItemSupport", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class IconSupport:

    pass
class model_IconPositionSupport(IconSupport):

    def __init__(self, iconPosition: str):
        self.iconPosition = iconPosition
        
    @property
    def iconPosition(self) -> str:
        return self.__iconPosition

    @iconPosition.setter
    def iconPosition(self, iconPosition: str):
        self.__iconPosition = iconPosition

class FontSupport:

    pass
class ColorBackgroundSupport:

    pass
class StateSupport:

    pass
class Widget:

    pass
class model_HLine(SkinSupport, Widget, LineStyleSupport, ColorForegroundSupport):

    pass
class model_Breadcrumbs(SkinSupport, Widget, FontSupport, ItemSupport):

    pass
class model_SVGImage(ColorAlphaSupport, Widget, FlipSupport, LinkSupport, RotationSupport, ColorForegroundSupport, ColorBackgroundSupport):

    def __init__(self, src: str):
        self.src = src
        
    @property
    def src(self) -> str:
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src

class model_Popup(Widget, ItemSupport, SelectionSupport):

    pass
class model_Group(ColorAlphaSupport, Widget, FontSupport, VerticalScrollbarSupport, ColorBackgroundSupport, SkinSupport):

    pass
class model_TextField(ColorBorderSupport, ColorAlphaSupport, Widget, FontSupport, TextInputSupport, ColorBackgroundSupport, SkinSupport, StateSupport, TextAlignmentSupport):

    pass
class model_Browser(ColorAlphaSupport, Widget, FontSupport, VerticalScrollbarSupport, ColorBackgroundSupport, SkinSupport):

    pass
class model_Circle(ColorAlphaSupport, Widget, BorderSupport, IconSupport, LinkSupport, FontSupport, ColorForegroundSupport, ColorBackgroundSupport, IconPositionSupport, LineStyleSupport, TextAlignmentSupport):

    pass
class model_Chart(SkinSupport, Widget):

    def __init__(self, chartType: str):
        self.chartType = chartType
        
    @property
    def chartType(self) -> str:
        return self.__chartType

    @chartType.setter
    def chartType(self, chartType: str):
        self.__chartType = chartType

class model_Image(Widget, FlipSupport, BorderSupport, LinkSupport, RotationSupport):

    def __init__(self, src: str, grayscale: bool):
        self.src = src
        self.grayscale = grayscale
        
    @property
    def grayscale(self) -> bool:
        return self.__grayscale

    @grayscale.setter
    def grayscale(self, grayscale: bool):
        self.__grayscale = grayscale

    @property
    def src(self) -> str:
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src

class model_DateField(ColorBorderSupport, ColorAlphaSupport, Widget, ColorBackgroundSupport, SkinSupport, StateSupport):

    pass
class model_Area(Widget):

    pass
class model_VButtonBar(Widget, ItemSupport, FontSupport, ColorBackgroundSupport, SkinSupport, TextAlignmentSupport, SelectionSupport):

    pass
class model_VLine(SkinSupport, Widget, LineStyleSupport, ColorForegroundSupport):

    pass
class model_Switch(BooleanSelectionSupport, Widget, LinkSupport, FontSupport, ColorBackgroundSupport, SkinSupport, StateSupport):

    pass
class model_Label(Widget, TextLinksSupport, LinkSupport, IconSupport, FontSupport, RotationSupport, ColorForegroundSupport, IconPositionSupport, StateSupport, TextAlignmentSupport):

    pass
class model_Shape(ColorAlphaSupport, Widget, LinkSupport, BorderSupport, IconSupport, FontSupport, RotationSupport, ColorForegroundSupport, ColorBackgroundSupport, SkinSupport, IconPositionSupport, LineStyleSupport, TextAlignmentSupport):

    def __init__(self, shapeType: str):
        self.shapeType = shapeType
        
    @property
    def shapeType(self) -> str:
        return self.__shapeType

    @shapeType.setter
    def shapeType(self, shapeType: str):
        self.__shapeType = shapeType

    def isRotatable(self) -> bool:
        # TODO: Implement isRotatable method
        pass

class model_Tree(ColorAlphaSupport, Widget, ItemSupport, BorderSupport, FontSupport, VerticalScrollbarSupport, ColorBackgroundSupport, SelectionSupport):

    pass
class model_ColorPicker(SkinSupport, Widget, ColorBackgroundSupport):

    pass
class model_TextArea(ColorAlphaSupport, ColorBorderSupport, Widget, TextLinksSupport, LineHeightSupport, FontSupport, VerticalScrollbarSupport, ColorBackgroundSupport, SkinSupport, StateSupport, TextAlignmentSupport):

    pass
class model_ProgressBar(SkinSupport, Widget, ValueSupport, ColorBackgroundSupport):

    pass
class model_Window(ColorAlphaSupport, Widget, VerticalScrollbarSupport, ColorBackgroundSupport, SkinSupport):

    def __init__(self, closeButton: bool, minimizeButton: bool, maximizeButton: bool):
        self.closeButton = closeButton
        self.minimizeButton = minimizeButton
        self.maximizeButton = maximizeButton
        
    @property
    def maximizeButton(self) -> bool:
        return self.__maximizeButton

    @maximizeButton.setter
    def maximizeButton(self, maximizeButton: bool):
        self.__maximizeButton = maximizeButton

    @property
    def closeButton(self) -> bool:
        return self.__closeButton

    @closeButton.setter
    def closeButton(self, closeButton: bool):
        self.__closeButton = closeButton

    @property
    def minimizeButton(self) -> bool:
        return self.__minimizeButton

    @minimizeButton.setter
    def minimizeButton(self, minimizeButton: bool):
        self.__minimizeButton = minimizeButton

class model_Map(SkinSupport, Widget):

    pass
class model_Arrow(Widget, AnnotationSupport, LineStyleSupport, ColorForegroundSupport):

    def __init__(self, left: bool, right: bool, direction: str):
        self.left = left
        self.right = right
        self.direction = direction
        
    @property
    def right(self) -> bool:
        return self.__right

    @right.setter
    def right(self, right: bool):
        self.__right = right

    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def left(self) -> bool:
        return self.__left

    @left.setter
    def left(self, left: bool):
        self.__left = left

class model_VScrollbar(SkinSupport, Widget, ValueSupport):

    pass
class model_SearchField(ColorBorderSupport, Widget, LinkSupport, FontSupport, SkinSupport, StateSupport):

    pass
class model_Spinner(ColorAlphaSupport, ColorBorderSupport, Widget, FontSupport, ColorBackgroundSupport, SkinSupport, StateSupport):

    pass
class model_Combo(ColorBorderSupport, ColorAlphaSupport, Widget, LinkSupport, FontSupport, ColorBackgroundSupport, SkinSupport, StateSupport, SelectionSupport):

    pass
class model_Table(ColorAlphaSupport, Widget, TextLinksSupport, BorderSupport, FontSupport, VerticalScrollbarSupport, TextInputSupport, ColorBackgroundSupport, DoubleClickSupport, ClickSupport, ColorAlternativeSupport, TextAlignmentSupport, ListSupport, SelectionSupport):

    def __init__(self, verticalLines: bool, header: bool):
        self.verticalLines = verticalLines
        self.header = header
        
    @property
    def verticalLines(self) -> bool:
        return self.__verticalLines

    @verticalLines.setter
    def verticalLines(self, verticalLines: bool):
        self.__verticalLines = verticalLines

    @property
    def header(self) -> bool:
        return self.__header

    @header.setter
    def header(self, header: bool):
        self.__header = header

class model_Checkbox(Widget, BooleanSelectionSupport, LinkSupport, FontSupport, SkinSupport, StateSupport):

    pass
class model_Panel(ColorAlphaSupport, Widget, LinkSupport, VerticalScrollbarSupport, ColorForegroundSupport, ColorBackgroundSupport, SkinSupport, BorderStyleSupport):

    pass
class model_ButtonBar(Widget, ItemSupport, FontSupport, ColorBackgroundSupport, SkinSupport, SelectionSupport):

    pass
class model_HScrollbar(SkinSupport, Widget, ValueSupport):

    pass
class model_Callout(ColorAlphaSupport, Widget, LinkSupport, FontSupport, ColorBackgroundSupport, SkinSupport, AnnotationSupport):

    pass
class model_Tabs(Widget, ItemSupport, FontSupport, SkinSupport, SelectionSupport):

    pass
class model_ScratchOut(ColorAlphaSupport, Widget, ColorForegroundSupport, SkinSupport, AnnotationSupport):

    pass
class model_CrossOut(ColorAlphaSupport, Widget, ColorForegroundSupport, SkinSupport, AnnotationSupport):

    pass
class model_CoverFlow(SkinSupport, Widget):

    pass
class model_List(ColorAlphaSupport, Widget, ItemSupport, BorderSupport, FontSupport, VerticalScrollbarSupport, ColorBackgroundSupport, ColorAlternativeSupport, ListSupport, SelectionSupport):

    def __init__(self, header: bool):
        self.header = header
        
    @property
    def header(self) -> bool:
        return self.__header

    @header.setter
    def header(self, header: bool):
        self.__header = header

class model_Rectangle(ColorAlphaSupport, Widget, LinkSupport, IconSupport, FontSupport, ColorForegroundSupport, ColorBackgroundSupport, IconPositionSupport, TextAlignmentSupport, BorderStyleSupport):

    pass
class model_CurlyBrace(Widget, TextLinksSupport, FontSupport, ColorForegroundSupport, SkinSupport, AnnotationSupport):

    def __init__(self, position: str):
        self.position = position
        
    @property
    def position(self) -> str:
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position

class model_TabbedPane(ColorAlphaSupport, Widget, ItemSupport, FontSupport, VerticalScrollbarSupport, ColorBackgroundSupport, SkinSupport, SelectionSupport):

    def __init__(self, position: str):
        self.position = position
        
    @property
    def position(self) -> str:
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position

class model_HSplitter(SkinSupport, Widget):

    pass
class model_LinkBar(Widget, ItemSupport, FontSupport, SkinSupport, SelectionSupport):

    pass
class model_Note(ColorAlphaSupport, Widget, TextLinksSupport, LinkSupport, FontSupport, ColorBackgroundSupport, SkinSupport, AnnotationSupport, TextAlignmentSupport):

    pass
class model_RadioButton(BooleanSelectionSupport, Widget, LinkSupport, FontSupport, SkinSupport, StateSupport):

    pass
class model_HSlider(Widget, ColorBackgroundSupport, SkinSupport, ValueSupport, StateSupport):

    pass
class model_Placeholder(SkinSupport, Widget, LinkSupport):

    pass
class model_Tooltip(Widget, TextLinksSupport, FontSupport, ColorBackgroundSupport, SkinSupport, TextAlignmentSupport):

    def __init__(self, position: str):
        self.position = position
        
    @property
    def position(self) -> str:
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position

class model_Hotspot(Widget, LinkSupport):

    pass
class model_VideoPlayer(SkinSupport, Widget):

    pass
class model_Icon(IconSupport, Widget, ColorForegroundSupport, LinkSupport):

    pass
class model_VSlider(Widget, ColorBackgroundSupport, SkinSupport, ValueSupport, StateSupport):

    pass
class model_Link(Widget, LinkSupport, FontSupport, SkinSupport, StateSupport):

    pass
class model_Master(Widget, LinkSupport):

    def __init__(self, dimmed: bool, model_Master13: "Overrides" = None, model_Master15: "model_WidgetContainer" = None, model_Master: "model_WidgetContainer" = None):
        self.dimmed = dimmed
        self.model_Master13 = model_Master13
        self.model_Master15 = model_Master15
        self.model_Master = model_Master
        
    @property
    def dimmed(self) -> bool:
        return self.__dimmed

    @dimmed.setter
    def dimmed(self, dimmed: bool):
        self.__dimmed = dimmed

    @property
    def model_Master(self):
        return self.__model_Master

    @model_Master.setter
    def model_Master(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Master__model_Master", None)
        self.__model_Master = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_WidgetContainer"):
                opp_val = getattr(old_value, "model_WidgetContainer", None)
                if opp_val == self:
                    setattr(old_value, "model_WidgetContainer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_WidgetContainer"):
                opp_val = getattr(value, "model_WidgetContainer", None)
                setattr(value, "model_WidgetContainer", self)

    @property
    def model_Master13(self):
        return self.__model_Master13

    @model_Master13.setter
    def model_Master13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Master__model_Master13", None)
        self.__model_Master13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Overrides"):
                opp_val = getattr(old_value, "Overrides", None)
                if opp_val == self:
                    setattr(old_value, "Overrides", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Overrides"):
                opp_val = getattr(value, "Overrides", None)
                setattr(value, "Overrides", self)

    @property
    def model_Master15(self):
        return self.__model_Master15

    @model_Master15.setter
    def model_Master15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Master__model_Master15", None)
        self.__model_Master15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_WidgetContainer16"):
                opp_val = getattr(old_value, "model_WidgetContainer16", None)
                if opp_val == self:
                    setattr(old_value, "model_WidgetContainer16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_WidgetContainer16"):
                opp_val = getattr(value, "model_WidgetContainer16", None)
                setattr(value, "model_WidgetContainer16", self)

class model_Text(Widget, TextLinksSupport, LinkSupport, LineHeightSupport, FontSupport, ColorForegroundSupport, TextAlignmentSupport):

    def __init__(self, dummyText: bool):
        self.dummyText = dummyText
        
    @property
    def dummyText(self) -> bool:
        return self.__dummyText

    @dummyText.setter
    def dummyText(self, dummyText: bool):
        self.__dummyText = dummyText

class model_Alert(Widget, ItemSupport, IconSupport, FontSupport, SkinSupport):

    pass
class model_Menu(Widget, ItemSupport, IconSupport, SkinSupport, SelectionSupport):

    pass
class model_Accordion(Widget, ItemSupport, FontSupport, VerticalScrollbarSupport, SelectionSupport):

    pass
class model_VSplitter(SkinSupport, Widget):

    pass
class model_Button(Widget, LinkSupport, IconSupport, FontSupport, ColorBackgroundSupport, SkinSupport, ClickSupport, StateSupport, TextAlignmentSupport):

    def __init__(self, style: str):
        self.style = style
        
    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

class model_WidgetDescriptor:

    def __init__(self, typeName: str, resizeMode: str, textEditable: bool, textWrappable: bool, textLines: int, textCentered: bool, model_WidgetDescriptor: "model_Widget" = None):
        self.typeName = typeName
        self.resizeMode = resizeMode
        self.textEditable = textEditable
        self.textWrappable = textWrappable
        self.textLines = textLines
        self.textCentered = textCentered
        self.model_WidgetDescriptor = model_WidgetDescriptor
        
    @property
    def typeName(self) -> str:
        return self.__typeName

    @typeName.setter
    def typeName(self, typeName: str):
        self.__typeName = typeName

    @property
    def resizeMode(self) -> str:
        return self.__resizeMode

    @resizeMode.setter
    def resizeMode(self, resizeMode: str):
        self.__resizeMode = resizeMode

    @property
    def textWrappable(self) -> bool:
        return self.__textWrappable

    @textWrappable.setter
    def textWrappable(self, textWrappable: bool):
        self.__textWrappable = textWrappable

    @property
    def textLines(self) -> int:
        return self.__textLines

    @textLines.setter
    def textLines(self, textLines: int):
        self.__textLines = textLines

    @property
    def textCentered(self) -> bool:
        return self.__textCentered

    @textCentered.setter
    def textCentered(self, textCentered: bool):
        self.__textCentered = textCentered

    @property
    def textEditable(self) -> bool:
        return self.__textEditable

    @textEditable.setter
    def textEditable(self, textEditable: bool):
        self.__textEditable = textEditable

    @property
    def model_WidgetDescriptor(self):
        return self.__model_WidgetDescriptor

    @model_WidgetDescriptor.setter
    def model_WidgetDescriptor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_WidgetDescriptor__model_WidgetDescriptor", None)
        self.__model_WidgetDescriptor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Widget"):
                opp_val = getattr(old_value, "model_Widget", None)
                if opp_val == self:
                    setattr(old_value, "model_Widget", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Widget"):
                opp_val = getattr(value, "model_Widget", None)
                setattr(value, "model_Widget", self)

class model_RulerGuide:

    def __init__(self, position: int, model_RulerGuide: "model_ScreenRuler" = None):
        self.position = position
        self.model_RulerGuide = model_RulerGuide
        
    @property
    def position(self) -> int:
        return self.__position

    @position.setter
    def position(self, position: int):
        self.__position = position

    @property
    def model_RulerGuide(self):
        return self.__model_RulerGuide

    @model_RulerGuide.setter
    def model_RulerGuide(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_RulerGuide__model_RulerGuide", None)
        self.__model_RulerGuide = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ScreenRuler7"):
                opp_val = getattr(old_value, "model_ScreenRuler7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ScreenRuler7"):
                opp_val = getattr(value, "model_ScreenRuler7", None)
                if opp_val is None:
                    setattr(value, "model_ScreenRuler7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_ScreenFont:

    def __init__(self, name: str, size: str, bold: bool, italic: bool, available: str, model_ScreenFont: "model_Screen" = None):
        self.name = name
        self.size = size
        self.bold = bold
        self.italic = italic
        self.available = available
        self.model_ScreenFont = model_ScreenFont
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def italic(self) -> bool:
        return self.__italic

    @italic.setter
    def italic(self, italic: bool):
        self.__italic = italic

    @property
    def bold(self) -> bool:
        return self.__bold

    @bold.setter
    def bold(self, bold: bool):
        self.__bold = bold

    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

    @property
    def available(self) -> str:
        return self.__available

    @available.setter
    def available(self, available: str):
        self.__available = available

    @property
    def model_ScreenFont(self):
        return self.__model_ScreenFont

    @model_ScreenFont.setter
    def model_ScreenFont(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ScreenFont__model_ScreenFont", None)
        self.__model_ScreenFont = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Screen5"):
                opp_val = getattr(old_value, "model_Screen5", None)
                if opp_val == self:
                    setattr(old_value, "model_Screen5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Screen5"):
                opp_val = getattr(value, "model_Screen5", None)
                setattr(value, "model_Screen5", self)

class model_ScreenRuler:

    pass
class NameSupport:

    pass
class model_TextInputSupport(NameSupport):

    def __init__(self):
        
    def doEnter(self):
        # TODO: Implement doEnter method
        pass

class model_DoubleClickSupport(NameSupport):

    def __init__(self):
        
    def doDoubleClick(self):
        # TODO: Implement doDoubleClick method
        pass

class model_ClickSupport(NameSupport):

    def __init__(self):
        
    def doClick(self):
        # TODO: Implement doClick method
        pass

class NoteSupport:

    pass
class model_Widget(NameSupport, NoteSupport, VisibleSupport):

    def __init__(self, x: int, y: int, width: int, height: int, text: str, locked: bool, measuredWidth: int, measuredHeight: int, customId: str, customData: str, annotation: bool, layoutParams: str, id: str, model_Widget: "model_WidgetDescriptor" = None, widgets: "model_WidgetContainer" = None, Widget: "model_WidgetContainer" = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.locked = locked
        self.measuredWidth = measuredWidth
        self.measuredHeight = measuredHeight
        self.customId = customId
        self.customData = customData
        self.annotation = annotation
        self.layoutParams = layoutParams
        self.id = id
        self.model_Widget = model_Widget
        self.widgets = widgets
        self.Widget = Widget
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def layoutParams(self) -> str:
        return self.__layoutParams

    @layoutParams.setter
    def layoutParams(self, layoutParams: str):
        self.__layoutParams = layoutParams

    @property
    def customId(self) -> str:
        return self.__customId

    @customId.setter
    def customId(self, customId: str):
        self.__customId = customId

    @property
    def measuredWidth(self) -> int:
        return self.__measuredWidth

    @measuredWidth.setter
    def measuredWidth(self, measuredWidth: int):
        self.__measuredWidth = measuredWidth

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x

    @property
    def annotation(self) -> bool:
        return self.__annotation

    @annotation.setter
    def annotation(self, annotation: bool):
        self.__annotation = annotation

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height

    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width

    @property
    def customData(self) -> str:
        return self.__customData

    @customData.setter
    def customData(self, customData: str):
        self.__customData = customData

    @property
    def locked(self) -> bool:
        return self.__locked

    @locked.setter
    def locked(self, locked: bool):
        self.__locked = locked

    @property
    def measuredHeight(self) -> int:
        return self.__measuredHeight

    @measuredHeight.setter
    def measuredHeight(self, measuredHeight: int):
        self.__measuredHeight = measuredHeight

    @property
    def widgets(self):
        return self.__widgets

    @widgets.setter
    def widgets(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Widget__widgets", None)
        self.__widgets = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WidgetContainer"):
                opp_val = getattr(old_value, "WidgetContainer", None)
                if opp_val == self:
                    setattr(old_value, "WidgetContainer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WidgetContainer"):
                opp_val = getattr(value, "WidgetContainer", None)
                setattr(value, "WidgetContainer", self)

    @property
    def model_Widget(self):
        return self.__model_Widget

    @model_Widget.setter
    def model_Widget(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Widget__model_Widget", None)
        self.__model_Widget = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_WidgetDescriptor"):
                opp_val = getattr(old_value, "model_WidgetDescriptor", None)
                if opp_val == self:
                    setattr(old_value, "model_WidgetDescriptor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_WidgetDescriptor"):
                opp_val = getattr(value, "model_WidgetDescriptor", None)
                setattr(value, "model_WidgetDescriptor", self)

    @property
    def Widget(self):
        return self.__Widget

    @Widget.setter
    def Widget(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Widget__Widget", None)
        self.__Widget = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "container"):
                opp_val = getattr(old_value, "container", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "container"):
                opp_val = getattr(value, "container", None)
                if opp_val is None:
                    setattr(value, "container", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class WidgetContainer:

    pass
class model_WidgetGroup(Widget, WidgetContainer, NameSupport, LinkSupport):

    pass
class model_Screen(WidgetContainer, NameSupport, NoteSupport):

    def __init__(self, theme: str, minVersion: str, model_Screen: "model_ScreenRuler" = None, model_Screen2: "model_ScreenRuler" = None, model_Screen5: "model_ScreenFont" = None):
        self.theme = theme
        self.minVersion = minVersion
        self.model_Screen = model_Screen
        self.model_Screen2 = model_Screen2
        self.model_Screen5 = model_Screen5
        
    @property
    def theme(self) -> str:
        return self.__theme

    @theme.setter
    def theme(self, theme: str):
        self.__theme = theme

    @property
    def minVersion(self) -> str:
        return self.__minVersion

    @minVersion.setter
    def minVersion(self, minVersion: str):
        self.__minVersion = minVersion

    @property
    def model_Screen2(self):
        return self.__model_Screen2

    @model_Screen2.setter
    def model_Screen2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Screen__model_Screen2", None)
        self.__model_Screen2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ScreenRuler3"):
                opp_val = getattr(old_value, "model_ScreenRuler3", None)
                if opp_val == self:
                    setattr(old_value, "model_ScreenRuler3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ScreenRuler3"):
                opp_val = getattr(value, "model_ScreenRuler3", None)
                setattr(value, "model_ScreenRuler3", self)

    @property
    def model_Screen5(self):
        return self.__model_Screen5

    @model_Screen5.setter
    def model_Screen5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Screen__model_Screen5", None)
        self.__model_Screen5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ScreenFont"):
                opp_val = getattr(old_value, "model_ScreenFont", None)
                if opp_val == self:
                    setattr(old_value, "model_ScreenFont", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ScreenFont"):
                opp_val = getattr(value, "model_ScreenFont", None)
                setattr(value, "model_ScreenFont", self)

    @property
    def model_Screen(self):
        return self.__model_Screen

    @model_Screen.setter
    def model_Screen(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Screen__model_Screen", None)
        self.__model_Screen = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ScreenRuler"):
                opp_val = getattr(old_value, "model_ScreenRuler", None)
                if opp_val == self:
                    setattr(old_value, "model_ScreenRuler", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ScreenRuler"):
                opp_val = getattr(value, "model_ScreenRuler", None)
                setattr(value, "model_ScreenRuler", self)
