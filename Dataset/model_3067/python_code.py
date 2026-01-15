from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ConditionType(Enum):
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
    Year = "Year"
    Email = "Email"
    Boolean = "Boolean"
    None = "None"
class BooleanOperators(Enum):
    AND = "AND"
    OR = "OR"


############################################
# Definition of Classes
############################################

class forms_entityModeling_Condition(ABC):

    def __init__(self, type: str, conditionID: str):
        self.type = type
        self.conditionID = conditionID
        
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

class forms_entityModeling_Column:

    pass
class Column:

    pass
class RelationshipPageElement:

    pass
class forms_entityModeling_Table(RelationshipPageElement):

    pass
class forms_entityModeling_List(RelationshipPageElement):

    pass
class AttributePageElement:

    pass
class forms_entityModeling_SelectionField(AttributePageElement):

    pass
class forms_entityModeling_DateSelectionField(AttributePageElement):

    pass
class forms_entityModeling_Textarea(AttributePageElement):

    pass
class forms_entityModeling_TimeSelectionField(AttributePageElement):

    pass
class forms_entityModeling_Textfield(AttributePageElement):

    def __init__(self, allowedValueFormat: str):
        self.allowedValueFormat = allowedValueFormat
        
    @property
    def allowedValueFormat(self) -> str:
        return self.__allowedValueFormat

    @allowedValueFormat.setter
    def allowedValueFormat(self, allowedValueFormat: str):
        self.__allowedValueFormat = allowedValueFormat

class forms_entityModeling_PageElement(ABC):

    def __init__(self, label: str, elementID: str, forms_entityModeling_PageElement: "Condition" = None):
        self.label = label
        self.elementID = elementID
        self.forms_entityModeling_PageElement = forms_entityModeling_PageElement
        
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
    def forms_entityModeling_PageElement(self):
        return self.__forms_entityModeling_PageElement

    @forms_entityModeling_PageElement.setter
    def forms_entityModeling_PageElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_entityModeling_PageElement__forms_entityModeling_PageElement", None)
        self.__forms_entityModeling_PageElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Condition33"):
                opp_val = getattr(old_value, "Condition33", None)
                if opp_val == self:
                    setattr(old_value, "Condition33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Condition33"):
                opp_val = getattr(value, "Condition33", None)
                setattr(value, "Condition33", self)

class forms_entityModeling_Form:

    def __init__(self, name: str, title: str, description: str, forms_entityModeling_Form: "Entity" = None, forms_entityModeling_Form28: set["Page"] = None):
        self.name = name
        self.title = title
        self.description = description
        self.forms_entityModeling_Form = forms_entityModeling_Form
        self.forms_entityModeling_Form28 = forms_entityModeling_Form28 if forms_entityModeling_Form28 is not None else set()
        
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
    def forms_entityModeling_Form28(self):
        return self.__forms_entityModeling_Form28

    @forms_entityModeling_Form28.setter
    def forms_entityModeling_Form28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_entityModeling_Form__forms_entityModeling_Form28", None)
        self.__forms_entityModeling_Form28 = value if value is not None else set()
        
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
                    

    @property
    def forms_entityModeling_Form(self):
        return self.__forms_entityModeling_Form

    @forms_entityModeling_Form.setter
    def forms_entityModeling_Form(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_entityModeling_Form__forms_entityModeling_Form", None)
        self.__forms_entityModeling_Form = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Entity26"):
                opp_val = getattr(old_value, "Entity26", None)
                if opp_val == self:
                    setattr(old_value, "Entity26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Entity26"):
                opp_val = getattr(value, "Entity26", None)
                setattr(value, "Entity26", self)

class Condition:

    pass
class forms_entityModeling_AttributeValueCondition(Condition):

    pass
class forms_entityModeling_CompositeCondition(Condition):

    def __init__(self, booleanOperator: str, forms_entityModeling_CompositeCondition: set["Condition"] = None, Condition33: "forms_entityModeling_PageElement", Condition: "forms_entityModeling_Page", Condition49: "forms_entityModeling_CompositeCondition"):
        self.booleanOperator = booleanOperator
        self.forms_entityModeling_CompositeCondition = forms_entityModeling_CompositeCondition if forms_entityModeling_CompositeCondition is not None else set()
        
    @property
    def booleanOperator(self) -> str:
        return self.__booleanOperator

    @booleanOperator.setter
    def booleanOperator(self, booleanOperator: str):
        self.__booleanOperator = booleanOperator

    @property
    def forms_entityModeling_CompositeCondition(self):
        return self.__forms_entityModeling_CompositeCondition

    @forms_entityModeling_CompositeCondition.setter
    def forms_entityModeling_CompositeCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_entityModeling_CompositeCondition__forms_entityModeling_CompositeCondition", None)
        self.__forms_entityModeling_CompositeCondition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Condition49"):
                    opp_val = getattr(item, "Condition49", None)
                    
                    if opp_val == self:
                        setattr(item, "Condition49", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Condition49"):
                    opp_val = getattr(item, "Condition49", None)
                    
                    setattr(item, "Condition49", self)
                    

class PageElement:

    pass
class forms_entityModeling_RelationshipPageElement(PageElement):

    pass
class forms_entityModeling_AttributePageElement(PageElement):

    def __init__(self, valueOfAttribute: str, forms_entityModeling_AttributePageElement: "Attribute" = None, PageElement: "forms_entityModeling_Page"):
        self.valueOfAttribute = valueOfAttribute
        self.forms_entityModeling_AttributePageElement = forms_entityModeling_AttributePageElement
        
    @property
    def valueOfAttribute(self) -> str:
        return self.__valueOfAttribute

    @valueOfAttribute.setter
    def valueOfAttribute(self, valueOfAttribute: str):
        self.__valueOfAttribute = valueOfAttribute

    @property
    def forms_entityModeling_AttributePageElement(self):
        return self.__forms_entityModeling_AttributePageElement

    @forms_entityModeling_AttributePageElement.setter
    def forms_entityModeling_AttributePageElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_entityModeling_AttributePageElement__forms_entityModeling_AttributePageElement", None)
        self.__forms_entityModeling_AttributePageElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Attribute35"):
                opp_val = getattr(old_value, "Attribute35", None)
                if opp_val == self:
                    setattr(old_value, "Attribute35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Attribute35"):
                opp_val = getattr(value, "Attribute35", None)
                setattr(value, "Attribute35", self)

    def enterValues(self):
        # TODO: Implement enterValues method
        pass

class forms_entityModeling_Page:

    def __init__(self, title: str, forms_entityModeling_Page: set["PageElement"] = None, forms_entityModeling_Page31: "Condition" = None):
        self.title = title
        self.forms_entityModeling_Page = forms_entityModeling_Page if forms_entityModeling_Page is not None else set()
        self.forms_entityModeling_Page31 = forms_entityModeling_Page31
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def forms_entityModeling_Page(self):
        return self.__forms_entityModeling_Page

    @forms_entityModeling_Page.setter
    def forms_entityModeling_Page(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_entityModeling_Page__forms_entityModeling_Page", None)
        self.__forms_entityModeling_Page = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PageElement"):
                    opp_val = getattr(item, "PageElement", None)
                    
                    if opp_val == self:
                        setattr(item, "PageElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PageElement"):
                    opp_val = getattr(item, "PageElement", None)
                    
                    setattr(item, "PageElement", self)
                    

    @property
    def forms_entityModeling_Page31(self):
        return self.__forms_entityModeling_Page31

    @forms_entityModeling_Page31.setter
    def forms_entityModeling_Page31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_entityModeling_Page__forms_entityModeling_Page31", None)
        self.__forms_entityModeling_Page31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Condition"):
                opp_val = getattr(old_value, "Condition", None)
                if opp_val == self:
                    setattr(old_value, "Condition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Condition"):
                opp_val = getattr(value, "Condition", None)
                setattr(value, "Condition", self)

class Page:

    pass
class forms_entityModeling_Literal:

    def __init__(self, name: str, value: str):
        self.name = name
        self.value = value
        
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

class forms_entityModeling_Relationship:

    def __init__(self, name: str, lowerBound: int, upperBound: int, forms_entityModeling_Relationship23: "Relationship" = None, forms_entityModeling_Relationship: "Entity" = None):
        self.name = name
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.forms_entityModeling_Relationship23 = forms_entityModeling_Relationship23
        self.forms_entityModeling_Relationship = forms_entityModeling_Relationship
        
    @property
    def upperBound(self) -> int:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: int):
        self.__upperBound = upperBound

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
    def forms_entityModeling_Relationship(self):
        return self.__forms_entityModeling_Relationship

    @forms_entityModeling_Relationship.setter
    def forms_entityModeling_Relationship(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_entityModeling_Relationship__forms_entityModeling_Relationship", None)
        self.__forms_entityModeling_Relationship = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Entity21"):
                opp_val = getattr(old_value, "Entity21", None)
                if opp_val == self:
                    setattr(old_value, "Entity21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Entity21"):
                opp_val = getattr(value, "Entity21", None)
                setattr(value, "Entity21", self)

    @property
    def forms_entityModeling_Relationship23(self):
        return self.__forms_entityModeling_Relationship23

    @forms_entityModeling_Relationship23.setter
    def forms_entityModeling_Relationship23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_entityModeling_Relationship__forms_entityModeling_Relationship23", None)
        self.__forms_entityModeling_Relationship23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Relationship24"):
                opp_val = getattr(old_value, "Relationship24", None)
                if opp_val == self:
                    setattr(old_value, "Relationship24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Relationship24"):
                opp_val = getattr(value, "Relationship24", None)
                setattr(value, "Relationship24", self)

class Literal:

    pass
class forms_entityModeling_Enumeration:

    def __init__(self, name: str, forms_entityModeling_Enumeration: set["Literal"] = None):
        self.name = name
        self.forms_entityModeling_Enumeration = forms_entityModeling_Enumeration if forms_entityModeling_Enumeration is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def forms_entityModeling_Enumeration(self):
        return self.__forms_entityModeling_Enumeration

    @forms_entityModeling_Enumeration.setter
    def forms_entityModeling_Enumeration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_entityModeling_Enumeration__forms_entityModeling_Enumeration", None)
        self.__forms_entityModeling_Enumeration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Literal"):
                    opp_val = getattr(item, "Literal", None)
                    
                    if opp_val == self:
                        setattr(item, "Literal", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Literal"):
                    opp_val = getattr(item, "Literal", None)
                    
                    setattr(item, "Literal", self)
                    

class forms_entityModeling_Entity:

    def __init__(self, name: str, forms_entityModeling_Entity: "Attribute" = None, forms_entityModeling_Entity10: set["Attribute"] = None, forms_entityModeling_Entity13: "Entity" = None, forms_entityModeling_Entity16: set["Relationship"] = None):
        self.name = name
        self.forms_entityModeling_Entity = forms_entityModeling_Entity
        self.forms_entityModeling_Entity10 = forms_entityModeling_Entity10 if forms_entityModeling_Entity10 is not None else set()
        self.forms_entityModeling_Entity13 = forms_entityModeling_Entity13
        self.forms_entityModeling_Entity16 = forms_entityModeling_Entity16 if forms_entityModeling_Entity16 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def forms_entityModeling_Entity13(self):
        return self.__forms_entityModeling_Entity13

    @forms_entityModeling_Entity13.setter
    def forms_entityModeling_Entity13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_entityModeling_Entity__forms_entityModeling_Entity13", None)
        self.__forms_entityModeling_Entity13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Entity14"):
                opp_val = getattr(old_value, "Entity14", None)
                if opp_val == self:
                    setattr(old_value, "Entity14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Entity14"):
                opp_val = getattr(value, "Entity14", None)
                setattr(value, "Entity14", self)

    @property
    def forms_entityModeling_Entity(self):
        return self.__forms_entityModeling_Entity

    @forms_entityModeling_Entity.setter
    def forms_entityModeling_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_entityModeling_Entity__forms_entityModeling_Entity", None)
        self.__forms_entityModeling_Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Attribute"):
                opp_val = getattr(old_value, "Attribute", None)
                if opp_val == self:
                    setattr(old_value, "Attribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Attribute"):
                opp_val = getattr(value, "Attribute", None)
                setattr(value, "Attribute", self)

    @property
    def forms_entityModeling_Entity10(self):
        return self.__forms_entityModeling_Entity10

    @forms_entityModeling_Entity10.setter
    def forms_entityModeling_Entity10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_entityModeling_Entity__forms_entityModeling_Entity10", None)
        self.__forms_entityModeling_Entity10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Attribute11"):
                    opp_val = getattr(item, "Attribute11", None)
                    
                    if opp_val == self:
                        setattr(item, "Attribute11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Attribute11"):
                    opp_val = getattr(item, "Attribute11", None)
                    
                    setattr(item, "Attribute11", self)
                    

    @property
    def forms_entityModeling_Entity16(self):
        return self.__forms_entityModeling_Entity16

    @forms_entityModeling_Entity16.setter
    def forms_entityModeling_Entity16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_entityModeling_Entity__forms_entityModeling_Entity16", None)
        self.__forms_entityModeling_Entity16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Relationship"):
                    opp_val = getattr(item, "Relationship", None)
                    
                    if opp_val == self:
                        setattr(item, "Relationship", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Relationship"):
                    opp_val = getattr(item, "Relationship", None)
                    
                    setattr(item, "Relationship", self)
                    

class forms_entityModeling_Attribute:

    def __init__(self, mandatory: bool, type: str, name: str, forms_entityModeling_Attribute: "Enumeration" = None):
        self.mandatory = mandatory
        self.type = type
        self.name = name
        self.forms_entityModeling_Attribute = forms_entityModeling_Attribute
        
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
    def mandatory(self) -> bool:
        return self.__mandatory

    @mandatory.setter
    def mandatory(self, mandatory: bool):
        self.__mandatory = mandatory

    @property
    def forms_entityModeling_Attribute(self):
        return self.__forms_entityModeling_Attribute

    @forms_entityModeling_Attribute.setter
    def forms_entityModeling_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_entityModeling_Attribute__forms_entityModeling_Attribute", None)
        self.__forms_entityModeling_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Enumeration18"):
                opp_val = getattr(old_value, "Enumeration18", None)
                if opp_val == self:
                    setattr(old_value, "Enumeration18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Enumeration18"):
                opp_val = getattr(value, "Enumeration18", None)
                setattr(value, "Enumeration18", self)

class Relationship:

    pass
class Attribute:

    pass
class forms_EFML_model:

    pass
class Form:

    pass
class Enumeration:

    pass
class Entity:

    pass