from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class LinkAction:

    pass
class DeployedArtifact:

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


class Constraint:

    pass
class AcceptEventAction:

    pass
class Type:

    pass
class Artifact:

    pass
class ExecutableNode:

    pass
class IntervalConstraint:

    pass
class State:

    pass
class Interval:

    pass
class StructuredClassifier:

    pass
class Namespace:

    pass
class InputPin:

    pass
class InstanceSpecification:

    pass
class Package:

    pass
class Realization:

    pass
class WriteVariableAction:

    pass
class VariableAction:

    pass
class WriteLinkAction:

    pass
class Vertex:

    pass
class Property:

    pass
class InvocationAction:

    pass
class CreateLinkAction:

    pass
class DataType:

    pass
class MessageTrigger:

    pass
class BehavioralFeature:

    pass
class Classifier:

    pass
class ControlNode:

    pass
class EncapsulatedClassifier:

    pass
class BehavioredClassifier:

    pass
class Feature:

    pass
class Pin:

    pass
class Abstraction:

    pass
class CallAction:

    pass
class MessageEnd:

    pass
class Action:

    pass
class Node:

    pass
class StateMachine:

    pass
class ActivityEdge:

    pass
class Association:

    pass
class Class:

    pass
class Behavior:

    pass
class StructuralFeatureAction:

    pass
class ObjectNode:

    pass
class PackageableElement:

    pass
class StructuredActivityNode:

    pass
class FinalNode:

    pass
class EventOccurrence:

    pass
class Trigger:

    pass
class Transition:

    pass
class InteractionOccurrence:

    pass
class OpaqueExpression:

    pass
class CentralBufferNode:

    pass
class NamedElement:

    pass
class Element:

    pass
class UML2WithID_LinkAction(Element, Action):

    pass
class UML2WithID_ClearAssociationAction(Element, Action):

    pass
class UML2WithID_BehavioralFeature(Feature, Element, Namespace):

    pass
class UML2WithID_CallTrigger(Element, MessageTrigger):

    pass
class UML2WithID_DurationConstraint(IntervalConstraint, Element):

    pass
class UML2WithID_DeploymentTarget(NamedElement, Element):

    pass
class UML2WithID_Gate(Element, MessageEnd):

    pass
class UML2WithID_ReadLinkObjectEndAction(Element, Action):

    pass
class UML2WithID_CreateObjectAction(Element, Action):

    pass
class UML2WithID_StructuralFeatureAction(Element, Action):

    pass
class UML2WithID_ActivityFinalNode(FinalNode, Element):

    pass
class UML2WithID_CreateLinkAction(Element, WriteLinkAction):

    pass
class UML2WithID_DestroyLinkAction(Element, WriteLinkAction):

    pass
class UML2WithID_Vertex(NamedElement, Element):

    pass
class UML2WithID_TimeConstraint(IntervalConstraint, Element):

    pass
class UML2WithID_Pseudostate(Vertex, Element):

    pass
class UML2WithID_ExpansionRegion(Element, StructuredActivityNode):

    pass
class UML2WithID_ReadLinkAction(LinkAction, Element):

    pass
class UML2WithID_InitialNode(Element, ControlNode):

    pass
class UML2WithID_ReadExtentAction(Element, Action):

    pass
class UML2WithID_SendSignalAction(InvocationAction, Element):

    pass
class UML2WithID_WriteStructuralFeatureAction(StructuralFeatureAction, Element):

    pass
class UML2WithID_Action(ExecutableNode, Element):

    pass
class UML2WithID_CreateLinkObjectAction(Element, CreateLinkAction):

    pass
class UML2WithID_ValuePin(Element, InputPin):

    pass
class UML2WithID_ReadVariableAction(VariableAction, Element):

    pass
class UML2WithID_Behavior(Element, Class):

    pass
class UML2WithID_Extension(Element, Association):

    pass
class UML2WithID_VariableAction(Element, Action):

    pass
class UML2WithID_InteractionConstraint(Constraint, Element):

    pass
class UML2WithID_TypedElement(NamedElement, Element):

    pass
class UML2WithID_ActivityPartition(NamedElement, Element):

    pass
class UML2WithID_Include(NamedElement, Element):

    pass
class UML2WithID_Artifact(Element, DeployedArtifact, Classifier):

    pass
class UML2WithID_FinalState(Element, State):

    pass
class UML2WithID_FinalNode(Element, ControlNode):

    pass
class UML2WithID_CommunicationPath(Element, Association):

    pass
class UML2WithID_ClearVariableAction(VariableAction, Element):

    pass
class UML2WithID_NamedElement(Element):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class UML2WithID_EncapsulatedClassifier(StructuredClassifier, Element):

    pass
class UML2WithID_Actor(Element, Classifier):

    pass
class UML2WithID_Profile(Package, Element):

    pass
class UML2WithID_TimeTrigger(Trigger, Element):

    pass
class UML2WithID_InputPin(Pin, Element):

    pass
class UML2WithID_UseCase(BehavioredClassifier, Element):

    pass
class UML2WithID_MessageTrigger(Element, Trigger):

    pass
class UML2WithID_Stereotype(Element, Class):

    pass
class UML2WithID_RedefinableElement(NamedElement, Element):

    pass
class UML2WithID_StructuredClassifier(Element, Classifier):

    pass
class UML2WithID_SignalTrigger(Element, MessageTrigger):

    pass
class UML2WithID_Activity(Element, Behavior):

    pass
class UML2WithID_ReadLinkObjectEndQualifierAction(Element, Action):

    pass
class UML2WithID_RaiseExceptionAction(Element, Action):

    pass
class UML2WithID_InvocationAction(Element, Action):

    pass
class UML2WithID_GeneralOrdering(NamedElement, Element):

    pass
class UML2WithID_JoinNode(ControlNode, Element):

    pass
class UML2WithID_BehavioredClassifier(Element, Classifier):

    pass
class UML2WithID_DeployedArtifact(NamedElement, Element):

    pass
class UML2WithID_Dependency(PackageableElement, Element):

    pass
class UML2WithID_Constraint(PackageableElement, Element):

    pass
class UML2WithID_ReadIsClassifiedObjectAction(Element, Action):

    pass
class UML2WithID_StartOwnedBehaviorAction(Element, Action):

    pass
class UML2WithID_BroadcastSignalAction(InvocationAction, Element):

    pass
class UML2WithID_ConnectionPointReference(Vertex, Element):

    pass
class UML2WithID_DataStoreNode(Element, CentralBufferNode):

    pass
class UML2WithID_IntervalConstraint(Constraint, Element):

    pass
class UML2WithID_AssociationClass(Association, Element, Class):

    pass
class UML2WithID_ObjectFlow(ActivityEdge, Element):

    pass
class UML2WithID_Reception(BehavioralFeature, Element):

    pass
class UML2WithID_Class(EncapsulatedClassifier, BehavioredClassifier, Element):

    pass
class UML2WithID_DeploymentSpecification(Artifact, Element):

    pass
class UML2WithID_ReadStructuralFeatureAction(StructuralFeatureAction, Element):

    pass
class UML2WithID_DataType(Element, Classifier):

    pass
class UML2WithID_TestIdentityAction(Element, Action):

    pass
class UML2WithID_LoopNode(Element, StructuredActivityNode):

    pass
class UML2WithID_ParameterSet(NamedElement, Element):

    pass
class UML2WithID_InformationFlow(PackageableElement, Element):

    pass
class UML2WithID_ClearStructuralFeatureAction(StructuralFeatureAction, Element):

    pass
class UML2WithID_PrimitiveFunction(PackageableElement, Element):

    pass
class UML2WithID_ActivityParameterNode(ObjectNode, Element):

    pass
class UML2WithID_CallAction(InvocationAction, Element):

    pass
class UML2WithID_Type(PackageableElement, Element):

    pass
class UML2WithID_Component(Element, Class):

    pass
class UML2WithID_Package(PackageableElement, Element, Namespace):

    pass
class UML2WithID_ReplyAction(Element, Action):

    pass
class UML2WithID_WriteVariableAction(VariableAction, Element):

    pass
class UML2WithID_Collaboration(StructuredClassifier, Element, BehavioredClassifier):

    pass
class UML2WithID_Connector(Feature, Element):

    pass
class UML2WithID_AddVariableValueAction(WriteVariableAction, Element):

    pass
class UML2WithID_InformationItem(Element, Classifier):

    pass
class UML2WithID_StateMachine(Element, Behavior):

    pass
class UML2WithID_Extend(NamedElement, Element):

    pass
class UML2WithID_CollaborationOccurrence(NamedElement, Element):

    pass
class UML2WithID_ReclassifyObjectAction(Element, Action):

    pass
class UML2WithID_Enumeration(DataType, Element):

    pass
class UML2WithID_ExtensionEnd(Property, Element):

    pass
class UML2WithID_MergeNode(Element, ControlNode):

    pass
class UML2WithID_Stop(EventOccurrence, Element):

    pass
class UML2WithID_ProtocolStateMachine(StateMachine, Element):

    pass
class UML2WithID_ReadSelfAction(Element, Action):

    pass
class UML2WithID_RemoveVariableValueAction(WriteVariableAction, Element):

    pass
class UML2WithID_ConnectableElement(NamedElement, Element):

    pass
class UML2WithID_DecisionNode(Element, ControlNode):

    pass
class UML2WithID_ConditionalNode(Element, StructuredActivityNode):

    pass
class UML2WithID_Expression(OpaqueExpression, Element):

    pass
class UML2WithID_Device(Node, Element):

    pass
class UML2WithID_Substitution(Realization, Element):

    pass
class UML2WithID_GeneralizationSet(PackageableElement, Element):

    pass
class UML2WithID_PackageableElement(NamedElement, Element):

    pass
class UML2WithID_ApplyFunctionAction(Element, Action):

    pass
class UML2WithID_TemplateableClassifier(Element, Classifier):

    pass
class UML2WithID_Interface(Element, Classifier):

    pass
class UML2WithID_PrimitiveType(DataType, Element):

    pass
class UML2WithID_FlowFinalNode(FinalNode, Element):

    pass
class UML2WithID_Pin(ObjectNode, Element):

    pass
class UML2WithID_AcceptEventAction(Element, Action):

    pass
class UML2WithID_ExecutionEnvironment(Node, Element):

    pass
class UML2WithID_PartDecomposition(Element, InteractionOccurrence):

    pass
class UML2WithID_DestroyObjectAction(Element, Action):

    pass
class UML2WithID_AnyTrigger(Element, MessageTrigger):

    pass
class UML2WithID_Signal(Element, Classifier):

    pass
class UML2WithID_EnumerationLiteral(InstanceSpecification, Element):

    pass
class UML2WithID_ControlFlow(ActivityEdge, Element):

    pass
class UML2WithID_ForkNode(ControlNode, Element):

    pass
class UML2WithID_CentralBufferNode(ObjectNode, Element):

    pass
class UML2WithID_SendObjectAction(InvocationAction, Element):

    pass
class UML2WithID_OutputPin(Pin, Element):

    pass
class UML2WithID_CallBehaviorAction(Element, CallAction):

    pass
class UML2WithID_Association(Element, Classifier):

    pass
class UML2WithID_ChangeTrigger(Element, Trigger):

    pass
class UML2WithID_ParameterableClassifier(Element, Classifier):

    pass
class UML2WithID_ExpansionNode(ObjectNode, Element):

    pass
class UML2WithID_StructuredActivityNode(Element, Action, Namespace):

    pass
class UML2WithID_InteractionFragment(NamedElement, Element):

    pass
class UML2WithID_Manifestation(Abstraction, Element):

    pass
class UML2WithID_Namespace(NamedElement, Element):

    pass
class UML2WithID_Model(Package, Element):

    pass
class UML2WithID_Lifeline(NamedElement, Element):

    pass
class UML2WithID_WriteLinkAction(LinkAction, Element):

    pass
class UML2WithID_Realization(Abstraction, Element):

    pass
class UML2WithID_Message(NamedElement, Element):

    pass
class UML2WithID_CallOperationAction(Element, CallAction):

    pass
class UML2WithID_AcceptCallAction(Element, AcceptEventAction):

    pass
class UML2WithID_TimeInterval(Interval, Element):

    pass
class UML2WithID_Implementation(Realization, Element):

    pass
class UML2WithID_Port(Property, Element):

    pass
class UML2WithID_ProtocolTransition(Element, Transition):

    pass
class UML2WithID_MessageEnd(NamedElement, Element):

    pass
class UML2WithID_DurationInterval(Interval, Element):

    pass
class UML2WithID_Trigger(NamedElement, Element):

    pass
class TypedElement:

    pass
class UML2WithID_ValueSpecification(TypedElement, Element):

    pass
class UML2WithID_StructuralFeature(Feature, TypedElement, Element):

    pass
class UML2WithID_Operation(TypedElement, BehavioralFeature, Element):

    pass
class ActivityNode:

    pass
class UML2WithID_ControlNode(Element, ActivityNode):

    pass
class UML2WithID_ExecutableNode(Element, ActivityNode):

    pass
class UML2WithID_ObjectNode(TypedElement, Element, ActivityNode):

    pass
class RedefinableElement:

    pass
class UML2WithID_ActivityEdge(RedefinableElement, Element):

    pass
class UML2WithID_RedefinableTemplateSignature(RedefinableElement, Element):

    pass
class UML2WithID_State(Vertex, RedefinableElement, Element, Namespace):

    pass
class UML2WithID_Region(RedefinableElement, Element, Namespace):

    pass
class UML2WithID_Classifier(RedefinableElement, Element, Type, Namespace):

    pass
class UML2WithID_ExtensionPoint(RedefinableElement, Element):

    pass
class UML2WithID_Transition(RedefinableElement, Element):

    pass
class UML2WithID_Feature(RedefinableElement, Element):

    pass
class UML2WithID_ActivityNode(RedefinableElement, Element):

    pass
class LiteralSpecification:

    pass
class UML2WithID_LiteralInteger(LiteralSpecification, Element):

    pass
class UML2WithID_LiteralNull(LiteralSpecification, Element):

    pass
class UML2WithID_LiteralBoolean(LiteralSpecification, Element):

    pass
class UML2WithID_LiteralString(LiteralSpecification, Element):

    pass
class UML2WithID_LiteralUnlimitedNatural(LiteralSpecification, Element):

    pass
class WriteStructuralFeatureAction:

    pass
class UML2WithID_RemoveStructuralFeatureValueAction(WriteStructuralFeatureAction, Element):

    pass
class UML2WithID_AddStructuralFeatureValueAction(WriteStructuralFeatureAction, Element):

    pass
class UML2WithID_TimeObservationAction(WriteStructuralFeatureAction, Element):

    pass
class UML2WithID_DurationObservationAction(WriteStructuralFeatureAction, Element):

    pass
class DeploymentTarget:

    pass
class UML2WithID_Node(DeploymentTarget, Element, Class):

    pass
class UML2WithID_InstanceSpecification(DeploymentTarget, PackageableElement, DeployedArtifact, Element):

    pass
class ConnectableElement:

    pass
class UML2WithID_Variable(TypedElement, Element, ConnectableElement):

    pass
class UML2WithID_Parameter(TypedElement, Element, ConnectableElement):

    pass
class StructuralFeature:

    pass
class UML2WithID_Property(StructuralFeature, DeploymentTarget, Element, ConnectableElement):

    pass
class Dependency:

    pass
class UML2WithID_Deployment(Dependency, Element):

    pass
class UML2WithID_Permission(Dependency, Element):

    pass
class UML2WithID_Abstraction(Dependency, Element):

    pass
class UML2WithID_Usage(Dependency, Element):

    pass
class InteractionFragment:

    pass
class UML2WithID_CombinedFragment(InteractionFragment, Element):

    pass
class UML2WithID_Interaction(InteractionFragment, Element, Behavior):

    pass
class UML2WithID_InteractionOperand(InteractionFragment, Element, Namespace):

    pass
class UML2WithID_Continuation(InteractionFragment, Element):

    pass
class UML2WithID_EventOccurrence(InteractionFragment, Element, MessageEnd):

    pass
class UML2WithID_InteractionOccurrence(InteractionFragment, Element):

    pass
class UML2WithID_StateInvariant(InteractionFragment, Element):

    pass
class UML2WithID_ExecutionOccurrence(InteractionFragment, Element):

    pass
class ValueSpecification:

    pass
class UML2WithID_TimeExpression(Element, ValueSpecification):

    pass
class UML2WithID_OpaqueExpression(Element, ValueSpecification):

    pass
class UML2WithID_InstanceValue(Element, ValueSpecification):

    pass
class UML2WithID_Duration(Element, ValueSpecification):

    pass
class UML2WithID_Interval(Element, ValueSpecification):

    pass
class UML2WithID_LiteralSpecification(Element, ValueSpecification):

    pass