from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class EncapsulatedClassifier:

    pass
class Artifact:

    pass
class Node:

    pass
class UML2WithID_Element(ABC):

    def __init__(self, ID: str):
        self.ID = ID
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

class StructuredClassifier:

    pass
class BehavioredClassifier:

    pass
class Classifier:

    pass
class Element:

    pass
class UML2WithID_StructuredClassifier(Element, Classifier):

    pass
class UML2WithID_EncapsulatedClassifier(Element, StructuredClassifier):

    pass
class UML2WithID_DeploymentSpecification(Artifact, Element):

    pass
class UML2WithID_UseCase(Element, BehavioredClassifier):

    pass
class UML2WithID_InformationItem(Element, Classifier):

    pass
class UML2WithID_BehavioredClassifier(Element, Classifier):

    pass
class UML2WithID_Class(Element, EncapsulatedClassifier, BehavioredClassifier):

    pass
class UML2WithID_Association(Element, Classifier):

    pass
class UML2WithID_Device(Node, Element):

    pass
class UML2WithID_Classifier(Element):

    def __init__(self, isAbstract: bool):
        self.isAbstract = isAbstract
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

class UML2WithID_ExecutionEnvironment(Node, Element):

    pass
class UML2WithID_DataType(Element, Classifier):

    pass
class UML2WithID_Collaboration(Element, StructuredClassifier, BehavioredClassifier):

    pass
class DataType:

    pass
class UML2WithID_PrimitiveType(Element, DataType):

    pass
class UML2WithID_Enumeration(DataType, Element):

    pass
class UML2WithID_Actor(Element, Classifier):

    pass
class UML2WithID_ParameterableClassifier(Element, Classifier):

    pass
class UML2WithID_Signal(Element, Classifier):

    pass
class UML2WithID_Interface(Element, Classifier):

    pass
class Behavior:

    pass
class UML2WithID_Interaction(Behavior, Element):

    pass
class UML2WithID_Activity(Behavior, Element):

    pass
class UML2WithID_StateMachine(Behavior, Element):

    pass
class StateMachine:

    pass
class UML2WithID_ProtocolStateMachine(Element, StateMachine):

    pass
class UML2WithID_TemplateableClassifier(Element, Classifier):

    pass
class Association:

    pass
class UML2WithID_CommunicationPath(Association, Element):

    pass
class UML2WithID_Extension(Association, Element):

    pass
class Class:

    pass
class UML2WithID_Component(Element, Class):

    pass
class UML2WithID_Stereotype(Element, Class):

    pass
class UML2WithID_Behavior(Element, Class):

    pass
class UML2WithID_Node(Element, Class):

    pass
class UML2WithID_AssociationClass(Association, Element, Class):

    pass
class UML2WithID_Artifact(Element, Classifier):

    pass