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
    None = "None"
class AttributeType(Enum):
    Date = "Date"
    Time = "Time"
    String = "String"
    Integer = "Integer"
    Text = "Text"
    Email = "Email"
    Boolean = "Boolean"
    Year = "Year"
    None = "None"
class CompositeConditionType(Enum):
    And = "And"
    Or = "Or"


############################################
# Definition of Classes
############################################

class PageElement:

    pass
class forms_RelationshipPageElement(PageElement):

    pass
class forms_AttributePageElement(PageElement):

    pass
class Condition:

    pass
class forms_AttributeValueCondition(Condition):

    def __init__(self, value: str, forms_AttributeValueCondition: "forms_Attribute" = None):
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
            if hasattr(old_value, "forms_Attribute31"):
                opp_val = getattr(old_value, "forms_Attribute31", None)
                if opp_val == self:
                    setattr(old_value, "forms_Attribute31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Attribute31"):
                opp_val = getattr(value, "forms_Attribute31", None)
                setattr(value, "forms_Attribute31", self)

class RelationshipPageElement:

    pass
class forms_Table(RelationshipPageElement):

    pass
class forms_List(RelationshipPageElement):

    pass
class forms_CompositeCondition(Condition):

    def __init__(self, compositionType: str, forms_CompositeCondition: set["forms_Condition"] = None):
        self.compositionType = compositionType
        self.forms_CompositeCondition = forms_CompositeCondition if forms_CompositeCondition is not None else set()
        
    @property
    def compositionType(self) -> str:
        return self.__compositionType

    @compositionType.setter
    def compositionType(self, compositionType: str):
        self.__compositionType = compositionType

    @property
    def forms_CompositeCondition(self):
        return self.__forms_CompositeCondition

    @forms_CompositeCondition.setter
    def forms_CompositeCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_CompositeCondition__forms_CompositeCondition", None)
        self.__forms_CompositeCondition = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "forms_Condition33"):
                    opp_val = getattr(item, "forms_Condition33", None)
                    
                    if opp_val == self:
                        setattr(item, "forms_Condition33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "forms_Condition33"):
                    opp_val = getattr(item, "forms_Condition33", None)
                    
                    setattr(item, "forms_Condition33", self)
                    

class AttributePageElement:

    pass
class forms_DateSelectionField(AttributePageElement):

    pass
class forms_Column(AttributePageElement):

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

class forms_Condition(ABC):

    def __init__(self, type: str, conditionID: str, forms_Condition: "forms_Page" = None, forms_Condition28: "forms_PageElement" = None, forms_Condition33: "forms_CompositeCondition" = None):
        self.type = type
        self.conditionID = conditionID
        self.forms_Condition = forms_Condition
        self.forms_Condition28 = forms_Condition28
        self.forms_Condition33 = forms_Condition33
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def conditionID(self) -> str:
        return self.__conditionID

    @conditionID.setter
    def conditionID(self, conditionID: str):
        self.__conditionID = conditionID

    @property
    def forms_Condition33(self):
        return self.__forms_Condition33

    @forms_Condition33.setter
    def forms_Condition33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Condition__forms_Condition33", None)
        self.__forms_Condition33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_CompositeCondition"):
                opp_val = getattr(old_value, "forms_CompositeCondition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_CompositeCondition"):
                opp_val = getattr(value, "forms_CompositeCondition", None)
                if opp_val is None:
                    setattr(value, "forms_CompositeCondition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def forms_Condition28(self):
        return self.__forms_Condition28

    @forms_Condition28.setter
    def forms_Condition28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Condition__forms_Condition28", None)
        self.__forms_Condition28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_PageElement27"):
                opp_val = getattr(old_value, "forms_PageElement27", None)
                if opp_val == self:
                    setattr(old_value, "forms_PageElement27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_PageElement27"):
                opp_val = getattr(value, "forms_PageElement27", None)
                setattr(value, "forms_PageElement27", self)

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
            if hasattr(old_value, "forms_Page25"):
                opp_val = getattr(old_value, "forms_Page25", None)
                if opp_val == self:
                    setattr(old_value, "forms_Page25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Page25"):
                opp_val = getattr(value, "forms_Page25", None)
                setattr(value, "forms_Page25", self)

class forms_PageElement(ABC):

    def __init__(self, label: str, elementID: str, forms_PageElement: "forms_Page" = None, forms_PageElement27: "forms_Condition" = None):
        self.label = label
        self.elementID = elementID
        self.forms_PageElement = forms_PageElement
        self.forms_PageElement27 = forms_PageElement27
        
    @property
    def elementID(self) -> str:
        return self.__elementID

    @elementID.setter
    def elementID(self, elementID: str):
        self.__elementID = elementID

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def forms_PageElement27(self):
        return self.__forms_PageElement27

    @forms_PageElement27.setter
    def forms_PageElement27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_PageElement__forms_PageElement27", None)
        self.__forms_PageElement27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Condition28"):
                opp_val = getattr(old_value, "forms_Condition28", None)
                if opp_val == self:
                    setattr(old_value, "forms_Condition28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Condition28"):
                opp_val = getattr(value, "forms_Condition28", None)
                setattr(value, "forms_Condition28", self)

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
            if hasattr(old_value, "forms_Page23"):
                opp_val = getattr(old_value, "forms_Page23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Page23"):
                opp_val = getattr(value, "forms_Page23", None)
                if opp_val is None:
                    setattr(value, "forms_Page23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class forms_SelectionField(AttributePageElement):

    pass
class forms_TextArea(AttributePageElement):

    pass
class forms_Page:

    def __init__(self, title: str, forms_Page: "forms_Form" = None, forms_Page23: set["forms_PageElement"] = None, forms_Page25: "forms_Condition" = None):
        self.title = title
        self.forms_Page = forms_Page
        self.forms_Page23 = forms_Page23 if forms_Page23 is not None else set()
        self.forms_Page25 = forms_Page25
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def forms_Page23(self):
        return self.__forms_Page23

    @forms_Page23.setter
    def forms_Page23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Page__forms_Page23", None)
        self.__forms_Page23 = value if value is not None else set()
        
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
            if hasattr(old_value, "forms_Form21"):
                opp_val = getattr(old_value, "forms_Form21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Form21"):
                opp_val = getattr(value, "forms_Form21", None)
                if opp_val is None:
                    setattr(value, "forms_Form21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def forms_Page25(self):
        return self.__forms_Page25

    @forms_Page25.setter
    def forms_Page25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Page__forms_Page25", None)
        self.__forms_Page25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Condition"):
                opp_val = getattr(old_value, "forms_Condition", None)
                if opp_val == self:
                    setattr(old_value, "forms_Condition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Condition"):
                opp_val = getattr(value, "forms_Condition", None)
                setattr(value, "forms_Condition", self)

class forms_FormModel:

    pass
class forms_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class forms_EntityModelElement(ABC):

    pass
class forms_EntityModel:

    pass
class Feature:

    pass
class forms_Relationship(Feature):

    def __init__(self, upperBound: int, lowerBound: int, forms_Relationship: "forms_Entity" = None, forms_Relationship12: "forms_Relationship" = None, forms_Relationship10: "forms_Relationship" = None, forms_Relationship37: "forms_RelationshipPageElement" = None):
        self.upperBound = upperBound
        self.lowerBound = lowerBound
        self.forms_Relationship = forms_Relationship
        self.forms_Relationship12 = forms_Relationship12
        self.forms_Relationship10 = forms_Relationship10
        self.forms_Relationship37 = forms_Relationship37
        
    @property
    def upperBound(self) -> int:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: int):
        self.__upperBound = upperBound

    @property
    def lowerBound(self) -> int:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: int):
        self.__lowerBound = lowerBound

    @property
    def forms_Relationship10(self):
        return self.__forms_Relationship10

    @forms_Relationship10.setter
    def forms_Relationship10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Relationship__forms_Relationship10", None)
        self.__forms_Relationship10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Relationship12"):
                opp_val = getattr(old_value, "forms_Relationship12", None)
                if opp_val == self:
                    setattr(old_value, "forms_Relationship12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Relationship12"):
                opp_val = getattr(value, "forms_Relationship12", None)
                setattr(value, "forms_Relationship12", self)

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
            if hasattr(old_value, "forms_Entity9"):
                opp_val = getattr(old_value, "forms_Entity9", None)
                if opp_val == self:
                    setattr(old_value, "forms_Entity9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Entity9"):
                opp_val = getattr(value, "forms_Entity9", None)
                setattr(value, "forms_Entity9", self)

    @property
    def forms_Relationship37(self):
        return self.__forms_Relationship37

    @forms_Relationship37.setter
    def forms_Relationship37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Relationship__forms_Relationship37", None)
        self.__forms_Relationship37 = value
        
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
    def forms_Relationship12(self):
        return self.__forms_Relationship12

    @forms_Relationship12.setter
    def forms_Relationship12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Relationship__forms_Relationship12", None)
        self.__forms_Relationship12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Relationship10"):
                opp_val = getattr(old_value, "forms_Relationship10", None)
                if opp_val == self:
                    setattr(old_value, "forms_Relationship10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Relationship10"):
                opp_val = getattr(value, "forms_Relationship10", None)
                setattr(value, "forms_Relationship10", self)

class forms_Attribute(Feature):

    def __init__(self, type: str, mandatory: bool, forms_Attribute: "forms_Entity" = None, forms_Attribute7: "forms_Enumeration" = None, forms_Attribute31: "forms_AttributeValueCondition" = None, forms_Attribute35: "forms_AttributePageElement" = None):
        self.type = type
        self.mandatory = mandatory
        self.forms_Attribute = forms_Attribute
        self.forms_Attribute7 = forms_Attribute7
        self.forms_Attribute31 = forms_Attribute31
        self.forms_Attribute35 = forms_Attribute35
        
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
    def forms_Attribute31(self):
        return self.__forms_Attribute31

    @forms_Attribute31.setter
    def forms_Attribute31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Attribute__forms_Attribute31", None)
        self.__forms_Attribute31 = value
        
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
    def forms_Attribute35(self):
        return self.__forms_Attribute35

    @forms_Attribute35.setter
    def forms_Attribute35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Attribute__forms_Attribute35", None)
        self.__forms_Attribute35 = value
        
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

class EntityModelElement:

    pass
class NamedElement:

    pass
class forms_Literal(NamedElement):

    def __init__(self, value: str, forms_Literal: "forms_Enumeration" = None):
        self.value = value
        self.forms_Literal = forms_Literal
        
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
            if hasattr(old_value, "forms_Enumeration14"):
                opp_val = getattr(old_value, "forms_Enumeration14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Enumeration14"):
                opp_val = getattr(value, "forms_Enumeration14", None)
                if opp_val is None:
                    setattr(value, "forms_Enumeration14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class forms_Enumeration(EntityModelElement, NamedElement):

    pass
class forms_Feature(NamedElement):

    pass
class forms_Entity(EntityModelElement, NamedElement):

    pass
class forms_Form(NamedElement):

    def __init__(self, title: str, description: str, welcomeForm: bool, forms_Form: "forms_FormModel" = None, forms_Form18: "forms_Entity" = None, forms_Form21: set["forms_Page"] = None, forms_Form40: "forms_RelationshipPageElement" = None):
        self.title = title
        self.description = description
        self.welcomeForm = welcomeForm
        self.forms_Form = forms_Form
        self.forms_Form18 = forms_Form18
        self.forms_Form21 = forms_Form21 if forms_Form21 is not None else set()
        self.forms_Form40 = forms_Form40
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def welcomeForm(self) -> bool:
        return self.__welcomeForm

    @welcomeForm.setter
    def welcomeForm(self, welcomeForm: bool):
        self.__welcomeForm = welcomeForm

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
            if hasattr(old_value, "forms_FormModel"):
                opp_val = getattr(old_value, "forms_FormModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_FormModel"):
                opp_val = getattr(value, "forms_FormModel", None)
                if opp_val is None:
                    setattr(value, "forms_FormModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def forms_Form18(self):
        return self.__forms_Form18

    @forms_Form18.setter
    def forms_Form18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Form__forms_Form18", None)
        self.__forms_Form18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Entity19"):
                opp_val = getattr(old_value, "forms_Entity19", None)
                if opp_val == self:
                    setattr(old_value, "forms_Entity19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Entity19"):
                opp_val = getattr(value, "forms_Entity19", None)
                setattr(value, "forms_Entity19", self)

    @property
    def forms_Form21(self):
        return self.__forms_Form21

    @forms_Form21.setter
    def forms_Form21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Form__forms_Form21", None)
        self.__forms_Form21 = value if value is not None else set()
        
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
    def forms_Form40(self):
        return self.__forms_Form40

    @forms_Form40.setter
    def forms_Form40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Form__forms_Form40", None)
        self.__forms_Form40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_RelationshipPageElement39"):
                opp_val = getattr(old_value, "forms_RelationshipPageElement39", None)
                if opp_val == self:
                    setattr(old_value, "forms_RelationshipPageElement39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_RelationshipPageElement39"):
                opp_val = getattr(value, "forms_RelationshipPageElement39", None)
                setattr(value, "forms_RelationshipPageElement39", self)
