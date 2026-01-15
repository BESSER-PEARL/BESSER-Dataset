from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class EncapsulatedClassifier:

    pass
class Transition:

    pass
class AcceptEventAction:

    pass
class UML2WithID_Element(ABC):

    def __init__(self, ID: str, UML2WithID_Element: "UML2WithID_Element" = None, UML2WithID_Element0: "UML2WithID_Element" = None):
        self.ID = ID
        self.UML2WithID_Element = UML2WithID_Element
        self.UML2WithID_Element0 = UML2WithID_Element0
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def UML2WithID_Element0(self):
        return self.__UML2WithID_Element0

    @UML2WithID_Element0.setter
    def UML2WithID_Element0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Element__UML2WithID_Element0", None)
        self.__UML2WithID_Element0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Element"):
                opp_val = getattr(old_value, "UML2WithID_Element", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_Element", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Element"):
                opp_val = getattr(value, "UML2WithID_Element", None)
                setattr(value, "UML2WithID_Element", self)

    @property
    def UML2WithID_Element(self):
        return self.__UML2WithID_Element

    @UML2WithID_Element.setter
    def UML2WithID_Element(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2WithID_Element__UML2WithID_Element", None)
        self.__UML2WithID_Element = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2WithID_Element0"):
                opp_val = getattr(old_value, "UML2WithID_Element0", None)
                if opp_val == self:
                    setattr(old_value, "UML2WithID_Element0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2WithID_Element0"):
                opp_val = getattr(value, "UML2WithID_Element0", None)
                setattr(value, "UML2WithID_Element0", self)

class State:

    pass
class Artifact:

    pass
class InputPin:

    pass
class Constraint:

    pass
class ActivityGroup:

    pass
class CreateLinkAction:

    pass
class StructuralFeature:

    pass
class DataType:

    pass
class Relationship:

    pass
class InvocationAction:

    pass
class InstanceSpecification:

    pass
class StructuralFeatureAction:

    pass
class Node:

    pass
class StructuredClassifier:

    pass
class ExecutableNode:

    pass
class BehavioredClassifier:

    pass
class StructuredActivityNode:

    pass
class Realization:

    pass
class PackageImport:

    pass
class Type:

    pass
class LinkEndData:

    pass
class Dependency:

    pass
class EventOccurrence:

    pass
class ValueSpecification:

    pass
class CentralBufferNode:

    pass
class VariableAction:

    pass
class Abstraction:

    pass
class ConnectableElement:

    pass
class Feature:

    pass
class Association:

    pass
class TemplateParameter:

    pass
class IntervalConstraint:

    pass
class WriteStructuralFeatureAction:

    pass
class StateMachine:

    pass
class MessageTrigger:

    pass
class OpaqueExpression:

    pass
class InteractionFragment:

    pass
class Behavior:

    pass
class Trigger:

    pass
class ParameterableElement:

    pass
class DirectedRelationship:

    pass
class DeploymentTarget:

    pass
class PackageableElement:

    pass
class Class:

    pass
class ActivityNode:

    pass
class Vertex:

    pass
class Namespace:

    pass
class TemplateSignature:

    pass
class Interval:

    pass
class Pin:

    pass
class Property:

    pass
class ObjectNode:

    pass
class LinkAction:

    pass
class Action:

    pass
class CallAction:

    pass
class InteractionOccurrence:

    pass
class ControlNode:

    pass
class DeployedArtifact:

    pass
class Classifier:

    pass
class NamedElement:

    pass
class MultiplicityElement:

    pass
class TypedElement:

    pass
class BehavioralFeature:

    pass
class FinalNode:

    pass
class WriteLinkAction:

    pass
class LiteralSpecification:

    pass
class WriteVariableAction:

    pass
class TemplateableElement:

    pass
class Package:

    pass
class ActivityEdge:

    pass
class RedefinableElement:

    pass
class Element:

    pass
class UML2WithID_ConnectableElementTemplateParameter(TemplateParameter, Element):

    pass
class UML2WithID_GeneralizationSet(PackageableElement, Element):

    pass
class UML2WithID_UseCase(BehavioredClassifier, Element):

    pass
class UML2WithID_InteractionConstraint(Constraint, Element):

    pass
class UML2WithID_OutputPin(Pin, Element):

    pass
class UML2WithID_Connector(Element, Feature):

    pass
class UML2WithID_ObjectNode(Element, TypedElement, ActivityNode):

    pass
class UML2WithID_Collaboration(StructuredClassifier, BehavioredClassifier, Element):

    pass
class UML2WithID_CallBehaviorAction(CallAction, Element):

    pass
class UML2WithID_TypedElement(NamedElement, Element):

    pass
class UML2WithID_DeploymentTarget(NamedElement, Element):

    pass
class UML2WithID_PackageableElement(NamedElement, ParameterableElement, Element):

    pass
class UML2WithID_ActivityGroup(Element):

    pass
class UML2WithID_SendSignalAction(InvocationAction, Element):

    pass
class UML2WithID_CollaborationOccurrence(NamedElement, Element):

    pass
class UML2WithID_ActivityNode(RedefinableElement, Element):

    pass
class UML2WithID_Pseudostate(Vertex, Element):

    pass
class UML2WithID_Interaction(Behavior, InteractionFragment, Element):

    pass
class UML2WithID_BehavioralFeature(Namespace, Feature, Element):

    pass
class UML2WithID_ExtensionPoint(RedefinableElement, Element):

    pass
class UML2WithID_ActivityPartition(NamedElement, ActivityGroup, Element):

    pass
class UML2WithID_StartOwnedBehaviorAction(Action, Element):

    pass
class UML2WithID_MultiplicityElement(Element):

    pass
class UML2WithID_ReadIsClassifiedObjectAction(Action, Element):

    pass
class UML2WithID_Manifestation(Abstraction, Element):

    pass
class UML2WithID_Duration(ValueSpecification, Element):

    pass
class UML2WithID_AddVariableValueAction(WriteVariableAction, Element):

    pass
class UML2WithID_Clause(Element):

    pass
class UML2WithID_TestIdentityAction(Action, Element):

    pass
class UML2WithID_WriteLinkAction(LinkAction, Element):

    pass
class UML2WithID_ConnectorEnd(MultiplicityElement, Element):

    pass
class UML2WithID_ReadLinkAction(Element, LinkAction):

    pass
class UML2WithID_ElementImport(DirectedRelationship, Element):

    pass
class UML2WithID_ConnectionPointReference(Vertex, Element):

    pass
class UML2WithID_Relationship(Element):

    pass
class UML2WithID_ValueSpecification(ParameterableElement, TypedElement, Element):

    pass
class UML2WithID_NamedElement(TemplateableElement, Element):

    pass
class UML2WithID_Pin(Element, MultiplicityElement, ObjectNode):

    pass
class UML2WithID_EnumerationLiteral(InstanceSpecification, Element):

    pass
class UML2WithID_Action(ExecutableNode, Element):

    pass
class UML2WithID_InteractionFragment(NamedElement, Element):

    pass
class UML2WithID_BroadcastSignalAction(InvocationAction, Element):

    pass
class UML2WithID_ParameterableElement(Element):

    pass
class UML2WithID_QualifierValue(Element):

    pass
class UML2WithID_LiteralSpecification(ValueSpecification, Element):

    pass
class UML2WithID_DirectedRelationship(Relationship, Element):

    pass
class UML2WithID_Reception(BehavioralFeature, Element):

    pass
class UML2WithID_InputPin(Pin, Element):

    pass
class UML2WithID_AddStructuralFeatureValueAction(WriteStructuralFeatureAction, Element):

    pass
class UML2WithID_ActivityParameterNode(ObjectNode, Element):

    pass
class UML2WithID_ForkNode(Element, ControlNode):

    pass
class UML2WithID_StateMachine(Behavior, Element):

    pass
class UML2WithID_Feature(RedefinableElement, Element):

    pass
class UML2WithID_InstanceValue(ValueSpecification, Element):

    pass
class UML2WithID_ReadStructuralFeatureAction(StructuralFeatureAction, Element):

    pass
class UML2WithID_StructuredActivityNode(ActivityGroup, Namespace, Action, Element):

    pass
class UML2WithID_Stereotype(Class, Element):

    pass
class UML2WithID_Generalization(DirectedRelationship, Element):

    pass
class UML2WithID_Deployment(Dependency, Element):

    pass
class UML2WithID_Comment(TemplateableElement, Element):

    pass
class UML2WithID_Extend(NamedElement, DirectedRelationship, Element):

    pass
class UML2WithID_MessageEnd(NamedElement, Element):

    pass
class UML2WithID_ConnectableElement(ParameterableElement, NamedElement, Element):

    pass
class UML2WithID_AcceptCallAction(AcceptEventAction, Element):

    pass
class UML2WithID_PrimitiveType(DataType, Element):

    pass
class UML2WithID_StateInvariant(InteractionFragment, Element):

    pass
class UML2WithID_DeployedArtifact(NamedElement, Element):

    pass
class UML2WithID_Permission(Dependency, Element):

    pass
class UML2WithID_ControlNode(ActivityNode, Element):

    pass
class UML2WithID_TimeTrigger(Trigger, Element):

    pass
class UML2WithID_ValuePin(InputPin, Element):

    pass
class UML2WithID_ReplyAction(Action, Element):

    pass
class UML2WithID_State(Vertex, Namespace, RedefinableElement, Element):

    pass
class UML2WithID_Transition(RedefinableElement, Element):

    pass
class UML2WithID_ObjectFlow(ActivityEdge, Element):

    pass
class UML2WithID_ClearAssociationAction(Action, Element):

    pass
class UML2WithID_Stop(EventOccurrence, Element):

    pass
class UML2WithID_Parameter(TypedElement, MultiplicityElement, ConnectableElement, Element):

    pass
class UML2WithID_LiteralBoolean(LiteralSpecification, Element):

    pass
class UML2WithID_ExecutionEnvironment(Element, Node):

    pass
class UML2WithID_ActivityEdge(RedefinableElement, Element):

    pass
class UML2WithID_ParameterableClassifier(Classifier, Element):

    pass
class UML2WithID_ProtocolConformance(DirectedRelationship, Element):

    pass
class UML2WithID_InstanceSpecification(DeploymentTarget, PackageableElement, DeployedArtifact, Element):

    pass
class UML2WithID_OperationTemplateParameter(TemplateParameter, Element):

    pass
class UML2WithID_IntervalConstraint(Constraint, Element):

    pass
class UML2WithID_Port(Property, Element):

    pass
class UML2WithID_InformationFlow(DirectedRelationship, PackageableElement, Element):

    pass
class UML2WithID_AnyTrigger(Element, MessageTrigger):

    pass
class UML2WithID_Abstraction(Dependency, Element):

    pass
class UML2WithID_Substitution(Element, Realization):

    pass
class UML2WithID_CommunicationPath(Association, Element):

    pass
class UML2WithID_Node(DeploymentTarget, Class, Element):

    pass
class UML2WithID_TimeExpression(ValueSpecification, Element):

    pass
class UML2WithID_InvocationAction(Action, Element):

    pass
class UML2WithID_StructuralFeatureAction(Action, Element):

    pass
class UML2WithID_CombinedFragment(InteractionFragment, Element):

    pass
class UML2WithID_Continuation(InteractionFragment, Element):

    pass
class UML2WithID_CreateLinkObjectAction(CreateLinkAction, Element):

    pass
class UML2WithID_BehavioredClassifier(Classifier, Element):

    pass
class UML2WithID_Interface(Classifier, Element):

    pass
class UML2WithID_DataStoreNode(CentralBufferNode, Element):

    pass
class UML2WithID_StringExpression(TemplateableElement, Element):

    pass
class UML2WithID_ReadLinkObjectEndAction(Action, Element):

    pass
class UML2WithID_ExecutableNode(Element, ActivityNode):

    pass
class UML2WithID_VariableAction(Action, Element):

    pass
class UML2WithID_ProtocolStateMachine(StateMachine, Element):

    pass
class UML2WithID_PartDecomposition(InteractionOccurrence, Element):

    pass
class UML2WithID_FinalNode(Element, ControlNode):

    pass
class UML2WithID_Usage(Dependency, Element):

    pass
class UML2WithID_Interval(ValueSpecification, Element):

    pass
class UML2WithID_InteractionOperand(Namespace, InteractionFragment, Element):

    pass
class UML2WithID_AssociationClass(Association, Class, Element):

    pass
class UML2WithID_ApplyFunctionAction(Action, Element):

    pass
class UML2WithID_Namespace(NamedElement, Element):

    pass
class UML2WithID_RemoveVariableValueAction(WriteVariableAction, Element):

    pass
class UML2WithID_Constraint(PackageableElement, Element):

    pass
class UML2WithID_Device(Element, Node):

    pass
class UML2WithID_CallTrigger(MessageTrigger, Element):

    pass
class UML2WithID_Type(PackageableElement, Element):

    pass
class UML2WithID_InteractionOccurrence(InteractionFragment, Element):

    pass
class UML2WithID_LinkEndCreationData(LinkEndData, Element):

    pass
class UML2WithID_Behavior(Class, Element):

    pass
class UML2WithID_TemplateableClassifier(Classifier, Element):

    pass
class UML2WithID_Variable(TypedElement, MultiplicityElement, ConnectableElement, Element):

    pass
class UML2WithID_Signal(Classifier, Element):

    pass
class UML2WithID_TimeConstraint(IntervalConstraint, Element):

    pass
class UML2WithID_ClassifierTemplateParameter(TemplateParameter, Element):

    pass
class UML2WithID_Classifier(Namespace, Type, RedefinableElement, Element):

    pass
class UML2WithID_ExceptionHandler(Element):

    pass
class UML2WithID_ConditionalNode(StructuredActivityNode, Element):

    pass
class UML2WithID_DurationObservationAction(WriteStructuralFeatureAction, Element):

    pass
class UML2WithID_CentralBufferNode(ObjectNode, Element):

    pass
class UML2WithID_PackageImport(DirectedRelationship, Element):

    pass
class UML2WithID_TemplateableElement(Element):

    pass
class UML2WithID_CallOperationAction(CallAction, Element):

    pass
class UML2WithID_Extension(Association, Element):

    pass
class UML2WithID_Model(Package, Element):

    pass
class UML2WithID_Message(NamedElement, Element):

    pass
class UML2WithID_WriteStructuralFeatureAction(StructuralFeatureAction, Element):

    pass
class UML2WithID_LiteralInteger(LiteralSpecification, Element):

    pass
class UML2WithID_DecisionNode(Element, ControlNode):

    pass
class UML2WithID_WriteVariableAction(VariableAction, Element):

    pass
class UML2WithID_ReadSelfAction(Action, Element):

    pass
class UML2WithID_ProtocolTransition(Transition, Element):

    pass
class UML2WithID_MessageTrigger(Trigger, Element):

    pass
class UML2WithID_Profile(Package, Element):

    pass
class UML2WithID_DeploymentSpecification(Artifact, Element):

    pass
class UML2WithID_Lifeline(NamedElement, Element):

    pass
class UML2WithID_LiteralNull(LiteralSpecification, Element):

    pass
class UML2WithID_MergeNode(ControlNode, Element):

    pass
class UML2WithID_SendObjectAction(InvocationAction, Element):

    pass
class UML2WithID_DestroyObjectAction(Action, Element):

    pass
class UML2WithID_StructuredClassifier(Classifier, Element):

    pass
class UML2WithID_ClearVariableAction(Element, VariableAction):

    pass
class UML2WithID_DurationConstraint(IntervalConstraint, Element):

    pass
class UML2WithID_ExecutionOccurrence(InteractionFragment, Element):

    pass
class UML2WithID_Component(Class, Element):

    pass
class UML2WithID_ChangeTrigger(Trigger, Element):

    pass
class UML2WithID_RedefinableElement(NamedElement, Element):

    pass
class UML2WithID_InterruptibleActivityRegion(ActivityGroup, Element):

    pass
class UML2WithID_TemplateParameterSubstitution(Element):

    pass
class UML2WithID_ProfileApplication(PackageImport, Element):

    pass
class UML2WithID_LinkEndData(Element):

    pass
class UML2WithID_RedefinableTemplateSignature(TemplateSignature, RedefinableElement, Element):

    pass
class UML2WithID_PrimitiveFunction(PackageableElement, Element):

    pass
class UML2WithID_TemplateParameter(Element):

    pass
class UML2WithID_GeneralOrdering(NamedElement, Element):

    pass
class UML2WithID_TemplateBinding(DirectedRelationship, Element):

    pass
class UML2WithID_CreateObjectAction(Action, Element):

    pass
class UML2WithID_Association(Classifier, Relationship, Element):

    pass
class UML2WithID_Package(PackageableElement, Namespace, Element):

    pass
class UML2WithID_ReclassifyObjectAction(Action, Element):

    pass
class UML2WithID_EncapsulatedClassifier(StructuredClassifier, Element):

    pass
class UML2WithID_JoinNode(Element, ControlNode):

    pass
class UML2WithID_DataType(Classifier, Element):

    pass
class UML2WithID_AcceptEventAction(Action, Element):

    pass
class UML2WithID_PackageMerge(DirectedRelationship, Element):

    pass
class UML2WithID_InitialNode(Element, ControlNode):

    pass
class UML2WithID_RaiseExceptionAction(Action, Element):

    pass
class UML2WithID_Enumeration(DataType, Element):

    pass
class UML2WithID_LinkAction(Action, Element):

    pass
class UML2WithID_Artifact(Classifier, DeployedArtifact, Element):

    pass
class UML2WithID_ExpansionNode(ObjectNode, Element):

    pass
class UML2WithID_ControlFlow(ActivityEdge, Element):

    pass
class UML2WithID_StructuralFeature(Element, MultiplicityElement, Feature, TypedElement):

    pass
class UML2WithID_TimeObservationAction(WriteStructuralFeatureAction, Element):

    pass
class UML2WithID_ReadLinkObjectEndQualifierAction(Action, Element):

    pass
class UML2WithID_ExpansionRegion(StructuredActivityNode, Element):

    pass
class UML2WithID_DestroyLinkAction(WriteLinkAction, Element):

    pass
class UML2WithID_TimeInterval(Interval, Element):

    pass
class UML2WithID_Expression(OpaqueExpression, Element):

    pass
class UML2WithID_Region(Namespace, RedefinableElement, Element):

    pass
class UML2WithID_CallAction(InvocationAction, Element):

    pass
class UML2WithID_LoopNode(StructuredActivityNode, Element):

    pass
class UML2WithID_Operation(MultiplicityElement, ParameterableElement, TypedElement, Element, BehavioralFeature):

    pass
class UML2WithID_SignalTrigger(MessageTrigger, Element):

    pass
class UML2WithID_RemoveStructuralFeatureValueAction(WriteStructuralFeatureAction, Element):

    pass
class UML2WithID_Property(StructuralFeature, DeploymentTarget, ConnectableElement, Element):

    pass
class UML2WithID_InformationItem(Classifier, Element):

    pass
class UML2WithID_Implementation(Realization, Element):

    pass
class UML2WithID_Actor(Classifier, Element):

    pass
class UML2WithID_DurationInterval(Interval, Element):

    pass
class UML2WithID_Include(NamedElement, DirectedRelationship, Element):

    pass
class UML2WithID_ReadVariableAction(Element, VariableAction):

    pass
class UML2WithID_Trigger(NamedElement, Element):

    pass
class UML2WithID_LiteralUnlimitedNatural(LiteralSpecification, Element):

    pass
class UML2WithID_Activity(Behavior, Element):

    pass
class UML2WithID_ActivityFinalNode(FinalNode, Element):

    pass
class UML2WithID_FinalState(Element, State):

    pass
class UML2WithID_ExtensionEnd(Property, Element):

    pass
class UML2WithID_Vertex(NamedElement, Element):

    pass
class UML2WithID_LiteralString(LiteralSpecification, Element):

    pass
class UML2WithID_FlowFinalNode(FinalNode, Element):

    pass
class UML2WithID_Slot(Element):

    pass
class UML2WithID_OpaqueExpression(ValueSpecification, Element):

    pass
class UML2WithID_ReadExtentAction(Action, Element):

    pass
class UML2WithID_Realization(Abstraction, Element):

    pass
class UML2WithID_ClearStructuralFeatureAction(StructuralFeatureAction, Element):

    pass
class UML2WithID_CreateLinkAction(WriteLinkAction, Element):

    pass
class UML2WithID_Class(EncapsulatedClassifier, BehavioredClassifier, Element):

    pass
class UML2WithID_Dependency(PackageableElement, DirectedRelationship, Element):

    pass
class UML2WithID_TemplateSignature(Element):

    pass
class UML2WithID_ParameterSet(NamedElement, Element):

    pass
class MessageEnd:

    pass
class UML2WithID_EventOccurrence(InteractionFragment, MessageEnd, Element):

    pass
class UML2WithID_Gate(MessageEnd, Element):

    pass