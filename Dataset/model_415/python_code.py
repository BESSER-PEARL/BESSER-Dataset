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
class Pin:

    pass
class DataType:

    pass
class StateMachine:

    pass
class EncapsulatedClassifier:

    pass
class Artifact:

    pass
class CallAction:

    pass
class Constraint:

    pass
class StructuredActivityNode:

    pass
class AcceptEventAction:

    pass
class FinalNode:

    pass
class WriteLinkAction:

    pass
class ActivityEdge:

    pass
class Realization:

    pass
class WriteStructuralFeatureAction:

    pass
class LinkAction:

    pass
class Abstraction:

    pass
class InputPin:

    pass
class Behavior:

    pass
class StructuralFeatureAction:

    pass
class ValueSpecification:

    pass
class ExecutableNode:

    pass
class OpaqueExpression:

    pass
class CreateLinkAction:

    pass
class InstanceSpecification:

    pass
class StructuredClassifier:

    pass
class InteractionFragment:

    pass
class BehavioredClassifier:

    pass
class IntervalConstraint:

    pass
class State:

    pass
class ConnectableElement:

    pass
class StructuralFeature:

    pass
class InvocationAction:

    pass
class ActivityNode:

    pass
class MessageTrigger:

    pass
class Property:

    pass
class LiteralSpecification:

    pass
class Dependency:

    pass
class MessageEnd:

    pass
class Type:

    pass
class Association:

    pass
class Node:

    pass
class Package:

    pass
class NamedElement:

    pass
class TypedElement:

    pass
class Feature:

    pass
class BehavioralFeature:

    pass
class CentralBufferNode:

    pass
class Class:

    pass
class Vertex:

    pass
class RedefinableElement:

    pass
class Namespace:

    pass
class DeployedArtifact:

    pass
class DeploymentTarget:

    pass
class PackageableElement:

    pass
class InteractionOccurrence:

    pass
class Transition:

    pass
class WriteVariableAction:

    pass
class Action:

    pass
class Trigger:

    pass
class VariableAction:

    pass
class Interval:

    pass
class Classifier:

    pass
class ObjectNode:

    pass
class Element:

    pass
class UML2WithID_Permission(Element, Dependency):

    pass
class UML2WithID_PrimitiveType(DataType, Element):

    pass
class UML2WithID_Package(Namespace, Element, PackageableElement):

    pass
class UML2WithID_Implementation(Element, Realization):

    pass
class UML2WithID_ExtensionPoint(RedefinableElement, Element):

    pass
class UML2WithID_MessageTrigger(Element, Trigger):

    pass
class UML2WithID_TimeExpression(Element, ValueSpecification):

    pass
class UML2WithID_ExtensionEnd(Element, Property):

    pass
class UML2WithID_Pseudostate(Vertex, Element):

    pass
class UML2WithID_ProtocolTransition(Transition, Element):

    pass
class UML2WithID_Interaction(InteractionFragment, Element, Behavior):

    pass
class UML2WithID_LiteralString(Element, LiteralSpecification):

    pass
class UML2WithID_ReclassifyObjectAction(Action, Element):

    pass
class UML2WithID_Realization(Element, Abstraction):

    pass
class UML2WithID_PartDecomposition(InteractionOccurrence, Element):

    pass
class UML2WithID_Behavior(Element, Class):

    pass
class UML2WithID_Node(Class, Element, DeploymentTarget):

    pass
class UML2WithID_CallAction(Element, InvocationAction):

    pass
class UML2WithID_Signal(Classifier, Element):

    pass
class UML2WithID_Transition(RedefinableElement, Element):

    pass
class UML2WithID_StructuredClassifier(Classifier, Element):

    pass
class UML2WithID_ChangeTrigger(Element, Trigger):

    pass
class UML2WithID_CallBehaviorAction(Element, CallAction):

    pass
class UML2WithID_Constraint(PackageableElement, Element):

    pass
class UML2WithID_CallTrigger(MessageTrigger, Element):

    pass
class UML2WithID_StructuralFeature(Element, Feature, TypedElement):

    pass
class UML2WithID_DeploymentSpecification(Artifact, Element):

    pass
class UML2WithID_StateInvariant(Element, InteractionFragment):

    pass
class UML2WithID_TypedElement(Element, NamedElement):

    pass
class UML2WithID_LoopNode(StructuredActivityNode, Element):

    pass
class UML2WithID_Port(Element, Property):

    pass
class UML2WithID_Lifeline(Element, NamedElement):

    pass
class UML2WithID_DeployedArtifact(Element, NamedElement):

    pass
class UML2WithID_ApplyFunctionAction(Action, Element):

    pass
class UML2WithID_OutputPin(Element, Pin):

    pass
class UML2WithID_Connector(Element, Feature):

    pass
class UML2WithID_ClearVariableAction(Element, VariableAction):

    pass
class UML2WithID_InteractionFragment(Element, NamedElement):

    pass
class UML2WithID_CreateLinkAction(WriteLinkAction, Element):

    pass
class UML2WithID_CreateObjectAction(Action, Element):

    pass
class UML2WithID_Operation(Element, BehavioralFeature, TypedElement):

    pass
class UML2WithID_ReadIsClassifiedObjectAction(Action, Element):

    pass
class UML2WithID_ConnectionPointReference(Vertex, Element):

    pass
class UML2WithID_TimeInterval(Element, Interval):

    pass
class UML2WithID_PackageableElement(Element, NamedElement):

    pass
class UML2WithID_LiteralNull(Element, LiteralSpecification):

    pass
class UML2WithID_DurationInterval(Element, Interval):

    pass
class UML2WithID_InstanceValue(Element, ValueSpecification):

    pass
class UML2WithID_Duration(Element, ValueSpecification):

    pass
class UML2WithID_Actor(Classifier, Element):

    pass
class UML2WithID_LiteralBoolean(Element, LiteralSpecification):

    pass
class UML2WithID_ReadLinkObjectEndQualifierAction(Action, Element):

    pass
class UML2WithID_RemoveStructuralFeatureValueAction(Element, WriteStructuralFeatureAction):

    pass
class UML2WithID_ActivityParameterNode(Element, ObjectNode):

    pass
class UML2WithID_ActivityFinalNode(Element, FinalNode):

    pass
class UML2WithID_TimeObservationAction(Element, WriteStructuralFeatureAction):

    pass
class UML2WithID_PrimitiveFunction(PackageableElement, Element):

    pass
class UML2WithID_EncapsulatedClassifier(Element, StructuredClassifier):

    pass
class UML2WithID_RaiseExceptionAction(Action, Element):

    pass
class UML2WithID_AcceptCallAction(AcceptEventAction, Element):

    pass
class UML2WithID_RedefinableElement(Element, NamedElement):

    pass
class UML2WithID_EnumerationLiteral(Element, InstanceSpecification):

    pass
class UML2WithID_Device(Element, Node):

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

class UML2WithID_Namespace(Element, NamedElement):

    pass
class UML2WithID_StructuralFeatureAction(Action, Element):

    pass
class UML2WithID_ReadLinkAction(LinkAction, Element):

    pass
class UML2WithID_ObjectFlow(ActivityEdge, Element):

    pass
class UML2WithID_Component(Element, Class):

    pass
class UML2WithID_GeneralizationSet(PackageableElement, Element):

    pass
class UML2WithID_Vertex(Element, NamedElement):

    pass
class UML2WithID_LiteralUnlimitedNatural(Element, LiteralSpecification):

    pass
class UML2WithID_State(RedefinableElement, Namespace, Element, Vertex):

    pass
class UML2WithID_TemplateableClassifier(Classifier, Element):

    pass
class UML2WithID_AddVariableValueAction(Element, WriteVariableAction):

    pass
class UML2WithID_InteractionOperand(Namespace, Element, InteractionFragment):

    pass
class UML2WithID_Extend(Element, NamedElement):

    pass
class UML2WithID_Reception(Element, BehavioralFeature):

    pass
class UML2WithID_ValueSpecification(Element, TypedElement):

    pass
class UML2WithID_Variable(Element, ConnectableElement, TypedElement):

    pass
class UML2WithID_ProtocolStateMachine(Element, StateMachine):

    pass
class UML2WithID_InstanceSpecification(DeployedArtifact, PackageableElement, Element, DeploymentTarget):

    pass
class UML2WithID_CreateLinkObjectAction(CreateLinkAction, Element):

    pass
class UML2WithID_Dependency(PackageableElement, Element):

    pass
class UML2WithID_CallOperationAction(Element, CallAction):

    pass
class UML2WithID_ReadLinkObjectEndAction(Action, Element):

    pass
class UML2WithID_Action(ExecutableNode, Element):

    pass
class UML2WithID_ParameterableClassifier(Classifier, Element):

    pass
class UML2WithID_GeneralOrdering(Element, NamedElement):

    pass
class UML2WithID_ReadVariableAction(Element, VariableAction):

    pass
class UML2WithID_Artifact(DeployedArtifact, Classifier, Element):

    pass
class UML2WithID_Type(PackageableElement, Element):

    pass
class UML2WithID_StateMachine(Element, Behavior):

    pass
class UML2WithID_ReadSelfAction(Action, Element):

    pass
class UML2WithID_Continuation(Element, InteractionFragment):

    pass
class UML2WithID_CommunicationPath(Association, Element):

    pass
class UML2WithID_DurationObservationAction(Element, WriteStructuralFeatureAction):

    pass
class UML2WithID_Stop(Element, EventOccurrence):

    pass
class UML2WithID_Interval(Element, ValueSpecification):

    pass
class UML2WithID_ConditionalNode(StructuredActivityNode, Element):

    pass
class UML2WithID_DurationConstraint(IntervalConstraint, Element):

    pass
class UML2WithID_LiteralSpecification(Element, ValueSpecification):

    pass
class UML2WithID_ExecutionEnvironment(Element, Node):

    pass
class UML2WithID_Feature(RedefinableElement, Element):

    pass
class UML2WithID_MessageEnd(Element, NamedElement):

    pass
class UML2WithID_ExecutionOccurrence(Element, InteractionFragment):

    pass
class UML2WithID_WriteStructuralFeatureAction(StructuralFeatureAction, Element):

    pass
class UML2WithID_ControlNode(Element, ActivityNode):

    pass
class UML2WithID_Message(Element, NamedElement):

    pass
class UML2WithID_CollaborationOccurrence(Element, NamedElement):

    pass
class UML2WithID_InteractionConstraint(Constraint, Element):

    pass
class UML2WithID_DestroyObjectAction(Action, Element):

    pass
class UML2WithID_AcceptEventAction(Action, Element):

    pass
class UML2WithID_StructuredActivityNode(Namespace, Element, Action):

    pass
class UML2WithID_LinkAction(Action, Element):

    pass
class UML2WithID_OpaqueExpression(Element, ValueSpecification):

    pass
class UML2WithID_Substitution(Element, Realization):

    pass
class UML2WithID_ClearStructuralFeatureAction(StructuralFeatureAction, Element):

    pass
class UML2WithID_ExecutableNode(Element, ActivityNode):

    pass
class UML2WithID_Pin(Element, ObjectNode):

    pass
class UML2WithID_SignalTrigger(MessageTrigger, Element):

    pass
class UML2WithID_StartOwnedBehaviorAction(Action, Element):

    pass
class UML2WithID_AddStructuralFeatureValueAction(Element, WriteStructuralFeatureAction):

    pass
class UML2WithID_Extension(Association, Element):

    pass
class UML2WithID_SendObjectAction(Element, InvocationAction):

    pass
class UML2WithID_VariableAction(Action, Element):

    pass
class UML2WithID_Property(Element, ConnectableElement, StructuralFeature, DeploymentTarget):

    pass
class UML2WithID_IntervalConstraint(Constraint, Element):

    pass
class UML2WithID_CombinedFragment(Element, InteractionFragment):

    pass
class UML2WithID_Activity(Element, Behavior):

    pass
class UML2WithID_TimeConstraint(IntervalConstraint, Element):

    pass
class UML2WithID_UseCase(Element, BehavioredClassifier):

    pass
class UML2WithID_ActivityPartition(Element, NamedElement):

    pass
class UML2WithID_Abstraction(Element, Dependency):

    pass
class UML2WithID_Expression(Element, OpaqueExpression):

    pass
class UML2WithID_TimeTrigger(Element, Trigger):

    pass
class UML2WithID_ReplyAction(Action, Element):

    pass
class UML2WithID_ActivityEdge(RedefinableElement, Element):

    pass
class UML2WithID_ReadStructuralFeatureAction(StructuralFeatureAction, Element):

    pass
class UML2WithID_ControlFlow(ActivityEdge, Element):

    pass
class UML2WithID_Region(Namespace, Element, RedefinableElement):

    pass
class UML2WithID_InteractionOccurrence(Element, InteractionFragment):

    pass
class UML2WithID_LiteralInteger(Element, LiteralSpecification):

    pass
class UML2WithID_ParameterSet(Element, NamedElement):

    pass
class UML2WithID_ObjectNode(Element, ActivityNode, TypedElement):

    pass
class UML2WithID_ValuePin(InputPin, Element):

    pass
class UML2WithID_InformationFlow(PackageableElement, Element):

    pass
class UML2WithID_DataType(Classifier, Element):

    pass
class UML2WithID_WriteVariableAction(Element, VariableAction):

    pass
class UML2WithID_Usage(Element, Dependency):

    pass
class UML2WithID_ActivityNode(RedefinableElement, Element):

    pass
class UML2WithID_ExpansionNode(ObjectNode, Element):

    pass
class UML2WithID_Parameter(Element, ConnectableElement, TypedElement):

    pass
class UML2WithID_DeploymentTarget(Element, NamedElement):

    pass
class UML2WithID_DestroyLinkAction(WriteLinkAction, Element):

    pass
class UML2WithID_ConnectableElement(Element, NamedElement):

    pass
class UML2WithID_InvocationAction(Action, Element):

    pass
class UML2WithID_Association(Classifier, Element):

    pass
class UML2WithID_Enumeration(DataType, Element):

    pass
class UML2WithID_InformationItem(Classifier, Element):

    pass
class UML2WithID_Stereotype(Element, Class):

    pass
class UML2WithID_TestIdentityAction(Action, Element):

    pass
class UML2WithID_BroadcastSignalAction(Element, InvocationAction):

    pass
class UML2WithID_Model(Package, Element):

    pass
class UML2WithID_Gate(MessageEnd, Element):

    pass
class UML2WithID_SendSignalAction(Element, InvocationAction):

    pass
class UML2WithID_Interface(Classifier, Element):

    pass
class UML2WithID_Manifestation(Element, Abstraction):

    pass
class UML2WithID_RemoveVariableValueAction(Element, WriteVariableAction):

    pass
class UML2WithID_Trigger(Element, NamedElement):

    pass
class UML2WithID_Collaboration(Element, BehavioredClassifier, StructuredClassifier):

    pass
class UML2WithID_CentralBufferNode(ObjectNode, Element):

    pass
class UML2WithID_Include(Element, NamedElement):

    pass
class UML2WithID_RedefinableTemplateSignature(RedefinableElement, Element):

    pass
class UML2WithID_WriteLinkAction(LinkAction, Element):

    pass
class UML2WithID_Classifier(Namespace, Type, Element, RedefinableElement):

    pass
class UML2WithID_Class(EncapsulatedClassifier, Element, BehavioredClassifier):

    pass
class UML2WithID_Deployment(Element, Dependency):

    pass
class UML2WithID_FlowFinalNode(Element, FinalNode):

    pass
class UML2WithID_ExpansionRegion(StructuredActivityNode, Element):

    pass
class UML2WithID_BehavioralFeature(Namespace, Element, Feature):

    pass
class UML2WithID_ClearAssociationAction(Action, Element):

    pass
class UML2WithID_AnyTrigger(MessageTrigger, Element):

    pass
class UML2WithID_AssociationClass(Association, Element, Class):

    pass
class UML2WithID_InputPin(Element, Pin):

    pass
class UML2WithID_EventOccurrence(MessageEnd, Element, InteractionFragment):

    pass
class UML2WithID_FinalState(State, Element):

    pass
class UML2WithID_DataStoreNode(Element, CentralBufferNode):

    pass
class UML2WithID_Profile(Package, Element):

    pass
class UML2WithID_ReadExtentAction(Action, Element):

    pass
class UML2WithID_BehavioredClassifier(Classifier, Element):

    pass
class ControlNode:

    pass
class UML2WithID_DecisionNode(Element, ControlNode):

    pass
class UML2WithID_InitialNode(Element, ControlNode):

    pass
class UML2WithID_ForkNode(Element, ControlNode):

    pass
class UML2WithID_FinalNode(Element, ControlNode):

    pass
class UML2WithID_MergeNode(Element, ControlNode):

    pass
class UML2WithID_JoinNode(Element, ControlNode):

    pass