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
        
        pass
    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID


class EventOccurrence:

    pass
class EncapsulatedClassifier:

    pass
class Artifact:

    pass
class Pin:

    pass
class DataType:

    pass
class StateMachine:

    pass
class FinalNode:

    pass
class CallAction:

    pass
class WriteLinkAction:

    pass
class ActivityEdge:

    pass
class Realization:

    pass
class Constraint:

    pass
class StructuredActivityNode:

    pass
class AcceptEventAction:

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
class ExecutableNode:

    pass
class OpaqueExpression:

    pass
class StructuralFeatureAction:

    pass
class CreateLinkAction:

    pass
class InstanceSpecification:

    pass
class StructuredClassifier:

    pass
class InteractionFragment:

    pass
class ValueSpecification:

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
class BehavioredClassifier:

    pass
class IntervalConstraint:

    pass
class State:

    pass
class MessageEnd:

    pass
class Type:

    pass
class Package:

    pass
class NamedElement:

    pass
class TypedElement:

    pass
class Feature:

    pass
class LiteralSpecification:

    pass
class Dependency:

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
class Association:

    pass
class Node:

    pass
class Action:

    pass
class Trigger:

    pass
class VariableAction:

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
class Classifier:

    pass
class ObjectNode:

    pass
class Element:

    pass
class UML2WithID_StateMachine(Behavior, Element):

    pass
class UML2WithID_CommunicationPath(Element, Association):

    pass
class UML2WithID_InformationItem(Element, Classifier):

    pass
class UML2WithID_IntervalConstraint(Constraint, Element):

    pass
class UML2WithID_Dependency(Element, PackageableElement):

    pass
class UML2WithID_FinalState(State, Element):

    pass
class UML2WithID_InteractionFragment(Element, NamedElement):

    pass
class UML2WithID_Constraint(Element, PackageableElement):

    pass
class UML2WithID_Message(Element, NamedElement):

    pass
class UML2WithID_StructuralFeature(TypedElement, Feature, Element):

    pass
class UML2WithID_Substitution(Realization, Element):

    pass
class UML2WithID_DurationObservationAction(WriteStructuralFeatureAction, Element):

    pass
class UML2WithID_ReclassifyObjectAction(Element, Action):

    pass
class UML2WithID_Connector(Feature, Element):

    pass
class UML2WithID_StateInvariant(InteractionFragment, Element):

    pass
class UML2WithID_CollaborationOccurrence(Element, NamedElement):

    pass
class UML2WithID_Activity(Behavior, Element):

    pass
class UML2WithID_OutputPin(Element, Pin):

    pass
class UML2WithID_Continuation(InteractionFragment, Element):

    pass
class UML2WithID_DeployedArtifact(Element, NamedElement):

    pass
class UML2WithID_Pin(ObjectNode, Element):

    pass
class UML2WithID_ConnectableElement(Element, NamedElement):

    pass
class UML2WithID_Deployment(Dependency, Element):

    pass
class UML2WithID_SendSignalAction(Element, InvocationAction):

    pass
class UML2WithID_Enumeration(DataType, Element):

    pass
class UML2WithID_Property(StructuralFeature, DeploymentTarget, Element, ConnectableElement):

    pass
class UML2WithID_LiteralBoolean(LiteralSpecification, Element):

    pass
class UML2WithID_WriteVariableAction(VariableAction, Element):

    pass
class UML2WithID_Device(Element, Node):

    pass
class UML2WithID_AcceptCallAction(AcceptEventAction, Element):

    pass
class UML2WithID_ReadVariableAction(VariableAction, Element):

    pass
class UML2WithID_CallOperationAction(CallAction, Element):

    pass
class UML2WithID_Lifeline(Element, NamedElement):

    pass
class UML2WithID_InstanceSpecification(DeployedArtifact, DeploymentTarget, Element, PackageableElement):

    pass
class UML2WithID_GeneralizationSet(Element, PackageableElement):

    pass
class UML2WithID_ExecutionOccurrence(InteractionFragment, Element):

    pass
class UML2WithID_Interface(Element, Classifier):

    pass
class UML2WithID_PrimitiveType(DataType, Element):

    pass
class UML2WithID_ControlFlow(ActivityEdge, Element):

    pass
class UML2WithID_BroadcastSignalAction(Element, InvocationAction):

    pass
class UML2WithID_DataType(Element, Classifier):

    pass
class UML2WithID_CallBehaviorAction(CallAction, Element):

    pass
class UML2WithID_CreateObjectAction(Element, Action):

    pass
class UML2WithID_LiteralNull(LiteralSpecification, Element):

    pass
class UML2WithID_PartDecomposition(Element, InteractionOccurrence):

    pass
class UML2WithID_Implementation(Realization, Element):

    pass
class UML2WithID_CreateLinkAction(Element, WriteLinkAction):

    pass
class UML2WithID_Variable(TypedElement, Element, ConnectableElement):

    pass
class UML2WithID_OpaqueExpression(ValueSpecification, Element):

    pass
class UML2WithID_CentralBufferNode(ObjectNode, Element):

    pass
class UML2WithID_VariableAction(Element, Action):

    pass
class UML2WithID_Extend(Element, NamedElement):

    pass
class UML2WithID_DestroyObjectAction(Element, Action):

    pass
class UML2WithID_TypedElement(Element, NamedElement):

    pass
class UML2WithID_ParameterSet(Element, NamedElement):

    pass
class UML2WithID_UseCase(Element, BehavioredClassifier):

    pass
class UML2WithID_SendObjectAction(Element, InvocationAction):

    pass
class UML2WithID_Node(Class, DeploymentTarget, Element):

    pass
class UML2WithID_ClearAssociationAction(Element, Action):

    pass
class UML2WithID_InvocationAction(Element, Action):

    pass
class UML2WithID_Signal(Element, Classifier):

    pass
class UML2WithID_InteractionConstraint(Constraint, Element):

    pass
class UML2WithID_DeploymentSpecification(Artifact, Element):

    pass
class UML2WithID_ChangeTrigger(Element, Trigger):

    pass
class UML2WithID_ClearVariableAction(VariableAction, Element):

    pass
class UML2WithID_InputPin(Element, Pin):

    pass
class UML2WithID_RemoveStructuralFeatureValueAction(WriteStructuralFeatureAction, Element):

    pass
class UML2WithID_ActivityEdge(RedefinableElement, Element):

    pass
class UML2WithID_Feature(RedefinableElement, Element):

    pass
class UML2WithID_InstanceValue(ValueSpecification, Element):

    pass
class UML2WithID_ActivityNode(RedefinableElement, Element):

    pass
class UML2WithID_Abstraction(Dependency, Element):

    pass
class UML2WithID_EventOccurrence(InteractionFragment, MessageEnd, Element):

    pass
class UML2WithID_ClearStructuralFeatureAction(StructuralFeatureAction, Element):

    pass
class UML2WithID_RedefinableTemplateSignature(RedefinableElement, Element):

    pass
class UML2WithID_Realization(Abstraction, Element):

    pass
class UML2WithID_ConnectionPointReference(Vertex, Element):

    pass
class UML2WithID_AddVariableValueAction(WriteVariableAction, Element):

    pass
class UML2WithID_Pseudostate(Vertex, Element):

    pass
class UML2WithID_ReadLinkObjectEndQualifierAction(Element, Action):

    pass
class UML2WithID_Include(Element, NamedElement):

    pass
class UML2WithID_LinkAction(Element, Action):

    pass
class UML2WithID_RedefinableElement(Element, NamedElement):

    pass
class UML2WithID_Interaction(InteractionFragment, Behavior, Element):

    pass
class UML2WithID_GeneralOrdering(Element, NamedElement):

    pass
class UML2WithID_ExpansionNode(ObjectNode, Element):

    pass
class UML2WithID_ControlNode(ActivityNode, Element):

    pass
class UML2WithID_WriteLinkAction(LinkAction, Element):

    pass
class UML2WithID_Collaboration(StructuredClassifier, Element, BehavioredClassifier):

    pass
class UML2WithID_Component(Class, Element):

    pass
class UML2WithID_DurationConstraint(IntervalConstraint, Element):

    pass
class UML2WithID_ExpansionRegion(StructuredActivityNode, Element):

    pass
class UML2WithID_Reception(BehavioralFeature, Element):

    pass
class UML2WithID_PackageableElement(Element, NamedElement):

    pass
class UML2WithID_Trigger(Element, NamedElement):

    pass
class UML2WithID_WriteStructuralFeatureAction(StructuralFeatureAction, Element):

    pass
class UML2WithID_ValueSpecification(TypedElement, Element):

    pass
class UML2WithID_ActivityPartition(Element, NamedElement):

    pass
class UML2WithID_TimeExpression(ValueSpecification, Element):

    pass
class UML2WithID_Action(ExecutableNode, Element):

    pass
class UML2WithID_ReadSelfAction(Element, Action):

    pass
class UML2WithID_AnyTrigger(MessageTrigger, Element):

    pass
class UML2WithID_AssociationClass(Class, Element, Association):

    pass
class UML2WithID_Operation(BehavioralFeature, TypedElement, Element):

    pass
class UML2WithID_ExecutableNode(ActivityNode, Element):

    pass
class UML2WithID_Duration(ValueSpecification, Element):

    pass
class UML2WithID_TimeConstraint(IntervalConstraint, Element):

    pass
class UML2WithID_Usage(Dependency, Element):

    pass
class UML2WithID_MessageTrigger(Element, Trigger):

    pass
class UML2WithID_Parameter(TypedElement, Element, ConnectableElement):

    pass
class UML2WithID_Interval(ValueSpecification, Element):

    pass
class UML2WithID_ReadLinkAction(LinkAction, Element):

    pass
class UML2WithID_CreateLinkObjectAction(CreateLinkAction, Element):

    pass
class UML2WithID_RemoveVariableValueAction(WriteVariableAction, Element):

    pass
class UML2WithID_CombinedFragment(InteractionFragment, Element):

    pass
class UML2WithID_Permission(Dependency, Element):

    pass
class UML2WithID_ReadStructuralFeatureAction(StructuralFeatureAction, Element):

    pass
class UML2WithID_MessageEnd(Element, NamedElement):

    pass
class UML2WithID_DeploymentTarget(Element, NamedElement):

    pass
class UML2WithID_LiteralInteger(LiteralSpecification, Element):

    pass
class UML2WithID_BehavioredClassifier(Element, Classifier):

    pass
class UML2WithID_ReadIsClassifiedObjectAction(Element, Action):

    pass
class UML2WithID_Type(Element, PackageableElement):

    pass
class UML2WithID_StructuralFeatureAction(Element, Action):

    pass
class UML2WithID_ExecutionEnvironment(Element, Node):

    pass
class UML2WithID_Expression(OpaqueExpression, Element):

    pass
class UML2WithID_Artifact(DeployedArtifact, Element, Classifier):

    pass
class UML2WithID_LiteralUnlimitedNatural(LiteralSpecification, Element):

    pass
class UML2WithID_ApplyFunctionAction(Element, Action):

    pass
class UML2WithID_SignalTrigger(MessageTrigger, Element):

    pass
class UML2WithID_TemplateableClassifier(Element, Classifier):

    pass
class UML2WithID_Stereotype(Class, Element):

    pass
class UML2WithID_Behavior(Class, Element):

    pass
class UML2WithID_Gate(MessageEnd, Element):

    pass
class UML2WithID_CallAction(Element, InvocationAction):

    pass
class UML2WithID_PrimitiveFunction(Element, PackageableElement):

    pass
class UML2WithID_TestIdentityAction(Element, Action):

    pass
class UML2WithID_Port(Property, Element):

    pass
class UML2WithID_TimeTrigger(Element, Trigger):

    pass
class UML2WithID_Actor(Element, Classifier):

    pass
class UML2WithID_CallTrigger(MessageTrigger, Element):

    pass
class UML2WithID_ActivityFinalNode(FinalNode, Element):

    pass
class UML2WithID_ObjectFlow(ActivityEdge, Element):

    pass
class UML2WithID_ReadExtentAction(Element, Action):

    pass
class UML2WithID_Stop(EventOccurrence, Element):

    pass
class UML2WithID_Class(Element, EncapsulatedClassifier, BehavioredClassifier):

    pass
class UML2WithID_DestroyLinkAction(Element, WriteLinkAction):

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

class UML2WithID_AddStructuralFeatureValueAction(WriteStructuralFeatureAction, Element):

    pass
class UML2WithID_AcceptEventAction(Element, Action):

    pass
class UML2WithID_ValuePin(InputPin, Element):

    pass
class UML2WithID_ExtensionPoint(RedefinableElement, Element):

    pass
class UML2WithID_StructuredClassifier(Element, Classifier):

    pass
class UML2WithID_RaiseExceptionAction(Element, Action):

    pass
class UML2WithID_FlowFinalNode(FinalNode, Element):

    pass
class UML2WithID_ObjectNode(TypedElement, ActivityNode, Element):

    pass
class UML2WithID_ActivityParameterNode(ObjectNode, Element):

    pass
class UML2WithID_StartOwnedBehaviorAction(Element, Action):

    pass
class UML2WithID_LiteralSpecification(ValueSpecification, Element):

    pass
class UML2WithID_LoopNode(StructuredActivityNode, Element):

    pass
class UML2WithID_Manifestation(Abstraction, Element):

    pass
class UML2WithID_ReadLinkObjectEndAction(Element, Action):

    pass
class UML2WithID_Namespace(Element, NamedElement):

    pass
class UML2WithID_DataStoreNode(CentralBufferNode, Element):

    pass
class UML2WithID_ProtocolStateMachine(StateMachine, Element):

    pass
class UML2WithID_TimeObservationAction(WriteStructuralFeatureAction, Element):

    pass
class UML2WithID_Profile(Element, Package):

    pass
class UML2WithID_Association(Element, Classifier):

    pass
class UML2WithID_Model(Element, Package):

    pass
class UML2WithID_Vertex(Element, NamedElement):

    pass
class UML2WithID_Transition(RedefinableElement, Element):

    pass
class UML2WithID_ExtensionEnd(Property, Element):

    pass
class UML2WithID_EncapsulatedClassifier(StructuredClassifier, Element):

    pass
class UML2WithID_ProtocolTransition(Transition, Element):

    pass
class UML2WithID_ConditionalNode(StructuredActivityNode, Element):

    pass
class UML2WithID_LiteralString(LiteralSpecification, Element):

    pass
class UML2WithID_ReplyAction(Element, Action):

    pass
class UML2WithID_EnumerationLiteral(InstanceSpecification, Element):

    pass
class UML2WithID_InformationFlow(Element, PackageableElement):

    pass
class UML2WithID_Extension(Element, Association):

    pass
class UML2WithID_InteractionOccurrence(InteractionFragment, Element):

    pass
class ControlNode:

    pass
class UML2WithID_MergeNode(ControlNode, Element):

    pass
class UML2WithID_DecisionNode(ControlNode, Element):

    pass
class UML2WithID_ForkNode(ControlNode, Element):

    pass
class UML2WithID_FinalNode(ControlNode, Element):

    pass
class UML2WithID_InitialNode(ControlNode, Element):

    pass
class UML2WithID_JoinNode(ControlNode, Element):

    pass
class Namespace:

    pass
class UML2WithID_StructuredActivityNode(Namespace, Element, Action):

    pass
class UML2WithID_InteractionOperand(InteractionFragment, Namespace, Element):

    pass
class UML2WithID_BehavioralFeature(Namespace, Element, Feature):

    pass
class UML2WithID_Region(RedefinableElement, Namespace, Element):

    pass
class UML2WithID_Classifier(RedefinableElement, Namespace, Element, Type):

    pass
class UML2WithID_Package(Namespace, Element, PackageableElement):

    pass
class UML2WithID_State(Vertex, RedefinableElement, Namespace, Element):

    pass
class UML2WithID_ParameterableClassifier(Element, Classifier):

    pass
class Interval:

    pass
class UML2WithID_TimeInterval(Interval, Element):

    pass
class UML2WithID_DurationInterval(Interval, Element):

    pass