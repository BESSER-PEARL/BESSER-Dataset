from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class DataType:

    pass
class Association:

    pass
class Artifact:

    pass
class Node:

    pass
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
class UML2WithID_Interaction(Element, Behavior):

    pass
class UML2WithID_Class(EncapsulatedClassifier, BehavioredClassifier, Element):

    pass
class UML2WithID_Classifier(Element):

    pass
class UML2WithID_ExtensionEnd(Element, Property):

    pass
class UML2WithID_Enumeration(Element, DataType):

    pass
class UML2WithID_StateMachine(Element, Behavior):

    pass
class UML2WithID_Property(Element):

    pass
class UML2WithID_CommunicationPath(Element, Association):

    pass
class UML2WithID_DeploymentSpecification(Element, Artifact):

    pass
class UML2WithID_Device(Element, Node):

    pass
class UML2WithID_ExecutionEnvironment(Element, Node):

    pass
class UML2WithID_Activity(Element, Behavior):

    pass
class UML2WithID_Generalization(Element):

    pass
class UML2WithID_UseCase(Element, BehavioredClassifier):

    pass
class UML2WithID_Port(Element, Property):

    pass
class UML2WithID_EncapsulatedClassifier(Element, StructuredClassifier):

    pass
class UML2WithID_Extension(Element, Association):

    pass
class UML2WithID_PrimitiveType(Element, DataType):

    pass
class Classifier:

    pass
class UML2WithID_Actor(Element, Classifier):

    pass
class UML2WithID_TemplateableClassifier(Classifier, Element):

    pass
class UML2WithID_Interface(Element, Classifier):

    pass
class UML2WithID_Association(Classifier, Element):

    pass
class UML2WithID_Artifact(Classifier, Element):

    pass
class UML2WithID_Signal(Classifier, Element):

    pass
class UML2WithID_StructuredClassifier(Classifier, Element):

    pass
class UML2WithID_BehavioredClassifier(Element, Classifier):

    pass
class UML2WithID_DataType(Element, Classifier):

    pass
class UML2WithID_InformationItem(Classifier, Element):

    pass
class UML2WithID_ParameterableClassifier(Classifier, Element):

    pass
class UML2WithID_Collaboration(BehavioredClassifier, Element, StructuredClassifier):

    pass
class Class:

    pass
class UML2WithID_Stereotype(Element, Class):

    pass
class UML2WithID_AssociationClass(Element, Class, Association):

    pass
class UML2WithID_Behavior(Element, Class):

    pass
class UML2WithID_Node(Element, Class):

    pass
class UML2WithID_Component(Element, Class):

    pass
class StateMachine:

    pass
class UML2WithID_ProtocolStateMachine(StateMachine, Element):

    pass