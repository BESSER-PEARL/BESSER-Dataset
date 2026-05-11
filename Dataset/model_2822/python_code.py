from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

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
class ButtonStyle(Enum):
    PointLeft = "PointLeft"
    Square = "Square"
    Round = "Round"
    PointRight = "PointRight"
class ChartType(Enum):
    Pie = "Pie"
    Line = "Line"
    Bar = "Bar"
    Column = "Column"
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
    None_ = "None_"
class IconSize(Enum):
    Small = "Small"
    Medium = "Medium"
    Large = "Large"
    XLarge = "XLarge"
    XXL = "XXL"
    Custom = "Custom"
class Theme(Enum):
    Default = "Default"
    Clean = "Clean"
    Sketch = "Sketch"
class State(Enum):
    Normal = "Normal"
    Disabled = "Disabled"
    Selected = "Selected"
    Focused = "Focused"
class Rotation90(Enum):
    _0 = "_0"
    _90 = "_90"
    _180 = "_180"
    _270 = "_270"
class BorderStyle(Enum):
    None_ = "None_"
    Solid = "Solid"
    SolidRounded = "SolidRounded"
    DashedRounded = "DashedRounded"
class TextAlignment(Enum):
    Left = "Left"
    Center = "Center"
    Right = "Right"
class LineStyle(Enum):
    Solid = "Solid"
    Dotted = "Dotted"
    Dashed = "Dashed"


############################################
# Definition of Classes
############################################

class model_overrides_WidgetContainerOverrides(ABC):

    pass
class model_overrides_Reference(ABC):

    def __init__(self, ref: str):
        self.ref = ref
        
        pass
    @property
    def ref(self):
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
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


class Storyboard:

    pass
class Reference:

    pass
class model_overrides_ItemOverrides(Reference):

    def __init__(self, noLink: bool, text: str, link: str):
        self.noLink = noLink
        self.text = text
        self.link = link
        
        pass
    @property
    def link(self):
        return self.__link

    @link.setter
    def link(self, link: str):
        self.__link = link


    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def noLink(self):
        return self.__noLink

    @noLink.setter
    def noLink(self, noLink: bool):
        self.__noLink = noLink


class model_overrides_FontOverrides:

    def __init__(self, size: str, bold: str, italic: str, underline: str):
        self.size = size
        self.bold = bold
        self.italic = italic
        self.underline = underline
        
        pass
    @property
    def italic(self):
        return self.__italic

    @italic.setter
    def italic(self, italic: str):
        self.__italic = italic


    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size


    @property
    def bold(self):
        return self.__bold

    @bold.setter
    def bold(self, bold: str):
        self.__bold = bold


    @property
    def underline(self):
        return self.__underline

    @underline.setter
    def underline(self, underline: str):
        self.__underline = underline


class Operation:

    pass
class model_overrides_Insert(Operation):

    def __init__(self, newIndex: int, model_overrides_Insert: "overrides_model_EObject" = None, Operation: "model_overrides_WidgetOverrides" = None, Operation33: "model_overrides_WidgetContainerOverrides" = None):
        self.newIndex = newIndex
        self.model_overrides_Insert = model_overrides_Insert
        
        pass
    @property
    def newIndex(self):
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

class ItemOverrides:

    pass
class FontOverrides:

    pass
class StringToStringMap:

    pass
class overrides_Reference:

    pass
class model_overrides_Delete(overrides_Operation, overrides_Reference):

    pass
class model_overrides_Move(overrides_Operation, overrides_Reference):

    def __init__(self, newIndex: int):
        self.newIndex = newIndex
        
        pass
    @property
    def newIndex(self):
        return self.__newIndex

    @newIndex.setter
    def newIndex(self, newIndex: int):
        self.__newIndex = newIndex


class overrides_WidgetContainerOverrides:

    pass
class model_overrides_WidgetOverrides(overrides_WidgetContainerOverrides, overrides_Reference):

    def __init__(self, x: str, y: str, width: str, height: str, text: str, noText: bool, link: str, noLink: bool, src: str, model_overrides_WidgetOverrides30: set["Operation"] = None, model_overrides_WidgetOverrides: set["StringToStringMap"] = None, model_overrides_WidgetOverrides26: "FontOverrides" = None, model_overrides_WidgetOverrides28: set["ItemOverrides"] = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.noText = noText
        self.link = link
        self.noLink = noLink
        self.src = src
        self.model_overrides_WidgetOverrides30 = model_overrides_WidgetOverrides30 if model_overrides_WidgetOverrides30 is not None else set()
        self.model_overrides_WidgetOverrides = model_overrides_WidgetOverrides if model_overrides_WidgetOverrides is not None else set()
        self.model_overrides_WidgetOverrides26 = model_overrides_WidgetOverrides26
        self.model_overrides_WidgetOverrides28 = model_overrides_WidgetOverrides28 if model_overrides_WidgetOverrides28 is not None else set()
        
        pass
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height


    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x


    @property
    def src(self):
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src


    @property
    def link(self):
        return self.__link

    @link.setter
    def link(self, link: str):
        self.__link = link


    @property
    def noText(self):
        return self.__noText

    @noText.setter
    def noText(self, noText: bool):
        self.__noText = noText


    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: str):
        self.__width = width


    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def noLink(self):
        return self.__noLink

    @noLink.setter
    def noLink(self, noLink: bool):
        self.__noLink = noLink


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
        
        pass
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x


    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


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

class Panel:

    pass
class model_story_Storyboard:

    pass
class model_NoteSupport(ABC):

    def __init__(self, note: str):
        self.note = note
        
        pass
    @property
    def note(self):
        return self.__note

    @note.setter
    def note(self, note: str):
        self.__note = note


class model_AnnotationSupport(ABC):

    pass
class model_LineHeightSupport(ABC):

    def __init__(self, lineHeight: str):
        self.lineHeight = lineHeight
        
        pass
    @property
    def lineHeight(self):
        return self.__lineHeight

    @lineHeight.setter
    def lineHeight(self, lineHeight: str):
        self.__lineHeight = lineHeight


class model_SkinSupport(ABC):

    def __init__(self, skin: str):
        self.skin = skin
        
        pass
    @property
    def skin(self):
        return self.__skin

    @skin.setter
    def skin(self, skin: str):
        self.__skin = skin


class model_FlipSupport(ABC):

    def __init__(self, hFlip: bool, vFlip: bool):
        self.hFlip = hFlip
        self.vFlip = vFlip
        
        pass
    @property
    def vFlip(self):
        return self.__vFlip

    @vFlip.setter
    def vFlip(self, vFlip: bool):
        self.__vFlip = vFlip


    @property
    def hFlip(self):
        return self.__hFlip

    @hFlip.setter
    def hFlip(self, hFlip: bool):
        self.__hFlip = hFlip


class model_RotationSupport(ABC):

    def __init__(self, rotation: str):
        self.rotation = rotation
        
        pass
    @property
    def rotation(self):
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation: str):
        self.__rotation = rotation


class model_LineStyleSupport(ABC):

    def __init__(self, lineStyle: str):
        self.lineStyle = lineStyle
        
        pass
    @property
    def lineStyle(self):
        return self.__lineStyle

    @lineStyle.setter
    def lineStyle(self, lineStyle: str):
        self.__lineStyle = lineStyle


class model_ColorAlternativeSupport(ABC):

    def __init__(self, alternative: str):
        self.alternative = alternative
        
        pass
    @property
    def alternative(self):
        return self.__alternative

    @alternative.setter
    def alternative(self, alternative: str):
        self.__alternative = alternative


class model_NameSupport(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class model_LinkSupport(ABC):

    def __init__(self, link: str):
        self.link = link
        
        pass
    @property
    def link(self):
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
        
        pass
    @property
    def horizontalLines(self):
        return self.__horizontalLines

    @horizontalLines.setter
    def horizontalLines(self, horizontalLines: bool):
        self.__horizontalLines = horizontalLines


    @property
    def rowHeight(self):
        return self.__rowHeight

    @rowHeight.setter
    def rowHeight(self, rowHeight: int):
        self.__rowHeight = rowHeight


class model_BorderStyleSupport(ABC):

    def __init__(self, border: str):
        self.border = border
        
        pass
    @property
    def border(self):
        return self.__border

    @border.setter
    def border(self, border: str):
        self.__border = border


class model_ValueSupport(ABC):

    def __init__(self, value: int):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


class model_IconSupport(ABC):

    def __init__(self, icon: str, iconRotation: str):
        self.icon = icon
        self.iconRotation = iconRotation
        
        pass
    @property
    def icon(self):
        return self.__icon

    @icon.setter
    def icon(self, icon: str):
        self.__icon = icon


    @property
    def iconRotation(self):
        return self.__iconRotation

    @iconRotation.setter
    def iconRotation(self, iconRotation: str):
        self.__iconRotation = iconRotation


class model_StateSupport(ABC):

    def __init__(self, state: str):
        self.state = state
        
        pass
    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state


    def isValidState(self, model_state) :
        # TODO: Implement isValidState method
        pass

class model_BorderSupport(ABC):

    def __init__(self, border: bool):
        self.border = border
        
        pass
    @property
    def border(self):
        return self.__border

    @border.setter
    def border(self, border: bool):
        self.__border = border


class AnnotationSupport:

    pass
class model_BooleanSelectionSupport(ABC):

    def __init__(self, selected: bool):
        self.selected = selected
        
        pass
    @property
    def selected(self):
        return self.__selected

    @selected.setter
    def selected(self, selected: bool):
        self.__selected = selected


class model_TextAlignmentSupport(ABC):

    def __init__(self, textAlignment: str):
        self.textAlignment = textAlignment
        
        pass
    @property
    def textAlignment(self):
        return self.__textAlignment

    @textAlignment.setter
    def textAlignment(self, textAlignment: str):
        self.__textAlignment = textAlignment


class model_SelectionSupport(ABC):

    def __init__(self, selection: str):
        self.selection = selection
        
        pass
    @property
    def selection(self):
        return self.__selection

    @selection.setter
    def selection(self, selection: str):
        self.__selection = selection


class model_ColorAlphaSupport(ABC):

    def __init__(self, alpha: int):
        self.alpha = alpha
        
        pass
    @property
    def alpha(self):
        return self.__alpha

    @alpha.setter
    def alpha(self, alpha: int):
        self.__alpha = alpha


class model_ColorBorderSupport(ABC):

    def __init__(self, borderColor: str):
        self.borderColor = borderColor
        
        pass
    @property
    def borderColor(self):
        return self.__borderColor

    @borderColor.setter
    def borderColor(self, borderColor: str):
        self.__borderColor = borderColor


class model_ColorBackgroundSupport(ABC):

    def __init__(self, background: str):
        self.background = background
        
        pass
    @property
    def background(self):
        return self.__background

    @background.setter
    def background(self, background: str):
        self.__background = background


class model_ColorForegroundSupport(ABC):

    def __init__(self, foreground: str):
        self.foreground = foreground
        
        pass
    @property
    def foreground(self):
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
class NameSupport:

    pass
class model_Font:

    def __init__(self, size: str, bold: str, italic: str, underline: str, model_Font: "model_FontSupport" = None):
        self.size = size
        self.bold = bold
        self.italic = italic
        self.underline = underline
        self.model_Font = model_Font
        
        pass
    @property
    def bold(self):
        return self.__bold

    @bold.setter
    def bold(self, bold: str):
        self.__bold = bold


    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size


    @property
    def italic(self):
        return self.__italic

    @italic.setter
    def italic(self, italic: str):
        self.__italic = italic


    @property
    def underline(self):
        return self.__underline

    @underline.setter
    def underline(self, underline: str):
        self.__underline = underline


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

class LineStyleSupport:

    pass
class ValueSupport:

    pass
class model_VerticalScrollbarSupport(ValueSupport):

    def __init__(self, verticalScrollbar: bool):
        self.verticalScrollbar = verticalScrollbar
        
        pass
    @property
    def verticalScrollbar(self):
        return self.__verticalScrollbar

    @verticalScrollbar.setter
    def verticalScrollbar(self, verticalScrollbar: bool):
        self.__verticalScrollbar = verticalScrollbar


class LineHeightSupport:

    pass
class ColorAlternativeSupport:

    pass
class ItemSupport:

    pass
class model_TextLinksSupport(ItemSupport):

    pass
class ListSupport:

    pass
class BorderSupport:

    pass
class SelectionSupport:

    pass
class BorderStyleSupport:

    pass
class ColorAlphaSupport:

    pass
class ColorBorderSupport:

    pass
class BooleanSelectionSupport:

    pass
class VerticalScrollbarSupport:

    pass
class TextLinksSupport:

    pass
class RotationSupport:

    pass
class IconPositionSupport:

    pass
class ColorForegroundSupport:

    pass
class model_RulerGuide:

    def __init__(self, position: int, model_RulerGuide: "model_ScreenRuler" = None):
        self.position = position
        self.model_RulerGuide = model_RulerGuide
        
        pass
    @property
    def position(self):
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

    def __init__(self, name: str, available: str, size: str, bold: bool, italic: bool, model_ScreenFont: "model_Screen" = None):
        self.name = name
        self.available = available
        self.size = size
        self.bold = bold
        self.italic = italic
        self.model_ScreenFont = model_ScreenFont
        
        pass
    @property
    def italic(self):
        return self.__italic

    @italic.setter
    def italic(self, italic: bool):
        self.__italic = italic


    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size


    @property
    def bold(self):
        return self.__bold

    @bold.setter
    def bold(self, bold: bool):
        self.__bold = bold


    @property
    def available(self):
        return self.__available

    @available.setter
    def available(self, available: str):
        self.__available = available


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


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

class SkinSupport:

    pass
class TextAlignmentSupport:

    pass
class LinkSupport:

    pass
class model_Item(LinkSupport):

    def __init__(self, x: int, y: int, width: int, height: int, text: str, model_Item: "model_ItemSupport" = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.model_Item = model_Item
        
        pass
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x


    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height


    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width


    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


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
        
        pass
    @property
    def iconPosition(self):
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
class model_Image(Widget, BorderSupport, FlipSupport, RotationSupport, LinkSupport):

    def __init__(self, src: str, grayscale: bool):
        self.src = src
        self.grayscale = grayscale
        
        pass
    @property
    def src(self):
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src


    @property
    def grayscale(self):
        return self.__grayscale

    @grayscale.setter
    def grayscale(self, grayscale: bool):
        self.__grayscale = grayscale


class model_Link(FontSupport, StateSupport, Widget, LinkSupport, SkinSupport):

    pass
class model_Menu(ItemSupport, SelectionSupport, Widget, IconSupport, SkinSupport):

    pass
class model_Area(Widget):

    pass
class model_TextArea(FontSupport, StateSupport, ColorAlphaSupport, TextAlignmentSupport, ColorBorderSupport, Widget, SkinSupport, TextLinksSupport, VerticalScrollbarSupport, LineHeightSupport, ColorBackgroundSupport):

    pass
class model_Combo(FontSupport, StateSupport, ColorBorderSupport, Widget, SkinSupport, LinkSupport, ColorAlphaSupport, ColorBackgroundSupport):

    pass
class model_VideoPlayer(Widget, SkinSupport):

    pass
class model_Label(FontSupport, StateSupport, IconPositionSupport, TextAlignmentSupport, Widget, TextLinksSupport, RotationSupport, IconSupport, LinkSupport, ColorForegroundSupport):

    pass
class model_Map(Widget, SkinSupport):

    pass
class model_Rectangle(FontSupport, BorderStyleSupport, IconPositionSupport, TextAlignmentSupport, Widget, IconSupport, LinkSupport, ColorBackgroundSupport, ColorAlphaSupport, ColorForegroundSupport):

    pass
class model_CurlyBrace(FontSupport, Widget, TextLinksSupport, AnnotationSupport, SkinSupport, ColorForegroundSupport):

    def __init__(self, position: str):
        self.position = position
        
        pass
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position


class model_HSplitter(Widget, SkinSupport):

    pass
class model_Text(FontSupport, TextAlignmentSupport, Widget, TextLinksSupport, LinkSupport, LineHeightSupport, ColorForegroundSupport):

    def __init__(self, dummyText: bool):
        self.dummyText = dummyText
        
        pass
    @property
    def dummyText(self):
        return self.__dummyText

    @dummyText.setter
    def dummyText(self, dummyText: bool):
        self.__dummyText = dummyText


class model_VSlider(StateSupport, Widget, ValueSupport, SkinSupport, ColorBackgroundSupport):

    pass
class model_List(FontSupport, ColorAlternativeSupport, ItemSupport, SelectionSupport, ListSupport, Widget, BorderSupport, VerticalScrollbarSupport, ColorAlphaSupport, ColorBackgroundSupport):

    def __init__(self, header: bool):
        self.header = header
        
        pass
    @property
    def header(self):
        return self.__header

    @header.setter
    def header(self, header: bool):
        self.__header = header


class model_Checkbox(BooleanSelectionSupport, FontSupport, StateSupport, Widget, LinkSupport, SkinSupport):

    pass
class model_Alert(FontSupport, ItemSupport, Widget, IconSupport, SkinSupport):

    pass
class model_Hotspot(LinkSupport, Widget):

    pass
class model_Tree(FontSupport, ItemSupport, SelectionSupport, Widget, BorderSupport, VerticalScrollbarSupport, ColorAlphaSupport, ColorBackgroundSupport):

    pass
class model_SearchField(FontSupport, StateSupport, ColorBorderSupport, Widget, LinkSupport, SkinSupport):

    pass
class model_RadioButton(BooleanSelectionSupport, FontSupport, StateSupport, Widget, LinkSupport, SkinSupport):

    pass
class model_Circle(FontSupport, IconPositionSupport, TextAlignmentSupport, LineStyleSupport, Widget, BorderSupport, IconSupport, LinkSupport, ColorAlphaSupport, ColorBackgroundSupport, ColorForegroundSupport):

    pass
class model_Popup(SelectionSupport, Widget, ItemSupport):

    pass
class model_HScrollbar(Widget, ValueSupport, SkinSupport):

    pass
class model_Arrow(LineStyleSupport, ColorForegroundSupport, Widget, AnnotationSupport):

    def __init__(self, left: bool, right: bool, direction: str):
        self.left = left
        self.right = right
        self.direction = direction
        
        pass
    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right: bool):
        self.__right = right


    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction


    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left: bool):
        self.__left = left


class model_ColorPicker(ColorBackgroundSupport, Widget, SkinSupport):

    pass
class model_VButtonBar(FontSupport, ItemSupport, TextAlignmentSupport, SelectionSupport, Widget, SkinSupport, ColorBackgroundSupport):

    pass
class model_VLine(LineStyleSupport, ColorForegroundSupport, Widget, SkinSupport):

    pass
class model_ScratchOut(ColorAlphaSupport, Widget, AnnotationSupport, SkinSupport, ColorForegroundSupport):

    pass
class model_Master(LinkSupport, Widget):

    def __init__(self, dimmed: bool, model_Master: "model_WidgetContainer" = None, model_Master13: "Overrides" = None, model_Master15: "model_WidgetContainer" = None):
        self.dimmed = dimmed
        self.model_Master = model_Master
        self.model_Master13 = model_Master13
        self.model_Master15 = model_Master15
        
        pass
    @property
    def dimmed(self):
        return self.__dimmed

    @dimmed.setter
    def dimmed(self, dimmed: bool):
        self.__dimmed = dimmed


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

class model_Breadcrumbs(FontSupport, Widget, ItemSupport, SkinSupport):

    pass
class model_ButtonBar(FontSupport, ItemSupport, SelectionSupport, Widget, SkinSupport, ColorBackgroundSupport):

    pass
class model_Spinner(FontSupport, StateSupport, ColorAlphaSupport, ColorBorderSupport, Widget, SkinSupport, ColorBackgroundSupport):

    pass
class model_ProgressBar(ColorBackgroundSupport, Widget, ValueSupport, SkinSupport):

    pass
class model_Callout(FontSupport, ColorAlphaSupport, Widget, AnnotationSupport, LinkSupport, SkinSupport, ColorBackgroundSupport):

    pass
class model_TextField(FontSupport, StateSupport, ColorAlphaSupport, TextAlignmentSupport, ColorBorderSupport, Widget, SkinSupport, ColorBackgroundSupport):

    pass
class model_SVGImage(Widget, RotationSupport, FlipSupport, LinkSupport, ColorBackgroundSupport, ColorAlphaSupport, ColorForegroundSupport):

    def __init__(self, src: str):
        self.src = src
        
        pass
    @property
    def src(self):
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src


class model_DateField(StateSupport, ColorBorderSupport, Widget, SkinSupport, ColorAlphaSupport, ColorBackgroundSupport):

    pass
class model_LinkBar(FontSupport, ItemSupport, SelectionSupport, Widget, SkinSupport):

    pass
class model_Table(FontSupport, ColorAlternativeSupport, TextAlignmentSupport, SelectionSupport, ListSupport, TextLinksSupport, BorderSupport, Widget, VerticalScrollbarSupport, ColorAlphaSupport, ColorBackgroundSupport):

    def __init__(self, verticalLines: bool, header: bool):
        self.verticalLines = verticalLines
        self.header = header
        
        pass
    @property
    def verticalLines(self):
        return self.__verticalLines

    @verticalLines.setter
    def verticalLines(self, verticalLines: bool):
        self.__verticalLines = verticalLines


    @property
    def header(self):
        return self.__header

    @header.setter
    def header(self, header: bool):
        self.__header = header


class model_Note(FontSupport, TextAlignmentSupport, SkinSupport, Widget, AnnotationSupport, TextLinksSupport, LinkSupport, ColorAlphaSupport, ColorBackgroundSupport):

    pass
class model_Placeholder(LinkSupport, Widget, SkinSupport):

    pass
class model_Tooltip(FontSupport, TextAlignmentSupport, Widget, TextLinksSupport, SkinSupport, ColorBackgroundSupport):

    def __init__(self, position: str):
        self.position = position
        
        pass
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position


class model_Accordion(FontSupport, ItemSupport, SelectionSupport, Widget, VerticalScrollbarSupport):

    pass
class model_Panel(BorderStyleSupport, SkinSupport, Widget, LinkSupport, VerticalScrollbarSupport, ColorAlphaSupport, ColorBackgroundSupport, ColorForegroundSupport):

    pass
class model_Group(FontSupport, ColorAlphaSupport, Widget, VerticalScrollbarSupport, SkinSupport, ColorBackgroundSupport):

    pass
class model_TabbedPane(FontSupport, ItemSupport, SelectionSupport, SkinSupport, Widget, VerticalScrollbarSupport, ColorAlphaSupport, ColorBackgroundSupport):

    def __init__(self, position: str):
        self.position = position
        
        pass
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position


class model_Icon(IconSupport, LinkSupport, ColorForegroundSupport, Widget):

    pass
class model_Shape(FontSupport, ColorAlphaSupport, IconPositionSupport, TextAlignmentSupport, LineStyleSupport, Widget, RotationSupport, IconSupport, BorderSupport, LinkSupport, SkinSupport, ColorBackgroundSupport, ColorForegroundSupport):

    def __init__(self, shapeType: str):
        self.shapeType = shapeType
        
        pass
    @property
    def shapeType(self):
        return self.__shapeType

    @shapeType.setter
    def shapeType(self, shapeType: str):
        self.__shapeType = shapeType


    def isRotatable(self) :
        # TODO: Implement isRotatable method
        pass

class model_Chart(Widget, SkinSupport):

    def __init__(self, chartType: str):
        self.chartType = chartType
        
        pass
    @property
    def chartType(self):
        return self.__chartType

    @chartType.setter
    def chartType(self, chartType: str):
        self.__chartType = chartType


class model_HLine(LineStyleSupport, ColorForegroundSupport, Widget, SkinSupport):

    pass
class model_VScrollbar(Widget, ValueSupport, SkinSupport):

    pass
class model_Window(ColorAlphaSupport, Widget, VerticalScrollbarSupport, SkinSupport, ColorBackgroundSupport):

    def __init__(self, closeButton: bool, minimizeButton: bool, maximizeButton: bool):
        self.closeButton = closeButton
        self.minimizeButton = minimizeButton
        self.maximizeButton = maximizeButton
        
        pass
    @property
    def closeButton(self):
        return self.__closeButton

    @closeButton.setter
    def closeButton(self, closeButton: bool):
        self.__closeButton = closeButton


    @property
    def maximizeButton(self):
        return self.__maximizeButton

    @maximizeButton.setter
    def maximizeButton(self, maximizeButton: bool):
        self.__maximizeButton = maximizeButton


    @property
    def minimizeButton(self):
        return self.__minimizeButton

    @minimizeButton.setter
    def minimizeButton(self, minimizeButton: bool):
        self.__minimizeButton = minimizeButton


class model_Switch(BooleanSelectionSupport, FontSupport, StateSupport, Widget, LinkSupport, SkinSupport, ColorBackgroundSupport):

    pass
class model_CrossOut(SkinSupport, Widget, AnnotationSupport, ColorAlphaSupport, ColorForegroundSupport):

    pass
class model_CoverFlow(Widget, SkinSupport):

    pass
class model_Browser(FontSupport, SkinSupport, Widget, VerticalScrollbarSupport, ColorAlphaSupport, ColorBackgroundSupport):

    pass
class model_HSlider(StateSupport, Widget, ValueSupport, SkinSupport, ColorBackgroundSupport):

    pass
class model_VSplitter(Widget, SkinSupport):

    pass
class model_Tabs(FontSupport, ItemSupport, SelectionSupport, Widget, SkinSupport):

    pass
class model_Button(FontSupport, StateSupport, TextAlignmentSupport, Widget, IconSupport, LinkSupport, SkinSupport, ColorBackgroundSupport):

    def __init__(self, style: str):
        self.style = style
        
        pass
    @property
    def style(self):
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
        
        pass
    @property
    def textLines(self):
        return self.__textLines

    @textLines.setter
    def textLines(self, textLines: int):
        self.__textLines = textLines


    @property
    def typeName(self):
        return self.__typeName

    @typeName.setter
    def typeName(self, typeName: str):
        self.__typeName = typeName


    @property
    def textEditable(self):
        return self.__textEditable

    @textEditable.setter
    def textEditable(self, textEditable: bool):
        self.__textEditable = textEditable


    @property
    def textWrappable(self):
        return self.__textWrappable

    @textWrappable.setter
    def textWrappable(self, textWrappable: bool):
        self.__textWrappable = textWrappable


    @property
    def resizeMode(self):
        return self.__resizeMode

    @resizeMode.setter
    def resizeMode(self, resizeMode: str):
        self.__resizeMode = resizeMode


    @property
    def textCentered(self):
        return self.__textCentered

    @textCentered.setter
    def textCentered(self, textCentered: bool):
        self.__textCentered = textCentered


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

class model_WidgetContainer(ABC):

    pass
class model_ScreenRuler:

    pass
class NoteSupport:

    pass
class model_Widget(NoteSupport):

    def __init__(self, id: str, x: int, y: int, width: int, height: int, text: str, locked: bool, measuredWidth: int, measuredHeight: int, customId: str, customData: str, annotation: bool, layoutParams: str, widgets: "model_WidgetContainer" = None, model_Widget: "model_WidgetDescriptor" = None, Widget: "model_WidgetContainer" = None):
        self.id = id
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
        self.widgets = widgets
        self.model_Widget = model_Widget
        self.Widget = Widget
        
        pass
    @property
    def locked(self):
        return self.__locked

    @locked.setter
    def locked(self, locked: bool):
        self.__locked = locked


    @property
    def measuredWidth(self):
        return self.__measuredWidth

    @measuredWidth.setter
    def measuredWidth(self, measuredWidth: int):
        self.__measuredWidth = measuredWidth


    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height


    @property
    def measuredHeight(self):
        return self.__measuredHeight

    @measuredHeight.setter
    def measuredHeight(self, measuredHeight: int):
        self.__measuredHeight = measuredHeight


    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: int):
        self.__y = y


    @property
    def layoutParams(self):
        return self.__layoutParams

    @layoutParams.setter
    def layoutParams(self, layoutParams: str):
        self.__layoutParams = layoutParams


    @property
    def customData(self):
        return self.__customData

    @customData.setter
    def customData(self, customData: str):
        self.__customData = customData


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width


    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def customId(self):
        return self.__customId

    @customId.setter
    def customId(self, customId: str):
        self.__customId = customId


    @property
    def annotation(self):
        return self.__annotation

    @annotation.setter
    def annotation(self, annotation: bool):
        self.__annotation = annotation


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x: int):
        self.__x = x


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

class WidgetContainer:

    pass
class model_WidgetGroup(NameSupport, LinkSupport, Widget, WidgetContainer):

    pass
class model_Screen(NoteSupport, WidgetContainer):

    def __init__(self, name: str, theme: str, minVersion: str, model_Screen: "model_ScreenRuler" = None, model_Screen2: "model_ScreenRuler" = None, model_Screen5: "model_ScreenFont" = None):
        self.name = name
        self.theme = theme
        self.minVersion = minVersion
        self.model_Screen = model_Screen
        self.model_Screen2 = model_Screen2
        self.model_Screen5 = model_Screen5
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def theme(self):
        return self.__theme

    @theme.setter
    def theme(self, theme: str):
        self.__theme = theme


    @property
    def minVersion(self):
        return self.__minVersion

    @minVersion.setter
    def minVersion(self, minVersion: str):
        self.__minVersion = minVersion


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
