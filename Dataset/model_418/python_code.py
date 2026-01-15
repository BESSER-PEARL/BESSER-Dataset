from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ParameterDirectionKind(Enum):
    in = "in"
    inout = "inout"
    out = "out"
    return = "return"
class AggregationKind(Enum):
    composite = "composite"
    none = "none"
    shared = "shared"
class VisibilityKind(Enum):
    package = "package"
    private = "private"
    protected = "protected"
    public = "public"


############################################
# Definition of Classes
############################################

class DataType:

    pass
class UML2_PrimitiveType(DataType):

    pass
class UML2_Enumeration(DataType):

    pass
class StateMachine:

    pass
class UML2_ProtocolStateMachine(StateMachine):

    pass
class LinkEndData:

    pass
class UML2_LinkEndCreationData(LinkEndData):

    pass
class TemplateSignature:

    pass
class WriteLinkAction:

    pass
class UML2_DestroyLinkAction(WriteLinkAction):

    pass
class UML2_CreateLinkAction(WriteLinkAction):

    pass
class Realization:

    pass
class UML2_Implementation(Realization):

    pass
class UML2_Substitution(Realization):

    pass
class Type:

    pass
class EncapsulatedClassifier:

    pass
class Package:

    pass
class UML2_Profile(Package):

    pass
class UML2_Model(Package):

    pass
class Association:

    pass
class UML2_CommunicationPath(Association):

    pass
class UML2_Extension(Association):

    pass
class ExecutableNode:

    pass
class UML2_Action(ExecutableNode):

    pass
class IntervalConstraint:

    pass
class UML2_TimeConstraint(IntervalConstraint):

    pass
class UML2_DurationConstraint(IntervalConstraint):

    pass
class ObjectNode:

    pass
class UML2_ActivityParameterNode(ObjectNode):

    pass
class UML2_ExpansionNode(ObjectNode):

    pass
class UML2_CentralBufferNode(ObjectNode):

    pass
class CentralBufferNode:

    pass
class UML2_DataStoreNode(CentralBufferNode):

    pass
class Abstraction:

    pass
class UML2_Manifestation(Abstraction):

    pass
class UML2_Realization(Abstraction):

    pass
class InteractionOccurrence:

    pass
class UML2_PartDecomposition(InteractionOccurrence):

    pass
class UML2_Element:

    pass
class ActivityGroup:

    pass
class UML2_InterruptibleActivityRegion(ActivityGroup):

    pass
class MessageTrigger:

    pass
class UML2_SignalTrigger(MessageTrigger):

    pass
class UML2_CallTrigger(MessageTrigger):

    pass
class UML2_AnyTrigger(MessageTrigger):

    pass
class ActivityEdge:

    pass
class UML2_ObjectFlow(ActivityEdge):

    pass
class UML2_ControlFlow(ActivityEdge):

    pass
class CreateLinkAction:

    pass
class UML2_CreateLinkObjectAction(CreateLinkAction):

    pass
class Relationship:

    pass
class UML2_DirectedRelationship(Relationship):

    pass
class EventOccurrence:

    pass
class UML2_Stop(EventOccurrence):

    pass
class MessageEnd:

    pass
class UML2_Gate(MessageEnd):

    pass
class InvocationAction:

    pass
class UML2_CallAction(InvocationAction):

    pass
class UML2_BroadcastSignalAction(InvocationAction):

    pass
class UML2_SendObjectAction(InvocationAction):

    pass
class UML2_SendSignalAction(InvocationAction):

    pass
class TemplateableElement:

    pass
class UML2_NamedElement(TemplateableElement):

    def __init__(self, name: str, visibility: str, UML2_NamedElement: "UML2_Namespace" = None, UML2_NamedElement58: "UML2_Classifier" = None):
        self.name = name
        self.visibility = visibility
        self.UML2_NamedElement = UML2_NamedElement
        self.UML2_NamedElement58 = UML2_NamedElement58
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

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
    def UML2_NamedElement58(self):
        return self.__UML2_NamedElement58

    @UML2_NamedElement58.setter
    def UML2_NamedElement58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_NamedElement__UML2_NamedElement58", None)
        self.__UML2_NamedElement58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Classifier57"):
                opp_val = getattr(old_value, "UML2_Classifier57", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Classifier57"):
                opp_val = getattr(value, "UML2_Classifier57", None)
                if opp_val is None:
                    setattr(value, "UML2_Classifier57", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UML2_Comment(TemplateableElement):

    pass
class UML2_StringExpression(TemplateableElement):

    pass
class StructuralFeature:

    pass
class WriteVariableAction:

    pass
class UML2_RemoveVariableValueAction(WriteVariableAction):

    pass
class UML2_AddVariableValueAction(WriteVariableAction):

    pass
class InteractionFragment:

    pass
class UML2_ExecutionOccurrence(InteractionFragment):

    pass
class UML2_StateInvariant(InteractionFragment):

    pass
class UML2_Continuation(InteractionFragment):

    pass
class UML2_InteractionOccurrence(InteractionFragment):

    pass
class UML2_EventOccurrence(MessageEnd, InteractionFragment):

    pass
class UML2_CombinedFragment(InteractionFragment):

    pass
class OpaqueExpression:

    pass
class UML2_Expression(OpaqueExpression):

    pass
class LiteralSpecification:

    pass
class UML2_LiteralBoolean(LiteralSpecification):

    pass
class UML2_LiteralUnlimitedNatural(LiteralSpecification):

    pass
class UML2_LiteralInteger(LiteralSpecification):

    pass
class UML2_LiteralNull(LiteralSpecification):

    pass
class LinkAction:

    pass
class UML2_ReadLinkAction(LinkAction):

    pass
class UML2_WriteLinkAction(LinkAction):

    pass
class Dependency:

    pass
class UML2_Deployment(Dependency):

    pass
class UML2_Permission(Dependency):

    pass
class UML2_Usage(Dependency):

    pass
class UML2_Abstraction(Dependency):

    pass
class TemplateParameter:

    pass
class UML2_OperationTemplateParameter(TemplateParameter):

    pass
class UML2_ClassifierTemplateParameter(TemplateParameter):

    pass
class UML2_ConnectableElementTemplateParameter(TemplateParameter):

    pass
class ActivityNode:

    pass
class UML2_ControlNode(ActivityNode):

    pass
class UML2_ExecutableNode(ActivityNode):

    pass
class PackageImport:

    pass
class UML2_ProfileApplication(PackageImport):

    pass
class BehavioralFeature:

    pass
class UML2_Reception(BehavioralFeature):

    pass
class Behavior:

    pass
class UML2_StateMachine(Behavior):

    pass
class UML2_Interaction(Behavior, InteractionFragment):

    pass
class UML2_Activity(Behavior):

    pass
class State:

    pass
class UML2_FinalState(State):

    pass
class UML2_LiteralString(LiteralSpecification):

    pass
class Constraint:

    pass
class UML2_InteractionConstraint(Constraint):

    pass
class UML2_IntervalConstraint(Constraint):

    pass
class Class:

    pass
class UML2_AssociationClass(Association, Class):

    pass
class UML2_Component(Class):

    pass
class UML2_Behavior(Class):

    pass
class UML2_Stereotype(Class):

    pass
class AcceptEventAction:

    pass
class UML2_AcceptCallAction(AcceptEventAction):

    pass
class FinalNode:

    pass
class UML2_ActivityFinalNode(FinalNode):

    pass
class UML2_FlowFinalNode(FinalNode):

    pass
class Classifier:

    pass
class UML2_Interface(Classifier):

    pass
class UML2_BehavioredClassifier(Classifier):

    pass
class UML2_InformationItem(Classifier):

    pass
class UML2_DataType(Classifier):

    pass
class UML2_ParameterableClassifier(Classifier):

    pass
class UML2_StructuredClassifier(Classifier):

    pass
class UML2_Actor(Classifier):

    pass
class UML2_Association(Classifier, Relationship):

    pass
class UML2_Signal(Classifier):

    pass
class UML2_TemplateableClassifier(Classifier):

    pass
class StructuredActivityNode:

    pass
class UML2_ConditionalNode(StructuredActivityNode):

    pass
class UML2_ExpansionRegion(StructuredActivityNode):

    pass
class UML2_LoopNode(StructuredActivityNode):

    pass
class DeployedArtifact:

    pass
class UML2_Artifact(Classifier, DeployedArtifact):

    pass
class DeploymentTarget:

    pass
class UML2_Node(Class, DeploymentTarget):

    pass
class PackageableElement:

    pass
class UML2_GeneralizationSet(PackageableElement):

    pass
class UML2_Constraint(PackageableElement):

    pass
class UML2_PrimitiveFunction(PackageableElement):

    pass
class UML2_Type(PackageableElement):

    pass
class UML2_InstanceSpecification(PackageableElement, DeployedArtifact, DeploymentTarget):

    pass
class Element:

    pass
class UML2_Slot(Element):

    pass
class UML2_Relationship(Element):

    pass
class UML2_TemplateParameterSubstitution(Element):

    pass
class UML2_Clause(Element):

    pass
class UML2_LinkEndData(Element):

    pass
class UML2_ExceptionHandler(Element):

    pass
class UML2_ParameterableElement(Element):

    pass
class UML2_ActivityGroup(Element):

    pass
class UML2_QualifierValue(Element):

    pass
class UML2_TemplateableElement(Element):

    pass
class UML2_TemplateSignature(Element):

    pass
class UML2_TemplateParameter(Element):

    pass
class Pin:

    pass
class UML2_InputPin(Pin):

    pass
class UML2_OutputPin(Pin):

    pass
class DirectedRelationship:

    pass
class UML2_InformationFlow(PackageableElement, DirectedRelationship):

    pass
class UML2_ProtocolConformance(DirectedRelationship):

    pass
class UML2_Generalization(DirectedRelationship):

    pass
class UML2_ElementImport(DirectedRelationship):

    pass
class UML2_TemplateBinding(DirectedRelationship):

    pass
class UML2_Dependency(PackageableElement, DirectedRelationship):

    pass
class UML2_PackageImport(DirectedRelationship):

    pass
class UML2_PackageMerge(DirectedRelationship):

    pass
class Feature:

    pass
class UML2_Connector(Feature):

    pass
class Namespace:

    pass
class UML2_InteractionOperand(InteractionFragment, Namespace):

    pass
class UML2_Package(PackageableElement, Namespace):

    pass
class UML2_BehavioralFeature(Feature, Namespace):

    pass
class Artifact:

    pass
class UML2_DeploymentSpecification(Artifact):

    pass
class StructuredClassifier:

    pass
class UML2_EncapsulatedClassifier(StructuredClassifier):

    pass
class BehavioredClassifier:

    pass
class UML2_Class(EncapsulatedClassifier, BehavioredClassifier):

    def __init__(self, isActive: bool, UML2_Class: set["UML2_Classifier"] = None, UML2_Class39: set["UML2_Reception"] = None):
        self.isActive = isActive
        self.UML2_Class = UML2_Class if UML2_Class is not None else set()
        self.UML2_Class39 = UML2_Class39 if UML2_Class39 is not None else set()
        
    @property
    def isActive(self) -> bool:
        return self.__isActive

    @isActive.setter
    def isActive(self, isActive: bool):
        self.__isActive = isActive

    @property
    def UML2_Class39(self):
        return self.__UML2_Class39

    @UML2_Class39.setter
    def UML2_Class39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Class__UML2_Class39", None)
        self.__UML2_Class39 = value if value is not None else set()
        
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
                if hasattr(item, "UML2_Classifier37"):
                    opp_val = getattr(item, "UML2_Classifier37", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Classifier37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Classifier37"):
                    opp_val = getattr(item, "UML2_Classifier37", None)
                    
                    setattr(item, "UML2_Classifier37", self)
                    

class UML2_UseCase(BehavioredClassifier):

    pass
class UML2_Collaboration(BehavioredClassifier, StructuredClassifier):

    pass
class Property:

    pass
class UML2_Port(Property):

    pass
class UML2_ExtensionEnd(Property):

    pass
class ParameterableElement:

    pass
class VariableAction:

    pass
class UML2_WriteVariableAction(VariableAction):

    pass
class UML2_ClearVariableAction(VariableAction):

    pass
class UML2_ReadVariableAction(VariableAction):

    pass
class StructuralFeatureAction:

    pass
class UML2_WriteStructuralFeatureAction(StructuralFeatureAction):

    pass
class UML2_ReadStructuralFeatureAction(StructuralFeatureAction):

    pass
class UML2_ClearStructuralFeatureAction(StructuralFeatureAction):

    pass
class Node:

    pass
class UML2_Device(Node):

    pass
class UML2_ExecutionEnvironment(Node):

    pass
class InstanceSpecification:

    pass
class UML2_EnumerationLiteral(InstanceSpecification):

    pass
class Vertex:

    pass
class UML2_ConnectionPointReference(Vertex):

    pass
class UML2_Pseudostate(Vertex):

    pass
class Interval:

    pass
class UML2_TimeInterval(Interval):

    pass
class UML2_DurationInterval(Interval):

    pass
class NamedElement:

    pass
class UML2_Trigger(NamedElement):

    pass
class UML2_DeployedArtifact(NamedElement):

    pass
class UML2_ParameterSet(NamedElement):

    pass
class UML2_GeneralOrdering(NamedElement):

    pass
class UML2_CollaborationOccurrence(NamedElement):

    pass
class UML2_MessageEnd(NamedElement):

    pass
class UML2_Lifeline(NamedElement):

    pass
class UML2_PackageableElement(NamedElement, ParameterableElement):

    pass
class UML2_Extend(NamedElement, DirectedRelationship):

    pass
class UML2_Message(NamedElement):

    pass
class UML2_DeploymentTarget(NamedElement):

    pass
class UML2_RedefinableElement(NamedElement):

    pass
class UML2_TypedElement(NamedElement):

    pass
class UML2_ActivityPartition(ActivityGroup, NamedElement):

    pass
class UML2_ConnectableElement(NamedElement, ParameterableElement):

    pass
class UML2_Namespace(NamedElement):

    pass
class UML2_Include(NamedElement, DirectedRelationship):

    pass
class UML2_InteractionFragment(NamedElement):

    pass
class UML2_Vertex(NamedElement):

    pass
class ValueSpecification:

    pass
class UML2_TimeExpression(ValueSpecification):

    pass
class UML2_LiteralSpecification(ValueSpecification):

    pass
class UML2_Interval(ValueSpecification):

    pass
class UML2_OpaqueExpression(ValueSpecification):

    pass
class UML2_Duration(ValueSpecification):

    pass
class UML2_InstanceValue(ValueSpecification):

    pass
class Transition:

    pass
class UML2_ProtocolTransition(Transition):

    pass
class InputPin:

    pass
class UML2_ValuePin(InputPin):

    pass
class CallAction:

    pass
class UML2_CallBehaviorAction(CallAction):

    pass
class UML2_CallOperationAction(CallAction):

    pass
class WriteStructuralFeatureAction:

    pass
class UML2_AddStructuralFeatureValueAction(WriteStructuralFeatureAction):

    pass
class UML2_TimeObservationAction(WriteStructuralFeatureAction):

    pass
class UML2_RemoveStructuralFeatureValueAction(WriteStructuralFeatureAction):

    pass
class UML2_DurationObservationAction(WriteStructuralFeatureAction):

    pass
class Action:

    pass
class UML2_ReclassifyObjectAction(Action):

    pass
class UML2_VariableAction(Action):

    pass
class UML2_StructuralFeatureAction(Action):

    pass
class UML2_TestIdentityAction(Action):

    pass
class UML2_StructuredActivityNode(ActivityGroup, Action, Namespace):

    pass
class UML2_InvocationAction(Action):

    pass
class UML2_ReplyAction(Action):

    pass
class UML2_StartOwnedBehaviorAction(Action):

    pass
class UML2_ReadIsClassifiedObjectAction(Action):

    pass
class UML2_ClearAssociationAction(Action):

    pass
class UML2_ApplyFunctionAction(Action):

    pass
class UML2_ReadExtentAction(Action):

    pass
class UML2_DestroyObjectAction(Action):

    pass
class UML2_ReadSelfAction(Action):

    pass
class UML2_CreateObjectAction(Action):

    pass
class UML2_LinkAction(Action):

    pass
class UML2_ReadLinkObjectEndAction(Action):

    pass
class UML2_ReadLinkObjectEndQualifierAction(Action):

    pass
class UML2_AcceptEventAction(Action):

    pass
class UML2_RaiseExceptionAction(Action):

    pass
class Trigger:

    pass
class UML2_TimeTrigger(Trigger):

    pass
class UML2_ChangeTrigger(Trigger):

    pass
class UML2_MultiplicityElement(Element):

    def __init__(self, isOrdered: bool, isUnique: bool, lower: int, upper: str):
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.lower = lower
        self.upper = upper
        
    @property
    def isUnique(self) -> bool:
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: bool):
        self.__isUnique = isUnique

    @property
    def lower(self) -> int:
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower

    @property
    def isOrdered(self) -> bool:
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: bool):
        self.__isOrdered = isOrdered

    @property
    def upper(self) -> str:
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper

class MultiplicityElement:

    pass
class UML2_ConnectorEnd(MultiplicityElement):

    pass
class UML2_Pin(ObjectNode, MultiplicityElement):

    pass
class TypedElement:

    pass
class UML2_ValueSpecification(TypedElement, ParameterableElement):

    pass
class UML2_StructuralFeature(TypedElement, Feature, MultiplicityElement):

    def __init__(self, isReadOnly: bool, UML2_StructuralFeature: "UML2_Slot" = None, UML2_StructuralFeature72: "UML2_StructuralFeatureAction" = None):
        self.isReadOnly = isReadOnly
        self.UML2_StructuralFeature = UML2_StructuralFeature
        self.UML2_StructuralFeature72 = UML2_StructuralFeature72
        
    @property
    def isReadOnly(self) -> bool:
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: bool):
        self.__isReadOnly = isReadOnly

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
            if hasattr(old_value, "UML2_Slot33"):
                opp_val = getattr(old_value, "UML2_Slot33", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Slot33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Slot33"):
                opp_val = getattr(value, "UML2_Slot33", None)
                setattr(value, "UML2_Slot33", self)

    @property
    def UML2_StructuralFeature72(self):
        return self.__UML2_StructuralFeature72

    @UML2_StructuralFeature72.setter
    def UML2_StructuralFeature72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_StructuralFeature__UML2_StructuralFeature72", None)
        self.__UML2_StructuralFeature72 = value
        
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

class UML2_ObjectNode(TypedElement, ActivityNode):

    pass
class UML2_Operation(BehavioralFeature, TypedElement, ParameterableElement, MultiplicityElement):

    pass
class ConnectableElement:

    pass
class UML2_Variable(ConnectableElement, TypedElement, MultiplicityElement):

    pass
class UML2_Property(ConnectableElement, StructuralFeature, DeploymentTarget):

    def __init__(self, isComposite: bool, isDerived: bool, isDerivedUnion: bool, aggregation: str, UML2_Property: "UML2_Property" = None, UML2_Property12: set["UML2_Property"] = None, UML2_Property15: "UML2_Association" = None, UML2_Property18: "UML2_Property" = None, UML2_Property16: set["UML2_Property"] = None, UML2_Property44: "UML2_LinkEndData" = None, UML2_Property49: "UML2_QualifierValue" = None, UML2_Property67: "UML2_Association" = None, UML2_Property70: "UML2_Association" = None):
        self.isComposite = isComposite
        self.isDerived = isDerived
        self.isDerivedUnion = isDerivedUnion
        self.aggregation = aggregation
        self.UML2_Property = UML2_Property
        self.UML2_Property12 = UML2_Property12 if UML2_Property12 is not None else set()
        self.UML2_Property15 = UML2_Property15
        self.UML2_Property18 = UML2_Property18
        self.UML2_Property16 = UML2_Property16 if UML2_Property16 is not None else set()
        self.UML2_Property44 = UML2_Property44
        self.UML2_Property49 = UML2_Property49
        self.UML2_Property67 = UML2_Property67
        self.UML2_Property70 = UML2_Property70
        
    @property
    def isDerivedUnion(self) -> bool:
        return self.__isDerivedUnion

    @isDerivedUnion.setter
    def isDerivedUnion(self, isDerivedUnion: bool):
        self.__isDerivedUnion = isDerivedUnion

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
    def UML2_Property49(self):
        return self.__UML2_Property49

    @UML2_Property49.setter
    def UML2_Property49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property49", None)
        self.__UML2_Property49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_QualifierValue48"):
                opp_val = getattr(old_value, "UML2_QualifierValue48", None)
                if opp_val == self:
                    setattr(old_value, "UML2_QualifierValue48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_QualifierValue48"):
                opp_val = getattr(value, "UML2_QualifierValue48", None)
                setattr(value, "UML2_QualifierValue48", self)

    @property
    def UML2_Property18(self):
        return self.__UML2_Property18

    @UML2_Property18.setter
    def UML2_Property18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property18", None)
        self.__UML2_Property18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Property16"):
                opp_val = getattr(old_value, "UML2_Property16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Property16"):
                opp_val = getattr(value, "UML2_Property16", None)
                if opp_val is None:
                    setattr(value, "UML2_Property16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Property67(self):
        return self.__UML2_Property67

    @UML2_Property67.setter
    def UML2_Property67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property67", None)
        self.__UML2_Property67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Association66"):
                opp_val = getattr(old_value, "UML2_Association66", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Association66"):
                opp_val = getattr(value, "UML2_Association66", None)
                if opp_val is None:
                    setattr(value, "UML2_Association66", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Property12(self):
        return self.__UML2_Property12

    @UML2_Property12.setter
    def UML2_Property12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property12", None)
        self.__UML2_Property12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Property"):
                    opp_val = getattr(item, "UML2_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Property"):
                    opp_val = getattr(item, "UML2_Property", None)
                    
                    setattr(item, "UML2_Property", self)
                    

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
            if hasattr(old_value, "UML2_Property12"):
                opp_val = getattr(old_value, "UML2_Property12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Property12"):
                opp_val = getattr(value, "UML2_Property12", None)
                if opp_val is None:
                    setattr(value, "UML2_Property12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "UML2_LinkEndData43"):
                opp_val = getattr(old_value, "UML2_LinkEndData43", None)
                if opp_val == self:
                    setattr(old_value, "UML2_LinkEndData43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_LinkEndData43"):
                opp_val = getattr(value, "UML2_LinkEndData43", None)
                setattr(value, "UML2_LinkEndData43", self)

    @property
    def UML2_Property15(self):
        return self.__UML2_Property15

    @UML2_Property15.setter
    def UML2_Property15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property15", None)
        self.__UML2_Property15 = value
        
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
    def UML2_Property16(self):
        return self.__UML2_Property16

    @UML2_Property16.setter
    def UML2_Property16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property16", None)
        self.__UML2_Property16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Property18"):
                    opp_val = getattr(item, "UML2_Property18", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Property18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Property18"):
                    opp_val = getattr(item, "UML2_Property18", None)
                    
                    setattr(item, "UML2_Property18", self)
                    

    @property
    def UML2_Property70(self):
        return self.__UML2_Property70

    @UML2_Property70.setter
    def UML2_Property70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property70", None)
        self.__UML2_Property70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Association69"):
                opp_val = getattr(old_value, "UML2_Association69", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Association69"):
                opp_val = getattr(value, "UML2_Association69", None)
                if opp_val is None:
                    setattr(value, "UML2_Association69", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UML2_Parameter(ConnectableElement, TypedElement, MultiplicityElement):

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

class RedefinableElement:

    pass
class UML2_RedefinableTemplateSignature(TemplateSignature, RedefinableElement):

    pass
class UML2_Feature(RedefinableElement):

    def __init__(self, isStatic: bool, UML2_Feature: set["UML2_Classifier"] = None, UML2_Feature55: "UML2_Classifier" = None):
        self.isStatic = isStatic
        self.UML2_Feature = UML2_Feature if UML2_Feature is not None else set()
        self.UML2_Feature55 = UML2_Feature55
        
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
        self.__UML2_Feature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Classifier"):
                    opp_val = getattr(item, "UML2_Classifier", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Classifier", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Classifier"):
                    opp_val = getattr(item, "UML2_Classifier", None)
                    
                    setattr(item, "UML2_Classifier", self)
                    

    @property
    def UML2_Feature55(self):
        return self.__UML2_Feature55

    @UML2_Feature55.setter
    def UML2_Feature55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Feature__UML2_Feature55", None)
        self.__UML2_Feature55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Classifier54"):
                opp_val = getattr(old_value, "UML2_Classifier54", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Classifier54"):
                opp_val = getattr(value, "UML2_Classifier54", None)
                if opp_val is None:
                    setattr(value, "UML2_Classifier54", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UML2_ExtensionPoint(RedefinableElement):

    pass
class UML2_Classifier(Namespace, RedefinableElement, Type):

    def __init__(self, isAbstract: bool, UML2_Classifier: "UML2_Feature" = None, UML2_Classifier8: "UML2_InstanceSpecification" = None, UML2_Classifier21: "UML2_CreateObjectAction" = None, UML2_Classifier35: "UML2_Action" = None, UML2_Classifier37: "UML2_Class" = None, UML2_Classifier54: set["UML2_Feature"] = None, UML2_Classifier57: set["UML2_NamedElement"] = None, UML2_Classifier60: set["UML2_Generalization"] = None, UML2_Classifier77: "UML2_Generalization" = None):
        self.isAbstract = isAbstract
        self.UML2_Classifier = UML2_Classifier
        self.UML2_Classifier8 = UML2_Classifier8
        self.UML2_Classifier21 = UML2_Classifier21
        self.UML2_Classifier35 = UML2_Classifier35
        self.UML2_Classifier37 = UML2_Classifier37
        self.UML2_Classifier54 = UML2_Classifier54 if UML2_Classifier54 is not None else set()
        self.UML2_Classifier57 = UML2_Classifier57 if UML2_Classifier57 is not None else set()
        self.UML2_Classifier60 = UML2_Classifier60 if UML2_Classifier60 is not None else set()
        self.UML2_Classifier77 = UML2_Classifier77
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def UML2_Classifier54(self):
        return self.__UML2_Classifier54

    @UML2_Classifier54.setter
    def UML2_Classifier54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier54", None)
        self.__UML2_Classifier54 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Feature55"):
                    opp_val = getattr(item, "UML2_Feature55", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Feature55", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Feature55"):
                    opp_val = getattr(item, "UML2_Feature55", None)
                    
                    setattr(item, "UML2_Feature55", self)
                    

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
            if hasattr(old_value, "UML2_Feature"):
                opp_val = getattr(old_value, "UML2_Feature", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Feature"):
                opp_val = getattr(value, "UML2_Feature", None)
                if opp_val is None:
                    setattr(value, "UML2_Feature", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Classifier21(self):
        return self.__UML2_Classifier21

    @UML2_Classifier21.setter
    def UML2_Classifier21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier21", None)
        self.__UML2_Classifier21 = value
        
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
    def UML2_Classifier8(self):
        return self.__UML2_Classifier8

    @UML2_Classifier8.setter
    def UML2_Classifier8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier8", None)
        self.__UML2_Classifier8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_InstanceSpecification7"):
                opp_val = getattr(old_value, "UML2_InstanceSpecification7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_InstanceSpecification7"):
                opp_val = getattr(value, "UML2_InstanceSpecification7", None)
                if opp_val is None:
                    setattr(value, "UML2_InstanceSpecification7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Classifier35(self):
        return self.__UML2_Classifier35

    @UML2_Classifier35.setter
    def UML2_Classifier35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier35", None)
        self.__UML2_Classifier35 = value
        
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
    def UML2_Classifier77(self):
        return self.__UML2_Classifier77

    @UML2_Classifier77.setter
    def UML2_Classifier77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier77", None)
        self.__UML2_Classifier77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Generalization76"):
                opp_val = getattr(old_value, "UML2_Generalization76", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Generalization76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Generalization76"):
                opp_val = getattr(value, "UML2_Generalization76", None)
                setattr(value, "UML2_Generalization76", self)

    @property
    def UML2_Classifier57(self):
        return self.__UML2_Classifier57

    @UML2_Classifier57.setter
    def UML2_Classifier57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier57", None)
        self.__UML2_Classifier57 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_NamedElement58"):
                    opp_val = getattr(item, "UML2_NamedElement58", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_NamedElement58", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_NamedElement58"):
                    opp_val = getattr(item, "UML2_NamedElement58", None)
                    
                    setattr(item, "UML2_NamedElement58", self)
                    

    @property
    def UML2_Classifier37(self):
        return self.__UML2_Classifier37

    @UML2_Classifier37.setter
    def UML2_Classifier37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier37", None)
        self.__UML2_Classifier37 = value
        
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
    def UML2_Classifier60(self):
        return self.__UML2_Classifier60

    @UML2_Classifier60.setter
    def UML2_Classifier60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier60", None)
        self.__UML2_Classifier60 = value if value is not None else set()
        
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
                    

class UML2_ActivityNode(RedefinableElement):

    pass
class UML2_State(RedefinableElement, Namespace, Vertex):

    pass
class UML2_Region(RedefinableElement, Namespace):

    pass
class UML2_Transition(RedefinableElement):

    pass
class UML2_ActivityEdge(RedefinableElement):

    pass
class UML2_MessageTrigger(Trigger):

    pass
class ControlNode:

    pass
class UML2_DecisionNode(ControlNode):

    pass
class UML2_JoinNode(ControlNode):

    pass
class UML2_MergeNode(ControlNode):

    pass
class UML2_InitialNode(ControlNode):

    pass
class UML2_ForkNode(ControlNode):

    pass
class UML2_FinalNode(ControlNode):

    pass