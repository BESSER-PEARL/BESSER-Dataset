from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class StateMachine:

    pass
class BehavioralFeature:

    pass
class Behavior:

    pass
class Element:

    pass
class UML2WithID_Interaction(Behavior, Element):

    pass
class UML2WithID_Activity(Behavior, Element):

    pass
class UML2WithID_ProtocolStateMachine(StateMachine, Element):

    pass
class UML2WithID_Operation(BehavioralFeature, Element):

    pass
class UML2WithID_BehavioredClassifier(Element):

    pass
class UML2WithID_BehavioralFeature(Element):

    pass
class UML2WithID_Reception(BehavioralFeature, Element):

    pass
class Node:

    pass
class UML2WithID_Device(Node, Element):

    pass
class UML2WithID_ExecutionEnvironment(Node, Element):

    pass
class Class:

    pass
class UML2WithID_Stereotype(Class, Element):

    pass
class UML2WithID_Component(Class, Element):

    pass
class UML2WithID_AssociationClass(Class, Element):

    pass
class UML2WithID_Behavior(Class, Element):

    pass
class UML2WithID_Node(Class, Element):

    pass
class BehavioredClassifier:

    pass
class UML2WithID_Class(BehavioredClassifier, Element):

    pass
class UML2WithID_UseCase(Element, BehavioredClassifier):

    pass
class UML2WithID_Collaboration(BehavioredClassifier, Element):

    pass
class UML2WithID_Element(ABC):

    def __init__(self, ID: str):
        self.ID = ID
        
        pass
    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID


class UML2WithID_StateMachine(Behavior, Element):

    pass