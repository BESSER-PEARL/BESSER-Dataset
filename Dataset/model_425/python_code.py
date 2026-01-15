from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class VisibilityKind(Enum):
    protected = "protected"
    public = "public"
    package = "package"
    private = "private"
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

class CreateLinkAction:

    pass
class UML2_CreateLinkObjectAction(CreateLinkAction):

    pass
class ExecutableNode:

    pass
class UML2_Action(ExecutableNode):

    pass
class EncapsulatedClassifier:

    pass
class StateMachine:

    pass
class UML2_ProtocolStateMachine(StateMachine):

    pass
class Type:

    pass
class InteractionOccurrence:

    pass
class UML2_PartDecomposition(InteractionOccurrence):

    pass
class CentralBufferNode:

    pass
class UML2_DataStoreNode(CentralBufferNode):

    pass
class OpaqueExpression:

    pass
class UML2_Expression(OpaqueExpression):

    pass
class Constraint:

    pass
class UML2_InteractionConstraint(Constraint):

    pass
class UML2_IntervalConstraint(Constraint):

    pass
class Behavior:

    pass
class UML2_Activity(Behavior):

    pass
class UML2_StateMachine(Behavior):

    pass
class AcceptEventAction:

    pass
class UML2_AcceptCallAction(AcceptEventAction):

    pass
class UML2_Element:

    pass
class InstanceSpecification:

    pass
class UML2_EnumerationLiteral(InstanceSpecification):

    pass
class Interval:

    pass
class UML2_TimeInterval(Interval):

    pass
class UML2_DurationInterval(Interval):

    pass
class DeployedArtifact:

    pass
class LinkEndData:

    pass
class UML2_LinkEndCreationData(LinkEndData):

    pass
class DataType:

    pass
class UML2_Enumeration(DataType):

    pass
class UML2_PrimitiveType(DataType):

    pass
class PackageImport:

    pass
class UML2_ProfileApplication(PackageImport):

    pass
class State:

    pass
class UML2_FinalState(State):

    pass
class Transition:

    pass
class UML2_ProtocolTransition(Transition):

    pass
class WriteLinkAction:

    pass
class UML2_DestroyLinkAction(WriteLinkAction):

    pass
class UML2_CreateLinkAction(WriteLinkAction):

    pass
class Pin:

    pass
class UML2_OutputPin(Pin):

    pass
class Property:

    pass
class UML2_ExtensionEnd(Property):

    pass
class UML2_Port(Property):

    pass
class Realization:

    pass
class UML2_Substitution(Realization):

    pass
class UML2_Implementation(Realization):

    pass
class Dependency:

    pass
class UML2_Permission(Dependency):

    pass
class UML2_Deployment(Dependency):

    pass
class UML2_Usage(Dependency):

    pass
class UML2_Abstraction(Dependency):

    pass
class LiteralSpecification:

    pass
class UML2_LiteralInteger(LiteralSpecification):

    pass
class UML2_LiteralString(LiteralSpecification):

    pass
class UML2_LiteralNull(LiteralSpecification):

    pass
class UML2_LiteralBoolean(LiteralSpecification):

    pass
class UML2_LiteralUnlimitedNatural(LiteralSpecification):

    pass
class TemplateSignature:

    pass
class InvocationAction:

    pass
class UML2_SendObjectAction(InvocationAction):

    pass
class UML2_BroadcastSignalAction(InvocationAction):

    pass
class UML2_CallAction(InvocationAction):

    pass
class IntervalConstraint:

    pass
class UML2_TimeConstraint(IntervalConstraint):

    pass
class UML2_DurationConstraint(IntervalConstraint):

    pass
class WriteVariableAction:

    pass
class UML2_RemoveVariableValueAction(WriteVariableAction):

    pass
class UML2_AddVariableValueAction(WriteVariableAction):

    pass
class LinkAction:

    pass
class UML2_ReadLinkAction(LinkAction):

    pass
class UML2_WriteLinkAction(LinkAction):

    pass
class Node:

    pass
class UML2_Device(Node):

    pass
class UML2_ExecutionEnvironment(Node):

    pass
class UML2_SendSignalAction(InvocationAction):

    pass
class Relationship:

    pass
class UML2_DirectedRelationship(Relationship):

    pass
class TemplateParameter:

    pass
class UML2_OperationTemplateParameter(TemplateParameter):

    pass
class UML2_ConnectableElementTemplateParameter(TemplateParameter):

    pass
class UML2_ClassifierTemplateParameter(TemplateParameter):

    pass
class UML2_InputPin(Pin):

    pass
class StructuredClassifier:

    pass
class UML2_EncapsulatedClassifier(StructuredClassifier):

    pass
class Class:

    pass
class UML2_Component(Class):

    pass
class UML2_Stereotype(Class):

    pass
class Association:

    pass
class UML2_CommunicationPath(Association):

    pass
class UML2_AssociationClass(Association, Class):

    pass
class UML2_Extension(Association):

    pass
class StructuralFeatureAction:

    pass
class UML2_WriteStructuralFeatureAction(StructuralFeatureAction):

    pass
class UML2_ClearStructuralFeatureAction(StructuralFeatureAction):

    pass
class UML2_ReadStructuralFeatureAction(StructuralFeatureAction):

    pass
class Feature:

    pass
class UML2_Connector(Feature):

    pass
class Abstraction:

    pass
class UML2_Manifestation(Abstraction):

    pass
class UML2_Realization(Abstraction):

    pass
class MessageEnd:

    pass
class UML2_Gate(MessageEnd):

    pass
class UML2_Behavior(Class):

    pass
class BehavioralFeature:

    pass
class UML2_Reception(BehavioralFeature):

    pass
class Action:

    pass
class UML2_LinkAction(Action):

    pass
class UML2_ReadLinkObjectEndAction(Action):

    pass
class UML2_DestroyObjectAction(Action):

    pass
class UML2_StructuralFeatureAction(Action):

    pass
class UML2_ReplyAction(Action):

    pass
class UML2_CreateObjectAction(Action):

    pass
class UML2_InvocationAction(Action):

    pass
class UML2_ReadIsClassifiedObjectAction(Action):

    pass
class UML2_AcceptEventAction(Action):

    pass
class UML2_ApplyFunctionAction(Action):

    pass
class UML2_ReadExtentAction(Action):

    pass
class UML2_ClearAssociationAction(Action):

    pass
class UML2_VariableAction(Action):

    pass
class UML2_ReadSelfAction(Action):

    pass
class UML2_TestIdentityAction(Action):

    pass
class UML2_ReadLinkObjectEndQualifierAction(Action):

    pass
class UML2_RaiseExceptionAction(Action):

    pass
class UML2_StartOwnedBehaviorAction(Action):

    pass
class UML2_ReclassifyObjectAction(Action):

    pass
class Trigger:

    pass
class UML2_ChangeTrigger(Trigger):

    pass
class UML2_TimeTrigger(Trigger):

    pass
class UML2_MessageTrigger(Trigger):

    pass
class VariableAction:

    pass
class UML2_ReadVariableAction(VariableAction):

    pass
class UML2_ClearVariableAction(VariableAction):

    pass
class UML2_WriteVariableAction(VariableAction):

    pass
class ValueSpecification:

    pass
class UML2_TimeExpression(ValueSpecification):

    pass
class UML2_Interval(ValueSpecification):

    pass
class UML2_InstanceValue(ValueSpecification):

    pass
class UML2_OpaqueExpression(ValueSpecification):

    def __init__(self, bodies: str, language: str, UML2_OpaqueExpression: "UML2_Behavior" = None):
        self.bodies = bodies
        self.language = language
        self.UML2_OpaqueExpression = UML2_OpaqueExpression
        
    @property
    def bodies(self) -> str:
        return self.__bodies

    @bodies.setter
    def bodies(self, bodies: str):
        self.__bodies = bodies

    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

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
            if hasattr(old_value, "UML2_Behavior43"):
                opp_val = getattr(old_value, "UML2_Behavior43", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Behavior43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Behavior43"):
                opp_val = getattr(value, "UML2_Behavior43", None)
                setattr(value, "UML2_Behavior43", self)

class UML2_LiteralSpecification(ValueSpecification):

    pass
class UML2_Duration(ValueSpecification):

    pass
class Package:

    pass
class UML2_Model(Package):

    pass
class UML2_Profile(Package):

    pass
class ObjectNode:

    pass
class UML2_CentralBufferNode(ObjectNode):

    pass
class UML2_ActivityParameterNode(ObjectNode):

    pass
class UML2_ExpansionNode(ObjectNode):

    pass
class TemplateableElement:

    pass
class UML2_Comment(TemplateableElement):

    pass
class UML2_StringExpression(TemplateableElement):

    pass
class UML2_NamedElement(TemplateableElement):

    def __init__(self, name: str, visibility: str, UML2_NamedElement: "UML2_Namespace" = None, UML2_NamedElement73: "UML2_Classifier" = None):
        self.name = name
        self.visibility = visibility
        self.UML2_NamedElement = UML2_NamedElement
        self.UML2_NamedElement73 = UML2_NamedElement73
        
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
    def UML2_NamedElement73(self):
        return self.__UML2_NamedElement73

    @UML2_NamedElement73.setter
    def UML2_NamedElement73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_NamedElement__UML2_NamedElement73", None)
        self.__UML2_NamedElement73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Classifier72"):
                opp_val = getattr(old_value, "UML2_Classifier72", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Classifier72"):
                opp_val = getattr(value, "UML2_Classifier72", None)
                if opp_val is None:
                    setattr(value, "UML2_Classifier72", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ActivityGroup:

    pass
class UML2_InterruptibleActivityRegion(ActivityGroup):

    pass
class ParameterableElement:

    pass
class Artifact:

    pass
class UML2_DeploymentSpecification(Artifact):

    pass
class ControlNode:

    pass
class UML2_DecisionNode(ControlNode):

    pass
class UML2_JoinNode(ControlNode):

    pass
class UML2_ForkNode(ControlNode):

    pass
class UML2_MergeNode(ControlNode):

    pass
class UML2_InitialNode(ControlNode):

    pass
class UML2_FinalNode(ControlNode):

    pass
class Element:

    pass
class UML2_Relationship(Element):

    pass
class UML2_Clause(Element):

    pass
class UML2_ParameterableElement(Element):

    pass
class UML2_TemplateParameter(Element):

    pass
class UML2_Slot(Element):

    pass
class UML2_TemplateableElement(Element):

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

class UML2_TemplateParameterSubstitution(Element):

    pass
class UML2_ActivityGroup(Element):

    pass
class UML2_LinkEndData(Element):

    pass
class UML2_QualifierValue(Element):

    pass
class UML2_ExceptionHandler(Element):

    pass
class UML2_TemplateSignature(Element):

    pass
class FinalNode:

    pass
class UML2_ActivityFinalNode(FinalNode):

    pass
class UML2_FlowFinalNode(FinalNode):

    pass
class DeploymentTarget:

    pass
class UML2_Node(DeploymentTarget, Class):

    pass
class StructuralFeature:

    pass
class Classifier:

    pass
class UML2_Interface(Classifier):

    pass
class UML2_StructuredClassifier(Classifier):

    pass
class UML2_Association(Classifier, Relationship):

    pass
class UML2_Signal(Classifier):

    pass
class UML2_TemplateableClassifier(Classifier):

    pass
class UML2_Actor(Classifier):

    pass
class UML2_Artifact(Classifier, DeployedArtifact):

    pass
class UML2_DataType(Classifier):

    pass
class UML2_InformationItem(Classifier):

    pass
class UML2_BehavioredClassifier(Classifier):

    pass
class UML2_ParameterableClassifier(Classifier):

    pass
class MessageTrigger:

    pass
class UML2_CallTrigger(MessageTrigger):

    pass
class UML2_SignalTrigger(MessageTrigger):

    pass
class UML2_AnyTrigger(MessageTrigger):

    pass
class MultiplicityElement:

    pass
class UML2_Pin(MultiplicityElement, ObjectNode):

    pass
class UML2_ConnectorEnd(MultiplicityElement):

    pass
class TypedElement:

    pass
class UML2_ValueSpecification(TypedElement, ParameterableElement):

    pass
class UML2_StructuralFeature(MultiplicityElement, TypedElement, Feature):

    def __init__(self, isReadOnly: bool, UML2_StructuralFeature: "UML2_Slot" = None, UML2_StructuralFeature85: "UML2_StructuralFeatureAction" = None):
        self.isReadOnly = isReadOnly
        self.UML2_StructuralFeature = UML2_StructuralFeature
        self.UML2_StructuralFeature85 = UML2_StructuralFeature85
        
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
            if hasattr(old_value, "UML2_Slot49"):
                opp_val = getattr(old_value, "UML2_Slot49", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Slot49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Slot49"):
                opp_val = getattr(value, "UML2_Slot49", None)
                setattr(value, "UML2_Slot49", self)

    @property
    def UML2_StructuralFeature85(self):
        return self.__UML2_StructuralFeature85

    @UML2_StructuralFeature85.setter
    def UML2_StructuralFeature85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_StructuralFeature__UML2_StructuralFeature85", None)
        self.__UML2_StructuralFeature85 = value
        
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

class UML2_Operation(MultiplicityElement, TypedElement, BehavioralFeature, ParameterableElement):

    def __init__(self, isQuery: bool, UML2_Operation: set["UML2_Parameter"] = None, UML2_Operation33: "UML2_Constraint" = None):
        self.isQuery = isQuery
        self.UML2_Operation = UML2_Operation if UML2_Operation is not None else set()
        self.UML2_Operation33 = UML2_Operation33
        
    @property
    def isQuery(self) -> bool:
        return self.__isQuery

    @isQuery.setter
    def isQuery(self, isQuery: bool):
        self.__isQuery = isQuery

    @property
    def UML2_Operation33(self):
        return self.__UML2_Operation33

    @UML2_Operation33.setter
    def UML2_Operation33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Operation__UML2_Operation33", None)
        self.__UML2_Operation33 = value
        
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
                    

class ConnectableElement:

    pass
class UML2_Variable(MultiplicityElement, TypedElement, ConnectableElement):

    pass
class UML2_Property(DeploymentTarget, ConnectableElement, StructuralFeature):

    def __init__(self, isComposite: bool, isDerivedUnion: bool, aggregation: str, isDerived: bool, UML2_Property: "UML2_Property" = None, UML2_Property1: set["UML2_Property"] = None, UML2_Property4: "UML2_Association" = None, UML2_Property7: "UML2_Property" = None, UML2_Property5: set["UML2_Property"] = None, UML2_Property13: "UML2_QualifierValue" = None, UML2_Property22: "UML2_LinkEndData" = None, UML2_Property41: "UML2_Association" = None, UML2_Property38: "UML2_Association" = None):
        self.isComposite = isComposite
        self.isDerivedUnion = isDerivedUnion
        self.aggregation = aggregation
        self.isDerived = isDerived
        self.UML2_Property = UML2_Property
        self.UML2_Property1 = UML2_Property1 if UML2_Property1 is not None else set()
        self.UML2_Property4 = UML2_Property4
        self.UML2_Property7 = UML2_Property7
        self.UML2_Property5 = UML2_Property5 if UML2_Property5 is not None else set()
        self.UML2_Property13 = UML2_Property13
        self.UML2_Property22 = UML2_Property22
        self.UML2_Property41 = UML2_Property41
        self.UML2_Property38 = UML2_Property38
        
    @property
    def isDerived(self) -> bool:
        return self.__isDerived

    @isDerived.setter
    def isDerived(self, isDerived: bool):
        self.__isDerived = isDerived

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
    def aggregation(self) -> str:
        return self.__aggregation

    @aggregation.setter
    def aggregation(self, aggregation: str):
        self.__aggregation = aggregation

    @property
    def UML2_Property5(self):
        return self.__UML2_Property5

    @UML2_Property5.setter
    def UML2_Property5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property5", None)
        self.__UML2_Property5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Property7"):
                    opp_val = getattr(item, "UML2_Property7", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Property7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Property7"):
                    opp_val = getattr(item, "UML2_Property7", None)
                    
                    setattr(item, "UML2_Property7", self)
                    

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
            if hasattr(old_value, "UML2_Association40"):
                opp_val = getattr(old_value, "UML2_Association40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Association40"):
                opp_val = getattr(value, "UML2_Association40", None)
                if opp_val is None:
                    setattr(value, "UML2_Association40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Property22(self):
        return self.__UML2_Property22

    @UML2_Property22.setter
    def UML2_Property22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property22", None)
        self.__UML2_Property22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_LinkEndData21"):
                opp_val = getattr(old_value, "UML2_LinkEndData21", None)
                if opp_val == self:
                    setattr(old_value, "UML2_LinkEndData21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_LinkEndData21"):
                opp_val = getattr(value, "UML2_LinkEndData21", None)
                setattr(value, "UML2_LinkEndData21", self)

    @property
    def UML2_Property38(self):
        return self.__UML2_Property38

    @UML2_Property38.setter
    def UML2_Property38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property38", None)
        self.__UML2_Property38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Association37"):
                opp_val = getattr(old_value, "UML2_Association37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Association37"):
                opp_val = getattr(value, "UML2_Association37", None)
                if opp_val is None:
                    setattr(value, "UML2_Association37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Property13(self):
        return self.__UML2_Property13

    @UML2_Property13.setter
    def UML2_Property13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property13", None)
        self.__UML2_Property13 = value
        
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
    def UML2_Property(self):
        return self.__UML2_Property

    @UML2_Property.setter
    def UML2_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property", None)
        self.__UML2_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Property1"):
                opp_val = getattr(old_value, "UML2_Property1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Property1"):
                opp_val = getattr(value, "UML2_Property1", None)
                if opp_val is None:
                    setattr(value, "UML2_Property1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Property1(self):
        return self.__UML2_Property1

    @UML2_Property1.setter
    def UML2_Property1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property1", None)
        self.__UML2_Property1 = value if value is not None else set()
        
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
    def UML2_Property7(self):
        return self.__UML2_Property7

    @UML2_Property7.setter
    def UML2_Property7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property7", None)
        self.__UML2_Property7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Property5"):
                opp_val = getattr(old_value, "UML2_Property5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Property5"):
                opp_val = getattr(value, "UML2_Property5", None)
                if opp_val is None:
                    setattr(value, "UML2_Property5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Property4(self):
        return self.__UML2_Property4

    @UML2_Property4.setter
    def UML2_Property4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Property__UML2_Property4", None)
        self.__UML2_Property4 = value
        
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

class UML2_Parameter(MultiplicityElement, TypedElement, ConnectableElement):

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

class DirectedRelationship:

    pass
class UML2_PackageMerge(DirectedRelationship):

    pass
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

class UML2_ProtocolConformance(DirectedRelationship):

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

class UML2_TemplateBinding(DirectedRelationship):

    pass
class WriteStructuralFeatureAction:

    pass
class UML2_RemoveStructuralFeatureValueAction(WriteStructuralFeatureAction):

    pass
class UML2_DurationObservationAction(WriteStructuralFeatureAction):

    pass
class UML2_TimeObservationAction(WriteStructuralFeatureAction):

    pass
class UML2_AddStructuralFeatureValueAction(WriteStructuralFeatureAction):

    pass
class InputPin:

    pass
class UML2_ValuePin(InputPin):

    pass
class StructuredActivityNode:

    pass
class UML2_LoopNode(StructuredActivityNode):

    pass
class UML2_ExpansionRegion(StructuredActivityNode):

    pass
class UML2_ConditionalNode(StructuredActivityNode):

    pass
class NamedElement:

    pass
class UML2_Include(DirectedRelationship, NamedElement):

    pass
class UML2_ParameterSet(NamedElement):

    pass
class UML2_Message(NamedElement):

    pass
class UML2_CollaborationOccurrence(NamedElement):

    pass
class UML2_Trigger(NamedElement):

    pass
class UML2_TypedElement(NamedElement):

    pass
class UML2_Extend(NamedElement, DirectedRelationship):

    pass
class UML2_Namespace(NamedElement):

    pass
class UML2_RedefinableElement(NamedElement):

    pass
class UML2_ConnectableElement(NamedElement, ParameterableElement):

    pass
class UML2_GeneralOrdering(NamedElement):

    pass
class UML2_Lifeline(NamedElement):

    pass
class UML2_DeployedArtifact(NamedElement):

    pass
class UML2_DeploymentTarget(NamedElement):

    pass
class UML2_MessageEnd(NamedElement):

    pass
class UML2_Vertex(NamedElement):

    pass
class UML2_ActivityPartition(NamedElement, ActivityGroup):

    pass
class UML2_PackageableElement(NamedElement, ParameterableElement):

    pass
class UML2_InteractionFragment(NamedElement):

    pass
class UML2_Generalization(DirectedRelationship):

    pass
class PackageableElement:

    pass
class UML2_Constraint(PackageableElement):

    pass
class UML2_Type(PackageableElement):

    pass
class UML2_PrimitiveFunction(PackageableElement):

    pass
class UML2_Dependency(PackageableElement, DirectedRelationship):

    pass
class UML2_InformationFlow(PackageableElement, DirectedRelationship):

    pass
class UML2_InstanceSpecification(DeploymentTarget, PackageableElement, DeployedArtifact):

    pass
class UML2_GeneralizationSet(PackageableElement):

    pass
class ActivityEdge:

    pass
class UML2_ControlFlow(ActivityEdge):

    pass
class UML2_ObjectFlow(ActivityEdge):

    pass
class CallAction:

    pass
class UML2_CallOperationAction(CallAction):

    pass
class UML2_CallBehaviorAction(CallAction):

    pass
class ActivityNode:

    pass
class UML2_ExecutableNode(ActivityNode):

    pass
class UML2_ObjectNode(TypedElement, ActivityNode):

    pass
class UML2_ControlNode(ActivityNode):

    pass
class BehavioredClassifier:

    pass
class UML2_Collaboration(BehavioredClassifier, StructuredClassifier):

    pass
class UML2_Class(EncapsulatedClassifier, BehavioredClassifier):

    def __init__(self, isActive: bool, UML2_Class: set["UML2_Classifier"] = None, UML2_Class80: set["UML2_Reception"] = None):
        self.isActive = isActive
        self.UML2_Class = UML2_Class if UML2_Class is not None else set()
        self.UML2_Class80 = UML2_Class80 if UML2_Class80 is not None else set()
        
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
                if hasattr(item, "UML2_Classifier78"):
                    opp_val = getattr(item, "UML2_Classifier78", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Classifier78", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Classifier78"):
                    opp_val = getattr(item, "UML2_Classifier78", None)
                    
                    setattr(item, "UML2_Classifier78", self)
                    

    @property
    def UML2_Class80(self):
        return self.__UML2_Class80

    @UML2_Class80.setter
    def UML2_Class80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Class__UML2_Class80", None)
        self.__UML2_Class80 = value if value is not None else set()
        
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
class InteractionFragment:

    pass
class UML2_InteractionOccurrence(InteractionFragment):

    pass
class UML2_Continuation(InteractionFragment):

    pass
class UML2_CombinedFragment(InteractionFragment):

    pass
class UML2_EventOccurrence(MessageEnd, InteractionFragment):

    pass
class UML2_Interaction(InteractionFragment, Behavior):

    pass
class UML2_StateInvariant(InteractionFragment):

    pass
class UML2_ExecutionOccurrence(InteractionFragment):

    pass
class EventOccurrence:

    pass
class UML2_Stop(EventOccurrence):

    pass
class Vertex:

    pass
class UML2_Pseudostate(Vertex):

    pass
class UML2_ConnectionPointReference(Vertex):

    pass
class RedefinableElement:

    pass
class UML2_ActivityEdge(RedefinableElement):

    pass
class UML2_ExtensionPoint(RedefinableElement):

    pass
class UML2_Feature(RedefinableElement):

    def __init__(self, isStatic: bool, UML2_Feature: set["UML2_Classifier"] = None, UML2_Feature70: "UML2_Classifier" = None):
        self.isStatic = isStatic
        self.UML2_Feature = UML2_Feature if UML2_Feature is not None else set()
        self.UML2_Feature70 = UML2_Feature70
        
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
    def UML2_Feature70(self):
        return self.__UML2_Feature70

    @UML2_Feature70.setter
    def UML2_Feature70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Feature__UML2_Feature70", None)
        self.__UML2_Feature70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_Classifier69"):
                opp_val = getattr(old_value, "UML2_Classifier69", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Classifier69"):
                opp_val = getattr(value, "UML2_Classifier69", None)
                if opp_val is None:
                    setattr(value, "UML2_Classifier69", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UML2_RedefinableTemplateSignature(RedefinableElement, TemplateSignature):

    pass
class UML2_Transition(RedefinableElement):

    pass
class UML2_ActivityNode(RedefinableElement):

    pass
class Namespace:

    pass
class UML2_InteractionOperand(InteractionFragment, Namespace):

    pass
class UML2_StructuredActivityNode(Action, Namespace, ActivityGroup):

    pass
class UML2_Package(PackageableElement, Namespace):

    pass
class UML2_BehavioralFeature(Feature, Namespace):

    pass
class UML2_Classifier(Type, Namespace, RedefinableElement):

    def __init__(self, isAbstract: bool, UML2_Classifier: "UML2_Generalization" = None, UML2_Classifier47: "UML2_InstanceSpecification" = None, UML2_Classifier58: "UML2_CreateObjectAction" = None, UML2_Classifier66: "UML2_Feature" = None, UML2_Classifier69: set["UML2_Feature"] = None, UML2_Classifier78: "UML2_Class" = None, UML2_Classifier82: "UML2_Action" = None, UML2_Classifier72: set["UML2_NamedElement"] = None, UML2_Classifier75: set["UML2_Generalization"] = None):
        self.isAbstract = isAbstract
        self.UML2_Classifier = UML2_Classifier
        self.UML2_Classifier47 = UML2_Classifier47
        self.UML2_Classifier58 = UML2_Classifier58
        self.UML2_Classifier66 = UML2_Classifier66
        self.UML2_Classifier69 = UML2_Classifier69 if UML2_Classifier69 is not None else set()
        self.UML2_Classifier78 = UML2_Classifier78
        self.UML2_Classifier82 = UML2_Classifier82
        self.UML2_Classifier72 = UML2_Classifier72 if UML2_Classifier72 is not None else set()
        self.UML2_Classifier75 = UML2_Classifier75 if UML2_Classifier75 is not None else set()
        
    @property
    def isAbstract(self) -> bool:
        return self.__isAbstract

    @isAbstract.setter
    def isAbstract(self, isAbstract: bool):
        self.__isAbstract = isAbstract

    @property
    def UML2_Classifier82(self):
        return self.__UML2_Classifier82

    @UML2_Classifier82.setter
    def UML2_Classifier82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier82", None)
        self.__UML2_Classifier82 = value
        
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
    def UML2_Classifier69(self):
        return self.__UML2_Classifier69

    @UML2_Classifier69.setter
    def UML2_Classifier69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier69", None)
        self.__UML2_Classifier69 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Feature70"):
                    opp_val = getattr(item, "UML2_Feature70", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Feature70", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Feature70"):
                    opp_val = getattr(item, "UML2_Feature70", None)
                    
                    setattr(item, "UML2_Feature70", self)
                    

    @property
    def UML2_Classifier47(self):
        return self.__UML2_Classifier47

    @UML2_Classifier47.setter
    def UML2_Classifier47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier47", None)
        self.__UML2_Classifier47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UML2_InstanceSpecification46"):
                opp_val = getattr(old_value, "UML2_InstanceSpecification46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_InstanceSpecification46"):
                opp_val = getattr(value, "UML2_InstanceSpecification46", None)
                if opp_val is None:
                    setattr(value, "UML2_InstanceSpecification46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UML2_Classifier75(self):
        return self.__UML2_Classifier75

    @UML2_Classifier75.setter
    def UML2_Classifier75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier75", None)
        self.__UML2_Classifier75 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_Generalization76"):
                    opp_val = getattr(item, "UML2_Generalization76", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_Generalization76", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_Generalization76"):
                    opp_val = getattr(item, "UML2_Generalization76", None)
                    
                    setattr(item, "UML2_Generalization76", self)
                    

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
    def UML2_Classifier78(self):
        return self.__UML2_Classifier78

    @UML2_Classifier78.setter
    def UML2_Classifier78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier78", None)
        self.__UML2_Classifier78 = value
        
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
    def UML2_Classifier72(self):
        return self.__UML2_Classifier72

    @UML2_Classifier72.setter
    def UML2_Classifier72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UML2_Classifier__UML2_Classifier72", None)
        self.__UML2_Classifier72 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "UML2_NamedElement73"):
                    opp_val = getattr(item, "UML2_NamedElement73", None)
                    
                    if opp_val == self:
                        setattr(item, "UML2_NamedElement73", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "UML2_NamedElement73"):
                    opp_val = getattr(item, "UML2_NamedElement73", None)
                    
                    setattr(item, "UML2_NamedElement73", self)
                    

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
            if hasattr(old_value, "UML2_Generalization30"):
                opp_val = getattr(old_value, "UML2_Generalization30", None)
                if opp_val == self:
                    setattr(old_value, "UML2_Generalization30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UML2_Generalization30"):
                opp_val = getattr(value, "UML2_Generalization30", None)
                setattr(value, "UML2_Generalization30", self)

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

class UML2_Region(RedefinableElement, Namespace):

    pass
class UML2_State(Namespace, RedefinableElement, Vertex):

    pass