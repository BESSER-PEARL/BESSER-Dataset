from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class AcceptEventAction:

    pass
class UML2_AcceptCallAction(AcceptEventAction):

    pass
class CallAction:

    pass
class UML2_CallBehaviorAction(CallAction):

    pass
class UML2_CallOperationAction(CallAction):

    pass
class EventOccurrence:

    pass
class UML2_Stop(EventOccurrence):

    pass
class ExecutableNode:

    pass
class UML2_Action(ExecutableNode):

    pass
class Transition:

    pass
class UML2_ProtocolTransition(Transition):

    pass
class TemplateSignature:

    pass
class Relationship:

    pass
class UML2_DirectedRelationship(Relationship):

    pass
class Package:

    pass
class UML2_Model(Package):

    pass
class UML2_Profile(Package):

    pass
class Constraint:

    pass
class UML2_InteractionConstraint(Constraint):

    pass
class UML2_IntervalConstraint(Constraint):

    pass
class TemplateParameter:

    pass
class UML2_ConnectableElementTemplateParameter(TemplateParameter):

    pass
class UML2_OperationTemplateParameter(TemplateParameter):

    pass
class Type:

    pass
class UML2_Element:

    pass
class IntervalConstraint:

    pass
class UML2_TimeConstraint(IntervalConstraint):

    pass
class UML2_DurationConstraint(IntervalConstraint):

    pass
class MessageEnd:

    pass
class UML2_Gate(MessageEnd):

    pass
class CreateLinkAction:

    pass
class UML2_CreateLinkObjectAction(CreateLinkAction):

    pass
class UML2_ClassifierTemplateParameter(TemplateParameter):

    pass
class WriteVariableAction:

    pass
class UML2_AddVariableValueAction(WriteVariableAction):

    pass
class UML2_RemoveVariableValueAction(WriteVariableAction):

    pass
class Pin:

    pass
class UML2_OutputPin(Pin):

    pass
class UML2_InputPin(Pin):

    pass
class Interval:

    pass
class UML2_TimeInterval(Interval):

    pass
class UML2_DurationInterval(Interval):

    pass
class ActivityEdge:

    pass
class UML2_ControlFlow(ActivityEdge):

    pass
class UML2_ObjectFlow(ActivityEdge):

    pass
class PackageImport:

    pass
class UML2_ProfileApplication(PackageImport):

    pass
class Association:

    pass
class UML2_Extension(Association):

    pass
class Class:

    pass
class UML2_Behavior(Class):

    pass
class UML2_Stereotype(Class):

    pass
class UML2_Component(Class):

    pass
class UML2_AssociationClass(Class, Association):

    pass
class Realization:

    pass
class UML2_Substitution(Realization):

    pass
class UML2_Implementation(Realization):

    pass
class DeployedArtifact:

    pass
class StateMachine:

    pass
class UML2_ProtocolStateMachine(StateMachine):

    pass
class Node:

    pass
class UML2_ExecutionEnvironment(Node):

    pass
class UML2_Device(Node):

    pass
class LinkEndData:

    pass
class UML2_LinkEndCreationData(LinkEndData):

    pass
class OpaqueExpression:

    pass
class UML2_Expression(OpaqueExpression):

    pass
class UML2_CommunicationPath(Association):

    pass
class TemplateableElement:

    pass
class UML2_Comment(TemplateableElement):

    pass
class UML2_NamedElement(TemplateableElement):

    pass
class UML2_StringExpression(TemplateableElement):

    pass
class ObjectNode:

    pass
class UML2_ExpansionNode(ObjectNode):

    pass
class UML2_ActivityParameterNode(ObjectNode):

    pass
class UML2_CentralBufferNode(ObjectNode):

    pass
class RedefinableElement:

    pass
class UML2_ActivityEdge(RedefinableElement):

    pass
class UML2_Feature(RedefinableElement):

    pass
class UML2_ExtensionPoint(RedefinableElement):

    pass
class UML2_Transition(RedefinableElement):

    pass
class UML2_RedefinableTemplateSignature(RedefinableElement, TemplateSignature):

    pass
class UML2_ActivityNode(RedefinableElement):

    pass
class InputPin:

    pass
class UML2_ValuePin(InputPin):

    pass
class InstanceSpecification:

    pass
class UML2_EnumerationLiteral(InstanceSpecification):

    pass
class StructuredActivityNode:

    pass
class UML2_ExpansionRegion(StructuredActivityNode):

    pass
class UML2_ConditionalNode(StructuredActivityNode):

    pass
class UML2_LoopNode(StructuredActivityNode):

    pass
class MessageTrigger:

    pass
class UML2_AnyTrigger(MessageTrigger):

    pass
class UML2_CallTrigger(MessageTrigger):

    pass
class WriteStructuralFeatureAction:

    pass
class UML2_RemoveStructuralFeatureValueAction(WriteStructuralFeatureAction):

    pass
class UML2_DurationObservationAction(WriteStructuralFeatureAction):

    pass
class UML2_TimeObservationAction(WriteStructuralFeatureAction):

    pass
class UML2_AddStructuralFeatureValueAction(WriteStructuralFeatureAction):

    pass
class CentralBufferNode:

    pass
class UML2_DataStoreNode(CentralBufferNode):

    pass
class InteractionOccurrence:

    pass
class UML2_PartDecomposition(InteractionOccurrence):

    pass
class Vertex:

    pass
class UML2_Pseudostate(Vertex):

    pass
class UML2_ConnectionPointReference(Vertex):

    pass
class BehavioralFeature:

    pass
class UML2_Reception(BehavioralFeature):

    pass
class ActivityNode:

    pass
class UML2_ExecutableNode(ActivityNode):

    pass
class UML2_ControlNode(ActivityNode):

    pass
class Abstraction:

    pass
class UML2_Realization(Abstraction):

    pass
class UML2_Manifestation(Abstraction):

    pass
class Behavior:

    pass
class UML2_Activity(Behavior):

    pass
class UML2_StateMachine(Behavior):

    pass
class Namespace:

    pass
class UML2_Region(RedefinableElement, Namespace):

    pass
class UML2_Classifier(RedefinableElement, Type, Namespace):

    pass
class UML2_State(RedefinableElement, Vertex, Namespace):

    pass
class DataType:

    pass
class UML2_PrimitiveType(DataType):

    pass
class ValueSpecification:

    pass
class UML2_Duration(ValueSpecification):

    pass
class UML2_TimeExpression(ValueSpecification):

    pass
class UML2_OpaqueExpression(ValueSpecification):

    pass
class UML2_InstanceValue(ValueSpecification):

    pass
class UML2_Interval(ValueSpecification):

    pass
class UML2_LiteralSpecification(ValueSpecification):

    pass
class DeploymentTarget:

    pass
class UML2_Node(Class, DeploymentTarget):

    pass
class ConnectableElement:

    pass
class StructuralFeature:

    pass
class UML2_Property(DeploymentTarget, StructuralFeature, ConnectableElement):

    pass
class Trigger:

    pass
class UML2_TimeTrigger(Trigger):

    pass
class UML2_ChangeTrigger(Trigger):

    pass
class UML2_MessageTrigger(Trigger):

    pass
class InteractionFragment:

    pass
class UML2_InteractionOperand(Namespace, InteractionFragment):

    pass
class UML2_StateInvariant(InteractionFragment):

    pass
class UML2_InteractionOccurrence(InteractionFragment):

    pass
class UML2_EventOccurrence(MessageEnd, InteractionFragment):

    pass
class UML2_Interaction(InteractionFragment, Behavior):

    pass
class UML2_Continuation(InteractionFragment):

    pass
class UML2_CombinedFragment(InteractionFragment):

    pass
class UML2_ExecutionOccurrence(InteractionFragment):

    pass
class ActivityGroup:

    pass
class UML2_InterruptibleActivityRegion(ActivityGroup):

    pass
class WriteLinkAction:

    pass
class UML2_DestroyLinkAction(WriteLinkAction):

    pass
class UML2_CreateLinkAction(WriteLinkAction):

    pass
class VariableAction:

    pass
class UML2_ReadVariableAction(VariableAction):

    pass
class UML2_ClearVariableAction(VariableAction):

    pass
class UML2_WriteVariableAction(VariableAction):

    pass
class NamedElement:

    pass
class UML2_DeployedArtifact(NamedElement):

    pass
class UML2_Trigger(NamedElement):

    pass
class UML2_DeploymentTarget(NamedElement):

    pass
class UML2_RedefinableElement(NamedElement):

    pass
class UML2_TypedElement(NamedElement):

    pass
class UML2_GeneralOrdering(NamedElement):

    pass
class UML2_Vertex(NamedElement):

    pass
class UML2_ActivityPartition(ActivityGroup, NamedElement):

    pass
class UML2_MessageEnd(NamedElement):

    pass
class UML2_Namespace(NamedElement):

    pass
class UML2_ParameterSet(NamedElement):

    pass
class UML2_InteractionFragment(NamedElement):

    pass
class UML2_Lifeline(NamedElement):

    pass
class UML2_CollaborationOccurrence(NamedElement):

    pass
class PackageableElement:

    pass
class UML2_InstanceSpecification(DeploymentTarget, PackageableElement, DeployedArtifact):

    pass
class UML2_Package(PackageableElement, Namespace):

    pass
class UML2_PrimitiveFunction(PackageableElement):

    pass
class UML2_Type(PackageableElement):

    pass
class UML2_Constraint(PackageableElement):

    pass
class UML2_GeneralizationSet(PackageableElement):

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
class StructuralFeatureAction:

    pass
class UML2_ReadStructuralFeatureAction(StructuralFeatureAction):

    pass
class UML2_WriteStructuralFeatureAction(StructuralFeatureAction):

    pass
class UML2_ClearStructuralFeatureAction(StructuralFeatureAction):

    pass
class State:

    pass
class UML2_FinalState(State):

    pass
class StructuredClassifier:

    pass
class UML2_EncapsulatedClassifier(StructuredClassifier):

    pass
class UML2_SignalTrigger(MessageTrigger):

    pass
class UML2_Message(NamedElement):

    pass
class Artifact:

    pass
class UML2_DeploymentSpecification(Artifact):

    pass
class UML2_Enumeration(DataType):

    pass
class Classifier:

    pass
class UML2_StructuredClassifier(Classifier):

    pass
class UML2_Interface(Classifier):

    pass
class UML2_InformationItem(Classifier):

    pass
class UML2_TemplateableClassifier(Classifier):

    pass
class UML2_Actor(Classifier):

    pass
class UML2_Artifact(Classifier, DeployedArtifact):

    pass
class UML2_DataType(Classifier):

    pass
class UML2_Association(Classifier, Relationship):

    pass
class UML2_Signal(Classifier):

    pass
class UML2_BehavioredClassifier(Classifier):

    pass
class UML2_ParameterableClassifier(Classifier):

    pass
class ParameterableElement:

    pass
class UML2_ConnectableElement(ParameterableElement, NamedElement):

    pass
class UML2_PackageableElement(ParameterableElement, NamedElement):

    pass
class MultiplicityElement:

    pass
class UML2_ConnectorEnd(MultiplicityElement):

    pass
class UML2_Pin(ObjectNode, MultiplicityElement):

    pass
class TypedElement:

    pass
class UML2_Variable(TypedElement, ConnectableElement, MultiplicityElement):

    pass
class UML2_Parameter(TypedElement, MultiplicityElement, ConnectableElement):

    pass
class UML2_ObjectNode(TypedElement, ActivityNode):

    pass
class UML2_Operation(TypedElement, ParameterableElement, BehavioralFeature, MultiplicityElement):

    pass
class UML2_ValueSpecification(TypedElement, ParameterableElement):

    pass
class Feature:

    pass
class UML2_BehavioralFeature(Feature, Namespace):

    pass
class UML2_Connector(Feature):

    pass
class UML2_StructuralFeature(TypedElement, Feature, MultiplicityElement):

    pass
class ControlNode:

    pass
class UML2_MergeNode(ControlNode):

    pass
class UML2_JoinNode(ControlNode):

    pass
class UML2_InitialNode(ControlNode):

    pass
class UML2_FinalNode(ControlNode):

    pass
class UML2_ForkNode(ControlNode):

    pass
class UML2_DecisionNode(ControlNode):

    pass
class DirectedRelationship:

    pass
class UML2_Include(DirectedRelationship, NamedElement):

    pass
class UML2_InformationFlow(PackageableElement, DirectedRelationship):

    pass
class UML2_PackageMerge(DirectedRelationship):

    pass
class UML2_Extend(DirectedRelationship, NamedElement):

    pass
class UML2_ElementImport(DirectedRelationship):

    pass
class UML2_ProtocolConformance(DirectedRelationship):

    pass
class UML2_Dependency(PackageableElement, DirectedRelationship):

    pass
class UML2_TemplateBinding(DirectedRelationship):

    pass
class UML2_PackageImport(DirectedRelationship):

    pass
class UML2_Generalization(DirectedRelationship):

    pass
class FinalNode:

    pass
class UML2_FlowFinalNode(FinalNode):

    pass
class UML2_ActivityFinalNode(FinalNode):

    pass
class LiteralSpecification:

    pass
class UML2_LiteralNull(LiteralSpecification):

    pass
class UML2_LiteralUnlimitedNatural(LiteralSpecification):

    pass
class UML2_LiteralString(LiteralSpecification):

    pass
class UML2_LiteralInteger(LiteralSpecification):

    pass
class UML2_LiteralBoolean(LiteralSpecification):

    pass
class EncapsulatedClassifier:

    pass
class BehavioredClassifier:

    pass
class UML2_UseCase(BehavioredClassifier):

    pass
class UML2_Collaboration(StructuredClassifier, BehavioredClassifier):

    pass
class UML2_Class(BehavioredClassifier, EncapsulatedClassifier):

    pass
class LinkAction:

    pass
class UML2_ReadLinkAction(LinkAction):

    pass
class UML2_WriteLinkAction(LinkAction):

    pass
class Element:

    pass
class UML2_QualifierValue(Element):

    pass
class UML2_MultiplicityElement(Element):

    pass
class UML2_Clause(Element):

    pass
class UML2_ActivityGroup(Element):

    pass
class UML2_ExceptionHandler(Element):

    pass
class UML2_TemplateSignature(Element):

    pass
class UML2_ParameterableElement(Element):

    pass
class UML2_LinkEndData(Element):

    pass
class UML2_TemplateParameter(Element):

    pass
class UML2_TemplateableElement(Element):

    pass
class UML2_Slot(Element):

    pass
class UML2_Relationship(Element):

    pass
class UML2_TemplateParameterSubstitution(Element):

    pass
class Action:

    pass
class UML2_TestIdentityAction(Action):

    pass
class UML2_DestroyObjectAction(Action):

    pass
class UML2_VariableAction(Action):

    pass
class UML2_CreateObjectAction(Action):

    pass
class UML2_ReplyAction(Action):

    pass
class UML2_ApplyFunctionAction(Action):

    pass
class UML2_AcceptEventAction(Action):

    pass
class UML2_StructuredActivityNode(ActivityGroup, Action, Namespace):

    pass
class UML2_ReadExtentAction(Action):

    pass
class UML2_ReadLinkObjectEndQualifierAction(Action):

    pass
class UML2_ReclassifyObjectAction(Action):

    pass
class UML2_StartOwnedBehaviorAction(Action):

    pass
class UML2_RaiseExceptionAction(Action):

    pass
class UML2_StructuralFeatureAction(Action):

    pass
class UML2_ReadLinkObjectEndAction(Action):

    pass
class UML2_LinkAction(Action):

    pass
class UML2_ReadSelfAction(Action):

    pass
class UML2_ReadIsClassifiedObjectAction(Action):

    pass
class UML2_InvocationAction(Action):

    pass
class UML2_ClearAssociationAction(Action):

    pass
class Dependency:

    pass
class UML2_Abstraction(Dependency):

    pass
class UML2_Deployment(Dependency):

    pass
class UML2_Permission(Dependency):

    pass
class UML2_Usage(Dependency):

    pass
class Property:

    pass
class UML2_Port(Property):

    pass
class UML2_ExtensionEnd(Property):

    pass