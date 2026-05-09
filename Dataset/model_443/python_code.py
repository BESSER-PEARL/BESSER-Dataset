from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

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


class CentralBufferNode:

    pass
class StateMachine:

    pass
class ObjectNode:

    pass
class InputPin:

    pass
class Transition:

    pass
class EventOccurrence:

    pass
class InteractionOccurrence:

    pass
class AcceptEventAction:

    pass
class FinalNode:

    pass
class LinkAction:

    pass
class ActivityNode:

    pass
class CreateLinkAction:

    pass
class Feature:

    pass
class DeployedArtifact:

    pass
class Association:

    pass
class MessageTrigger:

    pass
class ExecutableNode:

    pass
class BehavioralFeature:

    pass
class Behavior:

    pass
class EncapsulatedClassifier:

    pass
class DataType:

    pass
class WriteVariableAction:

    pass
class TypedElement:

    pass
class InstanceSpecification:

    pass
class PackageableElement:

    pass
class DeploymentTarget:

    pass
class ConnectableElement:

    pass
class StructuralFeature:

    pass
class State:

    pass
class StructuralFeatureAction:

    pass
class Pin:

    pass
class Abstraction:

    pass
class OpaqueExpression:

    pass
class Realization:

    pass
class LiteralSpecification:

    pass
class ActivityEdge:

    pass
class StructuredActivityNode:

    pass
class Package:

    pass
class Vertex:

    pass
class Dependency:

    pass
class ControlNode:

    pass
class MessageEnd:

    pass
class InteractionFragment:

    pass
class Type:

    pass
class Action:

    pass
class RedefinableElement:

    pass
class Namespace:

    pass
class InvocationAction:

    pass
class WriteLinkAction:

    pass
class Property:

    pass
class Node:

    pass
class BehavioredClassifier:

    pass
class WriteStructuralFeatureAction:

    pass
class ValueSpecification:

    pass
class Classifier:

    pass
class VariableAction:

    pass
class Interval:

    pass
class StructuredClassifier:

    pass
class NamedElement:

    pass
class Element:

    pass
class UML2WithID_SendObjectAction(Element, InvocationAction):

    pass
class UML2WithID_Signal(Element, Classifier):

    pass
class UML2WithID_InteractionOccurrence(InteractionFragment, Element):

    pass
class UML2WithID_GeneralOrdering(Element, NamedElement):

    pass
class UML2WithID_LiteralInteger(Element, LiteralSpecification):

    pass
class UML2WithID_Class(Element, BehavioredClassifier, EncapsulatedClassifier):

    pass
class UML2WithID_RedefinableTemplateSignature(Element, RedefinableElement):

    pass
class UML2WithID_OpaqueExpression(Element, ValueSpecification):

    pass
class UML2WithID_Extend(Element, NamedElement):

    pass
class UML2WithID_Trigger(Element, NamedElement):

    pass
class UML2WithID_AddVariableValueAction(Element, WriteVariableAction):

    pass
class UML2WithID_ActivityNode(Element, RedefinableElement):

    pass
class UML2WithID_InformationItem(Element, Classifier):

    pass
class UML2WithID_CreateLinkAction(Element, WriteLinkAction):

    pass
class UML2WithID_Substitution(Element, Realization):

    pass
class UML2WithID_Model(Element, Package):

    pass
class UML2WithID_StateMachine(Behavior, Element):

    pass
class UML2WithID_MergeNode(Element, ControlNode):

    pass
class UML2WithID_InputPin(Element, Pin):

    pass
class UML2WithID_AcceptCallAction(Element, AcceptEventAction):

    pass
class UML2WithID_Interval(Element, ValueSpecification):

    pass
class UML2WithID_Realization(Element, Abstraction):

    pass
class UML2WithID_ClearAssociationAction(Element, Action):

    pass
class UML2WithID_EncapsulatedClassifier(Element, StructuredClassifier):

    pass
class UML2WithID_Property(StructuralFeature, Element, DeploymentTarget, ConnectableElement):

    pass
class UML2WithID_ParameterSet(Element, NamedElement):

    pass
class UML2WithID_Pseudostate(Element, Vertex):

    pass
class UML2WithID_StructuralFeatureAction(Element, Action):

    pass
class UML2WithID_ExtensionEnd(Element, Property):

    pass
class UML2WithID_ClearStructuralFeatureAction(Element, StructuralFeatureAction):

    pass
class UML2WithID_ProtocolStateMachine(Element, StateMachine):

    pass
class UML2WithID_ReplyAction(Element, Action):

    pass
class UML2WithID_Vertex(Element, NamedElement):

    pass
class UML2WithID_StartOwnedBehaviorAction(Element, Action):

    pass
class UML2WithID_TestIdentityAction(Element, Action):

    pass
class UML2WithID_EnumerationLiteral(Element, InstanceSpecification):

    pass
class UML2WithID_ReadVariableAction(Element, VariableAction):

    pass
class UML2WithID_Usage(Element, Dependency):

    pass
class UML2WithID_ExtensionPoint(Element, RedefinableElement):

    pass
class UML2WithID_FlowFinalNode(FinalNode, Element):

    pass
class UML2WithID_PrimitiveType(Element, DataType):

    pass
class UML2WithID_Expression(Element, OpaqueExpression):

    pass
class UML2WithID_ReclassifyObjectAction(Element, Action):

    pass
class UML2WithID_Type(PackageableElement, Element):

    pass
class UML2WithID_Gate(Element, MessageEnd):

    pass
class UML2WithID_DestroyLinkAction(Element, WriteLinkAction):

    pass
class UML2WithID_DeployedArtifact(Element, NamedElement):

    pass
class UML2WithID_FinalState(Element, State):

    pass
class UML2WithID_ExecutableNode(ActivityNode, Element):

    pass
class UML2WithID_TimeInterval(Element, Interval):

    pass
class UML2WithID_StructuralFeature(Element, TypedElement, Feature):

    pass
class UML2WithID_ConnectionPointReference(Element, Vertex):

    pass
class UML2WithID_Dependency(PackageableElement, Element):

    pass
class UML2WithID_AnyTrigger(Element, MessageTrigger):

    pass
class UML2WithID_LiteralString(Element, LiteralSpecification):

    pass
class UML2WithID_ControlNode(ActivityNode, Element):

    pass
class UML2WithID_ClearVariableAction(Element, VariableAction):

    pass
class UML2WithID_Profile(Element, Package):

    pass
class UML2WithID_CreateLinkObjectAction(Element, CreateLinkAction):

    pass
class UML2WithID_ExpansionNode(Element, ObjectNode):

    pass
class UML2WithID_CombinedFragment(InteractionFragment, Element):

    pass
class UML2WithID_Operation(Element, TypedElement, BehavioralFeature):

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


class UML2WithID_Parameter(Element, TypedElement, ConnectableElement):

    pass
class UML2WithID_InteractionOperand(InteractionFragment, Element, Namespace):

    pass
class UML2WithID_CollaborationOccurrence(Element, NamedElement):

    pass
class UML2WithID_Actor(Element, Classifier):

    pass
class UML2WithID_ParameterableClassifier(Element, Classifier):

    pass
class UML2WithID_AddStructuralFeatureValueAction(Element, WriteStructuralFeatureAction):

    pass
class UML2WithID_DeploymentTarget(Element, NamedElement):

    pass
class UML2WithID_Abstraction(Element, Dependency):

    pass
class UML2WithID_StructuredClassifier(Element, Classifier):

    pass
class UML2WithID_DestroyObjectAction(Element, Action):

    pass
class UML2WithID_LiteralBoolean(Element, LiteralSpecification):

    pass
class UML2WithID_RedefinableElement(Element, NamedElement):

    pass
class UML2WithID_Duration(Element, ValueSpecification):

    pass
class UML2WithID_CentralBufferNode(Element, ObjectNode):

    pass
class UML2WithID_ActivityParameterNode(Element, ObjectNode):

    pass
class UML2WithID_State(Element, RedefinableElement, Namespace, Vertex):

    pass
class UML2WithID_ValueSpecification(Element, TypedElement):

    pass
class UML2WithID_Implementation(Element, Realization):

    pass
class UML2WithID_DecisionNode(Element, ControlNode):

    pass
class UML2WithID_LiteralNull(Element, LiteralSpecification):

    pass
class UML2WithID_ReadLinkObjectEndAction(Element, Action):

    pass
class UML2WithID_DataStoreNode(Element, CentralBufferNode):

    pass
class UML2WithID_CreateObjectAction(Element, Action):

    pass
class UML2WithID_Package(PackageableElement, Element, Namespace):

    pass
class UML2WithID_ReadIsClassifiedObjectAction(Element, Action):

    pass
class UML2WithID_GeneralizationSet(PackageableElement, Element):

    pass
class UML2WithID_CallTrigger(MessageTrigger, Element):

    pass
class UML2WithID_ActivityFinalNode(FinalNode, Element):

    pass
class UML2WithID_RemoveStructuralFeatureValueAction(Element, WriteStructuralFeatureAction):

    pass
class UML2WithID_Include(Element, NamedElement):

    pass
class UML2WithID_Activity(Behavior, Element):

    pass
class UML2WithID_StateInvariant(InteractionFragment, Element):

    pass
class UML2WithID_InvocationAction(Element, Action):

    pass
class UML2WithID_ControlFlow(ActivityEdge, Element):

    pass
class UML2WithID_DurationObservationAction(Element, WriteStructuralFeatureAction):

    pass
class UML2WithID_Lifeline(Element, NamedElement):

    pass
class UML2WithID_ProtocolTransition(Element, Transition):

    pass
class UML2WithID_Deployment(Element, Dependency):

    pass
class UML2WithID_ObjectNode(ActivityNode, Element, TypedElement):

    pass
class UML2WithID_ExpansionRegion(Element, StructuredActivityNode):

    pass
class UML2WithID_Constraint(PackageableElement, Element):

    pass
class UML2WithID_Interface(Element, Classifier):

    pass
class UML2WithID_LiteralSpecification(Element, ValueSpecification):

    pass
class UML2WithID_Collaboration(Element, BehavioredClassifier, StructuredClassifier):

    pass
class UML2WithID_UseCase(Element, BehavioredClassifier):

    pass
class UML2WithID_ExecutionOccurrence(InteractionFragment, Element):

    pass
class UML2WithID_Association(Element, Classifier):

    pass
class UML2WithID_ExecutionEnvironment(Element, Node):

    pass
class UML2WithID_InstanceSpecification(PackageableElement, Element, DeployedArtifact, DeploymentTarget):

    pass
class UML2WithID_SignalTrigger(MessageTrigger, Element):

    pass
class UML2WithID_WriteVariableAction(Element, VariableAction):

    pass
class UML2WithID_InstanceValue(Element, ValueSpecification):

    pass
class UML2WithID_Continuation(InteractionFragment, Element):

    pass
class UML2WithID_CommunicationPath(Element, Association):

    pass
class UML2WithID_TimeExpression(Element, ValueSpecification):

    pass
class UML2WithID_VariableAction(Element, Action):

    pass
class UML2WithID_ApplyFunctionAction(Element, Action):

    pass
class UML2WithID_DurationInterval(Element, Interval):

    pass
class UML2WithID_Message(Element, NamedElement):

    pass
class UML2WithID_ActivityPartition(Element, NamedElement):

    pass
class UML2WithID_RemoveVariableValueAction(Element, WriteVariableAction):

    pass
class UML2WithID_Manifestation(Element, Abstraction):

    pass
class UML2WithID_WriteLinkAction(LinkAction, Element):

    pass
class UML2WithID_Pin(Element, ObjectNode):

    pass
class UML2WithID_Stop(Element, EventOccurrence):

    pass
class UML2WithID_WriteStructuralFeatureAction(Element, StructuralFeatureAction):

    pass
class UML2WithID_ValuePin(Element, InputPin):

    pass
class UML2WithID_Permission(Element, Dependency):

    pass
class UML2WithID_BehavioralFeature(Element, Namespace, Feature):

    pass
class UML2WithID_ReadExtentAction(Element, Action):

    pass
class UML2WithID_TimeObservationAction(Element, WriteStructuralFeatureAction):

    pass
class UML2WithID_FinalNode(Element, ControlNode):

    pass
class UML2WithID_BehavioredClassifier(Element, Classifier):

    pass
class UML2WithID_ReadSelfAction(Element, Action):

    pass
class UML2WithID_ForkNode(Element, ControlNode):

    pass
class UML2WithID_Action(Element, ExecutableNode):

    pass
class UML2WithID_StructuredActivityNode(Element, Namespace, Action):

    pass
class UML2WithID_ReadStructuralFeatureAction(Element, StructuralFeatureAction):

    pass
class UML2WithID_Classifier(Element, RedefinableElement, Namespace, Type):

    pass
class UML2WithID_Variable(Element, TypedElement, ConnectableElement):

    pass
class UML2WithID_BroadcastSignalAction(Element, InvocationAction):

    pass
class UML2WithID_ReadLinkAction(LinkAction, Element):

    pass
class UML2WithID_PackageableElement(Element, NamedElement):

    pass
class UML2WithID_Enumeration(Element, DataType):

    pass
class UML2WithID_Connector(Element, Feature):

    pass
class UML2WithID_Port(Element, Property):

    pass
class UML2WithID_TypedElement(Element, NamedElement):

    pass
class UML2WithID_ObjectFlow(ActivityEdge, Element):

    pass
class UML2WithID_EventOccurrence(InteractionFragment, Element, MessageEnd):

    pass
class UML2WithID_PartDecomposition(Element, InteractionOccurrence):

    pass
class UML2WithID_MessageEnd(Element, NamedElement):

    pass
class UML2WithID_LinkAction(Element, Action):

    pass
class UML2WithID_LiteralUnlimitedNatural(Element, LiteralSpecification):

    pass
class UML2WithID_Device(Element, Node):

    pass
class UML2WithID_Region(Element, RedefinableElement, Namespace):

    pass
class UML2WithID_ActivityEdge(Element, RedefinableElement):

    pass
class UML2WithID_Transition(Element, RedefinableElement):

    pass
class UML2WithID_Artifact(Element, DeployedArtifact, Classifier):

    pass
class UML2WithID_Extension(Element, Association):

    pass
class UML2WithID_ConditionalNode(Element, StructuredActivityNode):

    pass
class UML2WithID_ConnectableElement(Element, NamedElement):

    pass
class UML2WithID_Interaction(InteractionFragment, Behavior, Element):

    pass
class UML2WithID_CallAction(Element, InvocationAction):

    pass
class Class:

    pass
class UML2WithID_Behavior(Element, Class):

    pass
class UML2WithID_Stereotype(Class, Element):

    pass
class UML2WithID_AssociationClass(Element, Association, Class):

    pass
class UML2WithID_Node(Class, Element, DeploymentTarget):

    pass
class UML2WithID_Component(Class, Element):

    pass
class UML2WithID_Feature(Element, RedefinableElement):

    pass
class Artifact:

    pass
class UML2WithID_DeploymentSpecification(Element, Artifact):

    pass
class UML2WithID_TemplateableClassifier(Element, Classifier):

    pass
class UML2WithID_DataType(Element, Classifier):

    pass
class UML2WithID_RaiseExceptionAction(Element, Action):

    pass
class UML2WithID_InteractionFragment(Element, NamedElement):

    pass
class UML2WithID_Reception(Element, BehavioralFeature):

    pass
class UML2WithID_InitialNode(Element, ControlNode):

    pass
class UML2WithID_JoinNode(Element, ControlNode):

    pass
class UML2WithID_Namespace(Element, NamedElement):

    pass
class UML2WithID_OutputPin(Element, Pin):

    pass
class Constraint:

    pass
class UML2WithID_IntervalConstraint(Element, Constraint):

    pass
class UML2WithID_InteractionConstraint(Element, Constraint):

    pass
class UML2WithID_ReadLinkObjectEndQualifierAction(Element, Action):

    pass
class UML2WithID_SendSignalAction(Element, InvocationAction):

    pass
class UML2WithID_InformationFlow(PackageableElement, Element):

    pass
class Trigger:

    pass
class UML2WithID_ChangeTrigger(Element, Trigger):

    pass
class UML2WithID_TimeTrigger(Element, Trigger):

    pass
class UML2WithID_MessageTrigger(Element, Trigger):

    pass
class UML2WithID_AcceptEventAction(Element, Action):

    pass
class UML2WithID_PrimitiveFunction(PackageableElement, Element):

    pass
class CallAction:

    pass
class UML2WithID_CallOperationAction(Element, CallAction):

    pass
class UML2WithID_CallBehaviorAction(Element, CallAction):

    pass
class UML2WithID_LoopNode(Element, StructuredActivityNode):

    pass
class IntervalConstraint:

    pass
class UML2WithID_DurationConstraint(Element, IntervalConstraint):

    pass
class UML2WithID_TimeConstraint(Element, IntervalConstraint):

    pass