from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ItemType:

    pass
class forms_Number(ItemType):

    pass
class forms_Decision(ItemType):

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

class forms_ItemType(ABC):

    pass
class forms_Item:

    def __init__(self, text: str, explanation: str, forms_Item: "forms_ItemType" = None, forms_Item3: set["forms_Option"] = None, forms_Item8: "forms_Group" = None):
        self.text = text
        self.explanation = explanation
        self.forms_Item = forms_Item
        self.forms_Item3 = forms_Item3 if forms_Item3 is not None else set()
        self.forms_Item8 = forms_Item8
        
    @property
    def explanation(self) -> str:
        return self.__explanation

    @explanation.setter
    def explanation(self, explanation: str):
        self.__explanation = explanation

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

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
                    

    @property
    def forms_Item8(self):
        return self.__forms_Item8

    @forms_Item8.setter
    def forms_Item8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Item__forms_Item8", None)
        self.__forms_Item8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Group7"):
                opp_val = getattr(old_value, "forms_Group7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Group7"):
                opp_val = getattr(value, "forms_Group7", None)
                if opp_val is None:
                    setattr(value, "forms_Group7", set([self]))
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

class forms_Group:

    def __init__(self, name: str, forms_Group: "forms_Form" = None, forms_Group7: set["forms_Item"] = None):
        self.name = name
        self.forms_Group = forms_Group
        self.forms_Group7 = forms_Group7 if forms_Group7 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def forms_Group7(self):
        return self.__forms_Group7

    @forms_Group7.setter
    def forms_Group7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Group__forms_Group7", None)
        self.__forms_Group7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "forms_Item8"):
                    opp_val = getattr(item, "forms_Item8", None)
                    
                    if opp_val == self:
                        setattr(item, "forms_Item8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "forms_Item8"):
                    opp_val = getattr(item, "forms_Item8", None)
                    
                    setattr(item, "forms_Item8", self)
                    

    @property
    def forms_Group(self):
        return self.__forms_Group

    @forms_Group.setter
    def forms_Group(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Group__forms_Group", None)
        self.__forms_Group = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Form"):
                opp_val = getattr(old_value, "forms_Form", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Form"):
                opp_val = getattr(value, "forms_Form", None)
                if opp_val is None:
                    setattr(value, "forms_Form", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class forms_Form:

    def __init__(self, caption: str, forms_Form: set["forms_Group"] = None):
        self.caption = caption
        self.forms_Form = forms_Form if forms_Form is not None else set()
        
    @property
    def caption(self) -> str:
        return self.__caption

    @caption.setter
    def caption(self, caption: str):
        self.__caption = caption

    @property
    def forms_Form(self):
        return self.__forms_Form

    @forms_Form.setter
    def forms_Form(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Form__forms_Form", None)
        self.__forms_Form = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "forms_Group"):
                    opp_val = getattr(item, "forms_Group", None)
                    
                    if opp_val == self:
                        setattr(item, "forms_Group", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "forms_Group"):
                    opp_val = getattr(item, "forms_Group", None)
                    
                    setattr(item, "forms_Group", self)
                    
