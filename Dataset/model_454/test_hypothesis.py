import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    EObject,
    UMLModel_UMLBase,
    Expression,
    TemplateSignature,
    LinkAction,
    UMLModel_WriteLinkAction,
    UMLModel_ReadLinkAction,
    StructuralFeature,
    Transition,
    UMLModel_ProtocolTransition,
    StateMachine,
    InteractionUse,
    UMLModel_PartDecomposition,
    ConnectableElement,
    BehavioralFeature,
    Package,
    UMLModel_Profile,
    UMLModel_Model,
    Abstraction,
    UMLModel_Realization,
    LinkEndData,
    UMLModel_LinkEndDestructionData,
    UMLModel_LinkEndCreationData,
    LiteralSpecification,
    UMLModel_LiteralBoolean,
    UMLModel_LiteralNull,
    UMLModel_LiteralString,
    UMLModel_LiteralUnlimitedNatural,
    UMLModel_LiteralInteger,
    Constraint,
    UMLModel_IntervalConstraint,
    UMLModel_InteractionConstraint,
    Pin,
    DeploymentTarget,
    UMLModel_ProtocolStateMachine,
    MessageEnd,
    OpaqueBehavior,
    UMLModel_FunctionBehavior,
    State,
    UMLModel_FinalState,
    Property,
    UMLModel_Port,
    UMLModel_ExtensionEnd,
    OccurrenceSpecification,
    UMLModel_MessageOccurrenceSpecification,
    UMLModel_ExecutionOccurrenceSpecification,
    InstanceSpecification,
    UMLBase,
    UMLModel_Element,
    Observation,
    UMLModel_TimeObservation,
    UMLModel_DurationObservation,
    Interval,
    UMLModel_TimeInterval,
    UMLModel_DurationInterval,
    IntervalConstraint,
    UMLModel_TimeConstraint,
    UMLModel_DurationConstraint,
    ValueSpecification,
    UMLModel_Expression,
    UMLModel_LiteralSpecification,
    UMLModel_TimeExpression,
    UMLModel_Interval,
    UMLModel_InstanceValue,
    UMLModel_Duration,
    UMLModel_EnumerationLiteral,
    DataType,
    UMLModel_PrimitiveType,
    UMLModel_Enumeration,
    Node,
    UMLModel_ExecutionEnvironment,
    UMLModel_Device,
    Artifact,
    UMLModel_DeploymentSpecification,
    MultiplicityElement,
    UMLModel_ConnectorEnd,
    DirectedRelationship,
    UMLModel_TemplateBinding,
    UMLModel_ProfileApplication,
    UMLModel_ElementImport,
    UMLModel_PackageImport,
    UMLModel_PackageMerge,
    UMLModel_ProtocolConformance,
    ParameterableElement,
    TypedElement,
    ControlNode,
    UMLModel_MergeNode,
    UMLModel_ForkNode,
    UMLModel_FinalNode,
    UMLModel_JoinNode,
    UMLModel_InitialNode,
    UMLModel_ConnectableElement,
    UMLModel_DecisionNode,
    Element,
    UMLModel_Slot,
    UMLModel_LinkEndData,
    UMLModel_ParameterableElement,
    UMLModel_TemplateParameter,
    UMLModel_MultiplicityElement,
    UMLModel_TemplateParameterSubstitution,
    UMLModel_TemplateableElement,
    UMLModel_Relationship,
    UMLModel_ExceptionHandler,
    UMLModel_NamedElement,
    UMLModel_QualifierValue,
    UMLModel_TemplateSignature,
    UMLModel_Image,
    FinalNode,
    UMLModel_FlowFinalNode,
    UMLModel_ActivityFinalNode,
    ObjectNode,
    UMLModel_Pin,
    UMLModel_ExpansionNode,
    UMLModel_ActivityParameterNode,
    RedefinableElement,
    UMLModel_ExtensionPoint,
    UMLModel_Feature,
    UMLModel_RedefinableTemplateSignature,
    ActivityGroup,
    UMLModel_InterruptibleActivityRegion,
    NamedElement,
    UMLModel_Vertex,
    UMLModel_GeneralOrdering,
    UMLModel_Lifeline,
    UMLModel_MessageEnd,
    UMLModel_Message,
    UMLModel_DeploymentTarget,
    UMLModel_TypedElement,
    UMLModel_RedefinableElement,
    UMLModel_Include,
    UMLModel_Extend,
    UMLModel_InteractionFragment,
    UMLModel_Namespace,
    UMLModel_DeployedArtifact,
    UMLModel_ActivityPartition,
    UMLModel_ActivityNode,
    UMLModel_Variable,
    Behavior,
    UMLModel_OpaqueBehavior,
    UMLModel_StateMachine,
    UMLModel_Activity,
    InputPin,
    UMLModel_ValuePin,
    UMLModel_ActionInputPin,
    ExecutionSpecification,
    UMLModel_ActionExecutionSpecification,
    UMLModel_ActivityGroup,
    UMLModel_ActivityEdge,
    AcceptEventAction,
    UMLModel_AcceptCallAction,
    UMLModel_OpaqueExpression,
    Dependency,
    UMLModel_Usage,
    UMLModel_Deployment,
    UMLModel_Abstraction,
    ExecutableNode,
    UMLModel_Action,
    UMLModel_Trigger,
    Action,
    UMLModel_ReduceAction,
    UMLModel_RaiseExceptionAction,
    UMLModel_ReadSelfAction,
    UMLModel_DestroyObjectAction,
    UMLModel_StructuralFeatureAction,
    UMLModel_TestIdentityAction,
    UMLModel_ReadIsClassifiedObjectAction,
    UMLModel_ReadExtentAction,
    UMLModel_StartClassifierBehaviorAction,
    UMLModel_OpaqueAction,
    UMLModel_LinkAction,
    UMLModel_InvocationAction,
    UMLModel_ValueSpecificationAction,
    UMLModel_UnmarshallAction,
    UMLModel_ReadLinkObjectEndAction,
    UMLModel_ReadLinkObjectEndQualifierAction,
    UMLModel_ReplyAction,
    UMLModel_VariableAction,
    UMLModel_ReclassifyObjectAction,
    UMLModel_AcceptEventAction,
    UMLModel_OutputPin,
    CombinedFragment,
    UMLModel_ConsiderIgnoreFragment,
    CentralBufferNode,
    UMLModel_DataStoreNode,
    UMLModel_CentralBufferNode,
    WriteLinkAction,
    UMLModel_DestroyLinkAction,
    UMLModel_CreateLinkAction,
    PackageableElement,
    UMLModel_Event,
    UMLModel_InformationFlow,
    UMLModel_Constraint,
    UMLModel_GeneralizationSet,
    UMLModel_Observation,
    UMLModel_ValueSpecification,
    UMLModel_Type,
    UMLModel_CreateObjectAction,
    CreateLinkAction,
    UMLModel_CreateLinkObjectAction,
    StructuredActivityNode,
    UMLModel_SequenceNode,
    UMLModel_LoopNode,
    UMLModel_ExpansionRegion,
    UMLModel_ConditionalNode,
    UMLModel_Gate,
    ActivityNode,
    UMLModel_ObjectNode,
    UMLModel_ExecutableNode,
    UMLModel_ControlNode,
    ActivityEdge,
    UMLModel_ObjectFlow,
    UMLModel_ControlFlow,
    Vertex,
    UMLModel_Pseudostate,
    UMLModel_ConnectionPointReference,
    UMLModel_Comment,
    UMLModel_Dependency,
    StructuredClassifier,
    UMLModel_EncapsulatedClassifier,
    StructuralFeatureAction,
    UMLModel_WriteStructuralFeatureAction,
    UMLModel_ReadStructuralFeatureAction,
    UMLModel_ClearStructuralFeatureAction,
    UMLModel_ClearAssociationAction,
    VariableAction,
    UMLModel_ReadVariableAction,
    UMLModel_WriteVariableAction,
    UMLModel_ClearVariableAction,
    UMLModel_Clause,
    InteractionFragment,
    UMLModel_OccurrenceSpecification,
    UMLModel_InteractionUse,
    UMLModel_StateInvariant,
    UMLModel_Interaction,
    UMLModel_Continuation,
    UMLModel_ExecutionSpecification,
    UMLModel_CombinedFragment,
    Realization,
    UMLModel_ComponentRealization,
    UMLModel_PackageableElement,
    UMLModel_Generalization,
    TemplateableElement,
    UMLModel_StringExpression,
    Type,
    UMLModel_Reception,
    EncapsulatedClassifier,
    Event,
    UMLModel_ExecutionEvent,
    UMLModel_DestructionEvent,
    UMLModel_MessageEvent,
    UMLModel_CreationEvent,
    UMLModel_TimeEvent,
    UMLModel_ChangeEvent,
    TemplateParameter,
    UMLModel_ConnectableElementTemplateParameter,
    UMLModel_OperationTemplateParameter,
    UMLModel_ClassifierTemplateParameter,
    UMLModel_CollaborationUse,
    UMLModel_Substitution,
    UMLModel_InterfaceRealization,
    Feature,
    UMLModel_StructuralFeature,
    UMLModel_Connector,
    Namespace,
    UMLModel_Package,
    UMLModel_InteractionOperand,
    UMLModel_Transition,
    UMLModel_State,
    UMLModel_StructuredActivityNode,
    UMLModel_Region,
    UMLModel_Classifier,
    UMLModel_BehavioralFeature,
    UMLModel_BehaviorExecutionSpecification,
    UMLModel_ParameterSet,
    UMLModel_Parameter,
    CallAction,
    UMLModel_CallOperationAction,
    UMLModel_CallBehaviorAction,
    UMLModel_Property,
    InvocationAction,
    UMLModel_SendObjectAction,
    UMLModel_CallAction,
    UMLModel_SendSignalAction,
    UMLModel_BroadcastSignalAction,
    UMLModel_Operation,
    UMLModel_Manifestation,
    DeployedArtifact,
    UMLModel_InstanceSpecification,
    Classifier,
    UMLModel_StructuredClassifier,
    UMLModel_Signal,
    UMLModel_DataType,
    UMLModel_BehavioredClassifier,
    UMLModel_Interface,
    UMLModel_InformationItem,
    UMLModel_Artifact,
    MessageEvent,
    UMLModel_CallEvent,
    UMLModel_ReceiveOperationEvent,
    UMLModel_ReceiveSignalEvent,
    UMLModel_SignalEvent,
    UMLModel_SendSignalEvent,
    UMLModel_AnyReceiveEvent,
    WriteVariableAction,
    UMLModel_RemoveVariableValueAction,
    UMLModel_AddVariableValueAction,
    UMLModel_InputPin,
    WriteStructuralFeatureAction,
    UMLModel_RemoveStructuralFeatureValueAction,
    UMLModel_AddStructuralFeatureValueAction,
    BehavioredClassifier,
    UMLModel_Collaboration,
    UMLModel_Class,
    UMLModel_UseCase,
    UMLModel_Actor,
    Association,
    UMLModel_CommunicationPath,
    UMLModel_Extension,
    Class,
    UMLModel_Stereotype,
    UMLModel_Component,
    UMLModel_Node,
    UMLModel_Behavior,
    UMLModel_AssociationClass,
    Relationship,
    UMLModel_DirectedRelationship,
    UMLModel_Association,
    ParameterEffectKind,
    VisibilityKind,
    MessageSort,
    ConnectorKind,
    ParameterDirectionKind,
    ExpansionKind,
    PseudostateKind,
    CallConcurrencyKind,
    InteractionOperatorKind,
    TransitionKind,
    MessageKind,
    ObjectNodeOrderingKind,
    AggregationKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_eobject_is_not_abstract():
    assert not inspect.isabstract(EObject)


def test_eobject_constructor_exists():
    assert callable(EObject.__init__)


def test_eobject_constructor_args():
    sig = inspect.signature(EObject.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_umlbase_is_not_abstract():
    assert not inspect.isabstract(UMLModel_UMLBase)


def test_umlmodel_umlbase_constructor_exists():
    assert callable(UMLModel_UMLBase.__init__)


def test_umlmodel_umlbase_constructor_args():
    sig = inspect.signature(UMLModel_UMLBase.__init__)
    params = list(sig.parameters.keys())
    assert "umlID" in params, "Missing parameter 'umlID'"

def test_umlmodel_umlbase_has_umlID():
    assert hasattr(UMLModel_UMLBase, "umlID")
    descriptor = None
    for klass in UMLModel_UMLBase.__mro__:
        if "umlID" in klass.__dict__:
            descriptor = klass.__dict__["umlID"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_templatesignature_is_not_abstract():
    assert not inspect.isabstract(TemplateSignature)


def test_templatesignature_constructor_exists():
    assert callable(TemplateSignature.__init__)


def test_templatesignature_constructor_args():
    sig = inspect.signature(TemplateSignature.__init__)
    params = list(sig.parameters.keys())



def test_linkaction_is_not_abstract():
    assert not inspect.isabstract(LinkAction)


def test_linkaction_constructor_exists():
    assert callable(LinkAction.__init__)


def test_linkaction_constructor_args():
    sig = inspect.signature(LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_writelinkaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel_WriteLinkAction)


def test_umlmodel_writelinkaction_constructor_exists():
    assert callable(UMLModel_WriteLinkAction.__init__)


def test_umlmodel_writelinkaction_constructor_args():
    sig = inspect.signature(UMLModel_WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_readlinkaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ReadLinkAction)


def test_umlmodel_readlinkaction_constructor_exists():
    assert callable(UMLModel_ReadLinkAction.__init__)


def test_umlmodel_readlinkaction_constructor_args():
    sig = inspect.signature(UMLModel_ReadLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(StructuralFeature)


def test_structuralfeature_constructor_exists():
    assert callable(StructuralFeature.__init__)


def test_structuralfeature_constructor_args():
    sig = inspect.signature(StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_protocoltransition_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ProtocolTransition)


def test_umlmodel_protocoltransition_constructor_exists():
    assert callable(UMLModel_ProtocolTransition.__init__)


def test_umlmodel_protocoltransition_constructor_args():
    sig = inspect.signature(UMLModel_ProtocolTransition.__init__)
    params = list(sig.parameters.keys())
    assert "referred" in params, "Missing parameter 'referred'"
    assert "preCondition" in params, "Missing parameter 'preCondition'"
    assert "postCondition" in params, "Missing parameter 'postCondition'"

def test_umlmodel_protocoltransition_has_referred():
    assert hasattr(UMLModel_ProtocolTransition, "referred")
    descriptor = None
    for klass in UMLModel_ProtocolTransition.__mro__:
        if "referred" in klass.__dict__:
            descriptor = klass.__dict__["referred"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_protocoltransition_has_preCondition():
    assert hasattr(UMLModel_ProtocolTransition, "preCondition")
    descriptor = None
    for klass in UMLModel_ProtocolTransition.__mro__:
        if "preCondition" in klass.__dict__:
            descriptor = klass.__dict__["preCondition"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_protocoltransition_has_postCondition():
    assert hasattr(UMLModel_ProtocolTransition, "postCondition")
    descriptor = None
    for klass in UMLModel_ProtocolTransition.__mro__:
        if "postCondition" in klass.__dict__:
            descriptor = klass.__dict__["postCondition"]
            break
    assert isinstance(descriptor, property)



def test_statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachine)


def test_statemachine_constructor_exists():
    assert callable(StateMachine.__init__)


def test_statemachine_constructor_args():
    sig = inspect.signature(StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_interactionuse_is_not_abstract():
    assert not inspect.isabstract(InteractionUse)


def test_interactionuse_constructor_exists():
    assert callable(InteractionUse.__init__)


def test_interactionuse_constructor_args():
    sig = inspect.signature(InteractionUse.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_partdecomposition_is_not_abstract():
    assert not inspect.isabstract(UMLModel_PartDecomposition)


def test_umlmodel_partdecomposition_constructor_exists():
    assert callable(UMLModel_PartDecomposition.__init__)


def test_umlmodel_partdecomposition_constructor_args():
    sig = inspect.signature(UMLModel_PartDecomposition.__init__)
    params = list(sig.parameters.keys())



def test_connectableelement_is_not_abstract():
    assert not inspect.isabstract(ConnectableElement)


def test_connectableelement_constructor_exists():
    assert callable(ConnectableElement.__init__)


def test_connectableelement_constructor_args():
    sig = inspect.signature(ConnectableElement.__init__)
    params = list(sig.parameters.keys())



def test_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(BehavioralFeature)


def test_behavioralfeature_constructor_exists():
    assert callable(BehavioralFeature.__init__)


def test_behavioralfeature_constructor_args():
    sig = inspect.signature(BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_package_constructor_exists():
    assert callable(Package.__init__)


def test_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_profile_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Profile)


def test_umlmodel_profile_constructor_exists():
    assert callable(UMLModel_Profile.__init__)


def test_umlmodel_profile_constructor_args():
    sig = inspect.signature(UMLModel_Profile.__init__)
    params = list(sig.parameters.keys())
    assert "metamodelReference" in params, "Missing parameter 'metamodelReference'"
    assert "metaclassReference" in params, "Missing parameter 'metaclassReference'"
    assert "ownedStereotype" in params, "Missing parameter 'ownedStereotype'"

def test_umlmodel_profile_has_metamodelReference():
    assert hasattr(UMLModel_Profile, "metamodelReference")
    descriptor = None
    for klass in UMLModel_Profile.__mro__:
        if "metamodelReference" in klass.__dict__:
            descriptor = klass.__dict__["metamodelReference"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_profile_has_metaclassReference():
    assert hasattr(UMLModel_Profile, "metaclassReference")
    descriptor = None
    for klass in UMLModel_Profile.__mro__:
        if "metaclassReference" in klass.__dict__:
            descriptor = klass.__dict__["metaclassReference"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_profile_has_ownedStereotype():
    assert hasattr(UMLModel_Profile, "ownedStereotype")
    descriptor = None
    for klass in UMLModel_Profile.__mro__:
        if "ownedStereotype" in klass.__dict__:
            descriptor = klass.__dict__["ownedStereotype"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_model_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Model)


def test_umlmodel_model_constructor_exists():
    assert callable(UMLModel_Model.__init__)


def test_umlmodel_model_constructor_args():
    sig = inspect.signature(UMLModel_Model.__init__)
    params = list(sig.parameters.keys())
    assert "viewpoint" in params, "Missing parameter 'viewpoint'"

def test_umlmodel_model_has_viewpoint():
    assert hasattr(UMLModel_Model, "viewpoint")
    descriptor = None
    for klass in UMLModel_Model.__mro__:
        if "viewpoint" in klass.__dict__:
            descriptor = klass.__dict__["viewpoint"]
            break
    assert isinstance(descriptor, property)



def test_abstraction_is_not_abstract():
    assert not inspect.isabstract(Abstraction)


def test_abstraction_constructor_exists():
    assert callable(Abstraction.__init__)


def test_abstraction_constructor_args():
    sig = inspect.signature(Abstraction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_realization_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Realization)


def test_umlmodel_realization_constructor_exists():
    assert callable(UMLModel_Realization.__init__)


def test_umlmodel_realization_constructor_args():
    sig = inspect.signature(UMLModel_Realization.__init__)
    params = list(sig.parameters.keys())



def test_linkenddata_is_not_abstract():
    assert not inspect.isabstract(LinkEndData)


def test_linkenddata_constructor_exists():
    assert callable(LinkEndData.__init__)


def test_linkenddata_constructor_args():
    sig = inspect.signature(LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_linkenddestructiondata_is_not_abstract():
    assert not inspect.isabstract(UMLModel_LinkEndDestructionData)


def test_umlmodel_linkenddestructiondata_constructor_exists():
    assert callable(UMLModel_LinkEndDestructionData.__init__)


def test_umlmodel_linkenddestructiondata_constructor_args():
    sig = inspect.signature(UMLModel_LinkEndDestructionData.__init__)
    params = list(sig.parameters.keys())
    assert "destroyAt" in params, "Missing parameter 'destroyAt'"
    assert "isDestroyDuplicates" in params, "Missing parameter 'isDestroyDuplicates'"

def test_umlmodel_linkenddestructiondata_has_destroyAt():
    assert hasattr(UMLModel_LinkEndDestructionData, "destroyAt")
    descriptor = None
    for klass in UMLModel_LinkEndDestructionData.__mro__:
        if "destroyAt" in klass.__dict__:
            descriptor = klass.__dict__["destroyAt"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_linkenddestructiondata_has_isDestroyDuplicates():
    assert hasattr(UMLModel_LinkEndDestructionData, "isDestroyDuplicates")
    descriptor = None
    for klass in UMLModel_LinkEndDestructionData.__mro__:
        if "isDestroyDuplicates" in klass.__dict__:
            descriptor = klass.__dict__["isDestroyDuplicates"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_linkendcreationdata_is_not_abstract():
    assert not inspect.isabstract(UMLModel_LinkEndCreationData)


def test_umlmodel_linkendcreationdata_constructor_exists():
    assert callable(UMLModel_LinkEndCreationData.__init__)


def test_umlmodel_linkendcreationdata_constructor_args():
    sig = inspect.signature(UMLModel_LinkEndCreationData.__init__)
    params = list(sig.parameters.keys())
    assert "insertAt" in params, "Missing parameter 'insertAt'"
    assert "isReplaceAll" in params, "Missing parameter 'isReplaceAll'"

def test_umlmodel_linkendcreationdata_has_insertAt():
    assert hasattr(UMLModel_LinkEndCreationData, "insertAt")
    descriptor = None
    for klass in UMLModel_LinkEndCreationData.__mro__:
        if "insertAt" in klass.__dict__:
            descriptor = klass.__dict__["insertAt"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_linkendcreationdata_has_isReplaceAll():
    assert hasattr(UMLModel_LinkEndCreationData, "isReplaceAll")
    descriptor = None
    for klass in UMLModel_LinkEndCreationData.__mro__:
        if "isReplaceAll" in klass.__dict__:
            descriptor = klass.__dict__["isReplaceAll"]
            break
    assert isinstance(descriptor, property)



def test_literalspecification_is_not_abstract():
    assert not inspect.isabstract(LiteralSpecification)


def test_literalspecification_constructor_exists():
    assert callable(LiteralSpecification.__init__)


def test_literalspecification_constructor_args():
    sig = inspect.signature(LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_literalboolean_is_not_abstract():
    assert not inspect.isabstract(UMLModel_LiteralBoolean)


def test_umlmodel_literalboolean_constructor_exists():
    assert callable(UMLModel_LiteralBoolean.__init__)


def test_umlmodel_literalboolean_constructor_args():
    sig = inspect.signature(UMLModel_LiteralBoolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_umlmodel_literalboolean_has_value():
    assert hasattr(UMLModel_LiteralBoolean, "value")
    descriptor = None
    for klass in UMLModel_LiteralBoolean.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_literalnull_is_not_abstract():
    assert not inspect.isabstract(UMLModel_LiteralNull)


def test_umlmodel_literalnull_constructor_exists():
    assert callable(UMLModel_LiteralNull.__init__)


def test_umlmodel_literalnull_constructor_args():
    sig = inspect.signature(UMLModel_LiteralNull.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_literalstring_is_not_abstract():
    assert not inspect.isabstract(UMLModel_LiteralString)


def test_umlmodel_literalstring_constructor_exists():
    assert callable(UMLModel_LiteralString.__init__)


def test_umlmodel_literalstring_constructor_args():
    sig = inspect.signature(UMLModel_LiteralString.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_umlmodel_literalstring_has_value():
    assert hasattr(UMLModel_LiteralString, "value")
    descriptor = None
    for klass in UMLModel_LiteralString.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_literalunlimitednatural_is_not_abstract():
    assert not inspect.isabstract(UMLModel_LiteralUnlimitedNatural)


def test_umlmodel_literalunlimitednatural_constructor_exists():
    assert callable(UMLModel_LiteralUnlimitedNatural.__init__)


def test_umlmodel_literalunlimitednatural_constructor_args():
    sig = inspect.signature(UMLModel_LiteralUnlimitedNatural.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_umlmodel_literalunlimitednatural_has_value():
    assert hasattr(UMLModel_LiteralUnlimitedNatural, "value")
    descriptor = None
    for klass in UMLModel_LiteralUnlimitedNatural.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_literalinteger_is_not_abstract():
    assert not inspect.isabstract(UMLModel_LiteralInteger)


def test_umlmodel_literalinteger_constructor_exists():
    assert callable(UMLModel_LiteralInteger.__init__)


def test_umlmodel_literalinteger_constructor_args():
    sig = inspect.signature(UMLModel_LiteralInteger.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_umlmodel_literalinteger_has_value():
    assert hasattr(UMLModel_LiteralInteger, "value")
    descriptor = None
    for klass in UMLModel_LiteralInteger.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_intervalconstraint_is_not_abstract():
    assert not inspect.isabstract(UMLModel_IntervalConstraint)


def test_umlmodel_intervalconstraint_constructor_exists():
    assert callable(UMLModel_IntervalConstraint.__init__)


def test_umlmodel_intervalconstraint_constructor_args():
    sig = inspect.signature(UMLModel_IntervalConstraint.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_interactionconstraint_is_not_abstract():
    assert not inspect.isabstract(UMLModel_InteractionConstraint)


def test_umlmodel_interactionconstraint_constructor_exists():
    assert callable(UMLModel_InteractionConstraint.__init__)


def test_umlmodel_interactionconstraint_constructor_args():
    sig = inspect.signature(UMLModel_InteractionConstraint.__init__)
    params = list(sig.parameters.keys())



def test_pin_is_not_abstract():
    assert not inspect.isabstract(Pin)


def test_pin_constructor_exists():
    assert callable(Pin.__init__)


def test_pin_constructor_args():
    sig = inspect.signature(Pin.__init__)
    params = list(sig.parameters.keys())



def test_deploymenttarget_is_not_abstract():
    assert not inspect.isabstract(DeploymentTarget)


def test_deploymenttarget_constructor_exists():
    assert callable(DeploymentTarget.__init__)


def test_deploymenttarget_constructor_args():
    sig = inspect.signature(DeploymentTarget.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_protocolstatemachine_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ProtocolStateMachine)


def test_umlmodel_protocolstatemachine_constructor_exists():
    assert callable(UMLModel_ProtocolStateMachine.__init__)


def test_umlmodel_protocolstatemachine_constructor_args():
    sig = inspect.signature(UMLModel_ProtocolStateMachine.__init__)
    params = list(sig.parameters.keys())



def test_messageend_is_not_abstract():
    assert not inspect.isabstract(MessageEnd)


def test_messageend_constructor_exists():
    assert callable(MessageEnd.__init__)


def test_messageend_constructor_args():
    sig = inspect.signature(MessageEnd.__init__)
    params = list(sig.parameters.keys())



def test_opaquebehavior_is_not_abstract():
    assert not inspect.isabstract(OpaqueBehavior)


def test_opaquebehavior_constructor_exists():
    assert callable(OpaqueBehavior.__init__)


def test_opaquebehavior_constructor_args():
    sig = inspect.signature(OpaqueBehavior.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_functionbehavior_is_not_abstract():
    assert not inspect.isabstract(UMLModel_FunctionBehavior)


def test_umlmodel_functionbehavior_constructor_exists():
    assert callable(UMLModel_FunctionBehavior.__init__)


def test_umlmodel_functionbehavior_constructor_args():
    sig = inspect.signature(UMLModel_FunctionBehavior.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_finalstate_is_not_abstract():
    assert not inspect.isabstract(UMLModel_FinalState)


def test_umlmodel_finalstate_constructor_exists():
    assert callable(UMLModel_FinalState.__init__)


def test_umlmodel_finalstate_constructor_args():
    sig = inspect.signature(UMLModel_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_port_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Port)


def test_umlmodel_port_constructor_exists():
    assert callable(UMLModel_Port.__init__)


def test_umlmodel_port_constructor_args():
    sig = inspect.signature(UMLModel_Port.__init__)
    params = list(sig.parameters.keys())
    assert "provided" in params, "Missing parameter 'provided'"
    assert "protocol" in params, "Missing parameter 'protocol'"
    assert "required" in params, "Missing parameter 'required'"
    assert "isService" in params, "Missing parameter 'isService'"
    assert "redefinedPort" in params, "Missing parameter 'redefinedPort'"
    assert "isBehavior" in params, "Missing parameter 'isBehavior'"

def test_umlmodel_port_has_provided():
    assert hasattr(UMLModel_Port, "provided")
    descriptor = None
    for klass in UMLModel_Port.__mro__:
        if "provided" in klass.__dict__:
            descriptor = klass.__dict__["provided"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_port_has_protocol():
    assert hasattr(UMLModel_Port, "protocol")
    descriptor = None
    for klass in UMLModel_Port.__mro__:
        if "protocol" in klass.__dict__:
            descriptor = klass.__dict__["protocol"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_port_has_required():
    assert hasattr(UMLModel_Port, "required")
    descriptor = None
    for klass in UMLModel_Port.__mro__:
        if "required" in klass.__dict__:
            descriptor = klass.__dict__["required"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_port_has_isService():
    assert hasattr(UMLModel_Port, "isService")
    descriptor = None
    for klass in UMLModel_Port.__mro__:
        if "isService" in klass.__dict__:
            descriptor = klass.__dict__["isService"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_port_has_redefinedPort():
    assert hasattr(UMLModel_Port, "redefinedPort")
    descriptor = None
    for klass in UMLModel_Port.__mro__:
        if "redefinedPort" in klass.__dict__:
            descriptor = klass.__dict__["redefinedPort"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_port_has_isBehavior():
    assert hasattr(UMLModel_Port, "isBehavior")
    descriptor = None
    for klass in UMLModel_Port.__mro__:
        if "isBehavior" in klass.__dict__:
            descriptor = klass.__dict__["isBehavior"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_extensionend_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ExtensionEnd)


def test_umlmodel_extensionend_constructor_exists():
    assert callable(UMLModel_ExtensionEnd.__init__)


def test_umlmodel_extensionend_constructor_args():
    sig = inspect.signature(UMLModel_ExtensionEnd.__init__)
    params = list(sig.parameters.keys())



def test_occurrencespecification_is_not_abstract():
    assert not inspect.isabstract(OccurrenceSpecification)


def test_occurrencespecification_constructor_exists():
    assert callable(OccurrenceSpecification.__init__)


def test_occurrencespecification_constructor_args():
    sig = inspect.signature(OccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_messageoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(UMLModel_MessageOccurrenceSpecification)


def test_umlmodel_messageoccurrencespecification_constructor_exists():
    assert callable(UMLModel_MessageOccurrenceSpecification.__init__)


def test_umlmodel_messageoccurrencespecification_constructor_args():
    sig = inspect.signature(UMLModel_MessageOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_executionoccurrencespecification_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ExecutionOccurrenceSpecification)


def test_umlmodel_executionoccurrencespecification_constructor_exists():
    assert callable(UMLModel_ExecutionOccurrenceSpecification.__init__)


def test_umlmodel_executionoccurrencespecification_constructor_args():
    sig = inspect.signature(UMLModel_ExecutionOccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "execution" in params, "Missing parameter 'execution'"

def test_umlmodel_executionoccurrencespecification_has_execution():
    assert hasattr(UMLModel_ExecutionOccurrenceSpecification, "execution")
    descriptor = None
    for klass in UMLModel_ExecutionOccurrenceSpecification.__mro__:
        if "execution" in klass.__dict__:
            descriptor = klass.__dict__["execution"]
            break
    assert isinstance(descriptor, property)



def test_instancespecification_is_not_abstract():
    assert not inspect.isabstract(InstanceSpecification)


def test_instancespecification_constructor_exists():
    assert callable(InstanceSpecification.__init__)


def test_instancespecification_constructor_args():
    sig = inspect.signature(InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_umlbase_is_not_abstract():
    assert not inspect.isabstract(UMLBase)


def test_umlbase_constructor_exists():
    assert callable(UMLBase.__init__)


def test_umlbase_constructor_args():
    sig = inspect.signature(UMLBase.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_element_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Element)


def test_umlmodel_element_constructor_exists():
    assert callable(UMLModel_Element.__init__)


def test_umlmodel_element_constructor_args():
    sig = inspect.signature(UMLModel_Element.__init__)
    params = list(sig.parameters.keys())
    assert "owner" in params, "Missing parameter 'owner'"
    assert "ownedElement" in params, "Missing parameter 'ownedElement'"
    assert "href" in params, "Missing parameter 'href'"

def test_umlmodel_element_has_owner():
    assert hasattr(UMLModel_Element, "owner")
    descriptor = None
    for klass in UMLModel_Element.__mro__:
        if "owner" in klass.__dict__:
            descriptor = klass.__dict__["owner"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_element_has_ownedElement():
    assert hasattr(UMLModel_Element, "ownedElement")
    descriptor = None
    for klass in UMLModel_Element.__mro__:
        if "ownedElement" in klass.__dict__:
            descriptor = klass.__dict__["ownedElement"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_element_has_href():
    assert hasattr(UMLModel_Element, "href")
    descriptor = None
    for klass in UMLModel_Element.__mro__:
        if "href" in klass.__dict__:
            descriptor = klass.__dict__["href"]
            break
    assert isinstance(descriptor, property)



def test_observation_is_not_abstract():
    assert not inspect.isabstract(Observation)


def test_observation_constructor_exists():
    assert callable(Observation.__init__)


def test_observation_constructor_args():
    sig = inspect.signature(Observation.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_timeobservation_is_not_abstract():
    assert not inspect.isabstract(UMLModel_TimeObservation)


def test_umlmodel_timeobservation_constructor_exists():
    assert callable(UMLModel_TimeObservation.__init__)


def test_umlmodel_timeobservation_constructor_args():
    sig = inspect.signature(UMLModel_TimeObservation.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"
    assert "firstEvent" in params, "Missing parameter 'firstEvent'"

def test_umlmodel_timeobservation_has_event():
    assert hasattr(UMLModel_TimeObservation, "event")
    descriptor = None
    for klass in UMLModel_TimeObservation.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_timeobservation_has_firstEvent():
    assert hasattr(UMLModel_TimeObservation, "firstEvent")
    descriptor = None
    for klass in UMLModel_TimeObservation.__mro__:
        if "firstEvent" in klass.__dict__:
            descriptor = klass.__dict__["firstEvent"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_durationobservation_is_not_abstract():
    assert not inspect.isabstract(UMLModel_DurationObservation)


def test_umlmodel_durationobservation_constructor_exists():
    assert callable(UMLModel_DurationObservation.__init__)


def test_umlmodel_durationobservation_constructor_args():
    sig = inspect.signature(UMLModel_DurationObservation.__init__)
    params = list(sig.parameters.keys())
    assert "firstEvent" in params, "Missing parameter 'firstEvent'"
    assert "event" in params, "Missing parameter 'event'"

def test_umlmodel_durationobservation_has_firstEvent():
    assert hasattr(UMLModel_DurationObservation, "firstEvent")
    descriptor = None
    for klass in UMLModel_DurationObservation.__mro__:
        if "firstEvent" in klass.__dict__:
            descriptor = klass.__dict__["firstEvent"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_durationobservation_has_event():
    assert hasattr(UMLModel_DurationObservation, "event")
    descriptor = None
    for klass in UMLModel_DurationObservation.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)



def test_interval_is_not_abstract():
    assert not inspect.isabstract(Interval)


def test_interval_constructor_exists():
    assert callable(Interval.__init__)


def test_interval_constructor_args():
    sig = inspect.signature(Interval.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_timeinterval_is_not_abstract():
    assert not inspect.isabstract(UMLModel_TimeInterval)


def test_umlmodel_timeinterval_constructor_exists():
    assert callable(UMLModel_TimeInterval.__init__)


def test_umlmodel_timeinterval_constructor_args():
    sig = inspect.signature(UMLModel_TimeInterval.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_durationinterval_is_not_abstract():
    assert not inspect.isabstract(UMLModel_DurationInterval)


def test_umlmodel_durationinterval_constructor_exists():
    assert callable(UMLModel_DurationInterval.__init__)


def test_umlmodel_durationinterval_constructor_args():
    sig = inspect.signature(UMLModel_DurationInterval.__init__)
    params = list(sig.parameters.keys())



def test_intervalconstraint_is_not_abstract():
    assert not inspect.isabstract(IntervalConstraint)


def test_intervalconstraint_constructor_exists():
    assert callable(IntervalConstraint.__init__)


def test_intervalconstraint_constructor_args():
    sig = inspect.signature(IntervalConstraint.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_timeconstraint_is_not_abstract():
    assert not inspect.isabstract(UMLModel_TimeConstraint)


def test_umlmodel_timeconstraint_constructor_exists():
    assert callable(UMLModel_TimeConstraint.__init__)


def test_umlmodel_timeconstraint_constructor_args():
    sig = inspect.signature(UMLModel_TimeConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "firstEvent" in params, "Missing parameter 'firstEvent'"

def test_umlmodel_timeconstraint_has_firstEvent():
    assert hasattr(UMLModel_TimeConstraint, "firstEvent")
    descriptor = None
    for klass in UMLModel_TimeConstraint.__mro__:
        if "firstEvent" in klass.__dict__:
            descriptor = klass.__dict__["firstEvent"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_durationconstraint_is_not_abstract():
    assert not inspect.isabstract(UMLModel_DurationConstraint)


def test_umlmodel_durationconstraint_constructor_exists():
    assert callable(UMLModel_DurationConstraint.__init__)


def test_umlmodel_durationconstraint_constructor_args():
    sig = inspect.signature(UMLModel_DurationConstraint.__init__)
    params = list(sig.parameters.keys())
    assert "firstEvent" in params, "Missing parameter 'firstEvent'"

def test_umlmodel_durationconstraint_has_firstEvent():
    assert hasattr(UMLModel_DurationConstraint, "firstEvent")
    descriptor = None
    for klass in UMLModel_DurationConstraint.__mro__:
        if "firstEvent" in klass.__dict__:
            descriptor = klass.__dict__["firstEvent"]
            break
    assert isinstance(descriptor, property)



def test_valuespecification_is_not_abstract():
    assert not inspect.isabstract(ValueSpecification)


def test_valuespecification_constructor_exists():
    assert callable(ValueSpecification.__init__)


def test_valuespecification_constructor_args():
    sig = inspect.signature(ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_expression_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Expression)


def test_umlmodel_expression_constructor_exists():
    assert callable(UMLModel_Expression.__init__)


def test_umlmodel_expression_constructor_args():
    sig = inspect.signature(UMLModel_Expression.__init__)
    params = list(sig.parameters.keys())
    assert "symbol" in params, "Missing parameter 'symbol'"

def test_umlmodel_expression_has_symbol():
    assert hasattr(UMLModel_Expression, "symbol")
    descriptor = None
    for klass in UMLModel_Expression.__mro__:
        if "symbol" in klass.__dict__:
            descriptor = klass.__dict__["symbol"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_literalspecification_is_not_abstract():
    assert not inspect.isabstract(UMLModel_LiteralSpecification)


def test_umlmodel_literalspecification_constructor_exists():
    assert callable(UMLModel_LiteralSpecification.__init__)


def test_umlmodel_literalspecification_constructor_args():
    sig = inspect.signature(UMLModel_LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_timeexpression_is_not_abstract():
    assert not inspect.isabstract(UMLModel_TimeExpression)


def test_umlmodel_timeexpression_constructor_exists():
    assert callable(UMLModel_TimeExpression.__init__)


def test_umlmodel_timeexpression_constructor_args():
    sig = inspect.signature(UMLModel_TimeExpression.__init__)
    params = list(sig.parameters.keys())
    assert "expr" in params, "Missing parameter 'expr'"
    assert "observation" in params, "Missing parameter 'observation'"

def test_umlmodel_timeexpression_has_expr():
    assert hasattr(UMLModel_TimeExpression, "expr")
    descriptor = None
    for klass in UMLModel_TimeExpression.__mro__:
        if "expr" in klass.__dict__:
            descriptor = klass.__dict__["expr"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_timeexpression_has_observation():
    assert hasattr(UMLModel_TimeExpression, "observation")
    descriptor = None
    for klass in UMLModel_TimeExpression.__mro__:
        if "observation" in klass.__dict__:
            descriptor = klass.__dict__["observation"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_interval_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Interval)


def test_umlmodel_interval_constructor_exists():
    assert callable(UMLModel_Interval.__init__)


def test_umlmodel_interval_constructor_args():
    sig = inspect.signature(UMLModel_Interval.__init__)
    params = list(sig.parameters.keys())
    assert "max" in params, "Missing parameter 'max'"
    assert "min" in params, "Missing parameter 'min'"

def test_umlmodel_interval_has_max():
    assert hasattr(UMLModel_Interval, "max")
    descriptor = None
    for klass in UMLModel_Interval.__mro__:
        if "max" in klass.__dict__:
            descriptor = klass.__dict__["max"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_interval_has_min():
    assert hasattr(UMLModel_Interval, "min")
    descriptor = None
    for klass in UMLModel_Interval.__mro__:
        if "min" in klass.__dict__:
            descriptor = klass.__dict__["min"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_instancevalue_is_not_abstract():
    assert not inspect.isabstract(UMLModel_InstanceValue)


def test_umlmodel_instancevalue_constructor_exists():
    assert callable(UMLModel_InstanceValue.__init__)


def test_umlmodel_instancevalue_constructor_args():
    sig = inspect.signature(UMLModel_InstanceValue.__init__)
    params = list(sig.parameters.keys())
    assert "instance" in params, "Missing parameter 'instance'"

def test_umlmodel_instancevalue_has_instance():
    assert hasattr(UMLModel_InstanceValue, "instance")
    descriptor = None
    for klass in UMLModel_InstanceValue.__mro__:
        if "instance" in klass.__dict__:
            descriptor = klass.__dict__["instance"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_duration_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Duration)


def test_umlmodel_duration_constructor_exists():
    assert callable(UMLModel_Duration.__init__)


def test_umlmodel_duration_constructor_args():
    sig = inspect.signature(UMLModel_Duration.__init__)
    params = list(sig.parameters.keys())
    assert "expr" in params, "Missing parameter 'expr'"
    assert "observation" in params, "Missing parameter 'observation'"

def test_umlmodel_duration_has_expr():
    assert hasattr(UMLModel_Duration, "expr")
    descriptor = None
    for klass in UMLModel_Duration.__mro__:
        if "expr" in klass.__dict__:
            descriptor = klass.__dict__["expr"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_duration_has_observation():
    assert hasattr(UMLModel_Duration, "observation")
    descriptor = None
    for klass in UMLModel_Duration.__mro__:
        if "observation" in klass.__dict__:
            descriptor = klass.__dict__["observation"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(UMLModel_EnumerationLiteral)


def test_umlmodel_enumerationliteral_constructor_exists():
    assert callable(UMLModel_EnumerationLiteral.__init__)


def test_umlmodel_enumerationliteral_constructor_args():
    sig = inspect.signature(UMLModel_EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "enumeration" in params, "Missing parameter 'enumeration'"

def test_umlmodel_enumerationliteral_has_enumeration():
    assert hasattr(UMLModel_EnumerationLiteral, "enumeration")
    descriptor = None
    for klass in UMLModel_EnumerationLiteral.__mro__:
        if "enumeration" in klass.__dict__:
            descriptor = klass.__dict__["enumeration"]
            break
    assert isinstance(descriptor, property)



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_primitivetype_is_not_abstract():
    assert not inspect.isabstract(UMLModel_PrimitiveType)


def test_umlmodel_primitivetype_constructor_exists():
    assert callable(UMLModel_PrimitiveType.__init__)


def test_umlmodel_primitivetype_constructor_args():
    sig = inspect.signature(UMLModel_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_enumeration_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Enumeration)


def test_umlmodel_enumeration_constructor_exists():
    assert callable(UMLModel_Enumeration.__init__)


def test_umlmodel_enumeration_constructor_args():
    sig = inspect.signature(UMLModel_Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_executionenvironment_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ExecutionEnvironment)


def test_umlmodel_executionenvironment_constructor_exists():
    assert callable(UMLModel_ExecutionEnvironment.__init__)


def test_umlmodel_executionenvironment_constructor_args():
    sig = inspect.signature(UMLModel_ExecutionEnvironment.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_device_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Device)


def test_umlmodel_device_constructor_exists():
    assert callable(UMLModel_Device.__init__)


def test_umlmodel_device_constructor_args():
    sig = inspect.signature(UMLModel_Device.__init__)
    params = list(sig.parameters.keys())



def test_artifact_is_not_abstract():
    assert not inspect.isabstract(Artifact)


def test_artifact_constructor_exists():
    assert callable(Artifact.__init__)


def test_artifact_constructor_args():
    sig = inspect.signature(Artifact.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_deploymentspecification_is_not_abstract():
    assert not inspect.isabstract(UMLModel_DeploymentSpecification)


def test_umlmodel_deploymentspecification_constructor_exists():
    assert callable(UMLModel_DeploymentSpecification.__init__)


def test_umlmodel_deploymentspecification_constructor_args():
    sig = inspect.signature(UMLModel_DeploymentSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "deployment" in params, "Missing parameter 'deployment'"
    assert "executionLocation" in params, "Missing parameter 'executionLocation'"
    assert "deploymentLocation" in params, "Missing parameter 'deploymentLocation'"

def test_umlmodel_deploymentspecification_has_deployment():
    assert hasattr(UMLModel_DeploymentSpecification, "deployment")
    descriptor = None
    for klass in UMLModel_DeploymentSpecification.__mro__:
        if "deployment" in klass.__dict__:
            descriptor = klass.__dict__["deployment"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_deploymentspecification_has_executionLocation():
    assert hasattr(UMLModel_DeploymentSpecification, "executionLocation")
    descriptor = None
    for klass in UMLModel_DeploymentSpecification.__mro__:
        if "executionLocation" in klass.__dict__:
            descriptor = klass.__dict__["executionLocation"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_deploymentspecification_has_deploymentLocation():
    assert hasattr(UMLModel_DeploymentSpecification, "deploymentLocation")
    descriptor = None
    for klass in UMLModel_DeploymentSpecification.__mro__:
        if "deploymentLocation" in klass.__dict__:
            descriptor = klass.__dict__["deploymentLocation"]
            break
    assert isinstance(descriptor, property)



def test_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(MultiplicityElement)


def test_multiplicityelement_constructor_exists():
    assert callable(MultiplicityElement.__init__)


def test_multiplicityelement_constructor_args():
    sig = inspect.signature(MultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_connectorend_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ConnectorEnd)


def test_umlmodel_connectorend_constructor_exists():
    assert callable(UMLModel_ConnectorEnd.__init__)


def test_umlmodel_connectorend_constructor_args():
    sig = inspect.signature(UMLModel_ConnectorEnd.__init__)
    params = list(sig.parameters.keys())
    assert "partWithPort" in params, "Missing parameter 'partWithPort'"
    assert "definingEnd" in params, "Missing parameter 'definingEnd'"
    assert "role" in params, "Missing parameter 'role'"

def test_umlmodel_connectorend_has_partWithPort():
    assert hasattr(UMLModel_ConnectorEnd, "partWithPort")
    descriptor = None
    for klass in UMLModel_ConnectorEnd.__mro__:
        if "partWithPort" in klass.__dict__:
            descriptor = klass.__dict__["partWithPort"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_connectorend_has_definingEnd():
    assert hasattr(UMLModel_ConnectorEnd, "definingEnd")
    descriptor = None
    for klass in UMLModel_ConnectorEnd.__mro__:
        if "definingEnd" in klass.__dict__:
            descriptor = klass.__dict__["definingEnd"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_connectorend_has_role():
    assert hasattr(UMLModel_ConnectorEnd, "role")
    descriptor = None
    for klass in UMLModel_ConnectorEnd.__mro__:
        if "role" in klass.__dict__:
            descriptor = klass.__dict__["role"]
            break
    assert isinstance(descriptor, property)



def test_directedrelationship_is_not_abstract():
    assert not inspect.isabstract(DirectedRelationship)


def test_directedrelationship_constructor_exists():
    assert callable(DirectedRelationship.__init__)


def test_directedrelationship_constructor_args():
    sig = inspect.signature(DirectedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_templatebinding_is_not_abstract():
    assert not inspect.isabstract(UMLModel_TemplateBinding)


def test_umlmodel_templatebinding_constructor_exists():
    assert callable(UMLModel_TemplateBinding.__init__)


def test_umlmodel_templatebinding_constructor_args():
    sig = inspect.signature(UMLModel_TemplateBinding.__init__)
    params = list(sig.parameters.keys())
    assert "boundElement" in params, "Missing parameter 'boundElement'"
    assert "signature" in params, "Missing parameter 'signature'"

def test_umlmodel_templatebinding_has_boundElement():
    assert hasattr(UMLModel_TemplateBinding, "boundElement")
    descriptor = None
    for klass in UMLModel_TemplateBinding.__mro__:
        if "boundElement" in klass.__dict__:
            descriptor = klass.__dict__["boundElement"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_templatebinding_has_signature():
    assert hasattr(UMLModel_TemplateBinding, "signature")
    descriptor = None
    for klass in UMLModel_TemplateBinding.__mro__:
        if "signature" in klass.__dict__:
            descriptor = klass.__dict__["signature"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_profileapplication_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ProfileApplication)


def test_umlmodel_profileapplication_constructor_exists():
    assert callable(UMLModel_ProfileApplication.__init__)


def test_umlmodel_profileapplication_constructor_args():
    sig = inspect.signature(UMLModel_ProfileApplication.__init__)
    params = list(sig.parameters.keys())
    assert "applyingPackage" in params, "Missing parameter 'applyingPackage'"
    assert "isStrict" in params, "Missing parameter 'isStrict'"
    assert "appliedProfile" in params, "Missing parameter 'appliedProfile'"

def test_umlmodel_profileapplication_has_applyingPackage():
    assert hasattr(UMLModel_ProfileApplication, "applyingPackage")
    descriptor = None
    for klass in UMLModel_ProfileApplication.__mro__:
        if "applyingPackage" in klass.__dict__:
            descriptor = klass.__dict__["applyingPackage"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_profileapplication_has_isStrict():
    assert hasattr(UMLModel_ProfileApplication, "isStrict")
    descriptor = None
    for klass in UMLModel_ProfileApplication.__mro__:
        if "isStrict" in klass.__dict__:
            descriptor = klass.__dict__["isStrict"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_profileapplication_has_appliedProfile():
    assert hasattr(UMLModel_ProfileApplication, "appliedProfile")
    descriptor = None
    for klass in UMLModel_ProfileApplication.__mro__:
        if "appliedProfile" in klass.__dict__:
            descriptor = klass.__dict__["appliedProfile"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_elementimport_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ElementImport)


def test_umlmodel_elementimport_constructor_exists():
    assert callable(UMLModel_ElementImport.__init__)


def test_umlmodel_elementimport_constructor_args():
    sig = inspect.signature(UMLModel_ElementImport.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "importingNamespace" in params, "Missing parameter 'importingNamespace'"
    assert "alias" in params, "Missing parameter 'alias'"

def test_umlmodel_elementimport_has_visibility():
    assert hasattr(UMLModel_ElementImport, "visibility")
    descriptor = None
    for klass in UMLModel_ElementImport.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_elementimport_has_importingNamespace():
    assert hasattr(UMLModel_ElementImport, "importingNamespace")
    descriptor = None
    for klass in UMLModel_ElementImport.__mro__:
        if "importingNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importingNamespace"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_elementimport_has_alias():
    assert hasattr(UMLModel_ElementImport, "alias")
    descriptor = None
    for klass in UMLModel_ElementImport.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_packageimport_is_not_abstract():
    assert not inspect.isabstract(UMLModel_PackageImport)


def test_umlmodel_packageimport_constructor_exists():
    assert callable(UMLModel_PackageImport.__init__)


def test_umlmodel_packageimport_constructor_args():
    sig = inspect.signature(UMLModel_PackageImport.__init__)
    params = list(sig.parameters.keys())
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "importingNamespace" in params, "Missing parameter 'importingNamespace'"

def test_umlmodel_packageimport_has_visibility():
    assert hasattr(UMLModel_PackageImport, "visibility")
    descriptor = None
    for klass in UMLModel_PackageImport.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_packageimport_has_importingNamespace():
    assert hasattr(UMLModel_PackageImport, "importingNamespace")
    descriptor = None
    for klass in UMLModel_PackageImport.__mro__:
        if "importingNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importingNamespace"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_packagemerge_is_not_abstract():
    assert not inspect.isabstract(UMLModel_PackageMerge)


def test_umlmodel_packagemerge_constructor_exists():
    assert callable(UMLModel_PackageMerge.__init__)


def test_umlmodel_packagemerge_constructor_args():
    sig = inspect.signature(UMLModel_PackageMerge.__init__)
    params = list(sig.parameters.keys())
    assert "receivingPackage" in params, "Missing parameter 'receivingPackage'"
    assert "mergedPackage" in params, "Missing parameter 'mergedPackage'"

def test_umlmodel_packagemerge_has_receivingPackage():
    assert hasattr(UMLModel_PackageMerge, "receivingPackage")
    descriptor = None
    for klass in UMLModel_PackageMerge.__mro__:
        if "receivingPackage" in klass.__dict__:
            descriptor = klass.__dict__["receivingPackage"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_packagemerge_has_mergedPackage():
    assert hasattr(UMLModel_PackageMerge, "mergedPackage")
    descriptor = None
    for klass in UMLModel_PackageMerge.__mro__:
        if "mergedPackage" in klass.__dict__:
            descriptor = klass.__dict__["mergedPackage"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_protocolconformance_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ProtocolConformance)


def test_umlmodel_protocolconformance_constructor_exists():
    assert callable(UMLModel_ProtocolConformance.__init__)


def test_umlmodel_protocolconformance_constructor_args():
    sig = inspect.signature(UMLModel_ProtocolConformance.__init__)
    params = list(sig.parameters.keys())
    assert "specificMachine" in params, "Missing parameter 'specificMachine'"
    assert "generalMachine" in params, "Missing parameter 'generalMachine'"

def test_umlmodel_protocolconformance_has_specificMachine():
    assert hasattr(UMLModel_ProtocolConformance, "specificMachine")
    descriptor = None
    for klass in UMLModel_ProtocolConformance.__mro__:
        if "specificMachine" in klass.__dict__:
            descriptor = klass.__dict__["specificMachine"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_protocolconformance_has_generalMachine():
    assert hasattr(UMLModel_ProtocolConformance, "generalMachine")
    descriptor = None
    for klass in UMLModel_ProtocolConformance.__mro__:
        if "generalMachine" in klass.__dict__:
            descriptor = klass.__dict__["generalMachine"]
            break
    assert isinstance(descriptor, property)



def test_parameterableelement_is_not_abstract():
    assert not inspect.isabstract(ParameterableElement)


def test_parameterableelement_constructor_exists():
    assert callable(ParameterableElement.__init__)


def test_parameterableelement_constructor_args():
    sig = inspect.signature(ParameterableElement.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_controlnode_is_not_abstract():
    assert not inspect.isabstract(ControlNode)


def test_controlnode_constructor_exists():
    assert callable(ControlNode.__init__)


def test_controlnode_constructor_args():
    sig = inspect.signature(ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_mergenode_is_not_abstract():
    assert not inspect.isabstract(UMLModel_MergeNode)


def test_umlmodel_mergenode_constructor_exists():
    assert callable(UMLModel_MergeNode.__init__)


def test_umlmodel_mergenode_constructor_args():
    sig = inspect.signature(UMLModel_MergeNode.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_forknode_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ForkNode)


def test_umlmodel_forknode_constructor_exists():
    assert callable(UMLModel_ForkNode.__init__)


def test_umlmodel_forknode_constructor_args():
    sig = inspect.signature(UMLModel_ForkNode.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_finalnode_is_not_abstract():
    assert not inspect.isabstract(UMLModel_FinalNode)


def test_umlmodel_finalnode_constructor_exists():
    assert callable(UMLModel_FinalNode.__init__)


def test_umlmodel_finalnode_constructor_args():
    sig = inspect.signature(UMLModel_FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_joinnode_is_not_abstract():
    assert not inspect.isabstract(UMLModel_JoinNode)


def test_umlmodel_joinnode_constructor_exists():
    assert callable(UMLModel_JoinNode.__init__)


def test_umlmodel_joinnode_constructor_args():
    sig = inspect.signature(UMLModel_JoinNode.__init__)
    params = list(sig.parameters.keys())
    assert "isCombineDuplicate" in params, "Missing parameter 'isCombineDuplicate'"

def test_umlmodel_joinnode_has_isCombineDuplicate():
    assert hasattr(UMLModel_JoinNode, "isCombineDuplicate")
    descriptor = None
    for klass in UMLModel_JoinNode.__mro__:
        if "isCombineDuplicate" in klass.__dict__:
            descriptor = klass.__dict__["isCombineDuplicate"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_initialnode_is_not_abstract():
    assert not inspect.isabstract(UMLModel_InitialNode)


def test_umlmodel_initialnode_constructor_exists():
    assert callable(UMLModel_InitialNode.__init__)


def test_umlmodel_initialnode_constructor_args():
    sig = inspect.signature(UMLModel_InitialNode.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_connectableelement_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ConnectableElement)


def test_umlmodel_connectableelement_constructor_exists():
    assert callable(UMLModel_ConnectableElement.__init__)


def test_umlmodel_connectableelement_constructor_args():
    sig = inspect.signature(UMLModel_ConnectableElement.__init__)
    params = list(sig.parameters.keys())
    assert "end" in params, "Missing parameter 'end'"

def test_umlmodel_connectableelement_has_end():
    assert hasattr(UMLModel_ConnectableElement, "end")
    descriptor = None
    for klass in UMLModel_ConnectableElement.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_decisionnode_is_not_abstract():
    assert not inspect.isabstract(UMLModel_DecisionNode)


def test_umlmodel_decisionnode_constructor_exists():
    assert callable(UMLModel_DecisionNode.__init__)


def test_umlmodel_decisionnode_constructor_args():
    sig = inspect.signature(UMLModel_DecisionNode.__init__)
    params = list(sig.parameters.keys())
    assert "decisionInput" in params, "Missing parameter 'decisionInput'"

def test_umlmodel_decisionnode_has_decisionInput():
    assert hasattr(UMLModel_DecisionNode, "decisionInput")
    descriptor = None
    for klass in UMLModel_DecisionNode.__mro__:
        if "decisionInput" in klass.__dict__:
            descriptor = klass.__dict__["decisionInput"]
            break
    assert isinstance(descriptor, property)



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_slot_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Slot)


def test_umlmodel_slot_constructor_exists():
    assert callable(UMLModel_Slot.__init__)


def test_umlmodel_slot_constructor_args():
    sig = inspect.signature(UMLModel_Slot.__init__)
    params = list(sig.parameters.keys())
    assert "owningInstance" in params, "Missing parameter 'owningInstance'"
    assert "definingFeature" in params, "Missing parameter 'definingFeature'"

def test_umlmodel_slot_has_owningInstance():
    assert hasattr(UMLModel_Slot, "owningInstance")
    descriptor = None
    for klass in UMLModel_Slot.__mro__:
        if "owningInstance" in klass.__dict__:
            descriptor = klass.__dict__["owningInstance"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_slot_has_definingFeature():
    assert hasattr(UMLModel_Slot, "definingFeature")
    descriptor = None
    for klass in UMLModel_Slot.__mro__:
        if "definingFeature" in klass.__dict__:
            descriptor = klass.__dict__["definingFeature"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_linkenddata_is_not_abstract():
    assert not inspect.isabstract(UMLModel_LinkEndData)


def test_umlmodel_linkenddata_constructor_exists():
    assert callable(UMLModel_LinkEndData.__init__)


def test_umlmodel_linkenddata_constructor_args():
    sig = inspect.signature(UMLModel_LinkEndData.__init__)
    params = list(sig.parameters.keys())
    assert "end" in params, "Missing parameter 'end'"
    assert "value" in params, "Missing parameter 'value'"

def test_umlmodel_linkenddata_has_end():
    assert hasattr(UMLModel_LinkEndData, "end")
    descriptor = None
    for klass in UMLModel_LinkEndData.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_linkenddata_has_value():
    assert hasattr(UMLModel_LinkEndData, "value")
    descriptor = None
    for klass in UMLModel_LinkEndData.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_parameterableelement_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ParameterableElement)


def test_umlmodel_parameterableelement_constructor_exists():
    assert callable(UMLModel_ParameterableElement.__init__)


def test_umlmodel_parameterableelement_constructor_args():
    sig = inspect.signature(UMLModel_ParameterableElement.__init__)
    params = list(sig.parameters.keys())
    assert "owningTemplateParameter" in params, "Missing parameter 'owningTemplateParameter'"
    assert "templateParameter" in params, "Missing parameter 'templateParameter'"

def test_umlmodel_parameterableelement_has_owningTemplateParameter():
    assert hasattr(UMLModel_ParameterableElement, "owningTemplateParameter")
    descriptor = None
    for klass in UMLModel_ParameterableElement.__mro__:
        if "owningTemplateParameter" in klass.__dict__:
            descriptor = klass.__dict__["owningTemplateParameter"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_parameterableelement_has_templateParameter():
    assert hasattr(UMLModel_ParameterableElement, "templateParameter")
    descriptor = None
    for klass in UMLModel_ParameterableElement.__mro__:
        if "templateParameter" in klass.__dict__:
            descriptor = klass.__dict__["templateParameter"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_templateparameter_is_not_abstract():
    assert not inspect.isabstract(UMLModel_TemplateParameter)


def test_umlmodel_templateparameter_constructor_exists():
    assert callable(UMLModel_TemplateParameter.__init__)


def test_umlmodel_templateparameter_constructor_args():
    sig = inspect.signature(UMLModel_TemplateParameter.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"
    assert "parameteredElement" in params, "Missing parameter 'parameteredElement'"
    assert "signature" in params, "Missing parameter 'signature'"

def test_umlmodel_templateparameter_has_default():
    assert hasattr(UMLModel_TemplateParameter, "default")
    descriptor = None
    for klass in UMLModel_TemplateParameter.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_templateparameter_has_parameteredElement():
    assert hasattr(UMLModel_TemplateParameter, "parameteredElement")
    descriptor = None
    for klass in UMLModel_TemplateParameter.__mro__:
        if "parameteredElement" in klass.__dict__:
            descriptor = klass.__dict__["parameteredElement"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_templateparameter_has_signature():
    assert hasattr(UMLModel_TemplateParameter, "signature")
    descriptor = None
    for klass in UMLModel_TemplateParameter.__mro__:
        if "signature" in klass.__dict__:
            descriptor = klass.__dict__["signature"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(UMLModel_MultiplicityElement)


def test_umlmodel_multiplicityelement_constructor_exists():
    assert callable(UMLModel_MultiplicityElement.__init__)


def test_umlmodel_multiplicityelement_constructor_args():
    sig = inspect.signature(UMLModel_MultiplicityElement.__init__)
    params = list(sig.parameters.keys())
    assert "lower" in params, "Missing parameter 'lower'"
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"
    assert "isUnique" in params, "Missing parameter 'isUnique'"
    assert "upper" in params, "Missing parameter 'upper'"

def test_umlmodel_multiplicityelement_has_lower():
    assert hasattr(UMLModel_MultiplicityElement, "lower")
    descriptor = None
    for klass in UMLModel_MultiplicityElement.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_multiplicityelement_has_isOrdered():
    assert hasattr(UMLModel_MultiplicityElement, "isOrdered")
    descriptor = None
    for klass in UMLModel_MultiplicityElement.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_multiplicityelement_has_isUnique():
    assert hasattr(UMLModel_MultiplicityElement, "isUnique")
    descriptor = None
    for klass in UMLModel_MultiplicityElement.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_multiplicityelement_has_upper():
    assert hasattr(UMLModel_MultiplicityElement, "upper")
    descriptor = None
    for klass in UMLModel_MultiplicityElement.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_templateparametersubstitution_is_not_abstract():
    assert not inspect.isabstract(UMLModel_TemplateParameterSubstitution)


def test_umlmodel_templateparametersubstitution_constructor_exists():
    assert callable(UMLModel_TemplateParameterSubstitution.__init__)


def test_umlmodel_templateparametersubstitution_constructor_args():
    sig = inspect.signature(UMLModel_TemplateParameterSubstitution.__init__)
    params = list(sig.parameters.keys())
    assert "templateBinding" in params, "Missing parameter 'templateBinding'"
    assert "formal" in params, "Missing parameter 'formal'"
    assert "actual" in params, "Missing parameter 'actual'"

def test_umlmodel_templateparametersubstitution_has_templateBinding():
    assert hasattr(UMLModel_TemplateParameterSubstitution, "templateBinding")
    descriptor = None
    for klass in UMLModel_TemplateParameterSubstitution.__mro__:
        if "templateBinding" in klass.__dict__:
            descriptor = klass.__dict__["templateBinding"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_templateparametersubstitution_has_formal():
    assert hasattr(UMLModel_TemplateParameterSubstitution, "formal")
    descriptor = None
    for klass in UMLModel_TemplateParameterSubstitution.__mro__:
        if "formal" in klass.__dict__:
            descriptor = klass.__dict__["formal"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_templateparametersubstitution_has_actual():
    assert hasattr(UMLModel_TemplateParameterSubstitution, "actual")
    descriptor = None
    for klass in UMLModel_TemplateParameterSubstitution.__mro__:
        if "actual" in klass.__dict__:
            descriptor = klass.__dict__["actual"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_templateableelement_is_not_abstract():
    assert not inspect.isabstract(UMLModel_TemplateableElement)


def test_umlmodel_templateableelement_constructor_exists():
    assert callable(UMLModel_TemplateableElement.__init__)


def test_umlmodel_templateableelement_constructor_args():
    sig = inspect.signature(UMLModel_TemplateableElement.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_relationship_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Relationship)


def test_umlmodel_relationship_constructor_exists():
    assert callable(UMLModel_Relationship.__init__)


def test_umlmodel_relationship_constructor_args():
    sig = inspect.signature(UMLModel_Relationship.__init__)
    params = list(sig.parameters.keys())
    assert "relatedElement" in params, "Missing parameter 'relatedElement'"

def test_umlmodel_relationship_has_relatedElement():
    assert hasattr(UMLModel_Relationship, "relatedElement")
    descriptor = None
    for klass in UMLModel_Relationship.__mro__:
        if "relatedElement" in klass.__dict__:
            descriptor = klass.__dict__["relatedElement"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_exceptionhandler_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ExceptionHandler)


def test_umlmodel_exceptionhandler_constructor_exists():
    assert callable(UMLModel_ExceptionHandler.__init__)


def test_umlmodel_exceptionhandler_constructor_args():
    sig = inspect.signature(UMLModel_ExceptionHandler.__init__)
    params = list(sig.parameters.keys())
    assert "handlerBody" in params, "Missing parameter 'handlerBody'"
    assert "exceptionInput" in params, "Missing parameter 'exceptionInput'"
    assert "exceptionType" in params, "Missing parameter 'exceptionType'"
    assert "protectedNode" in params, "Missing parameter 'protectedNode'"

def test_umlmodel_exceptionhandler_has_handlerBody():
    assert hasattr(UMLModel_ExceptionHandler, "handlerBody")
    descriptor = None
    for klass in UMLModel_ExceptionHandler.__mro__:
        if "handlerBody" in klass.__dict__:
            descriptor = klass.__dict__["handlerBody"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_exceptionhandler_has_exceptionInput():
    assert hasattr(UMLModel_ExceptionHandler, "exceptionInput")
    descriptor = None
    for klass in UMLModel_ExceptionHandler.__mro__:
        if "exceptionInput" in klass.__dict__:
            descriptor = klass.__dict__["exceptionInput"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_exceptionhandler_has_exceptionType():
    assert hasattr(UMLModel_ExceptionHandler, "exceptionType")
    descriptor = None
    for klass in UMLModel_ExceptionHandler.__mro__:
        if "exceptionType" in klass.__dict__:
            descriptor = klass.__dict__["exceptionType"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_exceptionhandler_has_protectedNode():
    assert hasattr(UMLModel_ExceptionHandler, "protectedNode")
    descriptor = None
    for klass in UMLModel_ExceptionHandler.__mro__:
        if "protectedNode" in klass.__dict__:
            descriptor = klass.__dict__["protectedNode"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_namedelement_is_not_abstract():
    assert not inspect.isabstract(UMLModel_NamedElement)


def test_umlmodel_namedelement_constructor_exists():
    assert callable(UMLModel_NamedElement.__init__)


def test_umlmodel_namedelement_constructor_args():
    sig = inspect.signature(UMLModel_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "qualifiedName" in params, "Missing parameter 'qualifiedName'"
    assert "namespace" in params, "Missing parameter 'namespace'"
    assert "visibility" in params, "Missing parameter 'visibility'"
    assert "clientDependency" in params, "Missing parameter 'clientDependency'"
    assert "name" in params, "Missing parameter 'name'"

def test_umlmodel_namedelement_has_qualifiedName():
    assert hasattr(UMLModel_NamedElement, "qualifiedName")
    descriptor = None
    for klass in UMLModel_NamedElement.__mro__:
        if "qualifiedName" in klass.__dict__:
            descriptor = klass.__dict__["qualifiedName"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_namedelement_has_namespace():
    assert hasattr(UMLModel_NamedElement, "namespace")
    descriptor = None
    for klass in UMLModel_NamedElement.__mro__:
        if "namespace" in klass.__dict__:
            descriptor = klass.__dict__["namespace"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_namedelement_has_visibility():
    assert hasattr(UMLModel_NamedElement, "visibility")
    descriptor = None
    for klass in UMLModel_NamedElement.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_namedelement_has_clientDependency():
    assert hasattr(UMLModel_NamedElement, "clientDependency")
    descriptor = None
    for klass in UMLModel_NamedElement.__mro__:
        if "clientDependency" in klass.__dict__:
            descriptor = klass.__dict__["clientDependency"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_namedelement_has_name():
    assert hasattr(UMLModel_NamedElement, "name")
    descriptor = None
    for klass in UMLModel_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_qualifiervalue_is_not_abstract():
    assert not inspect.isabstract(UMLModel_QualifierValue)


def test_umlmodel_qualifiervalue_constructor_exists():
    assert callable(UMLModel_QualifierValue.__init__)


def test_umlmodel_qualifiervalue_constructor_args():
    sig = inspect.signature(UMLModel_QualifierValue.__init__)
    params = list(sig.parameters.keys())
    assert "qualifier" in params, "Missing parameter 'qualifier'"
    assert "value" in params, "Missing parameter 'value'"

def test_umlmodel_qualifiervalue_has_qualifier():
    assert hasattr(UMLModel_QualifierValue, "qualifier")
    descriptor = None
    for klass in UMLModel_QualifierValue.__mro__:
        if "qualifier" in klass.__dict__:
            descriptor = klass.__dict__["qualifier"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_qualifiervalue_has_value():
    assert hasattr(UMLModel_QualifierValue, "value")
    descriptor = None
    for klass in UMLModel_QualifierValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_templatesignature_is_not_abstract():
    assert not inspect.isabstract(UMLModel_TemplateSignature)


def test_umlmodel_templatesignature_constructor_exists():
    assert callable(UMLModel_TemplateSignature.__init__)


def test_umlmodel_templatesignature_constructor_args():
    sig = inspect.signature(UMLModel_TemplateSignature.__init__)
    params = list(sig.parameters.keys())
    assert "parameter" in params, "Missing parameter 'parameter'"
    assert "template" in params, "Missing parameter 'template'"

def test_umlmodel_templatesignature_has_parameter():
    assert hasattr(UMLModel_TemplateSignature, "parameter")
    descriptor = None
    for klass in UMLModel_TemplateSignature.__mro__:
        if "parameter" in klass.__dict__:
            descriptor = klass.__dict__["parameter"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_templatesignature_has_template():
    assert hasattr(UMLModel_TemplateSignature, "template")
    descriptor = None
    for klass in UMLModel_TemplateSignature.__mro__:
        if "template" in klass.__dict__:
            descriptor = klass.__dict__["template"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_image_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Image)


def test_umlmodel_image_constructor_exists():
    assert callable(UMLModel_Image.__init__)


def test_umlmodel_image_constructor_args():
    sig = inspect.signature(UMLModel_Image.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"
    assert "format" in params, "Missing parameter 'format'"
    assert "location" in params, "Missing parameter 'location'"

def test_umlmodel_image_has_content():
    assert hasattr(UMLModel_Image, "content")
    descriptor = None
    for klass in UMLModel_Image.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_image_has_format():
    assert hasattr(UMLModel_Image, "format")
    descriptor = None
    for klass in UMLModel_Image.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_image_has_location():
    assert hasattr(UMLModel_Image, "location")
    descriptor = None
    for klass in UMLModel_Image.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_finalnode_is_not_abstract():
    assert not inspect.isabstract(FinalNode)


def test_finalnode_constructor_exists():
    assert callable(FinalNode.__init__)


def test_finalnode_constructor_args():
    sig = inspect.signature(FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_flowfinalnode_is_not_abstract():
    assert not inspect.isabstract(UMLModel_FlowFinalNode)


def test_umlmodel_flowfinalnode_constructor_exists():
    assert callable(UMLModel_FlowFinalNode.__init__)


def test_umlmodel_flowfinalnode_constructor_args():
    sig = inspect.signature(UMLModel_FlowFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_activityfinalnode_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ActivityFinalNode)


def test_umlmodel_activityfinalnode_constructor_exists():
    assert callable(UMLModel_ActivityFinalNode.__init__)


def test_umlmodel_activityfinalnode_constructor_args():
    sig = inspect.signature(UMLModel_ActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_objectnode_is_not_abstract():
    assert not inspect.isabstract(ObjectNode)


def test_objectnode_constructor_exists():
    assert callable(ObjectNode.__init__)


def test_objectnode_constructor_args():
    sig = inspect.signature(ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_pin_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Pin)


def test_umlmodel_pin_constructor_exists():
    assert callable(UMLModel_Pin.__init__)


def test_umlmodel_pin_constructor_args():
    sig = inspect.signature(UMLModel_Pin.__init__)
    params = list(sig.parameters.keys())
    assert "isControl" in params, "Missing parameter 'isControl'"

def test_umlmodel_pin_has_isControl():
    assert hasattr(UMLModel_Pin, "isControl")
    descriptor = None
    for klass in UMLModel_Pin.__mro__:
        if "isControl" in klass.__dict__:
            descriptor = klass.__dict__["isControl"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_expansionnode_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ExpansionNode)


def test_umlmodel_expansionnode_constructor_exists():
    assert callable(UMLModel_ExpansionNode.__init__)


def test_umlmodel_expansionnode_constructor_args():
    sig = inspect.signature(UMLModel_ExpansionNode.__init__)
    params = list(sig.parameters.keys())
    assert "regionAsInput" in params, "Missing parameter 'regionAsInput'"
    assert "regionAsOutput" in params, "Missing parameter 'regionAsOutput'"

def test_umlmodel_expansionnode_has_regionAsInput():
    assert hasattr(UMLModel_ExpansionNode, "regionAsInput")
    descriptor = None
    for klass in UMLModel_ExpansionNode.__mro__:
        if "regionAsInput" in klass.__dict__:
            descriptor = klass.__dict__["regionAsInput"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_expansionnode_has_regionAsOutput():
    assert hasattr(UMLModel_ExpansionNode, "regionAsOutput")
    descriptor = None
    for klass in UMLModel_ExpansionNode.__mro__:
        if "regionAsOutput" in klass.__dict__:
            descriptor = klass.__dict__["regionAsOutput"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_activityparameternode_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ActivityParameterNode)


def test_umlmodel_activityparameternode_constructor_exists():
    assert callable(UMLModel_ActivityParameterNode.__init__)


def test_umlmodel_activityparameternode_constructor_args():
    sig = inspect.signature(UMLModel_ActivityParameterNode.__init__)
    params = list(sig.parameters.keys())
    assert "parameter" in params, "Missing parameter 'parameter'"

def test_umlmodel_activityparameternode_has_parameter():
    assert hasattr(UMLModel_ActivityParameterNode, "parameter")
    descriptor = None
    for klass in UMLModel_ActivityParameterNode.__mro__:
        if "parameter" in klass.__dict__:
            descriptor = klass.__dict__["parameter"]
            break
    assert isinstance(descriptor, property)



def test_redefinableelement_is_not_abstract():
    assert not inspect.isabstract(RedefinableElement)


def test_redefinableelement_constructor_exists():
    assert callable(RedefinableElement.__init__)


def test_redefinableelement_constructor_args():
    sig = inspect.signature(RedefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_extensionpoint_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ExtensionPoint)


def test_umlmodel_extensionpoint_constructor_exists():
    assert callable(UMLModel_ExtensionPoint.__init__)


def test_umlmodel_extensionpoint_constructor_args():
    sig = inspect.signature(UMLModel_ExtensionPoint.__init__)
    params = list(sig.parameters.keys())
    assert "useCase" in params, "Missing parameter 'useCase'"

def test_umlmodel_extensionpoint_has_useCase():
    assert hasattr(UMLModel_ExtensionPoint, "useCase")
    descriptor = None
    for klass in UMLModel_ExtensionPoint.__mro__:
        if "useCase" in klass.__dict__:
            descriptor = klass.__dict__["useCase"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_feature_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Feature)


def test_umlmodel_feature_constructor_exists():
    assert callable(UMLModel_Feature.__init__)


def test_umlmodel_feature_constructor_args():
    sig = inspect.signature(UMLModel_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "featuringClassifier" in params, "Missing parameter 'featuringClassifier'"
    assert "isStatic" in params, "Missing parameter 'isStatic'"

def test_umlmodel_feature_has_featuringClassifier():
    assert hasattr(UMLModel_Feature, "featuringClassifier")
    descriptor = None
    for klass in UMLModel_Feature.__mro__:
        if "featuringClassifier" in klass.__dict__:
            descriptor = klass.__dict__["featuringClassifier"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_feature_has_isStatic():
    assert hasattr(UMLModel_Feature, "isStatic")
    descriptor = None
    for klass in UMLModel_Feature.__mro__:
        if "isStatic" in klass.__dict__:
            descriptor = klass.__dict__["isStatic"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_redefinabletemplatesignature_is_not_abstract():
    assert not inspect.isabstract(UMLModel_RedefinableTemplateSignature)


def test_umlmodel_redefinabletemplatesignature_constructor_exists():
    assert callable(UMLModel_RedefinableTemplateSignature.__init__)


def test_umlmodel_redefinabletemplatesignature_constructor_args():
    sig = inspect.signature(UMLModel_RedefinableTemplateSignature.__init__)
    params = list(sig.parameters.keys())
    assert "extendedSignature" in params, "Missing parameter 'extendedSignature'"
    assert "inheritedParameter" in params, "Missing parameter 'inheritedParameter'"
    assert "classifier" in params, "Missing parameter 'classifier'"

def test_umlmodel_redefinabletemplatesignature_has_extendedSignature():
    assert hasattr(UMLModel_RedefinableTemplateSignature, "extendedSignature")
    descriptor = None
    for klass in UMLModel_RedefinableTemplateSignature.__mro__:
        if "extendedSignature" in klass.__dict__:
            descriptor = klass.__dict__["extendedSignature"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_redefinabletemplatesignature_has_inheritedParameter():
    assert hasattr(UMLModel_RedefinableTemplateSignature, "inheritedParameter")
    descriptor = None
    for klass in UMLModel_RedefinableTemplateSignature.__mro__:
        if "inheritedParameter" in klass.__dict__:
            descriptor = klass.__dict__["inheritedParameter"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_redefinabletemplatesignature_has_classifier():
    assert hasattr(UMLModel_RedefinableTemplateSignature, "classifier")
    descriptor = None
    for klass in UMLModel_RedefinableTemplateSignature.__mro__:
        if "classifier" in klass.__dict__:
            descriptor = klass.__dict__["classifier"]
            break
    assert isinstance(descriptor, property)



def test_activitygroup_is_not_abstract():
    assert not inspect.isabstract(ActivityGroup)


def test_activitygroup_constructor_exists():
    assert callable(ActivityGroup.__init__)


def test_activitygroup_constructor_args():
    sig = inspect.signature(ActivityGroup.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_interruptibleactivityregion_is_not_abstract():
    assert not inspect.isabstract(UMLModel_InterruptibleActivityRegion)


def test_umlmodel_interruptibleactivityregion_constructor_exists():
    assert callable(UMLModel_InterruptibleActivityRegion.__init__)


def test_umlmodel_interruptibleactivityregion_constructor_args():
    sig = inspect.signature(UMLModel_InterruptibleActivityRegion.__init__)
    params = list(sig.parameters.keys())
    assert "interruptingEdge" in params, "Missing parameter 'interruptingEdge'"
    assert "node" in params, "Missing parameter 'node'"

def test_umlmodel_interruptibleactivityregion_has_interruptingEdge():
    assert hasattr(UMLModel_InterruptibleActivityRegion, "interruptingEdge")
    descriptor = None
    for klass in UMLModel_InterruptibleActivityRegion.__mro__:
        if "interruptingEdge" in klass.__dict__:
            descriptor = klass.__dict__["interruptingEdge"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_interruptibleactivityregion_has_node():
    assert hasattr(UMLModel_InterruptibleActivityRegion, "node")
    descriptor = None
    for klass in UMLModel_InterruptibleActivityRegion.__mro__:
        if "node" in klass.__dict__:
            descriptor = klass.__dict__["node"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_vertex_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Vertex)


def test_umlmodel_vertex_constructor_exists():
    assert callable(UMLModel_Vertex.__init__)


def test_umlmodel_vertex_constructor_args():
    sig = inspect.signature(UMLModel_Vertex.__init__)
    params = list(sig.parameters.keys())
    assert "incoming" in params, "Missing parameter 'incoming'"
    assert "outgoing" in params, "Missing parameter 'outgoing'"
    assert "container" in params, "Missing parameter 'container'"

def test_umlmodel_vertex_has_incoming():
    assert hasattr(UMLModel_Vertex, "incoming")
    descriptor = None
    for klass in UMLModel_Vertex.__mro__:
        if "incoming" in klass.__dict__:
            descriptor = klass.__dict__["incoming"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_vertex_has_outgoing():
    assert hasattr(UMLModel_Vertex, "outgoing")
    descriptor = None
    for klass in UMLModel_Vertex.__mro__:
        if "outgoing" in klass.__dict__:
            descriptor = klass.__dict__["outgoing"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_vertex_has_container():
    assert hasattr(UMLModel_Vertex, "container")
    descriptor = None
    for klass in UMLModel_Vertex.__mro__:
        if "container" in klass.__dict__:
            descriptor = klass.__dict__["container"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_generalordering_is_not_abstract():
    assert not inspect.isabstract(UMLModel_GeneralOrdering)


def test_umlmodel_generalordering_constructor_exists():
    assert callable(UMLModel_GeneralOrdering.__init__)


def test_umlmodel_generalordering_constructor_args():
    sig = inspect.signature(UMLModel_GeneralOrdering.__init__)
    params = list(sig.parameters.keys())
    assert "before" in params, "Missing parameter 'before'"
    assert "after" in params, "Missing parameter 'after'"

def test_umlmodel_generalordering_has_before():
    assert hasattr(UMLModel_GeneralOrdering, "before")
    descriptor = None
    for klass in UMLModel_GeneralOrdering.__mro__:
        if "before" in klass.__dict__:
            descriptor = klass.__dict__["before"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_generalordering_has_after():
    assert hasattr(UMLModel_GeneralOrdering, "after")
    descriptor = None
    for klass in UMLModel_GeneralOrdering.__mro__:
        if "after" in klass.__dict__:
            descriptor = klass.__dict__["after"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_lifeline_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Lifeline)


def test_umlmodel_lifeline_constructor_exists():
    assert callable(UMLModel_Lifeline.__init__)


def test_umlmodel_lifeline_constructor_args():
    sig = inspect.signature(UMLModel_Lifeline.__init__)
    params = list(sig.parameters.keys())
    assert "decomposedAs" in params, "Missing parameter 'decomposedAs'"
    assert "interaction" in params, "Missing parameter 'interaction'"
    assert "represents" in params, "Missing parameter 'represents'"
    assert "coveredBy" in params, "Missing parameter 'coveredBy'"

def test_umlmodel_lifeline_has_decomposedAs():
    assert hasattr(UMLModel_Lifeline, "decomposedAs")
    descriptor = None
    for klass in UMLModel_Lifeline.__mro__:
        if "decomposedAs" in klass.__dict__:
            descriptor = klass.__dict__["decomposedAs"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_lifeline_has_interaction():
    assert hasattr(UMLModel_Lifeline, "interaction")
    descriptor = None
    for klass in UMLModel_Lifeline.__mro__:
        if "interaction" in klass.__dict__:
            descriptor = klass.__dict__["interaction"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_lifeline_has_represents():
    assert hasattr(UMLModel_Lifeline, "represents")
    descriptor = None
    for klass in UMLModel_Lifeline.__mro__:
        if "represents" in klass.__dict__:
            descriptor = klass.__dict__["represents"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_lifeline_has_coveredBy():
    assert hasattr(UMLModel_Lifeline, "coveredBy")
    descriptor = None
    for klass in UMLModel_Lifeline.__mro__:
        if "coveredBy" in klass.__dict__:
            descriptor = klass.__dict__["coveredBy"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_messageend_is_not_abstract():
    assert not inspect.isabstract(UMLModel_MessageEnd)


def test_umlmodel_messageend_constructor_exists():
    assert callable(UMLModel_MessageEnd.__init__)


def test_umlmodel_messageend_constructor_args():
    sig = inspect.signature(UMLModel_MessageEnd.__init__)
    params = list(sig.parameters.keys())
    assert "message" in params, "Missing parameter 'message'"

def test_umlmodel_messageend_has_message():
    assert hasattr(UMLModel_MessageEnd, "message")
    descriptor = None
    for klass in UMLModel_MessageEnd.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_message_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Message)


def test_umlmodel_message_constructor_exists():
    assert callable(UMLModel_Message.__init__)


def test_umlmodel_message_constructor_args():
    sig = inspect.signature(UMLModel_Message.__init__)
    params = list(sig.parameters.keys())
    assert "signature" in params, "Missing parameter 'signature'"
    assert "receiveEvent" in params, "Missing parameter 'receiveEvent'"
    assert "messageSort" in params, "Missing parameter 'messageSort'"
    assert "interaction" in params, "Missing parameter 'interaction'"
    assert "sendEvent" in params, "Missing parameter 'sendEvent'"
    assert "messageKind" in params, "Missing parameter 'messageKind'"
    assert "connector" in params, "Missing parameter 'connector'"

def test_umlmodel_message_has_signature():
    assert hasattr(UMLModel_Message, "signature")
    descriptor = None
    for klass in UMLModel_Message.__mro__:
        if "signature" in klass.__dict__:
            descriptor = klass.__dict__["signature"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_message_has_receiveEvent():
    assert hasattr(UMLModel_Message, "receiveEvent")
    descriptor = None
    for klass in UMLModel_Message.__mro__:
        if "receiveEvent" in klass.__dict__:
            descriptor = klass.__dict__["receiveEvent"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_message_has_messageSort():
    assert hasattr(UMLModel_Message, "messageSort")
    descriptor = None
    for klass in UMLModel_Message.__mro__:
        if "messageSort" in klass.__dict__:
            descriptor = klass.__dict__["messageSort"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_message_has_interaction():
    assert hasattr(UMLModel_Message, "interaction")
    descriptor = None
    for klass in UMLModel_Message.__mro__:
        if "interaction" in klass.__dict__:
            descriptor = klass.__dict__["interaction"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_message_has_sendEvent():
    assert hasattr(UMLModel_Message, "sendEvent")
    descriptor = None
    for klass in UMLModel_Message.__mro__:
        if "sendEvent" in klass.__dict__:
            descriptor = klass.__dict__["sendEvent"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_message_has_messageKind():
    assert hasattr(UMLModel_Message, "messageKind")
    descriptor = None
    for klass in UMLModel_Message.__mro__:
        if "messageKind" in klass.__dict__:
            descriptor = klass.__dict__["messageKind"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_message_has_connector():
    assert hasattr(UMLModel_Message, "connector")
    descriptor = None
    for klass in UMLModel_Message.__mro__:
        if "connector" in klass.__dict__:
            descriptor = klass.__dict__["connector"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_deploymenttarget_is_not_abstract():
    assert not inspect.isabstract(UMLModel_DeploymentTarget)


def test_umlmodel_deploymenttarget_constructor_exists():
    assert callable(UMLModel_DeploymentTarget.__init__)


def test_umlmodel_deploymenttarget_constructor_args():
    sig = inspect.signature(UMLModel_DeploymentTarget.__init__)
    params = list(sig.parameters.keys())
    assert "deployedElement" in params, "Missing parameter 'deployedElement'"

def test_umlmodel_deploymenttarget_has_deployedElement():
    assert hasattr(UMLModel_DeploymentTarget, "deployedElement")
    descriptor = None
    for klass in UMLModel_DeploymentTarget.__mro__:
        if "deployedElement" in klass.__dict__:
            descriptor = klass.__dict__["deployedElement"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_typedelement_is_not_abstract():
    assert not inspect.isabstract(UMLModel_TypedElement)


def test_umlmodel_typedelement_constructor_exists():
    assert callable(UMLModel_TypedElement.__init__)


def test_umlmodel_typedelement_constructor_args():
    sig = inspect.signature(UMLModel_TypedElement.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_umlmodel_typedelement_has_type():
    assert hasattr(UMLModel_TypedElement, "type")
    descriptor = None
    for klass in UMLModel_TypedElement.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_redefinableelement_is_not_abstract():
    assert not inspect.isabstract(UMLModel_RedefinableElement)


def test_umlmodel_redefinableelement_constructor_exists():
    assert callable(UMLModel_RedefinableElement.__init__)


def test_umlmodel_redefinableelement_constructor_args():
    sig = inspect.signature(UMLModel_RedefinableElement.__init__)
    params = list(sig.parameters.keys())
    assert "redefinitionContext" in params, "Missing parameter 'redefinitionContext'"
    assert "redefinedElement" in params, "Missing parameter 'redefinedElement'"
    assert "isLeaf" in params, "Missing parameter 'isLeaf'"

def test_umlmodel_redefinableelement_has_redefinitionContext():
    assert hasattr(UMLModel_RedefinableElement, "redefinitionContext")
    descriptor = None
    for klass in UMLModel_RedefinableElement.__mro__:
        if "redefinitionContext" in klass.__dict__:
            descriptor = klass.__dict__["redefinitionContext"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_redefinableelement_has_redefinedElement():
    assert hasattr(UMLModel_RedefinableElement, "redefinedElement")
    descriptor = None
    for klass in UMLModel_RedefinableElement.__mro__:
        if "redefinedElement" in klass.__dict__:
            descriptor = klass.__dict__["redefinedElement"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_redefinableelement_has_isLeaf():
    assert hasattr(UMLModel_RedefinableElement, "isLeaf")
    descriptor = None
    for klass in UMLModel_RedefinableElement.__mro__:
        if "isLeaf" in klass.__dict__:
            descriptor = klass.__dict__["isLeaf"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_include_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Include)


def test_umlmodel_include_constructor_exists():
    assert callable(UMLModel_Include.__init__)


def test_umlmodel_include_constructor_args():
    sig = inspect.signature(UMLModel_Include.__init__)
    params = list(sig.parameters.keys())
    assert "includingCase" in params, "Missing parameter 'includingCase'"
    assert "addition" in params, "Missing parameter 'addition'"

def test_umlmodel_include_has_includingCase():
    assert hasattr(UMLModel_Include, "includingCase")
    descriptor = None
    for klass in UMLModel_Include.__mro__:
        if "includingCase" in klass.__dict__:
            descriptor = klass.__dict__["includingCase"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_include_has_addition():
    assert hasattr(UMLModel_Include, "addition")
    descriptor = None
    for klass in UMLModel_Include.__mro__:
        if "addition" in klass.__dict__:
            descriptor = klass.__dict__["addition"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_extend_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Extend)


def test_umlmodel_extend_constructor_exists():
    assert callable(UMLModel_Extend.__init__)


def test_umlmodel_extend_constructor_args():
    sig = inspect.signature(UMLModel_Extend.__init__)
    params = list(sig.parameters.keys())
    assert "extension" in params, "Missing parameter 'extension'"
    assert "extensionLocation" in params, "Missing parameter 'extensionLocation'"
    assert "extendedCase" in params, "Missing parameter 'extendedCase'"

def test_umlmodel_extend_has_extension():
    assert hasattr(UMLModel_Extend, "extension")
    descriptor = None
    for klass in UMLModel_Extend.__mro__:
        if "extension" in klass.__dict__:
            descriptor = klass.__dict__["extension"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_extend_has_extensionLocation():
    assert hasattr(UMLModel_Extend, "extensionLocation")
    descriptor = None
    for klass in UMLModel_Extend.__mro__:
        if "extensionLocation" in klass.__dict__:
            descriptor = klass.__dict__["extensionLocation"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_extend_has_extendedCase():
    assert hasattr(UMLModel_Extend, "extendedCase")
    descriptor = None
    for klass in UMLModel_Extend.__mro__:
        if "extendedCase" in klass.__dict__:
            descriptor = klass.__dict__["extendedCase"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_interactionfragment_is_not_abstract():
    assert not inspect.isabstract(UMLModel_InteractionFragment)


def test_umlmodel_interactionfragment_constructor_exists():
    assert callable(UMLModel_InteractionFragment.__init__)


def test_umlmodel_interactionfragment_constructor_args():
    sig = inspect.signature(UMLModel_InteractionFragment.__init__)
    params = list(sig.parameters.keys())
    assert "enclosingInteraction" in params, "Missing parameter 'enclosingInteraction'"
    assert "covered" in params, "Missing parameter 'covered'"
    assert "enclosingOperand" in params, "Missing parameter 'enclosingOperand'"

def test_umlmodel_interactionfragment_has_enclosingInteraction():
    assert hasattr(UMLModel_InteractionFragment, "enclosingInteraction")
    descriptor = None
    for klass in UMLModel_InteractionFragment.__mro__:
        if "enclosingInteraction" in klass.__dict__:
            descriptor = klass.__dict__["enclosingInteraction"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_interactionfragment_has_covered():
    assert hasattr(UMLModel_InteractionFragment, "covered")
    descriptor = None
    for klass in UMLModel_InteractionFragment.__mro__:
        if "covered" in klass.__dict__:
            descriptor = klass.__dict__["covered"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_interactionfragment_has_enclosingOperand():
    assert hasattr(UMLModel_InteractionFragment, "enclosingOperand")
    descriptor = None
    for klass in UMLModel_InteractionFragment.__mro__:
        if "enclosingOperand" in klass.__dict__:
            descriptor = klass.__dict__["enclosingOperand"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_namespace_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Namespace)


def test_umlmodel_namespace_constructor_exists():
    assert callable(UMLModel_Namespace.__init__)


def test_umlmodel_namespace_constructor_args():
    sig = inspect.signature(UMLModel_Namespace.__init__)
    params = list(sig.parameters.keys())
    assert "importedMember" in params, "Missing parameter 'importedMember'"
    assert "member" in params, "Missing parameter 'member'"
    assert "ownedMember" in params, "Missing parameter 'ownedMember'"

def test_umlmodel_namespace_has_importedMember():
    assert hasattr(UMLModel_Namespace, "importedMember")
    descriptor = None
    for klass in UMLModel_Namespace.__mro__:
        if "importedMember" in klass.__dict__:
            descriptor = klass.__dict__["importedMember"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_namespace_has_member():
    assert hasattr(UMLModel_Namespace, "member")
    descriptor = None
    for klass in UMLModel_Namespace.__mro__:
        if "member" in klass.__dict__:
            descriptor = klass.__dict__["member"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_namespace_has_ownedMember():
    assert hasattr(UMLModel_Namespace, "ownedMember")
    descriptor = None
    for klass in UMLModel_Namespace.__mro__:
        if "ownedMember" in klass.__dict__:
            descriptor = klass.__dict__["ownedMember"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_deployedartifact_is_not_abstract():
    assert not inspect.isabstract(UMLModel_DeployedArtifact)


def test_umlmodel_deployedartifact_constructor_exists():
    assert callable(UMLModel_DeployedArtifact.__init__)


def test_umlmodel_deployedartifact_constructor_args():
    sig = inspect.signature(UMLModel_DeployedArtifact.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_activitypartition_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ActivityPartition)


def test_umlmodel_activitypartition_constructor_exists():
    assert callable(UMLModel_ActivityPartition.__init__)


def test_umlmodel_activitypartition_constructor_args():
    sig = inspect.signature(UMLModel_ActivityPartition.__init__)
    params = list(sig.parameters.keys())
    assert "isDimension" in params, "Missing parameter 'isDimension'"
    assert "superPartition" in params, "Missing parameter 'superPartition'"
    assert "node" in params, "Missing parameter 'node'"
    assert "isExternal" in params, "Missing parameter 'isExternal'"
    assert "represents" in params, "Missing parameter 'represents'"
    assert "subpartition" in params, "Missing parameter 'subpartition'"
    assert "edge" in params, "Missing parameter 'edge'"

def test_umlmodel_activitypartition_has_isDimension():
    assert hasattr(UMLModel_ActivityPartition, "isDimension")
    descriptor = None
    for klass in UMLModel_ActivityPartition.__mro__:
        if "isDimension" in klass.__dict__:
            descriptor = klass.__dict__["isDimension"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_activitypartition_has_superPartition():
    assert hasattr(UMLModel_ActivityPartition, "superPartition")
    descriptor = None
    for klass in UMLModel_ActivityPartition.__mro__:
        if "superPartition" in klass.__dict__:
            descriptor = klass.__dict__["superPartition"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_activitypartition_has_node():
    assert hasattr(UMLModel_ActivityPartition, "node")
    descriptor = None
    for klass in UMLModel_ActivityPartition.__mro__:
        if "node" in klass.__dict__:
            descriptor = klass.__dict__["node"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_activitypartition_has_isExternal():
    assert hasattr(UMLModel_ActivityPartition, "isExternal")
    descriptor = None
    for klass in UMLModel_ActivityPartition.__mro__:
        if "isExternal" in klass.__dict__:
            descriptor = klass.__dict__["isExternal"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_activitypartition_has_represents():
    assert hasattr(UMLModel_ActivityPartition, "represents")
    descriptor = None
    for klass in UMLModel_ActivityPartition.__mro__:
        if "represents" in klass.__dict__:
            descriptor = klass.__dict__["represents"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_activitypartition_has_subpartition():
    assert hasattr(UMLModel_ActivityPartition, "subpartition")
    descriptor = None
    for klass in UMLModel_ActivityPartition.__mro__:
        if "subpartition" in klass.__dict__:
            descriptor = klass.__dict__["subpartition"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_activitypartition_has_edge():
    assert hasattr(UMLModel_ActivityPartition, "edge")
    descriptor = None
    for klass in UMLModel_ActivityPartition.__mro__:
        if "edge" in klass.__dict__:
            descriptor = klass.__dict__["edge"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_activitynode_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ActivityNode)


def test_umlmodel_activitynode_constructor_exists():
    assert callable(UMLModel_ActivityNode.__init__)


def test_umlmodel_activitynode_constructor_args():
    sig = inspect.signature(UMLModel_ActivityNode.__init__)
    params = list(sig.parameters.keys())
    assert "inGroup" in params, "Missing parameter 'inGroup'"
    assert "incoming" in params, "Missing parameter 'incoming'"
    assert "inPartition" in params, "Missing parameter 'inPartition'"
    assert "activity" in params, "Missing parameter 'activity'"
    assert "outgoing" in params, "Missing parameter 'outgoing'"
    assert "redefinedNode" in params, "Missing parameter 'redefinedNode'"
    assert "inStructuredNode" in params, "Missing parameter 'inStructuredNode'"
    assert "inInterruptibleRegion" in params, "Missing parameter 'inInterruptibleRegion'"

def test_umlmodel_activitynode_has_inGroup():
    assert hasattr(UMLModel_ActivityNode, "inGroup")
    descriptor = None
    for klass in UMLModel_ActivityNode.__mro__:
        if "inGroup" in klass.__dict__:
            descriptor = klass.__dict__["inGroup"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_activitynode_has_incoming():
    assert hasattr(UMLModel_ActivityNode, "incoming")
    descriptor = None
    for klass in UMLModel_ActivityNode.__mro__:
        if "incoming" in klass.__dict__:
            descriptor = klass.__dict__["incoming"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_activitynode_has_inPartition():
    assert hasattr(UMLModel_ActivityNode, "inPartition")
    descriptor = None
    for klass in UMLModel_ActivityNode.__mro__:
        if "inPartition" in klass.__dict__:
            descriptor = klass.__dict__["inPartition"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_activitynode_has_activity():
    assert hasattr(UMLModel_ActivityNode, "activity")
    descriptor = None
    for klass in UMLModel_ActivityNode.__mro__:
        if "activity" in klass.__dict__:
            descriptor = klass.__dict__["activity"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_activitynode_has_outgoing():
    assert hasattr(UMLModel_ActivityNode, "outgoing")
    descriptor = None
    for klass in UMLModel_ActivityNode.__mro__:
        if "outgoing" in klass.__dict__:
            descriptor = klass.__dict__["outgoing"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_activitynode_has_redefinedNode():
    assert hasattr(UMLModel_ActivityNode, "redefinedNode")
    descriptor = None
    for klass in UMLModel_ActivityNode.__mro__:
        if "redefinedNode" in klass.__dict__:
            descriptor = klass.__dict__["redefinedNode"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_activitynode_has_inStructuredNode():
    assert hasattr(UMLModel_ActivityNode, "inStructuredNode")
    descriptor = None
    for klass in UMLModel_ActivityNode.__mro__:
        if "inStructuredNode" in klass.__dict__:
            descriptor = klass.__dict__["inStructuredNode"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_activitynode_has_inInterruptibleRegion():
    assert hasattr(UMLModel_ActivityNode, "inInterruptibleRegion")
    descriptor = None
    for klass in UMLModel_ActivityNode.__mro__:
        if "inInterruptibleRegion" in klass.__dict__:
            descriptor = klass.__dict__["inInterruptibleRegion"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_variable_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Variable)


def test_umlmodel_variable_constructor_exists():
    assert callable(UMLModel_Variable.__init__)


def test_umlmodel_variable_constructor_args():
    sig = inspect.signature(UMLModel_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "scope" in params, "Missing parameter 'scope'"
    assert "activityScope" in params, "Missing parameter 'activityScope'"

def test_umlmodel_variable_has_scope():
    assert hasattr(UMLModel_Variable, "scope")
    descriptor = None
    for klass in UMLModel_Variable.__mro__:
        if "scope" in klass.__dict__:
            descriptor = klass.__dict__["scope"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_variable_has_activityScope():
    assert hasattr(UMLModel_Variable, "activityScope")
    descriptor = None
    for klass in UMLModel_Variable.__mro__:
        if "activityScope" in klass.__dict__:
            descriptor = klass.__dict__["activityScope"]
            break
    assert isinstance(descriptor, property)



def test_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_opaquebehavior_is_not_abstract():
    assert not inspect.isabstract(UMLModel_OpaqueBehavior)


def test_umlmodel_opaquebehavior_constructor_exists():
    assert callable(UMLModel_OpaqueBehavior.__init__)


def test_umlmodel_opaquebehavior_constructor_args():
    sig = inspect.signature(UMLModel_OpaqueBehavior.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "language" in params, "Missing parameter 'language'"

def test_umlmodel_opaquebehavior_has_body():
    assert hasattr(UMLModel_OpaqueBehavior, "body")
    descriptor = None
    for klass in UMLModel_OpaqueBehavior.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_opaquebehavior_has_language():
    assert hasattr(UMLModel_OpaqueBehavior, "language")
    descriptor = None
    for klass in UMLModel_OpaqueBehavior.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_statemachine_is_not_abstract():
    assert not inspect.isabstract(UMLModel_StateMachine)


def test_umlmodel_statemachine_constructor_exists():
    assert callable(UMLModel_StateMachine.__init__)


def test_umlmodel_statemachine_constructor_args():
    sig = inspect.signature(UMLModel_StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "submachineState" in params, "Missing parameter 'submachineState'"
    assert "extendedStateMachine" in params, "Missing parameter 'extendedStateMachine'"

def test_umlmodel_statemachine_has_submachineState():
    assert hasattr(UMLModel_StateMachine, "submachineState")
    descriptor = None
    for klass in UMLModel_StateMachine.__mro__:
        if "submachineState" in klass.__dict__:
            descriptor = klass.__dict__["submachineState"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_statemachine_has_extendedStateMachine():
    assert hasattr(UMLModel_StateMachine, "extendedStateMachine")
    descriptor = None
    for klass in UMLModel_StateMachine.__mro__:
        if "extendedStateMachine" in klass.__dict__:
            descriptor = klass.__dict__["extendedStateMachine"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_activity_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Activity)


def test_umlmodel_activity_constructor_exists():
    assert callable(UMLModel_Activity.__init__)


def test_umlmodel_activity_constructor_args():
    sig = inspect.signature(UMLModel_Activity.__init__)
    params = list(sig.parameters.keys())
    assert "isSingleExecution" in params, "Missing parameter 'isSingleExecution'"
    assert "structuredNode" in params, "Missing parameter 'structuredNode'"
    assert "partition" in params, "Missing parameter 'partition'"
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"

def test_umlmodel_activity_has_isSingleExecution():
    assert hasattr(UMLModel_Activity, "isSingleExecution")
    descriptor = None
    for klass in UMLModel_Activity.__mro__:
        if "isSingleExecution" in klass.__dict__:
            descriptor = klass.__dict__["isSingleExecution"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_activity_has_structuredNode():
    assert hasattr(UMLModel_Activity, "structuredNode")
    descriptor = None
    for klass in UMLModel_Activity.__mro__:
        if "structuredNode" in klass.__dict__:
            descriptor = klass.__dict__["structuredNode"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_activity_has_partition():
    assert hasattr(UMLModel_Activity, "partition")
    descriptor = None
    for klass in UMLModel_Activity.__mro__:
        if "partition" in klass.__dict__:
            descriptor = klass.__dict__["partition"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_activity_has_isReadOnly():
    assert hasattr(UMLModel_Activity, "isReadOnly")
    descriptor = None
    for klass in UMLModel_Activity.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)



def test_inputpin_is_not_abstract():
    assert not inspect.isabstract(InputPin)


def test_inputpin_constructor_exists():
    assert callable(InputPin.__init__)


def test_inputpin_constructor_args():
    sig = inspect.signature(InputPin.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_valuepin_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ValuePin)


def test_umlmodel_valuepin_constructor_exists():
    assert callable(UMLModel_ValuePin.__init__)


def test_umlmodel_valuepin_constructor_args():
    sig = inspect.signature(UMLModel_ValuePin.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_actioninputpin_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ActionInputPin)


def test_umlmodel_actioninputpin_constructor_exists():
    assert callable(UMLModel_ActionInputPin.__init__)


def test_umlmodel_actioninputpin_constructor_args():
    sig = inspect.signature(UMLModel_ActionInputPin.__init__)
    params = list(sig.parameters.keys())



def test_executionspecification_is_not_abstract():
    assert not inspect.isabstract(ExecutionSpecification)


def test_executionspecification_constructor_exists():
    assert callable(ExecutionSpecification.__init__)


def test_executionspecification_constructor_args():
    sig = inspect.signature(ExecutionSpecification.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_actionexecutionspecification_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ActionExecutionSpecification)


def test_umlmodel_actionexecutionspecification_constructor_exists():
    assert callable(UMLModel_ActionExecutionSpecification.__init__)


def test_umlmodel_actionexecutionspecification_constructor_args():
    sig = inspect.signature(UMLModel_ActionExecutionSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"

def test_umlmodel_actionexecutionspecification_has_action():
    assert hasattr(UMLModel_ActionExecutionSpecification, "action")
    descriptor = None
    for klass in UMLModel_ActionExecutionSpecification.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_activitygroup_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ActivityGroup)


def test_umlmodel_activitygroup_constructor_exists():
    assert callable(UMLModel_ActivityGroup.__init__)


def test_umlmodel_activitygroup_constructor_args():
    sig = inspect.signature(UMLModel_ActivityGroup.__init__)
    params = list(sig.parameters.keys())
    assert "subgroup" in params, "Missing parameter 'subgroup'"
    assert "inActivity" in params, "Missing parameter 'inActivity'"
    assert "superGroup" in params, "Missing parameter 'superGroup'"

def test_umlmodel_activitygroup_has_subgroup():
    assert hasattr(UMLModel_ActivityGroup, "subgroup")
    descriptor = None
    for klass in UMLModel_ActivityGroup.__mro__:
        if "subgroup" in klass.__dict__:
            descriptor = klass.__dict__["subgroup"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_activitygroup_has_inActivity():
    assert hasattr(UMLModel_ActivityGroup, "inActivity")
    descriptor = None
    for klass in UMLModel_ActivityGroup.__mro__:
        if "inActivity" in klass.__dict__:
            descriptor = klass.__dict__["inActivity"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_activitygroup_has_superGroup():
    assert hasattr(UMLModel_ActivityGroup, "superGroup")
    descriptor = None
    for klass in UMLModel_ActivityGroup.__mro__:
        if "superGroup" in klass.__dict__:
            descriptor = klass.__dict__["superGroup"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_activityedge_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ActivityEdge)


def test_umlmodel_activityedge_constructor_exists():
    assert callable(UMLModel_ActivityEdge.__init__)


def test_umlmodel_activityedge_constructor_args():
    sig = inspect.signature(UMLModel_ActivityEdge.__init__)
    params = list(sig.parameters.keys())
    assert "target" in params, "Missing parameter 'target'"
    assert "activity" in params, "Missing parameter 'activity'"
    assert "inStructuredNode" in params, "Missing parameter 'inStructuredNode'"
    assert "inGroup" in params, "Missing parameter 'inGroup'"
    assert "interrupts" in params, "Missing parameter 'interrupts'"
    assert "source" in params, "Missing parameter 'source'"
    assert "inPartition" in params, "Missing parameter 'inPartition'"
    assert "redefinedEdge" in params, "Missing parameter 'redefinedEdge'"

def test_umlmodel_activityedge_has_target():
    assert hasattr(UMLModel_ActivityEdge, "target")
    descriptor = None
    for klass in UMLModel_ActivityEdge.__mro__:
        if "target" in klass.__dict__:
            descriptor = klass.__dict__["target"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_activityedge_has_activity():
    assert hasattr(UMLModel_ActivityEdge, "activity")
    descriptor = None
    for klass in UMLModel_ActivityEdge.__mro__:
        if "activity" in klass.__dict__:
            descriptor = klass.__dict__["activity"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_activityedge_has_inStructuredNode():
    assert hasattr(UMLModel_ActivityEdge, "inStructuredNode")
    descriptor = None
    for klass in UMLModel_ActivityEdge.__mro__:
        if "inStructuredNode" in klass.__dict__:
            descriptor = klass.__dict__["inStructuredNode"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_activityedge_has_inGroup():
    assert hasattr(UMLModel_ActivityEdge, "inGroup")
    descriptor = None
    for klass in UMLModel_ActivityEdge.__mro__:
        if "inGroup" in klass.__dict__:
            descriptor = klass.__dict__["inGroup"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_activityedge_has_interrupts():
    assert hasattr(UMLModel_ActivityEdge, "interrupts")
    descriptor = None
    for klass in UMLModel_ActivityEdge.__mro__:
        if "interrupts" in klass.__dict__:
            descriptor = klass.__dict__["interrupts"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_activityedge_has_source():
    assert hasattr(UMLModel_ActivityEdge, "source")
    descriptor = None
    for klass in UMLModel_ActivityEdge.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_activityedge_has_inPartition():
    assert hasattr(UMLModel_ActivityEdge, "inPartition")
    descriptor = None
    for klass in UMLModel_ActivityEdge.__mro__:
        if "inPartition" in klass.__dict__:
            descriptor = klass.__dict__["inPartition"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_activityedge_has_redefinedEdge():
    assert hasattr(UMLModel_ActivityEdge, "redefinedEdge")
    descriptor = None
    for klass in UMLModel_ActivityEdge.__mro__:
        if "redefinedEdge" in klass.__dict__:
            descriptor = klass.__dict__["redefinedEdge"]
            break
    assert isinstance(descriptor, property)



def test_accepteventaction_is_not_abstract():
    assert not inspect.isabstract(AcceptEventAction)


def test_accepteventaction_constructor_exists():
    assert callable(AcceptEventAction.__init__)


def test_accepteventaction_constructor_args():
    sig = inspect.signature(AcceptEventAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_acceptcallaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel_AcceptCallAction)


def test_umlmodel_acceptcallaction_constructor_exists():
    assert callable(UMLModel_AcceptCallAction.__init__)


def test_umlmodel_acceptcallaction_constructor_args():
    sig = inspect.signature(UMLModel_AcceptCallAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(UMLModel_OpaqueExpression)


def test_umlmodel_opaqueexpression_constructor_exists():
    assert callable(UMLModel_OpaqueExpression.__init__)


def test_umlmodel_opaqueexpression_constructor_args():
    sig = inspect.signature(UMLModel_OpaqueExpression.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "result" in params, "Missing parameter 'result'"
    assert "behavior" in params, "Missing parameter 'behavior'"
    assert "language" in params, "Missing parameter 'language'"

def test_umlmodel_opaqueexpression_has_body():
    assert hasattr(UMLModel_OpaqueExpression, "body")
    descriptor = None
    for klass in UMLModel_OpaqueExpression.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_opaqueexpression_has_result():
    assert hasattr(UMLModel_OpaqueExpression, "result")
    descriptor = None
    for klass in UMLModel_OpaqueExpression.__mro__:
        if "result" in klass.__dict__:
            descriptor = klass.__dict__["result"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_opaqueexpression_has_behavior():
    assert hasattr(UMLModel_OpaqueExpression, "behavior")
    descriptor = None
    for klass in UMLModel_OpaqueExpression.__mro__:
        if "behavior" in klass.__dict__:
            descriptor = klass.__dict__["behavior"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_opaqueexpression_has_language():
    assert hasattr(UMLModel_OpaqueExpression, "language")
    descriptor = None
    for klass in UMLModel_OpaqueExpression.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_dependency_is_not_abstract():
    assert not inspect.isabstract(Dependency)


def test_dependency_constructor_exists():
    assert callable(Dependency.__init__)


def test_dependency_constructor_args():
    sig = inspect.signature(Dependency.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_usage_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Usage)


def test_umlmodel_usage_constructor_exists():
    assert callable(UMLModel_Usage.__init__)


def test_umlmodel_usage_constructor_args():
    sig = inspect.signature(UMLModel_Usage.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_deployment_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Deployment)


def test_umlmodel_deployment_constructor_exists():
    assert callable(UMLModel_Deployment.__init__)


def test_umlmodel_deployment_constructor_args():
    sig = inspect.signature(UMLModel_Deployment.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "deployedArtifact" in params, "Missing parameter 'deployedArtifact'"

def test_umlmodel_deployment_has_location():
    assert hasattr(UMLModel_Deployment, "location")
    descriptor = None
    for klass in UMLModel_Deployment.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_deployment_has_deployedArtifact():
    assert hasattr(UMLModel_Deployment, "deployedArtifact")
    descriptor = None
    for klass in UMLModel_Deployment.__mro__:
        if "deployedArtifact" in klass.__dict__:
            descriptor = klass.__dict__["deployedArtifact"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_abstraction_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Abstraction)


def test_umlmodel_abstraction_constructor_exists():
    assert callable(UMLModel_Abstraction.__init__)


def test_umlmodel_abstraction_constructor_args():
    sig = inspect.signature(UMLModel_Abstraction.__init__)
    params = list(sig.parameters.keys())



def test_executablenode_is_not_abstract():
    assert not inspect.isabstract(ExecutableNode)


def test_executablenode_constructor_exists():
    assert callable(ExecutableNode.__init__)


def test_executablenode_constructor_args():
    sig = inspect.signature(ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_action_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Action)


def test_umlmodel_action_constructor_exists():
    assert callable(UMLModel_Action.__init__)


def test_umlmodel_action_constructor_args():
    sig = inspect.signature(UMLModel_Action.__init__)
    params = list(sig.parameters.keys())
    assert "input" in params, "Missing parameter 'input'"
    assert "context" in params, "Missing parameter 'context'"
    assert "output" in params, "Missing parameter 'output'"

def test_umlmodel_action_has_input():
    assert hasattr(UMLModel_Action, "input")
    descriptor = None
    for klass in UMLModel_Action.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_action_has_context():
    assert hasattr(UMLModel_Action, "context")
    descriptor = None
    for klass in UMLModel_Action.__mro__:
        if "context" in klass.__dict__:
            descriptor = klass.__dict__["context"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_action_has_output():
    assert hasattr(UMLModel_Action, "output")
    descriptor = None
    for klass in UMLModel_Action.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_trigger_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Trigger)


def test_umlmodel_trigger_constructor_exists():
    assert callable(UMLModel_Trigger.__init__)


def test_umlmodel_trigger_constructor_args():
    sig = inspect.signature(UMLModel_Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"
    assert "port" in params, "Missing parameter 'port'"

def test_umlmodel_trigger_has_event():
    assert hasattr(UMLModel_Trigger, "event")
    descriptor = None
    for klass in UMLModel_Trigger.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_trigger_has_port():
    assert hasattr(UMLModel_Trigger, "port")
    descriptor = None
    for klass in UMLModel_Trigger.__mro__:
        if "port" in klass.__dict__:
            descriptor = klass.__dict__["port"]
            break
    assert isinstance(descriptor, property)



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_reduceaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ReduceAction)


def test_umlmodel_reduceaction_constructor_exists():
    assert callable(UMLModel_ReduceAction.__init__)


def test_umlmodel_reduceaction_constructor_args():
    sig = inspect.signature(UMLModel_ReduceAction.__init__)
    params = list(sig.parameters.keys())
    assert "reducer" in params, "Missing parameter 'reducer'"
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"

def test_umlmodel_reduceaction_has_reducer():
    assert hasattr(UMLModel_ReduceAction, "reducer")
    descriptor = None
    for klass in UMLModel_ReduceAction.__mro__:
        if "reducer" in klass.__dict__:
            descriptor = klass.__dict__["reducer"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_reduceaction_has_isOrdered():
    assert hasattr(UMLModel_ReduceAction, "isOrdered")
    descriptor = None
    for klass in UMLModel_ReduceAction.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_raiseexceptionaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel_RaiseExceptionAction)


def test_umlmodel_raiseexceptionaction_constructor_exists():
    assert callable(UMLModel_RaiseExceptionAction.__init__)


def test_umlmodel_raiseexceptionaction_constructor_args():
    sig = inspect.signature(UMLModel_RaiseExceptionAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_readselfaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ReadSelfAction)


def test_umlmodel_readselfaction_constructor_exists():
    assert callable(UMLModel_ReadSelfAction.__init__)


def test_umlmodel_readselfaction_constructor_args():
    sig = inspect.signature(UMLModel_ReadSelfAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_destroyobjectaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel_DestroyObjectAction)


def test_umlmodel_destroyobjectaction_constructor_exists():
    assert callable(UMLModel_DestroyObjectAction.__init__)


def test_umlmodel_destroyobjectaction_constructor_args():
    sig = inspect.signature(UMLModel_DestroyObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "isDestroyLinks" in params, "Missing parameter 'isDestroyLinks'"
    assert "isDestroyOwnedObjects" in params, "Missing parameter 'isDestroyOwnedObjects'"

def test_umlmodel_destroyobjectaction_has_isDestroyLinks():
    assert hasattr(UMLModel_DestroyObjectAction, "isDestroyLinks")
    descriptor = None
    for klass in UMLModel_DestroyObjectAction.__mro__:
        if "isDestroyLinks" in klass.__dict__:
            descriptor = klass.__dict__["isDestroyLinks"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_destroyobjectaction_has_isDestroyOwnedObjects():
    assert hasattr(UMLModel_DestroyObjectAction, "isDestroyOwnedObjects")
    descriptor = None
    for klass in UMLModel_DestroyObjectAction.__mro__:
        if "isDestroyOwnedObjects" in klass.__dict__:
            descriptor = klass.__dict__["isDestroyOwnedObjects"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel_StructuralFeatureAction)


def test_umlmodel_structuralfeatureaction_constructor_exists():
    assert callable(UMLModel_StructuralFeatureAction.__init__)


def test_umlmodel_structuralfeatureaction_constructor_args():
    sig = inspect.signature(UMLModel_StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())
    assert "structuralFeature" in params, "Missing parameter 'structuralFeature'"

def test_umlmodel_structuralfeatureaction_has_structuralFeature():
    assert hasattr(UMLModel_StructuralFeatureAction, "structuralFeature")
    descriptor = None
    for klass in UMLModel_StructuralFeatureAction.__mro__:
        if "structuralFeature" in klass.__dict__:
            descriptor = klass.__dict__["structuralFeature"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_testidentityaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel_TestIdentityAction)


def test_umlmodel_testidentityaction_constructor_exists():
    assert callable(UMLModel_TestIdentityAction.__init__)


def test_umlmodel_testidentityaction_constructor_args():
    sig = inspect.signature(UMLModel_TestIdentityAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_readisclassifiedobjectaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ReadIsClassifiedObjectAction)


def test_umlmodel_readisclassifiedobjectaction_constructor_exists():
    assert callable(UMLModel_ReadIsClassifiedObjectAction.__init__)


def test_umlmodel_readisclassifiedobjectaction_constructor_args():
    sig = inspect.signature(UMLModel_ReadIsClassifiedObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "isDirect" in params, "Missing parameter 'isDirect'"
    assert "classifier" in params, "Missing parameter 'classifier'"

def test_umlmodel_readisclassifiedobjectaction_has_isDirect():
    assert hasattr(UMLModel_ReadIsClassifiedObjectAction, "isDirect")
    descriptor = None
    for klass in UMLModel_ReadIsClassifiedObjectAction.__mro__:
        if "isDirect" in klass.__dict__:
            descriptor = klass.__dict__["isDirect"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_readisclassifiedobjectaction_has_classifier():
    assert hasattr(UMLModel_ReadIsClassifiedObjectAction, "classifier")
    descriptor = None
    for klass in UMLModel_ReadIsClassifiedObjectAction.__mro__:
        if "classifier" in klass.__dict__:
            descriptor = klass.__dict__["classifier"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_readextentaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ReadExtentAction)


def test_umlmodel_readextentaction_constructor_exists():
    assert callable(UMLModel_ReadExtentAction.__init__)


def test_umlmodel_readextentaction_constructor_args():
    sig = inspect.signature(UMLModel_ReadExtentAction.__init__)
    params = list(sig.parameters.keys())
    assert "classifier" in params, "Missing parameter 'classifier'"

def test_umlmodel_readextentaction_has_classifier():
    assert hasattr(UMLModel_ReadExtentAction, "classifier")
    descriptor = None
    for klass in UMLModel_ReadExtentAction.__mro__:
        if "classifier" in klass.__dict__:
            descriptor = klass.__dict__["classifier"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_startclassifierbehavioraction_is_not_abstract():
    assert not inspect.isabstract(UMLModel_StartClassifierBehaviorAction)


def test_umlmodel_startclassifierbehavioraction_constructor_exists():
    assert callable(UMLModel_StartClassifierBehaviorAction.__init__)


def test_umlmodel_startclassifierbehavioraction_constructor_args():
    sig = inspect.signature(UMLModel_StartClassifierBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_opaqueaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel_OpaqueAction)


def test_umlmodel_opaqueaction_constructor_exists():
    assert callable(UMLModel_OpaqueAction.__init__)


def test_umlmodel_opaqueaction_constructor_args():
    sig = inspect.signature(UMLModel_OpaqueAction.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "language" in params, "Missing parameter 'language'"

def test_umlmodel_opaqueaction_has_body():
    assert hasattr(UMLModel_OpaqueAction, "body")
    descriptor = None
    for klass in UMLModel_OpaqueAction.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_opaqueaction_has_language():
    assert hasattr(UMLModel_OpaqueAction, "language")
    descriptor = None
    for klass in UMLModel_OpaqueAction.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_linkaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel_LinkAction)


def test_umlmodel_linkaction_constructor_exists():
    assert callable(UMLModel_LinkAction.__init__)


def test_umlmodel_linkaction_constructor_args():
    sig = inspect.signature(UMLModel_LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_invocationaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel_InvocationAction)


def test_umlmodel_invocationaction_constructor_exists():
    assert callable(UMLModel_InvocationAction.__init__)


def test_umlmodel_invocationaction_constructor_args():
    sig = inspect.signature(UMLModel_InvocationAction.__init__)
    params = list(sig.parameters.keys())
    assert "onPort" in params, "Missing parameter 'onPort'"

def test_umlmodel_invocationaction_has_onPort():
    assert hasattr(UMLModel_InvocationAction, "onPort")
    descriptor = None
    for klass in UMLModel_InvocationAction.__mro__:
        if "onPort" in klass.__dict__:
            descriptor = klass.__dict__["onPort"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_valuespecificationaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ValueSpecificationAction)


def test_umlmodel_valuespecificationaction_constructor_exists():
    assert callable(UMLModel_ValueSpecificationAction.__init__)


def test_umlmodel_valuespecificationaction_constructor_args():
    sig = inspect.signature(UMLModel_ValueSpecificationAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_unmarshallaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel_UnmarshallAction)


def test_umlmodel_unmarshallaction_constructor_exists():
    assert callable(UMLModel_UnmarshallAction.__init__)


def test_umlmodel_unmarshallaction_constructor_args():
    sig = inspect.signature(UMLModel_UnmarshallAction.__init__)
    params = list(sig.parameters.keys())
    assert "unmarshallType" in params, "Missing parameter 'unmarshallType'"

def test_umlmodel_unmarshallaction_has_unmarshallType():
    assert hasattr(UMLModel_UnmarshallAction, "unmarshallType")
    descriptor = None
    for klass in UMLModel_UnmarshallAction.__mro__:
        if "unmarshallType" in klass.__dict__:
            descriptor = klass.__dict__["unmarshallType"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_readlinkobjectendaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ReadLinkObjectEndAction)


def test_umlmodel_readlinkobjectendaction_constructor_exists():
    assert callable(UMLModel_ReadLinkObjectEndAction.__init__)


def test_umlmodel_readlinkobjectendaction_constructor_args():
    sig = inspect.signature(UMLModel_ReadLinkObjectEndAction.__init__)
    params = list(sig.parameters.keys())
    assert "end" in params, "Missing parameter 'end'"

def test_umlmodel_readlinkobjectendaction_has_end():
    assert hasattr(UMLModel_ReadLinkObjectEndAction, "end")
    descriptor = None
    for klass in UMLModel_ReadLinkObjectEndAction.__mro__:
        if "end" in klass.__dict__:
            descriptor = klass.__dict__["end"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_readlinkobjectendqualifieraction_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ReadLinkObjectEndQualifierAction)


def test_umlmodel_readlinkobjectendqualifieraction_constructor_exists():
    assert callable(UMLModel_ReadLinkObjectEndQualifierAction.__init__)


def test_umlmodel_readlinkobjectendqualifieraction_constructor_args():
    sig = inspect.signature(UMLModel_ReadLinkObjectEndQualifierAction.__init__)
    params = list(sig.parameters.keys())
    assert "qualifier" in params, "Missing parameter 'qualifier'"

def test_umlmodel_readlinkobjectendqualifieraction_has_qualifier():
    assert hasattr(UMLModel_ReadLinkObjectEndQualifierAction, "qualifier")
    descriptor = None
    for klass in UMLModel_ReadLinkObjectEndQualifierAction.__mro__:
        if "qualifier" in klass.__dict__:
            descriptor = klass.__dict__["qualifier"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_replyaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ReplyAction)


def test_umlmodel_replyaction_constructor_exists():
    assert callable(UMLModel_ReplyAction.__init__)


def test_umlmodel_replyaction_constructor_args():
    sig = inspect.signature(UMLModel_ReplyAction.__init__)
    params = list(sig.parameters.keys())
    assert "replyToCall" in params, "Missing parameter 'replyToCall'"

def test_umlmodel_replyaction_has_replyToCall():
    assert hasattr(UMLModel_ReplyAction, "replyToCall")
    descriptor = None
    for klass in UMLModel_ReplyAction.__mro__:
        if "replyToCall" in klass.__dict__:
            descriptor = klass.__dict__["replyToCall"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_variableaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel_VariableAction)


def test_umlmodel_variableaction_constructor_exists():
    assert callable(UMLModel_VariableAction.__init__)


def test_umlmodel_variableaction_constructor_args():
    sig = inspect.signature(UMLModel_VariableAction.__init__)
    params = list(sig.parameters.keys())
    assert "variable" in params, "Missing parameter 'variable'"

def test_umlmodel_variableaction_has_variable():
    assert hasattr(UMLModel_VariableAction, "variable")
    descriptor = None
    for klass in UMLModel_VariableAction.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_reclassifyobjectaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ReclassifyObjectAction)


def test_umlmodel_reclassifyobjectaction_constructor_exists():
    assert callable(UMLModel_ReclassifyObjectAction.__init__)


def test_umlmodel_reclassifyobjectaction_constructor_args():
    sig = inspect.signature(UMLModel_ReclassifyObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "isReplaceAll" in params, "Missing parameter 'isReplaceAll'"
    assert "newClassifier" in params, "Missing parameter 'newClassifier'"
    assert "oldClassifier" in params, "Missing parameter 'oldClassifier'"

def test_umlmodel_reclassifyobjectaction_has_isReplaceAll():
    assert hasattr(UMLModel_ReclassifyObjectAction, "isReplaceAll")
    descriptor = None
    for klass in UMLModel_ReclassifyObjectAction.__mro__:
        if "isReplaceAll" in klass.__dict__:
            descriptor = klass.__dict__["isReplaceAll"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_reclassifyobjectaction_has_newClassifier():
    assert hasattr(UMLModel_ReclassifyObjectAction, "newClassifier")
    descriptor = None
    for klass in UMLModel_ReclassifyObjectAction.__mro__:
        if "newClassifier" in klass.__dict__:
            descriptor = klass.__dict__["newClassifier"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_reclassifyobjectaction_has_oldClassifier():
    assert hasattr(UMLModel_ReclassifyObjectAction, "oldClassifier")
    descriptor = None
    for klass in UMLModel_ReclassifyObjectAction.__mro__:
        if "oldClassifier" in klass.__dict__:
            descriptor = klass.__dict__["oldClassifier"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_accepteventaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel_AcceptEventAction)


def test_umlmodel_accepteventaction_constructor_exists():
    assert callable(UMLModel_AcceptEventAction.__init__)


def test_umlmodel_accepteventaction_constructor_args():
    sig = inspect.signature(UMLModel_AcceptEventAction.__init__)
    params = list(sig.parameters.keys())
    assert "isUnmarshall" in params, "Missing parameter 'isUnmarshall'"

def test_umlmodel_accepteventaction_has_isUnmarshall():
    assert hasattr(UMLModel_AcceptEventAction, "isUnmarshall")
    descriptor = None
    for klass in UMLModel_AcceptEventAction.__mro__:
        if "isUnmarshall" in klass.__dict__:
            descriptor = klass.__dict__["isUnmarshall"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_outputpin_is_not_abstract():
    assert not inspect.isabstract(UMLModel_OutputPin)


def test_umlmodel_outputpin_constructor_exists():
    assert callable(UMLModel_OutputPin.__init__)


def test_umlmodel_outputpin_constructor_args():
    sig = inspect.signature(UMLModel_OutputPin.__init__)
    params = list(sig.parameters.keys())



def test_combinedfragment_is_not_abstract():
    assert not inspect.isabstract(CombinedFragment)


def test_combinedfragment_constructor_exists():
    assert callable(CombinedFragment.__init__)


def test_combinedfragment_constructor_args():
    sig = inspect.signature(CombinedFragment.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_considerignorefragment_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ConsiderIgnoreFragment)


def test_umlmodel_considerignorefragment_constructor_exists():
    assert callable(UMLModel_ConsiderIgnoreFragment.__init__)


def test_umlmodel_considerignorefragment_constructor_args():
    sig = inspect.signature(UMLModel_ConsiderIgnoreFragment.__init__)
    params = list(sig.parameters.keys())
    assert "message" in params, "Missing parameter 'message'"

def test_umlmodel_considerignorefragment_has_message():
    assert hasattr(UMLModel_ConsiderIgnoreFragment, "message")
    descriptor = None
    for klass in UMLModel_ConsiderIgnoreFragment.__mro__:
        if "message" in klass.__dict__:
            descriptor = klass.__dict__["message"]
            break
    assert isinstance(descriptor, property)



def test_centralbuffernode_is_not_abstract():
    assert not inspect.isabstract(CentralBufferNode)


def test_centralbuffernode_constructor_exists():
    assert callable(CentralBufferNode.__init__)


def test_centralbuffernode_constructor_args():
    sig = inspect.signature(CentralBufferNode.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_datastorenode_is_not_abstract():
    assert not inspect.isabstract(UMLModel_DataStoreNode)


def test_umlmodel_datastorenode_constructor_exists():
    assert callable(UMLModel_DataStoreNode.__init__)


def test_umlmodel_datastorenode_constructor_args():
    sig = inspect.signature(UMLModel_DataStoreNode.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_centralbuffernode_is_not_abstract():
    assert not inspect.isabstract(UMLModel_CentralBufferNode)


def test_umlmodel_centralbuffernode_constructor_exists():
    assert callable(UMLModel_CentralBufferNode.__init__)


def test_umlmodel_centralbuffernode_constructor_args():
    sig = inspect.signature(UMLModel_CentralBufferNode.__init__)
    params = list(sig.parameters.keys())



def test_writelinkaction_is_not_abstract():
    assert not inspect.isabstract(WriteLinkAction)


def test_writelinkaction_constructor_exists():
    assert callable(WriteLinkAction.__init__)


def test_writelinkaction_constructor_args():
    sig = inspect.signature(WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_destroylinkaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel_DestroyLinkAction)


def test_umlmodel_destroylinkaction_constructor_exists():
    assert callable(UMLModel_DestroyLinkAction.__init__)


def test_umlmodel_destroylinkaction_constructor_args():
    sig = inspect.signature(UMLModel_DestroyLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_createlinkaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel_CreateLinkAction)


def test_umlmodel_createlinkaction_constructor_exists():
    assert callable(UMLModel_CreateLinkAction.__init__)


def test_umlmodel_createlinkaction_constructor_args():
    sig = inspect.signature(UMLModel_CreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_packageableelement_is_not_abstract():
    assert not inspect.isabstract(PackageableElement)


def test_packageableelement_constructor_exists():
    assert callable(PackageableElement.__init__)


def test_packageableelement_constructor_args():
    sig = inspect.signature(PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_event_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Event)


def test_umlmodel_event_constructor_exists():
    assert callable(UMLModel_Event.__init__)


def test_umlmodel_event_constructor_args():
    sig = inspect.signature(UMLModel_Event.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_informationflow_is_not_abstract():
    assert not inspect.isabstract(UMLModel_InformationFlow)


def test_umlmodel_informationflow_constructor_exists():
    assert callable(UMLModel_InformationFlow.__init__)


def test_umlmodel_informationflow_constructor_args():
    sig = inspect.signature(UMLModel_InformationFlow.__init__)
    params = list(sig.parameters.keys())
    assert "realizingConnector" in params, "Missing parameter 'realizingConnector'"
    assert "conveyed" in params, "Missing parameter 'conveyed'"
    assert "informationSource" in params, "Missing parameter 'informationSource'"
    assert "realizingActivityEdge" in params, "Missing parameter 'realizingActivityEdge'"
    assert "informationTarget" in params, "Missing parameter 'informationTarget'"
    assert "realizingMessage" in params, "Missing parameter 'realizingMessage'"
    assert "realization" in params, "Missing parameter 'realization'"

def test_umlmodel_informationflow_has_realizingConnector():
    assert hasattr(UMLModel_InformationFlow, "realizingConnector")
    descriptor = None
    for klass in UMLModel_InformationFlow.__mro__:
        if "realizingConnector" in klass.__dict__:
            descriptor = klass.__dict__["realizingConnector"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_informationflow_has_conveyed():
    assert hasattr(UMLModel_InformationFlow, "conveyed")
    descriptor = None
    for klass in UMLModel_InformationFlow.__mro__:
        if "conveyed" in klass.__dict__:
            descriptor = klass.__dict__["conveyed"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_informationflow_has_informationSource():
    assert hasattr(UMLModel_InformationFlow, "informationSource")
    descriptor = None
    for klass in UMLModel_InformationFlow.__mro__:
        if "informationSource" in klass.__dict__:
            descriptor = klass.__dict__["informationSource"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_informationflow_has_realizingActivityEdge():
    assert hasattr(UMLModel_InformationFlow, "realizingActivityEdge")
    descriptor = None
    for klass in UMLModel_InformationFlow.__mro__:
        if "realizingActivityEdge" in klass.__dict__:
            descriptor = klass.__dict__["realizingActivityEdge"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_informationflow_has_informationTarget():
    assert hasattr(UMLModel_InformationFlow, "informationTarget")
    descriptor = None
    for klass in UMLModel_InformationFlow.__mro__:
        if "informationTarget" in klass.__dict__:
            descriptor = klass.__dict__["informationTarget"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_informationflow_has_realizingMessage():
    assert hasattr(UMLModel_InformationFlow, "realizingMessage")
    descriptor = None
    for klass in UMLModel_InformationFlow.__mro__:
        if "realizingMessage" in klass.__dict__:
            descriptor = klass.__dict__["realizingMessage"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_informationflow_has_realization():
    assert hasattr(UMLModel_InformationFlow, "realization")
    descriptor = None
    for klass in UMLModel_InformationFlow.__mro__:
        if "realization" in klass.__dict__:
            descriptor = klass.__dict__["realization"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_constraint_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Constraint)


def test_umlmodel_constraint_constructor_exists():
    assert callable(UMLModel_Constraint.__init__)


def test_umlmodel_constraint_constructor_args():
    sig = inspect.signature(UMLModel_Constraint.__init__)
    params = list(sig.parameters.keys())
    assert "context" in params, "Missing parameter 'context'"
    assert "constrainedElement" in params, "Missing parameter 'constrainedElement'"

def test_umlmodel_constraint_has_context():
    assert hasattr(UMLModel_Constraint, "context")
    descriptor = None
    for klass in UMLModel_Constraint.__mro__:
        if "context" in klass.__dict__:
            descriptor = klass.__dict__["context"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_constraint_has_constrainedElement():
    assert hasattr(UMLModel_Constraint, "constrainedElement")
    descriptor = None
    for klass in UMLModel_Constraint.__mro__:
        if "constrainedElement" in klass.__dict__:
            descriptor = klass.__dict__["constrainedElement"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_generalizationset_is_not_abstract():
    assert not inspect.isabstract(UMLModel_GeneralizationSet)


def test_umlmodel_generalizationset_constructor_exists():
    assert callable(UMLModel_GeneralizationSet.__init__)


def test_umlmodel_generalizationset_constructor_args():
    sig = inspect.signature(UMLModel_GeneralizationSet.__init__)
    params = list(sig.parameters.keys())
    assert "isCovering" in params, "Missing parameter 'isCovering'"
    assert "powerType" in params, "Missing parameter 'powerType'"
    assert "generalization" in params, "Missing parameter 'generalization'"
    assert "isDisjoint" in params, "Missing parameter 'isDisjoint'"

def test_umlmodel_generalizationset_has_isCovering():
    assert hasattr(UMLModel_GeneralizationSet, "isCovering")
    descriptor = None
    for klass in UMLModel_GeneralizationSet.__mro__:
        if "isCovering" in klass.__dict__:
            descriptor = klass.__dict__["isCovering"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_generalizationset_has_powerType():
    assert hasattr(UMLModel_GeneralizationSet, "powerType")
    descriptor = None
    for klass in UMLModel_GeneralizationSet.__mro__:
        if "powerType" in klass.__dict__:
            descriptor = klass.__dict__["powerType"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_generalizationset_has_generalization():
    assert hasattr(UMLModel_GeneralizationSet, "generalization")
    descriptor = None
    for klass in UMLModel_GeneralizationSet.__mro__:
        if "generalization" in klass.__dict__:
            descriptor = klass.__dict__["generalization"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_generalizationset_has_isDisjoint():
    assert hasattr(UMLModel_GeneralizationSet, "isDisjoint")
    descriptor = None
    for klass in UMLModel_GeneralizationSet.__mro__:
        if "isDisjoint" in klass.__dict__:
            descriptor = klass.__dict__["isDisjoint"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_observation_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Observation)


def test_umlmodel_observation_constructor_exists():
    assert callable(UMLModel_Observation.__init__)


def test_umlmodel_observation_constructor_args():
    sig = inspect.signature(UMLModel_Observation.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_valuespecification_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ValueSpecification)


def test_umlmodel_valuespecification_constructor_exists():
    assert callable(UMLModel_ValueSpecification.__init__)


def test_umlmodel_valuespecification_constructor_args():
    sig = inspect.signature(UMLModel_ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_type_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Type)


def test_umlmodel_type_constructor_exists():
    assert callable(UMLModel_Type.__init__)


def test_umlmodel_type_constructor_args():
    sig = inspect.signature(UMLModel_Type.__init__)
    params = list(sig.parameters.keys())
    assert "package" in params, "Missing parameter 'package'"

def test_umlmodel_type_has_package():
    assert hasattr(UMLModel_Type, "package")
    descriptor = None
    for klass in UMLModel_Type.__mro__:
        if "package" in klass.__dict__:
            descriptor = klass.__dict__["package"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_createobjectaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel_CreateObjectAction)


def test_umlmodel_createobjectaction_constructor_exists():
    assert callable(UMLModel_CreateObjectAction.__init__)


def test_umlmodel_createobjectaction_constructor_args():
    sig = inspect.signature(UMLModel_CreateObjectAction.__init__)
    params = list(sig.parameters.keys())
    assert "classifier" in params, "Missing parameter 'classifier'"

def test_umlmodel_createobjectaction_has_classifier():
    assert hasattr(UMLModel_CreateObjectAction, "classifier")
    descriptor = None
    for klass in UMLModel_CreateObjectAction.__mro__:
        if "classifier" in klass.__dict__:
            descriptor = klass.__dict__["classifier"]
            break
    assert isinstance(descriptor, property)



def test_createlinkaction_is_not_abstract():
    assert not inspect.isabstract(CreateLinkAction)


def test_createlinkaction_constructor_exists():
    assert callable(CreateLinkAction.__init__)


def test_createlinkaction_constructor_args():
    sig = inspect.signature(CreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_createlinkobjectaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel_CreateLinkObjectAction)


def test_umlmodel_createlinkobjectaction_constructor_exists():
    assert callable(UMLModel_CreateLinkObjectAction.__init__)


def test_umlmodel_createlinkobjectaction_constructor_args():
    sig = inspect.signature(UMLModel_CreateLinkObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(StructuredActivityNode)


def test_structuredactivitynode_constructor_exists():
    assert callable(StructuredActivityNode.__init__)


def test_structuredactivitynode_constructor_args():
    sig = inspect.signature(StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_sequencenode_is_not_abstract():
    assert not inspect.isabstract(UMLModel_SequenceNode)


def test_umlmodel_sequencenode_constructor_exists():
    assert callable(UMLModel_SequenceNode.__init__)


def test_umlmodel_sequencenode_constructor_args():
    sig = inspect.signature(UMLModel_SequenceNode.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_loopnode_is_not_abstract():
    assert not inspect.isabstract(UMLModel_LoopNode)


def test_umlmodel_loopnode_constructor_exists():
    assert callable(UMLModel_LoopNode.__init__)


def test_umlmodel_loopnode_constructor_args():
    sig = inspect.signature(UMLModel_LoopNode.__init__)
    params = list(sig.parameters.keys())
    assert "isTestedFirst" in params, "Missing parameter 'isTestedFirst'"
    assert "test" in params, "Missing parameter 'test'"
    assert "loopVariable" in params, "Missing parameter 'loopVariable'"
    assert "bodyPart" in params, "Missing parameter 'bodyPart'"
    assert "decider" in params, "Missing parameter 'decider'"
    assert "bodyOutput" in params, "Missing parameter 'bodyOutput'"
    assert "setupPart" in params, "Missing parameter 'setupPart'"

def test_umlmodel_loopnode_has_isTestedFirst():
    assert hasattr(UMLModel_LoopNode, "isTestedFirst")
    descriptor = None
    for klass in UMLModel_LoopNode.__mro__:
        if "isTestedFirst" in klass.__dict__:
            descriptor = klass.__dict__["isTestedFirst"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_loopnode_has_test():
    assert hasattr(UMLModel_LoopNode, "test")
    descriptor = None
    for klass in UMLModel_LoopNode.__mro__:
        if "test" in klass.__dict__:
            descriptor = klass.__dict__["test"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_loopnode_has_loopVariable():
    assert hasattr(UMLModel_LoopNode, "loopVariable")
    descriptor = None
    for klass in UMLModel_LoopNode.__mro__:
        if "loopVariable" in klass.__dict__:
            descriptor = klass.__dict__["loopVariable"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_loopnode_has_bodyPart():
    assert hasattr(UMLModel_LoopNode, "bodyPart")
    descriptor = None
    for klass in UMLModel_LoopNode.__mro__:
        if "bodyPart" in klass.__dict__:
            descriptor = klass.__dict__["bodyPart"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_loopnode_has_decider():
    assert hasattr(UMLModel_LoopNode, "decider")
    descriptor = None
    for klass in UMLModel_LoopNode.__mro__:
        if "decider" in klass.__dict__:
            descriptor = klass.__dict__["decider"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_loopnode_has_bodyOutput():
    assert hasattr(UMLModel_LoopNode, "bodyOutput")
    descriptor = None
    for klass in UMLModel_LoopNode.__mro__:
        if "bodyOutput" in klass.__dict__:
            descriptor = klass.__dict__["bodyOutput"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_loopnode_has_setupPart():
    assert hasattr(UMLModel_LoopNode, "setupPart")
    descriptor = None
    for klass in UMLModel_LoopNode.__mro__:
        if "setupPart" in klass.__dict__:
            descriptor = klass.__dict__["setupPart"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_expansionregion_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ExpansionRegion)


def test_umlmodel_expansionregion_constructor_exists():
    assert callable(UMLModel_ExpansionRegion.__init__)


def test_umlmodel_expansionregion_constructor_args():
    sig = inspect.signature(UMLModel_ExpansionRegion.__init__)
    params = list(sig.parameters.keys())
    assert "mode" in params, "Missing parameter 'mode'"
    assert "outputElement" in params, "Missing parameter 'outputElement'"
    assert "inputElement" in params, "Missing parameter 'inputElement'"

def test_umlmodel_expansionregion_has_mode():
    assert hasattr(UMLModel_ExpansionRegion, "mode")
    descriptor = None
    for klass in UMLModel_ExpansionRegion.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_expansionregion_has_outputElement():
    assert hasattr(UMLModel_ExpansionRegion, "outputElement")
    descriptor = None
    for klass in UMLModel_ExpansionRegion.__mro__:
        if "outputElement" in klass.__dict__:
            descriptor = klass.__dict__["outputElement"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_expansionregion_has_inputElement():
    assert hasattr(UMLModel_ExpansionRegion, "inputElement")
    descriptor = None
    for klass in UMLModel_ExpansionRegion.__mro__:
        if "inputElement" in klass.__dict__:
            descriptor = klass.__dict__["inputElement"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_conditionalnode_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ConditionalNode)


def test_umlmodel_conditionalnode_constructor_exists():
    assert callable(UMLModel_ConditionalNode.__init__)


def test_umlmodel_conditionalnode_constructor_args():
    sig = inspect.signature(UMLModel_ConditionalNode.__init__)
    params = list(sig.parameters.keys())
    assert "isDeterminate" in params, "Missing parameter 'isDeterminate'"
    assert "isAssured" in params, "Missing parameter 'isAssured'"

def test_umlmodel_conditionalnode_has_isDeterminate():
    assert hasattr(UMLModel_ConditionalNode, "isDeterminate")
    descriptor = None
    for klass in UMLModel_ConditionalNode.__mro__:
        if "isDeterminate" in klass.__dict__:
            descriptor = klass.__dict__["isDeterminate"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_conditionalnode_has_isAssured():
    assert hasattr(UMLModel_ConditionalNode, "isAssured")
    descriptor = None
    for klass in UMLModel_ConditionalNode.__mro__:
        if "isAssured" in klass.__dict__:
            descriptor = klass.__dict__["isAssured"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_gate_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Gate)


def test_umlmodel_gate_constructor_exists():
    assert callable(UMLModel_Gate.__init__)


def test_umlmodel_gate_constructor_args():
    sig = inspect.signature(UMLModel_Gate.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_is_not_abstract():
    assert not inspect.isabstract(ActivityNode)


def test_activitynode_constructor_exists():
    assert callable(ActivityNode.__init__)


def test_activitynode_constructor_args():
    sig = inspect.signature(ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_objectnode_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ObjectNode)


def test_umlmodel_objectnode_constructor_exists():
    assert callable(UMLModel_ObjectNode.__init__)


def test_umlmodel_objectnode_constructor_args():
    sig = inspect.signature(UMLModel_ObjectNode.__init__)
    params = list(sig.parameters.keys())
    assert "selection" in params, "Missing parameter 'selection'"
    assert "inState" in params, "Missing parameter 'inState'"
    assert "isControlType" in params, "Missing parameter 'isControlType'"
    assert "ordering" in params, "Missing parameter 'ordering'"

def test_umlmodel_objectnode_has_selection():
    assert hasattr(UMLModel_ObjectNode, "selection")
    descriptor = None
    for klass in UMLModel_ObjectNode.__mro__:
        if "selection" in klass.__dict__:
            descriptor = klass.__dict__["selection"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_objectnode_has_inState():
    assert hasattr(UMLModel_ObjectNode, "inState")
    descriptor = None
    for klass in UMLModel_ObjectNode.__mro__:
        if "inState" in klass.__dict__:
            descriptor = klass.__dict__["inState"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_objectnode_has_isControlType():
    assert hasattr(UMLModel_ObjectNode, "isControlType")
    descriptor = None
    for klass in UMLModel_ObjectNode.__mro__:
        if "isControlType" in klass.__dict__:
            descriptor = klass.__dict__["isControlType"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_objectnode_has_ordering():
    assert hasattr(UMLModel_ObjectNode, "ordering")
    descriptor = None
    for klass in UMLModel_ObjectNode.__mro__:
        if "ordering" in klass.__dict__:
            descriptor = klass.__dict__["ordering"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_executablenode_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ExecutableNode)


def test_umlmodel_executablenode_constructor_exists():
    assert callable(UMLModel_ExecutableNode.__init__)


def test_umlmodel_executablenode_constructor_args():
    sig = inspect.signature(UMLModel_ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_controlnode_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ControlNode)


def test_umlmodel_controlnode_constructor_exists():
    assert callable(UMLModel_ControlNode.__init__)


def test_umlmodel_controlnode_constructor_args():
    sig = inspect.signature(UMLModel_ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_activityedge_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge)


def test_activityedge_constructor_exists():
    assert callable(ActivityEdge.__init__)


def test_activityedge_constructor_args():
    sig = inspect.signature(ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_objectflow_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ObjectFlow)


def test_umlmodel_objectflow_constructor_exists():
    assert callable(UMLModel_ObjectFlow.__init__)


def test_umlmodel_objectflow_constructor_args():
    sig = inspect.signature(UMLModel_ObjectFlow.__init__)
    params = list(sig.parameters.keys())
    assert "isMulticast" in params, "Missing parameter 'isMulticast'"
    assert "isMultireceive" in params, "Missing parameter 'isMultireceive'"
    assert "transformation" in params, "Missing parameter 'transformation'"
    assert "selection" in params, "Missing parameter 'selection'"

def test_umlmodel_objectflow_has_isMulticast():
    assert hasattr(UMLModel_ObjectFlow, "isMulticast")
    descriptor = None
    for klass in UMLModel_ObjectFlow.__mro__:
        if "isMulticast" in klass.__dict__:
            descriptor = klass.__dict__["isMulticast"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_objectflow_has_isMultireceive():
    assert hasattr(UMLModel_ObjectFlow, "isMultireceive")
    descriptor = None
    for klass in UMLModel_ObjectFlow.__mro__:
        if "isMultireceive" in klass.__dict__:
            descriptor = klass.__dict__["isMultireceive"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_objectflow_has_transformation():
    assert hasattr(UMLModel_ObjectFlow, "transformation")
    descriptor = None
    for klass in UMLModel_ObjectFlow.__mro__:
        if "transformation" in klass.__dict__:
            descriptor = klass.__dict__["transformation"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_objectflow_has_selection():
    assert hasattr(UMLModel_ObjectFlow, "selection")
    descriptor = None
    for klass in UMLModel_ObjectFlow.__mro__:
        if "selection" in klass.__dict__:
            descriptor = klass.__dict__["selection"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_controlflow_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ControlFlow)


def test_umlmodel_controlflow_constructor_exists():
    assert callable(UMLModel_ControlFlow.__init__)


def test_umlmodel_controlflow_constructor_args():
    sig = inspect.signature(UMLModel_ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_pseudostate_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Pseudostate)


def test_umlmodel_pseudostate_constructor_exists():
    assert callable(UMLModel_Pseudostate.__init__)


def test_umlmodel_pseudostate_constructor_args():
    sig = inspect.signature(UMLModel_Pseudostate.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "stateMachine" in params, "Missing parameter 'stateMachine'"
    assert "state" in params, "Missing parameter 'state'"

def test_umlmodel_pseudostate_has_kind():
    assert hasattr(UMLModel_Pseudostate, "kind")
    descriptor = None
    for klass in UMLModel_Pseudostate.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_pseudostate_has_stateMachine():
    assert hasattr(UMLModel_Pseudostate, "stateMachine")
    descriptor = None
    for klass in UMLModel_Pseudostate.__mro__:
        if "stateMachine" in klass.__dict__:
            descriptor = klass.__dict__["stateMachine"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_pseudostate_has_state():
    assert hasattr(UMLModel_Pseudostate, "state")
    descriptor = None
    for klass in UMLModel_Pseudostate.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_connectionpointreference_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ConnectionPointReference)


def test_umlmodel_connectionpointreference_constructor_exists():
    assert callable(UMLModel_ConnectionPointReference.__init__)


def test_umlmodel_connectionpointreference_constructor_args():
    sig = inspect.signature(UMLModel_ConnectionPointReference.__init__)
    params = list(sig.parameters.keys())
    assert "entry" in params, "Missing parameter 'entry'"
    assert "exit" in params, "Missing parameter 'exit'"
    assert "state" in params, "Missing parameter 'state'"

def test_umlmodel_connectionpointreference_has_entry():
    assert hasattr(UMLModel_ConnectionPointReference, "entry")
    descriptor = None
    for klass in UMLModel_ConnectionPointReference.__mro__:
        if "entry" in klass.__dict__:
            descriptor = klass.__dict__["entry"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_connectionpointreference_has_exit():
    assert hasattr(UMLModel_ConnectionPointReference, "exit")
    descriptor = None
    for klass in UMLModel_ConnectionPointReference.__mro__:
        if "exit" in klass.__dict__:
            descriptor = klass.__dict__["exit"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_connectionpointreference_has_state():
    assert hasattr(UMLModel_ConnectionPointReference, "state")
    descriptor = None
    for klass in UMLModel_ConnectionPointReference.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_comment_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Comment)


def test_umlmodel_comment_constructor_exists():
    assert callable(UMLModel_Comment.__init__)


def test_umlmodel_comment_constructor_args():
    sig = inspect.signature(UMLModel_Comment.__init__)
    params = list(sig.parameters.keys())
    assert "body" in params, "Missing parameter 'body'"
    assert "annotatedElement" in params, "Missing parameter 'annotatedElement'"

def test_umlmodel_comment_has_body():
    assert hasattr(UMLModel_Comment, "body")
    descriptor = None
    for klass in UMLModel_Comment.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_comment_has_annotatedElement():
    assert hasattr(UMLModel_Comment, "annotatedElement")
    descriptor = None
    for klass in UMLModel_Comment.__mro__:
        if "annotatedElement" in klass.__dict__:
            descriptor = klass.__dict__["annotatedElement"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_dependency_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Dependency)


def test_umlmodel_dependency_constructor_exists():
    assert callable(UMLModel_Dependency.__init__)


def test_umlmodel_dependency_constructor_args():
    sig = inspect.signature(UMLModel_Dependency.__init__)
    params = list(sig.parameters.keys())
    assert "client" in params, "Missing parameter 'client'"
    assert "supplier" in params, "Missing parameter 'supplier'"

def test_umlmodel_dependency_has_client():
    assert hasattr(UMLModel_Dependency, "client")
    descriptor = None
    for klass in UMLModel_Dependency.__mro__:
        if "client" in klass.__dict__:
            descriptor = klass.__dict__["client"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_dependency_has_supplier():
    assert hasattr(UMLModel_Dependency, "supplier")
    descriptor = None
    for klass in UMLModel_Dependency.__mro__:
        if "supplier" in klass.__dict__:
            descriptor = klass.__dict__["supplier"]
            break
    assert isinstance(descriptor, property)



def test_structuredclassifier_is_not_abstract():
    assert not inspect.isabstract(StructuredClassifier)


def test_structuredclassifier_constructor_exists():
    assert callable(StructuredClassifier.__init__)


def test_structuredclassifier_constructor_args():
    sig = inspect.signature(StructuredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_encapsulatedclassifier_is_not_abstract():
    assert not inspect.isabstract(UMLModel_EncapsulatedClassifier)


def test_umlmodel_encapsulatedclassifier_constructor_exists():
    assert callable(UMLModel_EncapsulatedClassifier.__init__)


def test_umlmodel_encapsulatedclassifier_constructor_args():
    sig = inspect.signature(UMLModel_EncapsulatedClassifier.__init__)
    params = list(sig.parameters.keys())
    assert "ownedPort" in params, "Missing parameter 'ownedPort'"

def test_umlmodel_encapsulatedclassifier_has_ownedPort():
    assert hasattr(UMLModel_EncapsulatedClassifier, "ownedPort")
    descriptor = None
    for klass in UMLModel_EncapsulatedClassifier.__mro__:
        if "ownedPort" in klass.__dict__:
            descriptor = klass.__dict__["ownedPort"]
            break
    assert isinstance(descriptor, property)



def test_structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(StructuralFeatureAction)


def test_structuralfeatureaction_constructor_exists():
    assert callable(StructuralFeatureAction.__init__)


def test_structuralfeatureaction_constructor_args():
    sig = inspect.signature(StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel_WriteStructuralFeatureAction)


def test_umlmodel_writestructuralfeatureaction_constructor_exists():
    assert callable(UMLModel_WriteStructuralFeatureAction.__init__)


def test_umlmodel_writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(UMLModel_WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_readstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ReadStructuralFeatureAction)


def test_umlmodel_readstructuralfeatureaction_constructor_exists():
    assert callable(UMLModel_ReadStructuralFeatureAction.__init__)


def test_umlmodel_readstructuralfeatureaction_constructor_args():
    sig = inspect.signature(UMLModel_ReadStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_clearstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ClearStructuralFeatureAction)


def test_umlmodel_clearstructuralfeatureaction_constructor_exists():
    assert callable(UMLModel_ClearStructuralFeatureAction.__init__)


def test_umlmodel_clearstructuralfeatureaction_constructor_args():
    sig = inspect.signature(UMLModel_ClearStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_clearassociationaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ClearAssociationAction)


def test_umlmodel_clearassociationaction_constructor_exists():
    assert callable(UMLModel_ClearAssociationAction.__init__)


def test_umlmodel_clearassociationaction_constructor_args():
    sig = inspect.signature(UMLModel_ClearAssociationAction.__init__)
    params = list(sig.parameters.keys())
    assert "association" in params, "Missing parameter 'association'"

def test_umlmodel_clearassociationaction_has_association():
    assert hasattr(UMLModel_ClearAssociationAction, "association")
    descriptor = None
    for klass in UMLModel_ClearAssociationAction.__mro__:
        if "association" in klass.__dict__:
            descriptor = klass.__dict__["association"]
            break
    assert isinstance(descriptor, property)



def test_variableaction_is_not_abstract():
    assert not inspect.isabstract(VariableAction)


def test_variableaction_constructor_exists():
    assert callable(VariableAction.__init__)


def test_variableaction_constructor_args():
    sig = inspect.signature(VariableAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_readvariableaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ReadVariableAction)


def test_umlmodel_readvariableaction_constructor_exists():
    assert callable(UMLModel_ReadVariableAction.__init__)


def test_umlmodel_readvariableaction_constructor_args():
    sig = inspect.signature(UMLModel_ReadVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_writevariableaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel_WriteVariableAction)


def test_umlmodel_writevariableaction_constructor_exists():
    assert callable(UMLModel_WriteVariableAction.__init__)


def test_umlmodel_writevariableaction_constructor_args():
    sig = inspect.signature(UMLModel_WriteVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_clearvariableaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ClearVariableAction)


def test_umlmodel_clearvariableaction_constructor_exists():
    assert callable(UMLModel_ClearVariableAction.__init__)


def test_umlmodel_clearvariableaction_constructor_args():
    sig = inspect.signature(UMLModel_ClearVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_clause_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Clause)


def test_umlmodel_clause_constructor_exists():
    assert callable(UMLModel_Clause.__init__)


def test_umlmodel_clause_constructor_args():
    sig = inspect.signature(UMLModel_Clause.__init__)
    params = list(sig.parameters.keys())
    assert "decider" in params, "Missing parameter 'decider'"
    assert "bodyOutput" in params, "Missing parameter 'bodyOutput'"
    assert "successorClause" in params, "Missing parameter 'successorClause'"
    assert "test" in params, "Missing parameter 'test'"
    assert "predecessorClause" in params, "Missing parameter 'predecessorClause'"
    assert "body" in params, "Missing parameter 'body'"

def test_umlmodel_clause_has_decider():
    assert hasattr(UMLModel_Clause, "decider")
    descriptor = None
    for klass in UMLModel_Clause.__mro__:
        if "decider" in klass.__dict__:
            descriptor = klass.__dict__["decider"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_clause_has_bodyOutput():
    assert hasattr(UMLModel_Clause, "bodyOutput")
    descriptor = None
    for klass in UMLModel_Clause.__mro__:
        if "bodyOutput" in klass.__dict__:
            descriptor = klass.__dict__["bodyOutput"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_clause_has_successorClause():
    assert hasattr(UMLModel_Clause, "successorClause")
    descriptor = None
    for klass in UMLModel_Clause.__mro__:
        if "successorClause" in klass.__dict__:
            descriptor = klass.__dict__["successorClause"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_clause_has_test():
    assert hasattr(UMLModel_Clause, "test")
    descriptor = None
    for klass in UMLModel_Clause.__mro__:
        if "test" in klass.__dict__:
            descriptor = klass.__dict__["test"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_clause_has_predecessorClause():
    assert hasattr(UMLModel_Clause, "predecessorClause")
    descriptor = None
    for klass in UMLModel_Clause.__mro__:
        if "predecessorClause" in klass.__dict__:
            descriptor = klass.__dict__["predecessorClause"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_clause_has_body():
    assert hasattr(UMLModel_Clause, "body")
    descriptor = None
    for klass in UMLModel_Clause.__mro__:
        if "body" in klass.__dict__:
            descriptor = klass.__dict__["body"]
            break
    assert isinstance(descriptor, property)



def test_interactionfragment_is_not_abstract():
    assert not inspect.isabstract(InteractionFragment)


def test_interactionfragment_constructor_exists():
    assert callable(InteractionFragment.__init__)


def test_interactionfragment_constructor_args():
    sig = inspect.signature(InteractionFragment.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_occurrencespecification_is_not_abstract():
    assert not inspect.isabstract(UMLModel_OccurrenceSpecification)


def test_umlmodel_occurrencespecification_constructor_exists():
    assert callable(UMLModel_OccurrenceSpecification.__init__)


def test_umlmodel_occurrencespecification_constructor_args():
    sig = inspect.signature(UMLModel_OccurrenceSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "event" in params, "Missing parameter 'event'"
    assert "toAfter" in params, "Missing parameter 'toAfter'"
    assert "toBefore" in params, "Missing parameter 'toBefore'"

def test_umlmodel_occurrencespecification_has_event():
    assert hasattr(UMLModel_OccurrenceSpecification, "event")
    descriptor = None
    for klass in UMLModel_OccurrenceSpecification.__mro__:
        if "event" in klass.__dict__:
            descriptor = klass.__dict__["event"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_occurrencespecification_has_toAfter():
    assert hasattr(UMLModel_OccurrenceSpecification, "toAfter")
    descriptor = None
    for klass in UMLModel_OccurrenceSpecification.__mro__:
        if "toAfter" in klass.__dict__:
            descriptor = klass.__dict__["toAfter"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_occurrencespecification_has_toBefore():
    assert hasattr(UMLModel_OccurrenceSpecification, "toBefore")
    descriptor = None
    for klass in UMLModel_OccurrenceSpecification.__mro__:
        if "toBefore" in klass.__dict__:
            descriptor = klass.__dict__["toBefore"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_interactionuse_is_not_abstract():
    assert not inspect.isabstract(UMLModel_InteractionUse)


def test_umlmodel_interactionuse_constructor_exists():
    assert callable(UMLModel_InteractionUse.__init__)


def test_umlmodel_interactionuse_constructor_args():
    sig = inspect.signature(UMLModel_InteractionUse.__init__)
    params = list(sig.parameters.keys())
    assert "refersTo" in params, "Missing parameter 'refersTo'"

def test_umlmodel_interactionuse_has_refersTo():
    assert hasattr(UMLModel_InteractionUse, "refersTo")
    descriptor = None
    for klass in UMLModel_InteractionUse.__mro__:
        if "refersTo" in klass.__dict__:
            descriptor = klass.__dict__["refersTo"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_stateinvariant_is_not_abstract():
    assert not inspect.isabstract(UMLModel_StateInvariant)


def test_umlmodel_stateinvariant_constructor_exists():
    assert callable(UMLModel_StateInvariant.__init__)


def test_umlmodel_stateinvariant_constructor_args():
    sig = inspect.signature(UMLModel_StateInvariant.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_interaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Interaction)


def test_umlmodel_interaction_constructor_exists():
    assert callable(UMLModel_Interaction.__init__)


def test_umlmodel_interaction_constructor_args():
    sig = inspect.signature(UMLModel_Interaction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_continuation_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Continuation)


def test_umlmodel_continuation_constructor_exists():
    assert callable(UMLModel_Continuation.__init__)


def test_umlmodel_continuation_constructor_args():
    sig = inspect.signature(UMLModel_Continuation.__init__)
    params = list(sig.parameters.keys())
    assert "setting" in params, "Missing parameter 'setting'"

def test_umlmodel_continuation_has_setting():
    assert hasattr(UMLModel_Continuation, "setting")
    descriptor = None
    for klass in UMLModel_Continuation.__mro__:
        if "setting" in klass.__dict__:
            descriptor = klass.__dict__["setting"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_executionspecification_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ExecutionSpecification)


def test_umlmodel_executionspecification_constructor_exists():
    assert callable(UMLModel_ExecutionSpecification.__init__)


def test_umlmodel_executionspecification_constructor_args():
    sig = inspect.signature(UMLModel_ExecutionSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "finish" in params, "Missing parameter 'finish'"
    assert "start" in params, "Missing parameter 'start'"

def test_umlmodel_executionspecification_has_finish():
    assert hasattr(UMLModel_ExecutionSpecification, "finish")
    descriptor = None
    for klass in UMLModel_ExecutionSpecification.__mro__:
        if "finish" in klass.__dict__:
            descriptor = klass.__dict__["finish"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_executionspecification_has_start():
    assert hasattr(UMLModel_ExecutionSpecification, "start")
    descriptor = None
    for klass in UMLModel_ExecutionSpecification.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_combinedfragment_is_not_abstract():
    assert not inspect.isabstract(UMLModel_CombinedFragment)


def test_umlmodel_combinedfragment_constructor_exists():
    assert callable(UMLModel_CombinedFragment.__init__)


def test_umlmodel_combinedfragment_constructor_args():
    sig = inspect.signature(UMLModel_CombinedFragment.__init__)
    params = list(sig.parameters.keys())
    assert "interactionOperator" in params, "Missing parameter 'interactionOperator'"

def test_umlmodel_combinedfragment_has_interactionOperator():
    assert hasattr(UMLModel_CombinedFragment, "interactionOperator")
    descriptor = None
    for klass in UMLModel_CombinedFragment.__mro__:
        if "interactionOperator" in klass.__dict__:
            descriptor = klass.__dict__["interactionOperator"]
            break
    assert isinstance(descriptor, property)



def test_realization_is_not_abstract():
    assert not inspect.isabstract(Realization)


def test_realization_constructor_exists():
    assert callable(Realization.__init__)


def test_realization_constructor_args():
    sig = inspect.signature(Realization.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_componentrealization_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ComponentRealization)


def test_umlmodel_componentrealization_constructor_exists():
    assert callable(UMLModel_ComponentRealization.__init__)


def test_umlmodel_componentrealization_constructor_args():
    sig = inspect.signature(UMLModel_ComponentRealization.__init__)
    params = list(sig.parameters.keys())
    assert "realizingClassifier" in params, "Missing parameter 'realizingClassifier'"
    assert "abstraction" in params, "Missing parameter 'abstraction'"

def test_umlmodel_componentrealization_has_realizingClassifier():
    assert hasattr(UMLModel_ComponentRealization, "realizingClassifier")
    descriptor = None
    for klass in UMLModel_ComponentRealization.__mro__:
        if "realizingClassifier" in klass.__dict__:
            descriptor = klass.__dict__["realizingClassifier"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_componentrealization_has_abstraction():
    assert hasattr(UMLModel_ComponentRealization, "abstraction")
    descriptor = None
    for klass in UMLModel_ComponentRealization.__mro__:
        if "abstraction" in klass.__dict__:
            descriptor = klass.__dict__["abstraction"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_packageableelement_is_not_abstract():
    assert not inspect.isabstract(UMLModel_PackageableElement)


def test_umlmodel_packageableelement_constructor_exists():
    assert callable(UMLModel_PackageableElement.__init__)


def test_umlmodel_packageableelement_constructor_args():
    sig = inspect.signature(UMLModel_PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_generalization_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Generalization)


def test_umlmodel_generalization_constructor_exists():
    assert callable(UMLModel_Generalization.__init__)


def test_umlmodel_generalization_constructor_args():
    sig = inspect.signature(UMLModel_Generalization.__init__)
    params = list(sig.parameters.keys())
    assert "generalizationSet" in params, "Missing parameter 'generalizationSet'"
    assert "general" in params, "Missing parameter 'general'"
    assert "specific" in params, "Missing parameter 'specific'"
    assert "isSubstitutable" in params, "Missing parameter 'isSubstitutable'"

def test_umlmodel_generalization_has_generalizationSet():
    assert hasattr(UMLModel_Generalization, "generalizationSet")
    descriptor = None
    for klass in UMLModel_Generalization.__mro__:
        if "generalizationSet" in klass.__dict__:
            descriptor = klass.__dict__["generalizationSet"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_generalization_has_general():
    assert hasattr(UMLModel_Generalization, "general")
    descriptor = None
    for klass in UMLModel_Generalization.__mro__:
        if "general" in klass.__dict__:
            descriptor = klass.__dict__["general"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_generalization_has_specific():
    assert hasattr(UMLModel_Generalization, "specific")
    descriptor = None
    for klass in UMLModel_Generalization.__mro__:
        if "specific" in klass.__dict__:
            descriptor = klass.__dict__["specific"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_generalization_has_isSubstitutable():
    assert hasattr(UMLModel_Generalization, "isSubstitutable")
    descriptor = None
    for klass in UMLModel_Generalization.__mro__:
        if "isSubstitutable" in klass.__dict__:
            descriptor = klass.__dict__["isSubstitutable"]
            break
    assert isinstance(descriptor, property)



def test_templateableelement_is_not_abstract():
    assert not inspect.isabstract(TemplateableElement)


def test_templateableelement_constructor_exists():
    assert callable(TemplateableElement.__init__)


def test_templateableelement_constructor_args():
    sig = inspect.signature(TemplateableElement.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_stringexpression_is_not_abstract():
    assert not inspect.isabstract(UMLModel_StringExpression)


def test_umlmodel_stringexpression_constructor_exists():
    assert callable(UMLModel_StringExpression.__init__)


def test_umlmodel_stringexpression_constructor_args():
    sig = inspect.signature(UMLModel_StringExpression.__init__)
    params = list(sig.parameters.keys())
    assert "owningExpression" in params, "Missing parameter 'owningExpression'"

def test_umlmodel_stringexpression_has_owningExpression():
    assert hasattr(UMLModel_StringExpression, "owningExpression")
    descriptor = None
    for klass in UMLModel_StringExpression.__mro__:
        if "owningExpression" in klass.__dict__:
            descriptor = klass.__dict__["owningExpression"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_reception_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Reception)


def test_umlmodel_reception_constructor_exists():
    assert callable(UMLModel_Reception.__init__)


def test_umlmodel_reception_constructor_args():
    sig = inspect.signature(UMLModel_Reception.__init__)
    params = list(sig.parameters.keys())
    assert "signal" in params, "Missing parameter 'signal'"

def test_umlmodel_reception_has_signal():
    assert hasattr(UMLModel_Reception, "signal")
    descriptor = None
    for klass in UMLModel_Reception.__mro__:
        if "signal" in klass.__dict__:
            descriptor = klass.__dict__["signal"]
            break
    assert isinstance(descriptor, property)



def test_encapsulatedclassifier_is_not_abstract():
    assert not inspect.isabstract(EncapsulatedClassifier)


def test_encapsulatedclassifier_constructor_exists():
    assert callable(EncapsulatedClassifier.__init__)


def test_encapsulatedclassifier_constructor_args():
    sig = inspect.signature(EncapsulatedClassifier.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_executionevent_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ExecutionEvent)


def test_umlmodel_executionevent_constructor_exists():
    assert callable(UMLModel_ExecutionEvent.__init__)


def test_umlmodel_executionevent_constructor_args():
    sig = inspect.signature(UMLModel_ExecutionEvent.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_destructionevent_is_not_abstract():
    assert not inspect.isabstract(UMLModel_DestructionEvent)


def test_umlmodel_destructionevent_constructor_exists():
    assert callable(UMLModel_DestructionEvent.__init__)


def test_umlmodel_destructionevent_constructor_args():
    sig = inspect.signature(UMLModel_DestructionEvent.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_messageevent_is_not_abstract():
    assert not inspect.isabstract(UMLModel_MessageEvent)


def test_umlmodel_messageevent_constructor_exists():
    assert callable(UMLModel_MessageEvent.__init__)


def test_umlmodel_messageevent_constructor_args():
    sig = inspect.signature(UMLModel_MessageEvent.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_creationevent_is_not_abstract():
    assert not inspect.isabstract(UMLModel_CreationEvent)


def test_umlmodel_creationevent_constructor_exists():
    assert callable(UMLModel_CreationEvent.__init__)


def test_umlmodel_creationevent_constructor_args():
    sig = inspect.signature(UMLModel_CreationEvent.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_timeevent_is_not_abstract():
    assert not inspect.isabstract(UMLModel_TimeEvent)


def test_umlmodel_timeevent_constructor_exists():
    assert callable(UMLModel_TimeEvent.__init__)


def test_umlmodel_timeevent_constructor_args():
    sig = inspect.signature(UMLModel_TimeEvent.__init__)
    params = list(sig.parameters.keys())
    assert "isRelative" in params, "Missing parameter 'isRelative'"

def test_umlmodel_timeevent_has_isRelative():
    assert hasattr(UMLModel_TimeEvent, "isRelative")
    descriptor = None
    for klass in UMLModel_TimeEvent.__mro__:
        if "isRelative" in klass.__dict__:
            descriptor = klass.__dict__["isRelative"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_changeevent_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ChangeEvent)


def test_umlmodel_changeevent_constructor_exists():
    assert callable(UMLModel_ChangeEvent.__init__)


def test_umlmodel_changeevent_constructor_args():
    sig = inspect.signature(UMLModel_ChangeEvent.__init__)
    params = list(sig.parameters.keys())



def test_templateparameter_is_not_abstract():
    assert not inspect.isabstract(TemplateParameter)


def test_templateparameter_constructor_exists():
    assert callable(TemplateParameter.__init__)


def test_templateparameter_constructor_args():
    sig = inspect.signature(TemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_connectableelementtemplateparameter_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ConnectableElementTemplateParameter)


def test_umlmodel_connectableelementtemplateparameter_constructor_exists():
    assert callable(UMLModel_ConnectableElementTemplateParameter.__init__)


def test_umlmodel_connectableelementtemplateparameter_constructor_args():
    sig = inspect.signature(UMLModel_ConnectableElementTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_operationtemplateparameter_is_not_abstract():
    assert not inspect.isabstract(UMLModel_OperationTemplateParameter)


def test_umlmodel_operationtemplateparameter_constructor_exists():
    assert callable(UMLModel_OperationTemplateParameter.__init__)


def test_umlmodel_operationtemplateparameter_constructor_args():
    sig = inspect.signature(UMLModel_OperationTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_classifiertemplateparameter_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ClassifierTemplateParameter)


def test_umlmodel_classifiertemplateparameter_constructor_exists():
    assert callable(UMLModel_ClassifierTemplateParameter.__init__)


def test_umlmodel_classifiertemplateparameter_constructor_args():
    sig = inspect.signature(UMLModel_ClassifierTemplateParameter.__init__)
    params = list(sig.parameters.keys())
    assert "constrainingClassifier" in params, "Missing parameter 'constrainingClassifier'"
    assert "defaultClassifier" in params, "Missing parameter 'defaultClassifier'"
    assert "allowSubstitutable" in params, "Missing parameter 'allowSubstitutable'"

def test_umlmodel_classifiertemplateparameter_has_constrainingClassifier():
    assert hasattr(UMLModel_ClassifierTemplateParameter, "constrainingClassifier")
    descriptor = None
    for klass in UMLModel_ClassifierTemplateParameter.__mro__:
        if "constrainingClassifier" in klass.__dict__:
            descriptor = klass.__dict__["constrainingClassifier"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_classifiertemplateparameter_has_defaultClassifier():
    assert hasattr(UMLModel_ClassifierTemplateParameter, "defaultClassifier")
    descriptor = None
    for klass in UMLModel_ClassifierTemplateParameter.__mro__:
        if "defaultClassifier" in klass.__dict__:
            descriptor = klass.__dict__["defaultClassifier"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_classifiertemplateparameter_has_allowSubstitutable():
    assert hasattr(UMLModel_ClassifierTemplateParameter, "allowSubstitutable")
    descriptor = None
    for klass in UMLModel_ClassifierTemplateParameter.__mro__:
        if "allowSubstitutable" in klass.__dict__:
            descriptor = klass.__dict__["allowSubstitutable"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_collaborationuse_is_not_abstract():
    assert not inspect.isabstract(UMLModel_CollaborationUse)


def test_umlmodel_collaborationuse_constructor_exists():
    assert callable(UMLModel_CollaborationUse.__init__)


def test_umlmodel_collaborationuse_constructor_args():
    sig = inspect.signature(UMLModel_CollaborationUse.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_umlmodel_collaborationuse_has_type():
    assert hasattr(UMLModel_CollaborationUse, "type")
    descriptor = None
    for klass in UMLModel_CollaborationUse.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_substitution_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Substitution)


def test_umlmodel_substitution_constructor_exists():
    assert callable(UMLModel_Substitution.__init__)


def test_umlmodel_substitution_constructor_args():
    sig = inspect.signature(UMLModel_Substitution.__init__)
    params = list(sig.parameters.keys())
    assert "substitutingClassifier" in params, "Missing parameter 'substitutingClassifier'"
    assert "contract" in params, "Missing parameter 'contract'"

def test_umlmodel_substitution_has_substitutingClassifier():
    assert hasattr(UMLModel_Substitution, "substitutingClassifier")
    descriptor = None
    for klass in UMLModel_Substitution.__mro__:
        if "substitutingClassifier" in klass.__dict__:
            descriptor = klass.__dict__["substitutingClassifier"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_substitution_has_contract():
    assert hasattr(UMLModel_Substitution, "contract")
    descriptor = None
    for klass in UMLModel_Substitution.__mro__:
        if "contract" in klass.__dict__:
            descriptor = klass.__dict__["contract"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_interfacerealization_is_not_abstract():
    assert not inspect.isabstract(UMLModel_InterfaceRealization)


def test_umlmodel_interfacerealization_constructor_exists():
    assert callable(UMLModel_InterfaceRealization.__init__)


def test_umlmodel_interfacerealization_constructor_args():
    sig = inspect.signature(UMLModel_InterfaceRealization.__init__)
    params = list(sig.parameters.keys())
    assert "realizingClassifier" in params, "Missing parameter 'realizingClassifier'"
    assert "contract" in params, "Missing parameter 'contract'"

def test_umlmodel_interfacerealization_has_realizingClassifier():
    assert hasattr(UMLModel_InterfaceRealization, "realizingClassifier")
    descriptor = None
    for klass in UMLModel_InterfaceRealization.__mro__:
        if "realizingClassifier" in klass.__dict__:
            descriptor = klass.__dict__["realizingClassifier"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_interfacerealization_has_contract():
    assert hasattr(UMLModel_InterfaceRealization, "contract")
    descriptor = None
    for klass in UMLModel_InterfaceRealization.__mro__:
        if "contract" in klass.__dict__:
            descriptor = klass.__dict__["contract"]
            break
    assert isinstance(descriptor, property)



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(UMLModel_StructuralFeature)


def test_umlmodel_structuralfeature_constructor_exists():
    assert callable(UMLModel_StructuralFeature.__init__)


def test_umlmodel_structuralfeature_constructor_args():
    sig = inspect.signature(UMLModel_StructuralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"

def test_umlmodel_structuralfeature_has_isReadOnly():
    assert hasattr(UMLModel_StructuralFeature, "isReadOnly")
    descriptor = None
    for klass in UMLModel_StructuralFeature.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_connector_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Connector)


def test_umlmodel_connector_constructor_exists():
    assert callable(UMLModel_Connector.__init__)


def test_umlmodel_connector_constructor_args():
    sig = inspect.signature(UMLModel_Connector.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "redefinedConnector" in params, "Missing parameter 'redefinedConnector'"
    assert "contract" in params, "Missing parameter 'contract'"
    assert "type" in params, "Missing parameter 'type'"

def test_umlmodel_connector_has_kind():
    assert hasattr(UMLModel_Connector, "kind")
    descriptor = None
    for klass in UMLModel_Connector.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_connector_has_redefinedConnector():
    assert hasattr(UMLModel_Connector, "redefinedConnector")
    descriptor = None
    for klass in UMLModel_Connector.__mro__:
        if "redefinedConnector" in klass.__dict__:
            descriptor = klass.__dict__["redefinedConnector"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_connector_has_contract():
    assert hasattr(UMLModel_Connector, "contract")
    descriptor = None
    for klass in UMLModel_Connector.__mro__:
        if "contract" in klass.__dict__:
            descriptor = klass.__dict__["contract"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_connector_has_type():
    assert hasattr(UMLModel_Connector, "type")
    descriptor = None
    for klass in UMLModel_Connector.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_namespace_is_not_abstract():
    assert not inspect.isabstract(Namespace)


def test_namespace_constructor_exists():
    assert callable(Namespace.__init__)


def test_namespace_constructor_args():
    sig = inspect.signature(Namespace.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_package_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Package)


def test_umlmodel_package_constructor_exists():
    assert callable(UMLModel_Package.__init__)


def test_umlmodel_package_constructor_args():
    sig = inspect.signature(UMLModel_Package.__init__)
    params = list(sig.parameters.keys())
    assert "nestedPackage" in params, "Missing parameter 'nestedPackage'"
    assert "ownedType" in params, "Missing parameter 'ownedType'"
    assert "nestingPackage" in params, "Missing parameter 'nestingPackage'"

def test_umlmodel_package_has_nestedPackage():
    assert hasattr(UMLModel_Package, "nestedPackage")
    descriptor = None
    for klass in UMLModel_Package.__mro__:
        if "nestedPackage" in klass.__dict__:
            descriptor = klass.__dict__["nestedPackage"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_package_has_ownedType():
    assert hasattr(UMLModel_Package, "ownedType")
    descriptor = None
    for klass in UMLModel_Package.__mro__:
        if "ownedType" in klass.__dict__:
            descriptor = klass.__dict__["ownedType"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_package_has_nestingPackage():
    assert hasattr(UMLModel_Package, "nestingPackage")
    descriptor = None
    for klass in UMLModel_Package.__mro__:
        if "nestingPackage" in klass.__dict__:
            descriptor = klass.__dict__["nestingPackage"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_interactionoperand_is_not_abstract():
    assert not inspect.isabstract(UMLModel_InteractionOperand)


def test_umlmodel_interactionoperand_constructor_exists():
    assert callable(UMLModel_InteractionOperand.__init__)


def test_umlmodel_interactionoperand_constructor_args():
    sig = inspect.signature(UMLModel_InteractionOperand.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_transition_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Transition)


def test_umlmodel_transition_constructor_exists():
    assert callable(UMLModel_Transition.__init__)


def test_umlmodel_transition_constructor_args():
    sig = inspect.signature(UMLModel_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "target" in params, "Missing parameter 'target'"
    assert "kind" in params, "Missing parameter 'kind'"
    assert "source" in params, "Missing parameter 'source'"
    assert "guard" in params, "Missing parameter 'guard'"
    assert "redefinedTransition" in params, "Missing parameter 'redefinedTransition'"
    assert "container" in params, "Missing parameter 'container'"

def test_umlmodel_transition_has_target():
    assert hasattr(UMLModel_Transition, "target")
    descriptor = None
    for klass in UMLModel_Transition.__mro__:
        if "target" in klass.__dict__:
            descriptor = klass.__dict__["target"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_transition_has_kind():
    assert hasattr(UMLModel_Transition, "kind")
    descriptor = None
    for klass in UMLModel_Transition.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_transition_has_source():
    assert hasattr(UMLModel_Transition, "source")
    descriptor = None
    for klass in UMLModel_Transition.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_transition_has_guard():
    assert hasattr(UMLModel_Transition, "guard")
    descriptor = None
    for klass in UMLModel_Transition.__mro__:
        if "guard" in klass.__dict__:
            descriptor = klass.__dict__["guard"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_transition_has_redefinedTransition():
    assert hasattr(UMLModel_Transition, "redefinedTransition")
    descriptor = None
    for klass in UMLModel_Transition.__mro__:
        if "redefinedTransition" in klass.__dict__:
            descriptor = klass.__dict__["redefinedTransition"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_transition_has_container():
    assert hasattr(UMLModel_Transition, "container")
    descriptor = None
    for klass in UMLModel_Transition.__mro__:
        if "container" in klass.__dict__:
            descriptor = klass.__dict__["container"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_state_is_not_abstract():
    assert not inspect.isabstract(UMLModel_State)


def test_umlmodel_state_constructor_exists():
    assert callable(UMLModel_State.__init__)


def test_umlmodel_state_constructor_args():
    sig = inspect.signature(UMLModel_State.__init__)
    params = list(sig.parameters.keys())
    assert "isSimple" in params, "Missing parameter 'isSimple'"
    assert "isSubmachineState" in params, "Missing parameter 'isSubmachineState'"
    assert "submachine" in params, "Missing parameter 'submachine'"
    assert "redefinedState" in params, "Missing parameter 'redefinedState'"
    assert "isOrthogonal" in params, "Missing parameter 'isOrthogonal'"
    assert "isComposite" in params, "Missing parameter 'isComposite'"

def test_umlmodel_state_has_isSimple():
    assert hasattr(UMLModel_State, "isSimple")
    descriptor = None
    for klass in UMLModel_State.__mro__:
        if "isSimple" in klass.__dict__:
            descriptor = klass.__dict__["isSimple"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_state_has_isSubmachineState():
    assert hasattr(UMLModel_State, "isSubmachineState")
    descriptor = None
    for klass in UMLModel_State.__mro__:
        if "isSubmachineState" in klass.__dict__:
            descriptor = klass.__dict__["isSubmachineState"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_state_has_submachine():
    assert hasattr(UMLModel_State, "submachine")
    descriptor = None
    for klass in UMLModel_State.__mro__:
        if "submachine" in klass.__dict__:
            descriptor = klass.__dict__["submachine"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_state_has_redefinedState():
    assert hasattr(UMLModel_State, "redefinedState")
    descriptor = None
    for klass in UMLModel_State.__mro__:
        if "redefinedState" in klass.__dict__:
            descriptor = klass.__dict__["redefinedState"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_state_has_isOrthogonal():
    assert hasattr(UMLModel_State, "isOrthogonal")
    descriptor = None
    for klass in UMLModel_State.__mro__:
        if "isOrthogonal" in klass.__dict__:
            descriptor = klass.__dict__["isOrthogonal"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_state_has_isComposite():
    assert hasattr(UMLModel_State, "isComposite")
    descriptor = None
    for klass in UMLModel_State.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(UMLModel_StructuredActivityNode)


def test_umlmodel_structuredactivitynode_constructor_exists():
    assert callable(UMLModel_StructuredActivityNode.__init__)


def test_umlmodel_structuredactivitynode_constructor_args():
    sig = inspect.signature(UMLModel_StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())
    assert "mustIsolate" in params, "Missing parameter 'mustIsolate'"

def test_umlmodel_structuredactivitynode_has_mustIsolate():
    assert hasattr(UMLModel_StructuredActivityNode, "mustIsolate")
    descriptor = None
    for klass in UMLModel_StructuredActivityNode.__mro__:
        if "mustIsolate" in klass.__dict__:
            descriptor = klass.__dict__["mustIsolate"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_region_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Region)


def test_umlmodel_region_constructor_exists():
    assert callable(UMLModel_Region.__init__)


def test_umlmodel_region_constructor_args():
    sig = inspect.signature(UMLModel_Region.__init__)
    params = list(sig.parameters.keys())
    assert "state" in params, "Missing parameter 'state'"
    assert "extendedRegion" in params, "Missing parameter 'extendedRegion'"
    assert "stateMachine" in params, "Missing parameter 'stateMachine'"

def test_umlmodel_region_has_state():
    assert hasattr(UMLModel_Region, "state")
    descriptor = None
    for klass in UMLModel_Region.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_region_has_extendedRegion():
    assert hasattr(UMLModel_Region, "extendedRegion")
    descriptor = None
    for klass in UMLModel_Region.__mro__:
        if "extendedRegion" in klass.__dict__:
            descriptor = klass.__dict__["extendedRegion"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_region_has_stateMachine():
    assert hasattr(UMLModel_Region, "stateMachine")
    descriptor = None
    for klass in UMLModel_Region.__mro__:
        if "stateMachine" in klass.__dict__:
            descriptor = klass.__dict__["stateMachine"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_classifier_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Classifier)


def test_umlmodel_classifier_constructor_exists():
    assert callable(UMLModel_Classifier.__init__)


def test_umlmodel_classifier_constructor_args():
    sig = inspect.signature(UMLModel_Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "general" in params, "Missing parameter 'general'"
    assert "inheritedMember" in params, "Missing parameter 'inheritedMember'"
    assert "representation" in params, "Missing parameter 'representation'"
    assert "redefinedClassifier" in params, "Missing parameter 'redefinedClassifier'"
    assert "feature" in params, "Missing parameter 'feature'"
    assert "useCase" in params, "Missing parameter 'useCase'"
    assert "powertypeExtent" in params, "Missing parameter 'powertypeExtent'"
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"
    assert "attribute" in params, "Missing parameter 'attribute'"

def test_umlmodel_classifier_has_general():
    assert hasattr(UMLModel_Classifier, "general")
    descriptor = None
    for klass in UMLModel_Classifier.__mro__:
        if "general" in klass.__dict__:
            descriptor = klass.__dict__["general"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_classifier_has_inheritedMember():
    assert hasattr(UMLModel_Classifier, "inheritedMember")
    descriptor = None
    for klass in UMLModel_Classifier.__mro__:
        if "inheritedMember" in klass.__dict__:
            descriptor = klass.__dict__["inheritedMember"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_classifier_has_representation():
    assert hasattr(UMLModel_Classifier, "representation")
    descriptor = None
    for klass in UMLModel_Classifier.__mro__:
        if "representation" in klass.__dict__:
            descriptor = klass.__dict__["representation"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_classifier_has_redefinedClassifier():
    assert hasattr(UMLModel_Classifier, "redefinedClassifier")
    descriptor = None
    for klass in UMLModel_Classifier.__mro__:
        if "redefinedClassifier" in klass.__dict__:
            descriptor = klass.__dict__["redefinedClassifier"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_classifier_has_feature():
    assert hasattr(UMLModel_Classifier, "feature")
    descriptor = None
    for klass in UMLModel_Classifier.__mro__:
        if "feature" in klass.__dict__:
            descriptor = klass.__dict__["feature"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_classifier_has_useCase():
    assert hasattr(UMLModel_Classifier, "useCase")
    descriptor = None
    for klass in UMLModel_Classifier.__mro__:
        if "useCase" in klass.__dict__:
            descriptor = klass.__dict__["useCase"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_classifier_has_powertypeExtent():
    assert hasattr(UMLModel_Classifier, "powertypeExtent")
    descriptor = None
    for klass in UMLModel_Classifier.__mro__:
        if "powertypeExtent" in klass.__dict__:
            descriptor = klass.__dict__["powertypeExtent"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_classifier_has_isAbstract():
    assert hasattr(UMLModel_Classifier, "isAbstract")
    descriptor = None
    for klass in UMLModel_Classifier.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_classifier_has_attribute():
    assert hasattr(UMLModel_Classifier, "attribute")
    descriptor = None
    for klass in UMLModel_Classifier.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(UMLModel_BehavioralFeature)


def test_umlmodel_behavioralfeature_constructor_exists():
    assert callable(UMLModel_BehavioralFeature.__init__)


def test_umlmodel_behavioralfeature_constructor_args():
    sig = inspect.signature(UMLModel_BehavioralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "raisedException" in params, "Missing parameter 'raisedException'"
    assert "concurrency" in params, "Missing parameter 'concurrency'"
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"
    assert "method" in params, "Missing parameter 'method'"

def test_umlmodel_behavioralfeature_has_raisedException():
    assert hasattr(UMLModel_BehavioralFeature, "raisedException")
    descriptor = None
    for klass in UMLModel_BehavioralFeature.__mro__:
        if "raisedException" in klass.__dict__:
            descriptor = klass.__dict__["raisedException"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_behavioralfeature_has_concurrency():
    assert hasattr(UMLModel_BehavioralFeature, "concurrency")
    descriptor = None
    for klass in UMLModel_BehavioralFeature.__mro__:
        if "concurrency" in klass.__dict__:
            descriptor = klass.__dict__["concurrency"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_behavioralfeature_has_isAbstract():
    assert hasattr(UMLModel_BehavioralFeature, "isAbstract")
    descriptor = None
    for klass in UMLModel_BehavioralFeature.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_behavioralfeature_has_method():
    assert hasattr(UMLModel_BehavioralFeature, "method")
    descriptor = None
    for klass in UMLModel_BehavioralFeature.__mro__:
        if "method" in klass.__dict__:
            descriptor = klass.__dict__["method"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_behaviorexecutionspecification_is_not_abstract():
    assert not inspect.isabstract(UMLModel_BehaviorExecutionSpecification)


def test_umlmodel_behaviorexecutionspecification_constructor_exists():
    assert callable(UMLModel_BehaviorExecutionSpecification.__init__)


def test_umlmodel_behaviorexecutionspecification_constructor_args():
    sig = inspect.signature(UMLModel_BehaviorExecutionSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "behavior" in params, "Missing parameter 'behavior'"

def test_umlmodel_behaviorexecutionspecification_has_behavior():
    assert hasattr(UMLModel_BehaviorExecutionSpecification, "behavior")
    descriptor = None
    for klass in UMLModel_BehaviorExecutionSpecification.__mro__:
        if "behavior" in klass.__dict__:
            descriptor = klass.__dict__["behavior"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_parameterset_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ParameterSet)


def test_umlmodel_parameterset_constructor_exists():
    assert callable(UMLModel_ParameterSet.__init__)


def test_umlmodel_parameterset_constructor_args():
    sig = inspect.signature(UMLModel_ParameterSet.__init__)
    params = list(sig.parameters.keys())
    assert "parameter" in params, "Missing parameter 'parameter'"

def test_umlmodel_parameterset_has_parameter():
    assert hasattr(UMLModel_ParameterSet, "parameter")
    descriptor = None
    for klass in UMLModel_ParameterSet.__mro__:
        if "parameter" in klass.__dict__:
            descriptor = klass.__dict__["parameter"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_parameter_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Parameter)


def test_umlmodel_parameter_constructor_exists():
    assert callable(UMLModel_Parameter.__init__)


def test_umlmodel_parameter_constructor_args():
    sig = inspect.signature(UMLModel_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"
    assert "effect" in params, "Missing parameter 'effect'"
    assert "isStream" in params, "Missing parameter 'isStream'"
    assert "parameterSet" in params, "Missing parameter 'parameterSet'"
    assert "isException" in params, "Missing parameter 'isException'"
    assert "direction" in params, "Missing parameter 'direction'"
    assert "operation" in params, "Missing parameter 'operation'"

def test_umlmodel_parameter_has_default():
    assert hasattr(UMLModel_Parameter, "default")
    descriptor = None
    for klass in UMLModel_Parameter.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_parameter_has_effect():
    assert hasattr(UMLModel_Parameter, "effect")
    descriptor = None
    for klass in UMLModel_Parameter.__mro__:
        if "effect" in klass.__dict__:
            descriptor = klass.__dict__["effect"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_parameter_has_isStream():
    assert hasattr(UMLModel_Parameter, "isStream")
    descriptor = None
    for klass in UMLModel_Parameter.__mro__:
        if "isStream" in klass.__dict__:
            descriptor = klass.__dict__["isStream"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_parameter_has_parameterSet():
    assert hasattr(UMLModel_Parameter, "parameterSet")
    descriptor = None
    for klass in UMLModel_Parameter.__mro__:
        if "parameterSet" in klass.__dict__:
            descriptor = klass.__dict__["parameterSet"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_parameter_has_isException():
    assert hasattr(UMLModel_Parameter, "isException")
    descriptor = None
    for klass in UMLModel_Parameter.__mro__:
        if "isException" in klass.__dict__:
            descriptor = klass.__dict__["isException"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_parameter_has_direction():
    assert hasattr(UMLModel_Parameter, "direction")
    descriptor = None
    for klass in UMLModel_Parameter.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_parameter_has_operation():
    assert hasattr(UMLModel_Parameter, "operation")
    descriptor = None
    for klass in UMLModel_Parameter.__mro__:
        if "operation" in klass.__dict__:
            descriptor = klass.__dict__["operation"]
            break
    assert isinstance(descriptor, property)



def test_callaction_is_not_abstract():
    assert not inspect.isabstract(CallAction)


def test_callaction_constructor_exists():
    assert callable(CallAction.__init__)


def test_callaction_constructor_args():
    sig = inspect.signature(CallAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_calloperationaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel_CallOperationAction)


def test_umlmodel_calloperationaction_constructor_exists():
    assert callable(UMLModel_CallOperationAction.__init__)


def test_umlmodel_calloperationaction_constructor_args():
    sig = inspect.signature(UMLModel_CallOperationAction.__init__)
    params = list(sig.parameters.keys())
    assert "operation" in params, "Missing parameter 'operation'"

def test_umlmodel_calloperationaction_has_operation():
    assert hasattr(UMLModel_CallOperationAction, "operation")
    descriptor = None
    for klass in UMLModel_CallOperationAction.__mro__:
        if "operation" in klass.__dict__:
            descriptor = klass.__dict__["operation"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_callbehavioraction_is_not_abstract():
    assert not inspect.isabstract(UMLModel_CallBehaviorAction)


def test_umlmodel_callbehavioraction_constructor_exists():
    assert callable(UMLModel_CallBehaviorAction.__init__)


def test_umlmodel_callbehavioraction_constructor_args():
    sig = inspect.signature(UMLModel_CallBehaviorAction.__init__)
    params = list(sig.parameters.keys())
    assert "behavior" in params, "Missing parameter 'behavior'"

def test_umlmodel_callbehavioraction_has_behavior():
    assert hasattr(UMLModel_CallBehaviorAction, "behavior")
    descriptor = None
    for klass in UMLModel_CallBehaviorAction.__mro__:
        if "behavior" in klass.__dict__:
            descriptor = klass.__dict__["behavior"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_property_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Property)


def test_umlmodel_property_constructor_exists():
    assert callable(UMLModel_Property.__init__)


def test_umlmodel_property_constructor_args():
    sig = inspect.signature(UMLModel_Property.__init__)
    params = list(sig.parameters.keys())
    assert "association" in params, "Missing parameter 'association'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "opposite" in params, "Missing parameter 'opposite'"
    assert "isComposite" in params, "Missing parameter 'isComposite'"
    assert "owningAssociation" in params, "Missing parameter 'owningAssociation'"
    assert "subsettedProperty" in params, "Missing parameter 'subsettedProperty'"
    assert "aggregation" in params, "Missing parameter 'aggregation'"
    assert "associationEnd" in params, "Missing parameter 'associationEnd'"
    assert "datatype" in params, "Missing parameter 'datatype'"
    assert "isDerived" in params, "Missing parameter 'isDerived'"
    assert "default" in params, "Missing parameter 'default'"
    assert "redefinedProperty" in params, "Missing parameter 'redefinedProperty'"
    assert "isDerivedUnion" in params, "Missing parameter 'isDerivedUnion'"

def test_umlmodel_property_has_association():
    assert hasattr(UMLModel_Property, "association")
    descriptor = None
    for klass in UMLModel_Property.__mro__:
        if "association" in klass.__dict__:
            descriptor = klass.__dict__["association"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_property_has_class_():
    assert hasattr(UMLModel_Property, "class_")
    descriptor = None
    for klass in UMLModel_Property.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_property_has_opposite():
    assert hasattr(UMLModel_Property, "opposite")
    descriptor = None
    for klass in UMLModel_Property.__mro__:
        if "opposite" in klass.__dict__:
            descriptor = klass.__dict__["opposite"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_property_has_isComposite():
    assert hasattr(UMLModel_Property, "isComposite")
    descriptor = None
    for klass in UMLModel_Property.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_property_has_owningAssociation():
    assert hasattr(UMLModel_Property, "owningAssociation")
    descriptor = None
    for klass in UMLModel_Property.__mro__:
        if "owningAssociation" in klass.__dict__:
            descriptor = klass.__dict__["owningAssociation"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_property_has_subsettedProperty():
    assert hasattr(UMLModel_Property, "subsettedProperty")
    descriptor = None
    for klass in UMLModel_Property.__mro__:
        if "subsettedProperty" in klass.__dict__:
            descriptor = klass.__dict__["subsettedProperty"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_property_has_aggregation():
    assert hasattr(UMLModel_Property, "aggregation")
    descriptor = None
    for klass in UMLModel_Property.__mro__:
        if "aggregation" in klass.__dict__:
            descriptor = klass.__dict__["aggregation"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_property_has_associationEnd():
    assert hasattr(UMLModel_Property, "associationEnd")
    descriptor = None
    for klass in UMLModel_Property.__mro__:
        if "associationEnd" in klass.__dict__:
            descriptor = klass.__dict__["associationEnd"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_property_has_datatype():
    assert hasattr(UMLModel_Property, "datatype")
    descriptor = None
    for klass in UMLModel_Property.__mro__:
        if "datatype" in klass.__dict__:
            descriptor = klass.__dict__["datatype"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_property_has_isDerived():
    assert hasattr(UMLModel_Property, "isDerived")
    descriptor = None
    for klass in UMLModel_Property.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_property_has_default():
    assert hasattr(UMLModel_Property, "default")
    descriptor = None
    for klass in UMLModel_Property.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_property_has_redefinedProperty():
    assert hasattr(UMLModel_Property, "redefinedProperty")
    descriptor = None
    for klass in UMLModel_Property.__mro__:
        if "redefinedProperty" in klass.__dict__:
            descriptor = klass.__dict__["redefinedProperty"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_property_has_isDerivedUnion():
    assert hasattr(UMLModel_Property, "isDerivedUnion")
    descriptor = None
    for klass in UMLModel_Property.__mro__:
        if "isDerivedUnion" in klass.__dict__:
            descriptor = klass.__dict__["isDerivedUnion"]
            break
    assert isinstance(descriptor, property)



def test_invocationaction_is_not_abstract():
    assert not inspect.isabstract(InvocationAction)


def test_invocationaction_constructor_exists():
    assert callable(InvocationAction.__init__)


def test_invocationaction_constructor_args():
    sig = inspect.signature(InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_sendobjectaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel_SendObjectAction)


def test_umlmodel_sendobjectaction_constructor_exists():
    assert callable(UMLModel_SendObjectAction.__init__)


def test_umlmodel_sendobjectaction_constructor_args():
    sig = inspect.signature(UMLModel_SendObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_callaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel_CallAction)


def test_umlmodel_callaction_constructor_exists():
    assert callable(UMLModel_CallAction.__init__)


def test_umlmodel_callaction_constructor_args():
    sig = inspect.signature(UMLModel_CallAction.__init__)
    params = list(sig.parameters.keys())
    assert "isSynchronous" in params, "Missing parameter 'isSynchronous'"

def test_umlmodel_callaction_has_isSynchronous():
    assert hasattr(UMLModel_CallAction, "isSynchronous")
    descriptor = None
    for klass in UMLModel_CallAction.__mro__:
        if "isSynchronous" in klass.__dict__:
            descriptor = klass.__dict__["isSynchronous"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_sendsignalaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel_SendSignalAction)


def test_umlmodel_sendsignalaction_constructor_exists():
    assert callable(UMLModel_SendSignalAction.__init__)


def test_umlmodel_sendsignalaction_constructor_args():
    sig = inspect.signature(UMLModel_SendSignalAction.__init__)
    params = list(sig.parameters.keys())
    assert "signal" in params, "Missing parameter 'signal'"

def test_umlmodel_sendsignalaction_has_signal():
    assert hasattr(UMLModel_SendSignalAction, "signal")
    descriptor = None
    for klass in UMLModel_SendSignalAction.__mro__:
        if "signal" in klass.__dict__:
            descriptor = klass.__dict__["signal"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_broadcastsignalaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel_BroadcastSignalAction)


def test_umlmodel_broadcastsignalaction_constructor_exists():
    assert callable(UMLModel_BroadcastSignalAction.__init__)


def test_umlmodel_broadcastsignalaction_constructor_args():
    sig = inspect.signature(UMLModel_BroadcastSignalAction.__init__)
    params = list(sig.parameters.keys())
    assert "signal" in params, "Missing parameter 'signal'"

def test_umlmodel_broadcastsignalaction_has_signal():
    assert hasattr(UMLModel_BroadcastSignalAction, "signal")
    descriptor = None
    for klass in UMLModel_BroadcastSignalAction.__mro__:
        if "signal" in klass.__dict__:
            descriptor = klass.__dict__["signal"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_operation_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Operation)


def test_umlmodel_operation_constructor_exists():
    assert callable(UMLModel_Operation.__init__)


def test_umlmodel_operation_constructor_args():
    sig = inspect.signature(UMLModel_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "isQuery" in params, "Missing parameter 'isQuery'"
    assert "upper" in params, "Missing parameter 'upper'"
    assert "lower" in params, "Missing parameter 'lower'"
    assert "isUnique" in params, "Missing parameter 'isUnique'"
    assert "interface" in params, "Missing parameter 'interface'"
    assert "datatype" in params, "Missing parameter 'datatype'"
    assert "postcondition" in params, "Missing parameter 'postcondition'"
    assert "bodyCondition" in params, "Missing parameter 'bodyCondition'"
    assert "redefinedOperation" in params, "Missing parameter 'redefinedOperation'"
    assert "type" in params, "Missing parameter 'type'"
    assert "precondition" in params, "Missing parameter 'precondition'"
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"
    assert "class_" in params, "Missing parameter 'class_'"

def test_umlmodel_operation_has_isQuery():
    assert hasattr(UMLModel_Operation, "isQuery")
    descriptor = None
    for klass in UMLModel_Operation.__mro__:
        if "isQuery" in klass.__dict__:
            descriptor = klass.__dict__["isQuery"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_operation_has_upper():
    assert hasattr(UMLModel_Operation, "upper")
    descriptor = None
    for klass in UMLModel_Operation.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_operation_has_lower():
    assert hasattr(UMLModel_Operation, "lower")
    descriptor = None
    for klass in UMLModel_Operation.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_operation_has_isUnique():
    assert hasattr(UMLModel_Operation, "isUnique")
    descriptor = None
    for klass in UMLModel_Operation.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_operation_has_interface():
    assert hasattr(UMLModel_Operation, "interface")
    descriptor = None
    for klass in UMLModel_Operation.__mro__:
        if "interface" in klass.__dict__:
            descriptor = klass.__dict__["interface"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_operation_has_datatype():
    assert hasattr(UMLModel_Operation, "datatype")
    descriptor = None
    for klass in UMLModel_Operation.__mro__:
        if "datatype" in klass.__dict__:
            descriptor = klass.__dict__["datatype"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_operation_has_postcondition():
    assert hasattr(UMLModel_Operation, "postcondition")
    descriptor = None
    for klass in UMLModel_Operation.__mro__:
        if "postcondition" in klass.__dict__:
            descriptor = klass.__dict__["postcondition"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_operation_has_bodyCondition():
    assert hasattr(UMLModel_Operation, "bodyCondition")
    descriptor = None
    for klass in UMLModel_Operation.__mro__:
        if "bodyCondition" in klass.__dict__:
            descriptor = klass.__dict__["bodyCondition"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_operation_has_redefinedOperation():
    assert hasattr(UMLModel_Operation, "redefinedOperation")
    descriptor = None
    for klass in UMLModel_Operation.__mro__:
        if "redefinedOperation" in klass.__dict__:
            descriptor = klass.__dict__["redefinedOperation"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_operation_has_type():
    assert hasattr(UMLModel_Operation, "type")
    descriptor = None
    for klass in UMLModel_Operation.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_operation_has_precondition():
    assert hasattr(UMLModel_Operation, "precondition")
    descriptor = None
    for klass in UMLModel_Operation.__mro__:
        if "precondition" in klass.__dict__:
            descriptor = klass.__dict__["precondition"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_operation_has_isOrdered():
    assert hasattr(UMLModel_Operation, "isOrdered")
    descriptor = None
    for klass in UMLModel_Operation.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_operation_has_class_():
    assert hasattr(UMLModel_Operation, "class_")
    descriptor = None
    for klass in UMLModel_Operation.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_manifestation_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Manifestation)


def test_umlmodel_manifestation_constructor_exists():
    assert callable(UMLModel_Manifestation.__init__)


def test_umlmodel_manifestation_constructor_args():
    sig = inspect.signature(UMLModel_Manifestation.__init__)
    params = list(sig.parameters.keys())
    assert "utilizedElement" in params, "Missing parameter 'utilizedElement'"

def test_umlmodel_manifestation_has_utilizedElement():
    assert hasattr(UMLModel_Manifestation, "utilizedElement")
    descriptor = None
    for klass in UMLModel_Manifestation.__mro__:
        if "utilizedElement" in klass.__dict__:
            descriptor = klass.__dict__["utilizedElement"]
            break
    assert isinstance(descriptor, property)



def test_deployedartifact_is_not_abstract():
    assert not inspect.isabstract(DeployedArtifact)


def test_deployedartifact_constructor_exists():
    assert callable(DeployedArtifact.__init__)


def test_deployedartifact_constructor_args():
    sig = inspect.signature(DeployedArtifact.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_instancespecification_is_not_abstract():
    assert not inspect.isabstract(UMLModel_InstanceSpecification)


def test_umlmodel_instancespecification_constructor_exists():
    assert callable(UMLModel_InstanceSpecification.__init__)


def test_umlmodel_instancespecification_constructor_args():
    sig = inspect.signature(UMLModel_InstanceSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "classifier" in params, "Missing parameter 'classifier'"

def test_umlmodel_instancespecification_has_classifier():
    assert hasattr(UMLModel_InstanceSpecification, "classifier")
    descriptor = None
    for klass in UMLModel_InstanceSpecification.__mro__:
        if "classifier" in klass.__dict__:
            descriptor = klass.__dict__["classifier"]
            break
    assert isinstance(descriptor, property)



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_structuredclassifier_is_not_abstract():
    assert not inspect.isabstract(UMLModel_StructuredClassifier)


def test_umlmodel_structuredclassifier_constructor_exists():
    assert callable(UMLModel_StructuredClassifier.__init__)


def test_umlmodel_structuredclassifier_constructor_args():
    sig = inspect.signature(UMLModel_StructuredClassifier.__init__)
    params = list(sig.parameters.keys())
    assert "part" in params, "Missing parameter 'part'"
    assert "role" in params, "Missing parameter 'role'"

def test_umlmodel_structuredclassifier_has_part():
    assert hasattr(UMLModel_StructuredClassifier, "part")
    descriptor = None
    for klass in UMLModel_StructuredClassifier.__mro__:
        if "part" in klass.__dict__:
            descriptor = klass.__dict__["part"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_structuredclassifier_has_role():
    assert hasattr(UMLModel_StructuredClassifier, "role")
    descriptor = None
    for klass in UMLModel_StructuredClassifier.__mro__:
        if "role" in klass.__dict__:
            descriptor = klass.__dict__["role"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_signal_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Signal)


def test_umlmodel_signal_constructor_exists():
    assert callable(UMLModel_Signal.__init__)


def test_umlmodel_signal_constructor_args():
    sig = inspect.signature(UMLModel_Signal.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_datatype_is_not_abstract():
    assert not inspect.isabstract(UMLModel_DataType)


def test_umlmodel_datatype_constructor_exists():
    assert callable(UMLModel_DataType.__init__)


def test_umlmodel_datatype_constructor_args():
    sig = inspect.signature(UMLModel_DataType.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(UMLModel_BehavioredClassifier)


def test_umlmodel_behavioredclassifier_constructor_exists():
    assert callable(UMLModel_BehavioredClassifier.__init__)


def test_umlmodel_behavioredclassifier_constructor_args():
    sig = inspect.signature(UMLModel_BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())
    assert "classifierBehavior" in params, "Missing parameter 'classifierBehavior'"

def test_umlmodel_behavioredclassifier_has_classifierBehavior():
    assert hasattr(UMLModel_BehavioredClassifier, "classifierBehavior")
    descriptor = None
    for klass in UMLModel_BehavioredClassifier.__mro__:
        if "classifierBehavior" in klass.__dict__:
            descriptor = klass.__dict__["classifierBehavior"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_interface_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Interface)


def test_umlmodel_interface_constructor_exists():
    assert callable(UMLModel_Interface.__init__)


def test_umlmodel_interface_constructor_args():
    sig = inspect.signature(UMLModel_Interface.__init__)
    params = list(sig.parameters.keys())
    assert "redefinedInterface" in params, "Missing parameter 'redefinedInterface'"
    assert "isActive" in params, "Missing parameter 'isActive'"

def test_umlmodel_interface_has_redefinedInterface():
    assert hasattr(UMLModel_Interface, "redefinedInterface")
    descriptor = None
    for klass in UMLModel_Interface.__mro__:
        if "redefinedInterface" in klass.__dict__:
            descriptor = klass.__dict__["redefinedInterface"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_interface_has_isActive():
    assert hasattr(UMLModel_Interface, "isActive")
    descriptor = None
    for klass in UMLModel_Interface.__mro__:
        if "isActive" in klass.__dict__:
            descriptor = klass.__dict__["isActive"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_informationitem_is_not_abstract():
    assert not inspect.isabstract(UMLModel_InformationItem)


def test_umlmodel_informationitem_constructor_exists():
    assert callable(UMLModel_InformationItem.__init__)


def test_umlmodel_informationitem_constructor_args():
    sig = inspect.signature(UMLModel_InformationItem.__init__)
    params = list(sig.parameters.keys())
    assert "represented" in params, "Missing parameter 'represented'"

def test_umlmodel_informationitem_has_represented():
    assert hasattr(UMLModel_InformationItem, "represented")
    descriptor = None
    for klass in UMLModel_InformationItem.__mro__:
        if "represented" in klass.__dict__:
            descriptor = klass.__dict__["represented"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_artifact_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Artifact)


def test_umlmodel_artifact_constructor_exists():
    assert callable(UMLModel_Artifact.__init__)


def test_umlmodel_artifact_constructor_args():
    sig = inspect.signature(UMLModel_Artifact.__init__)
    params = list(sig.parameters.keys())
    assert "fileName" in params, "Missing parameter 'fileName'"

def test_umlmodel_artifact_has_fileName():
    assert hasattr(UMLModel_Artifact, "fileName")
    descriptor = None
    for klass in UMLModel_Artifact.__mro__:
        if "fileName" in klass.__dict__:
            descriptor = klass.__dict__["fileName"]
            break
    assert isinstance(descriptor, property)



def test_messageevent_is_not_abstract():
    assert not inspect.isabstract(MessageEvent)


def test_messageevent_constructor_exists():
    assert callable(MessageEvent.__init__)


def test_messageevent_constructor_args():
    sig = inspect.signature(MessageEvent.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_callevent_is_not_abstract():
    assert not inspect.isabstract(UMLModel_CallEvent)


def test_umlmodel_callevent_constructor_exists():
    assert callable(UMLModel_CallEvent.__init__)


def test_umlmodel_callevent_constructor_args():
    sig = inspect.signature(UMLModel_CallEvent.__init__)
    params = list(sig.parameters.keys())
    assert "operation" in params, "Missing parameter 'operation'"

def test_umlmodel_callevent_has_operation():
    assert hasattr(UMLModel_CallEvent, "operation")
    descriptor = None
    for klass in UMLModel_CallEvent.__mro__:
        if "operation" in klass.__dict__:
            descriptor = klass.__dict__["operation"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_receiveoperationevent_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ReceiveOperationEvent)


def test_umlmodel_receiveoperationevent_constructor_exists():
    assert callable(UMLModel_ReceiveOperationEvent.__init__)


def test_umlmodel_receiveoperationevent_constructor_args():
    sig = inspect.signature(UMLModel_ReceiveOperationEvent.__init__)
    params = list(sig.parameters.keys())
    assert "operation" in params, "Missing parameter 'operation'"

def test_umlmodel_receiveoperationevent_has_operation():
    assert hasattr(UMLModel_ReceiveOperationEvent, "operation")
    descriptor = None
    for klass in UMLModel_ReceiveOperationEvent.__mro__:
        if "operation" in klass.__dict__:
            descriptor = klass.__dict__["operation"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_receivesignalevent_is_not_abstract():
    assert not inspect.isabstract(UMLModel_ReceiveSignalEvent)


def test_umlmodel_receivesignalevent_constructor_exists():
    assert callable(UMLModel_ReceiveSignalEvent.__init__)


def test_umlmodel_receivesignalevent_constructor_args():
    sig = inspect.signature(UMLModel_ReceiveSignalEvent.__init__)
    params = list(sig.parameters.keys())
    assert "signal" in params, "Missing parameter 'signal'"

def test_umlmodel_receivesignalevent_has_signal():
    assert hasattr(UMLModel_ReceiveSignalEvent, "signal")
    descriptor = None
    for klass in UMLModel_ReceiveSignalEvent.__mro__:
        if "signal" in klass.__dict__:
            descriptor = klass.__dict__["signal"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_signalevent_is_not_abstract():
    assert not inspect.isabstract(UMLModel_SignalEvent)


def test_umlmodel_signalevent_constructor_exists():
    assert callable(UMLModel_SignalEvent.__init__)


def test_umlmodel_signalevent_constructor_args():
    sig = inspect.signature(UMLModel_SignalEvent.__init__)
    params = list(sig.parameters.keys())
    assert "signal" in params, "Missing parameter 'signal'"

def test_umlmodel_signalevent_has_signal():
    assert hasattr(UMLModel_SignalEvent, "signal")
    descriptor = None
    for klass in UMLModel_SignalEvent.__mro__:
        if "signal" in klass.__dict__:
            descriptor = klass.__dict__["signal"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_sendsignalevent_is_not_abstract():
    assert not inspect.isabstract(UMLModel_SendSignalEvent)


def test_umlmodel_sendsignalevent_constructor_exists():
    assert callable(UMLModel_SendSignalEvent.__init__)


def test_umlmodel_sendsignalevent_constructor_args():
    sig = inspect.signature(UMLModel_SendSignalEvent.__init__)
    params = list(sig.parameters.keys())
    assert "signal" in params, "Missing parameter 'signal'"

def test_umlmodel_sendsignalevent_has_signal():
    assert hasattr(UMLModel_SendSignalEvent, "signal")
    descriptor = None
    for klass in UMLModel_SendSignalEvent.__mro__:
        if "signal" in klass.__dict__:
            descriptor = klass.__dict__["signal"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_anyreceiveevent_is_not_abstract():
    assert not inspect.isabstract(UMLModel_AnyReceiveEvent)


def test_umlmodel_anyreceiveevent_constructor_exists():
    assert callable(UMLModel_AnyReceiveEvent.__init__)


def test_umlmodel_anyreceiveevent_constructor_args():
    sig = inspect.signature(UMLModel_AnyReceiveEvent.__init__)
    params = list(sig.parameters.keys())



def test_writevariableaction_is_not_abstract():
    assert not inspect.isabstract(WriteVariableAction)


def test_writevariableaction_constructor_exists():
    assert callable(WriteVariableAction.__init__)


def test_writevariableaction_constructor_args():
    sig = inspect.signature(WriteVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_removevariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel_RemoveVariableValueAction)


def test_umlmodel_removevariablevalueaction_constructor_exists():
    assert callable(UMLModel_RemoveVariableValueAction.__init__)


def test_umlmodel_removevariablevalueaction_constructor_args():
    sig = inspect.signature(UMLModel_RemoveVariableValueAction.__init__)
    params = list(sig.parameters.keys())
    assert "isRemoveDuplicates" in params, "Missing parameter 'isRemoveDuplicates'"

def test_umlmodel_removevariablevalueaction_has_isRemoveDuplicates():
    assert hasattr(UMLModel_RemoveVariableValueAction, "isRemoveDuplicates")
    descriptor = None
    for klass in UMLModel_RemoveVariableValueAction.__mro__:
        if "isRemoveDuplicates" in klass.__dict__:
            descriptor = klass.__dict__["isRemoveDuplicates"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_addvariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel_AddVariableValueAction)


def test_umlmodel_addvariablevalueaction_constructor_exists():
    assert callable(UMLModel_AddVariableValueAction.__init__)


def test_umlmodel_addvariablevalueaction_constructor_args():
    sig = inspect.signature(UMLModel_AddVariableValueAction.__init__)
    params = list(sig.parameters.keys())
    assert "isReplaceAll" in params, "Missing parameter 'isReplaceAll'"

def test_umlmodel_addvariablevalueaction_has_isReplaceAll():
    assert hasattr(UMLModel_AddVariableValueAction, "isReplaceAll")
    descriptor = None
    for klass in UMLModel_AddVariableValueAction.__mro__:
        if "isReplaceAll" in klass.__dict__:
            descriptor = klass.__dict__["isReplaceAll"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_inputpin_is_not_abstract():
    assert not inspect.isabstract(UMLModel_InputPin)


def test_umlmodel_inputpin_constructor_exists():
    assert callable(UMLModel_InputPin.__init__)


def test_umlmodel_inputpin_constructor_args():
    sig = inspect.signature(UMLModel_InputPin.__init__)
    params = list(sig.parameters.keys())



def test_writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(WriteStructuralFeatureAction)


def test_writestructuralfeatureaction_constructor_exists():
    assert callable(WriteStructuralFeatureAction.__init__)


def test_writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_removestructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel_RemoveStructuralFeatureValueAction)


def test_umlmodel_removestructuralfeaturevalueaction_constructor_exists():
    assert callable(UMLModel_RemoveStructuralFeatureValueAction.__init__)


def test_umlmodel_removestructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(UMLModel_RemoveStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())
    assert "isRemoveDuplicates" in params, "Missing parameter 'isRemoveDuplicates'"

def test_umlmodel_removestructuralfeaturevalueaction_has_isRemoveDuplicates():
    assert hasattr(UMLModel_RemoveStructuralFeatureValueAction, "isRemoveDuplicates")
    descriptor = None
    for klass in UMLModel_RemoveStructuralFeatureValueAction.__mro__:
        if "isRemoveDuplicates" in klass.__dict__:
            descriptor = klass.__dict__["isRemoveDuplicates"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_addstructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(UMLModel_AddStructuralFeatureValueAction)


def test_umlmodel_addstructuralfeaturevalueaction_constructor_exists():
    assert callable(UMLModel_AddStructuralFeatureValueAction.__init__)


def test_umlmodel_addstructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(UMLModel_AddStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())
    assert "isReplaceAll" in params, "Missing parameter 'isReplaceAll'"

def test_umlmodel_addstructuralfeaturevalueaction_has_isReplaceAll():
    assert hasattr(UMLModel_AddStructuralFeatureValueAction, "isReplaceAll")
    descriptor = None
    for klass in UMLModel_AddStructuralFeatureValueAction.__mro__:
        if "isReplaceAll" in klass.__dict__:
            descriptor = klass.__dict__["isReplaceAll"]
            break
    assert isinstance(descriptor, property)



def test_behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(BehavioredClassifier)


def test_behavioredclassifier_constructor_exists():
    assert callable(BehavioredClassifier.__init__)


def test_behavioredclassifier_constructor_args():
    sig = inspect.signature(BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_collaboration_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Collaboration)


def test_umlmodel_collaboration_constructor_exists():
    assert callable(UMLModel_Collaboration.__init__)


def test_umlmodel_collaboration_constructor_args():
    sig = inspect.signature(UMLModel_Collaboration.__init__)
    params = list(sig.parameters.keys())
    assert "collaborationRole" in params, "Missing parameter 'collaborationRole'"

def test_umlmodel_collaboration_has_collaborationRole():
    assert hasattr(UMLModel_Collaboration, "collaborationRole")
    descriptor = None
    for klass in UMLModel_Collaboration.__mro__:
        if "collaborationRole" in klass.__dict__:
            descriptor = klass.__dict__["collaborationRole"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_class_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Class)


def test_umlmodel_class_constructor_exists():
    assert callable(UMLModel_Class.__init__)


def test_umlmodel_class_constructor_args():
    sig = inspect.signature(UMLModel_Class.__init__)
    params = list(sig.parameters.keys())
    assert "isActive" in params, "Missing parameter 'isActive'"
    assert "extension" in params, "Missing parameter 'extension'"
    assert "superclass" in params, "Missing parameter 'superclass'"

def test_umlmodel_class_has_isActive():
    assert hasattr(UMLModel_Class, "isActive")
    descriptor = None
    for klass in UMLModel_Class.__mro__:
        if "isActive" in klass.__dict__:
            descriptor = klass.__dict__["isActive"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_class_has_extension():
    assert hasattr(UMLModel_Class, "extension")
    descriptor = None
    for klass in UMLModel_Class.__mro__:
        if "extension" in klass.__dict__:
            descriptor = klass.__dict__["extension"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_class_has_superclass():
    assert hasattr(UMLModel_Class, "superclass")
    descriptor = None
    for klass in UMLModel_Class.__mro__:
        if "superclass" in klass.__dict__:
            descriptor = klass.__dict__["superclass"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_usecase_is_not_abstract():
    assert not inspect.isabstract(UMLModel_UseCase)


def test_umlmodel_usecase_constructor_exists():
    assert callable(UMLModel_UseCase.__init__)


def test_umlmodel_usecase_constructor_args():
    sig = inspect.signature(UMLModel_UseCase.__init__)
    params = list(sig.parameters.keys())
    assert "subject" in params, "Missing parameter 'subject'"

def test_umlmodel_usecase_has_subject():
    assert hasattr(UMLModel_UseCase, "subject")
    descriptor = None
    for klass in UMLModel_UseCase.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_actor_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Actor)


def test_umlmodel_actor_constructor_exists():
    assert callable(UMLModel_Actor.__init__)


def test_umlmodel_actor_constructor_args():
    sig = inspect.signature(UMLModel_Actor.__init__)
    params = list(sig.parameters.keys())



def test_association_is_not_abstract():
    assert not inspect.isabstract(Association)


def test_association_constructor_exists():
    assert callable(Association.__init__)


def test_association_constructor_args():
    sig = inspect.signature(Association.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_communicationpath_is_not_abstract():
    assert not inspect.isabstract(UMLModel_CommunicationPath)


def test_umlmodel_communicationpath_constructor_exists():
    assert callable(UMLModel_CommunicationPath.__init__)


def test_umlmodel_communicationpath_constructor_args():
    sig = inspect.signature(UMLModel_CommunicationPath.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_extension_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Extension)


def test_umlmodel_extension_constructor_exists():
    assert callable(UMLModel_Extension.__init__)


def test_umlmodel_extension_constructor_args():
    sig = inspect.signature(UMLModel_Extension.__init__)
    params = list(sig.parameters.keys())
    assert "isRequired" in params, "Missing parameter 'isRequired'"
    assert "metaClass" in params, "Missing parameter 'metaClass'"

def test_umlmodel_extension_has_isRequired():
    assert hasattr(UMLModel_Extension, "isRequired")
    descriptor = None
    for klass in UMLModel_Extension.__mro__:
        if "isRequired" in klass.__dict__:
            descriptor = klass.__dict__["isRequired"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_extension_has_metaClass():
    assert hasattr(UMLModel_Extension, "metaClass")
    descriptor = None
    for klass in UMLModel_Extension.__mro__:
        if "metaClass" in klass.__dict__:
            descriptor = klass.__dict__["metaClass"]
            break
    assert isinstance(descriptor, property)



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_stereotype_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Stereotype)


def test_umlmodel_stereotype_constructor_exists():
    assert callable(UMLModel_Stereotype.__init__)


def test_umlmodel_stereotype_constructor_args():
    sig = inspect.signature(UMLModel_Stereotype.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_component_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Component)


def test_umlmodel_component_constructor_exists():
    assert callable(UMLModel_Component.__init__)


def test_umlmodel_component_constructor_args():
    sig = inspect.signature(UMLModel_Component.__init__)
    params = list(sig.parameters.keys())
    assert "required" in params, "Missing parameter 'required'"
    assert "indirectlyInstantiated" in params, "Missing parameter 'indirectlyInstantiated'"
    assert "provided" in params, "Missing parameter 'provided'"

def test_umlmodel_component_has_required():
    assert hasattr(UMLModel_Component, "required")
    descriptor = None
    for klass in UMLModel_Component.__mro__:
        if "required" in klass.__dict__:
            descriptor = klass.__dict__["required"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_component_has_indirectlyInstantiated():
    assert hasattr(UMLModel_Component, "indirectlyInstantiated")
    descriptor = None
    for klass in UMLModel_Component.__mro__:
        if "indirectlyInstantiated" in klass.__dict__:
            descriptor = klass.__dict__["indirectlyInstantiated"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_component_has_provided():
    assert hasattr(UMLModel_Component, "provided")
    descriptor = None
    for klass in UMLModel_Component.__mro__:
        if "provided" in klass.__dict__:
            descriptor = klass.__dict__["provided"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_node_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Node)


def test_umlmodel_node_constructor_exists():
    assert callable(UMLModel_Node.__init__)


def test_umlmodel_node_constructor_args():
    sig = inspect.signature(UMLModel_Node.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_behavior_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Behavior)


def test_umlmodel_behavior_constructor_exists():
    assert callable(UMLModel_Behavior.__init__)


def test_umlmodel_behavior_constructor_args():
    sig = inspect.signature(UMLModel_Behavior.__init__)
    params = list(sig.parameters.keys())
    assert "postcondition" in params, "Missing parameter 'postcondition'"
    assert "isReentrant" in params, "Missing parameter 'isReentrant'"
    assert "precondition" in params, "Missing parameter 'precondition'"
    assert "redefinedBahavior" in params, "Missing parameter 'redefinedBahavior'"
    assert "specification" in params, "Missing parameter 'specification'"
    assert "context" in params, "Missing parameter 'context'"

def test_umlmodel_behavior_has_postcondition():
    assert hasattr(UMLModel_Behavior, "postcondition")
    descriptor = None
    for klass in UMLModel_Behavior.__mro__:
        if "postcondition" in klass.__dict__:
            descriptor = klass.__dict__["postcondition"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_behavior_has_isReentrant():
    assert hasattr(UMLModel_Behavior, "isReentrant")
    descriptor = None
    for klass in UMLModel_Behavior.__mro__:
        if "isReentrant" in klass.__dict__:
            descriptor = klass.__dict__["isReentrant"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_behavior_has_precondition():
    assert hasattr(UMLModel_Behavior, "precondition")
    descriptor = None
    for klass in UMLModel_Behavior.__mro__:
        if "precondition" in klass.__dict__:
            descriptor = klass.__dict__["precondition"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_behavior_has_redefinedBahavior():
    assert hasattr(UMLModel_Behavior, "redefinedBahavior")
    descriptor = None
    for klass in UMLModel_Behavior.__mro__:
        if "redefinedBahavior" in klass.__dict__:
            descriptor = klass.__dict__["redefinedBahavior"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_behavior_has_specification():
    assert hasattr(UMLModel_Behavior, "specification")
    descriptor = None
    for klass in UMLModel_Behavior.__mro__:
        if "specification" in klass.__dict__:
            descriptor = klass.__dict__["specification"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_behavior_has_context():
    assert hasattr(UMLModel_Behavior, "context")
    descriptor = None
    for klass in UMLModel_Behavior.__mro__:
        if "context" in klass.__dict__:
            descriptor = klass.__dict__["context"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_associationclass_is_not_abstract():
    assert not inspect.isabstract(UMLModel_AssociationClass)


def test_umlmodel_associationclass_constructor_exists():
    assert callable(UMLModel_AssociationClass.__init__)


def test_umlmodel_associationclass_constructor_args():
    sig = inspect.signature(UMLModel_AssociationClass.__init__)
    params = list(sig.parameters.keys())



def test_relationship_is_not_abstract():
    assert not inspect.isabstract(Relationship)


def test_relationship_constructor_exists():
    assert callable(Relationship.__init__)


def test_relationship_constructor_args():
    sig = inspect.signature(Relationship.__init__)
    params = list(sig.parameters.keys())



def test_umlmodel_directedrelationship_is_not_abstract():
    assert not inspect.isabstract(UMLModel_DirectedRelationship)


def test_umlmodel_directedrelationship_constructor_exists():
    assert callable(UMLModel_DirectedRelationship.__init__)


def test_umlmodel_directedrelationship_constructor_args():
    sig = inspect.signature(UMLModel_DirectedRelationship.__init__)
    params = list(sig.parameters.keys())
    assert "target" in params, "Missing parameter 'target'"
    assert "source" in params, "Missing parameter 'source'"

def test_umlmodel_directedrelationship_has_target():
    assert hasattr(UMLModel_DirectedRelationship, "target")
    descriptor = None
    for klass in UMLModel_DirectedRelationship.__mro__:
        if "target" in klass.__dict__:
            descriptor = klass.__dict__["target"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_directedrelationship_has_source():
    assert hasattr(UMLModel_DirectedRelationship, "source")
    descriptor = None
    for klass in UMLModel_DirectedRelationship.__mro__:
        if "source" in klass.__dict__:
            descriptor = klass.__dict__["source"]
            break
    assert isinstance(descriptor, property)



def test_umlmodel_association_is_not_abstract():
    assert not inspect.isabstract(UMLModel_Association)


def test_umlmodel_association_constructor_exists():
    assert callable(UMLModel_Association.__init__)


def test_umlmodel_association_constructor_args():
    sig = inspect.signature(UMLModel_Association.__init__)
    params = list(sig.parameters.keys())
    assert "navigableOwnedEnd" in params, "Missing parameter 'navigableOwnedEnd'"
    assert "memberEnd" in params, "Missing parameter 'memberEnd'"
    assert "isDerived" in params, "Missing parameter 'isDerived'"
    assert "endType" in params, "Missing parameter 'endType'"

def test_umlmodel_association_has_navigableOwnedEnd():
    assert hasattr(UMLModel_Association, "navigableOwnedEnd")
    descriptor = None
    for klass in UMLModel_Association.__mro__:
        if "navigableOwnedEnd" in klass.__dict__:
            descriptor = klass.__dict__["navigableOwnedEnd"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_association_has_memberEnd():
    assert hasattr(UMLModel_Association, "memberEnd")
    descriptor = None
    for klass in UMLModel_Association.__mro__:
        if "memberEnd" in klass.__dict__:
            descriptor = klass.__dict__["memberEnd"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_association_has_isDerived():
    assert hasattr(UMLModel_Association, "isDerived")
    descriptor = None
    for klass in UMLModel_Association.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)

def test_umlmodel_association_has_endType():
    assert hasattr(UMLModel_Association, "endType")
    descriptor = None
    for klass in UMLModel_Association.__mro__:
        if "endType" in klass.__dict__:
            descriptor = klass.__dict__["endType"]
            break
    assert isinstance(descriptor, property)

def test_parametereffectkind_exists():
    # Check that the Enumeration exists
    assert ParameterEffectKind is not None

def test_parametereffectkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterEffectKind]
    expected_literals = [
        "delete",
        "read",
        "create",
        "update",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterEffectKind"

def test_visibilitykind_exists():
    # Check that the Enumeration exists
    assert VisibilityKind is not None

def test_visibilitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VisibilityKind]
    expected_literals = [
        "protected",
        "public",
        "private",
        "package",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VisibilityKind"

def test_messagesort_exists():
    # Check that the Enumeration exists
    assert MessageSort is not None

def test_messagesort_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MessageSort]
    expected_literals = [
        "reply",
        "createMessage",
        "deleteMessage",
        "asynchSignal",
        "asynchCall",
        "synchCall",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MessageSort"

def test_connectorkind_exists():
    # Check that the Enumeration exists
    assert ConnectorKind is not None

def test_connectorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ConnectorKind]
    expected_literals = [
        "delegation",
        "assembly",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ConnectorKind"

def test_parameterdirectionkind_exists():
    # Check that the Enumeration exists
    assert ParameterDirectionKind is not None

def test_parameterdirectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterDirectionKind]
    expected_literals = [
        "out",
        "return_",
        "inout",
        "in_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterDirectionKind"

def test_expansionkind_exists():
    # Check that the Enumeration exists
    assert ExpansionKind is not None

def test_expansionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExpansionKind]
    expected_literals = [
        "stream",
        "parallel",
        "iterative",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExpansionKind"

def test_pseudostatekind_exists():
    # Check that the Enumeration exists
    assert PseudostateKind is not None

def test_pseudostatekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PseudostateKind]
    expected_literals = [
        "junction",
        "shallowHistory",
        "entryPoint",
        "initial",
        "join",
        "deepHistory",
        "fork",
        "exitPoint",
        "choice",
        "terminate",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PseudostateKind"

def test_callconcurrencykind_exists():
    # Check that the Enumeration exists
    assert CallConcurrencyKind is not None

def test_callconcurrencykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CallConcurrencyKind]
    expected_literals = [
        "concurrent",
        "guarded",
        "sequential",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CallConcurrencyKind"

def test_interactionoperatorkind_exists():
    # Check that the Enumeration exists
    assert InteractionOperatorKind is not None

def test_interactionoperatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InteractionOperatorKind]
    expected_literals = [
        "opt",
        "loop",
        "consider",
        "neg",
        "alt",
        "par",
        "seq",
        "critical",
        "break_",
        "strict",
        "ignore",
        "assert_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InteractionOperatorKind"

def test_transitionkind_exists():
    # Check that the Enumeration exists
    assert TransitionKind is not None

def test_transitionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TransitionKind]
    expected_literals = [
        "internal",
        "external",
        "local",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TransitionKind"

def test_messagekind_exists():
    # Check that the Enumeration exists
    assert MessageKind is not None

def test_messagekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MessageKind]
    expected_literals = [
        "complete",
        "unknown",
        "lost",
        "found",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MessageKind"

def test_objectnodeorderingkind_exists():
    # Check that the Enumeration exists
    assert ObjectNodeOrderingKind is not None

def test_objectnodeorderingkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ObjectNodeOrderingKind]
    expected_literals = [
        "FIFO",
        "ordered",
        "LIFO",
        "unordered",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ObjectNodeOrderingKind"

def test_aggregationkind_exists():
    # Check that the Enumeration exists
    assert AggregationKind is not None

def test_aggregationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AggregationKind]
    expected_literals = [
        "composite",
        "shared",
        "none",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AggregationKind"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
EObject_strategy = st.builds(
    EObject,
)
UMLModel_UMLBase_strategy = st.builds(
    UMLModel_UMLBase,
    umlID=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
TemplateSignature_strategy = st.builds(
    TemplateSignature,
)
LinkAction_strategy = st.builds(
    LinkAction,
)
UMLModel_WriteLinkAction_strategy = st.builds(
    UMLModel_WriteLinkAction,
)
UMLModel_ReadLinkAction_strategy = st.builds(
    UMLModel_ReadLinkAction,
)
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
Transition_strategy = st.builds(
    Transition,
)
UMLModel_ProtocolTransition_strategy = st.builds(
    UMLModel_ProtocolTransition,
    referred=
        safe_text,
    preCondition=
        safe_text,
    postCondition=
        safe_text
)
StateMachine_strategy = st.builds(
    StateMachine,
)
InteractionUse_strategy = st.builds(
    InteractionUse,
)
UMLModel_PartDecomposition_strategy = st.builds(
    UMLModel_PartDecomposition,
)
ConnectableElement_strategy = st.builds(
    ConnectableElement,
)
BehavioralFeature_strategy = st.builds(
    BehavioralFeature,
)
Package_strategy = st.builds(
    Package,
)
UMLModel_Profile_strategy = st.builds(
    UMLModel_Profile,
    metamodelReference=
        safe_text,
    metaclassReference=
        safe_text,
    ownedStereotype=
        safe_text
)
UMLModel_Model_strategy = st.builds(
    UMLModel_Model,
    viewpoint=
        safe_text
)
Abstraction_strategy = st.builds(
    Abstraction,
)
UMLModel_Realization_strategy = st.builds(
    UMLModel_Realization,
)
LinkEndData_strategy = st.builds(
    LinkEndData,
)
UMLModel_LinkEndDestructionData_strategy = st.builds(
    UMLModel_LinkEndDestructionData,
    destroyAt=
        safe_text,
    isDestroyDuplicates=
        safe_text
)
UMLModel_LinkEndCreationData_strategy = st.builds(
    UMLModel_LinkEndCreationData,
    insertAt=
        safe_text,
    isReplaceAll=
        safe_text
)
LiteralSpecification_strategy = st.builds(
    LiteralSpecification,
)
UMLModel_LiteralBoolean_strategy = st.builds(
    UMLModel_LiteralBoolean,
    value=
        safe_text
)
UMLModel_LiteralNull_strategy = st.builds(
    UMLModel_LiteralNull,
)
UMLModel_LiteralString_strategy = st.builds(
    UMLModel_LiteralString,
    value=
        safe_text
)
UMLModel_LiteralUnlimitedNatural_strategy = st.builds(
    UMLModel_LiteralUnlimitedNatural,
    value=
        safe_text
)
UMLModel_LiteralInteger_strategy = st.builds(
    UMLModel_LiteralInteger,
    value=
        safe_text
)
Constraint_strategy = st.builds(
    Constraint,
)
UMLModel_IntervalConstraint_strategy = st.builds(
    UMLModel_IntervalConstraint,
)
UMLModel_InteractionConstraint_strategy = st.builds(
    UMLModel_InteractionConstraint,
)
Pin_strategy = st.builds(
    Pin,
)
DeploymentTarget_strategy = st.builds(
    DeploymentTarget,
)
UMLModel_ProtocolStateMachine_strategy = st.builds(
    UMLModel_ProtocolStateMachine,
)
MessageEnd_strategy = st.builds(
    MessageEnd,
)
OpaqueBehavior_strategy = st.builds(
    OpaqueBehavior,
)
UMLModel_FunctionBehavior_strategy = st.builds(
    UMLModel_FunctionBehavior,
)
State_strategy = st.builds(
    State,
)
UMLModel_FinalState_strategy = st.builds(
    UMLModel_FinalState,
)
Property_strategy = st.builds(
    Property,
)
UMLModel_Port_strategy = st.builds(
    UMLModel_Port,
    provided=
        safe_text,
    protocol=
        safe_text,
    required=
        safe_text,
    isService=
        safe_text,
    redefinedPort=
        safe_text,
    isBehavior=
        safe_text
)
UMLModel_ExtensionEnd_strategy = st.builds(
    UMLModel_ExtensionEnd,
)
OccurrenceSpecification_strategy = st.builds(
    OccurrenceSpecification,
)
UMLModel_MessageOccurrenceSpecification_strategy = st.builds(
    UMLModel_MessageOccurrenceSpecification,
)
UMLModel_ExecutionOccurrenceSpecification_strategy = st.builds(
    UMLModel_ExecutionOccurrenceSpecification,
    execution=
        safe_text
)
InstanceSpecification_strategy = st.builds(
    InstanceSpecification,
)
UMLBase_strategy = st.builds(
    UMLBase,
)
UMLModel_Element_strategy = st.builds(
    UMLModel_Element,
    owner=
        safe_text,
    ownedElement=
        safe_text,
    href=
        safe_text
)
Observation_strategy = st.builds(
    Observation,
)
UMLModel_TimeObservation_strategy = st.builds(
    UMLModel_TimeObservation,
    event=
        safe_text,
    firstEvent=
        safe_text
)
UMLModel_DurationObservation_strategy = st.builds(
    UMLModel_DurationObservation,
    firstEvent=
        safe_text,
    event=
        safe_text
)
Interval_strategy = st.builds(
    Interval,
)
UMLModel_TimeInterval_strategy = st.builds(
    UMLModel_TimeInterval,
)
UMLModel_DurationInterval_strategy = st.builds(
    UMLModel_DurationInterval,
)
IntervalConstraint_strategy = st.builds(
    IntervalConstraint,
)
UMLModel_TimeConstraint_strategy = st.builds(
    UMLModel_TimeConstraint,
    firstEvent=
        safe_text
)
UMLModel_DurationConstraint_strategy = st.builds(
    UMLModel_DurationConstraint,
    firstEvent=
        safe_text
)
ValueSpecification_strategy = st.builds(
    ValueSpecification,
)
UMLModel_Expression_strategy = st.builds(
    UMLModel_Expression,
    symbol=
        safe_text
)
UMLModel_LiteralSpecification_strategy = st.builds(
    UMLModel_LiteralSpecification,
)
UMLModel_TimeExpression_strategy = st.builds(
    UMLModel_TimeExpression,
    expr=
        safe_text,
    observation=
        safe_text
)
UMLModel_Interval_strategy = st.builds(
    UMLModel_Interval,
    max=
        safe_text,
    min=
        safe_text
)
UMLModel_InstanceValue_strategy = st.builds(
    UMLModel_InstanceValue,
    instance=
        safe_text
)
UMLModel_Duration_strategy = st.builds(
    UMLModel_Duration,
    expr=
        safe_text,
    observation=
        safe_text
)
UMLModel_EnumerationLiteral_strategy = st.builds(
    UMLModel_EnumerationLiteral,
    enumeration=
        safe_text
)
DataType_strategy = st.builds(
    DataType,
)
UMLModel_PrimitiveType_strategy = st.builds(
    UMLModel_PrimitiveType,
)
UMLModel_Enumeration_strategy = st.builds(
    UMLModel_Enumeration,
)
Node_strategy = st.builds(
    Node,
)
UMLModel_ExecutionEnvironment_strategy = st.builds(
    UMLModel_ExecutionEnvironment,
)
UMLModel_Device_strategy = st.builds(
    UMLModel_Device,
)
Artifact_strategy = st.builds(
    Artifact,
)
UMLModel_DeploymentSpecification_strategy = st.builds(
    UMLModel_DeploymentSpecification,
    deployment=
        safe_text,
    executionLocation=
        safe_text,
    deploymentLocation=
        safe_text
)
MultiplicityElement_strategy = st.builds(
    MultiplicityElement,
)
UMLModel_ConnectorEnd_strategy = st.builds(
    UMLModel_ConnectorEnd,
    partWithPort=
        safe_text,
    definingEnd=
        safe_text,
    role=
        safe_text
)
DirectedRelationship_strategy = st.builds(
    DirectedRelationship,
)
UMLModel_TemplateBinding_strategy = st.builds(
    UMLModel_TemplateBinding,
    boundElement=
        safe_text,
    signature=
        safe_text
)
UMLModel_ProfileApplication_strategy = st.builds(
    UMLModel_ProfileApplication,
    applyingPackage=
        safe_text,
    isStrict=
        safe_text,
    appliedProfile=
        safe_text
)
UMLModel_ElementImport_strategy = st.builds(
    UMLModel_ElementImport,
    visibility=
        safe_text,
    importingNamespace=
        safe_text,
    alias=
        safe_text
)
UMLModel_PackageImport_strategy = st.builds(
    UMLModel_PackageImport,
    visibility=
        safe_text,
    importingNamespace=
        safe_text
)
UMLModel_PackageMerge_strategy = st.builds(
    UMLModel_PackageMerge,
    receivingPackage=
        safe_text,
    mergedPackage=
        safe_text
)
UMLModel_ProtocolConformance_strategy = st.builds(
    UMLModel_ProtocolConformance,
    specificMachine=
        safe_text,
    generalMachine=
        safe_text
)
ParameterableElement_strategy = st.builds(
    ParameterableElement,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
ControlNode_strategy = st.builds(
    ControlNode,
)
UMLModel_MergeNode_strategy = st.builds(
    UMLModel_MergeNode,
)
UMLModel_ForkNode_strategy = st.builds(
    UMLModel_ForkNode,
)
UMLModel_FinalNode_strategy = st.builds(
    UMLModel_FinalNode,
)
UMLModel_JoinNode_strategy = st.builds(
    UMLModel_JoinNode,
    isCombineDuplicate=
        safe_text
)
UMLModel_InitialNode_strategy = st.builds(
    UMLModel_InitialNode,
)
UMLModel_ConnectableElement_strategy = st.builds(
    UMLModel_ConnectableElement,
    end=
        safe_text
)
UMLModel_DecisionNode_strategy = st.builds(
    UMLModel_DecisionNode,
    decisionInput=
        safe_text
)
Element_strategy = st.builds(
    Element,
)
UMLModel_Slot_strategy = st.builds(
    UMLModel_Slot,
    owningInstance=
        safe_text,
    definingFeature=
        safe_text
)
UMLModel_LinkEndData_strategy = st.builds(
    UMLModel_LinkEndData,
    end=
        safe_text,
    value=
        safe_text
)
UMLModel_ParameterableElement_strategy = st.builds(
    UMLModel_ParameterableElement,
    owningTemplateParameter=
        safe_text,
    templateParameter=
        safe_text
)
UMLModel_TemplateParameter_strategy = st.builds(
    UMLModel_TemplateParameter,
    default=
        safe_text,
    parameteredElement=
        safe_text,
    signature=
        safe_text
)
UMLModel_MultiplicityElement_strategy = st.builds(
    UMLModel_MultiplicityElement,
    lower=
        safe_text,
    isOrdered=
        safe_text,
    isUnique=
        safe_text,
    upper=
        safe_text
)
UMLModel_TemplateParameterSubstitution_strategy = st.builds(
    UMLModel_TemplateParameterSubstitution,
    templateBinding=
        safe_text,
    formal=
        safe_text,
    actual=
        safe_text
)
UMLModel_TemplateableElement_strategy = st.builds(
    UMLModel_TemplateableElement,
)
UMLModel_Relationship_strategy = st.builds(
    UMLModel_Relationship,
    relatedElement=
        safe_text
)
UMLModel_ExceptionHandler_strategy = st.builds(
    UMLModel_ExceptionHandler,
    handlerBody=
        safe_text,
    exceptionInput=
        safe_text,
    exceptionType=
        safe_text,
    protectedNode=
        safe_text
)
UMLModel_NamedElement_strategy = st.builds(
    UMLModel_NamedElement,
    qualifiedName=
        safe_text,
    namespace=
        safe_text,
    visibility=
        safe_text,
    clientDependency=
        safe_text,
    name=
        safe_text
)
UMLModel_QualifierValue_strategy = st.builds(
    UMLModel_QualifierValue,
    qualifier=
        safe_text,
    value=
        safe_text
)
UMLModel_TemplateSignature_strategy = st.builds(
    UMLModel_TemplateSignature,
    parameter=
        safe_text,
    template=
        safe_text
)
UMLModel_Image_strategy = st.builds(
    UMLModel_Image,
    content=
        safe_text,
    format=
        safe_text,
    location=
        safe_text
)
FinalNode_strategy = st.builds(
    FinalNode,
)
UMLModel_FlowFinalNode_strategy = st.builds(
    UMLModel_FlowFinalNode,
)
UMLModel_ActivityFinalNode_strategy = st.builds(
    UMLModel_ActivityFinalNode,
)
ObjectNode_strategy = st.builds(
    ObjectNode,
)
UMLModel_Pin_strategy = st.builds(
    UMLModel_Pin,
    isControl=
        safe_text
)
UMLModel_ExpansionNode_strategy = st.builds(
    UMLModel_ExpansionNode,
    regionAsInput=
        safe_text,
    regionAsOutput=
        safe_text
)
UMLModel_ActivityParameterNode_strategy = st.builds(
    UMLModel_ActivityParameterNode,
    parameter=
        safe_text
)
RedefinableElement_strategy = st.builds(
    RedefinableElement,
)
UMLModel_ExtensionPoint_strategy = st.builds(
    UMLModel_ExtensionPoint,
    useCase=
        safe_text
)
UMLModel_Feature_strategy = st.builds(
    UMLModel_Feature,
    featuringClassifier=
        safe_text,
    isStatic=
        safe_text
)
UMLModel_RedefinableTemplateSignature_strategy = st.builds(
    UMLModel_RedefinableTemplateSignature,
    extendedSignature=
        safe_text,
    inheritedParameter=
        safe_text,
    classifier=
        safe_text
)
ActivityGroup_strategy = st.builds(
    ActivityGroup,
)
UMLModel_InterruptibleActivityRegion_strategy = st.builds(
    UMLModel_InterruptibleActivityRegion,
    interruptingEdge=
        safe_text,
    node=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
UMLModel_Vertex_strategy = st.builds(
    UMLModel_Vertex,
    incoming=
        safe_text,
    outgoing=
        safe_text,
    container=
        safe_text
)
UMLModel_GeneralOrdering_strategy = st.builds(
    UMLModel_GeneralOrdering,
    before=
        safe_text,
    after=
        safe_text
)
UMLModel_Lifeline_strategy = st.builds(
    UMLModel_Lifeline,
    decomposedAs=
        safe_text,
    interaction=
        safe_text,
    represents=
        safe_text,
    coveredBy=
        safe_text
)
UMLModel_MessageEnd_strategy = st.builds(
    UMLModel_MessageEnd,
    message=
        safe_text
)
UMLModel_Message_strategy = st.builds(
    UMLModel_Message,
    signature=
        safe_text,
    receiveEvent=
        safe_text,
    messageSort=
        safe_text,
    interaction=
        safe_text,
    sendEvent=
        safe_text,
    messageKind=
        safe_text,
    connector=
        safe_text
)
UMLModel_DeploymentTarget_strategy = st.builds(
    UMLModel_DeploymentTarget,
    deployedElement=
        safe_text
)
UMLModel_TypedElement_strategy = st.builds(
    UMLModel_TypedElement,
    type=
        safe_text
)
UMLModel_RedefinableElement_strategy = st.builds(
    UMLModel_RedefinableElement,
    redefinitionContext=
        safe_text,
    redefinedElement=
        safe_text,
    isLeaf=
        safe_text
)
UMLModel_Include_strategy = st.builds(
    UMLModel_Include,
    includingCase=
        safe_text,
    addition=
        safe_text
)
UMLModel_Extend_strategy = st.builds(
    UMLModel_Extend,
    extension=
        safe_text,
    extensionLocation=
        safe_text,
    extendedCase=
        safe_text
)
UMLModel_InteractionFragment_strategy = st.builds(
    UMLModel_InteractionFragment,
    enclosingInteraction=
        safe_text,
    covered=
        safe_text,
    enclosingOperand=
        safe_text
)
UMLModel_Namespace_strategy = st.builds(
    UMLModel_Namespace,
    importedMember=
        safe_text,
    member=
        safe_text,
    ownedMember=
        safe_text
)
UMLModel_DeployedArtifact_strategy = st.builds(
    UMLModel_DeployedArtifact,
)
UMLModel_ActivityPartition_strategy = st.builds(
    UMLModel_ActivityPartition,
    isDimension=
        safe_text,
    superPartition=
        safe_text,
    node=
        safe_text,
    isExternal=
        safe_text,
    represents=
        safe_text,
    subpartition=
        safe_text,
    edge=
        safe_text
)
UMLModel_ActivityNode_strategy = st.builds(
    UMLModel_ActivityNode,
    inGroup=
        safe_text,
    incoming=
        safe_text,
    inPartition=
        safe_text,
    activity=
        safe_text,
    outgoing=
        safe_text,
    redefinedNode=
        safe_text,
    inStructuredNode=
        safe_text,
    inInterruptibleRegion=
        safe_text
)
UMLModel_Variable_strategy = st.builds(
    UMLModel_Variable,
    scope=
        safe_text,
    activityScope=
        safe_text
)
Behavior_strategy = st.builds(
    Behavior,
)
UMLModel_OpaqueBehavior_strategy = st.builds(
    UMLModel_OpaqueBehavior,
    body=
        safe_text,
    language=
        safe_text
)
UMLModel_StateMachine_strategy = st.builds(
    UMLModel_StateMachine,
    submachineState=
        safe_text,
    extendedStateMachine=
        safe_text
)
UMLModel_Activity_strategy = st.builds(
    UMLModel_Activity,
    isSingleExecution=
        safe_text,
    structuredNode=
        safe_text,
    partition=
        safe_text,
    isReadOnly=
        safe_text
)
InputPin_strategy = st.builds(
    InputPin,
)
UMLModel_ValuePin_strategy = st.builds(
    UMLModel_ValuePin,
)
UMLModel_ActionInputPin_strategy = st.builds(
    UMLModel_ActionInputPin,
)
ExecutionSpecification_strategy = st.builds(
    ExecutionSpecification,
)
UMLModel_ActionExecutionSpecification_strategy = st.builds(
    UMLModel_ActionExecutionSpecification,
    action=
        safe_text
)
UMLModel_ActivityGroup_strategy = st.builds(
    UMLModel_ActivityGroup,
    subgroup=
        safe_text,
    inActivity=
        safe_text,
    superGroup=
        safe_text
)
UMLModel_ActivityEdge_strategy = st.builds(
    UMLModel_ActivityEdge,
    target=
        safe_text,
    activity=
        safe_text,
    inStructuredNode=
        safe_text,
    inGroup=
        safe_text,
    interrupts=
        safe_text,
    source=
        safe_text,
    inPartition=
        safe_text,
    redefinedEdge=
        safe_text
)
AcceptEventAction_strategy = st.builds(
    AcceptEventAction,
)
UMLModel_AcceptCallAction_strategy = st.builds(
    UMLModel_AcceptCallAction,
)
UMLModel_OpaqueExpression_strategy = st.builds(
    UMLModel_OpaqueExpression,
    body=
        safe_text,
    result=
        safe_text,
    behavior=
        safe_text,
    language=
        safe_text
)
Dependency_strategy = st.builds(
    Dependency,
)
UMLModel_Usage_strategy = st.builds(
    UMLModel_Usage,
)
UMLModel_Deployment_strategy = st.builds(
    UMLModel_Deployment,
    location=
        safe_text,
    deployedArtifact=
        safe_text
)
UMLModel_Abstraction_strategy = st.builds(
    UMLModel_Abstraction,
)
ExecutableNode_strategy = st.builds(
    ExecutableNode,
)
UMLModel_Action_strategy = st.builds(
    UMLModel_Action,
    input=
        safe_text,
    context=
        safe_text,
    output=
        safe_text
)
UMLModel_Trigger_strategy = st.builds(
    UMLModel_Trigger,
    event=
        safe_text,
    port=
        safe_text
)
Action_strategy = st.builds(
    Action,
)
UMLModel_ReduceAction_strategy = st.builds(
    UMLModel_ReduceAction,
    reducer=
        safe_text,
    isOrdered=
        safe_text
)
UMLModel_RaiseExceptionAction_strategy = st.builds(
    UMLModel_RaiseExceptionAction,
)
UMLModel_ReadSelfAction_strategy = st.builds(
    UMLModel_ReadSelfAction,
)
UMLModel_DestroyObjectAction_strategy = st.builds(
    UMLModel_DestroyObjectAction,
    isDestroyLinks=
        safe_text,
    isDestroyOwnedObjects=
        safe_text
)
UMLModel_StructuralFeatureAction_strategy = st.builds(
    UMLModel_StructuralFeatureAction,
    structuralFeature=
        safe_text
)
UMLModel_TestIdentityAction_strategy = st.builds(
    UMLModel_TestIdentityAction,
)
UMLModel_ReadIsClassifiedObjectAction_strategy = st.builds(
    UMLModel_ReadIsClassifiedObjectAction,
    isDirect=
        safe_text,
    classifier=
        safe_text
)
UMLModel_ReadExtentAction_strategy = st.builds(
    UMLModel_ReadExtentAction,
    classifier=
        safe_text
)
UMLModel_StartClassifierBehaviorAction_strategy = st.builds(
    UMLModel_StartClassifierBehaviorAction,
)
UMLModel_OpaqueAction_strategy = st.builds(
    UMLModel_OpaqueAction,
    body=
        safe_text,
    language=
        safe_text
)
UMLModel_LinkAction_strategy = st.builds(
    UMLModel_LinkAction,
)
UMLModel_InvocationAction_strategy = st.builds(
    UMLModel_InvocationAction,
    onPort=
        safe_text
)
UMLModel_ValueSpecificationAction_strategy = st.builds(
    UMLModel_ValueSpecificationAction,
)
UMLModel_UnmarshallAction_strategy = st.builds(
    UMLModel_UnmarshallAction,
    unmarshallType=
        safe_text
)
UMLModel_ReadLinkObjectEndAction_strategy = st.builds(
    UMLModel_ReadLinkObjectEndAction,
    end=
        safe_text
)
UMLModel_ReadLinkObjectEndQualifierAction_strategy = st.builds(
    UMLModel_ReadLinkObjectEndQualifierAction,
    qualifier=
        safe_text
)
UMLModel_ReplyAction_strategy = st.builds(
    UMLModel_ReplyAction,
    replyToCall=
        safe_text
)
UMLModel_VariableAction_strategy = st.builds(
    UMLModel_VariableAction,
    variable=
        safe_text
)
UMLModel_ReclassifyObjectAction_strategy = st.builds(
    UMLModel_ReclassifyObjectAction,
    isReplaceAll=
        safe_text,
    newClassifier=
        safe_text,
    oldClassifier=
        safe_text
)
UMLModel_AcceptEventAction_strategy = st.builds(
    UMLModel_AcceptEventAction,
    isUnmarshall=
        safe_text
)
UMLModel_OutputPin_strategy = st.builds(
    UMLModel_OutputPin,
)
CombinedFragment_strategy = st.builds(
    CombinedFragment,
)
UMLModel_ConsiderIgnoreFragment_strategy = st.builds(
    UMLModel_ConsiderIgnoreFragment,
    message=
        safe_text
)
CentralBufferNode_strategy = st.builds(
    CentralBufferNode,
)
UMLModel_DataStoreNode_strategy = st.builds(
    UMLModel_DataStoreNode,
)
UMLModel_CentralBufferNode_strategy = st.builds(
    UMLModel_CentralBufferNode,
)
WriteLinkAction_strategy = st.builds(
    WriteLinkAction,
)
UMLModel_DestroyLinkAction_strategy = st.builds(
    UMLModel_DestroyLinkAction,
)
UMLModel_CreateLinkAction_strategy = st.builds(
    UMLModel_CreateLinkAction,
)
PackageableElement_strategy = st.builds(
    PackageableElement,
)
UMLModel_Event_strategy = st.builds(
    UMLModel_Event,
)
UMLModel_InformationFlow_strategy = st.builds(
    UMLModel_InformationFlow,
    realizingConnector=
        safe_text,
    conveyed=
        safe_text,
    informationSource=
        safe_text,
    realizingActivityEdge=
        safe_text,
    informationTarget=
        safe_text,
    realizingMessage=
        safe_text,
    realization=
        safe_text
)
UMLModel_Constraint_strategy = st.builds(
    UMLModel_Constraint,
    context=
        safe_text,
    constrainedElement=
        safe_text
)
UMLModel_GeneralizationSet_strategy = st.builds(
    UMLModel_GeneralizationSet,
    isCovering=
        safe_text,
    powerType=
        safe_text,
    generalization=
        safe_text,
    isDisjoint=
        safe_text
)
UMLModel_Observation_strategy = st.builds(
    UMLModel_Observation,
)
UMLModel_ValueSpecification_strategy = st.builds(
    UMLModel_ValueSpecification,
)
UMLModel_Type_strategy = st.builds(
    UMLModel_Type,
    package=
        safe_text
)
UMLModel_CreateObjectAction_strategy = st.builds(
    UMLModel_CreateObjectAction,
    classifier=
        safe_text
)
CreateLinkAction_strategy = st.builds(
    CreateLinkAction,
)
UMLModel_CreateLinkObjectAction_strategy = st.builds(
    UMLModel_CreateLinkObjectAction,
)
StructuredActivityNode_strategy = st.builds(
    StructuredActivityNode,
)
UMLModel_SequenceNode_strategy = st.builds(
    UMLModel_SequenceNode,
)
UMLModel_LoopNode_strategy = st.builds(
    UMLModel_LoopNode,
    isTestedFirst=
        safe_text,
    test=
        safe_text,
    loopVariable=
        safe_text,
    bodyPart=
        safe_text,
    decider=
        safe_text,
    bodyOutput=
        safe_text,
    setupPart=
        safe_text
)
UMLModel_ExpansionRegion_strategy = st.builds(
    UMLModel_ExpansionRegion,
    mode=
        safe_text,
    outputElement=
        safe_text,
    inputElement=
        safe_text
)
UMLModel_ConditionalNode_strategy = st.builds(
    UMLModel_ConditionalNode,
    isDeterminate=
        safe_text,
    isAssured=
        safe_text
)
UMLModel_Gate_strategy = st.builds(
    UMLModel_Gate,
)
ActivityNode_strategy = st.builds(
    ActivityNode,
)
UMLModel_ObjectNode_strategy = st.builds(
    UMLModel_ObjectNode,
    selection=
        safe_text,
    inState=
        safe_text,
    isControlType=
        safe_text,
    ordering=
        safe_text
)
UMLModel_ExecutableNode_strategy = st.builds(
    UMLModel_ExecutableNode,
)
UMLModel_ControlNode_strategy = st.builds(
    UMLModel_ControlNode,
)
ActivityEdge_strategy = st.builds(
    ActivityEdge,
)
UMLModel_ObjectFlow_strategy = st.builds(
    UMLModel_ObjectFlow,
    isMulticast=
        safe_text,
    isMultireceive=
        safe_text,
    transformation=
        safe_text,
    selection=
        safe_text
)
UMLModel_ControlFlow_strategy = st.builds(
    UMLModel_ControlFlow,
)
Vertex_strategy = st.builds(
    Vertex,
)
UMLModel_Pseudostate_strategy = st.builds(
    UMLModel_Pseudostate,
    kind=
        safe_text,
    stateMachine=
        safe_text,
    state=
        safe_text
)
UMLModel_ConnectionPointReference_strategy = st.builds(
    UMLModel_ConnectionPointReference,
    entry=
        safe_text,
    exit=
        safe_text,
    state=
        safe_text
)
UMLModel_Comment_strategy = st.builds(
    UMLModel_Comment,
    body=
        safe_text,
    annotatedElement=
        safe_text
)
UMLModel_Dependency_strategy = st.builds(
    UMLModel_Dependency,
    client=
        safe_text,
    supplier=
        safe_text
)
StructuredClassifier_strategy = st.builds(
    StructuredClassifier,
)
UMLModel_EncapsulatedClassifier_strategy = st.builds(
    UMLModel_EncapsulatedClassifier,
    ownedPort=
        safe_text
)
StructuralFeatureAction_strategy = st.builds(
    StructuralFeatureAction,
)
UMLModel_WriteStructuralFeatureAction_strategy = st.builds(
    UMLModel_WriteStructuralFeatureAction,
)
UMLModel_ReadStructuralFeatureAction_strategy = st.builds(
    UMLModel_ReadStructuralFeatureAction,
)
UMLModel_ClearStructuralFeatureAction_strategy = st.builds(
    UMLModel_ClearStructuralFeatureAction,
)
UMLModel_ClearAssociationAction_strategy = st.builds(
    UMLModel_ClearAssociationAction,
    association=
        safe_text
)
VariableAction_strategy = st.builds(
    VariableAction,
)
UMLModel_ReadVariableAction_strategy = st.builds(
    UMLModel_ReadVariableAction,
)
UMLModel_WriteVariableAction_strategy = st.builds(
    UMLModel_WriteVariableAction,
)
UMLModel_ClearVariableAction_strategy = st.builds(
    UMLModel_ClearVariableAction,
)
UMLModel_Clause_strategy = st.builds(
    UMLModel_Clause,
    decider=
        safe_text,
    bodyOutput=
        safe_text,
    successorClause=
        safe_text,
    test=
        safe_text,
    predecessorClause=
        safe_text,
    body=
        safe_text
)
InteractionFragment_strategy = st.builds(
    InteractionFragment,
)
UMLModel_OccurrenceSpecification_strategy = st.builds(
    UMLModel_OccurrenceSpecification,
    event=
        safe_text,
    toAfter=
        safe_text,
    toBefore=
        safe_text
)
UMLModel_InteractionUse_strategy = st.builds(
    UMLModel_InteractionUse,
    refersTo=
        safe_text
)
UMLModel_StateInvariant_strategy = st.builds(
    UMLModel_StateInvariant,
)
UMLModel_Interaction_strategy = st.builds(
    UMLModel_Interaction,
)
UMLModel_Continuation_strategy = st.builds(
    UMLModel_Continuation,
    setting=
        safe_text
)
UMLModel_ExecutionSpecification_strategy = st.builds(
    UMLModel_ExecutionSpecification,
    finish=
        safe_text,
    start=
        safe_text
)
UMLModel_CombinedFragment_strategy = st.builds(
    UMLModel_CombinedFragment,
    interactionOperator=
        safe_text
)
Realization_strategy = st.builds(
    Realization,
)
UMLModel_ComponentRealization_strategy = st.builds(
    UMLModel_ComponentRealization,
    realizingClassifier=
        safe_text,
    abstraction=
        safe_text
)
UMLModel_PackageableElement_strategy = st.builds(
    UMLModel_PackageableElement,
)
UMLModel_Generalization_strategy = st.builds(
    UMLModel_Generalization,
    generalizationSet=
        safe_text,
    general=
        safe_text,
    specific=
        safe_text,
    isSubstitutable=
        safe_text
)
TemplateableElement_strategy = st.builds(
    TemplateableElement,
)
UMLModel_StringExpression_strategy = st.builds(
    UMLModel_StringExpression,
    owningExpression=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
UMLModel_Reception_strategy = st.builds(
    UMLModel_Reception,
    signal=
        safe_text
)
EncapsulatedClassifier_strategy = st.builds(
    EncapsulatedClassifier,
)
Event_strategy = st.builds(
    Event,
)
UMLModel_ExecutionEvent_strategy = st.builds(
    UMLModel_ExecutionEvent,
)
UMLModel_DestructionEvent_strategy = st.builds(
    UMLModel_DestructionEvent,
)
UMLModel_MessageEvent_strategy = st.builds(
    UMLModel_MessageEvent,
)
UMLModel_CreationEvent_strategy = st.builds(
    UMLModel_CreationEvent,
)
UMLModel_TimeEvent_strategy = st.builds(
    UMLModel_TimeEvent,
    isRelative=
        safe_text
)
UMLModel_ChangeEvent_strategy = st.builds(
    UMLModel_ChangeEvent,
)
TemplateParameter_strategy = st.builds(
    TemplateParameter,
)
UMLModel_ConnectableElementTemplateParameter_strategy = st.builds(
    UMLModel_ConnectableElementTemplateParameter,
)
UMLModel_OperationTemplateParameter_strategy = st.builds(
    UMLModel_OperationTemplateParameter,
)
UMLModel_ClassifierTemplateParameter_strategy = st.builds(
    UMLModel_ClassifierTemplateParameter,
    constrainingClassifier=
        safe_text,
    defaultClassifier=
        safe_text,
    allowSubstitutable=
        safe_text
)
UMLModel_CollaborationUse_strategy = st.builds(
    UMLModel_CollaborationUse,
    type=
        safe_text
)
UMLModel_Substitution_strategy = st.builds(
    UMLModel_Substitution,
    substitutingClassifier=
        safe_text,
    contract=
        safe_text
)
UMLModel_InterfaceRealization_strategy = st.builds(
    UMLModel_InterfaceRealization,
    realizingClassifier=
        safe_text,
    contract=
        safe_text
)
Feature_strategy = st.builds(
    Feature,
)
UMLModel_StructuralFeature_strategy = st.builds(
    UMLModel_StructuralFeature,
    isReadOnly=
        safe_text
)
UMLModel_Connector_strategy = st.builds(
    UMLModel_Connector,
    kind=
        safe_text,
    redefinedConnector=
        safe_text,
    contract=
        safe_text,
    type=
        safe_text
)
Namespace_strategy = st.builds(
    Namespace,
)
UMLModel_Package_strategy = st.builds(
    UMLModel_Package,
    nestedPackage=
        safe_text,
    ownedType=
        safe_text,
    nestingPackage=
        safe_text
)
UMLModel_InteractionOperand_strategy = st.builds(
    UMLModel_InteractionOperand,
)
UMLModel_Transition_strategy = st.builds(
    UMLModel_Transition,
    target=
        safe_text,
    kind=
        safe_text,
    source=
        safe_text,
    guard=
        safe_text,
    redefinedTransition=
        safe_text,
    container=
        safe_text
)
UMLModel_State_strategy = st.builds(
    UMLModel_State,
    isSimple=
        safe_text,
    isSubmachineState=
        safe_text,
    submachine=
        safe_text,
    redefinedState=
        safe_text,
    isOrthogonal=
        safe_text,
    isComposite=
        safe_text
)
UMLModel_StructuredActivityNode_strategy = st.builds(
    UMLModel_StructuredActivityNode,
    mustIsolate=
        safe_text
)
UMLModel_Region_strategy = st.builds(
    UMLModel_Region,
    state=
        safe_text,
    extendedRegion=
        safe_text,
    stateMachine=
        safe_text
)
UMLModel_Classifier_strategy = st.builds(
    UMLModel_Classifier,
    general=
        safe_text,
    inheritedMember=
        safe_text,
    representation=
        safe_text,
    redefinedClassifier=
        safe_text,
    feature=
        safe_text,
    useCase=
        safe_text,
    powertypeExtent=
        safe_text,
    isAbstract=
        safe_text,
    attribute=
        safe_text
)
UMLModel_BehavioralFeature_strategy = st.builds(
    UMLModel_BehavioralFeature,
    raisedException=
        safe_text,
    concurrency=
        safe_text,
    isAbstract=
        safe_text,
    method=
        safe_text
)
UMLModel_BehaviorExecutionSpecification_strategy = st.builds(
    UMLModel_BehaviorExecutionSpecification,
    behavior=
        safe_text
)
UMLModel_ParameterSet_strategy = st.builds(
    UMLModel_ParameterSet,
    parameter=
        safe_text
)
UMLModel_Parameter_strategy = st.builds(
    UMLModel_Parameter,
    default=
        safe_text,
    effect=
        safe_text,
    isStream=
        safe_text,
    parameterSet=
        safe_text,
    isException=
        safe_text,
    direction=
        safe_text,
    operation=
        safe_text
)
CallAction_strategy = st.builds(
    CallAction,
)
UMLModel_CallOperationAction_strategy = st.builds(
    UMLModel_CallOperationAction,
    operation=
        safe_text
)
UMLModel_CallBehaviorAction_strategy = st.builds(
    UMLModel_CallBehaviorAction,
    behavior=
        safe_text
)
UMLModel_Property_strategy = st.builds(
    UMLModel_Property,
    association=
        safe_text,
    class_=
        safe_text,
    opposite=
        safe_text,
    isComposite=
        safe_text,
    owningAssociation=
        safe_text,
    subsettedProperty=
        safe_text,
    aggregation=
        safe_text,
    associationEnd=
        safe_text,
    datatype=
        safe_text,
    isDerived=
        safe_text,
    default=
        safe_text,
    redefinedProperty=
        safe_text,
    isDerivedUnion=
        safe_text
)
InvocationAction_strategy = st.builds(
    InvocationAction,
)
UMLModel_SendObjectAction_strategy = st.builds(
    UMLModel_SendObjectAction,
)
UMLModel_CallAction_strategy = st.builds(
    UMLModel_CallAction,
    isSynchronous=
        safe_text
)
UMLModel_SendSignalAction_strategy = st.builds(
    UMLModel_SendSignalAction,
    signal=
        safe_text
)
UMLModel_BroadcastSignalAction_strategy = st.builds(
    UMLModel_BroadcastSignalAction,
    signal=
        safe_text
)
UMLModel_Operation_strategy = st.builds(
    UMLModel_Operation,
    isQuery=
        safe_text,
    upper=
        safe_text,
    lower=
        safe_text,
    isUnique=
        safe_text,
    interface=
        safe_text,
    datatype=
        safe_text,
    postcondition=
        safe_text,
    bodyCondition=
        safe_text,
    redefinedOperation=
        safe_text,
    type=
        safe_text,
    precondition=
        safe_text,
    isOrdered=
        safe_text,
    class_=
        safe_text
)
UMLModel_Manifestation_strategy = st.builds(
    UMLModel_Manifestation,
    utilizedElement=
        safe_text
)
DeployedArtifact_strategy = st.builds(
    DeployedArtifact,
)
UMLModel_InstanceSpecification_strategy = st.builds(
    UMLModel_InstanceSpecification,
    classifier=
        safe_text
)
Classifier_strategy = st.builds(
    Classifier,
)
UMLModel_StructuredClassifier_strategy = st.builds(
    UMLModel_StructuredClassifier,
    part=
        safe_text,
    role=
        safe_text
)
UMLModel_Signal_strategy = st.builds(
    UMLModel_Signal,
)
UMLModel_DataType_strategy = st.builds(
    UMLModel_DataType,
)
UMLModel_BehavioredClassifier_strategy = st.builds(
    UMLModel_BehavioredClassifier,
    classifierBehavior=
        safe_text
)
UMLModel_Interface_strategy = st.builds(
    UMLModel_Interface,
    redefinedInterface=
        safe_text,
    isActive=
        st.booleans()
)
UMLModel_InformationItem_strategy = st.builds(
    UMLModel_InformationItem,
    represented=
        safe_text
)
UMLModel_Artifact_strategy = st.builds(
    UMLModel_Artifact,
    fileName=
        safe_text
)
MessageEvent_strategy = st.builds(
    MessageEvent,
)
UMLModel_CallEvent_strategy = st.builds(
    UMLModel_CallEvent,
    operation=
        safe_text
)
UMLModel_ReceiveOperationEvent_strategy = st.builds(
    UMLModel_ReceiveOperationEvent,
    operation=
        safe_text
)
UMLModel_ReceiveSignalEvent_strategy = st.builds(
    UMLModel_ReceiveSignalEvent,
    signal=
        safe_text
)
UMLModel_SignalEvent_strategy = st.builds(
    UMLModel_SignalEvent,
    signal=
        safe_text
)
UMLModel_SendSignalEvent_strategy = st.builds(
    UMLModel_SendSignalEvent,
    signal=
        safe_text
)
UMLModel_AnyReceiveEvent_strategy = st.builds(
    UMLModel_AnyReceiveEvent,
)
WriteVariableAction_strategy = st.builds(
    WriteVariableAction,
)
UMLModel_RemoveVariableValueAction_strategy = st.builds(
    UMLModel_RemoveVariableValueAction,
    isRemoveDuplicates=
        safe_text
)
UMLModel_AddVariableValueAction_strategy = st.builds(
    UMLModel_AddVariableValueAction,
    isReplaceAll=
        safe_text
)
UMLModel_InputPin_strategy = st.builds(
    UMLModel_InputPin,
)
WriteStructuralFeatureAction_strategy = st.builds(
    WriteStructuralFeatureAction,
)
UMLModel_RemoveStructuralFeatureValueAction_strategy = st.builds(
    UMLModel_RemoveStructuralFeatureValueAction,
    isRemoveDuplicates=
        safe_text
)
UMLModel_AddStructuralFeatureValueAction_strategy = st.builds(
    UMLModel_AddStructuralFeatureValueAction,
    isReplaceAll=
        safe_text
)
BehavioredClassifier_strategy = st.builds(
    BehavioredClassifier,
)
UMLModel_Collaboration_strategy = st.builds(
    UMLModel_Collaboration,
    collaborationRole=
        safe_text
)
UMLModel_Class_strategy = st.builds(
    UMLModel_Class,
    isActive=
        safe_text,
    extension=
        safe_text,
    superclass=
        safe_text
)
UMLModel_UseCase_strategy = st.builds(
    UMLModel_UseCase,
    subject=
        safe_text
)
UMLModel_Actor_strategy = st.builds(
    UMLModel_Actor,
)
Association_strategy = st.builds(
    Association,
)
UMLModel_CommunicationPath_strategy = st.builds(
    UMLModel_CommunicationPath,
)
UMLModel_Extension_strategy = st.builds(
    UMLModel_Extension,
    isRequired=
        safe_text,
    metaClass=
        safe_text
)
Class_strategy = st.builds(
    Class,
)
UMLModel_Stereotype_strategy = st.builds(
    UMLModel_Stereotype,
)
UMLModel_Component_strategy = st.builds(
    UMLModel_Component,
    required=
        safe_text,
    indirectlyInstantiated=
        safe_text,
    provided=
        safe_text
)
UMLModel_Node_strategy = st.builds(
    UMLModel_Node,
)
UMLModel_Behavior_strategy = st.builds(
    UMLModel_Behavior,
    postcondition=
        safe_text,
    isReentrant=
        safe_text,
    precondition=
        safe_text,
    redefinedBahavior=
        safe_text,
    specification=
        safe_text,
    context=
        safe_text
)
UMLModel_AssociationClass_strategy = st.builds(
    UMLModel_AssociationClass,
)
Relationship_strategy = st.builds(
    Relationship,
)
UMLModel_DirectedRelationship_strategy = st.builds(
    UMLModel_DirectedRelationship,
    target=
        safe_text,
    source=
        safe_text
)
UMLModel_Association_strategy = st.builds(
    UMLModel_Association,
    navigableOwnedEnd=
        safe_text,
    memberEnd=
        safe_text,
    isDerived=
        safe_text,
    endType=
        safe_text
)

@given(instance=EObject_strategy)
@settings(max_examples=50)
def test_eobject_instantiation(instance):
    assert isinstance(instance, EObject)

@given(instance=UMLModel_UMLBase_strategy)
@settings(max_examples=50)
def test_umlmodel_umlbase_instantiation(instance):
    assert isinstance(instance, UMLModel_UMLBase)



@given(instance=UMLModel_UMLBase_strategy)
def test_umlmodel_umlbase_umlID_setter(instance):
    original = instance.umlID
    instance.umlID = original
    assert instance.umlID == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=TemplateSignature_strategy)
@settings(max_examples=50)
def test_templatesignature_instantiation(instance):
    assert isinstance(instance, TemplateSignature)

@given(instance=LinkAction_strategy)
@settings(max_examples=50)
def test_linkaction_instantiation(instance):
    assert isinstance(instance, LinkAction)

@given(instance=UMLModel_WriteLinkAction_strategy)
@settings(max_examples=50)
def test_umlmodel_writelinkaction_instantiation(instance):
    assert isinstance(instance, UMLModel_WriteLinkAction)

@given(instance=UMLModel_ReadLinkAction_strategy)
@settings(max_examples=50)
def test_umlmodel_readlinkaction_instantiation(instance):
    assert isinstance(instance, UMLModel_ReadLinkAction)

@given(instance=StructuralFeature_strategy)
@settings(max_examples=50)
def test_structuralfeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=UMLModel_ProtocolTransition_strategy)
@settings(max_examples=50)
def test_umlmodel_protocoltransition_instantiation(instance):
    assert isinstance(instance, UMLModel_ProtocolTransition)



@given(instance=UMLModel_ProtocolTransition_strategy)
def test_umlmodel_protocoltransition_referred_setter(instance):
    original = instance.referred
    instance.referred = original
    assert instance.referred == original



@given(instance=UMLModel_ProtocolTransition_strategy)
def test_umlmodel_protocoltransition_preCondition_setter(instance):
    original = instance.preCondition
    instance.preCondition = original
    assert instance.preCondition == original



@given(instance=UMLModel_ProtocolTransition_strategy)
def test_umlmodel_protocoltransition_postCondition_setter(instance):
    original = instance.postCondition
    instance.postCondition = original
    assert instance.postCondition == original

@given(instance=StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_instantiation(instance):
    assert isinstance(instance, StateMachine)

@given(instance=InteractionUse_strategy)
@settings(max_examples=50)
def test_interactionuse_instantiation(instance):
    assert isinstance(instance, InteractionUse)

@given(instance=UMLModel_PartDecomposition_strategy)
@settings(max_examples=50)
def test_umlmodel_partdecomposition_instantiation(instance):
    assert isinstance(instance, UMLModel_PartDecomposition)

@given(instance=ConnectableElement_strategy)
@settings(max_examples=50)
def test_connectableelement_instantiation(instance):
    assert isinstance(instance, ConnectableElement)

@given(instance=BehavioralFeature_strategy)
@settings(max_examples=50)
def test_behavioralfeature_instantiation(instance):
    assert isinstance(instance, BehavioralFeature)

@given(instance=Package_strategy)
@settings(max_examples=50)
def test_package_instantiation(instance):
    assert isinstance(instance, Package)

@given(instance=UMLModel_Profile_strategy)
@settings(max_examples=50)
def test_umlmodel_profile_instantiation(instance):
    assert isinstance(instance, UMLModel_Profile)



@given(instance=UMLModel_Profile_strategy)
def test_umlmodel_profile_metamodelReference_setter(instance):
    original = instance.metamodelReference
    instance.metamodelReference = original
    assert instance.metamodelReference == original



@given(instance=UMLModel_Profile_strategy)
def test_umlmodel_profile_metaclassReference_setter(instance):
    original = instance.metaclassReference
    instance.metaclassReference = original
    assert instance.metaclassReference == original



@given(instance=UMLModel_Profile_strategy)
def test_umlmodel_profile_ownedStereotype_setter(instance):
    original = instance.ownedStereotype
    instance.ownedStereotype = original
    assert instance.ownedStereotype == original

@given(instance=UMLModel_Model_strategy)
@settings(max_examples=50)
def test_umlmodel_model_instantiation(instance):
    assert isinstance(instance, UMLModel_Model)



@given(instance=UMLModel_Model_strategy)
def test_umlmodel_model_viewpoint_setter(instance):
    original = instance.viewpoint
    instance.viewpoint = original
    assert instance.viewpoint == original

@given(instance=Abstraction_strategy)
@settings(max_examples=50)
def test_abstraction_instantiation(instance):
    assert isinstance(instance, Abstraction)

@given(instance=UMLModel_Realization_strategy)
@settings(max_examples=50)
def test_umlmodel_realization_instantiation(instance):
    assert isinstance(instance, UMLModel_Realization)

@given(instance=LinkEndData_strategy)
@settings(max_examples=50)
def test_linkenddata_instantiation(instance):
    assert isinstance(instance, LinkEndData)

@given(instance=UMLModel_LinkEndDestructionData_strategy)
@settings(max_examples=50)
def test_umlmodel_linkenddestructiondata_instantiation(instance):
    assert isinstance(instance, UMLModel_LinkEndDestructionData)



@given(instance=UMLModel_LinkEndDestructionData_strategy)
def test_umlmodel_linkenddestructiondata_destroyAt_setter(instance):
    original = instance.destroyAt
    instance.destroyAt = original
    assert instance.destroyAt == original



@given(instance=UMLModel_LinkEndDestructionData_strategy)
def test_umlmodel_linkenddestructiondata_isDestroyDuplicates_setter(instance):
    original = instance.isDestroyDuplicates
    instance.isDestroyDuplicates = original
    assert instance.isDestroyDuplicates == original

@given(instance=UMLModel_LinkEndCreationData_strategy)
@settings(max_examples=50)
def test_umlmodel_linkendcreationdata_instantiation(instance):
    assert isinstance(instance, UMLModel_LinkEndCreationData)



@given(instance=UMLModel_LinkEndCreationData_strategy)
def test_umlmodel_linkendcreationdata_insertAt_setter(instance):
    original = instance.insertAt
    instance.insertAt = original
    assert instance.insertAt == original



@given(instance=UMLModel_LinkEndCreationData_strategy)
def test_umlmodel_linkendcreationdata_isReplaceAll_setter(instance):
    original = instance.isReplaceAll
    instance.isReplaceAll = original
    assert instance.isReplaceAll == original

@given(instance=LiteralSpecification_strategy)
@settings(max_examples=50)
def test_literalspecification_instantiation(instance):
    assert isinstance(instance, LiteralSpecification)

@given(instance=UMLModel_LiteralBoolean_strategy)
@settings(max_examples=50)
def test_umlmodel_literalboolean_instantiation(instance):
    assert isinstance(instance, UMLModel_LiteralBoolean)



@given(instance=UMLModel_LiteralBoolean_strategy)
def test_umlmodel_literalboolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=UMLModel_LiteralNull_strategy)
@settings(max_examples=50)
def test_umlmodel_literalnull_instantiation(instance):
    assert isinstance(instance, UMLModel_LiteralNull)

@given(instance=UMLModel_LiteralString_strategy)
@settings(max_examples=50)
def test_umlmodel_literalstring_instantiation(instance):
    assert isinstance(instance, UMLModel_LiteralString)



@given(instance=UMLModel_LiteralString_strategy)
def test_umlmodel_literalstring_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=UMLModel_LiteralUnlimitedNatural_strategy)
@settings(max_examples=50)
def test_umlmodel_literalunlimitednatural_instantiation(instance):
    assert isinstance(instance, UMLModel_LiteralUnlimitedNatural)



@given(instance=UMLModel_LiteralUnlimitedNatural_strategy)
def test_umlmodel_literalunlimitednatural_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=UMLModel_LiteralInteger_strategy)
@settings(max_examples=50)
def test_umlmodel_literalinteger_instantiation(instance):
    assert isinstance(instance, UMLModel_LiteralInteger)



@given(instance=UMLModel_LiteralInteger_strategy)
def test_umlmodel_literalinteger_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=UMLModel_IntervalConstraint_strategy)
@settings(max_examples=50)
def test_umlmodel_intervalconstraint_instantiation(instance):
    assert isinstance(instance, UMLModel_IntervalConstraint)

@given(instance=UMLModel_InteractionConstraint_strategy)
@settings(max_examples=50)
def test_umlmodel_interactionconstraint_instantiation(instance):
    assert isinstance(instance, UMLModel_InteractionConstraint)

@given(instance=Pin_strategy)
@settings(max_examples=50)
def test_pin_instantiation(instance):
    assert isinstance(instance, Pin)

@given(instance=DeploymentTarget_strategy)
@settings(max_examples=50)
def test_deploymenttarget_instantiation(instance):
    assert isinstance(instance, DeploymentTarget)

@given(instance=UMLModel_ProtocolStateMachine_strategy)
@settings(max_examples=50)
def test_umlmodel_protocolstatemachine_instantiation(instance):
    assert isinstance(instance, UMLModel_ProtocolStateMachine)

@given(instance=MessageEnd_strategy)
@settings(max_examples=50)
def test_messageend_instantiation(instance):
    assert isinstance(instance, MessageEnd)

@given(instance=OpaqueBehavior_strategy)
@settings(max_examples=50)
def test_opaquebehavior_instantiation(instance):
    assert isinstance(instance, OpaqueBehavior)

@given(instance=UMLModel_FunctionBehavior_strategy)
@settings(max_examples=50)
def test_umlmodel_functionbehavior_instantiation(instance):
    assert isinstance(instance, UMLModel_FunctionBehavior)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=UMLModel_FinalState_strategy)
@settings(max_examples=50)
def test_umlmodel_finalstate_instantiation(instance):
    assert isinstance(instance, UMLModel_FinalState)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=UMLModel_Port_strategy)
@settings(max_examples=50)
def test_umlmodel_port_instantiation(instance):
    assert isinstance(instance, UMLModel_Port)



@given(instance=UMLModel_Port_strategy)
def test_umlmodel_port_provided_setter(instance):
    original = instance.provided
    instance.provided = original
    assert instance.provided == original



@given(instance=UMLModel_Port_strategy)
def test_umlmodel_port_protocol_setter(instance):
    original = instance.protocol
    instance.protocol = original
    assert instance.protocol == original



@given(instance=UMLModel_Port_strategy)
def test_umlmodel_port_required_setter(instance):
    original = instance.required
    instance.required = original
    assert instance.required == original



@given(instance=UMLModel_Port_strategy)
def test_umlmodel_port_isService_setter(instance):
    original = instance.isService
    instance.isService = original
    assert instance.isService == original



@given(instance=UMLModel_Port_strategy)
def test_umlmodel_port_redefinedPort_setter(instance):
    original = instance.redefinedPort
    instance.redefinedPort = original
    assert instance.redefinedPort == original



@given(instance=UMLModel_Port_strategy)
def test_umlmodel_port_isBehavior_setter(instance):
    original = instance.isBehavior
    instance.isBehavior = original
    assert instance.isBehavior == original

@given(instance=UMLModel_ExtensionEnd_strategy)
@settings(max_examples=50)
def test_umlmodel_extensionend_instantiation(instance):
    assert isinstance(instance, UMLModel_ExtensionEnd)

@given(instance=OccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_occurrencespecification_instantiation(instance):
    assert isinstance(instance, OccurrenceSpecification)

@given(instance=UMLModel_MessageOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_umlmodel_messageoccurrencespecification_instantiation(instance):
    assert isinstance(instance, UMLModel_MessageOccurrenceSpecification)

@given(instance=UMLModel_ExecutionOccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_umlmodel_executionoccurrencespecification_instantiation(instance):
    assert isinstance(instance, UMLModel_ExecutionOccurrenceSpecification)



@given(instance=UMLModel_ExecutionOccurrenceSpecification_strategy)
def test_umlmodel_executionoccurrencespecification_execution_setter(instance):
    original = instance.execution
    instance.execution = original
    assert instance.execution == original

@given(instance=InstanceSpecification_strategy)
@settings(max_examples=50)
def test_instancespecification_instantiation(instance):
    assert isinstance(instance, InstanceSpecification)

@given(instance=UMLBase_strategy)
@settings(max_examples=50)
def test_umlbase_instantiation(instance):
    assert isinstance(instance, UMLBase)

@given(instance=UMLModel_Element_strategy)
@settings(max_examples=50)
def test_umlmodel_element_instantiation(instance):
    assert isinstance(instance, UMLModel_Element)



@given(instance=UMLModel_Element_strategy)
def test_umlmodel_element_owner_setter(instance):
    original = instance.owner
    instance.owner = original
    assert instance.owner == original



@given(instance=UMLModel_Element_strategy)
def test_umlmodel_element_ownedElement_setter(instance):
    original = instance.ownedElement
    instance.ownedElement = original
    assert instance.ownedElement == original



@given(instance=UMLModel_Element_strategy)
def test_umlmodel_element_href_setter(instance):
    original = instance.href
    instance.href = original
    assert instance.href == original

@given(instance=Observation_strategy)
@settings(max_examples=50)
def test_observation_instantiation(instance):
    assert isinstance(instance, Observation)

@given(instance=UMLModel_TimeObservation_strategy)
@settings(max_examples=50)
def test_umlmodel_timeobservation_instantiation(instance):
    assert isinstance(instance, UMLModel_TimeObservation)



@given(instance=UMLModel_TimeObservation_strategy)
def test_umlmodel_timeobservation_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original



@given(instance=UMLModel_TimeObservation_strategy)
def test_umlmodel_timeobservation_firstEvent_setter(instance):
    original = instance.firstEvent
    instance.firstEvent = original
    assert instance.firstEvent == original

@given(instance=UMLModel_DurationObservation_strategy)
@settings(max_examples=50)
def test_umlmodel_durationobservation_instantiation(instance):
    assert isinstance(instance, UMLModel_DurationObservation)



@given(instance=UMLModel_DurationObservation_strategy)
def test_umlmodel_durationobservation_firstEvent_setter(instance):
    original = instance.firstEvent
    instance.firstEvent = original
    assert instance.firstEvent == original



@given(instance=UMLModel_DurationObservation_strategy)
def test_umlmodel_durationobservation_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original

@given(instance=Interval_strategy)
@settings(max_examples=50)
def test_interval_instantiation(instance):
    assert isinstance(instance, Interval)

@given(instance=UMLModel_TimeInterval_strategy)
@settings(max_examples=50)
def test_umlmodel_timeinterval_instantiation(instance):
    assert isinstance(instance, UMLModel_TimeInterval)

@given(instance=UMLModel_DurationInterval_strategy)
@settings(max_examples=50)
def test_umlmodel_durationinterval_instantiation(instance):
    assert isinstance(instance, UMLModel_DurationInterval)

@given(instance=IntervalConstraint_strategy)
@settings(max_examples=50)
def test_intervalconstraint_instantiation(instance):
    assert isinstance(instance, IntervalConstraint)

@given(instance=UMLModel_TimeConstraint_strategy)
@settings(max_examples=50)
def test_umlmodel_timeconstraint_instantiation(instance):
    assert isinstance(instance, UMLModel_TimeConstraint)



@given(instance=UMLModel_TimeConstraint_strategy)
def test_umlmodel_timeconstraint_firstEvent_setter(instance):
    original = instance.firstEvent
    instance.firstEvent = original
    assert instance.firstEvent == original

@given(instance=UMLModel_DurationConstraint_strategy)
@settings(max_examples=50)
def test_umlmodel_durationconstraint_instantiation(instance):
    assert isinstance(instance, UMLModel_DurationConstraint)



@given(instance=UMLModel_DurationConstraint_strategy)
def test_umlmodel_durationconstraint_firstEvent_setter(instance):
    original = instance.firstEvent
    instance.firstEvent = original
    assert instance.firstEvent == original

@given(instance=ValueSpecification_strategy)
@settings(max_examples=50)
def test_valuespecification_instantiation(instance):
    assert isinstance(instance, ValueSpecification)

@given(instance=UMLModel_Expression_strategy)
@settings(max_examples=50)
def test_umlmodel_expression_instantiation(instance):
    assert isinstance(instance, UMLModel_Expression)



@given(instance=UMLModel_Expression_strategy)
def test_umlmodel_expression_symbol_setter(instance):
    original = instance.symbol
    instance.symbol = original
    assert instance.symbol == original

@given(instance=UMLModel_LiteralSpecification_strategy)
@settings(max_examples=50)
def test_umlmodel_literalspecification_instantiation(instance):
    assert isinstance(instance, UMLModel_LiteralSpecification)

@given(instance=UMLModel_TimeExpression_strategy)
@settings(max_examples=50)
def test_umlmodel_timeexpression_instantiation(instance):
    assert isinstance(instance, UMLModel_TimeExpression)



@given(instance=UMLModel_TimeExpression_strategy)
def test_umlmodel_timeexpression_expr_setter(instance):
    original = instance.expr
    instance.expr = original
    assert instance.expr == original



@given(instance=UMLModel_TimeExpression_strategy)
def test_umlmodel_timeexpression_observation_setter(instance):
    original = instance.observation
    instance.observation = original
    assert instance.observation == original

@given(instance=UMLModel_Interval_strategy)
@settings(max_examples=50)
def test_umlmodel_interval_instantiation(instance):
    assert isinstance(instance, UMLModel_Interval)



@given(instance=UMLModel_Interval_strategy)
def test_umlmodel_interval_max_setter(instance):
    original = instance.max
    instance.max = original
    assert instance.max == original



@given(instance=UMLModel_Interval_strategy)
def test_umlmodel_interval_min_setter(instance):
    original = instance.min
    instance.min = original
    assert instance.min == original

@given(instance=UMLModel_InstanceValue_strategy)
@settings(max_examples=50)
def test_umlmodel_instancevalue_instantiation(instance):
    assert isinstance(instance, UMLModel_InstanceValue)



@given(instance=UMLModel_InstanceValue_strategy)
def test_umlmodel_instancevalue_instance_setter(instance):
    original = instance.instance
    instance.instance = original
    assert instance.instance == original

@given(instance=UMLModel_Duration_strategy)
@settings(max_examples=50)
def test_umlmodel_duration_instantiation(instance):
    assert isinstance(instance, UMLModel_Duration)



@given(instance=UMLModel_Duration_strategy)
def test_umlmodel_duration_expr_setter(instance):
    original = instance.expr
    instance.expr = original
    assert instance.expr == original



@given(instance=UMLModel_Duration_strategy)
def test_umlmodel_duration_observation_setter(instance):
    original = instance.observation
    instance.observation = original
    assert instance.observation == original

@given(instance=UMLModel_EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_umlmodel_enumerationliteral_instantiation(instance):
    assert isinstance(instance, UMLModel_EnumerationLiteral)



@given(instance=UMLModel_EnumerationLiteral_strategy)
def test_umlmodel_enumerationliteral_enumeration_setter(instance):
    original = instance.enumeration
    instance.enumeration = original
    assert instance.enumeration == original

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=UMLModel_PrimitiveType_strategy)
@settings(max_examples=50)
def test_umlmodel_primitivetype_instantiation(instance):
    assert isinstance(instance, UMLModel_PrimitiveType)

@given(instance=UMLModel_Enumeration_strategy)
@settings(max_examples=50)
def test_umlmodel_enumeration_instantiation(instance):
    assert isinstance(instance, UMLModel_Enumeration)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=UMLModel_ExecutionEnvironment_strategy)
@settings(max_examples=50)
def test_umlmodel_executionenvironment_instantiation(instance):
    assert isinstance(instance, UMLModel_ExecutionEnvironment)

@given(instance=UMLModel_Device_strategy)
@settings(max_examples=50)
def test_umlmodel_device_instantiation(instance):
    assert isinstance(instance, UMLModel_Device)

@given(instance=Artifact_strategy)
@settings(max_examples=50)
def test_artifact_instantiation(instance):
    assert isinstance(instance, Artifact)

@given(instance=UMLModel_DeploymentSpecification_strategy)
@settings(max_examples=50)
def test_umlmodel_deploymentspecification_instantiation(instance):
    assert isinstance(instance, UMLModel_DeploymentSpecification)



@given(instance=UMLModel_DeploymentSpecification_strategy)
def test_umlmodel_deploymentspecification_deployment_setter(instance):
    original = instance.deployment
    instance.deployment = original
    assert instance.deployment == original



@given(instance=UMLModel_DeploymentSpecification_strategy)
def test_umlmodel_deploymentspecification_executionLocation_setter(instance):
    original = instance.executionLocation
    instance.executionLocation = original
    assert instance.executionLocation == original



@given(instance=UMLModel_DeploymentSpecification_strategy)
def test_umlmodel_deploymentspecification_deploymentLocation_setter(instance):
    original = instance.deploymentLocation
    instance.deploymentLocation = original
    assert instance.deploymentLocation == original

@given(instance=MultiplicityElement_strategy)
@settings(max_examples=50)
def test_multiplicityelement_instantiation(instance):
    assert isinstance(instance, MultiplicityElement)

@given(instance=UMLModel_ConnectorEnd_strategy)
@settings(max_examples=50)
def test_umlmodel_connectorend_instantiation(instance):
    assert isinstance(instance, UMLModel_ConnectorEnd)



@given(instance=UMLModel_ConnectorEnd_strategy)
def test_umlmodel_connectorend_partWithPort_setter(instance):
    original = instance.partWithPort
    instance.partWithPort = original
    assert instance.partWithPort == original



@given(instance=UMLModel_ConnectorEnd_strategy)
def test_umlmodel_connectorend_definingEnd_setter(instance):
    original = instance.definingEnd
    instance.definingEnd = original
    assert instance.definingEnd == original



@given(instance=UMLModel_ConnectorEnd_strategy)
def test_umlmodel_connectorend_role_setter(instance):
    original = instance.role
    instance.role = original
    assert instance.role == original

@given(instance=DirectedRelationship_strategy)
@settings(max_examples=50)
def test_directedrelationship_instantiation(instance):
    assert isinstance(instance, DirectedRelationship)

@given(instance=UMLModel_TemplateBinding_strategy)
@settings(max_examples=50)
def test_umlmodel_templatebinding_instantiation(instance):
    assert isinstance(instance, UMLModel_TemplateBinding)



@given(instance=UMLModel_TemplateBinding_strategy)
def test_umlmodel_templatebinding_boundElement_setter(instance):
    original = instance.boundElement
    instance.boundElement = original
    assert instance.boundElement == original



@given(instance=UMLModel_TemplateBinding_strategy)
def test_umlmodel_templatebinding_signature_setter(instance):
    original = instance.signature
    instance.signature = original
    assert instance.signature == original

@given(instance=UMLModel_ProfileApplication_strategy)
@settings(max_examples=50)
def test_umlmodel_profileapplication_instantiation(instance):
    assert isinstance(instance, UMLModel_ProfileApplication)



@given(instance=UMLModel_ProfileApplication_strategy)
def test_umlmodel_profileapplication_applyingPackage_setter(instance):
    original = instance.applyingPackage
    instance.applyingPackage = original
    assert instance.applyingPackage == original



@given(instance=UMLModel_ProfileApplication_strategy)
def test_umlmodel_profileapplication_isStrict_setter(instance):
    original = instance.isStrict
    instance.isStrict = original
    assert instance.isStrict == original



@given(instance=UMLModel_ProfileApplication_strategy)
def test_umlmodel_profileapplication_appliedProfile_setter(instance):
    original = instance.appliedProfile
    instance.appliedProfile = original
    assert instance.appliedProfile == original

@given(instance=UMLModel_ElementImport_strategy)
@settings(max_examples=50)
def test_umlmodel_elementimport_instantiation(instance):
    assert isinstance(instance, UMLModel_ElementImport)



@given(instance=UMLModel_ElementImport_strategy)
def test_umlmodel_elementimport_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original



@given(instance=UMLModel_ElementImport_strategy)
def test_umlmodel_elementimport_importingNamespace_setter(instance):
    original = instance.importingNamespace
    instance.importingNamespace = original
    assert instance.importingNamespace == original



@given(instance=UMLModel_ElementImport_strategy)
def test_umlmodel_elementimport_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=UMLModel_PackageImport_strategy)
@settings(max_examples=50)
def test_umlmodel_packageimport_instantiation(instance):
    assert isinstance(instance, UMLModel_PackageImport)



@given(instance=UMLModel_PackageImport_strategy)
def test_umlmodel_packageimport_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original



@given(instance=UMLModel_PackageImport_strategy)
def test_umlmodel_packageimport_importingNamespace_setter(instance):
    original = instance.importingNamespace
    instance.importingNamespace = original
    assert instance.importingNamespace == original

@given(instance=UMLModel_PackageMerge_strategy)
@settings(max_examples=50)
def test_umlmodel_packagemerge_instantiation(instance):
    assert isinstance(instance, UMLModel_PackageMerge)



@given(instance=UMLModel_PackageMerge_strategy)
def test_umlmodel_packagemerge_receivingPackage_setter(instance):
    original = instance.receivingPackage
    instance.receivingPackage = original
    assert instance.receivingPackage == original



@given(instance=UMLModel_PackageMerge_strategy)
def test_umlmodel_packagemerge_mergedPackage_setter(instance):
    original = instance.mergedPackage
    instance.mergedPackage = original
    assert instance.mergedPackage == original

@given(instance=UMLModel_ProtocolConformance_strategy)
@settings(max_examples=50)
def test_umlmodel_protocolconformance_instantiation(instance):
    assert isinstance(instance, UMLModel_ProtocolConformance)



@given(instance=UMLModel_ProtocolConformance_strategy)
def test_umlmodel_protocolconformance_specificMachine_setter(instance):
    original = instance.specificMachine
    instance.specificMachine = original
    assert instance.specificMachine == original



@given(instance=UMLModel_ProtocolConformance_strategy)
def test_umlmodel_protocolconformance_generalMachine_setter(instance):
    original = instance.generalMachine
    instance.generalMachine = original
    assert instance.generalMachine == original

@given(instance=ParameterableElement_strategy)
@settings(max_examples=50)
def test_parameterableelement_instantiation(instance):
    assert isinstance(instance, ParameterableElement)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=ControlNode_strategy)
@settings(max_examples=50)
def test_controlnode_instantiation(instance):
    assert isinstance(instance, ControlNode)

@given(instance=UMLModel_MergeNode_strategy)
@settings(max_examples=50)
def test_umlmodel_mergenode_instantiation(instance):
    assert isinstance(instance, UMLModel_MergeNode)

@given(instance=UMLModel_ForkNode_strategy)
@settings(max_examples=50)
def test_umlmodel_forknode_instantiation(instance):
    assert isinstance(instance, UMLModel_ForkNode)

@given(instance=UMLModel_FinalNode_strategy)
@settings(max_examples=50)
def test_umlmodel_finalnode_instantiation(instance):
    assert isinstance(instance, UMLModel_FinalNode)

@given(instance=UMLModel_JoinNode_strategy)
@settings(max_examples=50)
def test_umlmodel_joinnode_instantiation(instance):
    assert isinstance(instance, UMLModel_JoinNode)



@given(instance=UMLModel_JoinNode_strategy)
def test_umlmodel_joinnode_isCombineDuplicate_setter(instance):
    original = instance.isCombineDuplicate
    instance.isCombineDuplicate = original
    assert instance.isCombineDuplicate == original

@given(instance=UMLModel_InitialNode_strategy)
@settings(max_examples=50)
def test_umlmodel_initialnode_instantiation(instance):
    assert isinstance(instance, UMLModel_InitialNode)

@given(instance=UMLModel_ConnectableElement_strategy)
@settings(max_examples=50)
def test_umlmodel_connectableelement_instantiation(instance):
    assert isinstance(instance, UMLModel_ConnectableElement)



@given(instance=UMLModel_ConnectableElement_strategy)
def test_umlmodel_connectableelement_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original

@given(instance=UMLModel_DecisionNode_strategy)
@settings(max_examples=50)
def test_umlmodel_decisionnode_instantiation(instance):
    assert isinstance(instance, UMLModel_DecisionNode)



@given(instance=UMLModel_DecisionNode_strategy)
def test_umlmodel_decisionnode_decisionInput_setter(instance):
    original = instance.decisionInput
    instance.decisionInput = original
    assert instance.decisionInput == original

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=UMLModel_Slot_strategy)
@settings(max_examples=50)
def test_umlmodel_slot_instantiation(instance):
    assert isinstance(instance, UMLModel_Slot)



@given(instance=UMLModel_Slot_strategy)
def test_umlmodel_slot_owningInstance_setter(instance):
    original = instance.owningInstance
    instance.owningInstance = original
    assert instance.owningInstance == original



@given(instance=UMLModel_Slot_strategy)
def test_umlmodel_slot_definingFeature_setter(instance):
    original = instance.definingFeature
    instance.definingFeature = original
    assert instance.definingFeature == original

@given(instance=UMLModel_LinkEndData_strategy)
@settings(max_examples=50)
def test_umlmodel_linkenddata_instantiation(instance):
    assert isinstance(instance, UMLModel_LinkEndData)



@given(instance=UMLModel_LinkEndData_strategy)
def test_umlmodel_linkenddata_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original



@given(instance=UMLModel_LinkEndData_strategy)
def test_umlmodel_linkenddata_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=UMLModel_ParameterableElement_strategy)
@settings(max_examples=50)
def test_umlmodel_parameterableelement_instantiation(instance):
    assert isinstance(instance, UMLModel_ParameterableElement)



@given(instance=UMLModel_ParameterableElement_strategy)
def test_umlmodel_parameterableelement_owningTemplateParameter_setter(instance):
    original = instance.owningTemplateParameter
    instance.owningTemplateParameter = original
    assert instance.owningTemplateParameter == original



@given(instance=UMLModel_ParameterableElement_strategy)
def test_umlmodel_parameterableelement_templateParameter_setter(instance):
    original = instance.templateParameter
    instance.templateParameter = original
    assert instance.templateParameter == original

@given(instance=UMLModel_TemplateParameter_strategy)
@settings(max_examples=50)
def test_umlmodel_templateparameter_instantiation(instance):
    assert isinstance(instance, UMLModel_TemplateParameter)



@given(instance=UMLModel_TemplateParameter_strategy)
def test_umlmodel_templateparameter_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original



@given(instance=UMLModel_TemplateParameter_strategy)
def test_umlmodel_templateparameter_parameteredElement_setter(instance):
    original = instance.parameteredElement
    instance.parameteredElement = original
    assert instance.parameteredElement == original



@given(instance=UMLModel_TemplateParameter_strategy)
def test_umlmodel_templateparameter_signature_setter(instance):
    original = instance.signature
    instance.signature = original
    assert instance.signature == original

@given(instance=UMLModel_MultiplicityElement_strategy)
@settings(max_examples=50)
def test_umlmodel_multiplicityelement_instantiation(instance):
    assert isinstance(instance, UMLModel_MultiplicityElement)



@given(instance=UMLModel_MultiplicityElement_strategy)
def test_umlmodel_multiplicityelement_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original



@given(instance=UMLModel_MultiplicityElement_strategy)
def test_umlmodel_multiplicityelement_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original



@given(instance=UMLModel_MultiplicityElement_strategy)
def test_umlmodel_multiplicityelement_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original



@given(instance=UMLModel_MultiplicityElement_strategy)
def test_umlmodel_multiplicityelement_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original

@given(instance=UMLModel_TemplateParameterSubstitution_strategy)
@settings(max_examples=50)
def test_umlmodel_templateparametersubstitution_instantiation(instance):
    assert isinstance(instance, UMLModel_TemplateParameterSubstitution)



@given(instance=UMLModel_TemplateParameterSubstitution_strategy)
def test_umlmodel_templateparametersubstitution_templateBinding_setter(instance):
    original = instance.templateBinding
    instance.templateBinding = original
    assert instance.templateBinding == original



@given(instance=UMLModel_TemplateParameterSubstitution_strategy)
def test_umlmodel_templateparametersubstitution_formal_setter(instance):
    original = instance.formal
    instance.formal = original
    assert instance.formal == original



@given(instance=UMLModel_TemplateParameterSubstitution_strategy)
def test_umlmodel_templateparametersubstitution_actual_setter(instance):
    original = instance.actual
    instance.actual = original
    assert instance.actual == original

@given(instance=UMLModel_TemplateableElement_strategy)
@settings(max_examples=50)
def test_umlmodel_templateableelement_instantiation(instance):
    assert isinstance(instance, UMLModel_TemplateableElement)

@given(instance=UMLModel_Relationship_strategy)
@settings(max_examples=50)
def test_umlmodel_relationship_instantiation(instance):
    assert isinstance(instance, UMLModel_Relationship)



@given(instance=UMLModel_Relationship_strategy)
def test_umlmodel_relationship_relatedElement_setter(instance):
    original = instance.relatedElement
    instance.relatedElement = original
    assert instance.relatedElement == original

@given(instance=UMLModel_ExceptionHandler_strategy)
@settings(max_examples=50)
def test_umlmodel_exceptionhandler_instantiation(instance):
    assert isinstance(instance, UMLModel_ExceptionHandler)



@given(instance=UMLModel_ExceptionHandler_strategy)
def test_umlmodel_exceptionhandler_handlerBody_setter(instance):
    original = instance.handlerBody
    instance.handlerBody = original
    assert instance.handlerBody == original



@given(instance=UMLModel_ExceptionHandler_strategy)
def test_umlmodel_exceptionhandler_exceptionInput_setter(instance):
    original = instance.exceptionInput
    instance.exceptionInput = original
    assert instance.exceptionInput == original



@given(instance=UMLModel_ExceptionHandler_strategy)
def test_umlmodel_exceptionhandler_exceptionType_setter(instance):
    original = instance.exceptionType
    instance.exceptionType = original
    assert instance.exceptionType == original



@given(instance=UMLModel_ExceptionHandler_strategy)
def test_umlmodel_exceptionhandler_protectedNode_setter(instance):
    original = instance.protectedNode
    instance.protectedNode = original
    assert instance.protectedNode == original

@given(instance=UMLModel_NamedElement_strategy)
@settings(max_examples=50)
def test_umlmodel_namedelement_instantiation(instance):
    assert isinstance(instance, UMLModel_NamedElement)



@given(instance=UMLModel_NamedElement_strategy)
def test_umlmodel_namedelement_qualifiedName_setter(instance):
    original = instance.qualifiedName
    instance.qualifiedName = original
    assert instance.qualifiedName == original



@given(instance=UMLModel_NamedElement_strategy)
def test_umlmodel_namedelement_namespace_setter(instance):
    original = instance.namespace
    instance.namespace = original
    assert instance.namespace == original



@given(instance=UMLModel_NamedElement_strategy)
def test_umlmodel_namedelement_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original



@given(instance=UMLModel_NamedElement_strategy)
def test_umlmodel_namedelement_clientDependency_setter(instance):
    original = instance.clientDependency
    instance.clientDependency = original
    assert instance.clientDependency == original



@given(instance=UMLModel_NamedElement_strategy)
def test_umlmodel_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=UMLModel_QualifierValue_strategy)
@settings(max_examples=50)
def test_umlmodel_qualifiervalue_instantiation(instance):
    assert isinstance(instance, UMLModel_QualifierValue)



@given(instance=UMLModel_QualifierValue_strategy)
def test_umlmodel_qualifiervalue_qualifier_setter(instance):
    original = instance.qualifier
    instance.qualifier = original
    assert instance.qualifier == original



@given(instance=UMLModel_QualifierValue_strategy)
def test_umlmodel_qualifiervalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=UMLModel_TemplateSignature_strategy)
@settings(max_examples=50)
def test_umlmodel_templatesignature_instantiation(instance):
    assert isinstance(instance, UMLModel_TemplateSignature)



@given(instance=UMLModel_TemplateSignature_strategy)
def test_umlmodel_templatesignature_parameter_setter(instance):
    original = instance.parameter
    instance.parameter = original
    assert instance.parameter == original



@given(instance=UMLModel_TemplateSignature_strategy)
def test_umlmodel_templatesignature_template_setter(instance):
    original = instance.template
    instance.template = original
    assert instance.template == original

@given(instance=UMLModel_Image_strategy)
@settings(max_examples=50)
def test_umlmodel_image_instantiation(instance):
    assert isinstance(instance, UMLModel_Image)



@given(instance=UMLModel_Image_strategy)
def test_umlmodel_image_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original



@given(instance=UMLModel_Image_strategy)
def test_umlmodel_image_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original



@given(instance=UMLModel_Image_strategy)
def test_umlmodel_image_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=FinalNode_strategy)
@settings(max_examples=50)
def test_finalnode_instantiation(instance):
    assert isinstance(instance, FinalNode)

@given(instance=UMLModel_FlowFinalNode_strategy)
@settings(max_examples=50)
def test_umlmodel_flowfinalnode_instantiation(instance):
    assert isinstance(instance, UMLModel_FlowFinalNode)

@given(instance=UMLModel_ActivityFinalNode_strategy)
@settings(max_examples=50)
def test_umlmodel_activityfinalnode_instantiation(instance):
    assert isinstance(instance, UMLModel_ActivityFinalNode)

@given(instance=ObjectNode_strategy)
@settings(max_examples=50)
def test_objectnode_instantiation(instance):
    assert isinstance(instance, ObjectNode)

@given(instance=UMLModel_Pin_strategy)
@settings(max_examples=50)
def test_umlmodel_pin_instantiation(instance):
    assert isinstance(instance, UMLModel_Pin)



@given(instance=UMLModel_Pin_strategy)
def test_umlmodel_pin_isControl_setter(instance):
    original = instance.isControl
    instance.isControl = original
    assert instance.isControl == original

@given(instance=UMLModel_ExpansionNode_strategy)
@settings(max_examples=50)
def test_umlmodel_expansionnode_instantiation(instance):
    assert isinstance(instance, UMLModel_ExpansionNode)



@given(instance=UMLModel_ExpansionNode_strategy)
def test_umlmodel_expansionnode_regionAsInput_setter(instance):
    original = instance.regionAsInput
    instance.regionAsInput = original
    assert instance.regionAsInput == original



@given(instance=UMLModel_ExpansionNode_strategy)
def test_umlmodel_expansionnode_regionAsOutput_setter(instance):
    original = instance.regionAsOutput
    instance.regionAsOutput = original
    assert instance.regionAsOutput == original

@given(instance=UMLModel_ActivityParameterNode_strategy)
@settings(max_examples=50)
def test_umlmodel_activityparameternode_instantiation(instance):
    assert isinstance(instance, UMLModel_ActivityParameterNode)



@given(instance=UMLModel_ActivityParameterNode_strategy)
def test_umlmodel_activityparameternode_parameter_setter(instance):
    original = instance.parameter
    instance.parameter = original
    assert instance.parameter == original

@given(instance=RedefinableElement_strategy)
@settings(max_examples=50)
def test_redefinableelement_instantiation(instance):
    assert isinstance(instance, RedefinableElement)

@given(instance=UMLModel_ExtensionPoint_strategy)
@settings(max_examples=50)
def test_umlmodel_extensionpoint_instantiation(instance):
    assert isinstance(instance, UMLModel_ExtensionPoint)



@given(instance=UMLModel_ExtensionPoint_strategy)
def test_umlmodel_extensionpoint_useCase_setter(instance):
    original = instance.useCase
    instance.useCase = original
    assert instance.useCase == original

@given(instance=UMLModel_Feature_strategy)
@settings(max_examples=50)
def test_umlmodel_feature_instantiation(instance):
    assert isinstance(instance, UMLModel_Feature)



@given(instance=UMLModel_Feature_strategy)
def test_umlmodel_feature_featuringClassifier_setter(instance):
    original = instance.featuringClassifier
    instance.featuringClassifier = original
    assert instance.featuringClassifier == original



@given(instance=UMLModel_Feature_strategy)
def test_umlmodel_feature_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original

@given(instance=UMLModel_RedefinableTemplateSignature_strategy)
@settings(max_examples=50)
def test_umlmodel_redefinabletemplatesignature_instantiation(instance):
    assert isinstance(instance, UMLModel_RedefinableTemplateSignature)



@given(instance=UMLModel_RedefinableTemplateSignature_strategy)
def test_umlmodel_redefinabletemplatesignature_extendedSignature_setter(instance):
    original = instance.extendedSignature
    instance.extendedSignature = original
    assert instance.extendedSignature == original



@given(instance=UMLModel_RedefinableTemplateSignature_strategy)
def test_umlmodel_redefinabletemplatesignature_inheritedParameter_setter(instance):
    original = instance.inheritedParameter
    instance.inheritedParameter = original
    assert instance.inheritedParameter == original



@given(instance=UMLModel_RedefinableTemplateSignature_strategy)
def test_umlmodel_redefinabletemplatesignature_classifier_setter(instance):
    original = instance.classifier
    instance.classifier = original
    assert instance.classifier == original

@given(instance=ActivityGroup_strategy)
@settings(max_examples=50)
def test_activitygroup_instantiation(instance):
    assert isinstance(instance, ActivityGroup)

@given(instance=UMLModel_InterruptibleActivityRegion_strategy)
@settings(max_examples=50)
def test_umlmodel_interruptibleactivityregion_instantiation(instance):
    assert isinstance(instance, UMLModel_InterruptibleActivityRegion)



@given(instance=UMLModel_InterruptibleActivityRegion_strategy)
def test_umlmodel_interruptibleactivityregion_interruptingEdge_setter(instance):
    original = instance.interruptingEdge
    instance.interruptingEdge = original
    assert instance.interruptingEdge == original



@given(instance=UMLModel_InterruptibleActivityRegion_strategy)
def test_umlmodel_interruptibleactivityregion_node_setter(instance):
    original = instance.node
    instance.node = original
    assert instance.node == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=UMLModel_Vertex_strategy)
@settings(max_examples=50)
def test_umlmodel_vertex_instantiation(instance):
    assert isinstance(instance, UMLModel_Vertex)



@given(instance=UMLModel_Vertex_strategy)
def test_umlmodel_vertex_incoming_setter(instance):
    original = instance.incoming
    instance.incoming = original
    assert instance.incoming == original



@given(instance=UMLModel_Vertex_strategy)
def test_umlmodel_vertex_outgoing_setter(instance):
    original = instance.outgoing
    instance.outgoing = original
    assert instance.outgoing == original



@given(instance=UMLModel_Vertex_strategy)
def test_umlmodel_vertex_container_setter(instance):
    original = instance.container
    instance.container = original
    assert instance.container == original

@given(instance=UMLModel_GeneralOrdering_strategy)
@settings(max_examples=50)
def test_umlmodel_generalordering_instantiation(instance):
    assert isinstance(instance, UMLModel_GeneralOrdering)



@given(instance=UMLModel_GeneralOrdering_strategy)
def test_umlmodel_generalordering_before_setter(instance):
    original = instance.before
    instance.before = original
    assert instance.before == original



@given(instance=UMLModel_GeneralOrdering_strategy)
def test_umlmodel_generalordering_after_setter(instance):
    original = instance.after
    instance.after = original
    assert instance.after == original

@given(instance=UMLModel_Lifeline_strategy)
@settings(max_examples=50)
def test_umlmodel_lifeline_instantiation(instance):
    assert isinstance(instance, UMLModel_Lifeline)



@given(instance=UMLModel_Lifeline_strategy)
def test_umlmodel_lifeline_decomposedAs_setter(instance):
    original = instance.decomposedAs
    instance.decomposedAs = original
    assert instance.decomposedAs == original



@given(instance=UMLModel_Lifeline_strategy)
def test_umlmodel_lifeline_interaction_setter(instance):
    original = instance.interaction
    instance.interaction = original
    assert instance.interaction == original



@given(instance=UMLModel_Lifeline_strategy)
def test_umlmodel_lifeline_represents_setter(instance):
    original = instance.represents
    instance.represents = original
    assert instance.represents == original



@given(instance=UMLModel_Lifeline_strategy)
def test_umlmodel_lifeline_coveredBy_setter(instance):
    original = instance.coveredBy
    instance.coveredBy = original
    assert instance.coveredBy == original

@given(instance=UMLModel_MessageEnd_strategy)
@settings(max_examples=50)
def test_umlmodel_messageend_instantiation(instance):
    assert isinstance(instance, UMLModel_MessageEnd)



@given(instance=UMLModel_MessageEnd_strategy)
def test_umlmodel_messageend_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=UMLModel_Message_strategy)
@settings(max_examples=50)
def test_umlmodel_message_instantiation(instance):
    assert isinstance(instance, UMLModel_Message)



@given(instance=UMLModel_Message_strategy)
def test_umlmodel_message_signature_setter(instance):
    original = instance.signature
    instance.signature = original
    assert instance.signature == original



@given(instance=UMLModel_Message_strategy)
def test_umlmodel_message_receiveEvent_setter(instance):
    original = instance.receiveEvent
    instance.receiveEvent = original
    assert instance.receiveEvent == original



@given(instance=UMLModel_Message_strategy)
def test_umlmodel_message_messageSort_setter(instance):
    original = instance.messageSort
    instance.messageSort = original
    assert instance.messageSort == original



@given(instance=UMLModel_Message_strategy)
def test_umlmodel_message_interaction_setter(instance):
    original = instance.interaction
    instance.interaction = original
    assert instance.interaction == original



@given(instance=UMLModel_Message_strategy)
def test_umlmodel_message_sendEvent_setter(instance):
    original = instance.sendEvent
    instance.sendEvent = original
    assert instance.sendEvent == original



@given(instance=UMLModel_Message_strategy)
def test_umlmodel_message_messageKind_setter(instance):
    original = instance.messageKind
    instance.messageKind = original
    assert instance.messageKind == original



@given(instance=UMLModel_Message_strategy)
def test_umlmodel_message_connector_setter(instance):
    original = instance.connector
    instance.connector = original
    assert instance.connector == original

@given(instance=UMLModel_DeploymentTarget_strategy)
@settings(max_examples=50)
def test_umlmodel_deploymenttarget_instantiation(instance):
    assert isinstance(instance, UMLModel_DeploymentTarget)



@given(instance=UMLModel_DeploymentTarget_strategy)
def test_umlmodel_deploymenttarget_deployedElement_setter(instance):
    original = instance.deployedElement
    instance.deployedElement = original
    assert instance.deployedElement == original

@given(instance=UMLModel_TypedElement_strategy)
@settings(max_examples=50)
def test_umlmodel_typedelement_instantiation(instance):
    assert isinstance(instance, UMLModel_TypedElement)



@given(instance=UMLModel_TypedElement_strategy)
def test_umlmodel_typedelement_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=UMLModel_RedefinableElement_strategy)
@settings(max_examples=50)
def test_umlmodel_redefinableelement_instantiation(instance):
    assert isinstance(instance, UMLModel_RedefinableElement)



@given(instance=UMLModel_RedefinableElement_strategy)
def test_umlmodel_redefinableelement_redefinitionContext_setter(instance):
    original = instance.redefinitionContext
    instance.redefinitionContext = original
    assert instance.redefinitionContext == original



@given(instance=UMLModel_RedefinableElement_strategy)
def test_umlmodel_redefinableelement_redefinedElement_setter(instance):
    original = instance.redefinedElement
    instance.redefinedElement = original
    assert instance.redefinedElement == original



@given(instance=UMLModel_RedefinableElement_strategy)
def test_umlmodel_redefinableelement_isLeaf_setter(instance):
    original = instance.isLeaf
    instance.isLeaf = original
    assert instance.isLeaf == original

@given(instance=UMLModel_Include_strategy)
@settings(max_examples=50)
def test_umlmodel_include_instantiation(instance):
    assert isinstance(instance, UMLModel_Include)



@given(instance=UMLModel_Include_strategy)
def test_umlmodel_include_includingCase_setter(instance):
    original = instance.includingCase
    instance.includingCase = original
    assert instance.includingCase == original



@given(instance=UMLModel_Include_strategy)
def test_umlmodel_include_addition_setter(instance):
    original = instance.addition
    instance.addition = original
    assert instance.addition == original

@given(instance=UMLModel_Extend_strategy)
@settings(max_examples=50)
def test_umlmodel_extend_instantiation(instance):
    assert isinstance(instance, UMLModel_Extend)



@given(instance=UMLModel_Extend_strategy)
def test_umlmodel_extend_extension_setter(instance):
    original = instance.extension
    instance.extension = original
    assert instance.extension == original



@given(instance=UMLModel_Extend_strategy)
def test_umlmodel_extend_extensionLocation_setter(instance):
    original = instance.extensionLocation
    instance.extensionLocation = original
    assert instance.extensionLocation == original



@given(instance=UMLModel_Extend_strategy)
def test_umlmodel_extend_extendedCase_setter(instance):
    original = instance.extendedCase
    instance.extendedCase = original
    assert instance.extendedCase == original

@given(instance=UMLModel_InteractionFragment_strategy)
@settings(max_examples=50)
def test_umlmodel_interactionfragment_instantiation(instance):
    assert isinstance(instance, UMLModel_InteractionFragment)



@given(instance=UMLModel_InteractionFragment_strategy)
def test_umlmodel_interactionfragment_enclosingInteraction_setter(instance):
    original = instance.enclosingInteraction
    instance.enclosingInteraction = original
    assert instance.enclosingInteraction == original



@given(instance=UMLModel_InteractionFragment_strategy)
def test_umlmodel_interactionfragment_covered_setter(instance):
    original = instance.covered
    instance.covered = original
    assert instance.covered == original



@given(instance=UMLModel_InteractionFragment_strategy)
def test_umlmodel_interactionfragment_enclosingOperand_setter(instance):
    original = instance.enclosingOperand
    instance.enclosingOperand = original
    assert instance.enclosingOperand == original

@given(instance=UMLModel_Namespace_strategy)
@settings(max_examples=50)
def test_umlmodel_namespace_instantiation(instance):
    assert isinstance(instance, UMLModel_Namespace)



@given(instance=UMLModel_Namespace_strategy)
def test_umlmodel_namespace_importedMember_setter(instance):
    original = instance.importedMember
    instance.importedMember = original
    assert instance.importedMember == original



@given(instance=UMLModel_Namespace_strategy)
def test_umlmodel_namespace_member_setter(instance):
    original = instance.member
    instance.member = original
    assert instance.member == original



@given(instance=UMLModel_Namespace_strategy)
def test_umlmodel_namespace_ownedMember_setter(instance):
    original = instance.ownedMember
    instance.ownedMember = original
    assert instance.ownedMember == original

@given(instance=UMLModel_DeployedArtifact_strategy)
@settings(max_examples=50)
def test_umlmodel_deployedartifact_instantiation(instance):
    assert isinstance(instance, UMLModel_DeployedArtifact)

@given(instance=UMLModel_ActivityPartition_strategy)
@settings(max_examples=50)
def test_umlmodel_activitypartition_instantiation(instance):
    assert isinstance(instance, UMLModel_ActivityPartition)



@given(instance=UMLModel_ActivityPartition_strategy)
def test_umlmodel_activitypartition_isDimension_setter(instance):
    original = instance.isDimension
    instance.isDimension = original
    assert instance.isDimension == original



@given(instance=UMLModel_ActivityPartition_strategy)
def test_umlmodel_activitypartition_superPartition_setter(instance):
    original = instance.superPartition
    instance.superPartition = original
    assert instance.superPartition == original



@given(instance=UMLModel_ActivityPartition_strategy)
def test_umlmodel_activitypartition_node_setter(instance):
    original = instance.node
    instance.node = original
    assert instance.node == original



@given(instance=UMLModel_ActivityPartition_strategy)
def test_umlmodel_activitypartition_isExternal_setter(instance):
    original = instance.isExternal
    instance.isExternal = original
    assert instance.isExternal == original



@given(instance=UMLModel_ActivityPartition_strategy)
def test_umlmodel_activitypartition_represents_setter(instance):
    original = instance.represents
    instance.represents = original
    assert instance.represents == original



@given(instance=UMLModel_ActivityPartition_strategy)
def test_umlmodel_activitypartition_subpartition_setter(instance):
    original = instance.subpartition
    instance.subpartition = original
    assert instance.subpartition == original



@given(instance=UMLModel_ActivityPartition_strategy)
def test_umlmodel_activitypartition_edge_setter(instance):
    original = instance.edge
    instance.edge = original
    assert instance.edge == original

@given(instance=UMLModel_ActivityNode_strategy)
@settings(max_examples=50)
def test_umlmodel_activitynode_instantiation(instance):
    assert isinstance(instance, UMLModel_ActivityNode)



@given(instance=UMLModel_ActivityNode_strategy)
def test_umlmodel_activitynode_inGroup_setter(instance):
    original = instance.inGroup
    instance.inGroup = original
    assert instance.inGroup == original



@given(instance=UMLModel_ActivityNode_strategy)
def test_umlmodel_activitynode_incoming_setter(instance):
    original = instance.incoming
    instance.incoming = original
    assert instance.incoming == original



@given(instance=UMLModel_ActivityNode_strategy)
def test_umlmodel_activitynode_inPartition_setter(instance):
    original = instance.inPartition
    instance.inPartition = original
    assert instance.inPartition == original



@given(instance=UMLModel_ActivityNode_strategy)
def test_umlmodel_activitynode_activity_setter(instance):
    original = instance.activity
    instance.activity = original
    assert instance.activity == original



@given(instance=UMLModel_ActivityNode_strategy)
def test_umlmodel_activitynode_outgoing_setter(instance):
    original = instance.outgoing
    instance.outgoing = original
    assert instance.outgoing == original



@given(instance=UMLModel_ActivityNode_strategy)
def test_umlmodel_activitynode_redefinedNode_setter(instance):
    original = instance.redefinedNode
    instance.redefinedNode = original
    assert instance.redefinedNode == original



@given(instance=UMLModel_ActivityNode_strategy)
def test_umlmodel_activitynode_inStructuredNode_setter(instance):
    original = instance.inStructuredNode
    instance.inStructuredNode = original
    assert instance.inStructuredNode == original



@given(instance=UMLModel_ActivityNode_strategy)
def test_umlmodel_activitynode_inInterruptibleRegion_setter(instance):
    original = instance.inInterruptibleRegion
    instance.inInterruptibleRegion = original
    assert instance.inInterruptibleRegion == original

@given(instance=UMLModel_Variable_strategy)
@settings(max_examples=50)
def test_umlmodel_variable_instantiation(instance):
    assert isinstance(instance, UMLModel_Variable)



@given(instance=UMLModel_Variable_strategy)
def test_umlmodel_variable_scope_setter(instance):
    original = instance.scope
    instance.scope = original
    assert instance.scope == original



@given(instance=UMLModel_Variable_strategy)
def test_umlmodel_variable_activityScope_setter(instance):
    original = instance.activityScope
    instance.activityScope = original
    assert instance.activityScope == original

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=UMLModel_OpaqueBehavior_strategy)
@settings(max_examples=50)
def test_umlmodel_opaquebehavior_instantiation(instance):
    assert isinstance(instance, UMLModel_OpaqueBehavior)



@given(instance=UMLModel_OpaqueBehavior_strategy)
def test_umlmodel_opaquebehavior_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original



@given(instance=UMLModel_OpaqueBehavior_strategy)
def test_umlmodel_opaquebehavior_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=UMLModel_StateMachine_strategy)
@settings(max_examples=50)
def test_umlmodel_statemachine_instantiation(instance):
    assert isinstance(instance, UMLModel_StateMachine)



@given(instance=UMLModel_StateMachine_strategy)
def test_umlmodel_statemachine_submachineState_setter(instance):
    original = instance.submachineState
    instance.submachineState = original
    assert instance.submachineState == original



@given(instance=UMLModel_StateMachine_strategy)
def test_umlmodel_statemachine_extendedStateMachine_setter(instance):
    original = instance.extendedStateMachine
    instance.extendedStateMachine = original
    assert instance.extendedStateMachine == original

@given(instance=UMLModel_Activity_strategy)
@settings(max_examples=50)
def test_umlmodel_activity_instantiation(instance):
    assert isinstance(instance, UMLModel_Activity)



@given(instance=UMLModel_Activity_strategy)
def test_umlmodel_activity_isSingleExecution_setter(instance):
    original = instance.isSingleExecution
    instance.isSingleExecution = original
    assert instance.isSingleExecution == original



@given(instance=UMLModel_Activity_strategy)
def test_umlmodel_activity_structuredNode_setter(instance):
    original = instance.structuredNode
    instance.structuredNode = original
    assert instance.structuredNode == original



@given(instance=UMLModel_Activity_strategy)
def test_umlmodel_activity_partition_setter(instance):
    original = instance.partition
    instance.partition = original
    assert instance.partition == original



@given(instance=UMLModel_Activity_strategy)
def test_umlmodel_activity_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original

@given(instance=InputPin_strategy)
@settings(max_examples=50)
def test_inputpin_instantiation(instance):
    assert isinstance(instance, InputPin)

@given(instance=UMLModel_ValuePin_strategy)
@settings(max_examples=50)
def test_umlmodel_valuepin_instantiation(instance):
    assert isinstance(instance, UMLModel_ValuePin)

@given(instance=UMLModel_ActionInputPin_strategy)
@settings(max_examples=50)
def test_umlmodel_actioninputpin_instantiation(instance):
    assert isinstance(instance, UMLModel_ActionInputPin)

@given(instance=ExecutionSpecification_strategy)
@settings(max_examples=50)
def test_executionspecification_instantiation(instance):
    assert isinstance(instance, ExecutionSpecification)

@given(instance=UMLModel_ActionExecutionSpecification_strategy)
@settings(max_examples=50)
def test_umlmodel_actionexecutionspecification_instantiation(instance):
    assert isinstance(instance, UMLModel_ActionExecutionSpecification)



@given(instance=UMLModel_ActionExecutionSpecification_strategy)
def test_umlmodel_actionexecutionspecification_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=UMLModel_ActivityGroup_strategy)
@settings(max_examples=50)
def test_umlmodel_activitygroup_instantiation(instance):
    assert isinstance(instance, UMLModel_ActivityGroup)



@given(instance=UMLModel_ActivityGroup_strategy)
def test_umlmodel_activitygroup_subgroup_setter(instance):
    original = instance.subgroup
    instance.subgroup = original
    assert instance.subgroup == original



@given(instance=UMLModel_ActivityGroup_strategy)
def test_umlmodel_activitygroup_inActivity_setter(instance):
    original = instance.inActivity
    instance.inActivity = original
    assert instance.inActivity == original



@given(instance=UMLModel_ActivityGroup_strategy)
def test_umlmodel_activitygroup_superGroup_setter(instance):
    original = instance.superGroup
    instance.superGroup = original
    assert instance.superGroup == original

@given(instance=UMLModel_ActivityEdge_strategy)
@settings(max_examples=50)
def test_umlmodel_activityedge_instantiation(instance):
    assert isinstance(instance, UMLModel_ActivityEdge)



@given(instance=UMLModel_ActivityEdge_strategy)
def test_umlmodel_activityedge_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original



@given(instance=UMLModel_ActivityEdge_strategy)
def test_umlmodel_activityedge_activity_setter(instance):
    original = instance.activity
    instance.activity = original
    assert instance.activity == original



@given(instance=UMLModel_ActivityEdge_strategy)
def test_umlmodel_activityedge_inStructuredNode_setter(instance):
    original = instance.inStructuredNode
    instance.inStructuredNode = original
    assert instance.inStructuredNode == original



@given(instance=UMLModel_ActivityEdge_strategy)
def test_umlmodel_activityedge_inGroup_setter(instance):
    original = instance.inGroup
    instance.inGroup = original
    assert instance.inGroup == original



@given(instance=UMLModel_ActivityEdge_strategy)
def test_umlmodel_activityedge_interrupts_setter(instance):
    original = instance.interrupts
    instance.interrupts = original
    assert instance.interrupts == original



@given(instance=UMLModel_ActivityEdge_strategy)
def test_umlmodel_activityedge_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original



@given(instance=UMLModel_ActivityEdge_strategy)
def test_umlmodel_activityedge_inPartition_setter(instance):
    original = instance.inPartition
    instance.inPartition = original
    assert instance.inPartition == original



@given(instance=UMLModel_ActivityEdge_strategy)
def test_umlmodel_activityedge_redefinedEdge_setter(instance):
    original = instance.redefinedEdge
    instance.redefinedEdge = original
    assert instance.redefinedEdge == original

@given(instance=AcceptEventAction_strategy)
@settings(max_examples=50)
def test_accepteventaction_instantiation(instance):
    assert isinstance(instance, AcceptEventAction)

@given(instance=UMLModel_AcceptCallAction_strategy)
@settings(max_examples=50)
def test_umlmodel_acceptcallaction_instantiation(instance):
    assert isinstance(instance, UMLModel_AcceptCallAction)

@given(instance=UMLModel_OpaqueExpression_strategy)
@settings(max_examples=50)
def test_umlmodel_opaqueexpression_instantiation(instance):
    assert isinstance(instance, UMLModel_OpaqueExpression)



@given(instance=UMLModel_OpaqueExpression_strategy)
def test_umlmodel_opaqueexpression_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original



@given(instance=UMLModel_OpaqueExpression_strategy)
def test_umlmodel_opaqueexpression_result_setter(instance):
    original = instance.result
    instance.result = original
    assert instance.result == original



@given(instance=UMLModel_OpaqueExpression_strategy)
def test_umlmodel_opaqueexpression_behavior_setter(instance):
    original = instance.behavior
    instance.behavior = original
    assert instance.behavior == original



@given(instance=UMLModel_OpaqueExpression_strategy)
def test_umlmodel_opaqueexpression_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=Dependency_strategy)
@settings(max_examples=50)
def test_dependency_instantiation(instance):
    assert isinstance(instance, Dependency)

@given(instance=UMLModel_Usage_strategy)
@settings(max_examples=50)
def test_umlmodel_usage_instantiation(instance):
    assert isinstance(instance, UMLModel_Usage)

@given(instance=UMLModel_Deployment_strategy)
@settings(max_examples=50)
def test_umlmodel_deployment_instantiation(instance):
    assert isinstance(instance, UMLModel_Deployment)



@given(instance=UMLModel_Deployment_strategy)
def test_umlmodel_deployment_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=UMLModel_Deployment_strategy)
def test_umlmodel_deployment_deployedArtifact_setter(instance):
    original = instance.deployedArtifact
    instance.deployedArtifact = original
    assert instance.deployedArtifact == original

@given(instance=UMLModel_Abstraction_strategy)
@settings(max_examples=50)
def test_umlmodel_abstraction_instantiation(instance):
    assert isinstance(instance, UMLModel_Abstraction)

@given(instance=ExecutableNode_strategy)
@settings(max_examples=50)
def test_executablenode_instantiation(instance):
    assert isinstance(instance, ExecutableNode)

@given(instance=UMLModel_Action_strategy)
@settings(max_examples=50)
def test_umlmodel_action_instantiation(instance):
    assert isinstance(instance, UMLModel_Action)



@given(instance=UMLModel_Action_strategy)
def test_umlmodel_action_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original



@given(instance=UMLModel_Action_strategy)
def test_umlmodel_action_context_setter(instance):
    original = instance.context
    instance.context = original
    assert instance.context == original



@given(instance=UMLModel_Action_strategy)
def test_umlmodel_action_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original

@given(instance=UMLModel_Trigger_strategy)
@settings(max_examples=50)
def test_umlmodel_trigger_instantiation(instance):
    assert isinstance(instance, UMLModel_Trigger)



@given(instance=UMLModel_Trigger_strategy)
def test_umlmodel_trigger_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original



@given(instance=UMLModel_Trigger_strategy)
def test_umlmodel_trigger_port_setter(instance):
    original = instance.port
    instance.port = original
    assert instance.port == original

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=UMLModel_ReduceAction_strategy)
@settings(max_examples=50)
def test_umlmodel_reduceaction_instantiation(instance):
    assert isinstance(instance, UMLModel_ReduceAction)



@given(instance=UMLModel_ReduceAction_strategy)
def test_umlmodel_reduceaction_reducer_setter(instance):
    original = instance.reducer
    instance.reducer = original
    assert instance.reducer == original



@given(instance=UMLModel_ReduceAction_strategy)
def test_umlmodel_reduceaction_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original

@given(instance=UMLModel_RaiseExceptionAction_strategy)
@settings(max_examples=50)
def test_umlmodel_raiseexceptionaction_instantiation(instance):
    assert isinstance(instance, UMLModel_RaiseExceptionAction)

@given(instance=UMLModel_ReadSelfAction_strategy)
@settings(max_examples=50)
def test_umlmodel_readselfaction_instantiation(instance):
    assert isinstance(instance, UMLModel_ReadSelfAction)

@given(instance=UMLModel_DestroyObjectAction_strategy)
@settings(max_examples=50)
def test_umlmodel_destroyobjectaction_instantiation(instance):
    assert isinstance(instance, UMLModel_DestroyObjectAction)



@given(instance=UMLModel_DestroyObjectAction_strategy)
def test_umlmodel_destroyobjectaction_isDestroyLinks_setter(instance):
    original = instance.isDestroyLinks
    instance.isDestroyLinks = original
    assert instance.isDestroyLinks == original



@given(instance=UMLModel_DestroyObjectAction_strategy)
def test_umlmodel_destroyobjectaction_isDestroyOwnedObjects_setter(instance):
    original = instance.isDestroyOwnedObjects
    instance.isDestroyOwnedObjects = original
    assert instance.isDestroyOwnedObjects == original

@given(instance=UMLModel_StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_umlmodel_structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, UMLModel_StructuralFeatureAction)



@given(instance=UMLModel_StructuralFeatureAction_strategy)
def test_umlmodel_structuralfeatureaction_structuralFeature_setter(instance):
    original = instance.structuralFeature
    instance.structuralFeature = original
    assert instance.structuralFeature == original

@given(instance=UMLModel_TestIdentityAction_strategy)
@settings(max_examples=50)
def test_umlmodel_testidentityaction_instantiation(instance):
    assert isinstance(instance, UMLModel_TestIdentityAction)

@given(instance=UMLModel_ReadIsClassifiedObjectAction_strategy)
@settings(max_examples=50)
def test_umlmodel_readisclassifiedobjectaction_instantiation(instance):
    assert isinstance(instance, UMLModel_ReadIsClassifiedObjectAction)



@given(instance=UMLModel_ReadIsClassifiedObjectAction_strategy)
def test_umlmodel_readisclassifiedobjectaction_isDirect_setter(instance):
    original = instance.isDirect
    instance.isDirect = original
    assert instance.isDirect == original



@given(instance=UMLModel_ReadIsClassifiedObjectAction_strategy)
def test_umlmodel_readisclassifiedobjectaction_classifier_setter(instance):
    original = instance.classifier
    instance.classifier = original
    assert instance.classifier == original

@given(instance=UMLModel_ReadExtentAction_strategy)
@settings(max_examples=50)
def test_umlmodel_readextentaction_instantiation(instance):
    assert isinstance(instance, UMLModel_ReadExtentAction)



@given(instance=UMLModel_ReadExtentAction_strategy)
def test_umlmodel_readextentaction_classifier_setter(instance):
    original = instance.classifier
    instance.classifier = original
    assert instance.classifier == original

@given(instance=UMLModel_StartClassifierBehaviorAction_strategy)
@settings(max_examples=50)
def test_umlmodel_startclassifierbehavioraction_instantiation(instance):
    assert isinstance(instance, UMLModel_StartClassifierBehaviorAction)

@given(instance=UMLModel_OpaqueAction_strategy)
@settings(max_examples=50)
def test_umlmodel_opaqueaction_instantiation(instance):
    assert isinstance(instance, UMLModel_OpaqueAction)



@given(instance=UMLModel_OpaqueAction_strategy)
def test_umlmodel_opaqueaction_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original



@given(instance=UMLModel_OpaqueAction_strategy)
def test_umlmodel_opaqueaction_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=UMLModel_LinkAction_strategy)
@settings(max_examples=50)
def test_umlmodel_linkaction_instantiation(instance):
    assert isinstance(instance, UMLModel_LinkAction)

@given(instance=UMLModel_InvocationAction_strategy)
@settings(max_examples=50)
def test_umlmodel_invocationaction_instantiation(instance):
    assert isinstance(instance, UMLModel_InvocationAction)



@given(instance=UMLModel_InvocationAction_strategy)
def test_umlmodel_invocationaction_onPort_setter(instance):
    original = instance.onPort
    instance.onPort = original
    assert instance.onPort == original

@given(instance=UMLModel_ValueSpecificationAction_strategy)
@settings(max_examples=50)
def test_umlmodel_valuespecificationaction_instantiation(instance):
    assert isinstance(instance, UMLModel_ValueSpecificationAction)

@given(instance=UMLModel_UnmarshallAction_strategy)
@settings(max_examples=50)
def test_umlmodel_unmarshallaction_instantiation(instance):
    assert isinstance(instance, UMLModel_UnmarshallAction)



@given(instance=UMLModel_UnmarshallAction_strategy)
def test_umlmodel_unmarshallaction_unmarshallType_setter(instance):
    original = instance.unmarshallType
    instance.unmarshallType = original
    assert instance.unmarshallType == original

@given(instance=UMLModel_ReadLinkObjectEndAction_strategy)
@settings(max_examples=50)
def test_umlmodel_readlinkobjectendaction_instantiation(instance):
    assert isinstance(instance, UMLModel_ReadLinkObjectEndAction)



@given(instance=UMLModel_ReadLinkObjectEndAction_strategy)
def test_umlmodel_readlinkobjectendaction_end_setter(instance):
    original = instance.end
    instance.end = original
    assert instance.end == original

@given(instance=UMLModel_ReadLinkObjectEndQualifierAction_strategy)
@settings(max_examples=50)
def test_umlmodel_readlinkobjectendqualifieraction_instantiation(instance):
    assert isinstance(instance, UMLModel_ReadLinkObjectEndQualifierAction)



@given(instance=UMLModel_ReadLinkObjectEndQualifierAction_strategy)
def test_umlmodel_readlinkobjectendqualifieraction_qualifier_setter(instance):
    original = instance.qualifier
    instance.qualifier = original
    assert instance.qualifier == original

@given(instance=UMLModel_ReplyAction_strategy)
@settings(max_examples=50)
def test_umlmodel_replyaction_instantiation(instance):
    assert isinstance(instance, UMLModel_ReplyAction)



@given(instance=UMLModel_ReplyAction_strategy)
def test_umlmodel_replyaction_replyToCall_setter(instance):
    original = instance.replyToCall
    instance.replyToCall = original
    assert instance.replyToCall == original

@given(instance=UMLModel_VariableAction_strategy)
@settings(max_examples=50)
def test_umlmodel_variableaction_instantiation(instance):
    assert isinstance(instance, UMLModel_VariableAction)



@given(instance=UMLModel_VariableAction_strategy)
def test_umlmodel_variableaction_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original

@given(instance=UMLModel_ReclassifyObjectAction_strategy)
@settings(max_examples=50)
def test_umlmodel_reclassifyobjectaction_instantiation(instance):
    assert isinstance(instance, UMLModel_ReclassifyObjectAction)



@given(instance=UMLModel_ReclassifyObjectAction_strategy)
def test_umlmodel_reclassifyobjectaction_isReplaceAll_setter(instance):
    original = instance.isReplaceAll
    instance.isReplaceAll = original
    assert instance.isReplaceAll == original



@given(instance=UMLModel_ReclassifyObjectAction_strategy)
def test_umlmodel_reclassifyobjectaction_newClassifier_setter(instance):
    original = instance.newClassifier
    instance.newClassifier = original
    assert instance.newClassifier == original



@given(instance=UMLModel_ReclassifyObjectAction_strategy)
def test_umlmodel_reclassifyobjectaction_oldClassifier_setter(instance):
    original = instance.oldClassifier
    instance.oldClassifier = original
    assert instance.oldClassifier == original

@given(instance=UMLModel_AcceptEventAction_strategy)
@settings(max_examples=50)
def test_umlmodel_accepteventaction_instantiation(instance):
    assert isinstance(instance, UMLModel_AcceptEventAction)



@given(instance=UMLModel_AcceptEventAction_strategy)
def test_umlmodel_accepteventaction_isUnmarshall_setter(instance):
    original = instance.isUnmarshall
    instance.isUnmarshall = original
    assert instance.isUnmarshall == original

@given(instance=UMLModel_OutputPin_strategy)
@settings(max_examples=50)
def test_umlmodel_outputpin_instantiation(instance):
    assert isinstance(instance, UMLModel_OutputPin)

@given(instance=CombinedFragment_strategy)
@settings(max_examples=50)
def test_combinedfragment_instantiation(instance):
    assert isinstance(instance, CombinedFragment)

@given(instance=UMLModel_ConsiderIgnoreFragment_strategy)
@settings(max_examples=50)
def test_umlmodel_considerignorefragment_instantiation(instance):
    assert isinstance(instance, UMLModel_ConsiderIgnoreFragment)



@given(instance=UMLModel_ConsiderIgnoreFragment_strategy)
def test_umlmodel_considerignorefragment_message_setter(instance):
    original = instance.message
    instance.message = original
    assert instance.message == original

@given(instance=CentralBufferNode_strategy)
@settings(max_examples=50)
def test_centralbuffernode_instantiation(instance):
    assert isinstance(instance, CentralBufferNode)

@given(instance=UMLModel_DataStoreNode_strategy)
@settings(max_examples=50)
def test_umlmodel_datastorenode_instantiation(instance):
    assert isinstance(instance, UMLModel_DataStoreNode)

@given(instance=UMLModel_CentralBufferNode_strategy)
@settings(max_examples=50)
def test_umlmodel_centralbuffernode_instantiation(instance):
    assert isinstance(instance, UMLModel_CentralBufferNode)

@given(instance=WriteLinkAction_strategy)
@settings(max_examples=50)
def test_writelinkaction_instantiation(instance):
    assert isinstance(instance, WriteLinkAction)

@given(instance=UMLModel_DestroyLinkAction_strategy)
@settings(max_examples=50)
def test_umlmodel_destroylinkaction_instantiation(instance):
    assert isinstance(instance, UMLModel_DestroyLinkAction)

@given(instance=UMLModel_CreateLinkAction_strategy)
@settings(max_examples=50)
def test_umlmodel_createlinkaction_instantiation(instance):
    assert isinstance(instance, UMLModel_CreateLinkAction)

@given(instance=PackageableElement_strategy)
@settings(max_examples=50)
def test_packageableelement_instantiation(instance):
    assert isinstance(instance, PackageableElement)

@given(instance=UMLModel_Event_strategy)
@settings(max_examples=50)
def test_umlmodel_event_instantiation(instance):
    assert isinstance(instance, UMLModel_Event)

@given(instance=UMLModel_InformationFlow_strategy)
@settings(max_examples=50)
def test_umlmodel_informationflow_instantiation(instance):
    assert isinstance(instance, UMLModel_InformationFlow)



@given(instance=UMLModel_InformationFlow_strategy)
def test_umlmodel_informationflow_realizingConnector_setter(instance):
    original = instance.realizingConnector
    instance.realizingConnector = original
    assert instance.realizingConnector == original



@given(instance=UMLModel_InformationFlow_strategy)
def test_umlmodel_informationflow_conveyed_setter(instance):
    original = instance.conveyed
    instance.conveyed = original
    assert instance.conveyed == original



@given(instance=UMLModel_InformationFlow_strategy)
def test_umlmodel_informationflow_informationSource_setter(instance):
    original = instance.informationSource
    instance.informationSource = original
    assert instance.informationSource == original



@given(instance=UMLModel_InformationFlow_strategy)
def test_umlmodel_informationflow_realizingActivityEdge_setter(instance):
    original = instance.realizingActivityEdge
    instance.realizingActivityEdge = original
    assert instance.realizingActivityEdge == original



@given(instance=UMLModel_InformationFlow_strategy)
def test_umlmodel_informationflow_informationTarget_setter(instance):
    original = instance.informationTarget
    instance.informationTarget = original
    assert instance.informationTarget == original



@given(instance=UMLModel_InformationFlow_strategy)
def test_umlmodel_informationflow_realizingMessage_setter(instance):
    original = instance.realizingMessage
    instance.realizingMessage = original
    assert instance.realizingMessage == original



@given(instance=UMLModel_InformationFlow_strategy)
def test_umlmodel_informationflow_realization_setter(instance):
    original = instance.realization
    instance.realization = original
    assert instance.realization == original

@given(instance=UMLModel_Constraint_strategy)
@settings(max_examples=50)
def test_umlmodel_constraint_instantiation(instance):
    assert isinstance(instance, UMLModel_Constraint)



@given(instance=UMLModel_Constraint_strategy)
def test_umlmodel_constraint_context_setter(instance):
    original = instance.context
    instance.context = original
    assert instance.context == original



@given(instance=UMLModel_Constraint_strategy)
def test_umlmodel_constraint_constrainedElement_setter(instance):
    original = instance.constrainedElement
    instance.constrainedElement = original
    assert instance.constrainedElement == original

@given(instance=UMLModel_GeneralizationSet_strategy)
@settings(max_examples=50)
def test_umlmodel_generalizationset_instantiation(instance):
    assert isinstance(instance, UMLModel_GeneralizationSet)



@given(instance=UMLModel_GeneralizationSet_strategy)
def test_umlmodel_generalizationset_isCovering_setter(instance):
    original = instance.isCovering
    instance.isCovering = original
    assert instance.isCovering == original



@given(instance=UMLModel_GeneralizationSet_strategy)
def test_umlmodel_generalizationset_powerType_setter(instance):
    original = instance.powerType
    instance.powerType = original
    assert instance.powerType == original



@given(instance=UMLModel_GeneralizationSet_strategy)
def test_umlmodel_generalizationset_generalization_setter(instance):
    original = instance.generalization
    instance.generalization = original
    assert instance.generalization == original



@given(instance=UMLModel_GeneralizationSet_strategy)
def test_umlmodel_generalizationset_isDisjoint_setter(instance):
    original = instance.isDisjoint
    instance.isDisjoint = original
    assert instance.isDisjoint == original

@given(instance=UMLModel_Observation_strategy)
@settings(max_examples=50)
def test_umlmodel_observation_instantiation(instance):
    assert isinstance(instance, UMLModel_Observation)

@given(instance=UMLModel_ValueSpecification_strategy)
@settings(max_examples=50)
def test_umlmodel_valuespecification_instantiation(instance):
    assert isinstance(instance, UMLModel_ValueSpecification)

@given(instance=UMLModel_Type_strategy)
@settings(max_examples=50)
def test_umlmodel_type_instantiation(instance):
    assert isinstance(instance, UMLModel_Type)



@given(instance=UMLModel_Type_strategy)
def test_umlmodel_type_package_setter(instance):
    original = instance.package
    instance.package = original
    assert instance.package == original

@given(instance=UMLModel_CreateObjectAction_strategy)
@settings(max_examples=50)
def test_umlmodel_createobjectaction_instantiation(instance):
    assert isinstance(instance, UMLModel_CreateObjectAction)



@given(instance=UMLModel_CreateObjectAction_strategy)
def test_umlmodel_createobjectaction_classifier_setter(instance):
    original = instance.classifier
    instance.classifier = original
    assert instance.classifier == original

@given(instance=CreateLinkAction_strategy)
@settings(max_examples=50)
def test_createlinkaction_instantiation(instance):
    assert isinstance(instance, CreateLinkAction)

@given(instance=UMLModel_CreateLinkObjectAction_strategy)
@settings(max_examples=50)
def test_umlmodel_createlinkobjectaction_instantiation(instance):
    assert isinstance(instance, UMLModel_CreateLinkObjectAction)

@given(instance=StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_structuredactivitynode_instantiation(instance):
    assert isinstance(instance, StructuredActivityNode)

@given(instance=UMLModel_SequenceNode_strategy)
@settings(max_examples=50)
def test_umlmodel_sequencenode_instantiation(instance):
    assert isinstance(instance, UMLModel_SequenceNode)

@given(instance=UMLModel_LoopNode_strategy)
@settings(max_examples=50)
def test_umlmodel_loopnode_instantiation(instance):
    assert isinstance(instance, UMLModel_LoopNode)



@given(instance=UMLModel_LoopNode_strategy)
def test_umlmodel_loopnode_isTestedFirst_setter(instance):
    original = instance.isTestedFirst
    instance.isTestedFirst = original
    assert instance.isTestedFirst == original



@given(instance=UMLModel_LoopNode_strategy)
def test_umlmodel_loopnode_test_setter(instance):
    original = instance.test
    instance.test = original
    assert instance.test == original



@given(instance=UMLModel_LoopNode_strategy)
def test_umlmodel_loopnode_loopVariable_setter(instance):
    original = instance.loopVariable
    instance.loopVariable = original
    assert instance.loopVariable == original



@given(instance=UMLModel_LoopNode_strategy)
def test_umlmodel_loopnode_bodyPart_setter(instance):
    original = instance.bodyPart
    instance.bodyPart = original
    assert instance.bodyPart == original



@given(instance=UMLModel_LoopNode_strategy)
def test_umlmodel_loopnode_decider_setter(instance):
    original = instance.decider
    instance.decider = original
    assert instance.decider == original



@given(instance=UMLModel_LoopNode_strategy)
def test_umlmodel_loopnode_bodyOutput_setter(instance):
    original = instance.bodyOutput
    instance.bodyOutput = original
    assert instance.bodyOutput == original



@given(instance=UMLModel_LoopNode_strategy)
def test_umlmodel_loopnode_setupPart_setter(instance):
    original = instance.setupPart
    instance.setupPart = original
    assert instance.setupPart == original

@given(instance=UMLModel_ExpansionRegion_strategy)
@settings(max_examples=50)
def test_umlmodel_expansionregion_instantiation(instance):
    assert isinstance(instance, UMLModel_ExpansionRegion)



@given(instance=UMLModel_ExpansionRegion_strategy)
def test_umlmodel_expansionregion_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original



@given(instance=UMLModel_ExpansionRegion_strategy)
def test_umlmodel_expansionregion_outputElement_setter(instance):
    original = instance.outputElement
    instance.outputElement = original
    assert instance.outputElement == original



@given(instance=UMLModel_ExpansionRegion_strategy)
def test_umlmodel_expansionregion_inputElement_setter(instance):
    original = instance.inputElement
    instance.inputElement = original
    assert instance.inputElement == original

@given(instance=UMLModel_ConditionalNode_strategy)
@settings(max_examples=50)
def test_umlmodel_conditionalnode_instantiation(instance):
    assert isinstance(instance, UMLModel_ConditionalNode)



@given(instance=UMLModel_ConditionalNode_strategy)
def test_umlmodel_conditionalnode_isDeterminate_setter(instance):
    original = instance.isDeterminate
    instance.isDeterminate = original
    assert instance.isDeterminate == original



@given(instance=UMLModel_ConditionalNode_strategy)
def test_umlmodel_conditionalnode_isAssured_setter(instance):
    original = instance.isAssured
    instance.isAssured = original
    assert instance.isAssured == original

@given(instance=UMLModel_Gate_strategy)
@settings(max_examples=50)
def test_umlmodel_gate_instantiation(instance):
    assert isinstance(instance, UMLModel_Gate)

@given(instance=ActivityNode_strategy)
@settings(max_examples=50)
def test_activitynode_instantiation(instance):
    assert isinstance(instance, ActivityNode)

@given(instance=UMLModel_ObjectNode_strategy)
@settings(max_examples=50)
def test_umlmodel_objectnode_instantiation(instance):
    assert isinstance(instance, UMLModel_ObjectNode)



@given(instance=UMLModel_ObjectNode_strategy)
def test_umlmodel_objectnode_selection_setter(instance):
    original = instance.selection
    instance.selection = original
    assert instance.selection == original



@given(instance=UMLModel_ObjectNode_strategy)
def test_umlmodel_objectnode_inState_setter(instance):
    original = instance.inState
    instance.inState = original
    assert instance.inState == original



@given(instance=UMLModel_ObjectNode_strategy)
def test_umlmodel_objectnode_isControlType_setter(instance):
    original = instance.isControlType
    instance.isControlType = original
    assert instance.isControlType == original



@given(instance=UMLModel_ObjectNode_strategy)
def test_umlmodel_objectnode_ordering_setter(instance):
    original = instance.ordering
    instance.ordering = original
    assert instance.ordering == original

@given(instance=UMLModel_ExecutableNode_strategy)
@settings(max_examples=50)
def test_umlmodel_executablenode_instantiation(instance):
    assert isinstance(instance, UMLModel_ExecutableNode)

@given(instance=UMLModel_ControlNode_strategy)
@settings(max_examples=50)
def test_umlmodel_controlnode_instantiation(instance):
    assert isinstance(instance, UMLModel_ControlNode)

@given(instance=ActivityEdge_strategy)
@settings(max_examples=50)
def test_activityedge_instantiation(instance):
    assert isinstance(instance, ActivityEdge)

@given(instance=UMLModel_ObjectFlow_strategy)
@settings(max_examples=50)
def test_umlmodel_objectflow_instantiation(instance):
    assert isinstance(instance, UMLModel_ObjectFlow)



@given(instance=UMLModel_ObjectFlow_strategy)
def test_umlmodel_objectflow_isMulticast_setter(instance):
    original = instance.isMulticast
    instance.isMulticast = original
    assert instance.isMulticast == original



@given(instance=UMLModel_ObjectFlow_strategy)
def test_umlmodel_objectflow_isMultireceive_setter(instance):
    original = instance.isMultireceive
    instance.isMultireceive = original
    assert instance.isMultireceive == original



@given(instance=UMLModel_ObjectFlow_strategy)
def test_umlmodel_objectflow_transformation_setter(instance):
    original = instance.transformation
    instance.transformation = original
    assert instance.transformation == original



@given(instance=UMLModel_ObjectFlow_strategy)
def test_umlmodel_objectflow_selection_setter(instance):
    original = instance.selection
    instance.selection = original
    assert instance.selection == original

@given(instance=UMLModel_ControlFlow_strategy)
@settings(max_examples=50)
def test_umlmodel_controlflow_instantiation(instance):
    assert isinstance(instance, UMLModel_ControlFlow)

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=UMLModel_Pseudostate_strategy)
@settings(max_examples=50)
def test_umlmodel_pseudostate_instantiation(instance):
    assert isinstance(instance, UMLModel_Pseudostate)



@given(instance=UMLModel_Pseudostate_strategy)
def test_umlmodel_pseudostate_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=UMLModel_Pseudostate_strategy)
def test_umlmodel_pseudostate_stateMachine_setter(instance):
    original = instance.stateMachine
    instance.stateMachine = original
    assert instance.stateMachine == original



@given(instance=UMLModel_Pseudostate_strategy)
def test_umlmodel_pseudostate_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original

@given(instance=UMLModel_ConnectionPointReference_strategy)
@settings(max_examples=50)
def test_umlmodel_connectionpointreference_instantiation(instance):
    assert isinstance(instance, UMLModel_ConnectionPointReference)



@given(instance=UMLModel_ConnectionPointReference_strategy)
def test_umlmodel_connectionpointreference_entry_setter(instance):
    original = instance.entry
    instance.entry = original
    assert instance.entry == original



@given(instance=UMLModel_ConnectionPointReference_strategy)
def test_umlmodel_connectionpointreference_exit_setter(instance):
    original = instance.exit
    instance.exit = original
    assert instance.exit == original



@given(instance=UMLModel_ConnectionPointReference_strategy)
def test_umlmodel_connectionpointreference_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original

@given(instance=UMLModel_Comment_strategy)
@settings(max_examples=50)
def test_umlmodel_comment_instantiation(instance):
    assert isinstance(instance, UMLModel_Comment)



@given(instance=UMLModel_Comment_strategy)
def test_umlmodel_comment_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original



@given(instance=UMLModel_Comment_strategy)
def test_umlmodel_comment_annotatedElement_setter(instance):
    original = instance.annotatedElement
    instance.annotatedElement = original
    assert instance.annotatedElement == original

@given(instance=UMLModel_Dependency_strategy)
@settings(max_examples=50)
def test_umlmodel_dependency_instantiation(instance):
    assert isinstance(instance, UMLModel_Dependency)



@given(instance=UMLModel_Dependency_strategy)
def test_umlmodel_dependency_client_setter(instance):
    original = instance.client
    instance.client = original
    assert instance.client == original



@given(instance=UMLModel_Dependency_strategy)
def test_umlmodel_dependency_supplier_setter(instance):
    original = instance.supplier
    instance.supplier = original
    assert instance.supplier == original

@given(instance=StructuredClassifier_strategy)
@settings(max_examples=50)
def test_structuredclassifier_instantiation(instance):
    assert isinstance(instance, StructuredClassifier)

@given(instance=UMLModel_EncapsulatedClassifier_strategy)
@settings(max_examples=50)
def test_umlmodel_encapsulatedclassifier_instantiation(instance):
    assert isinstance(instance, UMLModel_EncapsulatedClassifier)



@given(instance=UMLModel_EncapsulatedClassifier_strategy)
def test_umlmodel_encapsulatedclassifier_ownedPort_setter(instance):
    original = instance.ownedPort
    instance.ownedPort = original
    assert instance.ownedPort == original

@given(instance=StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, StructuralFeatureAction)

@given(instance=UMLModel_WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_umlmodel_writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, UMLModel_WriteStructuralFeatureAction)

@given(instance=UMLModel_ReadStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_umlmodel_readstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, UMLModel_ReadStructuralFeatureAction)

@given(instance=UMLModel_ClearStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_umlmodel_clearstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, UMLModel_ClearStructuralFeatureAction)

@given(instance=UMLModel_ClearAssociationAction_strategy)
@settings(max_examples=50)
def test_umlmodel_clearassociationaction_instantiation(instance):
    assert isinstance(instance, UMLModel_ClearAssociationAction)



@given(instance=UMLModel_ClearAssociationAction_strategy)
def test_umlmodel_clearassociationaction_association_setter(instance):
    original = instance.association
    instance.association = original
    assert instance.association == original

@given(instance=VariableAction_strategy)
@settings(max_examples=50)
def test_variableaction_instantiation(instance):
    assert isinstance(instance, VariableAction)

@given(instance=UMLModel_ReadVariableAction_strategy)
@settings(max_examples=50)
def test_umlmodel_readvariableaction_instantiation(instance):
    assert isinstance(instance, UMLModel_ReadVariableAction)

@given(instance=UMLModel_WriteVariableAction_strategy)
@settings(max_examples=50)
def test_umlmodel_writevariableaction_instantiation(instance):
    assert isinstance(instance, UMLModel_WriteVariableAction)

@given(instance=UMLModel_ClearVariableAction_strategy)
@settings(max_examples=50)
def test_umlmodel_clearvariableaction_instantiation(instance):
    assert isinstance(instance, UMLModel_ClearVariableAction)

@given(instance=UMLModel_Clause_strategy)
@settings(max_examples=50)
def test_umlmodel_clause_instantiation(instance):
    assert isinstance(instance, UMLModel_Clause)



@given(instance=UMLModel_Clause_strategy)
def test_umlmodel_clause_decider_setter(instance):
    original = instance.decider
    instance.decider = original
    assert instance.decider == original



@given(instance=UMLModel_Clause_strategy)
def test_umlmodel_clause_bodyOutput_setter(instance):
    original = instance.bodyOutput
    instance.bodyOutput = original
    assert instance.bodyOutput == original



@given(instance=UMLModel_Clause_strategy)
def test_umlmodel_clause_successorClause_setter(instance):
    original = instance.successorClause
    instance.successorClause = original
    assert instance.successorClause == original



@given(instance=UMLModel_Clause_strategy)
def test_umlmodel_clause_test_setter(instance):
    original = instance.test
    instance.test = original
    assert instance.test == original



@given(instance=UMLModel_Clause_strategy)
def test_umlmodel_clause_predecessorClause_setter(instance):
    original = instance.predecessorClause
    instance.predecessorClause = original
    assert instance.predecessorClause == original



@given(instance=UMLModel_Clause_strategy)
def test_umlmodel_clause_body_setter(instance):
    original = instance.body
    instance.body = original
    assert instance.body == original

@given(instance=InteractionFragment_strategy)
@settings(max_examples=50)
def test_interactionfragment_instantiation(instance):
    assert isinstance(instance, InteractionFragment)

@given(instance=UMLModel_OccurrenceSpecification_strategy)
@settings(max_examples=50)
def test_umlmodel_occurrencespecification_instantiation(instance):
    assert isinstance(instance, UMLModel_OccurrenceSpecification)



@given(instance=UMLModel_OccurrenceSpecification_strategy)
def test_umlmodel_occurrencespecification_event_setter(instance):
    original = instance.event
    instance.event = original
    assert instance.event == original



@given(instance=UMLModel_OccurrenceSpecification_strategy)
def test_umlmodel_occurrencespecification_toAfter_setter(instance):
    original = instance.toAfter
    instance.toAfter = original
    assert instance.toAfter == original



@given(instance=UMLModel_OccurrenceSpecification_strategy)
def test_umlmodel_occurrencespecification_toBefore_setter(instance):
    original = instance.toBefore
    instance.toBefore = original
    assert instance.toBefore == original

@given(instance=UMLModel_InteractionUse_strategy)
@settings(max_examples=50)
def test_umlmodel_interactionuse_instantiation(instance):
    assert isinstance(instance, UMLModel_InteractionUse)



@given(instance=UMLModel_InteractionUse_strategy)
def test_umlmodel_interactionuse_refersTo_setter(instance):
    original = instance.refersTo
    instance.refersTo = original
    assert instance.refersTo == original

@given(instance=UMLModel_StateInvariant_strategy)
@settings(max_examples=50)
def test_umlmodel_stateinvariant_instantiation(instance):
    assert isinstance(instance, UMLModel_StateInvariant)

@given(instance=UMLModel_Interaction_strategy)
@settings(max_examples=50)
def test_umlmodel_interaction_instantiation(instance):
    assert isinstance(instance, UMLModel_Interaction)

@given(instance=UMLModel_Continuation_strategy)
@settings(max_examples=50)
def test_umlmodel_continuation_instantiation(instance):
    assert isinstance(instance, UMLModel_Continuation)



@given(instance=UMLModel_Continuation_strategy)
def test_umlmodel_continuation_setting_setter(instance):
    original = instance.setting
    instance.setting = original
    assert instance.setting == original

@given(instance=UMLModel_ExecutionSpecification_strategy)
@settings(max_examples=50)
def test_umlmodel_executionspecification_instantiation(instance):
    assert isinstance(instance, UMLModel_ExecutionSpecification)



@given(instance=UMLModel_ExecutionSpecification_strategy)
def test_umlmodel_executionspecification_finish_setter(instance):
    original = instance.finish
    instance.finish = original
    assert instance.finish == original



@given(instance=UMLModel_ExecutionSpecification_strategy)
def test_umlmodel_executionspecification_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

@given(instance=UMLModel_CombinedFragment_strategy)
@settings(max_examples=50)
def test_umlmodel_combinedfragment_instantiation(instance):
    assert isinstance(instance, UMLModel_CombinedFragment)



@given(instance=UMLModel_CombinedFragment_strategy)
def test_umlmodel_combinedfragment_interactionOperator_setter(instance):
    original = instance.interactionOperator
    instance.interactionOperator = original
    assert instance.interactionOperator == original

@given(instance=Realization_strategy)
@settings(max_examples=50)
def test_realization_instantiation(instance):
    assert isinstance(instance, Realization)

@given(instance=UMLModel_ComponentRealization_strategy)
@settings(max_examples=50)
def test_umlmodel_componentrealization_instantiation(instance):
    assert isinstance(instance, UMLModel_ComponentRealization)



@given(instance=UMLModel_ComponentRealization_strategy)
def test_umlmodel_componentrealization_realizingClassifier_setter(instance):
    original = instance.realizingClassifier
    instance.realizingClassifier = original
    assert instance.realizingClassifier == original



@given(instance=UMLModel_ComponentRealization_strategy)
def test_umlmodel_componentrealization_abstraction_setter(instance):
    original = instance.abstraction
    instance.abstraction = original
    assert instance.abstraction == original

@given(instance=UMLModel_PackageableElement_strategy)
@settings(max_examples=50)
def test_umlmodel_packageableelement_instantiation(instance):
    assert isinstance(instance, UMLModel_PackageableElement)

@given(instance=UMLModel_Generalization_strategy)
@settings(max_examples=50)
def test_umlmodel_generalization_instantiation(instance):
    assert isinstance(instance, UMLModel_Generalization)



@given(instance=UMLModel_Generalization_strategy)
def test_umlmodel_generalization_generalizationSet_setter(instance):
    original = instance.generalizationSet
    instance.generalizationSet = original
    assert instance.generalizationSet == original



@given(instance=UMLModel_Generalization_strategy)
def test_umlmodel_generalization_general_setter(instance):
    original = instance.general
    instance.general = original
    assert instance.general == original



@given(instance=UMLModel_Generalization_strategy)
def test_umlmodel_generalization_specific_setter(instance):
    original = instance.specific
    instance.specific = original
    assert instance.specific == original



@given(instance=UMLModel_Generalization_strategy)
def test_umlmodel_generalization_isSubstitutable_setter(instance):
    original = instance.isSubstitutable
    instance.isSubstitutable = original
    assert instance.isSubstitutable == original

@given(instance=TemplateableElement_strategy)
@settings(max_examples=50)
def test_templateableelement_instantiation(instance):
    assert isinstance(instance, TemplateableElement)

@given(instance=UMLModel_StringExpression_strategy)
@settings(max_examples=50)
def test_umlmodel_stringexpression_instantiation(instance):
    assert isinstance(instance, UMLModel_StringExpression)



@given(instance=UMLModel_StringExpression_strategy)
def test_umlmodel_stringexpression_owningExpression_setter(instance):
    original = instance.owningExpression
    instance.owningExpression = original
    assert instance.owningExpression == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=UMLModel_Reception_strategy)
@settings(max_examples=50)
def test_umlmodel_reception_instantiation(instance):
    assert isinstance(instance, UMLModel_Reception)



@given(instance=UMLModel_Reception_strategy)
def test_umlmodel_reception_signal_setter(instance):
    original = instance.signal
    instance.signal = original
    assert instance.signal == original

@given(instance=EncapsulatedClassifier_strategy)
@settings(max_examples=50)
def test_encapsulatedclassifier_instantiation(instance):
    assert isinstance(instance, EncapsulatedClassifier)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=UMLModel_ExecutionEvent_strategy)
@settings(max_examples=50)
def test_umlmodel_executionevent_instantiation(instance):
    assert isinstance(instance, UMLModel_ExecutionEvent)

@given(instance=UMLModel_DestructionEvent_strategy)
@settings(max_examples=50)
def test_umlmodel_destructionevent_instantiation(instance):
    assert isinstance(instance, UMLModel_DestructionEvent)

@given(instance=UMLModel_MessageEvent_strategy)
@settings(max_examples=50)
def test_umlmodel_messageevent_instantiation(instance):
    assert isinstance(instance, UMLModel_MessageEvent)

@given(instance=UMLModel_CreationEvent_strategy)
@settings(max_examples=50)
def test_umlmodel_creationevent_instantiation(instance):
    assert isinstance(instance, UMLModel_CreationEvent)

@given(instance=UMLModel_TimeEvent_strategy)
@settings(max_examples=50)
def test_umlmodel_timeevent_instantiation(instance):
    assert isinstance(instance, UMLModel_TimeEvent)



@given(instance=UMLModel_TimeEvent_strategy)
def test_umlmodel_timeevent_isRelative_setter(instance):
    original = instance.isRelative
    instance.isRelative = original
    assert instance.isRelative == original

@given(instance=UMLModel_ChangeEvent_strategy)
@settings(max_examples=50)
def test_umlmodel_changeevent_instantiation(instance):
    assert isinstance(instance, UMLModel_ChangeEvent)

@given(instance=TemplateParameter_strategy)
@settings(max_examples=50)
def test_templateparameter_instantiation(instance):
    assert isinstance(instance, TemplateParameter)

@given(instance=UMLModel_ConnectableElementTemplateParameter_strategy)
@settings(max_examples=50)
def test_umlmodel_connectableelementtemplateparameter_instantiation(instance):
    assert isinstance(instance, UMLModel_ConnectableElementTemplateParameter)

@given(instance=UMLModel_OperationTemplateParameter_strategy)
@settings(max_examples=50)
def test_umlmodel_operationtemplateparameter_instantiation(instance):
    assert isinstance(instance, UMLModel_OperationTemplateParameter)

@given(instance=UMLModel_ClassifierTemplateParameter_strategy)
@settings(max_examples=50)
def test_umlmodel_classifiertemplateparameter_instantiation(instance):
    assert isinstance(instance, UMLModel_ClassifierTemplateParameter)



@given(instance=UMLModel_ClassifierTemplateParameter_strategy)
def test_umlmodel_classifiertemplateparameter_constrainingClassifier_setter(instance):
    original = instance.constrainingClassifier
    instance.constrainingClassifier = original
    assert instance.constrainingClassifier == original



@given(instance=UMLModel_ClassifierTemplateParameter_strategy)
def test_umlmodel_classifiertemplateparameter_defaultClassifier_setter(instance):
    original = instance.defaultClassifier
    instance.defaultClassifier = original
    assert instance.defaultClassifier == original



@given(instance=UMLModel_ClassifierTemplateParameter_strategy)
def test_umlmodel_classifiertemplateparameter_allowSubstitutable_setter(instance):
    original = instance.allowSubstitutable
    instance.allowSubstitutable = original
    assert instance.allowSubstitutable == original

@given(instance=UMLModel_CollaborationUse_strategy)
@settings(max_examples=50)
def test_umlmodel_collaborationuse_instantiation(instance):
    assert isinstance(instance, UMLModel_CollaborationUse)



@given(instance=UMLModel_CollaborationUse_strategy)
def test_umlmodel_collaborationuse_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=UMLModel_Substitution_strategy)
@settings(max_examples=50)
def test_umlmodel_substitution_instantiation(instance):
    assert isinstance(instance, UMLModel_Substitution)



@given(instance=UMLModel_Substitution_strategy)
def test_umlmodel_substitution_substitutingClassifier_setter(instance):
    original = instance.substitutingClassifier
    instance.substitutingClassifier = original
    assert instance.substitutingClassifier == original



@given(instance=UMLModel_Substitution_strategy)
def test_umlmodel_substitution_contract_setter(instance):
    original = instance.contract
    instance.contract = original
    assert instance.contract == original

@given(instance=UMLModel_InterfaceRealization_strategy)
@settings(max_examples=50)
def test_umlmodel_interfacerealization_instantiation(instance):
    assert isinstance(instance, UMLModel_InterfaceRealization)



@given(instance=UMLModel_InterfaceRealization_strategy)
def test_umlmodel_interfacerealization_realizingClassifier_setter(instance):
    original = instance.realizingClassifier
    instance.realizingClassifier = original
    assert instance.realizingClassifier == original



@given(instance=UMLModel_InterfaceRealization_strategy)
def test_umlmodel_interfacerealization_contract_setter(instance):
    original = instance.contract
    instance.contract = original
    assert instance.contract == original

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=UMLModel_StructuralFeature_strategy)
@settings(max_examples=50)
def test_umlmodel_structuralfeature_instantiation(instance):
    assert isinstance(instance, UMLModel_StructuralFeature)



@given(instance=UMLModel_StructuralFeature_strategy)
def test_umlmodel_structuralfeature_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original

@given(instance=UMLModel_Connector_strategy)
@settings(max_examples=50)
def test_umlmodel_connector_instantiation(instance):
    assert isinstance(instance, UMLModel_Connector)



@given(instance=UMLModel_Connector_strategy)
def test_umlmodel_connector_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=UMLModel_Connector_strategy)
def test_umlmodel_connector_redefinedConnector_setter(instance):
    original = instance.redefinedConnector
    instance.redefinedConnector = original
    assert instance.redefinedConnector == original



@given(instance=UMLModel_Connector_strategy)
def test_umlmodel_connector_contract_setter(instance):
    original = instance.contract
    instance.contract = original
    assert instance.contract == original



@given(instance=UMLModel_Connector_strategy)
def test_umlmodel_connector_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Namespace_strategy)
@settings(max_examples=50)
def test_namespace_instantiation(instance):
    assert isinstance(instance, Namespace)

@given(instance=UMLModel_Package_strategy)
@settings(max_examples=50)
def test_umlmodel_package_instantiation(instance):
    assert isinstance(instance, UMLModel_Package)



@given(instance=UMLModel_Package_strategy)
def test_umlmodel_package_nestedPackage_setter(instance):
    original = instance.nestedPackage
    instance.nestedPackage = original
    assert instance.nestedPackage == original



@given(instance=UMLModel_Package_strategy)
def test_umlmodel_package_ownedType_setter(instance):
    original = instance.ownedType
    instance.ownedType = original
    assert instance.ownedType == original



@given(instance=UMLModel_Package_strategy)
def test_umlmodel_package_nestingPackage_setter(instance):
    original = instance.nestingPackage
    instance.nestingPackage = original
    assert instance.nestingPackage == original

@given(instance=UMLModel_InteractionOperand_strategy)
@settings(max_examples=50)
def test_umlmodel_interactionoperand_instantiation(instance):
    assert isinstance(instance, UMLModel_InteractionOperand)

@given(instance=UMLModel_Transition_strategy)
@settings(max_examples=50)
def test_umlmodel_transition_instantiation(instance):
    assert isinstance(instance, UMLModel_Transition)



@given(instance=UMLModel_Transition_strategy)
def test_umlmodel_transition_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original



@given(instance=UMLModel_Transition_strategy)
def test_umlmodel_transition_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=UMLModel_Transition_strategy)
def test_umlmodel_transition_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original



@given(instance=UMLModel_Transition_strategy)
def test_umlmodel_transition_guard_setter(instance):
    original = instance.guard
    instance.guard = original
    assert instance.guard == original



@given(instance=UMLModel_Transition_strategy)
def test_umlmodel_transition_redefinedTransition_setter(instance):
    original = instance.redefinedTransition
    instance.redefinedTransition = original
    assert instance.redefinedTransition == original



@given(instance=UMLModel_Transition_strategy)
def test_umlmodel_transition_container_setter(instance):
    original = instance.container
    instance.container = original
    assert instance.container == original

@given(instance=UMLModel_State_strategy)
@settings(max_examples=50)
def test_umlmodel_state_instantiation(instance):
    assert isinstance(instance, UMLModel_State)



@given(instance=UMLModel_State_strategy)
def test_umlmodel_state_isSimple_setter(instance):
    original = instance.isSimple
    instance.isSimple = original
    assert instance.isSimple == original



@given(instance=UMLModel_State_strategy)
def test_umlmodel_state_isSubmachineState_setter(instance):
    original = instance.isSubmachineState
    instance.isSubmachineState = original
    assert instance.isSubmachineState == original



@given(instance=UMLModel_State_strategy)
def test_umlmodel_state_submachine_setter(instance):
    original = instance.submachine
    instance.submachine = original
    assert instance.submachine == original



@given(instance=UMLModel_State_strategy)
def test_umlmodel_state_redefinedState_setter(instance):
    original = instance.redefinedState
    instance.redefinedState = original
    assert instance.redefinedState == original



@given(instance=UMLModel_State_strategy)
def test_umlmodel_state_isOrthogonal_setter(instance):
    original = instance.isOrthogonal
    instance.isOrthogonal = original
    assert instance.isOrthogonal == original



@given(instance=UMLModel_State_strategy)
def test_umlmodel_state_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original

@given(instance=UMLModel_StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_umlmodel_structuredactivitynode_instantiation(instance):
    assert isinstance(instance, UMLModel_StructuredActivityNode)



@given(instance=UMLModel_StructuredActivityNode_strategy)
def test_umlmodel_structuredactivitynode_mustIsolate_setter(instance):
    original = instance.mustIsolate
    instance.mustIsolate = original
    assert instance.mustIsolate == original

@given(instance=UMLModel_Region_strategy)
@settings(max_examples=50)
def test_umlmodel_region_instantiation(instance):
    assert isinstance(instance, UMLModel_Region)



@given(instance=UMLModel_Region_strategy)
def test_umlmodel_region_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original



@given(instance=UMLModel_Region_strategy)
def test_umlmodel_region_extendedRegion_setter(instance):
    original = instance.extendedRegion
    instance.extendedRegion = original
    assert instance.extendedRegion == original



@given(instance=UMLModel_Region_strategy)
def test_umlmodel_region_stateMachine_setter(instance):
    original = instance.stateMachine
    instance.stateMachine = original
    assert instance.stateMachine == original

@given(instance=UMLModel_Classifier_strategy)
@settings(max_examples=50)
def test_umlmodel_classifier_instantiation(instance):
    assert isinstance(instance, UMLModel_Classifier)



@given(instance=UMLModel_Classifier_strategy)
def test_umlmodel_classifier_general_setter(instance):
    original = instance.general
    instance.general = original
    assert instance.general == original



@given(instance=UMLModel_Classifier_strategy)
def test_umlmodel_classifier_inheritedMember_setter(instance):
    original = instance.inheritedMember
    instance.inheritedMember = original
    assert instance.inheritedMember == original



@given(instance=UMLModel_Classifier_strategy)
def test_umlmodel_classifier_representation_setter(instance):
    original = instance.representation
    instance.representation = original
    assert instance.representation == original



@given(instance=UMLModel_Classifier_strategy)
def test_umlmodel_classifier_redefinedClassifier_setter(instance):
    original = instance.redefinedClassifier
    instance.redefinedClassifier = original
    assert instance.redefinedClassifier == original



@given(instance=UMLModel_Classifier_strategy)
def test_umlmodel_classifier_feature_setter(instance):
    original = instance.feature
    instance.feature = original
    assert instance.feature == original



@given(instance=UMLModel_Classifier_strategy)
def test_umlmodel_classifier_useCase_setter(instance):
    original = instance.useCase
    instance.useCase = original
    assert instance.useCase == original



@given(instance=UMLModel_Classifier_strategy)
def test_umlmodel_classifier_powertypeExtent_setter(instance):
    original = instance.powertypeExtent
    instance.powertypeExtent = original
    assert instance.powertypeExtent == original



@given(instance=UMLModel_Classifier_strategy)
def test_umlmodel_classifier_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original



@given(instance=UMLModel_Classifier_strategy)
def test_umlmodel_classifier_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

@given(instance=UMLModel_BehavioralFeature_strategy)
@settings(max_examples=50)
def test_umlmodel_behavioralfeature_instantiation(instance):
    assert isinstance(instance, UMLModel_BehavioralFeature)



@given(instance=UMLModel_BehavioralFeature_strategy)
def test_umlmodel_behavioralfeature_raisedException_setter(instance):
    original = instance.raisedException
    instance.raisedException = original
    assert instance.raisedException == original



@given(instance=UMLModel_BehavioralFeature_strategy)
def test_umlmodel_behavioralfeature_concurrency_setter(instance):
    original = instance.concurrency
    instance.concurrency = original
    assert instance.concurrency == original



@given(instance=UMLModel_BehavioralFeature_strategy)
def test_umlmodel_behavioralfeature_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original



@given(instance=UMLModel_BehavioralFeature_strategy)
def test_umlmodel_behavioralfeature_method_setter(instance):
    original = instance.method
    instance.method = original
    assert instance.method == original

@given(instance=UMLModel_BehaviorExecutionSpecification_strategy)
@settings(max_examples=50)
def test_umlmodel_behaviorexecutionspecification_instantiation(instance):
    assert isinstance(instance, UMLModel_BehaviorExecutionSpecification)



@given(instance=UMLModel_BehaviorExecutionSpecification_strategy)
def test_umlmodel_behaviorexecutionspecification_behavior_setter(instance):
    original = instance.behavior
    instance.behavior = original
    assert instance.behavior == original

@given(instance=UMLModel_ParameterSet_strategy)
@settings(max_examples=50)
def test_umlmodel_parameterset_instantiation(instance):
    assert isinstance(instance, UMLModel_ParameterSet)



@given(instance=UMLModel_ParameterSet_strategy)
def test_umlmodel_parameterset_parameter_setter(instance):
    original = instance.parameter
    instance.parameter = original
    assert instance.parameter == original

@given(instance=UMLModel_Parameter_strategy)
@settings(max_examples=50)
def test_umlmodel_parameter_instantiation(instance):
    assert isinstance(instance, UMLModel_Parameter)



@given(instance=UMLModel_Parameter_strategy)
def test_umlmodel_parameter_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original



@given(instance=UMLModel_Parameter_strategy)
def test_umlmodel_parameter_effect_setter(instance):
    original = instance.effect
    instance.effect = original
    assert instance.effect == original



@given(instance=UMLModel_Parameter_strategy)
def test_umlmodel_parameter_isStream_setter(instance):
    original = instance.isStream
    instance.isStream = original
    assert instance.isStream == original



@given(instance=UMLModel_Parameter_strategy)
def test_umlmodel_parameter_parameterSet_setter(instance):
    original = instance.parameterSet
    instance.parameterSet = original
    assert instance.parameterSet == original



@given(instance=UMLModel_Parameter_strategy)
def test_umlmodel_parameter_isException_setter(instance):
    original = instance.isException
    instance.isException = original
    assert instance.isException == original



@given(instance=UMLModel_Parameter_strategy)
def test_umlmodel_parameter_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original



@given(instance=UMLModel_Parameter_strategy)
def test_umlmodel_parameter_operation_setter(instance):
    original = instance.operation
    instance.operation = original
    assert instance.operation == original

@given(instance=CallAction_strategy)
@settings(max_examples=50)
def test_callaction_instantiation(instance):
    assert isinstance(instance, CallAction)

@given(instance=UMLModel_CallOperationAction_strategy)
@settings(max_examples=50)
def test_umlmodel_calloperationaction_instantiation(instance):
    assert isinstance(instance, UMLModel_CallOperationAction)



@given(instance=UMLModel_CallOperationAction_strategy)
def test_umlmodel_calloperationaction_operation_setter(instance):
    original = instance.operation
    instance.operation = original
    assert instance.operation == original

@given(instance=UMLModel_CallBehaviorAction_strategy)
@settings(max_examples=50)
def test_umlmodel_callbehavioraction_instantiation(instance):
    assert isinstance(instance, UMLModel_CallBehaviorAction)



@given(instance=UMLModel_CallBehaviorAction_strategy)
def test_umlmodel_callbehavioraction_behavior_setter(instance):
    original = instance.behavior
    instance.behavior = original
    assert instance.behavior == original

@given(instance=UMLModel_Property_strategy)
@settings(max_examples=50)
def test_umlmodel_property_instantiation(instance):
    assert isinstance(instance, UMLModel_Property)



@given(instance=UMLModel_Property_strategy)
def test_umlmodel_property_association_setter(instance):
    original = instance.association
    instance.association = original
    assert instance.association == original



@given(instance=UMLModel_Property_strategy)
def test_umlmodel_property_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=UMLModel_Property_strategy)
def test_umlmodel_property_opposite_setter(instance):
    original = instance.opposite
    instance.opposite = original
    assert instance.opposite == original



@given(instance=UMLModel_Property_strategy)
def test_umlmodel_property_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original



@given(instance=UMLModel_Property_strategy)
def test_umlmodel_property_owningAssociation_setter(instance):
    original = instance.owningAssociation
    instance.owningAssociation = original
    assert instance.owningAssociation == original



@given(instance=UMLModel_Property_strategy)
def test_umlmodel_property_subsettedProperty_setter(instance):
    original = instance.subsettedProperty
    instance.subsettedProperty = original
    assert instance.subsettedProperty == original



@given(instance=UMLModel_Property_strategy)
def test_umlmodel_property_aggregation_setter(instance):
    original = instance.aggregation
    instance.aggregation = original
    assert instance.aggregation == original



@given(instance=UMLModel_Property_strategy)
def test_umlmodel_property_associationEnd_setter(instance):
    original = instance.associationEnd
    instance.associationEnd = original
    assert instance.associationEnd == original



@given(instance=UMLModel_Property_strategy)
def test_umlmodel_property_datatype_setter(instance):
    original = instance.datatype
    instance.datatype = original
    assert instance.datatype == original



@given(instance=UMLModel_Property_strategy)
def test_umlmodel_property_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original



@given(instance=UMLModel_Property_strategy)
def test_umlmodel_property_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original



@given(instance=UMLModel_Property_strategy)
def test_umlmodel_property_redefinedProperty_setter(instance):
    original = instance.redefinedProperty
    instance.redefinedProperty = original
    assert instance.redefinedProperty == original



@given(instance=UMLModel_Property_strategy)
def test_umlmodel_property_isDerivedUnion_setter(instance):
    original = instance.isDerivedUnion
    instance.isDerivedUnion = original
    assert instance.isDerivedUnion == original

@given(instance=InvocationAction_strategy)
@settings(max_examples=50)
def test_invocationaction_instantiation(instance):
    assert isinstance(instance, InvocationAction)

@given(instance=UMLModel_SendObjectAction_strategy)
@settings(max_examples=50)
def test_umlmodel_sendobjectaction_instantiation(instance):
    assert isinstance(instance, UMLModel_SendObjectAction)

@given(instance=UMLModel_CallAction_strategy)
@settings(max_examples=50)
def test_umlmodel_callaction_instantiation(instance):
    assert isinstance(instance, UMLModel_CallAction)



@given(instance=UMLModel_CallAction_strategy)
def test_umlmodel_callaction_isSynchronous_setter(instance):
    original = instance.isSynchronous
    instance.isSynchronous = original
    assert instance.isSynchronous == original

@given(instance=UMLModel_SendSignalAction_strategy)
@settings(max_examples=50)
def test_umlmodel_sendsignalaction_instantiation(instance):
    assert isinstance(instance, UMLModel_SendSignalAction)



@given(instance=UMLModel_SendSignalAction_strategy)
def test_umlmodel_sendsignalaction_signal_setter(instance):
    original = instance.signal
    instance.signal = original
    assert instance.signal == original

@given(instance=UMLModel_BroadcastSignalAction_strategy)
@settings(max_examples=50)
def test_umlmodel_broadcastsignalaction_instantiation(instance):
    assert isinstance(instance, UMLModel_BroadcastSignalAction)



@given(instance=UMLModel_BroadcastSignalAction_strategy)
def test_umlmodel_broadcastsignalaction_signal_setter(instance):
    original = instance.signal
    instance.signal = original
    assert instance.signal == original

@given(instance=UMLModel_Operation_strategy)
@settings(max_examples=50)
def test_umlmodel_operation_instantiation(instance):
    assert isinstance(instance, UMLModel_Operation)



@given(instance=UMLModel_Operation_strategy)
def test_umlmodel_operation_isQuery_setter(instance):
    original = instance.isQuery
    instance.isQuery = original
    assert instance.isQuery == original



@given(instance=UMLModel_Operation_strategy)
def test_umlmodel_operation_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original



@given(instance=UMLModel_Operation_strategy)
def test_umlmodel_operation_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original



@given(instance=UMLModel_Operation_strategy)
def test_umlmodel_operation_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original



@given(instance=UMLModel_Operation_strategy)
def test_umlmodel_operation_interface_setter(instance):
    original = instance.interface
    instance.interface = original
    assert instance.interface == original



@given(instance=UMLModel_Operation_strategy)
def test_umlmodel_operation_datatype_setter(instance):
    original = instance.datatype
    instance.datatype = original
    assert instance.datatype == original



@given(instance=UMLModel_Operation_strategy)
def test_umlmodel_operation_postcondition_setter(instance):
    original = instance.postcondition
    instance.postcondition = original
    assert instance.postcondition == original



@given(instance=UMLModel_Operation_strategy)
def test_umlmodel_operation_bodyCondition_setter(instance):
    original = instance.bodyCondition
    instance.bodyCondition = original
    assert instance.bodyCondition == original



@given(instance=UMLModel_Operation_strategy)
def test_umlmodel_operation_redefinedOperation_setter(instance):
    original = instance.redefinedOperation
    instance.redefinedOperation = original
    assert instance.redefinedOperation == original



@given(instance=UMLModel_Operation_strategy)
def test_umlmodel_operation_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=UMLModel_Operation_strategy)
def test_umlmodel_operation_precondition_setter(instance):
    original = instance.precondition
    instance.precondition = original
    assert instance.precondition == original



@given(instance=UMLModel_Operation_strategy)
def test_umlmodel_operation_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original



@given(instance=UMLModel_Operation_strategy)
def test_umlmodel_operation_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=UMLModel_Manifestation_strategy)
@settings(max_examples=50)
def test_umlmodel_manifestation_instantiation(instance):
    assert isinstance(instance, UMLModel_Manifestation)



@given(instance=UMLModel_Manifestation_strategy)
def test_umlmodel_manifestation_utilizedElement_setter(instance):
    original = instance.utilizedElement
    instance.utilizedElement = original
    assert instance.utilizedElement == original

@given(instance=DeployedArtifact_strategy)
@settings(max_examples=50)
def test_deployedartifact_instantiation(instance):
    assert isinstance(instance, DeployedArtifact)

@given(instance=UMLModel_InstanceSpecification_strategy)
@settings(max_examples=50)
def test_umlmodel_instancespecification_instantiation(instance):
    assert isinstance(instance, UMLModel_InstanceSpecification)



@given(instance=UMLModel_InstanceSpecification_strategy)
def test_umlmodel_instancespecification_classifier_setter(instance):
    original = instance.classifier
    instance.classifier = original
    assert instance.classifier == original

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=UMLModel_StructuredClassifier_strategy)
@settings(max_examples=50)
def test_umlmodel_structuredclassifier_instantiation(instance):
    assert isinstance(instance, UMLModel_StructuredClassifier)



@given(instance=UMLModel_StructuredClassifier_strategy)
def test_umlmodel_structuredclassifier_part_setter(instance):
    original = instance.part
    instance.part = original
    assert instance.part == original



@given(instance=UMLModel_StructuredClassifier_strategy)
def test_umlmodel_structuredclassifier_role_setter(instance):
    original = instance.role
    instance.role = original
    assert instance.role == original

@given(instance=UMLModel_Signal_strategy)
@settings(max_examples=50)
def test_umlmodel_signal_instantiation(instance):
    assert isinstance(instance, UMLModel_Signal)

@given(instance=UMLModel_DataType_strategy)
@settings(max_examples=50)
def test_umlmodel_datatype_instantiation(instance):
    assert isinstance(instance, UMLModel_DataType)

@given(instance=UMLModel_BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_umlmodel_behavioredclassifier_instantiation(instance):
    assert isinstance(instance, UMLModel_BehavioredClassifier)



@given(instance=UMLModel_BehavioredClassifier_strategy)
def test_umlmodel_behavioredclassifier_classifierBehavior_setter(instance):
    original = instance.classifierBehavior
    instance.classifierBehavior = original
    assert instance.classifierBehavior == original

@given(instance=UMLModel_Interface_strategy)
@settings(max_examples=50)
def test_umlmodel_interface_instantiation(instance):
    assert isinstance(instance, UMLModel_Interface)



@given(instance=UMLModel_Interface_strategy)
def test_umlmodel_interface_redefinedInterface_setter(instance):
    original = instance.redefinedInterface
    instance.redefinedInterface = original
    assert instance.redefinedInterface == original



@given(instance=UMLModel_Interface_strategy)
def test_umlmodel_interface_isActive_setter(instance):
    original = instance.isActive
    instance.isActive = original
    assert instance.isActive == original

@given(instance=UMLModel_InformationItem_strategy)
@settings(max_examples=50)
def test_umlmodel_informationitem_instantiation(instance):
    assert isinstance(instance, UMLModel_InformationItem)



@given(instance=UMLModel_InformationItem_strategy)
def test_umlmodel_informationitem_represented_setter(instance):
    original = instance.represented
    instance.represented = original
    assert instance.represented == original

@given(instance=UMLModel_Artifact_strategy)
@settings(max_examples=50)
def test_umlmodel_artifact_instantiation(instance):
    assert isinstance(instance, UMLModel_Artifact)



@given(instance=UMLModel_Artifact_strategy)
def test_umlmodel_artifact_fileName_setter(instance):
    original = instance.fileName
    instance.fileName = original
    assert instance.fileName == original

@given(instance=MessageEvent_strategy)
@settings(max_examples=50)
def test_messageevent_instantiation(instance):
    assert isinstance(instance, MessageEvent)

@given(instance=UMLModel_CallEvent_strategy)
@settings(max_examples=50)
def test_umlmodel_callevent_instantiation(instance):
    assert isinstance(instance, UMLModel_CallEvent)



@given(instance=UMLModel_CallEvent_strategy)
def test_umlmodel_callevent_operation_setter(instance):
    original = instance.operation
    instance.operation = original
    assert instance.operation == original

@given(instance=UMLModel_ReceiveOperationEvent_strategy)
@settings(max_examples=50)
def test_umlmodel_receiveoperationevent_instantiation(instance):
    assert isinstance(instance, UMLModel_ReceiveOperationEvent)



@given(instance=UMLModel_ReceiveOperationEvent_strategy)
def test_umlmodel_receiveoperationevent_operation_setter(instance):
    original = instance.operation
    instance.operation = original
    assert instance.operation == original

@given(instance=UMLModel_ReceiveSignalEvent_strategy)
@settings(max_examples=50)
def test_umlmodel_receivesignalevent_instantiation(instance):
    assert isinstance(instance, UMLModel_ReceiveSignalEvent)



@given(instance=UMLModel_ReceiveSignalEvent_strategy)
def test_umlmodel_receivesignalevent_signal_setter(instance):
    original = instance.signal
    instance.signal = original
    assert instance.signal == original

@given(instance=UMLModel_SignalEvent_strategy)
@settings(max_examples=50)
def test_umlmodel_signalevent_instantiation(instance):
    assert isinstance(instance, UMLModel_SignalEvent)



@given(instance=UMLModel_SignalEvent_strategy)
def test_umlmodel_signalevent_signal_setter(instance):
    original = instance.signal
    instance.signal = original
    assert instance.signal == original

@given(instance=UMLModel_SendSignalEvent_strategy)
@settings(max_examples=50)
def test_umlmodel_sendsignalevent_instantiation(instance):
    assert isinstance(instance, UMLModel_SendSignalEvent)



@given(instance=UMLModel_SendSignalEvent_strategy)
def test_umlmodel_sendsignalevent_signal_setter(instance):
    original = instance.signal
    instance.signal = original
    assert instance.signal == original

@given(instance=UMLModel_AnyReceiveEvent_strategy)
@settings(max_examples=50)
def test_umlmodel_anyreceiveevent_instantiation(instance):
    assert isinstance(instance, UMLModel_AnyReceiveEvent)

@given(instance=WriteVariableAction_strategy)
@settings(max_examples=50)
def test_writevariableaction_instantiation(instance):
    assert isinstance(instance, WriteVariableAction)

@given(instance=UMLModel_RemoveVariableValueAction_strategy)
@settings(max_examples=50)
def test_umlmodel_removevariablevalueaction_instantiation(instance):
    assert isinstance(instance, UMLModel_RemoveVariableValueAction)



@given(instance=UMLModel_RemoveVariableValueAction_strategy)
def test_umlmodel_removevariablevalueaction_isRemoveDuplicates_setter(instance):
    original = instance.isRemoveDuplicates
    instance.isRemoveDuplicates = original
    assert instance.isRemoveDuplicates == original

@given(instance=UMLModel_AddVariableValueAction_strategy)
@settings(max_examples=50)
def test_umlmodel_addvariablevalueaction_instantiation(instance):
    assert isinstance(instance, UMLModel_AddVariableValueAction)



@given(instance=UMLModel_AddVariableValueAction_strategy)
def test_umlmodel_addvariablevalueaction_isReplaceAll_setter(instance):
    original = instance.isReplaceAll
    instance.isReplaceAll = original
    assert instance.isReplaceAll == original

@given(instance=UMLModel_InputPin_strategy)
@settings(max_examples=50)
def test_umlmodel_inputpin_instantiation(instance):
    assert isinstance(instance, UMLModel_InputPin)

@given(instance=WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, WriteStructuralFeatureAction)

@given(instance=UMLModel_RemoveStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_umlmodel_removestructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, UMLModel_RemoveStructuralFeatureValueAction)



@given(instance=UMLModel_RemoveStructuralFeatureValueAction_strategy)
def test_umlmodel_removestructuralfeaturevalueaction_isRemoveDuplicates_setter(instance):
    original = instance.isRemoveDuplicates
    instance.isRemoveDuplicates = original
    assert instance.isRemoveDuplicates == original

@given(instance=UMLModel_AddStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_umlmodel_addstructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, UMLModel_AddStructuralFeatureValueAction)



@given(instance=UMLModel_AddStructuralFeatureValueAction_strategy)
def test_umlmodel_addstructuralfeaturevalueaction_isReplaceAll_setter(instance):
    original = instance.isReplaceAll
    instance.isReplaceAll = original
    assert instance.isReplaceAll == original

@given(instance=BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_behavioredclassifier_instantiation(instance):
    assert isinstance(instance, BehavioredClassifier)

@given(instance=UMLModel_Collaboration_strategy)
@settings(max_examples=50)
def test_umlmodel_collaboration_instantiation(instance):
    assert isinstance(instance, UMLModel_Collaboration)



@given(instance=UMLModel_Collaboration_strategy)
def test_umlmodel_collaboration_collaborationRole_setter(instance):
    original = instance.collaborationRole
    instance.collaborationRole = original
    assert instance.collaborationRole == original

@given(instance=UMLModel_Class_strategy)
@settings(max_examples=50)
def test_umlmodel_class_instantiation(instance):
    assert isinstance(instance, UMLModel_Class)



@given(instance=UMLModel_Class_strategy)
def test_umlmodel_class_isActive_setter(instance):
    original = instance.isActive
    instance.isActive = original
    assert instance.isActive == original



@given(instance=UMLModel_Class_strategy)
def test_umlmodel_class_extension_setter(instance):
    original = instance.extension
    instance.extension = original
    assert instance.extension == original



@given(instance=UMLModel_Class_strategy)
def test_umlmodel_class_superclass_setter(instance):
    original = instance.superclass
    instance.superclass = original
    assert instance.superclass == original

@given(instance=UMLModel_UseCase_strategy)
@settings(max_examples=50)
def test_umlmodel_usecase_instantiation(instance):
    assert isinstance(instance, UMLModel_UseCase)



@given(instance=UMLModel_UseCase_strategy)
def test_umlmodel_usecase_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original

@given(instance=UMLModel_Actor_strategy)
@settings(max_examples=50)
def test_umlmodel_actor_instantiation(instance):
    assert isinstance(instance, UMLModel_Actor)

@given(instance=Association_strategy)
@settings(max_examples=50)
def test_association_instantiation(instance):
    assert isinstance(instance, Association)

@given(instance=UMLModel_CommunicationPath_strategy)
@settings(max_examples=50)
def test_umlmodel_communicationpath_instantiation(instance):
    assert isinstance(instance, UMLModel_CommunicationPath)

@given(instance=UMLModel_Extension_strategy)
@settings(max_examples=50)
def test_umlmodel_extension_instantiation(instance):
    assert isinstance(instance, UMLModel_Extension)



@given(instance=UMLModel_Extension_strategy)
def test_umlmodel_extension_isRequired_setter(instance):
    original = instance.isRequired
    instance.isRequired = original
    assert instance.isRequired == original



@given(instance=UMLModel_Extension_strategy)
def test_umlmodel_extension_metaClass_setter(instance):
    original = instance.metaClass
    instance.metaClass = original
    assert instance.metaClass == original

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=UMLModel_Stereotype_strategy)
@settings(max_examples=50)
def test_umlmodel_stereotype_instantiation(instance):
    assert isinstance(instance, UMLModel_Stereotype)

@given(instance=UMLModel_Component_strategy)
@settings(max_examples=50)
def test_umlmodel_component_instantiation(instance):
    assert isinstance(instance, UMLModel_Component)



@given(instance=UMLModel_Component_strategy)
def test_umlmodel_component_required_setter(instance):
    original = instance.required
    instance.required = original
    assert instance.required == original



@given(instance=UMLModel_Component_strategy)
def test_umlmodel_component_indirectlyInstantiated_setter(instance):
    original = instance.indirectlyInstantiated
    instance.indirectlyInstantiated = original
    assert instance.indirectlyInstantiated == original



@given(instance=UMLModel_Component_strategy)
def test_umlmodel_component_provided_setter(instance):
    original = instance.provided
    instance.provided = original
    assert instance.provided == original

@given(instance=UMLModel_Node_strategy)
@settings(max_examples=50)
def test_umlmodel_node_instantiation(instance):
    assert isinstance(instance, UMLModel_Node)

@given(instance=UMLModel_Behavior_strategy)
@settings(max_examples=50)
def test_umlmodel_behavior_instantiation(instance):
    assert isinstance(instance, UMLModel_Behavior)



@given(instance=UMLModel_Behavior_strategy)
def test_umlmodel_behavior_postcondition_setter(instance):
    original = instance.postcondition
    instance.postcondition = original
    assert instance.postcondition == original



@given(instance=UMLModel_Behavior_strategy)
def test_umlmodel_behavior_isReentrant_setter(instance):
    original = instance.isReentrant
    instance.isReentrant = original
    assert instance.isReentrant == original



@given(instance=UMLModel_Behavior_strategy)
def test_umlmodel_behavior_precondition_setter(instance):
    original = instance.precondition
    instance.precondition = original
    assert instance.precondition == original



@given(instance=UMLModel_Behavior_strategy)
def test_umlmodel_behavior_redefinedBahavior_setter(instance):
    original = instance.redefinedBahavior
    instance.redefinedBahavior = original
    assert instance.redefinedBahavior == original



@given(instance=UMLModel_Behavior_strategy)
def test_umlmodel_behavior_specification_setter(instance):
    original = instance.specification
    instance.specification = original
    assert instance.specification == original



@given(instance=UMLModel_Behavior_strategy)
def test_umlmodel_behavior_context_setter(instance):
    original = instance.context
    instance.context = original
    assert instance.context == original

@given(instance=UMLModel_AssociationClass_strategy)
@settings(max_examples=50)
def test_umlmodel_associationclass_instantiation(instance):
    assert isinstance(instance, UMLModel_AssociationClass)

@given(instance=Relationship_strategy)
@settings(max_examples=50)
def test_relationship_instantiation(instance):
    assert isinstance(instance, Relationship)

@given(instance=UMLModel_DirectedRelationship_strategy)
@settings(max_examples=50)
def test_umlmodel_directedrelationship_instantiation(instance):
    assert isinstance(instance, UMLModel_DirectedRelationship)



@given(instance=UMLModel_DirectedRelationship_strategy)
def test_umlmodel_directedrelationship_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original



@given(instance=UMLModel_DirectedRelationship_strategy)
def test_umlmodel_directedrelationship_source_setter(instance):
    original = instance.source
    instance.source = original
    assert instance.source == original

@given(instance=UMLModel_Association_strategy)
@settings(max_examples=50)
def test_umlmodel_association_instantiation(instance):
    assert isinstance(instance, UMLModel_Association)



@given(instance=UMLModel_Association_strategy)
def test_umlmodel_association_navigableOwnedEnd_setter(instance):
    original = instance.navigableOwnedEnd
    instance.navigableOwnedEnd = original
    assert instance.navigableOwnedEnd == original



@given(instance=UMLModel_Association_strategy)
def test_umlmodel_association_memberEnd_setter(instance):
    original = instance.memberEnd
    instance.memberEnd = original
    assert instance.memberEnd == original



@given(instance=UMLModel_Association_strategy)
def test_umlmodel_association_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original



@given(instance=UMLModel_Association_strategy)
def test_umlmodel_association_endType_setter(instance):
    original = instance.endType
    instance.endType = original
    assert instance.endType == original
