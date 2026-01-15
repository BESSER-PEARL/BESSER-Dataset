from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class OperatorType(Enum):
    AND = "AND"
    OR = "OR"
class AttributeType(Enum):
    Boolean = "Boolean"
    None = "None"
    String = "String"
    Text = "Text"
    Integer = "Integer"
    Date = "Date"
    Time = "Time"
    Year = "Year"
    Email = "Email"
class ConditionType(Enum):
    Hide = "Hide"
    Show = "Show"
    Enable = "Enable"
    Disable = "Disable"


############################################
# Definition of Classes
############################################

class AttributePageElement:

    pass
class forms_TimeSelectionFields(AttributePageElement):

    pass
class forms_TextAreas(AttributePageElement):

    pass
class forms_SelectionFields(AttributePageElement):

    pass
class forms_DateSelectionFields(AttributePageElement):

    pass
class forms_TextFields(AttributePageElement):

    def __init__(self, format: str):
        self.format = format
        
    @property
    def format(self) -> str:
        return self.__format

    @format.setter
    def format(self, format: str):
        self.__format = format

class Condition:

    pass
class forms_CompositeCondition(Condition):

    def __init__(self, operatorType: str, forms_CompositeCondition: "forms_Condition" = None, forms_CompositeCondition54: "forms_Condition" = None):
        self.operatorType = operatorType
        self.forms_CompositeCondition = forms_CompositeCondition
        self.forms_CompositeCondition54 = forms_CompositeCondition54
        
    @property
    def operatorType(self) -> str:
        return self.__operatorType

    @operatorType.setter
    def operatorType(self, operatorType: str):
        self.__operatorType = operatorType

    @property
    def forms_CompositeCondition(self):
        return self.__forms_CompositeCondition

    @forms_CompositeCondition.setter
    def forms_CompositeCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_CompositeCondition__forms_CompositeCondition", None)
        self.__forms_CompositeCondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Condition52"):
                opp_val = getattr(old_value, "forms_Condition52", None)
                if opp_val == self:
                    setattr(old_value, "forms_Condition52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Condition52"):
                opp_val = getattr(value, "forms_Condition52", None)
                setattr(value, "forms_Condition52", self)

    @property
    def forms_CompositeCondition54(self):
        return self.__forms_CompositeCondition54

    @forms_CompositeCondition54.setter
    def forms_CompositeCondition54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_CompositeCondition__forms_CompositeCondition54", None)
        self.__forms_CompositeCondition54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Condition55"):
                opp_val = getattr(old_value, "forms_Condition55", None)
                if opp_val == self:
                    setattr(old_value, "forms_Condition55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Condition55"):
                opp_val = getattr(value, "forms_Condition55", None)
                setattr(value, "forms_Condition55", self)

class forms_AttributeValueCondition(Condition):

    def __init__(self, value: str, forms_AttributeValueCondition: "forms_AttributePageElement" = None):
        self.value = value
        self.forms_AttributeValueCondition = forms_AttributeValueCondition
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

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
            if hasattr(old_value, "forms_AttributePageElement50"):
                opp_val = getattr(old_value, "forms_AttributePageElement50", None)
                if opp_val == self:
                    setattr(old_value, "forms_AttributePageElement50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_AttributePageElement50"):
                opp_val = getattr(value, "forms_AttributePageElement50", None)
                setattr(value, "forms_AttributePageElement50", self)

class forms_Column:

    pass
class RelationshipPageElement:

    pass
class forms_TableRelationshipPageElement(RelationshipPageElement):

    pass
class forms_ListRelationshipPageElement(RelationshipPageElement):

    pass
class PageElement:

    pass
class forms_RelationshipPageElement(PageElement):

    pass
class forms_AttributePageElement(PageElement):

    def __init__(self, value: str, forms_AttributePageElement: "forms_Attribute" = None, forms_AttributePageElement50: "forms_AttributeValueCondition" = None):
        self.value = value
        self.forms_AttributePageElement = forms_AttributePageElement
        self.forms_AttributePageElement50 = forms_AttributePageElement50
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def forms_AttributePageElement(self):
        return self.__forms_AttributePageElement

    @forms_AttributePageElement.setter
    def forms_AttributePageElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_AttributePageElement__forms_AttributePageElement", None)
        self.__forms_AttributePageElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Attribute33"):
                opp_val = getattr(old_value, "forms_Attribute33", None)
                if opp_val == self:
                    setattr(old_value, "forms_Attribute33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Attribute33"):
                opp_val = getattr(value, "forms_Attribute33", None)
                setattr(value, "forms_Attribute33", self)

    @property
    def forms_AttributePageElement50(self):
        return self.__forms_AttributePageElement50

    @forms_AttributePageElement50.setter
    def forms_AttributePageElement50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_AttributePageElement__forms_AttributePageElement50", None)
        self.__forms_AttributePageElement50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_AttributeValueCondition"):
                opp_val = getattr(old_value, "forms_AttributeValueCondition", None)
                if opp_val == self:
                    setattr(old_value, "forms_AttributeValueCondition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_AttributeValueCondition"):
                opp_val = getattr(value, "forms_AttributeValueCondition", None)
                setattr(value, "forms_AttributeValueCondition", self)

class forms_PageElement(ABC):

    def __init__(self, label: str, elementID: str, forms_PageElement: "forms_Page" = None, forms_PageElement48: "forms_Condition" = None):
        self.label = label
        self.elementID = elementID
        self.forms_PageElement = forms_PageElement
        self.forms_PageElement48 = forms_PageElement48
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def elementID(self) -> str:
        return self.__elementID

    @elementID.setter
    def elementID(self, elementID: str):
        self.__elementID = elementID

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
            if hasattr(old_value, "forms_Page31"):
                opp_val = getattr(old_value, "forms_Page31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Page31"):
                opp_val = getattr(value, "forms_Page31", None)
                if opp_val is None:
                    setattr(value, "forms_Page31", set([self]))
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
            if hasattr(old_value, "forms_Condition47"):
                opp_val = getattr(old_value, "forms_Condition47", None)
                if opp_val == self:
                    setattr(old_value, "forms_Condition47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Condition47"):
                opp_val = getattr(value, "forms_Condition47", None)
                setattr(value, "forms_Condition47", self)

class forms_Page:

    def __init__(self, title: str, forms_Page: "forms_Form" = None, forms_Page31: set["forms_PageElement"] = None, forms_Page45: "forms_Condition" = None):
        self.title = title
        self.forms_Page = forms_Page
        self.forms_Page31 = forms_Page31 if forms_Page31 is not None else set()
        self.forms_Page45 = forms_Page45
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def forms_Page45(self):
        return self.__forms_Page45

    @forms_Page45.setter
    def forms_Page45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Page__forms_Page45", None)
        self.__forms_Page45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Condition44"):
                opp_val = getattr(old_value, "forms_Condition44", None)
                if opp_val == self:
                    setattr(old_value, "forms_Condition44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Condition44"):
                opp_val = getattr(value, "forms_Condition44", None)
                setattr(value, "forms_Condition44", self)

    @property
    def forms_Page31(self):
        return self.__forms_Page31

    @forms_Page31.setter
    def forms_Page31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Page__forms_Page31", None)
        self.__forms_Page31 = value if value is not None else set()
        
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
    def forms_Page(self):
        return self.__forms_Page

    @forms_Page.setter
    def forms_Page(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Page__forms_Page", None)
        self.__forms_Page = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Form29"):
                opp_val = getattr(old_value, "forms_Form29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Form29"):
                opp_val = getattr(value, "forms_Form29", None)
                if opp_val is None:
                    setattr(value, "forms_Form29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class forms_Literal:

    def __init__(self, name: str, value: str, forms_Literal: "forms_Enumeration" = None):
        self.name = name
        self.value = value
        self.forms_Literal = forms_Literal
        
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
            if hasattr(old_value, "forms_Enumeration18"):
                opp_val = getattr(old_value, "forms_Enumeration18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Enumeration18"):
                opp_val = getattr(value, "forms_Enumeration18", None)
                if opp_val is None:
                    setattr(value, "forms_Enumeration18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class forms_Attribute:

    def __init__(self, name: str, mandatory: bool, type: str, isId: str, forms_Attribute: "forms_Entity" = None, forms_Attribute7: "forms_Enumeration" = None, forms_Attribute33: "forms_AttributePageElement" = None, forms_Attribute42: "forms_Column" = None):
        self.name = name
        self.mandatory = mandatory
        self.type = type
        self.isId = isId
        self.forms_Attribute = forms_Attribute
        self.forms_Attribute7 = forms_Attribute7
        self.forms_Attribute33 = forms_Attribute33
        self.forms_Attribute42 = forms_Attribute42
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isId(self) -> str:
        return self.__isId

    @isId.setter
    def isId(self, isId: str):
        self.__isId = isId

    @property
    def mandatory(self) -> bool:
        return self.__mandatory

    @mandatory.setter
    def mandatory(self, mandatory: bool):
        self.__mandatory = mandatory

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def forms_Attribute7(self):
        return self.__forms_Attribute7

    @forms_Attribute7.setter
    def forms_Attribute7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Attribute__forms_Attribute7", None)
        self.__forms_Attribute7 = value
        
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
    def forms_Attribute33(self):
        return self.__forms_Attribute33

    @forms_Attribute33.setter
    def forms_Attribute33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Attribute__forms_Attribute33", None)
        self.__forms_Attribute33 = value
        
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
    def forms_Attribute42(self):
        return self.__forms_Attribute42

    @forms_Attribute42.setter
    def forms_Attribute42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Attribute__forms_Attribute42", None)
        self.__forms_Attribute42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Column41"):
                opp_val = getattr(old_value, "forms_Column41", None)
                if opp_val == self:
                    setattr(old_value, "forms_Column41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Column41"):
                opp_val = getattr(value, "forms_Column41", None)
                setattr(value, "forms_Column41", self)

class forms_Condition(ABC):

    def __init__(self, conditionID: str, type: str, forms_Condition: "forms_Model" = None, forms_Condition44: "forms_Page" = None, forms_Condition47: "forms_PageElement" = None, forms_Condition52: "forms_CompositeCondition" = None, forms_Condition55: "forms_CompositeCondition" = None):
        self.conditionID = conditionID
        self.type = type
        self.forms_Condition = forms_Condition
        self.forms_Condition44 = forms_Condition44
        self.forms_Condition47 = forms_Condition47
        self.forms_Condition52 = forms_Condition52
        self.forms_Condition55 = forms_Condition55
        
    @property
    def conditionID(self) -> str:
        return self.__conditionID

    @conditionID.setter
    def conditionID(self, conditionID: str):
        self.__conditionID = conditionID

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def forms_Condition44(self):
        return self.__forms_Condition44

    @forms_Condition44.setter
    def forms_Condition44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Condition__forms_Condition44", None)
        self.__forms_Condition44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Page45"):
                opp_val = getattr(old_value, "forms_Page45", None)
                if opp_val == self:
                    setattr(old_value, "forms_Page45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Page45"):
                opp_val = getattr(value, "forms_Page45", None)
                setattr(value, "forms_Page45", self)

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
            if hasattr(old_value, "forms_Model16"):
                opp_val = getattr(old_value, "forms_Model16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Model16"):
                opp_val = getattr(value, "forms_Model16", None)
                if opp_val is None:
                    setattr(value, "forms_Model16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def forms_Condition55(self):
        return self.__forms_Condition55

    @forms_Condition55.setter
    def forms_Condition55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Condition__forms_Condition55", None)
        self.__forms_Condition55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_CompositeCondition54"):
                opp_val = getattr(old_value, "forms_CompositeCondition54", None)
                if opp_val == self:
                    setattr(old_value, "forms_CompositeCondition54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_CompositeCondition54"):
                opp_val = getattr(value, "forms_CompositeCondition54", None)
                setattr(value, "forms_CompositeCondition54", self)

    @property
    def forms_Condition47(self):
        return self.__forms_Condition47

    @forms_Condition47.setter
    def forms_Condition47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Condition__forms_Condition47", None)
        self.__forms_Condition47 = value
        
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

    @property
    def forms_Condition52(self):
        return self.__forms_Condition52

    @forms_Condition52.setter
    def forms_Condition52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Condition__forms_Condition52", None)
        self.__forms_Condition52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_CompositeCondition"):
                opp_val = getattr(old_value, "forms_CompositeCondition", None)
                if opp_val == self:
                    setattr(old_value, "forms_CompositeCondition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_CompositeCondition"):
                opp_val = getattr(value, "forms_CompositeCondition", None)
                setattr(value, "forms_CompositeCondition", self)

class forms_Form:

    def __init__(self, isWelcomeForm: str, name: str, title: str, description: str, forms_Form: "forms_Model" = None, forms_Form29: set["forms_Page"] = None, forms_Form35: "forms_RelationshipPageElement" = None, forms_Form26: "forms_Entity" = None):
        self.isWelcomeForm = isWelcomeForm
        self.name = name
        self.title = title
        self.description = description
        self.forms_Form = forms_Form
        self.forms_Form29 = forms_Form29 if forms_Form29 is not None else set()
        self.forms_Form35 = forms_Form35
        self.forms_Form26 = forms_Form26
        
    @property
    def isWelcomeForm(self) -> str:
        return self.__isWelcomeForm

    @isWelcomeForm.setter
    def isWelcomeForm(self, isWelcomeForm: str):
        self.__isWelcomeForm = isWelcomeForm

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

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
    def forms_Form26(self):
        return self.__forms_Form26

    @forms_Form26.setter
    def forms_Form26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Form__forms_Form26", None)
        self.__forms_Form26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Entity27"):
                opp_val = getattr(old_value, "forms_Entity27", None)
                if opp_val == self:
                    setattr(old_value, "forms_Entity27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Entity27"):
                opp_val = getattr(value, "forms_Entity27", None)
                setattr(value, "forms_Entity27", self)

    @property
    def forms_Form29(self):
        return self.__forms_Form29

    @forms_Form29.setter
    def forms_Form29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Form__forms_Form29", None)
        self.__forms_Form29 = value if value is not None else set()
        
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
                    

    @property
    def forms_Form35(self):
        return self.__forms_Form35

    @forms_Form35.setter
    def forms_Form35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Form__forms_Form35", None)
        self.__forms_Form35 = value
        
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
    def forms_Form(self):
        return self.__forms_Form

    @forms_Form.setter
    def forms_Form(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Form__forms_Form", None)
        self.__forms_Form = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Model11"):
                opp_val = getattr(old_value, "forms_Model11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Model11"):
                opp_val = getattr(value, "forms_Model11", None)
                if opp_val is None:
                    setattr(value, "forms_Model11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class forms_Model:

    pass
class forms_Enumeration:

    def __init__(self, name: str, forms_Enumeration: "forms_Attribute" = None, forms_Enumeration14: "forms_Model" = None, forms_Enumeration18: set["forms_Literal"] = None):
        self.name = name
        self.forms_Enumeration = forms_Enumeration
        self.forms_Enumeration14 = forms_Enumeration14
        self.forms_Enumeration18 = forms_Enumeration18 if forms_Enumeration18 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "forms_Attribute7"):
                opp_val = getattr(old_value, "forms_Attribute7", None)
                if opp_val == self:
                    setattr(old_value, "forms_Attribute7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Attribute7"):
                opp_val = getattr(value, "forms_Attribute7", None)
                setattr(value, "forms_Attribute7", self)

    @property
    def forms_Enumeration18(self):
        return self.__forms_Enumeration18

    @forms_Enumeration18.setter
    def forms_Enumeration18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Enumeration__forms_Enumeration18", None)
        self.__forms_Enumeration18 = value if value is not None else set()
        
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
    def forms_Enumeration14(self):
        return self.__forms_Enumeration14

    @forms_Enumeration14.setter
    def forms_Enumeration14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Enumeration__forms_Enumeration14", None)
        self.__forms_Enumeration14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Model13"):
                opp_val = getattr(old_value, "forms_Model13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Model13"):
                opp_val = getattr(value, "forms_Model13", None)
                if opp_val is None:
                    setattr(value, "forms_Model13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class forms_Relationship:

    def __init__(self, name: str, lowerBound: str, upperBound: str, forms_Relationship: "forms_Entity" = None, forms_Relationship20: "forms_Entity" = None, forms_Relationship24: "forms_Relationship" = None, forms_Relationship22: "forms_Relationship" = None, forms_Relationship38: "forms_RelationshipPageElement" = None):
        self.name = name
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.forms_Relationship = forms_Relationship
        self.forms_Relationship20 = forms_Relationship20
        self.forms_Relationship24 = forms_Relationship24
        self.forms_Relationship22 = forms_Relationship22
        self.forms_Relationship38 = forms_Relationship38
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def lowerBound(self) -> str:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: str):
        self.__lowerBound = lowerBound

    @property
    def upperBound(self) -> str:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: str):
        self.__upperBound = upperBound

    @property
    def forms_Relationship22(self):
        return self.__forms_Relationship22

    @forms_Relationship22.setter
    def forms_Relationship22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Relationship__forms_Relationship22", None)
        self.__forms_Relationship22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Relationship24"):
                opp_val = getattr(old_value, "forms_Relationship24", None)
                if opp_val == self:
                    setattr(old_value, "forms_Relationship24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Relationship24"):
                opp_val = getattr(value, "forms_Relationship24", None)
                setattr(value, "forms_Relationship24", self)

    @property
    def forms_Relationship20(self):
        return self.__forms_Relationship20

    @forms_Relationship20.setter
    def forms_Relationship20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Relationship__forms_Relationship20", None)
        self.__forms_Relationship20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Entity21"):
                opp_val = getattr(old_value, "forms_Entity21", None)
                if opp_val == self:
                    setattr(old_value, "forms_Entity21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Entity21"):
                opp_val = getattr(value, "forms_Entity21", None)
                setattr(value, "forms_Entity21", self)

    @property
    def forms_Relationship38(self):
        return self.__forms_Relationship38

    @forms_Relationship38.setter
    def forms_Relationship38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Relationship__forms_Relationship38", None)
        self.__forms_Relationship38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_RelationshipPageElement37"):
                opp_val = getattr(old_value, "forms_RelationshipPageElement37", None)
                if opp_val == self:
                    setattr(old_value, "forms_RelationshipPageElement37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_RelationshipPageElement37"):
                opp_val = getattr(value, "forms_RelationshipPageElement37", None)
                setattr(value, "forms_RelationshipPageElement37", self)

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
            if hasattr(old_value, "forms_Entity2"):
                opp_val = getattr(old_value, "forms_Entity2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Entity2"):
                opp_val = getattr(value, "forms_Entity2", None)
                if opp_val is None:
                    setattr(value, "forms_Entity2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def forms_Relationship24(self):
        return self.__forms_Relationship24

    @forms_Relationship24.setter
    def forms_Relationship24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Relationship__forms_Relationship24", None)
        self.__forms_Relationship24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Relationship22"):
                opp_val = getattr(old_value, "forms_Relationship22", None)
                if opp_val == self:
                    setattr(old_value, "forms_Relationship22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Relationship22"):
                opp_val = getattr(value, "forms_Relationship22", None)
                setattr(value, "forms_Relationship22", self)

class forms_Entity:

    def __init__(self, name: str, forms_Entity: set["forms_Attribute"] = None, forms_Entity2: set["forms_Relationship"] = None, forms_Entity5: "forms_Entity" = None, forms_Entity3: "forms_Entity" = None, forms_Entity9: "forms_Model" = None, forms_Entity21: "forms_Relationship" = None, forms_Entity27: "forms_Form" = None):
        self.name = name
        self.forms_Entity = forms_Entity if forms_Entity is not None else set()
        self.forms_Entity2 = forms_Entity2 if forms_Entity2 is not None else set()
        self.forms_Entity5 = forms_Entity5
        self.forms_Entity3 = forms_Entity3
        self.forms_Entity9 = forms_Entity9
        self.forms_Entity21 = forms_Entity21
        self.forms_Entity27 = forms_Entity27
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def forms_Entity21(self):
        return self.__forms_Entity21

    @forms_Entity21.setter
    def forms_Entity21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Entity__forms_Entity21", None)
        self.__forms_Entity21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Relationship20"):
                opp_val = getattr(old_value, "forms_Relationship20", None)
                if opp_val == self:
                    setattr(old_value, "forms_Relationship20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Relationship20"):
                opp_val = getattr(value, "forms_Relationship20", None)
                setattr(value, "forms_Relationship20", self)

    @property
    def forms_Entity2(self):
        return self.__forms_Entity2

    @forms_Entity2.setter
    def forms_Entity2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Entity__forms_Entity2", None)
        self.__forms_Entity2 = value if value is not None else set()
        
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
    def forms_Entity3(self):
        return self.__forms_Entity3

    @forms_Entity3.setter
    def forms_Entity3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Entity__forms_Entity3", None)
        self.__forms_Entity3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Entity5"):
                opp_val = getattr(old_value, "forms_Entity5", None)
                if opp_val == self:
                    setattr(old_value, "forms_Entity5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Entity5"):
                opp_val = getattr(value, "forms_Entity5", None)
                setattr(value, "forms_Entity5", self)

    @property
    def forms_Entity27(self):
        return self.__forms_Entity27

    @forms_Entity27.setter
    def forms_Entity27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Entity__forms_Entity27", None)
        self.__forms_Entity27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Form26"):
                opp_val = getattr(old_value, "forms_Form26", None)
                if opp_val == self:
                    setattr(old_value, "forms_Form26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Form26"):
                opp_val = getattr(value, "forms_Form26", None)
                setattr(value, "forms_Form26", self)

    @property
    def forms_Entity5(self):
        return self.__forms_Entity5

    @forms_Entity5.setter
    def forms_Entity5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Entity__forms_Entity5", None)
        self.__forms_Entity5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Entity3"):
                opp_val = getattr(old_value, "forms_Entity3", None)
                if opp_val == self:
                    setattr(old_value, "forms_Entity3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Entity3"):
                opp_val = getattr(value, "forms_Entity3", None)
                setattr(value, "forms_Entity3", self)

    @property
    def forms_Entity9(self):
        return self.__forms_Entity9

    @forms_Entity9.setter
    def forms_Entity9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Entity__forms_Entity9", None)
        self.__forms_Entity9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Model"):
                opp_val = getattr(old_value, "forms_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Model"):
                opp_val = getattr(value, "forms_Model", None)
                if opp_val is None:
                    setattr(value, "forms_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
