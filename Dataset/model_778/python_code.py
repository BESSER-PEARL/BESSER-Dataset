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

class Property:

    pass
class Association:

    pass
class StateMachine:

    pass
class Artifact:

    pass
class Behavior:

    pass
class Class:

    pass
class Node:

    pass
class Element:

    pass
class UML2WithID_Extension(Association, Element):

    pass
class UML2WithID_StateMachine(Element, Behavior):

    pass
class UML2WithID_CommunicationPath(Association, Element):

    pass
class UML2WithID_Device(Element, Node):

    pass
class UML2WithID_Port(Element, Property):

    pass
class UML2WithID_Interaction(Element, Behavior):

    pass
class UML2WithID_Behavior(Class, Element):

    pass
class UML2WithID_Generalization(Element):

    pass
class UML2WithID_ProtocolStateMachine(Element, StateMachine):

    pass
class UML2WithID_Activity(Element, Behavior):

    pass
class UML2WithID_Node(Class, Element):

    pass
class UML2WithID_DeploymentSpecification(Element, Artifact):

    pass
class UML2WithID_Property(Element):

    pass
class UML2WithID_Stereotype(Class, Element):

    pass
class UML2WithID_ExecutionEnvironment(Element, Node):

    pass
class UML2WithID_ExtensionEnd(Element, Property):

    pass
class UML2WithID_AssociationClass(Class, Association, Element):

    pass
class UML2WithID_Classifier(Element):

    pass
class StructuredClassifier:

    pass
class UML2WithID_EncapsulatedClassifier(Element, StructuredClassifier):

    pass
class Classifier:

    pass
class UML2WithID_BehavioredClassifier(Element, Classifier):

    pass
class UML2WithID_StructuredClassifier(Element, Classifier):

    pass
class UML2WithID_DataType(Element, Classifier):

    pass
class UML2WithID_Interface(Element, Classifier):

    pass
class UML2WithID_ParameterableClassifier(Element, Classifier):

    pass
class UML2WithID_Signal(Element, Classifier):

    pass
class UML2WithID_Association(Element, Classifier):

    pass
class UML2WithID_TemplateableClassifier(Element, Classifier):

    pass
class UML2WithID_InformationItem(Element, Classifier):

    pass
class UML2WithID_Artifact(Element, Classifier):

    pass
class UML2WithID_Actor(Element, Classifier):

    pass
class UML2WithID_Component(Class, Element):

    pass
class DataType:

    pass
class UML2WithID_PrimitiveType(Element, DataType):

    pass
class UML2WithID_Enumeration(Element, DataType):

    pass
class EncapsulatedClassifier:

    pass
class BehavioredClassifier:

    pass
class UML2WithID_UseCase(Element, BehavioredClassifier):

    pass
class UML2WithID_Collaboration(Element, BehavioredClassifier, StructuredClassifier):

    pass
class UML2WithID_Class(Element, BehavioredClassifier, EncapsulatedClassifier):

    pass