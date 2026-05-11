from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class TextOrientationStyle(Enum):
    LEFT_TO_RIGHT = "LEFT_TO_RIGHT"
    RIGHT_TO_LEFT = "RIGHT_TO_LEFT"
class ProgressState(Enum):
    NORMAL = "NORMAL"
    PAUSED = "PAUSED"
    ERROR = "ERROR"
class JoinStyle(Enum):
    MITER = "MITER"
    ROUND = "ROUND"
    BEVEL = "BEVEL"
class ComboStyle(Enum):
    DROP_DOWN = "DROP_DOWN"
    READ_ONLY = "READ_ONLY"
    SIMPLE = "SIMPLE"
class ButtonStyle(Enum):
    TOGGLE = "TOGGLE"
    PUSH = "PUSH"
    RADIO = "RADIO"
    CHECK = "CHECK"
    ARROW = "ARROW"
class LineStyle(Enum):
    CUSTOM = "CUSTOM"
    DASH = "DASH"
    DASHDOT = "DASHDOT"
    DASHDOTDOT = "DASHDOTDOT"
    DOT = "DOT"
    SOLID = "SOLID"
class BorderStyle(Enum):
    NONE = "NONE"
    BORDER = "BORDER"
class MenuItemStyle(Enum):
    PUSH = "PUSH"
    CASCADE = "CASCADE"
    CHECK = "CHECK"
    RADIO = "RADIO"
    SEPARATOR = "SEPARATOR"
class HorizontalAlignmentStyle(Enum):
    CENTER = "CENTER"
    RIGHT = "RIGHT"
    FILL = "FILL"
    LEFT = "LEFT"
class ModalStyle(Enum):
    SYSTEM_MODAL = "SYSTEM_MODAL"
    APPLICATION_MODAL = "APPLICATION_MODAL"
    PRIMARY_MODAL = "PRIMARY_MODAL"
class FormAttachmentAlignment(Enum):
    DEFAULT = "DEFAULT"
    TOP = "TOP"
    BOTTOM = "BOTTOM"
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    CENTER = "CENTER"
class CapStyle(Enum):
    FLAT = "FLAT"
    ROUND = "ROUND"
    SQUARE = "SQUARE"
class SortDirection(Enum):
    NONE = "NONE"
    UP = "UP"
    DOWN = "DOWN"
class FontStyle(Enum):
    NORMAL = "NORMAL"
    BOLD = "BOLD"
    ITALIC = "ITALIC"
class MenuStyle(Enum):
    POP_UP = "POP_UP"
    DROP_DOWN = "DROP_DOWN"
class VerticalAlignmentStyle(Enum):
    CENTER = "CENTER"
    TOP = "TOP"
    BOTTOM = "BOTTOM"
    FILL = "FILL"
class TrimStyle(Enum):
    NOT_TRIM = "NOT_TRIM"
    SHELL_TRIM = "SHELL_TRIM"
    DIALOG_TRIM = "DIALOG_TRIM"
class SystemColors(Enum):
    RED = "RED"
    GREEN = "GREEN"
    BLUE = "BLUE"
class MultiplicityStyle(Enum):
    SINGLE = "SINGLE"
    MULTI = "MULTI"
class OrientationStyle(Enum):
    HORIZONTAL = "HORIZONTAL"
    VERTICAL = "VERTICAL"
class ArrowStyle(Enum):
    NONE = "NONE"
    UP = "UP"
    DOWN = "DOWN"
    LEFT = "LEFT"
    RIGHT = "RIGHT"


############################################
# Definition of Classes
############################################

class swt_CoolBar:

    def __init__(self, orientationStyle: str, parent15: set["swt_CoolItem"] = None, CoolBar: "swt_CoolItem" = None):
        self.orientationStyle = orientationStyle
        self.parent15 = parent15 if parent15 is not None else set()
        self.CoolBar = CoolBar
        
        pass
    @property
    def orientationStyle(self):
        return self.__orientationStyle

    @orientationStyle.setter
    def orientationStyle(self, orientationStyle: str):
        self.__orientationStyle = orientationStyle


    @property
    def CoolBar(self):
        return self.__CoolBar

    @CoolBar.setter
    def CoolBar(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_CoolBar__CoolBar", None)
        self.__CoolBar = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "items17"):
                opp_val = getattr(old_value, "items17", None)
                if opp_val == self:
                    setattr(old_value, "items17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "items17"):
                opp_val = getattr(value, "items17", None)
                setattr(value, "items17", self)

    @property
    def parent15(self):
        return self.__parent15

    @parent15.setter
    def parent15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_CoolBar__parent15", None)
        self.__parent15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CoolItem"):
                    opp_val = getattr(item, "CoolItem", None)
                    
                    if opp_val == self:
                        setattr(item, "CoolItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CoolItem"):
                    opp_val = getattr(item, "CoolItem", None)
                    
                    setattr(item, "CoolItem", self)
                    

class IntervalSelector:

    pass
class swt_Spinner(IntervalSelector):

    def __init__(self, digits: int, textLimit: int):
        self.digits = digits
        self.textLimit = textLimit
        
        pass
    @property
    def textLimit(self):
        return self.__textLimit

    @textLimit.setter
    def textLimit(self, textLimit: int):
        self.__textLimit = textLimit


    @property
    def digits(self):
        return self.__digits

    @digits.setter
    def digits(self, digits: int):
        self.__digits = digits


class swt_Slider(IntervalSelector):

    def __init__(self, thumb: int):
        self.thumb = thumb
        
        pass
    @property
    def thumb(self):
        return self.__thumb

    @thumb.setter
    def thumb(self, thumb: int):
        self.__thumb = thumb


class IntervalControl:

    pass
class swt_ProgressBar(IntervalControl):

    def __init__(self, state: str):
        self.state = state
        
        pass
    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state


class swt_IntervalSelector(IntervalControl):

    def __init__(self, orientationStyle: str, increment: int, pageIncrement: int):
        self.orientationStyle = orientationStyle
        self.increment = increment
        self.pageIncrement = pageIncrement
        
        pass
    @property
    def increment(self):
        return self.__increment

    @increment.setter
    def increment(self, increment: int):
        self.__increment = increment


    @property
    def pageIncrement(self):
        return self.__pageIncrement

    @pageIncrement.setter
    def pageIncrement(self, pageIncrement: int):
        self.__pageIncrement = pageIncrement


    @property
    def orientationStyle(self):
        return self.__orientationStyle

    @orientationStyle.setter
    def orientationStyle(self, orientationStyle: str):
        self.__orientationStyle = orientationStyle


class Text:

    pass
class swt_SearchText(Text):

    pass
class swt_PasswordText(Text):

    pass
class Item:

    pass
class swt_ToolItem(Item):

    def __init__(self, enabled: bool, hotImage: str, toolTipText: str, selection: bool, ToolItem: "swt_ToolBar" = None, items: "swt_ToolBar" = None):
        self.enabled = enabled
        self.hotImage = hotImage
        self.toolTipText = toolTipText
        self.selection = selection
        self.ToolItem = ToolItem
        self.items = items
        
        pass
    @property
    def toolTipText(self):
        return self.__toolTipText

    @toolTipText.setter
    def toolTipText(self, toolTipText: str):
        self.__toolTipText = toolTipText


    @property
    def hotImage(self):
        return self.__hotImage

    @hotImage.setter
    def hotImage(self, hotImage: str):
        self.__hotImage = hotImage


    @property
    def selection(self):
        return self.__selection

    @selection.setter
    def selection(self, selection: bool):
        self.__selection = selection


    @property
    def enabled(self):
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled: bool):
        self.__enabled = enabled


    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_ToolItem__items", None)
        self.__items = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ToolBar"):
                opp_val = getattr(old_value, "ToolBar", None)
                if opp_val == self:
                    setattr(old_value, "ToolBar", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ToolBar"):
                opp_val = getattr(value, "ToolBar", None)
                setattr(value, "ToolBar", self)

    @property
    def ToolItem(self):
        return self.__ToolItem

    @ToolItem.setter
    def ToolItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_ToolItem__ToolItem", None)
        self.__ToolItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent12"):
                opp_val = getattr(old_value, "parent12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent12"):
                opp_val = getattr(value, "parent12", None)
                if opp_val is None:
                    setattr(value, "parent12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class swt_CoolItem(Item):

    def __init__(self, minimumSize: str, preferredSize: str, size: str, CoolItem: "swt_CoolBar" = None, items17: "swt_CoolBar" = None, swt_CoolItem: "swt_Control" = None):
        self.minimumSize = minimumSize
        self.preferredSize = preferredSize
        self.size = size
        self.CoolItem = CoolItem
        self.items17 = items17
        self.swt_CoolItem = swt_CoolItem
        
        pass
    @property
    def minimumSize(self):
        return self.__minimumSize

    @minimumSize.setter
    def minimumSize(self, minimumSize: str):
        self.__minimumSize = minimumSize


    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size


    @property
    def preferredSize(self):
        return self.__preferredSize

    @preferredSize.setter
    def preferredSize(self, preferredSize: str):
        self.__preferredSize = preferredSize


    @property
    def CoolItem(self):
        return self.__CoolItem

    @CoolItem.setter
    def CoolItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_CoolItem__CoolItem", None)
        self.__CoolItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parent15"):
                opp_val = getattr(old_value, "parent15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parent15"):
                opp_val = getattr(value, "parent15", None)
                if opp_val is None:
                    setattr(value, "parent15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def swt_CoolItem(self):
        return self.__swt_CoolItem

    @swt_CoolItem.setter
    def swt_CoolItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_CoolItem__swt_CoolItem", None)
        self.__swt_CoolItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_Control19"):
                opp_val = getattr(old_value, "swt_Control19", None)
                if opp_val == self:
                    setattr(old_value, "swt_Control19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_Control19"):
                opp_val = getattr(value, "swt_Control19", None)
                setattr(value, "swt_Control19", self)

    @property
    def items17(self):
        return self.__items17

    @items17.setter
    def items17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_CoolItem__items17", None)
        self.__items17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CoolBar"):
                opp_val = getattr(old_value, "CoolBar", None)
                if opp_val == self:
                    setattr(old_value, "CoolBar", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CoolBar"):
                opp_val = getattr(value, "CoolBar", None)
                setattr(value, "CoolBar", self)

class Labeled:

    pass
class swt_Labeled(ABC):

    def __init__(self, text: str, image: str):
        self.text = text
        self.image = image
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, image: str):
        self.__image = image


class AbstractMenu:

    pass
class swt_Menu(AbstractMenu):

    def __init__(self, menuStyle: str, menu: "swt_MenuItem" = None, Menu: "swt_MenuItem" = None):
        self.menuStyle = menuStyle
        self.menu = menu
        self.Menu = Menu
        
        pass
    @property
    def menuStyle(self):
        return self.__menuStyle

    @menuStyle.setter
    def menuStyle(self, menuStyle: str):
        self.__menuStyle = menuStyle


    @property
    def Menu(self):
        return self.__Menu

    @Menu.setter
    def Menu(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_Menu__Menu", None)
        self.__Menu = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parentItem"):
                opp_val = getattr(old_value, "parentItem", None)
                if opp_val == self:
                    setattr(old_value, "parentItem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parentItem"):
                opp_val = getattr(value, "parentItem", None)
                setattr(value, "parentItem", self)

    @property
    def menu(self):
        return self.__menu

    @menu.setter
    def menu(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_Menu__menu", None)
        self.__menu = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MenuItem"):
                opp_val = getattr(old_value, "MenuItem", None)
                if opp_val == self:
                    setattr(old_value, "MenuItem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MenuItem"):
                opp_val = getattr(value, "MenuItem", None)
                setattr(value, "MenuItem", self)

class swt_MenuItem(Item):

    def __init__(self, menuItemStyle: str, ID: int, accelerator: int, enabled: bool, selection: bool, swt_MenuItem: "swt_AbstractMenu" = None, MenuItem: "swt_Menu" = None, parentItem: "swt_Menu" = None):
        self.menuItemStyle = menuItemStyle
        self.ID = ID
        self.accelerator = accelerator
        self.enabled = enabled
        self.selection = selection
        self.swt_MenuItem = swt_MenuItem
        self.MenuItem = MenuItem
        self.parentItem = parentItem
        
        pass
    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID


    @property
    def accelerator(self):
        return self.__accelerator

    @accelerator.setter
    def accelerator(self, accelerator: int):
        self.__accelerator = accelerator


    @property
    def menuItemStyle(self):
        return self.__menuItemStyle

    @menuItemStyle.setter
    def menuItemStyle(self, menuItemStyle: str):
        self.__menuItemStyle = menuItemStyle


    @property
    def enabled(self):
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled: bool):
        self.__enabled = enabled


    @property
    def selection(self):
        return self.__selection

    @selection.setter
    def selection(self, selection: bool):
        self.__selection = selection


    @property
    def swt_MenuItem(self):
        return self.__swt_MenuItem

    @swt_MenuItem.setter
    def swt_MenuItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_MenuItem__swt_MenuItem", None)
        self.__swt_MenuItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_AbstractMenu"):
                opp_val = getattr(old_value, "swt_AbstractMenu", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_AbstractMenu"):
                opp_val = getattr(value, "swt_AbstractMenu", None)
                if opp_val is None:
                    setattr(value, "swt_AbstractMenu", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MenuItem(self):
        return self.__MenuItem

    @MenuItem.setter
    def MenuItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_MenuItem__MenuItem", None)
        self.__MenuItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "menu"):
                opp_val = getattr(old_value, "menu", None)
                if opp_val == self:
                    setattr(old_value, "menu", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "menu"):
                opp_val = getattr(value, "menu", None)
                setattr(value, "menu", self)

    @property
    def parentItem(self):
        return self.__parentItem

    @parentItem.setter
    def parentItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_MenuItem__parentItem", None)
        self.__parentItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Menu"):
                opp_val = getattr(old_value, "Menu", None)
                if opp_val == self:
                    setattr(old_value, "Menu", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Menu"):
                opp_val = getattr(value, "Menu", None)
                setattr(value, "Menu", self)

class Widget:

    pass
class swt_AbstractMenu(Widget):

    def __init__(self, textOrientationStyle: str, enabled: bool, visible: bool, swt_AbstractMenu: set["swt_MenuItem"] = None):
        self.textOrientationStyle = textOrientationStyle
        self.enabled = enabled
        self.visible = visible
        self.swt_AbstractMenu = swt_AbstractMenu if swt_AbstractMenu is not None else set()
        
        pass
    @property
    def enabled(self):
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled: bool):
        self.__enabled = enabled


    @property
    def textOrientationStyle(self):
        return self.__textOrientationStyle

    @textOrientationStyle.setter
    def textOrientationStyle(self, textOrientationStyle: str):
        self.__textOrientationStyle = textOrientationStyle


    @property
    def visible(self):
        return self.__visible

    @visible.setter
    def visible(self, visible: bool):
        self.__visible = visible


    @property
    def swt_AbstractMenu(self):
        return self.__swt_AbstractMenu

    @swt_AbstractMenu.setter
    def swt_AbstractMenu(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_AbstractMenu__swt_AbstractMenu", None)
        self.__swt_AbstractMenu = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "swt_MenuItem"):
                    opp_val = getattr(item, "swt_MenuItem", None)
                    
                    if opp_val == self:
                        setattr(item, "swt_MenuItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "swt_MenuItem"):
                    opp_val = getattr(item, "swt_MenuItem", None)
                    
                    setattr(item, "swt_MenuItem", self)
                    

class swt_Item(Labeled, Widget):

    pass
class swt_Control(Widget):

    def __init__(self, borderStyle: str, textOrientationStyle: str, enabled: bool, visible: bool, touchEnabled: bool, toolTipText: str, size: str, swt_Control: "swt_LayoutData" = None, swt_Control2: "swt_Color" = None, swt_Control4: "swt_Font" = None, swt_Control19: "swt_CoolItem" = None, swt_Control23: "swt_TabItem" = None, swt_Control36: "swt_FormAttachment" = None):
        self.borderStyle = borderStyle
        self.textOrientationStyle = textOrientationStyle
        self.enabled = enabled
        self.visible = visible
        self.touchEnabled = touchEnabled
        self.toolTipText = toolTipText
        self.size = size
        self.swt_Control = swt_Control
        self.swt_Control2 = swt_Control2
        self.swt_Control4 = swt_Control4
        self.swt_Control19 = swt_Control19
        self.swt_Control23 = swt_Control23
        self.swt_Control36 = swt_Control36
        
        pass
    @property
    def borderStyle(self):
        return self.__borderStyle

    @borderStyle.setter
    def borderStyle(self, borderStyle: str):
        self.__borderStyle = borderStyle


    @property
    def textOrientationStyle(self):
        return self.__textOrientationStyle

    @textOrientationStyle.setter
    def textOrientationStyle(self, textOrientationStyle: str):
        self.__textOrientationStyle = textOrientationStyle


    @property
    def visible(self):
        return self.__visible

    @visible.setter
    def visible(self, visible: bool):
        self.__visible = visible


    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size


    @property
    def touchEnabled(self):
        return self.__touchEnabled

    @touchEnabled.setter
    def touchEnabled(self, touchEnabled: bool):
        self.__touchEnabled = touchEnabled


    @property
    def toolTipText(self):
        return self.__toolTipText

    @toolTipText.setter
    def toolTipText(self, toolTipText: str):
        self.__toolTipText = toolTipText


    @property
    def enabled(self):
        return self.__enabled

    @enabled.setter
    def enabled(self, enabled: bool):
        self.__enabled = enabled


    @property
    def swt_Control36(self):
        return self.__swt_Control36

    @swt_Control36.setter
    def swt_Control36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_Control__swt_Control36", None)
        self.__swt_Control36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_FormAttachment35"):
                opp_val = getattr(old_value, "swt_FormAttachment35", None)
                if opp_val == self:
                    setattr(old_value, "swt_FormAttachment35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_FormAttachment35"):
                opp_val = getattr(value, "swt_FormAttachment35", None)
                setattr(value, "swt_FormAttachment35", self)

    @property
    def swt_Control(self):
        return self.__swt_Control

    @swt_Control.setter
    def swt_Control(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_Control__swt_Control", None)
        self.__swt_Control = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_LayoutData"):
                opp_val = getattr(old_value, "swt_LayoutData", None)
                if opp_val == self:
                    setattr(old_value, "swt_LayoutData", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_LayoutData"):
                opp_val = getattr(value, "swt_LayoutData", None)
                setattr(value, "swt_LayoutData", self)

    @property
    def swt_Control4(self):
        return self.__swt_Control4

    @swt_Control4.setter
    def swt_Control4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_Control__swt_Control4", None)
        self.__swt_Control4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_Font"):
                opp_val = getattr(old_value, "swt_Font", None)
                if opp_val == self:
                    setattr(old_value, "swt_Font", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_Font"):
                opp_val = getattr(value, "swt_Font", None)
                setattr(value, "swt_Font", self)

    @property
    def swt_Control19(self):
        return self.__swt_Control19

    @swt_Control19.setter
    def swt_Control19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_Control__swt_Control19", None)
        self.__swt_Control19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_CoolItem"):
                opp_val = getattr(old_value, "swt_CoolItem", None)
                if opp_val == self:
                    setattr(old_value, "swt_CoolItem", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_CoolItem"):
                opp_val = getattr(value, "swt_CoolItem", None)
                setattr(value, "swt_CoolItem", self)

    @property
    def swt_Control2(self):
        return self.__swt_Control2

    @swt_Control2.setter
    def swt_Control2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_Control__swt_Control2", None)
        self.__swt_Control2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_Color"):
                opp_val = getattr(old_value, "swt_Color", None)
                if opp_val == self:
                    setattr(old_value, "swt_Color", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_Color"):
                opp_val = getattr(value, "swt_Color", None)
                setattr(value, "swt_Color", self)

    @property
    def swt_Control23(self):
        return self.__swt_Control23

    @swt_Control23.setter
    def swt_Control23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_Control__swt_Control23", None)
        self.__swt_Control23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_TabItem22"):
                opp_val = getattr(old_value, "swt_TabItem22", None)
                if opp_val == self:
                    setattr(old_value, "swt_TabItem22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_TabItem22"):
                opp_val = getattr(value, "swt_TabItem22", None)
                setattr(value, "swt_TabItem22", self)

class swt_LayoutData(ABC):

    pass
class Decorations:

    pass
class swt_Shell(Decorations):

    def __init__(self, modalStyle: str, trimStyle: str, fullScreen: bool, alpha: int, swt_Shell: "swt_Button" = None):
        self.modalStyle = modalStyle
        self.trimStyle = trimStyle
        self.fullScreen = fullScreen
        self.alpha = alpha
        self.swt_Shell = swt_Shell
        
        pass
    @property
    def modalStyle(self):
        return self.__modalStyle

    @modalStyle.setter
    def modalStyle(self, modalStyle: str):
        self.__modalStyle = modalStyle


    @property
    def trimStyle(self):
        return self.__trimStyle

    @trimStyle.setter
    def trimStyle(self, trimStyle: str):
        self.__trimStyle = trimStyle


    @property
    def fullScreen(self):
        return self.__fullScreen

    @fullScreen.setter
    def fullScreen(self, fullScreen: bool):
        self.__fullScreen = fullScreen


    @property
    def alpha(self):
        return self.__alpha

    @alpha.setter
    def alpha(self, alpha: int):
        self.__alpha = alpha


    @property
    def swt_Shell(self):
        return self.__swt_Shell

    @swt_Shell.setter
    def swt_Shell(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_Shell__swt_Shell", None)
        self.__swt_Shell = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_Button"):
                opp_val = getattr(old_value, "swt_Button", None)
                if opp_val == self:
                    setattr(old_value, "swt_Button", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_Button"):
                opp_val = getattr(value, "swt_Button", None)
                setattr(value, "swt_Button", self)

class swt_MenuBar(AbstractMenu):

    pass
class Canvas:

    pass
class swt_Decorations(Canvas):

    def __init__(self, maximized: bool, minimized: bool, parent: "swt_MenuBar" = None, Decorations: "swt_MenuBar" = None):
        self.maximized = maximized
        self.minimized = minimized
        self.parent = parent
        self.Decorations = Decorations
        
        pass
    @property
    def maximized(self):
        return self.__maximized

    @maximized.setter
    def maximized(self, maximized: bool):
        self.__maximized = maximized


    @property
    def minimized(self):
        return self.__minimized

    @minimized.setter
    def minimized(self, minimized: bool):
        self.__minimized = minimized


    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_Decorations__parent", None)
        self.__parent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MenuBar"):
                opp_val = getattr(old_value, "MenuBar", None)
                if opp_val == self:
                    setattr(old_value, "MenuBar", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MenuBar"):
                opp_val = getattr(value, "MenuBar", None)
                setattr(value, "MenuBar", self)

    @property
    def Decorations(self):
        return self.__Decorations

    @Decorations.setter
    def Decorations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_Decorations__Decorations", None)
        self.__Decorations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "menuBar"):
                opp_val = getattr(old_value, "menuBar", None)
                if opp_val == self:
                    setattr(old_value, "menuBar", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "menuBar"):
                opp_val = getattr(value, "menuBar", None)
                setattr(value, "menuBar", self)

class Composite:

    pass
class swt_Canvas(Composite):

    pass
class swt_Group(Composite):

    def __init__(self, text: str):
        self.text = text
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


class swt_Composite:

    pass
class Control:

    pass
class swt_Separator(Control):

    def __init__(self, orientationStyle: str):
        self.orientationStyle = orientationStyle
        
        pass
    @property
    def orientationStyle(self):
        return self.__orientationStyle

    @orientationStyle.setter
    def orientationStyle(self, orientationStyle: str):
        self.__orientationStyle = orientationStyle


class swt_Label(Labeled, Control):

    pass
class swt_ToolBar(Control):

    def __init__(self, orientationStyle: str, parent12: set["swt_ToolItem"] = None, ToolBar: "swt_ToolItem" = None):
        self.orientationStyle = orientationStyle
        self.parent12 = parent12 if parent12 is not None else set()
        self.ToolBar = ToolBar
        
        pass
    @property
    def orientationStyle(self):
        return self.__orientationStyle

    @orientationStyle.setter
    def orientationStyle(self, orientationStyle: str):
        self.__orientationStyle = orientationStyle


    @property
    def ToolBar(self):
        return self.__ToolBar

    @ToolBar.setter
    def ToolBar(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_ToolBar__ToolBar", None)
        self.__ToolBar = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "items"):
                opp_val = getattr(old_value, "items", None)
                if opp_val == self:
                    setattr(old_value, "items", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "items"):
                opp_val = getattr(value, "items", None)
                setattr(value, "items", self)

    @property
    def parent12(self):
        return self.__parent12

    @parent12.setter
    def parent12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_ToolBar__parent12", None)
        self.__parent12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ToolItem"):
                    opp_val = getattr(item, "ToolItem", None)
                    
                    if opp_val == self:
                        setattr(item, "ToolItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ToolItem"):
                    opp_val = getattr(item, "ToolItem", None)
                    
                    setattr(item, "ToolItem", self)
                    

class swt_Text(Control):

    def __init__(self, topIndex: int, message: str, multiplicityStyle: str, text: str, selection: str, editable: bool, echoChar: str, tabs: int, textLimit: int):
        self.topIndex = topIndex
        self.message = message
        self.multiplicityStyle = multiplicityStyle
        self.text = text
        self.selection = selection
        self.editable = editable
        self.echoChar = echoChar
        self.tabs = tabs
        self.textLimit = textLimit
        
        pass
    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message


    @property
    def tabs(self):
        return self.__tabs

    @tabs.setter
    def tabs(self, tabs: int):
        self.__tabs = tabs


    @property
    def editable(self):
        return self.__editable

    @editable.setter
    def editable(self, editable: bool):
        self.__editable = editable


    @property
    def echoChar(self):
        return self.__echoChar

    @echoChar.setter
    def echoChar(self, echoChar: str):
        self.__echoChar = echoChar


    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def topIndex(self):
        return self.__topIndex

    @topIndex.setter
    def topIndex(self, topIndex: int):
        self.__topIndex = topIndex


    @property
    def textLimit(self):
        return self.__textLimit

    @textLimit.setter
    def textLimit(self, textLimit: int):
        self.__textLimit = textLimit


    @property
    def multiplicityStyle(self):
        return self.__multiplicityStyle

    @multiplicityStyle.setter
    def multiplicityStyle(self, multiplicityStyle: str):
        self.__multiplicityStyle = multiplicityStyle


    @property
    def selection(self):
        return self.__selection

    @selection.setter
    def selection(self, selection: str):
        self.__selection = selection


class swt_Button(Labeled, Control):

    def __init__(self, buttonStyle: str, arrowStyle: str, selection: bool, swt_Button: "swt_Shell" = None):
        self.buttonStyle = buttonStyle
        self.arrowStyle = arrowStyle
        self.selection = selection
        self.swt_Button = swt_Button
        
        pass
    @property
    def arrowStyle(self):
        return self.__arrowStyle

    @arrowStyle.setter
    def arrowStyle(self, arrowStyle: str):
        self.__arrowStyle = arrowStyle


    @property
    def selection(self):
        return self.__selection

    @selection.setter
    def selection(self, selection: bool):
        self.__selection = selection


    @property
    def buttonStyle(self):
        return self.__buttonStyle

    @buttonStyle.setter
    def buttonStyle(self, buttonStyle: str):
        self.__buttonStyle = buttonStyle


    @property
    def swt_Button(self):
        return self.__swt_Button

    @swt_Button.setter
    def swt_Button(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_Button__swt_Button", None)
        self.__swt_Button = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_Shell"):
                opp_val = getattr(old_value, "swt_Shell", None)
                if opp_val == self:
                    setattr(old_value, "swt_Shell", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_Shell"):
                opp_val = getattr(value, "swt_Shell", None)
                setattr(value, "swt_Shell", self)

class swt_IntervalControl(Control):

    def __init__(self, minimum: int, maximum: int, selection: int):
        self.minimum = minimum
        self.maximum = maximum
        self.selection = selection
        
        pass
    @property
    def maximum(self):
        return self.__maximum

    @maximum.setter
    def maximum(self, maximum: int):
        self.__maximum = maximum


    @property
    def selection(self):
        return self.__selection

    @selection.setter
    def selection(self, selection: int):
        self.__selection = selection


    @property
    def minimum(self):
        return self.__minimum

    @minimum.setter
    def minimum(self, minimum: int):
        self.__minimum = minimum


class swt_AbstractComposite(Control):

    pass
class swt_Font:

    def __init__(self, name: str, style: int, height: int, swt_Font: "swt_Control" = None):
        self.name = name
        self.style = style
        self.height = height
        self.swt_Font = swt_Font
        
        pass
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def style(self):
        return self.__style

    @style.setter
    def style(self, style: int):
        self.__style = style


    @property
    def swt_Font(self):
        return self.__swt_Font

    @swt_Font.setter
    def swt_Font(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_Font__swt_Font", None)
        self.__swt_Font = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_Control4"):
                opp_val = getattr(old_value, "swt_Control4", None)
                if opp_val == self:
                    setattr(old_value, "swt_Control4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_Control4"):
                opp_val = getattr(value, "swt_Control4", None)
                setattr(value, "swt_Control4", self)

class swt_Color(ABC):

    pass
class swt_Layout(ABC):

    pass
class swt_Widget(ABC):

    def __init__(self, style: int):
        self.style = style
        
        pass
    @property
    def style(self):
        return self.__style

    @style.setter
    def style(self, style: int):
        self.__style = style


class swt_Viewer(ABC):

    def __init__(self, input: str):
        self.input = input
        
        pass
    @property
    def input(self):
        return self.__input

    @input.setter
    def input(self, input: str):
        self.__input = input


class swt_TreeViewer:

    pass
class swt_Tree(Control):

    def __init__(self, headerVisible: bool, linesVisible: bool, sortDirection: str, swt_Tree: set["swt_TreeColumn"] = None, swt_Tree39: "swt_TreeColumn" = None, swt_Tree42: "swt_TreeViewer" = None):
        self.headerVisible = headerVisible
        self.linesVisible = linesVisible
        self.sortDirection = sortDirection
        self.swt_Tree = swt_Tree if swt_Tree is not None else set()
        self.swt_Tree39 = swt_Tree39
        self.swt_Tree42 = swt_Tree42
        
        pass
    @property
    def sortDirection(self):
        return self.__sortDirection

    @sortDirection.setter
    def sortDirection(self, sortDirection: str):
        self.__sortDirection = sortDirection


    @property
    def headerVisible(self):
        return self.__headerVisible

    @headerVisible.setter
    def headerVisible(self, headerVisible: bool):
        self.__headerVisible = headerVisible


    @property
    def linesVisible(self):
        return self.__linesVisible

    @linesVisible.setter
    def linesVisible(self, linesVisible: bool):
        self.__linesVisible = linesVisible


    @property
    def swt_Tree42(self):
        return self.__swt_Tree42

    @swt_Tree42.setter
    def swt_Tree42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_Tree__swt_Tree42", None)
        self.__swt_Tree42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_TreeViewer"):
                opp_val = getattr(old_value, "swt_TreeViewer", None)
                if opp_val == self:
                    setattr(old_value, "swt_TreeViewer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_TreeViewer"):
                opp_val = getattr(value, "swt_TreeViewer", None)
                setattr(value, "swt_TreeViewer", self)

    @property
    def swt_Tree(self):
        return self.__swt_Tree

    @swt_Tree.setter
    def swt_Tree(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_Tree__swt_Tree", None)
        self.__swt_Tree = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "swt_TreeColumn"):
                    opp_val = getattr(item, "swt_TreeColumn", None)
                    
                    if opp_val == self:
                        setattr(item, "swt_TreeColumn", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "swt_TreeColumn"):
                    opp_val = getattr(item, "swt_TreeColumn", None)
                    
                    setattr(item, "swt_TreeColumn", self)
                    

    @property
    def swt_Tree39(self):
        return self.__swt_Tree39

    @swt_Tree39.setter
    def swt_Tree39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_Tree__swt_Tree39", None)
        self.__swt_Tree39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_TreeColumn40"):
                opp_val = getattr(old_value, "swt_TreeColumn40", None)
                if opp_val == self:
                    setattr(old_value, "swt_TreeColumn40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_TreeColumn40"):
                opp_val = getattr(value, "swt_TreeColumn40", None)
                setattr(value, "swt_TreeColumn40", self)

class swt_TreeColumn(Item):

    def __init__(self, toolTipText: str, displayText: str, swt_TreeColumn: "swt_Tree" = None, swt_TreeColumn40: "swt_Tree" = None):
        self.toolTipText = toolTipText
        self.displayText = displayText
        self.swt_TreeColumn = swt_TreeColumn
        self.swt_TreeColumn40 = swt_TreeColumn40
        
        pass
    @property
    def toolTipText(self):
        return self.__toolTipText

    @toolTipText.setter
    def toolTipText(self, toolTipText: str):
        self.__toolTipText = toolTipText


    @property
    def displayText(self):
        return self.__displayText

    @displayText.setter
    def displayText(self, displayText: str):
        self.__displayText = displayText


    @property
    def swt_TreeColumn(self):
        return self.__swt_TreeColumn

    @swt_TreeColumn.setter
    def swt_TreeColumn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_TreeColumn__swt_TreeColumn", None)
        self.__swt_TreeColumn = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_Tree"):
                opp_val = getattr(old_value, "swt_Tree", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_Tree"):
                opp_val = getattr(value, "swt_Tree", None)
                if opp_val is None:
                    setattr(value, "swt_Tree", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def swt_TreeColumn40(self):
        return self.__swt_TreeColumn40

    @swt_TreeColumn40.setter
    def swt_TreeColumn40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_TreeColumn__swt_TreeColumn40", None)
        self.__swt_TreeColumn40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_Tree39"):
                opp_val = getattr(old_value, "swt_Tree39", None)
                if opp_val == self:
                    setattr(old_value, "swt_Tree39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_Tree39"):
                opp_val = getattr(value, "swt_Tree39", None)
                setattr(value, "swt_Tree39", self)

class swt_LineAttributes:

    def __init__(self, width: float, style: str, cap: str, join: str, dash: float, dashOffset: float, miterLimit: float):
        self.width = width
        self.style = style
        self.cap = cap
        self.join = join
        self.dash = dash
        self.dashOffset = dashOffset
        self.miterLimit = miterLimit
        
        pass
    @property
    def dash(self):
        return self.__dash

    @dash.setter
    def dash(self, dash: float):
        self.__dash = dash


    @property
    def cap(self):
        return self.__cap

    @cap.setter
    def cap(self, cap: str):
        self.__cap = cap


    @property
    def style(self):
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style


    @property
    def miterLimit(self):
        return self.__miterLimit

    @miterLimit.setter
    def miterLimit(self, miterLimit: float):
        self.__miterLimit = miterLimit


    @property
    def dashOffset(self):
        return self.__dashOffset

    @dashOffset.setter
    def dashOffset(self, dashOffset: float):
        self.__dashOffset = dashOffset


    @property
    def join(self):
        return self.__join

    @join.setter
    def join(self, join: str):
        self.__join = join


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: float):
        self.__width = width


class swt_FormLayout:

    def __init__(self, marginHeight: int, spacing: int, marginLeft: int, marginTop: int, marginRight: int, marginBottom: int, marginWidth: int):
        self.marginHeight = marginHeight
        self.spacing = spacing
        self.marginLeft = marginLeft
        self.marginTop = marginTop
        self.marginRight = marginRight
        self.marginBottom = marginBottom
        self.marginWidth = marginWidth
        
        pass
    @property
    def marginTop(self):
        return self.__marginTop

    @marginTop.setter
    def marginTop(self, marginTop: int):
        self.__marginTop = marginTop


    @property
    def spacing(self):
        return self.__spacing

    @spacing.setter
    def spacing(self, spacing: int):
        self.__spacing = spacing


    @property
    def marginBottom(self):
        return self.__marginBottom

    @marginBottom.setter
    def marginBottom(self, marginBottom: int):
        self.__marginBottom = marginBottom


    @property
    def marginWidth(self):
        return self.__marginWidth

    @marginWidth.setter
    def marginWidth(self, marginWidth: int):
        self.__marginWidth = marginWidth


    @property
    def marginHeight(self):
        return self.__marginHeight

    @marginHeight.setter
    def marginHeight(self, marginHeight: int):
        self.__marginHeight = marginHeight


    @property
    def marginLeft(self):
        return self.__marginLeft

    @marginLeft.setter
    def marginLeft(self, marginLeft: int):
        self.__marginLeft = marginLeft


    @property
    def marginRight(self):
        return self.__marginRight

    @marginRight.setter
    def marginRight(self, marginRight: int):
        self.__marginRight = marginRight


class swt_FormAttachment:

    def __init__(self, alignment: str, denominator: int, numerator: int, offset: int, swt_FormAttachment: "swt_FormData" = None, swt_FormAttachment27: "swt_FormData" = None, swt_FormAttachment30: "swt_FormData" = None, swt_FormAttachment33: "swt_FormData" = None, swt_FormAttachment35: "swt_Control" = None):
        self.alignment = alignment
        self.denominator = denominator
        self.numerator = numerator
        self.offset = offset
        self.swt_FormAttachment = swt_FormAttachment
        self.swt_FormAttachment27 = swt_FormAttachment27
        self.swt_FormAttachment30 = swt_FormAttachment30
        self.swt_FormAttachment33 = swt_FormAttachment33
        self.swt_FormAttachment35 = swt_FormAttachment35
        
        pass
    @property
    def alignment(self):
        return self.__alignment

    @alignment.setter
    def alignment(self, alignment: str):
        self.__alignment = alignment


    @property
    def numerator(self):
        return self.__numerator

    @numerator.setter
    def numerator(self, numerator: int):
        self.__numerator = numerator


    @property
    def denominator(self):
        return self.__denominator

    @denominator.setter
    def denominator(self, denominator: int):
        self.__denominator = denominator


    @property
    def offset(self):
        return self.__offset

    @offset.setter
    def offset(self, offset: int):
        self.__offset = offset


    @property
    def swt_FormAttachment30(self):
        return self.__swt_FormAttachment30

    @swt_FormAttachment30.setter
    def swt_FormAttachment30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_FormAttachment__swt_FormAttachment30", None)
        self.__swt_FormAttachment30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_FormData29"):
                opp_val = getattr(old_value, "swt_FormData29", None)
                if opp_val == self:
                    setattr(old_value, "swt_FormData29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_FormData29"):
                opp_val = getattr(value, "swt_FormData29", None)
                setattr(value, "swt_FormData29", self)

    @property
    def swt_FormAttachment33(self):
        return self.__swt_FormAttachment33

    @swt_FormAttachment33.setter
    def swt_FormAttachment33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_FormAttachment__swt_FormAttachment33", None)
        self.__swt_FormAttachment33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_FormData32"):
                opp_val = getattr(old_value, "swt_FormData32", None)
                if opp_val == self:
                    setattr(old_value, "swt_FormData32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_FormData32"):
                opp_val = getattr(value, "swt_FormData32", None)
                setattr(value, "swt_FormData32", self)

    @property
    def swt_FormAttachment27(self):
        return self.__swt_FormAttachment27

    @swt_FormAttachment27.setter
    def swt_FormAttachment27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_FormAttachment__swt_FormAttachment27", None)
        self.__swt_FormAttachment27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_FormData26"):
                opp_val = getattr(old_value, "swt_FormData26", None)
                if opp_val == self:
                    setattr(old_value, "swt_FormData26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_FormData26"):
                opp_val = getattr(value, "swt_FormData26", None)
                setattr(value, "swt_FormData26", self)

    @property
    def swt_FormAttachment35(self):
        return self.__swt_FormAttachment35

    @swt_FormAttachment35.setter
    def swt_FormAttachment35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_FormAttachment__swt_FormAttachment35", None)
        self.__swt_FormAttachment35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_Control36"):
                opp_val = getattr(old_value, "swt_Control36", None)
                if opp_val == self:
                    setattr(old_value, "swt_Control36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_Control36"):
                opp_val = getattr(value, "swt_Control36", None)
                setattr(value, "swt_Control36", self)

    @property
    def swt_FormAttachment(self):
        return self.__swt_FormAttachment

    @swt_FormAttachment.setter
    def swt_FormAttachment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_FormAttachment__swt_FormAttachment", None)
        self.__swt_FormAttachment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_FormData"):
                opp_val = getattr(old_value, "swt_FormData", None)
                if opp_val == self:
                    setattr(old_value, "swt_FormData", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_FormData"):
                opp_val = getattr(value, "swt_FormData", None)
                setattr(value, "swt_FormData", self)

class swt_RowLayout:

    def __init__(self, spacing: int, wrap: bool, pack: bool, fill: bool, center: bool, justify: bool, marginLeft: int, marginTop: int, marginRight: int, marginBottom: int, orientationStyle: str, marginWidth: int, marginHeight: int):
        self.spacing = spacing
        self.wrap = wrap
        self.pack = pack
        self.fill = fill
        self.center = center
        self.justify = justify
        self.marginLeft = marginLeft
        self.marginTop = marginTop
        self.marginRight = marginRight
        self.marginBottom = marginBottom
        self.orientationStyle = orientationStyle
        self.marginWidth = marginWidth
        self.marginHeight = marginHeight
        
        pass
    @property
    def orientationStyle(self):
        return self.__orientationStyle

    @orientationStyle.setter
    def orientationStyle(self, orientationStyle: str):
        self.__orientationStyle = orientationStyle


    @property
    def marginRight(self):
        return self.__marginRight

    @marginRight.setter
    def marginRight(self, marginRight: int):
        self.__marginRight = marginRight


    @property
    def marginLeft(self):
        return self.__marginLeft

    @marginLeft.setter
    def marginLeft(self, marginLeft: int):
        self.__marginLeft = marginLeft


    @property
    def marginBottom(self):
        return self.__marginBottom

    @marginBottom.setter
    def marginBottom(self, marginBottom: int):
        self.__marginBottom = marginBottom


    @property
    def pack(self):
        return self.__pack

    @pack.setter
    def pack(self, pack: bool):
        self.__pack = pack


    @property
    def marginWidth(self):
        return self.__marginWidth

    @marginWidth.setter
    def marginWidth(self, marginWidth: int):
        self.__marginWidth = marginWidth


    @property
    def fill(self):
        return self.__fill

    @fill.setter
    def fill(self, fill: bool):
        self.__fill = fill


    @property
    def center(self):
        return self.__center

    @center.setter
    def center(self, center: bool):
        self.__center = center


    @property
    def wrap(self):
        return self.__wrap

    @wrap.setter
    def wrap(self, wrap: bool):
        self.__wrap = wrap


    @property
    def marginTop(self):
        return self.__marginTop

    @marginTop.setter
    def marginTop(self, marginTop: int):
        self.__marginTop = marginTop


    @property
    def spacing(self):
        return self.__spacing

    @spacing.setter
    def spacing(self, spacing: int):
        self.__spacing = spacing


    @property
    def justify(self):
        return self.__justify

    @justify.setter
    def justify(self, justify: bool):
        self.__justify = justify


    @property
    def marginHeight(self):
        return self.__marginHeight

    @marginHeight.setter
    def marginHeight(self, marginHeight: int):
        self.__marginHeight = marginHeight


class swt_FillLayout:

    def __init__(self, orientationStyle: str, marginWidth: int, marginHeight: int, spacing: int):
        self.orientationStyle = orientationStyle
        self.marginWidth = marginWidth
        self.marginHeight = marginHeight
        self.spacing = spacing
        
        pass
    @property
    def marginHeight(self):
        return self.__marginHeight

    @marginHeight.setter
    def marginHeight(self, marginHeight: int):
        self.__marginHeight = marginHeight


    @property
    def marginWidth(self):
        return self.__marginWidth

    @marginWidth.setter
    def marginWidth(self, marginWidth: int):
        self.__marginWidth = marginWidth


    @property
    def orientationStyle(self):
        return self.__orientationStyle

    @orientationStyle.setter
    def orientationStyle(self, orientationStyle: str):
        self.__orientationStyle = orientationStyle


    @property
    def spacing(self):
        return self.__spacing

    @spacing.setter
    def spacing(self, spacing: int):
        self.__spacing = spacing


class swt_GridLayout:

    def __init__(self, numColumns: int, makeColumnsEqualWidth: bool, marginWidth: int, marginHeight: int, marginLeft: int, marginTop: int, marginRight: int, marginBottom: int, horizontalSpacing: int, verticalSpacing: int):
        self.numColumns = numColumns
        self.makeColumnsEqualWidth = makeColumnsEqualWidth
        self.marginWidth = marginWidth
        self.marginHeight = marginHeight
        self.marginLeft = marginLeft
        self.marginTop = marginTop
        self.marginRight = marginRight
        self.marginBottom = marginBottom
        self.horizontalSpacing = horizontalSpacing
        self.verticalSpacing = verticalSpacing
        
        pass
    @property
    def marginBottom(self):
        return self.__marginBottom

    @marginBottom.setter
    def marginBottom(self, marginBottom: int):
        self.__marginBottom = marginBottom


    @property
    def marginHeight(self):
        return self.__marginHeight

    @marginHeight.setter
    def marginHeight(self, marginHeight: int):
        self.__marginHeight = marginHeight


    @property
    def marginWidth(self):
        return self.__marginWidth

    @marginWidth.setter
    def marginWidth(self, marginWidth: int):
        self.__marginWidth = marginWidth


    @property
    def marginTop(self):
        return self.__marginTop

    @marginTop.setter
    def marginTop(self, marginTop: int):
        self.__marginTop = marginTop


    @property
    def numColumns(self):
        return self.__numColumns

    @numColumns.setter
    def numColumns(self, numColumns: int):
        self.__numColumns = numColumns


    @property
    def marginLeft(self):
        return self.__marginLeft

    @marginLeft.setter
    def marginLeft(self, marginLeft: int):
        self.__marginLeft = marginLeft


    @property
    def horizontalSpacing(self):
        return self.__horizontalSpacing

    @horizontalSpacing.setter
    def horizontalSpacing(self, horizontalSpacing: int):
        self.__horizontalSpacing = horizontalSpacing


    @property
    def makeColumnsEqualWidth(self):
        return self.__makeColumnsEqualWidth

    @makeColumnsEqualWidth.setter
    def makeColumnsEqualWidth(self, makeColumnsEqualWidth: bool):
        self.__makeColumnsEqualWidth = makeColumnsEqualWidth


    @property
    def marginRight(self):
        return self.__marginRight

    @marginRight.setter
    def marginRight(self, marginRight: int):
        self.__marginRight = marginRight


    @property
    def verticalSpacing(self):
        return self.__verticalSpacing

    @verticalSpacing.setter
    def verticalSpacing(self, verticalSpacing: int):
        self.__verticalSpacing = verticalSpacing


class LayoutData:

    pass
class swt_FormData(LayoutData):

    def __init__(self, width: int, height: int, swt_FormData: "swt_FormAttachment" = None, swt_FormData26: "swt_FormAttachment" = None, swt_FormData29: "swt_FormAttachment" = None, swt_FormData32: "swt_FormAttachment" = None):
        self.width = width
        self.height = height
        self.swt_FormData = swt_FormData
        self.swt_FormData26 = swt_FormData26
        self.swt_FormData29 = swt_FormData29
        self.swt_FormData32 = swt_FormData32
        
        pass
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width


    @property
    def swt_FormData(self):
        return self.__swt_FormData

    @swt_FormData.setter
    def swt_FormData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_FormData__swt_FormData", None)
        self.__swt_FormData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_FormAttachment"):
                opp_val = getattr(old_value, "swt_FormAttachment", None)
                if opp_val == self:
                    setattr(old_value, "swt_FormAttachment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_FormAttachment"):
                opp_val = getattr(value, "swt_FormAttachment", None)
                setattr(value, "swt_FormAttachment", self)

    @property
    def swt_FormData26(self):
        return self.__swt_FormData26

    @swt_FormData26.setter
    def swt_FormData26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_FormData__swt_FormData26", None)
        self.__swt_FormData26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_FormAttachment27"):
                opp_val = getattr(old_value, "swt_FormAttachment27", None)
                if opp_val == self:
                    setattr(old_value, "swt_FormAttachment27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_FormAttachment27"):
                opp_val = getattr(value, "swt_FormAttachment27", None)
                setattr(value, "swt_FormAttachment27", self)

    @property
    def swt_FormData32(self):
        return self.__swt_FormData32

    @swt_FormData32.setter
    def swt_FormData32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_FormData__swt_FormData32", None)
        self.__swt_FormData32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_FormAttachment33"):
                opp_val = getattr(old_value, "swt_FormAttachment33", None)
                if opp_val == self:
                    setattr(old_value, "swt_FormAttachment33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_FormAttachment33"):
                opp_val = getattr(value, "swt_FormAttachment33", None)
                setattr(value, "swt_FormAttachment33", self)

    @property
    def swt_FormData29(self):
        return self.__swt_FormData29

    @swt_FormData29.setter
    def swt_FormData29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_FormData__swt_FormData29", None)
        self.__swt_FormData29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_FormAttachment30"):
                opp_val = getattr(old_value, "swt_FormAttachment30", None)
                if opp_val == self:
                    setattr(old_value, "swt_FormAttachment30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_FormAttachment30"):
                opp_val = getattr(value, "swt_FormAttachment30", None)
                setattr(value, "swt_FormAttachment30", self)

class swt_GridData(LayoutData):

    def __init__(self, verticalAlignment: str, horizontalAlignment: str, widthHint: int, heightHint: int, horizontalIndent: int, verticalIndent: int, horizontalSpan: int, verticalSpan: int, grabExcessHorizontalSpace: bool, grabExcessVerticalSpace: bool, minimumWidth: int, minimumHeight: int, exclude: bool):
        self.verticalAlignment = verticalAlignment
        self.horizontalAlignment = horizontalAlignment
        self.widthHint = widthHint
        self.heightHint = heightHint
        self.horizontalIndent = horizontalIndent
        self.verticalIndent = verticalIndent
        self.horizontalSpan = horizontalSpan
        self.verticalSpan = verticalSpan
        self.grabExcessHorizontalSpace = grabExcessHorizontalSpace
        self.grabExcessVerticalSpace = grabExcessVerticalSpace
        self.minimumWidth = minimumWidth
        self.minimumHeight = minimumHeight
        self.exclude = exclude
        
        pass
    @property
    def minimumWidth(self):
        return self.__minimumWidth

    @minimumWidth.setter
    def minimumWidth(self, minimumWidth: int):
        self.__minimumWidth = minimumWidth


    @property
    def horizontalIndent(self):
        return self.__horizontalIndent

    @horizontalIndent.setter
    def horizontalIndent(self, horizontalIndent: int):
        self.__horizontalIndent = horizontalIndent


    @property
    def verticalSpan(self):
        return self.__verticalSpan

    @verticalSpan.setter
    def verticalSpan(self, verticalSpan: int):
        self.__verticalSpan = verticalSpan


    @property
    def heightHint(self):
        return self.__heightHint

    @heightHint.setter
    def heightHint(self, heightHint: int):
        self.__heightHint = heightHint


    @property
    def exclude(self):
        return self.__exclude

    @exclude.setter
    def exclude(self, exclude: bool):
        self.__exclude = exclude


    @property
    def horizontalAlignment(self):
        return self.__horizontalAlignment

    @horizontalAlignment.setter
    def horizontalAlignment(self, horizontalAlignment: str):
        self.__horizontalAlignment = horizontalAlignment


    @property
    def grabExcessVerticalSpace(self):
        return self.__grabExcessVerticalSpace

    @grabExcessVerticalSpace.setter
    def grabExcessVerticalSpace(self, grabExcessVerticalSpace: bool):
        self.__grabExcessVerticalSpace = grabExcessVerticalSpace


    @property
    def grabExcessHorizontalSpace(self):
        return self.__grabExcessHorizontalSpace

    @grabExcessHorizontalSpace.setter
    def grabExcessHorizontalSpace(self, grabExcessHorizontalSpace: bool):
        self.__grabExcessHorizontalSpace = grabExcessHorizontalSpace


    @property
    def verticalAlignment(self):
        return self.__verticalAlignment

    @verticalAlignment.setter
    def verticalAlignment(self, verticalAlignment: str):
        self.__verticalAlignment = verticalAlignment


    @property
    def verticalIndent(self):
        return self.__verticalIndent

    @verticalIndent.setter
    def verticalIndent(self, verticalIndent: int):
        self.__verticalIndent = verticalIndent


    @property
    def horizontalSpan(self):
        return self.__horizontalSpan

    @horizontalSpan.setter
    def horizontalSpan(self, horizontalSpan: int):
        self.__horizontalSpan = horizontalSpan


    @property
    def widthHint(self):
        return self.__widthHint

    @widthHint.setter
    def widthHint(self, widthHint: int):
        self.__widthHint = widthHint


    @property
    def minimumHeight(self):
        return self.__minimumHeight

    @minimumHeight.setter
    def minimumHeight(self, minimumHeight: int):
        self.__minimumHeight = minimumHeight


class swt_RowData(LayoutData):

    def __init__(self, width: int, height: int, exclude: bool):
        self.width = width
        self.height = height
        self.exclude = exclude
        
        pass
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height


    @property
    def exclude(self):
        return self.__exclude

    @exclude.setter
    def exclude(self, exclude: bool):
        self.__exclude = exclude


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width


class AbstractList:

    pass
class swt_List(AbstractList):

    def __init__(self, multiplicityStyle: str, selectionIndices: int, selection: str):
        self.multiplicityStyle = multiplicityStyle
        self.selectionIndices = selectionIndices
        self.selection = selection
        
        pass
    @property
    def multiplicityStyle(self):
        return self.__multiplicityStyle

    @multiplicityStyle.setter
    def multiplicityStyle(self, multiplicityStyle: str):
        self.__multiplicityStyle = multiplicityStyle


    @property
    def selection(self):
        return self.__selection

    @selection.setter
    def selection(self, selection: str):
        self.__selection = selection


    @property
    def selectionIndices(self):
        return self.__selectionIndices

    @selectionIndices.setter
    def selectionIndices(self, selectionIndices: int):
        self.__selectionIndices = selectionIndices


class swt_AbstractList(Control):

    def __init__(self, items: str, selectionIndex: int):
        self.items = items
        self.selectionIndex = selectionIndex
        
        pass
    @property
    def selectionIndex(self):
        return self.__selectionIndex

    @selectionIndex.setter
    def selectionIndex(self, selectionIndex: int):
        self.__selectionIndex = selectionIndex


    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, items: str):
        self.__items = items


class swt_Browser(Control):

    def __init__(self, javascriptEnabled: bool, text: str, url: str):
        self.javascriptEnabled = javascriptEnabled
        self.text = text
        self.url = url
        
        pass
    @property
    def javascriptEnabled(self):
        return self.__javascriptEnabled

    @javascriptEnabled.setter
    def javascriptEnabled(self, javascriptEnabled: bool):
        self.__javascriptEnabled = javascriptEnabled


    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url


class swt_DateTime(Control):

    def __init__(self, seconds: int, minutes: int, hours: int, day: int, month: int, year: int):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours
        self.day = day
        self.month = month
        self.year = year
        
        pass
    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month: int):
        self.__month = month


    @property
    def minutes(self):
        return self.__minutes

    @minutes.setter
    def minutes(self, minutes: int):
        self.__minutes = minutes


    @property
    def seconds(self):
        return self.__seconds

    @seconds.setter
    def seconds(self, seconds: int):
        self.__seconds = seconds


    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year


    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, hours: int):
        self.__hours = hours


    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day: int):
        self.__day = day


class Color:

    pass
class swt_RGBColor(Color):

    def __init__(self, red: int, green: int, blue: int):
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
    def blue(self):
        return self.__blue

    @blue.setter
    def blue(self, blue: int):
        self.__blue = blue


    @property
    def red(self):
        return self.__red

    @red.setter
    def red(self, red: int):
        self.__red = red


class swt_SystemColor(Color):

    def __init__(self, color: str):
        self.color = color
        
        pass
    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color


class swt_TabItem(Item):

    def __init__(self, toolTipText: str, swt_TabItem: "swt_TabFolder" = None, swt_TabItem22: "swt_Control" = None):
        self.toolTipText = toolTipText
        self.swt_TabItem = swt_TabItem
        self.swt_TabItem22 = swt_TabItem22
        
        pass
    @property
    def toolTipText(self):
        return self.__toolTipText

    @toolTipText.setter
    def toolTipText(self, toolTipText: str):
        self.__toolTipText = toolTipText


    @property
    def swt_TabItem22(self):
        return self.__swt_TabItem22

    @swt_TabItem22.setter
    def swt_TabItem22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_TabItem__swt_TabItem22", None)
        self.__swt_TabItem22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_Control23"):
                opp_val = getattr(old_value, "swt_Control23", None)
                if opp_val == self:
                    setattr(old_value, "swt_Control23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_Control23"):
                opp_val = getattr(value, "swt_Control23", None)
                setattr(value, "swt_Control23", self)

    @property
    def swt_TabItem(self):
        return self.__swt_TabItem

    @swt_TabItem.setter
    def swt_TabItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_swt_TabItem__swt_TabItem", None)
        self.__swt_TabItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "swt_TabFolder"):
                opp_val = getattr(old_value, "swt_TabFolder", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "swt_TabFolder"):
                opp_val = getattr(value, "swt_TabFolder", None)
                if opp_val is None:
                    setattr(value, "swt_TabFolder", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class swt_TabFolder(Control):

    pass
class swt_Combo(AbstractList):

    def __init__(self, text: str, textLimit: int):
        self.text = text
        self.textLimit = textLimit
        
        pass
    @property
    def textLimit(self):
        return self.__textLimit

    @textLimit.setter
    def textLimit(self, textLimit: int):
        self.__textLimit = textLimit


    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

