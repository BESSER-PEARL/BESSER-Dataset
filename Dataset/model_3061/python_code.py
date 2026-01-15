from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class conditionType(Enum):
    Hide = "Hide"
    Show = "Show"
    Enable = "Enable"
    Disable = "Disable"
class AttributeType(Enum):
    String = "String"
    Text = "Text"
    Integer = "Integer"
    Date = "Date"
    Time = "Time"
    Email = "Email"
    Boolean = "Boolean"
    None = "None"


############################################
# Definition of Classes
############################################

class forms_EMFL_FormModel:

    pass
class forms_EMFL_EntityModel:

    pass
class forms_Condition(ABC):

    def __init__(self, conditionId: int, forms_Condition: "forms_EMFL_FormModel" = None):
        self.conditionId = conditionId
        self.forms_Condition = forms_Condition
        
    @property
    def conditionId(self) -> int:
        return self.__conditionId

    @conditionId.setter
    def conditionId(self, conditionId: int):
        self.__conditionId = conditionId

    @property
    def forms_Condition(self):
        return self.__forms_Condition

    @forms_Condition.setter
    def forms_Condition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Condition__forms_Condition", None)
        self.__forms_Condition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_EMFL_FormModel52"):
                opp_val = getattr(old_value, "forms_EMFL_FormModel52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_EMFL_FormModel52"):
                opp_val = getattr(value, "forms_EMFL_FormModel52", None)
                if opp_val is None:
                    setattr(value, "forms_EMFL_FormModel52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class forms_Column:

    pass
class RelationshipPageElement:

    pass
class forms_Table(RelationshipPageElement):

    pass
class forms_List(RelationshipPageElement):

    pass
class Condition:

    pass
class forms_AttributeValueCondition(Condition):

    def __init__(self, type: str, value: str, forms_AttributeValueCondition: "forms_CompositionCondition" = None, forms_AttributeValueCondition41: "forms_Page" = None, forms_AttributeValueCondition44: "forms_PageElement" = None, forms_AttributeValueCondition47: "forms_PageElement" = None):
        self.type = type
        self.value = value
        self.forms_AttributeValueCondition = forms_AttributeValueCondition
        self.forms_AttributeValueCondition41 = forms_AttributeValueCondition41
        self.forms_AttributeValueCondition44 = forms_AttributeValueCondition44
        self.forms_AttributeValueCondition47 = forms_AttributeValueCondition47
        
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
    def forms_AttributeValueCondition44(self):
        return self.__forms_AttributeValueCondition44

    @forms_AttributeValueCondition44.setter
    def forms_AttributeValueCondition44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_AttributeValueCondition__forms_AttributeValueCondition44", None)
        self.__forms_AttributeValueCondition44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_PageElement45"):
                opp_val = getattr(old_value, "forms_PageElement45", None)
                if opp_val == self:
                    setattr(old_value, "forms_PageElement45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_PageElement45"):
                opp_val = getattr(value, "forms_PageElement45", None)
                setattr(value, "forms_PageElement45", self)

    @property
    def forms_AttributeValueCondition(self):
        return self.__forms_AttributeValueCondition

    @forms_AttributeValueCondition.setter
    def forms_AttributeValueCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_AttributeValueCondition__forms_AttributeValueCondition", None)
        self.__forms_AttributeValueCondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_CompositionCondition"):
                opp_val = getattr(old_value, "forms_CompositionCondition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_CompositionCondition"):
                opp_val = getattr(value, "forms_CompositionCondition", None)
                if opp_val is None:
                    setattr(value, "forms_CompositionCondition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def forms_AttributeValueCondition41(self):
        return self.__forms_AttributeValueCondition41

    @forms_AttributeValueCondition41.setter
    def forms_AttributeValueCondition41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_AttributeValueCondition__forms_AttributeValueCondition41", None)
        self.__forms_AttributeValueCondition41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Page42"):
                opp_val = getattr(old_value, "forms_Page42", None)
                if opp_val == self:
                    setattr(old_value, "forms_Page42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Page42"):
                opp_val = getattr(value, "forms_Page42", None)
                setattr(value, "forms_Page42", self)

    @property
    def forms_AttributeValueCondition47(self):
        return self.__forms_AttributeValueCondition47

    @forms_AttributeValueCondition47.setter
    def forms_AttributeValueCondition47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_AttributeValueCondition__forms_AttributeValueCondition47", None)
        self.__forms_AttributeValueCondition47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_PageElement48"):
                opp_val = getattr(old_value, "forms_PageElement48", None)
                if opp_val == self:
                    setattr(old_value, "forms_PageElement48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_PageElement48"):
                opp_val = getattr(value, "forms_PageElement48", None)
                setattr(value, "forms_PageElement48", self)

class forms_CompositionCondition(Condition):

    def __init__(self, isAnd: bool, forms_CompositionCondition: set["forms_AttributeValueCondition"] = None, forms_CompositionCondition39: "forms_CompositionCondition" = None, forms_CompositionCondition37: set["forms_CompositionCondition"] = None):
        self.isAnd = isAnd
        self.forms_CompositionCondition = forms_CompositionCondition if forms_CompositionCondition is not None else set()
        self.forms_CompositionCondition39 = forms_CompositionCondition39
        self.forms_CompositionCondition37 = forms_CompositionCondition37 if forms_CompositionCondition37 is not None else set()
        
    @property
    def isAnd(self) -> bool:
        return self.__isAnd

    @isAnd.setter
    def isAnd(self, isAnd: bool):
        self.__isAnd = isAnd

    @property
    def forms_CompositionCondition37(self):
        return self.__forms_CompositionCondition37

    @forms_CompositionCondition37.setter
    def forms_CompositionCondition37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_CompositionCondition__forms_CompositionCondition37", None)
        self.__forms_CompositionCondition37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "forms_CompositionCondition39"):
                    opp_val = getattr(item, "forms_CompositionCondition39", None)
                    
                    if opp_val == self:
                        setattr(item, "forms_CompositionCondition39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "forms_CompositionCondition39"):
                    opp_val = getattr(item, "forms_CompositionCondition39", None)
                    
                    setattr(item, "forms_CompositionCondition39", self)
                    

    @property
    def forms_CompositionCondition39(self):
        return self.__forms_CompositionCondition39

    @forms_CompositionCondition39.setter
    def forms_CompositionCondition39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_CompositionCondition__forms_CompositionCondition39", None)
        self.__forms_CompositionCondition39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_CompositionCondition37"):
                opp_val = getattr(old_value, "forms_CompositionCondition37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_CompositionCondition37"):
                opp_val = getattr(value, "forms_CompositionCondition37", None)
                if opp_val is None:
                    setattr(value, "forms_CompositionCondition37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def forms_CompositionCondition(self):
        return self.__forms_CompositionCondition

    @forms_CompositionCondition.setter
    def forms_CompositionCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_CompositionCondition__forms_CompositionCondition", None)
        self.__forms_CompositionCondition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "forms_AttributeValueCondition"):
                    opp_val = getattr(item, "forms_AttributeValueCondition", None)
                    
                    if opp_val == self:
                        setattr(item, "forms_AttributeValueCondition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "forms_AttributeValueCondition"):
                    opp_val = getattr(item, "forms_AttributeValueCondition", None)
                    
                    setattr(item, "forms_AttributeValueCondition", self)
                    

class PageElement:

    pass
class forms_AttributePageElement(PageElement):

    pass
class forms_PageElement(ABC):

    def __init__(self, elementID: int, label: str, forms_PageElement: "forms_Page" = None, forms_PageElement45: "forms_AttributeValueCondition" = None, forms_PageElement48: "forms_AttributeValueCondition" = None):
        self.elementID = elementID
        self.label = label
        self.forms_PageElement = forms_PageElement
        self.forms_PageElement45 = forms_PageElement45
        self.forms_PageElement48 = forms_PageElement48
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def elementID(self) -> int:
        return self.__elementID

    @elementID.setter
    def elementID(self, elementID: int):
        self.__elementID = elementID

    @property
    def forms_PageElement45(self):
        return self.__forms_PageElement45

    @forms_PageElement45.setter
    def forms_PageElement45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_PageElement__forms_PageElement45", None)
        self.__forms_PageElement45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_AttributeValueCondition44"):
                opp_val = getattr(old_value, "forms_AttributeValueCondition44", None)
                if opp_val == self:
                    setattr(old_value, "forms_AttributeValueCondition44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_AttributeValueCondition44"):
                opp_val = getattr(value, "forms_AttributeValueCondition44", None)
                setattr(value, "forms_AttributeValueCondition44", self)

    @property
    def forms_PageElement(self):
        return self.__forms_PageElement

    @forms_PageElement.setter
    def forms_PageElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_PageElement__forms_PageElement", None)
        self.__forms_PageElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Page24"):
                opp_val = getattr(old_value, "forms_Page24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Page24"):
                opp_val = getattr(value, "forms_Page24", None)
                if opp_val is None:
                    setattr(value, "forms_Page24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def forms_PageElement48(self):
        return self.__forms_PageElement48

    @forms_PageElement48.setter
    def forms_PageElement48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_PageElement__forms_PageElement48", None)
        self.__forms_PageElement48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_AttributeValueCondition47"):
                opp_val = getattr(old_value, "forms_AttributeValueCondition47", None)
                if opp_val == self:
                    setattr(old_value, "forms_AttributeValueCondition47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_AttributeValueCondition47"):
                opp_val = getattr(value, "forms_AttributeValueCondition47", None)
                setattr(value, "forms_AttributeValueCondition47", self)

class forms_Page:

    def __init__(self, title: str, forms_Page: "forms_Form" = None, forms_Page24: set["forms_PageElement"] = None, forms_Page42: "forms_AttributeValueCondition" = None):
        self.title = title
        self.forms_Page = forms_Page
        self.forms_Page24 = forms_Page24 if forms_Page24 is not None else set()
        self.forms_Page42 = forms_Page42
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def forms_Page24(self):
        return self.__forms_Page24

    @forms_Page24.setter
    def forms_Page24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Page__forms_Page24", None)
        self.__forms_Page24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "forms_PageElement"):
                    opp_val = getattr(item, "forms_PageElement", None)
                    
                    if opp_val == self:
                        setattr(item, "forms_PageElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "forms_PageElement"):
                    opp_val = getattr(item, "forms_PageElement", None)
                    
                    setattr(item, "forms_PageElement", self)
                    

    @property
    def forms_Page42(self):
        return self.__forms_Page42

    @forms_Page42.setter
    def forms_Page42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Page__forms_Page42", None)
        self.__forms_Page42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_AttributeValueCondition41"):
                opp_val = getattr(old_value, "forms_AttributeValueCondition41", None)
                if opp_val == self:
                    setattr(old_value, "forms_AttributeValueCondition41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_AttributeValueCondition41"):
                opp_val = getattr(value, "forms_AttributeValueCondition41", None)
                setattr(value, "forms_AttributeValueCondition41", self)

    @property
    def forms_Page(self):
        return self.__forms_Page

    @forms_Page.setter
    def forms_Page(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Page__forms_Page", None)
        self.__forms_Page = value
        
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

    def __init__(self, title: str, description: str, isWelcomeForm: bool, name: str, forms_Form28: "forms_RelationshipPageElement" = None, forms_Form: set["forms_Page"] = None, forms_Form21: "forms_Entity" = None, forms_Form50: "forms_EMFL_FormModel" = None):
        self.title = title
        self.description = description
        self.isWelcomeForm = isWelcomeForm
        self.name = name
        self.forms_Form28 = forms_Form28
        self.forms_Form = forms_Form if forms_Form is not None else set()
        self.forms_Form21 = forms_Form21
        self.forms_Form50 = forms_Form50
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isWelcomeForm(self) -> bool:
        return self.__isWelcomeForm

    @isWelcomeForm.setter
    def isWelcomeForm(self, isWelcomeForm: bool):
        self.__isWelcomeForm = isWelcomeForm

    @property
    def forms_Form21(self):
        return self.__forms_Form21

    @forms_Form21.setter
    def forms_Form21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Form__forms_Form21", None)
        self.__forms_Form21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Entity22"):
                opp_val = getattr(old_value, "forms_Entity22", None)
                if opp_val == self:
                    setattr(old_value, "forms_Entity22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Entity22"):
                opp_val = getattr(value, "forms_Entity22", None)
                setattr(value, "forms_Entity22", self)

    @property
    def forms_Form28(self):
        return self.__forms_Form28

    @forms_Form28.setter
    def forms_Form28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Form__forms_Form28", None)
        self.__forms_Form28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_RelationshipPageElement"):
                opp_val = getattr(old_value, "forms_RelationshipPageElement", None)
                if opp_val == self:
                    setattr(old_value, "forms_RelationshipPageElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_RelationshipPageElement"):
                opp_val = getattr(value, "forms_RelationshipPageElement", None)
                setattr(value, "forms_RelationshipPageElement", self)

    @property
    def forms_Form50(self):
        return self.__forms_Form50

    @forms_Form50.setter
    def forms_Form50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Form__forms_Form50", None)
        self.__forms_Form50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_EMFL_FormModel"):
                opp_val = getattr(old_value, "forms_EMFL_FormModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_EMFL_FormModel"):
                opp_val = getattr(value, "forms_EMFL_FormModel", None)
                if opp_val is None:
                    setattr(value, "forms_EMFL_FormModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
                if hasattr(item, "forms_Page"):
                    opp_val = getattr(item, "forms_Page", None)
                    
                    if opp_val == self:
                        setattr(item, "forms_Page", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "forms_Page"):
                    opp_val = getattr(item, "forms_Page", None)
                    
                    setattr(item, "forms_Page", self)
                    

class AttributePageElement:

    pass
class forms_SelectionField(AttributePageElement):

    pass
class forms_DateSelectionField(AttributePageElement):

    pass
class forms_TimeSelectionField(AttributePageElement):

    pass
class forms_TextField(AttributePageElement):

    def __init__(self, format: str):
        self.format = format
        
    @property
    def format(self) -> str:
        return self.__format

    @format.setter
    def format(self, format: str):
        self.__format = format

class forms_TextArea(AttributePageElement):

    pass
class forms_RelationshipPageElement(PageElement):

    pass
class forms_Literal:

    def __init__(self, name: str, Value: str, forms_Literal: "forms_Enumeration" = None):
        self.name = name
        self.Value = Value
        self.forms_Literal = forms_Literal
        
    @property
    def Value(self) -> str:
        return self.__Value

    @Value.setter
    def Value(self, Value: str):
        self.__Value = Value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def forms_Literal(self):
        return self.__forms_Literal

    @forms_Literal.setter
    def forms_Literal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Literal__forms_Literal", None)
        self.__forms_Literal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Enumeration12"):
                opp_val = getattr(old_value, "forms_Enumeration12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Enumeration12"):
                opp_val = getattr(value, "forms_Enumeration12", None)
                if opp_val is None:
                    setattr(value, "forms_Enumeration12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class forms_Enumeration:

    def __init__(self, name: str, forms_Enumeration: "forms_Attribute" = None, forms_Enumeration12: set["forms_Literal"] = None, forms_Enumeration60: "forms_EMFL_EntityModel" = None):
        self.name = name
        self.forms_Enumeration = forms_Enumeration
        self.forms_Enumeration12 = forms_Enumeration12 if forms_Enumeration12 is not None else set()
        self.forms_Enumeration60 = forms_Enumeration60
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def forms_Enumeration12(self):
        return self.__forms_Enumeration12

    @forms_Enumeration12.setter
    def forms_Enumeration12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Enumeration__forms_Enumeration12", None)
        self.__forms_Enumeration12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "forms_Literal"):
                    opp_val = getattr(item, "forms_Literal", None)
                    
                    if opp_val == self:
                        setattr(item, "forms_Literal", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "forms_Literal"):
                    opp_val = getattr(item, "forms_Literal", None)
                    
                    setattr(item, "forms_Literal", self)
                    

    @property
    def forms_Enumeration(self):
        return self.__forms_Enumeration

    @forms_Enumeration.setter
    def forms_Enumeration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Enumeration__forms_Enumeration", None)
        self.__forms_Enumeration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Attribute10"):
                opp_val = getattr(old_value, "forms_Attribute10", None)
                if opp_val == self:
                    setattr(old_value, "forms_Attribute10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Attribute10"):
                opp_val = getattr(value, "forms_Attribute10", None)
                setattr(value, "forms_Attribute10", self)

    @property
    def forms_Enumeration60(self):
        return self.__forms_Enumeration60

    @forms_Enumeration60.setter
    def forms_Enumeration60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Enumeration__forms_Enumeration60", None)
        self.__forms_Enumeration60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_EMFL_EntityModel59"):
                opp_val = getattr(old_value, "forms_EMFL_EntityModel59", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_EMFL_EntityModel59"):
                opp_val = getattr(value, "forms_EMFL_EntityModel59", None)
                if opp_val is None:
                    setattr(value, "forms_EMFL_EntityModel59", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class forms_Entity:

    def __init__(self, name: str, forms_Entity: set["forms_Attribute"] = None, forms_Entity2: "forms_Attribute" = None, forms_Entity15: "forms_Relationship" = None, forms_Entity5: set["forms_Relationship"] = None, forms_Entity8: "forms_Entity" = None, forms_Entity6: "forms_Entity" = None, forms_Entity22: "forms_Form" = None, forms_Entity55: "forms_EMFL_FormModel" = None, forms_Entity57: "forms_EMFL_EntityModel" = None):
        self.name = name
        self.forms_Entity = forms_Entity if forms_Entity is not None else set()
        self.forms_Entity2 = forms_Entity2
        self.forms_Entity15 = forms_Entity15
        self.forms_Entity5 = forms_Entity5 if forms_Entity5 is not None else set()
        self.forms_Entity8 = forms_Entity8
        self.forms_Entity6 = forms_Entity6
        self.forms_Entity22 = forms_Entity22
        self.forms_Entity55 = forms_Entity55
        self.forms_Entity57 = forms_Entity57
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def forms_Entity8(self):
        return self.__forms_Entity8

    @forms_Entity8.setter
    def forms_Entity8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Entity__forms_Entity8", None)
        self.__forms_Entity8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Entity6"):
                opp_val = getattr(old_value, "forms_Entity6", None)
                if opp_val == self:
                    setattr(old_value, "forms_Entity6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Entity6"):
                opp_val = getattr(value, "forms_Entity6", None)
                setattr(value, "forms_Entity6", self)

    @property
    def forms_Entity22(self):
        return self.__forms_Entity22

    @forms_Entity22.setter
    def forms_Entity22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Entity__forms_Entity22", None)
        self.__forms_Entity22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Form21"):
                opp_val = getattr(old_value, "forms_Form21", None)
                if opp_val == self:
                    setattr(old_value, "forms_Form21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Form21"):
                opp_val = getattr(value, "forms_Form21", None)
                setattr(value, "forms_Form21", self)

    @property
    def forms_Entity57(self):
        return self.__forms_Entity57

    @forms_Entity57.setter
    def forms_Entity57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Entity__forms_Entity57", None)
        self.__forms_Entity57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_EMFL_EntityModel"):
                opp_val = getattr(old_value, "forms_EMFL_EntityModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_EMFL_EntityModel"):
                opp_val = getattr(value, "forms_EMFL_EntityModel", None)
                if opp_val is None:
                    setattr(value, "forms_EMFL_EntityModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def forms_Entity2(self):
        return self.__forms_Entity2

    @forms_Entity2.setter
    def forms_Entity2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Entity__forms_Entity2", None)
        self.__forms_Entity2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Attribute3"):
                opp_val = getattr(old_value, "forms_Attribute3", None)
                if opp_val == self:
                    setattr(old_value, "forms_Attribute3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Attribute3"):
                opp_val = getattr(value, "forms_Attribute3", None)
                setattr(value, "forms_Attribute3", self)

    @property
    def forms_Entity6(self):
        return self.__forms_Entity6

    @forms_Entity6.setter
    def forms_Entity6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Entity__forms_Entity6", None)
        self.__forms_Entity6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Entity8"):
                opp_val = getattr(old_value, "forms_Entity8", None)
                if opp_val == self:
                    setattr(old_value, "forms_Entity8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Entity8"):
                opp_val = getattr(value, "forms_Entity8", None)
                setattr(value, "forms_Entity8", self)

    @property
    def forms_Entity5(self):
        return self.__forms_Entity5

    @forms_Entity5.setter
    def forms_Entity5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Entity__forms_Entity5", None)
        self.__forms_Entity5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "forms_Relationship"):
                    opp_val = getattr(item, "forms_Relationship", None)
                    
                    if opp_val == self:
                        setattr(item, "forms_Relationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "forms_Relationship"):
                    opp_val = getattr(item, "forms_Relationship", None)
                    
                    setattr(item, "forms_Relationship", self)
                    

    @property
    def forms_Entity15(self):
        return self.__forms_Entity15

    @forms_Entity15.setter
    def forms_Entity15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Entity__forms_Entity15", None)
        self.__forms_Entity15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Relationship14"):
                opp_val = getattr(old_value, "forms_Relationship14", None)
                if opp_val == self:
                    setattr(old_value, "forms_Relationship14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Relationship14"):
                opp_val = getattr(value, "forms_Relationship14", None)
                setattr(value, "forms_Relationship14", self)

    @property
    def forms_Entity(self):
        return self.__forms_Entity

    @forms_Entity.setter
    def forms_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Entity__forms_Entity", None)
        self.__forms_Entity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "forms_Attribute"):
                    opp_val = getattr(item, "forms_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "forms_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "forms_Attribute"):
                    opp_val = getattr(item, "forms_Attribute", None)
                    
                    setattr(item, "forms_Attribute", self)
                    

    @property
    def forms_Entity55(self):
        return self.__forms_Entity55

    @forms_Entity55.setter
    def forms_Entity55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Entity__forms_Entity55", None)
        self.__forms_Entity55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_EMFL_FormModel54"):
                opp_val = getattr(old_value, "forms_EMFL_FormModel54", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_EMFL_FormModel54"):
                opp_val = getattr(value, "forms_EMFL_FormModel54", None)
                if opp_val is None:
                    setattr(value, "forms_EMFL_FormModel54", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class forms_Relationship:

    def __init__(self, name: str, lowerBound: int, upperBound: int, forms_Relationship: "forms_Entity" = None, forms_Relationship14: "forms_Entity" = None, forms_Relationship18: "forms_Relationship" = None, forms_Relationship16: "forms_Relationship" = None, forms_Relationship31: "forms_RelationshipPageElement" = None):
        self.name = name
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.forms_Relationship = forms_Relationship
        self.forms_Relationship14 = forms_Relationship14
        self.forms_Relationship18 = forms_Relationship18
        self.forms_Relationship16 = forms_Relationship16
        self.forms_Relationship31 = forms_Relationship31
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def lowerBound(self) -> int:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: int):
        self.__lowerBound = lowerBound

    @property
    def upperBound(self) -> int:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: int):
        self.__upperBound = upperBound

    @property
    def forms_Relationship31(self):
        return self.__forms_Relationship31

    @forms_Relationship31.setter
    def forms_Relationship31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Relationship__forms_Relationship31", None)
        self.__forms_Relationship31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_RelationshipPageElement30"):
                opp_val = getattr(old_value, "forms_RelationshipPageElement30", None)
                if opp_val == self:
                    setattr(old_value, "forms_RelationshipPageElement30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_RelationshipPageElement30"):
                opp_val = getattr(value, "forms_RelationshipPageElement30", None)
                setattr(value, "forms_RelationshipPageElement30", self)

    @property
    def forms_Relationship18(self):
        return self.__forms_Relationship18

    @forms_Relationship18.setter
    def forms_Relationship18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Relationship__forms_Relationship18", None)
        self.__forms_Relationship18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Relationship16"):
                opp_val = getattr(old_value, "forms_Relationship16", None)
                if opp_val == self:
                    setattr(old_value, "forms_Relationship16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Relationship16"):
                opp_val = getattr(value, "forms_Relationship16", None)
                setattr(value, "forms_Relationship16", self)

    @property
    def forms_Relationship14(self):
        return self.__forms_Relationship14

    @forms_Relationship14.setter
    def forms_Relationship14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Relationship__forms_Relationship14", None)
        self.__forms_Relationship14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Entity15"):
                opp_val = getattr(old_value, "forms_Entity15", None)
                if opp_val == self:
                    setattr(old_value, "forms_Entity15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Entity15"):
                opp_val = getattr(value, "forms_Entity15", None)
                setattr(value, "forms_Entity15", self)

    @property
    def forms_Relationship(self):
        return self.__forms_Relationship

    @forms_Relationship.setter
    def forms_Relationship(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Relationship__forms_Relationship", None)
        self.__forms_Relationship = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Entity5"):
                opp_val = getattr(old_value, "forms_Entity5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Entity5"):
                opp_val = getattr(value, "forms_Entity5", None)
                if opp_val is None:
                    setattr(value, "forms_Entity5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def forms_Relationship16(self):
        return self.__forms_Relationship16

    @forms_Relationship16.setter
    def forms_Relationship16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Relationship__forms_Relationship16", None)
        self.__forms_Relationship16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Relationship18"):
                opp_val = getattr(old_value, "forms_Relationship18", None)
                if opp_val == self:
                    setattr(old_value, "forms_Relationship18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Relationship18"):
                opp_val = getattr(value, "forms_Relationship18", None)
                setattr(value, "forms_Relationship18", self)

class forms_Attribute:

    def __init__(self, name: str, mandatory: bool, type: str, forms_Attribute: "forms_Entity" = None, forms_Attribute3: "forms_Entity" = None, forms_Attribute10: "forms_Enumeration" = None, forms_Attribute26: "forms_AttributePageElement" = None, forms_Attribute35: "forms_Column" = None):
        self.name = name
        self.mandatory = mandatory
        self.type = type
        self.forms_Attribute = forms_Attribute
        self.forms_Attribute3 = forms_Attribute3
        self.forms_Attribute10 = forms_Attribute10
        self.forms_Attribute26 = forms_Attribute26
        self.forms_Attribute35 = forms_Attribute35
        
    @property
    def mandatory(self) -> bool:
        return self.__mandatory

    @mandatory.setter
    def mandatory(self, mandatory: bool):
        self.__mandatory = mandatory

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def forms_Attribute(self):
        return self.__forms_Attribute

    @forms_Attribute.setter
    def forms_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Attribute__forms_Attribute", None)
        self.__forms_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Entity"):
                opp_val = getattr(old_value, "forms_Entity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Entity"):
                opp_val = getattr(value, "forms_Entity", None)
                if opp_val is None:
                    setattr(value, "forms_Entity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def forms_Attribute3(self):
        return self.__forms_Attribute3

    @forms_Attribute3.setter
    def forms_Attribute3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Attribute__forms_Attribute3", None)
        self.__forms_Attribute3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Entity2"):
                opp_val = getattr(old_value, "forms_Entity2", None)
                if opp_val == self:
                    setattr(old_value, "forms_Entity2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Entity2"):
                opp_val = getattr(value, "forms_Entity2", None)
                setattr(value, "forms_Entity2", self)

    @property
    def forms_Attribute10(self):
        return self.__forms_Attribute10

    @forms_Attribute10.setter
    def forms_Attribute10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Attribute__forms_Attribute10", None)
        self.__forms_Attribute10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Enumeration"):
                opp_val = getattr(old_value, "forms_Enumeration", None)
                if opp_val == self:
                    setattr(old_value, "forms_Enumeration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Enumeration"):
                opp_val = getattr(value, "forms_Enumeration", None)
                setattr(value, "forms_Enumeration", self)

    @property
    def forms_Attribute35(self):
        return self.__forms_Attribute35

    @forms_Attribute35.setter
    def forms_Attribute35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Attribute__forms_Attribute35", None)
        self.__forms_Attribute35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Column34"):
                opp_val = getattr(old_value, "forms_Column34", None)
                if opp_val == self:
                    setattr(old_value, "forms_Column34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Column34"):
                opp_val = getattr(value, "forms_Column34", None)
                setattr(value, "forms_Column34", self)

    @property
    def forms_Attribute26(self):
        return self.__forms_Attribute26

    @forms_Attribute26.setter
    def forms_Attribute26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Attribute__forms_Attribute26", None)
        self.__forms_Attribute26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_AttributePageElement"):
                opp_val = getattr(old_value, "forms_AttributePageElement", None)
                if opp_val == self:
                    setattr(old_value, "forms_AttributePageElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_AttributePageElement"):
                opp_val = getattr(value, "forms_AttributePageElement", None)
                setattr(value, "forms_AttributePageElement", self)
