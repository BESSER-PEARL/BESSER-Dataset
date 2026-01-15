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
class AggregationKind(Enum):
    composite = "composite"
    none = "none"
    shared = "shared"
class ParameterDirectionKind(Enum):
    in = "in"
    inout = "inout"
    out = "out"
    return = "return"


############################################
# Definition of Classes
############################################

class StateMachine:

    pass
class UML2_ProtocolStateMachine(StateMachine):

    pass
class ExecutableNode:

    pass
class UML2_Action(ExecutableNode):

    pass
class TemplateSignature:

    pass
class EncapsulatedClassifier:

    pass
class Artifact:

    pass
class UML2_DeploymentSpecification(Artifact):

    pass
class WriteLinkAction:

    pass
class UML2_CreateLinkAction(WriteLinkAction):

    pass
class UML2_DestroyLinkAction(WriteLinkAction):

    pass
class Abstraction:

    pass
class UML2_Realization(Abstraction):

    pass
class UML2_Manifestation(Abstraction):

    pass
class InstanceSpecification:

    pass
class UML2_EnumerationLiteral(InstanceSpecification):

    pass
class WriteVariableAction:

    pass
class UML2_AddVariableValueAction(WriteVariableAction):

    pass
class UML2_RemoveVariableValueAction(WriteVariableAction):

    pass
class Association:

    pass
class UML2_Extension(Association):

    pass
class UML2_CommunicationPath(Association):

    pass
class TemplateableElement:

    pass
class UML2_StringExpression(TemplateableElement):

    pass
class UML2_Comment(TemplateableElement):

    pass
class ActivityNode:

    pass
class UML2_ControlNode(ActivityNode):

    pass
class UML2_ExecutableNode(ActivityNode):

    pass
class TemplateParameter:

    pass
class UML2_ConnectableElementTemplateParameter(TemplateParameter):

    pass
class UML2_OperationTemplateParameter(TemplateParameter):

    pass
class UML2_ClassifierTemplateParameter(TemplateParameter):

    pass
class AcceptEventAction:

    pass
class UML2_AcceptCallAction(AcceptEventAction):

    pass
class EventOccurrence:

    pass
class UML2_Stop(EventOccurrence):

    pass
class Relationship:

    pass
class UML2_DirectedRelationship(Relationship):

    pass
class StructuredClassifier:

    pass
class UML2_EncapsulatedClassifier(StructuredClassifier):

    pass
class InteractionFragment:

    pass
class UML2_CombinedFragment(InteractionFragment):

    pass
class UML2_InteractionOccurrence(InteractionFragment):

    pass
class UML2_ExecutionOccurrence(InteractionFragment):

    pass
class UML2_Continuation(InteractionFragment):

    pass
class UML2_StateInvariant(InteractionFragment):

    pass
class State:

    pass
class UML2_FinalState(State):

    pass
class FinalNode:

    pass
class UML2_FlowFinalNode(FinalNode):

    pass
class UML2_ActivityFinalNode(FinalNode):

    pass
class StructuredActivityNode:

    pass
class UML2_ConditionalNode(StructuredActivityNode):

    pass
class UML2_ExpansionRegion(StructuredActivityNode):

    pass
class UML2_LoopNode(StructuredActivityNode):

    pass
class ActivityGroup:

    pass
class UML2_InterruptibleActivityRegion(ActivityGroup):

    pass
class Feature:

    pass
class UML2_Connector(Feature):

    pass
class Pin:

    pass
class UML2_OutputPin(Pin):

    pass
class Realization:

    pass
class UML2_Implementation(Realization):

    pass
class UML2_Substitution(Realization):

    pass
class LinkEndData:

    pass
class UML2_LinkEndCreationData(LinkEndData):

    pass
class StructuralFeature:

    pass
class CentralBufferNode:

    pass
class UML2_DataStoreNode(CentralBufferNode):

    pass
class PackageImport:

    pass
class UML2_ProfileApplication(PackageImport):

    pass
class InputPin:

    pass
class UML2_ValuePin(InputPin):

    pass
class Node:

    pass
class UML2_ExecutionEnvironment(Node):

    pass
class UML2_Device(Node):

    pass
class Dependency:

    pass
class UML2_Permission(Dependency):

    pass
class UML2_Deployment(Dependency):

    pass
class UML2_Abstraction(Dependency):

    pass
class UML2_Usage(Dependency):

    pass
class WriteStructuralFeatureAction:

    pass
class UML2_TimeObservationAction(WriteStructuralFeatureAction):

    pass
class UML2_DurationObservationAction(WriteStructuralFeatureAction):

    pass
class UML2_RemoveStructuralFeatureValueAction(WriteStructuralFeatureAction):

    pass
class UML2_AddStructuralFeatureValueAction(WriteStructuralFeatureAction):

    pass
class MessageTrigger:

    pass
class UML2_AnyTrigger(MessageTrigger):

    pass
class UML2_CallTrigger(MessageTrigger):

    pass
class UML2_SignalTrigger(MessageTrigger):

    pass
class LinkAction:

    pass
class UML2_ReadLinkAction(LinkAction):

    pass
class UML2_WriteLinkAction(LinkAction):

    pass
class VariableAction:

    pass
class UML2_ReadVariableAction(VariableAction):

    pass
class UML2_ClearVariableAction(VariableAction):

    pass
class UML2_WriteVariableAction(VariableAction):

    pass
class ObjectNode:

    pass
class UML2_ActivityParameterNode(ObjectNode):

    pass
class UML2_ExpansionNode(ObjectNode):

    pass
class UML2_CentralBufferNode(ObjectNode):

    pass
class Property:

    pass
class UML2_Port(Property):

    pass
class UML2_ExtensionEnd(Property):

    pass
class Transition:

    pass
class UML2_ProtocolTransition(Transition):

    pass
class Interval:

    pass
class UML2_TimeInterval(Interval):

    pass
class Constraint:

    pass
class UML2_InteractionConstraint(Constraint):

    pass
class UML2_IntervalConstraint(Constraint):

    pass
class Trigger:

    pass
class UML2_TimeTrigger(Trigger):

    pass
class UML2_ChangeTrigger(Trigger):

    pass
class UML2_MessageTrigger(Trigger):

    pass
class MessageEnd:

    pass
class UML2_EventOccurrence(InteractionFragment, MessageEnd):

    pass
class UML2_Gate(MessageEnd):

    pass
class DataType:

    pass
class UML2_PrimitiveType(DataType):

    pass
class UML2_Enumeration(DataType):

    pass
class ConnectableElement:

    pass
class InteractionOccurrence:

    pass
class UML2_PartDecomposition(InteractionOccurrence):

    pass
class UML2_DurationInterval(Interval):

    pass
class CallAction:

    pass
class UML2_CallOperationAction(CallAction):

    pass
class UML2_CallBehaviorAction(CallAction):

    pass
class CreateLinkAction:

    pass
class UML2_CreateLinkObjectAction(CreateLinkAction):

    pass
class Behavior:

    pass
class UML2_StateMachine(Behavior):

    pass
class UML2_Interaction(InteractionFragment, Behavior):

    pass
class UML2_Activity(Behavior):

    pass
class UML2_InputPin(Pin):

    pass
class StructuralFeatureAction:

    pass
class UML2_ClearStructuralFeatureAction(StructuralFeatureAction):

    pass
class UML2_ReadStructuralFeatureAction(StructuralFeatureAction):

    pass
class OpaqueExpression:

    pass
class UML2_Expression(OpaqueExpression):

    pass
class InvocationAction:

    pass
class UML2_CallAction(InvocationAction):

    pass
class UML2_SendObjectAction(InvocationAction):

    pass
class UML2_BroadcastSignalAction(InvocationAction):

    pass
class UML2_SendSignalAction(InvocationAction):

    pass
class MultiplicityElement:

    pass
class UML2_ConnectorEnd(MultiplicityElement):

    pass
class UML2_Pin(ObjectNode, MultiplicityElement):

    pass
class TypedElement:

    pass
class UML2_ObjectNode(TypedElement, ActivityNode):

    pass
class UML2_Variable(TypedElement, MultiplicityElement, ConnectableElement):

    pass
class UML2_Parameter(TypedElement, MultiplicityElement, ConnectableElement):

    def __init__(self, direction: str, UML2_Parameter: "UML2_Operation" = None):
        self.direction = direction
        self.UML2_Parameter = UML2_Parameter
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def UML2_Parameter(self):
        return self.__UML2_Parameter

    @UML2_Parameter.setter
    def UML2_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Parameter__UML2_Parameter", None)
        self.__UML2_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Operation"):
                opp_val = getattr(old_value, "UML2_Operation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Operation"):
                opp_val = getattr(value, "UML2_Operation", None)
                if opp_val is None:
                    setattr(value, "UML2_Operation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UML2_StructuralFeature(MultiplicityElement, TypedElement, Feature):

    def __init__(self, isReadOnly: bool, UML2_StructuralFeature: "UML2_StructuralFeatureAction" = None, UML2_StructuralFeature35: "UML2_Slot" = None):
        self.isReadOnly = isReadOnly
        self.UML2_StructuralFeature = UML2_StructuralFeature
        self.UML2_StructuralFeature35 = UML2_StructuralFeature35
        
    @property
    def isReadOnly(self) -> bool:
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: bool):
        self.__isReadOnly = isReadOnly

    @property
    def UML2_StructuralFeature35(self):
        return self.__UML2_StructuralFeature35

    @UML2_StructuralFeature35.setter
    def UML2_StructuralFeature35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_StructuralFeature__UML2_StructuralFeature35", None)
        self.__UML2_StructuralFeature35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Slot34"):
                opp_val = getattr(old_value, "UML2_Slot34", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Slot34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Slot34"):
                opp_val = getattr(value, "UML2_Slot34", None)
                setattr(value, "UML2_Slot34", self)

    @property
    def UML2_StructuralFeature(self):
        return self.__UML2_StructuralFeature

    @UML2_StructuralFeature.setter
    def UML2_StructuralFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_StructuralFeature__UML2_StructuralFeature", None)
        self.__UML2_StructuralFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_StructuralFeatureAction"):
                opp_val = getattr(old_value, "UML2_StructuralFeatureAction", None)
                if opp_val == self:
                    setattr(old_value, "UML2_StructuralFeatureAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_StructuralFeatureAction"):
                opp_val = getattr(value, "UML2_StructuralFeatureAction", None)
                setattr(value, "UML2_StructuralFeatureAction", self)

class BehavioralFeature:

    pass
class UML2_Reception(BehavioralFeature):

    pass
class Element:

    pass
class UML2_LinkEndData(Element):

    pass
class UML2_Clause(Element):

    pass
class UML2_MultiplicityElement(Element):

    def __init__(self, isOrdered: bool, isUnique: bool, lower: int, upper: str):
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.lower = lower
        self.upper = upper
        
    @property
    def lower(self) -> int:
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower

    @property
    def isUnique(self) -> bool:
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: bool):
        self.__isUnique = isUnique

    @property
    def upper(self) -> str:
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper

    @property
    def isOrdered(self) -> bool:
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: bool):
        self.__isOrdered = isOrdered

class UML2_ExceptionHandler(Element):

    pass
class UML2_QualifierValue(Element):

    pass
class UML2_TemplateSignature(Element):

    pass
class UML2_Relationship(Element):

    pass
class UML2_ActivityGroup(Element):

    pass
class UML2_ParameterableElement(Element):

    pass
class UML2_TemplateParameter(Element):

    pass
class UML2_TemplateableElement(Element):

    pass
class UML2_TemplateParameterSubstitution(Element):

    pass
class Type:

    pass
class Package:

    pass
class UML2_Profile(Package):

    pass
class UML2_Model(Package):

    pass
class UML2_Slot(Element):

    pass
class DeployedArtifact:

    pass
class RedefinableElement:

    pass
class UML2_ActivityEdge(RedefinableElement):

    pass
class UML2_RedefinableTemplateSignature(TemplateSignature, RedefinableElement):

    pass
class UML2_ExtensionPoint(RedefinableElement):

    pass
class UML2_ActivityNode(RedefinableElement):

    pass
class UML2_Transition(RedefinableElement):

    pass
class ActivityEdge:

    pass
class UML2_ObjectFlow(ActivityEdge):

    pass
class UML2_ControlFlow(ActivityEdge):

    pass
class Action:

    pass
class UML2_InvocationAction(Action):

    pass
class UML2_StartOwnedBehaviorAction(Action):

    pass
class UML2_ApplyFunctionAction(Action):

    pass
class UML2_StructuralFeatureAction(Action):

    pass
class UML2_ReadSelfAction(Action):

    pass
class UML2_TestIdentityAction(Action):

    pass
class UML2_ReplyAction(Action):

    pass
class UML2_ReadLinkObjectEndQualifierAction(Action):

    pass
class UML2_ReadIsClassifiedObjectAction(Action):

    pass
class UML2_ReadLinkObjectEndAction(Action):

    pass
class UML2_RaiseExceptionAction(Action):

    pass
class UML2_ReclassifyObjectAction(Action):

    pass
class UML2_DestroyObjectAction(Action):

    pass
class UML2_CreateObjectAction(Action):

    pass
class UML2_AcceptEventAction(Action):

    pass
class UML2_VariableAction(Action):

    pass
class UML2_ClearAssociationAction(Action):

    pass
class UML2_LinkAction(Action):

    pass
class ParameterableElement:

    pass
class UML2_Operation(ParameterableElement, TypedElement, BehavioralFeature, MultiplicityElement):

    pass
class UML2_ValueSpecification(ParameterableElement, TypedElement):

    pass
class NamedElement:

    pass
class UML2_DeployedArtifact(NamedElement):

    pass
class UML2_CollaborationOccurrence(NamedElement):

    pass
class UML2_DeploymentTarget(NamedElement):

    pass
class UML2_GeneralOrdering(NamedElement):

    pass
class UML2_ParameterSet(NamedElement):

    pass
class UML2_PackageableElement(ParameterableElement, NamedElement):

    pass
class UML2_RedefinableElement(NamedElement):

    pass
class UML2_InteractionFragment(NamedElement):

    pass
class UML2_Namespace(NamedElement):

    pass
class UML2_Lifeline(NamedElement):

    pass
class UML2_TypedElement(NamedElement):

    pass
class UML2_Message(NamedElement):

    pass
class UML2_MessageEnd(NamedElement):

    pass
class UML2_Vertex(NamedElement):

    pass
class UML2_Trigger(NamedElement):

    pass
class UML2_ActivityPartition(ActivityGroup, NamedElement):

    pass
class UML2_ConnectableElement(ParameterableElement, NamedElement):

    pass
class DirectedRelationship:

    pass
class UML2_PackageImport(DirectedRelationship):

    pass
class UML2_ProtocolConformance(DirectedRelationship):

    pass
class UML2_Extend(DirectedRelationship, NamedElement):

    pass
class UML2_Include(DirectedRelationship, NamedElement):

    pass
class UML2_ElementImport(DirectedRelationship):

    pass
class UML2_TemplateBinding(DirectedRelationship):

    pass
class UML2_PackageMerge(DirectedRelationship):

    pass
class LiteralSpecification:

    pass
class UML2_LiteralString(LiteralSpecification):

    pass
class UML2_LiteralBoolean(LiteralSpecification):

    pass
class UML2_LiteralInteger(LiteralSpecification):

    pass
class UML2_LiteralUnlimitedNatural(LiteralSpecification):

    pass
class UML2_LiteralNull(LiteralSpecification):

    pass
class IntervalConstraint:

    pass
class UML2_DurationConstraint(IntervalConstraint):

    pass
class UML2_TimeConstraint(IntervalConstraint):

    pass
class ControlNode:

    pass
class UML2_FinalNode(ControlNode):

    pass
class UML2_JoinNode(ControlNode):

    pass
class UML2_InitialNode(ControlNode):

    pass
class UML2_DecisionNode(ControlNode):

    pass
class UML2_MergeNode(ControlNode):

    pass
class UML2_ForkNode(ControlNode):

    pass
class ValueSpecification:

    pass
class UML2_Duration(ValueSpecification):

    pass
class UML2_TimeExpression(ValueSpecification):

    pass
class UML2_Interval(ValueSpecification):

    pass
class UML2_InstanceValue(ValueSpecification):

    pass
class UML2_OpaqueExpression(ValueSpecification):

    pass
class UML2_LiteralSpecification(ValueSpecification):

    pass
class Namespace:

    pass
class UML2_StructuredActivityNode(ActivityGroup, Namespace, Action):

    pass
class UML2_BehavioralFeature(Namespace, Feature):

    pass
class UML2_InteractionOperand(InteractionFragment, Namespace):

    pass
class UML2_Classifier(Type, RedefinableElement, Namespace):

    def __init__(self, isAbstract: bool, UML2_Classifier5: set["UML2_Feature"] = None, UML2_Classifier7: set["UML2_NamedElement"] = None, UML2_Classifier9: set["UML2_Generalization"] = None, UML2_Classifier: "UML2_InstanceSpecification" = None, UML2_Classifier14: "UML2_Feature" = None, UML2_Classifier53: "UML2_CreateObjectAction" = None, UML2_Classifier64: "UML2_Generalization" = None, UML2_Classifier66: "UML2_Class" = None, UML2_Classifier76: "UML2_Action" = None):
        self.isAbstract = isAbstract
        self.UML2_Classifier5 = UML2_Classifier5 if UML2_Classifier5 is not None else set()
        self.UML2_Classifier7 = UML2_Classifier7 if UML2_Classifier7 is not None else set()
        self.UML2_Classifier9 = UML2_Classifier9 if UML2_Classifier9 is not None else set()
        self.UML2_Classifier = UML2_Classifier
        self.UML2_Classifier14 = UML2_Classifier14
        self.UML2_Classifier53 = UML2_Classifier53
        self.UML2_Classifier64 = UML2_Classifier64
        self.UML2_Classifier66 = UML2_Classifier66
        self.UML2_Classifier76 = UML2_Classifier76
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def UML2_Classifier(self):
        return self.__UML2_Classifier

    @UML2_Classifier.setter
    def UML2_Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier", None)
        self.__UML2_Classifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_InstanceSpecification3"):
                opp_val = getattr(old_value, "UML2_InstanceSpecification3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_InstanceSpecification3"):
                opp_val = getattr(value, "UML2_InstanceSpecification3", None)
                if opp_val is None:
                    setattr(value, "UML2_InstanceSpecification3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Classifier53(self):
        return self.__UML2_Classifier53

    @UML2_Classifier53.setter
    def UML2_Classifier53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier53", None)
        self.__UML2_Classifier53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_CreateObjectAction"):
                opp_val = getattr(old_value, "UML2_CreateObjectAction", None)
                if opp_val == self:
                    setattr(old_value, "UML2_CreateObjectAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_CreateObjectAction"):
                opp_val = getattr(value, "UML2_CreateObjectAction", None)
                setattr(value, "UML2_CreateObjectAction", self)

    @property
    def UML2_Classifier7(self):
        return self.__UML2_Classifier7

    @UML2_Classifier7.setter
    def UML2_Classifier7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier7", None)
        self.__UML2_Classifier7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_NamedElement"):
                    opp_val = getattr(item, "UML2_NamedElement", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_NamedElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_NamedElement"):
                    opp_val = getattr(item, "UML2_NamedElement", None)
                    
                    setattr(item, "UML2_NamedElement", self)
                    

    @property
    def UML2_Classifier64(self):
        return self.__UML2_Classifier64

    @UML2_Classifier64.setter
    def UML2_Classifier64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier64", None)
        self.__UML2_Classifier64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Generalization63"):
                opp_val = getattr(old_value, "UML2_Generalization63", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Generalization63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Generalization63"):
                opp_val = getattr(value, "UML2_Generalization63", None)
                setattr(value, "UML2_Generalization63", self)

    @property
    def UML2_Classifier5(self):
        return self.__UML2_Classifier5

    @UML2_Classifier5.setter
    def UML2_Classifier5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier5", None)
        self.__UML2_Classifier5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Feature"):
                    opp_val = getattr(item, "UML2_Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Feature"):
                    opp_val = getattr(item, "UML2_Feature", None)
                    
                    setattr(item, "UML2_Feature", self)
                    

    @property
    def UML2_Classifier14(self):
        return self.__UML2_Classifier14

    @UML2_Classifier14.setter
    def UML2_Classifier14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier14", None)
        self.__UML2_Classifier14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Feature13"):
                opp_val = getattr(old_value, "UML2_Feature13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Feature13"):
                opp_val = getattr(value, "UML2_Feature13", None)
                if opp_val is None:
                    setattr(value, "UML2_Feature13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Classifier76(self):
        return self.__UML2_Classifier76

    @UML2_Classifier76.setter
    def UML2_Classifier76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier76", None)
        self.__UML2_Classifier76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Action"):
                opp_val = getattr(old_value, "UML2_Action", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Action", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Action"):
                opp_val = getattr(value, "UML2_Action", None)
                setattr(value, "UML2_Action", self)

    @property
    def UML2_Classifier66(self):
        return self.__UML2_Classifier66

    @UML2_Classifier66.setter
    def UML2_Classifier66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier66", None)
        self.__UML2_Classifier66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Class"):
                opp_val = getattr(old_value, "UML2_Class", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Class"):
                opp_val = getattr(value, "UML2_Class", None)
                if opp_val is None:
                    setattr(value, "UML2_Class", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Classifier9(self):
        return self.__UML2_Classifier9

    @UML2_Classifier9.setter
    def UML2_Classifier9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier9", None)
        self.__UML2_Classifier9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Generalization"):
                    opp_val = getattr(item, "UML2_Generalization", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Generalization", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Generalization"):
                    opp_val = getattr(item, "UML2_Generalization", None)
                    
                    setattr(item, "UML2_Generalization", self)
                    

class UML2_Region(RedefinableElement, Namespace):

    pass
class UML2_Element:

    pass
class UML2_WriteStructuralFeatureAction(StructuralFeatureAction):

    pass
class Vertex:

    pass
class UML2_State(Vertex, RedefinableElement, Namespace):

    pass
class UML2_ConnectionPointReference(Vertex):

    pass
class UML2_Pseudostate(Vertex):

    pass
class BehavioredClassifier:

    pass
class UML2_Collaboration(StructuredClassifier, BehavioredClassifier):

    pass
class UML2_Class(EncapsulatedClassifier, BehavioredClassifier):

    def __init__(self, isActive: bool, UML2_Class: set["UML2_Classifier"] = None, UML2_Class68: set["UML2_Reception"] = None):
        self.isActive = isActive
        self.UML2_Class = UML2_Class if UML2_Class is not None else set()
        self.UML2_Class68 = UML2_Class68 if UML2_Class68 is not None else set()
        
    @property
    def isActive(self) -> bool:
        return self.__isActive

    @isActive.setter
    def isActive(self, isActive: bool):
        self.__isActive = isActive

    @property
    def UML2_Class(self):
        return self.__UML2_Class

    @UML2_Class.setter
    def UML2_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Class__UML2_Class", None)
        self.__UML2_Class = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Classifier66"):
                    opp_val = getattr(item, "UML2_Classifier66", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Classifier66", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Classifier66"):
                    opp_val = getattr(item, "UML2_Classifier66", None)
                    
                    setattr(item, "UML2_Classifier66", self)
                    

    @property
    def UML2_Class68(self):
        return self.__UML2_Class68

    @UML2_Class68.setter
    def UML2_Class68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Class__UML2_Class68", None)
        self.__UML2_Class68 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Reception"):
                    opp_val = getattr(item, "UML2_Reception", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Reception", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Reception"):
                    opp_val = getattr(item, "UML2_Reception", None)
                    
                    setattr(item, "UML2_Reception", self)
                    

class UML2_UseCase(BehavioredClassifier):

    pass
class Classifier:

    pass
class UML2_Association(Classifier, Relationship):

    pass
class UML2_ParameterableClassifier(Classifier):

    pass
class UML2_Actor(Classifier):

    pass
class UML2_Signal(Classifier):

    pass
class UML2_TemplateableClassifier(Classifier):

    pass
class UML2_DataType(Classifier):

    pass
class UML2_StructuredClassifier(Classifier):

    pass
class UML2_InformationItem(Classifier):

    pass
class UML2_Artifact(Classifier, DeployedArtifact):

    pass
class UML2_BehavioredClassifier(Classifier):

    pass
class UML2_Interface(Classifier):

    pass
class UML2_ReadExtentAction(Action):

    pass
class UML2_Generalization(DirectedRelationship):

    pass
class UML2_NamedElement(TemplateableElement):

    def __init__(self, name: str, visibility: str, UML2_NamedElement: "UML2_Classifier" = None, UML2_NamedElement78: "UML2_Namespace" = None):
        self.name = name
        self.visibility = visibility
        self.UML2_NamedElement = UML2_NamedElement
        self.UML2_NamedElement78 = UML2_NamedElement78
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "UML2_Classifier7"):
                opp_val = getattr(old_value, "UML2_Classifier7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Classifier7"):
                opp_val = getattr(value, "UML2_Classifier7", None)
                if opp_val is None:
                    setattr(value, "UML2_Classifier7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_NamedElement78(self):
        return self.__UML2_NamedElement78

    @UML2_NamedElement78.setter
    def UML2_NamedElement78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_NamedElement__UML2_NamedElement78", None)
        self.__UML2_NamedElement78 = value
        
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

class UML2_Feature(RedefinableElement):

    def __init__(self, isStatic: bool, UML2_Feature: "UML2_Classifier" = None, UML2_Feature13: set["UML2_Classifier"] = None):
        self.isStatic = isStatic
        self.UML2_Feature = UML2_Feature
        self.UML2_Feature13 = UML2_Feature13 if UML2_Feature13 is not None else set()
        
    @property
    def isStatic(self) -> bool:
        return self.__isStatic

    @isStatic.setter
    def isStatic(self, isStatic: bool):
        self.__isStatic = isStatic

    @property
    def UML2_Feature(self):
        return self.__UML2_Feature

    @UML2_Feature.setter
    def UML2_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Feature__UML2_Feature", None)
        self.__UML2_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Classifier5"):
                opp_val = getattr(old_value, "UML2_Classifier5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Classifier5"):
                opp_val = getattr(value, "UML2_Classifier5", None)
                if opp_val is None:
                    setattr(value, "UML2_Classifier5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Feature13(self):
        return self.__UML2_Feature13

    @UML2_Feature13.setter
    def UML2_Feature13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Feature__UML2_Feature13", None)
        self.__UML2_Feature13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Classifier14"):
                    opp_val = getattr(item, "UML2_Classifier14", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Classifier14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Classifier14"):
                    opp_val = getattr(item, "UML2_Classifier14", None)
                    
                    setattr(item, "UML2_Classifier14", self)
                    

class PackageableElement:

    pass
class UML2_InformationFlow(DirectedRelationship, PackageableElement):

    pass
class UML2_Type(PackageableElement):

    pass
class UML2_Package(Namespace, PackageableElement):

    pass
class UML2_GeneralizationSet(PackageableElement):

    pass
class UML2_Dependency(DirectedRelationship, PackageableElement):

    pass
class UML2_PrimitiveFunction(PackageableElement):

    pass
class UML2_Constraint(PackageableElement):

    pass
class DeploymentTarget:

    pass
class UML2_Property(DeploymentTarget, StructuralFeature, ConnectableElement):

    def __init__(self, isComposite: bool, isDerived: bool, isDerivedUnion: bool, aggregation: str, UML2_Property25: "UML2_QualifierValue" = None, UML2_Property: "UML2_LinkEndData" = None, UML2_Property39: "UML2_Property" = None, UML2_Property37: set["UML2_Property"] = None, UML2_Property41: "UML2_Association" = None, UML2_Property44: "UML2_Property" = None, UML2_Property42: set["UML2_Property"] = None, UML2_Property48: "UML2_Association" = None, UML2_Property51: "UML2_Association" = None):
        self.isComposite = isComposite
        self.isDerived = isDerived
        self.isDerivedUnion = isDerivedUnion
        self.aggregation = aggregation
        self.UML2_Property25 = UML2_Property25
        self.UML2_Property = UML2_Property
        self.UML2_Property39 = UML2_Property39
        self.UML2_Property37 = UML2_Property37 if UML2_Property37 is not None else set()
        self.UML2_Property41 = UML2_Property41
        self.UML2_Property44 = UML2_Property44
        self.UML2_Property42 = UML2_Property42 if UML2_Property42 is not None else set()
        self.UML2_Property48 = UML2_Property48
        self.UML2_Property51 = UML2_Property51
        
    @property
    def isComposite(self) -> bool:
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: bool):
        self.__isComposite = isComposite

    @property
    def aggregation(self) -> str:
        return self.__aggregation

    @aggregation.setter
    def aggregation(self, aggregation: str):
        self.__aggregation = aggregation

    @property
    def isDerived(self) -> bool:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: bool):
        self.__isDerived = isDerived

    @property
    def isDerivedUnion(self) -> bool:
        return self.__isDerivedUnion

    @isDerivedUnion.setter
    def isDerivedUnion(self, isDerivedUnion: bool):
        self.__isDerivedUnion = isDerivedUnion

    @property
    def UML2_Property37(self):
        return self.__UML2_Property37

    @UML2_Property37.setter
    def UML2_Property37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property37", None)
        self.__UML2_Property37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Property39"):
                    opp_val = getattr(item, "UML2_Property39", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Property39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Property39"):
                    opp_val = getattr(item, "UML2_Property39", None)
                    
                    setattr(item, "UML2_Property39", self)
                    

    @property
    def UML2_Property48(self):
        return self.__UML2_Property48

    @UML2_Property48.setter
    def UML2_Property48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property48", None)
        self.__UML2_Property48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Association47"):
                opp_val = getattr(old_value, "UML2_Association47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Association47"):
                opp_val = getattr(value, "UML2_Association47", None)
                if opp_val is None:
                    setattr(value, "UML2_Association47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Property39(self):
        return self.__UML2_Property39

    @UML2_Property39.setter
    def UML2_Property39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property39", None)
        self.__UML2_Property39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Property37"):
                opp_val = getattr(old_value, "UML2_Property37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Property37"):
                opp_val = getattr(value, "UML2_Property37", None)
                if opp_val is None:
                    setattr(value, "UML2_Property37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Property41(self):
        return self.__UML2_Property41

    @UML2_Property41.setter
    def UML2_Property41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property41", None)
        self.__UML2_Property41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Association"):
                opp_val = getattr(old_value, "UML2_Association", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Association", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Association"):
                opp_val = getattr(value, "UML2_Association", None)
                setattr(value, "UML2_Association", self)

    @property
    def UML2_Property51(self):
        return self.__UML2_Property51

    @UML2_Property51.setter
    def UML2_Property51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property51", None)
        self.__UML2_Property51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Association50"):
                opp_val = getattr(old_value, "UML2_Association50", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Association50"):
                opp_val = getattr(value, "UML2_Association50", None)
                if opp_val is None:
                    setattr(value, "UML2_Association50", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Property42(self):
        return self.__UML2_Property42

    @UML2_Property42.setter
    def UML2_Property42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property42", None)
        self.__UML2_Property42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Property44"):
                    opp_val = getattr(item, "UML2_Property44", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Property44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Property44"):
                    opp_val = getattr(item, "UML2_Property44", None)
                    
                    setattr(item, "UML2_Property44", self)
                    

    @property
    def UML2_Property25(self):
        return self.__UML2_Property25

    @UML2_Property25.setter
    def UML2_Property25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property25", None)
        self.__UML2_Property25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_QualifierValue24"):
                opp_val = getattr(old_value, "UML2_QualifierValue24", None)
                if opp_val == self:
                    setattr(old_value, "UML2_QualifierValue24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_QualifierValue24"):
                opp_val = getattr(value, "UML2_QualifierValue24", None)
                setattr(value, "UML2_QualifierValue24", self)

    @property
    def UML2_Property44(self):
        return self.__UML2_Property44

    @UML2_Property44.setter
    def UML2_Property44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property44", None)
        self.__UML2_Property44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Property42"):
                opp_val = getattr(old_value, "UML2_Property42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Property42"):
                opp_val = getattr(value, "UML2_Property42", None)
                if opp_val is None:
                    setattr(value, "UML2_Property42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Property(self):
        return self.__UML2_Property

    @UML2_Property.setter
    def UML2_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property", None)
        self.__UML2_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_LinkEndData18"):
                opp_val = getattr(old_value, "UML2_LinkEndData18", None)
                if opp_val == self:
                    setattr(old_value, "UML2_LinkEndData18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_LinkEndData18"):
                opp_val = getattr(value, "UML2_LinkEndData18", None)
                setattr(value, "UML2_LinkEndData18", self)

class UML2_InstanceSpecification(DeployedArtifact, DeploymentTarget, PackageableElement):

    pass
class Class:

    pass
class UML2_Behavior(Class):

    pass
class UML2_Component(Class):

    pass
class UML2_Stereotype(Class):

    pass
class UML2_AssociationClass(Class, Association):

    pass
class UML2_Node(DeploymentTarget, Class):

    pass