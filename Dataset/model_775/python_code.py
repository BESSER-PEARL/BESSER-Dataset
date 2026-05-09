from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

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


class Artifact:

    pass
class StateMachine:

    pass
class Node:

    pass
class StructuredClassifier:

    pass
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
class UML2WithID_Node(Element, Class):

    pass
class UML2WithID_StateMachine(Behavior, Element):

    pass
class UML2WithID_Enumeration(Element, DataType):

    pass
class UML2WithID_Component(Element, Class):

    pass
class UML2WithID_Activity(Element, Behavior):

    pass
class UML2WithID_EncapsulatedClassifier(StructuredClassifier, Element):

    pass
class UML2WithID_ExecutionEnvironment(Node, Element):

    pass
class UML2WithID_Classifier(Element):

    def __init__(self, isAbstract: bool):
        self.isAbstract = isAbstract
        
        pass
    @property
    def isAbstract(self):
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract


class UML2WithID_PrimitiveType(Element, DataType):

    pass
class UML2WithID_Extension(Association, Element):

    pass
class UML2WithID_Behavior(Element, Class):

    pass
class UML2WithID_DeploymentSpecification(Artifact, Element):

    pass
class UML2WithID_UseCase(Element, BehavioredClassifier):

    pass
class UML2WithID_AssociationClass(Association, Element, Class):

    pass
class UML2WithID_ProtocolStateMachine(Element, StateMachine):

    pass
class UML2WithID_Class(EncapsulatedClassifier, Element, BehavioredClassifier):

    pass
class UML2WithID_Stereotype(Element, Class):

    pass
class UML2WithID_Device(Node, Element):

    pass
class UML2WithID_Collaboration(StructuredClassifier, Element, BehavioredClassifier):

    pass
class UML2WithID_CommunicationPath(Association, Element):

    pass
class UML2WithID_Interaction(Element, Behavior):

    pass
class Classifier:

    pass
class UML2WithID_Association(Classifier, Element):

    pass
class UML2WithID_StructuredClassifier(Classifier, Element):

    pass
class UML2WithID_TemplateableClassifier(Classifier, Element):

    pass
class UML2WithID_Actor(Classifier, Element):

    pass
class UML2WithID_DataType(Classifier, Element):

    pass
class UML2WithID_Artifact(Classifier, Element):

    pass
class UML2WithID_ParameterableClassifier(Classifier, Element):

    pass
class UML2WithID_Signal(Classifier, Element):

    pass
class UML2WithID_Interface(Classifier, Element):

    pass
class UML2WithID_InformationItem(Classifier, Element):

    pass
class UML2WithID_BehavioredClassifier(Classifier, Element):

    pass