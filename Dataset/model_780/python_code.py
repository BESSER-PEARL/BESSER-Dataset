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


class EncapsulatedClassifier:

    pass
class StructuredClassifier:

    pass
class BehavioredClassifier:

    pass
class StateMachine:

    pass
class DataType:

    pass
class Node:

    pass
class Property:

    pass
class Behavior:

    pass
class Class:

    pass
class Artifact:

    pass
class Classifier:

    pass
class Association:

    pass
class Element:

    pass
class UML2WithID_Artifact(Classifier, Element):

    pass
class UML2WithID_DataType(Classifier, Element):

    pass
class UML2WithID_Enumeration(DataType, Element):

    pass
class UML2WithID_StructuredClassifier(Classifier, Element):

    pass
class UML2WithID_Class(EncapsulatedClassifier, Element, BehavioredClassifier):

    pass
class UML2WithID_AssociationClass(Class, Association, Element):

    pass
class UML2WithID_Signal(Classifier, Element):

    pass
class UML2WithID_Classifier(Element):

    pass
class UML2WithID_Interaction(Behavior, Element):

    pass
class UML2WithID_Actor(Classifier, Element):

    pass
class UML2WithID_PrimitiveType(DataType, Element):

    pass
class UML2WithID_Node(Class, Element):

    pass
class UML2WithID_ProtocolStateMachine(StateMachine, Element):

    pass
class UML2WithID_ParameterableClassifier(Classifier, Element):

    pass
class UML2WithID_DeploymentSpecification(Artifact, Element):

    pass
class UML2WithID_Association(Classifier, Element):

    pass
class UML2WithID_Interface(Classifier, Element):

    pass
class UML2WithID_Extension(Association, Element):

    pass
class UML2WithID_ExecutionEnvironment(Node, Element):

    pass
class UML2WithID_UseCase(BehavioredClassifier, Element):

    pass
class UML2WithID_InformationItem(Classifier, Element):

    pass
class UML2WithID_Collaboration(StructuredClassifier, BehavioredClassifier, Element):

    pass
class UML2WithID_TemplateableClassifier(Classifier, Element):

    pass
class UML2WithID_Port(Property, Element):

    pass
class UML2WithID_Stereotype(Class, Element):

    pass
class UML2WithID_Component(Class, Element):

    pass
class UML2WithID_CommunicationPath(Association, Element):

    pass
class UML2WithID_ExtensionEnd(Property, Element):

    pass
class UML2WithID_Device(Node, Element):

    pass
class UML2WithID_EncapsulatedClassifier(StructuredClassifier, Element):

    pass
class UML2WithID_Activity(Behavior, Element):

    pass
class UML2WithID_BehavioredClassifier(Classifier, Element):

    pass
class UML2WithID_StateMachine(Behavior, Element):

    pass
class UML2WithID_Behavior(Class, Element):

    pass
class UML2WithID_Generalization(Element):

    pass
class UML2WithID_Property(Element):

    pass