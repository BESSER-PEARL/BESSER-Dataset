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
class Operators(Enum):
    AND = "AND"
    OR = "OR"
class AttributeType(Enum):
    None = "None"
    String = "String"
    Text = "Text"
    Integer = "Integer"
    Date = "Date"
    Time = "Time"
    Year = "Year"
    Email = "Email"
    Boolean = "Boolean"


############################################
# Definition of Classes
############################################

class Condition:

    pass
class forms_AttributeValueCondition(Condition):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class forms_Condition(ABC):

    def __init__(self, conditionID: str, type: str, forms_Condition: "forms_CompositeCondition" = None):
        self.conditionID = conditionID
        self.type = type
        self.forms_Condition = forms_Condition
        
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
    def forms_Condition(self):
        return self.__forms_Condition

    @forms_Condition.setter
    def forms_Condition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Condition__forms_Condition", None)
        self.__forms_Condition = value
        
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

class forms_Column:

    pass
class RelationshipPageElement:

    pass
class forms_Table(RelationshipPageElement):

    pass
class forms_List(RelationshipPageElement):

    pass
class forms_CompositeCondition(Condition):

    def __init__(self, operator: str, forms_CompositeCondition: set["forms_Condition"] = None):
        self.operator = operator
        self.forms_CompositeCondition = forms_CompositeCondition if forms_CompositeCondition is not None else set()
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

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
                if hasattr(item, "forms_Condition"):
                    opp_val = getattr(item, "forms_Condition", None)
                    
                    if opp_val == self:
                        setattr(item, "forms_Condition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "forms_Condition"):
                    opp_val = getattr(item, "forms_Condition", None)
                    
                    setattr(item, "forms_Condition", self)
                    

class PageElement:

    pass
class forms_RelationshipPageElement(PageElement):

    pass
class forms_AttributePageElement(PageElement):

    pass
class forms_PageElement(ABC):

    def __init__(self, label: str, elementID: str, forms_PageElement: "forms_Page" = None):
        self.label = label
        self.elementID = elementID
        self.forms_PageElement = forms_PageElement
        
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
            if hasattr(old_value, "forms_Page29"):
                opp_val = getattr(old_value, "forms_Page29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Page29"):
                opp_val = getattr(value, "forms_Page29", None)
                if opp_val is None:
                    setattr(value, "forms_Page29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class forms_Page:

    def __init__(self, title: str, forms_Page: "forms_Form" = None, forms_Page29: set["forms_PageElement"] = None):
        self.title = title
        self.forms_Page = forms_Page
        self.forms_Page29 = forms_Page29 if forms_Page29 is not None else set()
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

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
            if hasattr(old_value, "forms_Form27"):
                opp_val = getattr(old_value, "forms_Form27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Form27"):
                opp_val = getattr(value, "forms_Form27", None)
                if opp_val is None:
                    setattr(value, "forms_Form27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def forms_Page29(self):
        return self.__forms_Page29

    @forms_Page29.setter
    def forms_Page29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Page__forms_Page29", None)
        self.__forms_Page29 = value if value is not None else set()
        
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
                    

class AttributePageElement:

    pass
class forms_TimeSelectionField(AttributePageElement):

    pass
class forms_SelectionField(AttributePageElement):

    pass
class forms_TextArea(AttributePageElement):

    pass
class forms_DateSelectionField(AttributePageElement):

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

class forms_Literal:

    def __init__(self, name: str, value: str, forms_Literal: "forms_Enumeration" = None):
        self.name = name
        self.value = value
        self.forms_Literal = forms_Literal
        
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
            if hasattr(old_value, "forms_Enumeration16"):
                opp_val = getattr(old_value, "forms_Enumeration16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Enumeration16"):
                opp_val = getattr(value, "forms_Enumeration16", None)
                if opp_val is None:
                    setattr(value, "forms_Enumeration16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class forms_Enumeration:

    def __init__(self, name: str, forms_Enumeration: "forms_Attribute" = None, forms_Enumeration16: set["forms_Literal"] = None):
        self.name = name
        self.forms_Enumeration = forms_Enumeration
        self.forms_Enumeration16 = forms_Enumeration16 if forms_Enumeration16 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def forms_Enumeration16(self):
        return self.__forms_Enumeration16

    @forms_Enumeration16.setter
    def forms_Enumeration16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Enumeration__forms_Enumeration16", None)
        self.__forms_Enumeration16 = value if value is not None else set()
        
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
            if hasattr(old_value, "forms_Attribute14"):
                opp_val = getattr(old_value, "forms_Attribute14", None)
                if opp_val == self:
                    setattr(old_value, "forms_Attribute14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Attribute14"):
                opp_val = getattr(value, "forms_Attribute14", None)
                setattr(value, "forms_Attribute14", self)

class forms_Relationship:

    def __init__(self, lowerBound: int, name: str, upperBound: int, forms_Relationship: "forms_Entity" = None, forms_Relationship19: "forms_Relationship" = None, forms_Relationship17: "forms_Relationship" = None, forms_Relationship21: "forms_Entity" = None):
        self.lowerBound = lowerBound
        self.name = name
        self.upperBound = upperBound
        self.forms_Relationship = forms_Relationship
        self.forms_Relationship19 = forms_Relationship19
        self.forms_Relationship17 = forms_Relationship17
        self.forms_Relationship21 = forms_Relationship21
        
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
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def forms_Relationship19(self):
        return self.__forms_Relationship19

    @forms_Relationship19.setter
    def forms_Relationship19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Relationship__forms_Relationship19", None)
        self.__forms_Relationship19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Relationship17"):
                opp_val = getattr(old_value, "forms_Relationship17", None)
                if opp_val == self:
                    setattr(old_value, "forms_Relationship17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Relationship17"):
                opp_val = getattr(value, "forms_Relationship17", None)
                setattr(value, "forms_Relationship17", self)

    @property
    def forms_Relationship17(self):
        return self.__forms_Relationship17

    @forms_Relationship17.setter
    def forms_Relationship17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Relationship__forms_Relationship17", None)
        self.__forms_Relationship17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Relationship19"):
                opp_val = getattr(old_value, "forms_Relationship19", None)
                if opp_val == self:
                    setattr(old_value, "forms_Relationship19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Relationship19"):
                opp_val = getattr(value, "forms_Relationship19", None)
                setattr(value, "forms_Relationship19", self)

    @property
    def forms_Relationship21(self):
        return self.__forms_Relationship21

    @forms_Relationship21.setter
    def forms_Relationship21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Relationship__forms_Relationship21", None)
        self.__forms_Relationship21 = value
        
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
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Entity9"):
                opp_val = getattr(value, "forms_Entity9", None)
                if opp_val is None:
                    setattr(value, "forms_Entity9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class forms_Attribute:

    def __init__(self, name: str, mandatory: bool, type: str, forms_Attribute: "forms_Entity" = None, forms_Attribute7: "forms_Entity" = None, forms_Attribute14: "forms_Enumeration" = None, forms_Attribute31: "forms_AttributePageElement" = None, forms_Attribute37: "forms_Column" = None):
        self.name = name
        self.mandatory = mandatory
        self.type = type
        self.forms_Attribute = forms_Attribute
        self.forms_Attribute7 = forms_Attribute7
        self.forms_Attribute14 = forms_Attribute14
        self.forms_Attribute31 = forms_Attribute31
        self.forms_Attribute37 = forms_Attribute37
        
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
    def forms_Attribute31(self):
        return self.__forms_Attribute31

    @forms_Attribute31.setter
    def forms_Attribute31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Attribute__forms_Attribute31", None)
        self.__forms_Attribute31 = value
        
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
            if hasattr(old_value, "forms_Entity4"):
                opp_val = getattr(old_value, "forms_Entity4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Entity4"):
                opp_val = getattr(value, "forms_Entity4", None)
                if opp_val is None:
                    setattr(value, "forms_Entity4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def forms_Attribute37(self):
        return self.__forms_Attribute37

    @forms_Attribute37.setter
    def forms_Attribute37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Attribute__forms_Attribute37", None)
        self.__forms_Attribute37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Column36"):
                opp_val = getattr(old_value, "forms_Column36", None)
                if opp_val == self:
                    setattr(old_value, "forms_Column36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Column36"):
                opp_val = getattr(value, "forms_Column36", None)
                setattr(value, "forms_Column36", self)

    @property
    def forms_Attribute14(self):
        return self.__forms_Attribute14

    @forms_Attribute14.setter
    def forms_Attribute14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Attribute__forms_Attribute14", None)
        self.__forms_Attribute14 = value
        
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
    def forms_Attribute7(self):
        return self.__forms_Attribute7

    @forms_Attribute7.setter
    def forms_Attribute7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Attribute__forms_Attribute7", None)
        self.__forms_Attribute7 = value
        
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

class forms_Form:

    def __init__(self, description: str, name: str, title: str, mainForm: bool, forms_Form: "forms_EFML" = None, forms_Form24: "forms_Entity" = None, forms_Form27: set["forms_Page"] = None, forms_Form33: "forms_RelationshipPageElement" = None):
        self.description = description
        self.name = name
        self.title = title
        self.mainForm = mainForm
        self.forms_Form = forms_Form
        self.forms_Form24 = forms_Form24
        self.forms_Form27 = forms_Form27 if forms_Form27 is not None else set()
        self.forms_Form33 = forms_Form33
        
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
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mainForm(self) -> bool:
        return self.__mainForm

    @mainForm.setter
    def mainForm(self, mainForm: bool):
        self.__mainForm = mainForm

    @property
    def forms_Form27(self):
        return self.__forms_Form27

    @forms_Form27.setter
    def forms_Form27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Form__forms_Form27", None)
        self.__forms_Form27 = value if value is not None else set()
        
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
    def forms_Form33(self):
        return self.__forms_Form33

    @forms_Form33.setter
    def forms_Form33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Form__forms_Form33", None)
        self.__forms_Form33 = value
        
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
            if hasattr(old_value, "forms_EFML2"):
                opp_val = getattr(old_value, "forms_EFML2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_EFML2"):
                opp_val = getattr(value, "forms_EFML2", None)
                if opp_val is None:
                    setattr(value, "forms_EFML2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def forms_Form24(self):
        return self.__forms_Form24

    @forms_Form24.setter
    def forms_Form24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Form__forms_Form24", None)
        self.__forms_Form24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Entity25"):
                opp_val = getattr(old_value, "forms_Entity25", None)
                if opp_val == self:
                    setattr(old_value, "forms_Entity25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Entity25"):
                opp_val = getattr(value, "forms_Entity25", None)
                setattr(value, "forms_Entity25", self)

class forms_Entity:

    def __init__(self, name: str, forms_Entity: "forms_EFML" = None, forms_Entity4: set["forms_Attribute"] = None, forms_Entity6: "forms_Attribute" = None, forms_Entity9: set["forms_Relationship"] = None, forms_Entity12: "forms_Entity" = None, forms_Entity10: "forms_Entity" = None, forms_Entity22: "forms_Relationship" = None, forms_Entity25: "forms_Form" = None):
        self.name = name
        self.forms_Entity = forms_Entity
        self.forms_Entity4 = forms_Entity4 if forms_Entity4 is not None else set()
        self.forms_Entity6 = forms_Entity6
        self.forms_Entity9 = forms_Entity9 if forms_Entity9 is not None else set()
        self.forms_Entity12 = forms_Entity12
        self.forms_Entity10 = forms_Entity10
        self.forms_Entity22 = forms_Entity22
        self.forms_Entity25 = forms_Entity25
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def forms_Entity4(self):
        return self.__forms_Entity4

    @forms_Entity4.setter
    def forms_Entity4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Entity__forms_Entity4", None)
        self.__forms_Entity4 = value if value is not None else set()
        
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
    def forms_Entity25(self):
        return self.__forms_Entity25

    @forms_Entity25.setter
    def forms_Entity25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Entity__forms_Entity25", None)
        self.__forms_Entity25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Form24"):
                opp_val = getattr(old_value, "forms_Form24", None)
                if opp_val == self:
                    setattr(old_value, "forms_Form24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Form24"):
                opp_val = getattr(value, "forms_Form24", None)
                setattr(value, "forms_Form24", self)

    @property
    def forms_Entity12(self):
        return self.__forms_Entity12

    @forms_Entity12.setter
    def forms_Entity12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Entity__forms_Entity12", None)
        self.__forms_Entity12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Entity10"):
                opp_val = getattr(old_value, "forms_Entity10", None)
                if opp_val == self:
                    setattr(old_value, "forms_Entity10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Entity10"):
                opp_val = getattr(value, "forms_Entity10", None)
                setattr(value, "forms_Entity10", self)

    @property
    def forms_Entity(self):
        return self.__forms_Entity

    @forms_Entity.setter
    def forms_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Entity__forms_Entity", None)
        self.__forms_Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_EFML"):
                opp_val = getattr(old_value, "forms_EFML", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_EFML"):
                opp_val = getattr(value, "forms_EFML", None)
                if opp_val is None:
                    setattr(value, "forms_EFML", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def forms_Entity10(self):
        return self.__forms_Entity10

    @forms_Entity10.setter
    def forms_Entity10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Entity__forms_Entity10", None)
        self.__forms_Entity10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Entity12"):
                opp_val = getattr(old_value, "forms_Entity12", None)
                if opp_val == self:
                    setattr(old_value, "forms_Entity12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Entity12"):
                opp_val = getattr(value, "forms_Entity12", None)
                setattr(value, "forms_Entity12", self)

    @property
    def forms_Entity9(self):
        return self.__forms_Entity9

    @forms_Entity9.setter
    def forms_Entity9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Entity__forms_Entity9", None)
        self.__forms_Entity9 = value if value is not None else set()
        
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
    def forms_Entity22(self):
        return self.__forms_Entity22

    @forms_Entity22.setter
    def forms_Entity22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Entity__forms_Entity22", None)
        self.__forms_Entity22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Relationship21"):
                opp_val = getattr(old_value, "forms_Relationship21", None)
                if opp_val == self:
                    setattr(old_value, "forms_Relationship21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Relationship21"):
                opp_val = getattr(value, "forms_Relationship21", None)
                setattr(value, "forms_Relationship21", self)

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
            if hasattr(old_value, "forms_Attribute7"):
                opp_val = getattr(old_value, "forms_Attribute7", None)
                if opp_val == self:
                    setattr(old_value, "forms_Attribute7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Attribute7"):
                opp_val = getattr(value, "forms_Attribute7", None)
                setattr(value, "forms_Attribute7", self)

class forms_EFML:

    pass