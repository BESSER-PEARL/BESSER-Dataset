from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class StructuralFeature:

    pass
class UML2_Property(StructuralFeature):

    pass
class UML2_Type:

    pass
class UML2_TypedElement:

    pass
class CentralBufferNode:

    pass
class UML2_DataStoreNode(CentralBufferNode):

    pass
class OpaqueExpression:

    pass
class UML2_Expression(OpaqueExpression):

    pass
class Class:

    pass
class UML2_Node(Class):

    pass
class UML2_Behavior(Class):

    pass
class UML2_Stereotype(Class):

    pass
class Association:

    pass
class UML2_AssociationClass(Class, Association):

    pass
class UML2_CommunicationPath(Association):

    pass
class StateMachine:

    pass
class UML2_ProtocolStateMachine(StateMachine):

    pass
class Interval:

    pass
class UML2_DurationInterval(Interval):

    pass
class UML2_TimeInterval(Interval):

    pass
class UML2_Extension(Association):

    pass
class StructuredClassifier:

    pass
class UML2_EncapsulatedClassifier(StructuredClassifier):

    pass
class InputPin:

    pass
class UML2_ValuePin(InputPin):

    pass
class UML2_Component(Class):

    pass
class Pin:

    pass
class UML2_InputPin(Pin):

    pass
class UML2_OutputPin(Pin):

    pass
class ValueSpecification:

    pass
class UML2_LiteralSpecification(ValueSpecification):

    pass
class UML2_OpaqueExpression(ValueSpecification):

    pass
class UML2_TimeExpression(ValueSpecification):

    pass
class UML2_InstanceValue(ValueSpecification):

    pass
class UML2_Duration(ValueSpecification):

    pass
class Classifier:

    pass
class UML2_Signal(Classifier):

    pass
class UML2_InformationItem(Classifier):

    pass
class UML2_BehavioredClassifier(Classifier):

    pass
class UML2_Interface(Classifier):

    pass
class UML2_DataType(Classifier):

    pass
class UML2_TemplateableClassifier(Classifier):

    pass
class UML2_ParameterableClassifier(Classifier):

    pass
class UML2_Actor(Classifier):

    pass
class UML2_Artifact(Classifier):

    pass
class UML2_StructuredClassifier(Classifier):

    pass
class ObjectNode:

    pass
class UML2_CentralBufferNode(ObjectNode):

    pass
class UML2_ExpansionNode(ObjectNode):

    pass
class UML2_ActivityParameterNode(ObjectNode):

    pass
class UML2_Pin(ObjectNode):

    pass
class Node:

    pass
class UML2_ExecutionEnvironment(Node):

    pass
class UML2_Feature:

    pass
class UML2_Device(Node):

    pass
class EncapsulatedClassifier:

    pass
class Artifact:

    pass
class UML2_DeploymentSpecification(Artifact):

    pass
class Feature:

    pass
class UML2_Connector(Feature):

    pass
class UML2_BehavioralFeature(Feature):

    pass
class UML2_StructuralFeatureAction:

    pass
class BehavioralFeature:

    pass
class UML2_Reception(BehavioralFeature):

    pass
class DataType:

    pass
class UML2_PrimitiveType(DataType):

    pass
class UML2_Enumeration(DataType):

    pass
class UML2_Interval(ValueSpecification):

    pass
class LiteralSpecification:

    pass
class UML2_LiteralUnlimitedNatural(LiteralSpecification):

    pass
class UML2_LiteralNull(LiteralSpecification):

    pass
class UML2_LiteralString(LiteralSpecification):

    pass
class UML2_LiteralBoolean(LiteralSpecification):

    pass
class UML2_LiteralInteger(LiteralSpecification):

    pass
class UML2_Association(Classifier):

    pass
class BehavioredClassifier:

    pass
class UML2_Collaboration(BehavioredClassifier, StructuredClassifier):

    pass
class UML2_Class(BehavioredClassifier, EncapsulatedClassifier):

    pass
class UML2_UseCase(BehavioredClassifier):

    pass
class Property:

    pass
class UML2_ExtensionEnd(Property):

    pass
class UML2_Port(Property):

    pass
class TypedElement:

    pass
class UML2_ObjectNode(TypedElement):

    pass
class UML2_Variable(TypedElement):

    pass
class UML2_Parameter(TypedElement):

    pass
class UML2_Operation(BehavioralFeature, TypedElement):

    pass
class UML2_StructuralFeature(Feature, TypedElement):

    pass
class UML2_ValueSpecification(TypedElement):

    pass
class WriteStructuralFeatureAction:

    pass
class UML2_DurationObservationAction(WriteStructuralFeatureAction):

    pass
class UML2_RemoveStructuralFeatureValueAction(WriteStructuralFeatureAction):

    pass
class UML2_AddStructuralFeatureValueAction(WriteStructuralFeatureAction):

    pass
class UML2_TimeObservationAction(WriteStructuralFeatureAction):

    pass
class Behavior:

    pass
class UML2_Activity(Behavior):

    pass
class UML2_StateMachine(Behavior):

    pass
class UML2_Interaction(Behavior):

    pass
class StructuralFeatureAction:

    pass
class UML2_ReadStructuralFeatureAction(StructuralFeatureAction):

    pass
class UML2_WriteStructuralFeatureAction(StructuralFeatureAction):

    pass
class UML2_ClearStructuralFeatureAction(StructuralFeatureAction):

    pass
class Type:

    pass
class UML2_Classifier(Type):

    pass