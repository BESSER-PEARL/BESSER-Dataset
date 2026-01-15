from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class State:

    pass
class LinkEndData:

    pass
class InputPin:

    pass
class Package:

    pass
class Abstraction:

    pass
class Type:

    pass
class OpaqueExpression:

    pass
class Realization:

    pass
class PackageImport:

    pass
class StateMachine:

    pass
class Vertex:

    pass
class Dependency:

    pass
class Interval:

    pass
class EventOccurrence:

    pass
class Transition:

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

class Artifact:

    pass
class WriteVariableAction:

    pass
class Pin:

    pass
class Relationship:

    pass
class StructuralFeature:

    pass
class ActivityGroup:

    pass
class Property:

    pass
class MessageEnd:

    pass
class InteractionFragment:

    pass
class WriteStructuralFeatureAction:

    pass
class Constraint:

    pass
class ParameterableElement:

    pass
class BehavioralFeature:

    pass
class Namespace:

    pass
class CallAction:

    pass
class ObjectNode:

    pass
class Association:

    pass
class IntervalConstraint:

    pass
class StructuredActivityNode:

    pass
class InstanceSpecification:

    pass
class VariableAction:

    pass
class FinalNode:

    pass
class EncapsulatedClassifier:

    pass
class AcceptEventAction:

    pass
class Behavior:

    pass
class ValueSpecification:

    pass
class TemplateableElement:

    pass
class CentralBufferNode:

    pass
class TypedElement:

    pass
class ConnectableElement:

    pass
class LinkAction:

    pass
class PackageableElement:

    pass
class DataType:

    pass
class DeploymentTarget:

    pass
class StructuralFeatureAction:

    pass
class Feature:

    pass
class WriteLinkAction:

    pass
class DirectedRelationship:

    pass
class TemplateParameter:

    pass
class ControlNode:

    pass
class CreateLinkAction:

    pass
class ActivityNode:

    pass
class LiteralSpecification:

    pass
class InteractionOccurrence:

    pass
class StructuredClassifier:

    pass
class BehavioredClassifier:

    pass
class InvocationAction:

    pass
class ExecutableNode:

    pass
class Action:

    pass
class Trigger:

    pass
class Classifier:

    pass
class MessageTrigger:

    pass
class DeployedArtifact:

    pass
class NamedElement:

    pass
class Class:

    pass
class TemplateSignature:

    pass
class RedefinableElement:

    pass
class Element:

    pass
class UML2WithID_DurationInterval(Element, Interval):

    pass
class UML2WithID_StructuredClassifier(Element, Classifier):

    pass
class UML2WithID_TypedElement(Element, NamedElement):

    pass
class UML2WithID_InteractionConstraint(Element, Constraint):

    pass
class UML2WithID_RemoveStructuralFeatureValueAction(Element, WriteStructuralFeatureAction):

    pass
class UML2WithID_TimeInterval(Element, Interval):

    pass
class UML2WithID_Gate(Element, MessageEnd):

    pass
class UML2WithID_Collaboration(BehavioredClassifier, Element, StructuredClassifier):

    pass
class UML2WithID_ConnectionPointReference(Vertex, Element):

    pass
class UML2WithID_LiteralString(Element, LiteralSpecification):

    pass
class UML2WithID_Permission(Element, Dependency):

    pass
class UML2WithID_ReadLinkAction(Element, LinkAction):

    pass
class UML2WithID_ExpansionRegion(Element, StructuredActivityNode):

    pass
class UML2WithID_LinkEndCreationData(Element, LinkEndData):

    pass
class UML2WithID_UseCase(BehavioredClassifier, Element):

    pass
class UML2WithID_ProtocolTransition(Transition, Element):

    pass
class UML2WithID_StructuredActivityNode(Element, ActivityGroup, Action, Namespace):

    pass
class UML2WithID_InputPin(Element, Pin):

    pass
class UML2WithID_ParameterableElement(Element):

    pass
class UML2WithID_ReadSelfAction(Element, Action):

    pass
class UML2WithID_CentralBufferNode(Element, ObjectNode):

    pass
class UML2WithID_AcceptEventAction(Element, Action):

    pass
class UML2WithID_ReplyAction(Element, Action):

    pass
class UML2WithID_ExecutableNode(Element, ActivityNode):

    pass
class UML2WithID_InterruptibleActivityRegion(Element, ActivityGroup):

    pass
class UML2WithID_ValueSpecification(Element, TypedElement, ParameterableElement):

    pass
class UML2WithID_ApplyFunctionAction(Element, Action):

    pass
class UML2WithID_Realization(Element, Abstraction):

    pass
class UML2WithID_GeneralOrdering(Element, NamedElement):

    pass
class UML2WithID_ReadExtentAction(Element, Action):

    pass
class UML2WithID_ReadLinkObjectEndQualifierAction(Element, Action):

    pass
class UML2WithID_DataStoreNode(Element, CentralBufferNode):

    pass
class UML2WithID_ConnectableElementTemplateParameter(Element, TemplateParameter):

    pass
class UML2WithID_Actor(Element, Classifier):

    pass
class UML2WithID_RedefinableElement(Element, NamedElement):

    pass
class UML2WithID_ExceptionHandler(Element):

    pass
class UML2WithID_AnyTrigger(Element, MessageTrigger):

    pass
class UML2WithID_DurationConstraint(Element, IntervalConstraint):

    pass
class UML2WithID_VariableAction(Element, Action):

    pass
class UML2WithID_Message(Element, NamedElement):

    pass
class UML2WithID_Artifact(Element, DeployedArtifact, Classifier):

    pass
class UML2WithID_RemoveVariableValueAction(Element, WriteVariableAction):

    pass
class UML2WithID_Pseudostate(Vertex, Element):

    pass
class UML2WithID_Type(Element, PackageableElement):

    pass
class UML2WithID_MessageEnd(Element, NamedElement):

    pass
class UML2WithID_Stop(Element, EventOccurrence):

    pass
class UML2WithID_Trigger(Element, NamedElement):

    pass
class UML2WithID_StateInvariant(Element, InteractionFragment):

    pass
class UML2WithID_JoinNode(Element, ControlNode):

    pass
class UML2WithID_AssociationClass(Element, Association, Class):

    pass
class UML2WithID_Package(Element, PackageableElement, Namespace):

    pass
class UML2WithID_BroadcastSignalAction(Element, InvocationAction):

    pass
class UML2WithID_ActivityParameterNode(Element, ObjectNode):

    pass
class UML2WithID_DeployedArtifact(Element, NamedElement):

    pass
class UML2WithID_LoopNode(Element, StructuredActivityNode):

    pass
class UML2WithID_OperationTemplateParameter(Element, TemplateParameter):

    pass
class UML2WithID_MergeNode(Element, ControlNode):

    pass
class UML2WithID_ReadStructuralFeatureAction(StructuralFeatureAction, Element):

    pass
class UML2WithID_Model(Package, Element):

    pass
class UML2WithID_Region(Element, RedefinableElement, Namespace):

    pass
class UML2WithID_Connector(Element, Feature):

    pass
class UML2WithID_ReadIsClassifiedObjectAction(Element, Action):

    pass
class UML2WithID_CallAction(Element, InvocationAction):

    pass
class UML2WithID_EncapsulatedClassifier(Element, StructuredClassifier):

    pass
class UML2WithID_Deployment(Element, Dependency):

    pass
class UML2WithID_Component(Element, Class):

    pass
class UML2WithID_Feature(Element, RedefinableElement):

    pass
class UML2WithID_Namespace(Element, NamedElement):

    pass
class UML2WithID_ElementImport(Element, DirectedRelationship):

    pass
class UML2WithID_DestroyLinkAction(WriteLinkAction, Element):

    pass
class UML2WithID_ActivityGroup(Element):

    pass
class UML2WithID_Enumeration(Element, DataType):

    pass
class UML2WithID_ChangeTrigger(Element, Trigger):

    pass
class UML2WithID_Slot(Element):

    pass
class UML2WithID_ProtocolConformance(Element, DirectedRelationship):

    pass
class UML2WithID_DeploymentSpecification(Element, Artifact):

    pass
class UML2WithID_MultiplicityElement(Element):

    pass
class UML2WithID_InitialNode(Element, ControlNode):

    pass
class UML2WithID_LiteralBoolean(LiteralSpecification, Element):

    pass
class UML2WithID_TemplateableClassifier(Element, Classifier):

    pass
class UML2WithID_Node(Element, DeploymentTarget, Class):

    pass
class UML2WithID_LiteralUnlimitedNatural(LiteralSpecification, Element):

    pass
class UML2WithID_MessageTrigger(Element, Trigger):

    pass
class UML2WithID_Constraint(Element, PackageableElement):

    pass
class UML2WithID_Usage(Element, Dependency):

    pass
class UML2WithID_ValuePin(Element, InputPin):

    pass
class UML2WithID_InvocationAction(Element, Action):

    pass
class UML2WithID_QualifierValue(Element):

    pass
class UML2WithID_RaiseExceptionAction(Element, Action):

    pass
class UML2WithID_LiteralNull(Element, LiteralSpecification):

    pass
class UML2WithID_Continuation(Element, InteractionFragment):

    pass
class UML2WithID_PartDecomposition(Element, InteractionOccurrence):

    pass
class UML2WithID_ForkNode(Element, ControlNode):

    pass
class UML2WithID_LiteralSpecification(Element, ValueSpecification):

    pass
class UML2WithID_TimeConstraint(Element, IntervalConstraint):

    pass
class UML2WithID_AddStructuralFeatureValueAction(Element, WriteStructuralFeatureAction):

    pass
class UML2WithID_CallBehaviorAction(Element, CallAction):

    pass
class UML2WithID_InformationItem(Classifier, Element):

    pass
class UML2WithID_FinalNode(Element, ControlNode):

    pass
class UML2WithID_Association(Element, Relationship, Classifier):

    pass
class UML2WithID_Duration(Element, ValueSpecification):

    pass
class UML2WithID_CombinedFragment(Element, InteractionFragment):

    pass
class UML2WithID_SignalTrigger(Element, MessageTrigger):

    pass
class UML2WithID_TestIdentityAction(Element, Action):

    pass
class UML2WithID_EnumerationLiteral(Element, InstanceSpecification):

    pass
class UML2WithID_Comment(Element, TemplateableElement):

    pass
class UML2WithID_ActivityPartition(Element, ActivityGroup, NamedElement):

    pass
class UML2WithID_TemplateParameter(Element):

    pass
class UML2WithID_CreateObjectAction(Element, Action):

    pass
class UML2WithID_Property(Element, StructuralFeature, DeploymentTarget, ConnectableElement):

    pass
class UML2WithID_FinalState(Element, State):

    pass
class UML2WithID_LinkEndData(Element):

    pass
class UML2WithID_DecisionNode(Element, ControlNode):

    pass
class UML2WithID_WriteVariableAction(Element, VariableAction):

    pass
class UML2WithID_Signal(Classifier, Element):

    pass
class UML2WithID_DataType(Classifier, Element):

    pass
class UML2WithID_Extension(Element, Association):

    pass
class UML2WithID_InteractionFragment(Element, NamedElement):

    pass
class UML2WithID_AcceptCallAction(Element, AcceptEventAction):

    pass
class UML2WithID_ConnectableElement(Element, NamedElement, ParameterableElement):

    pass
class UML2WithID_PackageMerge(Element, DirectedRelationship):

    pass
class UML2WithID_PrimitiveFunction(Element, PackageableElement):

    pass
class UML2WithID_ReadLinkObjectEndAction(Element, Action):

    pass
class UML2WithID_Include(Element, DirectedRelationship, NamedElement):

    pass
class UML2WithID_ActivityFinalNode(Element, FinalNode):

    pass
class UML2WithID_WriteStructuralFeatureAction(StructuralFeatureAction, Element):

    pass
class UML2WithID_TemplateParameterSubstitution(Element):

    pass
class UML2WithID_CommunicationPath(Element, Association):

    pass
class UML2WithID_Profile(Package, Element):

    pass
class UML2WithID_ProtocolStateMachine(StateMachine, Element):

    pass
class UML2WithID_ExtensionEnd(Element, Property):

    pass
class UML2WithID_LinkAction(Element, Action):

    pass
class UML2WithID_Abstraction(Element, Dependency):

    pass
class UML2WithID_LiteralInteger(Element, LiteralSpecification):

    pass
class UML2WithID_PrimitiveType(Element, DataType):

    pass
class UML2WithID_BehavioredClassifier(Classifier, Element):

    pass
class UML2WithID_Dependency(Element, DirectedRelationship, PackageableElement):

    pass
class UML2WithID_InstanceSpecification(Element, DeploymentTarget, DeployedArtifact, PackageableElement):

    pass
class UML2WithID_ClearAssociationAction(Element, Action):

    pass
class UML2WithID_TimeExpression(Element, ValueSpecification):

    pass
class UML2WithID_ActivityNode(Element, RedefinableElement):

    pass
class UML2WithID_WriteLinkAction(Element, LinkAction):

    pass
class UML2WithID_Relationship(Element):

    pass
class UML2WithID_Activity(Behavior, Element):

    pass
class UML2WithID_Lifeline(Element, NamedElement):

    pass
class UML2WithID_ClearVariableAction(Element, VariableAction):

    pass
class UML2WithID_Behavior(Element, Class):

    pass
class UML2WithID_ObjectNode(Element, ActivityNode, TypedElement):

    pass
class UML2WithID_ClearStructuralFeatureAction(StructuralFeatureAction, Element):

    pass
class UML2WithID_Classifier(Element, RedefinableElement, Namespace, Type):

    pass
class UML2WithID_DirectedRelationship(Element, Relationship):

    pass
class UML2WithID_ReclassifyObjectAction(Element, Action):

    pass
class UML2WithID_GeneralizationSet(Element, PackageableElement):

    pass
class UML2WithID_PackageableElement(Element, NamedElement, ParameterableElement):

    pass
class UML2WithID_IntervalConstraint(Element, Constraint):

    pass
class UML2WithID_Interaction(Behavior, Element, InteractionFragment):

    pass
class UML2WithID_AddVariableValueAction(WriteVariableAction, Element):

    pass
class UML2WithID_DurationObservationAction(Element, WriteStructuralFeatureAction):

    pass
class UML2WithID_Generalization(Element, DirectedRelationship):

    pass
class UML2WithID_StringExpression(Element, TemplateableElement):

    pass
class UML2WithID_FlowFinalNode(Element, FinalNode):

    pass
class UML2WithID_TemplateSignature(Element):

    pass
class UML2WithID_ProfileApplication(Element, PackageImport):

    pass
class UML2WithID_StateMachine(Behavior, Element):

    pass
class UML2WithID_ConditionalNode(Element, StructuredActivityNode):

    pass
class UML2WithID_TimeTrigger(Element, Trigger):

    pass
class UML2WithID_Clause(Element):

    pass
class UML2WithID_InstanceValue(Element, ValueSpecification):

    pass
class UML2WithID_InformationFlow(Element, DirectedRelationship, PackageableElement):

    pass
class UML2WithID_BehavioralFeature(Element, Feature, Namespace):

    pass
class UML2WithID_NamedElement(Element, TemplateableElement):

    pass
class UML2WithID_StartOwnedBehaviorAction(Element, Action):

    pass
class UML2WithID_ParameterableClassifier(Element, Classifier):

    pass
class UML2WithID_Substitution(Element, Realization):

    pass
class UML2WithID_Interval(Element, ValueSpecification):

    pass
class UML2WithID_InteractionOperand(Element, InteractionFragment, Namespace):

    pass
class UML2WithID_Transition(Element, RedefinableElement):

    pass
class UML2WithID_Implementation(Element, Realization):

    pass
class UML2WithID_CreateLinkObjectAction(CreateLinkAction, Element):

    pass
class UML2WithID_DeploymentTarget(Element, NamedElement):

    pass
class UML2WithID_Extend(Element, DirectedRelationship, NamedElement):

    pass
class UML2WithID_Vertex(Element, NamedElement):

    pass
class UML2WithID_OpaqueExpression(Element, ValueSpecification):

    pass
class UML2WithID_CollaborationOccurrence(Element, NamedElement):

    pass
class UML2WithID_Expression(Element, OpaqueExpression):

    pass
class UML2WithID_RedefinableTemplateSignature(Element, RedefinableElement, TemplateSignature):

    pass
class UML2WithID_Class(BehavioredClassifier, Element, EncapsulatedClassifier):

    pass
class UML2WithID_OutputPin(Element, Pin):

    pass
class UML2WithID_ExecutionOccurrence(Element, InteractionFragment):

    pass
class UML2WithID_ExtensionPoint(Element, RedefinableElement):

    pass
class UML2WithID_DestroyObjectAction(Element, Action):

    pass
class UML2WithID_ActivityEdge(Element, RedefinableElement):

    pass
class UML2WithID_TimeObservationAction(Element, WriteStructuralFeatureAction):

    pass
class UML2WithID_ControlNode(Element, ActivityNode):

    pass
class UML2WithID_Manifestation(Element, Abstraction):

    pass
class UML2WithID_TemplateableElement(Element):

    pass
class UML2WithID_InteractionOccurrence(Element, InteractionFragment):

    pass
class UML2WithID_Reception(Element, BehavioralFeature):

    pass
class UML2WithID_SendObjectAction(Element, InvocationAction):

    pass
class UML2WithID_EventOccurrence(Element, MessageEnd, InteractionFragment):

    pass
class UML2WithID_SendSignalAction(Element, InvocationAction):

    pass
class UML2WithID_PackageImport(Element, DirectedRelationship):

    pass
class UML2WithID_TemplateBinding(Element, DirectedRelationship):

    pass
class UML2WithID_Stereotype(Element, Class):

    pass
class UML2WithID_Action(Element, ExecutableNode):

    pass
class UML2WithID_ReadVariableAction(Element, VariableAction):

    pass
class UML2WithID_ClassifierTemplateParameter(Element, TemplateParameter):

    pass
class UML2WithID_ExpansionNode(Element, ObjectNode):

    pass
class UML2WithID_State(Vertex, Element, RedefinableElement, Namespace):

    pass
class UML2WithID_StructuralFeatureAction(Element, Action):

    pass
class UML2WithID_Interface(Classifier, Element):

    pass
class UML2WithID_CreateLinkAction(WriteLinkAction, Element):

    pass
class UML2WithID_ParameterSet(Element, NamedElement):

    pass
class UML2WithID_Port(Element, Property):

    pass
class UML2WithID_CallOperationAction(Element, CallAction):

    pass
class MultiplicityElement:

    pass
class UML2WithID_Variable(Element, ConnectableElement, TypedElement, MultiplicityElement):

    pass
class UML2WithID_Parameter(Element, ConnectableElement, TypedElement, MultiplicityElement):

    pass
class UML2WithID_Operation(ParameterableElement, BehavioralFeature, MultiplicityElement, Element, TypedElement):

    pass
class UML2WithID_Pin(Element, MultiplicityElement, ObjectNode):

    pass
class UML2WithID_StructuralFeature(Element, TypedElement, MultiplicityElement, Feature):

    pass
class UML2WithID_ConnectorEnd(Element, MultiplicityElement):

    pass
class UML2WithID_CallTrigger(Element, MessageTrigger):

    pass
class ActivityEdge:

    pass
class UML2WithID_ObjectFlow(Element, ActivityEdge):

    pass
class UML2WithID_ControlFlow(Element, ActivityEdge):

    pass
class Node:

    pass
class UML2WithID_ExecutionEnvironment(Element, Node):

    pass
class UML2WithID_Device(Element, Node):

    pass