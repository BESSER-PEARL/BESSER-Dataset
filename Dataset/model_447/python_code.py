from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class EncapsulatedClassifier:

    pass
class InstanceSpecification:

    pass
class LinkEndData:

    pass
class InputPin:

    pass
class Constraint:

    pass
class ExecutableNode:

    pass
class State:

    pass
class StateMachine:

    pass
class CreateLinkAction:

    pass
class WriteStructuralFeatureAction:

    pass
class StructuredClassifier:

    pass
class CentralBufferNode:

    pass
class AcceptEventAction:

    pass
class Type:

    pass
class CallAction:

    pass
class StructuredActivityNode:

    pass
class Property:

    pass
class EventOccurrence:

    pass
class Abstraction:

    pass
class LinkAction:

    pass
class Relationship:

    pass
class ObjectNode:

    pass
class Pin:

    pass
class OpaqueExpression:

    pass
class Association:

    pass
class TemplateParameter:

    pass
class BehavioredClassifier:

    pass
class StructuralFeatureAction:

    pass
class TemplateSignature:

    pass
class ParameterableElement:

    pass
class StructuralFeature:

    pass
class DeployedArtifact:

    pass
class FinalNode:

    pass
class Realization:

    pass
class NamedElement:

    pass
class ConnectableElement:

    pass
class PackageImport:

    pass
class Vertex:

    pass
class Dependency:

    pass
class WriteVariableAction:

    pass
class Node:

    pass
class WriteLinkAction:

    pass
class MessageTrigger:

    pass
class PackageableElement:

    pass
class Artifact:

    pass
class Interval:

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

class InteractionOccurrence:

    pass
class ControlNode:

    pass
class BehavioralFeature:

    pass
class MultiplicityElement:

    pass
class TypedElement:

    pass
class Feature:

    pass
class MessageEnd:

    pass
class Element:

    pass
class UML2WithID_LinkEndData(Element):

    pass
class UML2WithID_MergeNode(Element, ControlNode):

    pass
class UML2WithID_AddStructuralFeatureValueAction(WriteStructuralFeatureAction, Element):

    pass
class UML2WithID_Permission(Element, Dependency):

    pass
class UML2WithID_TemplateableElement(Element):

    pass
class UML2WithID_GeneralizationSet(Element, PackageableElement):

    pass
class UML2WithID_CallTrigger(Element, MessageTrigger):

    pass
class UML2WithID_ActivityFinalNode(Element, FinalNode):

    pass
class UML2WithID_TemplateSignature(Element):

    pass
class UML2WithID_UseCase(BehavioredClassifier, Element):

    pass
class UML2WithID_Connector(Feature, Element):

    pass
class UML2WithID_Lifeline(NamedElement, Element):

    pass
class UML2WithID_Pin(ObjectNode, Element, MultiplicityElement):

    pass
class UML2WithID_FlowFinalNode(Element, FinalNode):

    pass
class UML2WithID_ConnectableElementTemplateParameter(Element, TemplateParameter):

    pass
class UML2WithID_Variable(ConnectableElement, MultiplicityElement, TypedElement, Element):

    pass
class UML2WithID_Class(BehavioredClassifier, Element, EncapsulatedClassifier):

    pass
class UML2WithID_ExpansionNode(ObjectNode, Element):

    pass
class UML2WithID_Parameter(Element, ConnectableElement, TypedElement, MultiplicityElement):

    pass
class UML2WithID_ForkNode(Element, ControlNode):

    pass
class UML2WithID_Namespace(NamedElement, Element):

    pass
class UML2WithID_DataStoreNode(Element, CentralBufferNode):

    pass
class UML2WithID_AnyTrigger(Element, MessageTrigger):

    pass
class UML2WithID_ConnectableElement(ParameterableElement, NamedElement, Element):

    pass
class UML2WithID_Deployment(Element, Dependency):

    pass
class UML2WithID_ReadStructuralFeatureAction(StructuralFeatureAction, Element):

    pass
class UML2WithID_ExtensionEnd(Property, Element):

    pass
class UML2WithID_Relationship(Element):

    pass
class UML2WithID_TimeInterval(Element, Interval):

    pass
class UML2WithID_ConnectorEnd(MultiplicityElement, Element):

    pass
class UML2WithID_QualifierValue(Element):

    pass
class UML2WithID_ParameterSet(NamedElement, Element):

    pass
class UML2WithID_ExpansionRegion(Element, StructuredActivityNode):

    pass
class UML2WithID_Pseudostate(Element, Vertex):

    pass
class UML2WithID_InputPin(Pin, Element):

    pass
class UML2WithID_AcceptCallAction(Element, AcceptEventAction):

    pass
class UML2WithID_InteractionFragment(NamedElement, Element):

    pass
class UML2WithID_CreateLinkObjectAction(CreateLinkAction, Element):

    pass
class UML2WithID_PrimitiveFunction(Element, PackageableElement):

    pass
class UML2WithID_ProfileApplication(Element, PackageImport):

    pass
class UML2WithID_RemoveStructuralFeatureValueAction(WriteStructuralFeatureAction, Element):

    pass
class UML2WithID_Slot(Element):

    pass
class UML2WithID_Device(Element, Node):

    pass
class UML2WithID_PackageableElement(ParameterableElement, NamedElement, Element):

    pass
class UML2WithID_ValueSpecification(ParameterableElement, Element, TypedElement):

    pass
class UML2WithID_Collaboration(BehavioredClassifier, StructuredClassifier, Element):

    pass
class UML2WithID_LoopNode(Element, StructuredActivityNode):

    pass
class UML2WithID_Stop(Element, EventOccurrence):

    pass
class UML2WithID_DurationObservationAction(WriteStructuralFeatureAction, Element):

    pass
class UML2WithID_Abstraction(Element, Dependency):

    pass
class UML2WithID_JoinNode(Element, ControlNode):

    pass
class UML2WithID_ConditionalNode(Element, StructuredActivityNode):

    pass
class UML2WithID_DecisionNode(Element, ControlNode):

    pass
class UML2WithID_Vertex(NamedElement, Element):

    pass
class UML2WithID_GeneralOrdering(NamedElement, Element):

    pass
class UML2WithID_Gate(Element, MessageEnd):

    pass
class UML2WithID_EnumerationLiteral(Element, InstanceSpecification):

    pass
class UML2WithID_MultiplicityElement(Element):

    pass
class UML2WithID_OutputPin(Pin, Element):

    pass
class UML2WithID_InitialNode(Element, ControlNode):

    pass
class UML2WithID_DirectedRelationship(Element, Relationship):

    pass
class UML2WithID_CentralBufferNode(ObjectNode, Element):

    pass
class UML2WithID_AddVariableValueAction(Element, WriteVariableAction):

    pass
class UML2WithID_EncapsulatedClassifier(StructuredClassifier, Element):

    pass
class UML2WithID_RedefinableElement(NamedElement, Element):

    pass
class UML2WithID_Type(Element, PackageableElement):

    pass
class UML2WithID_TimeObservationAction(WriteStructuralFeatureAction, Element):

    pass
class UML2WithID_ExceptionHandler(Element):

    pass
class UML2WithID_Action(Element, ExecutableNode):

    pass
class UML2WithID_DestroyLinkAction(WriteLinkAction, Element):

    pass
class UML2WithID_Port(Property, Element):

    pass
class UML2WithID_Implementation(Realization, Element):

    pass
class UML2WithID_Trigger(NamedElement, Element):

    pass
class UML2WithID_PartDecomposition(Element, InteractionOccurrence):

    pass
class UML2WithID_LinkEndCreationData(LinkEndData, Element):

    pass
class UML2WithID_StructuralFeature(MultiplicityElement, Feature, TypedElement, Element):

    pass
class UML2WithID_ClearStructuralFeatureAction(StructuralFeatureAction, Element):

    pass
class UML2WithID_MessageEnd(NamedElement, Element):

    pass
class UML2WithID_Reception(Element, BehavioralFeature):

    pass
class UML2WithID_Realization(Abstraction, Element):

    pass
class UML2WithID_DeploymentSpecification(Element, Artifact):

    pass
class UML2WithID_ValuePin(InputPin, Element):

    pass
class UML2WithID_ExecutionEnvironment(Element, Node):

    pass
class UML2WithID_Manifestation(Abstraction, Element):

    pass
class UML2WithID_FinalState(Element, State):

    pass
class UML2WithID_CreateLinkAction(WriteLinkAction, Element):

    pass
class UML2WithID_Extension(Element, Association):

    pass
class UML2WithID_Constraint(Element, PackageableElement):

    pass
class UML2WithID_OperationTemplateParameter(Element, TemplateParameter):

    pass
class UML2WithID_ActivityParameterNode(ObjectNode, Element):

    pass
class UML2WithID_ProtocolStateMachine(StateMachine, Element):

    pass
class UML2WithID_ClassifierTemplateParameter(Element, TemplateParameter):

    pass
class UML2WithID_ActivityGroup(Element):

    pass
class UML2WithID_FinalNode(Element, ControlNode):

    pass
class UML2WithID_RemoveVariableValueAction(Element, WriteVariableAction):

    pass
class UML2WithID_CallBehaviorAction(CallAction, Element):

    pass
class UML2WithID_TypedElement(NamedElement, Element):

    pass
class UML2WithID_Usage(Element, Dependency):

    pass
class UML2WithID_TemplateParameterSubstitution(Element):

    pass
class UML2WithID_WriteStructuralFeatureAction(StructuralFeatureAction, Element):

    pass
class UML2WithID_Substitution(Realization, Element):

    pass
class UML2WithID_DurationInterval(Element, Interval):

    pass
class UML2WithID_CollaborationOccurrence(NamedElement, Element):

    pass
class UML2WithID_InteractionConstraint(Element, Constraint):

    pass
class UML2WithID_DeployedArtifact(NamedElement, Element):

    pass
class UML2WithID_CommunicationPath(Element, Association):

    pass
class UML2WithID_ConnectionPointReference(Element, Vertex):

    pass
class UML2WithID_TemplateParameter(Element):

    pass
class UML2WithID_Operation(ParameterableElement, BehavioralFeature, TypedElement, MultiplicityElement, Element):

    pass
class UML2WithID_ReadLinkAction(Element, LinkAction):

    pass
class UML2WithID_Message(NamedElement, Element):

    pass
class UML2WithID_Expression(OpaqueExpression, Element):

    pass
class UML2WithID_IntervalConstraint(Element, Constraint):

    pass
class UML2WithID_CallOperationAction(Element, CallAction):

    pass
class UML2WithID_DeploymentTarget(NamedElement, Element):

    pass
class UML2WithID_Clause(Element):

    pass
class UML2WithID_WriteLinkAction(Element, LinkAction):

    pass
class UML2WithID_SignalTrigger(Element, MessageTrigger):

    pass
class Transition:

    pass
class Classifier:

    pass
class UML2WithID_ParameterableClassifier(Element, Classifier):

    pass
class UML2WithID_StructuredClassifier(Element, Classifier):

    pass
class UML2WithID_Association(Element, Relationship, Classifier):

    pass
class UML2WithID_Artifact(Element, DeployedArtifact, Classifier):

    pass
class UML2WithID_TemplateableClassifier(Element, Classifier):

    pass
class UML2WithID_DataType(Element, Classifier):

    pass
class UML2WithID_BehavioredClassifier(Element, Classifier):

    pass
class UML2WithID_Signal(Element, Classifier):

    pass
class UML2WithID_Actor(Element, Classifier):

    pass
class UML2WithID_InformationItem(Element, Classifier):

    pass
class UML2WithID_Interface(Element, Classifier):

    pass
class DirectedRelationship:

    pass
class UML2WithID_TemplateBinding(DirectedRelationship, Element):

    pass
class UML2WithID_PackageImport(DirectedRelationship, Element):

    pass
class UML2WithID_PackageMerge(DirectedRelationship, Element):

    pass
class UML2WithID_InformationFlow(DirectedRelationship, Element, PackageableElement):

    pass
class UML2WithID_Include(NamedElement, DirectedRelationship, Element):

    pass
class UML2WithID_Generalization(DirectedRelationship, Element):

    pass
class UML2WithID_Extend(NamedElement, DirectedRelationship, Element):

    pass
class UML2WithID_ElementImport(DirectedRelationship, Element):

    pass
class UML2WithID_Dependency(DirectedRelationship, PackageableElement, Element):

    pass
class UML2WithID_ProtocolConformance(DirectedRelationship, Element):

    pass
class InteractionFragment:

    pass
class UML2WithID_ExecutionOccurrence(InteractionFragment, Element):

    pass
class UML2WithID_CombinedFragment(InteractionFragment, Element):

    pass
class UML2WithID_InteractionOccurrence(Element, InteractionFragment):

    pass
class UML2WithID_EventOccurrence(MessageEnd, InteractionFragment, Element):

    pass
class UML2WithID_Continuation(InteractionFragment, Element):

    pass
class UML2WithID_StateInvariant(Element, InteractionFragment):

    pass
class Trigger:

    pass
class UML2WithID_ChangeTrigger(Element, Trigger):

    pass
class UML2WithID_MessageTrigger(Element, Trigger):

    pass
class UML2WithID_TimeTrigger(Element, Trigger):

    pass
class InvocationAction:

    pass
class UML2WithID_CallAction(InvocationAction, Element):

    pass
class UML2WithID_BroadcastSignalAction(InvocationAction, Element):

    pass
class UML2WithID_SendSignalAction(InvocationAction, Element):

    pass
class UML2WithID_SendObjectAction(InvocationAction, Element):

    pass
class ActivityEdge:

    pass
class UML2WithID_ObjectFlow(Element, ActivityEdge):

    pass
class UML2WithID_ControlFlow(Element, ActivityEdge):

    pass
class RedefinableElement:

    pass
class UML2WithID_ActivityEdge(Element, RedefinableElement):

    pass
class UML2WithID_Feature(Element, RedefinableElement):

    pass
class UML2WithID_RedefinableTemplateSignature(Element, RedefinableElement, TemplateSignature):

    pass
class UML2WithID_Transition(Element, RedefinableElement):

    pass
class UML2WithID_ActivityNode(Element, RedefinableElement):

    pass
class UML2WithID_ExtensionPoint(Element, RedefinableElement):

    pass
class IntervalConstraint:

    pass
class UML2WithID_DurationConstraint(Element, IntervalConstraint):

    pass
class UML2WithID_TimeConstraint(Element, IntervalConstraint):

    pass
class TemplateableElement:

    pass
class UML2WithID_NamedElement(Element, TemplateableElement):

    pass
class UML2WithID_StringExpression(Element, TemplateableElement):

    pass
class UML2WithID_Comment(Element, TemplateableElement):

    pass
class Behavior:

    pass
class UML2WithID_Interaction(Element, InteractionFragment, Behavior):

    pass
class UML2WithID_Activity(Element, Behavior):

    pass
class UML2WithID_StateMachine(Element, Behavior):

    pass
class ActivityNode:

    pass
class UML2WithID_ControlNode(ActivityNode, Element):

    pass
class UML2WithID_ObjectNode(ActivityNode, TypedElement, Element):

    pass
class UML2WithID_ExecutableNode(ActivityNode, Element):

    pass
class ValueSpecification:

    pass
class UML2WithID_Duration(Element, ValueSpecification):

    pass
class UML2WithID_TimeExpression(Element, ValueSpecification):

    pass
class UML2WithID_OpaqueExpression(Element, ValueSpecification):

    pass
class UML2WithID_InstanceValue(Element, ValueSpecification):

    pass
class UML2WithID_Interval(Element, ValueSpecification):

    pass
class UML2WithID_LiteralSpecification(Element, ValueSpecification):

    pass
class VariableAction:

    pass
class UML2WithID_WriteVariableAction(VariableAction, Element):

    pass
class UML2WithID_ClearVariableAction(VariableAction, Element):

    pass
class UML2WithID_ReadVariableAction(VariableAction, Element):

    pass
class LiteralSpecification:

    pass
class UML2WithID_LiteralBoolean(LiteralSpecification, Element):

    pass
class UML2WithID_LiteralInteger(LiteralSpecification, Element):

    pass
class UML2WithID_LiteralString(LiteralSpecification, Element):

    pass
class UML2WithID_LiteralNull(LiteralSpecification, Element):

    pass
class UML2WithID_LiteralUnlimitedNatural(LiteralSpecification, Element):

    pass
class DeploymentTarget:

    pass
class UML2WithID_InstanceSpecification(DeploymentTarget, DeployedArtifact, PackageableElement, Element):

    pass
class UML2WithID_Property(StructuralFeature, Element, ConnectableElement, DeploymentTarget):

    pass
class Class:

    pass
class UML2WithID_Component(Class, Element):

    pass
class UML2WithID_AssociationClass(Class, Element, Association):

    pass
class UML2WithID_Stereotype(Class, Element):

    pass
class UML2WithID_Behavior(Class, Element):

    pass
class UML2WithID_Node(Class, DeploymentTarget, Element):

    pass
class DataType:

    pass
class UML2WithID_Enumeration(DataType, Element):

    pass
class UML2WithID_PrimitiveType(DataType, Element):

    pass
class Package:

    pass
class UML2WithID_Model(Element, Package):

    pass
class UML2WithID_Profile(Element, Package):

    pass
class ActivityGroup:

    pass
class UML2WithID_ActivityPartition(NamedElement, ActivityGroup, Element):

    pass
class UML2WithID_InterruptibleActivityRegion(Element, ActivityGroup):

    pass
class Namespace:

    pass
class UML2WithID_Package(Namespace, Element, PackageableElement):

    pass
class UML2WithID_InteractionOperand(Namespace, InteractionFragment, Element):

    pass
class UML2WithID_BehavioralFeature(Namespace, Element, Feature):

    pass
class UML2WithID_State(Namespace, Element, RedefinableElement, Vertex):

    pass
class UML2WithID_Classifier(Namespace, Element, RedefinableElement, Type):

    pass
class UML2WithID_Region(Namespace, Element, RedefinableElement):

    pass
class Action:

    pass
class UML2WithID_ApplyFunctionAction(Action, Element):

    pass
class UML2WithID_InvocationAction(Action, Element):

    pass
class UML2WithID_ReclassifyObjectAction(Action, Element):

    pass
class UML2WithID_StructuralFeatureAction(Action, Element):

    pass
class UML2WithID_StartOwnedBehaviorAction(Action, Element):

    pass
class UML2WithID_ReadLinkObjectEndQualifierAction(Action, Element):

    pass
class UML2WithID_LinkAction(Action, Element):

    pass
class UML2WithID_ReadExtentAction(Action, Element):

    pass
class UML2WithID_ReadLinkObjectEndAction(Action, Element):

    pass
class UML2WithID_AcceptEventAction(Action, Element):

    pass
class UML2WithID_CreateObjectAction(Action, Element):

    pass
class UML2WithID_VariableAction(Action, Element):

    pass
class UML2WithID_DestroyObjectAction(Action, Element):

    pass
class UML2WithID_RaiseExceptionAction(Action, Element):

    pass
class UML2WithID_TestIdentityAction(Action, Element):

    pass
class UML2WithID_ClearAssociationAction(Action, Element):

    pass
class UML2WithID_ReadSelfAction(Action, Element):

    pass
class UML2WithID_ReadIsClassifiedObjectAction(Action, Element):

    pass
class UML2WithID_ReplyAction(Action, Element):

    pass
class UML2WithID_StructuredActivityNode(Action, Element, Namespace, ActivityGroup):

    pass
class UML2WithID_ParameterableElement(Element):

    pass
class UML2WithID_ProtocolTransition(Transition, Element):

    pass