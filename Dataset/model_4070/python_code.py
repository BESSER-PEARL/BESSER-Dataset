from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Classifier:

    pass
class PackageElement:

    pass
class uml_Association(PackageElement):

    pass
class uml_Classifier(PackageElement):

    pass
class uml_Class(Classifier):

    pass
class uml_UMLModelElement(ABC):

    def __init__(self, kind: str, name: str):
        self.kind = kind
        self.name = name
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class uml_PrimitiveDataType(Classifier):

    pass
class UMLModelElement:

    pass
class uml_Package(UMLModelElement):

    pass
class uml_PackageElement(UMLModelElement):

    pass
class uml_Attribute(UMLModelElement):

    pass