from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class UML2WithID_Element(ABC):

    def __init__(self, ID: str):
        self.ID = ID
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

class Behavior:

    pass
class BehavioralFeature:

    pass
class Class:

    pass
class BehavioredClassifier:

    pass
class StateMachine:

    pass
class Element:

    pass
class UML2WithID_Class(Element, BehavioredClassifier):

    pass
class UML2WithID_Interaction(Element, Behavior):

    pass
class UML2WithID_Reception(Element, BehavioralFeature):

    pass
class UML2WithID_BehavioredClassifier(Element):

    pass
class UML2WithID_Activity(Element, Behavior):

    pass
class UML2WithID_Stereotype(Class, Element):

    pass
class UML2WithID_Operation(Element, BehavioralFeature):

    pass
class UML2WithID_Node(Class, Element):

    pass
class UML2WithID_BehavioralFeature(Element):

    pass
class UML2WithID_ProtocolStateMachine(StateMachine, Element):

    pass
class UML2WithID_Component(Class, Element):

    pass
class UML2WithID_AssociationClass(Class, Element):

    pass
class UML2WithID_StateMachine(Element, Behavior):

    pass
class UML2WithID_Behavior(Class, Element):

    pass
class UML2WithID_Collaboration(Element, BehavioredClassifier):

    pass
class UML2WithID_UseCase(Element, BehavioredClassifier):

    pass
class Node:

    pass
class UML2WithID_ExecutionEnvironment(Element, Node):

    pass
class UML2WithID_Device(Element, Node):

    pass