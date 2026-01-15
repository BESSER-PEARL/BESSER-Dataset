from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Type(Enum):
    int = "int"
    float = "float"


############################################
# Definition of Classes
############################################

class dsml_visitor_Visitor(ABC):

    def __init__(self, tag: str):
        self.tag = tag
        
    @property
    def tag(self) -> str:
        return self.__tag

    @tag.setter
    def tag(self, tag: str):
        self.__tag = tag

class Visitor:

    pass
class dsml_visitor_ResourceVisitor(Visitor):

    pass
class dsml_visitor_POJOVisitor(Visitor):

    pass
class dsml_visitor_JSPVisitor(Visitor):

    pass
class dsml_web_Validator(ABC):

    def __init__(self):
        
    def accept(self, visitor: str) -> str:
        # TODO: Implement accept method
        pass

class dsml_web_Text:

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    def accept(self, visitor: str) -> str:
        # TODO: Implement accept method
        pass

class Error:

    pass
class Success:

    pass
class dsml_web_Error:

    pass
class dsml_web_Success:

    pass
class dsml_web_Item:

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class Button:

    pass
class dsml_web_CancelButton(Button):

    pass
class dsml_web_SubmitButton(Button):

    pass
class ListField:

    pass
class dsml_web_RadioButton(ListField):

    pass
class dsml_web_Form:

    def __init__(self, action: str, dsml_web_Form: set["FormElement"] = None, dsml_web_Form12: "Success" = None, dsml_web_Form14: "Error" = None):
        self.action = action
        self.dsml_web_Form = dsml_web_Form if dsml_web_Form is not None else set()
        self.dsml_web_Form12 = dsml_web_Form12
        self.dsml_web_Form14 = dsml_web_Form14
        
    @property
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

    @property
    def dsml_web_Form12(self):
        return self.__dsml_web_Form12

    @dsml_web_Form12.setter
    def dsml_web_Form12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsml_web_Form__dsml_web_Form12", None)
        self.__dsml_web_Form12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Success"):
                opp_val = getattr(old_value, "Success", None)
                if opp_val == self:
                    setattr(old_value, "Success", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Success"):
                opp_val = getattr(value, "Success", None)
                setattr(value, "Success", self)

    @property
    def dsml_web_Form(self):
        return self.__dsml_web_Form

    @dsml_web_Form.setter
    def dsml_web_Form(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsml_web_Form__dsml_web_Form", None)
        self.__dsml_web_Form = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FormElement"):
                    opp_val = getattr(item, "FormElement", None)
                    
                    if opp_val == self:
                        setattr(item, "FormElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FormElement"):
                    opp_val = getattr(item, "FormElement", None)
                    
                    setattr(item, "FormElement", self)
                    

    @property
    def dsml_web_Form14(self):
        return self.__dsml_web_Form14

    @dsml_web_Form14.setter
    def dsml_web_Form14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsml_web_Form__dsml_web_Form14", None)
        self.__dsml_web_Form14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Error"):
                opp_val = getattr(old_value, "Error", None)
                if opp_val == self:
                    setattr(old_value, "Error", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Error"):
                opp_val = getattr(value, "Error", None)
                setattr(value, "Error", self)

    def accept(self, visitor: str) -> str:
        # TODO: Implement accept method
        pass

class dsml_web_FormElement(ABC):

    def __init__(self, name: str, value: str):
        self.name = name
        self.value = value
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    def accept(self, visitor: str) -> str:
        # TODO: Implement accept method
        pass

class dsml_web_Link:

    def __init__(self, value: str, dsml_web_Link: "Page" = None):
        self.value = value
        self.dsml_web_Link = dsml_web_Link
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def dsml_web_Link(self):
        return self.__dsml_web_Link

    @dsml_web_Link.setter
    def dsml_web_Link(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsml_web_Link__dsml_web_Link", None)
        self.__dsml_web_Link = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Page9"):
                opp_val = getattr(old_value, "Page9", None)
                if opp_val == self:
                    setattr(old_value, "Page9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Page9"):
                opp_val = getattr(value, "Page9", None)
                setattr(value, "Page9", self)

    def accept(self, visitor: str) -> str:
        # TODO: Implement accept method
        pass

class dsml_web_ResetButton(Button):

    pass
class Item:

    pass
class dsml_web_Select(ListField):

    def __init__(self, size: int):
        self.size = size
        
    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

class Field:

    pass
class dsml_web_PasswordField(Field):

    def __init__(self, size: int, maxlength: int):
        self.size = size
        self.maxlength = maxlength
        
    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def maxlength(self) -> int:
        return self.__maxlength

    @maxlength.setter
    def maxlength(self, maxlength: int):
        self.__maxlength = maxlength

class dsml_web_TextArea(Field):

    def __init__(self, cols: int, rows: int):
        self.cols = cols
        self.rows = rows
        
    @property
    def rows(self) -> int:
        return self.__rows

    @rows.setter
    def rows(self, rows: int):
        self.__rows = rows

    @property
    def cols(self) -> int:
        return self.__cols

    @cols.setter
    def cols(self, cols: int):
        self.__cols = cols

class dsml_web_TextField(Field):

    def __init__(self, size: int, maxlength: int):
        self.size = size
        self.maxlength = maxlength
        
    @property
    def maxlength(self) -> int:
        return self.__maxlength

    @maxlength.setter
    def maxlength(self, maxlength: int):
        self.__maxlength = maxlength

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

class Validator:

    pass
class dsml_web_TypeValidator(Validator):

    def __init__(self, type: str, Validator: "dsml_web_Field"):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class dsml_web_DateValidator(Validator):

    pass
class dsml_web_RegexValidator(Validator):

    def __init__(self, regex: str, Validator: "dsml_web_Field"):
        self.regex = regex
        
    @property
    def regex(self) -> str:
        return self.__regex

    @regex.setter
    def regex(self, regex: str):
        self.__regex = regex

class dsml_web_BetweenValidator(Validator):

    def __init__(self, valueL: int, valueG: int, Validator: "dsml_web_Field"):
        self.valueL = valueL
        self.valueG = valueG
        
    @property
    def valueL(self) -> int:
        return self.__valueL

    @valueL.setter
    def valueL(self, valueL: int):
        self.__valueL = valueL

    @property
    def valueG(self) -> int:
        return self.__valueG

    @valueG.setter
    def valueG(self, valueG: int):
        self.__valueG = valueG

class dsml_web_EmailValidator(Validator):

    pass
class dsml_web_GreaterThanValidator(Validator):

    def __init__(self, value: int, Validator: "dsml_web_Field"):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class dsml_web_URLValidator(Validator):

    pass
class dsml_web_Required(Validator):

    pass
class dsml_web_LessThanValidator(Validator):

    def __init__(self, value: int, Validator: "dsml_web_Field"):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class dsml_web_StringLengthValidator(Validator):

    def __init__(self, min: int, max: int, Validator: "dsml_web_Field"):
        self.min = min
        self.max = max
        
    @property
    def min(self) -> int:
        return self.__min

    @min.setter
    def min(self, min: int):
        self.__min = min

    @property
    def max(self) -> int:
        return self.__max

    @max.setter
    def max(self, max: int):
        self.__max = max

class dsml_web_TimeValidator(Validator):

    pass
class FormElement:

    pass
class dsml_web_Label(FormElement):

    pass
class dsml_web_Button(FormElement):

    pass
class dsml_web_Hidden(FormElement):

    pass
class dsml_web_ListField(FormElement):

    pass
class dsml_web_CheckBox(FormElement):

    pass
class dsml_web_Field(FormElement):

    pass
class Link:

    pass
class Text:

    pass
class Form:

    pass
class dsml_web_Page:

    def __init__(self, title: str, name: str, dsml_web_Page: "Form" = None, dsml_web_Page3: set["Text"] = None, dsml_web_Page5: set["Link"] = None):
        self.title = title
        self.name = name
        self.dsml_web_Page = dsml_web_Page
        self.dsml_web_Page3 = dsml_web_Page3 if dsml_web_Page3 is not None else set()
        self.dsml_web_Page5 = dsml_web_Page5 if dsml_web_Page5 is not None else set()
        
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
    def dsml_web_Page5(self):
        return self.__dsml_web_Page5

    @dsml_web_Page5.setter
    def dsml_web_Page5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsml_web_Page__dsml_web_Page5", None)
        self.__dsml_web_Page5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Link"):
                    opp_val = getattr(item, "Link", None)
                    
                    if opp_val == self:
                        setattr(item, "Link", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Link"):
                    opp_val = getattr(item, "Link", None)
                    
                    setattr(item, "Link", self)
                    

    @property
    def dsml_web_Page3(self):
        return self.__dsml_web_Page3

    @dsml_web_Page3.setter
    def dsml_web_Page3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsml_web_Page__dsml_web_Page3", None)
        self.__dsml_web_Page3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Text"):
                    opp_val = getattr(item, "Text", None)
                    
                    if opp_val == self:
                        setattr(item, "Text", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Text"):
                    opp_val = getattr(item, "Text", None)
                    
                    setattr(item, "Text", self)
                    

    @property
    def dsml_web_Page(self):
        return self.__dsml_web_Page

    @dsml_web_Page.setter
    def dsml_web_Page(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsml_web_Page__dsml_web_Page", None)
        self.__dsml_web_Page = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Form"):
                opp_val = getattr(old_value, "Form", None)
                if opp_val == self:
                    setattr(old_value, "Form", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Form"):
                opp_val = getattr(value, "Form", None)
                setattr(value, "Form", self)

class Page:

    pass
class dsml_web_Website:

    def __init__(self, name: str, dsml_web_Website: set["Page"] = None):
        self.name = name
        self.dsml_web_Website = dsml_web_Website if dsml_web_Website is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsml_web_Website(self):
        return self.__dsml_web_Website

    @dsml_web_Website.setter
    def dsml_web_Website(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsml_web_Website__dsml_web_Website", None)
        self.__dsml_web_Website = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Page"):
                    opp_val = getattr(item, "Page", None)
                    
                    if opp_val == self:
                        setattr(item, "Page", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Page"):
                    opp_val = getattr(item, "Page", None)
                    
                    setattr(item, "Page", self)
                    
