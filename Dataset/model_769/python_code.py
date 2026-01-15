from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class StateMachine:

    pass
class UML2_ProtocolStateMachine(StateMachine):

    pass
class Property:

    pass
class UML2_ExtensionEnd(Property):

    pass
class Behavior:

    pass
class UML2_Interaction(Behavior):

    pass
class Association:

    pass
class UML2_CommunicationPath(Association):

    pass
class UML2_Extension(Association):

    pass
class DataType:

    pass
class UML2_PrimitiveType(DataType):

    pass
class UML2_Property:

    pass
class UML2_Port(Property):

    pass
class Artifact:

    pass
class UML2_DeploymentSpecification(Artifact):

    pass
class UML2_Enumeration(DataType):

    pass
class UML2_StateMachine(Behavior):

    pass
class Class:

    pass
class UML2_Node(Class):

    pass
class UML2_Stereotype(Class):

    pass
class UML2_AssociationClass(Association, Class):

    pass
class UML2_Component(Class):

    pass
class UML2_Behavior(Class):

    pass
class Node:

    pass
class UML2_ExecutionEnvironment(Node):

    pass
class UML2_Device(Node):

    pass
class EncapsulatedClassifier:

    pass
class UML2_Classifier:

    pass
class UML2_Generalization:

    pass
class BehavioredClassifier:

    pass
class UML2_Class(EncapsulatedClassifier, BehavioredClassifier):

    pass
class UML2_UseCase(BehavioredClassifier):

    pass
class UML2_Activity(Behavior):

    pass
class StructuredClassifier:

    pass
class UML2_Collaboration(StructuredClassifier, BehavioredClassifier):

    pass
class UML2_EncapsulatedClassifier(StructuredClassifier):

    pass
class Classifier:

    pass
class UML2_Association(Classifier):

    pass
class UML2_BehavioredClassifier(Classifier):

    pass
class UML2_DataType(Classifier):

    pass
class UML2_Actor(Classifier):

    pass
class UML2_StructuredClassifier(Classifier):

    pass
class UML2_InformationItem(Classifier):

    pass
class UML2_TemplateableClassifier(Classifier):

    pass
class UML2_Signal(Classifier):

    pass
class UML2_Interface(Classifier):

    pass
class UML2_Artifact(Classifier):

    pass
class UML2_ParameterableClassifier(Classifier):

    pass