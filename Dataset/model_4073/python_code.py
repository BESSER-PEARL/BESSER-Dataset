from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class PackageElement:

    pass
class simpleUml_Classifier(PackageElement):

    pass
class simpleUml_UMLModelElement:

    def __init__(self, kind: str, name: str):
        self.kind = kind
        self.name = name
        
        pass
    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class simpleUml_Association:

    pass
class simpleUml_Attribute:

    pass
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