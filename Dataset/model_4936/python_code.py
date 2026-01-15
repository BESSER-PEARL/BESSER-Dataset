from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class DateFormat(Enum):
    DayMonthYear = "DayMonthYear"
    YearMonthDay = "YearMonthDay"


############################################
# Definition of Classes
############################################

class webapp_DynamicWebApp:

    def __init__(self, name: str, webapp_DynamicWebApp: set["webapp_Page"] = None):
        self.name = name
        self.webapp_DynamicWebApp = webapp_DynamicWebApp if webapp_DynamicWebApp is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def webapp_DynamicWebApp(self):
        return self.__webapp_DynamicWebApp

    @webapp_DynamicWebApp.setter
    def webapp_DynamicWebApp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_DynamicWebApp__webapp_DynamicWebApp", None)
        self.__webapp_DynamicWebApp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "webapp_Page13"):
                    opp_val = getattr(item, "webapp_Page13", None)
                    
                    if opp_val == self:
                        setattr(item, "webapp_Page13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "webapp_Page13"):
                    opp_val = getattr(item, "webapp_Page13", None)
                    
                    setattr(item, "webapp_Page13", self)
                    

class TextBox:

    pass
class webapp_EmailBox(TextBox):

    pass
class webapp_DateBox(TextBox):

    def __init__(self, format: str):
        self.format = format
        
    @property
    def format(self) -> str:
        return self.__format

    @format.setter
    def format(self, format: str):
        self.__format = format

class webapp_PasswordBox(TextBox):

    pass
class FormButton:

    pass
class webapp_SubmitButton(FormButton):

    pass
class webapp_ResetButton(FormButton):

    pass
class NormalControl:

    pass
class webapp_NormalButton(NormalControl):

    pass
class Control:

    pass
class webapp_CheckBox(Control):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class webapp_FormButton(Control):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class webapp_Link(Control, NormalControl):

    pass
class webapp_Label(NormalControl, Control):

    pass
class webapp_NormalControl(Control):

    def __init__(self, text: str, webapp_NormalControl: "webapp_NormalPage" = None):
        self.text = text
        self.webapp_NormalControl = webapp_NormalControl
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def webapp_NormalControl(self):
        return self.__webapp_NormalControl

    @webapp_NormalControl.setter
    def webapp_NormalControl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_NormalControl__webapp_NormalControl", None)
        self.__webapp_NormalControl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_NormalPage"):
                opp_val = getattr(old_value, "webapp_NormalPage", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_NormalPage"):
                opp_val = getattr(value, "webapp_NormalPage", None)
                if opp_val is None:
                    setattr(value, "webapp_NormalPage", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class webapp_RadioButton(Control):

    pass
class webapp_ListElement:

    def __init__(self, value: str, webapp_ListElement: "webapp_DropDownList" = None, webapp_ListElement11: "webapp_RadioButton" = None):
        self.value = value
        self.webapp_ListElement = webapp_ListElement
        self.webapp_ListElement11 = webapp_ListElement11
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def webapp_ListElement(self):
        return self.__webapp_ListElement

    @webapp_ListElement.setter
    def webapp_ListElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_ListElement__webapp_ListElement", None)
        self.__webapp_ListElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_DropDownList"):
                opp_val = getattr(old_value, "webapp_DropDownList", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_DropDownList"):
                opp_val = getattr(value, "webapp_DropDownList", None)
                if opp_val is None:
                    setattr(value, "webapp_DropDownList", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def webapp_ListElement11(self):
        return self.__webapp_ListElement11

    @webapp_ListElement11.setter
    def webapp_ListElement11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_ListElement__webapp_ListElement11", None)
        self.__webapp_ListElement11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_RadioButton"):
                opp_val = getattr(old_value, "webapp_RadioButton", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_RadioButton"):
                opp_val = getattr(value, "webapp_RadioButton", None)
                if opp_val is None:
                    setattr(value, "webapp_RadioButton", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class webapp_DropDownList(Control):

    pass
class webapp_TextBox(Control):

    def __init__(self, text: str, maxLength: int, size: int, required: bool):
        self.text = text
        self.maxLength = maxLength
        self.size = size
        self.required = required
        
    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def maxLength(self) -> int:
        return self.__maxLength

    @maxLength.setter
    def maxLength(self, maxLength: int):
        self.__maxLength = maxLength

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def required(self) -> bool:
        return self.__required

    @required.setter
    def required(self, required: bool):
        self.__required = required

class webapp_Control(ABC):

    def __init__(self, id: str, name: str, webapp_Control: "webapp_FormPage" = None):
        self.id = id
        self.name = name
        self.webapp_Control = webapp_Control
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def webapp_Control(self):
        return self.__webapp_Control

    @webapp_Control.setter
    def webapp_Control(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Control__webapp_Control", None)
        self.__webapp_Control = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_FormPage5"):
                opp_val = getattr(old_value, "webapp_FormPage5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_FormPage5"):
                opp_val = getattr(value, "webapp_FormPage5", None)
                if opp_val is None:
                    setattr(value, "webapp_FormPage5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Page:

    pass
class webapp_NormalPage(Page):

    pass
class webapp_FormPage(Page):

    def __init__(self, persist: bool, webapp_FormPage: "webapp_Page" = None, webapp_FormPage2: "webapp_Page" = None, webapp_FormPage5: set["webapp_Control"] = None):
        self.persist = persist
        self.webapp_FormPage = webapp_FormPage
        self.webapp_FormPage2 = webapp_FormPage2
        self.webapp_FormPage5 = webapp_FormPage5 if webapp_FormPage5 is not None else set()
        
    @property
    def persist(self) -> bool:
        return self.__persist

    @persist.setter
    def persist(self, persist: bool):
        self.__persist = persist

    @property
    def webapp_FormPage2(self):
        return self.__webapp_FormPage2

    @webapp_FormPage2.setter
    def webapp_FormPage2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_FormPage__webapp_FormPage2", None)
        self.__webapp_FormPage2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Page3"):
                opp_val = getattr(old_value, "webapp_Page3", None)
                if opp_val == self:
                    setattr(old_value, "webapp_Page3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Page3"):
                opp_val = getattr(value, "webapp_Page3", None)
                setattr(value, "webapp_Page3", self)

    @property
    def webapp_FormPage(self):
        return self.__webapp_FormPage

    @webapp_FormPage.setter
    def webapp_FormPage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_FormPage__webapp_FormPage", None)
        self.__webapp_FormPage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Page"):
                opp_val = getattr(old_value, "webapp_Page", None)
                if opp_val == self:
                    setattr(old_value, "webapp_Page", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Page"):
                opp_val = getattr(value, "webapp_Page", None)
                setattr(value, "webapp_Page", self)

    @property
    def webapp_FormPage5(self):
        return self.__webapp_FormPage5

    @webapp_FormPage5.setter
    def webapp_FormPage5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_FormPage__webapp_FormPage5", None)
        self.__webapp_FormPage5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "webapp_Control"):
                    opp_val = getattr(item, "webapp_Control", None)
                    
                    if opp_val == self:
                        setattr(item, "webapp_Control", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "webapp_Control"):
                    opp_val = getattr(item, "webapp_Control", None)
                    
                    setattr(item, "webapp_Control", self)
                    

class webapp_Page(ABC):

    def __init__(self, name: str, title: str, default: bool, webapp_Page: "webapp_FormPage" = None, webapp_Page3: "webapp_FormPage" = None, webapp_Page8: "webapp_Link" = None, webapp_Page13: "webapp_DynamicWebApp" = None):
        self.name = name
        self.title = title
        self.default = default
        self.webapp_Page = webapp_Page
        self.webapp_Page3 = webapp_Page3
        self.webapp_Page8 = webapp_Page8
        self.webapp_Page13 = webapp_Page13
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def default(self) -> bool:
        return self.__default

    @default.setter
    def default(self, default: bool):
        self.__default = default

    @property
    def webapp_Page3(self):
        return self.__webapp_Page3

    @webapp_Page3.setter
    def webapp_Page3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Page__webapp_Page3", None)
        self.__webapp_Page3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_FormPage2"):
                opp_val = getattr(old_value, "webapp_FormPage2", None)
                if opp_val == self:
                    setattr(old_value, "webapp_FormPage2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_FormPage2"):
                opp_val = getattr(value, "webapp_FormPage2", None)
                setattr(value, "webapp_FormPage2", self)

    @property
    def webapp_Page8(self):
        return self.__webapp_Page8

    @webapp_Page8.setter
    def webapp_Page8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Page__webapp_Page8", None)
        self.__webapp_Page8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_Link"):
                opp_val = getattr(old_value, "webapp_Link", None)
                if opp_val == self:
                    setattr(old_value, "webapp_Link", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_Link"):
                opp_val = getattr(value, "webapp_Link", None)
                setattr(value, "webapp_Link", self)

    @property
    def webapp_Page(self):
        return self.__webapp_Page

    @webapp_Page.setter
    def webapp_Page(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Page__webapp_Page", None)
        self.__webapp_Page = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_FormPage"):
                opp_val = getattr(old_value, "webapp_FormPage", None)
                if opp_val == self:
                    setattr(old_value, "webapp_FormPage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_FormPage"):
                opp_val = getattr(value, "webapp_FormPage", None)
                setattr(value, "webapp_FormPage", self)

    @property
    def webapp_Page13(self):
        return self.__webapp_Page13

    @webapp_Page13.setter
    def webapp_Page13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_webapp_Page__webapp_Page13", None)
        self.__webapp_Page13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webapp_DynamicWebApp"):
                opp_val = getattr(old_value, "webapp_DynamicWebApp", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webapp_DynamicWebApp"):
                opp_val = getattr(value, "webapp_DynamicWebApp", None)
                if opp_val is None:
                    setattr(value, "webapp_DynamicWebApp", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
