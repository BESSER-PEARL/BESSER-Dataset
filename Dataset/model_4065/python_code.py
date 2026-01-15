from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Classifier:

    pass
class PackageElement:

    pass
class simpleuml_Association(PackageElement):

    pass
class simpleuml_Classifier(PackageElement):

    pass
class simpleuml_Class(Classifier):

    pass
class simpleuml_UMLModelElement(ABC):

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

class simpleuml_PrimitiveDataType(Classifier):

    pass
class UMLModelElement:

    pass
class simpleuml_Package(UMLModelElement):

    pass
class simpleuml_PackageElement(UMLModelElement):

    pass
class simpleuml_Attribute(UMLModelElement):

    pass