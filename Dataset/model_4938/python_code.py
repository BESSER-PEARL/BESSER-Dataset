from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ObjectAlign(Enum):
    default = "default"
    baseline = "baseline"
    top = "top"
    middle = "middle"
    bottom = "bottom"
    textTop = "textTop"
    absoluteMiddle = "absoluteMiddle"
    absoluteBottom = "absoluteBottom"
    left = "left"
    right = "right"
class LogicalOperator(Enum):
    AND = "AND"
    OR = "OR"
class Align(Enum):
    left = "left"
    right = "right"
    center = "center"
    justify = "justify"
class Extension(Enum):
    html = "html"
    xhtml = "xhtml"
    jsp = "jsp"
    php = "php"
    asp = "asp"
class ButtonType(Enum):
    Submit = "Submit"
    Reset = "Reset"
    Push = "Push"
class SubmitFormMethod(Enum):
    post = "post"
    get = "get"
class UnorderedListType(Enum):
    disc = "disc"
    circle = "circle"
    square = "square"
    none = "none"
class ScriptType(Enum):
    textJavaScript = "textJavaScript"
    textTcl = "textTcl"
    textVBScript = "textVBScript"
class MessageDialogEvent(Enum):
    closeDialog = "closeDialog"
class DateFormat(Enum):
    Default = "Default"
    ISO8601 = "ISO8601"
    Short = "Short"
    Medium = "Medium"
    Full = "Full"
class OrderedListType(Enum):
    ArabicNumber = "ArabicNumber"
    LowerAlpha = "LowerAlpha"
    UpperAlpha = "UpperAlpha"
    LowerRoman = "LowerRoman"
    UpperRoman = "UpperRoman"
    none = "none"
class Orientation(Enum):
    Vertical = "Vertical"
    Horizontal = "Horizontal"
class PhraseElementType(Enum):
    Emphasis = "Emphasis"
    StrongerEmphasis = "StrongerEmphasis"
    Citation = "Citation"
    Definition = "Definition"
    ComputerCode = "ComputerCode"
    SampleProgramOutput = "SampleProgramOutput"
    EntryFromUser = "EntryFromUser"
    VariableInstance = "VariableInstance"
    Abbreviation = "Abbreviation"
    Acronym = "Acronym"
    None = "None"
class Locale(Enum):
    English_UK = "English_UK"
    Spanish = "Spanish"
    German = "German"
    Portuguese_Brazilian = "Portuguese_Brazilian"
class EventType(Enum):
    onload = "onload"
    onunload = "onunload"
    onclick = "onclick"
    ondblclick = "ondblclick"
    onmousedown = "onmousedown"
    onmouseup = "onmouseup"
    onmouseover = "onmouseover"
    onmousemove = "onmousemove"
    onmouseout = "onmouseout"
    onfocus = "onfocus"
    onblur = "onblur"
    onkeypress = "onkeypress"
    onkeydown = "onkeydown"
    onkeyup = "onkeyup"
    onsubmit = "onsubmit"
    onreset = "onreset"
    onselect = "onselect"
    onchange = "onchange"
class HeadingLevel(Enum):
    h1 = "h1"
    h2 = "h2"
    h3 = "h3"
    h4 = "h4"
    h5 = "h5"
    h6 = "h6"
class FieldSetLegendAlign(Enum):
    left = "left"
    right = "right"
    center = "center"
    bottom = "bottom"
    top = "top"
class MatchingOperator(Enum):
    Contains = "Contains"
    Equals = "Equals"
    GreaterThan = "GreaterThan"
    LessThan = "LessThan"
    GreaterOrEqualsThan = "GreaterOrEqualsThan"
    LessOrEqualsThan = "LessOrEqualsThan"
    Different = "Different"


############################################
# Definition of Classes
############################################

class ric_ListItem:

    def __init__(self, text: str, format: str, ric_ListItem: "ric_OrderedList" = None, ric_ListItem192: "ric_UnorderedList" = None):
        self.text = text
        self.format = format
        self.ric_ListItem = ric_ListItem
        self.ric_ListItem192 = ric_ListItem192
        
    @property
    def format(self) -> str:
        return self.__format

    @format.setter
    def format(self, format: str):
        self.__format = format

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def ric_ListItem(self):
        return self.__ric_ListItem

    @ric_ListItem.setter
    def ric_ListItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_ListItem__ric_ListItem", None)
        self.__ric_ListItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_OrderedList"):
                opp_val = getattr(old_value, "ric_OrderedList", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_OrderedList"):
                opp_val = getattr(value, "ric_OrderedList", None)
                if opp_val is None:
                    setattr(value, "ric_OrderedList", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ric_ListItem192(self):
        return self.__ric_ListItem192

    @ric_ListItem192.setter
    def ric_ListItem192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_ListItem__ric_ListItem192", None)
        self.__ric_ListItem192 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_UnorderedList"):
                opp_val = getattr(old_value, "ric_UnorderedList", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_UnorderedList"):
                opp_val = getattr(value, "ric_UnorderedList", None)
                if opp_val is None:
                    setattr(value, "ric_UnorderedList", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class List:

    pass
class ric_UnorderedList(List):

    def __init__(self, type: str, ric_UnorderedList: set["ric_ListItem"] = None):
        self.type = type
        self.ric_UnorderedList = ric_UnorderedList if ric_UnorderedList is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def ric_UnorderedList(self):
        return self.__ric_UnorderedList

    @ric_UnorderedList.setter
    def ric_UnorderedList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_UnorderedList__ric_UnorderedList", None)
        self.__ric_UnorderedList = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ric_ListItem192"):
                    opp_val = getattr(item, "ric_ListItem192", None)
                    
                    if opp_val == self:
                        setattr(item, "ric_ListItem192", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ric_ListItem192"):
                    opp_val = getattr(item, "ric_ListItem192", None)
                    
                    setattr(item, "ric_ListItem192", self)
                    

class ric_OrderedList(List):

    def __init__(self, type: str, ric_OrderedList: set["ric_ListItem"] = None):
        self.type = type
        self.ric_OrderedList = ric_OrderedList if ric_OrderedList is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def ric_OrderedList(self):
        return self.__ric_OrderedList

    @ric_OrderedList.setter
    def ric_OrderedList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_OrderedList__ric_OrderedList", None)
        self.__ric_OrderedList = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ric_ListItem"):
                    opp_val = getattr(item, "ric_ListItem", None)
                    
                    if opp_val == self:
                        setattr(item, "ric_ListItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ric_ListItem"):
                    opp_val = getattr(item, "ric_ListItem", None)
                    
                    setattr(item, "ric_ListItem", self)
                    

class ric_LinkGroup:

    def __init__(self, title: str, ric_LinkGroup: "ric_NavigationRegion" = None, ric_LinkGroup204: set["ric_Link"] = None, ric_LinkGroup208: "ric_LinkGroup" = None, ric_LinkGroup206: set["ric_LinkGroup"] = None):
        self.title = title
        self.ric_LinkGroup = ric_LinkGroup
        self.ric_LinkGroup204 = ric_LinkGroup204 if ric_LinkGroup204 is not None else set()
        self.ric_LinkGroup208 = ric_LinkGroup208
        self.ric_LinkGroup206 = ric_LinkGroup206 if ric_LinkGroup206 is not None else set()
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def ric_LinkGroup204(self):
        return self.__ric_LinkGroup204

    @ric_LinkGroup204.setter
    def ric_LinkGroup204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_LinkGroup__ric_LinkGroup204", None)
        self.__ric_LinkGroup204 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ric_Link205"):
                    opp_val = getattr(item, "ric_Link205", None)
                    
                    if opp_val == self:
                        setattr(item, "ric_Link205", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ric_Link205"):
                    opp_val = getattr(item, "ric_Link205", None)
                    
                    setattr(item, "ric_Link205", self)
                    

    @property
    def ric_LinkGroup206(self):
        return self.__ric_LinkGroup206

    @ric_LinkGroup206.setter
    def ric_LinkGroup206(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_LinkGroup__ric_LinkGroup206", None)
        self.__ric_LinkGroup206 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ric_LinkGroup208"):
                    opp_val = getattr(item, "ric_LinkGroup208", None)
                    
                    if opp_val == self:
                        setattr(item, "ric_LinkGroup208", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ric_LinkGroup208"):
                    opp_val = getattr(item, "ric_LinkGroup208", None)
                    
                    setattr(item, "ric_LinkGroup208", self)
                    

    @property
    def ric_LinkGroup208(self):
        return self.__ric_LinkGroup208

    @ric_LinkGroup208.setter
    def ric_LinkGroup208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_LinkGroup__ric_LinkGroup208", None)
        self.__ric_LinkGroup208 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_LinkGroup206"):
                opp_val = getattr(old_value, "ric_LinkGroup206", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_LinkGroup206"):
                opp_val = getattr(value, "ric_LinkGroup206", None)
                if opp_val is None:
                    setattr(value, "ric_LinkGroup206", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ric_LinkGroup(self):
        return self.__ric_LinkGroup

    @ric_LinkGroup.setter
    def ric_LinkGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_LinkGroup__ric_LinkGroup", None)
        self.__ric_LinkGroup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_NavigationRegion126"):
                opp_val = getattr(old_value, "ric_NavigationRegion126", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_NavigationRegion126"):
                opp_val = getattr(value, "ric_NavigationRegion126", None)
                if opp_val is None:
                    setattr(value, "ric_NavigationRegion126", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ric_Logo:

    pass
class ric_FooterRegion:

    pass
class ric_ContentRegion:

    pass
class ric_SearchRegion:

    pass
class ric_ContextualNavigationRegion:

    pass
class ric_NavigationRegion:

    def __init__(self, orientation: str, ric_NavigationRegion: "ric_Portal" = None, ric_NavigationRegion126: set["ric_LinkGroup"] = None, ric_NavigationRegion116: "ric_HeaderRegion" = None):
        self.orientation = orientation
        self.ric_NavigationRegion = ric_NavigationRegion
        self.ric_NavigationRegion126 = ric_NavigationRegion126 if ric_NavigationRegion126 is not None else set()
        self.ric_NavigationRegion116 = ric_NavigationRegion116
        
    @property
    def orientation(self) -> str:
        return self.__orientation

    @orientation.setter
    def orientation(self, orientation: str):
        self.__orientation = orientation

    @property
    def ric_NavigationRegion116(self):
        return self.__ric_NavigationRegion116

    @ric_NavigationRegion116.setter
    def ric_NavigationRegion116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_NavigationRegion__ric_NavigationRegion116", None)
        self.__ric_NavigationRegion116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_HeaderRegion115"):
                opp_val = getattr(old_value, "ric_HeaderRegion115", None)
                if opp_val == self:
                    setattr(old_value, "ric_HeaderRegion115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_HeaderRegion115"):
                opp_val = getattr(value, "ric_HeaderRegion115", None)
                setattr(value, "ric_HeaderRegion115", self)

    @property
    def ric_NavigationRegion126(self):
        return self.__ric_NavigationRegion126

    @ric_NavigationRegion126.setter
    def ric_NavigationRegion126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_NavigationRegion__ric_NavigationRegion126", None)
        self.__ric_NavigationRegion126 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ric_LinkGroup"):
                    opp_val = getattr(item, "ric_LinkGroup", None)
                    
                    if opp_val == self:
                        setattr(item, "ric_LinkGroup", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ric_LinkGroup"):
                    opp_val = getattr(item, "ric_LinkGroup", None)
                    
                    setattr(item, "ric_LinkGroup", self)
                    

    @property
    def ric_NavigationRegion(self):
        return self.__ric_NavigationRegion

    @ric_NavigationRegion.setter
    def ric_NavigationRegion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_NavigationRegion__ric_NavigationRegion", None)
        self.__ric_NavigationRegion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_Portal103"):
                opp_val = getattr(old_value, "ric_Portal103", None)
                if opp_val == self:
                    setattr(old_value, "ric_Portal103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_Portal103"):
                opp_val = getattr(value, "ric_Portal103", None)
                setattr(value, "ric_Portal103", self)

class ric_HeaderRegion:

    pass
class ric_Portal:

    def __init__(self, name: str, documentsExtension: str, ric_Portal: "ric_HeaderRegion" = None, ric_Portal103: "ric_NavigationRegion" = None, ric_Portal105: "ric_ContextualNavigationRegion" = None, ric_Portal107: "ric_SearchRegion" = None, ric_Portal109: "ric_ContentRegion" = None, ric_Portal111: "ric_FooterRegion" = None):
        self.name = name
        self.documentsExtension = documentsExtension
        self.ric_Portal = ric_Portal
        self.ric_Portal103 = ric_Portal103
        self.ric_Portal105 = ric_Portal105
        self.ric_Portal107 = ric_Portal107
        self.ric_Portal109 = ric_Portal109
        self.ric_Portal111 = ric_Portal111
        
    @property
    def documentsExtension(self) -> str:
        return self.__documentsExtension

    @documentsExtension.setter
    def documentsExtension(self, documentsExtension: str):
        self.__documentsExtension = documentsExtension

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ric_Portal105(self):
        return self.__ric_Portal105

    @ric_Portal105.setter
    def ric_Portal105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Portal__ric_Portal105", None)
        self.__ric_Portal105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_ContextualNavigationRegion"):
                opp_val = getattr(old_value, "ric_ContextualNavigationRegion", None)
                if opp_val == self:
                    setattr(old_value, "ric_ContextualNavigationRegion", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_ContextualNavigationRegion"):
                opp_val = getattr(value, "ric_ContextualNavigationRegion", None)
                setattr(value, "ric_ContextualNavigationRegion", self)

    @property
    def ric_Portal(self):
        return self.__ric_Portal

    @ric_Portal.setter
    def ric_Portal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Portal__ric_Portal", None)
        self.__ric_Portal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_HeaderRegion"):
                opp_val = getattr(old_value, "ric_HeaderRegion", None)
                if opp_val == self:
                    setattr(old_value, "ric_HeaderRegion", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_HeaderRegion"):
                opp_val = getattr(value, "ric_HeaderRegion", None)
                setattr(value, "ric_HeaderRegion", self)

    @property
    def ric_Portal111(self):
        return self.__ric_Portal111

    @ric_Portal111.setter
    def ric_Portal111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Portal__ric_Portal111", None)
        self.__ric_Portal111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_FooterRegion"):
                opp_val = getattr(old_value, "ric_FooterRegion", None)
                if opp_val == self:
                    setattr(old_value, "ric_FooterRegion", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_FooterRegion"):
                opp_val = getattr(value, "ric_FooterRegion", None)
                setattr(value, "ric_FooterRegion", self)

    @property
    def ric_Portal109(self):
        return self.__ric_Portal109

    @ric_Portal109.setter
    def ric_Portal109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Portal__ric_Portal109", None)
        self.__ric_Portal109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_ContentRegion"):
                opp_val = getattr(old_value, "ric_ContentRegion", None)
                if opp_val == self:
                    setattr(old_value, "ric_ContentRegion", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_ContentRegion"):
                opp_val = getattr(value, "ric_ContentRegion", None)
                setattr(value, "ric_ContentRegion", self)

    @property
    def ric_Portal103(self):
        return self.__ric_Portal103

    @ric_Portal103.setter
    def ric_Portal103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Portal__ric_Portal103", None)
        self.__ric_Portal103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_NavigationRegion"):
                opp_val = getattr(old_value, "ric_NavigationRegion", None)
                if opp_val == self:
                    setattr(old_value, "ric_NavigationRegion", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_NavigationRegion"):
                opp_val = getattr(value, "ric_NavigationRegion", None)
                setattr(value, "ric_NavigationRegion", self)

    @property
    def ric_Portal107(self):
        return self.__ric_Portal107

    @ric_Portal107.setter
    def ric_Portal107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Portal__ric_Portal107", None)
        self.__ric_Portal107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_SearchRegion"):
                opp_val = getattr(old_value, "ric_SearchRegion", None)
                if opp_val == self:
                    setattr(old_value, "ric_SearchRegion", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_SearchRegion"):
                opp_val = getattr(value, "ric_SearchRegion", None)
                setattr(value, "ric_SearchRegion", self)

class FormControlConstraint:

    pass
class ric_FormControlConstraint(ABC):

    pass
class TextField:

    pass
class ric_MessageDialogButton:

    def __init__(self, label: str, event: str, ric_MessageDialogButton: "ric_MessageDialog" = None):
        self.label = label
        self.event = event
        self.ric_MessageDialogButton = ric_MessageDialogButton
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def event(self) -> str:
        return self.__event

    @event.setter
    def event(self, event: str):
        self.__event = event

    @property
    def ric_MessageDialogButton(self):
        return self.__ric_MessageDialogButton

    @ric_MessageDialogButton.setter
    def ric_MessageDialogButton(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_MessageDialogButton__ric_MessageDialogButton", None)
        self.__ric_MessageDialogButton = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_MessageDialog"):
                opp_val = getattr(old_value, "ric_MessageDialog", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_MessageDialog"):
                opp_val = getattr(value, "ric_MessageDialog", None)
                if opp_val is None:
                    setattr(value, "ric_MessageDialog", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ric_Section:

    def __init__(self, title: str, ric_Section: "ric_AccordionPanel" = None, ric_Section80: set["ric_InlineComponent"] = None, ric_Section83: set["ric_BlockLevelComponent"] = None, ric_Section86: set["ric_ObjectComponent"] = None, ric_Section89: set["ric_LineBreak"] = None, ric_Section92: set["ric_RichWidget"] = None, ric_Section95: set["ric_List"] = None, ric_Section98: set["ric_Form"] = None):
        self.title = title
        self.ric_Section = ric_Section
        self.ric_Section80 = ric_Section80 if ric_Section80 is not None else set()
        self.ric_Section83 = ric_Section83 if ric_Section83 is not None else set()
        self.ric_Section86 = ric_Section86 if ric_Section86 is not None else set()
        self.ric_Section89 = ric_Section89 if ric_Section89 is not None else set()
        self.ric_Section92 = ric_Section92 if ric_Section92 is not None else set()
        self.ric_Section95 = ric_Section95 if ric_Section95 is not None else set()
        self.ric_Section98 = ric_Section98 if ric_Section98 is not None else set()
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def ric_Section83(self):
        return self.__ric_Section83

    @ric_Section83.setter
    def ric_Section83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Section__ric_Section83", None)
        self.__ric_Section83 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ric_BlockLevelComponent84"):
                    opp_val = getattr(item, "ric_BlockLevelComponent84", None)
                    
                    if opp_val == self:
                        setattr(item, "ric_BlockLevelComponent84", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ric_BlockLevelComponent84"):
                    opp_val = getattr(item, "ric_BlockLevelComponent84", None)
                    
                    setattr(item, "ric_BlockLevelComponent84", self)
                    

    @property
    def ric_Section95(self):
        return self.__ric_Section95

    @ric_Section95.setter
    def ric_Section95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Section__ric_Section95", None)
        self.__ric_Section95 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ric_List96"):
                    opp_val = getattr(item, "ric_List96", None)
                    
                    if opp_val == self:
                        setattr(item, "ric_List96", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ric_List96"):
                    opp_val = getattr(item, "ric_List96", None)
                    
                    setattr(item, "ric_List96", self)
                    

    @property
    def ric_Section98(self):
        return self.__ric_Section98

    @ric_Section98.setter
    def ric_Section98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Section__ric_Section98", None)
        self.__ric_Section98 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ric_Form99"):
                    opp_val = getattr(item, "ric_Form99", None)
                    
                    if opp_val == self:
                        setattr(item, "ric_Form99", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ric_Form99"):
                    opp_val = getattr(item, "ric_Form99", None)
                    
                    setattr(item, "ric_Form99", self)
                    

    @property
    def ric_Section92(self):
        return self.__ric_Section92

    @ric_Section92.setter
    def ric_Section92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Section__ric_Section92", None)
        self.__ric_Section92 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ric_RichWidget93"):
                    opp_val = getattr(item, "ric_RichWidget93", None)
                    
                    if opp_val == self:
                        setattr(item, "ric_RichWidget93", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ric_RichWidget93"):
                    opp_val = getattr(item, "ric_RichWidget93", None)
                    
                    setattr(item, "ric_RichWidget93", self)
                    

    @property
    def ric_Section(self):
        return self.__ric_Section

    @ric_Section.setter
    def ric_Section(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Section__ric_Section", None)
        self.__ric_Section = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_AccordionPanel"):
                opp_val = getattr(old_value, "ric_AccordionPanel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_AccordionPanel"):
                opp_val = getattr(value, "ric_AccordionPanel", None)
                if opp_val is None:
                    setattr(value, "ric_AccordionPanel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ric_Section80(self):
        return self.__ric_Section80

    @ric_Section80.setter
    def ric_Section80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Section__ric_Section80", None)
        self.__ric_Section80 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ric_InlineComponent81"):
                    opp_val = getattr(item, "ric_InlineComponent81", None)
                    
                    if opp_val == self:
                        setattr(item, "ric_InlineComponent81", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ric_InlineComponent81"):
                    opp_val = getattr(item, "ric_InlineComponent81", None)
                    
                    setattr(item, "ric_InlineComponent81", self)
                    

    @property
    def ric_Section86(self):
        return self.__ric_Section86

    @ric_Section86.setter
    def ric_Section86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Section__ric_Section86", None)
        self.__ric_Section86 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ric_ObjectComponent87"):
                    opp_val = getattr(item, "ric_ObjectComponent87", None)
                    
                    if opp_val == self:
                        setattr(item, "ric_ObjectComponent87", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ric_ObjectComponent87"):
                    opp_val = getattr(item, "ric_ObjectComponent87", None)
                    
                    setattr(item, "ric_ObjectComponent87", self)
                    

    @property
    def ric_Section89(self):
        return self.__ric_Section89

    @ric_Section89.setter
    def ric_Section89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Section__ric_Section89", None)
        self.__ric_Section89 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ric_LineBreak90"):
                    opp_val = getattr(item, "ric_LineBreak90", None)
                    
                    if opp_val == self:
                        setattr(item, "ric_LineBreak90", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ric_LineBreak90"):
                    opp_val = getattr(item, "ric_LineBreak90", None)
                    
                    setattr(item, "ric_LineBreak90", self)
                    

class ric_Tab:

    def __init__(self, title: str, ric_Tab: "ric_TabbedPanel" = None, ric_Tab61: set["ric_BlockLevelComponent"] = None, ric_Tab64: set["ric_ObjectComponent"] = None, ric_Tab67: set["ric_LineBreak"] = None, ric_Tab70: set["ric_RichWidget"] = None, ric_Tab73: set["ric_List"] = None, ric_Tab76: set["ric_Form"] = None, ric_Tab58: set["ric_InlineComponent"] = None):
        self.title = title
        self.ric_Tab = ric_Tab
        self.ric_Tab61 = ric_Tab61 if ric_Tab61 is not None else set()
        self.ric_Tab64 = ric_Tab64 if ric_Tab64 is not None else set()
        self.ric_Tab67 = ric_Tab67 if ric_Tab67 is not None else set()
        self.ric_Tab70 = ric_Tab70 if ric_Tab70 is not None else set()
        self.ric_Tab73 = ric_Tab73 if ric_Tab73 is not None else set()
        self.ric_Tab76 = ric_Tab76 if ric_Tab76 is not None else set()
        self.ric_Tab58 = ric_Tab58 if ric_Tab58 is not None else set()
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def ric_Tab(self):
        return self.__ric_Tab

    @ric_Tab.setter
    def ric_Tab(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Tab__ric_Tab", None)
        self.__ric_Tab = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_TabbedPanel"):
                opp_val = getattr(old_value, "ric_TabbedPanel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_TabbedPanel"):
                opp_val = getattr(value, "ric_TabbedPanel", None)
                if opp_val is None:
                    setattr(value, "ric_TabbedPanel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ric_Tab64(self):
        return self.__ric_Tab64

    @ric_Tab64.setter
    def ric_Tab64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Tab__ric_Tab64", None)
        self.__ric_Tab64 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ric_ObjectComponent65"):
                    opp_val = getattr(item, "ric_ObjectComponent65", None)
                    
                    if opp_val == self:
                        setattr(item, "ric_ObjectComponent65", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ric_ObjectComponent65"):
                    opp_val = getattr(item, "ric_ObjectComponent65", None)
                    
                    setattr(item, "ric_ObjectComponent65", self)
                    

    @property
    def ric_Tab67(self):
        return self.__ric_Tab67

    @ric_Tab67.setter
    def ric_Tab67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Tab__ric_Tab67", None)
        self.__ric_Tab67 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ric_LineBreak68"):
                    opp_val = getattr(item, "ric_LineBreak68", None)
                    
                    if opp_val == self:
                        setattr(item, "ric_LineBreak68", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ric_LineBreak68"):
                    opp_val = getattr(item, "ric_LineBreak68", None)
                    
                    setattr(item, "ric_LineBreak68", self)
                    

    @property
    def ric_Tab70(self):
        return self.__ric_Tab70

    @ric_Tab70.setter
    def ric_Tab70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Tab__ric_Tab70", None)
        self.__ric_Tab70 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ric_RichWidget71"):
                    opp_val = getattr(item, "ric_RichWidget71", None)
                    
                    if opp_val == self:
                        setattr(item, "ric_RichWidget71", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ric_RichWidget71"):
                    opp_val = getattr(item, "ric_RichWidget71", None)
                    
                    setattr(item, "ric_RichWidget71", self)
                    

    @property
    def ric_Tab76(self):
        return self.__ric_Tab76

    @ric_Tab76.setter
    def ric_Tab76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Tab__ric_Tab76", None)
        self.__ric_Tab76 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ric_Form77"):
                    opp_val = getattr(item, "ric_Form77", None)
                    
                    if opp_val == self:
                        setattr(item, "ric_Form77", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ric_Form77"):
                    opp_val = getattr(item, "ric_Form77", None)
                    
                    setattr(item, "ric_Form77", self)
                    

    @property
    def ric_Tab61(self):
        return self.__ric_Tab61

    @ric_Tab61.setter
    def ric_Tab61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Tab__ric_Tab61", None)
        self.__ric_Tab61 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ric_BlockLevelComponent62"):
                    opp_val = getattr(item, "ric_BlockLevelComponent62", None)
                    
                    if opp_val == self:
                        setattr(item, "ric_BlockLevelComponent62", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ric_BlockLevelComponent62"):
                    opp_val = getattr(item, "ric_BlockLevelComponent62", None)
                    
                    setattr(item, "ric_BlockLevelComponent62", self)
                    

    @property
    def ric_Tab73(self):
        return self.__ric_Tab73

    @ric_Tab73.setter
    def ric_Tab73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Tab__ric_Tab73", None)
        self.__ric_Tab73 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ric_List74"):
                    opp_val = getattr(item, "ric_List74", None)
                    
                    if opp_val == self:
                        setattr(item, "ric_List74", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ric_List74"):
                    opp_val = getattr(item, "ric_List74", None)
                    
                    setattr(item, "ric_List74", self)
                    

    @property
    def ric_Tab58(self):
        return self.__ric_Tab58

    @ric_Tab58.setter
    def ric_Tab58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Tab__ric_Tab58", None)
        self.__ric_Tab58 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ric_InlineComponent59"):
                    opp_val = getattr(item, "ric_InlineComponent59", None)
                    
                    if opp_val == self:
                        setattr(item, "ric_InlineComponent59", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ric_InlineComponent59"):
                    opp_val = getattr(item, "ric_InlineComponent59", None)
                    
                    setattr(item, "ric_InlineComponent59", self)
                    

class RichWidget:

    pass
class ric_AccordionPanel(RichWidget):

    pass
class ric_Datepicker(TextField, RichWidget):

    def __init__(self, showButtonImage: bool, dateFormat: str, locale: str, numberMonthsToShow: int, showMonthMenu: bool, showYearMenu: bool, showWeekOfYear: bool, showButtonClosePanel: bool):
        self.showButtonImage = showButtonImage
        self.dateFormat = dateFormat
        self.locale = locale
        self.numberMonthsToShow = numberMonthsToShow
        self.showMonthMenu = showMonthMenu
        self.showYearMenu = showYearMenu
        self.showWeekOfYear = showWeekOfYear
        self.showButtonClosePanel = showButtonClosePanel
        
    @property
    def locale(self) -> str:
        return self.__locale

    @locale.setter
    def locale(self, locale: str):
        self.__locale = locale

    @property
    def showButtonImage(self) -> bool:
        return self.__showButtonImage

    @showButtonImage.setter
    def showButtonImage(self, showButtonImage: bool):
        self.__showButtonImage = showButtonImage

    @property
    def showYearMenu(self) -> bool:
        return self.__showYearMenu

    @showYearMenu.setter
    def showYearMenu(self, showYearMenu: bool):
        self.__showYearMenu = showYearMenu

    @property
    def showWeekOfYear(self) -> bool:
        return self.__showWeekOfYear

    @showWeekOfYear.setter
    def showWeekOfYear(self, showWeekOfYear: bool):
        self.__showWeekOfYear = showWeekOfYear

    @property
    def showMonthMenu(self) -> bool:
        return self.__showMonthMenu

    @showMonthMenu.setter
    def showMonthMenu(self, showMonthMenu: bool):
        self.__showMonthMenu = showMonthMenu

    @property
    def numberMonthsToShow(self) -> int:
        return self.__numberMonthsToShow

    @numberMonthsToShow.setter
    def numberMonthsToShow(self, numberMonthsToShow: int):
        self.__numberMonthsToShow = numberMonthsToShow

    @property
    def showButtonClosePanel(self) -> bool:
        return self.__showButtonClosePanel

    @showButtonClosePanel.setter
    def showButtonClosePanel(self, showButtonClosePanel: bool):
        self.__showButtonClosePanel = showButtonClosePanel

    @property
    def dateFormat(self) -> str:
        return self.__dateFormat

    @dateFormat.setter
    def dateFormat(self, dateFormat: str):
        self.__dateFormat = dateFormat

class ric_MessageDialog(RichWidget):

    def __init__(self, title: str, message: str, modal: bool, autoOpen: bool, resizable: bool, height: int, minHeightResize: int, maxHeightResize: int, width: int, minWidthResize: int, maxWidthResize: int, ric_MessageDialog: set["ric_MessageDialogButton"] = None):
        self.title = title
        self.message = message
        self.modal = modal
        self.autoOpen = autoOpen
        self.resizable = resizable
        self.height = height
        self.minHeightResize = minHeightResize
        self.maxHeightResize = maxHeightResize
        self.width = width
        self.minWidthResize = minWidthResize
        self.maxWidthResize = maxWidthResize
        self.ric_MessageDialog = ric_MessageDialog if ric_MessageDialog is not None else set()
        
    @property
    def resizable(self) -> bool:
        return self.__resizable

    @resizable.setter
    def resizable(self, resizable: bool):
        self.__resizable = resizable

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def modal(self) -> bool:
        return self.__modal

    @modal.setter
    def modal(self, modal: bool):
        self.__modal = modal

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height

    @property
    def maxHeightResize(self) -> int:
        return self.__maxHeightResize

    @maxHeightResize.setter
    def maxHeightResize(self, maxHeightResize: int):
        self.__maxHeightResize = maxHeightResize

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width

    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def maxWidthResize(self) -> int:
        return self.__maxWidthResize

    @maxWidthResize.setter
    def maxWidthResize(self, maxWidthResize: int):
        self.__maxWidthResize = maxWidthResize

    @property
    def minWidthResize(self) -> int:
        return self.__minWidthResize

    @minWidthResize.setter
    def minWidthResize(self, minWidthResize: int):
        self.__minWidthResize = minWidthResize

    @property
    def minHeightResize(self) -> int:
        return self.__minHeightResize

    @minHeightResize.setter
    def minHeightResize(self, minHeightResize: int):
        self.__minHeightResize = minHeightResize

    @property
    def autoOpen(self) -> bool:
        return self.__autoOpen

    @autoOpen.setter
    def autoOpen(self, autoOpen: bool):
        self.__autoOpen = autoOpen

    @property
    def ric_MessageDialog(self):
        return self.__ric_MessageDialog

    @ric_MessageDialog.setter
    def ric_MessageDialog(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_MessageDialog__ric_MessageDialog", None)
        self.__ric_MessageDialog = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ric_MessageDialogButton"):
                    opp_val = getattr(item, "ric_MessageDialogButton", None)
                    
                    if opp_val == self:
                        setattr(item, "ric_MessageDialogButton", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ric_MessageDialogButton"):
                    opp_val = getattr(item, "ric_MessageDialogButton", None)
                    
                    setattr(item, "ric_MessageDialogButton", self)
                    

class ric_TabbedPanel(RichWidget):

    pass
class ObjectComponent:

    pass
class InlineComponent:

    pass
class ric_ObjectComponent(ABC):

    def __init__(self, align: str, width: int, height: int, border: int, hspace: int, vspace: int, ric_ObjectComponent: "ric_Div" = None, ric_ObjectComponent65: "ric_Tab" = None, ric_ObjectComponent87: "ric_Section" = None, ric_ObjectComponent135: "ric_ContextualNavigationRegion" = None, ric_ObjectComponent162: "ric_Document" = None, ric_ObjectComponent183: "ric_FooterRegion" = None):
        self.align = align
        self.width = width
        self.height = height
        self.border = border
        self.hspace = hspace
        self.vspace = vspace
        self.ric_ObjectComponent = ric_ObjectComponent
        self.ric_ObjectComponent65 = ric_ObjectComponent65
        self.ric_ObjectComponent87 = ric_ObjectComponent87
        self.ric_ObjectComponent135 = ric_ObjectComponent135
        self.ric_ObjectComponent162 = ric_ObjectComponent162
        self.ric_ObjectComponent183 = ric_ObjectComponent183
        
    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height

    @property
    def hspace(self) -> int:
        return self.__hspace

    @hspace.setter
    def hspace(self, hspace: int):
        self.__hspace = hspace

    @property
    def border(self) -> int:
        return self.__border

    @border.setter
    def border(self, border: int):
        self.__border = border

    @property
    def vspace(self) -> int:
        return self.__vspace

    @vspace.setter
    def vspace(self, vspace: int):
        self.__vspace = vspace

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        self.__width = width

    @property
    def align(self) -> str:
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align

    @property
    def ric_ObjectComponent65(self):
        return self.__ric_ObjectComponent65

    @ric_ObjectComponent65.setter
    def ric_ObjectComponent65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_ObjectComponent__ric_ObjectComponent65", None)
        self.__ric_ObjectComponent65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_Tab64"):
                opp_val = getattr(old_value, "ric_Tab64", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_Tab64"):
                opp_val = getattr(value, "ric_Tab64", None)
                if opp_val is None:
                    setattr(value, "ric_Tab64", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ric_ObjectComponent135(self):
        return self.__ric_ObjectComponent135

    @ric_ObjectComponent135.setter
    def ric_ObjectComponent135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_ObjectComponent__ric_ObjectComponent135", None)
        self.__ric_ObjectComponent135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_ContextualNavigationRegion134"):
                opp_val = getattr(old_value, "ric_ContextualNavigationRegion134", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_ContextualNavigationRegion134"):
                opp_val = getattr(value, "ric_ContextualNavigationRegion134", None)
                if opp_val is None:
                    setattr(value, "ric_ContextualNavigationRegion134", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ric_ObjectComponent162(self):
        return self.__ric_ObjectComponent162

    @ric_ObjectComponent162.setter
    def ric_ObjectComponent162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_ObjectComponent__ric_ObjectComponent162", None)
        self.__ric_ObjectComponent162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_Document161"):
                opp_val = getattr(old_value, "ric_Document161", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_Document161"):
                opp_val = getattr(value, "ric_Document161", None)
                if opp_val is None:
                    setattr(value, "ric_Document161", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ric_ObjectComponent87(self):
        return self.__ric_ObjectComponent87

    @ric_ObjectComponent87.setter
    def ric_ObjectComponent87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_ObjectComponent__ric_ObjectComponent87", None)
        self.__ric_ObjectComponent87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_Section86"):
                opp_val = getattr(old_value, "ric_Section86", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_Section86"):
                opp_val = getattr(value, "ric_Section86", None)
                if opp_val is None:
                    setattr(value, "ric_Section86", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ric_ObjectComponent(self):
        return self.__ric_ObjectComponent

    @ric_ObjectComponent.setter
    def ric_ObjectComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_ObjectComponent__ric_ObjectComponent", None)
        self.__ric_ObjectComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_Div"):
                opp_val = getattr(old_value, "ric_Div", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_Div"):
                opp_val = getattr(value, "ric_Div", None)
                if opp_val is None:
                    setattr(value, "ric_Div", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ric_ObjectComponent183(self):
        return self.__ric_ObjectComponent183

    @ric_ObjectComponent183.setter
    def ric_ObjectComponent183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_ObjectComponent__ric_ObjectComponent183", None)
        self.__ric_ObjectComponent183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_FooterRegion182"):
                opp_val = getattr(old_value, "ric_FooterRegion182", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_FooterRegion182"):
                opp_val = getattr(value, "ric_FooterRegion182", None)
                if opp_val is None:
                    setattr(value, "ric_FooterRegion182", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BlockLevelComponent:

    pass
class ric_CheckGroup:

    def __init__(self, orientation: str, ric_CheckGroup: "ric_Fieldset" = None, ric_CheckGroup199: set["ric_Checkbox"] = None, ric_CheckGroup201: "ric_Label" = None):
        self.orientation = orientation
        self.ric_CheckGroup = ric_CheckGroup
        self.ric_CheckGroup199 = ric_CheckGroup199 if ric_CheckGroup199 is not None else set()
        self.ric_CheckGroup201 = ric_CheckGroup201
        
    @property
    def orientation(self) -> str:
        return self.__orientation

    @orientation.setter
    def orientation(self, orientation: str):
        self.__orientation = orientation

    @property
    def ric_CheckGroup199(self):
        return self.__ric_CheckGroup199

    @ric_CheckGroup199.setter
    def ric_CheckGroup199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_CheckGroup__ric_CheckGroup199", None)
        self.__ric_CheckGroup199 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ric_Checkbox"):
                    opp_val = getattr(item, "ric_Checkbox", None)
                    
                    if opp_val == self:
                        setattr(item, "ric_Checkbox", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ric_Checkbox"):
                    opp_val = getattr(item, "ric_Checkbox", None)
                    
                    setattr(item, "ric_Checkbox", self)
                    

    @property
    def ric_CheckGroup(self):
        return self.__ric_CheckGroup

    @ric_CheckGroup.setter
    def ric_CheckGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_CheckGroup__ric_CheckGroup", None)
        self.__ric_CheckGroup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_Fieldset31"):
                opp_val = getattr(old_value, "ric_Fieldset31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_Fieldset31"):
                opp_val = getattr(value, "ric_Fieldset31", None)
                if opp_val is None:
                    setattr(value, "ric_Fieldset31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ric_CheckGroup201(self):
        return self.__ric_CheckGroup201

    @ric_CheckGroup201.setter
    def ric_CheckGroup201(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_CheckGroup__ric_CheckGroup201", None)
        self.__ric_CheckGroup201 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_Label202"):
                opp_val = getattr(old_value, "ric_Label202", None)
                if opp_val == self:
                    setattr(old_value, "ric_Label202", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_Label202"):
                opp_val = getattr(value, "ric_Label202", None)
                setattr(value, "ric_Label202", self)

class ric_RadioGroup:

    def __init__(self, orientation: str, ric_RadioGroup: "ric_Fieldset" = None, ric_RadioGroup194: set["ric_Radio"] = None, ric_RadioGroup196: "ric_Label" = None):
        self.orientation = orientation
        self.ric_RadioGroup = ric_RadioGroup
        self.ric_RadioGroup194 = ric_RadioGroup194 if ric_RadioGroup194 is not None else set()
        self.ric_RadioGroup196 = ric_RadioGroup196
        
    @property
    def orientation(self) -> str:
        return self.__orientation

    @orientation.setter
    def orientation(self, orientation: str):
        self.__orientation = orientation

    @property
    def ric_RadioGroup196(self):
        return self.__ric_RadioGroup196

    @ric_RadioGroup196.setter
    def ric_RadioGroup196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_RadioGroup__ric_RadioGroup196", None)
        self.__ric_RadioGroup196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_Label197"):
                opp_val = getattr(old_value, "ric_Label197", None)
                if opp_val == self:
                    setattr(old_value, "ric_Label197", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_Label197"):
                opp_val = getattr(value, "ric_Label197", None)
                setattr(value, "ric_Label197", self)

    @property
    def ric_RadioGroup194(self):
        return self.__ric_RadioGroup194

    @ric_RadioGroup194.setter
    def ric_RadioGroup194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_RadioGroup__ric_RadioGroup194", None)
        self.__ric_RadioGroup194 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ric_Radio"):
                    opp_val = getattr(item, "ric_Radio", None)
                    
                    if opp_val == self:
                        setattr(item, "ric_Radio", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ric_Radio"):
                    opp_val = getattr(item, "ric_Radio", None)
                    
                    setattr(item, "ric_Radio", self)
                    

    @property
    def ric_RadioGroup(self):
        return self.__ric_RadioGroup

    @ric_RadioGroup.setter
    def ric_RadioGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_RadioGroup__ric_RadioGroup", None)
        self.__ric_RadioGroup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_Fieldset29"):
                opp_val = getattr(old_value, "ric_Fieldset29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_Fieldset29"):
                opp_val = getattr(value, "ric_Fieldset29", None)
                if opp_val is None:
                    setattr(value, "ric_Fieldset29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ric_SelectItem:

    def __init__(self, itemLabel: str, value: str, selected: bool, ric_SelectItem: "ric_Select" = None):
        self.itemLabel = itemLabel
        self.value = value
        self.selected = selected
        self.ric_SelectItem = ric_SelectItem
        
    @property
    def itemLabel(self) -> str:
        return self.__itemLabel

    @itemLabel.setter
    def itemLabel(self, itemLabel: str):
        self.__itemLabel = itemLabel

    @property
    def selected(self) -> bool:
        return self.__selected

    @selected.setter
    def selected(self, selected: bool):
        self.__selected = selected

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def ric_SelectItem(self):
        return self.__ric_SelectItem

    @ric_SelectItem.setter
    def ric_SelectItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_SelectItem__ric_SelectItem", None)
        self.__ric_SelectItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_Select"):
                opp_val = getattr(old_value, "ric_Select", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_Select"):
                opp_val = getattr(value, "ric_Select", None)
                if opp_val is None:
                    setattr(value, "ric_Select", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ric_InlineComponent(ABC):

    def __init__(self, text: str, ric_InlineComponent: "ric_Form" = None, ric_InlineComponent50: "ric_BlockLevelComponent" = None, ric_InlineComponent53: "ric_InlineComponent" = None, ric_InlineComponent51: set["ric_InlineComponent"] = None, ric_InlineComponent81: "ric_Section" = None, ric_InlineComponent59: "ric_Tab" = None, ric_InlineComponent129: "ric_ContextualNavigationRegion" = None, ric_InlineComponent119: "ric_HeaderRegion" = None, ric_InlineComponent156: "ric_Document" = None, ric_InlineComponent177: "ric_FooterRegion" = None):
        self.text = text
        self.ric_InlineComponent = ric_InlineComponent
        self.ric_InlineComponent50 = ric_InlineComponent50
        self.ric_InlineComponent53 = ric_InlineComponent53
        self.ric_InlineComponent51 = ric_InlineComponent51 if ric_InlineComponent51 is not None else set()
        self.ric_InlineComponent81 = ric_InlineComponent81
        self.ric_InlineComponent59 = ric_InlineComponent59
        self.ric_InlineComponent129 = ric_InlineComponent129
        self.ric_InlineComponent119 = ric_InlineComponent119
        self.ric_InlineComponent156 = ric_InlineComponent156
        self.ric_InlineComponent177 = ric_InlineComponent177
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def ric_InlineComponent177(self):
        return self.__ric_InlineComponent177

    @ric_InlineComponent177.setter
    def ric_InlineComponent177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_InlineComponent__ric_InlineComponent177", None)
        self.__ric_InlineComponent177 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_FooterRegion176"):
                opp_val = getattr(old_value, "ric_FooterRegion176", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_FooterRegion176"):
                opp_val = getattr(value, "ric_FooterRegion176", None)
                if opp_val is None:
                    setattr(value, "ric_FooterRegion176", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ric_InlineComponent51(self):
        return self.__ric_InlineComponent51

    @ric_InlineComponent51.setter
    def ric_InlineComponent51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_InlineComponent__ric_InlineComponent51", None)
        self.__ric_InlineComponent51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ric_InlineComponent53"):
                    opp_val = getattr(item, "ric_InlineComponent53", None)
                    
                    if opp_val == self:
                        setattr(item, "ric_InlineComponent53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ric_InlineComponent53"):
                    opp_val = getattr(item, "ric_InlineComponent53", None)
                    
                    setattr(item, "ric_InlineComponent53", self)
                    

    @property
    def ric_InlineComponent156(self):
        return self.__ric_InlineComponent156

    @ric_InlineComponent156.setter
    def ric_InlineComponent156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_InlineComponent__ric_InlineComponent156", None)
        self.__ric_InlineComponent156 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_Document155"):
                opp_val = getattr(old_value, "ric_Document155", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_Document155"):
                opp_val = getattr(value, "ric_Document155", None)
                if opp_val is None:
                    setattr(value, "ric_Document155", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ric_InlineComponent129(self):
        return self.__ric_InlineComponent129

    @ric_InlineComponent129.setter
    def ric_InlineComponent129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_InlineComponent__ric_InlineComponent129", None)
        self.__ric_InlineComponent129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_ContextualNavigationRegion128"):
                opp_val = getattr(old_value, "ric_ContextualNavigationRegion128", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_ContextualNavigationRegion128"):
                opp_val = getattr(value, "ric_ContextualNavigationRegion128", None)
                if opp_val is None:
                    setattr(value, "ric_ContextualNavigationRegion128", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ric_InlineComponent53(self):
        return self.__ric_InlineComponent53

    @ric_InlineComponent53.setter
    def ric_InlineComponent53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_InlineComponent__ric_InlineComponent53", None)
        self.__ric_InlineComponent53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_InlineComponent51"):
                opp_val = getattr(old_value, "ric_InlineComponent51", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_InlineComponent51"):
                opp_val = getattr(value, "ric_InlineComponent51", None)
                if opp_val is None:
                    setattr(value, "ric_InlineComponent51", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ric_InlineComponent119(self):
        return self.__ric_InlineComponent119

    @ric_InlineComponent119.setter
    def ric_InlineComponent119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_InlineComponent__ric_InlineComponent119", None)
        self.__ric_InlineComponent119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_HeaderRegion118"):
                opp_val = getattr(old_value, "ric_HeaderRegion118", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_HeaderRegion118"):
                opp_val = getattr(value, "ric_HeaderRegion118", None)
                if opp_val is None:
                    setattr(value, "ric_HeaderRegion118", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ric_InlineComponent59(self):
        return self.__ric_InlineComponent59

    @ric_InlineComponent59.setter
    def ric_InlineComponent59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_InlineComponent__ric_InlineComponent59", None)
        self.__ric_InlineComponent59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_Tab58"):
                opp_val = getattr(old_value, "ric_Tab58", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_Tab58"):
                opp_val = getattr(value, "ric_Tab58", None)
                if opp_val is None:
                    setattr(value, "ric_Tab58", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ric_InlineComponent50(self):
        return self.__ric_InlineComponent50

    @ric_InlineComponent50.setter
    def ric_InlineComponent50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_InlineComponent__ric_InlineComponent50", None)
        self.__ric_InlineComponent50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_BlockLevelComponent49"):
                opp_val = getattr(old_value, "ric_BlockLevelComponent49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_BlockLevelComponent49"):
                opp_val = getattr(value, "ric_BlockLevelComponent49", None)
                if opp_val is None:
                    setattr(value, "ric_BlockLevelComponent49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ric_InlineComponent(self):
        return self.__ric_InlineComponent

    @ric_InlineComponent.setter
    def ric_InlineComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_InlineComponent__ric_InlineComponent", None)
        self.__ric_InlineComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_Form20"):
                opp_val = getattr(old_value, "ric_Form20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_Form20"):
                opp_val = getattr(value, "ric_Form20", None)
                if opp_val is None:
                    setattr(value, "ric_Form20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ric_InlineComponent81(self):
        return self.__ric_InlineComponent81

    @ric_InlineComponent81.setter
    def ric_InlineComponent81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_InlineComponent__ric_InlineComponent81", None)
        self.__ric_InlineComponent81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_Section80"):
                opp_val = getattr(old_value, "ric_Section80", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_Section80"):
                opp_val = getattr(value, "ric_Section80", None)
                if opp_val is None:
                    setattr(value, "ric_Section80", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ric_BlockLevelComponent(ABC):

    pass
class ric_Script:

    def __init__(self, name: str, type: str, implementation: str, ric_Script: "ric_Event" = None):
        self.name = name
        self.type = type
        self.implementation = implementation
        self.ric_Script = ric_Script
        
    @property
    def implementation(self) -> str:
        return self.__implementation

    @implementation.setter
    def implementation(self, implementation: str):
        self.__implementation = implementation

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ric_Script(self):
        return self.__ric_Script

    @ric_Script.setter
    def ric_Script(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Script__ric_Script", None)
        self.__ric_Script = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_Event13"):
                opp_val = getattr(old_value, "ric_Event13", None)
                if opp_val == self:
                    setattr(old_value, "ric_Event13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_Event13"):
                opp_val = getattr(value, "ric_Event13", None)
                setattr(value, "ric_Event13", self)

class FormControl:

    pass
class ric_Radio(FormControl):

    def __init__(self, checked: bool, ric_Radio: "ric_RadioGroup" = None):
        self.checked = checked
        self.ric_Radio = ric_Radio
        
    @property
    def checked(self) -> bool:
        return self.__checked

    @checked.setter
    def checked(self, checked: bool):
        self.__checked = checked

    @property
    def ric_Radio(self):
        return self.__ric_Radio

    @ric_Radio.setter
    def ric_Radio(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Radio__ric_Radio", None)
        self.__ric_Radio = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_RadioGroup194"):
                opp_val = getattr(old_value, "ric_RadioGroup194", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_RadioGroup194"):
                opp_val = getattr(value, "ric_RadioGroup194", None)
                if opp_val is None:
                    setattr(value, "ric_RadioGroup194", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ric_InputFile(FormControl):

    def __init__(self, charWidth: int, maxChars: int, readonly: bool):
        self.charWidth = charWidth
        self.maxChars = maxChars
        self.readonly = readonly
        
    @property
    def maxChars(self) -> int:
        return self.__maxChars

    @maxChars.setter
    def maxChars(self, maxChars: int):
        self.__maxChars = maxChars

    @property
    def charWidth(self) -> int:
        return self.__charWidth

    @charWidth.setter
    def charWidth(self, charWidth: int):
        self.__charWidth = charWidth

    @property
    def readonly(self) -> bool:
        return self.__readonly

    @readonly.setter
    def readonly(self, readonly: bool):
        self.__readonly = readonly

class ric_TextArea(FormControl):

    def __init__(self, cols: int, rols: int, readonly: bool):
        self.cols = cols
        self.rols = rols
        self.readonly = readonly
        
    @property
    def readonly(self) -> bool:
        return self.__readonly

    @readonly.setter
    def readonly(self, readonly: bool):
        self.__readonly = readonly

    @property
    def cols(self) -> int:
        return self.__cols

    @cols.setter
    def cols(self, cols: int):
        self.__cols = cols

    @property
    def rols(self) -> int:
        return self.__rols

    @rols.setter
    def rols(self, rols: int):
        self.__rols = rols

class ric_Checkbox(FormControl):

    def __init__(self, checked: bool, ric_Checkbox: "ric_CheckGroup" = None):
        self.checked = checked
        self.ric_Checkbox = ric_Checkbox
        
    @property
    def checked(self) -> bool:
        return self.__checked

    @checked.setter
    def checked(self, checked: bool):
        self.__checked = checked

    @property
    def ric_Checkbox(self):
        return self.__ric_Checkbox

    @ric_Checkbox.setter
    def ric_Checkbox(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Checkbox__ric_Checkbox", None)
        self.__ric_Checkbox = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_CheckGroup199"):
                opp_val = getattr(old_value, "ric_CheckGroup199", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_CheckGroup199"):
                opp_val = getattr(value, "ric_CheckGroup199", None)
                if opp_val is None:
                    setattr(value, "ric_CheckGroup199", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ric_Select(FormControl):

    def __init__(self, size: int, multiple: bool, ric_Select: set["ric_SelectItem"] = None):
        self.size = size
        self.multiple = multiple
        self.ric_Select = ric_Select if ric_Select is not None else set()
        
    @property
    def multiple(self) -> bool:
        return self.__multiple

    @multiple.setter
    def multiple(self, multiple: bool):
        self.__multiple = multiple

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def ric_Select(self):
        return self.__ric_Select

    @ric_Select.setter
    def ric_Select(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Select__ric_Select", None)
        self.__ric_Select = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ric_SelectItem"):
                    opp_val = getattr(item, "ric_SelectItem", None)
                    
                    if opp_val == self:
                        setattr(item, "ric_SelectItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ric_SelectItem"):
                    opp_val = getattr(item, "ric_SelectItem", None)
                    
                    setattr(item, "ric_SelectItem", self)
                    

class ric_TextField(FormControl):

    def __init__(self, charWidth: int, maxChars: int, readonly: bool, password: bool):
        self.charWidth = charWidth
        self.maxChars = maxChars
        self.readonly = readonly
        self.password = password
        
    @property
    def maxChars(self) -> int:
        return self.__maxChars

    @maxChars.setter
    def maxChars(self, maxChars: int):
        self.__maxChars = maxChars

    @property
    def password(self) -> bool:
        return self.__password

    @password.setter
    def password(self, password: bool):
        self.__password = password

    @property
    def charWidth(self) -> int:
        return self.__charWidth

    @charWidth.setter
    def charWidth(self, charWidth: int):
        self.__charWidth = charWidth

    @property
    def readonly(self) -> bool:
        return self.__readonly

    @readonly.setter
    def readonly(self, readonly: bool):
        self.__readonly = readonly

class ric_Button(FormControl):

    def __init__(self, type: str, disabled: bool, image: str):
        self.type = type
        self.disabled = disabled
        self.image = image
        
    @property
    def image(self) -> str:
        return self.__image

    @image.setter
    def image(self, image: str):
        self.__image = image

    @property
    def disabled(self) -> bool:
        return self.__disabled

    @disabled.setter
    def disabled(self, disabled: bool):
        self.__disabled = disabled

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class ric_ValidDateConstraint(FormControlConstraint):

    def __init__(self, dateFormat: str, ric_ValidDateConstraint: "ric_FormControl" = None):
        self.dateFormat = dateFormat
        self.ric_ValidDateConstraint = ric_ValidDateConstraint
        
    @property
    def dateFormat(self) -> str:
        return self.__dateFormat

    @dateFormat.setter
    def dateFormat(self, dateFormat: str):
        self.__dateFormat = dateFormat

    @property
    def ric_ValidDateConstraint(self):
        return self.__ric_ValidDateConstraint

    @ric_ValidDateConstraint.setter
    def ric_ValidDateConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_ValidDateConstraint__ric_ValidDateConstraint", None)
        self.__ric_ValidDateConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_FormControl11"):
                opp_val = getattr(old_value, "ric_FormControl11", None)
                if opp_val == self:
                    setattr(old_value, "ric_FormControl11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_FormControl11"):
                opp_val = getattr(value, "ric_FormControl11", None)
                setattr(value, "ric_FormControl11", self)

class ric_RequiredFieldConstraint(FormControlConstraint):

    pass
class ric_NumberValueConstraint(FormControlConstraint):

    pass
class ric_ValueConstraint(FormControlConstraint):

    def __init__(self, matchingOperator: str, matchingValue: str, logicalOperator: str, ric_ValueConstraint: "ric_FormControl" = None):
        self.matchingOperator = matchingOperator
        self.matchingValue = matchingValue
        self.logicalOperator = logicalOperator
        self.ric_ValueConstraint = ric_ValueConstraint
        
    @property
    def matchingValue(self) -> str:
        return self.__matchingValue

    @matchingValue.setter
    def matchingValue(self, matchingValue: str):
        self.__matchingValue = matchingValue

    @property
    def logicalOperator(self) -> str:
        return self.__logicalOperator

    @logicalOperator.setter
    def logicalOperator(self, logicalOperator: str):
        self.__logicalOperator = logicalOperator

    @property
    def matchingOperator(self) -> str:
        return self.__matchingOperator

    @matchingOperator.setter
    def matchingOperator(self, matchingOperator: str):
        self.__matchingOperator = matchingOperator

    @property
    def ric_ValueConstraint(self):
        return self.__ric_ValueConstraint

    @ric_ValueConstraint.setter
    def ric_ValueConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_ValueConstraint__ric_ValueConstraint", None)
        self.__ric_ValueConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_FormControl5"):
                opp_val = getattr(old_value, "ric_FormControl5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_FormControl5"):
                opp_val = getattr(value, "ric_FormControl5", None)
                if opp_val is None:
                    setattr(value, "ric_FormControl5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class EventComponent:

    pass
class ric_Document(EventComponent):

    def __init__(self, fileName: str, title: str, index: bool, ric_Document: "ric_Form" = None, ric_Document55: "ric_Link" = None, ric_Document153: "ric_ContentRegion" = None, ric_Document155: set["ric_InlineComponent"] = None, ric_Document158: set["ric_BlockLevelComponent"] = None, ric_Document161: set["ric_ObjectComponent"] = None, ric_Document164: set["ric_LineBreak"] = None, ric_Document167: set["ric_RichWidget"] = None, ric_Document170: set["ric_List"] = None, ric_Document173: set["ric_Form"] = None):
        self.fileName = fileName
        self.title = title
        self.index = index
        self.ric_Document = ric_Document
        self.ric_Document55 = ric_Document55
        self.ric_Document153 = ric_Document153
        self.ric_Document155 = ric_Document155 if ric_Document155 is not None else set()
        self.ric_Document158 = ric_Document158 if ric_Document158 is not None else set()
        self.ric_Document161 = ric_Document161 if ric_Document161 is not None else set()
        self.ric_Document164 = ric_Document164 if ric_Document164 is not None else set()
        self.ric_Document167 = ric_Document167 if ric_Document167 is not None else set()
        self.ric_Document170 = ric_Document170 if ric_Document170 is not None else set()
        self.ric_Document173 = ric_Document173 if ric_Document173 is not None else set()
        
    @property
    def index(self) -> bool:
        return self.__index

    @index.setter
    def index(self, index: bool):
        self.__index = index

    @property
    def fileName(self) -> str:
        return self.__fileName

    @fileName.setter
    def fileName(self, fileName: str):
        self.__fileName = fileName

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def ric_Document170(self):
        return self.__ric_Document170

    @ric_Document170.setter
    def ric_Document170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Document__ric_Document170", None)
        self.__ric_Document170 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ric_List171"):
                    opp_val = getattr(item, "ric_List171", None)
                    
                    if opp_val == self:
                        setattr(item, "ric_List171", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ric_List171"):
                    opp_val = getattr(item, "ric_List171", None)
                    
                    setattr(item, "ric_List171", self)
                    

    @property
    def ric_Document(self):
        return self.__ric_Document

    @ric_Document.setter
    def ric_Document(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Document__ric_Document", None)
        self.__ric_Document = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_Form"):
                opp_val = getattr(old_value, "ric_Form", None)
                if opp_val == self:
                    setattr(old_value, "ric_Form", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_Form"):
                opp_val = getattr(value, "ric_Form", None)
                setattr(value, "ric_Form", self)

    @property
    def ric_Document55(self):
        return self.__ric_Document55

    @ric_Document55.setter
    def ric_Document55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Document__ric_Document55", None)
        self.__ric_Document55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_Link"):
                opp_val = getattr(old_value, "ric_Link", None)
                if opp_val == self:
                    setattr(old_value, "ric_Link", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_Link"):
                opp_val = getattr(value, "ric_Link", None)
                setattr(value, "ric_Link", self)

    @property
    def ric_Document155(self):
        return self.__ric_Document155

    @ric_Document155.setter
    def ric_Document155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Document__ric_Document155", None)
        self.__ric_Document155 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ric_InlineComponent156"):
                    opp_val = getattr(item, "ric_InlineComponent156", None)
                    
                    if opp_val == self:
                        setattr(item, "ric_InlineComponent156", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ric_InlineComponent156"):
                    opp_val = getattr(item, "ric_InlineComponent156", None)
                    
                    setattr(item, "ric_InlineComponent156", self)
                    

    @property
    def ric_Document158(self):
        return self.__ric_Document158

    @ric_Document158.setter
    def ric_Document158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Document__ric_Document158", None)
        self.__ric_Document158 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ric_BlockLevelComponent159"):
                    opp_val = getattr(item, "ric_BlockLevelComponent159", None)
                    
                    if opp_val == self:
                        setattr(item, "ric_BlockLevelComponent159", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ric_BlockLevelComponent159"):
                    opp_val = getattr(item, "ric_BlockLevelComponent159", None)
                    
                    setattr(item, "ric_BlockLevelComponent159", self)
                    

    @property
    def ric_Document164(self):
        return self.__ric_Document164

    @ric_Document164.setter
    def ric_Document164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Document__ric_Document164", None)
        self.__ric_Document164 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ric_LineBreak165"):
                    opp_val = getattr(item, "ric_LineBreak165", None)
                    
                    if opp_val == self:
                        setattr(item, "ric_LineBreak165", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ric_LineBreak165"):
                    opp_val = getattr(item, "ric_LineBreak165", None)
                    
                    setattr(item, "ric_LineBreak165", self)
                    

    @property
    def ric_Document161(self):
        return self.__ric_Document161

    @ric_Document161.setter
    def ric_Document161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Document__ric_Document161", None)
        self.__ric_Document161 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ric_ObjectComponent162"):
                    opp_val = getattr(item, "ric_ObjectComponent162", None)
                    
                    if opp_val == self:
                        setattr(item, "ric_ObjectComponent162", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ric_ObjectComponent162"):
                    opp_val = getattr(item, "ric_ObjectComponent162", None)
                    
                    setattr(item, "ric_ObjectComponent162", self)
                    

    @property
    def ric_Document167(self):
        return self.__ric_Document167

    @ric_Document167.setter
    def ric_Document167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Document__ric_Document167", None)
        self.__ric_Document167 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ric_RichWidget168"):
                    opp_val = getattr(item, "ric_RichWidget168", None)
                    
                    if opp_val == self:
                        setattr(item, "ric_RichWidget168", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ric_RichWidget168"):
                    opp_val = getattr(item, "ric_RichWidget168", None)
                    
                    setattr(item, "ric_RichWidget168", self)
                    

    @property
    def ric_Document173(self):
        return self.__ric_Document173

    @ric_Document173.setter
    def ric_Document173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Document__ric_Document173", None)
        self.__ric_Document173 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ric_Form174"):
                    opp_val = getattr(item, "ric_Form174", None)
                    
                    if opp_val == self:
                        setattr(item, "ric_Form174", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ric_Form174"):
                    opp_val = getattr(item, "ric_Form174", None)
                    
                    setattr(item, "ric_Form174", self)
                    

    @property
    def ric_Document153(self):
        return self.__ric_Document153

    @ric_Document153.setter
    def ric_Document153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Document__ric_Document153", None)
        self.__ric_Document153 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_ContentRegion152"):
                opp_val = getattr(old_value, "ric_ContentRegion152", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_ContentRegion152"):
                opp_val = getattr(value, "ric_ContentRegion152", None)
                if opp_val is None:
                    setattr(value, "ric_ContentRegion152", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ClassifiableComponent:

    pass
class IdentifiableComponent:

    pass
class ric_Paragraph(EventComponent, ClassifiableComponent, IdentifiableComponent, InlineComponent):

    def __init__(self, align: str):
        self.align = align
        
    @property
    def align(self) -> str:
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align

class ric_LineBreak(ClassifiableComponent, IdentifiableComponent):

    pass
class ric_Fieldset(EventComponent, ClassifiableComponent, IdentifiableComponent):

    def __init__(self, legend: str, legendAlign: str, legendFormat: str, ric_Fieldset: "ric_Form" = None, ric_Fieldset26: set["ric_FormControl"] = None, ric_Fieldset29: set["ric_RadioGroup"] = None, ric_Fieldset31: set["ric_CheckGroup"] = None, ric_Fieldset44: "ric_Div" = None):
        self.legend = legend
        self.legendAlign = legendAlign
        self.legendFormat = legendFormat
        self.ric_Fieldset = ric_Fieldset
        self.ric_Fieldset26 = ric_Fieldset26 if ric_Fieldset26 is not None else set()
        self.ric_Fieldset29 = ric_Fieldset29 if ric_Fieldset29 is not None else set()
        self.ric_Fieldset31 = ric_Fieldset31 if ric_Fieldset31 is not None else set()
        self.ric_Fieldset44 = ric_Fieldset44
        
    @property
    def legendAlign(self) -> str:
        return self.__legendAlign

    @legendAlign.setter
    def legendAlign(self, legendAlign: str):
        self.__legendAlign = legendAlign

    @property
    def legendFormat(self) -> str:
        return self.__legendFormat

    @legendFormat.setter
    def legendFormat(self, legendFormat: str):
        self.__legendFormat = legendFormat

    @property
    def legend(self) -> str:
        return self.__legend

    @legend.setter
    def legend(self, legend: str):
        self.__legend = legend

    @property
    def ric_Fieldset(self):
        return self.__ric_Fieldset

    @ric_Fieldset.setter
    def ric_Fieldset(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Fieldset__ric_Fieldset", None)
        self.__ric_Fieldset = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_Form16"):
                opp_val = getattr(old_value, "ric_Form16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_Form16"):
                opp_val = getattr(value, "ric_Form16", None)
                if opp_val is None:
                    setattr(value, "ric_Form16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ric_Fieldset44(self):
        return self.__ric_Fieldset44

    @ric_Fieldset44.setter
    def ric_Fieldset44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Fieldset__ric_Fieldset44", None)
        self.__ric_Fieldset44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_Div43"):
                opp_val = getattr(old_value, "ric_Div43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_Div43"):
                opp_val = getattr(value, "ric_Div43", None)
                if opp_val is None:
                    setattr(value, "ric_Div43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ric_Fieldset29(self):
        return self.__ric_Fieldset29

    @ric_Fieldset29.setter
    def ric_Fieldset29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Fieldset__ric_Fieldset29", None)
        self.__ric_Fieldset29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ric_RadioGroup"):
                    opp_val = getattr(item, "ric_RadioGroup", None)
                    
                    if opp_val == self:
                        setattr(item, "ric_RadioGroup", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ric_RadioGroup"):
                    opp_val = getattr(item, "ric_RadioGroup", None)
                    
                    setattr(item, "ric_RadioGroup", self)
                    

    @property
    def ric_Fieldset31(self):
        return self.__ric_Fieldset31

    @ric_Fieldset31.setter
    def ric_Fieldset31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Fieldset__ric_Fieldset31", None)
        self.__ric_Fieldset31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ric_CheckGroup"):
                    opp_val = getattr(item, "ric_CheckGroup", None)
                    
                    if opp_val == self:
                        setattr(item, "ric_CheckGroup", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ric_CheckGroup"):
                    opp_val = getattr(item, "ric_CheckGroup", None)
                    
                    setattr(item, "ric_CheckGroup", self)
                    

    @property
    def ric_Fieldset26(self):
        return self.__ric_Fieldset26

    @ric_Fieldset26.setter
    def ric_Fieldset26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Fieldset__ric_Fieldset26", None)
        self.__ric_Fieldset26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ric_FormControl27"):
                    opp_val = getattr(item, "ric_FormControl27", None)
                    
                    if opp_val == self:
                        setattr(item, "ric_FormControl27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ric_FormControl27"):
                    opp_val = getattr(item, "ric_FormControl27", None)
                    
                    setattr(item, "ric_FormControl27", self)
                    

class ric_PhraseElement(EventComponent, ClassifiableComponent, InlineComponent, IdentifiableComponent):

    def __init__(self, phraseType: str, title: str, ric_PhraseElement: "ric_FormControl" = None):
        self.phraseType = phraseType
        self.title = title
        self.ric_PhraseElement = ric_PhraseElement
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def phraseType(self) -> str:
        return self.__phraseType

    @phraseType.setter
    def phraseType(self, phraseType: str):
        self.__phraseType = phraseType

    @property
    def ric_PhraseElement(self):
        return self.__ric_PhraseElement

    @ric_PhraseElement.setter
    def ric_PhraseElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_PhraseElement__ric_PhraseElement", None)
        self.__ric_PhraseElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_FormControl3"):
                opp_val = getattr(old_value, "ric_FormControl3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_FormControl3"):
                opp_val = getattr(value, "ric_FormControl3", None)
                if opp_val is None:
                    setattr(value, "ric_FormControl3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ric_Label(ClassifiableComponent, IdentifiableComponent):

    def __init__(self, text: str, format: str, ric_Label: "ric_FormControl" = None, ric_Label23: set["ric_Event"] = None, ric_Label197: "ric_RadioGroup" = None, ric_Label202: "ric_CheckGroup" = None):
        self.text = text
        self.format = format
        self.ric_Label = ric_Label
        self.ric_Label23 = ric_Label23 if ric_Label23 is not None else set()
        self.ric_Label197 = ric_Label197
        self.ric_Label202 = ric_Label202
        
    @property
    def format(self) -> str:
        return self.__format

    @format.setter
    def format(self, format: str):
        self.__format = format

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def ric_Label202(self):
        return self.__ric_Label202

    @ric_Label202.setter
    def ric_Label202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Label__ric_Label202", None)
        self.__ric_Label202 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_CheckGroup201"):
                opp_val = getattr(old_value, "ric_CheckGroup201", None)
                if opp_val == self:
                    setattr(old_value, "ric_CheckGroup201", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_CheckGroup201"):
                opp_val = getattr(value, "ric_CheckGroup201", None)
                setattr(value, "ric_CheckGroup201", self)

    @property
    def ric_Label(self):
        return self.__ric_Label

    @ric_Label.setter
    def ric_Label(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Label__ric_Label", None)
        self.__ric_Label = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_FormControl"):
                opp_val = getattr(old_value, "ric_FormControl", None)
                if opp_val == self:
                    setattr(old_value, "ric_FormControl", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_FormControl"):
                opp_val = getattr(value, "ric_FormControl", None)
                setattr(value, "ric_FormControl", self)

    @property
    def ric_Label23(self):
        return self.__ric_Label23

    @ric_Label23.setter
    def ric_Label23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Label__ric_Label23", None)
        self.__ric_Label23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ric_Event24"):
                    opp_val = getattr(item, "ric_Event24", None)
                    
                    if opp_val == self:
                        setattr(item, "ric_Event24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ric_Event24"):
                    opp_val = getattr(item, "ric_Event24", None)
                    
                    setattr(item, "ric_Event24", self)
                    

    @property
    def ric_Label197(self):
        return self.__ric_Label197

    @ric_Label197.setter
    def ric_Label197(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Label__ric_Label197", None)
        self.__ric_Label197 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_RadioGroup196"):
                opp_val = getattr(old_value, "ric_RadioGroup196", None)
                if opp_val == self:
                    setattr(old_value, "ric_RadioGroup196", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_RadioGroup196"):
                opp_val = getattr(value, "ric_RadioGroup196", None)
                setattr(value, "ric_RadioGroup196", self)

class ric_Image(ClassifiableComponent, IdentifiableComponent, ObjectComponent, EventComponent):

    def __init__(self, src: str, alt: str, ric_Image: "ric_Logo" = None):
        self.src = src
        self.alt = alt
        self.ric_Image = ric_Image
        
    @property
    def alt(self) -> str:
        return self.__alt

    @alt.setter
    def alt(self, alt: str):
        self.__alt = alt

    @property
    def src(self) -> str:
        return self.__src

    @src.setter
    def src(self, src: str):
        self.__src = src

    @property
    def ric_Image(self):
        return self.__ric_Image

    @ric_Image.setter
    def ric_Image(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Image__ric_Image", None)
        self.__ric_Image = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_Logo124"):
                opp_val = getattr(old_value, "ric_Logo124", None)
                if opp_val == self:
                    setattr(old_value, "ric_Logo124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_Logo124"):
                opp_val = getattr(value, "ric_Logo124", None)
                setattr(value, "ric_Logo124", self)

class ric_Form(EventComponent, ClassifiableComponent, IdentifiableComponent):

    def __init__(self, name: str, method: str, ric_Form: "ric_Document" = None, ric_Form16: set["ric_Fieldset"] = None, ric_Form18: set["ric_BlockLevelComponent"] = None, ric_Form20: set["ric_InlineComponent"] = None, ric_Form41: "ric_Div" = None, ric_Form77: "ric_Tab" = None, ric_Form99: "ric_Section" = None, ric_Form147: "ric_ContextualNavigationRegion" = None, ric_Form150: "ric_SearchRegion" = None, ric_Form174: "ric_Document" = None):
        self.name = name
        self.method = method
        self.ric_Form = ric_Form
        self.ric_Form16 = ric_Form16 if ric_Form16 is not None else set()
        self.ric_Form18 = ric_Form18 if ric_Form18 is not None else set()
        self.ric_Form20 = ric_Form20 if ric_Form20 is not None else set()
        self.ric_Form41 = ric_Form41
        self.ric_Form77 = ric_Form77
        self.ric_Form99 = ric_Form99
        self.ric_Form147 = ric_Form147
        self.ric_Form150 = ric_Form150
        self.ric_Form174 = ric_Form174
        
    @property
    def method(self) -> str:
        return self.__method

    @method.setter
    def method(self, method: str):
        self.__method = method

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ric_Form147(self):
        return self.__ric_Form147

    @ric_Form147.setter
    def ric_Form147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Form__ric_Form147", None)
        self.__ric_Form147 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_ContextualNavigationRegion146"):
                opp_val = getattr(old_value, "ric_ContextualNavigationRegion146", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_ContextualNavigationRegion146"):
                opp_val = getattr(value, "ric_ContextualNavigationRegion146", None)
                if opp_val is None:
                    setattr(value, "ric_ContextualNavigationRegion146", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ric_Form150(self):
        return self.__ric_Form150

    @ric_Form150.setter
    def ric_Form150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Form__ric_Form150", None)
        self.__ric_Form150 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_SearchRegion149"):
                opp_val = getattr(old_value, "ric_SearchRegion149", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_SearchRegion149"):
                opp_val = getattr(value, "ric_SearchRegion149", None)
                if opp_val is None:
                    setattr(value, "ric_SearchRegion149", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ric_Form41(self):
        return self.__ric_Form41

    @ric_Form41.setter
    def ric_Form41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Form__ric_Form41", None)
        self.__ric_Form41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_Div40"):
                opp_val = getattr(old_value, "ric_Div40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_Div40"):
                opp_val = getattr(value, "ric_Div40", None)
                if opp_val is None:
                    setattr(value, "ric_Div40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ric_Form174(self):
        return self.__ric_Form174

    @ric_Form174.setter
    def ric_Form174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Form__ric_Form174", None)
        self.__ric_Form174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_Document173"):
                opp_val = getattr(old_value, "ric_Document173", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_Document173"):
                opp_val = getattr(value, "ric_Document173", None)
                if opp_val is None:
                    setattr(value, "ric_Document173", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ric_Form(self):
        return self.__ric_Form

    @ric_Form.setter
    def ric_Form(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Form__ric_Form", None)
        self.__ric_Form = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_Document"):
                opp_val = getattr(old_value, "ric_Document", None)
                if opp_val == self:
                    setattr(old_value, "ric_Document", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_Document"):
                opp_val = getattr(value, "ric_Document", None)
                setattr(value, "ric_Document", self)

    @property
    def ric_Form77(self):
        return self.__ric_Form77

    @ric_Form77.setter
    def ric_Form77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Form__ric_Form77", None)
        self.__ric_Form77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_Tab76"):
                opp_val = getattr(old_value, "ric_Tab76", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_Tab76"):
                opp_val = getattr(value, "ric_Tab76", None)
                if opp_val is None:
                    setattr(value, "ric_Tab76", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ric_Form18(self):
        return self.__ric_Form18

    @ric_Form18.setter
    def ric_Form18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Form__ric_Form18", None)
        self.__ric_Form18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ric_BlockLevelComponent"):
                    opp_val = getattr(item, "ric_BlockLevelComponent", None)
                    
                    if opp_val == self:
                        setattr(item, "ric_BlockLevelComponent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ric_BlockLevelComponent"):
                    opp_val = getattr(item, "ric_BlockLevelComponent", None)
                    
                    setattr(item, "ric_BlockLevelComponent", self)
                    

    @property
    def ric_Form20(self):
        return self.__ric_Form20

    @ric_Form20.setter
    def ric_Form20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Form__ric_Form20", None)
        self.__ric_Form20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ric_InlineComponent"):
                    opp_val = getattr(item, "ric_InlineComponent", None)
                    
                    if opp_val == self:
                        setattr(item, "ric_InlineComponent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ric_InlineComponent"):
                    opp_val = getattr(item, "ric_InlineComponent", None)
                    
                    setattr(item, "ric_InlineComponent", self)
                    

    @property
    def ric_Form99(self):
        return self.__ric_Form99

    @ric_Form99.setter
    def ric_Form99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Form__ric_Form99", None)
        self.__ric_Form99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_Section98"):
                opp_val = getattr(old_value, "ric_Section98", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_Section98"):
                opp_val = getattr(value, "ric_Section98", None)
                if opp_val is None:
                    setattr(value, "ric_Section98", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ric_Form16(self):
        return self.__ric_Form16

    @ric_Form16.setter
    def ric_Form16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Form__ric_Form16", None)
        self.__ric_Form16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ric_Fieldset"):
                    opp_val = getattr(item, "ric_Fieldset", None)
                    
                    if opp_val == self:
                        setattr(item, "ric_Fieldset", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ric_Fieldset"):
                    opp_val = getattr(item, "ric_Fieldset", None)
                    
                    setattr(item, "ric_Fieldset", self)
                    

class ric_Heading(EventComponent, ClassifiableComponent, InlineComponent, IdentifiableComponent):

    def __init__(self, level: str):
        self.level = level
        
    @property
    def level(self) -> str:
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level

class ric_Div(EventComponent, ClassifiableComponent, IdentifiableComponent, BlockLevelComponent):

    def __init__(self, align: str, ric_Div: set["ric_ObjectComponent"] = None, ric_Div34: set["ric_LineBreak"] = None, ric_Div36: set["ric_RichWidget"] = None, ric_Div38: set["ric_List"] = None, ric_Div40: set["ric_Form"] = None, ric_Div43: set["ric_Fieldset"] = None):
        self.align = align
        self.ric_Div = ric_Div if ric_Div is not None else set()
        self.ric_Div34 = ric_Div34 if ric_Div34 is not None else set()
        self.ric_Div36 = ric_Div36 if ric_Div36 is not None else set()
        self.ric_Div38 = ric_Div38 if ric_Div38 is not None else set()
        self.ric_Div40 = ric_Div40 if ric_Div40 is not None else set()
        self.ric_Div43 = ric_Div43 if ric_Div43 is not None else set()
        
    @property
    def align(self) -> str:
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align

    @property
    def ric_Div34(self):
        return self.__ric_Div34

    @ric_Div34.setter
    def ric_Div34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Div__ric_Div34", None)
        self.__ric_Div34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ric_LineBreak"):
                    opp_val = getattr(item, "ric_LineBreak", None)
                    
                    if opp_val == self:
                        setattr(item, "ric_LineBreak", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ric_LineBreak"):
                    opp_val = getattr(item, "ric_LineBreak", None)
                    
                    setattr(item, "ric_LineBreak", self)
                    

    @property
    def ric_Div43(self):
        return self.__ric_Div43

    @ric_Div43.setter
    def ric_Div43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Div__ric_Div43", None)
        self.__ric_Div43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ric_Fieldset44"):
                    opp_val = getattr(item, "ric_Fieldset44", None)
                    
                    if opp_val == self:
                        setattr(item, "ric_Fieldset44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ric_Fieldset44"):
                    opp_val = getattr(item, "ric_Fieldset44", None)
                    
                    setattr(item, "ric_Fieldset44", self)
                    

    @property
    def ric_Div36(self):
        return self.__ric_Div36

    @ric_Div36.setter
    def ric_Div36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Div__ric_Div36", None)
        self.__ric_Div36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ric_RichWidget"):
                    opp_val = getattr(item, "ric_RichWidget", None)
                    
                    if opp_val == self:
                        setattr(item, "ric_RichWidget", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ric_RichWidget"):
                    opp_val = getattr(item, "ric_RichWidget", None)
                    
                    setattr(item, "ric_RichWidget", self)
                    

    @property
    def ric_Div40(self):
        return self.__ric_Div40

    @ric_Div40.setter
    def ric_Div40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Div__ric_Div40", None)
        self.__ric_Div40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ric_Form41"):
                    opp_val = getattr(item, "ric_Form41", None)
                    
                    if opp_val == self:
                        setattr(item, "ric_Form41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ric_Form41"):
                    opp_val = getattr(item, "ric_Form41", None)
                    
                    setattr(item, "ric_Form41", self)
                    

    @property
    def ric_Div38(self):
        return self.__ric_Div38

    @ric_Div38.setter
    def ric_Div38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Div__ric_Div38", None)
        self.__ric_Div38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ric_List"):
                    opp_val = getattr(item, "ric_List", None)
                    
                    if opp_val == self:
                        setattr(item, "ric_List", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ric_List"):
                    opp_val = getattr(item, "ric_List", None)
                    
                    setattr(item, "ric_List", self)
                    

    @property
    def ric_Div(self):
        return self.__ric_Div

    @ric_Div.setter
    def ric_Div(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Div__ric_Div", None)
        self.__ric_Div = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ric_ObjectComponent"):
                    opp_val = getattr(item, "ric_ObjectComponent", None)
                    
                    if opp_val == self:
                        setattr(item, "ric_ObjectComponent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ric_ObjectComponent"):
                    opp_val = getattr(item, "ric_ObjectComponent", None)
                    
                    setattr(item, "ric_ObjectComponent", self)
                    

class ric_List(EventComponent, ClassifiableComponent, IdentifiableComponent):

    pass
class ric_Span(ClassifiableComponent, InlineComponent, IdentifiableComponent, EventComponent):

    def __init__(self, align: str):
        self.align = align
        
    @property
    def align(self) -> str:
        return self.__align

    @align.setter
    def align(self, align: str):
        self.__align = align

class ric_Link(ClassifiableComponent, InlineComponent, EventComponent, IdentifiableComponent):

    def __init__(self, title: str, ric_Link: "ric_Document" = None, ric_Link205: "ric_LinkGroup" = None):
        self.title = title
        self.ric_Link = ric_Link
        self.ric_Link205 = ric_Link205
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def ric_Link205(self):
        return self.__ric_Link205

    @ric_Link205.setter
    def ric_Link205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Link__ric_Link205", None)
        self.__ric_Link205 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_LinkGroup204"):
                opp_val = getattr(old_value, "ric_LinkGroup204", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_LinkGroup204"):
                opp_val = getattr(value, "ric_LinkGroup204", None)
                if opp_val is None:
                    setattr(value, "ric_LinkGroup204", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ric_Link(self):
        return self.__ric_Link

    @ric_Link.setter
    def ric_Link(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Link__ric_Link", None)
        self.__ric_Link = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_Document55"):
                opp_val = getattr(old_value, "ric_Document55", None)
                if opp_val == self:
                    setattr(old_value, "ric_Document55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_Document55"):
                opp_val = getattr(value, "ric_Document55", None)
                setattr(value, "ric_Document55", self)

class ric_RichWidget(ClassifiableComponent, IdentifiableComponent):

    pass
class ric_FormControl(ClassifiableComponent, IdentifiableComponent, EventComponent):

    def __init__(self, name: str, value: str, ric_FormControl: "ric_Label" = None, ric_FormControl3: set["ric_PhraseElement"] = None, ric_FormControl5: set["ric_ValueConstraint"] = None, ric_FormControl7: "ric_NumberValueConstraint" = None, ric_FormControl9: "ric_RequiredFieldConstraint" = None, ric_FormControl11: "ric_ValidDateConstraint" = None, ric_FormControl27: "ric_Fieldset" = None):
        self.name = name
        self.value = value
        self.ric_FormControl = ric_FormControl
        self.ric_FormControl3 = ric_FormControl3 if ric_FormControl3 is not None else set()
        self.ric_FormControl5 = ric_FormControl5 if ric_FormControl5 is not None else set()
        self.ric_FormControl7 = ric_FormControl7
        self.ric_FormControl9 = ric_FormControl9
        self.ric_FormControl11 = ric_FormControl11
        self.ric_FormControl27 = ric_FormControl27
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ric_FormControl27(self):
        return self.__ric_FormControl27

    @ric_FormControl27.setter
    def ric_FormControl27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_FormControl__ric_FormControl27", None)
        self.__ric_FormControl27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_Fieldset26"):
                opp_val = getattr(old_value, "ric_Fieldset26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_Fieldset26"):
                opp_val = getattr(value, "ric_Fieldset26", None)
                if opp_val is None:
                    setattr(value, "ric_Fieldset26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ric_FormControl9(self):
        return self.__ric_FormControl9

    @ric_FormControl9.setter
    def ric_FormControl9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_FormControl__ric_FormControl9", None)
        self.__ric_FormControl9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_RequiredFieldConstraint"):
                opp_val = getattr(old_value, "ric_RequiredFieldConstraint", None)
                if opp_val == self:
                    setattr(old_value, "ric_RequiredFieldConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_RequiredFieldConstraint"):
                opp_val = getattr(value, "ric_RequiredFieldConstraint", None)
                setattr(value, "ric_RequiredFieldConstraint", self)

    @property
    def ric_FormControl11(self):
        return self.__ric_FormControl11

    @ric_FormControl11.setter
    def ric_FormControl11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_FormControl__ric_FormControl11", None)
        self.__ric_FormControl11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_ValidDateConstraint"):
                opp_val = getattr(old_value, "ric_ValidDateConstraint", None)
                if opp_val == self:
                    setattr(old_value, "ric_ValidDateConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_ValidDateConstraint"):
                opp_val = getattr(value, "ric_ValidDateConstraint", None)
                setattr(value, "ric_ValidDateConstraint", self)

    @property
    def ric_FormControl7(self):
        return self.__ric_FormControl7

    @ric_FormControl7.setter
    def ric_FormControl7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_FormControl__ric_FormControl7", None)
        self.__ric_FormControl7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_NumberValueConstraint"):
                opp_val = getattr(old_value, "ric_NumberValueConstraint", None)
                if opp_val == self:
                    setattr(old_value, "ric_NumberValueConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_NumberValueConstraint"):
                opp_val = getattr(value, "ric_NumberValueConstraint", None)
                setattr(value, "ric_NumberValueConstraint", self)

    @property
    def ric_FormControl3(self):
        return self.__ric_FormControl3

    @ric_FormControl3.setter
    def ric_FormControl3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_FormControl__ric_FormControl3", None)
        self.__ric_FormControl3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ric_PhraseElement"):
                    opp_val = getattr(item, "ric_PhraseElement", None)
                    
                    if opp_val == self:
                        setattr(item, "ric_PhraseElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ric_PhraseElement"):
                    opp_val = getattr(item, "ric_PhraseElement", None)
                    
                    setattr(item, "ric_PhraseElement", self)
                    

    @property
    def ric_FormControl(self):
        return self.__ric_FormControl

    @ric_FormControl.setter
    def ric_FormControl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_FormControl__ric_FormControl", None)
        self.__ric_FormControl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_Label"):
                opp_val = getattr(old_value, "ric_Label", None)
                if opp_val == self:
                    setattr(old_value, "ric_Label", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_Label"):
                opp_val = getattr(value, "ric_Label", None)
                setattr(value, "ric_Label", self)

    @property
    def ric_FormControl5(self):
        return self.__ric_FormControl5

    @ric_FormControl5.setter
    def ric_FormControl5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_FormControl__ric_FormControl5", None)
        self.__ric_FormControl5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ric_ValueConstraint"):
                    opp_val = getattr(item, "ric_ValueConstraint", None)
                    
                    if opp_val == self:
                        setattr(item, "ric_ValueConstraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ric_ValueConstraint"):
                    opp_val = getattr(item, "ric_ValueConstraint", None)
                    
                    setattr(item, "ric_ValueConstraint", self)
                    

class ric_Event:

    def __init__(self, type: str, ric_Event: "ric_EventComponent" = None, ric_Event13: "ric_Script" = None, ric_Event24: "ric_Label" = None):
        self.type = type
        self.ric_Event = ric_Event
        self.ric_Event13 = ric_Event13
        self.ric_Event24 = ric_Event24
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def ric_Event24(self):
        return self.__ric_Event24

    @ric_Event24.setter
    def ric_Event24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Event__ric_Event24", None)
        self.__ric_Event24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_Label23"):
                opp_val = getattr(old_value, "ric_Label23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_Label23"):
                opp_val = getattr(value, "ric_Label23", None)
                if opp_val is None:
                    setattr(value, "ric_Label23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ric_Event13(self):
        return self.__ric_Event13

    @ric_Event13.setter
    def ric_Event13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Event__ric_Event13", None)
        self.__ric_Event13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_Script"):
                opp_val = getattr(old_value, "ric_Script", None)
                if opp_val == self:
                    setattr(old_value, "ric_Script", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_Script"):
                opp_val = getattr(value, "ric_Script", None)
                setattr(value, "ric_Script", self)

    @property
    def ric_Event(self):
        return self.__ric_Event

    @ric_Event.setter
    def ric_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ric_Event__ric_Event", None)
        self.__ric_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ric_EventComponent"):
                opp_val = getattr(old_value, "ric_EventComponent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ric_EventComponent"):
                opp_val = getattr(value, "ric_EventComponent", None)
                if opp_val is None:
                    setattr(value, "ric_EventComponent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ric_EventComponent(ABC):

    pass
class ric_ClassifiableComponent(ABC):

    def __init__(self, class: str):
        self.class = class
        
    @property
    def class(self) -> str:
        return self.__class

    @class.setter
    def class(self, class: str):
        self.__class = class

class ric_IdentifiableComponent(ABC):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id
