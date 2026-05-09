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

class Abstraction:

    pass
class Transition:

    pass
class BehavioralFeature:

    pass
class DeployedArtifact:

    pass
class ValueSpecification:

    pass
class Association:

    pass
class Element:

    pass
class UML2WithID_Extension(Association, Element):

    pass
class UML2WithID_Interval(ValueSpecification, Element):

    pass
class UML2WithID_ProtocolTransition(Transition, Element):

    pass
class UML2WithID_Reception(BehavioralFeature, Element):

    pass
class UML2WithID_Manifestation(Abstraction, Element):

    pass
class TypedElement:

    pass
class UML2WithID_Operation(TypedElement, BehavioralFeature, Element):

    pass
class ActivityNode:

    pass
class UML2WithID_ObjectNode(TypedElement, ActivityNode, Element):

    pass
class Classifier:

    pass
class UML2WithID_Artifact(DeployedArtifact, Classifier, Element):

    pass
class UML2WithID_Association(Classifier, Element):

    pass
class WriteVariableAction:

    pass
class UML2WithID_RemoveVariableValueAction(WriteVariableAction, Element):

    pass
class MessageTrigger:

    pass
class UML2WithID_SignalTrigger(MessageTrigger, Element):

    pass
class InteractionFragment:

    pass
class UML2WithID_Continuation(InteractionFragment, Element):

    pass
class UML2WithID_ExecutionOccurrence(InteractionFragment, Element):

    pass
class Namespace:

    pass
class Action:

    pass
class UML2WithID_StructuredActivityNode(Action, Namespace, Element):

    pass
class UML2WithID_ReadIsClassifiedObjectAction(Action, Element):

    pass
class UML2WithID_StartOwnedBehaviorAction(Action, Element):

    pass
class UML2WithID_VariableAction(Action, Element):

    pass
class Vertex:

    pass
class UML2WithID_ConnectionPointReference(Vertex, Element):

    pass
class UML2WithID_Pseudostate(Vertex, Element):

    pass
class PackageableElement:

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


class UML2WithID_ControlNode(ActivityNode, Element):

    pass
class UML2WithID_CallTrigger(MessageTrigger, Element):

    pass
class UML2WithID_PrimitiveFunction(PackageableElement, Element):

    pass
class CreateLinkAction:

    pass
class UML2WithID_CreateLinkObjectAction(CreateLinkAction, Element):

    pass
class IntervalConstraint:

    pass
class UML2WithID_TimeConstraint(Element, IntervalConstraint):

    pass
class UML2WithID_DurationConstraint(IntervalConstraint, Element):

    pass
class CentralBufferNode:

    pass
class UML2WithID_DataStoreNode(CentralBufferNode, Element):

    pass
class EventOccurrence:

    pass
class UML2WithID_Stop(EventOccurrence, Element):

    pass
class UML2WithID_InformationItem(Classifier, Element):

    pass
class UML2WithID_InteractionOccurrence(InteractionFragment, Element):

    pass
class AcceptEventAction:

    pass
class UML2WithID_AcceptCallAction(AcceptEventAction, Element):

    pass
class UML2WithID_CombinedFragment(InteractionFragment, Element):

    pass
class InteractionOccurrence:

    pass
class UML2WithID_PartDecomposition(InteractionOccurrence, Element):

    pass
class UML2WithID_ReadExtentAction(Action, Element):

    pass
class UML2WithID_CreateObjectAction(Action, Element):

    pass
class UML2WithID_CommunicationPath(Association, Element):

    pass
class UML2WithID_ClearAssociationAction(Action, Element):

    pass
class UML2WithID_AnyTrigger(MessageTrigger, Element):

    pass
class StructuredClassifier:

    pass
class UML2WithID_EncapsulatedClassifier(StructuredClassifier, Element):

    pass
class UML2WithID_Dependency(PackageableElement, Element):

    pass
class UML2WithID_AcceptEventAction(Action, Element):

    pass
class UML2WithID_TestIdentityAction(Action, Element):

    pass
class Realization:

    pass
class UML2WithID_Substitution(Realization, Element):

    pass
class UML2WithID_Implementation(Realization, Element):

    pass
class UML2WithID_RaiseExceptionAction(Action, Element):

    pass
class UML2WithID_Signal(Classifier, Element):

    pass
class UML2WithID_BehavioredClassifier(Classifier, Element):

    pass
class UML2WithID_Interface(Classifier, Element):

    pass
class Type:

    pass
class UML2WithID_TemplateableClassifier(Classifier, Element):

    pass
class WriteStructuralFeatureAction:

    pass
class UML2WithID_AddStructuralFeatureValueAction(WriteStructuralFeatureAction, Element):

    pass
class UML2WithID_TimeObservationAction(WriteStructuralFeatureAction, Element):

    pass
class UML2WithID_DurationObservationAction(WriteStructuralFeatureAction, Element):

    pass
class UML2WithID_RemoveStructuralFeatureValueAction(WriteStructuralFeatureAction, Element):

    pass
class UML2WithID_ValueSpecification(TypedElement, Element):

    pass
class UML2WithID_DataType(Classifier, Element):

    pass
class UML2WithID_LiteralSpecification(ValueSpecification, Element):

    pass
class UML2WithID_ExecutableNode(ActivityNode, Element):

    pass
class LinkAction:

    pass
class UML2WithID_WriteLinkAction(LinkAction, Element):

    pass
class UML2WithID_ReadLinkAction(LinkAction, Element):

    pass
class Pin:

    pass
class UML2WithID_OutputPin(Pin, Element):

    pass
class UML2WithID_InputPin(Pin, Element):

    pass
class UML2WithID_ReclassifyObjectAction(Action, Element):

    pass
class UML2WithID_LinkAction(Action, Element):

    pass
class UML2WithID_ReadLinkObjectEndAction(Action, Element):

    pass
class Feature:

    pass
class UML2WithID_StructuralFeature(TypedElement, Feature, Element):

    pass
class UML2WithID_Connector(Feature, Element):

    pass
class UML2WithID_BehavioralFeature(Feature, Namespace, Element):

    pass
class UML2WithID_InteractionOperand(Namespace, InteractionFragment, Element):

    pass
class Artifact:

    pass
class UML2WithID_DeploymentSpecification(Artifact, Element):

    pass
class StructuralFeature:

    pass
class UML2WithID_Constraint(PackageableElement, Element):

    pass
class MessageEnd:

    pass
class UML2WithID_Gate(MessageEnd, Element):

    pass
class UML2WithID_EventOccurrence(MessageEnd, InteractionFragment, Element):

    pass
class UML2WithID_Realization(Abstraction, Element):

    pass
class DeploymentTarget:

    pass
class UML2WithID_InstanceSpecification(PackageableElement, DeployedArtifact, DeploymentTarget, Element):

    pass
class Package:

    pass
class UML2WithID_Profile(Package, Element):

    pass
class UML2WithID_Model(Package, Element):

    pass
class Constraint:

    pass
class UML2WithID_InteractionConstraint(Constraint, Element):

    pass
class UML2WithID_IntervalConstraint(Constraint, Element):

    pass
class ExecutableNode:

    pass
class UML2WithID_Action(ExecutableNode, Element):

    pass
class UML2WithID_ReplyAction(Action, Element):

    pass
class StateMachine:

    pass
class UML2WithID_ProtocolStateMachine(StateMachine, Element):

    pass
class UML2WithID_StructuredClassifier(Classifier, Element):

    pass
class VariableAction:

    pass
class UML2WithID_ClearVariableAction(VariableAction, Element):

    pass
class UML2WithID_WriteVariableAction(VariableAction, Element):

    pass
class UML2WithID_ReadVariableAction(VariableAction, Element):

    pass
class Node:

    pass
class UML2WithID_ExecutionEnvironment(Node, Element):

    pass
class UML2WithID_Device(Node, Element):

    pass
class FinalNode:

    pass
class UML2WithID_FlowFinalNode(FinalNode, Element):

    pass
class ConnectableElement:

    pass
class UML2WithID_Parameter(ConnectableElement, TypedElement, Element):

    pass
class UML2WithID_Property(ConnectableElement, StructuralFeature, DeploymentTarget, Element):

    pass
class UML2WithID_Variable(ConnectableElement, TypedElement, Element):

    pass
class StructuredActivityNode:

    pass
class UML2WithID_LoopNode(StructuredActivityNode, Element):

    pass
class UML2WithID_ExpansionRegion(StructuredActivityNode, Element):

    pass
class UML2WithID_ConditionalNode(StructuredActivityNode, Element):

    pass
class EncapsulatedClassifier:

    pass
class BehavioredClassifier:

    pass
class UML2WithID_UseCase(BehavioredClassifier, Element):

    pass
class UML2WithID_Collaboration(BehavioredClassifier, StructuredClassifier, Element):

    pass
class UML2WithID_Class(EncapsulatedClassifier, BehavioredClassifier, Element):

    pass
class UML2WithID_Package(PackageableElement, Namespace, Element):

    pass
class UML2WithID_AddVariableValueAction(Element, WriteVariableAction):

    pass
class UML2WithID_StateInvariant(InteractionFragment, Element):

    pass
class UML2WithID_ReadLinkObjectEndQualifierAction(Action, Element):

    pass
class UML2WithID_Type(PackageableElement, Element):

    pass
class UML2WithID_GeneralizationSet(PackageableElement, Element):

    pass
class WriteLinkAction:

    pass
class UML2WithID_CreateLinkAction(WriteLinkAction, Element):

    pass
class UML2WithID_DestroyLinkAction(WriteLinkAction, Element):

    pass
class Trigger:

    pass
class UML2WithID_MessageTrigger(Trigger, Element):

    pass
class UML2WithID_ChangeTrigger(Trigger, Element):

    pass
class UML2WithID_TimeTrigger(Trigger, Element):

    pass
class Property:

    pass
class UML2WithID_Port(Property, Element):

    pass
class UML2WithID_ExtensionEnd(Property, Element):

    pass
class InstanceSpecification:

    pass
class UML2WithID_EnumerationLiteral(InstanceSpecification, Element):

    pass
class ControlNode:

    pass
class UML2WithID_ForkNode(ControlNode, Element):

    pass
class UML2WithID_InitialNode(ControlNode, Element):

    pass
class UML2WithID_FinalNode(ControlNode, Element):

    pass
class UML2WithID_MergeNode(ControlNode, Element):

    pass
class UML2WithID_DecisionNode(ControlNode, Element):

    pass
class UML2WithID_JoinNode(ControlNode, Element):

    pass
class UML2WithID_NamedElement(Element):

    def __init__(self, visibility: str, UML2WithID_NamedElement: "UML2WithID_Namespace" = None):
        self.visibility = visibility
        self.UML2WithID_NamedElement = UML2WithID_NamedElement
        
        pass
    @property
    def visibility(self):
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

class UML2WithID_ParameterableClassifier(Classifier, Element):

    pass
class ObjectNode:

    pass
class UML2WithID_Pin(Element, ObjectNode):

    pass
class UML2WithID_ExpansionNode(Element, ObjectNode):

    pass
class UML2WithID_CentralBufferNode(Element, ObjectNode):

    pass
class UML2WithID_ActivityParameterNode(Element, ObjectNode):

    pass
class DataType:

    pass
class UML2WithID_Enumeration(DataType, Element):

    pass
class UML2WithID_PrimitiveType(DataType, Element):

    pass
class UML2WithID_Actor(Classifier, Element):

    pass
class UML2WithID_ReadSelfAction(Action, Element):

    pass
class Behavior:

    pass
class UML2WithID_Interaction(Behavior, InteractionFragment, Element):

    pass
class UML2WithID_StateMachine(Behavior, Element):

    pass
class UML2WithID_Activity(Behavior, Element):

    pass
class UML2WithID_ActivityFinalNode(FinalNode, Element):

    pass
class UML2WithID_InstanceValue(ValueSpecification, Element):

    pass
class StructuralFeatureAction:

    pass
class UML2WithID_WriteStructuralFeatureAction(StructuralFeatureAction, Element):

    pass
class UML2WithID_ClearStructuralFeatureAction(Element, StructuralFeatureAction):

    pass
class UML2WithID_ReadStructuralFeatureAction(Element, StructuralFeatureAction):

    pass
class CallAction:

    pass
class UML2WithID_CallOperationAction(CallAction, Element):

    pass
class UML2WithID_CallBehaviorAction(CallAction, Element):

    pass
class OpaqueExpression:

    pass
class UML2WithID_Expression(OpaqueExpression, Element):

    pass
class Interval:

    pass
class UML2WithID_DurationInterval(Element, Interval):

    pass
class UML2WithID_TimeInterval(Interval, Element):

    pass
class UML2WithID_StructuralFeatureAction(Action, Element):

    pass
class RedefinableElement:

    pass
class UML2WithID_Transition(RedefinableElement, Element):

    pass
class UML2WithID_ExtensionPoint(RedefinableElement, Element):

    pass
class UML2WithID_ActivityEdge(RedefinableElement, Element):

    pass
class UML2WithID_Classifier(Namespace, RedefinableElement, Type, Element):

    pass
class UML2WithID_Region(Namespace, RedefinableElement, Element):

    pass
class UML2WithID_Feature(RedefinableElement, Element):

    pass
class UML2WithID_State(Element, Vertex, RedefinableElement, Namespace):

    pass
class UML2WithID_RedefinableTemplateSignature(RedefinableElement, Element):

    pass
class UML2WithID_ActivityNode(RedefinableElement, Element):

    pass
class UML2WithID_Duration(ValueSpecification, Element):

    pass
class ActivityEdge:

    pass
class UML2WithID_ObjectFlow(ActivityEdge, Element):

    pass
class UML2WithID_ControlFlow(ActivityEdge, Element):

    pass
class Class:

    pass
class UML2WithID_Node(DeploymentTarget, Class, Element):

    pass
class UML2WithID_Component(Class, Element):

    pass
class UML2WithID_Stereotype(Class, Element):

    pass
class UML2WithID_AssociationClass(Association, Class, Element):

    pass
class UML2WithID_Behavior(Class, Element):

    pass
class InputPin:

    pass
class UML2WithID_ValuePin(InputPin, Element):

    pass
class UML2WithID_ApplyFunctionAction(Action, Element):

    pass
class UML2WithID_InvocationAction(Action, Element):

    pass
class NamedElement:

    pass
class UML2WithID_ParameterSet(NamedElement, Element):

    pass
class UML2WithID_DeploymentTarget(NamedElement, Element):

    pass
class UML2WithID_ConnectableElement(NamedElement, Element):

    pass
class UML2WithID_Extend(NamedElement, Element):

    pass
class UML2WithID_CollaborationOccurrence(NamedElement, Element):

    pass
class UML2WithID_TypedElement(NamedElement, Element):

    pass
class UML2WithID_Namespace(NamedElement, Element):

    pass
class UML2WithID_PackageableElement(NamedElement, Element):

    pass
class UML2WithID_Include(NamedElement, Element):

    pass
class UML2WithID_Lifeline(NamedElement, Element):

    pass
class UML2WithID_Trigger(NamedElement, Element):

    pass
class UML2WithID_Message(NamedElement, Element):

    pass
class UML2WithID_GeneralOrdering(NamedElement, Element):

    pass
class UML2WithID_Vertex(NamedElement, Element):

    pass
class UML2WithID_DeployedArtifact(NamedElement, Element):

    pass
class UML2WithID_InteractionFragment(NamedElement, Element):

    pass
class UML2WithID_MessageEnd(NamedElement, Element):

    pass
class UML2WithID_ActivityPartition(NamedElement, Element):

    pass
class UML2WithID_RedefinableElement(NamedElement, Element):

    pass
class Dependency:

    pass
class UML2WithID_Deployment(Dependency, Element):

    pass
class UML2WithID_Abstraction(Dependency, Element):

    pass
class UML2WithID_Usage(Dependency, Element):

    pass
class UML2WithID_Permission(Dependency, Element):

    pass
class InvocationAction:

    pass
class UML2WithID_SendSignalAction(InvocationAction, Element):

    pass
class UML2WithID_BroadcastSignalAction(InvocationAction, Element):

    pass
class UML2WithID_SendObjectAction(InvocationAction, Element):

    pass
class UML2WithID_CallAction(InvocationAction, Element):

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
class UML2WithID_DestroyObjectAction(Action, Element):

    pass
class State:

    pass
class UML2WithID_FinalState(State, Element):

    pass
class UML2WithID_OpaqueExpression(ValueSpecification, Element):

    pass
class UML2WithID_TimeExpression(ValueSpecification, Element):

    pass
class UML2WithID_InformationFlow(PackageableElement, Element):

    pass