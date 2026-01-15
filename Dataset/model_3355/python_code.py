from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Widget:

    pass
class uispecDsl_CheckBoxWidget(Widget):

    pass
class uispecDsl_ComboWidget(Widget):

    def __init__(self, values: str):
        self.values = values
        
    @property
    def values(self) -> str:
        return self.__values

    @values.setter
    def values(self, values: str):
        self.__values = values

class uispecDsl_TextFieldWidget(Widget):

    def __init__(self, length: int):
        self.length = length
        
    @property
    def length(self) -> int:
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length

class uispecDsl_Attribute:

    pass
class uispecDsl_Widget:

    pass
class uispecDsl_Entity:

    pass
class uispecDsl_Field:

    def __init__(self, label: str, uispecDsl_Field: "uispecDsl_Form" = None, uispecDsl_Field6: "uispecDsl_Widget" = None, uispecDsl_Field8: "uispecDsl_Attribute" = None):
        self.label = label
        self.uispecDsl_Field = uispecDsl_Field
        self.uispecDsl_Field6 = uispecDsl_Field6
        self.uispecDsl_Field8 = uispecDsl_Field8
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def uispecDsl_Field8(self):
        return self.__uispecDsl_Field8

    @uispecDsl_Field8.setter
    def uispecDsl_Field8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uispecDsl_Field__uispecDsl_Field8", None)
        self.__uispecDsl_Field8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uispecDsl_Attribute"):
                opp_val = getattr(old_value, "uispecDsl_Attribute", None)
                if opp_val == self:
                    setattr(old_value, "uispecDsl_Attribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uispecDsl_Attribute"):
                opp_val = getattr(value, "uispecDsl_Attribute", None)
                setattr(value, "uispecDsl_Attribute", self)

    @property
    def uispecDsl_Field6(self):
        return self.__uispecDsl_Field6

    @uispecDsl_Field6.setter
    def uispecDsl_Field6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uispecDsl_Field__uispecDsl_Field6", None)
        self.__uispecDsl_Field6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uispecDsl_Widget"):
                opp_val = getattr(old_value, "uispecDsl_Widget", None)
                if opp_val == self:
                    setattr(old_value, "uispecDsl_Widget", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uispecDsl_Widget"):
                opp_val = getattr(value, "uispecDsl_Widget", None)
                setattr(value, "uispecDsl_Widget", self)

    @property
    def uispecDsl_Field(self):
        return self.__uispecDsl_Field

    @uispecDsl_Field.setter
    def uispecDsl_Field(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uispecDsl_Field__uispecDsl_Field", None)
        self.__uispecDsl_Field = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uispecDsl_Form2"):
                opp_val = getattr(old_value, "uispecDsl_Form2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uispecDsl_Form2"):
                opp_val = getattr(value, "uispecDsl_Form2", None)
                if opp_val is None:
                    setattr(value, "uispecDsl_Form2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class uispecDsl_EntityReference:

    pass
class uispecDsl_Form:

    def __init__(self, name: str, uispecDsl_Form: set["uispecDsl_EntityReference"] = None, uispecDsl_Form2: set["uispecDsl_Field"] = None):
        self.name = name
        self.uispecDsl_Form = uispecDsl_Form if uispecDsl_Form is not None else set()
        self.uispecDsl_Form2 = uispecDsl_Form2 if uispecDsl_Form2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uispecDsl_Form(self):
        return self.__uispecDsl_Form

    @uispecDsl_Form.setter
    def uispecDsl_Form(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uispecDsl_Form__uispecDsl_Form", None)
        self.__uispecDsl_Form = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uispecDsl_EntityReference"):
                    opp_val = getattr(item, "uispecDsl_EntityReference", None)
                    
                    if opp_val == self:
                        setattr(item, "uispecDsl_EntityReference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uispecDsl_EntityReference"):
                    opp_val = getattr(item, "uispecDsl_EntityReference", None)
                    
                    setattr(item, "uispecDsl_EntityReference", self)
                    

    @property
    def uispecDsl_Form2(self):
        return self.__uispecDsl_Form2

    @uispecDsl_Form2.setter
    def uispecDsl_Form2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_uispecDsl_Form__uispecDsl_Form2", None)
        self.__uispecDsl_Form2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "uispecDsl_Field"):
                    opp_val = getattr(item, "uispecDsl_Field", None)
                    
                    if opp_val == self:
                        setattr(item, "uispecDsl_Field", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "uispecDsl_Field"):
                    opp_val = getattr(item, "uispecDsl_Field", None)
                    
                    setattr(item, "uispecDsl_Field", self)
                    
