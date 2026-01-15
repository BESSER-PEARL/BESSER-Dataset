from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class SelectionFieldType(Enum):
    Radio = "Radio"
    Checkbox = "Checkbox"
    Combobox = "Combobox"


############################################
# Definition of Classes
############################################

class form_SelectionItem:

    def __init__(self, label: str, selected: bool, form_SelectionItem: "form_SelectionCondition" = None, SelectionItem: "form_SelectionField" = None, items: "form_SelectionField" = None):
        self.label = label
        self.selected = selected
        self.form_SelectionItem = form_SelectionItem
        self.SelectionItem = SelectionItem
        self.items = items
        
    @property
    def selected(self) -> bool:
        return self.__selected

    @selected.setter
    def selected(self, selected: bool):
        self.__selected = selected

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def SelectionItem(self):
        return self.__SelectionItem

    @SelectionItem.setter
    def SelectionItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_SelectionItem__SelectionItem", None)
        self.__SelectionItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "field"):
                opp_val = getattr(old_value, "field", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "field"):
                opp_val = getattr(value, "field", None)
                if opp_val is None:
                    setattr(value, "field", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_SelectionItem__items", None)
        self.__items = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SelectionField"):
                opp_val = getattr(old_value, "SelectionField", None)
                if opp_val == self:
                    setattr(old_value, "SelectionField", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SelectionField"):
                opp_val = getattr(value, "SelectionField", None)
                setattr(value, "SelectionField", self)

    @property
    def form_SelectionItem(self):
        return self.__form_SelectionItem

    @form_SelectionItem.setter
    def form_SelectionItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_SelectionItem__form_SelectionItem", None)
        self.__form_SelectionItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_SelectionCondition"):
                opp_val = getattr(old_value, "form_SelectionCondition", None)
                if opp_val == self:
                    setattr(old_value, "form_SelectionCondition", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_SelectionCondition"):
                opp_val = getattr(value, "form_SelectionCondition", None)
                setattr(value, "form_SelectionCondition", self)

class InputField:

    pass
class form_SelectionField(InputField):

    def __init__(self, selectionFieldType: str, field: set["form_SelectionItem"] = None, SelectionField: "form_SelectionItem" = None):
        self.selectionFieldType = selectionFieldType
        self.field = field if field is not None else set()
        self.SelectionField = SelectionField
        
    @property
    def selectionFieldType(self) -> str:
        return self.__selectionFieldType

    @selectionFieldType.setter
    def selectionFieldType(self, selectionFieldType: str):
        self.__selectionFieldType = selectionFieldType

    @property
    def field(self):
        return self.__field

    @field.setter
    def field(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_SelectionField__field", None)
        self.__field = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SelectionItem"):
                    opp_val = getattr(item, "SelectionItem", None)
                    
                    if opp_val == self:
                        setattr(item, "SelectionItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SelectionItem"):
                    opp_val = getattr(item, "SelectionItem", None)
                    
                    setattr(item, "SelectionItem", self)
                    

    @property
    def SelectionField(self):
        return self.__SelectionField

    @SelectionField.setter
    def SelectionField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_SelectionField__SelectionField", None)
        self.__SelectionField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "items"):
                opp_val = getattr(old_value, "items", None)
                if opp_val == self:
                    setattr(old_value, "items", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "items"):
                opp_val = getattr(value, "items", None)
                setattr(value, "items", self)

class form_TextArea(InputField):

    pass
class form_TextField(InputField):

    def __init__(self, encrypted: bool):
        self.encrypted = encrypted
        
    @property
    def encrypted(self) -> bool:
        return self.__encrypted

    @encrypted.setter
    def encrypted(self, encrypted: bool):
        self.__encrypted = encrypted

class VisibilityCondition:

    pass
class form_SelectionCondition(VisibilityCondition):

    pass
class form_ListItem:

    def __init__(self, label: str, form_ListItem: "form_List" = None):
        self.label = label
        self.form_ListItem = form_ListItem
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def form_ListItem(self):
        return self.__form_ListItem

    @form_ListItem.setter
    def form_ListItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_ListItem__form_ListItem", None)
        self.__form_ListItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_List"):
                opp_val = getattr(old_value, "form_List", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_List"):
                opp_val = getattr(value, "form_List", None)
                if opp_val is None:
                    setattr(value, "form_List", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Text:

    pass
class form_Paragraph(Text):

    pass
class form_Heading(Text):

    def __init__(self, level: int):
        self.level = level
        
    @property
    def level(self) -> int:
        return self.__level

    @level.setter
    def level(self, level: int):
        self.__level = level

class form_Page:

    def __init__(self, title: str, form_Page6: "form_Page" = None, form_Page4: set["form_Page"] = None, form_Page9: "form_Page" = None, form_Page7: set["form_Page"] = None, Page: "form_Page" = None, previousPage: "form_Page" = None, page: set["form_PageElement"] = None, Page15: "form_Page" = None, nextPage: "form_Page" = None, page17: set["form_VisibilityCondition"] = None, Page19: "form_PageElement" = None, form_Page: "form_Form" = None, form_Page3: "form_Form" = None, Page24: "form_VisibilityCondition" = None):
        self.title = title
        self.form_Page6 = form_Page6
        self.form_Page4 = form_Page4 if form_Page4 is not None else set()
        self.form_Page9 = form_Page9
        self.form_Page7 = form_Page7 if form_Page7 is not None else set()
        self.Page = Page
        self.previousPage = previousPage
        self.page = page if page is not None else set()
        self.Page15 = Page15
        self.nextPage = nextPage
        self.page17 = page17 if page17 is not None else set()
        self.Page19 = Page19
        self.form_Page = form_Page
        self.form_Page3 = form_Page3
        self.Page24 = Page24
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def form_Page7(self):
        return self.__form_Page7

    @form_Page7.setter
    def form_Page7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Page__form_Page7", None)
        self.__form_Page7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "form_Page9"):
                    opp_val = getattr(item, "form_Page9", None)
                    
                    if opp_val == self:
                        setattr(item, "form_Page9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "form_Page9"):
                    opp_val = getattr(item, "form_Page9", None)
                    
                    setattr(item, "form_Page9", self)
                    

    @property
    def Page19(self):
        return self.__Page19

    @Page19.setter
    def Page19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Page__Page19", None)
        self.__Page19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "elements"):
                opp_val = getattr(old_value, "elements", None)
                if opp_val == self:
                    setattr(old_value, "elements", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "elements"):
                opp_val = getattr(value, "elements", None)
                setattr(value, "elements", self)

    @property
    def form_Page3(self):
        return self.__form_Page3

    @form_Page3.setter
    def form_Page3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Page__form_Page3", None)
        self.__form_Page3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Form2"):
                opp_val = getattr(old_value, "form_Form2", None)
                if opp_val == self:
                    setattr(old_value, "form_Form2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Form2"):
                opp_val = getattr(value, "form_Form2", None)
                setattr(value, "form_Form2", self)

    @property
    def Page(self):
        return self.__Page

    @Page.setter
    def Page(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Page__Page", None)
        self.__Page = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "previousPage"):
                opp_val = getattr(old_value, "previousPage", None)
                if opp_val == self:
                    setattr(old_value, "previousPage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "previousPage"):
                opp_val = getattr(value, "previousPage", None)
                setattr(value, "previousPage", self)

    @property
    def page17(self):
        return self.__page17

    @page17.setter
    def page17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Page__page17", None)
        self.__page17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VisibilityCondition"):
                    opp_val = getattr(item, "VisibilityCondition", None)
                    
                    if opp_val == self:
                        setattr(item, "VisibilityCondition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VisibilityCondition"):
                    opp_val = getattr(item, "VisibilityCondition", None)
                    
                    setattr(item, "VisibilityCondition", self)
                    

    @property
    def previousPage(self):
        return self.__previousPage

    @previousPage.setter
    def previousPage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Page__previousPage", None)
        self.__previousPage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Page"):
                opp_val = getattr(old_value, "Page", None)
                if opp_val == self:
                    setattr(old_value, "Page", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Page"):
                opp_val = getattr(value, "Page", None)
                setattr(value, "Page", self)

    @property
    def form_Page4(self):
        return self.__form_Page4

    @form_Page4.setter
    def form_Page4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Page__form_Page4", None)
        self.__form_Page4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "form_Page6"):
                    opp_val = getattr(item, "form_Page6", None)
                    
                    if opp_val == self:
                        setattr(item, "form_Page6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "form_Page6"):
                    opp_val = getattr(item, "form_Page6", None)
                    
                    setattr(item, "form_Page6", self)
                    

    @property
    def Page15(self):
        return self.__Page15

    @Page15.setter
    def Page15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Page__Page15", None)
        self.__Page15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nextPage"):
                opp_val = getattr(old_value, "nextPage", None)
                if opp_val == self:
                    setattr(old_value, "nextPage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nextPage"):
                opp_val = getattr(value, "nextPage", None)
                setattr(value, "nextPage", self)

    @property
    def form_Page(self):
        return self.__form_Page

    @form_Page.setter
    def form_Page(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Page__form_Page", None)
        self.__form_Page = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Form"):
                opp_val = getattr(old_value, "form_Form", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Form"):
                opp_val = getattr(value, "form_Form", None)
                if opp_val is None:
                    setattr(value, "form_Form", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def form_Page6(self):
        return self.__form_Page6

    @form_Page6.setter
    def form_Page6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Page__form_Page6", None)
        self.__form_Page6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Page4"):
                opp_val = getattr(old_value, "form_Page4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Page4"):
                opp_val = getattr(value, "form_Page4", None)
                if opp_val is None:
                    setattr(value, "form_Page4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def page(self):
        return self.__page

    @page.setter
    def page(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Page__page", None)
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
    def nextPage(self):
        return self.__nextPage

    @nextPage.setter
    def nextPage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Page__nextPage", None)
        self.__nextPage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Page15"):
                opp_val = getattr(old_value, "Page15", None)
                if opp_val == self:
                    setattr(old_value, "Page15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Page15"):
                opp_val = getattr(value, "Page15", None)
                setattr(value, "Page15", self)

    @property
    def Page24(self):
        return self.__Page24

    @Page24.setter
    def Page24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Page__Page24", None)
        self.__Page24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "visibilityConditions"):
                opp_val = getattr(old_value, "visibilityConditions", None)
                if opp_val == self:
                    setattr(old_value, "visibilityConditions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "visibilityConditions"):
                opp_val = getattr(value, "visibilityConditions", None)
                setattr(value, "visibilityConditions", self)

    @property
    def form_Page9(self):
        return self.__form_Page9

    @form_Page9.setter
    def form_Page9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_Page__form_Page9", None)
        self.__form_Page9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_Page7"):
                opp_val = getattr(old_value, "form_Page7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_Page7"):
                opp_val = getattr(value, "form_Page7", None)
                if opp_val is None:
                    setattr(value, "form_Page7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class form_Form:

    pass
class PageElement:

    pass
class form_Text(PageElement):

    def __init__(self, content: str):
        self.content = content
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

class form_List(PageElement):

    def __init__(self, ordered: bool, form_List: set["form_ListItem"] = None):
        self.ordered = ordered
        self.form_List = form_List if form_List is not None else set()
        
    @property
    def ordered(self) -> bool:
        return self.__ordered

    @ordered.setter
    def ordered(self, ordered: bool):
        self.__ordered = ordered

    @property
    def form_List(self):
        return self.__form_List

    @form_List.setter
    def form_List(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_List__form_List", None)
        self.__form_List = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "form_ListItem"):
                    opp_val = getattr(item, "form_ListItem", None)
                    
                    if opp_val == self:
                        setattr(item, "form_ListItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "form_ListItem"):
                    opp_val = getattr(item, "form_ListItem", None)
                    
                    setattr(item, "form_ListItem", self)
                    

class form_InputField(PageElement):

    def __init__(self, label: str, mandatory: bool):
        self.label = label
        self.mandatory = mandatory
        
    @property
    def mandatory(self) -> bool:
        return self.__mandatory

    @mandatory.setter
    def mandatory(self, mandatory: bool):
        self.__mandatory = mandatory

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

class form_VisibilityCondition(ABC):

    pass
class form_PageElement(ABC):

    def __init__(self, elementId: str, PageElement: "form_Page" = None, elements: "form_Page" = None, form_PageElement: "form_VisibilityCondition" = None):
        self.elementId = elementId
        self.PageElement = PageElement
        self.elements = elements
        self.form_PageElement = form_PageElement
        
    @property
    def elementId(self) -> str:
        return self.__elementId

    @elementId.setter
    def elementId(self, elementId: str):
        self.__elementId = elementId

    @property
    def elements(self):
        return self.__elements

    @elements.setter
    def elements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_PageElement__elements", None)
        self.__elements = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Page19"):
                opp_val = getattr(old_value, "Page19", None)
                if opp_val == self:
                    setattr(old_value, "Page19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Page19"):
                opp_val = getattr(value, "Page19", None)
                setattr(value, "Page19", self)

    @property
    def form_PageElement(self):
        return self.__form_PageElement

    @form_PageElement.setter
    def form_PageElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_PageElement__form_PageElement", None)
        self.__form_PageElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "form_VisibilityCondition"):
                opp_val = getattr(old_value, "form_VisibilityCondition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "form_VisibilityCondition"):
                opp_val = getattr(value, "form_VisibilityCondition", None)
                if opp_val is None:
                    setattr(value, "form_VisibilityCondition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PageElement(self):
        return self.__PageElement

    @PageElement.setter
    def PageElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_form_PageElement__PageElement", None)
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
