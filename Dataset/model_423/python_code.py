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
class VisibilityKind(Enum):
    package = "package"
    private = "private"
    protected = "protected"
    public = "public"
class AggregationKind(Enum):
    composite = "composite"
    none = "none"
    shared = "shared"


############################################
# Definition of Classes
############################################

class StructuralFeature:

    pass
class InteractionOccurrence:

    pass
class UML2_PartDecomposition(InteractionOccurrence):

    pass
class Property:

    pass
class UML2_ExtensionEnd(Property):

    pass
class UML2_Port(Property):

    pass
class DeploymentTarget:

    pass
class MessageEnd:

    pass
class UML2_Gate(MessageEnd):

    pass
class InputPin:

    pass
class UML2_ValuePin(InputPin):

    pass
class State:

    pass
class UML2_FinalState(State):

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
class OpaqueExpression:

    pass
class UML2_Expression(OpaqueExpression):

    pass
class InstanceSpecification:

    pass
class UML2_EnumerationLiteral(InstanceSpecification):

    pass
class Constraint:

    pass
class UML2_IntervalConstraint(Constraint):

    pass
class UML2_InteractionConstraint(Constraint):

    pass
class StructuredClassifier:

    pass
class UML2_EncapsulatedClassifier(StructuredClassifier):

    pass
class BehavioralFeature:

    pass
class DeployedArtifact:

    pass
class FinalNode:

    pass
class UML2_ActivityFinalNode(FinalNode):

    pass
class UML2_FlowFinalNode(FinalNode):

    pass
class WriteLinkAction:

    pass
class UML2_CreateLinkAction(WriteLinkAction):

    pass
class Vertex:

    pass
class UML2_Pseudostate(Vertex):

    pass
class UML2_ConnectionPointReference(Vertex):

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
class IntervalConstraint:

    pass
class UML2_TimeConstraint(IntervalConstraint):

    pass
class UML2_DurationConstraint(IntervalConstraint):

    pass
class Behavior:

    pass
class UML2_Activity(Behavior):

    pass
class UML2_StateMachine(Behavior):

    pass
class Interval:

    pass
class UML2_TimeInterval(Interval):

    pass
class UML2_DurationInterval(Interval):

    pass
class UML2_Element:

    pass
class Relationship:

    pass
class UML2_DirectedRelationship(Relationship):

    pass
class CentralBufferNode:

    pass
class UML2_DataStoreNode(CentralBufferNode):

    pass
class CallAction:

    pass
class UML2_CallOperationAction(CallAction):

    pass
class UML2_CallBehaviorAction(CallAction):

    pass
class Artifact:

    pass
class UML2_DeploymentSpecification(Artifact):

    pass
class TemplateSignature:

    pass
class Type:

    pass
class MessageTrigger:

    pass
class UML2_AnyTrigger(MessageTrigger):

    pass
class UML2_SignalTrigger(MessageTrigger):

    pass
class UML2_CallTrigger(MessageTrigger):

    pass
class UML2_DestroyLinkAction(WriteLinkAction):

    pass
class ValueSpecification:

    pass
class UML2_Interval(ValueSpecification):

    pass
class UML2_InstanceValue(ValueSpecification):

    pass
class UML2_LiteralSpecification(ValueSpecification):

    pass
class UML2_TimeExpression(ValueSpecification):

    pass
class UML2_Duration(ValueSpecification):

    pass
class UML2_OpaqueExpression(ValueSpecification):

    pass
class Pin:

    pass
class UML2_OutputPin(Pin):

    pass
class TemplateParameter:

    pass
class UML2_ClassifierTemplateParameter(TemplateParameter):

    pass
class UML2_OperationTemplateParameter(TemplateParameter):

    pass
class UML2_ConnectableElementTemplateParameter(TemplateParameter):

    pass
class Class:

    pass
class UML2_Component(Class):

    pass
class UML2_Node(DeploymentTarget, Class):

    pass
class UML2_Behavior(Class):

    pass
class UML2_Stereotype(Class):

    pass
class UML2_Reception(BehavioralFeature):

    pass
class LinkEndData:

    pass
class UML2_LinkEndCreationData(LinkEndData):

    pass
class EncapsulatedClassifier:

    pass
class Abstraction:

    pass
class UML2_Manifestation(Abstraction):

    pass
class UML2_Realization(Abstraction):

    pass
class Dependency:

    pass
class UML2_Usage(Dependency):

    pass
class UML2_Abstraction(Dependency):

    pass
class UML2_Deployment(Dependency):

    pass
class AcceptEventAction:

    pass
class UML2_AcceptCallAction(AcceptEventAction):

    pass
class ActivityGroup:

    pass
class UML2_InterruptibleActivityRegion(ActivityGroup):

    pass
class CreateLinkAction:

    pass
class UML2_CreateLinkObjectAction(CreateLinkAction):

    pass
class Feature:

    pass
class UML2_Connector(Feature):

    pass
class BehavioredClassifier:

    pass
class UML2_Class(BehavioredClassifier, EncapsulatedClassifier):

    def __init__(self, isActive: bool, UML2_Class: set["UML2_Classifier"] = None, UML2_Class8: set["UML2_Reception"] = None):
        self.isActive = isActive
        self.UML2_Class = UML2_Class if UML2_Class is not None else set()
        self.UML2_Class8 = UML2_Class8 if UML2_Class8 is not None else set()
        
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
                if hasattr(item, "UML2_Classifier6"):
                    opp_val = getattr(item, "UML2_Classifier6", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Classifier6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Classifier6"):
                    opp_val = getattr(item, "UML2_Classifier6", None)
                    
                    setattr(item, "UML2_Classifier6", self)
                    

    @property
    def UML2_Class8(self):
        return self.__UML2_Class8

    @UML2_Class8.setter
    def UML2_Class8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Class__UML2_Class8", None)
        self.__UML2_Class8 = value if value is not None else set()
        
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
                    

class UML2_Collaboration(StructuredClassifier, BehavioredClassifier):

    pass
class UML2_UseCase(BehavioredClassifier):

    pass
class TemplateableElement:

    pass
class UML2_StringExpression(TemplateableElement):

    pass
class UML2_NamedElement(TemplateableElement):

    def __init__(self, name: str, visibility: str, UML2_NamedElement: "UML2_Namespace" = None, UML2_NamedElement18: "UML2_Classifier" = None):
        self.name = name
        self.visibility = visibility
        self.UML2_NamedElement = UML2_NamedElement
        self.UML2_NamedElement18 = UML2_NamedElement18
        
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
    def UML2_NamedElement18(self):
        return self.__UML2_NamedElement18

    @UML2_NamedElement18.setter
    def UML2_NamedElement18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_NamedElement__UML2_NamedElement18", None)
        self.__UML2_NamedElement18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Classifier17"):
                opp_val = getattr(old_value, "UML2_Classifier17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Classifier17"):
                opp_val = getattr(value, "UML2_Classifier17", None)
                if opp_val is None:
                    setattr(value, "UML2_Classifier17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UML2_Comment(TemplateableElement):

    pass
class UML2_Permission(Dependency):

    pass
class Transition:

    pass
class UML2_ProtocolTransition(Transition):

    pass
class ObjectNode:

    pass
class UML2_ActivityParameterNode(ObjectNode):

    pass
class UML2_ExpansionNode(ObjectNode):

    pass
class UML2_CentralBufferNode(ObjectNode):

    pass
class StateMachine:

    pass
class UML2_ProtocolStateMachine(StateMachine):

    pass
class PackageableElement:

    pass
class UML2_PrimitiveFunction(PackageableElement):

    pass
class UML2_Type(PackageableElement):

    pass
class UML2_Constraint(PackageableElement):

    pass
class UML2_InstanceSpecification(DeploymentTarget, DeployedArtifact, PackageableElement):

    pass
class UML2_GeneralizationSet(PackageableElement):

    pass
class ControlNode:

    pass
class UML2_InitialNode(ControlNode):

    pass
class UML2_FinalNode(ControlNode):

    pass
class UML2_ForkNode(ControlNode):

    pass
class UML2_DecisionNode(ControlNode):

    pass
class UML2_JoinNode(ControlNode):

    pass
class Trigger:

    pass
class UML2_MessageTrigger(Trigger):

    pass
class UML2_ChangeTrigger(Trigger):

    pass
class RedefinableElement:

    pass
class UML2_Transition(RedefinableElement):

    pass
class UML2_RedefinableTemplateSignature(TemplateSignature, RedefinableElement):

    pass
class UML2_Feature(RedefinableElement):

    def __init__(self, isStatic: bool, UML2_Feature: "UML2_Classifier" = None, UML2_Feature57: set["UML2_Classifier"] = None):
        self.isStatic = isStatic
        self.UML2_Feature = UML2_Feature
        self.UML2_Feature57 = UML2_Feature57 if UML2_Feature57 is not None else set()
        
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
            if hasattr(old_value, "UML2_Classifier15"):
                opp_val = getattr(old_value, "UML2_Classifier15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Classifier15"):
                opp_val = getattr(value, "UML2_Classifier15", None)
                if opp_val is None:
                    setattr(value, "UML2_Classifier15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Feature57(self):
        return self.__UML2_Feature57

    @UML2_Feature57.setter
    def UML2_Feature57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Feature__UML2_Feature57", None)
        self.__UML2_Feature57 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Classifier58"):
                    opp_val = getattr(item, "UML2_Classifier58", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Classifier58", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Classifier58"):
                    opp_val = getattr(item, "UML2_Classifier58", None)
                    
                    setattr(item, "UML2_Classifier58", self)
                    

class UML2_ExtensionPoint(RedefinableElement):

    pass
class UML2_ActivityNode(RedefinableElement):

    pass
class LiteralSpecification:

    pass
class UML2_LiteralUnlimitedNatural(LiteralSpecification):

    pass
class UML2_LiteralNull(LiteralSpecification):

    pass
class UML2_LiteralInteger(LiteralSpecification):

    pass
class UML2_LiteralBoolean(LiteralSpecification):

    pass
class UML2_LiteralString(LiteralSpecification):

    pass
class WriteVariableAction:

    pass
class UML2_RemoveVariableValueAction(WriteVariableAction):

    pass
class UML2_AddVariableValueAction(WriteVariableAction):

    pass
class VariableAction:

    pass
class UML2_ReadVariableAction(VariableAction):

    pass
class UML2_ClearVariableAction(VariableAction):

    pass
class UML2_WriteVariableAction(VariableAction):

    pass
class UML2_ActivityEdge(RedefinableElement):

    pass
class UML2_TimeTrigger(Trigger):

    pass
class UML2_MergeNode(ControlNode):

    pass
class UML2_InputPin(Pin):

    pass
class StructuralFeatureAction:

    pass
class UML2_ClearStructuralFeatureAction(StructuralFeatureAction):

    pass
class UML2_ReadStructuralFeatureAction(StructuralFeatureAction):

    pass
class UML2_WriteStructuralFeatureAction(StructuralFeatureAction):

    pass
class Package:

    pass
class UML2_Profile(Package):

    pass
class UML2_Model(Package):

    pass
class Realization:

    pass
class UML2_Substitution(Realization):

    pass
class UML2_Implementation(Realization):

    pass
class LinkAction:

    pass
class UML2_ReadLinkAction(LinkAction):

    pass
class UML2_WriteLinkAction(LinkAction):

    pass
class DataType:

    pass
class UML2_Enumeration(DataType):

    pass
class UML2_PrimitiveType(DataType):

    pass
class ParameterableElement:

    pass
class NamedElement:

    pass
class UML2_ParameterSet(NamedElement):

    pass
class UML2_Namespace(NamedElement):

    pass
class UML2_Lifeline(NamedElement):

    pass
class UML2_Vertex(NamedElement):

    pass
class UML2_MessageEnd(NamedElement):

    pass
class UML2_Trigger(NamedElement):

    pass
class UML2_CollaborationOccurrence(NamedElement):

    pass
class UML2_GeneralOrdering(NamedElement):

    pass
class UML2_TypedElement(NamedElement):

    pass
class UML2_ConnectableElement(ParameterableElement, NamedElement):

    pass
class UML2_RedefinableElement(NamedElement):

    pass
class UML2_DeploymentTarget(NamedElement):

    pass
class UML2_ActivityPartition(NamedElement, ActivityGroup):

    pass
class UML2_Message(NamedElement):

    pass
class UML2_InteractionFragment(NamedElement):

    pass
class UML2_DeployedArtifact(NamedElement):

    pass
class UML2_PackageableElement(ParameterableElement, NamedElement):

    pass
class InvocationAction:

    pass
class UML2_BroadcastSignalAction(InvocationAction):

    pass
class UML2_SendSignalAction(InvocationAction):

    pass
class UML2_SendObjectAction(InvocationAction):

    pass
class UML2_CallAction(InvocationAction):

    pass
class InteractionFragment:

    pass
class UML2_InteractionOccurrence(InteractionFragment):

    pass
class UML2_Continuation(InteractionFragment):

    pass
class UML2_EventOccurrence(InteractionFragment, MessageEnd):

    pass
class UML2_Interaction(InteractionFragment, Behavior):

    pass
class UML2_ExecutionOccurrence(InteractionFragment):

    pass
class UML2_StateInvariant(InteractionFragment):

    pass
class UML2_CombinedFragment(InteractionFragment):

    pass
class Namespace:

    pass
class UML2_Region(Namespace, RedefinableElement):

    pass
class UML2_State(Namespace, Vertex, RedefinableElement):

    pass
class UML2_InteractionOperand(Namespace, InteractionFragment):

    pass
class UML2_BehavioralFeature(Namespace, Feature):

    pass
class UML2_Package(Namespace, PackageableElement):

    pass
class DirectedRelationship:

    pass
class UML2_ProtocolConformance(DirectedRelationship):

    pass
class UML2_Include(DirectedRelationship, NamedElement):

    pass
class UML2_Extend(DirectedRelationship, NamedElement):

    pass
class UML2_Generalization(DirectedRelationship):

    pass
class UML2_ElementImport(DirectedRelationship):

    pass
class UML2_InformationFlow(DirectedRelationship, PackageableElement):

    pass
class UML2_PackageMerge(DirectedRelationship):

    pass
class UML2_PackageImport(DirectedRelationship):

    pass
class UML2_Dependency(DirectedRelationship, PackageableElement):

    pass
class UML2_TemplateBinding(DirectedRelationship):

    pass
class ExecutableNode:

    pass
class UML2_Action(ExecutableNode):

    pass
class Association:

    pass
class UML2_AssociationClass(Association, Class):

    pass
class UML2_CommunicationPath(Association):

    pass
class UML2_Extension(Association):

    pass
class Action:

    pass
class UML2_ApplyFunctionAction(Action):

    pass
class UML2_ReplyAction(Action):

    pass
class UML2_CreateObjectAction(Action):

    pass
class UML2_ReadLinkObjectEndQualifierAction(Action):

    pass
class UML2_ReadExtentAction(Action):

    pass
class UML2_StartOwnedBehaviorAction(Action):

    pass
class UML2_VariableAction(Action):

    pass
class UML2_DestroyObjectAction(Action):

    pass
class UML2_AcceptEventAction(Action):

    pass
class UML2_StructuralFeatureAction(Action):

    pass
class UML2_TestIdentityAction(Action):

    pass
class UML2_InvocationAction(Action):

    pass
class UML2_ReclassifyObjectAction(Action):

    pass
class UML2_ClearAssociationAction(Action):

    pass
class UML2_StructuredActivityNode(Action, Namespace, ActivityGroup):

    pass
class UML2_RaiseExceptionAction(Action):

    pass
class UML2_ReadLinkObjectEndAction(Action):

    pass
class UML2_ReadSelfAction(Action):

    pass
class UML2_LinkAction(Action):

    pass
class UML2_ReadIsClassifiedObjectAction(Action):

    pass
class Element:

    pass
class UML2_ParameterableElement(Element):

    pass
class UML2_Clause(Element):

    pass
class UML2_TemplateableElement(Element):

    pass
class UML2_LinkEndData(Element):

    pass
class UML2_QualifierValue(Element):

    pass
class UML2_TemplateSignature(Element):

    pass
class UML2_TemplateParameterSubstitution(Element):

    pass
class UML2_Relationship(Element):

    pass
class UML2_ActivityGroup(Element):

    pass
class UML2_TemplateParameter(Element):

    pass
class UML2_ExceptionHandler(Element):

    pass
class UML2_MultiplicityElement(Element):

    def __init__(self, isOrdered: bool, isUnique: bool, lower: int, upper: str):
        self.isOrdered = isOrdered
        self.isUnique = isUnique
        self.lower = lower
        self.upper = upper
        
    @property
    def isOrdered(self) -> bool:
        return self.__isOrdered

    @isOrdered.setter
    def isOrdered(self, isOrdered: bool):
        self.__isOrdered = isOrdered

    @property
    def lower(self) -> int:
        return self.__lower

    @lower.setter
    def lower(self, lower: int):
        self.__lower = lower

    @property
    def upper(self) -> str:
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper

    @property
    def isUnique(self) -> bool:
        return self.__isUnique

    @isUnique.setter
    def isUnique(self, isUnique: bool):
        self.__isUnique = isUnique

class UML2_Slot(Element):

    pass
class Node:

    pass
class UML2_ExecutionEnvironment(Node):

    pass
class UML2_Device(Node):

    pass
class StructuredActivityNode:

    pass
class UML2_LoopNode(StructuredActivityNode):

    pass
class UML2_ExpansionRegion(StructuredActivityNode):

    pass
class UML2_ConditionalNode(StructuredActivityNode):

    pass
class Classifier:

    pass
class UML2_Association(Classifier, Relationship):

    pass
class UML2_Actor(Classifier):

    pass
class UML2_DataType(Classifier):

    pass
class UML2_Signal(Classifier):

    pass
class UML2_BehavioredClassifier(Classifier):

    pass
class UML2_ParameterableClassifier(Classifier):

    pass
class UML2_Artifact(Classifier, DeployedArtifact):

    pass
class UML2_StructuredClassifier(Classifier):

    pass
class UML2_InformationItem(Classifier):

    pass
class UML2_TemplateableClassifier(Classifier):

    pass
class UML2_Interface(Classifier):

    pass
class MultiplicityElement:

    pass
class UML2_Pin(ObjectNode, MultiplicityElement):

    pass
class UML2_ConnectorEnd(MultiplicityElement):

    pass
class TypedElement:

    pass
class UML2_StructuralFeature(Feature, TypedElement, MultiplicityElement):

    def __init__(self, isReadOnly: bool, UML2_StructuralFeature: "UML2_Slot" = None, UML2_StructuralFeature44: "UML2_StructuralFeatureAction" = None):
        self.isReadOnly = isReadOnly
        self.UML2_StructuralFeature = UML2_StructuralFeature
        self.UML2_StructuralFeature44 = UML2_StructuralFeature44
        
    @property
    def isReadOnly(self) -> bool:
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: bool):
        self.__isReadOnly = isReadOnly

    @property
    def UML2_StructuralFeature44(self):
        return self.__UML2_StructuralFeature44

    @UML2_StructuralFeature44.setter
    def UML2_StructuralFeature44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_StructuralFeature__UML2_StructuralFeature44", None)
        self.__UML2_StructuralFeature44 = value
        
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
            if hasattr(old_value, "UML2_Slot"):
                opp_val = getattr(old_value, "UML2_Slot", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Slot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Slot"):
                opp_val = getattr(value, "UML2_Slot", None)
                setattr(value, "UML2_Slot", self)

class UML2_ValueSpecification(ParameterableElement, TypedElement):

    pass
class UML2_Operation(ParameterableElement, TypedElement, BehavioralFeature, MultiplicityElement):

    def __init__(self, isQuery: bool, UML2_Operation: set["UML2_Parameter"] = None, UML2_Operation71: "UML2_Constraint" = None):
        self.isQuery = isQuery
        self.UML2_Operation = UML2_Operation if UML2_Operation is not None else set()
        self.UML2_Operation71 = UML2_Operation71
        
    @property
    def isQuery(self) -> bool:
        return self.__isQuery

    @isQuery.setter
    def isQuery(self, isQuery: bool):
        self.__isQuery = isQuery

    @property
    def UML2_Operation71(self):
        return self.__UML2_Operation71

    @UML2_Operation71.setter
    def UML2_Operation71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Operation__UML2_Operation71", None)
        self.__UML2_Operation71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Constraint72"):
                opp_val = getattr(old_value, "UML2_Constraint72", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Constraint72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Constraint72"):
                opp_val = getattr(value, "UML2_Constraint72", None)
                setattr(value, "UML2_Constraint72", self)

    @property
    def UML2_Operation(self):
        return self.__UML2_Operation

    @UML2_Operation.setter
    def UML2_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Operation__UML2_Operation", None)
        self.__UML2_Operation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Parameter"):
                    opp_val = getattr(item, "UML2_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Parameter"):
                    opp_val = getattr(item, "UML2_Parameter", None)
                    
                    setattr(item, "UML2_Parameter", self)
                    

class UML2_ObjectNode(ActivityNode, TypedElement):

    pass
class ConnectableElement:

    pass
class UML2_Variable(ConnectableElement, TypedElement, MultiplicityElement):

    pass
class UML2_Property(DeploymentTarget, StructuralFeature, ConnectableElement):

    def __init__(self, isComposite: bool, isDerived: bool, isDerivedUnion: bool, aggregation: str, UML2_Property: "UML2_LinkEndData" = None, UML2_Property33: "UML2_Association" = None, UML2_Property36: "UML2_Association" = None, UML2_Property39: "UML2_QualifierValue" = None, UML2_Property75: "UML2_Property" = None, UML2_Property73: set["UML2_Property"] = None, UML2_Property77: "UML2_Association" = None, UML2_Property81: "UML2_Property" = None, UML2_Property79: set["UML2_Property"] = None):
        self.isComposite = isComposite
        self.isDerived = isDerived
        self.isDerivedUnion = isDerivedUnion
        self.aggregation = aggregation
        self.UML2_Property = UML2_Property
        self.UML2_Property33 = UML2_Property33
        self.UML2_Property36 = UML2_Property36
        self.UML2_Property39 = UML2_Property39
        self.UML2_Property75 = UML2_Property75
        self.UML2_Property73 = UML2_Property73 if UML2_Property73 is not None else set()
        self.UML2_Property77 = UML2_Property77
        self.UML2_Property81 = UML2_Property81
        self.UML2_Property79 = UML2_Property79 if UML2_Property79 is not None else set()
        
    @property
    def isComposite(self) -> bool:
        return self.__isComposite

    @isComposite.setter
    def isComposite(self, isComposite: bool):
        self.__isComposite = isComposite

    @property
    def isDerivedUnion(self) -> bool:
        return self.__isDerivedUnion

    @isDerivedUnion.setter
    def isDerivedUnion(self, isDerivedUnion: bool):
        self.__isDerivedUnion = isDerivedUnion

    @property
    def isDerived(self) -> bool:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: bool):
        self.__isDerived = isDerived

    @property
    def aggregation(self) -> str:
        return self.__aggregation

    @aggregation.setter
    def aggregation(self, aggregation: str):
        self.__aggregation = aggregation

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
            if hasattr(old_value, "UML2_QualifierValue38"):
                opp_val = getattr(old_value, "UML2_QualifierValue38", None)
                if opp_val == self:
                    setattr(old_value, "UML2_QualifierValue38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_QualifierValue38"):
                opp_val = getattr(value, "UML2_QualifierValue38", None)
                setattr(value, "UML2_QualifierValue38", self)

    @property
    def UML2_Property79(self):
        return self.__UML2_Property79

    @UML2_Property79.setter
    def UML2_Property79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property79", None)
        self.__UML2_Property79 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Property81"):
                    opp_val = getattr(item, "UML2_Property81", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Property81", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Property81"):
                    opp_val = getattr(item, "UML2_Property81", None)
                    
                    setattr(item, "UML2_Property81", self)
                    

    @property
    def UML2_Property36(self):
        return self.__UML2_Property36

    @UML2_Property36.setter
    def UML2_Property36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property36", None)
        self.__UML2_Property36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Association35"):
                opp_val = getattr(old_value, "UML2_Association35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Association35"):
                opp_val = getattr(value, "UML2_Association35", None)
                if opp_val is None:
                    setattr(value, "UML2_Association35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Property33(self):
        return self.__UML2_Property33

    @UML2_Property33.setter
    def UML2_Property33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property33", None)
        self.__UML2_Property33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Association"):
                opp_val = getattr(old_value, "UML2_Association", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Association"):
                opp_val = getattr(value, "UML2_Association", None)
                if opp_val is None:
                    setattr(value, "UML2_Association", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Property73(self):
        return self.__UML2_Property73

    @UML2_Property73.setter
    def UML2_Property73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property73", None)
        self.__UML2_Property73 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Property75"):
                    opp_val = getattr(item, "UML2_Property75", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Property75", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Property75"):
                    opp_val = getattr(item, "UML2_Property75", None)
                    
                    setattr(item, "UML2_Property75", self)
                    

    @property
    def UML2_Property81(self):
        return self.__UML2_Property81

    @UML2_Property81.setter
    def UML2_Property81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property81", None)
        self.__UML2_Property81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Property79"):
                opp_val = getattr(old_value, "UML2_Property79", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Property79"):
                opp_val = getattr(value, "UML2_Property79", None)
                if opp_val is None:
                    setattr(value, "UML2_Property79", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Property75(self):
        return self.__UML2_Property75

    @UML2_Property75.setter
    def UML2_Property75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property75", None)
        self.__UML2_Property75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Property73"):
                opp_val = getattr(old_value, "UML2_Property73", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Property73"):
                opp_val = getattr(value, "UML2_Property73", None)
                if opp_val is None:
                    setattr(value, "UML2_Property73", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Property77(self):
        return self.__UML2_Property77

    @UML2_Property77.setter
    def UML2_Property77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property77", None)
        self.__UML2_Property77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Association78"):
                opp_val = getattr(old_value, "UML2_Association78", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Association78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Association78"):
                opp_val = getattr(value, "UML2_Association78", None)
                setattr(value, "UML2_Association78", self)

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
            if hasattr(old_value, "UML2_LinkEndData29"):
                opp_val = getattr(old_value, "UML2_LinkEndData29", None)
                if opp_val == self:
                    setattr(old_value, "UML2_LinkEndData29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_LinkEndData29"):
                opp_val = getattr(value, "UML2_LinkEndData29", None)
                setattr(value, "UML2_LinkEndData29", self)

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

class EventOccurrence:

    pass
class UML2_Stop(EventOccurrence):

    pass
class ActivityEdge:

    pass
class UML2_ControlFlow(ActivityEdge):

    pass
class UML2_ObjectFlow(ActivityEdge):

    pass
class UML2_Classifier(Namespace, Type, RedefinableElement):

    def __init__(self, isAbstract: bool, UML2_Classifier: "UML2_Action" = None, UML2_Classifier6: "UML2_Class" = None, UML2_Classifier15: set["UML2_Feature"] = None, UML2_Classifier17: set["UML2_NamedElement"] = None, UML2_Classifier20: set["UML2_Generalization"] = None, UML2_Classifier10: "UML2_CreateObjectAction" = None, UML2_Classifier54: "UML2_InstanceSpecification" = None, UML2_Classifier58: "UML2_Feature" = None, UML2_Classifier61: "UML2_Generalization" = None):
        self.isAbstract = isAbstract
        self.UML2_Classifier = UML2_Classifier
        self.UML2_Classifier6 = UML2_Classifier6
        self.UML2_Classifier15 = UML2_Classifier15 if UML2_Classifier15 is not None else set()
        self.UML2_Classifier17 = UML2_Classifier17 if UML2_Classifier17 is not None else set()
        self.UML2_Classifier20 = UML2_Classifier20 if UML2_Classifier20 is not None else set()
        self.UML2_Classifier10 = UML2_Classifier10
        self.UML2_Classifier54 = UML2_Classifier54
        self.UML2_Classifier58 = UML2_Classifier58
        self.UML2_Classifier61 = UML2_Classifier61
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def UML2_Classifier10(self):
        return self.__UML2_Classifier10

    @UML2_Classifier10.setter
    def UML2_Classifier10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier10", None)
        self.__UML2_Classifier10 = value
        
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
    def UML2_Classifier61(self):
        return self.__UML2_Classifier61

    @UML2_Classifier61.setter
    def UML2_Classifier61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier61", None)
        self.__UML2_Classifier61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Generalization60"):
                opp_val = getattr(old_value, "UML2_Generalization60", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Generalization60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Generalization60"):
                opp_val = getattr(value, "UML2_Generalization60", None)
                setattr(value, "UML2_Generalization60", self)

    @property
    def UML2_Classifier15(self):
        return self.__UML2_Classifier15

    @UML2_Classifier15.setter
    def UML2_Classifier15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier15", None)
        self.__UML2_Classifier15 = value if value is not None else set()
        
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
    def UML2_Classifier20(self):
        return self.__UML2_Classifier20

    @UML2_Classifier20.setter
    def UML2_Classifier20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier20", None)
        self.__UML2_Classifier20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Generalization21"):
                    opp_val = getattr(item, "UML2_Generalization21", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Generalization21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Generalization21"):
                    opp_val = getattr(item, "UML2_Generalization21", None)
                    
                    setattr(item, "UML2_Generalization21", self)
                    

    @property
    def UML2_Classifier54(self):
        return self.__UML2_Classifier54

    @UML2_Classifier54.setter
    def UML2_Classifier54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier54", None)
        self.__UML2_Classifier54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_InstanceSpecification53"):
                opp_val = getattr(old_value, "UML2_InstanceSpecification53", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_InstanceSpecification53"):
                opp_val = getattr(value, "UML2_InstanceSpecification53", None)
                if opp_val is None:
                    setattr(value, "UML2_InstanceSpecification53", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def UML2_Classifier6(self):
        return self.__UML2_Classifier6

    @UML2_Classifier6.setter
    def UML2_Classifier6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier6", None)
        self.__UML2_Classifier6 = value
        
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
    def UML2_Classifier58(self):
        return self.__UML2_Classifier58

    @UML2_Classifier58.setter
    def UML2_Classifier58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier58", None)
        self.__UML2_Classifier58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Feature57"):
                opp_val = getattr(old_value, "UML2_Feature57", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Feature57"):
                opp_val = getattr(value, "UML2_Feature57", None)
                if opp_val is None:
                    setattr(value, "UML2_Feature57", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Classifier17(self):
        return self.__UML2_Classifier17

    @UML2_Classifier17.setter
    def UML2_Classifier17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier17", None)
        self.__UML2_Classifier17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_NamedElement18"):
                    opp_val = getattr(item, "UML2_NamedElement18", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_NamedElement18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_NamedElement18"):
                    opp_val = getattr(item, "UML2_NamedElement18", None)
                    
                    setattr(item, "UML2_NamedElement18", self)
                    
