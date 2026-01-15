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

class CreateLinkAction:

    pass
class MessageEnd:

    pass
class Realization:

    pass
class DataType:

    pass
class AcceptEventAction:

    pass
class Artifact:

    pass
class StructuralFeature:

    pass
class IntervalConstraint:

    pass
class Feature:

    pass
class DeployedArtifact:

    pass
class Property:

    pass
class Package:

    pass
class WriteLinkAction:

    pass
class EncapsulatedClassifier:

    pass
class State:

    pass
class BehavioralFeature:

    pass
class InstanceSpecification:

    pass
class OpaqueExpression:

    pass
class DeploymentTarget:

    pass
class InvocationAction:

    pass
class StateMachine:

    pass
class ExecutableNode:

    pass
class Type:

    pass
class Pin:

    pass
class InputPin:

    pass
class Abstraction:

    pass
class Transition:

    pass
class WriteStructuralFeatureAction:

    pass
class Node:

    pass
class FinalNode:

    pass
class LinkAction:

    pass
class CentralBufferNode:

    pass
class Trigger:

    pass
class Association:

    pass
class Class:

    pass
class ControlNode:

    pass
class Interval:

    pass
class ConnectableElement:

    pass
class VariableAction:

    pass
class Classifier:

    pass
class ObjectNode:

    pass
class Behavior:

    pass
class MessageTrigger:

    pass
class StructuredClassifier:

    pass
class BehavioredClassifier:

    pass
class InteractionOccurrence:

    pass
class Dependency:

    pass
class Vertex:

    pass
class RedefinableElement:

    pass
class Namespace:

    pass
class Element:

    pass
class UML2WithID_Realization(Element, Abstraction):

    pass
class UML2WithID_PrimitiveType(Element, DataType):

    pass
class UML2WithID_InformationItem(Classifier, Element):

    pass
class UML2WithID_BehavioralFeature(Feature, Namespace, Element):

    pass
class UML2WithID_Connector(Feature, Element):

    pass
class UML2WithID_FinalNode(Element, ControlNode):

    pass
class UML2WithID_ReadLinkAction(LinkAction, Element):

    pass
class UML2WithID_DeploymentSpecification(Artifact, Element):

    pass
class UML2WithID_Deployment(Dependency, Element):

    pass
class UML2WithID_ExecutionEnvironment(Node, Element):

    pass
class UML2WithID_Pin(Element, ObjectNode):

    pass
class UML2WithID_Gate(MessageEnd, Element):

    pass
class UML2WithID_AddStructuralFeatureValueAction(WriteStructuralFeatureAction, Element):

    pass
class UML2WithID_Profile(Package, Element):

    pass
class UML2WithID_ProtocolStateMachine(StateMachine, Element):

    pass
class UML2WithID_Behavior(Class, Element):

    pass
class UML2WithID_DurationConstraint(IntervalConstraint, Element):

    pass
class UML2WithID_Action(Element, ExecutableNode):

    pass
class UML2WithID_Permission(Dependency, Element):

    pass
class UML2WithID_Port(Property, Element):

    pass
class UML2WithID_OutputPin(Pin, Element):

    pass
class UML2WithID_State(Vertex, Namespace, Element, RedefinableElement):

    pass
class UML2WithID_CallAction(Element, InvocationAction):

    pass
class UML2WithID_Stereotype(Element, Class):

    pass
class UML2WithID_BehavioredClassifier(Classifier, Element):

    pass
class UML2WithID_TemplateableClassifier(Classifier, Element):

    pass
class UML2WithID_EnumerationLiteral(InstanceSpecification, Element):

    pass
class UML2WithID_ChangeTrigger(Trigger, Element):

    pass
class UML2WithID_DurationInterval(Interval, Element):

    pass
class UML2WithID_Extension(Association, Element):

    pass
class UML2WithID_Model(Package, Element):

    pass
class UML2WithID_TimeTrigger(Trigger, Element):

    pass
class UML2WithID_Association(Classifier, Element):

    pass
class UML2WithID_MessageTrigger(Trigger, Element):

    pass
class UML2WithID_Expression(OpaqueExpression, Element):

    pass
class UML2WithID_Classifier(Type, Namespace, Element, RedefinableElement):

    pass
class UML2WithID_CommunicationPath(Association, Element):

    pass
class UML2WithID_ExpansionNode(Element, ObjectNode):

    pass
class UML2WithID_Region(Namespace, Element, RedefinableElement):

    pass
class UML2WithID_StateMachine(Behavior, Element):

    pass
class UML2WithID_Signal(Classifier, Element):

    pass
class UML2WithID_InitialNode(Element, ControlNode):

    pass
class UML2WithID_ActivityFinalNode(Element, FinalNode):

    pass
class UML2WithID_ValuePin(InputPin, Element):

    pass
class UML2WithID_Node(Element, Class, DeploymentTarget):

    pass
class UML2WithID_Interface(Classifier, Element):

    pass
class UML2WithID_FlowFinalNode(Element, FinalNode):

    pass
class UML2WithID_MergeNode(Element, ControlNode):

    pass
class UML2WithID_WriteLinkAction(LinkAction, Element):

    pass
class UML2WithID_AcceptCallAction(AcceptEventAction, Element):

    pass
class UML2WithID_StructuredClassifier(Classifier, Element):

    pass
class UML2WithID_TimeObservationAction(WriteStructuralFeatureAction, Element):

    pass
class UML2WithID_Activity(Behavior, Element):

    pass
class UML2WithID_ExtensionPoint(Element, RedefinableElement):

    pass
class UML2WithID_SendSignalAction(InvocationAction, Element):

    pass
class UML2WithID_Pseudostate(Vertex, Element):

    pass
class UML2WithID_Substitution(Realization, Element):

    pass
class UML2WithID_CentralBufferNode(ObjectNode, Element):

    pass
class UML2WithID_UseCase(BehavioredClassifier, Element):

    pass
class UML2WithID_AnyTrigger(MessageTrigger, Element):

    pass
class UML2WithID_CreateLinkObjectAction(CreateLinkAction, Element):

    pass
class UML2WithID_Artifact(Classifier, Element, DeployedArtifact):

    pass
class UML2WithID_CallTrigger(MessageTrigger, Element):

    pass
class UML2WithID_Usage(Dependency, Element):

    pass
class UML2WithID_ConnectionPointReference(Vertex, Element):

    pass
class UML2WithID_Device(Node, Element):

    pass
class UML2WithID_ActivityParameterNode(Element, ObjectNode):

    pass
class UML2WithID_DataType(Classifier, Element):

    pass
class UML2WithID_DataStoreNode(CentralBufferNode, Element):

    pass
class UML2WithID_DurationObservationAction(WriteStructuralFeatureAction, Element):

    pass
class UML2WithID_Feature(Element, RedefinableElement):

    pass
class UML2WithID_WriteVariableAction(VariableAction, Element):

    pass
class UML2WithID_FinalState(Element, State):

    pass
class UML2WithID_Transition(Element, RedefinableElement):

    pass
class UML2WithID_DecisionNode(Element, ControlNode):

    pass
class UML2WithID_Enumeration(Element, DataType):

    pass
class UML2WithID_ExtensionEnd(Property, Element):

    pass
class UML2WithID_NamedElement(Element):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class UML2WithID_RedefinableTemplateSignature(Element, RedefinableElement):

    pass
class UML2WithID_InputPin(Pin, Element):

    pass
class UML2WithID_ParameterableClassifier(Classifier, Element):

    pass
class UML2WithID_Manifestation(Element, Abstraction):

    pass
class UML2WithID_Reception(BehavioralFeature, Element):

    pass
class UML2WithID_Property(Element, StructuralFeature, ConnectableElement, DeploymentTarget):

    pass
class UML2WithID_TimeConstraint(Element, IntervalConstraint):

    pass
class UML2WithID_ClearVariableAction(Element, VariableAction):

    pass
class UML2WithID_JoinNode(Element, ControlNode):

    pass
class UML2WithID_Component(Class, Element):

    pass
class UML2WithID_ProtocolTransition(Transition, Element):

    pass
class UML2WithID_Collaboration(BehavioredClassifier, StructuredClassifier, Element):

    pass
class UML2WithID_ReadVariableAction(VariableAction, Element):

    pass
class UML2WithID_SendObjectAction(InvocationAction, Element):

    pass
class UML2WithID_Implementation(Realization, Element):

    pass
class UML2WithID_Abstraction(Dependency, Element):

    pass
class UML2WithID_AssociationClass(Class, Association, Element):

    pass
class UML2WithID_Actor(Classifier, Element):

    pass
class UML2WithID_CreateLinkAction(Element, WriteLinkAction):

    pass
class UML2WithID_BroadcastSignalAction(InvocationAction, Element):

    pass
class UML2WithID_Class(BehavioredClassifier, EncapsulatedClassifier, Element):

    pass
class UML2WithID_EncapsulatedClassifier(StructuredClassifier, Element):

    pass
class UML2WithID_PartDecomposition(Element, InteractionOccurrence):

    pass
class UML2WithID_ActivityNode(Element, RedefinableElement):

    pass
class UML2WithID_RemoveStructuralFeatureValueAction(WriteStructuralFeatureAction, Element):

    pass
class UML2WithID_SignalTrigger(MessageTrigger, Element):

    pass
class UML2WithID_TimeInterval(Interval, Element):

    pass
class UML2WithID_ForkNode(Element, ControlNode):

    pass
class UML2WithID_DestroyLinkAction(Element, WriteLinkAction):

    pass
class InteractionFragment:

    pass
class UML2WithID_InteractionOccurrence(InteractionFragment, Element):

    pass
class UML2WithID_Continuation(InteractionFragment, Element):

    pass
class UML2WithID_InteractionOperand(InteractionFragment, Namespace, Element):

    pass
class UML2WithID_Interaction(InteractionFragment, Behavior, Element):

    pass
class UML2WithID_StateInvariant(InteractionFragment, Element):

    pass
class UML2WithID_CombinedFragment(InteractionFragment, Element):

    pass
class UML2WithID_EventOccurrence(MessageEnd, InteractionFragment, Element):

    pass
class UML2WithID_ExecutionOccurrence(InteractionFragment, Element):

    pass
class LiteralSpecification:

    pass
class UML2WithID_LiteralString(LiteralSpecification, Element):

    pass
class UML2WithID_LiteralNull(LiteralSpecification, Element):

    pass
class UML2WithID_LiteralBoolean(LiteralSpecification, Element):

    pass
class UML2WithID_LiteralUnlimitedNatural(LiteralSpecification, Element):

    pass
class UML2WithID_LiteralInteger(LiteralSpecification, Element):

    pass
class ActivityEdge:

    pass
class UML2WithID_ObjectFlow(Element, ActivityEdge):

    pass
class UML2WithID_ControlFlow(Element, ActivityEdge):

    pass
class StructuralFeatureAction:

    pass
class UML2WithID_ReadStructuralFeatureAction(Element, StructuralFeatureAction):

    pass
class UML2WithID_ClearStructuralFeatureAction(Element, StructuralFeatureAction):

    pass
class UML2WithID_WriteStructuralFeatureAction(Element, StructuralFeatureAction):

    pass
class CallAction:

    pass
class UML2WithID_CallOperationAction(CallAction, Element):

    pass
class UML2WithID_CallBehaviorAction(CallAction, Element):

    pass
class NamedElement:

    pass
class UML2WithID_ConnectableElement(NamedElement, Element):

    pass
class UML2WithID_PackageableElement(NamedElement, Element):

    pass
class UML2WithID_Trigger(NamedElement, Element):

    pass
class UML2WithID_Message(NamedElement, Element):

    pass
class UML2WithID_ActivityPartition(NamedElement, Element):

    pass
class UML2WithID_RedefinableElement(NamedElement, Element):

    pass
class UML2WithID_TypedElement(NamedElement, Element):

    pass
class UML2WithID_Include(NamedElement, Element):

    pass
class UML2WithID_ParameterSet(NamedElement, Element):

    pass
class UML2WithID_DeploymentTarget(NamedElement, Element):

    pass
class UML2WithID_Extend(NamedElement, Element):

    pass
class UML2WithID_Namespace(NamedElement, Element):

    pass
class UML2WithID_Vertex(NamedElement, Element):

    pass
class UML2WithID_GeneralOrdering(NamedElement, Element):

    pass
class UML2WithID_DeployedArtifact(NamedElement, Element):

    pass
class UML2WithID_CollaborationOccurrence(NamedElement, Element):

    pass
class UML2WithID_MessageEnd(NamedElement, Element):

    pass
class UML2WithID_Lifeline(NamedElement, Element):

    pass
class UML2WithID_InteractionFragment(NamedElement, Element):

    pass
class TypedElement:

    pass
class UML2WithID_Variable(TypedElement, ConnectableElement, Element):

    pass
class UML2WithID_StructuralFeature(Feature, Element, TypedElement):

    pass
class UML2WithID_Parameter(Element, ConnectableElement, TypedElement):

    pass
class UML2WithID_Operation(BehavioralFeature, TypedElement, Element):

    pass
class UML2WithID_ValueSpecification(Element, TypedElement):

    pass
class ActivityNode:

    pass
class UML2WithID_ExecutableNode(ActivityNode, Element):

    pass
class UML2WithID_ControlNode(ActivityNode, Element):

    pass
class UML2WithID_ObjectNode(ActivityNode, TypedElement, Element):

    pass
class UML2WithID_ActivityEdge(Element, RedefinableElement):

    pass
class ValueSpecification:

    pass
class UML2WithID_Interval(ValueSpecification, Element):

    pass
class UML2WithID_OpaqueExpression(ValueSpecification, Element):

    pass
class UML2WithID_TimeExpression(ValueSpecification, Element):

    pass
class UML2WithID_Duration(ValueSpecification, Element):

    pass
class UML2WithID_InstanceValue(ValueSpecification, Element):

    pass
class UML2WithID_LiteralSpecification(ValueSpecification, Element):

    pass
class WriteVariableAction:

    pass
class UML2WithID_RemoveVariableValueAction(Element, WriteVariableAction):

    pass
class UML2WithID_AddVariableValueAction(WriteVariableAction, Element):

    pass
class EventOccurrence:

    pass
class UML2WithID_Stop(Element, EventOccurrence):

    pass
class Constraint:

    pass
class UML2WithID_InteractionConstraint(Element, Constraint):

    pass
class UML2WithID_IntervalConstraint(Constraint, Element):

    pass
class Action:

    pass
class UML2WithID_ApplyFunctionAction(Action, Element):

    pass
class UML2WithID_StructuredActivityNode(Element, Namespace, Action):

    pass
class UML2WithID_ReadSelfAction(Element, Action):

    pass
class UML2WithID_ReadLinkObjectEndQualifierAction(Element, Action):

    pass
class UML2WithID_StructuralFeatureAction(Action, Element):

    pass
class UML2WithID_TestIdentityAction(Element, Action):

    pass
class UML2WithID_ReadExtentAction(Action, Element):

    pass
class UML2WithID_VariableAction(Element, Action):

    pass
class UML2WithID_RaiseExceptionAction(Action, Element):

    pass
class UML2WithID_DestroyObjectAction(Element, Action):

    pass
class UML2WithID_LinkAction(Action, Element):

    pass
class UML2WithID_ReclassifyObjectAction(Element, Action):

    pass
class UML2WithID_CreateObjectAction(Action, Element):

    pass
class UML2WithID_ClearAssociationAction(Element, Action):

    pass
class UML2WithID_StartOwnedBehaviorAction(Action, Element):

    pass
class UML2WithID_ReadIsClassifiedObjectAction(Element, Action):

    pass
class UML2WithID_ReadLinkObjectEndAction(Element, Action):

    pass
class UML2WithID_AcceptEventAction(Element, Action):

    pass
class UML2WithID_InvocationAction(Action, Element):

    pass
class UML2WithID_ReplyAction(Element, Action):

    pass
class StructuredActivityNode:

    pass
class UML2WithID_ExpansionRegion(StructuredActivityNode, Element):

    pass
class UML2WithID_LoopNode(StructuredActivityNode, Element):

    pass
class UML2WithID_ConditionalNode(StructuredActivityNode, Element):

    pass
class PackageableElement:

    pass
class UML2WithID_InformationFlow(PackageableElement, Element):

    pass
class UML2WithID_InstanceSpecification(PackageableElement, DeployedArtifact, Element, DeploymentTarget):

    pass
class UML2WithID_Dependency(PackageableElement, Element):

    pass
class UML2WithID_PrimitiveFunction(PackageableElement, Element):

    pass
class UML2WithID_Package(PackageableElement, Namespace, Element):

    pass
class UML2WithID_Constraint(PackageableElement, Element):

    pass
class UML2WithID_Type(PackageableElement, Element):

    pass
class UML2WithID_GeneralizationSet(PackageableElement, Element):

    pass