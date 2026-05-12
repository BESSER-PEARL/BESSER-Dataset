from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Abstract:

    pass
class Keywords:

    pass
class Type:

    pass
class LaTeX_Document:

    pass
class Document:

    pass
class LaTeX_Citation:

    pass
class LaTeX_DocumentBody:

    pass
class DocumentBody:

    pass
class Citation:

    pass
class LaTeX_Bibliography:

    pass
class Bibliography:

    pass
class Description:

    pass
class Date:

    pass
class Item:

    pass
class Enumerate:

    pass
class Items:

    pass
class Title:

    pass
class Label:

    pass
class Path:

    pass
class SectionBody:

    pass
class LaTeX_Corps(ABC):

    pass
class Section:

    pass
class Corps:

    pass
class LaTeX_Enumerate(Corps):

    pass
class LaTeX_Figure(Corps):

    pass
class LaTeX_Items(Corps):

    pass
class LaTeX_Section(Corps):

    pass
class LaTeX_SectionBody:

    pass
class Heading:

    pass
class Adress:

    pass
class EMail:

    pass
class Fax:

    pass
class Phone:

    pass
class LaTeX_Heading:

    pass
class Organisation:

    pass
class Author:

    pass
class LaTeX_Organisation:

    pass
class Name:

    pass
class LaTeX_Author:

    pass
class ValuedElement:

    pass
class LaTeX_Fax(ValuedElement):

    pass
class LaTeX_Adress(ValuedElement):

    pass
class LaTeX_Path(ValuedElement):

    pass
class LaTeX_EMail(ValuedElement):

    pass
class LaTeX_Keywords(ValuedElement):

    pass
class LaTeX_Cite(ValuedElement, Corps):

    pass
class LaTeX_Abstract(ValuedElement):

    pass
class LaTeX_Date(ValuedElement):

    pass
class LaTeX_Name(ValuedElement):

    pass
class LaTeX_Item(ValuedElement):

    pass
class LaTeX_Title(ValuedElement):

    pass
class LaTeX_Description(ValuedElement):

    pass
class LaTeX_Value(ValuedElement, Corps):

    pass
class LaTeX_Label(ValuedElement):

    pass
class LaTeX_Phone(ValuedElement):

    pass
class LaTeX_Type(ValuedElement):

    pass
class LaTeX_ValuedElement(ABC):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

