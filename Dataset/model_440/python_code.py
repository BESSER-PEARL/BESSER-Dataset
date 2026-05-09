from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class CreateLinkAction:

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


class Realization:

    pass
class DataType:

    pass
class MessageEnd:

    pass
class AcceptEventAction:

    pass
class StructuralFeature:

    pass
class IntervalConstraint:

    pass
class Feature:

    pass
class InteractionFragment:

    pass
class Artifact:

    pass
class DeployedArtifact:

    pass
class Property:

    pass
class Package:

    pass
class Pin:

    pass
class InputPin:

    pass
class BehavioralFeature:

    pass
class InstanceSpecification:

    pass
class OpaqueExpression:

    pass
class DeploymentTarget:

    pass
class WriteLinkAction:

    pass
class EncapsulatedClassifier:

    pass
class State:

    pass
class Trigger:

    pass
class Association:

    pass
class Class:

    pass
class Abstraction:

    pass
class Transition:

    pass
class InvocationAction:

    pass
class StateMachine:

    pass
class ExecutableNode:

    pass
class Type:

    pass
class FinalNode:

    pass
class LinkAction:

    pass
class CentralBufferNode:

    pass
class LiteralSpecification:

    pass
class ActivityEdge:

    pass
class StructuralFeatureAction:

    pass
class WriteStructuralFeatureAction:

    pass
class Node:

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
class CallAction:

    pass
class NamedElement:

    pass
class TypedElement:

    pass
class ActivityNode:

    pass
class ValueSpecification:

    pass
class WriteVariableAction:

    pass
class EventOccurrence:

    pass
class Constraint:

    pass
class Action:

    pass
class StructuredActivityNode:

    pass
class PackageableElement:

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
class UML2WithID_Implementation(Element, Realization):

    pass
class UML2WithID_MergeNode(Element, ControlNode):

    pass
class UML2WithID_ActivityEdge(Element, RedefinableElement):

    pass
class UML2WithID_Realization(Element, Abstraction):

    pass
class UML2WithID_Node(Element, DeploymentTarget, Class):

    pass
class UML2WithID_LiteralUnlimitedNatural(Element, LiteralSpecification):

    pass
class UML2WithID_DestroyLinkAction(Element, WriteLinkAction):

    pass
class UML2WithID_Deployment(Element, Dependency):

    pass
class UML2WithID_ReadIsClassifiedObjectAction(Element, Action):

    pass
class UML2WithID_InformationFlow(Element, PackageableElement):

    pass
class UML2WithID_CombinedFragment(Element, InteractionFragment):

    pass
class UML2WithID_Package(Element, PackageableElement, Namespace):

    pass
class UML2WithID_ExtensionEnd(Element, Property):

    pass
class UML2WithID_Connector(Element, Feature):

    pass
class UML2WithID_ExecutableNode(Element, ActivityNode):

    pass
class UML2WithID_CallOperationAction(Element, CallAction):

    pass
class UML2WithID_ConditionalNode(Element, StructuredActivityNode):

    pass
class UML2WithID_ReadStructuralFeatureAction(Element, StructuralFeatureAction):

    pass
class UML2WithID_Actor(Element, Classifier):

    pass
class UML2WithID_Continuation(Element, InteractionFragment):

    pass
class UML2WithID_DataType(Element, Classifier):

    pass
class UML2WithID_DurationObservationAction(Element, WriteStructuralFeatureAction):

    pass
class UML2WithID_Stereotype(Element, Class):

    pass
class UML2WithID_RemoveVariableValueAction(Element, WriteVariableAction):

    pass
class UML2WithID_ExecutionEnvironment(Element, Node):

    pass
class UML2WithID_InitialNode(Element, ControlNode):

    pass
class UML2WithID_ReadLinkObjectEndQualifierAction(Element, Action):

    pass
class UML2WithID_ExpansionRegion(Element, StructuredActivityNode):

    pass
class UML2WithID_Port(Element, Property):

    pass
class UML2WithID_PrimitiveFunction(Element, PackageableElement):

    pass
class UML2WithID_Usage(Element, Dependency):

    pass
class UML2WithID_EnumerationLiteral(Element, InstanceSpecification):

    pass
class UML2WithID_ObjectNode(Element, ActivityNode, TypedElement):

    pass
class UML2WithID_Permission(Element, Dependency):

    pass
class UML2WithID_FinalNode(Element, ControlNode):

    pass
class UML2WithID_BroadcastSignalAction(Element, InvocationAction):

    pass
class UML2WithID_LiteralBoolean(Element, LiteralSpecification):

    pass
class UML2WithID_CollaborationOccurrence(Element, NamedElement):

    pass
class UML2WithID_Pseudostate(Element, Vertex):

    pass
class UML2WithID_CallTrigger(Element, MessageTrigger):

    pass
class UML2WithID_ClearAssociationAction(Element, Action):

    pass
class UML2WithID_RaiseExceptionAction(Element, Action):

    pass
class UML2WithID_ReadLinkObjectEndAction(Element, Action):

    pass
class UML2WithID_Extend(Element, NamedElement):

    pass
class UML2WithID_CentralBufferNode(Element, ObjectNode):

    pass
class UML2WithID_DeploymentTarget(Element, NamedElement):

    pass
class UML2WithID_Behavior(Element, Class):

    pass
class UML2WithID_IntervalConstraint(Element, Constraint):

    pass
class UML2WithID_StructuralFeature(Element, TypedElement, Feature):

    pass
class UML2WithID_AcceptEventAction(Element, Action):

    pass
class UML2WithID_OutputPin(Element, Pin):

    pass
class UML2WithID_DataStoreNode(Element, CentralBufferNode):

    pass
class UML2WithID_InteractionOccurrence(Element, InteractionFragment):

    pass
class UML2WithID_MessageEnd(Element, NamedElement):

    pass
class UML2WithID_StructuralFeatureAction(Element, Action):

    pass
class UML2WithID_ForkNode(Element, ControlNode):

    pass
class UML2WithID_Reception(Element, BehavioralFeature):

    pass
class UML2WithID_InstanceValue(Element, ValueSpecification):

    pass
class UML2WithID_RemoveStructuralFeatureValueAction(Element, WriteStructuralFeatureAction):

    pass
class UML2WithID_PartDecomposition(Element, InteractionOccurrence):

    pass
class UML2WithID_ActivityPartition(Element, NamedElement):

    pass
class UML2WithID_StructuredActivityNode(Namespace, Element, Action):

    pass
class UML2WithID_FlowFinalNode(Element, FinalNode):

    pass
class UML2WithID_Type(Element, PackageableElement):

    pass
class UML2WithID_ReclassifyObjectAction(Element, Action):

    pass
class UML2WithID_LoopNode(Element, StructuredActivityNode):

    pass
class UML2WithID_Include(Element, NamedElement):

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


class UML2WithID_DecisionNode(Element, ControlNode):

    pass
class UML2WithID_Device(Element, Node):

    pass
class UML2WithID_StateMachine(Element, Behavior):

    pass
class UML2WithID_LiteralString(Element, LiteralSpecification):

    pass
class UML2WithID_GeneralOrdering(Element, NamedElement):

    pass
class UML2WithID_TimeInterval(Element, Interval):

    pass
class UML2WithID_BehavioredClassifier(Element, Classifier):

    pass
class UML2WithID_ControlNode(Element, ActivityNode):

    pass
class UML2WithID_TimeObservationAction(Element, WriteStructuralFeatureAction):

    pass
class UML2WithID_Gate(MessageEnd, Element):

    pass
class UML2WithID_TimeExpression(Element, ValueSpecification):

    pass
class UML2WithID_ExtensionPoint(Element, RedefinableElement):

    pass
class UML2WithID_Message(Element, NamedElement):

    pass
class UML2WithID_TimeConstraint(Element, IntervalConstraint):

    pass
class UML2WithID_CallBehaviorAction(Element, CallAction):

    pass
class UML2WithID_TimeTrigger(Element, Trigger):

    pass
class UML2WithID_DestroyObjectAction(Element, Action):

    pass
class UML2WithID_RedefinableTemplateSignature(Element, RedefinableElement):

    pass
class UML2WithID_ActivityParameterNode(Element, ObjectNode):

    pass
class UML2WithID_ParameterSet(Element, NamedElement):

    pass
class UML2WithID_InteractionOperand(Namespace, Element, InteractionFragment):

    pass
class UML2WithID_ExpansionNode(Element, ObjectNode):

    pass
class UML2WithID_InputPin(Element, Pin):

    pass
class UML2WithID_SendSignalAction(Element, InvocationAction):

    pass
class UML2WithID_BehavioralFeature(Namespace, Element, Feature):

    pass
class UML2WithID_InstanceSpecification(Element, DeploymentTarget, DeployedArtifact, PackageableElement):

    pass
class UML2WithID_PrimitiveType(Element, DataType):

    pass
class UML2WithID_DurationConstraint(Element, IntervalConstraint):

    pass
class UML2WithID_AddVariableValueAction(Element, WriteVariableAction):

    pass
class UML2WithID_Model(Element, Package):

    pass
class UML2WithID_DeployedArtifact(Element, NamedElement):

    pass
class UML2WithID_ConnectableElement(Element, NamedElement):

    pass
class UML2WithID_Region(Namespace, Element, RedefinableElement):

    pass
class UML2WithID_StateInvariant(Element, InteractionFragment):

    pass
class UML2WithID_Constraint(Element, PackageableElement):

    pass
class UML2WithID_AcceptCallAction(Element, AcceptEventAction):

    pass
class UML2WithID_ConnectionPointReference(Element, Vertex):

    pass
class UML2WithID_Interface(Element, Classifier):

    pass
class UML2WithID_Dependency(Element, PackageableElement):

    pass
class UML2WithID_Action(ExecutableNode, Element):

    pass
class UML2WithID_Interval(Element, ValueSpecification):

    pass
class UML2WithID_InteractionConstraint(Element, Constraint):

    pass
class UML2WithID_DeploymentSpecification(Element, Artifact):

    pass
class UML2WithID_Class(Element, EncapsulatedClassifier, BehavioredClassifier):

    pass
class UML2WithID_EncapsulatedClassifier(Element, StructuredClassifier):

    pass
class UML2WithID_Feature(Element, RedefinableElement):

    pass
class UML2WithID_UseCase(Element, BehavioredClassifier):

    pass
class UML2WithID_CreateLinkAction(Element, WriteLinkAction):

    pass
class UML2WithID_TemplateableClassifier(Element, Classifier):

    pass
class UML2WithID_ActivityFinalNode(Element, FinalNode):

    pass
class UML2WithID_ClearVariableAction(Element, VariableAction):

    pass
class UML2WithID_ReplyAction(Element, Action):

    pass
class UML2WithID_AssociationClass(Element, Class, Association):

    pass
class UML2WithID_EventOccurrence(Element, InteractionFragment, MessageEnd):

    pass
class UML2WithID_Collaboration(Element, StructuredClassifier, BehavioredClassifier):

    pass
class UML2WithID_DurationInterval(Element, Interval):

    pass
class UML2WithID_ParameterableClassifier(Element, Classifier):

    pass
class UML2WithID_ValuePin(Element, InputPin):

    pass
class UML2WithID_PackageableElement(Element, NamedElement):

    pass
class UML2WithID_ObjectFlow(Element, ActivityEdge):

    pass
class UML2WithID_Lifeline(Element, NamedElement):

    pass
class UML2WithID_Variable(ConnectableElement, Element, TypedElement):

    pass
class UML2WithID_Artifact(Element, DeployedArtifact, Classifier):

    pass
class UML2WithID_CallAction(Element, InvocationAction):

    pass
class UML2WithID_CommunicationPath(Element, Association):

    pass
class UML2WithID_InformationItem(Element, Classifier):

    pass
class UML2WithID_Profile(Element, Package):

    pass
class UML2WithID_ReadSelfAction(Element, Action):

    pass
class UML2WithID_Activity(Behavior, Element):

    pass
class UML2WithID_Pin(Element, ObjectNode):

    pass
class UML2WithID_Substitution(Element, Realization):

    pass
class UML2WithID_FinalState(Element, State):

    pass
class UML2WithID_AnyTrigger(Element, MessageTrigger):

    pass
class UML2WithID_WriteStructuralFeatureAction(Element, StructuralFeatureAction):

    pass
class UML2WithID_JoinNode(Element, ControlNode):

    pass
class UML2WithID_InvocationAction(Element, Action):

    pass
class UML2WithID_ExecutionOccurrence(Element, InteractionFragment):

    pass
class UML2WithID_Parameter(ConnectableElement, Element, TypedElement):

    pass
class UML2WithID_ReadVariableAction(Element, VariableAction):

    pass
class UML2WithID_WriteLinkAction(Element, LinkAction):

    pass
class UML2WithID_SendObjectAction(Element, InvocationAction):

    pass
class UML2WithID_RedefinableElement(Element, NamedElement):

    pass
class UML2WithID_ClearStructuralFeatureAction(Element, StructuralFeatureAction):

    pass
class UML2WithID_LiteralNull(Element, LiteralSpecification):

    pass
class UML2WithID_GeneralizationSet(Element, PackageableElement):

    pass
class UML2WithID_Namespace(Element, NamedElement):

    pass
class UML2WithID_SignalTrigger(Element, MessageTrigger):

    pass
class UML2WithID_StartOwnedBehaviorAction(Element, Action):

    pass
class UML2WithID_Signal(Element, Classifier):

    pass
class UML2WithID_LinkAction(Element, Action):

    pass
class UML2WithID_ActivityNode(Element, RedefinableElement):

    pass
class UML2WithID_CreateObjectAction(Element, Action):

    pass
class UML2WithID_ProtocolTransition(Element, Transition):

    pass
class UML2WithID_TestIdentityAction(Element, Action):

    pass
class UML2WithID_Expression(Element, OpaqueExpression):

    pass
class UML2WithID_LiteralInteger(Element, LiteralSpecification):

    pass
class UML2WithID_Stop(Element, EventOccurrence):

    pass
class UML2WithID_InteractionFragment(Element, NamedElement):

    pass
class UML2WithID_ChangeTrigger(Element, Trigger):

    pass
class UML2WithID_ControlFlow(Element, ActivityEdge):

    pass
class UML2WithID_MessageTrigger(Element, Trigger):

    pass
class UML2WithID_ReadLinkAction(LinkAction, Element):

    pass
class UML2WithID_ReadExtentAction(Element, Action):

    pass
class UML2WithID_Enumeration(Element, DataType):

    pass
class UML2WithID_Extension(Element, Association):

    pass
class UML2WithID_Manifestation(Element, Abstraction):

    pass
class UML2WithID_ApplyFunctionAction(Element, Action):

    pass
class UML2WithID_WriteVariableAction(Element, VariableAction):

    pass
class UML2WithID_ValueSpecification(Element, TypedElement):

    pass
class UML2WithID_ProtocolStateMachine(Element, StateMachine):

    pass
class UML2WithID_Property(Element, DeploymentTarget, ConnectableElement, StructuralFeature):

    pass
class UML2WithID_Interaction(Element, Behavior, InteractionFragment):

    pass
class UML2WithID_Classifier(Namespace, RedefinableElement, Type, Element):

    pass
class UML2WithID_Abstraction(Element, Dependency):

    pass
class UML2WithID_State(Namespace, Element, RedefinableElement, Vertex):

    pass
class UML2WithID_OpaqueExpression(Element, ValueSpecification):

    pass
class UML2WithID_Trigger(Element, NamedElement):

    pass
class UML2WithID_TypedElement(Element, NamedElement):

    pass
class UML2WithID_Vertex(Element, NamedElement):

    pass
class UML2WithID_Duration(Element, ValueSpecification):

    pass
class UML2WithID_AddStructuralFeatureValueAction(Element, WriteStructuralFeatureAction):

    pass
class UML2WithID_Transition(Element, RedefinableElement):

    pass
class UML2WithID_CreateLinkObjectAction(Element, CreateLinkAction):

    pass
class UML2WithID_LiteralSpecification(Element, ValueSpecification):

    pass
class UML2WithID_VariableAction(Element, Action):

    pass
class UML2WithID_Component(Element, Class):

    pass
class UML2WithID_StructuredClassifier(Element, Classifier):

    pass
class UML2WithID_Operation(Element, TypedElement, BehavioralFeature):

    pass
class UML2WithID_Association(Element, Classifier):

    pass