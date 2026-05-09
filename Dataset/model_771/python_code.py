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


class Class:

    pass
class Association:

    pass
class StateMachine:

    pass
class EncapsulatedClassifier:

    pass
class Behavior:

    pass
class Artifact:

    pass
class Node:

    pass
class StructuredClassifier:

    pass
class BehavioredClassifier:

    pass
class Classifier:

    pass
class Element:

    pass
class UML2WithID_Signal(Classifier, Element):

    pass
class UML2WithID_Stereotype(Element, Class):

    pass
class UML2WithID_Class(BehavioredClassifier, Element, EncapsulatedClassifier):

    pass
class UML2WithID_Component(Element, Class):

    pass
class UML2WithID_EncapsulatedClassifier(Element, StructuredClassifier):

    pass
class UML2WithID_ProtocolStateMachine(StateMachine, Element):

    pass
class UML2WithID_Device(Element, Node):

    pass
class UML2WithID_Interface(Classifier, Element):

    pass
class UML2WithID_Interaction(Behavior, Element):

    pass
class UML2WithID_Actor(Classifier, Element):

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


class UML2WithID_ParameterableClassifier(Classifier, Element):

    pass
class UML2WithID_Artifact(Classifier, Element):

    pass
class UML2WithID_StateMachine(Behavior, Element):

    pass
class UML2WithID_InformationItem(Classifier, Element):

    pass
class UML2WithID_DataType(Classifier, Element):

    pass
class UML2WithID_Node(Element, Class):

    pass
class UML2WithID_StructuredClassifier(Classifier, Element):

    pass
class UML2WithID_CommunicationPath(Element, Association):

    pass
class UML2WithID_Activity(Behavior, Element):

    pass
class UML2WithID_AssociationClass(Element, Class, Association):

    pass
class UML2WithID_DeploymentSpecification(Element, Artifact):

    pass
class UML2WithID_TemplateableClassifier(Classifier, Element):

    pass
class UML2WithID_Behavior(Element, Class):

    pass
class UML2WithID_UseCase(BehavioredClassifier, Element):

    pass
class UML2WithID_Collaboration(BehavioredClassifier, Element, StructuredClassifier):

    pass
class UML2WithID_ExecutionEnvironment(Element, Node):

    pass
class UML2WithID_Association(Classifier, Element):

    pass
class UML2WithID_BehavioredClassifier(Classifier, Element):

    pass
class UML2WithID_Extension(Element, Association):

    pass
class DataType:

    pass
class UML2WithID_PrimitiveType(Element, DataType):

    pass
class UML2WithID_Enumeration(Element, DataType):

    pass