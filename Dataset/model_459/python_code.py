from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class EncapsulatedClassifier:

    pass
class CreateLinkAction:

    pass
class UML2_CreateLinkObjectAction(CreateLinkAction):

    pass
class AcceptEventAction:

    pass
class UML2_AcceptCallAction(AcceptEventAction):

    pass
class LinkAction:

    pass
class UML2_WriteLinkAction(LinkAction):

    pass
class UML2_ReadLinkAction(LinkAction):

    pass
class StructuralFeatureAction:

    pass
class UML2_ClearStructuralFeatureAction(StructuralFeatureAction):

    pass
class UML2_ReadStructuralFeatureAction(StructuralFeatureAction):

    pass
class UML2_WriteStructuralFeatureAction(StructuralFeatureAction):

    pass
class StateMachine:

    pass
class UML2_ProtocolStateMachine(StateMachine):

    pass
class BehavioredClassifier:

    pass
class UML2_UseCase(BehavioredClassifier):

    pass
class UML2_Class(EncapsulatedClassifier, BehavioredClassifier):

    pass
class VariableAction:

    pass
class UML2_ReadVariableAction(VariableAction):

    pass
class UML2_WriteVariableAction(VariableAction):

    pass
class UML2_ClearVariableAction(VariableAction):

    pass
class WriteStructuralFeatureAction:

    pass
class UML2_DurationObservationAction(WriteStructuralFeatureAction):

    pass
class UML2_AddStructuralFeatureValueAction(WriteStructuralFeatureAction):

    pass
class UML2_RemoveStructuralFeatureValueAction(WriteStructuralFeatureAction):

    pass
class Artifact:

    pass
class UML2_DeploymentSpecification(Artifact):

    pass
class Association:

    pass
class UML2_CommunicationPath(Association):

    pass
class UML2_Extension(Association):

    pass
class Behavior:

    pass
class UML2_Activity(Behavior):

    pass
class UML2_StateMachine(Behavior):

    pass
class UML2_Interaction(Behavior):

    pass
class WriteLinkAction:

    pass
class UML2_DestroyLinkAction(WriteLinkAction):

    pass
class UML2_CreateLinkAction(WriteLinkAction):

    pass
class WriteVariableAction:

    pass
class UML2_AddVariableValueAction(WriteVariableAction):

    pass
class UML2_RemoveVariableValueAction(WriteVariableAction):

    pass
class UML2_Classifier:

    pass
class UML2_Action:

    pass
class StructuredClassifier:

    pass
class UML2_Collaboration(StructuredClassifier, BehavioredClassifier):

    pass
class UML2_EncapsulatedClassifier(StructuredClassifier):

    pass
class UML2_TimeObservationAction(WriteStructuralFeatureAction):

    pass
class InvocationAction:

    pass
class UML2_SendSignalAction(InvocationAction):

    pass
class UML2_CallAction(InvocationAction):

    pass
class UML2_SendObjectAction(InvocationAction):

    pass
class UML2_BroadcastSignalAction(InvocationAction):

    pass
class StructuredActivityNode:

    pass
class UML2_ConditionalNode(StructuredActivityNode):

    pass
class UML2_ExpansionRegion(StructuredActivityNode):

    pass
class UML2_LoopNode(StructuredActivityNode):

    pass
class Node:

    pass
class UML2_ExecutionEnvironment(Node):

    pass
class UML2_Device(Node):

    pass
class CallAction:

    pass
class UML2_CallOperationAction(CallAction):

    pass
class UML2_CallBehaviorAction(CallAction):

    pass
class Class:

    pass
class UML2_Component(Class):

    pass
class UML2_Stereotype(Class):

    pass
class UML2_Behavior(Class):

    pass
class UML2_AssociationClass(Class, Association):

    pass
class UML2_Node(Class):

    pass
class DataType:

    pass
class UML2_Enumeration(DataType):

    pass
class Classifier:

    pass
class UML2_TemplateableClassifier(Classifier):

    pass
class UML2_ParameterableClassifier(Classifier):

    pass
class UML2_Signal(Classifier):

    pass
class UML2_Actor(Classifier):

    pass
class UML2_InformationItem(Classifier):

    pass
class UML2_StructuredClassifier(Classifier):

    pass
class UML2_Interface(Classifier):

    pass
class UML2_BehavioredClassifier(Classifier):

    pass
class UML2_Artifact(Classifier):

    pass
class UML2_DataType(Classifier):

    pass
class UML2_Association(Classifier):

    pass
class Action:

    pass
class UML2_StructuredActivityNode(Action):

    pass
class UML2_ApplyFunctionAction(Action):

    pass
class UML2_ReclassifyObjectAction(Action):

    pass
class UML2_StartOwnedBehaviorAction(Action):

    pass
class UML2_ReplyAction(Action):

    pass
class UML2_RaiseExceptionAction(Action):

    pass
class UML2_TestIdentityAction(Action):

    pass
class UML2_AcceptEventAction(Action):

    pass
class UML2_LinkAction(Action):

    pass
class UML2_StructuralFeatureAction(Action):

    pass
class UML2_ReadExtentAction(Action):

    pass
class UML2_ReadLinkObjectEndAction(Action):

    pass
class UML2_CreateObjectAction(Action):

    pass
class UML2_ReadSelfAction(Action):

    pass
class UML2_ReadLinkObjectEndQualifierAction(Action):

    pass
class UML2_DestroyObjectAction(Action):

    pass
class UML2_VariableAction(Action):

    pass
class UML2_InvocationAction(Action):

    pass
class UML2_ReadIsClassifiedObjectAction(Action):

    pass
class UML2_PrimitiveType(DataType):

    pass
class UML2_ClearAssociationAction(Action):

    pass