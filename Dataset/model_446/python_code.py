from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class OpaqueExpression:

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

class StateMachine:

    pass
class StructuralFeatureAction:

    pass
class Node:

    pass
class CentralBufferNode:

    pass
class LinkAction:

    pass
class ActivityNode:

    pass
class StructuredActivityNode:

    pass
class Type:

    pass
class StructuredClassifier:

    pass
class Realization:

    pass
class InstanceSpecification:

    pass
class Association:

    pass
class ExecutableNode:

    pass
class WriteLinkAction:

    pass
class WriteStructuralFeatureAction:

    pass
class Package:

    pass
class PackageImport:

    pass
class ActivityGroup:

    pass
class Interval:

    pass
class Transition:

    pass
class LinkEndData:

    pass
class EventOccurrence:

    pass
class FinalNode:

    pass
class Artifact:

    pass
class InputPin:

    pass
class IntervalConstraint:

    pass
class VariableAction:

    pass
class Relationship:

    pass
class CallAction:

    pass
class Property:

    pass
class AcceptEventAction:

    pass
class ActivityEdge:

    pass
class LiteralSpecification:

    pass
class ParameterableElement:

    pass
class Feature:

    pass
class ValueSpecification:

    pass
class MessageTrigger:

    pass
class ControlNode:

    pass
class BehavioralFeature:

    pass
class TemplateSignature:

    pass
class TemplateableElement:

    pass
class Trigger:

    pass
class Behavior:

    pass
class CreateLinkAction:

    pass
class WriteVariableAction:

    pass
class Vertex:

    pass
class Constraint:

    pass
class Namespace:

    pass
class StructuralFeature:

    pass
class State:

    pass
class MultiplicityElement:

    pass
class TypedElement:

    pass
class ConnectableElement:

    pass
class InteractionOccurrence:

    pass
class TemplateParameter:

    pass
class Pin:

    pass
class EncapsulatedClassifier:

    pass
class BehavioredClassifier:

    pass
class RedefinableElement:

    pass
class DirectedRelationship:

    pass
class NamedElement:

    pass
class PackageableElement:

    pass
class Abstraction:

    pass
class MessageEnd:

    pass
class InteractionFragment:

    pass
class Action:

    pass
class DeployedArtifact:

    pass
class Classifier:

    pass
class DataType:

    pass
class Dependency:

    pass
class ObjectNode:

    pass
class DeploymentTarget:

    pass
class Class:

    pass
class Element:

    pass
class UML2WithID_ProtocolTransition(Element, Transition):

    pass
class UML2WithID_Interaction(Element, InteractionFragment, Behavior):

    pass
class UML2WithID_Transition(Element, RedefinableElement):

    pass
class UML2WithID_LiteralBoolean(Element, LiteralSpecification):

    pass
class UML2WithID_Feature(Element, RedefinableElement):

    pass
class UML2WithID_Operation(MultiplicityElement, ParameterableElement, Element, TypedElement, BehavioralFeature):

    pass
class UML2WithID_Relationship(Element):

    pass
class UML2WithID_DestroyLinkAction(WriteLinkAction, Element):

    pass
class UML2WithID_Clause(Element):

    pass
class UML2WithID_AssociationClass(Element, Class, Association):

    pass
class UML2WithID_UseCase(Element, BehavioredClassifier):

    pass
class UML2WithID_ExpansionRegion(Element, StructuredActivityNode):

    pass
class UML2WithID_Property(ConnectableElement, StructuralFeature, DeploymentTarget, Element):

    pass
class UML2WithID_OutputPin(Element, Pin):

    pass
class UML2WithID_TemplateSignature(Element):

    pass
class UML2WithID_Dependency(Element, DirectedRelationship, PackageableElement):

    pass
class UML2WithID_ClassifierTemplateParameter(Element, TemplateParameter):

    pass
class UML2WithID_Realization(Element, Abstraction):

    pass
class UML2WithID_TemplateableElement(Element):

    pass
class UML2WithID_ReadExtentAction(Element, Action):

    pass
class UML2WithID_PartDecomposition(Element, InteractionOccurrence):

    pass
class UML2WithID_WriteStructuralFeatureAction(Element, StructuralFeatureAction):

    pass
class UML2WithID_TimeObservationAction(Element, WriteStructuralFeatureAction):

    pass
class UML2WithID_ActivityGroup(Element):

    pass
class UML2WithID_DataType(Element, Classifier):

    pass
class UML2WithID_EnumerationLiteral(Element, InstanceSpecification):

    pass
class UML2WithID_AcceptCallAction(Element, AcceptEventAction):

    pass
class UML2WithID_Usage(Element, Dependency):

    pass
class UML2WithID_GeneralOrdering(Element, NamedElement):

    pass
class UML2WithID_LinkEndCreationData(Element, LinkEndData):

    pass
class UML2WithID_RemoveVariableValueAction(Element, WriteVariableAction):

    pass
class UML2WithID_DeploymentSpecification(Element, Artifact):

    pass
class UML2WithID_Association(Element, Classifier, Relationship):

    pass
class UML2WithID_ActivityFinalNode(Element, FinalNode):

    pass
class UML2WithID_StructuralFeature(Element, TypedElement, Feature, MultiplicityElement):

    pass
class UML2WithID_TemplateableClassifier(Element, Classifier):

    pass
class UML2WithID_InstanceValue(Element, ValueSpecification):

    pass
class UML2WithID_Gate(Element, MessageEnd):

    pass
class UML2WithID_ApplyFunctionAction(Element, Action):

    pass
class UML2WithID_Node(Element, Class, DeploymentTarget):

    pass
class UML2WithID_DurationInterval(Element, Interval):

    pass
class UML2WithID_Variable(Element, TypedElement, ConnectableElement, MultiplicityElement):

    pass
class UML2WithID_ReclassifyObjectAction(Element, Action):

    pass
class UML2WithID_ReadStructuralFeatureAction(Element, StructuralFeatureAction):

    pass
class UML2WithID_CollaborationOccurrence(Element, NamedElement):

    pass
class UML2WithID_Include(Element, DirectedRelationship, NamedElement):

    pass
class UML2WithID_InformationFlow(Element, DirectedRelationship, PackageableElement):

    pass
class UML2WithID_Port(Element, Property):

    pass
class UML2WithID_Reception(Element, BehavioralFeature):

    pass
class UML2WithID_CreateObjectAction(Element, Action):

    pass
class UML2WithID_ActivityEdge(Element, RedefinableElement):

    pass
class UML2WithID_ExtensionPoint(Element, RedefinableElement):

    pass
class UML2WithID_InformationItem(Element, Classifier):

    pass
class UML2WithID_ControlNode(Element, ActivityNode):

    pass
class UML2WithID_InitialNode(Element, ControlNode):

    pass
class UML2WithID_TemplateBinding(Element, DirectedRelationship):

    pass
class UML2WithID_ExtensionEnd(Element, Property):

    pass
class UML2WithID_PackageImport(Element, DirectedRelationship):

    pass
class UML2WithID_DataStoreNode(Element, CentralBufferNode):

    pass
class UML2WithID_TimeConstraint(Element, IntervalConstraint):

    pass
class UML2WithID_Component(Element, Class):

    pass
class UML2WithID_ExecutableNode(Element, ActivityNode):

    pass
class UML2WithID_CentralBufferNode(Element, ObjectNode):

    pass
class UML2WithID_CallOperationAction(Element, CallAction):

    pass
class UML2WithID_Trigger(Element, NamedElement):

    pass
class UML2WithID_ConnectableElement(Element, NamedElement, ParameterableElement):

    pass
class UML2WithID_LiteralSpecification(Element, ValueSpecification):

    pass
class UML2WithID_Device(Element, Node):

    pass
class UML2WithID_JoinNode(Element, ControlNode):

    pass
class UML2WithID_Behavior(Element, Class):

    pass
class UML2WithID_InteractionOperand(Element, InteractionFragment, Namespace):

    pass
class UML2WithID_Message(Element, NamedElement):

    pass
class UML2WithID_Extension(Element, Association):

    pass
class UML2WithID_DurationConstraint(Element, IntervalConstraint):

    pass
class UML2WithID_ParameterSet(Element, NamedElement):

    pass
class UML2WithID_ClearStructuralFeatureAction(Element, StructuralFeatureAction):

    pass
class UML2WithID_TestIdentityAction(Element, Action):

    pass
class UML2WithID_RedefinableTemplateSignature(Element, TemplateSignature, RedefinableElement):

    pass
class UML2WithID_MessageTrigger(Element, Trigger):

    pass
class UML2WithID_TimeExpression(Element, ValueSpecification):

    pass
class UML2WithID_StateMachine(Element, Behavior):

    pass
class UML2WithID_CombinedFragment(InteractionFragment, Element):

    pass
class UML2WithID_Profile(Element, Package):

    pass
class UML2WithID_DecisionNode(Element, ControlNode):

    pass
class UML2WithID_ReadLinkObjectEndAction(Element, Action):

    pass
class UML2WithID_ActivityNode(Element, RedefinableElement):

    pass
class UML2WithID_StructuredActivityNode(ActivityGroup, Action, Namespace, Element):

    pass
class UML2WithID_ReadVariableAction(Element, VariableAction):

    pass
class UML2WithID_Slot(Element):

    pass
class UML2WithID_Classifier(Element, Namespace, Type, RedefinableElement):

    pass
class UML2WithID_Deployment(Element, Dependency):

    pass
class UML2WithID_Pin(MultiplicityElement, ObjectNode, Element):

    pass
class UML2WithID_ForkNode(Element, ControlNode):

    pass
class UML2WithID_TimeTrigger(Element, Trigger):

    pass
class UML2WithID_StateInvariant(InteractionFragment, Element):

    pass
class UML2WithID_Constraint(Element, PackageableElement):

    pass
class UML2WithID_InstanceSpecification(Element, DeployedArtifact, DeploymentTarget, PackageableElement):

    pass
class UML2WithID_Type(Element, PackageableElement):

    pass
class UML2WithID_Connector(Element, Feature):

    pass
class UML2WithID_Activity(Element, Behavior):

    pass
class UML2WithID_ProfileApplication(Element, PackageImport):

    pass
class UML2WithID_ReadIsClassifiedObjectAction(Element, Action):

    pass
class UML2WithID_RemoveStructuralFeatureValueAction(Element, WriteStructuralFeatureAction):

    pass
class UML2WithID_MergeNode(Element, ControlNode):

    pass
class UML2WithID_AddVariableValueAction(Element, WriteVariableAction):

    pass
class UML2WithID_ChangeTrigger(Element, Trigger):

    pass
class UML2WithID_Expression(Element, OpaqueExpression):

    pass
class UML2WithID_Actor(Element, Classifier):

    pass
class UML2WithID_Vertex(Element, NamedElement):

    pass
class UML2WithID_Package(Element, Namespace, PackageableElement):

    pass
class UML2WithID_OperationTemplateParameter(Element, TemplateParameter):

    pass
class UML2WithID_ClearVariableAction(Element, VariableAction):

    pass
class UML2WithID_EncapsulatedClassifier(Element, StructuredClassifier):

    pass
class UML2WithID_BehavioralFeature(Element, Feature, Namespace):

    pass
class UML2WithID_Artifact(Element, Classifier, DeployedArtifact):

    pass
class UML2WithID_StructuralFeatureAction(Element, Action):

    pass
class UML2WithID_LiteralUnlimitedNatural(Element, LiteralSpecification):

    pass
class UML2WithID_Interval(Element, ValueSpecification):

    pass
class UML2WithID_VariableAction(Element, Action):

    pass
class UML2WithID_Substitution(Element, Realization):

    pass
class UML2WithID_ExceptionHandler(Element):

    pass
class UML2WithID_InteractionConstraint(Constraint, Element):

    pass
class UML2WithID_RedefinableElement(Element, NamedElement):

    pass
class UML2WithID_InterruptibleActivityRegion(ActivityGroup, Element):

    pass
class UML2WithID_ExecutionEnvironment(Node, Element):

    pass
class UML2WithID_FinalNode(Element, ControlNode):

    pass
class UML2WithID_PackageableElement(Element, NamedElement, ParameterableElement):

    pass
class UML2WithID_AddStructuralFeatureValueAction(Element, WriteStructuralFeatureAction):

    pass
class UML2WithID_Comment(Element, TemplateableElement):

    pass
class UML2WithID_InputPin(Pin, Element):

    pass
class UML2WithID_Region(Element, Namespace, RedefinableElement):

    pass
class UML2WithID_DestroyObjectAction(Element, Action):

    pass
class UML2WithID_PrimitiveFunction(Element, PackageableElement):

    pass
class UML2WithID_Parameter(MultiplicityElement, TypedElement, ConnectableElement, Element):

    pass
class UML2WithID_QualifierValue(Element):

    pass
class UML2WithID_LinkEndData(Element):

    pass
class UML2WithID_FlowFinalNode(Element, FinalNode):

    pass
class UML2WithID_Stop(Element, EventOccurrence):

    pass
class UML2WithID_ElementImport(Element, DirectedRelationship):

    pass
class UML2WithID_ValuePin(InputPin, Element):

    pass
class UML2WithID_Implementation(Element, Realization):

    pass
class UML2WithID_PackageMerge(Element, DirectedRelationship):

    pass
class UML2WithID_ReadLinkObjectEndQualifierAction(Element, Action):

    pass
class UML2WithID_GeneralizationSet(Element, PackageableElement):

    pass
class UML2WithID_Abstraction(Element, Dependency):

    pass
class UML2WithID_CreateLinkAction(WriteLinkAction, Element):

    pass
class UML2WithID_Signal(Element, Classifier):

    pass
class UML2WithID_TemplateParameterSubstitution(Element):

    pass
class UML2WithID_Manifestation(Element, Abstraction):

    pass
class UML2WithID_Collaboration(Element, StructuredClassifier, BehavioredClassifier):

    pass
class UML2WithID_ActivityParameterNode(Element, ObjectNode):

    pass
class UML2WithID_ValueSpecification(Element, TypedElement, ParameterableElement):

    pass
class UML2WithID_InvocationAction(Element, Action):

    pass
class UML2WithID_DeployedArtifact(Element, NamedElement):

    pass
class UML2WithID_Namespace(Element, NamedElement):

    pass
class UML2WithID_ConnectableElementTemplateParameter(Element, TemplateParameter):

    pass
class UML2WithID_ReadLinkAction(Element, LinkAction):

    pass
class UML2WithID_ConditionalNode(Element, StructuredActivityNode):

    pass
class UML2WithID_Action(Element, ExecutableNode):

    pass
class UML2WithID_ExecutionOccurrence(InteractionFragment, Element):

    pass
class UML2WithID_InteractionOccurrence(Element, InteractionFragment):

    pass
class UML2WithID_StartOwnedBehaviorAction(Element, Action):

    pass
class UML2WithID_InteractionFragment(Element, NamedElement):

    pass
class UML2WithID_ObjectFlow(ActivityEdge, Element):

    pass
class UML2WithID_LiteralNull(Element, LiteralSpecification):

    pass
class UML2WithID_StringExpression(Element, TemplateableElement):

    pass
class UML2WithID_DirectedRelationship(Element, Relationship):

    pass
class UML2WithID_Extend(Element, DirectedRelationship, NamedElement):

    pass
class UML2WithID_ReplyAction(Element, Action):

    pass
class UML2WithID_NamedElement(Element, TemplateableElement):

    pass
class UML2WithID_ProtocolConformance(Element, DirectedRelationship):

    pass
class UML2WithID_Interface(Element, Classifier):

    pass
class UML2WithID_DeploymentTarget(Element, NamedElement):

    pass
class UML2WithID_ReadSelfAction(Element, Action):

    pass
class UML2WithID_AnyTrigger(Element, MessageTrigger):

    pass
class UML2WithID_ParameterableElement(Element):

    pass
class UML2WithID_Model(Element, Package):

    pass
class UML2WithID_TypedElement(Element, NamedElement):

    pass
class UML2WithID_ParameterableClassifier(Element, Classifier):

    pass
class UML2WithID_LiteralString(Element, LiteralSpecification):

    pass
class UML2WithID_OpaqueExpression(Element, ValueSpecification):

    pass
class UML2WithID_EventOccurrence(InteractionFragment, MessageEnd, Element):

    pass
class UML2WithID_Pseudostate(Element, Vertex):

    pass
class UML2WithID_IntervalConstraint(Constraint, Element):

    pass
class UML2WithID_AcceptEventAction(Element, Action):

    pass
class UML2WithID_DurationObservationAction(Element, WriteStructuralFeatureAction):

    pass
class UML2WithID_ConnectorEnd(MultiplicityElement, Element):

    pass
class UML2WithID_Enumeration(Element, DataType):

    pass
class UML2WithID_Generalization(Element, DirectedRelationship):

    pass
class UML2WithID_LinkAction(Element, Action):

    pass
class UML2WithID_ActivityPartition(Element, ActivityGroup, NamedElement):

    pass
class UML2WithID_Stereotype(Element, Class):

    pass
class UML2WithID_WriteLinkAction(Element, LinkAction):

    pass
class UML2WithID_TimeInterval(Element, Interval):

    pass
class UML2WithID_CreateLinkObjectAction(Element, CreateLinkAction):

    pass
class UML2WithID_SignalTrigger(Element, MessageTrigger):

    pass
class UML2WithID_State(Element, Vertex, Namespace, RedefinableElement):

    pass
class UML2WithID_ExpansionNode(Element, ObjectNode):

    pass
class UML2WithID_ClearAssociationAction(Element, Action):

    pass
class UML2WithID_Duration(Element, ValueSpecification):

    pass
class UML2WithID_BehavioredClassifier(Element, Classifier):

    pass
class UML2WithID_CallTrigger(Element, MessageTrigger):

    pass
class UML2WithID_ProtocolStateMachine(Element, StateMachine):

    pass
class UML2WithID_WriteVariableAction(Element, VariableAction):

    pass
class UML2WithID_Permission(Element, Dependency):

    pass
class UML2WithID_Continuation(Element, InteractionFragment):

    pass
class UML2WithID_LiteralInteger(Element, LiteralSpecification):

    pass
class UML2WithID_RaiseExceptionAction(Element, Action):

    pass
class UML2WithID_CallBehaviorAction(Element, CallAction):

    pass
class UML2WithID_ControlFlow(Element, ActivityEdge):

    pass
class UML2WithID_Lifeline(Element, NamedElement):

    pass
class UML2WithID_LoopNode(StructuredActivityNode, Element):

    pass
class UML2WithID_ConnectionPointReference(Element, Vertex):

    pass
class UML2WithID_PrimitiveType(Element, DataType):

    pass
class UML2WithID_TemplateParameter(Element):

    pass
class UML2WithID_ObjectNode(Element, TypedElement, ActivityNode):

    pass
class UML2WithID_MessageEnd(Element, NamedElement):

    pass
class UML2WithID_CommunicationPath(Element, Association):

    pass
class UML2WithID_MultiplicityElement(Element):

    pass
class UML2WithID_StructuredClassifier(Element, Classifier):

    pass
class UML2WithID_FinalState(Element, State):

    pass
class UML2WithID_Class(Element, BehavioredClassifier, EncapsulatedClassifier):

    pass
class InvocationAction:

    pass
class UML2WithID_CallAction(Element, InvocationAction):

    pass
class UML2WithID_SendObjectAction(Element, InvocationAction):

    pass
class UML2WithID_SendSignalAction(Element, InvocationAction):

    pass
class UML2WithID_BroadcastSignalAction(Element, InvocationAction):

    pass