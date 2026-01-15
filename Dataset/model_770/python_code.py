from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Artifact:

    pass
class UML2_DeploymentSpecification(Artifact):

    pass
class DataType:

    pass
class UML2_Enumeration(DataType):

    pass
class Association:

    pass
class UML2_Extension(Association):

    pass
class UML2_CommunicationPath(Association):

    pass
class StructuralFeature:

    pass
class UML2_Property(StructuralFeature):

    pass
class BehavioralFeature:

    pass
class UML2_Operation(BehavioralFeature):

    pass
class UML2_Reception(BehavioralFeature):

    pass
class UML2_PrimitiveType(DataType):

    pass
class WriteStructuralFeatureAction:

    pass
class UML2_DurationObservationAction(WriteStructuralFeatureAction):

    pass
class UML2_AddStructuralFeatureValueAction(WriteStructuralFeatureAction):

    pass
class UML2_RemoveStructuralFeatureValueAction(WriteStructuralFeatureAction):

    pass
class UML2_TimeObservationAction(WriteStructuralFeatureAction):

    pass
class Class:

    pass
class UML2_AssociationClass(Association, Class):

    pass
class UML2_Stereotype(Class):

    pass
class UML2_Behavior(Class):

    pass
class UML2_Component(Class):

    pass
class UML2_Node(Class):

    pass
class Property:

    pass
class UML2_Port(Property):

    pass
class UML2_ExtensionEnd(Property):

    pass
class Classifier:

    pass
class UML2_TemplateableClassifier(Classifier):

    pass
class UML2_StructuredClassifier(Classifier):

    pass
class UML2_Artifact(Classifier):

    pass
class UML2_ParameterableClassifier(Classifier):

    pass
class UML2_InformationItem(Classifier):

    pass
class UML2_Association(Classifier):

    pass
class UML2_BehavioredClassifier(Classifier):

    pass
class UML2_DataType(Classifier):

    pass
class UML2_Actor(Classifier):

    pass
class Node:

    pass
class UML2_ExecutionEnvironment(Node):

    pass
class UML2_Device(Node):

    pass
class StructuralFeatureAction:

    pass
class UML2_ClearStructuralFeatureAction(StructuralFeatureAction):

    pass
class UML2_WriteStructuralFeatureAction(StructuralFeatureAction):

    pass
class UML2_ReadStructuralFeatureAction(StructuralFeatureAction):

    pass
class UML2_Interface(Classifier):

    pass
class UML2_Signal(Classifier):

    pass
class StructuredClassifier:

    pass
class UML2_EncapsulatedClassifier(StructuredClassifier):

    pass
class EncapsulatedClassifier:

    pass
class BehavioredClassifier:

    pass
class UML2_UseCase(BehavioredClassifier):

    pass
class UML2_Collaboration(BehavioredClassifier, StructuredClassifier):

    pass
class UML2_Class(BehavioredClassifier, EncapsulatedClassifier):

    pass
class StateMachine:

    pass
class UML2_ProtocolStateMachine(StateMachine):

    pass
class UML2_StructuralFeatureAction:

    pass
class Feature:

    pass
class UML2_BehavioralFeature(Feature):

    pass
class UML2_Connector(Feature):

    pass
class UML2_StructuralFeature(Feature):

    pass
class UML2_Classifier:

    pass
class UML2_Feature:

    pass
class Behavior:

    pass
class UML2_StateMachine(Behavior):

    pass
class UML2_Activity(Behavior):

    pass
class UML2_Interaction(Behavior):

    pass