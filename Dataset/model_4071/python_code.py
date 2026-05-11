from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class uml_UMLModelElement(ABC):

    def __init__(self, kind: str, name: str):
        self.kind = kind
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


class Classifier:

    pass
class uml_PrimitiveDataType(Classifier):

    pass
class PackageElement:

    pass
class uml_Association(PackageElement):

    pass
class uml_Classifier(PackageElement):

    pass
class uml_Class(Classifier):

    pass
class UMLModelElement:

    pass
class uml_PackageElement(UMLModelElement):

    pass
class uml_Attribute(UMLModelElement):

    pass
class uml_Package(UMLModelElement):

    pass