from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Behavior:

    pass
class Artifact:

    pass
class StateMachine:

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

class EncapsulatedClassifier:

    pass
class Class:

    pass
class Element:

    pass
class UML2WithID_DeploymentSpecification(Artifact, Element):

    pass
class UML2WithID_ProtocolStateMachine(StateMachine, Element):

    pass
class UML2WithID_StateMachine(Behavior, Element):

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

class UML2WithID_Node(Class, Element):

    pass
class UML2WithID_Activity(Element, Behavior):

    pass
class UML2WithID_Interaction(Element, Behavior):

    pass
class UML2WithID_Component(Class, Element):

    pass
class Classifier:

    pass
class UML2WithID_InformationItem(Element, Classifier):

    pass
class UML2WithID_ParameterableClassifier(Element, Classifier):

    pass
class UML2WithID_StructuredClassifier(Classifier, Element):

    pass
class UML2WithID_Signal(Classifier, Element):

    pass
class UML2WithID_Artifact(Element, Classifier):

    pass
class UML2WithID_TemplateableClassifier(Classifier, Element):

    pass
class UML2WithID_DataType(Classifier, Element):

    pass
class UML2WithID_Interface(Classifier, Element):

    pass
class UML2WithID_Actor(Element, Classifier):

    pass
class DataType:

    pass
class UML2WithID_PrimitiveType(DataType, Element):

    pass
class UML2WithID_Enumeration(DataType, Element):

    pass
class UML2WithID_Behavior(Class, Element):

    pass
class UML2WithID_Stereotype(Class, Element):

    pass
class UML2WithID_Association(Classifier, Element):

    pass
class UML2WithID_BehavioredClassifier(Classifier, Element):

    pass
class Association:

    pass
class UML2WithID_AssociationClass(Association, Class, Element):

    pass
class UML2WithID_Extension(Association, Element):

    pass
class UML2WithID_CommunicationPath(Association, Element):

    pass
class Node:

    pass
class UML2WithID_ExecutionEnvironment(Node, Element):

    pass
class UML2WithID_Device(Node, Element):

    pass
class StructuredClassifier:

    pass
class UML2WithID_EncapsulatedClassifier(StructuredClassifier, Element):

    pass
class BehavioredClassifier:

    pass
class UML2WithID_Collaboration(StructuredClassifier, BehavioredClassifier, Element):

    pass
class UML2WithID_Class(BehavioredClassifier, Element, EncapsulatedClassifier):

    pass
class UML2WithID_UseCase(BehavioredClassifier, Element):

    pass