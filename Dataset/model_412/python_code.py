from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class VisibilityKind(Enum):
    package = "package"
    private = "private"
    protected = "protected"
    public = "public"


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

class EventOccurrence:

    pass
class Transition:

    pass
class Type:

    pass
class CallAction:

    pass
class Dependency:

    pass
class EncapsulatedClassifier:

    pass
class InstanceSpecification:

    pass
class Node:

    pass
class StateMachine:

    pass
class OpaqueExpression:

    pass
class StructuralFeature:

    pass
class MessageEnd:

    pass
class MessageTrigger:

    pass
class ActivityEdge:

    pass
class Package:

    pass
class ObjectNode:

    pass
class ControlNode:

    pass
class CreateLinkAction:

    pass
class Trigger:

    pass
class Abstraction:

    pass
class WriteLinkAction:

    pass
class StructuredActivityNode:

    pass
class FinalNode:

    pass
class StructuralFeatureAction:

    pass
class Property:

    pass
class Vertex:

    pass
class Interval:

    pass
class ConnectableElement:

    pass
class Artifact:

    pass
class Feature:

    pass
class State:

    pass
class VariableAction:

    pass
class StructuredClassifier:

    pass
class BehavioredClassifier:

    pass
class Association:

    pass
class BehavioralFeature:

    pass
class AcceptEventAction:

    pass
class InvocationAction:

    pass
class LiteralSpecification:

    pass
class DataType:

    pass
class InteractionOccurrence:

    pass
class DeploymentTarget:

    pass
class Class:

    pass
class IntervalConstraint:

    pass
class ExecutableNode:

    pass
class Classifier:

    pass
class Behavior:

    pass
class InputPin:

    pass
class Realization:

    pass
class TypedElement:

    pass
class ActivityNode:

    pass
class ValueSpecification:

    pass
class NamedElement:

    pass
class RedefinableElement:

    pass
class Constraint:

    pass
class WriteVariableAction:

    pass
class LinkAction:

    pass
class CentralBufferNode:

    pass
class InteractionFragment:

    pass
class Namespace:

    pass
class Element:

    pass
class UML2WithID_WriteStructuralFeatureAction(Element, StructuralFeatureAction):

    pass
class UML2WithID_DataStoreNode(CentralBufferNode, Element):

    pass
class UML2WithID_EventOccurrence(MessageEnd, Element, InteractionFragment):

    pass
class UML2WithID_Deployment(Element, Dependency):

    pass
class UML2WithID_ClearStructuralFeatureAction(Element, StructuralFeatureAction):

    pass
class UML2WithID_InteractionConstraint(Constraint, Element):

    pass
class UML2WithID_ActivityFinalNode(FinalNode, Element):

    pass
class UML2WithID_ExpansionNode(ObjectNode, Element):

    pass
class UML2WithID_LiteralString(LiteralSpecification, Element):

    pass
class UML2WithID_DurationConstraint(Element, IntervalConstraint):

    pass
class UML2WithID_UseCase(Element, BehavioredClassifier):

    pass
class UML2WithID_MessageTrigger(Element, Trigger):

    pass
class UML2WithID_Extension(Association, Element):

    pass
class UML2WithID_TypedElement(NamedElement, Element):

    pass
class UML2WithID_DeploymentSpecification(Artifact, Element):

    pass
class UML2WithID_ActivityNode(Element, RedefinableElement):

    pass
class UML2WithID_ProtocolStateMachine(StateMachine, Element):

    pass
class UML2WithID_InteractionOccurrence(Element, InteractionFragment):

    pass
class UML2WithID_ReadStructuralFeatureAction(Element, StructuralFeatureAction):

    pass
class UML2WithID_Implementation(Element, Realization):

    pass
class UML2WithID_ActivityPartition(NamedElement, Element):

    pass
class UML2WithID_InteractionFragment(NamedElement, Element):

    pass
class UML2WithID_TimeInterval(Interval, Element):

    pass
class UML2WithID_ExtensionEnd(Property, Element):

    pass
class UML2WithID_LoopNode(StructuredActivityNode, Element):

    pass
class UML2WithID_Permission(Element, Dependency):

    pass
class UML2WithID_ActivityEdge(Element, RedefinableElement):

    pass
class UML2WithID_Interaction(Element, Behavior, InteractionFragment):

    pass
class UML2WithID_Parameter(TypedElement, Element, ConnectableElement):

    pass
class UML2WithID_StructuralFeature(TypedElement, Feature, Element):

    pass
class UML2WithID_Transition(Element, RedefinableElement):

    pass
class UML2WithID_Action(ExecutableNode, Element):

    pass
class UML2WithID_Stereotype(Class, Element):

    pass
class UML2WithID_Pin(ObjectNode, Element):

    pass
class UML2WithID_ExecutionEnvironment(Element, Node):

    pass
class UML2WithID_Signal(Classifier, Element):

    pass
class UML2WithID_IntervalConstraint(Element, Constraint):

    pass
class UML2WithID_Trigger(NamedElement, Element):

    pass
class UML2WithID_ConditionalNode(StructuredActivityNode, Element):

    pass
class UML2WithID_Message(NamedElement, Element):

    pass
class UML2WithID_State(Namespace, Element, Vertex, RedefinableElement):

    pass
class UML2WithID_ExtensionPoint(Element, RedefinableElement):

    pass
class UML2WithID_Association(Classifier, Element):

    pass
class UML2WithID_Pseudostate(Element, Vertex):

    pass
class UML2WithID_Interface(Classifier, Element):

    pass
class UML2WithID_SendSignalAction(Element, InvocationAction):

    pass
class UML2WithID_ActivityParameterNode(ObjectNode, Element):

    pass
class UML2WithID_ParameterableClassifier(Classifier, Element):

    pass
class UML2WithID_CentralBufferNode(ObjectNode, Element):

    pass
class UML2WithID_BehavioredClassifier(Classifier, Element):

    pass
class UML2WithID_SendObjectAction(Element, InvocationAction):

    pass
class UML2WithID_ChangeTrigger(Element, Trigger):

    pass
class UML2WithID_DeployedArtifact(NamedElement, Element):

    pass
class UML2WithID_ExpansionRegion(StructuredActivityNode, Element):

    pass
class UML2WithID_Activity(Element, Behavior):

    pass
class UML2WithID_InteractionOperand(Namespace, Element, InteractionFragment):

    pass
class UML2WithID_AnyTrigger(MessageTrigger, Element):

    pass
class UML2WithID_StateInvariant(Element, InteractionFragment):

    pass
class UML2WithID_LiteralInteger(LiteralSpecification, Element):

    pass
class UML2WithID_Variable(TypedElement, Element, ConnectableElement):

    pass
class UML2WithID_InstanceValue(ValueSpecification, Element):

    pass
class UML2WithID_ValueSpecification(TypedElement, Element):

    pass
class UML2WithID_Profile(Element, Package):

    pass
class UML2WithID_TimeExpression(ValueSpecification, Element):

    pass
class UML2WithID_LiteralSpecification(ValueSpecification, Element):

    pass
class UML2WithID_ForkNode(ControlNode, Element):

    pass
class UML2WithID_Device(Element, Node):

    pass
class UML2WithID_Model(Element, Package):

    pass
class UML2WithID_AddVariableValueAction(Element, WriteVariableAction):

    pass
class UML2WithID_ValuePin(InputPin, Element):

    pass
class UML2WithID_Lifeline(NamedElement, Element):

    pass
class UML2WithID_LiteralNull(LiteralSpecification, Element):

    pass
class UML2WithID_Realization(Element, Abstraction):

    pass
class UML2WithID_MergeNode(ControlNode, Element):

    pass
class UML2WithID_JoinNode(ControlNode, Element):

    pass
class UML2WithID_TimeConstraint(Element, IntervalConstraint):

    pass
class UML2WithID_InformationItem(Classifier, Element):

    pass
class UML2WithID_RedefinableElement(NamedElement, Element):

    pass
class UML2WithID_PartDecomposition(InteractionOccurrence, Element):

    pass
class UML2WithID_FinalState(State, Element):

    pass
class UML2WithID_Gate(MessageEnd, Element):

    pass
class UML2WithID_SignalTrigger(MessageTrigger, Element):

    pass
class UML2WithID_Reception(Element, BehavioralFeature):

    pass
class UML2WithID_CreateLinkObjectAction(Element, CreateLinkAction):

    pass
class UML2WithID_Component(Class, Element):

    pass
class UML2WithID_Extend(NamedElement, Element):

    pass
class UML2WithID_Behavior(Class, Element):

    pass
class UML2WithID_Actor(Classifier, Element):

    pass
class UML2WithID_EnumerationLiteral(Element, InstanceSpecification):

    pass
class UML2WithID_Substitution(Element, Realization):

    pass
class UML2WithID_ParameterSet(NamedElement, Element):

    pass
class UML2WithID_Duration(ValueSpecification, Element):

    pass
class UML2WithID_DestroyLinkAction(WriteLinkAction, Element):

    pass
class UML2WithID_ReadLinkAction(LinkAction, Element):

    pass
class UML2WithID_ControlNode(ActivityNode, Element):

    pass
class UML2WithID_ObjectNode(ActivityNode, TypedElement, Element):

    pass
class UML2WithID_FlowFinalNode(FinalNode, Element):

    pass
class UML2WithID_TimeTrigger(Element, Trigger):

    pass
class UML2WithID_Namespace(NamedElement, Element):

    pass
class UML2WithID_Interval(ValueSpecification, Element):

    pass
class UML2WithID_ClearVariableAction(VariableAction, Element):

    pass
class UML2WithID_Property(StructuralFeature, Element, ConnectableElement, DeploymentTarget):

    pass
class UML2WithID_StateMachine(Element, Behavior):

    pass
class UML2WithID_CallTrigger(MessageTrigger, Element):

    pass
class UML2WithID_DecisionNode(ControlNode, Element):

    pass
class UML2WithID_CreateLinkAction(WriteLinkAction, Element):

    pass
class UML2WithID_AcceptCallAction(AcceptEventAction, Element):

    pass
class UML2WithID_CallOperationAction(CallAction, Element):

    pass
class UML2WithID_Connector(Feature, Element):

    pass
class UML2WithID_Include(NamedElement, Element):

    pass
class UML2WithID_Usage(Element, Dependency):

    pass
class UML2WithID_TemplateableClassifier(Classifier, Element):

    pass
class UML2WithID_DurationInterval(Interval, Element):

    pass
class UML2WithID_Manifestation(Element, Abstraction):

    pass
class UML2WithID_InitialNode(ControlNode, Element):

    pass
class UML2WithID_Class(Element, EncapsulatedClassifier, BehavioredClassifier):

    pass
class UML2WithID_FinalNode(ControlNode, Element):

    pass
class UML2WithID_WriteVariableAction(VariableAction, Element):

    pass
class UML2WithID_PackageableElement(NamedElement, Element):

    pass
class UML2WithID_LiteralBoolean(LiteralSpecification, Element):

    pass
class UML2WithID_Enumeration(DataType, Element):

    pass
class UML2WithID_WriteLinkAction(LinkAction, Element):

    pass
class UML2WithID_OpaqueExpression(ValueSpecification, Element):

    pass
class UML2WithID_Collaboration(StructuredClassifier, Element, BehavioredClassifier):

    pass
class UML2WithID_MessageEnd(NamedElement, Element):

    pass
class UML2WithID_Abstraction(Element, Dependency):

    pass
class UML2WithID_RemoveVariableValueAction(Element, WriteVariableAction):

    pass
class UML2WithID_CommunicationPath(Association, Element):

    pass
class UML2WithID_Operation(TypedElement, Element, BehavioralFeature):

    pass
class UML2WithID_Region(Namespace, Element, RedefinableElement):

    pass
class UML2WithID_PrimitiveType(DataType, Element):

    pass
class UML2WithID_ObjectFlow(ActivityEdge, Element):

    pass
class UML2WithID_CallAction(Element, InvocationAction):

    pass
class UML2WithID_BroadcastSignalAction(Element, InvocationAction):

    pass
class UML2WithID_EncapsulatedClassifier(StructuredClassifier, Element):

    pass
class UML2WithID_Classifier(Namespace, Type, Element, RedefinableElement):

    pass
class UML2WithID_ConnectionPointReference(Element, Vertex):

    pass
class UML2WithID_ExecutableNode(ActivityNode, Element):

    pass
class UML2WithID_NamedElement(Element):

    def __init__(self, visibility: str, UML2WithID_NamedElement: "UML2WithID_Namespace" = None):
        self.visibility = visibility
        self.UML2WithID_NamedElement = UML2WithID_NamedElement
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def UML2WithID_NamedElement(self):
        return self.__UML2WithID_NamedElement

    @UML2WithID_NamedElement.setter
    def UML2WithID_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_NamedElement__UML2WithID_NamedElement", None)
        self.__UML2WithID_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Namespace"):
                opp_val = getattr(old_value, "UML2WithID_Namespace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Namespace"):
                opp_val = getattr(value, "UML2WithID_Namespace", None)
                if opp_val is None:
                    setattr(value, "UML2WithID_Namespace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UML2WithID_Vertex(NamedElement, Element):

    pass
class UML2WithID_LiteralUnlimitedNatural(LiteralSpecification, Element):

    pass
class UML2WithID_Expression(Element, OpaqueExpression):

    pass
class UML2WithID_DataType(Classifier, Element):

    pass
class UML2WithID_Node(Class, Element, DeploymentTarget):

    pass
class UML2WithID_Continuation(Element, InteractionFragment):

    pass
class UML2WithID_ControlFlow(ActivityEdge, Element):

    pass
class UML2WithID_ExecutionOccurrence(Element, InteractionFragment):

    pass
class UML2WithID_RedefinableTemplateSignature(Element, RedefinableElement):

    pass
class UML2WithID_Feature(Element, RedefinableElement):

    pass
class UML2WithID_Stop(EventOccurrence, Element):

    pass
class UML2WithID_DeploymentTarget(NamedElement, Element):

    pass
class UML2WithID_ReadVariableAction(VariableAction, Element):

    pass
class UML2WithID_ConnectableElement(NamedElement, Element):

    pass
class UML2WithID_ProtocolTransition(Transition, Element):

    pass
class UML2WithID_CombinedFragment(Element, InteractionFragment):

    pass
class UML2WithID_GeneralOrdering(NamedElement, Element):

    pass
class UML2WithID_Port(Property, Element):

    pass
class UML2WithID_BehavioralFeature(Namespace, Feature, Element):

    pass
class UML2WithID_CallBehaviorAction(CallAction, Element):

    pass
class UML2WithID_AssociationClass(Association, Class, Element):

    pass
class Action:

    pass
class UML2WithID_StructuredActivityNode(Namespace, Element, Action):

    pass
class UML2WithID_ClearAssociationAction(Element, Action):

    pass
class UML2WithID_VariableAction(Element, Action):

    pass
class UML2WithID_ReclassifyObjectAction(Element, Action):

    pass
class UML2WithID_DestroyObjectAction(Element, Action):

    pass
class UML2WithID_ReadIsClassifiedObjectAction(Element, Action):

    pass
class UML2WithID_ReadSelfAction(Element, Action):

    pass
class UML2WithID_TestIdentityAction(Element, Action):

    pass
class UML2WithID_InvocationAction(Element, Action):

    pass
class UML2WithID_AcceptEventAction(Element, Action):

    pass
class UML2WithID_StartOwnedBehaviorAction(Element, Action):

    pass
class UML2WithID_StructuralFeatureAction(Element, Action):

    pass
class UML2WithID_ReadLinkObjectEndAction(Element, Action):

    pass
class UML2WithID_ApplyFunctionAction(Element, Action):

    pass
class UML2WithID_ReplyAction(Element, Action):

    pass
class UML2WithID_CreateObjectAction(Element, Action):

    pass
class UML2WithID_ReadExtentAction(Element, Action):

    pass
class UML2WithID_RaiseExceptionAction(Element, Action):

    pass
class UML2WithID_LinkAction(Element, Action):

    pass
class UML2WithID_ReadLinkObjectEndQualifierAction(Element, Action):

    pass
class UML2WithID_StructuredClassifier(Classifier, Element):

    pass
class WriteStructuralFeatureAction:

    pass
class UML2WithID_DurationObservationAction(Element, WriteStructuralFeatureAction):

    pass
class UML2WithID_TimeObservationAction(Element, WriteStructuralFeatureAction):

    pass
class UML2WithID_AddStructuralFeatureValueAction(Element, WriteStructuralFeatureAction):

    pass
class UML2WithID_RemoveStructuralFeatureValueAction(Element, WriteStructuralFeatureAction):

    pass
class Pin:

    pass
class UML2WithID_InputPin(Pin, Element):

    pass
class UML2WithID_OutputPin(Pin, Element):

    pass
class DeployedArtifact:

    pass
class UML2WithID_Artifact(Classifier, DeployedArtifact, Element):

    pass
class UML2WithID_CollaborationOccurrence(NamedElement, Element):

    pass
class PackageableElement:

    pass
class UML2WithID_GeneralizationSet(PackageableElement, Element):

    pass
class UML2WithID_Constraint(PackageableElement, Element):

    pass
class UML2WithID_Package(Namespace, PackageableElement, Element):

    pass
class UML2WithID_InstanceSpecification(DeployedArtifact, PackageableElement, Element, DeploymentTarget):

    pass
class UML2WithID_Type(PackageableElement, Element):

    pass
class UML2WithID_InformationFlow(PackageableElement, Element):

    pass
class UML2WithID_Dependency(PackageableElement, Element):

    pass
class UML2WithID_PrimitiveFunction(PackageableElement, Element):

    pass