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

class StateMachine:

    pass
class Node:

    pass
class BehavioredClassifier:

    pass
class Element:

    pass
class UML2WithID_ExecutionEnvironment(Element, Node):

    pass
class UML2WithID_Device(Element, Node):

    pass
class UML2WithID_Class(Element, BehavioredClassifier):

    pass
class UML2WithID_UseCase(Element, BehavioredClassifier):

    pass
class UML2WithID_BehavioralFeature(Element):

    pass
class UML2WithID_BehavioredClassifier(Element):

    pass
class UML2WithID_ProtocolStateMachine(Element, StateMachine):

    pass
class UML2WithID_Collaboration(Element, BehavioredClassifier):

    pass
class Class:

    pass
class UML2WithID_AssociationClass(Element, Class):

    pass
class UML2WithID_Component(Element, Class):

    pass
class UML2WithID_Behavior(Element, Class):

    pass
class UML2WithID_Node(Element, Class):

    pass
class UML2WithID_Stereotype(Element, Class):

    pass
class BehavioralFeature:

    pass
class UML2WithID_Operation(BehavioralFeature, Element):

    pass
class UML2WithID_Reception(BehavioralFeature, Element):

    pass
class Behavior:

    pass
class UML2WithID_StateMachine(Behavior, Element):

    pass
class UML2WithID_Activity(Behavior, Element):

    pass
class UML2WithID_Interaction(Behavior, Element):

    pass