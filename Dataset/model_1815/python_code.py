from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class DocBook_Para:

    def __init__(self, content: str):
        self.content = content
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

class Sect2:

    pass
class Section:

    pass
class DocBook_Sect2(Section):

    pass
class DocBook_Sect1(Section):

    pass
class Book:

    pass
class DocBook_DocBook:

    pass
class Para:

    pass
class Sect1:

    pass
class TitledElement:

    pass
class DocBook_Section(TitledElement):

    pass
class DocBook_Article(TitledElement):

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

class Article:

    pass
class DocBook_Book:

    pass