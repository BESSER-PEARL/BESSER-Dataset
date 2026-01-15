from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class StructuralFeature:

    pass
class simpleuml_Property(StructuralFeature):

    pass
class Classifier:

    pass
class simpleuml_Class(Classifier):

    pass
class Feature:

    pass
class simpleuml_StructuralFeature(Feature):

    pass
class simpleuml_Generalization:

    pass
class Type:

    pass
class simpleuml_Classifier(Type):

    pass
class NamedElement:

    pass
class simpleuml_Type(NamedElement):

    pass
class simpleuml_Feature(NamedElement):

    pass
class simpleuml_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
