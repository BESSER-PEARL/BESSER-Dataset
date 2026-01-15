from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class GraphType(Enum):
    BAR = "BAR"
    PIE = "PIE"
    SCALAR = "SCALAR"
    NONE = "NONE"
class InputType(Enum):
    TEXT = "TEXT"
    NUMBER = "NUMBER"
    DATE = "DATE"
    EMAIL = "EMAIL"
    RANGE = "RANGE"
class SelectType(Enum):
    LIST = "LIST"
    COMBO = "COMBO"


############################################
# Definition of Classes
############################################

class html_Container:

    def __init__(self, name: str, html_Container: set["html_Page"] = None):
        self.name = name
        self.html_Container = html_Container if html_Container is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def html_Container(self):
        return self.__html_Container

    @html_Container.setter
    def html_Container(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_html_Container__html_Container", None)
        self.__html_Container = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "html_Page"):
                    opp_val = getattr(item, "html_Page", None)
                    
                    if opp_val == self:
                        setattr(item, "html_Page", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "html_Page"):
                    opp_val = getattr(item, "html_Page", None)
                    
                    setattr(item, "html_Page", self)
                    

class html_ColumnOption:

    def __init__(self, content: str, value: int, html_ColumnOption: "html_SelectComplex" = None):
        self.content = content
        self.value = value
        self.html_ColumnOption = html_ColumnOption
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def html_ColumnOption(self):
        return self.__html_ColumnOption

    @html_ColumnOption.setter
    def html_ColumnOption(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_html_ColumnOption__html_ColumnOption", None)
        self.__html_ColumnOption = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "html_SelectComplex"):
                opp_val = getattr(old_value, "html_SelectComplex", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "html_SelectComplex"):
                opp_val = getattr(value, "html_SelectComplex", None)
                if opp_val is None:
                    setattr(value, "html_SelectComplex", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class html_Page:

    def __init__(self, title: str, urlToSaveResponses: str, urlToGetData: str, urlToGetRelationResult: str, description: str, id: int, html_Page: "html_Container" = None, html_Page18: set["html_View"] = None):
        self.title = title
        self.urlToSaveResponses = urlToSaveResponses
        self.urlToGetData = urlToGetData
        self.urlToGetRelationResult = urlToGetRelationResult
        self.description = description
        self.id = id
        self.html_Page = html_Page
        self.html_Page18 = html_Page18 if html_Page18 is not None else set()
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

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
    def urlToSaveResponses(self) -> str:
        return self.__urlToSaveResponses

    @urlToSaveResponses.setter
    def urlToSaveResponses(self, urlToSaveResponses: str):
        self.__urlToSaveResponses = urlToSaveResponses

    @property
    def urlToGetRelationResult(self) -> str:
        return self.__urlToGetRelationResult

    @urlToGetRelationResult.setter
    def urlToGetRelationResult(self, urlToGetRelationResult: str):
        self.__urlToGetRelationResult = urlToGetRelationResult

    @property
    def urlToGetData(self) -> str:
        return self.__urlToGetData

    @urlToGetData.setter
    def urlToGetData(self, urlToGetData: str):
        self.__urlToGetData = urlToGetData

    @property
    def html_Page(self):
        return self.__html_Page

    @html_Page.setter
    def html_Page(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_html_Page__html_Page", None)
        self.__html_Page = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "html_Container"):
                opp_val = getattr(old_value, "html_Container", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "html_Container"):
                opp_val = getattr(value, "html_Container", None)
                if opp_val is None:
                    setattr(value, "html_Container", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def html_Page18(self):
        return self.__html_Page18

    @html_Page18.setter
    def html_Page18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_html_Page__html_Page18", None)
        self.__html_Page18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "html_View19"):
                    opp_val = getattr(item, "html_View19", None)
                    
                    if opp_val == self:
                        setattr(item, "html_View19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "html_View19"):
                    opp_val = getattr(item, "html_View19", None)
                    
                    setattr(item, "html_View19", self)
                    

class html_FormElement(ABC):

    def __init__(self, id: str, visible: bool, html_FormElement: "html_Section" = None, html_FormElement11: "html_Option" = None):
        self.id = id
        self.visible = visible
        self.html_FormElement = html_FormElement
        self.html_FormElement11 = html_FormElement11
        
    @property
    def visible(self) -> bool:
        return self.__visible

    @visible.setter
    def visible(self, visible: bool):
        self.__visible = visible

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def html_FormElement(self):
        return self.__html_FormElement

    @html_FormElement.setter
    def html_FormElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_html_FormElement__html_FormElement", None)
        self.__html_FormElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "html_Section4"):
                opp_val = getattr(old_value, "html_Section4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "html_Section4"):
                opp_val = getattr(value, "html_Section4", None)
                if opp_val is None:
                    setattr(value, "html_Section4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def html_FormElement11(self):
        return self.__html_FormElement11

    @html_FormElement11.setter
    def html_FormElement11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_html_FormElement__html_FormElement11", None)
        self.__html_FormElement11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "html_Option10"):
                opp_val = getattr(old_value, "html_Option10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "html_Option10"):
                opp_val = getattr(value, "html_Option10", None)
                if opp_val is None:
                    setattr(value, "html_Option10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class html_Section:

    def __init__(self, title: str, id: int, html_Section: "html_View" = None, html_Section4: set["html_FormElement"] = None):
        self.title = title
        self.id = id
        self.html_Section = html_Section
        self.html_Section4 = html_Section4 if html_Section4 is not None else set()
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def html_Section(self):
        return self.__html_Section

    @html_Section.setter
    def html_Section(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_html_Section__html_Section", None)
        self.__html_Section = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "html_View2"):
                opp_val = getattr(old_value, "html_View2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "html_View2"):
                opp_val = getattr(value, "html_View2", None)
                if opp_val is None:
                    setattr(value, "html_View2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def html_Section4(self):
        return self.__html_Section4

    @html_Section4.setter
    def html_Section4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_html_Section__html_Section4", None)
        self.__html_Section4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "html_FormElement"):
                    opp_val = getattr(item, "html_FormElement", None)
                    
                    if opp_val == self:
                        setattr(item, "html_FormElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "html_FormElement"):
                    opp_val = getattr(item, "html_FormElement", None)
                    
                    setattr(item, "html_FormElement", self)
                    

class html_Graph:

    def __init__(self, type: str, title: str, html_Graph: "html_View" = None):
        self.type = type
        self.title = title
        self.html_Graph = html_Graph
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def html_Graph(self):
        return self.__html_Graph

    @html_Graph.setter
    def html_Graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_html_Graph__html_Graph", None)
        self.__html_Graph = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "html_View"):
                opp_val = getattr(old_value, "html_View", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "html_View"):
                opp_val = getattr(value, "html_View", None)
                if opp_val is None:
                    setattr(value, "html_View", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class html_Option:

    def __init__(self, content: str, value: int, html_Option: "html_Select" = None, html_Option8: "html_TextArea" = None, html_Option10: set["html_FormElement"] = None, html_Option15: "html_SelectComplex" = None):
        self.content = content
        self.value = value
        self.html_Option = html_Option
        self.html_Option8 = html_Option8
        self.html_Option10 = html_Option10 if html_Option10 is not None else set()
        self.html_Option15 = html_Option15
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def html_Option(self):
        return self.__html_Option

    @html_Option.setter
    def html_Option(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_html_Option__html_Option", None)
        self.__html_Option = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "html_Select"):
                opp_val = getattr(old_value, "html_Select", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "html_Select"):
                opp_val = getattr(value, "html_Select", None)
                if opp_val is None:
                    setattr(value, "html_Select", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def html_Option15(self):
        return self.__html_Option15

    @html_Option15.setter
    def html_Option15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_html_Option__html_Option15", None)
        self.__html_Option15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "html_SelectComplex14"):
                opp_val = getattr(old_value, "html_SelectComplex14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "html_SelectComplex14"):
                opp_val = getattr(value, "html_SelectComplex14", None)
                if opp_val is None:
                    setattr(value, "html_SelectComplex14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def html_Option10(self):
        return self.__html_Option10

    @html_Option10.setter
    def html_Option10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_html_Option__html_Option10", None)
        self.__html_Option10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "html_FormElement11"):
                    opp_val = getattr(item, "html_FormElement11", None)
                    
                    if opp_val == self:
                        setattr(item, "html_FormElement11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "html_FormElement11"):
                    opp_val = getattr(item, "html_FormElement11", None)
                    
                    setattr(item, "html_FormElement11", self)
                    

    @property
    def html_Option8(self):
        return self.__html_Option8

    @html_Option8.setter
    def html_Option8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_html_Option__html_Option8", None)
        self.__html_Option8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "html_TextArea"):
                opp_val = getattr(old_value, "html_TextArea", None)
                if opp_val == self:
                    setattr(old_value, "html_TextArea", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "html_TextArea"):
                opp_val = getattr(value, "html_TextArea", None)
                setattr(value, "html_TextArea", self)

class SelectionList:

    pass
class html_SelectComplex(SelectionList):

    pass
class html_Select(SelectionList):

    def __init__(self, type: str, html_Select: set["html_Option"] = None):
        self.type = type
        self.html_Select = html_Select if html_Select is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def html_Select(self):
        return self.__html_Select

    @html_Select.setter
    def html_Select(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_html_Select__html_Select", None)
        self.__html_Select = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "html_Option"):
                    opp_val = getattr(item, "html_Option", None)
                    
                    if opp_val == self:
                        setattr(item, "html_Option", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "html_Option"):
                    opp_val = getattr(item, "html_Option", None)
                    
                    setattr(item, "html_Option", self)
                    

class Editable:

    pass
class html_TextArea(Editable):

    def __init__(self, rows: int, maxLength: int, html_TextArea: "html_Option" = None):
        self.rows = rows
        self.maxLength = maxLength
        self.html_TextArea = html_TextArea
        
    @property
    def maxLength(self) -> int:
        return self.__maxLength

    @maxLength.setter
    def maxLength(self, maxLength: int):
        self.__maxLength = maxLength

    @property
    def rows(self) -> int:
        return self.__rows

    @rows.setter
    def rows(self, rows: int):
        self.__rows = rows

    @property
    def html_TextArea(self):
        return self.__html_TextArea

    @html_TextArea.setter
    def html_TextArea(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_html_TextArea__html_TextArea", None)
        self.__html_TextArea = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "html_Option8"):
                opp_val = getattr(old_value, "html_Option8", None)
                if opp_val == self:
                    setattr(old_value, "html_Option8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "html_Option8"):
                opp_val = getattr(value, "html_Option8", None)
                setattr(value, "html_Option8", self)

class html_SelectionList(Editable):

    def __init__(self, multiple: bool):
        self.multiple = multiple
        
    @property
    def multiple(self) -> bool:
        return self.__multiple

    @multiple.setter
    def multiple(self, multiple: bool):
        self.__multiple = multiple

class html_Input(Editable):

    def __init__(self, checked: bool, type: str, min: int, max: int, step: int, maxLength: int):
        self.checked = checked
        self.type = type
        self.min = min
        self.max = max
        self.step = step
        self.maxLength = maxLength
        
    @property
    def maxLength(self) -> int:
        return self.__maxLength

    @maxLength.setter
    def maxLength(self, maxLength: int):
        self.__maxLength = maxLength

    @property
    def checked(self) -> bool:
        return self.__checked

    @checked.setter
    def checked(self, checked: bool):
        self.__checked = checked

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def min(self) -> int:
        return self.__min

    @min.setter
    def min(self, min: int):
        self.__min = min

    @property
    def max(self) -> int:
        return self.__max

    @max.setter
    def max(self, max: int):
        self.__max = max

    @property
    def step(self) -> int:
        return self.__step

    @step.setter
    def step(self, step: int):
        self.__step = step

class FormElement:

    pass
class html_Editable(FormElement):

    def __init__(self, name: int, required: bool, html_Editable: "html_Label" = None):
        self.name = name
        self.required = required
        self.html_Editable = html_Editable
        
    @property
    def name(self) -> int:
        return self.__name

    @name.setter
    def name(self, name: int):
        self.__name = name

    @property
    def required(self) -> bool:
        return self.__required

    @required.setter
    def required(self, required: bool):
        self.__required = required

    @property
    def html_Editable(self):
        return self.__html_Editable

    @html_Editable.setter
    def html_Editable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_html_Editable__html_Editable", None)
        self.__html_Editable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "html_Label"):
                opp_val = getattr(old_value, "html_Label", None)
                if opp_val == self:
                    setattr(old_value, "html_Label", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "html_Label"):
                opp_val = getattr(value, "html_Label", None)
                setattr(value, "html_Label", self)

class html_Label(FormElement):

    def __init__(self, content: str, forText: int, html_Label: "html_Editable" = None):
        self.content = content
        self.forText = forText
        self.html_Label = html_Label
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def forText(self) -> int:
        return self.__forText

    @forText.setter
    def forText(self, forText: int):
        self.__forText = forText

    @property
    def html_Label(self):
        return self.__html_Label

    @html_Label.setter
    def html_Label(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_html_Label__html_Label", None)
        self.__html_Label = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "html_Editable"):
                opp_val = getattr(old_value, "html_Editable", None)
                if opp_val == self:
                    setattr(old_value, "html_Editable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "html_Editable"):
                opp_val = getattr(value, "html_Editable", None)
                setattr(value, "html_Editable", self)

class html_View:

    def __init__(self, title: str, html_View: set["html_Graph"] = None, html_View2: set["html_Section"] = None, html_View19: "html_Page" = None):
        self.title = title
        self.html_View = html_View if html_View is not None else set()
        self.html_View2 = html_View2 if html_View2 is not None else set()
        self.html_View19 = html_View19
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def html_View2(self):
        return self.__html_View2

    @html_View2.setter
    def html_View2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_html_View__html_View2", None)
        self.__html_View2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "html_Section"):
                    opp_val = getattr(item, "html_Section", None)
                    
                    if opp_val == self:
                        setattr(item, "html_Section", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "html_Section"):
                    opp_val = getattr(item, "html_Section", None)
                    
                    setattr(item, "html_Section", self)
                    

    @property
    def html_View19(self):
        return self.__html_View19

    @html_View19.setter
    def html_View19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_html_View__html_View19", None)
        self.__html_View19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "html_Page18"):
                opp_val = getattr(old_value, "html_Page18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "html_Page18"):
                opp_val = getattr(value, "html_Page18", None)
                if opp_val is None:
                    setattr(value, "html_Page18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def html_View(self):
        return self.__html_View

    @html_View.setter
    def html_View(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_html_View__html_View", None)
        self.__html_View = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "html_Graph"):
                    opp_val = getattr(item, "html_Graph", None)
                    
                    if opp_val == self:
                        setattr(item, "html_Graph", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "html_Graph"):
                    opp_val = getattr(item, "html_Graph", None)
                    
                    setattr(item, "html_Graph", self)
                    
