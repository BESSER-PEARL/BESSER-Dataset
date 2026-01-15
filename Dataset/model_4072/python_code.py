from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Classifier:

    pass
class simpleUml_Class(Classifier):

    pass
class UMLModelElement:

    pass
class simpleUml_PackageElement(UMLModelElement):

    pass
class simpleUml_Package(UMLModelElement):

    pass
class PackageElement:

    pass
class simpleUml_Classifier(PackageElement):

    pass
class simpleUml_UMLModelElement:

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

class simpleUml_Association:

    pass
class simpleUml_Attribute:

    pass