from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class form_option:

    def __init__(self, content: str, value: str, form_option: "form_SelectionList" = None):
        self.content = content
        self.value = value
        self.form_option = form_option
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def form_option(self):
        return self.__form_option

    @form_option.setter
    def form_option(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_option__form_option", None)
        self.__form_option = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_SelectionList"):
                opp_val = getattr(old_value, "form_SelectionList", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_SelectionList"):
                opp_val = getattr(value, "form_SelectionList", None)
                if opp_val is None:
                    setattr(value, "form_SelectionList", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Editable:

    pass
class form_SelectionList(Editable):

    def __init__(self, multiple: bool, form_SelectionList: set["form_option"] = None):
        self.multiple = multiple
        self.form_SelectionList = form_SelectionList if form_SelectionList is not None else set()
        
    @property
    def multiple(self) -> bool:
        return self.__multiple

    @multiple.setter
    def multiple(self, multiple: bool):
        self.__multiple = multiple

    @property
    def form_SelectionList(self):
        return self.__form_SelectionList

    @form_SelectionList.setter
    def form_SelectionList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_SelectionList__form_SelectionList", None)
        self.__form_SelectionList = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "form_option"):
                    opp_val = getattr(item, "form_option", None)
                    
                    if opp_val == self:
                        setattr(item, "form_option", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "form_option"):
                    opp_val = getattr(item, "form_option", None)
                    
                    setattr(item, "form_option", self)
                    

class form_Input(Editable):

    def __init__(self, checked: bool, type: str, value: str):
        self.checked = checked
        self.type = type
        self.value = value
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def checked(self) -> bool:
        return self.__checked

    @checked.setter
    def checked(self, checked: bool):
        self.__checked = checked

class Element:

    pass
class form_Editable(Element):

    def __init__(self, disabled: bool, name: str, form_Editable: "form_Label" = None):
        self.disabled = disabled
        self.name = name
        self.form_Editable = form_Editable
        
    @property
    def disabled(self) -> bool:
        return self.__disabled

    @disabled.setter
    def disabled(self, disabled: bool):
        self.__disabled = disabled

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def form_Editable(self):
        return self.__form_Editable

    @form_Editable.setter
    def form_Editable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Editable__form_Editable", None)
        self.__form_Editable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Label"):
                opp_val = getattr(old_value, "form_Label", None)
                if opp_val == self:
                    setattr(old_value, "form_Label", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Label"):
                opp_val = getattr(value, "form_Label", None)
                setattr(value, "form_Label", self)

class form_Label(Element):

    def __init__(self, content: str, for: str, form_Label: "form_Editable" = None):
        self.content = content
        self.for = for
        self.form_Label = form_Label
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def for(self) -> str:
        return self.__for

    @for.setter
    def for(self, for: str):
        self.__for = for

    @property
    def form_Label(self):
        return self.__form_Label

    @form_Label.setter
    def form_Label(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Label__form_Label", None)
        self.__form_Label = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Editable"):
                opp_val = getattr(old_value, "form_Editable", None)
                if opp_val == self:
                    setattr(old_value, "form_Editable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Editable"):
                opp_val = getattr(value, "form_Editable", None)
                setattr(value, "form_Editable", self)

class form_textArea(Editable):

    def __init__(self, content: str):
        self.content = content
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

class form_Orden:

    pass
class form_Element(ABC):

    pass
class form_Formulario:

    pass