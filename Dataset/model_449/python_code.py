from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Abstraction:

    pass
class Feature:

    pass
class MessageTrigger:

    pass
class LiteralSpecification:

    pass
class Pin:

    pass
class MessageEnd:

    pass
class UML2WithID_Element(ABC):

    def __init__(self, ID: str, UML2WithID_Element: "UML2WithID_Element" = None, UML2WithID_Element0: "UML2WithID_Element" = None):
        self.ID = ID
        self.UML2WithID_Element = UML2WithID_Element
        self.UML2WithID_Element0 = UML2WithID_Element0
        
        pass
    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID


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

class EncapsulatedClassifier:

    pass
class TemplateSignature:

    pass
class OpaqueExpression:

    pass
class VariableAction:

    pass
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
class DataType:

    pass
class CreateLinkAction:

    pass
class InvocationAction:

    pass
class TemplateParameter:

    pass
class IntervalConstraint:

    pass
class Transition:

    pass
class Trigger:

    pass
class WriteVariableAction:

    pass
class FinalNode:

    pass
class Relationship:

    pass
class InstanceSpecification:

    pass
class ExecutableNode:

    pass
class State:

    pass
class DeployedArtifact:

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
class Artifact:

    pass
class StateMachine:

    pass
class TemplateableElement:

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
class WriteLinkAction:

    pass
class InputPin:

    pass
class Dependency:

    pass
class DirectedRelationship:

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
class UML2WithID_AddVariableValueAction(Element, WriteVariableAction):

    pass
class UML2WithID_TemplateSignature(Element):

    pass
class UML2WithID_TimeExpression(Element, ValueSpecification):

    pass
class UML2WithID_ProtocolStateMachine(StateMachine, Element):

    pass
class UML2WithID_Feature(Element, RedefinableElement):

    pass
class UML2WithID_Reception(Element, BehavioralFeature):

    pass
class UML2WithID_RedefinableTemplateSignature(TemplateSignature, Element, RedefinableElement):

    pass
class UML2WithID_ClearVariableAction(Element, VariableAction):

    pass
class UML2WithID_ProtocolTransition(Transition, Element):

    pass
class UML2WithID_Action(ExecutableNode, Element):

    pass
class UML2WithID_EnumerationLiteral(InstanceSpecification, Element):

    pass
class UML2WithID_CallAction(Element, InvocationAction):

    pass
class UML2WithID_MultiplicityElement(Element):

    pass
class UML2WithID_LiteralBoolean(LiteralSpecification, Element):

    pass
class UML2WithID_Duration(Element, ValueSpecification):

    pass
class UML2WithID_MessageTrigger(Element, Trigger):

    pass
class UML2WithID_TemplateParameterSubstitution(Element):

    pass
class UML2WithID_StartOwnedBehaviorAction(Action, Element):

    pass
class UML2WithID_EncapsulatedClassifier(Element, StructuredClassifier):

    pass
class UML2WithID_PrimitiveType(Element, DataType):

    pass
class UML2WithID_Behavior(Class, Element):

    pass
class UML2WithID_StateInvariant(InteractionFragment, Element):

    pass
class UML2WithID_InstanceValue(Element, ValueSpecification):

    pass
class UML2WithID_DestroyObjectAction(Action, Element):

    pass
class UML2WithID_Slot(Element):

    pass
class UML2WithID_RedefinableElement(Element, NamedElement):

    pass
class UML2WithID_InteractionFragment(Element, NamedElement):

    pass
class UML2WithID_Collaboration(StructuredClassifier, Element, BehavioredClassifier):

    pass
class UML2WithID_ConnectableElementTemplateParameter(TemplateParameter, Element):

    pass
class UML2WithID_ParameterableClassifier(Classifier, Element):

    pass
class UML2WithID_StructuredClassifier(Classifier, Element):

    pass
class UML2WithID_Substitution(Element, Realization):

    pass
class UML2WithID_Expression(Element, OpaqueExpression):

    pass
class UML2WithID_Vertex(Element, NamedElement):

    pass
class UML2WithID_SignalTrigger(Element, MessageTrigger):

    pass
class UML2WithID_ConnectionPointReference(Vertex, Element):

    pass
class UML2WithID_ParameterSet(Element, NamedElement):

    pass
class UML2WithID_Constraint(PackageableElement, Element):

    pass
class UML2WithID_StateMachine(Element, Behavior):

    pass
class UML2WithID_DestroyLinkAction(Element, WriteLinkAction):

    pass
class UML2WithID_Dependency(PackageableElement, Element, DirectedRelationship):

    pass
class UML2WithID_Extension(Element, Association):

    pass
class UML2WithID_Package(Namespace, PackageableElement, Element):

    pass
class UML2WithID_InteractionConstraint(Element, Constraint):

    pass
class UML2WithID_BehavioralFeature(Namespace, Element, Feature):

    pass
class UML2WithID_MessageEnd(Element, NamedElement):

    pass
class UML2WithID_Relationship(Element):

    pass
class UML2WithID_DeploymentTarget(Element, NamedElement):

    pass
class UML2WithID_LoopNode(Element, StructuredActivityNode):

    pass
class UML2WithID_QualifierValue(Element):

    pass
class UML2WithID_ExtensionEnd(Property, Element):

    pass
class UML2WithID_InstanceSpecification(DeployedArtifact, DeploymentTarget, PackageableElement, Element):

    pass
class UML2WithID_Variable(TypedElement, Element, MultiplicityElement, ConnectableElement):

    pass
class UML2WithID_Activity(Element, Behavior):

    pass
class UML2WithID_WriteLinkAction(Element, LinkAction):

    pass
class UML2WithID_ClassifierTemplateParameter(TemplateParameter, Element):

    pass
class UML2WithID_FlowFinalNode(FinalNode, Element):

    pass
class UML2WithID_Interaction(InteractionFragment, Element, Behavior):

    pass
class UML2WithID_LiteralNull(LiteralSpecification, Element):

    pass
class UML2WithID_CombinedFragment(InteractionFragment, Element):

    pass
class UML2WithID_CreateObjectAction(Action, Element):

    pass
class UML2WithID_ExecutionOccurrence(InteractionFragment, Element):

    pass
class UML2WithID_UseCase(Element, BehavioredClassifier):

    pass
class UML2WithID_MergeNode(ControlNode, Element):

    pass
class UML2WithID_InformationFlow(PackageableElement, Element, DirectedRelationship):

    pass
class UML2WithID_TimeTrigger(Element, Trigger):

    pass
class UML2WithID_LiteralInteger(LiteralSpecification, Element):

    pass
class UML2WithID_Abstraction(Dependency, Element):

    pass
class UML2WithID_Parameter(TypedElement, Element, MultiplicityElement, ConnectableElement):

    pass
class UML2WithID_RaiseExceptionAction(Action, Element):

    pass
class UML2WithID_InteractionOperand(Namespace, Element, InteractionFragment):

    pass
class UML2WithID_Lifeline(Element, NamedElement):

    pass
class UML2WithID_State(Namespace, RedefinableElement, Element, Vertex):

    pass
class UML2WithID_ExtensionPoint(Element, RedefinableElement):

    pass
class UML2WithID_Connector(Element, Feature):

    pass
class UML2WithID_Permission(Dependency, Element):

    pass
class UML2WithID_AcceptCallAction(AcceptEventAction, Element):

    pass
class UML2WithID_InitialNode(ControlNode, Element):

    pass
class UML2WithID_Device(Element, Node):

    pass
class UML2WithID_ClearStructuralFeatureAction(StructuralFeatureAction, Element):

    pass
class UML2WithID_InterruptibleActivityRegion(Element, ActivityGroup):

    pass
class UML2WithID_LinkEndData(Element):

    pass
class UML2WithID_WriteVariableAction(Element, VariableAction):

    pass
class UML2WithID_TestIdentityAction(Action, Element):

    pass
class UML2WithID_Port(Property, Element):

    pass
class UML2WithID_BroadcastSignalAction(Element, InvocationAction):

    pass
class UML2WithID_ProfileApplication(PackageImport, Element):

    pass
class UML2WithID_TemplateableClassifier(Classifier, Element):

    pass
class UML2WithID_StructuralFeatureAction(Action, Element):

    pass
class UML2WithID_Interface(Classifier, Element):

    pass
class UML2WithID_Stop(Element, EventOccurrence):

    pass
class UML2WithID_PrimitiveFunction(PackageableElement, Element):

    pass
class UML2WithID_StructuralFeature(TypedElement, Element, MultiplicityElement, Feature):

    pass
class UML2WithID_LiteralString(LiteralSpecification, Element):

    pass
class UML2WithID_TimeObservationAction(WriteStructuralFeatureAction, Element):

    pass
class UML2WithID_CreateLinkObjectAction(CreateLinkAction, Element):

    pass
class UML2WithID_Interval(Element, ValueSpecification):

    pass
class UML2WithID_Property(ConnectableElement, DeploymentTarget, Element, StructuralFeature):

    pass
class UML2WithID_Usage(Dependency, Element):

    pass
class UML2WithID_Manifestation(Element, Abstraction):

    pass
class UML2WithID_ActivityFinalNode(FinalNode, Element):

    pass
class UML2WithID_DirectedRelationship(Relationship, Element):

    pass
class UML2WithID_AcceptEventAction(Action, Element):

    pass
class UML2WithID_Clause(Element):

    pass
class UML2WithID_Trigger(Element, NamedElement):

    pass
class UML2WithID_TimeInterval(Element, Interval):

    pass
class UML2WithID_Artifact(DeployedArtifact, Classifier, Element):

    pass
class UML2WithID_Deployment(Dependency, Element):

    pass
class UML2WithID_CallTrigger(Element, MessageTrigger):

    pass
class UML2WithID_LiteralUnlimitedNatural(LiteralSpecification, Element):

    pass
class UML2WithID_PackageableElement(ParameterableElement, Element, NamedElement):

    pass
class UML2WithID_FinalState(Element, State):

    pass
class UML2WithID_ExpansionRegion(Element, StructuredActivityNode):

    pass
class UML2WithID_PackageImport(Element, DirectedRelationship):

    pass
class UML2WithID_ActivityPartition(NamedElement, Element, ActivityGroup):

    pass
class UML2WithID_ValuePin(InputPin, Element):

    pass
class UML2WithID_ReadExtentAction(Action, Element):

    pass
class UML2WithID_Region(Namespace, Element, RedefinableElement):

    pass
class UML2WithID_Gate(MessageEnd, Element):

    pass
class UML2WithID_DurationObservationAction(Element, WriteStructuralFeatureAction):

    pass
class UML2WithID_ReadLinkObjectEndQualifierAction(Action, Element):

    pass
class UML2WithID_ReplyAction(Action, Element):

    pass
class UML2WithID_PartDecomposition(InteractionOccurrence, Element):

    pass
class UML2WithID_ParameterableElement(Element):

    pass
class UML2WithID_Pin(Element, MultiplicityElement, ObjectNode):

    pass
class UML2WithID_BehavioredClassifier(Classifier, Element):

    pass
class UML2WithID_GeneralOrdering(Element, NamedElement):

    pass
class UML2WithID_ActivityParameterNode(Element, ObjectNode):

    pass
class UML2WithID_Node(Class, DeploymentTarget, Element):

    pass
class UML2WithID_ChangeTrigger(Element, Trigger):

    pass
class UML2WithID_ReadVariableAction(Element, VariableAction):

    pass
class UML2WithID_RemoveStructuralFeatureValueAction(Element, WriteStructuralFeatureAction):

    pass
class UML2WithID_Model(Package, Element):

    pass
class UML2WithID_ReadIsClassifiedObjectAction(Action, Element):

    pass
class UML2WithID_Include(NamedElement, Element, DirectedRelationship):

    pass
class UML2WithID_LiteralSpecification(Element, ValueSpecification):

    pass
class UML2WithID_ActivityGroup(Element):

    pass
class UML2WithID_VariableAction(Action, Element):

    pass
class UML2WithID_InvocationAction(Action, Element):

    pass
class UML2WithID_Pseudostate(Element, Vertex):

    pass
class UML2WithID_TypedElement(Element, NamedElement):

    pass
class UML2WithID_Type(PackageableElement, Element):

    pass
class UML2WithID_CallBehaviorAction(Element, CallAction):

    pass
class UML2WithID_ApplyFunctionAction(Action, Element):

    pass
class UML2WithID_ProtocolConformance(Element, DirectedRelationship):

    pass
class UML2WithID_Comment(TemplateableElement, Element):

    pass
class UML2WithID_ActivityEdge(Element, RedefinableElement):

    pass
class UML2WithID_ExpansionNode(Element, ObjectNode):

    pass
class UML2WithID_DeploymentSpecification(Artifact, Element):

    pass
class UML2WithID_Classifier(Type, Namespace, Element, RedefinableElement):

    pass
class UML2WithID_ReadLinkAction(Element, LinkAction):

    pass
class UML2WithID_ValueSpecification(TypedElement, ParameterableElement, Element):

    pass
class UML2WithID_ReadStructuralFeatureAction(StructuralFeatureAction, Element):

    pass
class UML2WithID_ReadLinkObjectEndAction(Action, Element):

    pass
class UML2WithID_TemplateParameter(Element):

    pass
class UML2WithID_CollaborationOccurrence(Element, NamedElement):

    pass
class UML2WithID_DeployedArtifact(Element, NamedElement):

    pass
class UML2WithID_JoinNode(ControlNode, Element):

    pass
class UML2WithID_Operation(MultiplicityElement, BehavioralFeature, TypedElement, ParameterableElement, Element):

    pass
class UML2WithID_PackageMerge(Element, DirectedRelationship):

    pass
class UML2WithID_Signal(Classifier, Element):

    pass
class UML2WithID_Realization(Element, Abstraction):

    pass
class UML2WithID_ConnectableElement(ParameterableElement, Element, NamedElement):

    pass
class UML2WithID_Actor(Classifier, Element):

    pass
class UML2WithID_DurationInterval(Element, Interval):

    pass
class UML2WithID_Implementation(Element, Realization):

    pass
class UML2WithID_CallOperationAction(Element, CallAction):

    pass
class UML2WithID_WriteStructuralFeatureAction(StructuralFeatureAction, Element):

    pass
class UML2WithID_LinkEndCreationData(LinkEndData, Element):

    pass
class UML2WithID_LinkAction(Action, Element):

    pass
class UML2WithID_Profile(Package, Element):

    pass
class UML2WithID_TemplateableElement(Element):

    pass
class UML2WithID_AnyTrigger(Element, MessageTrigger):

    pass
class UML2WithID_StructuredActivityNode(Action, Namespace, ActivityGroup, Element):

    pass
class UML2WithID_Message(Element, NamedElement):

    pass
class UML2WithID_Namespace(Element, NamedElement):

    pass
class UML2WithID_ReadSelfAction(Action, Element):

    pass
class UML2WithID_TemplateBinding(Element, DirectedRelationship):

    pass
class UML2WithID_ExecutionEnvironment(Element, Node):

    pass
class UML2WithID_EventOccurrence(MessageEnd, InteractionFragment, Element):

    pass
class UML2WithID_DataStoreNode(CentralBufferNode, Element):

    pass
class UML2WithID_ElementImport(Element, DirectedRelationship):

    pass
class UML2WithID_CreateLinkAction(Element, WriteLinkAction):

    pass
class UML2WithID_IntervalConstraint(Element, Constraint):

    pass
class UML2WithID_ReclassifyObjectAction(Action, Element):

    pass
class UML2WithID_Component(Class, Element):

    pass
class UML2WithID_SendSignalAction(Element, InvocationAction):

    pass
class UML2WithID_ConnectorEnd(Element, MultiplicityElement):

    pass
class UML2WithID_ActivityNode(Element, RedefinableElement):

    pass
class UML2WithID_SendObjectAction(Element, InvocationAction):

    pass
class UML2WithID_CentralBufferNode(Element, ObjectNode):

    pass
class UML2WithID_RemoveVariableValueAction(Element, WriteVariableAction):

    pass
class UML2WithID_OutputPin(Element, Pin):

    pass
class UML2WithID_DecisionNode(ControlNode, Element):

    pass
class UML2WithID_AssociationClass(Class, Element, Association):

    pass
class UML2WithID_TimeConstraint(IntervalConstraint, Element):

    pass
class UML2WithID_ConditionalNode(Element, StructuredActivityNode):

    pass
class UML2WithID_InformationItem(Classifier, Element):

    pass
class UML2WithID_DurationConstraint(IntervalConstraint, Element):

    pass
class UML2WithID_InteractionOccurrence(InteractionFragment, Element):

    pass
class UML2WithID_Continuation(InteractionFragment, Element):

    pass
class UML2WithID_Association(Classifier, Relationship, Element):

    pass
class UML2WithID_ClearAssociationAction(Action, Element):

    pass
class UML2WithID_Generalization(Element, DirectedRelationship):

    pass
class UML2WithID_ObjectFlow(ActivityEdge, Element):

    pass
class UML2WithID_ForkNode(ControlNode, Element):

    pass
class UML2WithID_StringExpression(TemplateableElement, Element):

    pass
class UML2WithID_CommunicationPath(Element, Association):

    pass
class UML2WithID_Transition(Element, RedefinableElement):

    pass
class UML2WithID_InputPin(Element, Pin):

    pass
class UML2WithID_AddStructuralFeatureValueAction(Element, WriteStructuralFeatureAction):

    pass
class UML2WithID_ControlFlow(ActivityEdge, Element):

    pass
class UML2WithID_Enumeration(Element, DataType):

    pass
class UML2WithID_DataType(Classifier, Element):

    pass
class UML2WithID_Extend(NamedElement, Element, DirectedRelationship):

    pass
class UML2WithID_Class(Element, BehavioredClassifier, EncapsulatedClassifier):

    pass
class UML2WithID_NamedElement(TemplateableElement, Element):

    pass
class UML2WithID_FinalNode(ControlNode, Element):

    pass
class UML2WithID_OperationTemplateParameter(TemplateParameter, Element):

    pass
class UML2WithID_GeneralizationSet(PackageableElement, Element):

    pass
class UML2WithID_OpaqueExpression(Element, ValueSpecification):

    pass
class UML2WithID_Stereotype(Class, Element):

    pass
class UML2WithID_ExceptionHandler(Element):

    pass
class ActivityNode:

    pass
class UML2WithID_ObjectNode(TypedElement, Element, ActivityNode):

    pass
class UML2WithID_ControlNode(ActivityNode, Element):

    pass
class UML2WithID_ExecutableNode(ActivityNode, Element):

    pass