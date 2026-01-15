from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class docbook_Para:

    def __init__(self, content: str, docbook_Para: "docbook_Section" = None):
        self.content = content
        self.docbook_Para = docbook_Para
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def docbook_Para(self):
        return self.__docbook_Para

    @docbook_Para.setter
    def docbook_Para(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_docbook_Para__docbook_Para", None)
        self.__docbook_Para = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "docbook_Section"):
                opp_val = getattr(old_value, "docbook_Section", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "docbook_Section"):
                opp_val = getattr(value, "docbook_Section", None)
                if opp_val is None:
                    setattr(value, "docbook_Section", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Section:

    pass
class docbook_Sect1(Section):

    pass
class docbook_Sect2(Section):

    pass
class docbook_Book:

    pass
class docbook_DocBook:

    pass
class TitledElement:

    pass
class docbook_Section(TitledElement):

    pass
class docbook_TitledElement(ABC):

    def __init__(self, title: str):
        self.title = title
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

class docbook_Article(TitledElement):

    pass