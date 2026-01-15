from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class CorrectAnwser(Enum):
    True = "True"
    False = "False"
class MySqlType(Enum):
    INT = "INT"
    REAL = "REAL"
    BOOLEAN = "BOOLEAN"
    DATE = "DATE"
    VARCHAR = "VARCHAR"
class VisualRepresentation(Enum):
    BAR_CHART = "BAR_CHART"
    LINEAL_CHART = "LINEAL_CHART"
    PIE_CHART = "PIE_CHART"
    TEXTUAL = "TEXTUAL"


############################################
# Definition of Classes
############################################

class ExternalSource:

    pass
class WebApp_RSSFeed(ExternalSource):

    def __init__(self, url: str, items_to_display: int, show_date: str, feedname: str):
        self.url = url
        self.items_to_display = items_to_display
        self.show_date = show_date
        self.feedname = feedname
        
    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def items_to_display(self) -> int:
        return self.__items_to_display

    @items_to_display.setter
    def items_to_display(self, items_to_display: int):
        self.__items_to_display = items_to_display

    @property
    def feedname(self) -> str:
        return self.__feedname

    @feedname.setter
    def feedname(self, feedname: str):
        self.__feedname = feedname

    @property
    def show_date(self) -> str:
        return self.__show_date

    @show_date.setter
    def show_date(self, show_date: str):
        self.__show_date = show_date

class WebApp_Twitter(ExternalSource):

    def __init__(self, username: str):
        self.username = username
        
    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, username: str):
        self.__username = username

class Multiple:

    pass
class WebApp_MultipleForQuestionnary(Multiple):

    pass
class WebApp_MultipleForSurvey(Multiple):

    pass
class Question:

    pass
class WebApp_GroupOfQuestions(Question):

    def __init__(self, name: str, WebApp_GroupOfQuestions: set["WebApp_Question"] = None):
        self.name = name
        self.WebApp_GroupOfQuestions = WebApp_GroupOfQuestions if WebApp_GroupOfQuestions is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def WebApp_GroupOfQuestions(self):
        return self.__WebApp_GroupOfQuestions

    @WebApp_GroupOfQuestions.setter
    def WebApp_GroupOfQuestions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WebApp_GroupOfQuestions__WebApp_GroupOfQuestions", None)
        self.__WebApp_GroupOfQuestions = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "WebApp_Question18"):
                    opp_val = getattr(item, "WebApp_Question18", None)
                    
                    if opp_val == self:
                        setattr(item, "WebApp_Question18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WebApp_Question18"):
                    opp_val = getattr(item, "WebApp_Question18", None)
                    
                    setattr(item, "WebApp_Question18", self)
                    

class TrueFalse:

    pass
class WebApp_TrueFalseForQuestionnary(TrueFalse):

    def __init__(self, correct: str):
        self.correct = correct
        
    @property
    def correct(self) -> str:
        return self.__correct

    @correct.setter
    def correct(self, correct: str):
        self.__correct = correct

class WebApp_TrueFalseForSurvey(TrueFalse):

    pass
class WebApp_SimpleQuestion(Question):

    def __init__(self, QuestionText: str, visualRep: str):
        self.QuestionText = QuestionText
        self.visualRep = visualRep
        
    @property
    def QuestionText(self) -> str:
        return self.__QuestionText

    @QuestionText.setter
    def QuestionText(self, QuestionText: str):
        self.__QuestionText = QuestionText

    @property
    def visualRep(self) -> str:
        return self.__visualRep

    @visualRep.setter
    def visualRep(self, visualRep: str):
        self.__visualRep = visualRep

class EntityWebPage:

    pass
class WebApp_Details(EntityWebPage):

    pass
class WebApp_Index(EntityWebPage):

    pass
class WebApp_ExternalLink:

    def __init__(self, url: str, WebApp_ExternalLink: "WebApp_WebPage" = None):
        self.url = url
        self.WebApp_ExternalLink = WebApp_ExternalLink
        
    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

    @property
    def WebApp_ExternalLink(self):
        return self.__WebApp_ExternalLink

    @WebApp_ExternalLink.setter
    def WebApp_ExternalLink(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WebApp_ExternalLink__WebApp_ExternalLink", None)
        self.__WebApp_ExternalLink = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WebApp_WebPage16"):
                opp_val = getattr(old_value, "WebApp_WebPage16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WebApp_WebPage16"):
                opp_val = getattr(value, "WebApp_WebPage16", None)
                if opp_val is None:
                    setattr(value, "WebApp_WebPage16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class WebApp_ExternalSource(ABC):

    pass
class WebApp_Option:

    def __init__(self, text: str, fraction: int, WebApp_Option: "WebApp_Multiple" = None, WebApp_Option29: "WebApp_MultipleForQuestionnary" = None):
        self.text = text
        self.fraction = fraction
        self.WebApp_Option = WebApp_Option
        self.WebApp_Option29 = WebApp_Option29
        
    @property
    def fraction(self) -> int:
        return self.__fraction

    @fraction.setter
    def fraction(self, fraction: int):
        self.__fraction = fraction

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def WebApp_Option(self):
        return self.__WebApp_Option

    @WebApp_Option.setter
    def WebApp_Option(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WebApp_Option__WebApp_Option", None)
        self.__WebApp_Option = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WebApp_Multiple"):
                opp_val = getattr(old_value, "WebApp_Multiple", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WebApp_Multiple"):
                opp_val = getattr(value, "WebApp_Multiple", None)
                if opp_val is None:
                    setattr(value, "WebApp_Multiple", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def WebApp_Option29(self):
        return self.__WebApp_Option29

    @WebApp_Option29.setter
    def WebApp_Option29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WebApp_Option__WebApp_Option29", None)
        self.__WebApp_Option29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WebApp_MultipleForQuestionnary"):
                opp_val = getattr(old_value, "WebApp_MultipleForQuestionnary", None)
                if opp_val == self:
                    setattr(old_value, "WebApp_MultipleForQuestionnary", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WebApp_MultipleForQuestionnary"):
                opp_val = getattr(value, "WebApp_MultipleForQuestionnary", None)
                setattr(value, "WebApp_MultipleForQuestionnary", self)

class WebApp_CRUD(EntityWebPage):

    pass
class WebApp_Delete(EntityWebPage):

    pass
class WebApp_Create(EntityWebPage):

    pass
class WebApp_Attribute:

    def __init__(self, name: str, type: str, WebApp_Attribute: "WebApp_Entity" = None):
        self.name = name
        self.type = type
        self.WebApp_Attribute = WebApp_Attribute
        
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
    def WebApp_Attribute(self):
        return self.__WebApp_Attribute

    @WebApp_Attribute.setter
    def WebApp_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WebApp_Attribute__WebApp_Attribute", None)
        self.__WebApp_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WebApp_Entity"):
                opp_val = getattr(old_value, "WebApp_Entity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WebApp_Entity"):
                opp_val = getattr(value, "WebApp_Entity", None)
                if opp_val is None:
                    setattr(value, "WebApp_Entity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class WebApp_QuestionBank:

    pass
class WebApp_DataBase:

    pass
class WebApp_WebPage(ABC):

    def __init__(self, name: str, WebApp_WebPage: "WebApp_WebApp" = None, WebApp_WebPage11: set["WebApp_ExternalSource"] = None, WebApp_WebPage14: "WebApp_WebPage" = None, WebApp_WebPage12: set["WebApp_WebPage"] = None, WebApp_WebPage16: set["WebApp_ExternalLink"] = None):
        self.name = name
        self.WebApp_WebPage = WebApp_WebPage
        self.WebApp_WebPage11 = WebApp_WebPage11 if WebApp_WebPage11 is not None else set()
        self.WebApp_WebPage14 = WebApp_WebPage14
        self.WebApp_WebPage12 = WebApp_WebPage12 if WebApp_WebPage12 is not None else set()
        self.WebApp_WebPage16 = WebApp_WebPage16 if WebApp_WebPage16 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def WebApp_WebPage(self):
        return self.__WebApp_WebPage

    @WebApp_WebPage.setter
    def WebApp_WebPage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WebApp_WebPage__WebApp_WebPage", None)
        self.__WebApp_WebPage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WebApp_WebApp"):
                opp_val = getattr(old_value, "WebApp_WebApp", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WebApp_WebApp"):
                opp_val = getattr(value, "WebApp_WebApp", None)
                if opp_val is None:
                    setattr(value, "WebApp_WebApp", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def WebApp_WebPage14(self):
        return self.__WebApp_WebPage14

    @WebApp_WebPage14.setter
    def WebApp_WebPage14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WebApp_WebPage__WebApp_WebPage14", None)
        self.__WebApp_WebPage14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WebApp_WebPage12"):
                opp_val = getattr(old_value, "WebApp_WebPage12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WebApp_WebPage12"):
                opp_val = getattr(value, "WebApp_WebPage12", None)
                if opp_val is None:
                    setattr(value, "WebApp_WebPage12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def WebApp_WebPage12(self):
        return self.__WebApp_WebPage12

    @WebApp_WebPage12.setter
    def WebApp_WebPage12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WebApp_WebPage__WebApp_WebPage12", None)
        self.__WebApp_WebPage12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "WebApp_WebPage14"):
                    opp_val = getattr(item, "WebApp_WebPage14", None)
                    
                    if opp_val == self:
                        setattr(item, "WebApp_WebPage14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WebApp_WebPage14"):
                    opp_val = getattr(item, "WebApp_WebPage14", None)
                    
                    setattr(item, "WebApp_WebPage14", self)
                    

    @property
    def WebApp_WebPage11(self):
        return self.__WebApp_WebPage11

    @WebApp_WebPage11.setter
    def WebApp_WebPage11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WebApp_WebPage__WebApp_WebPage11", None)
        self.__WebApp_WebPage11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "WebApp_ExternalSource"):
                    opp_val = getattr(item, "WebApp_ExternalSource", None)
                    
                    if opp_val == self:
                        setattr(item, "WebApp_ExternalSource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WebApp_ExternalSource"):
                    opp_val = getattr(item, "WebApp_ExternalSource", None)
                    
                    setattr(item, "WebApp_ExternalSource", self)
                    

    @property
    def WebApp_WebPage16(self):
        return self.__WebApp_WebPage16

    @WebApp_WebPage16.setter
    def WebApp_WebPage16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WebApp_WebPage__WebApp_WebPage16", None)
        self.__WebApp_WebPage16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "WebApp_ExternalLink"):
                    opp_val = getattr(item, "WebApp_ExternalLink", None)
                    
                    if opp_val == self:
                        setattr(item, "WebApp_ExternalLink", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WebApp_ExternalLink"):
                    opp_val = getattr(item, "WebApp_ExternalLink", None)
                    
                    setattr(item, "WebApp_ExternalLink", self)
                    

class WebApp_WebApp:

    def __init__(self, name: str, User: str, Password: str, WebApp_WebApp: set["WebApp_WebPage"] = None, WebApp_WebApp2: "WebApp_DataBase" = None, WebApp_WebApp4: "WebApp_QuestionBank" = None):
        self.name = name
        self.User = User
        self.Password = Password
        self.WebApp_WebApp = WebApp_WebApp if WebApp_WebApp is not None else set()
        self.WebApp_WebApp2 = WebApp_WebApp2
        self.WebApp_WebApp4 = WebApp_WebApp4
        
    @property
    def User(self) -> str:
        return self.__User

    @User.setter
    def User(self, User: str):
        self.__User = User

    @property
    def Password(self) -> str:
        return self.__Password

    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def WebApp_WebApp(self):
        return self.__WebApp_WebApp

    @WebApp_WebApp.setter
    def WebApp_WebApp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WebApp_WebApp__WebApp_WebApp", None)
        self.__WebApp_WebApp = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "WebApp_WebPage"):
                    opp_val = getattr(item, "WebApp_WebPage", None)
                    
                    if opp_val == self:
                        setattr(item, "WebApp_WebPage", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WebApp_WebPage"):
                    opp_val = getattr(item, "WebApp_WebPage", None)
                    
                    setattr(item, "WebApp_WebPage", self)
                    

    @property
    def WebApp_WebApp2(self):
        return self.__WebApp_WebApp2

    @WebApp_WebApp2.setter
    def WebApp_WebApp2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WebApp_WebApp__WebApp_WebApp2", None)
        self.__WebApp_WebApp2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WebApp_DataBase"):
                opp_val = getattr(old_value, "WebApp_DataBase", None)
                if opp_val == self:
                    setattr(old_value, "WebApp_DataBase", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WebApp_DataBase"):
                opp_val = getattr(value, "WebApp_DataBase", None)
                setattr(value, "WebApp_DataBase", self)

    @property
    def WebApp_WebApp4(self):
        return self.__WebApp_WebApp4

    @WebApp_WebApp4.setter
    def WebApp_WebApp4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WebApp_WebApp__WebApp_WebApp4", None)
        self.__WebApp_WebApp4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WebApp_QuestionBank"):
                opp_val = getattr(old_value, "WebApp_QuestionBank", None)
                if opp_val == self:
                    setattr(old_value, "WebApp_QuestionBank", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WebApp_QuestionBank"):
                opp_val = getattr(value, "WebApp_QuestionBank", None)
                setattr(value, "WebApp_QuestionBank", self)

class PageS_Q:

    pass
class WebApp_Questionnary(PageS_Q):

    def __init__(self, feedback: bool):
        self.feedback = feedback
        
    @property
    def feedback(self) -> bool:
        return self.__feedback

    @feedback.setter
    def feedback(self, feedback: bool):
        self.__feedback = feedback

class WebApp_Survey(PageS_Q):

    pass
class WebApp_Question(ABC):

    pass
class WebPage:

    pass
class WebApp_EntityWebPage(WebPage):

    pass
class WebApp_Home(WebPage):

    pass
class WebApp_PageS_Q(WebPage):

    pass
class SimpleQuestion:

    pass
class WebApp_Multiple(SimpleQuestion):

    pass
class WebApp_TrueFalse(SimpleQuestion):

    pass
class WebApp_Opened(SimpleQuestion):

    pass
class WebApp_Entity:

    def __init__(self, name: str, WebApp_Entity: set["WebApp_Attribute"] = None, WebApp_Entity8: "WebApp_Entity" = None, WebApp_Entity6: set["WebApp_Entity"] = None, WebApp_Entity21: "WebApp_EntityWebPage" = None, WebApp_Entity24: "WebApp_DataBase" = None):
        self.name = name
        self.WebApp_Entity = WebApp_Entity if WebApp_Entity is not None else set()
        self.WebApp_Entity8 = WebApp_Entity8
        self.WebApp_Entity6 = WebApp_Entity6 if WebApp_Entity6 is not None else set()
        self.WebApp_Entity21 = WebApp_Entity21
        self.WebApp_Entity24 = WebApp_Entity24
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def WebApp_Entity8(self):
        return self.__WebApp_Entity8

    @WebApp_Entity8.setter
    def WebApp_Entity8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WebApp_Entity__WebApp_Entity8", None)
        self.__WebApp_Entity8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WebApp_Entity6"):
                opp_val = getattr(old_value, "WebApp_Entity6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WebApp_Entity6"):
                opp_val = getattr(value, "WebApp_Entity6", None)
                if opp_val is None:
                    setattr(value, "WebApp_Entity6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def WebApp_Entity6(self):
        return self.__WebApp_Entity6

    @WebApp_Entity6.setter
    def WebApp_Entity6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WebApp_Entity__WebApp_Entity6", None)
        self.__WebApp_Entity6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "WebApp_Entity8"):
                    opp_val = getattr(item, "WebApp_Entity8", None)
                    
                    if opp_val == self:
                        setattr(item, "WebApp_Entity8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WebApp_Entity8"):
                    opp_val = getattr(item, "WebApp_Entity8", None)
                    
                    setattr(item, "WebApp_Entity8", self)
                    

    @property
    def WebApp_Entity(self):
        return self.__WebApp_Entity

    @WebApp_Entity.setter
    def WebApp_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WebApp_Entity__WebApp_Entity", None)
        self.__WebApp_Entity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "WebApp_Attribute"):
                    opp_val = getattr(item, "WebApp_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "WebApp_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WebApp_Attribute"):
                    opp_val = getattr(item, "WebApp_Attribute", None)
                    
                    setattr(item, "WebApp_Attribute", self)
                    

    @property
    def WebApp_Entity24(self):
        return self.__WebApp_Entity24

    @WebApp_Entity24.setter
    def WebApp_Entity24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WebApp_Entity__WebApp_Entity24", None)
        self.__WebApp_Entity24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WebApp_DataBase23"):
                opp_val = getattr(old_value, "WebApp_DataBase23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WebApp_DataBase23"):
                opp_val = getattr(value, "WebApp_DataBase23", None)
                if opp_val is None:
                    setattr(value, "WebApp_DataBase23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def WebApp_Entity21(self):
        return self.__WebApp_Entity21

    @WebApp_Entity21.setter
    def WebApp_Entity21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WebApp_Entity__WebApp_Entity21", None)
        self.__WebApp_Entity21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WebApp_EntityWebPage"):
                opp_val = getattr(old_value, "WebApp_EntityWebPage", None)
                if opp_val == self:
                    setattr(old_value, "WebApp_EntityWebPage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WebApp_EntityWebPage"):
                opp_val = getattr(value, "WebApp_EntityWebPage", None)
                setattr(value, "WebApp_EntityWebPage", self)
