from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class LinkAction:

    pass
class InteractionOccurrence:

    pass
class AcceptEventAction:

    pass
class Property:

    pass
class PackageImport:

    pass
class Realization:

    pass
class TemplateParameter:

    pass
class Feature:

    pass
class DataType:

    pass
class CreateLinkAction:

    pass
class InvocationAction:

    pass
class MessageEnd:

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

class Abstraction:

    pass
class TemplateSignature:

    pass
class MessageTrigger:

    pass
class LiteralSpecification:

    pass
class Pin:

    pass
class VariableAction:

    pass
class EncapsulatedClassifier:

    pass
class IntervalConstraint:

    pass
class OpaqueExpression:

    pass
class WriteVariableAction:

    pass
class InstanceSpecification:

    pass
class ExecutableNode:

    pass
class State:

    pass
class DeployedArtifact:

    pass
class Transition:

    pass
class Trigger:

    pass
class TemplateableElement:

    pass
class FinalNode:

    pass
class Relationship:

    pass
class WriteStructuralFeatureAction:

    pass
class StructuredActivityNode:

    pass
class LinkEndData:

    pass
class Association:

    pass
class Class:

    pass
class Constraint:

    pass
class Node:

    pass
class Action:

    pass
class Vertex:

    pass
class ActivityGroup:

    pass
class NamedElement:

    pass
class PackageableElement:

    pass
class Interval:

    pass
class RedefinableElement:

    pass
class Type:

    pass
class Namespace:

    pass
class StructuralFeatureAction:

    pass
class Classifier:

    pass
class ParameterableElement:

    pass
class MultiplicityElement:

    pass
class TypedElement:

    pass
class BehavioralFeature:

    pass
class ObjectNode:

    pass
class BehavioredClassifier:

    pass
class CallAction:

    pass
class DeploymentTarget:

    pass
class ConnectableElement:

    pass
class StructuralFeature:

    pass
class StructuredClassifier:

    pass
class ActivityEdge:

    pass
class ValueSpecification:

    pass
class WriteLinkAction:

    pass
class Artifact:

    pass
class StateMachine:

    pass
class DirectedRelationship:

    pass
class ControlNode:

    pass
class Package:

    pass
class EventOccurrence:

    pass
class CentralBufferNode:

    pass
class Behavior:

    pass
class InteractionFragment:

    pass
class Element:

    pass
class UML2WithID_Port(Property, Element):

    pass
class UML2WithID_OpaqueExpression(ValueSpecification, Element):

    pass
class UML2WithID_Expression(OpaqueExpression, Element):

    pass
class UML2WithID_TestIdentityAction(Action, Element):

    pass
class UML2WithID_Namespace(Element, NamedElement):

    pass
class UML2WithID_Package(Namespace, PackageableElement, Element):

    pass
class UML2WithID_AnyTrigger(MessageTrigger, Element):

    pass
class UML2WithID_ActivityFinalNode(FinalNode, Element):

    pass
class UML2WithID_Operation(ParameterableElement, MultiplicityElement, BehavioralFeature, Element, TypedElement):

    pass
class UML2WithID_MergeNode(ControlNode, Element):

    pass
class UML2WithID_Collaboration(StructuredClassifier, Element, BehavioredClassifier):

    pass
class UML2WithID_TemplateParameter(Element):

    pass
class UML2WithID_MessageEnd(Element, NamedElement):

    pass
class UML2WithID_CallTrigger(MessageTrigger, Element):

    pass
class UML2WithID_RedefinableElement(NamedElement, Element):

    pass
class UML2WithID_Parameter(MultiplicityElement, TypedElement, ConnectableElement, Element):

    pass
class UML2WithID_Node(Element, Class, DeploymentTarget):

    pass
class UML2WithID_ProtocolStateMachine(StateMachine, Element):

    pass
class UML2WithID_TemplateableClassifier(Classifier, Element):

    pass
class UML2WithID_Model(Package, Element):

    pass
class UML2WithID_ObjectFlow(ActivityEdge, Element):

    pass
class UML2WithID_ReadStructuralFeatureAction(StructuralFeatureAction, Element):

    pass
class UML2WithID_TemplateBinding(DirectedRelationship, Element):

    pass
class UML2WithID_ExpansionNode(Element, ObjectNode):

    pass
class UML2WithID_InputPin(Pin, Element):

    pass
class UML2WithID_ReadExtentAction(Action, Element):

    pass
class UML2WithID_Actor(Classifier, Element):

    pass
class UML2WithID_Association(Classifier, Relationship, Element):

    pass
class UML2WithID_Extension(Association, Element):

    pass
class UML2WithID_PrimitiveType(Element, DataType):

    pass
class UML2WithID_InstanceValue(ValueSpecification, Element):

    pass
class UML2WithID_GeneralOrdering(Element, NamedElement):

    pass
class UML2WithID_ElementImport(DirectedRelationship, Element):

    pass
class UML2WithID_TimeTrigger(Trigger, Element):

    pass
class UML2WithID_RemoveVariableValueAction(WriteVariableAction, Element):

    pass
class UML2WithID_AssociationClass(Association, Class, Element):

    pass
class UML2WithID_Interface(Classifier, Element):

    pass
class UML2WithID_EncapsulatedClassifier(StructuredClassifier, Element):

    pass
class UML2WithID_Enumeration(DataType, Element):

    pass
class UML2WithID_State(Vertex, RedefinableElement, Namespace, Element):

    pass
class UML2WithID_Message(Element, NamedElement):

    pass
class UML2WithID_Region(Namespace, RedefinableElement, Element):

    pass
class UML2WithID_ApplyFunctionAction(Action, Element):

    pass
class UML2WithID_AcceptCallAction(AcceptEventAction, Element):

    pass
class UML2WithID_ClearAssociationAction(Action, Element):

    pass
class UML2WithID_CommunicationPath(Association, Element):

    pass
class UML2WithID_Duration(ValueSpecification, Element):

    pass
class UML2WithID_ParameterSet(NamedElement, Element):

    pass
class UML2WithID_EnumerationLiteral(InstanceSpecification, Element):

    pass
class UML2WithID_Manifestation(Abstraction, Element):

    pass
class UML2WithID_RaiseExceptionAction(Action, Element):

    pass
class UML2WithID_Activity(Behavior, Element):

    pass
class UML2WithID_ForkNode(ControlNode, Element):

    pass
class UML2WithID_Vertex(Element, NamedElement):

    pass
class UML2WithID_DestroyLinkAction(WriteLinkAction, Element):

    pass
class UML2WithID_WriteVariableAction(VariableAction, Element):

    pass
class UML2WithID_OperationTemplateParameter(TemplateParameter, Element):

    pass
class UML2WithID_Class(Element, EncapsulatedClassifier, BehavioredClassifier):

    pass
class UML2WithID_ParameterableClassifier(Classifier, Element):

    pass
class UML2WithID_PrimitiveFunction(PackageableElement, Element):

    pass
class UML2WithID_OutputPin(Pin, Element):

    pass
class UML2WithID_Implementation(Realization, Element):

    pass
class UML2WithID_InteractionConstraint(Constraint, Element):

    pass
class UML2WithID_ReadLinkAction(LinkAction, Element):

    pass
class UML2WithID_Gate(MessageEnd, Element):

    pass
class UML2WithID_JoinNode(ControlNode, Element):

    pass
class UML2WithID_Interaction(InteractionFragment, Behavior, Element):

    pass
class UML2WithID_WriteLinkAction(LinkAction, Element):

    pass
class UML2WithID_InteractionOccurrence(InteractionFragment, Element):

    pass
class UML2WithID_StateMachine(Behavior, Element):

    pass
class UML2WithID_LiteralString(LiteralSpecification, Element):

    pass
class UML2WithID_Variable(MultiplicityElement, TypedElement, ConnectableElement, Element):

    pass
class UML2WithID_ReplyAction(Action, Element):

    pass
class UML2WithID_ReclassifyObjectAction(Action, Element):

    pass
class UML2WithID_NamedElement(TemplateableElement, Element):

    pass
class UML2WithID_RedefinableTemplateSignature(RedefinableElement, TemplateSignature, Element):

    pass
class UML2WithID_Pseudostate(Vertex, Element):

    pass
class UML2WithID_ConnectableElement(ParameterableElement, Element, NamedElement):

    pass
class UML2WithID_TemplateableElement(Element):

    pass
class UML2WithID_StartOwnedBehaviorAction(Action, Element):

    pass
class UML2WithID_Component(Class, Element):

    pass
class UML2WithID_TimeConstraint(IntervalConstraint, Element):

    pass
class UML2WithID_CreateObjectAction(Action, Element):

    pass
class UML2WithID_Continuation(InteractionFragment, Element):

    pass
class UML2WithID_ConditionalNode(StructuredActivityNode, Element):

    pass
class UML2WithID_DeploymentTarget(NamedElement, Element):

    pass
class UML2WithID_ReadVariableAction(VariableAction, Element):

    pass
class UML2WithID_Constraint(PackageableElement, Element):

    pass
class UML2WithID_StructuralFeatureAction(Action, Element):

    pass
class UML2WithID_ConnectorEnd(MultiplicityElement, Element):

    pass
class UML2WithID_Lifeline(Element, NamedElement):

    pass
class UML2WithID_BroadcastSignalAction(InvocationAction, Element):

    pass
class UML2WithID_DeployedArtifact(Element, NamedElement):

    pass
class UML2WithID_QualifierValue(Element):

    pass
class UML2WithID_Artifact(Classifier, DeployedArtifact, Element):

    pass
class UML2WithID_FinalState(State, Element):

    pass
class UML2WithID_ReadLinkObjectEndQualifierAction(Action, Element):

    pass
class UML2WithID_PackageMerge(DirectedRelationship, Element):

    pass
class UML2WithID_TimeExpression(ValueSpecification, Element):

    pass
class UML2WithID_VariableAction(Action, Element):

    pass
class UML2WithID_CollaborationOccurrence(Element, NamedElement):

    pass
class UML2WithID_InstanceSpecification(PackageableElement, DeployedArtifact, DeploymentTarget, Element):

    pass
class UML2WithID_Clause(Element):

    pass
class UML2WithID_Pin(MultiplicityElement, ObjectNode, Element):

    pass
class UML2WithID_ProfileApplication(PackageImport, Element):

    pass
class UML2WithID_DestroyObjectAction(Action, Element):

    pass
class UML2WithID_LinkEndData(Element):

    pass
class UML2WithID_InformationItem(Classifier, Element):

    pass
class UML2WithID_ValueSpecification(ParameterableElement, TypedElement, Element):

    pass
class UML2WithID_ProtocolConformance(DirectedRelationship, Element):

    pass
class UML2WithID_AddStructuralFeatureValueAction(WriteStructuralFeatureAction, Element):

    pass
class UML2WithID_CreateLinkObjectAction(CreateLinkAction, Element):

    pass
class UML2WithID_ExtensionEnd(Property, Element):

    pass
class UML2WithID_Relationship(Element):

    pass
class UML2WithID_InvocationAction(Action, Element):

    pass
class UML2WithID_LinkEndCreationData(LinkEndData, Element):

    pass
class UML2WithID_WriteStructuralFeatureAction(StructuralFeatureAction, Element):

    pass
class UML2WithID_StructuralFeature(MultiplicityElement, TypedElement, Feature, Element):

    pass
class UML2WithID_AddVariableValueAction(WriteVariableAction, Element):

    pass
class UML2WithID_InformationFlow(DirectedRelationship, PackageableElement, Element):

    pass
class UML2WithID_Generalization(DirectedRelationship, Element):

    pass
class UML2WithID_ActivityEdge(RedefinableElement, Element):

    pass
class UML2WithID_LiteralUnlimitedNatural(LiteralSpecification, Element):

    pass
class UML2WithID_ConnectionPointReference(Vertex, Element):

    pass
class UML2WithID_InterruptibleActivityRegion(ActivityGroup, Element):

    pass
class UML2WithID_LoopNode(StructuredActivityNode, Element):

    pass
class UML2WithID_Substitution(Realization, Element):

    pass
class UML2WithID_BehavioralFeature(Namespace, Element, Feature):

    pass
class UML2WithID_Dependency(DirectedRelationship, PackageableElement, Element):

    pass
class UML2WithID_Stop(EventOccurrence, Element):

    pass
class UML2WithID_Action(ExecutableNode, Element):

    pass
class UML2WithID_BehavioredClassifier(Classifier, Element):

    pass
class UML2WithID_ConnectableElementTemplateParameter(TemplateParameter, Element):

    pass
class UML2WithID_EventOccurrence(MessageEnd, InteractionFragment, Element):

    pass
class UML2WithID_Connector(Feature, Element):

    pass
class UML2WithID_SendSignalAction(InvocationAction, Element):

    pass
class UML2WithID_StateInvariant(InteractionFragment, Element):

    pass
class UML2WithID_Classifier(Namespace, RedefinableElement, Type, Element):

    pass
class UML2WithID_ReadLinkObjectEndAction(Action, Element):

    pass
class UML2WithID_DurationConstraint(IntervalConstraint, Element):

    pass
class UML2WithID_ClearStructuralFeatureAction(StructuralFeatureAction, Element):

    pass
class UML2WithID_FinalNode(ControlNode, Element):

    pass
class UML2WithID_ExceptionHandler(Element):

    pass
class UML2WithID_Stereotype(Class, Element):

    pass
class UML2WithID_ReadSelfAction(Action, Element):

    pass
class UML2WithID_ActivityGroup(Element):

    pass
class UML2WithID_SendObjectAction(InvocationAction, Element):

    pass
class UML2WithID_CallOperationAction(CallAction, Element):

    pass
class UML2WithID_MessageTrigger(Trigger, Element):

    pass
class UML2WithID_Include(DirectedRelationship, NamedElement, Element):

    pass
class UML2WithID_AcceptEventAction(Action, Element):

    pass
class UML2WithID_Signal(Classifier, Element):

    pass
class UML2WithID_TimeInterval(Interval, Element):

    pass
class UML2WithID_StructuredClassifier(Classifier, Element):

    pass
class UML2WithID_MultiplicityElement(Element):

    pass
class UML2WithID_ClassifierTemplateParameter(TemplateParameter, Element):

    pass
class UML2WithID_CallAction(InvocationAction, Element):

    pass
class UML2WithID_LiteralBoolean(LiteralSpecification, Element):

    pass
class UML2WithID_Interval(ValueSpecification, Element):

    pass
class UML2WithID_ChangeTrigger(Trigger, Element):

    pass
class UML2WithID_GeneralizationSet(PackageableElement, Element):

    pass
class UML2WithID_CentralBufferNode(ObjectNode, Element):

    pass
class UML2WithID_Extend(DirectedRelationship, Element, NamedElement):

    pass
class UML2WithID_ExtensionPoint(RedefinableElement, Element):

    pass
class UML2WithID_LiteralNull(LiteralSpecification, Element):

    pass
class UML2WithID_StructuredActivityNode(ActivityGroup, Namespace, Action, Element):

    pass
class UML2WithID_FlowFinalNode(FinalNode, Element):

    pass
class UML2WithID_LiteralSpecification(ValueSpecification, Element):

    pass
class UML2WithID_UseCase(Element, BehavioredClassifier):

    pass
class UML2WithID_Comment(Element, TemplateableElement):

    pass
class UML2WithID_ExpansionRegion(StructuredActivityNode, Element):

    pass
class UML2WithID_Trigger(NamedElement, Element):

    pass
class UML2WithID_IntervalConstraint(Constraint, Element):

    pass
class UML2WithID_Behavior(Class, Element):

    pass
class UML2WithID_ControlFlow(ActivityEdge, Element):

    pass
class UML2WithID_CallBehaviorAction(CallAction, Element):

    pass
class UML2WithID_ClearVariableAction(VariableAction, Element):

    pass
class UML2WithID_ExecutionOccurrence(InteractionFragment, Element):

    pass
class UML2WithID_PackageImport(DirectedRelationship, Element):

    pass
class UML2WithID_ActivityNode(RedefinableElement, Element):

    pass
class UML2WithID_ParameterableElement(Element):

    pass
class UML2WithID_LinkAction(Action, Element):

    pass
class UML2WithID_ExecutionEnvironment(Node, Element):

    pass
class UML2WithID_Type(PackageableElement, Element):

    pass
class UML2WithID_CreateLinkAction(WriteLinkAction, Element):

    pass
class UML2WithID_CombinedFragment(InteractionFragment, Element):

    pass
class UML2WithID_ReadIsClassifiedObjectAction(Action, Element):

    pass
class UML2WithID_DataStoreNode(CentralBufferNode, Element):

    pass
class UML2WithID_TimeObservationAction(WriteStructuralFeatureAction, Element):

    pass
class UML2WithID_PartDecomposition(InteractionOccurrence, Element):

    pass
class UML2WithID_ActivityPartition(ActivityGroup, Element, NamedElement):

    pass
class UML2WithID_DataType(Classifier, Element):

    pass
class UML2WithID_DurationObservationAction(WriteStructuralFeatureAction, Element):

    pass
class UML2WithID_Transition(RedefinableElement, Element):

    pass
class UML2WithID_PackageableElement(ParameterableElement, NamedElement, Element):

    pass
class UML2WithID_ProtocolTransition(Element, Transition):

    pass
class UML2WithID_Device(Node, Element):

    pass
class UML2WithID_RemoveStructuralFeatureValueAction(WriteStructuralFeatureAction, Element):

    pass
class UML2WithID_SignalTrigger(MessageTrigger, Element):

    pass
class UML2WithID_Slot(Element):

    pass
class UML2WithID_Feature(RedefinableElement, Element):

    pass
class UML2WithID_DirectedRelationship(Relationship, Element):

    pass
class UML2WithID_DeploymentSpecification(Artifact, Element):

    pass
class UML2WithID_Property(StructuralFeature, Element, ConnectableElement, DeploymentTarget):

    pass
class UML2WithID_StringExpression(Element, TemplateableElement):

    pass
class UML2WithID_TypedElement(Element, NamedElement):

    pass
class UML2WithID_TemplateParameterSubstitution(Element):

    pass
class UML2WithID_Profile(Package, Element):

    pass
class UML2WithID_LiteralInteger(LiteralSpecification, Element):

    pass
class UML2WithID_InteractionFragment(NamedElement, Element):

    pass
class UML2WithID_ActivityParameterNode(Element, ObjectNode):

    pass
class UML2WithID_Reception(BehavioralFeature, Element):

    pass
class UML2WithID_TemplateSignature(Element):

    pass
class UML2WithID_DurationInterval(Interval, Element):

    pass
class UML2WithID_Realization(Abstraction, Element):

    pass
class UML2WithID_InitialNode(ControlNode, Element):

    pass
class UML2WithID_InteractionOperand(Namespace, InteractionFragment, Element):

    pass
class ActivityNode:

    pass
class UML2WithID_ObjectNode(TypedElement, ActivityNode, Element):

    pass
class UML2WithID_ControlNode(ActivityNode, Element):

    pass
class UML2WithID_ExecutableNode(ActivityNode, Element):

    pass
class UML2WithID_DecisionNode(ControlNode, Element):

    pass
class InputPin:

    pass
class UML2WithID_ValuePin(InputPin, Element):

    pass
class Dependency:

    pass
class UML2WithID_Permission(Dependency, Element):

    pass
class UML2WithID_Abstraction(Dependency, Element):

    pass
class UML2WithID_Usage(Dependency, Element):

    pass
class UML2WithID_Deployment(Dependency, Element):

    pass