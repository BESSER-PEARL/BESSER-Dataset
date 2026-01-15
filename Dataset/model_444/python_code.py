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

class Type:

    pass
class BehavioralFeature:

    pass
class InstanceSpecification:

    pass
class InputPin:

    pass
class FinalNode:

    pass
class Transition:

    pass
class OpaqueExpression:

    pass
class StructuralFeatureAction:

    pass
class Package:

    pass
class StructuralFeature:

    pass
class DataType:

    pass
class WriteVariableAction:

    pass
class StructuredClassifier:

    pass
class Realization:

    pass
class InteractionOccurrence:

    pass
class EncapsulatedClassifier:

    pass
class Trigger:

    pass
class AcceptEventAction:

    pass
class State:

    pass
class CentralBufferNode:

    pass
class Abstraction:

    pass
class LiteralSpecification:

    pass
class Vertex:

    pass
class ObjectNode:

    pass
class Interval:

    pass
class VariableAction:

    pass
class Feature:

    pass
class Namespace:

    pass
class BehavioredClassifier:

    pass
class Property:

    pass
class Association:

    pass
class Class:

    pass
class Node:

    pass
class CallAction:

    pass
class MessageEnd:

    pass
class IntervalConstraint:

    pass
class DeployedArtifact:

    pass
class DeploymentTarget:

    pass
class StateMachine:

    pass
class Classifier:

    pass
class EventOccurrence:

    pass
class WriteLinkAction:

    pass
class ActivityNode:

    pass
class Constraint:

    pass
class ControlNode:

    pass
class TypedElement:

    pass
class ConnectableElement:

    pass
class RedefinableElement:

    pass
class MessageTrigger:

    pass
class ValueSpecification:

    pass
class LinkAction:

    pass
class WriteStructuralFeatureAction:

    pass
class ActivityEdge:

    pass
class ExecutableNode:

    pass
class InteractionFragment:

    pass
class Behavior:

    pass
class CreateLinkAction:

    pass
class Dependency:

    pass
class Action:

    pass
class PackageableElement:

    pass
class StructuredActivityNode:

    pass
class Pin:

    pass
class Artifact:

    pass
class NamedElement:

    pass
class Element:

    pass
class UML2WithID_InstanceSpecification(PackageableElement, Element, DeploymentTarget, DeployedArtifact):

    pass
class UML2WithID_FinalState(State, Element):

    pass
class UML2WithID_Model(Element, Package):

    pass
class UML2WithID_ValuePin(Element, InputPin):

    pass
class UML2WithID_ForkNode(ControlNode, Element):

    pass
class UML2WithID_Constraint(PackageableElement, Element):

    pass
class UML2WithID_PrimitiveType(Element, DataType):

    pass
class UML2WithID_Action(ExecutableNode, Element):

    pass
class UML2WithID_LoopNode(Element, StructuredActivityNode):

    pass
class UML2WithID_ReadIsClassifiedObjectAction(Action, Element):

    pass
class UML2WithID_StructuralFeature(Element, TypedElement, Feature):

    pass
class UML2WithID_Abstraction(Element, Dependency):

    pass
class UML2WithID_Manifestation(Abstraction, Element):

    pass
class UML2WithID_ActivityParameterNode(ObjectNode, Element):

    pass
class UML2WithID_Continuation(InteractionFragment, Element):

    pass
class UML2WithID_State(Vertex, Element, RedefinableElement, Namespace):

    pass
class UML2WithID_Implementation(Realization, Element):

    pass
class UML2WithID_Stop(Element, EventOccurrence):

    pass
class UML2WithID_ConditionalNode(Element, StructuredActivityNode):

    pass
class UML2WithID_LiteralInteger(LiteralSpecification, Element):

    pass
class UML2WithID_Feature(Element, RedefinableElement):

    pass
class UML2WithID_MessageTrigger(Trigger, Element):

    pass
class UML2WithID_CallBehaviorAction(CallAction, Element):

    pass
class UML2WithID_VariableAction(Element, Action):

    pass
class UML2WithID_ReplyAction(Action, Element):

    pass
class UML2WithID_Lifeline(Element, NamedElement):

    pass
class UML2WithID_AddStructuralFeatureValueAction(Element, WriteStructuralFeatureAction):

    pass
class UML2WithID_Variable(Element, TypedElement, ConnectableElement):

    pass
class UML2WithID_RedefinableTemplateSignature(Element, RedefinableElement):

    pass
class UML2WithID_TimeExpression(Element, ValueSpecification):

    pass
class UML2WithID_ActivityNode(Element, RedefinableElement):

    pass
class UML2WithID_ProtocolStateMachine(Element, StateMachine):

    pass
class UML2WithID_EncapsulatedClassifier(Element, StructuredClassifier):

    pass
class UML2WithID_ActivityEdge(Element, RedefinableElement):

    pass
class UML2WithID_Permission(Element, Dependency):

    pass
class UML2WithID_IntervalConstraint(Constraint, Element):

    pass
class UML2WithID_Interval(Element, ValueSpecification):

    pass
class UML2WithID_CombinedFragment(InteractionFragment, Element):

    pass
class UML2WithID_DeploymentSpecification(Artifact, Element):

    pass
class UML2WithID_Activity(Behavior, Element):

    pass
class UML2WithID_DurationObservationAction(Element, WriteStructuralFeatureAction):

    pass
class UML2WithID_ActivityFinalNode(Element, FinalNode):

    pass
class UML2WithID_Device(Node, Element):

    pass
class UML2WithID_EnumerationLiteral(Element, InstanceSpecification):

    pass
class UML2WithID_ConnectableElement(Element, NamedElement):

    pass
class UML2WithID_FlowFinalNode(Element, FinalNode):

    pass
class UML2WithID_PartDecomposition(InteractionOccurrence, Element):

    pass
class UML2WithID_Class(Element, BehavioredClassifier, EncapsulatedClassifier):

    pass
class UML2WithID_AcceptCallAction(Element, AcceptEventAction):

    pass
class UML2WithID_TimeObservationAction(Element, WriteStructuralFeatureAction):

    pass
class UML2WithID_GeneralOrdering(Element, NamedElement):

    pass
class UML2WithID_Enumeration(Element, DataType):

    pass
class UML2WithID_ControlNode(ActivityNode, Element):

    pass
class UML2WithID_DeploymentTarget(Element, NamedElement):

    pass
class UML2WithID_MessageEnd(Element, NamedElement):

    pass
class UML2WithID_Region(Element, RedefinableElement, Namespace):

    pass
class UML2WithID_Parameter(Element, TypedElement, ConnectableElement):

    pass
class UML2WithID_AcceptEventAction(Action, Element):

    pass
class UML2WithID_Deployment(Element, Dependency):

    pass
class UML2WithID_ExecutionEnvironment(Node, Element):

    pass
class UML2WithID_Extension(Element, Association):

    pass
class UML2WithID_Association(Element, Classifier):

    pass
class UML2WithID_ObjectNode(ActivityNode, Element, TypedElement):

    pass
class UML2WithID_CollaborationOccurrence(Element, NamedElement):

    pass
class UML2WithID_OutputPin(Element, Pin):

    pass
class UML2WithID_Dependency(PackageableElement, Element):

    pass
class UML2WithID_ReadStructuralFeatureAction(Element, StructuralFeatureAction):

    pass
class UML2WithID_StateMachine(Behavior, Element):

    pass
class UML2WithID_CommunicationPath(Element, Association):

    pass
class UML2WithID_ChangeTrigger(Trigger, Element):

    pass
class UML2WithID_WriteLinkAction(LinkAction, Element):

    pass
class UML2WithID_Behavior(Class, Element):

    pass
class UML2WithID_ActivityPartition(Element, NamedElement):

    pass
class UML2WithID_Substitution(Realization, Element):

    pass
class UML2WithID_Package(PackageableElement, Element, Namespace):

    pass
class UML2WithID_ReadLinkObjectEndAction(Action, Element):

    pass
class UML2WithID_ValueSpecification(Element, TypedElement):

    pass
class UML2WithID_ParameterableClassifier(Element, Classifier):

    pass
class UML2WithID_ExecutionOccurrence(InteractionFragment, Element):

    pass
class UML2WithID_TimeConstraint(IntervalConstraint, Element):

    pass
class UML2WithID_ReadLinkObjectEndQualifierAction(Element, Action):

    pass
class UML2WithID_CreateLinkObjectAction(CreateLinkAction, Element):

    pass
class UML2WithID_ControlFlow(Element, ActivityEdge):

    pass
class UML2WithID_Include(Element, NamedElement):

    pass
class UML2WithID_Transition(Element, RedefinableElement):

    pass
class UML2WithID_BehavioralFeature(Element, Namespace, Feature):

    pass
class UML2WithID_Operation(Element, TypedElement, BehavioralFeature):

    pass
class UML2WithID_PackageableElement(Element, NamedElement):

    pass
class UML2WithID_DecisionNode(ControlNode, Element):

    pass
class UML2WithID_Realization(Abstraction, Element):

    pass
class UML2WithID_Type(PackageableElement, Element):

    pass
class UML2WithID_AssociationClass(Class, Element, Association):

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

class UML2WithID_Interface(Element, Classifier):

    pass
class UML2WithID_FinalNode(ControlNode, Element):

    pass
class UML2WithID_UseCase(Element, BehavioredClassifier):

    pass
class UML2WithID_ReadSelfAction(Action, Element):

    pass
class UML2WithID_InvocationAction(Action, Element):

    pass
class UML2WithID_CreateObjectAction(Element, Action):

    pass
class UML2WithID_Usage(Element, Dependency):

    pass
class UML2WithID_ExpansionNode(ObjectNode, Element):

    pass
class UML2WithID_Signal(Element, Classifier):

    pass
class UML2WithID_Connector(Element, Feature):

    pass
class UML2WithID_InstanceValue(Element, ValueSpecification):

    pass
class UML2WithID_TimeInterval(Element, Interval):

    pass
class UML2WithID_ApplyFunctionAction(Element, Action):

    pass
class UML2WithID_DurationConstraint(IntervalConstraint, Element):

    pass
class UML2WithID_Port(Element, Property):

    pass
class UML2WithID_InformationItem(Element, Classifier):

    pass
class UML2WithID_CallTrigger(MessageTrigger, Element):

    pass
class UML2WithID_ReadVariableAction(VariableAction, Element):

    pass
class UML2WithID_ClearVariableAction(VariableAction, Element):

    pass
class UML2WithID_StartOwnedBehaviorAction(Element, Action):

    pass
class UML2WithID_DestroyObjectAction(Action, Element):

    pass
class UML2WithID_InputPin(Element, Pin):

    pass
class UML2WithID_RemoveStructuralFeatureValueAction(Element, WriteStructuralFeatureAction):

    pass
class UML2WithID_Node(DeploymentTarget, Element, Class):

    pass
class UML2WithID_StructuralFeatureAction(Action, Element):

    pass
class UML2WithID_WriteVariableAction(VariableAction, Element):

    pass
class UML2WithID_Gate(Element, MessageEnd):

    pass
class UML2WithID_ClearAssociationAction(Action, Element):

    pass
class UML2WithID_PrimitiveFunction(PackageableElement, Element):

    pass
class UML2WithID_InteractionFragment(Element, NamedElement):

    pass
class UML2WithID_Duration(Element, ValueSpecification):

    pass
class UML2WithID_CentralBufferNode(ObjectNode, Element):

    pass
class UML2WithID_OpaqueExpression(Element, ValueSpecification):

    pass
class UML2WithID_Profile(Element, Package):

    pass
class UML2WithID_CallOperationAction(CallAction, Element):

    pass
class UML2WithID_Reception(Element, BehavioralFeature):

    pass
class UML2WithID_ReclassifyObjectAction(Element, Action):

    pass
class UML2WithID_ObjectFlow(ActivityEdge, Element):

    pass
class UML2WithID_LiteralNull(LiteralSpecification, Element):

    pass
class UML2WithID_Vertex(Element, NamedElement):

    pass
class UML2WithID_DataStoreNode(CentralBufferNode, Element):

    pass
class UML2WithID_DeployedArtifact(Element, NamedElement):

    pass
class UML2WithID_LinkAction(Action, Element):

    pass
class UML2WithID_CreateLinkAction(Element, WriteLinkAction):

    pass
class UML2WithID_LiteralUnlimitedNatural(LiteralSpecification, Element):

    pass
class UML2WithID_TypedElement(Element, NamedElement):

    pass
class UML2WithID_AnyTrigger(MessageTrigger, Element):

    pass
class UML2WithID_TestIdentityAction(Element, Action):

    pass
class UML2WithID_Artifact(Element, Classifier, DeployedArtifact):

    pass
class UML2WithID_LiteralBoolean(LiteralSpecification, Element):

    pass
class UML2WithID_TimeTrigger(Trigger, Element):

    pass
class UML2WithID_ExpansionRegion(Element, StructuredActivityNode):

    pass
class UML2WithID_ExtensionPoint(Element, RedefinableElement):

    pass
class UML2WithID_Actor(Element, Classifier):

    pass
class UML2WithID_ConnectionPointReference(Vertex, Element):

    pass
class UML2WithID_ClearStructuralFeatureAction(Element, StructuralFeatureAction):

    pass
class UML2WithID_JoinNode(ControlNode, Element):

    pass
class UML2WithID_Stereotype(Class, Element):

    pass
class UML2WithID_RedefinableElement(Element, NamedElement):

    pass
class UML2WithID_DataType(Element, Classifier):

    pass
class UML2WithID_EventOccurrence(InteractionFragment, Element, MessageEnd):

    pass
class UML2WithID_StructuredActivityNode(Element, Namespace, Action):

    pass
class UML2WithID_Classifier(Element, Type, Namespace, RedefinableElement):

    pass
class UML2WithID_Trigger(Element, NamedElement):

    pass
class UML2WithID_Interaction(InteractionFragment, Element, Behavior):

    pass
class UML2WithID_InformationFlow(PackageableElement, Element):

    pass
class UML2WithID_RaiseExceptionAction(Element, Action):

    pass
class UML2WithID_LiteralString(LiteralSpecification, Element):

    pass
class UML2WithID_BehavioredClassifier(Element, Classifier):

    pass
class UML2WithID_InitialNode(ControlNode, Element):

    pass
class UML2WithID_ProtocolTransition(Transition, Element):

    pass
class UML2WithID_Extend(Element, NamedElement):

    pass
class UML2WithID_Collaboration(StructuredClassifier, Element, BehavioredClassifier):

    pass
class UML2WithID_GeneralizationSet(PackageableElement, Element):

    pass
class UML2WithID_Property(DeploymentTarget, Element, StructuralFeature, ConnectableElement):

    pass
class UML2WithID_Pseudostate(Vertex, Element):

    pass
class UML2WithID_TemplateableClassifier(Element, Classifier):

    pass
class UML2WithID_Message(Element, NamedElement):

    pass
class UML2WithID_Namespace(Element, NamedElement):

    pass
class UML2WithID_Pin(ObjectNode, Element):

    pass
class UML2WithID_LiteralSpecification(Element, ValueSpecification):

    pass
class UML2WithID_StateInvariant(InteractionFragment, Element):

    pass
class UML2WithID_ParameterSet(Element, NamedElement):

    pass
class UML2WithID_ReadExtentAction(Element, Action):

    pass
class UML2WithID_ExecutableNode(ActivityNode, Element):

    pass
class UML2WithID_DestroyLinkAction(Element, WriteLinkAction):

    pass
class UML2WithID_ReadLinkAction(Element, LinkAction):

    pass
class UML2WithID_Component(Class, Element):

    pass
class UML2WithID_InteractionConstraint(Constraint, Element):

    pass
class UML2WithID_SignalTrigger(MessageTrigger, Element):

    pass
class UML2WithID_ExtensionEnd(Element, Property):

    pass
class UML2WithID_MergeNode(ControlNode, Element):

    pass
class UML2WithID_DurationInterval(Element, Interval):

    pass
class UML2WithID_WriteStructuralFeatureAction(Element, StructuralFeatureAction):

    pass
class UML2WithID_InteractionOperand(InteractionFragment, Element, Namespace):

    pass
class UML2WithID_InteractionOccurrence(InteractionFragment, Element):

    pass
class UML2WithID_RemoveVariableValueAction(WriteVariableAction, Element):

    pass
class UML2WithID_AddVariableValueAction(WriteVariableAction, Element):

    pass
class UML2WithID_StructuredClassifier(Element, Classifier):

    pass
class UML2WithID_Expression(OpaqueExpression, Element):

    pass
class InvocationAction:

    pass
class UML2WithID_BroadcastSignalAction(Element, InvocationAction):

    pass
class UML2WithID_CallAction(Element, InvocationAction):

    pass
class UML2WithID_SendSignalAction(Element, InvocationAction):

    pass
class UML2WithID_SendObjectAction(Element, InvocationAction):

    pass