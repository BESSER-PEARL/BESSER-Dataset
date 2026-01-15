from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class DataType:

    pass
class Association:

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

class Class:

    pass
class StateMachine:

    pass
class Artifact:

    pass
class Node:

    pass
class Behavior:

    pass
class EncapsulatedClassifier:

    pass
class BehavioredClassifier:

    pass
class StructuredClassifier:

    pass
class Property:

    pass
class Element:

    pass
class UML2WithID_ExtensionEnd(Property, Element):

    pass
class UML2WithID_Interaction(Behavior, Element):

    pass
class UML2WithID_Node(Class, Element):

    pass
class UML2WithID_Collaboration(BehavioredClassifier, Element, StructuredClassifier):

    pass
class UML2WithID_Behavior(Class, Element):

    pass
class UML2WithID_StateMachine(Element, Behavior):

    pass
class UML2WithID_Enumeration(DataType, Element):

    pass
class UML2WithID_PrimitiveType(DataType, Element):

    pass
class UML2WithID_Extension(Association, Element):

    pass
class UML2WithID_CommunicationPath(Association, Element):

    pass
class UML2WithID_DeploymentSpecification(Element, Artifact):

    pass
class UML2WithID_Component(Class, Element):

    pass
class UML2WithID_Property(Element):

    pass
class UML2WithID_Activity(Element, Behavior):

    pass
class UML2WithID_Port(Property, Element):

    pass
class UML2WithID_EncapsulatedClassifier(StructuredClassifier, Element):

    pass
class UML2WithID_UseCase(BehavioredClassifier, Element):

    pass
class UML2WithID_Classifier(Element):

    pass
class UML2WithID_Generalization(Element):

    pass
class UML2WithID_AssociationClass(Association, Class, Element):

    pass
class UML2WithID_Stereotype(Class, Element):

    pass
class UML2WithID_ExecutionEnvironment(Node, Element):

    pass
class UML2WithID_Class(EncapsulatedClassifier, BehavioredClassifier, Element):

    pass
class UML2WithID_ProtocolStateMachine(Element, StateMachine):

    pass
class UML2WithID_Device(Node, Element):

    pass
class Classifier:

    pass
class UML2WithID_TemplateableClassifier(Classifier, Element):

    pass
class UML2WithID_Association(Classifier, Element):

    pass
class UML2WithID_DataType(Classifier, Element):

    pass
class UML2WithID_Signal(Classifier, Element):

    pass
class UML2WithID_Artifact(Classifier, Element):

    pass
class UML2WithID_Actor(Classifier, Element):

    pass
class UML2WithID_StructuredClassifier(Classifier, Element):

    pass
class UML2WithID_Interface(Classifier, Element):

    pass
class UML2WithID_ParameterableClassifier(Classifier, Element):

    pass
class UML2WithID_BehavioredClassifier(Classifier, Element):

    pass
class UML2WithID_InformationItem(Classifier, Element):

    pass