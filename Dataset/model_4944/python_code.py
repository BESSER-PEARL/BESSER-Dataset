from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class forms_Form:

    def __init__(self, caption: str, form: set["forms_Group"] = None, Form: "forms_Group" = None):
        self.caption = caption
        self.form = form if form is not None else set()
        self.Form = Form
        
    @property
    def caption(self) -> str:
        return self.__caption

    @caption.setter
    def caption(self, caption: str):
        self.__caption = caption

    @property
    def form(self):
        return self.__form

    @form.setter
    def form(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Form__form", None)
        self.__form = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Group"):
                    opp_val = getattr(item, "Group", None)
                    
                    if opp_val == self:
                        setattr(item, "Group", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Group"):
                    opp_val = getattr(item, "Group", None)
                    
                    setattr(item, "Group", self)
                    

    @property
    def Form(self):
        return self.__Form

    @Form.setter
    def Form(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Form__Form", None)
        self.__Form = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "groups"):
                opp_val = getattr(old_value, "groups", None)
                if opp_val == self:
                    setattr(old_value, "groups", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "groups"):
                opp_val = getattr(value, "groups", None)
                setattr(value, "groups", self)

class ItemType:

    pass
class forms_Date(ItemType):

    pass
class forms_Choice(ItemType):

    def __init__(self, multiple: bool, forms_Choice: set["forms_Option"] = None):
        self.multiple = multiple
        self.forms_Choice = forms_Choice if forms_Choice is not None else set()
        
    @property
    def multiple(self) -> bool:
        return self.__multiple

    @multiple.setter
    def multiple(self, multiple: bool):
        self.__multiple = multiple

    @property
    def forms_Choice(self):
        return self.__forms_Choice

    @forms_Choice.setter
    def forms_Choice(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Choice__forms_Choice", None)
        self.__forms_Choice = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "forms_Option5"):
                    opp_val = getattr(item, "forms_Option5", None)
                    
                    if opp_val == self:
                        setattr(item, "forms_Option5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "forms_Option5"):
                    opp_val = getattr(item, "forms_Option5", None)
                    
                    setattr(item, "forms_Option5", self)
                    

class forms_Number(ItemType):

    pass
class forms_Decision(ItemType):

    pass
class forms_FreeText(ItemType):

    pass
class forms_Option:

    def __init__(self, id: str, text: str, forms_Option: "forms_Item" = None, forms_Option5: "forms_Choice" = None, forms_Option10: "forms_Decision" = None):
        self.id = id
        self.text = text
        self.forms_Option = forms_Option
        self.forms_Option5 = forms_Option5
        self.forms_Option10 = forms_Option10
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def forms_Option10(self):
        return self.__forms_Option10

    @forms_Option10.setter
    def forms_Option10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Option__forms_Option10", None)
        self.__forms_Option10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Decision"):
                opp_val = getattr(old_value, "forms_Decision", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Decision"):
                opp_val = getattr(value, "forms_Decision", None)
                if opp_val is None:
                    setattr(value, "forms_Decision", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def forms_Option(self):
        return self.__forms_Option

    @forms_Option.setter
    def forms_Option(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Option__forms_Option", None)
        self.__forms_Option = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Item3"):
                opp_val = getattr(old_value, "forms_Item3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Item3"):
                opp_val = getattr(value, "forms_Item3", None)
                if opp_val is None:
                    setattr(value, "forms_Item3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def forms_Option5(self):
        return self.__forms_Option5

    @forms_Option5.setter
    def forms_Option5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Option__forms_Option5", None)
        self.__forms_Option5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Choice"):
                opp_val = getattr(old_value, "forms_Choice", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Choice"):
                opp_val = getattr(value, "forms_Choice", None)
                if opp_val is None:
                    setattr(value, "forms_Choice", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class forms_ItemType(ABC):

    pass
class forms_Item:

    def __init__(self, text: str, explanation: str, forms_Item: "forms_ItemType" = None, forms_Item3: set["forms_Option"] = None, forms_Item7: "forms_Group" = None):
        self.text = text
        self.explanation = explanation
        self.forms_Item = forms_Item
        self.forms_Item3 = forms_Item3 if forms_Item3 is not None else set()
        self.forms_Item7 = forms_Item7
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def explanation(self) -> str:
        return self.__explanation

    @explanation.setter
    def explanation(self, explanation: str):
        self.__explanation = explanation

    @property
    def forms_Item7(self):
        return self.__forms_Item7

    @forms_Item7.setter
    def forms_Item7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Item__forms_Item7", None)
        self.__forms_Item7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Group"):
                opp_val = getattr(old_value, "forms_Group", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Group"):
                opp_val = getattr(value, "forms_Group", None)
                if opp_val is None:
                    setattr(value, "forms_Group", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def forms_Item(self):
        return self.__forms_Item

    @forms_Item.setter
    def forms_Item(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Item__forms_Item", None)
        self.__forms_Item = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_ItemType"):
                opp_val = getattr(old_value, "forms_ItemType", None)
                if opp_val == self:
                    setattr(old_value, "forms_ItemType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_ItemType"):
                opp_val = getattr(value, "forms_ItemType", None)
                setattr(value, "forms_ItemType", self)

    @property
    def forms_Item3(self):
        return self.__forms_Item3

    @forms_Item3.setter
    def forms_Item3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Item__forms_Item3", None)
        self.__forms_Item3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "forms_Option"):
                    opp_val = getattr(item, "forms_Option", None)
                    
                    if opp_val == self:
                        setattr(item, "forms_Option", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "forms_Option"):
                    opp_val = getattr(item, "forms_Option", None)
                    
                    setattr(item, "forms_Option", self)
                    

class forms_Group:

    def __init__(self, name: str, Group: "forms_Form" = None, forms_Group: set["forms_Item"] = None, groups: "forms_Form" = None):
        self.name = name
        self.Group = Group
        self.forms_Group = forms_Group if forms_Group is not None else set()
        self.groups = groups
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def forms_Group(self):
        return self.__forms_Group

    @forms_Group.setter
    def forms_Group(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Group__forms_Group", None)
        self.__forms_Group = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "forms_Item7"):
                    opp_val = getattr(item, "forms_Item7", None)
                    
                    if opp_val == self:
                        setattr(item, "forms_Item7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "forms_Item7"):
                    opp_val = getattr(item, "forms_Item7", None)
                    
                    setattr(item, "forms_Item7", self)
                    

    @property
    def groups(self):
        return self.__groups

    @groups.setter
    def groups(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Group__groups", None)
        self.__groups = value
        
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

    @property
    def Group(self):
        return self.__Group

    @Group.setter
    def Group(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Group__Group", None)
        self.__Group = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form"):
                opp_val = getattr(old_value, "form", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form"):
                opp_val = getattr(value, "form", None)
                if opp_val is None:
                    setattr(value, "form", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
