from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Artifact:

    pass
class StateMachine:

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

class DataType:

    pass
class Association:

    pass
class Class:

    pass
class EncapsulatedClassifier:

    pass
class BehavioredClassifier:

    pass
class Behavior:

    pass
class Element:

    pass
class UML2WithID_ExecutionEnvironment(Node, Element):

    pass
class UML2WithID_ProtocolStateMachine(StateMachine, Element):

    pass
class UML2WithID_Extension(Association, Element):

    pass
class UML2WithID_UseCase(Element, BehavioredClassifier):

    pass
class UML2WithID_Interaction(Behavior, Element):

    pass
class UML2WithID_AssociationClass(Class, Element, Association):

    pass
class UML2WithID_Class(EncapsulatedClassifier, Element, BehavioredClassifier):

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

class UML2WithID_Activity(Behavior, Element):

    pass
class UML2WithID_Enumeration(DataType, Element):

    pass
class UML2WithID_PrimitiveType(DataType, Element):

    pass
class UML2WithID_Stereotype(Class, Element):

    pass
class UML2WithID_DeploymentSpecification(Artifact, Element):

    pass
class UML2WithID_Behavior(Class, Element):

    pass
class UML2WithID_Device(Node, Element):

    pass
class UML2WithID_Node(Class, Element):

    pass
class UML2WithID_Component(Class, Element):

    pass
class UML2WithID_StateMachine(Behavior, Element):

    pass
class Classifier:

    pass
class UML2WithID_Actor(Element, Classifier):

    pass
class UML2WithID_TemplateableClassifier(Element, Classifier):

    pass
class UML2WithID_DataType(Element, Classifier):

    pass
class UML2WithID_Signal(Element, Classifier):

    pass
class UML2WithID_Interface(Element, Classifier):

    pass
class UML2WithID_ParameterableClassifier(Element, Classifier):

    pass
class UML2WithID_InformationItem(Element, Classifier):

    pass
class UML2WithID_StructuredClassifier(Element, Classifier):

    pass
class UML2WithID_BehavioredClassifier(Element, Classifier):

    pass
class UML2WithID_Artifact(Element, Classifier):

    pass
class UML2WithID_Association(Element, Classifier):

    pass
class UML2WithID_CommunicationPath(Association, Element):

    pass
class StructuredClassifier:

    pass
class UML2WithID_EncapsulatedClassifier(StructuredClassifier, Element):

    pass
class UML2WithID_Collaboration(StructuredClassifier, Element, BehavioredClassifier):

    pass