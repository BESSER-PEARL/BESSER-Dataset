from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Dependency:

    pass
class Transition:

    pass
class Property:

    pass
class WriteLinkAction:

    pass
class TypedElement:

    pass
class CentralBufferNode:

    pass
class CallAction:

    pass
class Association:

    pass
class ExecutableNode:

    pass
class Package:

    pass
class Realization:

    pass
class Trigger:

    pass
class ActivityEdge:

    pass
class Feature:

    pass
class FinalNode:

    pass
class BehavioralFeature:

    pass
class State:

    pass
class Type:

    pass
class AcceptEventAction:

    pass
class Constraint:

    pass
class IntervalConstraint:

    pass
class WriteStructuralFeatureAction:

    pass
class Classifier:

    pass
class RedefinableElement:

    pass
class MessageEnd:

    pass
class InteractionFragment:

    pass
class StructuredClassifier:

    pass
class OpaqueExpression:

    pass
class MessageTrigger:

    pass
class Class:

    pass
class Action:

    pass
class ValueSpecification:

    pass
class ControlNode:

    pass
class EncapsulatedClassifier:

    pass
class BehavioredClassifier:

    pass
class PackageableElement:

    pass
class Namespace:

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


class InteractionOccurrence:

    pass
class Artifact:

    pass
class CreateLinkAction:

    pass
class DeployedArtifact:

    pass
class Node:

    pass
class StateMachine:

    pass
class Pin:

    pass
class EventOccurrence:

    pass
class DeploymentTarget:

    pass
class StructuralFeature:

    pass
class ConnectableElement:

    pass
class Abstraction:

    pass
class InputPin:

    pass
class Behavior:

    pass
class ObjectNode:

    pass
class StructuredActivityNode:

    pass
class Interval:

    pass
class ActivityNode:

    pass
class VariableAction:

    pass
class LiteralSpecification:

    pass
class DataType:

    pass
class Element:

    pass
class UML2WithID_ActivityNode(RedefinableElement, Element):

    pass
class UML2WithID_Duration(ValueSpecification, Element):

    pass
class UML2WithID_Interface(Classifier, Element):

    pass
class UML2WithID_ExecutionOccurrence(InteractionFragment, Element):

    pass
class UML2WithID_DecisionNode(ControlNode, Element):

    pass
class UML2WithID_CommunicationPath(Association, Element):

    pass
class UML2WithID_CentralBufferNode(ObjectNode, Element):

    pass
class UML2WithID_StructuralFeature(TypedElement, Feature, Element):

    pass
class UML2WithID_ProtocolStateMachine(StateMachine, Element):

    pass
class UML2WithID_DurationObservationAction(WriteStructuralFeatureAction, Element):

    pass
class UML2WithID_MergeNode(ControlNode, Element):

    pass
class UML2WithID_ActivityParameterNode(ObjectNode, Element):

    pass
class UML2WithID_AddStructuralFeatureValueAction(WriteStructuralFeatureAction, Element):

    pass
class UML2WithID_Stop(EventOccurrence, Element):

    pass
class UML2WithID_EventOccurrence(MessageEnd, InteractionFragment, Element):

    pass
class UML2WithID_Deployment(Element, Dependency):

    pass
class UML2WithID_ReadIsClassifiedObjectAction(Action, Element):

    pass
class UML2WithID_SignalTrigger(Element, MessageTrigger):

    pass
class UML2WithID_DeploymentSpecification(Artifact, Element):

    pass
class UML2WithID_PrimitiveFunction(PackageableElement, Element):

    pass
class UML2WithID_CallTrigger(Element, MessageTrigger):

    pass
class UML2WithID_EncapsulatedClassifier(StructuredClassifier, Element):

    pass
class UML2WithID_ReadExtentAction(Action, Element):

    pass
class UML2WithID_LiteralSpecification(ValueSpecification, Element):

    pass
class UML2WithID_ParameterableClassifier(Classifier, Element):

    pass
class UML2WithID_Actor(Classifier, Element):

    pass
class UML2WithID_RaiseExceptionAction(Action, Element):

    pass
class UML2WithID_ConditionalNode(StructuredActivityNode, Element):

    pass
class UML2WithID_ClearAssociationAction(Action, Element):

    pass
class UML2WithID_PartDecomposition(InteractionOccurrence, Element):

    pass
class UML2WithID_StateMachine(Behavior, Element):

    pass
class UML2WithID_WriteVariableAction(Element, VariableAction):

    pass
class UML2WithID_TimeConstraint(IntervalConstraint, Element):

    pass
class UML2WithID_Implementation(Element, Realization):

    pass
class UML2WithID_InteractionOperand(Namespace, InteractionFragment, Element):

    pass
class UML2WithID_Expression(OpaqueExpression, Element):

    pass
class UML2WithID_InstanceValue(ValueSpecification, Element):

    pass
class UML2WithID_ExpansionRegion(StructuredActivityNode, Element):

    pass
class UML2WithID_VariableAction(Action, Element):

    pass
class UML2WithID_FinalNode(ControlNode, Element):

    pass
class UML2WithID_Class(BehavioredClassifier, EncapsulatedClassifier, Element):

    pass
class UML2WithID_InputPin(Pin, Element):

    pass
class UML2WithID_ObjectNode(TypedElement, ActivityNode, Element):

    pass
class UML2WithID_TimeTrigger(Trigger, Element):

    pass
class UML2WithID_Region(Namespace, RedefinableElement, Element):

    pass
class UML2WithID_CreateObjectAction(Action, Element):

    pass
class UML2WithID_StateInvariant(InteractionFragment, Element):

    pass
class UML2WithID_Interaction(Behavior, InteractionFragment, Element):

    pass
class UML2WithID_FinalState(State, Element):

    pass
class UML2WithID_ReadSelfAction(Action, Element):

    pass
class UML2WithID_GeneralizationSet(PackageableElement, Element):

    pass
class UML2WithID_RedefinableTemplateSignature(RedefinableElement, Element):

    pass
class UML2WithID_ExtensionPoint(Element, RedefinableElement):

    pass
class UML2WithID_JoinNode(ControlNode, Element):

    pass
class UML2WithID_AcceptCallAction(AcceptEventAction, Element):

    pass
class UML2WithID_Collaboration(StructuredClassifier, BehavioredClassifier, Element):

    pass
class UML2WithID_Action(ExecutableNode, Element):

    pass
class UML2WithID_Enumeration(DataType, Element):

    pass
class UML2WithID_Association(Classifier, Element):

    pass
class UML2WithID_ReclassifyObjectAction(Action, Element):

    pass
class UML2WithID_Manifestation(Abstraction, Element):

    pass
class UML2WithID_Activity(Behavior, Element):

    pass
class UML2WithID_InformationFlow(PackageableElement, Element):

    pass
class UML2WithID_ApplyFunctionAction(Action, Element):

    pass
class UML2WithID_Model(Package, Element):

    pass
class UML2WithID_Connector(Feature, Element):

    pass
class UML2WithID_DestroyObjectAction(Action, Element):

    pass
class UML2WithID_StartOwnedBehaviorAction(Action, Element):

    pass
class UML2WithID_Pin(ObjectNode, Element):

    pass
class UML2WithID_OutputPin(Pin, Element):

    pass
class UML2WithID_Operation(TypedElement, BehavioralFeature, Element):

    pass
class UML2WithID_Classifier(Type, Namespace, RedefinableElement, Element):

    pass
class UML2WithID_ControlNode(ActivityNode, Element):

    pass
class UML2WithID_TestIdentityAction(Action, Element):

    pass
class UML2WithID_LiteralBoolean(LiteralSpecification, Element):

    pass
class UML2WithID_DestroyLinkAction(WriteLinkAction, Element):

    pass
class UML2WithID_CallOperationAction(CallAction, Element):

    pass
class UML2WithID_ReadVariableAction(VariableAction, Element):

    pass
class UML2WithID_InteractionConstraint(Constraint, Element):

    pass
class UML2WithID_Component(Class, Element):

    pass
class UML2WithID_ForkNode(ControlNode, Element):

    pass
class UML2WithID_ControlFlow(ActivityEdge, Element):

    pass
class UML2WithID_ChangeTrigger(Trigger, Element):

    pass
class UML2WithID_Interval(ValueSpecification, Element):

    pass
class UML2WithID_InteractionOccurrence(InteractionFragment, Element):

    pass
class UML2WithID_AcceptEventAction(Action, Element):

    pass
class UML2WithID_ObjectFlow(ActivityEdge, Element):

    pass
class UML2WithID_OpaqueExpression(ValueSpecification, Element):

    pass
class UML2WithID_TimeInterval(Interval, Element):

    pass
class UML2WithID_BehavioralFeature(Feature, Namespace, Element):

    pass
class UML2WithID_LiteralUnlimitedNatural(LiteralSpecification, Element):

    pass
class UML2WithID_ReadLinkObjectEndQualifierAction(Action, Element):

    pass
class UML2WithID_Node(Class, DeploymentTarget, Element):

    pass
class UML2WithID_Abstraction(Element, Dependency):

    pass
class UML2WithID_LiteralInteger(LiteralSpecification, Element):

    pass
class UML2WithID_FlowFinalNode(FinalNode, Element):

    pass
class UML2WithID_LoopNode(StructuredActivityNode, Element):

    pass
class UML2WithID_Port(Property, Element):

    pass
class UML2WithID_Device(Node, Element):

    pass
class UML2WithID_Signal(Classifier, Element):

    pass
class UML2WithID_Gate(MessageEnd, Element):

    pass
class UML2WithID_Behavior(Class, Element):

    pass
class UML2WithID_CallBehaviorAction(CallAction, Element):

    pass
class UML2WithID_Stereotype(Class, Element):

    pass
class UML2WithID_Realization(Abstraction, Element):

    pass
class UML2WithID_IntervalConstraint(Constraint, Element):

    pass
class UML2WithID_Reception(BehavioralFeature, Element):

    pass
class UML2WithID_Usage(Dependency, Element):

    pass
class UML2WithID_Package(PackageableElement, Namespace, Element):

    pass
class UML2WithID_ReadLinkObjectEndAction(Action, Element):

    pass
class UML2WithID_DataStoreNode(CentralBufferNode, Element):

    pass
class UML2WithID_Type(PackageableElement, Element):

    pass
class UML2WithID_InitialNode(ControlNode, Element):

    pass
class UML2WithID_Artifact(DeployedArtifact, Classifier, Element):

    pass
class UML2WithID_ValuePin(InputPin, Element):

    pass
class UML2WithID_ValueSpecification(TypedElement, Element):

    pass
class UML2WithID_TimeObservationAction(WriteStructuralFeatureAction, Element):

    pass
class UML2WithID_TimeExpression(ValueSpecification, Element):

    pass
class UML2WithID_ExecutableNode(ActivityNode, Element):

    pass
class UML2WithID_MessageTrigger(Trigger, Element):

    pass
class UML2WithID_ActivityEdge(Element, RedefinableElement):

    pass
class UML2WithID_BehavioredClassifier(Classifier, Element):

    pass
class UML2WithID_Extension(Association, Element):

    pass
class UML2WithID_ActivityFinalNode(FinalNode, Element):

    pass
class UML2WithID_DurationInterval(Interval, Element):

    pass
class UML2WithID_CombinedFragment(InteractionFragment, Element):

    pass
class UML2WithID_ExpansionNode(Element, ObjectNode):

    pass
class UML2WithID_ProtocolTransition(Transition, Element):

    pass
class UML2WithID_Profile(Package, Element):

    pass
class UML2WithID_AnyTrigger(MessageTrigger, Element):

    pass
class UML2WithID_CreateLinkAction(WriteLinkAction, Element):

    pass
class UML2WithID_InstanceSpecification(PackageableElement, DeployedArtifact, DeploymentTarget, Element):

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


class UML2WithID_StructuralFeatureAction(Action, Element):

    pass
class UML2WithID_InvocationAction(Action, Element):

    pass
class UML2WithID_Substitution(Realization, Element):

    pass
class UML2WithID_StructuredActivityNode(Action, Namespace, Element):

    pass
class UML2WithID_Variable(TypedElement, ConnectableElement, Element):

    pass
class UML2WithID_Permission(Dependency, Element):

    pass
class UML2WithID_DurationConstraint(IntervalConstraint, Element):

    pass
class UML2WithID_Continuation(InteractionFragment, Element):

    pass
class UML2WithID_LiteralNull(LiteralSpecification, Element):

    pass
class UML2WithID_DataType(Classifier, Element):

    pass
class UML2WithID_Dependency(PackageableElement, Element):

    pass
class UML2WithID_AssociationClass(Class, Association, Element):

    pass
class UML2WithID_PrimitiveType(DataType, Element):

    pass
class UML2WithID_RemoveStructuralFeatureValueAction(WriteStructuralFeatureAction, Element):

    pass
class UML2WithID_Transition(Element, RedefinableElement):

    pass
class UML2WithID_LinkAction(Action, Element):

    pass
class UML2WithID_CreateLinkObjectAction(CreateLinkAction, Element):

    pass
class UML2WithID_InformationItem(Classifier, Element):

    pass
class UML2WithID_TemplateableClassifier(Classifier, Element):

    pass
class UML2WithID_StructuredClassifier(Classifier, Element):

    pass
class UML2WithID_Parameter(TypedElement, ConnectableElement, Element):

    pass
class UML2WithID_ExecutionEnvironment(Node, Element):

    pass
class UML2WithID_Property(StructuralFeature, ConnectableElement, DeploymentTarget, Element):

    pass
class UML2WithID_Constraint(PackageableElement, Element):

    pass
class UML2WithID_ExtensionEnd(Property, Element):

    pass
class UML2WithID_Feature(Element, RedefinableElement):

    pass
class Vertex:

    pass
class UML2WithID_State(Vertex, Namespace, RedefinableElement, Element):

    pass
class UML2WithID_ConnectionPointReference(Vertex, Element):

    pass
class UML2WithID_Pseudostate(Vertex, Element):

    pass
class WriteVariableAction:

    pass
class UML2WithID_AddVariableValueAction(WriteVariableAction, Element):

    pass
class UML2WithID_RemoveVariableValueAction(WriteVariableAction, Element):

    pass
class InstanceSpecification:

    pass
class UML2WithID_EnumerationLiteral(InstanceSpecification, Element):

    pass
class NamedElement:

    pass
class UML2WithID_ActivityPartition(NamedElement, Element):

    pass
class UML2WithID_RedefinableElement(NamedElement, Element):

    pass
class UML2WithID_Message(NamedElement, Element):

    pass
class UML2WithID_CollaborationOccurrence(NamedElement, Element):

    pass
class UML2WithID_Vertex(NamedElement, Element):

    pass
class UML2WithID_DeploymentTarget(NamedElement, Element):

    pass
class UML2WithID_ConnectableElement(NamedElement, Element):

    pass
class UML2WithID_GeneralOrdering(NamedElement, Element):

    pass
class UML2WithID_Trigger(NamedElement, Element):

    pass
class UML2WithID_MessageEnd(NamedElement, Element):

    pass
class UML2WithID_Namespace(NamedElement, Element):

    pass
class UML2WithID_DeployedArtifact(NamedElement, Element):

    pass
class UML2WithID_Lifeline(NamedElement, Element):

    pass
class UML2WithID_Include(NamedElement, Element):

    pass
class UML2WithID_InteractionFragment(NamedElement, Element):

    pass
class UML2WithID_Extend(NamedElement, Element):

    pass
class UML2WithID_ParameterSet(NamedElement, Element):

    pass
class UML2WithID_TypedElement(NamedElement, Element):

    pass
class UML2WithID_PackageableElement(NamedElement, Element):

    pass
class LinkAction:

    pass
class UML2WithID_ReadLinkAction(LinkAction, Element):

    pass
class UML2WithID_WriteLinkAction(LinkAction, Element):

    pass
class StructuralFeatureAction:

    pass
class UML2WithID_ReadStructuralFeatureAction(StructuralFeatureAction, Element):

    pass
class UML2WithID_WriteStructuralFeatureAction(StructuralFeatureAction, Element):

    pass
class UML2WithID_ClearStructuralFeatureAction(StructuralFeatureAction, Element):

    pass
class UML2WithID_UseCase(BehavioredClassifier, Element):

    pass
class UML2WithID_ClearVariableAction(Element, VariableAction):

    pass
class UML2WithID_ReplyAction(Action, Element):

    pass
class InvocationAction:

    pass
class UML2WithID_SendSignalAction(InvocationAction, Element):

    pass
class UML2WithID_BroadcastSignalAction(InvocationAction, Element):

    pass
class UML2WithID_CallAction(InvocationAction, Element):

    pass
class UML2WithID_SendObjectAction(InvocationAction, Element):

    pass
class UML2WithID_LiteralString(LiteralSpecification, Element):

    pass