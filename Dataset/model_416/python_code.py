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

class EncapsulatedClassifier:

    pass
class Abstraction:

    pass
class WriteVariableAction:

    pass
class Artifact:

    pass
class EventOccurrence:

    pass
class Constraint:

    pass
class StateMachine:

    pass
class State:

    pass
class InstanceSpecification:

    pass
class WriteLinkAction:

    pass
class AcceptEventAction:

    pass
class ExecutableNode:

    pass
class IntervalConstraint:

    pass
class CallAction:

    pass
class VariableAction:

    pass
class Transition:

    pass
class LinkAction:

    pass
class Feature:

    pass
class FinalNode:

    pass
class Type:

    pass
class InteractionOccurrence:

    pass
class DataType:

    pass
class Node:

    pass
class BehavioredClassifier:

    pass
class StructuredClassifier:

    pass
class InputPin:

    pass
class Association:

    pass
class OpaqueExpression:

    pass
class StructuralFeatureAction:

    pass
class Pin:

    pass
class ActivityEdge:

    pass
class Class:

    pass
class Package:

    pass
class RedefinableElement:

    pass
class Realization:

    pass
class ValueSpecification:

    pass
class Dependency:

    pass
class MessageTrigger:

    pass
class Behavior:

    pass
class StructuredActivityNode:

    pass
class ConnectableElement:

    pass
class StructuralFeature:

    pass
class InvocationAction:

    pass
class BehavioralFeature:

    pass
class Interval:

    pass
class Vertex:

    pass
class Trigger:

    pass
class MessageEnd:

    pass
class Property:

    pass
class DeployedArtifact:

    pass
class DeploymentTarget:

    pass
class PackageableElement:

    pass
class CentralBufferNode:

    pass
class ObjectNode:

    pass
class Classifier:

    pass
class LiteralSpecification:

    pass
class ControlNode:

    pass
class TypedElement:

    pass
class ActivityNode:

    pass
class InteractionFragment:

    pass
class NamedElement:

    pass
class Namespace:

    pass
class Action:

    pass
class CreateLinkAction:

    pass
class Element:

    pass
class UML2WithID_StructuralFeature(TypedElement, Feature, Element):

    pass
class UML2WithID_CreateLinkObjectAction(CreateLinkAction, Element):

    pass
class UML2WithID_ClearAssociationAction(Element, Action):

    pass
class UML2WithID_ReadLinkObjectEndAction(Element, Action):

    pass
class UML2WithID_ParameterableClassifier(Element, Classifier):

    pass
class UML2WithID_Model(Package, Element):

    pass
class UML2WithID_CollaborationOccurrence(NamedElement, Element):

    pass
class UML2WithID_ExtensionPoint(Element, RedefinableElement):

    pass
class UML2WithID_WriteVariableAction(Element, VariableAction):

    pass
class UML2WithID_LiteralBoolean(LiteralSpecification, Element):

    pass
class UML2WithID_Parameter(TypedElement, ConnectableElement, Element):

    pass
class UML2WithID_ChangeTrigger(Element, Trigger):

    pass
class UML2WithID_InteractionFragment(NamedElement, Element):

    pass
class UML2WithID_Transition(Element, RedefinableElement):

    pass
class UML2WithID_CallOperationAction(CallAction, Element):

    pass
class UML2WithID_Actor(Element, Classifier):

    pass
class UML2WithID_LiteralSpecification(ValueSpecification, Element):

    pass
class UML2WithID_Association(Element, Classifier):

    pass
class UML2WithID_DecisionNode(ControlNode, Element):

    pass
class UML2WithID_Property(StructuralFeature, DeploymentTarget, ConnectableElement, Element):

    pass
class UML2WithID_BehavioralFeature(Namespace, Feature, Element):

    pass
class UML2WithID_StructuredClassifier(Element, Classifier):

    pass
class UML2WithID_InteractionOccurrence(Element, InteractionFragment):

    pass
class UML2WithID_CreateLinkAction(WriteLinkAction, Element):

    pass
class UML2WithID_Connector(Feature, Element):

    pass
class UML2WithID_AnyTrigger(Element, MessageTrigger):

    pass
class UML2WithID_Constraint(PackageableElement, Element):

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

class UML2WithID_Include(NamedElement, Element):

    pass
class UML2WithID_Node(Class, DeploymentTarget, Element):

    pass
class UML2WithID_CreateObjectAction(Element, Action):

    pass
class UML2WithID_UseCase(BehavioredClassifier, Element):

    pass
class UML2WithID_State(Namespace, Vertex, Element, RedefinableElement):

    pass
class UML2WithID_Realization(Abstraction, Element):

    pass
class UML2WithID_Implementation(Realization, Element):

    pass
class UML2WithID_ControlFlow(ActivityEdge, Element):

    pass
class UML2WithID_SendObjectAction(Element, InvocationAction):

    pass
class UML2WithID_ValueSpecification(TypedElement, Element):

    pass
class UML2WithID_DataStoreNode(CentralBufferNode, Element):

    pass
class UML2WithID_DataType(Element, Classifier):

    pass
class UML2WithID_Activity(Element, Behavior):

    pass
class UML2WithID_LiteralString(LiteralSpecification, Element):

    pass
class UML2WithID_Extension(Association, Element):

    pass
class UML2WithID_ReadStructuralFeatureAction(Element, StructuralFeatureAction):

    pass
class UML2WithID_Port(Element, Property):

    pass
class UML2WithID_Message(NamedElement, Element):

    pass
class UML2WithID_Stop(Element, EventOccurrence):

    pass
class UML2WithID_InstanceSpecification(DeploymentTarget, DeployedArtifact, PackageableElement, Element):

    pass
class UML2WithID_ConnectionPointReference(Vertex, Element):

    pass
class UML2WithID_StructuredActivityNode(Namespace, Element, Action):

    pass
class UML2WithID_DeploymentSpecification(Artifact, Element):

    pass
class UML2WithID_ReadSelfAction(Element, Action):

    pass
class UML2WithID_EnumerationLiteral(InstanceSpecification, Element):

    pass
class UML2WithID_VariableAction(Element, Action):

    pass
class UML2WithID_InputPin(Pin, Element):

    pass
class UML2WithID_Namespace(NamedElement, Element):

    pass
class UML2WithID_Pin(ObjectNode, Element):

    pass
class UML2WithID_Gate(MessageEnd, Element):

    pass
class UML2WithID_FinalState(Element, State):

    pass
class UML2WithID_Pseudostate(Vertex, Element):

    pass
class UML2WithID_Feature(Element, RedefinableElement):

    pass
class UML2WithID_IntervalConstraint(Constraint, Element):

    pass
class UML2WithID_Signal(Element, Classifier):

    pass
class UML2WithID_ForkNode(ControlNode, Element):

    pass
class UML2WithID_AcceptEventAction(Element, Action):

    pass
class UML2WithID_TimeInterval(Interval, Element):

    pass
class UML2WithID_LiteralUnlimitedNatural(LiteralSpecification, Element):

    pass
class UML2WithID_ExecutionEnvironment(Element, Node):

    pass
class UML2WithID_DestroyObjectAction(Element, Action):

    pass
class UML2WithID_TemplateableClassifier(Element, Classifier):

    pass
class UML2WithID_Duration(ValueSpecification, Element):

    pass
class UML2WithID_ReadLinkObjectEndQualifierAction(Element, Action):

    pass
class UML2WithID_Usage(Element, Dependency):

    pass
class UML2WithID_Action(ExecutableNode, Element):

    pass
class UML2WithID_StructuralFeatureAction(Element, Action):

    pass
class UML2WithID_TestIdentityAction(Element, Action):

    pass
class UML2WithID_ExecutionOccurrence(Element, InteractionFragment):

    pass
class UML2WithID_ObjectFlow(ActivityEdge, Element):

    pass
class UML2WithID_Manifestation(Abstraction, Element):

    pass
class UML2WithID_CallBehaviorAction(CallAction, Element):

    pass
class UML2WithID_LiteralNull(LiteralSpecification, Element):

    pass
class UML2WithID_RemoveVariableValueAction(WriteVariableAction, Element):

    pass
class UML2WithID_Interaction(InteractionFragment, Element, Behavior):

    pass
class UML2WithID_EventOccurrence(Element, MessageEnd, InteractionFragment):

    pass
class UML2WithID_InteractionConstraint(Constraint, Element):

    pass
class UML2WithID_Substitution(Realization, Element):

    pass
class UML2WithID_WriteStructuralFeatureAction(Element, StructuralFeatureAction):

    pass
class UML2WithID_Permission(Dependency, Element):

    pass
class UML2WithID_Package(Namespace, PackageableElement, Element):

    pass
class UML2WithID_TimeConstraint(IntervalConstraint, Element):

    pass
class UML2WithID_Variable(TypedElement, ConnectableElement, Element):

    pass
class UML2WithID_AddVariableValueAction(WriteVariableAction, Element):

    pass
class UML2WithID_ProtocolTransition(Element, Transition):

    pass
class UML2WithID_ClearStructuralFeatureAction(Element, StructuralFeatureAction):

    pass
class UML2WithID_EncapsulatedClassifier(Element, StructuredClassifier):

    pass
class UML2WithID_ValuePin(InputPin, Element):

    pass
class UML2WithID_ApplyFunctionAction(Element, Action):

    pass
class UML2WithID_StateMachine(Element, Behavior):

    pass
class UML2WithID_Profile(Package, Element):

    pass
class UML2WithID_CallTrigger(Element, MessageTrigger):

    pass
class UML2WithID_CallAction(Element, InvocationAction):

    pass
class UML2WithID_InteractionOperand(Namespace, Element, InteractionFragment):

    pass
class UML2WithID_Behavior(Element, Class):

    pass
class UML2WithID_ActivityPartition(NamedElement, Element):

    pass
class UML2WithID_ReadVariableAction(Element, VariableAction):

    pass
class UML2WithID_WriteLinkAction(LinkAction, Element):

    pass
class UML2WithID_PartDecomposition(Element, InteractionOccurrence):

    pass
class UML2WithID_ExecutableNode(ActivityNode, Element):

    pass
class UML2WithID_InvocationAction(Element, Action):

    pass
class UML2WithID_ActivityParameterNode(ObjectNode, Element):

    pass
class UML2WithID_ReplyAction(Element, Action):

    pass
class UML2WithID_Classifier(Namespace, Type, Element, RedefinableElement):

    pass
class UML2WithID_MessageEnd(NamedElement, Element):

    pass
class UML2WithID_OutputPin(Pin, Element):

    pass
class UML2WithID_DurationInterval(Interval, Element):

    pass
class UML2WithID_AcceptCallAction(AcceptEventAction, Element):

    pass
class UML2WithID_ExtensionEnd(Element, Property):

    pass
class UML2WithID_PackageableElement(NamedElement, Element):

    pass
class UML2WithID_ActivityFinalNode(FinalNode, Element):

    pass
class UML2WithID_BroadcastSignalAction(Element, InvocationAction):

    pass
class UML2WithID_StartOwnedBehaviorAction(Element, Action):

    pass
class UML2WithID_DestroyLinkAction(WriteLinkAction, Element):

    pass
class UML2WithID_Dependency(PackageableElement, Element):

    pass
class UML2WithID_ReclassifyObjectAction(Element, Action):

    pass
class UML2WithID_TypedElement(NamedElement, Element):

    pass
class UML2WithID_InitialNode(ControlNode, Element):

    pass
class UML2WithID_Lifeline(NamedElement, Element):

    pass
class UML2WithID_ExpansionRegion(StructuredActivityNode, Element):

    pass
class UML2WithID_Collaboration(BehavioredClassifier, Element, StructuredClassifier):

    pass
class UML2WithID_Artifact(DeployedArtifact, Element, Classifier):

    pass
class UML2WithID_ConnectableElement(NamedElement, Element):

    pass
class UML2WithID_CombinedFragment(Element, InteractionFragment):

    pass
class UML2WithID_Reception(Element, BehavioralFeature):

    pass
class UML2WithID_LiteralInteger(LiteralSpecification, Element):

    pass
class UML2WithID_ActivityEdge(Element, RedefinableElement):

    pass
class UML2WithID_RaiseExceptionAction(Element, Action):

    pass
class UML2WithID_InformationFlow(PackageableElement, Element):

    pass
class UML2WithID_Interval(ValueSpecification, Element):

    pass
class UML2WithID_DeploymentTarget(NamedElement, Element):

    pass
class UML2WithID_RedefinableTemplateSignature(Element, RedefinableElement):

    pass
class UML2WithID_PrimitiveFunction(PackageableElement, Element):

    pass
class UML2WithID_Device(Element, Node):

    pass
class UML2WithID_Class(BehavioredClassifier, EncapsulatedClassifier, Element):

    pass
class UML2WithID_ExpansionNode(ObjectNode, Element):

    pass
class UML2WithID_SignalTrigger(Element, MessageTrigger):

    pass
class UML2WithID_SendSignalAction(Element, InvocationAction):

    pass
class UML2WithID_MessageTrigger(Element, Trigger):

    pass
class UML2WithID_Vertex(NamedElement, Element):

    pass
class UML2WithID_DurationConstraint(IntervalConstraint, Element):

    pass
class UML2WithID_TimeTrigger(Element, Trigger):

    pass
class UML2WithID_GeneralizationSet(PackageableElement, Element):

    pass
class UML2WithID_ProtocolStateMachine(Element, StateMachine):

    pass
class UML2WithID_Operation(TypedElement, Element, BehavioralFeature):

    pass
class UML2WithID_InstanceValue(ValueSpecification, Element):

    pass
class UML2WithID_CommunicationPath(Association, Element):

    pass
class UML2WithID_MergeNode(ControlNode, Element):

    pass
class UML2WithID_ReadLinkAction(LinkAction, Element):

    pass
class UML2WithID_LoopNode(StructuredActivityNode, Element):

    pass
class UML2WithID_ReadIsClassifiedObjectAction(Element, Action):

    pass
class UML2WithID_DeployedArtifact(NamedElement, Element):

    pass
class UML2WithID_Expression(Element, OpaqueExpression):

    pass
class UML2WithID_ClearVariableAction(Element, VariableAction):

    pass
class UML2WithID_RedefinableElement(NamedElement, Element):

    pass
class UML2WithID_Stereotype(Class, Element):

    pass
class UML2WithID_Component(Element, Class):

    pass
class UML2WithID_JoinNode(ControlNode, Element):

    pass
class UML2WithID_AssociationClass(Class, Association, Element):

    pass
class UML2WithID_ReadExtentAction(Element, Action):

    pass
class UML2WithID_ConditionalNode(StructuredActivityNode, Element):

    pass
class UML2WithID_Deployment(Element, Dependency):

    pass
class UML2WithID_ActivityNode(Element, RedefinableElement):

    pass
class UML2WithID_Enumeration(Element, DataType):

    pass
class UML2WithID_Type(PackageableElement, Element):

    pass
class UML2WithID_ObjectNode(TypedElement, ActivityNode, Element):

    pass
class UML2WithID_InformationItem(Element, Classifier):

    pass
class UML2WithID_BehavioredClassifier(Element, Classifier):

    pass
class UML2WithID_ControlNode(ActivityNode, Element):

    pass
class UML2WithID_LinkAction(Element, Action):

    pass
class UML2WithID_StateInvariant(Element, InteractionFragment):

    pass
class UML2WithID_CentralBufferNode(ObjectNode, Element):

    pass
class UML2WithID_Abstraction(Dependency, Element):

    pass
class UML2WithID_GeneralOrdering(NamedElement, Element):

    pass
class UML2WithID_OpaqueExpression(ValueSpecification, Element):

    pass
class UML2WithID_FlowFinalNode(FinalNode, Element):

    pass
class UML2WithID_TimeExpression(ValueSpecification, Element):

    pass
class UML2WithID_Extend(NamedElement, Element):

    pass
class UML2WithID_Region(Namespace, Element, RedefinableElement):

    pass
class UML2WithID_Interface(Element, Classifier):

    pass
class UML2WithID_ParameterSet(NamedElement, Element):

    pass
class UML2WithID_PrimitiveType(Element, DataType):

    pass
class UML2WithID_Continuation(Element, InteractionFragment):

    pass
class UML2WithID_Trigger(NamedElement, Element):

    pass
class UML2WithID_FinalNode(ControlNode, Element):

    pass
class WriteStructuralFeatureAction:

    pass
class UML2WithID_TimeObservationAction(WriteStructuralFeatureAction, Element):

    pass
class UML2WithID_AddStructuralFeatureValueAction(WriteStructuralFeatureAction, Element):

    pass
class UML2WithID_RemoveStructuralFeatureValueAction(WriteStructuralFeatureAction, Element):

    pass
class UML2WithID_DurationObservationAction(WriteStructuralFeatureAction, Element):

    pass