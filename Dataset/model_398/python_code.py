from datetime import datetime, date, time
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

class InputPin:

    pass
class UML2_ValuePin(InputPin):

    pass
class AcceptEventAction:

    pass
class UML2_AcceptCallAction(AcceptEventAction):

    pass
class State:

    pass
class UML2_FinalState(State):

    pass
class Pin:

    pass
class UML2_OutputPin(Pin):

    pass
class UML2_InputPin(Pin):

    pass
class CallAction:

    pass
class UML2_CallOperationAction(CallAction):

    pass
class UML2_CallBehaviorAction(CallAction):

    pass
class EncapsulatedClassifier:

    pass
class CentralBufferNode:

    pass
class UML2_DataStoreNode(CentralBufferNode):

    pass
class StructuralFeature:

    pass
class ActivityNode:

    pass
class DataType:

    pass
class UML2_Enumeration(DataType):

    pass
class UML2_PrimitiveType(DataType):

    pass
class ActivityEdge:

    pass
class UML2_ControlFlow(ActivityEdge):

    pass
class UML2_ObjectFlow(ActivityEdge):

    pass
class Transition:

    pass
class UML2_ProtocolTransition(Transition):

    pass
class Artifact:

    pass
class UML2_DeploymentSpecification(Artifact):

    pass
class UML2_ExecutableNode(ActivityNode):

    pass
class StateMachine:

    pass
class UML2_ProtocolStateMachine(StateMachine):

    pass
class UML2_ControlNode(ActivityNode):

    pass
class Feature:

    pass
class UML2_Connector(Feature):

    pass
class DeploymentTarget:

    pass
class InteractionOccurrence:

    pass
class UML2_PartDecomposition(InteractionOccurrence):

    pass
class Node:

    pass
class UML2_ExecutionEnvironment(Node):

    pass
class UML2_Device(Node):

    pass
class VariableAction:

    pass
class UML2_ClearVariableAction(VariableAction):

    pass
class UML2_WriteVariableAction(VariableAction):

    pass
class UML2_ReadVariableAction(VariableAction):

    pass
class WriteLinkAction:

    pass
class UML2_CreateLinkAction(WriteLinkAction):

    pass
class UML2_DestroyLinkAction(WriteLinkAction):

    pass
class BehavioralFeature:

    pass
class UML2_Reception(BehavioralFeature):

    pass
class Interval:

    pass
class UML2_TimeInterval(Interval):

    pass
class UML2_DurationInterval(Interval):

    pass
class StructuredActivityNode:

    pass
class UML2_ExpansionRegion(StructuredActivityNode):

    pass
class UML2_ConditionalNode(StructuredActivityNode):

    pass
class UML2_LoopNode(StructuredActivityNode):

    pass
class CreateLinkAction:

    pass
class UML2_CreateLinkObjectAction(CreateLinkAction):

    pass
class WriteStructuralFeatureAction:

    pass
class UML2_AddStructuralFeatureValueAction(WriteStructuralFeatureAction):

    pass
class UML2_RemoveStructuralFeatureValueAction(WriteStructuralFeatureAction):

    pass
class UML2_DurationObservationAction(WriteStructuralFeatureAction):

    pass
class UML2_TimeObservationAction(WriteStructuralFeatureAction):

    pass
class OpaqueExpression:

    pass
class UML2_Expression(OpaqueExpression):

    pass
class ObjectNode:

    pass
class UML2_ActivityParameterNode(ObjectNode):

    pass
class UML2_ExpansionNode(ObjectNode):

    pass
class UML2_CentralBufferNode(ObjectNode):

    pass
class UML2_Pin(ObjectNode):

    pass
class DeployedArtifact:

    pass
class PackageableElement:

    pass
class UML2_InstanceSpecification(DeploymentTarget, PackageableElement, DeployedArtifact):

    pass
class UML2_PrimitiveFunction(PackageableElement):

    pass
class UML2_Type(PackageableElement):

    pass
class UML2_InformationFlow(PackageableElement):

    pass
class UML2_Constraint(PackageableElement):

    pass
class UML2_GeneralizationSet(PackageableElement):

    pass
class UML2_Dependency(PackageableElement):

    pass
class Property:

    pass
class UML2_Port(Property):

    pass
class UML2_ExtensionEnd(Property):

    pass
class ControlNode:

    pass
class UML2_DecisionNode(ControlNode):

    pass
class UML2_InitialNode(ControlNode):

    pass
class UML2_ForkNode(ControlNode):

    pass
class UML2_MergeNode(ControlNode):

    pass
class UML2_FinalNode(ControlNode):

    pass
class UML2_JoinNode(ControlNode):

    pass
class TypedElement:

    pass
class UML2_Operation(BehavioralFeature, TypedElement):

    pass
class UML2_ValueSpecification(TypedElement):

    pass
class UML2_ObjectNode(ActivityNode, TypedElement):

    pass
class UML2_StructuralFeature(Feature, TypedElement):

    pass
class ConnectableElement:

    pass
class UML2_Property(DeploymentTarget, ConnectableElement, StructuralFeature):

    pass
class UML2_Variable(ConnectableElement, TypedElement):

    pass
class UML2_Parameter(ConnectableElement, TypedElement):

    pass
class LinkAction:

    pass
class UML2_WriteLinkAction(LinkAction):

    pass
class UML2_ReadLinkAction(LinkAction):

    pass
class EventOccurrence:

    pass
class UML2_Stop(EventOccurrence):

    pass
class Classifier:

    pass
class UML2_Artifact(Classifier, DeployedArtifact):

    pass
class UML2_BehavioredClassifier(Classifier):

    pass
class UML2_Actor(Classifier):

    pass
class UML2_StructuredClassifier(Classifier):

    pass
class UML2_InformationItem(Classifier):

    pass
class UML2_Association(Classifier):

    pass
class UML2_DataType(Classifier):

    pass
class UML2_ParameterableClassifier(Classifier):

    pass
class UML2_Interface(Classifier):

    pass
class UML2_Signal(Classifier):

    pass
class Abstraction:

    pass
class UML2_Manifestation(Abstraction):

    pass
class UML2_Realization(Abstraction):

    pass
class Vertex:

    pass
class UML2_ConnectionPointReference(Vertex):

    pass
class UML2_Pseudostate(Vertex):

    pass
class InstanceSpecification:

    pass
class UML2_EnumerationLiteral(InstanceSpecification):

    pass
class MessageEnd:

    pass
class UML2_Gate(MessageEnd):

    pass
class UML2_TemplateableClassifier(Classifier):

    pass
class ExecutableNode:

    pass
class UML2_Action(ExecutableNode):

    pass
class Constraint:

    pass
class UML2_IntervalConstraint(Constraint):

    pass
class UML2_InteractionConstraint(Constraint):

    pass
class Package:

    pass
class UML2_Model(Package):

    pass
class UML2_Profile(Package):

    pass
class Action:

    pass
class UML2_ReadIsClassifiedObjectAction(Action):

    pass
class UML2_ClearAssociationAction(Action):

    pass
class UML2_StartOwnedBehaviorAction(Action):

    pass
class UML2_ReplyAction(Action):

    pass
class UML2_DestroyObjectAction(Action):

    pass
class UML2_ApplyFunctionAction(Action):

    pass
class UML2_LinkAction(Action):

    pass
class UML2_RaiseExceptionAction(Action):

    pass
class UML2_AcceptEventAction(Action):

    pass
class UML2_TestIdentityAction(Action):

    pass
class UML2_InvocationAction(Action):

    pass
class UML2_StructuralFeatureAction(Action):

    pass
class UML2_ReadExtentAction(Action):

    pass
class UML2_ReadLinkObjectEndAction(Action):

    pass
class UML2_CreateObjectAction(Action):

    pass
class UML2_ReadSelfAction(Action):

    pass
class UML2_ReclassifyObjectAction(Action):

    pass
class UML2_ReadLinkObjectEndQualifierAction(Action):

    pass
class UML2_VariableAction(Action):

    pass
class Association:

    pass
class UML2_Extension(Association):

    pass
class UML2_CommunicationPath(Association):

    pass
class Class:

    pass
class UML2_Stereotype(Class):

    pass
class UML2_Node(Class, DeploymentTarget):

    pass
class UML2_AssociationClass(Class, Association):

    pass
class UML2_Behavior(Class):

    pass
class UML2_Component(Class):

    pass
class UML2_NamedElement:

    def __init__(self, visibility: str, UML2_NamedElement: "UML2_Classifier" = None, UML2_NamedElement7: "UML2_Namespace" = None):
        self.visibility = visibility
        self.UML2_NamedElement = UML2_NamedElement
        self.UML2_NamedElement7 = UML2_NamedElement7
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def UML2_NamedElement7(self):
        return self.__UML2_NamedElement7

    @UML2_NamedElement7.setter
    def UML2_NamedElement7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_NamedElement__UML2_NamedElement7", None)
        self.__UML2_NamedElement7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Namespace"):
                opp_val = getattr(old_value, "UML2_Namespace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Namespace"):
                opp_val = getattr(value, "UML2_Namespace", None)
                if opp_val is None:
                    setattr(value, "UML2_Namespace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_NamedElement(self):
        return self.__UML2_NamedElement

    @UML2_NamedElement.setter
    def UML2_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_NamedElement__UML2_NamedElement", None)
        self.__UML2_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Classifier2"):
                opp_val = getattr(old_value, "UML2_Classifier2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Classifier2"):
                opp_val = getattr(value, "UML2_Classifier2", None)
                if opp_val is None:
                    setattr(value, "UML2_Classifier2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class RedefinableElement:

    pass
class UML2_ActivityEdge(RedefinableElement):

    pass
class UML2_ExtensionPoint(RedefinableElement):

    pass
class UML2_Transition(RedefinableElement):

    pass
class UML2_RedefinableTemplateSignature(RedefinableElement):

    pass
class UML2_ActivityNode(RedefinableElement):

    pass
class UML2_Feature(RedefinableElement):

    pass
class Type:

    pass
class Namespace:

    pass
class UML2_Package(PackageableElement, Namespace):

    pass
class UML2_State(Namespace, Vertex, RedefinableElement):

    pass
class UML2_Region(Namespace, RedefinableElement):

    pass
class UML2_BehavioralFeature(Namespace, Feature):

    pass
class UML2_StructuredActivityNode(Namespace, Action):

    pass
class MessageTrigger:

    pass
class UML2_AnyTrigger(MessageTrigger):

    pass
class UML2_SignalTrigger(MessageTrigger):

    pass
class UML2_CallTrigger(MessageTrigger):

    pass
class ValueSpecification:

    pass
class UML2_Duration(ValueSpecification):

    pass
class UML2_InstanceValue(ValueSpecification):

    pass
class UML2_Interval(ValueSpecification):

    pass
class UML2_OpaqueExpression(ValueSpecification):

    pass
class UML2_TimeExpression(ValueSpecification):

    pass
class UML2_LiteralSpecification(ValueSpecification):

    pass
class Realization:

    pass
class UML2_Implementation(Realization):

    pass
class UML2_Substitution(Realization):

    pass
class Dependency:

    pass
class UML2_Permission(Dependency):

    pass
class UML2_Abstraction(Dependency):

    pass
class UML2_Usage(Dependency):

    pass
class UML2_Deployment(Dependency):

    pass
class LiteralSpecification:

    pass
class UML2_LiteralUnlimitedNatural(LiteralSpecification):

    pass
class UML2_LiteralNull(LiteralSpecification):

    pass
class UML2_LiteralBoolean(LiteralSpecification):

    pass
class UML2_LiteralString(LiteralSpecification):

    pass
class UML2_LiteralInteger(LiteralSpecification):

    pass
class StructuredClassifier:

    pass
class UML2_EncapsulatedClassifier(StructuredClassifier):

    pass
class BehavioredClassifier:

    pass
class UML2_UseCase(BehavioredClassifier):

    pass
class UML2_Class(EncapsulatedClassifier, BehavioredClassifier):

    pass
class UML2_Collaboration(BehavioredClassifier, StructuredClassifier):

    pass
class IntervalConstraint:

    pass
class UML2_DurationConstraint(IntervalConstraint):

    pass
class UML2_TimeConstraint(IntervalConstraint):

    pass
class WriteVariableAction:

    pass
class UML2_AddVariableValueAction(WriteVariableAction):

    pass
class UML2_RemoveVariableValueAction(WriteVariableAction):

    pass
class UML2_Classifier(Namespace, Type, RedefinableElement):

    pass
class UML2_Generalization:

    pass
class FinalNode:

    pass
class UML2_ActivityFinalNode(FinalNode):

    pass
class UML2_FlowFinalNode(FinalNode):

    pass
class InteractionFragment:

    pass
class UML2_ExecutionOccurrence(InteractionFragment):

    pass
class UML2_CombinedFragment(InteractionFragment):

    pass
class UML2_InteractionOccurrence(InteractionFragment):

    pass
class UML2_EventOccurrence(MessageEnd, InteractionFragment):

    pass
class UML2_Continuation(InteractionFragment):

    pass
class UML2_InteractionOperand(Namespace, InteractionFragment):

    pass
class UML2_StateInvariant(InteractionFragment):

    pass
class Behavior:

    pass
class UML2_StateMachine(Behavior):

    pass
class UML2_Activity(Behavior):

    pass
class UML2_Interaction(Behavior, InteractionFragment):

    pass
class StructuralFeatureAction:

    pass
class UML2_ClearStructuralFeatureAction(StructuralFeatureAction):

    pass
class UML2_ReadStructuralFeatureAction(StructuralFeatureAction):

    pass
class UML2_WriteStructuralFeatureAction(StructuralFeatureAction):

    pass
class InvocationAction:

    pass
class UML2_SendObjectAction(InvocationAction):

    pass
class UML2_SendSignalAction(InvocationAction):

    pass
class UML2_BroadcastSignalAction(InvocationAction):

    pass
class UML2_CallAction(InvocationAction):

    pass
class NamedElement:

    pass
class UML2_Namespace(NamedElement):

    pass
class UML2_ConnectableElement(NamedElement):

    pass
class UML2_Lifeline(NamedElement):

    pass
class UML2_Message(NamedElement):

    pass
class UML2_GeneralOrdering(NamedElement):

    pass
class UML2_ParameterSet(NamedElement):

    pass
class UML2_DeploymentTarget(NamedElement):

    pass
class UML2_MessageEnd(NamedElement):

    pass
class UML2_Extend(NamedElement):

    pass
class UML2_CollaborationOccurrence(NamedElement):

    pass
class UML2_RedefinableElement(NamedElement):

    pass
class UML2_PackageableElement(NamedElement):

    pass
class UML2_InteractionFragment(NamedElement):

    pass
class UML2_TypedElement(NamedElement):

    pass
class UML2_ActivityPartition(NamedElement):

    pass
class UML2_Include(NamedElement):

    pass
class UML2_Trigger(NamedElement):

    pass
class UML2_DeployedArtifact(NamedElement):

    pass
class UML2_Vertex(NamedElement):

    pass
class Trigger:

    pass
class UML2_MessageTrigger(Trigger):

    pass
class UML2_TimeTrigger(Trigger):

    pass
class UML2_ChangeTrigger(Trigger):

    pass