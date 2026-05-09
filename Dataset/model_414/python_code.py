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


class Type:

    pass
class Package:

    pass
class State:

    pass
class InteractionOccurrence:

    pass
class BehavioralFeature:

    pass
class Interval:

    pass
class OpaqueExpression:

    pass
class InputPin:

    pass
class Constraint:

    pass
class ActivityEdge:

    pass
class Feature:

    pass
class StructuredClassifier:

    pass
class Realization:

    pass
class DataType:

    pass
class Pin:

    pass
class Dependency:

    pass
class CentralBufferNode:

    pass
class EventOccurrence:

    pass
class VariableAction:

    pass
class MessageTrigger:

    pass
class InstanceSpecification:

    pass
class CreateLinkAction:

    pass
class Association:

    pass
class DeployedArtifact:

    pass
class WriteStructuralFeatureAction:

    pass
class ActivityNode:

    pass
class IntervalConstraint:

    pass
class Node:

    pass
class ControlNode:

    pass
class Behavior:

    pass
class PackageableElement:

    pass
class Namespace:

    pass
class LinkAction:

    pass
class ValueSpecification:

    pass
class Abstraction:

    pass
class StateMachine:

    pass
class InvocationAction:

    pass
class CallAction:

    pass
class Classifier:

    pass
class FinalNode:

    pass
class RedefinableElement:

    pass
class Property:

    pass
class WriteVariableAction:

    pass
class MessageEnd:

    pass
class EncapsulatedClassifier:

    pass
class BehavioredClassifier:

    pass
class Artifact:

    pass
class StructuralFeatureAction:

    pass
class DeploymentTarget:

    pass
class StructuralFeature:

    pass
class InteractionFragment:

    pass
class StructuredActivityNode:

    pass
class LiteralSpecification:

    pass
class AcceptEventAction:

    pass
class ExecutableNode:

    pass
class ObjectNode:

    pass
class TypedElement:

    pass
class ConnectableElement:

    pass
class Vertex:

    pass
class NamedElement:

    pass
class Class:

    pass
class Element:

    pass
class UML2WithID_ParameterableClassifier(Classifier, Element):

    pass
class UML2WithID_ExpansionNode(ObjectNode, Element):

    pass
class UML2WithID_GeneralizationSet(PackageableElement, Element):

    pass
class UML2WithID_Stop(EventOccurrence, Element):

    pass
class UML2WithID_Include(NamedElement, Element):

    pass
class UML2WithID_ObjectFlow(ActivityEdge, Element):

    pass
class UML2WithID_DeploymentSpecification(Artifact, Element):

    pass
class UML2WithID_Manifestation(Abstraction, Element):

    pass
class UML2WithID_RedefinableElement(NamedElement, Element):

    pass
class UML2WithID_WriteLinkAction(LinkAction, Element):

    pass
class UML2WithID_PrimitiveType(DataType, Element):

    pass
class UML2WithID_Node(Class, DeploymentTarget, Element):

    pass
class UML2WithID_EnumerationLiteral(InstanceSpecification, Element):

    pass
class UML2WithID_RemoveStructuralFeatureValueAction(WriteStructuralFeatureAction, Element):

    pass
class UML2WithID_Package(PackageableElement, Namespace, Element):

    pass
class UML2WithID_State(Vertex, RedefinableElement, Namespace, Element):

    pass
class UML2WithID_ControlFlow(ActivityEdge, Element):

    pass
class UML2WithID_ObjectNode(ActivityNode, Element, TypedElement):

    pass
class UML2WithID_InitialNode(ControlNode, Element):

    pass
class UML2WithID_InformationFlow(PackageableElement, Element):

    pass
class UML2WithID_Action(Element, ExecutableNode):

    pass
class UML2WithID_Feature(RedefinableElement, Element):

    pass
class UML2WithID_TimeConstraint(Element, IntervalConstraint):

    pass
class UML2WithID_Port(Element, Property):

    pass
class UML2WithID_Artifact(Classifier, DeployedArtifact, Element):

    pass
class UML2WithID_AssociationClass(Class, Association, Element):

    pass
class UML2WithID_Trigger(NamedElement, Element):

    pass
class UML2WithID_InstanceSpecification(PackageableElement, DeploymentTarget, DeployedArtifact, Element):

    pass
class UML2WithID_ExtensionEnd(Element, Property):

    pass
class UML2WithID_ReadVariableAction(VariableAction, Element):

    pass
class UML2WithID_UseCase(BehavioredClassifier, Element):

    pass
class UML2WithID_Pseudostate(Element, Vertex):

    pass
class UML2WithID_InstanceValue(ValueSpecification, Element):

    pass
class UML2WithID_CallBehaviorAction(CallAction, Element):

    pass
class UML2WithID_Permission(Dependency, Element):

    pass
class UML2WithID_StructuredClassifier(Classifier, Element):

    pass
class UML2WithID_Usage(Dependency, Element):

    pass
class UML2WithID_TimeExpression(ValueSpecification, Element):

    pass
class UML2WithID_ExtensionPoint(RedefinableElement, Element):

    pass
class UML2WithID_AcceptCallAction(AcceptEventAction, Element):

    pass
class UML2WithID_AddVariableValueAction(WriteVariableAction, Element):

    pass
class UML2WithID_CollaborationOccurrence(NamedElement, Element):

    pass
class UML2WithID_OpaqueExpression(ValueSpecification, Element):

    pass
class UML2WithID_JoinNode(ControlNode, Element):

    pass
class UML2WithID_ValueSpecification(Element, TypedElement):

    pass
class UML2WithID_MessageEnd(NamedElement, Element):

    pass
class UML2WithID_CreateLinkObjectAction(CreateLinkAction, Element):

    pass
class UML2WithID_TimeObservationAction(WriteStructuralFeatureAction, Element):

    pass
class UML2WithID_StateMachine(Behavior, Element):

    pass
class UML2WithID_Association(Classifier, Element):

    pass
class UML2WithID_PartDecomposition(InteractionOccurrence, Element):

    pass
class UML2WithID_InteractionConstraint(Constraint, Element):

    pass
class UML2WithID_Gate(MessageEnd, Element):

    pass
class UML2WithID_ExecutionOccurrence(InteractionFragment, Element):

    pass
class UML2WithID_StateInvariant(InteractionFragment, Element):

    pass
class UML2WithID_ExpansionRegion(StructuredActivityNode, Element):

    pass
class UML2WithID_DeploymentTarget(NamedElement, Element):

    pass
class UML2WithID_TypedElement(NamedElement, Element):

    pass
class UML2WithID_Profile(Element, Package):

    pass
class UML2WithID_StructuralFeature(Feature, Element, TypedElement):

    pass
class UML2WithID_ClearStructuralFeatureAction(StructuralFeatureAction, Element):

    pass
class UML2WithID_SendSignalAction(InvocationAction, Element):

    pass
class UML2WithID_CommunicationPath(Association, Element):

    pass
class UML2WithID_ActivityPartition(NamedElement, Element):

    pass
class UML2WithID_Model(Package, Element):

    pass
class UML2WithID_ActivityFinalNode(FinalNode, Element):

    pass
class UML2WithID_CallAction(InvocationAction, Element):

    pass
class UML2WithID_WriteStructuralFeatureAction(StructuralFeatureAction, Element):

    pass
class UML2WithID_LiteralSpecification(ValueSpecification, Element):

    pass
class UML2WithID_SignalTrigger(Element, MessageTrigger):

    pass
class UML2WithID_ReadLinkAction(LinkAction, Element):

    pass
class UML2WithID_Reception(BehavioralFeature, Element):

    pass
class UML2WithID_FlowFinalNode(FinalNode, Element):

    pass
class UML2WithID_ConditionalNode(StructuredActivityNode, Element):

    pass
class UML2WithID_LiteralNull(LiteralSpecification, Element):

    pass
class UML2WithID_Interaction(InteractionFragment, Behavior, Element):

    pass
class UML2WithID_DecisionNode(ControlNode, Element):

    pass
class UML2WithID_DurationConstraint(Element, IntervalConstraint):

    pass
class UML2WithID_Signal(Classifier, Element):

    pass
class UML2WithID_PrimitiveFunction(PackageableElement, Element):

    pass
class UML2WithID_GeneralOrdering(NamedElement, Element):

    pass
class UML2WithID_ControlNode(ActivityNode, Element):

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

class UML2WithID_InteractionOperand(InteractionFragment, Namespace, Element):

    pass
class UML2WithID_Region(RedefinableElement, Namespace, Element):

    pass
class UML2WithID_Device(Node, Element):

    pass
class UML2WithID_Class(EncapsulatedClassifier, BehavioredClassifier, Element):

    pass
class UML2WithID_Operation(BehavioralFeature, Element, TypedElement):

    pass
class UML2WithID_Implementation(Realization, Element):

    pass
class UML2WithID_IntervalConstraint(Constraint, Element):

    pass
class UML2WithID_ExecutableNode(ActivityNode, Element):

    pass
class UML2WithID_SendObjectAction(InvocationAction, Element):

    pass
class UML2WithID_ProtocolStateMachine(StateMachine, Element):

    pass
class UML2WithID_Deployment(Dependency, Element):

    pass
class UML2WithID_Parameter(ConnectableElement, Element, TypedElement):

    pass
class UML2WithID_Type(PackageableElement, Element):

    pass
class UML2WithID_RedefinableTemplateSignature(RedefinableElement, Element):

    pass
class UML2WithID_RemoveVariableValueAction(WriteVariableAction, Element):

    pass
class UML2WithID_ActivityParameterNode(Element, ObjectNode):

    pass
class UML2WithID_PackageableElement(NamedElement, Element):

    pass
class UML2WithID_ParameterSet(NamedElement, Element):

    pass
class UML2WithID_Continuation(InteractionFragment, Element):

    pass
class UML2WithID_CallOperationAction(CallAction, Element):

    pass
class UML2WithID_Interface(Classifier, Element):

    pass
class UML2WithID_Substitution(Realization, Element):

    pass
class UML2WithID_ConnectionPointReference(Element, Vertex):

    pass
class UML2WithID_Extend(NamedElement, Element):

    pass
class UML2WithID_CentralBufferNode(Element, ObjectNode):

    pass
class UML2WithID_ExecutionEnvironment(Node, Element):

    pass
class UML2WithID_LoopNode(StructuredActivityNode, Element):

    pass
class UML2WithID_CallTrigger(Element, MessageTrigger):

    pass
class UML2WithID_Component(Class, Element):

    pass
class UML2WithID_OutputPin(Pin, Element):

    pass
class UML2WithID_AddStructuralFeatureValueAction(WriteStructuralFeatureAction, Element):

    pass
class UML2WithID_Variable(ConnectableElement, Element, TypedElement):

    pass
class UML2WithID_Interval(ValueSpecification, Element):

    pass
class UML2WithID_ClearVariableAction(VariableAction, Element):

    pass
class UML2WithID_Constraint(PackageableElement, Element):

    pass
class UML2WithID_Lifeline(NamedElement, Element):

    pass
class UML2WithID_InputPin(Pin, Element):

    pass
class UML2WithID_ValuePin(InputPin, Element):

    pass
class UML2WithID_InteractionOccurrence(InteractionFragment, Element):

    pass
class UML2WithID_LiteralBoolean(LiteralSpecification, Element):

    pass
class UML2WithID_WriteVariableAction(VariableAction, Element):

    pass
class UML2WithID_DurationObservationAction(WriteStructuralFeatureAction, Element):

    pass
class UML2WithID_DataStoreNode(CentralBufferNode, Element):

    pass
class UML2WithID_Actor(Classifier, Element):

    pass
class UML2WithID_Enumeration(DataType, Element):

    pass
class UML2WithID_DurationInterval(Element, Interval):

    pass
class UML2WithID_Dependency(PackageableElement, Element):

    pass
class UML2WithID_Namespace(NamedElement, Element):

    pass
class UML2WithID_CombinedFragment(InteractionFragment, Element):

    pass
class UML2WithID_InformationItem(Classifier, Element):

    pass
class UML2WithID_Extension(Association, Element):

    pass
class UML2WithID_BehavioredClassifier(Classifier, Element):

    pass
class UML2WithID_Connector(Element, Feature):

    pass
class UML2WithID_ActivityEdge(RedefinableElement, Element):

    pass
class UML2WithID_TemplateableClassifier(Classifier, Element):

    pass
class UML2WithID_LiteralInteger(LiteralSpecification, Element):

    pass
class UML2WithID_Collaboration(StructuredClassifier, BehavioredClassifier, Element):

    pass
class UML2WithID_ActivityNode(RedefinableElement, Element):

    pass
class UML2WithID_ForkNode(ControlNode, Element):

    pass
class UML2WithID_ReadStructuralFeatureAction(StructuralFeatureAction, Element):

    pass
class UML2WithID_Abstraction(Dependency, Element):

    pass
class UML2WithID_Property(ConnectableElement, DeploymentTarget, StructuralFeature, Element):

    pass
class UML2WithID_Message(NamedElement, Element):

    pass
class UML2WithID_FinalState(Element, State):

    pass
class UML2WithID_Behavior(Class, Element):

    pass
class UML2WithID_DataType(Classifier, Element):

    pass
class UML2WithID_BroadcastSignalAction(InvocationAction, Element):

    pass
class UML2WithID_TimeInterval(Element, Interval):

    pass
class UML2WithID_Classifier(RedefinableElement, Type, Namespace, Element):

    pass
class UML2WithID_Expression(OpaqueExpression, Element):

    pass
class UML2WithID_Stereotype(Class, Element):

    pass
class UML2WithID_MergeNode(ControlNode, Element):

    pass
class UML2WithID_BehavioralFeature(Namespace, Element, Feature):

    pass
class UML2WithID_Pin(Element, ObjectNode):

    pass
class UML2WithID_InteractionFragment(NamedElement, Element):

    pass
class UML2WithID_Transition(RedefinableElement, Element):

    pass
class UML2WithID_Vertex(NamedElement, Element):

    pass
class UML2WithID_EventOccurrence(MessageEnd, InteractionFragment, Element):

    pass
class UML2WithID_ConnectableElement(NamedElement, Element):

    pass
class UML2WithID_LiteralUnlimitedNatural(LiteralSpecification, Element):

    pass
class UML2WithID_DeployedArtifact(NamedElement, Element):

    pass
class Action:

    pass
class UML2WithID_TestIdentityAction(Action, Element):

    pass
class UML2WithID_CreateObjectAction(Action, Element):

    pass
class UML2WithID_ApplyFunctionAction(Action, Element):

    pass
class UML2WithID_ReadSelfAction(Action, Element):

    pass
class UML2WithID_StartOwnedBehaviorAction(Element, Action):

    pass
class UML2WithID_VariableAction(Action, Element):

    pass
class UML2WithID_DestroyObjectAction(Action, Element):

    pass
class UML2WithID_StructuralFeatureAction(Action, Element):

    pass
class UML2WithID_LinkAction(Action, Element):

    pass
class UML2WithID_StructuredActivityNode(Namespace, Action, Element):

    pass
class UML2WithID_ReadIsClassifiedObjectAction(Element, Action):

    pass
class UML2WithID_ReadExtentAction(Element, Action):

    pass
class UML2WithID_ClearAssociationAction(Element, Action):

    pass
class UML2WithID_AcceptEventAction(Action, Element):

    pass
class UML2WithID_ReadLinkObjectEndAction(Action, Element):

    pass
class UML2WithID_ReclassifyObjectAction(Action, Element):

    pass
class UML2WithID_InvocationAction(Action, Element):

    pass
class UML2WithID_RaiseExceptionAction(Action, Element):

    pass
class UML2WithID_ReadLinkObjectEndQualifierAction(Element, Action):

    pass
class UML2WithID_ReplyAction(Action, Element):

    pass
class UML2WithID_Duration(ValueSpecification, Element):

    pass
class Trigger:

    pass
class UML2WithID_MessageTrigger(Element, Trigger):

    pass
class UML2WithID_TimeTrigger(Element, Trigger):

    pass
class UML2WithID_ChangeTrigger(Element, Trigger):

    pass
class Transition:

    pass
class UML2WithID_ProtocolTransition(Transition, Element):

    pass
class UML2WithID_EncapsulatedClassifier(StructuredClassifier, Element):

    pass
class UML2WithID_LiteralString(LiteralSpecification, Element):

    pass
class UML2WithID_FinalNode(ControlNode, Element):

    pass
class WriteLinkAction:

    pass
class UML2WithID_DestroyLinkAction(WriteLinkAction, Element):

    pass
class UML2WithID_CreateLinkAction(WriteLinkAction, Element):

    pass
class UML2WithID_Realization(Abstraction, Element):

    pass
class UML2WithID_AnyTrigger(Element, MessageTrigger):

    pass
class UML2WithID_Activity(Behavior, Element):

    pass