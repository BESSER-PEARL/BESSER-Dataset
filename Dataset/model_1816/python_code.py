from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class DocBook_Book:

    pass
class DocBook_DocBook:

    pass
class Section:

    pass
class DocBook_Sect2(Section):

    pass
class DocBook_Para:

    def __init__(self, content: str, Para: "DocBook_Section" = None, paras: "DocBook_Section" = None):
        self.content = content
        self.Para = Para
        self.paras = paras
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def Para(self):
        return self.__Para

    @Para.setter
    def Para(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DocBook_Para__Para", None)
        self.__Para = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "section"):
                opp_val = getattr(old_value, "section", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "section"):
                opp_val = getattr(value, "section", None)
                if opp_val is None:
                    setattr(value, "section", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def paras(self):
        return self.__paras

    @paras.setter
    def paras(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DocBook_Para__paras", None)
        self.__paras = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Section"):
                opp_val = getattr(old_value, "Section", None)
                if opp_val == self:
                    setattr(old_value, "Section", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Section"):
                opp_val = getattr(value, "Section", None)
                setattr(value, "Section", self)

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