from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class SimpleUML_UMLModelElement(ABC):

    def __init__(self, kind: str, name: str):
        self.kind = kind
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

class Classifier:

    pass
class SimpleUML_PrimitiveDataType(Classifier):

    pass
class SimpleUML_Class(Classifier):

    pass
class UMLModelElement:

    pass
class SimpleUML_PackageElement(UMLModelElement):

    pass
class SimpleUML_Package(UMLModelElement):

    pass
class SimpleUML_Attribute(UMLModelElement):

    pass
class PackageElement:

    pass
class SimpleUML_Association(PackageElement):

    pass
class SimpleUML_Classifier(PackageElement):

    pass