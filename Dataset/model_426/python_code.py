from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class VisibilityKind(Enum):
    private = "private"
    protected = "protected"
    public = "public"
    package = "package"
class ParameterDirectionKind(Enum):
    in = "in"
    inout = "inout"
    out = "out"
    return = "return"
class AggregationKind(Enum):
    composite = "composite"
    none = "none"
    shared = "shared"


############################################
# Definition of Classes
############################################

class InteractionOccurrence:

    pass
class UML2_PartDecomposition(InteractionOccurrence):

    pass
class Type:

    pass
class InstanceSpecification:

    pass
class UML2_EnumerationLiteral(InstanceSpecification):

    pass
class Abstraction:

    pass
class UML2_Manifestation(Abstraction):

    pass
class UML2_Realization(Abstraction):

    pass
class WriteVariableAction:

    pass
class UML2_RemoveVariableValueAction(WriteVariableAction):

    pass
class UML2_AddVariableValueAction(WriteVariableAction):

    pass
class Node:

    pass
class UML2_ExecutionEnvironment(Node):

    pass
class ActivityEdge:

    pass
class UML2_ObjectFlow(ActivityEdge):

    pass
class UML2_ControlFlow(ActivityEdge):

    pass
class StructuredClassifier:

    pass
class UML2_EncapsulatedClassifier(StructuredClassifier):

    pass
class State:

    pass
class UML2_FinalState(State):

    pass
class UML2_Device(Node):

    pass
class StateMachine:

    pass
class UML2_ProtocolStateMachine(StateMachine):

    pass
class Transition:

    pass
class UML2_ProtocolTransition(Transition):

    pass
class Pin:

    pass
class Artifact:

    pass
class UML2_DeploymentSpecification(Artifact):

    pass
class UML2_InputPin(Pin):

    pass
class CallAction:

    pass
class UML2_CallBehaviorAction(CallAction):

    pass
class UML2_CallOperationAction(CallAction):

    pass
class TemplateParameter:

    pass
class UML2_OperationTemplateParameter(TemplateParameter):

    pass
class UML2_ClassifierTemplateParameter(TemplateParameter):

    pass
class UML2_ConnectableElementTemplateParameter(TemplateParameter):

    pass
class StructuralFeature:

    pass
class ControlNode:

    pass
class UML2_InitialNode(ControlNode):

    pass
class UML2_JoinNode(ControlNode):

    pass
class UML2_FinalNode(ControlNode):

    pass
class UML2_ForkNode(ControlNode):

    pass
class UML2_MergeNode(ControlNode):

    pass
class WriteStructuralFeatureAction:

    pass
class UML2_TimeObservationAction(WriteStructuralFeatureAction):

    pass
class UML2_RemoveStructuralFeatureValueAction(WriteStructuralFeatureAction):

    pass
class UML2_DurationObservationAction(WriteStructuralFeatureAction):

    pass
class UML2_AddStructuralFeatureValueAction(WriteStructuralFeatureAction):

    pass
class UML2_DecisionNode(ControlNode):

    pass
class Package:

    pass
class UML2_Profile(Package):

    pass
class UML2_Model(Package):

    pass
class OpaqueExpression:

    pass
class UML2_Expression(OpaqueExpression):

    pass
class EventOccurrence:

    pass
class UML2_Stop(EventOccurrence):

    pass
class EncapsulatedClassifier:

    pass
class BehavioredClassifier:

    pass
class UML2_UseCase(BehavioredClassifier):

    pass
class UML2_Collaboration(StructuredClassifier, BehavioredClassifier):

    pass
class UML2_Class(EncapsulatedClassifier, BehavioredClassifier):

    def __init__(self, isActive: bool, UML2_Class: set["UML2_Classifier"] = None, UML2_Class22: set["UML2_Reception"] = None):
        self.isActive = isActive
        self.UML2_Class = UML2_Class if UML2_Class is not None else set()
        self.UML2_Class22 = UML2_Class22 if UML2_Class22 is not None else set()
        
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
                if hasattr(item, "UML2_Classifier20"):
                    opp_val = getattr(item, "UML2_Classifier20", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Classifier20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Classifier20"):
                    opp_val = getattr(item, "UML2_Classifier20", None)
                    
                    setattr(item, "UML2_Classifier20", self)
                    

    @property
    def UML2_Class22(self):
        return self.__UML2_Class22

    @UML2_Class22.setter
    def UML2_Class22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Class__UML2_Class22", None)
        self.__UML2_Class22 = value if value is not None else set()
        
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
                    

class LinkAction:

    pass
class UML2_WriteLinkAction(LinkAction):

    pass
class UML2_ReadLinkAction(LinkAction):

    pass
class InputPin:

    pass
class UML2_ValuePin(InputPin):

    pass
class MessageEnd:

    pass
class UML2_Gate(MessageEnd):

    pass
class TemplateSignature:

    pass
class FinalNode:

    pass
class UML2_FlowFinalNode(FinalNode):

    pass
class DataType:

    pass
class UML2_Enumeration(DataType):

    pass
class UML2_PrimitiveType(DataType):

    pass
class ParameterableElement:

    pass
class BehavioralFeature:

    pass
class UML2_Reception(BehavioralFeature):

    pass
class StructuralFeatureAction:

    pass
class UML2_ReadStructuralFeatureAction(StructuralFeatureAction):

    pass
class UML2_WriteStructuralFeatureAction(StructuralFeatureAction):

    pass
class UML2_ClearStructuralFeatureAction(StructuralFeatureAction):

    pass
class CreateLinkAction:

    pass
class UML2_CreateLinkObjectAction(CreateLinkAction):

    pass
class Vertex:

    pass
class UML2_ConnectionPointReference(Vertex):

    pass
class UML2_Pseudostate(Vertex):

    pass
class Trigger:

    pass
class UML2_ChangeTrigger(Trigger):

    pass
class UML2_TimeTrigger(Trigger):

    pass
class UML2_MessageTrigger(Trigger):

    pass
class UML2_ActivityFinalNode(FinalNode):

    pass
class Interval:

    pass
class UML2_TimeInterval(Interval):

    pass
class UML2_DurationInterval(Interval):

    pass
class Realization:

    pass
class UML2_Substitution(Realization):

    pass
class UML2_Implementation(Realization):

    pass
class CentralBufferNode:

    pass
class UML2_DataStoreNode(CentralBufferNode):

    pass
class ObjectNode:

    pass
class UML2_ActivityParameterNode(ObjectNode):

    pass
class UML2_ExpansionNode(ObjectNode):

    pass
class UML2_CentralBufferNode(ObjectNode):

    pass
class VariableAction:

    pass
class UML2_ClearVariableAction(VariableAction):

    pass
class UML2_WriteVariableAction(VariableAction):

    pass
class UML2_ReadVariableAction(VariableAction):

    pass
class ExecutableNode:

    pass
class UML2_Action(ExecutableNode):

    pass
class MultiplicityElement:

    pass
class UML2_Pin(MultiplicityElement, ObjectNode):

    pass
class UML2_ConnectorEnd(MultiplicityElement):

    pass
class ConnectableElement:

    pass
class TypedElement:

    pass
class UML2_ValueSpecification(ParameterableElement, TypedElement):

    pass
class UML2_Variable(TypedElement, ConnectableElement, MultiplicityElement):

    pass
class UML2_Operation(ParameterableElement, TypedElement, MultiplicityElement, BehavioralFeature):

    def __init__(self, isQuery: bool, UML2_Operation: set["UML2_Parameter"] = None, UML2_Operation25: "UML2_Constraint" = None):
        self.isQuery = isQuery
        self.UML2_Operation = UML2_Operation if UML2_Operation is not None else set()
        self.UML2_Operation25 = UML2_Operation25
        
    @property
    def isQuery(self) -> bool:
        return self.__isQuery

    @isQuery.setter
    def isQuery(self, isQuery: bool):
        self.__isQuery = isQuery

    @property
    def UML2_Operation25(self):
        return self.__UML2_Operation25

    @UML2_Operation25.setter
    def UML2_Operation25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Operation__UML2_Operation25", None)
        self.__UML2_Operation25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Constraint"):
                opp_val = getattr(old_value, "UML2_Constraint", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Constraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Constraint"):
                opp_val = getattr(value, "UML2_Constraint", None)
                setattr(value, "UML2_Constraint", self)

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
                    

class UML2_Parameter(TypedElement, ConnectableElement, MultiplicityElement):

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

class ActivityNode:

    pass
class UML2_ControlNode(ActivityNode):

    pass
class UML2_ExecutableNode(ActivityNode):

    pass
class UML2_ObjectNode(TypedElement, ActivityNode):

    pass
class PackageImport:

    pass
class UML2_ProfileApplication(PackageImport):

    pass
class Feature:

    pass
class UML2_StructuralFeature(TypedElement, Feature, MultiplicityElement):

    def __init__(self, isReadOnly: bool, UML2_StructuralFeature39: "UML2_Slot" = None, UML2_StructuralFeature: "UML2_StructuralFeatureAction" = None):
        self.isReadOnly = isReadOnly
        self.UML2_StructuralFeature39 = UML2_StructuralFeature39
        self.UML2_StructuralFeature = UML2_StructuralFeature
        
    @property
    def isReadOnly(self) -> bool:
        return self.__isReadOnly

    @isReadOnly.setter
    def isReadOnly(self, isReadOnly: bool):
        self.__isReadOnly = isReadOnly

    @property
    def UML2_StructuralFeature39(self):
        return self.__UML2_StructuralFeature39

    @UML2_StructuralFeature39.setter
    def UML2_StructuralFeature39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_StructuralFeature__UML2_StructuralFeature39", None)
        self.__UML2_StructuralFeature39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Slot38"):
                opp_val = getattr(old_value, "UML2_Slot38", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Slot38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Slot38"):
                opp_val = getattr(value, "UML2_Slot38", None)
                setattr(value, "UML2_Slot38", self)

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

class UML2_Connector(Feature):

    pass
class StructuredActivityNode:

    pass
class UML2_LoopNode(StructuredActivityNode):

    pass
class UML2_ExpansionRegion(StructuredActivityNode):

    pass
class UML2_ConditionalNode(StructuredActivityNode):

    pass
class TemplateableElement:

    pass
class UML2_StringExpression(TemplateableElement):

    pass
class UML2_Comment(TemplateableElement):

    pass
class UML2_NamedElement(TemplateableElement):

    def __init__(self, name: str, visibility: str, UML2_NamedElement: "UML2_Namespace" = None, UML2_NamedElement82: "UML2_Classifier" = None):
        self.name = name
        self.visibility = visibility
        self.UML2_NamedElement = UML2_NamedElement
        self.UML2_NamedElement82 = UML2_NamedElement82
        
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
    def UML2_NamedElement82(self):
        return self.__UML2_NamedElement82

    @UML2_NamedElement82.setter
    def UML2_NamedElement82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_NamedElement__UML2_NamedElement82", None)
        self.__UML2_NamedElement82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Classifier81"):
                opp_val = getattr(old_value, "UML2_Classifier81", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Classifier81"):
                opp_val = getattr(value, "UML2_Classifier81", None)
                if opp_val is None:
                    setattr(value, "UML2_Classifier81", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Element:

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

class UML2_ParameterableElement(Element):

    pass
class UML2_TemplateSignature(Element):

    pass
class UML2_QualifierValue(Element):

    pass
class UML2_ActivityGroup(Element):

    pass
class UML2_TemplateParameter(Element):

    pass
class UML2_Relationship(Element):

    pass
class UML2_ExceptionHandler(Element):

    pass
class UML2_TemplateableElement(Element):

    pass
class UML2_LinkEndData(Element):

    pass
class UML2_TemplateParameterSubstitution(Element):

    pass
class MessageTrigger:

    pass
class UML2_SignalTrigger(MessageTrigger):

    pass
class UML2_AnyTrigger(MessageTrigger):

    pass
class UML2_CallTrigger(MessageTrigger):

    pass
class Classifier:

    pass
class UML2_Actor(Classifier):

    pass
class UML2_Signal(Classifier):

    pass
class UML2_DataType(Classifier):

    pass
class UML2_TemplateableClassifier(Classifier):

    pass
class UML2_ParameterableClassifier(Classifier):

    pass
class UML2_InformationItem(Classifier):

    pass
class UML2_Interface(Classifier):

    pass
class UML2_BehavioredClassifier(Classifier):

    pass
class UML2_StructuredClassifier(Classifier):

    pass
class InvocationAction:

    pass
class UML2_SendSignalAction(InvocationAction):

    pass
class UML2_BroadcastSignalAction(InvocationAction):

    pass
class UML2_SendObjectAction(InvocationAction):

    pass
class UML2_CallAction(InvocationAction):

    pass
class UML2_Slot(Element):

    pass
class DeployedArtifact:

    pass
class UML2_Artifact(Classifier, DeployedArtifact):

    pass
class DeploymentTarget:

    pass
class UML2_Property(ConnectableElement, StructuralFeature, DeploymentTarget):

    def __init__(self, isComposite: bool, isDerived: bool, isDerivedUnion: bool, aggregation: str, UML2_Property: "UML2_QualifierValue" = None, UML2_Property27: "UML2_Association" = None, UML2_Property30: "UML2_Association" = None, UML2_Property43: "UML2_Property" = None, UML2_Property41: set["UML2_Property"] = None, UML2_Property45: "UML2_Association" = None, UML2_Property49: "UML2_Property" = None, UML2_Property47: set["UML2_Property"] = None, UML2_Property73: "UML2_LinkEndData" = None):
        self.isComposite = isComposite
        self.isDerived = isDerived
        self.isDerivedUnion = isDerivedUnion
        self.aggregation = aggregation
        self.UML2_Property = UML2_Property
        self.UML2_Property27 = UML2_Property27
        self.UML2_Property30 = UML2_Property30
        self.UML2_Property43 = UML2_Property43
        self.UML2_Property41 = UML2_Property41 if UML2_Property41 is not None else set()
        self.UML2_Property45 = UML2_Property45
        self.UML2_Property49 = UML2_Property49
        self.UML2_Property47 = UML2_Property47 if UML2_Property47 is not None else set()
        self.UML2_Property73 = UML2_Property73
        
    @property
    def aggregation(self) -> str:
        return self.__aggregation

    @aggregation.setter
    def aggregation(self, aggregation: str):
        self.__aggregation = aggregation

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
    def UML2_Property43(self):
        return self.__UML2_Property43

    @UML2_Property43.setter
    def UML2_Property43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property43", None)
        self.__UML2_Property43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Property41"):
                opp_val = getattr(old_value, "UML2_Property41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Property41"):
                opp_val = getattr(value, "UML2_Property41", None)
                if opp_val is None:
                    setattr(value, "UML2_Property41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Property27(self):
        return self.__UML2_Property27

    @UML2_Property27.setter
    def UML2_Property27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property27", None)
        self.__UML2_Property27 = value
        
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
        self.__UML2_Property73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_LinkEndData72"):
                opp_val = getattr(old_value, "UML2_LinkEndData72", None)
                if opp_val == self:
                    setattr(old_value, "UML2_LinkEndData72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_LinkEndData72"):
                opp_val = getattr(value, "UML2_LinkEndData72", None)
                setattr(value, "UML2_LinkEndData72", self)

    @property
    def UML2_Property47(self):
        return self.__UML2_Property47

    @UML2_Property47.setter
    def UML2_Property47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property47", None)
        self.__UML2_Property47 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Property49"):
                    opp_val = getattr(item, "UML2_Property49", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Property49", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Property49"):
                    opp_val = getattr(item, "UML2_Property49", None)
                    
                    setattr(item, "UML2_Property49", self)
                    

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
            if hasattr(old_value, "UML2_QualifierValue"):
                opp_val = getattr(old_value, "UML2_QualifierValue", None)
                if opp_val == self:
                    setattr(old_value, "UML2_QualifierValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_QualifierValue"):
                opp_val = getattr(value, "UML2_QualifierValue", None)
                setattr(value, "UML2_QualifierValue", self)

    @property
    def UML2_Property41(self):
        return self.__UML2_Property41

    @UML2_Property41.setter
    def UML2_Property41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property41", None)
        self.__UML2_Property41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Property43"):
                    opp_val = getattr(item, "UML2_Property43", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Property43", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Property43"):
                    opp_val = getattr(item, "UML2_Property43", None)
                    
                    setattr(item, "UML2_Property43", self)
                    

    @property
    def UML2_Property30(self):
        return self.__UML2_Property30

    @UML2_Property30.setter
    def UML2_Property30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property30", None)
        self.__UML2_Property30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Association29"):
                opp_val = getattr(old_value, "UML2_Association29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Association29"):
                opp_val = getattr(value, "UML2_Association29", None)
                if opp_val is None:
                    setattr(value, "UML2_Association29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "UML2_Property47"):
                opp_val = getattr(old_value, "UML2_Property47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Property47"):
                opp_val = getattr(value, "UML2_Property47", None)
                if opp_val is None:
                    setattr(value, "UML2_Property47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Property45(self):
        return self.__UML2_Property45

    @UML2_Property45.setter
    def UML2_Property45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property45", None)
        self.__UML2_Property45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Association46"):
                opp_val = getattr(old_value, "UML2_Association46", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Association46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Association46"):
                opp_val = getattr(value, "UML2_Association46", None)
                setattr(value, "UML2_Association46", self)

class PackageableElement:

    pass
class UML2_PrimitiveFunction(PackageableElement):

    pass
class UML2_Constraint(PackageableElement):

    pass
class UML2_Type(PackageableElement):

    pass
class UML2_GeneralizationSet(PackageableElement):

    pass
class UML2_InstanceSpecification(PackageableElement, DeployedArtifact, DeploymentTarget):

    pass
class WriteLinkAction:

    pass
class UML2_DestroyLinkAction(WriteLinkAction):

    pass
class UML2_CreateLinkAction(WriteLinkAction):

    pass
class NamedElement:

    pass
class UML2_DeploymentTarget(NamedElement):

    pass
class UML2_GeneralOrdering(NamedElement):

    pass
class UML2_InteractionFragment(NamedElement):

    pass
class UML2_MessageEnd(NamedElement):

    pass
class UML2_Namespace(NamedElement):

    pass
class UML2_Message(NamedElement):

    pass
class UML2_ParameterSet(NamedElement):

    pass
class UML2_CollaborationOccurrence(NamedElement):

    pass
class UML2_DeployedArtifact(NamedElement):

    pass
class UML2_Trigger(NamedElement):

    pass
class UML2_Vertex(NamedElement):

    pass
class UML2_RedefinableElement(NamedElement):

    pass
class UML2_ConnectableElement(NamedElement, ParameterableElement):

    pass
class UML2_Lifeline(NamedElement):

    pass
class UML2_TypedElement(NamedElement):

    pass
class LinkEndData:

    pass
class UML2_LinkEndCreationData(LinkEndData):

    pass
class UML2_OutputPin(Pin):

    pass
class Property:

    pass
class UML2_Port(Property):

    pass
class UML2_ExtensionEnd(Property):

    pass
class LiteralSpecification:

    pass
class UML2_LiteralNull(LiteralSpecification):

    pass
class UML2_LiteralInteger(LiteralSpecification):

    pass
class UML2_LiteralBoolean(LiteralSpecification):

    pass
class UML2_LiteralString(LiteralSpecification):

    pass
class Class:

    pass
class UML2_Behavior(Class):

    pass
class UML2_Stereotype(Class):

    pass
class UML2_Node(Class, DeploymentTarget):

    pass
class UML2_Component(Class):

    pass
class RedefinableElement:

    pass
class UML2_ExtensionPoint(RedefinableElement):

    pass
class UML2_Transition(RedefinableElement):

    pass
class UML2_Feature(RedefinableElement):

    def __init__(self, isStatic: bool, UML2_Feature: set["UML2_Classifier"] = None, UML2_Feature79: "UML2_Classifier" = None):
        self.isStatic = isStatic
        self.UML2_Feature = UML2_Feature if UML2_Feature is not None else set()
        self.UML2_Feature79 = UML2_Feature79
        
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
                if hasattr(item, "UML2_Classifier68"):
                    opp_val = getattr(item, "UML2_Classifier68", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Classifier68", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Classifier68"):
                    opp_val = getattr(item, "UML2_Classifier68", None)
                    
                    setattr(item, "UML2_Classifier68", self)
                    

    @property
    def UML2_Feature79(self):
        return self.__UML2_Feature79

    @UML2_Feature79.setter
    def UML2_Feature79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Feature__UML2_Feature79", None)
        self.__UML2_Feature79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Classifier78"):
                opp_val = getattr(old_value, "UML2_Classifier78", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Classifier78"):
                opp_val = getattr(value, "UML2_Classifier78", None)
                if opp_val is None:
                    setattr(value, "UML2_Classifier78", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UML2_RedefinableTemplateSignature(RedefinableElement, TemplateSignature):

    pass
class UML2_ActivityEdge(RedefinableElement):

    pass
class Relationship:

    pass
class UML2_Association(Relationship, Classifier):

    pass
class UML2_DirectedRelationship(Relationship):

    pass
class ValueSpecification:

    pass
class UML2_LiteralSpecification(ValueSpecification):

    pass
class UML2_Duration(ValueSpecification):

    pass
class UML2_OpaqueExpression(ValueSpecification):

    def __init__(self, bodies: str, language: str, UML2_OpaqueExpression: "UML2_Behavior" = None):
        self.bodies = bodies
        self.language = language
        self.UML2_OpaqueExpression = UML2_OpaqueExpression
        
    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def bodies(self) -> str:
        return self.__bodies

    @bodies.setter
    def bodies(self, bodies: str):
        self.__bodies = bodies

    @property
    def UML2_OpaqueExpression(self):
        return self.__UML2_OpaqueExpression

    @UML2_OpaqueExpression.setter
    def UML2_OpaqueExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_OpaqueExpression__UML2_OpaqueExpression", None)
        self.__UML2_OpaqueExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Behavior59"):
                opp_val = getattr(old_value, "UML2_Behavior59", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Behavior59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Behavior59"):
                opp_val = getattr(value, "UML2_Behavior59", None)
                setattr(value, "UML2_Behavior59", self)

class UML2_Interval(ValueSpecification):

    pass
class UML2_InstanceValue(ValueSpecification):

    pass
class UML2_TimeExpression(ValueSpecification):

    pass
class InteractionFragment:

    pass
class UML2_EventOccurrence(MessageEnd, InteractionFragment):

    pass
class UML2_Continuation(InteractionFragment):

    pass
class UML2_ExecutionOccurrence(InteractionFragment):

    pass
class UML2_InteractionOccurrence(InteractionFragment):

    pass
class UML2_CombinedFragment(InteractionFragment):

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
class Dependency:

    pass
class UML2_Permission(Dependency):

    pass
class UML2_Usage(Dependency):

    pass
class UML2_Abstraction(Dependency):

    pass
class UML2_Element:

    pass
class AcceptEventAction:

    pass
class UML2_AcceptCallAction(AcceptEventAction):

    pass
class Association:

    pass
class UML2_Extension(Association):

    pass
class UML2_AssociationClass(Association, Class):

    pass
class UML2_CommunicationPath(Association):

    pass
class Constraint:

    pass
class UML2_IntervalConstraint(Constraint):

    pass
class UML2_InteractionConstraint(Constraint):

    pass
class UML2_LiteralUnlimitedNatural(LiteralSpecification):

    pass
class UML2_PackageableElement(NamedElement, ParameterableElement):

    pass
class DirectedRelationship:

    pass
class UML2_TemplateBinding(DirectedRelationship):

    pass
class UML2_ProtocolConformance(DirectedRelationship):

    pass
class UML2_Extend(NamedElement, DirectedRelationship):

    pass
class UML2_Include(NamedElement, DirectedRelationship):

    pass
class UML2_InformationFlow(PackageableElement, DirectedRelationship):

    pass
class UML2_Generalization(DirectedRelationship):

    pass
class UML2_PackageMerge(DirectedRelationship):

    pass
class UML2_Dependency(PackageableElement, DirectedRelationship):

    pass
class UML2_PackageImport(DirectedRelationship):

    def __init__(self, visibility: str):
        self.visibility = visibility
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

class UML2_ElementImport(DirectedRelationship):

    def __init__(self, visibility: str, UML2_ElementImport: "UML2_PackageableElement" = None):
        self.visibility = visibility
        self.UML2_ElementImport = UML2_ElementImport
        
    @property
    def visibility(self) -> str:
        return self.__visibility

    @visibility.setter
    def visibility(self, visibility: str):
        self.__visibility = visibility

    @property
    def UML2_ElementImport(self):
        return self.__UML2_ElementImport

    @UML2_ElementImport.setter
    def UML2_ElementImport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_ElementImport__UML2_ElementImport", None)
        self.__UML2_ElementImport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_PackageableElement"):
                opp_val = getattr(old_value, "UML2_PackageableElement", None)
                if opp_val == self:
                    setattr(old_value, "UML2_PackageableElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_PackageableElement"):
                opp_val = getattr(value, "UML2_PackageableElement", None)
                setattr(value, "UML2_PackageableElement", self)

class UML2_Deployment(Dependency):

    pass
class IntervalConstraint:

    pass
class UML2_DurationConstraint(IntervalConstraint):

    pass
class UML2_TimeConstraint(IntervalConstraint):

    pass
class UML2_ActivityNode(RedefinableElement):

    pass
class ActivityGroup:

    pass
class UML2_InterruptibleActivityRegion(ActivityGroup):

    pass
class UML2_ActivityPartition(NamedElement, ActivityGroup):

    pass
class Namespace:

    pass
class UML2_Package(PackageableElement, Namespace):

    pass
class UML2_BehavioralFeature(Feature, Namespace):

    pass
class UML2_Classifier(Type, RedefinableElement, Namespace):

    def __init__(self, isAbstract: bool, UML2_Classifier: "UML2_CreateObjectAction" = None, UML2_Classifier9: "UML2_InstanceSpecification" = None, UML2_Classifier18: "UML2_Action" = None, UML2_Classifier16: "UML2_Generalization" = None, UML2_Classifier20: "UML2_Class" = None, UML2_Classifier68: "UML2_Feature" = None, UML2_Classifier78: set["UML2_Feature"] = None, UML2_Classifier81: set["UML2_NamedElement"] = None, UML2_Classifier84: set["UML2_Generalization"] = None):
        self.isAbstract = isAbstract
        self.UML2_Classifier = UML2_Classifier
        self.UML2_Classifier9 = UML2_Classifier9
        self.UML2_Classifier18 = UML2_Classifier18
        self.UML2_Classifier16 = UML2_Classifier16
        self.UML2_Classifier20 = UML2_Classifier20
        self.UML2_Classifier68 = UML2_Classifier68
        self.UML2_Classifier78 = UML2_Classifier78 if UML2_Classifier78 is not None else set()
        self.UML2_Classifier81 = UML2_Classifier81 if UML2_Classifier81 is not None else set()
        self.UML2_Classifier84 = UML2_Classifier84 if UML2_Classifier84 is not None else set()
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def UML2_Classifier20(self):
        return self.__UML2_Classifier20

    @UML2_Classifier20.setter
    def UML2_Classifier20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier20", None)
        self.__UML2_Classifier20 = value
        
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
    def UML2_Classifier81(self):
        return self.__UML2_Classifier81

    @UML2_Classifier81.setter
    def UML2_Classifier81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier81", None)
        self.__UML2_Classifier81 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_NamedElement82"):
                    opp_val = getattr(item, "UML2_NamedElement82", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_NamedElement82", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_NamedElement82"):
                    opp_val = getattr(item, "UML2_NamedElement82", None)
                    
                    setattr(item, "UML2_NamedElement82", self)
                    

    @property
    def UML2_Classifier84(self):
        return self.__UML2_Classifier84

    @UML2_Classifier84.setter
    def UML2_Classifier84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier84", None)
        self.__UML2_Classifier84 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Generalization85"):
                    opp_val = getattr(item, "UML2_Generalization85", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Generalization85", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Generalization85"):
                    opp_val = getattr(item, "UML2_Generalization85", None)
                    
                    setattr(item, "UML2_Generalization85", self)
                    

    @property
    def UML2_Classifier68(self):
        return self.__UML2_Classifier68

    @UML2_Classifier68.setter
    def UML2_Classifier68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier68", None)
        self.__UML2_Classifier68 = value
        
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
    def UML2_Classifier(self):
        return self.__UML2_Classifier

    @UML2_Classifier.setter
    def UML2_Classifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier", None)
        self.__UML2_Classifier = value
        
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
    def UML2_Classifier9(self):
        return self.__UML2_Classifier9

    @UML2_Classifier9.setter
    def UML2_Classifier9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier9", None)
        self.__UML2_Classifier9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_InstanceSpecification8"):
                opp_val = getattr(old_value, "UML2_InstanceSpecification8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_InstanceSpecification8"):
                opp_val = getattr(value, "UML2_InstanceSpecification8", None)
                if opp_val is None:
                    setattr(value, "UML2_InstanceSpecification8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Classifier16(self):
        return self.__UML2_Classifier16

    @UML2_Classifier16.setter
    def UML2_Classifier16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier16", None)
        self.__UML2_Classifier16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Generalization"):
                opp_val = getattr(old_value, "UML2_Generalization", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Generalization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Generalization"):
                opp_val = getattr(value, "UML2_Generalization", None)
                setattr(value, "UML2_Generalization", self)

    @property
    def UML2_Classifier18(self):
        return self.__UML2_Classifier18

    @UML2_Classifier18.setter
    def UML2_Classifier18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier18", None)
        self.__UML2_Classifier18 = value
        
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
    def UML2_Classifier78(self):
        return self.__UML2_Classifier78

    @UML2_Classifier78.setter
    def UML2_Classifier78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier78", None)
        self.__UML2_Classifier78 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Feature79"):
                    opp_val = getattr(item, "UML2_Feature79", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Feature79", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Feature79"):
                    opp_val = getattr(item, "UML2_Feature79", None)
                    
                    setattr(item, "UML2_Feature79", self)
                    

class UML2_Region(RedefinableElement, Namespace):

    pass
class UML2_State(Vertex, RedefinableElement, Namespace):

    pass
class UML2_InteractionOperand(InteractionFragment, Namespace):

    pass
class Action:

    pass
class UML2_ReclassifyObjectAction(Action):

    pass
class UML2_ReadLinkObjectEndAction(Action):

    pass
class UML2_ReadSelfAction(Action):

    pass
class UML2_StructuredActivityNode(Action, ActivityGroup, Namespace):

    pass
class UML2_ReadExtentAction(Action):

    pass
class UML2_ReplyAction(Action):

    pass
class UML2_ReadLinkObjectEndQualifierAction(Action):

    pass
class UML2_CreateObjectAction(Action):

    pass
class UML2_ApplyFunctionAction(Action):

    pass
class UML2_StructuralFeatureAction(Action):

    pass
class UML2_ReadIsClassifiedObjectAction(Action):

    pass
class UML2_ClearAssociationAction(Action):

    pass
class UML2_DestroyObjectAction(Action):

    pass
class UML2_InvocationAction(Action):

    pass
class UML2_RaiseExceptionAction(Action):

    pass
class UML2_LinkAction(Action):

    pass
class UML2_TestIdentityAction(Action):

    pass
class UML2_VariableAction(Action):

    pass
class UML2_AcceptEventAction(Action):

    pass
class UML2_StartOwnedBehaviorAction(Action):

    pass