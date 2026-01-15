from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class UML2_Action:

    pass
class Artifact:

    pass
class UML2_DeploymentSpecification(Artifact):

    pass
class OpaqueExpression:

    pass
class UML2_Expression(OpaqueExpression):

    pass
class InputPin:

    pass
class UML2_ValuePin(InputPin):

    pass
class CreateLinkAction:

    pass
class UML2_CreateLinkObjectAction(CreateLinkAction):

    pass
class UML2_Type:

    pass
class UML2_TypedElement:

    pass
class StructuralFeature:

    pass
class UML2_Property(StructuralFeature):

    pass
class DataType:

    pass
class UML2_PrimitiveType(DataType):

    pass
class TypedElement:

    pass
class UML2_Variable(TypedElement):

    pass
class UML2_ObjectNode(TypedElement):

    pass
class UML2_Parameter(TypedElement):

    pass
class Interval:

    pass
class UML2_DurationInterval(Interval):

    pass
class UML2_TimeInterval(Interval):

    pass
class StructuredActivityNode:

    pass
class UML2_ExpansionRegion(StructuredActivityNode):

    pass
class UML2_LoopNode(StructuredActivityNode):

    pass
class UML2_ConditionalNode(StructuredActivityNode):

    pass
class Type:

    pass
class UML2_Classifier(Type):

    pass
class WriteVariableAction:

    pass
class UML2_AddVariableValueAction(WriteVariableAction):

    pass
class UML2_RemoveVariableValueAction(WriteVariableAction):

    pass
class StateMachine:

    pass
class UML2_ProtocolStateMachine(StateMachine):

    pass
class EncapsulatedClassifier:

    pass
class BehavioredClassifier:

    pass
class UML2_UseCase(BehavioredClassifier):

    pass
class UML2_Class(BehavioredClassifier, EncapsulatedClassifier):

    pass
class LiteralSpecification:

    pass
class UML2_LiteralString(LiteralSpecification):

    pass
class UML2_LiteralUnlimitedNatural(LiteralSpecification):

    pass
class UML2_LiteralInteger(LiteralSpecification):

    pass
class UML2_LiteralBoolean(LiteralSpecification):

    pass
class UML2_LiteralNull(LiteralSpecification):

    pass
class UML2_ValueSpecification(TypedElement):

    pass
class WriteLinkAction:

    pass
class UML2_DestroyLinkAction(WriteLinkAction):

    pass
class UML2_CreateLinkAction(WriteLinkAction):

    pass
class UML2_Enumeration(DataType):

    pass
class UML2_Operation(TypedElement):

    pass
class UML2_StructuralFeature(TypedElement):

    pass
class CallAction:

    pass
class UML2_CallBehaviorAction(CallAction):

    pass
class UML2_CallOperationAction(CallAction):

    pass
class Node:

    pass
class UML2_ExecutionEnvironment(Node):

    pass
class UML2_Device(Node):

    pass
class Behavior:

    pass
class UML2_Activity(Behavior):

    pass
class UML2_Interaction(Behavior):

    pass
class UML2_StateMachine(Behavior):

    pass
class Class:

    pass
class UML2_Component(Class):

    pass
class UML2_Node(Class):

    pass
class UML2_Behavior(Class):

    pass
class UML2_Stereotype(Class):

    pass
class LinkAction:

    pass
class UML2_WriteLinkAction(LinkAction):

    pass
class UML2_ReadLinkAction(LinkAction):

    pass
class Association:

    pass
class UML2_CommunicationPath(Association):

    pass
class UML2_AssociationClass(Class, Association):

    pass
class UML2_Extension(Association):

    pass
class Property:

    pass
class UML2_ExtensionEnd(Property):

    pass
class UML2_Port(Property):

    pass
class VariableAction:

    pass
class UML2_WriteVariableAction(VariableAction):

    pass
class UML2_ClearVariableAction(VariableAction):

    pass
class UML2_ReadVariableAction(VariableAction):

    pass
class ObjectNode:

    pass
class UML2_Pin(ObjectNode):

    pass
class UML2_ExpansionNode(ObjectNode):

    pass
class UML2_CentralBufferNode(ObjectNode):

    pass
class UML2_ActivityParameterNode(ObjectNode):

    pass
class InvocationAction:

    pass
class UML2_SendObjectAction(InvocationAction):

    pass
class UML2_SendSignalAction(InvocationAction):

    pass
class UML2_CallAction(InvocationAction):

    pass
class UML2_BroadcastSignalAction(InvocationAction):

    pass
class StructuredClassifier:

    pass
class UML2_Collaboration(StructuredClassifier, BehavioredClassifier):

    pass
class UML2_EncapsulatedClassifier(StructuredClassifier):

    pass
class Pin:

    pass
class UML2_InputPin(Pin):

    pass
class ValueSpecification:

    pass
class UML2_InstanceValue(ValueSpecification):

    pass
class UML2_Duration(ValueSpecification):

    pass
class UML2_OpaqueExpression(ValueSpecification):

    pass
class UML2_LiteralSpecification(ValueSpecification):

    pass
class UML2_TimeExpression(ValueSpecification):

    pass
class UML2_Interval(ValueSpecification):

    pass
class CentralBufferNode:

    pass
class UML2_DataStoreNode(CentralBufferNode):

    pass
class UML2_OutputPin(Pin):

    pass
class WriteStructuralFeatureAction:

    pass
class UML2_AddStructuralFeatureValueAction(WriteStructuralFeatureAction):

    pass
class UML2_DurationObservationAction(WriteStructuralFeatureAction):

    pass
class UML2_RemoveStructuralFeatureValueAction(WriteStructuralFeatureAction):

    pass
class UML2_TimeObservationAction(WriteStructuralFeatureAction):

    pass
class Action:

    pass
class UML2_AcceptEventAction(Action):

    pass
class UML2_StructuralFeatureAction(Action):

    pass
class UML2_CreateObjectAction(Action):

    pass
class UML2_InvocationAction(Action):

    pass
class UML2_ReadLinkObjectEndAction(Action):

    pass
class UML2_ClearAssociationAction(Action):

    pass
class UML2_LinkAction(Action):

    pass
class UML2_ApplyFunctionAction(Action):

    pass
class UML2_ReadIsClassifiedObjectAction(Action):

    pass
class UML2_VariableAction(Action):

    pass
class UML2_StartOwnedBehaviorAction(Action):

    pass
class UML2_ReadLinkObjectEndQualifierAction(Action):

    pass
class UML2_ReclassifyObjectAction(Action):

    pass
class UML2_ReplyAction(Action):

    pass
class UML2_ReadExtentAction(Action):

    pass
class UML2_TestIdentityAction(Action):

    pass
class UML2_ReadSelfAction(Action):

    pass
class UML2_RaiseExceptionAction(Action):

    pass
class UML2_DestroyObjectAction(Action):

    pass
class UML2_StructuredActivityNode(Action):

    pass
class Classifier:

    pass
class UML2_Actor(Classifier):

    pass
class UML2_StructuredClassifier(Classifier):

    pass
class UML2_Interface(Classifier):

    pass
class UML2_TemplateableClassifier(Classifier):

    pass
class UML2_BehavioredClassifier(Classifier):

    pass
class UML2_Artifact(Classifier):

    pass
class UML2_InformationItem(Classifier):

    pass
class UML2_Association(Classifier):

    pass
class UML2_ParameterableClassifier(Classifier):

    pass
class UML2_Signal(Classifier):

    pass
class UML2_DataType(Classifier):

    pass
class StructuralFeatureAction:

    pass
class UML2_WriteStructuralFeatureAction(StructuralFeatureAction):

    pass
class UML2_ClearStructuralFeatureAction(StructuralFeatureAction):

    pass
class UML2_ReadStructuralFeatureAction(StructuralFeatureAction):

    pass
class AcceptEventAction:

    pass
class UML2_AcceptCallAction(AcceptEventAction):

    pass