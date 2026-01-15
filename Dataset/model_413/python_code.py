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
class CreateLinkAction:

    pass
class IntervalConstraint:

    pass
class CentralBufferNode:

    pass
class AcceptEventAction:

    pass
class StructuredClassifier:

    pass
class InteractionOccurrence:

    pass
class Type:

    pass
class WriteStructuralFeatureAction:

    pass
class Realization:

    pass
class StructuralFeature:

    pass
class LinkAction:

    pass
class Pin:

    pass
class Feature:

    pass
class Artifact:

    pass
class StateMachine:

    pass
class MessageEnd:

    pass
class DeploymentTarget:

    pass
class Package:

    pass
class Constraint:

    pass
class ExecutableNode:

    pass
class Trigger:

    pass
class InstanceSpecification:

    pass
class VariableAction:

    pass
class Node:

    pass
class EncapsulatedClassifier:

    pass
class BehavioredClassifier:

    pass
class ControlNode:

    pass
class ObjectNode:

    pass
class DataType:

    pass
class Behavior:

    pass
class StructuralFeatureAction:

    pass
class CallAction:

    pass
class OpaqueExpression:

    pass
class DeployedArtifact:

    pass
class FinalNode:

    pass
class ConnectableElement:

    pass
class StructuredActivityNode:

    pass
class WriteLinkAction:

    pass
class Property:

    pass
class Abstraction:

    pass
class Transition:

    pass
class BehavioralFeature:

    pass
class Vertex:

    pass
class PackageableElement:

    pass
class ValueSpecification:

    pass
class Association:

    pass
class Interval:

    pass
class Element:

    pass
class UML2WithID_Extension(Element, Association):

    pass
class UML2WithID_Activity(Element, Behavior):

    pass
class UML2WithID_TimeExpression(Element, ValueSpecification):

    pass
class UML2WithID_CentralBufferNode(Element, ObjectNode):

    pass
class UML2WithID_Stop(EventOccurrence, Element):

    pass
class UML2WithID_CreateLinkObjectAction(Element, CreateLinkAction):

    pass
class UML2WithID_Connector(Feature, Element):

    pass
class UML2WithID_JoinNode(Element, ControlNode):

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

class UML2WithID_WriteStructuralFeatureAction(StructuralFeatureAction, Element):

    pass
class UML2WithID_EnumerationLiteral(Element, InstanceSpecification):

    pass
class UML2WithID_ProtocolTransition(Element, Transition):

    pass
class UML2WithID_MessageTrigger(Trigger, Element):

    pass
class UML2WithID_MergeNode(Element, ControlNode):

    pass
class UML2WithID_Property(DeploymentTarget, Element, StructuralFeature, ConnectableElement):

    pass
class UML2WithID_ClearStructuralFeatureAction(StructuralFeatureAction, Element):

    pass
class UML2WithID_LiteralSpecification(Element, ValueSpecification):

    pass
class UML2WithID_OutputPin(Element, Pin):

    pass
class UML2WithID_StateMachine(Element, Behavior):

    pass
class UML2WithID_Collaboration(BehavioredClassifier, Element, StructuredClassifier):

    pass
class UML2WithID_DecisionNode(Element, ControlNode):

    pass
class UML2WithID_Manifestation(Element, Abstraction):

    pass
class UML2WithID_ReadLinkAction(Element, LinkAction):

    pass
class UML2WithID_ExpansionNode(Element, ObjectNode):

    pass
class UML2WithID_IntervalConstraint(Element, Constraint):

    pass
class UML2WithID_Reception(Element, BehavioralFeature):

    pass
class UML2WithID_InstanceValue(Element, ValueSpecification):

    pass
class UML2WithID_ForkNode(Element, ControlNode):

    pass
class UML2WithID_ExecutionEnvironment(Element, Node):

    pass
class UML2WithID_Action(Element, ExecutableNode):

    pass
class UML2WithID_PartDecomposition(Element, InteractionOccurrence):

    pass
class UML2WithID_InteractionConstraint(Element, Constraint):

    pass
class UML2WithID_Implementation(Element, Realization):

    pass
class UML2WithID_ActivityFinalNode(Element, FinalNode):

    pass
class UML2WithID_Interval(Element, ValueSpecification):

    pass
class UML2WithID_CreateLinkAction(Element, WriteLinkAction):

    pass
class UML2WithID_CallBehaviorAction(Element, CallAction):

    pass
class UML2WithID_AddStructuralFeatureValueAction(Element, WriteStructuralFeatureAction):

    pass
class UML2WithID_ExtensionEnd(Element, Property):

    pass
class UML2WithID_InputPin(Element, Pin):

    pass
class UML2WithID_CallOperationAction(Element, CallAction):

    pass
class UML2WithID_Substitution(Element, Realization):

    pass
class UML2WithID_LoopNode(Element, StructuredActivityNode):

    pass
class UML2WithID_DurationConstraint(Element, IntervalConstraint):

    pass
class UML2WithID_ReadVariableAction(Element, VariableAction):

    pass
class UML2WithID_Model(Element, Package):

    pass
class UML2WithID_ChangeTrigger(Trigger, Element):

    pass
class UML2WithID_DeploymentSpecification(Element, Artifact):

    pass
class UML2WithID_UseCase(BehavioredClassifier, Element):

    pass
class UML2WithID_Type(Element, PackageableElement):

    pass
class UML2WithID_Dependency(Element, PackageableElement):

    pass
class UML2WithID_GeneralizationSet(Element, PackageableElement):

    pass
class UML2WithID_DataStoreNode(Element, CentralBufferNode):

    pass
class UML2WithID_ClearVariableAction(VariableAction, Element):

    pass
class UML2WithID_FinalNode(Element, ControlNode):

    pass
class UML2WithID_ExpansionRegion(Element, StructuredActivityNode):

    pass
class UML2WithID_Pseudostate(Element, Vertex):

    pass
class UML2WithID_Port(Element, Property):

    pass
class UML2WithID_PrimitiveType(DataType, Element):

    pass
class UML2WithID_Enumeration(DataType, Element):

    pass
class UML2WithID_InitialNode(Element, ControlNode):

    pass
class UML2WithID_Gate(Element, MessageEnd):

    pass
class UML2WithID_Constraint(Element, PackageableElement):

    pass
class UML2WithID_Class(BehavioredClassifier, Element, EncapsulatedClassifier):

    pass
class UML2WithID_DurationInterval(Interval, Element):

    pass
class UML2WithID_ProtocolStateMachine(Element, StateMachine):

    pass
class UML2WithID_Device(Element, Node):

    pass
class UML2WithID_Profile(Element, Package):

    pass
class UML2WithID_ReadStructuralFeatureAction(StructuralFeatureAction, Element):

    pass
class UML2WithID_DurationObservationAction(Element, WriteStructuralFeatureAction):

    pass
class UML2WithID_InstanceSpecification(DeploymentTarget, Element, DeployedArtifact, PackageableElement):

    pass
class UML2WithID_Realization(Element, Abstraction):

    pass
class UML2WithID_WriteLinkAction(Element, LinkAction):

    pass
class UML2WithID_TimeTrigger(Trigger, Element):

    pass
class UML2WithID_InformationFlow(Element, PackageableElement):

    pass
class UML2WithID_ActivityParameterNode(ObjectNode, Element):

    pass
class UML2WithID_Expression(Element, OpaqueExpression):

    pass
class UML2WithID_FlowFinalNode(Element, FinalNode):

    pass
class UML2WithID_EncapsulatedClassifier(Element, StructuredClassifier):

    pass
class UML2WithID_RemoveStructuralFeatureValueAction(Element, WriteStructuralFeatureAction):

    pass
class UML2WithID_DestroyLinkAction(Element, WriteLinkAction):

    pass
class UML2WithID_CommunicationPath(Element, Association):

    pass
class UML2WithID_AcceptCallAction(Element, AcceptEventAction):

    pass
class UML2WithID_TimeConstraint(Element, IntervalConstraint):

    pass
class UML2WithID_ConditionalNode(Element, StructuredActivityNode):

    pass
class UML2WithID_WriteVariableAction(Element, VariableAction):

    pass
class UML2WithID_Pin(Element, ObjectNode):

    pass
class UML2WithID_TimeObservationAction(Element, WriteStructuralFeatureAction):

    pass
class UML2WithID_PrimitiveFunction(Element, PackageableElement):

    pass
class UML2WithID_TimeInterval(Interval, Element):

    pass
class TypedElement:

    pass
class UML2WithID_Variable(Element, TypedElement, ConnectableElement):

    pass
class UML2WithID_Operation(Element, BehavioralFeature, TypedElement):

    pass
class UML2WithID_ValueSpecification(Element, TypedElement):

    pass
class UML2WithID_Parameter(Element, TypedElement, ConnectableElement):

    pass
class UML2WithID_StructuralFeature(Feature, Element, TypedElement):

    pass
class ActivityNode:

    pass
class UML2WithID_ExecutableNode(Element, ActivityNode):

    pass
class UML2WithID_ControlNode(Element, ActivityNode):

    pass
class UML2WithID_ObjectNode(Element, TypedElement, ActivityNode):

    pass
class RedefinableElement:

    pass
class UML2WithID_Feature(Element, RedefinableElement):

    pass
class UML2WithID_RedefinableTemplateSignature(Element, RedefinableElement):

    pass
class UML2WithID_ActivityEdge(Element, RedefinableElement):

    pass
class UML2WithID_Transition(Element, RedefinableElement):

    pass
class UML2WithID_ExtensionPoint(Element, RedefinableElement):

    pass
class UML2WithID_ActivityNode(Element, RedefinableElement):

    pass
class UML2WithID_Duration(Element, ValueSpecification):

    pass
class ActivityEdge:

    pass
class UML2WithID_ObjectFlow(Element, ActivityEdge):

    pass
class UML2WithID_ControlFlow(Element, ActivityEdge):

    pass
class Class:

    pass
class UML2WithID_AssociationClass(Element, Class, Association):

    pass
class UML2WithID_Node(DeploymentTarget, Element, Class):

    pass
class UML2WithID_Stereotype(Element, Class):

    pass
class UML2WithID_Component(Element, Class):

    pass
class UML2WithID_Behavior(Element, Class):

    pass
class InputPin:

    pass
class UML2WithID_ValuePin(Element, InputPin):

    pass
class NamedElement:

    pass
class UML2WithID_Namespace(NamedElement, Element):

    pass
class UML2WithID_ConnectableElement(NamedElement, Element):

    pass
class UML2WithID_Trigger(NamedElement, Element):

    pass
class UML2WithID_Extend(NamedElement, Element):

    pass
class UML2WithID_ParameterSet(NamedElement, Element):

    pass
class UML2WithID_DeployedArtifact(Element, NamedElement):

    pass
class UML2WithID_GeneralOrdering(NamedElement, Element):

    pass
class UML2WithID_CollaborationOccurrence(NamedElement, Element):

    pass
class UML2WithID_MessageEnd(Element, NamedElement):

    pass
class UML2WithID_Vertex(Element, NamedElement):

    pass
class UML2WithID_Message(NamedElement, Element):

    pass
class UML2WithID_DeploymentTarget(NamedElement, Element):

    pass
class UML2WithID_InteractionFragment(Element, NamedElement):

    pass
class UML2WithID_ActivityPartition(Element, NamedElement):

    pass
class UML2WithID_TypedElement(Element, NamedElement):

    pass
class UML2WithID_Include(Element, NamedElement):

    pass
class UML2WithID_PackageableElement(NamedElement, Element):

    pass
class UML2WithID_Lifeline(NamedElement, Element):

    pass
class UML2WithID_RedefinableElement(Element, NamedElement):

    pass
class Dependency:

    pass
class UML2WithID_Usage(Dependency, Element):

    pass
class UML2WithID_Deployment(Dependency, Element):

    pass
class UML2WithID_Abstraction(Element, Dependency):

    pass
class UML2WithID_Permission(Element, Dependency):

    pass
class InvocationAction:

    pass
class UML2WithID_SendObjectAction(Element, InvocationAction):

    pass
class UML2WithID_SendSignalAction(Element, InvocationAction):

    pass
class UML2WithID_BroadcastSignalAction(Element, InvocationAction):

    pass
class UML2WithID_CallAction(Element, InvocationAction):

    pass
class LiteralSpecification:

    pass
class UML2WithID_LiteralNull(LiteralSpecification, Element):

    pass
class UML2WithID_LiteralString(LiteralSpecification, Element):

    pass
class UML2WithID_LiteralUnlimitedNatural(LiteralSpecification, Element):

    pass
class UML2WithID_LiteralInteger(LiteralSpecification, Element):

    pass
class UML2WithID_LiteralBoolean(LiteralSpecification, Element):

    pass
class State:

    pass
class UML2WithID_FinalState(Element, State):

    pass
class UML2WithID_OpaqueExpression(Element, ValueSpecification):

    pass
class UML2WithID_ConnectionPointReference(Element, Vertex):

    pass
class Classifier:

    pass
class UML2WithID_InformationItem(Element, Classifier):

    pass
class UML2WithID_Artifact(DeployedArtifact, Classifier, Element):

    pass
class UML2WithID_Actor(Element, Classifier):

    pass
class UML2WithID_ParameterableClassifier(Element, Classifier):

    pass
class UML2WithID_DataType(Element, Classifier):

    pass
class UML2WithID_BehavioredClassifier(Element, Classifier):

    pass
class UML2WithID_StructuredClassifier(Element, Classifier):

    pass
class UML2WithID_TemplateableClassifier(Element, Classifier):

    pass
class UML2WithID_Signal(Element, Classifier):

    pass
class UML2WithID_Interface(Element, Classifier):

    pass
class UML2WithID_Association(Element, Classifier):

    pass
class WriteVariableAction:

    pass
class UML2WithID_AddVariableValueAction(Element, WriteVariableAction):

    pass
class UML2WithID_RemoveVariableValueAction(Element, WriteVariableAction):

    pass
class MessageTrigger:

    pass
class UML2WithID_CallTrigger(Element, MessageTrigger):

    pass
class UML2WithID_AnyTrigger(Element, MessageTrigger):

    pass
class UML2WithID_SignalTrigger(Element, MessageTrigger):

    pass
class InteractionFragment:

    pass
class UML2WithID_CombinedFragment(Element, InteractionFragment):

    pass
class UML2WithID_EventOccurrence(Element, MessageEnd, InteractionFragment):

    pass
class UML2WithID_StateInvariant(Element, InteractionFragment):

    pass
class UML2WithID_Continuation(Element, InteractionFragment):

    pass
class UML2WithID_InteractionOccurrence(Element, InteractionFragment):

    pass
class UML2WithID_Interaction(Element, Behavior, InteractionFragment):

    pass
class UML2WithID_ExecutionOccurrence(Element, InteractionFragment):

    pass
class Namespace:

    pass
class UML2WithID_State(Element, Vertex, RedefinableElement, Namespace):

    pass
class UML2WithID_Region(Element, RedefinableElement, Namespace):

    pass
class UML2WithID_BehavioralFeature(Feature, Element, Namespace):

    pass
class UML2WithID_Package(Element, PackageableElement, Namespace):

    pass
class UML2WithID_Classifier(Element, Type, RedefinableElement, Namespace):

    pass
class UML2WithID_InteractionOperand(Element, Namespace, InteractionFragment):

    pass
class Action:

    pass
class UML2WithID_ReadSelfAction(Action, Element):

    pass
class UML2WithID_StructuralFeatureAction(Action, Element):

    pass
class UML2WithID_ReplyAction(Action, Element):

    pass
class UML2WithID_CreateObjectAction(Action, Element):

    pass
class UML2WithID_ApplyFunctionAction(Action, Element):

    pass
class UML2WithID_ReclassifyObjectAction(Action, Element):

    pass
class UML2WithID_InvocationAction(Action, Element):

    pass
class UML2WithID_ReadLinkObjectEndAction(Action, Element):

    pass
class UML2WithID_AcceptEventAction(Action, Element):

    pass
class UML2WithID_ClearAssociationAction(Action, Element):

    pass
class UML2WithID_TestIdentityAction(Action, Element):

    pass
class UML2WithID_DestroyObjectAction(Action, Element):

    pass
class UML2WithID_RaiseExceptionAction(Action, Element):

    pass
class UML2WithID_ReadLinkObjectEndQualifierAction(Action, Element):

    pass
class UML2WithID_ReadIsClassifiedObjectAction(Action, Element):

    pass
class UML2WithID_StructuredActivityNode(Action, Element, Namespace):

    pass
class UML2WithID_StartOwnedBehaviorAction(Action, Element):

    pass
class UML2WithID_ReadExtentAction(Action, Element):

    pass
class UML2WithID_LinkAction(Action, Element):

    pass
class UML2WithID_VariableAction(Action, Element):

    pass