from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Section:

    pass
class DocBook_Sect2(Section):

    pass
class DocBook_Sect1(Section):

    pass
class TitledElement:

    pass
class DocBook_Section(TitledElement):

    pass
class DocBook_TitledElement(ABC):

    def __init__(self, title: str):
        self.title = title
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

class DocBook_Article(TitledElement):

    pass
class DocBook_Book:

    pass
class DocBook_DocBook:

    pass
class DocBook_Para:

    def __init__(self, content: str, DocBook_Para: "DocBook_Section" = None):
        self.content = content
        self.DocBook_Para = DocBook_Para
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def DocBook_Para(self):
        return self.__DocBook_Para

    @DocBook_Para.setter
    def DocBook_Para(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DocBook_Para__DocBook_Para", None)
        self.__DocBook_Para = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DocBook_Section"):
                opp_val = getattr(old_value, "DocBook_Section", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DocBook_Section"):
                opp_val = getattr(value, "DocBook_Section", None)
                if opp_val is None:
                    setattr(value, "DocBook_Section", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
