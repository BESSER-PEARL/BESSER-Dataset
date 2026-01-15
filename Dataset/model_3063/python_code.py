from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class CompositeConditionOperator(Enum):
    AND = "AND"
    OR = "OR"
class ConditionType(Enum):
    Show = "Show"
    Hide = "Hide"
    Enable = "Enable"
    Disable = "Disable"
class AttributeType(Enum):
    None = "None"
    Integer = "Integer"
    String = "String"
    Text = "Text"
    Date = "Date"
    Year = "Year"
    Time = "Time"
    Boolean = "Boolean"
    Email = "Email"


############################################
# Definition of Classes
############################################

class Condition:

    pass
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
            if hasattr(old_value, "forms_AttributePageElement64"):
                opp_val = getattr(old_value, "forms_AttributePageElement64", None)
                if opp_val == self:
                    setattr(old_value, "forms_AttributePageElement64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_AttributePageElement64"):
                opp_val = getattr(value, "forms_AttributePageElement64", None)
                setattr(value, "forms_AttributePageElement64", self)

class forms_CompositeCondition(Condition):

    def __init__(self, operator: str, CompositeCondition: "forms_Condition" = None, parentCondtion: set["forms_Condition"] = None):
        self.operator = operator
        self.CompositeCondition = CompositeCondition
        self.parentCondtion = parentCondtion if parentCondtion is not None else set()
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def CompositeCondition(self):
        return self.__CompositeCondition

    @CompositeCondition.setter
    def CompositeCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_CompositeCondition__CompositeCondition", None)
        self.__CompositeCondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conditions62"):
                opp_val = getattr(old_value, "conditions62", None)
                if opp_val == self:
                    setattr(old_value, "conditions62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conditions62"):
                opp_val = getattr(value, "conditions62", None)
                setattr(value, "conditions62", self)

    @property
    def parentCondtion(self):
        return self.__parentCondtion

    @parentCondtion.setter
    def parentCondtion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_CompositeCondition__parentCondtion", None)
        self.__parentCondtion = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Condition66"):
                    opp_val = getattr(item, "Condition66", None)
                    
                    if opp_val == self:
                        setattr(item, "Condition66", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Condition66"):
                    opp_val = getattr(item, "Condition66", None)
                    
                    setattr(item, "Condition66", self)
                    

class AttributePageElement:

    pass
class forms_SelectionAttributePageElement(AttributePageElement):

    pass
class forms_TextareaAttributePageElement(AttributePageElement):

    pass
class forms_TextFieldAttributePageElement(AttributePageElement):

    def __init__(self, format: str):
        self.format = format
        
    @property
    def format(self) -> str:
        return self.__format

    @format.setter
    def format(self, format: str):
        self.__format = format

class forms_Column:

    pass
class RelationshipPageElement:

    pass
class forms_TableRelationshipPageElement(RelationshipPageElement):

    pass
class forms_ListRelationshipPageElement(RelationshipPageElement):

    pass
class forms_TimeSelectionAttributePageElement(AttributePageElement):

    pass
class forms_DateSelectionAttributePageElement(AttributePageElement):

    pass
class PageElement:

    pass
class forms_RelationshipPageElement(PageElement):

    pass
class forms_AttributePageElement(PageElement):

    pass
class forms_Condition(ABC):

    def __init__(self, conditionID: str, type: str, Condition: "forms_Page" = None, Condition42: "forms_PageElement" = None, conditions: "forms_Page" = None, conditions59: "forms_PageElement" = None, conditions62: "forms_CompositeCondition" = None, Condition66: "forms_CompositeCondition" = None):
        self.conditionID = conditionID
        self.type = type
        self.Condition = Condition
        self.Condition42 = Condition42
        self.conditions = conditions
        self.conditions59 = conditions59
        self.conditions62 = conditions62
        self.Condition66 = Condition66
        
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
    def Condition(self):
        return self.__Condition

    @Condition.setter
    def Condition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Condition__Condition", None)
        self.__Condition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "page39"):
                opp_val = getattr(old_value, "page39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "page39"):
                opp_val = getattr(value, "page39", None)
                if opp_val is None:
                    setattr(value, "page39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def conditions59(self):
        return self.__conditions59

    @conditions59.setter
    def conditions59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Condition__conditions59", None)
        self.__conditions59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PageElement60"):
                opp_val = getattr(old_value, "PageElement60", None)
                if opp_val == self:
                    setattr(old_value, "PageElement60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PageElement60"):
                opp_val = getattr(value, "PageElement60", None)
                setattr(value, "PageElement60", self)

    @property
    def Condition66(self):
        return self.__Condition66

    @Condition66.setter
    def Condition66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Condition__Condition66", None)
        self.__Condition66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parentCondtion"):
                opp_val = getattr(old_value, "parentCondtion", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parentCondtion"):
                opp_val = getattr(value, "parentCondtion", None)
                if opp_val is None:
                    setattr(value, "parentCondtion", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def conditions(self):
        return self.__conditions

    @conditions.setter
    def conditions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Condition__conditions", None)
        self.__conditions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Page57"):
                opp_val = getattr(old_value, "Page57", None)
                if opp_val == self:
                    setattr(old_value, "Page57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Page57"):
                opp_val = getattr(value, "Page57", None)
                setattr(value, "Page57", self)

    @property
    def Condition42(self):
        return self.__Condition42

    @Condition42.setter
    def Condition42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Condition__Condition42", None)
        self.__Condition42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pageElement"):
                opp_val = getattr(old_value, "pageElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pageElement"):
                opp_val = getattr(value, "pageElement", None)
                if opp_val is None:
                    setattr(value, "pageElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def conditions62(self):
        return self.__conditions62

    @conditions62.setter
    def conditions62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Condition__conditions62", None)
        self.__conditions62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompositeCondition"):
                opp_val = getattr(old_value, "CompositeCondition", None)
                if opp_val == self:
                    setattr(old_value, "CompositeCondition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompositeCondition"):
                opp_val = getattr(value, "CompositeCondition", None)
                setattr(value, "CompositeCondition", self)

class forms_PageElement(ABC):

    def __init__(self, label: str, elementID: str, PageElement: "forms_Page" = None, pageElement: set["forms_Condition"] = None, pageElements: "forms_Page" = None, PageElement60: "forms_Condition" = None):
        self.label = label
        self.elementID = elementID
        self.PageElement = PageElement
        self.pageElement = pageElement if pageElement is not None else set()
        self.pageElements = pageElements
        self.PageElement60 = PageElement60
        
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
    def PageElement(self):
        return self.__PageElement

    @PageElement.setter
    def PageElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_PageElement__PageElement", None)
        self.__PageElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "page"):
                opp_val = getattr(old_value, "page", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "page"):
                opp_val = getattr(value, "page", None)
                if opp_val is None:
                    setattr(value, "page", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pageElements(self):
        return self.__pageElements

    @pageElements.setter
    def pageElements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_PageElement__pageElements", None)
        self.__pageElements = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Page44"):
                opp_val = getattr(old_value, "Page44", None)
                if opp_val == self:
                    setattr(old_value, "Page44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Page44"):
                opp_val = getattr(value, "Page44", None)
                setattr(value, "Page44", self)

    @property
    def pageElement(self):
        return self.__pageElement

    @pageElement.setter
    def pageElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_PageElement__pageElement", None)
        self.__pageElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Condition42"):
                    opp_val = getattr(item, "Condition42", None)
                    
                    if opp_val == self:
                        setattr(item, "Condition42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Condition42"):
                    opp_val = getattr(item, "Condition42", None)
                    
                    setattr(item, "Condition42", self)
                    

    @property
    def PageElement60(self):
        return self.__PageElement60

    @PageElement60.setter
    def PageElement60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_PageElement__PageElement60", None)
        self.__PageElement60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conditions59"):
                opp_val = getattr(old_value, "conditions59", None)
                if opp_val == self:
                    setattr(old_value, "conditions59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conditions59"):
                opp_val = getattr(value, "conditions59", None)
                setattr(value, "conditions59", self)

class forms_Page:

    def __init__(self, title: str, Page: "forms_Form" = None, page: set["forms_PageElement"] = None, page39: set["forms_Condition"] = None, pages: "forms_Form" = None, Page44: "forms_PageElement" = None, Page57: "forms_Condition" = None):
        self.title = title
        self.Page = Page
        self.page = page if page is not None else set()
        self.page39 = page39 if page39 is not None else set()
        self.pages = pages
        self.Page44 = Page44
        self.Page57 = Page57
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def Page57(self):
        return self.__Page57

    @Page57.setter
    def Page57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Page__Page57", None)
        self.__Page57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conditions"):
                opp_val = getattr(old_value, "conditions", None)
                if opp_val == self:
                    setattr(old_value, "conditions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conditions"):
                opp_val = getattr(value, "conditions", None)
                setattr(value, "conditions", self)

    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Page__pages", None)
        self.__pages = value
        
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
    def page39(self):
        return self.__page39

    @page39.setter
    def page39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Page__page39", None)
        self.__page39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Condition"):
                    opp_val = getattr(item, "Condition", None)
                    
                    if opp_val == self:
                        setattr(item, "Condition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Condition"):
                    opp_val = getattr(item, "Condition", None)
                    
                    setattr(item, "Condition", self)
                    

    @property
    def page(self):
        return self.__page

    @page.setter
    def page(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Page__page", None)
        self.__page = value if value is not None else set()
        
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
    def Page44(self):
        return self.__Page44

    @Page44.setter
    def Page44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Page__Page44", None)
        self.__Page44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pageElements"):
                opp_val = getattr(old_value, "pageElements", None)
                if opp_val == self:
                    setattr(old_value, "pageElements", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pageElements"):
                opp_val = getattr(value, "pageElements", None)
                setattr(value, "pageElements", self)

    @property
    def Page(self):
        return self.__Page

    @Page.setter
    def Page(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Page__Page", None)
        self.__Page = value
        
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

class forms_Form:

    def __init__(self, name: str, title: str, description: str, forms_Form: "forms_FormModel" = None, forms_Form32: "forms_FormModel" = None, forms_Form34: "forms_Entity" = None, form: set["forms_Page"] = None, Form: "forms_Page" = None, forms_Form51: "forms_RelationshipPageElement" = None):
        self.name = name
        self.title = title
        self.description = description
        self.forms_Form = forms_Form
        self.forms_Form32 = forms_Form32
        self.forms_Form34 = forms_Form34
        self.form = form if form is not None else set()
        self.Form = Form
        self.forms_Form51 = forms_Form51
        
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
    def forms_Form51(self):
        return self.__forms_Form51

    @forms_Form51.setter
    def forms_Form51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Form__forms_Form51", None)
        self.__forms_Form51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_RelationshipPageElement50"):
                opp_val = getattr(old_value, "forms_RelationshipPageElement50", None)
                if opp_val == self:
                    setattr(old_value, "forms_RelationshipPageElement50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_RelationshipPageElement50"):
                opp_val = getattr(value, "forms_RelationshipPageElement50", None)
                setattr(value, "forms_RelationshipPageElement50", self)

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
            if hasattr(old_value, "pages"):
                opp_val = getattr(old_value, "pages", None)
                if opp_val == self:
                    setattr(old_value, "pages", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pages"):
                opp_val = getattr(value, "pages", None)
                setattr(value, "pages", self)

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
            if hasattr(old_value, "forms_FormModel29"):
                opp_val = getattr(old_value, "forms_FormModel29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_FormModel29"):
                opp_val = getattr(value, "forms_FormModel29", None)
                if opp_val is None:
                    setattr(value, "forms_FormModel29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def forms_Form34(self):
        return self.__forms_Form34

    @forms_Form34.setter
    def forms_Form34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Form__forms_Form34", None)
        self.__forms_Form34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Entity35"):
                opp_val = getattr(old_value, "forms_Entity35", None)
                if opp_val == self:
                    setattr(old_value, "forms_Entity35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Entity35"):
                opp_val = getattr(value, "forms_Entity35", None)
                setattr(value, "forms_Entity35", self)

    @property
    def forms_Form32(self):
        return self.__forms_Form32

    @forms_Form32.setter
    def forms_Form32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Form__forms_Form32", None)
        self.__forms_Form32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_FormModel31"):
                opp_val = getattr(old_value, "forms_FormModel31", None)
                if opp_val == self:
                    setattr(old_value, "forms_FormModel31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_FormModel31"):
                opp_val = getattr(value, "forms_FormModel31", None)
                setattr(value, "forms_FormModel31", self)

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
                    

class forms_FormModel:

    pass
class forms_EnumerationLiteral:

    def __init__(self, name: str, value: str, forms_EnumerationLiteral: "forms_EnumerationType" = None):
        self.name = name
        self.value = value
        self.forms_EnumerationLiteral = forms_EnumerationLiteral
        
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
    def forms_EnumerationLiteral(self):
        return self.__forms_EnumerationLiteral

    @forms_EnumerationLiteral.setter
    def forms_EnumerationLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_EnumerationLiteral__forms_EnumerationLiteral", None)
        self.__forms_EnumerationLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_EnumerationType18"):
                opp_val = getattr(old_value, "forms_EnumerationType18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_EnumerationType18"):
                opp_val = getattr(value, "forms_EnumerationType18", None)
                if opp_val is None:
                    setattr(value, "forms_EnumerationType18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class forms_Attribute:

    def __init__(self, name: str, mandatory: bool, type: str, Attribute: "forms_Entity" = None, forms_Attribute: "forms_Entity" = None, forms_Attribute14: "forms_EnumerationType" = None, attributes: "forms_Entity" = None, forms_Attribute46: "forms_AttributePageElement" = None, forms_Attribute54: "forms_Column" = None):
        self.name = name
        self.mandatory = mandatory
        self.type = type
        self.Attribute = Attribute
        self.forms_Attribute = forms_Attribute
        self.forms_Attribute14 = forms_Attribute14
        self.attributes = attributes
        self.forms_Attribute46 = forms_Attribute46
        self.forms_Attribute54 = forms_Attribute54
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def attributes(self):
        return self.__attributes

    @attributes.setter
    def attributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Attribute__attributes", None)
        self.__attributes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Entity"):
                opp_val = getattr(old_value, "Entity", None)
                if opp_val == self:
                    setattr(old_value, "Entity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Entity"):
                opp_val = getattr(value, "Entity", None)
                setattr(value, "Entity", self)

    @property
    def forms_Attribute46(self):
        return self.__forms_Attribute46

    @forms_Attribute46.setter
    def forms_Attribute46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Attribute__forms_Attribute46", None)
        self.__forms_Attribute46 = value
        
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
    def forms_Attribute54(self):
        return self.__forms_Attribute54

    @forms_Attribute54.setter
    def forms_Attribute54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Attribute__forms_Attribute54", None)
        self.__forms_Attribute54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Column"):
                opp_val = getattr(old_value, "forms_Column", None)
                if opp_val == self:
                    setattr(old_value, "forms_Column", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Column"):
                opp_val = getattr(value, "forms_Column", None)
                setattr(value, "forms_Column", self)

    @property
    def Attribute(self):
        return self.__Attribute

    @Attribute.setter
    def Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Attribute__Attribute", None)
        self.__Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entity"):
                opp_val = getattr(old_value, "entity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entity"):
                opp_val = getattr(value, "entity", None)
                if opp_val is None:
                    setattr(value, "entity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
                if opp_val == self:
                    setattr(old_value, "forms_Entity4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Entity4"):
                opp_val = getattr(value, "forms_Entity4", None)
                setattr(value, "forms_Entity4", self)

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
            if hasattr(old_value, "forms_EnumerationType15"):
                opp_val = getattr(old_value, "forms_EnumerationType15", None)
                if opp_val == self:
                    setattr(old_value, "forms_EnumerationType15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_EnumerationType15"):
                opp_val = getattr(value, "forms_EnumerationType15", None)
                setattr(value, "forms_EnumerationType15", self)

class forms_EnumerationType:

    def __init__(self, name: str, forms_EnumerationType: "forms_EntityModel" = None, forms_EnumerationType18: set["forms_EnumerationLiteral"] = None, forms_EnumerationType15: "forms_Attribute" = None):
        self.name = name
        self.forms_EnumerationType = forms_EnumerationType
        self.forms_EnumerationType18 = forms_EnumerationType18 if forms_EnumerationType18 is not None else set()
        self.forms_EnumerationType15 = forms_EnumerationType15
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def forms_EnumerationType15(self):
        return self.__forms_EnumerationType15

    @forms_EnumerationType15.setter
    def forms_EnumerationType15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_EnumerationType__forms_EnumerationType15", None)
        self.__forms_EnumerationType15 = value
        
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

    @property
    def forms_EnumerationType(self):
        return self.__forms_EnumerationType

    @forms_EnumerationType.setter
    def forms_EnumerationType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_EnumerationType__forms_EnumerationType", None)
        self.__forms_EnumerationType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_EntityModel2"):
                opp_val = getattr(old_value, "forms_EntityModel2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_EntityModel2"):
                opp_val = getattr(value, "forms_EntityModel2", None)
                if opp_val is None:
                    setattr(value, "forms_EntityModel2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def forms_EnumerationType18(self):
        return self.__forms_EnumerationType18

    @forms_EnumerationType18.setter
    def forms_EnumerationType18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_EnumerationType__forms_EnumerationType18", None)
        self.__forms_EnumerationType18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "forms_EnumerationLiteral"):
                    opp_val = getattr(item, "forms_EnumerationLiteral", None)
                    
                    if opp_val == self:
                        setattr(item, "forms_EnumerationLiteral", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "forms_EnumerationLiteral"):
                    opp_val = getattr(item, "forms_EnumerationLiteral", None)
                    
                    setattr(item, "forms_EnumerationLiteral", self)
                    

class forms_Relationship:

    def __init__(self, name: str, lowerBound: str, upperBound: str, Relationship: "forms_Entity" = None, relationships: "forms_Entity" = None, forms_Relationship: "forms_Entity" = None, forms_Relationship25: "forms_Relationship" = None, forms_Relationship23: "forms_Relationship" = None, forms_Relationship48: "forms_RelationshipPageElement" = None):
        self.name = name
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.Relationship = Relationship
        self.relationships = relationships
        self.forms_Relationship = forms_Relationship
        self.forms_Relationship25 = forms_Relationship25
        self.forms_Relationship23 = forms_Relationship23
        self.forms_Relationship48 = forms_Relationship48
        
    @property
    def upperBound(self) -> str:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: str):
        self.__upperBound = upperBound

    @property
    def lowerBound(self) -> str:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: str):
        self.__lowerBound = lowerBound

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def relationships(self):
        return self.__relationships

    @relationships.setter
    def relationships(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Relationship__relationships", None)
        self.__relationships = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Entity20"):
                opp_val = getattr(old_value, "Entity20", None)
                if opp_val == self:
                    setattr(old_value, "Entity20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Entity20"):
                opp_val = getattr(value, "Entity20", None)
                setattr(value, "Entity20", self)

    @property
    def forms_Relationship25(self):
        return self.__forms_Relationship25

    @forms_Relationship25.setter
    def forms_Relationship25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Relationship__forms_Relationship25", None)
        self.__forms_Relationship25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Relationship23"):
                opp_val = getattr(old_value, "forms_Relationship23", None)
                if opp_val == self:
                    setattr(old_value, "forms_Relationship23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Relationship23"):
                opp_val = getattr(value, "forms_Relationship23", None)
                setattr(value, "forms_Relationship23", self)

    @property
    def forms_Relationship23(self):
        return self.__forms_Relationship23

    @forms_Relationship23.setter
    def forms_Relationship23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Relationship__forms_Relationship23", None)
        self.__forms_Relationship23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Relationship25"):
                opp_val = getattr(old_value, "forms_Relationship25", None)
                if opp_val == self:
                    setattr(old_value, "forms_Relationship25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Relationship25"):
                opp_val = getattr(value, "forms_Relationship25", None)
                setattr(value, "forms_Relationship25", self)

    @property
    def Relationship(self):
        return self.__Relationship

    @Relationship.setter
    def Relationship(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Relationship__Relationship", None)
        self.__Relationship = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def forms_Relationship48(self):
        return self.__forms_Relationship48

    @forms_Relationship48.setter
    def forms_Relationship48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Relationship__forms_Relationship48", None)
        self.__forms_Relationship48 = value
        
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
    def forms_Relationship(self):
        return self.__forms_Relationship

    @forms_Relationship.setter
    def forms_Relationship(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Relationship__forms_Relationship", None)
        self.__forms_Relationship = value
        
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

class forms_Entity:

    def __init__(self, name: str, forms_Entity: "forms_EntityModel" = None, forms_Entity8: set["forms_Entity"] = None, entity: set["forms_Attribute"] = None, source: set["forms_Relationship"] = None, forms_Entity4: "forms_Attribute" = None, forms_Entity7: "forms_Entity" = None, forms_Entity5: "forms_Entity" = None, forms_Entity10: "forms_Entity" = None, Entity: "forms_Attribute" = None, forms_Entity35: "forms_Form" = None, Entity20: "forms_Relationship" = None, forms_Entity22: "forms_Relationship" = None):
        self.name = name
        self.forms_Entity = forms_Entity
        self.forms_Entity8 = forms_Entity8 if forms_Entity8 is not None else set()
        self.entity = entity if entity is not None else set()
        self.source = source if source is not None else set()
        self.forms_Entity4 = forms_Entity4
        self.forms_Entity7 = forms_Entity7
        self.forms_Entity5 = forms_Entity5
        self.forms_Entity10 = forms_Entity10
        self.Entity = Entity
        self.forms_Entity35 = forms_Entity35
        self.Entity20 = Entity20
        self.forms_Entity22 = forms_Entity22
        
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
        self.__forms_Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_EntityModel"):
                opp_val = getattr(old_value, "forms_EntityModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_EntityModel"):
                opp_val = getattr(value, "forms_EntityModel", None)
                if opp_val is None:
                    setattr(value, "forms_EntityModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def forms_Entity8(self):
        return self.__forms_Entity8

    @forms_Entity8.setter
    def forms_Entity8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Entity__forms_Entity8", None)
        self.__forms_Entity8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "forms_Entity10"):
                    opp_val = getattr(item, "forms_Entity10", None)
                    
                    if opp_val == self:
                        setattr(item, "forms_Entity10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "forms_Entity10"):
                    opp_val = getattr(item, "forms_Entity10", None)
                    
                    setattr(item, "forms_Entity10", self)
                    

    @property
    def forms_Entity35(self):
        return self.__forms_Entity35

    @forms_Entity35.setter
    def forms_Entity35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Entity__forms_Entity35", None)
        self.__forms_Entity35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Form34"):
                opp_val = getattr(old_value, "forms_Form34", None)
                if opp_val == self:
                    setattr(old_value, "forms_Form34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Form34"):
                opp_val = getattr(value, "forms_Form34", None)
                setattr(value, "forms_Form34", self)

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
            if hasattr(old_value, "forms_Relationship"):
                opp_val = getattr(old_value, "forms_Relationship", None)
                if opp_val == self:
                    setattr(old_value, "forms_Relationship", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Relationship"):
                opp_val = getattr(value, "forms_Relationship", None)
                setattr(value, "forms_Relationship", self)

    @property
    def Entity(self):
        return self.__Entity

    @Entity.setter
    def Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Entity__Entity", None)
        self.__Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attributes"):
                opp_val = getattr(old_value, "attributes", None)
                if opp_val == self:
                    setattr(old_value, "attributes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attributes"):
                opp_val = getattr(value, "attributes", None)
                setattr(value, "attributes", self)

    @property
    def entity(self):
        return self.__entity

    @entity.setter
    def entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Entity__entity", None)
        self.__entity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Attribute"):
                    opp_val = getattr(item, "Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Attribute"):
                    opp_val = getattr(item, "Attribute", None)
                    
                    setattr(item, "Attribute", self)
                    

    @property
    def forms_Entity4(self):
        return self.__forms_Entity4

    @forms_Entity4.setter
    def forms_Entity4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Entity__forms_Entity4", None)
        self.__forms_Entity4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forms_Attribute"):
                opp_val = getattr(old_value, "forms_Attribute", None)
                if opp_val == self:
                    setattr(old_value, "forms_Attribute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Attribute"):
                opp_val = getattr(value, "forms_Attribute", None)
                setattr(value, "forms_Attribute", self)

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
            if hasattr(old_value, "forms_Entity8"):
                opp_val = getattr(old_value, "forms_Entity8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Entity8"):
                opp_val = getattr(value, "forms_Entity8", None)
                if opp_val is None:
                    setattr(value, "forms_Entity8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "forms_Entity7"):
                opp_val = getattr(old_value, "forms_Entity7", None)
                if opp_val == self:
                    setattr(old_value, "forms_Entity7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forms_Entity7"):
                opp_val = getattr(value, "forms_Entity7", None)
                setattr(value, "forms_Entity7", self)

    @property
    def forms_Entity7(self):
        return self.__forms_Entity7

    @forms_Entity7.setter
    def forms_Entity7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Entity__forms_Entity7", None)
        self.__forms_Entity7 = value
        
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
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Entity__source", None)
        self.__source = value if value is not None else set()
        
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
                    

    @property
    def Entity20(self):
        return self.__Entity20

    @Entity20.setter
    def Entity20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_forms_Entity__Entity20", None)
        self.__Entity20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "relationships"):
                opp_val = getattr(old_value, "relationships", None)
                if opp_val == self:
                    setattr(old_value, "relationships", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "relationships"):
                opp_val = getattr(value, "relationships", None)
                setattr(value, "relationships", self)

class forms_EntityModel:

    pass