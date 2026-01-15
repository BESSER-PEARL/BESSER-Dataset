from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class SelectionType(Enum):
    RADIO = "RADIO"
    CHECKBOX = "CHECKBOX"
    COMBOBOX = "COMBOBOX"
class TextInputType(Enum):
    TEXTAREA = "TEXTAREA"
    TEXTFIELD = "TEXTFIELD"
    ENCRYPTED_TEXTFIELD = "ENCRYPTED_TEXTFIELD"


############################################
# Definition of Classes
############################################

class InputElement:

    pass
class fml_SelectField(InputElement):

    def __init__(self, Label: str, Type: str, SelectField: "fml_SelectionItem" = None, contained9: set["fml_SelectionItem"] = None):
        self.Label = Label
        self.Type = Type
        self.SelectField = SelectField
        self.contained9 = contained9 if contained9 is not None else set()
        
    @property
    def Type(self) -> str:
        return self.__Type

    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def Label(self) -> str:
        return self.__Label

    @Label.setter
    def Label(self, Label: str):
        self.__Label = Label

    @property
    def SelectField(self):
        return self.__SelectField

    @SelectField.setter
    def SelectField(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fml_SelectField__SelectField", None)
        self.__SelectField = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "consists12"):
                opp_val = getattr(old_value, "consists12", None)
                if opp_val == self:
                    setattr(old_value, "consists12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "consists12"):
                opp_val = getattr(value, "consists12", None)
                setattr(value, "consists12", self)

    @property
    def contained9(self):
        return self.__contained9

    @contained9.setter
    def contained9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fml_SelectField__contained9", None)
        self.__contained9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SelectionItem10"):
                    opp_val = getattr(item, "SelectionItem10", None)
                    
                    if opp_val == self:
                        setattr(item, "SelectionItem10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SelectionItem10"):
                    opp_val = getattr(item, "SelectionItem10", None)
                    
                    setattr(item, "SelectionItem10", self)
                    

class fml_TextInput(InputElement):

    def __init__(self, Label: str, Type: str, Content: str):
        self.Label = Label
        self.Type = Type
        self.Content = Content
        
    @property
    def Content(self) -> str:
        return self.__Content

    @Content.setter
    def Content(self, Content: str):
        self.__Content = Content

    @property
    def Label(self) -> str:
        return self.__Label

    @Label.setter
    def Label(self, Label: str):
        self.__Label = Label

    @property
    def Type(self) -> str:
        return self.__Type

    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

class fml_ListItem:

    def __init__(self, Text: str, fml_ListItem: "fml_List" = None):
        self.Text = Text
        self.fml_ListItem = fml_ListItem
        
    @property
    def Text(self) -> str:
        return self.__Text

    @Text.setter
    def Text(self, Text: str):
        self.__Text = Text

    @property
    def fml_ListItem(self):
        return self.__fml_ListItem

    @fml_ListItem.setter
    def fml_ListItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fml_ListItem__fml_ListItem", None)
        self.__fml_ListItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fml_List"):
                opp_val = getattr(old_value, "fml_List", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fml_List"):
                opp_val = getattr(value, "fml_List", None)
                if opp_val is None:
                    setattr(value, "fml_List", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fml_PageElement(ABC):

    def __init__(self, ID: str, consists: "fml_Page" = None, displayElementVisible: set["fml_SelectionItem"] = None, PageElement: "fml_Page" = None, PageElement14: "fml_SelectionItem" = None):
        self.ID = ID
        self.consists = consists
        self.displayElementVisible = displayElementVisible if displayElementVisible is not None else set()
        self.PageElement = PageElement
        self.PageElement14 = PageElement14
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def consists(self):
        return self.__consists

    @consists.setter
    def consists(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fml_PageElement__consists", None)
        self.__consists = value
        
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
    def displayElementVisible(self):
        return self.__displayElementVisible

    @displayElementVisible.setter
    def displayElementVisible(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fml_PageElement__displayElementVisible", None)
        self.__displayElementVisible = value if value is not None else set()
        
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
    def PageElement(self):
        return self.__PageElement

    @PageElement.setter
    def PageElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fml_PageElement__PageElement", None)
        self.__PageElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contained"):
                opp_val = getattr(old_value, "contained", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contained"):
                opp_val = getattr(value, "contained", None)
                if opp_val is None:
                    setattr(value, "contained", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PageElement14(self):
        return self.__PageElement14

    @PageElement14.setter
    def PageElement14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fml_PageElement__PageElement14", None)
        self.__PageElement14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "visibleIfSelected"):
                opp_val = getattr(old_value, "visibleIfSelected", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "visibleIfSelected"):
                opp_val = getattr(value, "visibleIfSelected", None)
                if opp_val is None:
                    setattr(value, "visibleIfSelected", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fml_Page:

    def __init__(self, Title: str, isWelcome: bool, Page: "fml_PageElement" = None, fml_Page: "fml_Form" = None, fml_Page3: "fml_Page" = None, fml_Page1: "fml_Page" = None, contained: set["fml_PageElement"] = None):
        self.Title = Title
        self.isWelcome = isWelcome
        self.Page = Page
        self.fml_Page = fml_Page
        self.fml_Page3 = fml_Page3
        self.fml_Page1 = fml_Page1
        self.contained = contained if contained is not None else set()
        
    @property
    def Title(self) -> str:
        return self.__Title

    @Title.setter
    def Title(self, Title: str):
        self.__Title = Title

    @property
    def isWelcome(self) -> bool:
        return self.__isWelcome

    @isWelcome.setter
    def isWelcome(self, isWelcome: bool):
        self.__isWelcome = isWelcome

    @property
    def contained(self):
        return self.__contained

    @contained.setter
    def contained(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fml_Page__contained", None)
        self.__contained = value if value is not None else set()
        
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
    def fml_Page(self):
        return self.__fml_Page

    @fml_Page.setter
    def fml_Page(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fml_Page__fml_Page", None)
        self.__fml_Page = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fml_Form"):
                opp_val = getattr(old_value, "fml_Form", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fml_Form"):
                opp_val = getattr(value, "fml_Form", None)
                if opp_val is None:
                    setattr(value, "fml_Form", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fml_Page1(self):
        return self.__fml_Page1

    @fml_Page1.setter
    def fml_Page1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fml_Page__fml_Page1", None)
        self.__fml_Page1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fml_Page3"):
                opp_val = getattr(old_value, "fml_Page3", None)
                if opp_val == self:
                    setattr(old_value, "fml_Page3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fml_Page3"):
                opp_val = getattr(value, "fml_Page3", None)
                setattr(value, "fml_Page3", self)

    @property
    def Page(self):
        return self.__Page

    @Page.setter
    def Page(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fml_Page__Page", None)
        self.__Page = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "consists"):
                opp_val = getattr(old_value, "consists", None)
                if opp_val == self:
                    setattr(old_value, "consists", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "consists"):
                opp_val = getattr(value, "consists", None)
                setattr(value, "consists", self)

    @property
    def fml_Page3(self):
        return self.__fml_Page3

    @fml_Page3.setter
    def fml_Page3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fml_Page__fml_Page3", None)
        self.__fml_Page3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fml_Page1"):
                opp_val = getattr(old_value, "fml_Page1", None)
                if opp_val == self:
                    setattr(old_value, "fml_Page1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fml_Page1"):
                opp_val = getattr(value, "fml_Page1", None)
                setattr(value, "fml_Page1", self)

class fml_Form:

    pass
class DisplayElement:

    pass
class fml_TextParagraph(DisplayElement):

    def __init__(self, Text: str):
        self.Text = Text
        
    @property
    def Text(self) -> str:
        return self.__Text

    @Text.setter
    def Text(self, Text: str):
        self.__Text = Text

class fml_List(DisplayElement):

    def __init__(self, isOrdered: bool, fml_List: set["fml_ListItem"] = None):
        self.isOrdered = isOrdered
        self.fml_List = fml_List if fml_List is not None else set()
        
    @property
    def isOrdered(self) -> bool:
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: bool):
        self.__isOrdered = isOrdered

    @property
    def fml_List(self):
        return self.__fml_List

    @fml_List.setter
    def fml_List(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fml_List__fml_List", None)
        self.__fml_List = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fml_ListItem"):
                    opp_val = getattr(item, "fml_ListItem", None)
                    
                    if opp_val == self:
                        setattr(item, "fml_ListItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fml_ListItem"):
                    opp_val = getattr(item, "fml_ListItem", None)
                    
                    setattr(item, "fml_ListItem", self)
                    

class fml_Heading(DisplayElement):

    def __init__(self, Level: str, Text: str):
        self.Level = Level
        self.Text = Text
        
    @property
    def Level(self) -> str:
        return self.__Level

    @Level.setter
    def Level(self, Level: str):
        self.__Level = Level

    @property
    def Text(self) -> str:
        return self.__Text

    @Text.setter
    def Text(self, Text: str):
        self.__Text = Text

class PageElement:

    pass
class fml_InputElement(PageElement):

    def __init__(self, isMandatory: bool):
        self.isMandatory = isMandatory
        
    @property
    def isMandatory(self) -> bool:
        return self.__isMandatory

    @isMandatory.setter
    def isMandatory(self, isMandatory: bool):
        self.__isMandatory = isMandatory

class fml_DisplayElement(PageElement):

    pass
class fml_SelectionItem:

    def __init__(self, Text: str, preselected: bool, selected: bool, SelectionItem: "fml_PageElement" = None, consists12: "fml_SelectField" = None, visibleIfSelected: set["fml_PageElement"] = None, SelectionItem10: "fml_SelectField" = None):
        self.Text = Text
        self.preselected = preselected
        self.selected = selected
        self.SelectionItem = SelectionItem
        self.consists12 = consists12
        self.visibleIfSelected = visibleIfSelected if visibleIfSelected is not None else set()
        self.SelectionItem10 = SelectionItem10
        
    @property
    def Text(self) -> str:
        return self.__Text

    @Text.setter
    def Text(self, Text: str):
        self.__Text = Text

    @property
    def selected(self) -> bool:
        return self.__selected

    @selected.setter
    def selected(self, selected: bool):
        self.__selected = selected

    @property
    def preselected(self) -> bool:
        return self.__preselected

    @preselected.setter
    def preselected(self, preselected: bool):
        self.__preselected = preselected

    @property
    def visibleIfSelected(self):
        return self.__visibleIfSelected

    @visibleIfSelected.setter
    def visibleIfSelected(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fml_SelectionItem__visibleIfSelected", None)
        self.__visibleIfSelected = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PageElement14"):
                    opp_val = getattr(item, "PageElement14", None)
                    
                    if opp_val == self:
                        setattr(item, "PageElement14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PageElement14"):
                    opp_val = getattr(item, "PageElement14", None)
                    
                    setattr(item, "PageElement14", self)
                    

    @property
    def SelectionItem(self):
        return self.__SelectionItem

    @SelectionItem.setter
    def SelectionItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fml_SelectionItem__SelectionItem", None)
        self.__SelectionItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "displayElementVisible"):
                opp_val = getattr(old_value, "displayElementVisible", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "displayElementVisible"):
                opp_val = getattr(value, "displayElementVisible", None)
                if opp_val is None:
                    setattr(value, "displayElementVisible", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def consists12(self):
        return self.__consists12

    @consists12.setter
    def consists12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fml_SelectionItem__consists12", None)
        self.__consists12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SelectField"):
                opp_val = getattr(old_value, "SelectField", None)
                if opp_val == self:
                    setattr(old_value, "SelectField", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SelectField"):
                opp_val = getattr(value, "SelectField", None)
                setattr(value, "SelectField", self)

    @property
    def SelectionItem10(self):
        return self.__SelectionItem10

    @SelectionItem10.setter
    def SelectionItem10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fml_SelectionItem__SelectionItem10", None)
        self.__SelectionItem10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contained9"):
                opp_val = getattr(old_value, "contained9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contained9"):
                opp_val = getattr(value, "contained9", None)
                if opp_val is None:
                    setattr(value, "contained9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
