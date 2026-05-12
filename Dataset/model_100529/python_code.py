from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Actor:

    pass
class UseCase_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class UseCase_BehavioredClassifier:

    pass
class UseCase_UseCaseContainer:

    pass
class UseCase_Include:

    pass
class Extend:

    pass
class Include:

    pass
class NamedElement:

    pass
class UseCase_Association(NamedElement):

    pass
class UseCase_UseCase(NamedElement):

    pass
class UseCase_Actor(NamedElement):

    pass
class UseCase:

    pass
class UseCase_Extend:

    pass