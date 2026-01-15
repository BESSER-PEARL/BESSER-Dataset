from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Node:

    pass
class UML2_ExecutionEnvironment(Node):

    pass
class BehavioredClassifier:

    pass
class UML2_UseCase(BehavioredClassifier):

    pass
class Behavior:

    pass
class UML2_Interaction(Behavior):

    pass
class UML2_Activity(Behavior):

    pass
class UML2_StateMachine(Behavior):

    pass
class StateMachine:

    pass
class UML2_ProtocolStateMachine(StateMachine):

    pass
class Artifact:

    pass
class UML2_DeploymentSpecification(Artifact):

    pass
class UML2_Device(Node):

    pass
class EncapsulatedClassifier:

    pass
class UML2_Class(EncapsulatedClassifier, BehavioredClassifier):

    pass
class Association:

    pass
class UML2_Extension(Association):

    pass
class UML2_CommunicationPath(Association):

    pass
class UML2_Classifier:

    def __init__(self, isAbstract: bool):
        self.isAbstract = isAbstract
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

class StructuredClassifier:

    pass
class UML2_Collaboration(StructuredClassifier, BehavioredClassifier):

    pass
class UML2_EncapsulatedClassifier(StructuredClassifier):

    pass
class DataType:

    pass
class UML2_PrimitiveType(DataType):

    pass
class UML2_Enumeration(DataType):

    pass
class Classifier:

    pass
class UML2_ParameterableClassifier(Classifier):

    pass
class UML2_Association(Classifier):

    pass
class UML2_InformationItem(Classifier):

    pass
class UML2_Artifact(Classifier):

    pass
class UML2_BehavioredClassifier(Classifier):

    pass
class UML2_Interface(Classifier):

    pass
class UML2_Signal(Classifier):

    pass
class UML2_TemplateableClassifier(Classifier):

    pass
class UML2_StructuredClassifier(Classifier):

    pass
class UML2_DataType(Classifier):

    pass
class UML2_Actor(Classifier):

    pass
class Class:

    pass
class UML2_Component(Class):

    pass
class UML2_AssociationClass(Class, Association):

    pass
class UML2_Behavior(Class):

    pass
class UML2_Stereotype(Class):

    pass
class UML2_Node(Class):

    pass