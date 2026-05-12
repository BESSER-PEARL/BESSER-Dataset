from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class AbstractRequirement:

    pass
class Reqtify_MacroRequirement(AbstractRequirement):

    pass
class TextElement:

    pass
class Reqtify_AbstractRequirement(TextElement):

    pass
class Reqtify_Section(TextElement):

    pass
class Reqtify_Requirement(AbstractRequirement):

    pass
class Attribute:

    pass
class CoverLink:

    pass
class MacroRequirement:

    pass
class TypedElement:

    pass
class Reqtify_Attribute(TypedElement):

    def __init__(self, value: str):
        self.value = value
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class Reqtify_CoverLink(TypedElement):

    pass
class Reqtify_ElementWithIL(TypedElement):

    def __init__(self, label: str, name: str):
        self.label = label
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label


class Reqtify_TypedElement(ABC):

    def __init__(self, type: str):
        self.type = type
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


class Document:

    pass
class Reqtify_Project:

    pass
class Section:

    pass
class Project:

    pass
class ElementWithIL:

    pass
class Reqtify_TextElement(ElementWithIL):

    def __init__(self, description: str):
        self.description = description
        
        pass
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


class Reqtify_Document(ElementWithIL):

    pass