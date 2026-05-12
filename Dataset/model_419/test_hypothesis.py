import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Trigger,
    UML2_TimeTrigger,
    FinalNode,
    UML2_ActivityFinalNode,
    MessageEnd,
    InteractionFragment,
    UML2_EventOccurrence,
    UML2_Continuation,
    DeployedArtifact,
    Relationship,
    UML2_DirectedRelationship,
    DataType,
    UML2_PrimitiveType,
    InstanceSpecification,
    UML2_EnumerationLiteral,
    Artifact,
    UML2_DeploymentSpecification,
    TemplateableElement,
    UML2_NamedElement,
    InputPin,
    UML2_ValuePin,
    Interval,
    UML2_TimeInterval,
    StructuredActivityNode,
    UML2_ExpansionRegion,
    Type,
    WriteVariableAction,
    UML2_RemoveVariableValueAction,
    TemplateSignature,
    DirectedRelationship,
    EncapsulatedClassifier,
    OpaqueExpression,
    UML2_Expression,
    Transition,
    UML2_ProtocolTransition,
    TemplateParameter,
    UML2_ConnectableElementTemplateParameter,
    UML2_OperationTemplateParameter,
    UML2_ClassifierTemplateParameter,
    Package,
    UML2_Profile,
    UML2_Model,
    Constraint,
    UML2_IntervalConstraint,
    AcceptEventAction,
    UML2_AcceptCallAction,
    StateMachine,
    UML2_ProtocolStateMachine,
    UML2_StateInvariant,
    UML2_Comment,
    UML2_CombinedFragment,
    UML2_InteractionOccurrence,
    UML2_PackageMerge,
    UML2_ExecutionOccurrence,
    InteractionOccurrence,
    UML2_PartDecomposition,
    UML2_AddVariableValueAction,
    UML2_ElementImport,
    UML2_FlowFinalNode,
    UML2_DurationInterval,
    UML2_ChangeTrigger,
    CallAction,
    UML2_CallBehaviorAction,
    UML2_CallOperationAction,
    UML2_MessageTrigger,
    UML2_Gate,
    UML2_Enumeration,
    UML2_ProtocolConformance,
    State,
    UML2_FinalState,
    UML2_StringExpression,
    Node,
    UML2_Device,
    UML2_ExecutionEnvironment,
    UML2_PackageImport,
    BehavioralFeature,
    UML2_Reception,
    ActivityEdge,
    UML2_ObjectFlow,
    UML2_ControlFlow,
    LinkEndData,
    UML2_LinkEndCreationData,
    UML2_InteractionConstraint,
    ExecutableNode,
    UML2_Action,
    UML2_LoopNode,
    UML2_ConditionalNode,
    PackageImport,
    UML2_ProfileApplication,
    UML2_TemplateBinding,
    VariableAction,
    UML2_WriteVariableAction,
    UML2_ReadVariableAction,
    UML2_ClearVariableAction,
    Feature,
    UML2_Connector,
    UML2_Generalization,
    PackageableElement,
    UML2_Constraint,
    UML2_Dependency,
    UML2_Type,
    UML2_InformationFlow,
    UML2_GeneralizationSet,
    UML2_PrimitiveFunction,
    WriteLinkAction,
    UML2_DestroyLinkAction,
    UML2_CreateLinkAction,
    MultiplicityElement,
    UML2_ConnectorEnd,
    ObjectNode,
    UML2_ActivityParameterNode,
    UML2_CentralBufferNode,
    UML2_ExpansionNode,
    UML2_Pin,
    StructuredClassifier,
    UML2_EncapsulatedClassifier,
    IntervalConstraint,
    UML2_TimeConstraint,
    UML2_DurationConstraint,
    EventOccurrence,
    UML2_Stop,
    LinkAction,
    UML2_WriteLinkAction,
    UML2_ReadLinkAction,
    Dependency,
    UML2_Deployment,
    UML2_Usage,
    UML2_Abstraction,
    UML2_Permission,
    Pin,
    ActivityGroup,
    UML2_InterruptibleActivityRegion,
    Vertex,
    UML2_Pseudostate,
    UML2_ConnectionPointReference,
    Namespace,
    UML2_Package,
    UML2_BehavioralFeature,
    UML2_InteractionOperand,
    CentralBufferNode,
    UML2_DataStoreNode,
    WriteStructuralFeatureAction,
    UML2_RemoveStructuralFeatureValueAction,
    UML2_DurationObservationAction,
    UML2_TimeObservationAction,
    UML2_AddStructuralFeatureValueAction,
    UML2_Element,
    Classifier,
    UML2_StructuredClassifier,
    UML2_Artifact,
    UML2_BehavioredClassifier,
    UML2_InformationItem,
    UML2_TemplateableClassifier,
    UML2_Interface,
    UML2_Actor,
    UML2_DataType,
    UML2_Signal,
    UML2_ParameterableClassifier,
    Behavior,
    UML2_StateMachine,
    UML2_Interaction,
    UML2_Activity,
    RedefinableElement,
    UML2_Feature,
    UML2_State,
    UML2_ActivityEdge,
    UML2_Region,
    UML2_RedefinableTemplateSignature,
    UML2_Classifier,
    UML2_ExtensionPoint,
    UML2_Transition,
    UML2_ActivityNode,
    NamedElement,
    UML2_Message,
    UML2_ActivityPartition,
    UML2_Lifeline,
    UML2_RedefinableElement,
    UML2_InteractionFragment,
    UML2_DeployedArtifact,
    UML2_Namespace,
    UML2_MessageEnd,
    UML2_TypedElement,
    UML2_DeploymentTarget,
    UML2_Include,
    UML2_Extend,
    UML2_ParameterSet,
    UML2_Vertex,
    UML2_CollaborationOccurrence,
    UML2_GeneralOrdering,
    UML2_Trigger,
    InvocationAction,
    UML2_CallAction,
    UML2_BroadcastSignalAction,
    UML2_SendSignalAction,
    UML2_SendObjectAction,
    Abstraction,
    UML2_Manifestation,
    UML2_Realization,
    MessageTrigger,
    UML2_SignalTrigger,
    UML2_CallTrigger,
    UML2_AnyTrigger,
    Realization,
    UML2_Substitution,
    UML2_Implementation,
    Action,
    UML2_VariableAction,
    UML2_LinkAction,
    UML2_InvocationAction,
    UML2_ClearAssociationAction,
    UML2_ReadLinkObjectEndAction,
    UML2_ReplyAction,
    UML2_StartOwnedBehaviorAction,
    UML2_CreateObjectAction,
    UML2_RaiseExceptionAction,
    UML2_ReadExtentAction,
    UML2_AcceptEventAction,
    UML2_ReadIsClassifiedObjectAction,
    UML2_StructuredActivityNode,
    UML2_DestroyObjectAction,
    UML2_ReclassifyObjectAction,
    UML2_ApplyFunctionAction,
    UML2_StructuralFeatureAction,
    LiteralSpecification,
    UML2_LiteralNull,
    UML2_LiteralInteger,
    UML2_LiteralUnlimitedNatural,
    UML2_LiteralBoolean,
    UML2_LiteralString,
    ActivityNode,
    UML2_ControlNode,
    UML2_ExecutableNode,
    ControlNode,
    UML2_DecisionNode,
    UML2_MergeNode,
    UML2_InitialNode,
    UML2_ForkNode,
    UML2_JoinNode,
    UML2_FinalNode,
    UML2_Association,
    DeploymentTarget,
    UML2_InstanceSpecification,
    ConnectableElement,
    StructuralFeature,
    Property,
    UML2_Port,
    UML2_ExtensionEnd,
    StructuralFeatureAction,
    UML2_ReadStructuralFeatureAction,
    UML2_ClearStructuralFeatureAction,
    UML2_WriteStructuralFeatureAction,
    UML2_ReadLinkObjectEndQualifierAction,
    UML2_InputPin,
    UML2_TestIdentityAction,
    Association,
    UML2_CommunicationPath,
    UML2_Extension,
    Class,
    UML2_Stereotype,
    UML2_Component,
    UML2_Behavior,
    UML2_Node,
    UML2_AssociationClass,
    UML2_OutputPin,
    UML2_ReadSelfAction,
    ParameterableElement,
    UML2_PackageableElement,
    UML2_ConnectableElement,
    TypedElement,
    UML2_StructuralFeature,
    UML2_Parameter,
    UML2_Variable,
    UML2_ObjectNode,
    UML2_Operation,
    UML2_ValueSpecification,
    BehavioredClassifier,
    UML2_Collaboration,
    UML2_Class,
    UML2_UseCase,
    ValueSpecification,
    UML2_InstanceValue,
    UML2_LiteralSpecification,
    UML2_Duration,
    UML2_OpaqueExpression,
    UML2_TimeExpression,
    UML2_Interval,
    CreateLinkAction,
    UML2_CreateLinkObjectAction,
    UML2_Property,
    Element,
    UML2_TemplateParameter,
    UML2_ActivityGroup,
    UML2_Clause,
    UML2_MultiplicityElement,
    UML2_ParameterableElement,
    UML2_Slot,
    UML2_LinkEndData,
    UML2_TemplateableElement,
    UML2_TemplateSignature,
    UML2_ExceptionHandler,
    UML2_TemplateParameterSubstitution,
    UML2_Relationship,
    UML2_QualifierValue,
    VisibilityKind,
    ParameterDirectionKind,
    AggregationKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_trigger_is_not_abstract():
    assert not inspect.isabstract(Trigger)


def test_trigger_constructor_exists():
    assert callable(Trigger.__init__)


def test_trigger_constructor_args():
    sig = inspect.signature(Trigger.__init__)
    params = list(sig.parameters.keys())



def test_uml2_timetrigger_is_not_abstract():
    assert not inspect.isabstract(UML2_TimeTrigger)


def test_uml2_timetrigger_constructor_exists():
    assert callable(UML2_TimeTrigger.__init__)


def test_uml2_timetrigger_constructor_args():
    sig = inspect.signature(UML2_TimeTrigger.__init__)
    params = list(sig.parameters.keys())



def test_finalnode_is_not_abstract():
    assert not inspect.isabstract(FinalNode)


def test_finalnode_constructor_exists():
    assert callable(FinalNode.__init__)


def test_finalnode_constructor_args():
    sig = inspect.signature(FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2_activityfinalnode_is_not_abstract():
    assert not inspect.isabstract(UML2_ActivityFinalNode)


def test_uml2_activityfinalnode_constructor_exists():
    assert callable(UML2_ActivityFinalNode.__init__)


def test_uml2_activityfinalnode_constructor_args():
    sig = inspect.signature(UML2_ActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_messageend_is_not_abstract():
    assert not inspect.isabstract(MessageEnd)


def test_messageend_constructor_exists():
    assert callable(MessageEnd.__init__)


def test_messageend_constructor_args():
    sig = inspect.signature(MessageEnd.__init__)
    params = list(sig.parameters.keys())



def test_interactionfragment_is_not_abstract():
    assert not inspect.isabstract(InteractionFragment)


def test_interactionfragment_constructor_exists():
    assert callable(InteractionFragment.__init__)


def test_interactionfragment_constructor_args():
    sig = inspect.signature(InteractionFragment.__init__)
    params = list(sig.parameters.keys())



def test_uml2_eventoccurrence_is_not_abstract():
    assert not inspect.isabstract(UML2_EventOccurrence)


def test_uml2_eventoccurrence_constructor_exists():
    assert callable(UML2_EventOccurrence.__init__)


def test_uml2_eventoccurrence_constructor_args():
    sig = inspect.signature(UML2_EventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_uml2_continuation_is_not_abstract():
    assert not inspect.isabstract(UML2_Continuation)


def test_uml2_continuation_constructor_exists():
    assert callable(UML2_Continuation.__init__)


def test_uml2_continuation_constructor_args():
    sig = inspect.signature(UML2_Continuation.__init__)
    params = list(sig.parameters.keys())



def test_deployedartifact_is_not_abstract():
    assert not inspect.isabstract(DeployedArtifact)


def test_deployedartifact_constructor_exists():
    assert callable(DeployedArtifact.__init__)


def test_deployedartifact_constructor_args():
    sig = inspect.signature(DeployedArtifact.__init__)
    params = list(sig.parameters.keys())



def test_relationship_is_not_abstract():
    assert not inspect.isabstract(Relationship)


def test_relationship_constructor_exists():
    assert callable(Relationship.__init__)


def test_relationship_constructor_args():
    sig = inspect.signature(Relationship.__init__)
    params = list(sig.parameters.keys())



def test_uml2_directedrelationship_is_not_abstract():
    assert not inspect.isabstract(UML2_DirectedRelationship)


def test_uml2_directedrelationship_constructor_exists():
    assert callable(UML2_DirectedRelationship.__init__)


def test_uml2_directedrelationship_constructor_args():
    sig = inspect.signature(UML2_DirectedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_uml2_primitivetype_is_not_abstract():
    assert not inspect.isabstract(UML2_PrimitiveType)


def test_uml2_primitivetype_constructor_exists():
    assert callable(UML2_PrimitiveType.__init__)


def test_uml2_primitivetype_constructor_args():
    sig = inspect.signature(UML2_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_instancespecification_is_not_abstract():
    assert not inspect.isabstract(InstanceSpecification)


def test_instancespecification_constructor_exists():
    assert callable(InstanceSpecification.__init__)


def test_instancespecification_constructor_args():
    sig = inspect.signature(InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml2_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(UML2_EnumerationLiteral)


def test_uml2_enumerationliteral_constructor_exists():
    assert callable(UML2_EnumerationLiteral.__init__)


def test_uml2_enumerationliteral_constructor_args():
    sig = inspect.signature(UML2_EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_artifact_is_not_abstract():
    assert not inspect.isabstract(Artifact)


def test_artifact_constructor_exists():
    assert callable(Artifact.__init__)


def test_artifact_constructor_args():
    sig = inspect.signature(Artifact.__init__)
    params = list(sig.parameters.keys())



def test_uml2_deploymentspecification_is_not_abstract():
    assert not inspect.isabstract(UML2_DeploymentSpecification)


def test_uml2_deploymentspecification_constructor_exists():
    assert callable(UML2_DeploymentSpecification.__init__)


def test_uml2_deploymentspecification_constructor_args():
    sig = inspect.signature(UML2_DeploymentSpecification.__init__)
    params = list(sig.parameters.keys())



def test_templateableelement_is_not_abstract():
    assert not inspect.isabstract(TemplateableElement)


def test_templateableelement_constructor_exists():
    assert callable(TemplateableElement.__init__)


def test_templateableelement_constructor_args():
    sig = inspect.signature(TemplateableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2_namedelement_is_not_abstract():
    assert not inspect.isabstract(UML2_NamedElement)


def test_uml2_namedelement_constructor_exists():
    assert callable(UML2_NamedElement.__init__)


def test_uml2_namedelement_constructor_args():
    sig = inspect.signature(UML2_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "visibility" in params, "Missing parameter 'visibility'"

def test_uml2_namedelement_has_name():
    assert hasattr(UML2_NamedElement, "name")
    descriptor = None
    for klass in UML2_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_uml2_namedelement_has_visibility():
    assert hasattr(UML2_NamedElement, "visibility")
    descriptor = None
    for klass in UML2_NamedElement.__mro__:
        if "visibility" in klass.__dict__:
            descriptor = klass.__dict__["visibility"]
            break
    assert isinstance(descriptor, property)



def test_inputpin_is_not_abstract():
    assert not inspect.isabstract(InputPin)


def test_inputpin_constructor_exists():
    assert callable(InputPin.__init__)


def test_inputpin_constructor_args():
    sig = inspect.signature(InputPin.__init__)
    params = list(sig.parameters.keys())



def test_uml2_valuepin_is_not_abstract():
    assert not inspect.isabstract(UML2_ValuePin)


def test_uml2_valuepin_constructor_exists():
    assert callable(UML2_ValuePin.__init__)


def test_uml2_valuepin_constructor_args():
    sig = inspect.signature(UML2_ValuePin.__init__)
    params = list(sig.parameters.keys())



def test_interval_is_not_abstract():
    assert not inspect.isabstract(Interval)


def test_interval_constructor_exists():
    assert callable(Interval.__init__)


def test_interval_constructor_args():
    sig = inspect.signature(Interval.__init__)
    params = list(sig.parameters.keys())



def test_uml2_timeinterval_is_not_abstract():
    assert not inspect.isabstract(UML2_TimeInterval)


def test_uml2_timeinterval_constructor_exists():
    assert callable(UML2_TimeInterval.__init__)


def test_uml2_timeinterval_constructor_args():
    sig = inspect.signature(UML2_TimeInterval.__init__)
    params = list(sig.parameters.keys())



def test_structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(StructuredActivityNode)


def test_structuredactivitynode_constructor_exists():
    assert callable(StructuredActivityNode.__init__)


def test_structuredactivitynode_constructor_args():
    sig = inspect.signature(StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2_expansionregion_is_not_abstract():
    assert not inspect.isabstract(UML2_ExpansionRegion)


def test_uml2_expansionregion_constructor_exists():
    assert callable(UML2_ExpansionRegion.__init__)


def test_uml2_expansionregion_constructor_args():
    sig = inspect.signature(UML2_ExpansionRegion.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_writevariableaction_is_not_abstract():
    assert not inspect.isabstract(WriteVariableAction)


def test_writevariableaction_constructor_exists():
    assert callable(WriteVariableAction.__init__)


def test_writevariableaction_constructor_args():
    sig = inspect.signature(WriteVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_removevariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(UML2_RemoveVariableValueAction)


def test_uml2_removevariablevalueaction_constructor_exists():
    assert callable(UML2_RemoveVariableValueAction.__init__)


def test_uml2_removevariablevalueaction_constructor_args():
    sig = inspect.signature(UML2_RemoveVariableValueAction.__init__)
    params = list(sig.parameters.keys())



def test_templatesignature_is_not_abstract():
    assert not inspect.isabstract(TemplateSignature)


def test_templatesignature_constructor_exists():
    assert callable(TemplateSignature.__init__)


def test_templatesignature_constructor_args():
    sig = inspect.signature(TemplateSignature.__init__)
    params = list(sig.parameters.keys())



def test_directedrelationship_is_not_abstract():
    assert not inspect.isabstract(DirectedRelationship)


def test_directedrelationship_constructor_exists():
    assert callable(DirectedRelationship.__init__)


def test_directedrelationship_constructor_args():
    sig = inspect.signature(DirectedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_encapsulatedclassifier_is_not_abstract():
    assert not inspect.isabstract(EncapsulatedClassifier)


def test_encapsulatedclassifier_constructor_exists():
    assert callable(EncapsulatedClassifier.__init__)


def test_encapsulatedclassifier_constructor_args():
    sig = inspect.signature(EncapsulatedClassifier.__init__)
    params = list(sig.parameters.keys())



def test_opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(OpaqueExpression)


def test_opaqueexpression_constructor_exists():
    assert callable(OpaqueExpression.__init__)


def test_opaqueexpression_constructor_args():
    sig = inspect.signature(OpaqueExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml2_expression_is_not_abstract():
    assert not inspect.isabstract(UML2_Expression)


def test_uml2_expression_constructor_exists():
    assert callable(UML2_Expression.__init__)


def test_uml2_expression_constructor_args():
    sig = inspect.signature(UML2_Expression.__init__)
    params = list(sig.parameters.keys())



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_uml2_protocoltransition_is_not_abstract():
    assert not inspect.isabstract(UML2_ProtocolTransition)


def test_uml2_protocoltransition_constructor_exists():
    assert callable(UML2_ProtocolTransition.__init__)


def test_uml2_protocoltransition_constructor_args():
    sig = inspect.signature(UML2_ProtocolTransition.__init__)
    params = list(sig.parameters.keys())



def test_templateparameter_is_not_abstract():
    assert not inspect.isabstract(TemplateParameter)


def test_templateparameter_constructor_exists():
    assert callable(TemplateParameter.__init__)


def test_templateparameter_constructor_args():
    sig = inspect.signature(TemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_uml2_connectableelementtemplateparameter_is_not_abstract():
    assert not inspect.isabstract(UML2_ConnectableElementTemplateParameter)


def test_uml2_connectableelementtemplateparameter_constructor_exists():
    assert callable(UML2_ConnectableElementTemplateParameter.__init__)


def test_uml2_connectableelementtemplateparameter_constructor_args():
    sig = inspect.signature(UML2_ConnectableElementTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_uml2_operationtemplateparameter_is_not_abstract():
    assert not inspect.isabstract(UML2_OperationTemplateParameter)


def test_uml2_operationtemplateparameter_constructor_exists():
    assert callable(UML2_OperationTemplateParameter.__init__)


def test_uml2_operationtemplateparameter_constructor_args():
    sig = inspect.signature(UML2_OperationTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_uml2_classifiertemplateparameter_is_not_abstract():
    assert not inspect.isabstract(UML2_ClassifierTemplateParameter)


def test_uml2_classifiertemplateparameter_constructor_exists():
    assert callable(UML2_ClassifierTemplateParameter.__init__)


def test_uml2_classifiertemplateparameter_constructor_args():
    sig = inspect.signature(UML2_ClassifierTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_package_constructor_exists():
    assert callable(Package.__init__)


def test_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_uml2_profile_is_not_abstract():
    assert not inspect.isabstract(UML2_Profile)


def test_uml2_profile_constructor_exists():
    assert callable(UML2_Profile.__init__)


def test_uml2_profile_constructor_args():
    sig = inspect.signature(UML2_Profile.__init__)
    params = list(sig.parameters.keys())



def test_uml2_model_is_not_abstract():
    assert not inspect.isabstract(UML2_Model)


def test_uml2_model_constructor_exists():
    assert callable(UML2_Model.__init__)


def test_uml2_model_constructor_args():
    sig = inspect.signature(UML2_Model.__init__)
    params = list(sig.parameters.keys())



def test_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_uml2_intervalconstraint_is_not_abstract():
    assert not inspect.isabstract(UML2_IntervalConstraint)


def test_uml2_intervalconstraint_constructor_exists():
    assert callable(UML2_IntervalConstraint.__init__)


def test_uml2_intervalconstraint_constructor_args():
    sig = inspect.signature(UML2_IntervalConstraint.__init__)
    params = list(sig.parameters.keys())



def test_accepteventaction_is_not_abstract():
    assert not inspect.isabstract(AcceptEventAction)


def test_accepteventaction_constructor_exists():
    assert callable(AcceptEventAction.__init__)


def test_accepteventaction_constructor_args():
    sig = inspect.signature(AcceptEventAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_acceptcallaction_is_not_abstract():
    assert not inspect.isabstract(UML2_AcceptCallAction)


def test_uml2_acceptcallaction_constructor_exists():
    assert callable(UML2_AcceptCallAction.__init__)


def test_uml2_acceptcallaction_constructor_args():
    sig = inspect.signature(UML2_AcceptCallAction.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachine)


def test_statemachine_constructor_exists():
    assert callable(StateMachine.__init__)


def test_statemachine_constructor_args():
    sig = inspect.signature(StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_uml2_protocolstatemachine_is_not_abstract():
    assert not inspect.isabstract(UML2_ProtocolStateMachine)


def test_uml2_protocolstatemachine_constructor_exists():
    assert callable(UML2_ProtocolStateMachine.__init__)


def test_uml2_protocolstatemachine_constructor_args():
    sig = inspect.signature(UML2_ProtocolStateMachine.__init__)
    params = list(sig.parameters.keys())



def test_uml2_stateinvariant_is_not_abstract():
    assert not inspect.isabstract(UML2_StateInvariant)


def test_uml2_stateinvariant_constructor_exists():
    assert callable(UML2_StateInvariant.__init__)


def test_uml2_stateinvariant_constructor_args():
    sig = inspect.signature(UML2_StateInvariant.__init__)
    params = list(sig.parameters.keys())



def test_uml2_comment_is_not_abstract():
    assert not inspect.isabstract(UML2_Comment)


def test_uml2_comment_constructor_exists():
    assert callable(UML2_Comment.__init__)


def test_uml2_comment_constructor_args():
    sig = inspect.signature(UML2_Comment.__init__)
    params = list(sig.parameters.keys())



def test_uml2_combinedfragment_is_not_abstract():
    assert not inspect.isabstract(UML2_CombinedFragment)


def test_uml2_combinedfragment_constructor_exists():
    assert callable(UML2_CombinedFragment.__init__)


def test_uml2_combinedfragment_constructor_args():
    sig = inspect.signature(UML2_CombinedFragment.__init__)
    params = list(sig.parameters.keys())



def test_uml2_interactionoccurrence_is_not_abstract():
    assert not inspect.isabstract(UML2_InteractionOccurrence)


def test_uml2_interactionoccurrence_constructor_exists():
    assert callable(UML2_InteractionOccurrence.__init__)


def test_uml2_interactionoccurrence_constructor_args():
    sig = inspect.signature(UML2_InteractionOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_uml2_packagemerge_is_not_abstract():
    assert not inspect.isabstract(UML2_PackageMerge)


def test_uml2_packagemerge_constructor_exists():
    assert callable(UML2_PackageMerge.__init__)


def test_uml2_packagemerge_constructor_args():
    sig = inspect.signature(UML2_PackageMerge.__init__)
    params = list(sig.parameters.keys())



def test_uml2_executionoccurrence_is_not_abstract():
    assert not inspect.isabstract(UML2_ExecutionOccurrence)


def test_uml2_executionoccurrence_constructor_exists():
    assert callable(UML2_ExecutionOccurrence.__init__)


def test_uml2_executionoccurrence_constructor_args():
    sig = inspect.signature(UML2_ExecutionOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_interactionoccurrence_is_not_abstract():
    assert not inspect.isabstract(InteractionOccurrence)


def test_interactionoccurrence_constructor_exists():
    assert callable(InteractionOccurrence.__init__)


def test_interactionoccurrence_constructor_args():
    sig = inspect.signature(InteractionOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_uml2_partdecomposition_is_not_abstract():
    assert not inspect.isabstract(UML2_PartDecomposition)


def test_uml2_partdecomposition_constructor_exists():
    assert callable(UML2_PartDecomposition.__init__)


def test_uml2_partdecomposition_constructor_args():
    sig = inspect.signature(UML2_PartDecomposition.__init__)
    params = list(sig.parameters.keys())



def test_uml2_addvariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(UML2_AddVariableValueAction)


def test_uml2_addvariablevalueaction_constructor_exists():
    assert callable(UML2_AddVariableValueAction.__init__)


def test_uml2_addvariablevalueaction_constructor_args():
    sig = inspect.signature(UML2_AddVariableValueAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_elementimport_is_not_abstract():
    assert not inspect.isabstract(UML2_ElementImport)


def test_uml2_elementimport_constructor_exists():
    assert callable(UML2_ElementImport.__init__)


def test_uml2_elementimport_constructor_args():
    sig = inspect.signature(UML2_ElementImport.__init__)
    params = list(sig.parameters.keys())



def test_uml2_flowfinalnode_is_not_abstract():
    assert not inspect.isabstract(UML2_FlowFinalNode)


def test_uml2_flowfinalnode_constructor_exists():
    assert callable(UML2_FlowFinalNode.__init__)


def test_uml2_flowfinalnode_constructor_args():
    sig = inspect.signature(UML2_FlowFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2_durationinterval_is_not_abstract():
    assert not inspect.isabstract(UML2_DurationInterval)


def test_uml2_durationinterval_constructor_exists():
    assert callable(UML2_DurationInterval.__init__)


def test_uml2_durationinterval_constructor_args():
    sig = inspect.signature(UML2_DurationInterval.__init__)
    params = list(sig.parameters.keys())



def test_uml2_changetrigger_is_not_abstract():
    assert not inspect.isabstract(UML2_ChangeTrigger)


def test_uml2_changetrigger_constructor_exists():
    assert callable(UML2_ChangeTrigger.__init__)


def test_uml2_changetrigger_constructor_args():
    sig = inspect.signature(UML2_ChangeTrigger.__init__)
    params = list(sig.parameters.keys())



def test_callaction_is_not_abstract():
    assert not inspect.isabstract(CallAction)


def test_callaction_constructor_exists():
    assert callable(CallAction.__init__)


def test_callaction_constructor_args():
    sig = inspect.signature(CallAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_callbehavioraction_is_not_abstract():
    assert not inspect.isabstract(UML2_CallBehaviorAction)


def test_uml2_callbehavioraction_constructor_exists():
    assert callable(UML2_CallBehaviorAction.__init__)


def test_uml2_callbehavioraction_constructor_args():
    sig = inspect.signature(UML2_CallBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_calloperationaction_is_not_abstract():
    assert not inspect.isabstract(UML2_CallOperationAction)


def test_uml2_calloperationaction_constructor_exists():
    assert callable(UML2_CallOperationAction.__init__)


def test_uml2_calloperationaction_constructor_args():
    sig = inspect.signature(UML2_CallOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_messagetrigger_is_not_abstract():
    assert not inspect.isabstract(UML2_MessageTrigger)


def test_uml2_messagetrigger_constructor_exists():
    assert callable(UML2_MessageTrigger.__init__)


def test_uml2_messagetrigger_constructor_args():
    sig = inspect.signature(UML2_MessageTrigger.__init__)
    params = list(sig.parameters.keys())



def test_uml2_gate_is_not_abstract():
    assert not inspect.isabstract(UML2_Gate)


def test_uml2_gate_constructor_exists():
    assert callable(UML2_Gate.__init__)


def test_uml2_gate_constructor_args():
    sig = inspect.signature(UML2_Gate.__init__)
    params = list(sig.parameters.keys())



def test_uml2_enumeration_is_not_abstract():
    assert not inspect.isabstract(UML2_Enumeration)


def test_uml2_enumeration_constructor_exists():
    assert callable(UML2_Enumeration.__init__)


def test_uml2_enumeration_constructor_args():
    sig = inspect.signature(UML2_Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_uml2_protocolconformance_is_not_abstract():
    assert not inspect.isabstract(UML2_ProtocolConformance)


def test_uml2_protocolconformance_constructor_exists():
    assert callable(UML2_ProtocolConformance.__init__)


def test_uml2_protocolconformance_constructor_args():
    sig = inspect.signature(UML2_ProtocolConformance.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_uml2_finalstate_is_not_abstract():
    assert not inspect.isabstract(UML2_FinalState)


def test_uml2_finalstate_constructor_exists():
    assert callable(UML2_FinalState.__init__)


def test_uml2_finalstate_constructor_args():
    sig = inspect.signature(UML2_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_uml2_stringexpression_is_not_abstract():
    assert not inspect.isabstract(UML2_StringExpression)


def test_uml2_stringexpression_constructor_exists():
    assert callable(UML2_StringExpression.__init__)


def test_uml2_stringexpression_constructor_args():
    sig = inspect.signature(UML2_StringExpression.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_uml2_device_is_not_abstract():
    assert not inspect.isabstract(UML2_Device)


def test_uml2_device_constructor_exists():
    assert callable(UML2_Device.__init__)


def test_uml2_device_constructor_args():
    sig = inspect.signature(UML2_Device.__init__)
    params = list(sig.parameters.keys())



def test_uml2_executionenvironment_is_not_abstract():
    assert not inspect.isabstract(UML2_ExecutionEnvironment)


def test_uml2_executionenvironment_constructor_exists():
    assert callable(UML2_ExecutionEnvironment.__init__)


def test_uml2_executionenvironment_constructor_args():
    sig = inspect.signature(UML2_ExecutionEnvironment.__init__)
    params = list(sig.parameters.keys())



def test_uml2_packageimport_is_not_abstract():
    assert not inspect.isabstract(UML2_PackageImport)


def test_uml2_packageimport_constructor_exists():
    assert callable(UML2_PackageImport.__init__)


def test_uml2_packageimport_constructor_args():
    sig = inspect.signature(UML2_PackageImport.__init__)
    params = list(sig.parameters.keys())



def test_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(BehavioralFeature)


def test_behavioralfeature_constructor_exists():
    assert callable(BehavioralFeature.__init__)


def test_behavioralfeature_constructor_args():
    sig = inspect.signature(BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_uml2_reception_is_not_abstract():
    assert not inspect.isabstract(UML2_Reception)


def test_uml2_reception_constructor_exists():
    assert callable(UML2_Reception.__init__)


def test_uml2_reception_constructor_args():
    sig = inspect.signature(UML2_Reception.__init__)
    params = list(sig.parameters.keys())



def test_activityedge_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge)


def test_activityedge_constructor_exists():
    assert callable(ActivityEdge.__init__)


def test_activityedge_constructor_args():
    sig = inspect.signature(ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_uml2_objectflow_is_not_abstract():
    assert not inspect.isabstract(UML2_ObjectFlow)


def test_uml2_objectflow_constructor_exists():
    assert callable(UML2_ObjectFlow.__init__)


def test_uml2_objectflow_constructor_args():
    sig = inspect.signature(UML2_ObjectFlow.__init__)
    params = list(sig.parameters.keys())



def test_uml2_controlflow_is_not_abstract():
    assert not inspect.isabstract(UML2_ControlFlow)


def test_uml2_controlflow_constructor_exists():
    assert callable(UML2_ControlFlow.__init__)


def test_uml2_controlflow_constructor_args():
    sig = inspect.signature(UML2_ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_linkenddata_is_not_abstract():
    assert not inspect.isabstract(LinkEndData)


def test_linkenddata_constructor_exists():
    assert callable(LinkEndData.__init__)


def test_linkenddata_constructor_args():
    sig = inspect.signature(LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_uml2_linkendcreationdata_is_not_abstract():
    assert not inspect.isabstract(UML2_LinkEndCreationData)


def test_uml2_linkendcreationdata_constructor_exists():
    assert callable(UML2_LinkEndCreationData.__init__)


def test_uml2_linkendcreationdata_constructor_args():
    sig = inspect.signature(UML2_LinkEndCreationData.__init__)
    params = list(sig.parameters.keys())



def test_uml2_interactionconstraint_is_not_abstract():
    assert not inspect.isabstract(UML2_InteractionConstraint)


def test_uml2_interactionconstraint_constructor_exists():
    assert callable(UML2_InteractionConstraint.__init__)


def test_uml2_interactionconstraint_constructor_args():
    sig = inspect.signature(UML2_InteractionConstraint.__init__)
    params = list(sig.parameters.keys())



def test_executablenode_is_not_abstract():
    assert not inspect.isabstract(ExecutableNode)


def test_executablenode_constructor_exists():
    assert callable(ExecutableNode.__init__)


def test_executablenode_constructor_args():
    sig = inspect.signature(ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2_action_is_not_abstract():
    assert not inspect.isabstract(UML2_Action)


def test_uml2_action_constructor_exists():
    assert callable(UML2_Action.__init__)


def test_uml2_action_constructor_args():
    sig = inspect.signature(UML2_Action.__init__)
    params = list(sig.parameters.keys())



def test_uml2_loopnode_is_not_abstract():
    assert not inspect.isabstract(UML2_LoopNode)


def test_uml2_loopnode_constructor_exists():
    assert callable(UML2_LoopNode.__init__)


def test_uml2_loopnode_constructor_args():
    sig = inspect.signature(UML2_LoopNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2_conditionalnode_is_not_abstract():
    assert not inspect.isabstract(UML2_ConditionalNode)


def test_uml2_conditionalnode_constructor_exists():
    assert callable(UML2_ConditionalNode.__init__)


def test_uml2_conditionalnode_constructor_args():
    sig = inspect.signature(UML2_ConditionalNode.__init__)
    params = list(sig.parameters.keys())



def test_packageimport_is_not_abstract():
    assert not inspect.isabstract(PackageImport)


def test_packageimport_constructor_exists():
    assert callable(PackageImport.__init__)


def test_packageimport_constructor_args():
    sig = inspect.signature(PackageImport.__init__)
    params = list(sig.parameters.keys())



def test_uml2_profileapplication_is_not_abstract():
    assert not inspect.isabstract(UML2_ProfileApplication)


def test_uml2_profileapplication_constructor_exists():
    assert callable(UML2_ProfileApplication.__init__)


def test_uml2_profileapplication_constructor_args():
    sig = inspect.signature(UML2_ProfileApplication.__init__)
    params = list(sig.parameters.keys())



def test_uml2_templatebinding_is_not_abstract():
    assert not inspect.isabstract(UML2_TemplateBinding)


def test_uml2_templatebinding_constructor_exists():
    assert callable(UML2_TemplateBinding.__init__)


def test_uml2_templatebinding_constructor_args():
    sig = inspect.signature(UML2_TemplateBinding.__init__)
    params = list(sig.parameters.keys())



def test_variableaction_is_not_abstract():
    assert not inspect.isabstract(VariableAction)


def test_variableaction_constructor_exists():
    assert callable(VariableAction.__init__)


def test_variableaction_constructor_args():
    sig = inspect.signature(VariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_writevariableaction_is_not_abstract():
    assert not inspect.isabstract(UML2_WriteVariableAction)


def test_uml2_writevariableaction_constructor_exists():
    assert callable(UML2_WriteVariableAction.__init__)


def test_uml2_writevariableaction_constructor_args():
    sig = inspect.signature(UML2_WriteVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_readvariableaction_is_not_abstract():
    assert not inspect.isabstract(UML2_ReadVariableAction)


def test_uml2_readvariableaction_constructor_exists():
    assert callable(UML2_ReadVariableAction.__init__)


def test_uml2_readvariableaction_constructor_args():
    sig = inspect.signature(UML2_ReadVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_clearvariableaction_is_not_abstract():
    assert not inspect.isabstract(UML2_ClearVariableAction)


def test_uml2_clearvariableaction_constructor_exists():
    assert callable(UML2_ClearVariableAction.__init__)


def test_uml2_clearvariableaction_constructor_args():
    sig = inspect.signature(UML2_ClearVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_uml2_connector_is_not_abstract():
    assert not inspect.isabstract(UML2_Connector)


def test_uml2_connector_constructor_exists():
    assert callable(UML2_Connector.__init__)


def test_uml2_connector_constructor_args():
    sig = inspect.signature(UML2_Connector.__init__)
    params = list(sig.parameters.keys())



def test_uml2_generalization_is_not_abstract():
    assert not inspect.isabstract(UML2_Generalization)


def test_uml2_generalization_constructor_exists():
    assert callable(UML2_Generalization.__init__)


def test_uml2_generalization_constructor_args():
    sig = inspect.signature(UML2_Generalization.__init__)
    params = list(sig.parameters.keys())



def test_packageableelement_is_not_abstract():
    assert not inspect.isabstract(PackageableElement)


def test_packageableelement_constructor_exists():
    assert callable(PackageableElement.__init__)


def test_packageableelement_constructor_args():
    sig = inspect.signature(PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2_constraint_is_not_abstract():
    assert not inspect.isabstract(UML2_Constraint)


def test_uml2_constraint_constructor_exists():
    assert callable(UML2_Constraint.__init__)


def test_uml2_constraint_constructor_args():
    sig = inspect.signature(UML2_Constraint.__init__)
    params = list(sig.parameters.keys())



def test_uml2_dependency_is_not_abstract():
    assert not inspect.isabstract(UML2_Dependency)


def test_uml2_dependency_constructor_exists():
    assert callable(UML2_Dependency.__init__)


def test_uml2_dependency_constructor_args():
    sig = inspect.signature(UML2_Dependency.__init__)
    params = list(sig.parameters.keys())



def test_uml2_type_is_not_abstract():
    assert not inspect.isabstract(UML2_Type)


def test_uml2_type_constructor_exists():
    assert callable(UML2_Type.__init__)


def test_uml2_type_constructor_args():
    sig = inspect.signature(UML2_Type.__init__)
    params = list(sig.parameters.keys())



def test_uml2_informationflow_is_not_abstract():
    assert not inspect.isabstract(UML2_InformationFlow)


def test_uml2_informationflow_constructor_exists():
    assert callable(UML2_InformationFlow.__init__)


def test_uml2_informationflow_constructor_args():
    sig = inspect.signature(UML2_InformationFlow.__init__)
    params = list(sig.parameters.keys())



def test_uml2_generalizationset_is_not_abstract():
    assert not inspect.isabstract(UML2_GeneralizationSet)


def test_uml2_generalizationset_constructor_exists():
    assert callable(UML2_GeneralizationSet.__init__)


def test_uml2_generalizationset_constructor_args():
    sig = inspect.signature(UML2_GeneralizationSet.__init__)
    params = list(sig.parameters.keys())



def test_uml2_primitivefunction_is_not_abstract():
    assert not inspect.isabstract(UML2_PrimitiveFunction)


def test_uml2_primitivefunction_constructor_exists():
    assert callable(UML2_PrimitiveFunction.__init__)


def test_uml2_primitivefunction_constructor_args():
    sig = inspect.signature(UML2_PrimitiveFunction.__init__)
    params = list(sig.parameters.keys())



def test_writelinkaction_is_not_abstract():
    assert not inspect.isabstract(WriteLinkAction)


def test_writelinkaction_constructor_exists():
    assert callable(WriteLinkAction.__init__)


def test_writelinkaction_constructor_args():
    sig = inspect.signature(WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_destroylinkaction_is_not_abstract():
    assert not inspect.isabstract(UML2_DestroyLinkAction)


def test_uml2_destroylinkaction_constructor_exists():
    assert callable(UML2_DestroyLinkAction.__init__)


def test_uml2_destroylinkaction_constructor_args():
    sig = inspect.signature(UML2_DestroyLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_createlinkaction_is_not_abstract():
    assert not inspect.isabstract(UML2_CreateLinkAction)


def test_uml2_createlinkaction_constructor_exists():
    assert callable(UML2_CreateLinkAction.__init__)


def test_uml2_createlinkaction_constructor_args():
    sig = inspect.signature(UML2_CreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(MultiplicityElement)


def test_multiplicityelement_constructor_exists():
    assert callable(MultiplicityElement.__init__)


def test_multiplicityelement_constructor_args():
    sig = inspect.signature(MultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2_connectorend_is_not_abstract():
    assert not inspect.isabstract(UML2_ConnectorEnd)


def test_uml2_connectorend_constructor_exists():
    assert callable(UML2_ConnectorEnd.__init__)


def test_uml2_connectorend_constructor_args():
    sig = inspect.signature(UML2_ConnectorEnd.__init__)
    params = list(sig.parameters.keys())



def test_objectnode_is_not_abstract():
    assert not inspect.isabstract(ObjectNode)


def test_objectnode_constructor_exists():
    assert callable(ObjectNode.__init__)


def test_objectnode_constructor_args():
    sig = inspect.signature(ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2_activityparameternode_is_not_abstract():
    assert not inspect.isabstract(UML2_ActivityParameterNode)


def test_uml2_activityparameternode_constructor_exists():
    assert callable(UML2_ActivityParameterNode.__init__)


def test_uml2_activityparameternode_constructor_args():
    sig = inspect.signature(UML2_ActivityParameterNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2_centralbuffernode_is_not_abstract():
    assert not inspect.isabstract(UML2_CentralBufferNode)


def test_uml2_centralbuffernode_constructor_exists():
    assert callable(UML2_CentralBufferNode.__init__)


def test_uml2_centralbuffernode_constructor_args():
    sig = inspect.signature(UML2_CentralBufferNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2_expansionnode_is_not_abstract():
    assert not inspect.isabstract(UML2_ExpansionNode)


def test_uml2_expansionnode_constructor_exists():
    assert callable(UML2_ExpansionNode.__init__)


def test_uml2_expansionnode_constructor_args():
    sig = inspect.signature(UML2_ExpansionNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2_pin_is_not_abstract():
    assert not inspect.isabstract(UML2_Pin)


def test_uml2_pin_constructor_exists():
    assert callable(UML2_Pin.__init__)


def test_uml2_pin_constructor_args():
    sig = inspect.signature(UML2_Pin.__init__)
    params = list(sig.parameters.keys())



def test_structuredclassifier_is_not_abstract():
    assert not inspect.isabstract(StructuredClassifier)


def test_structuredclassifier_constructor_exists():
    assert callable(StructuredClassifier.__init__)


def test_structuredclassifier_constructor_args():
    sig = inspect.signature(StructuredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2_encapsulatedclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2_EncapsulatedClassifier)


def test_uml2_encapsulatedclassifier_constructor_exists():
    assert callable(UML2_EncapsulatedClassifier.__init__)


def test_uml2_encapsulatedclassifier_constructor_args():
    sig = inspect.signature(UML2_EncapsulatedClassifier.__init__)
    params = list(sig.parameters.keys())



def test_intervalconstraint_is_not_abstract():
    assert not inspect.isabstract(IntervalConstraint)


def test_intervalconstraint_constructor_exists():
    assert callable(IntervalConstraint.__init__)


def test_intervalconstraint_constructor_args():
    sig = inspect.signature(IntervalConstraint.__init__)
    params = list(sig.parameters.keys())



def test_uml2_timeconstraint_is_not_abstract():
    assert not inspect.isabstract(UML2_TimeConstraint)


def test_uml2_timeconstraint_constructor_exists():
    assert callable(UML2_TimeConstraint.__init__)


def test_uml2_timeconstraint_constructor_args():
    sig = inspect.signature(UML2_TimeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_uml2_durationconstraint_is_not_abstract():
    assert not inspect.isabstract(UML2_DurationConstraint)


def test_uml2_durationconstraint_constructor_exists():
    assert callable(UML2_DurationConstraint.__init__)


def test_uml2_durationconstraint_constructor_args():
    sig = inspect.signature(UML2_DurationConstraint.__init__)
    params = list(sig.parameters.keys())



def test_eventoccurrence_is_not_abstract():
    assert not inspect.isabstract(EventOccurrence)


def test_eventoccurrence_constructor_exists():
    assert callable(EventOccurrence.__init__)


def test_eventoccurrence_constructor_args():
    sig = inspect.signature(EventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_uml2_stop_is_not_abstract():
    assert not inspect.isabstract(UML2_Stop)


def test_uml2_stop_constructor_exists():
    assert callable(UML2_Stop.__init__)


def test_uml2_stop_constructor_args():
    sig = inspect.signature(UML2_Stop.__init__)
    params = list(sig.parameters.keys())



def test_linkaction_is_not_abstract():
    assert not inspect.isabstract(LinkAction)


def test_linkaction_constructor_exists():
    assert callable(LinkAction.__init__)


def test_linkaction_constructor_args():
    sig = inspect.signature(LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_writelinkaction_is_not_abstract():
    assert not inspect.isabstract(UML2_WriteLinkAction)


def test_uml2_writelinkaction_constructor_exists():
    assert callable(UML2_WriteLinkAction.__init__)


def test_uml2_writelinkaction_constructor_args():
    sig = inspect.signature(UML2_WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_readlinkaction_is_not_abstract():
    assert not inspect.isabstract(UML2_ReadLinkAction)


def test_uml2_readlinkaction_constructor_exists():
    assert callable(UML2_ReadLinkAction.__init__)


def test_uml2_readlinkaction_constructor_args():
    sig = inspect.signature(UML2_ReadLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_dependency_is_not_abstract():
    assert not inspect.isabstract(Dependency)


def test_dependency_constructor_exists():
    assert callable(Dependency.__init__)


def test_dependency_constructor_args():
    sig = inspect.signature(Dependency.__init__)
    params = list(sig.parameters.keys())



def test_uml2_deployment_is_not_abstract():
    assert not inspect.isabstract(UML2_Deployment)


def test_uml2_deployment_constructor_exists():
    assert callable(UML2_Deployment.__init__)


def test_uml2_deployment_constructor_args():
    sig = inspect.signature(UML2_Deployment.__init__)
    params = list(sig.parameters.keys())



def test_uml2_usage_is_not_abstract():
    assert not inspect.isabstract(UML2_Usage)


def test_uml2_usage_constructor_exists():
    assert callable(UML2_Usage.__init__)


def test_uml2_usage_constructor_args():
    sig = inspect.signature(UML2_Usage.__init__)
    params = list(sig.parameters.keys())



def test_uml2_abstraction_is_not_abstract():
    assert not inspect.isabstract(UML2_Abstraction)


def test_uml2_abstraction_constructor_exists():
    assert callable(UML2_Abstraction.__init__)


def test_uml2_abstraction_constructor_args():
    sig = inspect.signature(UML2_Abstraction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_permission_is_not_abstract():
    assert not inspect.isabstract(UML2_Permission)


def test_uml2_permission_constructor_exists():
    assert callable(UML2_Permission.__init__)


def test_uml2_permission_constructor_args():
    sig = inspect.signature(UML2_Permission.__init__)
    params = list(sig.parameters.keys())



def test_pin_is_not_abstract():
    assert not inspect.isabstract(Pin)


def test_pin_constructor_exists():
    assert callable(Pin.__init__)


def test_pin_constructor_args():
    sig = inspect.signature(Pin.__init__)
    params = list(sig.parameters.keys())



def test_activitygroup_is_not_abstract():
    assert not inspect.isabstract(ActivityGroup)


def test_activitygroup_constructor_exists():
    assert callable(ActivityGroup.__init__)


def test_activitygroup_constructor_args():
    sig = inspect.signature(ActivityGroup.__init__)
    params = list(sig.parameters.keys())



def test_uml2_interruptibleactivityregion_is_not_abstract():
    assert not inspect.isabstract(UML2_InterruptibleActivityRegion)


def test_uml2_interruptibleactivityregion_constructor_exists():
    assert callable(UML2_InterruptibleActivityRegion.__init__)


def test_uml2_interruptibleactivityregion_constructor_args():
    sig = inspect.signature(UML2_InterruptibleActivityRegion.__init__)
    params = list(sig.parameters.keys())



def test_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_uml2_pseudostate_is_not_abstract():
    assert not inspect.isabstract(UML2_Pseudostate)


def test_uml2_pseudostate_constructor_exists():
    assert callable(UML2_Pseudostate.__init__)


def test_uml2_pseudostate_constructor_args():
    sig = inspect.signature(UML2_Pseudostate.__init__)
    params = list(sig.parameters.keys())



def test_uml2_connectionpointreference_is_not_abstract():
    assert not inspect.isabstract(UML2_ConnectionPointReference)


def test_uml2_connectionpointreference_constructor_exists():
    assert callable(UML2_ConnectionPointReference.__init__)


def test_uml2_connectionpointreference_constructor_args():
    sig = inspect.signature(UML2_ConnectionPointReference.__init__)
    params = list(sig.parameters.keys())



def test_namespace_is_not_abstract():
    assert not inspect.isabstract(Namespace)


def test_namespace_constructor_exists():
    assert callable(Namespace.__init__)


def test_namespace_constructor_args():
    sig = inspect.signature(Namespace.__init__)
    params = list(sig.parameters.keys())



def test_uml2_package_is_not_abstract():
    assert not inspect.isabstract(UML2_Package)


def test_uml2_package_constructor_exists():
    assert callable(UML2_Package.__init__)


def test_uml2_package_constructor_args():
    sig = inspect.signature(UML2_Package.__init__)
    params = list(sig.parameters.keys())



def test_uml2_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(UML2_BehavioralFeature)


def test_uml2_behavioralfeature_constructor_exists():
    assert callable(UML2_BehavioralFeature.__init__)


def test_uml2_behavioralfeature_constructor_args():
    sig = inspect.signature(UML2_BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_uml2_interactionoperand_is_not_abstract():
    assert not inspect.isabstract(UML2_InteractionOperand)


def test_uml2_interactionoperand_constructor_exists():
    assert callable(UML2_InteractionOperand.__init__)


def test_uml2_interactionoperand_constructor_args():
    sig = inspect.signature(UML2_InteractionOperand.__init__)
    params = list(sig.parameters.keys())



def test_centralbuffernode_is_not_abstract():
    assert not inspect.isabstract(CentralBufferNode)


def test_centralbuffernode_constructor_exists():
    assert callable(CentralBufferNode.__init__)


def test_centralbuffernode_constructor_args():
    sig = inspect.signature(CentralBufferNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2_datastorenode_is_not_abstract():
    assert not inspect.isabstract(UML2_DataStoreNode)


def test_uml2_datastorenode_constructor_exists():
    assert callable(UML2_DataStoreNode.__init__)


def test_uml2_datastorenode_constructor_args():
    sig = inspect.signature(UML2_DataStoreNode.__init__)
    params = list(sig.parameters.keys())



def test_writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(WriteStructuralFeatureAction)


def test_writestructuralfeatureaction_constructor_exists():
    assert callable(WriteStructuralFeatureAction.__init__)


def test_writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_removestructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(UML2_RemoveStructuralFeatureValueAction)


def test_uml2_removestructuralfeaturevalueaction_constructor_exists():
    assert callable(UML2_RemoveStructuralFeatureValueAction.__init__)


def test_uml2_removestructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(UML2_RemoveStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_durationobservationaction_is_not_abstract():
    assert not inspect.isabstract(UML2_DurationObservationAction)


def test_uml2_durationobservationaction_constructor_exists():
    assert callable(UML2_DurationObservationAction.__init__)


def test_uml2_durationobservationaction_constructor_args():
    sig = inspect.signature(UML2_DurationObservationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_timeobservationaction_is_not_abstract():
    assert not inspect.isabstract(UML2_TimeObservationAction)


def test_uml2_timeobservationaction_constructor_exists():
    assert callable(UML2_TimeObservationAction.__init__)


def test_uml2_timeobservationaction_constructor_args():
    sig = inspect.signature(UML2_TimeObservationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_addstructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(UML2_AddStructuralFeatureValueAction)


def test_uml2_addstructuralfeaturevalueaction_constructor_exists():
    assert callable(UML2_AddStructuralFeatureValueAction.__init__)


def test_uml2_addstructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(UML2_AddStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_element_is_not_abstract():
    assert not inspect.isabstract(UML2_Element)


def test_uml2_element_constructor_exists():
    assert callable(UML2_Element.__init__)


def test_uml2_element_constructor_args():
    sig = inspect.signature(UML2_Element.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2_structuredclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2_StructuredClassifier)


def test_uml2_structuredclassifier_constructor_exists():
    assert callable(UML2_StructuredClassifier.__init__)


def test_uml2_structuredclassifier_constructor_args():
    sig = inspect.signature(UML2_StructuredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2_artifact_is_not_abstract():
    assert not inspect.isabstract(UML2_Artifact)


def test_uml2_artifact_constructor_exists():
    assert callable(UML2_Artifact.__init__)


def test_uml2_artifact_constructor_args():
    sig = inspect.signature(UML2_Artifact.__init__)
    params = list(sig.parameters.keys())



def test_uml2_behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2_BehavioredClassifier)


def test_uml2_behavioredclassifier_constructor_exists():
    assert callable(UML2_BehavioredClassifier.__init__)


def test_uml2_behavioredclassifier_constructor_args():
    sig = inspect.signature(UML2_BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2_informationitem_is_not_abstract():
    assert not inspect.isabstract(UML2_InformationItem)


def test_uml2_informationitem_constructor_exists():
    assert callable(UML2_InformationItem.__init__)


def test_uml2_informationitem_constructor_args():
    sig = inspect.signature(UML2_InformationItem.__init__)
    params = list(sig.parameters.keys())



def test_uml2_templateableclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2_TemplateableClassifier)


def test_uml2_templateableclassifier_constructor_exists():
    assert callable(UML2_TemplateableClassifier.__init__)


def test_uml2_templateableclassifier_constructor_args():
    sig = inspect.signature(UML2_TemplateableClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2_interface_is_not_abstract():
    assert not inspect.isabstract(UML2_Interface)


def test_uml2_interface_constructor_exists():
    assert callable(UML2_Interface.__init__)


def test_uml2_interface_constructor_args():
    sig = inspect.signature(UML2_Interface.__init__)
    params = list(sig.parameters.keys())



def test_uml2_actor_is_not_abstract():
    assert not inspect.isabstract(UML2_Actor)


def test_uml2_actor_constructor_exists():
    assert callable(UML2_Actor.__init__)


def test_uml2_actor_constructor_args():
    sig = inspect.signature(UML2_Actor.__init__)
    params = list(sig.parameters.keys())



def test_uml2_datatype_is_not_abstract():
    assert not inspect.isabstract(UML2_DataType)


def test_uml2_datatype_constructor_exists():
    assert callable(UML2_DataType.__init__)


def test_uml2_datatype_constructor_args():
    sig = inspect.signature(UML2_DataType.__init__)
    params = list(sig.parameters.keys())



def test_uml2_signal_is_not_abstract():
    assert not inspect.isabstract(UML2_Signal)


def test_uml2_signal_constructor_exists():
    assert callable(UML2_Signal.__init__)


def test_uml2_signal_constructor_args():
    sig = inspect.signature(UML2_Signal.__init__)
    params = list(sig.parameters.keys())



def test_uml2_parameterableclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2_ParameterableClassifier)


def test_uml2_parameterableclassifier_constructor_exists():
    assert callable(UML2_ParameterableClassifier.__init__)


def test_uml2_parameterableclassifier_constructor_args():
    sig = inspect.signature(UML2_ParameterableClassifier.__init__)
    params = list(sig.parameters.keys())



def test_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
    params = list(sig.parameters.keys())



def test_uml2_statemachine_is_not_abstract():
    assert not inspect.isabstract(UML2_StateMachine)


def test_uml2_statemachine_constructor_exists():
    assert callable(UML2_StateMachine.__init__)


def test_uml2_statemachine_constructor_args():
    sig = inspect.signature(UML2_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_uml2_interaction_is_not_abstract():
    assert not inspect.isabstract(UML2_Interaction)


def test_uml2_interaction_constructor_exists():
    assert callable(UML2_Interaction.__init__)


def test_uml2_interaction_constructor_args():
    sig = inspect.signature(UML2_Interaction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_activity_is_not_abstract():
    assert not inspect.isabstract(UML2_Activity)


def test_uml2_activity_constructor_exists():
    assert callable(UML2_Activity.__init__)


def test_uml2_activity_constructor_args():
    sig = inspect.signature(UML2_Activity.__init__)
    params = list(sig.parameters.keys())



def test_redefinableelement_is_not_abstract():
    assert not inspect.isabstract(RedefinableElement)


def test_redefinableelement_constructor_exists():
    assert callable(RedefinableElement.__init__)


def test_redefinableelement_constructor_args():
    sig = inspect.signature(RedefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2_feature_is_not_abstract():
    assert not inspect.isabstract(UML2_Feature)


def test_uml2_feature_constructor_exists():
    assert callable(UML2_Feature.__init__)


def test_uml2_feature_constructor_args():
    sig = inspect.signature(UML2_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "isStatic" in params, "Missing parameter 'isStatic'"

def test_uml2_feature_has_isStatic():
    assert hasattr(UML2_Feature, "isStatic")
    descriptor = None
    for klass in UML2_Feature.__mro__:
        if "isStatic" in klass.__dict__:
            descriptor = klass.__dict__["isStatic"]
            break
    assert isinstance(descriptor, property)



def test_uml2_state_is_not_abstract():
    assert not inspect.isabstract(UML2_State)


def test_uml2_state_constructor_exists():
    assert callable(UML2_State.__init__)


def test_uml2_state_constructor_args():
    sig = inspect.signature(UML2_State.__init__)
    params = list(sig.parameters.keys())



def test_uml2_activityedge_is_not_abstract():
    assert not inspect.isabstract(UML2_ActivityEdge)


def test_uml2_activityedge_constructor_exists():
    assert callable(UML2_ActivityEdge.__init__)


def test_uml2_activityedge_constructor_args():
    sig = inspect.signature(UML2_ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_uml2_region_is_not_abstract():
    assert not inspect.isabstract(UML2_Region)


def test_uml2_region_constructor_exists():
    assert callable(UML2_Region.__init__)


def test_uml2_region_constructor_args():
    sig = inspect.signature(UML2_Region.__init__)
    params = list(sig.parameters.keys())



def test_uml2_redefinabletemplatesignature_is_not_abstract():
    assert not inspect.isabstract(UML2_RedefinableTemplateSignature)


def test_uml2_redefinabletemplatesignature_constructor_exists():
    assert callable(UML2_RedefinableTemplateSignature.__init__)


def test_uml2_redefinabletemplatesignature_constructor_args():
    sig = inspect.signature(UML2_RedefinableTemplateSignature.__init__)
    params = list(sig.parameters.keys())



def test_uml2_classifier_is_not_abstract():
    assert not inspect.isabstract(UML2_Classifier)


def test_uml2_classifier_constructor_exists():
    assert callable(UML2_Classifier.__init__)


def test_uml2_classifier_constructor_args():
    sig = inspect.signature(UML2_Classifier.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_uml2_classifier_has_isAbstract():
    assert hasattr(UML2_Classifier, "isAbstract")
    descriptor = None
    for klass in UML2_Classifier.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_uml2_extensionpoint_is_not_abstract():
    assert not inspect.isabstract(UML2_ExtensionPoint)


def test_uml2_extensionpoint_constructor_exists():
    assert callable(UML2_ExtensionPoint.__init__)


def test_uml2_extensionpoint_constructor_args():
    sig = inspect.signature(UML2_ExtensionPoint.__init__)
    params = list(sig.parameters.keys())



def test_uml2_transition_is_not_abstract():
    assert not inspect.isabstract(UML2_Transition)


def test_uml2_transition_constructor_exists():
    assert callable(UML2_Transition.__init__)


def test_uml2_transition_constructor_args():
    sig = inspect.signature(UML2_Transition.__init__)
    params = list(sig.parameters.keys())



def test_uml2_activitynode_is_not_abstract():
    assert not inspect.isabstract(UML2_ActivityNode)


def test_uml2_activitynode_constructor_exists():
    assert callable(UML2_ActivityNode.__init__)


def test_uml2_activitynode_constructor_args():
    sig = inspect.signature(UML2_ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2_message_is_not_abstract():
    assert not inspect.isabstract(UML2_Message)


def test_uml2_message_constructor_exists():
    assert callable(UML2_Message.__init__)


def test_uml2_message_constructor_args():
    sig = inspect.signature(UML2_Message.__init__)
    params = list(sig.parameters.keys())



def test_uml2_activitypartition_is_not_abstract():
    assert not inspect.isabstract(UML2_ActivityPartition)


def test_uml2_activitypartition_constructor_exists():
    assert callable(UML2_ActivityPartition.__init__)


def test_uml2_activitypartition_constructor_args():
    sig = inspect.signature(UML2_ActivityPartition.__init__)
    params = list(sig.parameters.keys())



def test_uml2_lifeline_is_not_abstract():
    assert not inspect.isabstract(UML2_Lifeline)


def test_uml2_lifeline_constructor_exists():
    assert callable(UML2_Lifeline.__init__)


def test_uml2_lifeline_constructor_args():
    sig = inspect.signature(UML2_Lifeline.__init__)
    params = list(sig.parameters.keys())



def test_uml2_redefinableelement_is_not_abstract():
    assert not inspect.isabstract(UML2_RedefinableElement)


def test_uml2_redefinableelement_constructor_exists():
    assert callable(UML2_RedefinableElement.__init__)


def test_uml2_redefinableelement_constructor_args():
    sig = inspect.signature(UML2_RedefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2_interactionfragment_is_not_abstract():
    assert not inspect.isabstract(UML2_InteractionFragment)


def test_uml2_interactionfragment_constructor_exists():
    assert callable(UML2_InteractionFragment.__init__)


def test_uml2_interactionfragment_constructor_args():
    sig = inspect.signature(UML2_InteractionFragment.__init__)
    params = list(sig.parameters.keys())



def test_uml2_deployedartifact_is_not_abstract():
    assert not inspect.isabstract(UML2_DeployedArtifact)


def test_uml2_deployedartifact_constructor_exists():
    assert callable(UML2_DeployedArtifact.__init__)


def test_uml2_deployedartifact_constructor_args():
    sig = inspect.signature(UML2_DeployedArtifact.__init__)
    params = list(sig.parameters.keys())



def test_uml2_namespace_is_not_abstract():
    assert not inspect.isabstract(UML2_Namespace)


def test_uml2_namespace_constructor_exists():
    assert callable(UML2_Namespace.__init__)


def test_uml2_namespace_constructor_args():
    sig = inspect.signature(UML2_Namespace.__init__)
    params = list(sig.parameters.keys())



def test_uml2_messageend_is_not_abstract():
    assert not inspect.isabstract(UML2_MessageEnd)


def test_uml2_messageend_constructor_exists():
    assert callable(UML2_MessageEnd.__init__)


def test_uml2_messageend_constructor_args():
    sig = inspect.signature(UML2_MessageEnd.__init__)
    params = list(sig.parameters.keys())



def test_uml2_typedelement_is_not_abstract():
    assert not inspect.isabstract(UML2_TypedElement)


def test_uml2_typedelement_constructor_exists():
    assert callable(UML2_TypedElement.__init__)


def test_uml2_typedelement_constructor_args():
    sig = inspect.signature(UML2_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2_deploymenttarget_is_not_abstract():
    assert not inspect.isabstract(UML2_DeploymentTarget)


def test_uml2_deploymenttarget_constructor_exists():
    assert callable(UML2_DeploymentTarget.__init__)


def test_uml2_deploymenttarget_constructor_args():
    sig = inspect.signature(UML2_DeploymentTarget.__init__)
    params = list(sig.parameters.keys())



def test_uml2_include_is_not_abstract():
    assert not inspect.isabstract(UML2_Include)


def test_uml2_include_constructor_exists():
    assert callable(UML2_Include.__init__)


def test_uml2_include_constructor_args():
    sig = inspect.signature(UML2_Include.__init__)
    params = list(sig.parameters.keys())



def test_uml2_extend_is_not_abstract():
    assert not inspect.isabstract(UML2_Extend)


def test_uml2_extend_constructor_exists():
    assert callable(UML2_Extend.__init__)


def test_uml2_extend_constructor_args():
    sig = inspect.signature(UML2_Extend.__init__)
    params = list(sig.parameters.keys())



def test_uml2_parameterset_is_not_abstract():
    assert not inspect.isabstract(UML2_ParameterSet)


def test_uml2_parameterset_constructor_exists():
    assert callable(UML2_ParameterSet.__init__)


def test_uml2_parameterset_constructor_args():
    sig = inspect.signature(UML2_ParameterSet.__init__)
    params = list(sig.parameters.keys())



def test_uml2_vertex_is_not_abstract():
    assert not inspect.isabstract(UML2_Vertex)


def test_uml2_vertex_constructor_exists():
    assert callable(UML2_Vertex.__init__)


def test_uml2_vertex_constructor_args():
    sig = inspect.signature(UML2_Vertex.__init__)
    params = list(sig.parameters.keys())



def test_uml2_collaborationoccurrence_is_not_abstract():
    assert not inspect.isabstract(UML2_CollaborationOccurrence)


def test_uml2_collaborationoccurrence_constructor_exists():
    assert callable(UML2_CollaborationOccurrence.__init__)


def test_uml2_collaborationoccurrence_constructor_args():
    sig = inspect.signature(UML2_CollaborationOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_uml2_generalordering_is_not_abstract():
    assert not inspect.isabstract(UML2_GeneralOrdering)


def test_uml2_generalordering_constructor_exists():
    assert callable(UML2_GeneralOrdering.__init__)


def test_uml2_generalordering_constructor_args():
    sig = inspect.signature(UML2_GeneralOrdering.__init__)
    params = list(sig.parameters.keys())



def test_uml2_trigger_is_not_abstract():
    assert not inspect.isabstract(UML2_Trigger)


def test_uml2_trigger_constructor_exists():
    assert callable(UML2_Trigger.__init__)


def test_uml2_trigger_constructor_args():
    sig = inspect.signature(UML2_Trigger.__init__)
    params = list(sig.parameters.keys())



def test_invocationaction_is_not_abstract():
    assert not inspect.isabstract(InvocationAction)


def test_invocationaction_constructor_exists():
    assert callable(InvocationAction.__init__)


def test_invocationaction_constructor_args():
    sig = inspect.signature(InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_callaction_is_not_abstract():
    assert not inspect.isabstract(UML2_CallAction)


def test_uml2_callaction_constructor_exists():
    assert callable(UML2_CallAction.__init__)


def test_uml2_callaction_constructor_args():
    sig = inspect.signature(UML2_CallAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_broadcastsignalaction_is_not_abstract():
    assert not inspect.isabstract(UML2_BroadcastSignalAction)


def test_uml2_broadcastsignalaction_constructor_exists():
    assert callable(UML2_BroadcastSignalAction.__init__)


def test_uml2_broadcastsignalaction_constructor_args():
    sig = inspect.signature(UML2_BroadcastSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_sendsignalaction_is_not_abstract():
    assert not inspect.isabstract(UML2_SendSignalAction)


def test_uml2_sendsignalaction_constructor_exists():
    assert callable(UML2_SendSignalAction.__init__)


def test_uml2_sendsignalaction_constructor_args():
    sig = inspect.signature(UML2_SendSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_sendobjectaction_is_not_abstract():
    assert not inspect.isabstract(UML2_SendObjectAction)


def test_uml2_sendobjectaction_constructor_exists():
    assert callable(UML2_SendObjectAction.__init__)


def test_uml2_sendobjectaction_constructor_args():
    sig = inspect.signature(UML2_SendObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_abstraction_is_not_abstract():
    assert not inspect.isabstract(Abstraction)


def test_abstraction_constructor_exists():
    assert callable(Abstraction.__init__)


def test_abstraction_constructor_args():
    sig = inspect.signature(Abstraction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_manifestation_is_not_abstract():
    assert not inspect.isabstract(UML2_Manifestation)


def test_uml2_manifestation_constructor_exists():
    assert callable(UML2_Manifestation.__init__)


def test_uml2_manifestation_constructor_args():
    sig = inspect.signature(UML2_Manifestation.__init__)
    params = list(sig.parameters.keys())



def test_uml2_realization_is_not_abstract():
    assert not inspect.isabstract(UML2_Realization)


def test_uml2_realization_constructor_exists():
    assert callable(UML2_Realization.__init__)


def test_uml2_realization_constructor_args():
    sig = inspect.signature(UML2_Realization.__init__)
    params = list(sig.parameters.keys())



def test_messagetrigger_is_not_abstract():
    assert not inspect.isabstract(MessageTrigger)


def test_messagetrigger_constructor_exists():
    assert callable(MessageTrigger.__init__)


def test_messagetrigger_constructor_args():
    sig = inspect.signature(MessageTrigger.__init__)
    params = list(sig.parameters.keys())



def test_uml2_signaltrigger_is_not_abstract():
    assert not inspect.isabstract(UML2_SignalTrigger)


def test_uml2_signaltrigger_constructor_exists():
    assert callable(UML2_SignalTrigger.__init__)


def test_uml2_signaltrigger_constructor_args():
    sig = inspect.signature(UML2_SignalTrigger.__init__)
    params = list(sig.parameters.keys())



def test_uml2_calltrigger_is_not_abstract():
    assert not inspect.isabstract(UML2_CallTrigger)


def test_uml2_calltrigger_constructor_exists():
    assert callable(UML2_CallTrigger.__init__)


def test_uml2_calltrigger_constructor_args():
    sig = inspect.signature(UML2_CallTrigger.__init__)
    params = list(sig.parameters.keys())



def test_uml2_anytrigger_is_not_abstract():
    assert not inspect.isabstract(UML2_AnyTrigger)


def test_uml2_anytrigger_constructor_exists():
    assert callable(UML2_AnyTrigger.__init__)


def test_uml2_anytrigger_constructor_args():
    sig = inspect.signature(UML2_AnyTrigger.__init__)
    params = list(sig.parameters.keys())



def test_realization_is_not_abstract():
    assert not inspect.isabstract(Realization)


def test_realization_constructor_exists():
    assert callable(Realization.__init__)


def test_realization_constructor_args():
    sig = inspect.signature(Realization.__init__)
    params = list(sig.parameters.keys())



def test_uml2_substitution_is_not_abstract():
    assert not inspect.isabstract(UML2_Substitution)


def test_uml2_substitution_constructor_exists():
    assert callable(UML2_Substitution.__init__)


def test_uml2_substitution_constructor_args():
    sig = inspect.signature(UML2_Substitution.__init__)
    params = list(sig.parameters.keys())



def test_uml2_implementation_is_not_abstract():
    assert not inspect.isabstract(UML2_Implementation)


def test_uml2_implementation_constructor_exists():
    assert callable(UML2_Implementation.__init__)


def test_uml2_implementation_constructor_args():
    sig = inspect.signature(UML2_Implementation.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_uml2_variableaction_is_not_abstract():
    assert not inspect.isabstract(UML2_VariableAction)


def test_uml2_variableaction_constructor_exists():
    assert callable(UML2_VariableAction.__init__)


def test_uml2_variableaction_constructor_args():
    sig = inspect.signature(UML2_VariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_linkaction_is_not_abstract():
    assert not inspect.isabstract(UML2_LinkAction)


def test_uml2_linkaction_constructor_exists():
    assert callable(UML2_LinkAction.__init__)


def test_uml2_linkaction_constructor_args():
    sig = inspect.signature(UML2_LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_invocationaction_is_not_abstract():
    assert not inspect.isabstract(UML2_InvocationAction)


def test_uml2_invocationaction_constructor_exists():
    assert callable(UML2_InvocationAction.__init__)


def test_uml2_invocationaction_constructor_args():
    sig = inspect.signature(UML2_InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_clearassociationaction_is_not_abstract():
    assert not inspect.isabstract(UML2_ClearAssociationAction)


def test_uml2_clearassociationaction_constructor_exists():
    assert callable(UML2_ClearAssociationAction.__init__)


def test_uml2_clearassociationaction_constructor_args():
    sig = inspect.signature(UML2_ClearAssociationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_readlinkobjectendaction_is_not_abstract():
    assert not inspect.isabstract(UML2_ReadLinkObjectEndAction)


def test_uml2_readlinkobjectendaction_constructor_exists():
    assert callable(UML2_ReadLinkObjectEndAction.__init__)


def test_uml2_readlinkobjectendaction_constructor_args():
    sig = inspect.signature(UML2_ReadLinkObjectEndAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_replyaction_is_not_abstract():
    assert not inspect.isabstract(UML2_ReplyAction)


def test_uml2_replyaction_constructor_exists():
    assert callable(UML2_ReplyAction.__init__)


def test_uml2_replyaction_constructor_args():
    sig = inspect.signature(UML2_ReplyAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_startownedbehavioraction_is_not_abstract():
    assert not inspect.isabstract(UML2_StartOwnedBehaviorAction)


def test_uml2_startownedbehavioraction_constructor_exists():
    assert callable(UML2_StartOwnedBehaviorAction.__init__)


def test_uml2_startownedbehavioraction_constructor_args():
    sig = inspect.signature(UML2_StartOwnedBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_createobjectaction_is_not_abstract():
    assert not inspect.isabstract(UML2_CreateObjectAction)


def test_uml2_createobjectaction_constructor_exists():
    assert callable(UML2_CreateObjectAction.__init__)


def test_uml2_createobjectaction_constructor_args():
    sig = inspect.signature(UML2_CreateObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_raiseexceptionaction_is_not_abstract():
    assert not inspect.isabstract(UML2_RaiseExceptionAction)


def test_uml2_raiseexceptionaction_constructor_exists():
    assert callable(UML2_RaiseExceptionAction.__init__)


def test_uml2_raiseexceptionaction_constructor_args():
    sig = inspect.signature(UML2_RaiseExceptionAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_readextentaction_is_not_abstract():
    assert not inspect.isabstract(UML2_ReadExtentAction)


def test_uml2_readextentaction_constructor_exists():
    assert callable(UML2_ReadExtentAction.__init__)


def test_uml2_readextentaction_constructor_args():
    sig = inspect.signature(UML2_ReadExtentAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_accepteventaction_is_not_abstract():
    assert not inspect.isabstract(UML2_AcceptEventAction)


def test_uml2_accepteventaction_constructor_exists():
    assert callable(UML2_AcceptEventAction.__init__)


def test_uml2_accepteventaction_constructor_args():
    sig = inspect.signature(UML2_AcceptEventAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_readisclassifiedobjectaction_is_not_abstract():
    assert not inspect.isabstract(UML2_ReadIsClassifiedObjectAction)


def test_uml2_readisclassifiedobjectaction_constructor_exists():
    assert callable(UML2_ReadIsClassifiedObjectAction.__init__)


def test_uml2_readisclassifiedobjectaction_constructor_args():
    sig = inspect.signature(UML2_ReadIsClassifiedObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(UML2_StructuredActivityNode)


def test_uml2_structuredactivitynode_constructor_exists():
    assert callable(UML2_StructuredActivityNode.__init__)


def test_uml2_structuredactivitynode_constructor_args():
    sig = inspect.signature(UML2_StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2_destroyobjectaction_is_not_abstract():
    assert not inspect.isabstract(UML2_DestroyObjectAction)


def test_uml2_destroyobjectaction_constructor_exists():
    assert callable(UML2_DestroyObjectAction.__init__)


def test_uml2_destroyobjectaction_constructor_args():
    sig = inspect.signature(UML2_DestroyObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_reclassifyobjectaction_is_not_abstract():
    assert not inspect.isabstract(UML2_ReclassifyObjectAction)


def test_uml2_reclassifyobjectaction_constructor_exists():
    assert callable(UML2_ReclassifyObjectAction.__init__)


def test_uml2_reclassifyobjectaction_constructor_args():
    sig = inspect.signature(UML2_ReclassifyObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_applyfunctionaction_is_not_abstract():
    assert not inspect.isabstract(UML2_ApplyFunctionAction)


def test_uml2_applyfunctionaction_constructor_exists():
    assert callable(UML2_ApplyFunctionAction.__init__)


def test_uml2_applyfunctionaction_constructor_args():
    sig = inspect.signature(UML2_ApplyFunctionAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(UML2_StructuralFeatureAction)


def test_uml2_structuralfeatureaction_constructor_exists():
    assert callable(UML2_StructuralFeatureAction.__init__)


def test_uml2_structuralfeatureaction_constructor_args():
    sig = inspect.signature(UML2_StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_literalspecification_is_not_abstract():
    assert not inspect.isabstract(LiteralSpecification)


def test_literalspecification_constructor_exists():
    assert callable(LiteralSpecification.__init__)


def test_literalspecification_constructor_args():
    sig = inspect.signature(LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml2_literalnull_is_not_abstract():
    assert not inspect.isabstract(UML2_LiteralNull)


def test_uml2_literalnull_constructor_exists():
    assert callable(UML2_LiteralNull.__init__)


def test_uml2_literalnull_constructor_args():
    sig = inspect.signature(UML2_LiteralNull.__init__)
    params = list(sig.parameters.keys())



def test_uml2_literalinteger_is_not_abstract():
    assert not inspect.isabstract(UML2_LiteralInteger)


def test_uml2_literalinteger_constructor_exists():
    assert callable(UML2_LiteralInteger.__init__)


def test_uml2_literalinteger_constructor_args():
    sig = inspect.signature(UML2_LiteralInteger.__init__)
    params = list(sig.parameters.keys())



def test_uml2_literalunlimitednatural_is_not_abstract():
    assert not inspect.isabstract(UML2_LiteralUnlimitedNatural)


def test_uml2_literalunlimitednatural_constructor_exists():
    assert callable(UML2_LiteralUnlimitedNatural.__init__)


def test_uml2_literalunlimitednatural_constructor_args():
    sig = inspect.signature(UML2_LiteralUnlimitedNatural.__init__)
    params = list(sig.parameters.keys())



def test_uml2_literalboolean_is_not_abstract():
    assert not inspect.isabstract(UML2_LiteralBoolean)


def test_uml2_literalboolean_constructor_exists():
    assert callable(UML2_LiteralBoolean.__init__)


def test_uml2_literalboolean_constructor_args():
    sig = inspect.signature(UML2_LiteralBoolean.__init__)
    params = list(sig.parameters.keys())



def test_uml2_literalstring_is_not_abstract():
    assert not inspect.isabstract(UML2_LiteralString)


def test_uml2_literalstring_constructor_exists():
    assert callable(UML2_LiteralString.__init__)


def test_uml2_literalstring_constructor_args():
    sig = inspect.signature(UML2_LiteralString.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_is_not_abstract():
    assert not inspect.isabstract(ActivityNode)


def test_activitynode_constructor_exists():
    assert callable(ActivityNode.__init__)


def test_activitynode_constructor_args():
    sig = inspect.signature(ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2_controlnode_is_not_abstract():
    assert not inspect.isabstract(UML2_ControlNode)


def test_uml2_controlnode_constructor_exists():
    assert callable(UML2_ControlNode.__init__)


def test_uml2_controlnode_constructor_args():
    sig = inspect.signature(UML2_ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2_executablenode_is_not_abstract():
    assert not inspect.isabstract(UML2_ExecutableNode)


def test_uml2_executablenode_constructor_exists():
    assert callable(UML2_ExecutableNode.__init__)


def test_uml2_executablenode_constructor_args():
    sig = inspect.signature(UML2_ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_controlnode_is_not_abstract():
    assert not inspect.isabstract(ControlNode)


def test_controlnode_constructor_exists():
    assert callable(ControlNode.__init__)


def test_controlnode_constructor_args():
    sig = inspect.signature(ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2_decisionnode_is_not_abstract():
    assert not inspect.isabstract(UML2_DecisionNode)


def test_uml2_decisionnode_constructor_exists():
    assert callable(UML2_DecisionNode.__init__)


def test_uml2_decisionnode_constructor_args():
    sig = inspect.signature(UML2_DecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2_mergenode_is_not_abstract():
    assert not inspect.isabstract(UML2_MergeNode)


def test_uml2_mergenode_constructor_exists():
    assert callable(UML2_MergeNode.__init__)


def test_uml2_mergenode_constructor_args():
    sig = inspect.signature(UML2_MergeNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2_initialnode_is_not_abstract():
    assert not inspect.isabstract(UML2_InitialNode)


def test_uml2_initialnode_constructor_exists():
    assert callable(UML2_InitialNode.__init__)


def test_uml2_initialnode_constructor_args():
    sig = inspect.signature(UML2_InitialNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2_forknode_is_not_abstract():
    assert not inspect.isabstract(UML2_ForkNode)


def test_uml2_forknode_constructor_exists():
    assert callable(UML2_ForkNode.__init__)


def test_uml2_forknode_constructor_args():
    sig = inspect.signature(UML2_ForkNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2_joinnode_is_not_abstract():
    assert not inspect.isabstract(UML2_JoinNode)


def test_uml2_joinnode_constructor_exists():
    assert callable(UML2_JoinNode.__init__)


def test_uml2_joinnode_constructor_args():
    sig = inspect.signature(UML2_JoinNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2_finalnode_is_not_abstract():
    assert not inspect.isabstract(UML2_FinalNode)


def test_uml2_finalnode_constructor_exists():
    assert callable(UML2_FinalNode.__init__)


def test_uml2_finalnode_constructor_args():
    sig = inspect.signature(UML2_FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2_association_is_not_abstract():
    assert not inspect.isabstract(UML2_Association)


def test_uml2_association_constructor_exists():
    assert callable(UML2_Association.__init__)


def test_uml2_association_constructor_args():
    sig = inspect.signature(UML2_Association.__init__)
    params = list(sig.parameters.keys())



def test_deploymenttarget_is_not_abstract():
    assert not inspect.isabstract(DeploymentTarget)


def test_deploymenttarget_constructor_exists():
    assert callable(DeploymentTarget.__init__)


def test_deploymenttarget_constructor_args():
    sig = inspect.signature(DeploymentTarget.__init__)
    params = list(sig.parameters.keys())



def test_uml2_instancespecification_is_not_abstract():
    assert not inspect.isabstract(UML2_InstanceSpecification)


def test_uml2_instancespecification_constructor_exists():
    assert callable(UML2_InstanceSpecification.__init__)


def test_uml2_instancespecification_constructor_args():
    sig = inspect.signature(UML2_InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_connectableelement_is_not_abstract():
    assert not inspect.isabstract(ConnectableElement)


def test_connectableelement_constructor_exists():
    assert callable(ConnectableElement.__init__)


def test_connectableelement_constructor_args():
    sig = inspect.signature(ConnectableElement.__init__)
    params = list(sig.parameters.keys())



def test_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(StructuralFeature)


def test_structuralfeature_constructor_exists():
    assert callable(StructuralFeature.__init__)


def test_structuralfeature_constructor_args():
    sig = inspect.signature(StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_uml2_port_is_not_abstract():
    assert not inspect.isabstract(UML2_Port)


def test_uml2_port_constructor_exists():
    assert callable(UML2_Port.__init__)


def test_uml2_port_constructor_args():
    sig = inspect.signature(UML2_Port.__init__)
    params = list(sig.parameters.keys())



def test_uml2_extensionend_is_not_abstract():
    assert not inspect.isabstract(UML2_ExtensionEnd)


def test_uml2_extensionend_constructor_exists():
    assert callable(UML2_ExtensionEnd.__init__)


def test_uml2_extensionend_constructor_args():
    sig = inspect.signature(UML2_ExtensionEnd.__init__)
    params = list(sig.parameters.keys())



def test_structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(StructuralFeatureAction)


def test_structuralfeatureaction_constructor_exists():
    assert callable(StructuralFeatureAction.__init__)


def test_structuralfeatureaction_constructor_args():
    sig = inspect.signature(StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_readstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(UML2_ReadStructuralFeatureAction)


def test_uml2_readstructuralfeatureaction_constructor_exists():
    assert callable(UML2_ReadStructuralFeatureAction.__init__)


def test_uml2_readstructuralfeatureaction_constructor_args():
    sig = inspect.signature(UML2_ReadStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_clearstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(UML2_ClearStructuralFeatureAction)


def test_uml2_clearstructuralfeatureaction_constructor_exists():
    assert callable(UML2_ClearStructuralFeatureAction.__init__)


def test_uml2_clearstructuralfeatureaction_constructor_args():
    sig = inspect.signature(UML2_ClearStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(UML2_WriteStructuralFeatureAction)


def test_uml2_writestructuralfeatureaction_constructor_exists():
    assert callable(UML2_WriteStructuralFeatureAction.__init__)


def test_uml2_writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(UML2_WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_readlinkobjectendqualifieraction_is_not_abstract():
    assert not inspect.isabstract(UML2_ReadLinkObjectEndQualifierAction)


def test_uml2_readlinkobjectendqualifieraction_constructor_exists():
    assert callable(UML2_ReadLinkObjectEndQualifierAction.__init__)


def test_uml2_readlinkobjectendqualifieraction_constructor_args():
    sig = inspect.signature(UML2_ReadLinkObjectEndQualifierAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_inputpin_is_not_abstract():
    assert not inspect.isabstract(UML2_InputPin)


def test_uml2_inputpin_constructor_exists():
    assert callable(UML2_InputPin.__init__)


def test_uml2_inputpin_constructor_args():
    sig = inspect.signature(UML2_InputPin.__init__)
    params = list(sig.parameters.keys())



def test_uml2_testidentityaction_is_not_abstract():
    assert not inspect.isabstract(UML2_TestIdentityAction)


def test_uml2_testidentityaction_constructor_exists():
    assert callable(UML2_TestIdentityAction.__init__)


def test_uml2_testidentityaction_constructor_args():
    sig = inspect.signature(UML2_TestIdentityAction.__init__)
    params = list(sig.parameters.keys())



def test_association_is_not_abstract():
    assert not inspect.isabstract(Association)


def test_association_constructor_exists():
    assert callable(Association.__init__)


def test_association_constructor_args():
    sig = inspect.signature(Association.__init__)
    params = list(sig.parameters.keys())



def test_uml2_communicationpath_is_not_abstract():
    assert not inspect.isabstract(UML2_CommunicationPath)


def test_uml2_communicationpath_constructor_exists():
    assert callable(UML2_CommunicationPath.__init__)


def test_uml2_communicationpath_constructor_args():
    sig = inspect.signature(UML2_CommunicationPath.__init__)
    params = list(sig.parameters.keys())



def test_uml2_extension_is_not_abstract():
    assert not inspect.isabstract(UML2_Extension)


def test_uml2_extension_constructor_exists():
    assert callable(UML2_Extension.__init__)


def test_uml2_extension_constructor_args():
    sig = inspect.signature(UML2_Extension.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_uml2_stereotype_is_not_abstract():
    assert not inspect.isabstract(UML2_Stereotype)


def test_uml2_stereotype_constructor_exists():
    assert callable(UML2_Stereotype.__init__)


def test_uml2_stereotype_constructor_args():
    sig = inspect.signature(UML2_Stereotype.__init__)
    params = list(sig.parameters.keys())



def test_uml2_component_is_not_abstract():
    assert not inspect.isabstract(UML2_Component)


def test_uml2_component_constructor_exists():
    assert callable(UML2_Component.__init__)


def test_uml2_component_constructor_args():
    sig = inspect.signature(UML2_Component.__init__)
    params = list(sig.parameters.keys())



def test_uml2_behavior_is_not_abstract():
    assert not inspect.isabstract(UML2_Behavior)


def test_uml2_behavior_constructor_exists():
    assert callable(UML2_Behavior.__init__)


def test_uml2_behavior_constructor_args():
    sig = inspect.signature(UML2_Behavior.__init__)
    params = list(sig.parameters.keys())



def test_uml2_node_is_not_abstract():
    assert not inspect.isabstract(UML2_Node)


def test_uml2_node_constructor_exists():
    assert callable(UML2_Node.__init__)


def test_uml2_node_constructor_args():
    sig = inspect.signature(UML2_Node.__init__)
    params = list(sig.parameters.keys())



def test_uml2_associationclass_is_not_abstract():
    assert not inspect.isabstract(UML2_AssociationClass)


def test_uml2_associationclass_constructor_exists():
    assert callable(UML2_AssociationClass.__init__)


def test_uml2_associationclass_constructor_args():
    sig = inspect.signature(UML2_AssociationClass.__init__)
    params = list(sig.parameters.keys())



def test_uml2_outputpin_is_not_abstract():
    assert not inspect.isabstract(UML2_OutputPin)


def test_uml2_outputpin_constructor_exists():
    assert callable(UML2_OutputPin.__init__)


def test_uml2_outputpin_constructor_args():
    sig = inspect.signature(UML2_OutputPin.__init__)
    params = list(sig.parameters.keys())



def test_uml2_readselfaction_is_not_abstract():
    assert not inspect.isabstract(UML2_ReadSelfAction)


def test_uml2_readselfaction_constructor_exists():
    assert callable(UML2_ReadSelfAction.__init__)


def test_uml2_readselfaction_constructor_args():
    sig = inspect.signature(UML2_ReadSelfAction.__init__)
    params = list(sig.parameters.keys())



def test_parameterableelement_is_not_abstract():
    assert not inspect.isabstract(ParameterableElement)


def test_parameterableelement_constructor_exists():
    assert callable(ParameterableElement.__init__)


def test_parameterableelement_constructor_args():
    sig = inspect.signature(ParameterableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2_packageableelement_is_not_abstract():
    assert not inspect.isabstract(UML2_PackageableElement)


def test_uml2_packageableelement_constructor_exists():
    assert callable(UML2_PackageableElement.__init__)


def test_uml2_packageableelement_constructor_args():
    sig = inspect.signature(UML2_PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2_connectableelement_is_not_abstract():
    assert not inspect.isabstract(UML2_ConnectableElement)


def test_uml2_connectableelement_constructor_exists():
    assert callable(UML2_ConnectableElement.__init__)


def test_uml2_connectableelement_constructor_args():
    sig = inspect.signature(UML2_ConnectableElement.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(UML2_StructuralFeature)


def test_uml2_structuralfeature_constructor_exists():
    assert callable(UML2_StructuralFeature.__init__)


def test_uml2_structuralfeature_constructor_args():
    sig = inspect.signature(UML2_StructuralFeature.__init__)
    params = list(sig.parameters.keys())
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"

def test_uml2_structuralfeature_has_isReadOnly():
    assert hasattr(UML2_StructuralFeature, "isReadOnly")
    descriptor = None
    for klass in UML2_StructuralFeature.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)



def test_uml2_parameter_is_not_abstract():
    assert not inspect.isabstract(UML2_Parameter)


def test_uml2_parameter_constructor_exists():
    assert callable(UML2_Parameter.__init__)


def test_uml2_parameter_constructor_args():
    sig = inspect.signature(UML2_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_uml2_parameter_has_direction():
    assert hasattr(UML2_Parameter, "direction")
    descriptor = None
    for klass in UML2_Parameter.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_uml2_variable_is_not_abstract():
    assert not inspect.isabstract(UML2_Variable)


def test_uml2_variable_constructor_exists():
    assert callable(UML2_Variable.__init__)


def test_uml2_variable_constructor_args():
    sig = inspect.signature(UML2_Variable.__init__)
    params = list(sig.parameters.keys())



def test_uml2_objectnode_is_not_abstract():
    assert not inspect.isabstract(UML2_ObjectNode)


def test_uml2_objectnode_constructor_exists():
    assert callable(UML2_ObjectNode.__init__)


def test_uml2_objectnode_constructor_args():
    sig = inspect.signature(UML2_ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2_operation_is_not_abstract():
    assert not inspect.isabstract(UML2_Operation)


def test_uml2_operation_constructor_exists():
    assert callable(UML2_Operation.__init__)


def test_uml2_operation_constructor_args():
    sig = inspect.signature(UML2_Operation.__init__)
    params = list(sig.parameters.keys())



def test_uml2_valuespecification_is_not_abstract():
    assert not inspect.isabstract(UML2_ValueSpecification)


def test_uml2_valuespecification_constructor_exists():
    assert callable(UML2_ValueSpecification.__init__)


def test_uml2_valuespecification_constructor_args():
    sig = inspect.signature(UML2_ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(BehavioredClassifier)


def test_behavioredclassifier_constructor_exists():
    assert callable(BehavioredClassifier.__init__)


def test_behavioredclassifier_constructor_args():
    sig = inspect.signature(BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2_collaboration_is_not_abstract():
    assert not inspect.isabstract(UML2_Collaboration)


def test_uml2_collaboration_constructor_exists():
    assert callable(UML2_Collaboration.__init__)


def test_uml2_collaboration_constructor_args():
    sig = inspect.signature(UML2_Collaboration.__init__)
    params = list(sig.parameters.keys())



def test_uml2_class_is_not_abstract():
    assert not inspect.isabstract(UML2_Class)


def test_uml2_class_constructor_exists():
    assert callable(UML2_Class.__init__)


def test_uml2_class_constructor_args():
    sig = inspect.signature(UML2_Class.__init__)
    params = list(sig.parameters.keys())
    assert "isActive" in params, "Missing parameter 'isActive'"

def test_uml2_class_has_isActive():
    assert hasattr(UML2_Class, "isActive")
    descriptor = None
    for klass in UML2_Class.__mro__:
        if "isActive" in klass.__dict__:
            descriptor = klass.__dict__["isActive"]
            break
    assert isinstance(descriptor, property)



def test_uml2_usecase_is_not_abstract():
    assert not inspect.isabstract(UML2_UseCase)


def test_uml2_usecase_constructor_exists():
    assert callable(UML2_UseCase.__init__)


def test_uml2_usecase_constructor_args():
    sig = inspect.signature(UML2_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_valuespecification_is_not_abstract():
    assert not inspect.isabstract(ValueSpecification)


def test_valuespecification_constructor_exists():
    assert callable(ValueSpecification.__init__)


def test_valuespecification_constructor_args():
    sig = inspect.signature(ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml2_instancevalue_is_not_abstract():
    assert not inspect.isabstract(UML2_InstanceValue)


def test_uml2_instancevalue_constructor_exists():
    assert callable(UML2_InstanceValue.__init__)


def test_uml2_instancevalue_constructor_args():
    sig = inspect.signature(UML2_InstanceValue.__init__)
    params = list(sig.parameters.keys())



def test_uml2_literalspecification_is_not_abstract():
    assert not inspect.isabstract(UML2_LiteralSpecification)


def test_uml2_literalspecification_constructor_exists():
    assert callable(UML2_LiteralSpecification.__init__)


def test_uml2_literalspecification_constructor_args():
    sig = inspect.signature(UML2_LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml2_duration_is_not_abstract():
    assert not inspect.isabstract(UML2_Duration)


def test_uml2_duration_constructor_exists():
    assert callable(UML2_Duration.__init__)


def test_uml2_duration_constructor_args():
    sig = inspect.signature(UML2_Duration.__init__)
    params = list(sig.parameters.keys())



def test_uml2_opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(UML2_OpaqueExpression)


def test_uml2_opaqueexpression_constructor_exists():
    assert callable(UML2_OpaqueExpression.__init__)


def test_uml2_opaqueexpression_constructor_args():
    sig = inspect.signature(UML2_OpaqueExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml2_timeexpression_is_not_abstract():
    assert not inspect.isabstract(UML2_TimeExpression)


def test_uml2_timeexpression_constructor_exists():
    assert callable(UML2_TimeExpression.__init__)


def test_uml2_timeexpression_constructor_args():
    sig = inspect.signature(UML2_TimeExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml2_interval_is_not_abstract():
    assert not inspect.isabstract(UML2_Interval)


def test_uml2_interval_constructor_exists():
    assert callable(UML2_Interval.__init__)


def test_uml2_interval_constructor_args():
    sig = inspect.signature(UML2_Interval.__init__)
    params = list(sig.parameters.keys())



def test_createlinkaction_is_not_abstract():
    assert not inspect.isabstract(CreateLinkAction)


def test_createlinkaction_constructor_exists():
    assert callable(CreateLinkAction.__init__)


def test_createlinkaction_constructor_args():
    sig = inspect.signature(CreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_createlinkobjectaction_is_not_abstract():
    assert not inspect.isabstract(UML2_CreateLinkObjectAction)


def test_uml2_createlinkobjectaction_constructor_exists():
    assert callable(UML2_CreateLinkObjectAction.__init__)


def test_uml2_createlinkobjectaction_constructor_args():
    sig = inspect.signature(UML2_CreateLinkObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_property_is_not_abstract():
    assert not inspect.isabstract(UML2_Property)


def test_uml2_property_constructor_exists():
    assert callable(UML2_Property.__init__)


def test_uml2_property_constructor_args():
    sig = inspect.signature(UML2_Property.__init__)
    params = list(sig.parameters.keys())
    assert "aggregation" in params, "Missing parameter 'aggregation'"
    assert "isDerivedUnion" in params, "Missing parameter 'isDerivedUnion'"
    assert "isComposite" in params, "Missing parameter 'isComposite'"
    assert "isDerived" in params, "Missing parameter 'isDerived'"

def test_uml2_property_has_aggregation():
    assert hasattr(UML2_Property, "aggregation")
    descriptor = None
    for klass in UML2_Property.__mro__:
        if "aggregation" in klass.__dict__:
            descriptor = klass.__dict__["aggregation"]
            break
    assert isinstance(descriptor, property)

def test_uml2_property_has_isDerivedUnion():
    assert hasattr(UML2_Property, "isDerivedUnion")
    descriptor = None
    for klass in UML2_Property.__mro__:
        if "isDerivedUnion" in klass.__dict__:
            descriptor = klass.__dict__["isDerivedUnion"]
            break
    assert isinstance(descriptor, property)

def test_uml2_property_has_isComposite():
    assert hasattr(UML2_Property, "isComposite")
    descriptor = None
    for klass in UML2_Property.__mro__:
        if "isComposite" in klass.__dict__:
            descriptor = klass.__dict__["isComposite"]
            break
    assert isinstance(descriptor, property)

def test_uml2_property_has_isDerived():
    assert hasattr(UML2_Property, "isDerived")
    descriptor = None
    for klass in UML2_Property.__mro__:
        if "isDerived" in klass.__dict__:
            descriptor = klass.__dict__["isDerived"]
            break
    assert isinstance(descriptor, property)



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_uml2_templateparameter_is_not_abstract():
    assert not inspect.isabstract(UML2_TemplateParameter)


def test_uml2_templateparameter_constructor_exists():
    assert callable(UML2_TemplateParameter.__init__)


def test_uml2_templateparameter_constructor_args():
    sig = inspect.signature(UML2_TemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_uml2_activitygroup_is_not_abstract():
    assert not inspect.isabstract(UML2_ActivityGroup)


def test_uml2_activitygroup_constructor_exists():
    assert callable(UML2_ActivityGroup.__init__)


def test_uml2_activitygroup_constructor_args():
    sig = inspect.signature(UML2_ActivityGroup.__init__)
    params = list(sig.parameters.keys())



def test_uml2_clause_is_not_abstract():
    assert not inspect.isabstract(UML2_Clause)


def test_uml2_clause_constructor_exists():
    assert callable(UML2_Clause.__init__)


def test_uml2_clause_constructor_args():
    sig = inspect.signature(UML2_Clause.__init__)
    params = list(sig.parameters.keys())



def test_uml2_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(UML2_MultiplicityElement)


def test_uml2_multiplicityelement_constructor_exists():
    assert callable(UML2_MultiplicityElement.__init__)


def test_uml2_multiplicityelement_constructor_args():
    sig = inspect.signature(UML2_MultiplicityElement.__init__)
    params = list(sig.parameters.keys())
    assert "upper" in params, "Missing parameter 'upper'"
    assert "lower" in params, "Missing parameter 'lower'"
    assert "isOrdered" in params, "Missing parameter 'isOrdered'"
    assert "isUnique" in params, "Missing parameter 'isUnique'"

def test_uml2_multiplicityelement_has_upper():
    assert hasattr(UML2_MultiplicityElement, "upper")
    descriptor = None
    for klass in UML2_MultiplicityElement.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_uml2_multiplicityelement_has_lower():
    assert hasattr(UML2_MultiplicityElement, "lower")
    descriptor = None
    for klass in UML2_MultiplicityElement.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_uml2_multiplicityelement_has_isOrdered():
    assert hasattr(UML2_MultiplicityElement, "isOrdered")
    descriptor = None
    for klass in UML2_MultiplicityElement.__mro__:
        if "isOrdered" in klass.__dict__:
            descriptor = klass.__dict__["isOrdered"]
            break
    assert isinstance(descriptor, property)

def test_uml2_multiplicityelement_has_isUnique():
    assert hasattr(UML2_MultiplicityElement, "isUnique")
    descriptor = None
    for klass in UML2_MultiplicityElement.__mro__:
        if "isUnique" in klass.__dict__:
            descriptor = klass.__dict__["isUnique"]
            break
    assert isinstance(descriptor, property)



def test_uml2_parameterableelement_is_not_abstract():
    assert not inspect.isabstract(UML2_ParameterableElement)


def test_uml2_parameterableelement_constructor_exists():
    assert callable(UML2_ParameterableElement.__init__)


def test_uml2_parameterableelement_constructor_args():
    sig = inspect.signature(UML2_ParameterableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2_slot_is_not_abstract():
    assert not inspect.isabstract(UML2_Slot)


def test_uml2_slot_constructor_exists():
    assert callable(UML2_Slot.__init__)


def test_uml2_slot_constructor_args():
    sig = inspect.signature(UML2_Slot.__init__)
    params = list(sig.parameters.keys())



def test_uml2_linkenddata_is_not_abstract():
    assert not inspect.isabstract(UML2_LinkEndData)


def test_uml2_linkenddata_constructor_exists():
    assert callable(UML2_LinkEndData.__init__)


def test_uml2_linkenddata_constructor_args():
    sig = inspect.signature(UML2_LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_uml2_templateableelement_is_not_abstract():
    assert not inspect.isabstract(UML2_TemplateableElement)


def test_uml2_templateableelement_constructor_exists():
    assert callable(UML2_TemplateableElement.__init__)


def test_uml2_templateableelement_constructor_args():
    sig = inspect.signature(UML2_TemplateableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2_templatesignature_is_not_abstract():
    assert not inspect.isabstract(UML2_TemplateSignature)


def test_uml2_templatesignature_constructor_exists():
    assert callable(UML2_TemplateSignature.__init__)


def test_uml2_templatesignature_constructor_args():
    sig = inspect.signature(UML2_TemplateSignature.__init__)
    params = list(sig.parameters.keys())



def test_uml2_exceptionhandler_is_not_abstract():
    assert not inspect.isabstract(UML2_ExceptionHandler)


def test_uml2_exceptionhandler_constructor_exists():
    assert callable(UML2_ExceptionHandler.__init__)


def test_uml2_exceptionhandler_constructor_args():
    sig = inspect.signature(UML2_ExceptionHandler.__init__)
    params = list(sig.parameters.keys())



def test_uml2_templateparametersubstitution_is_not_abstract():
    assert not inspect.isabstract(UML2_TemplateParameterSubstitution)


def test_uml2_templateparametersubstitution_constructor_exists():
    assert callable(UML2_TemplateParameterSubstitution.__init__)


def test_uml2_templateparametersubstitution_constructor_args():
    sig = inspect.signature(UML2_TemplateParameterSubstitution.__init__)
    params = list(sig.parameters.keys())



def test_uml2_relationship_is_not_abstract():
    assert not inspect.isabstract(UML2_Relationship)


def test_uml2_relationship_constructor_exists():
    assert callable(UML2_Relationship.__init__)


def test_uml2_relationship_constructor_args():
    sig = inspect.signature(UML2_Relationship.__init__)
    params = list(sig.parameters.keys())



def test_uml2_qualifiervalue_is_not_abstract():
    assert not inspect.isabstract(UML2_QualifierValue)


def test_uml2_qualifiervalue_constructor_exists():
    assert callable(UML2_QualifierValue.__init__)


def test_uml2_qualifiervalue_constructor_args():
    sig = inspect.signature(UML2_QualifierValue.__init__)
    params = list(sig.parameters.keys())

def test_visibilitykind_exists():
    # Check that the Enumeration exists
    assert VisibilityKind is not None

def test_visibilitykind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VisibilityKind]
    expected_literals = [
        "private",
        "public",
        "protected",
        "package",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VisibilityKind"

def test_parameterdirectionkind_exists():
    # Check that the Enumeration exists
    assert ParameterDirectionKind is not None

def test_parameterdirectionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterDirectionKind]
    expected_literals = [
        "in_",
        "inout",
        "return_",
        "out",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterDirectionKind"

def test_aggregationkind_exists():
    # Check that the Enumeration exists
    assert AggregationKind is not None

def test_aggregationkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AggregationKind]
    expected_literals = [
        "shared",
        "composite",
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
Trigger_strategy = st.builds(
    Trigger,
)
UML2_TimeTrigger_strategy = st.builds(
    UML2_TimeTrigger,
)
FinalNode_strategy = st.builds(
    FinalNode,
)
UML2_ActivityFinalNode_strategy = st.builds(
    UML2_ActivityFinalNode,
)
MessageEnd_strategy = st.builds(
    MessageEnd,
)
InteractionFragment_strategy = st.builds(
    InteractionFragment,
)
UML2_EventOccurrence_strategy = st.builds(
    UML2_EventOccurrence,
)
UML2_Continuation_strategy = st.builds(
    UML2_Continuation,
)
DeployedArtifact_strategy = st.builds(
    DeployedArtifact,
)
Relationship_strategy = st.builds(
    Relationship,
)
UML2_DirectedRelationship_strategy = st.builds(
    UML2_DirectedRelationship,
)
DataType_strategy = st.builds(
    DataType,
)
UML2_PrimitiveType_strategy = st.builds(
    UML2_PrimitiveType,
)
InstanceSpecification_strategy = st.builds(
    InstanceSpecification,
)
UML2_EnumerationLiteral_strategy = st.builds(
    UML2_EnumerationLiteral,
)
Artifact_strategy = st.builds(
    Artifact,
)
UML2_DeploymentSpecification_strategy = st.builds(
    UML2_DeploymentSpecification,
)
TemplateableElement_strategy = st.builds(
    TemplateableElement,
)
UML2_NamedElement_strategy = st.builds(
    UML2_NamedElement,
    name=
        safe_text,
    visibility=
        safe_text
)
InputPin_strategy = st.builds(
    InputPin,
)
UML2_ValuePin_strategy = st.builds(
    UML2_ValuePin,
)
Interval_strategy = st.builds(
    Interval,
)
UML2_TimeInterval_strategy = st.builds(
    UML2_TimeInterval,
)
StructuredActivityNode_strategy = st.builds(
    StructuredActivityNode,
)
UML2_ExpansionRegion_strategy = st.builds(
    UML2_ExpansionRegion,
)
Type_strategy = st.builds(
    Type,
)
WriteVariableAction_strategy = st.builds(
    WriteVariableAction,
)
UML2_RemoveVariableValueAction_strategy = st.builds(
    UML2_RemoveVariableValueAction,
)
TemplateSignature_strategy = st.builds(
    TemplateSignature,
)
DirectedRelationship_strategy = st.builds(
    DirectedRelationship,
)
EncapsulatedClassifier_strategy = st.builds(
    EncapsulatedClassifier,
)
OpaqueExpression_strategy = st.builds(
    OpaqueExpression,
)
UML2_Expression_strategy = st.builds(
    UML2_Expression,
)
Transition_strategy = st.builds(
    Transition,
)
UML2_ProtocolTransition_strategy = st.builds(
    UML2_ProtocolTransition,
)
TemplateParameter_strategy = st.builds(
    TemplateParameter,
)
UML2_ConnectableElementTemplateParameter_strategy = st.builds(
    UML2_ConnectableElementTemplateParameter,
)
UML2_OperationTemplateParameter_strategy = st.builds(
    UML2_OperationTemplateParameter,
)
UML2_ClassifierTemplateParameter_strategy = st.builds(
    UML2_ClassifierTemplateParameter,
)
Package_strategy = st.builds(
    Package,
)
UML2_Profile_strategy = st.builds(
    UML2_Profile,
)
UML2_Model_strategy = st.builds(
    UML2_Model,
)
Constraint_strategy = st.builds(
    Constraint,
)
UML2_IntervalConstraint_strategy = st.builds(
    UML2_IntervalConstraint,
)
AcceptEventAction_strategy = st.builds(
    AcceptEventAction,
)
UML2_AcceptCallAction_strategy = st.builds(
    UML2_AcceptCallAction,
)
StateMachine_strategy = st.builds(
    StateMachine,
)
UML2_ProtocolStateMachine_strategy = st.builds(
    UML2_ProtocolStateMachine,
)
UML2_StateInvariant_strategy = st.builds(
    UML2_StateInvariant,
)
UML2_Comment_strategy = st.builds(
    UML2_Comment,
)
UML2_CombinedFragment_strategy = st.builds(
    UML2_CombinedFragment,
)
UML2_InteractionOccurrence_strategy = st.builds(
    UML2_InteractionOccurrence,
)
UML2_PackageMerge_strategy = st.builds(
    UML2_PackageMerge,
)
UML2_ExecutionOccurrence_strategy = st.builds(
    UML2_ExecutionOccurrence,
)
InteractionOccurrence_strategy = st.builds(
    InteractionOccurrence,
)
UML2_PartDecomposition_strategy = st.builds(
    UML2_PartDecomposition,
)
UML2_AddVariableValueAction_strategy = st.builds(
    UML2_AddVariableValueAction,
)
UML2_ElementImport_strategy = st.builds(
    UML2_ElementImport,
)
UML2_FlowFinalNode_strategy = st.builds(
    UML2_FlowFinalNode,
)
UML2_DurationInterval_strategy = st.builds(
    UML2_DurationInterval,
)
UML2_ChangeTrigger_strategy = st.builds(
    UML2_ChangeTrigger,
)
CallAction_strategy = st.builds(
    CallAction,
)
UML2_CallBehaviorAction_strategy = st.builds(
    UML2_CallBehaviorAction,
)
UML2_CallOperationAction_strategy = st.builds(
    UML2_CallOperationAction,
)
UML2_MessageTrigger_strategy = st.builds(
    UML2_MessageTrigger,
)
UML2_Gate_strategy = st.builds(
    UML2_Gate,
)
UML2_Enumeration_strategy = st.builds(
    UML2_Enumeration,
)
UML2_ProtocolConformance_strategy = st.builds(
    UML2_ProtocolConformance,
)
State_strategy = st.builds(
    State,
)
UML2_FinalState_strategy = st.builds(
    UML2_FinalState,
)
UML2_StringExpression_strategy = st.builds(
    UML2_StringExpression,
)
Node_strategy = st.builds(
    Node,
)
UML2_Device_strategy = st.builds(
    UML2_Device,
)
UML2_ExecutionEnvironment_strategy = st.builds(
    UML2_ExecutionEnvironment,
)
UML2_PackageImport_strategy = st.builds(
    UML2_PackageImport,
)
BehavioralFeature_strategy = st.builds(
    BehavioralFeature,
)
UML2_Reception_strategy = st.builds(
    UML2_Reception,
)
ActivityEdge_strategy = st.builds(
    ActivityEdge,
)
UML2_ObjectFlow_strategy = st.builds(
    UML2_ObjectFlow,
)
UML2_ControlFlow_strategy = st.builds(
    UML2_ControlFlow,
)
LinkEndData_strategy = st.builds(
    LinkEndData,
)
UML2_LinkEndCreationData_strategy = st.builds(
    UML2_LinkEndCreationData,
)
UML2_InteractionConstraint_strategy = st.builds(
    UML2_InteractionConstraint,
)
ExecutableNode_strategy = st.builds(
    ExecutableNode,
)
UML2_Action_strategy = st.builds(
    UML2_Action,
)
UML2_LoopNode_strategy = st.builds(
    UML2_LoopNode,
)
UML2_ConditionalNode_strategy = st.builds(
    UML2_ConditionalNode,
)
PackageImport_strategy = st.builds(
    PackageImport,
)
UML2_ProfileApplication_strategy = st.builds(
    UML2_ProfileApplication,
)
UML2_TemplateBinding_strategy = st.builds(
    UML2_TemplateBinding,
)
VariableAction_strategy = st.builds(
    VariableAction,
)
UML2_WriteVariableAction_strategy = st.builds(
    UML2_WriteVariableAction,
)
UML2_ReadVariableAction_strategy = st.builds(
    UML2_ReadVariableAction,
)
UML2_ClearVariableAction_strategy = st.builds(
    UML2_ClearVariableAction,
)
Feature_strategy = st.builds(
    Feature,
)
UML2_Connector_strategy = st.builds(
    UML2_Connector,
)
UML2_Generalization_strategy = st.builds(
    UML2_Generalization,
)
PackageableElement_strategy = st.builds(
    PackageableElement,
)
UML2_Constraint_strategy = st.builds(
    UML2_Constraint,
)
UML2_Dependency_strategy = st.builds(
    UML2_Dependency,
)
UML2_Type_strategy = st.builds(
    UML2_Type,
)
UML2_InformationFlow_strategy = st.builds(
    UML2_InformationFlow,
)
UML2_GeneralizationSet_strategy = st.builds(
    UML2_GeneralizationSet,
)
UML2_PrimitiveFunction_strategy = st.builds(
    UML2_PrimitiveFunction,
)
WriteLinkAction_strategy = st.builds(
    WriteLinkAction,
)
UML2_DestroyLinkAction_strategy = st.builds(
    UML2_DestroyLinkAction,
)
UML2_CreateLinkAction_strategy = st.builds(
    UML2_CreateLinkAction,
)
MultiplicityElement_strategy = st.builds(
    MultiplicityElement,
)
UML2_ConnectorEnd_strategy = st.builds(
    UML2_ConnectorEnd,
)
ObjectNode_strategy = st.builds(
    ObjectNode,
)
UML2_ActivityParameterNode_strategy = st.builds(
    UML2_ActivityParameterNode,
)
UML2_CentralBufferNode_strategy = st.builds(
    UML2_CentralBufferNode,
)
UML2_ExpansionNode_strategy = st.builds(
    UML2_ExpansionNode,
)
UML2_Pin_strategy = st.builds(
    UML2_Pin,
)
StructuredClassifier_strategy = st.builds(
    StructuredClassifier,
)
UML2_EncapsulatedClassifier_strategy = st.builds(
    UML2_EncapsulatedClassifier,
)
IntervalConstraint_strategy = st.builds(
    IntervalConstraint,
)
UML2_TimeConstraint_strategy = st.builds(
    UML2_TimeConstraint,
)
UML2_DurationConstraint_strategy = st.builds(
    UML2_DurationConstraint,
)
EventOccurrence_strategy = st.builds(
    EventOccurrence,
)
UML2_Stop_strategy = st.builds(
    UML2_Stop,
)
LinkAction_strategy = st.builds(
    LinkAction,
)
UML2_WriteLinkAction_strategy = st.builds(
    UML2_WriteLinkAction,
)
UML2_ReadLinkAction_strategy = st.builds(
    UML2_ReadLinkAction,
)
Dependency_strategy = st.builds(
    Dependency,
)
UML2_Deployment_strategy = st.builds(
    UML2_Deployment,
)
UML2_Usage_strategy = st.builds(
    UML2_Usage,
)
UML2_Abstraction_strategy = st.builds(
    UML2_Abstraction,
)
UML2_Permission_strategy = st.builds(
    UML2_Permission,
)
Pin_strategy = st.builds(
    Pin,
)
ActivityGroup_strategy = st.builds(
    ActivityGroup,
)
UML2_InterruptibleActivityRegion_strategy = st.builds(
    UML2_InterruptibleActivityRegion,
)
Vertex_strategy = st.builds(
    Vertex,
)
UML2_Pseudostate_strategy = st.builds(
    UML2_Pseudostate,
)
UML2_ConnectionPointReference_strategy = st.builds(
    UML2_ConnectionPointReference,
)
Namespace_strategy = st.builds(
    Namespace,
)
UML2_Package_strategy = st.builds(
    UML2_Package,
)
UML2_BehavioralFeature_strategy = st.builds(
    UML2_BehavioralFeature,
)
UML2_InteractionOperand_strategy = st.builds(
    UML2_InteractionOperand,
)
CentralBufferNode_strategy = st.builds(
    CentralBufferNode,
)
UML2_DataStoreNode_strategy = st.builds(
    UML2_DataStoreNode,
)
WriteStructuralFeatureAction_strategy = st.builds(
    WriteStructuralFeatureAction,
)
UML2_RemoveStructuralFeatureValueAction_strategy = st.builds(
    UML2_RemoveStructuralFeatureValueAction,
)
UML2_DurationObservationAction_strategy = st.builds(
    UML2_DurationObservationAction,
)
UML2_TimeObservationAction_strategy = st.builds(
    UML2_TimeObservationAction,
)
UML2_AddStructuralFeatureValueAction_strategy = st.builds(
    UML2_AddStructuralFeatureValueAction,
)
UML2_Element_strategy = st.builds(
    UML2_Element,
)
Classifier_strategy = st.builds(
    Classifier,
)
UML2_StructuredClassifier_strategy = st.builds(
    UML2_StructuredClassifier,
)
UML2_Artifact_strategy = st.builds(
    UML2_Artifact,
)
UML2_BehavioredClassifier_strategy = st.builds(
    UML2_BehavioredClassifier,
)
UML2_InformationItem_strategy = st.builds(
    UML2_InformationItem,
)
UML2_TemplateableClassifier_strategy = st.builds(
    UML2_TemplateableClassifier,
)
UML2_Interface_strategy = st.builds(
    UML2_Interface,
)
UML2_Actor_strategy = st.builds(
    UML2_Actor,
)
UML2_DataType_strategy = st.builds(
    UML2_DataType,
)
UML2_Signal_strategy = st.builds(
    UML2_Signal,
)
UML2_ParameterableClassifier_strategy = st.builds(
    UML2_ParameterableClassifier,
)
Behavior_strategy = st.builds(
    Behavior,
)
UML2_StateMachine_strategy = st.builds(
    UML2_StateMachine,
)
UML2_Interaction_strategy = st.builds(
    UML2_Interaction,
)
UML2_Activity_strategy = st.builds(
    UML2_Activity,
)
RedefinableElement_strategy = st.builds(
    RedefinableElement,
)
UML2_Feature_strategy = st.builds(
    UML2_Feature,
    isStatic=
        st.booleans()
)
UML2_State_strategy = st.builds(
    UML2_State,
)
UML2_ActivityEdge_strategy = st.builds(
    UML2_ActivityEdge,
)
UML2_Region_strategy = st.builds(
    UML2_Region,
)
UML2_RedefinableTemplateSignature_strategy = st.builds(
    UML2_RedefinableTemplateSignature,
)
UML2_Classifier_strategy = st.builds(
    UML2_Classifier,
    isAbstract=
        st.booleans()
)
UML2_ExtensionPoint_strategy = st.builds(
    UML2_ExtensionPoint,
)
UML2_Transition_strategy = st.builds(
    UML2_Transition,
)
UML2_ActivityNode_strategy = st.builds(
    UML2_ActivityNode,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
UML2_Message_strategy = st.builds(
    UML2_Message,
)
UML2_ActivityPartition_strategy = st.builds(
    UML2_ActivityPartition,
)
UML2_Lifeline_strategy = st.builds(
    UML2_Lifeline,
)
UML2_RedefinableElement_strategy = st.builds(
    UML2_RedefinableElement,
)
UML2_InteractionFragment_strategy = st.builds(
    UML2_InteractionFragment,
)
UML2_DeployedArtifact_strategy = st.builds(
    UML2_DeployedArtifact,
)
UML2_Namespace_strategy = st.builds(
    UML2_Namespace,
)
UML2_MessageEnd_strategy = st.builds(
    UML2_MessageEnd,
)
UML2_TypedElement_strategy = st.builds(
    UML2_TypedElement,
)
UML2_DeploymentTarget_strategy = st.builds(
    UML2_DeploymentTarget,
)
UML2_Include_strategy = st.builds(
    UML2_Include,
)
UML2_Extend_strategy = st.builds(
    UML2_Extend,
)
UML2_ParameterSet_strategy = st.builds(
    UML2_ParameterSet,
)
UML2_Vertex_strategy = st.builds(
    UML2_Vertex,
)
UML2_CollaborationOccurrence_strategy = st.builds(
    UML2_CollaborationOccurrence,
)
UML2_GeneralOrdering_strategy = st.builds(
    UML2_GeneralOrdering,
)
UML2_Trigger_strategy = st.builds(
    UML2_Trigger,
)
InvocationAction_strategy = st.builds(
    InvocationAction,
)
UML2_CallAction_strategy = st.builds(
    UML2_CallAction,
)
UML2_BroadcastSignalAction_strategy = st.builds(
    UML2_BroadcastSignalAction,
)
UML2_SendSignalAction_strategy = st.builds(
    UML2_SendSignalAction,
)
UML2_SendObjectAction_strategy = st.builds(
    UML2_SendObjectAction,
)
Abstraction_strategy = st.builds(
    Abstraction,
)
UML2_Manifestation_strategy = st.builds(
    UML2_Manifestation,
)
UML2_Realization_strategy = st.builds(
    UML2_Realization,
)
MessageTrigger_strategy = st.builds(
    MessageTrigger,
)
UML2_SignalTrigger_strategy = st.builds(
    UML2_SignalTrigger,
)
UML2_CallTrigger_strategy = st.builds(
    UML2_CallTrigger,
)
UML2_AnyTrigger_strategy = st.builds(
    UML2_AnyTrigger,
)
Realization_strategy = st.builds(
    Realization,
)
UML2_Substitution_strategy = st.builds(
    UML2_Substitution,
)
UML2_Implementation_strategy = st.builds(
    UML2_Implementation,
)
Action_strategy = st.builds(
    Action,
)
UML2_VariableAction_strategy = st.builds(
    UML2_VariableAction,
)
UML2_LinkAction_strategy = st.builds(
    UML2_LinkAction,
)
UML2_InvocationAction_strategy = st.builds(
    UML2_InvocationAction,
)
UML2_ClearAssociationAction_strategy = st.builds(
    UML2_ClearAssociationAction,
)
UML2_ReadLinkObjectEndAction_strategy = st.builds(
    UML2_ReadLinkObjectEndAction,
)
UML2_ReplyAction_strategy = st.builds(
    UML2_ReplyAction,
)
UML2_StartOwnedBehaviorAction_strategy = st.builds(
    UML2_StartOwnedBehaviorAction,
)
UML2_CreateObjectAction_strategy = st.builds(
    UML2_CreateObjectAction,
)
UML2_RaiseExceptionAction_strategy = st.builds(
    UML2_RaiseExceptionAction,
)
UML2_ReadExtentAction_strategy = st.builds(
    UML2_ReadExtentAction,
)
UML2_AcceptEventAction_strategy = st.builds(
    UML2_AcceptEventAction,
)
UML2_ReadIsClassifiedObjectAction_strategy = st.builds(
    UML2_ReadIsClassifiedObjectAction,
)
UML2_StructuredActivityNode_strategy = st.builds(
    UML2_StructuredActivityNode,
)
UML2_DestroyObjectAction_strategy = st.builds(
    UML2_DestroyObjectAction,
)
UML2_ReclassifyObjectAction_strategy = st.builds(
    UML2_ReclassifyObjectAction,
)
UML2_ApplyFunctionAction_strategy = st.builds(
    UML2_ApplyFunctionAction,
)
UML2_StructuralFeatureAction_strategy = st.builds(
    UML2_StructuralFeatureAction,
)
LiteralSpecification_strategy = st.builds(
    LiteralSpecification,
)
UML2_LiteralNull_strategy = st.builds(
    UML2_LiteralNull,
)
UML2_LiteralInteger_strategy = st.builds(
    UML2_LiteralInteger,
)
UML2_LiteralUnlimitedNatural_strategy = st.builds(
    UML2_LiteralUnlimitedNatural,
)
UML2_LiteralBoolean_strategy = st.builds(
    UML2_LiteralBoolean,
)
UML2_LiteralString_strategy = st.builds(
    UML2_LiteralString,
)
ActivityNode_strategy = st.builds(
    ActivityNode,
)
UML2_ControlNode_strategy = st.builds(
    UML2_ControlNode,
)
UML2_ExecutableNode_strategy = st.builds(
    UML2_ExecutableNode,
)
ControlNode_strategy = st.builds(
    ControlNode,
)
UML2_DecisionNode_strategy = st.builds(
    UML2_DecisionNode,
)
UML2_MergeNode_strategy = st.builds(
    UML2_MergeNode,
)
UML2_InitialNode_strategy = st.builds(
    UML2_InitialNode,
)
UML2_ForkNode_strategy = st.builds(
    UML2_ForkNode,
)
UML2_JoinNode_strategy = st.builds(
    UML2_JoinNode,
)
UML2_FinalNode_strategy = st.builds(
    UML2_FinalNode,
)
UML2_Association_strategy = st.builds(
    UML2_Association,
)
DeploymentTarget_strategy = st.builds(
    DeploymentTarget,
)
UML2_InstanceSpecification_strategy = st.builds(
    UML2_InstanceSpecification,
)
ConnectableElement_strategy = st.builds(
    ConnectableElement,
)
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
Property_strategy = st.builds(
    Property,
)
UML2_Port_strategy = st.builds(
    UML2_Port,
)
UML2_ExtensionEnd_strategy = st.builds(
    UML2_ExtensionEnd,
)
StructuralFeatureAction_strategy = st.builds(
    StructuralFeatureAction,
)
UML2_ReadStructuralFeatureAction_strategy = st.builds(
    UML2_ReadStructuralFeatureAction,
)
UML2_ClearStructuralFeatureAction_strategy = st.builds(
    UML2_ClearStructuralFeatureAction,
)
UML2_WriteStructuralFeatureAction_strategy = st.builds(
    UML2_WriteStructuralFeatureAction,
)
UML2_ReadLinkObjectEndQualifierAction_strategy = st.builds(
    UML2_ReadLinkObjectEndQualifierAction,
)
UML2_InputPin_strategy = st.builds(
    UML2_InputPin,
)
UML2_TestIdentityAction_strategy = st.builds(
    UML2_TestIdentityAction,
)
Association_strategy = st.builds(
    Association,
)
UML2_CommunicationPath_strategy = st.builds(
    UML2_CommunicationPath,
)
UML2_Extension_strategy = st.builds(
    UML2_Extension,
)
Class_strategy = st.builds(
    Class,
)
UML2_Stereotype_strategy = st.builds(
    UML2_Stereotype,
)
UML2_Component_strategy = st.builds(
    UML2_Component,
)
UML2_Behavior_strategy = st.builds(
    UML2_Behavior,
)
UML2_Node_strategy = st.builds(
    UML2_Node,
)
UML2_AssociationClass_strategy = st.builds(
    UML2_AssociationClass,
)
UML2_OutputPin_strategy = st.builds(
    UML2_OutputPin,
)
UML2_ReadSelfAction_strategy = st.builds(
    UML2_ReadSelfAction,
)
ParameterableElement_strategy = st.builds(
    ParameterableElement,
)
UML2_PackageableElement_strategy = st.builds(
    UML2_PackageableElement,
)
UML2_ConnectableElement_strategy = st.builds(
    UML2_ConnectableElement,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
UML2_StructuralFeature_strategy = st.builds(
    UML2_StructuralFeature,
    isReadOnly=
        st.booleans()
)
UML2_Parameter_strategy = st.builds(
    UML2_Parameter,
    direction=
        safe_text
)
UML2_Variable_strategy = st.builds(
    UML2_Variable,
)
UML2_ObjectNode_strategy = st.builds(
    UML2_ObjectNode,
)
UML2_Operation_strategy = st.builds(
    UML2_Operation,
)
UML2_ValueSpecification_strategy = st.builds(
    UML2_ValueSpecification,
)
BehavioredClassifier_strategy = st.builds(
    BehavioredClassifier,
)
UML2_Collaboration_strategy = st.builds(
    UML2_Collaboration,
)
UML2_Class_strategy = st.builds(
    UML2_Class,
    isActive=
        st.booleans()
)
UML2_UseCase_strategy = st.builds(
    UML2_UseCase,
)
ValueSpecification_strategy = st.builds(
    ValueSpecification,
)
UML2_InstanceValue_strategy = st.builds(
    UML2_InstanceValue,
)
UML2_LiteralSpecification_strategy = st.builds(
    UML2_LiteralSpecification,
)
UML2_Duration_strategy = st.builds(
    UML2_Duration,
)
UML2_OpaqueExpression_strategy = st.builds(
    UML2_OpaqueExpression,
)
UML2_TimeExpression_strategy = st.builds(
    UML2_TimeExpression,
)
UML2_Interval_strategy = st.builds(
    UML2_Interval,
)
CreateLinkAction_strategy = st.builds(
    CreateLinkAction,
)
UML2_CreateLinkObjectAction_strategy = st.builds(
    UML2_CreateLinkObjectAction,
)
UML2_Property_strategy = st.builds(
    UML2_Property,
    aggregation=
        safe_text,
    isDerivedUnion=
        st.booleans(),
    isComposite=
        st.booleans(),
    isDerived=
        st.booleans()
)
Element_strategy = st.builds(
    Element,
)
UML2_TemplateParameter_strategy = st.builds(
    UML2_TemplateParameter,
)
UML2_ActivityGroup_strategy = st.builds(
    UML2_ActivityGroup,
)
UML2_Clause_strategy = st.builds(
    UML2_Clause,
)
UML2_MultiplicityElement_strategy = st.builds(
    UML2_MultiplicityElement,
    upper=
        safe_text,
    lower=
        st.integers(),
    isOrdered=
        st.booleans(),
    isUnique=
        st.booleans()
)
UML2_ParameterableElement_strategy = st.builds(
    UML2_ParameterableElement,
)
UML2_Slot_strategy = st.builds(
    UML2_Slot,
)
UML2_LinkEndData_strategy = st.builds(
    UML2_LinkEndData,
)
UML2_TemplateableElement_strategy = st.builds(
    UML2_TemplateableElement,
)
UML2_TemplateSignature_strategy = st.builds(
    UML2_TemplateSignature,
)
UML2_ExceptionHandler_strategy = st.builds(
    UML2_ExceptionHandler,
)
UML2_TemplateParameterSubstitution_strategy = st.builds(
    UML2_TemplateParameterSubstitution,
)
UML2_Relationship_strategy = st.builds(
    UML2_Relationship,
)
UML2_QualifierValue_strategy = st.builds(
    UML2_QualifierValue,
)

@given(instance=Trigger_strategy)
@settings(max_examples=50)
def test_trigger_instantiation(instance):
    assert isinstance(instance, Trigger)

@given(instance=UML2_TimeTrigger_strategy)
@settings(max_examples=50)
def test_uml2_timetrigger_instantiation(instance):
    assert isinstance(instance, UML2_TimeTrigger)

@given(instance=FinalNode_strategy)
@settings(max_examples=50)
def test_finalnode_instantiation(instance):
    assert isinstance(instance, FinalNode)

@given(instance=UML2_ActivityFinalNode_strategy)
@settings(max_examples=50)
def test_uml2_activityfinalnode_instantiation(instance):
    assert isinstance(instance, UML2_ActivityFinalNode)

@given(instance=MessageEnd_strategy)
@settings(max_examples=50)
def test_messageend_instantiation(instance):
    assert isinstance(instance, MessageEnd)

@given(instance=InteractionFragment_strategy)
@settings(max_examples=50)
def test_interactionfragment_instantiation(instance):
    assert isinstance(instance, InteractionFragment)

@given(instance=UML2_EventOccurrence_strategy)
@settings(max_examples=50)
def test_uml2_eventoccurrence_instantiation(instance):
    assert isinstance(instance, UML2_EventOccurrence)

@given(instance=UML2_Continuation_strategy)
@settings(max_examples=50)
def test_uml2_continuation_instantiation(instance):
    assert isinstance(instance, UML2_Continuation)

@given(instance=DeployedArtifact_strategy)
@settings(max_examples=50)
def test_deployedartifact_instantiation(instance):
    assert isinstance(instance, DeployedArtifact)

@given(instance=Relationship_strategy)
@settings(max_examples=50)
def test_relationship_instantiation(instance):
    assert isinstance(instance, Relationship)

@given(instance=UML2_DirectedRelationship_strategy)
@settings(max_examples=50)
def test_uml2_directedrelationship_instantiation(instance):
    assert isinstance(instance, UML2_DirectedRelationship)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=UML2_PrimitiveType_strategy)
@settings(max_examples=50)
def test_uml2_primitivetype_instantiation(instance):
    assert isinstance(instance, UML2_PrimitiveType)

@given(instance=InstanceSpecification_strategy)
@settings(max_examples=50)
def test_instancespecification_instantiation(instance):
    assert isinstance(instance, InstanceSpecification)

@given(instance=UML2_EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_uml2_enumerationliteral_instantiation(instance):
    assert isinstance(instance, UML2_EnumerationLiteral)

@given(instance=Artifact_strategy)
@settings(max_examples=50)
def test_artifact_instantiation(instance):
    assert isinstance(instance, Artifact)

@given(instance=UML2_DeploymentSpecification_strategy)
@settings(max_examples=50)
def test_uml2_deploymentspecification_instantiation(instance):
    assert isinstance(instance, UML2_DeploymentSpecification)

@given(instance=TemplateableElement_strategy)
@settings(max_examples=50)
def test_templateableelement_instantiation(instance):
    assert isinstance(instance, TemplateableElement)

@given(instance=UML2_NamedElement_strategy)
@settings(max_examples=50)
def test_uml2_namedelement_instantiation(instance):
    assert isinstance(instance, UML2_NamedElement)



@given(instance=UML2_NamedElement_strategy)
def test_uml2_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=UML2_NamedElement_strategy)
def test_uml2_namedelement_visibility_setter(instance):
    original = instance.visibility
    instance.visibility = original
    assert instance.visibility == original

@given(instance=InputPin_strategy)
@settings(max_examples=50)
def test_inputpin_instantiation(instance):
    assert isinstance(instance, InputPin)

@given(instance=UML2_ValuePin_strategy)
@settings(max_examples=50)
def test_uml2_valuepin_instantiation(instance):
    assert isinstance(instance, UML2_ValuePin)

@given(instance=Interval_strategy)
@settings(max_examples=50)
def test_interval_instantiation(instance):
    assert isinstance(instance, Interval)

@given(instance=UML2_TimeInterval_strategy)
@settings(max_examples=50)
def test_uml2_timeinterval_instantiation(instance):
    assert isinstance(instance, UML2_TimeInterval)

@given(instance=StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_structuredactivitynode_instantiation(instance):
    assert isinstance(instance, StructuredActivityNode)

@given(instance=UML2_ExpansionRegion_strategy)
@settings(max_examples=50)
def test_uml2_expansionregion_instantiation(instance):
    assert isinstance(instance, UML2_ExpansionRegion)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=WriteVariableAction_strategy)
@settings(max_examples=50)
def test_writevariableaction_instantiation(instance):
    assert isinstance(instance, WriteVariableAction)

@given(instance=UML2_RemoveVariableValueAction_strategy)
@settings(max_examples=50)
def test_uml2_removevariablevalueaction_instantiation(instance):
    assert isinstance(instance, UML2_RemoveVariableValueAction)

@given(instance=TemplateSignature_strategy)
@settings(max_examples=50)
def test_templatesignature_instantiation(instance):
    assert isinstance(instance, TemplateSignature)

@given(instance=DirectedRelationship_strategy)
@settings(max_examples=50)
def test_directedrelationship_instantiation(instance):
    assert isinstance(instance, DirectedRelationship)

@given(instance=EncapsulatedClassifier_strategy)
@settings(max_examples=50)
def test_encapsulatedclassifier_instantiation(instance):
    assert isinstance(instance, EncapsulatedClassifier)

@given(instance=OpaqueExpression_strategy)
@settings(max_examples=50)
def test_opaqueexpression_instantiation(instance):
    assert isinstance(instance, OpaqueExpression)

@given(instance=UML2_Expression_strategy)
@settings(max_examples=50)
def test_uml2_expression_instantiation(instance):
    assert isinstance(instance, UML2_Expression)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=UML2_ProtocolTransition_strategy)
@settings(max_examples=50)
def test_uml2_protocoltransition_instantiation(instance):
    assert isinstance(instance, UML2_ProtocolTransition)

@given(instance=TemplateParameter_strategy)
@settings(max_examples=50)
def test_templateparameter_instantiation(instance):
    assert isinstance(instance, TemplateParameter)

@given(instance=UML2_ConnectableElementTemplateParameter_strategy)
@settings(max_examples=50)
def test_uml2_connectableelementtemplateparameter_instantiation(instance):
    assert isinstance(instance, UML2_ConnectableElementTemplateParameter)

@given(instance=UML2_OperationTemplateParameter_strategy)
@settings(max_examples=50)
def test_uml2_operationtemplateparameter_instantiation(instance):
    assert isinstance(instance, UML2_OperationTemplateParameter)

@given(instance=UML2_ClassifierTemplateParameter_strategy)
@settings(max_examples=50)
def test_uml2_classifiertemplateparameter_instantiation(instance):
    assert isinstance(instance, UML2_ClassifierTemplateParameter)

@given(instance=Package_strategy)
@settings(max_examples=50)
def test_package_instantiation(instance):
    assert isinstance(instance, Package)

@given(instance=UML2_Profile_strategy)
@settings(max_examples=50)
def test_uml2_profile_instantiation(instance):
    assert isinstance(instance, UML2_Profile)

@given(instance=UML2_Model_strategy)
@settings(max_examples=50)
def test_uml2_model_instantiation(instance):
    assert isinstance(instance, UML2_Model)

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=UML2_IntervalConstraint_strategy)
@settings(max_examples=50)
def test_uml2_intervalconstraint_instantiation(instance):
    assert isinstance(instance, UML2_IntervalConstraint)

@given(instance=AcceptEventAction_strategy)
@settings(max_examples=50)
def test_accepteventaction_instantiation(instance):
    assert isinstance(instance, AcceptEventAction)

@given(instance=UML2_AcceptCallAction_strategy)
@settings(max_examples=50)
def test_uml2_acceptcallaction_instantiation(instance):
    assert isinstance(instance, UML2_AcceptCallAction)

@given(instance=StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_instantiation(instance):
    assert isinstance(instance, StateMachine)

@given(instance=UML2_ProtocolStateMachine_strategy)
@settings(max_examples=50)
def test_uml2_protocolstatemachine_instantiation(instance):
    assert isinstance(instance, UML2_ProtocolStateMachine)

@given(instance=UML2_StateInvariant_strategy)
@settings(max_examples=50)
def test_uml2_stateinvariant_instantiation(instance):
    assert isinstance(instance, UML2_StateInvariant)

@given(instance=UML2_Comment_strategy)
@settings(max_examples=50)
def test_uml2_comment_instantiation(instance):
    assert isinstance(instance, UML2_Comment)

@given(instance=UML2_CombinedFragment_strategy)
@settings(max_examples=50)
def test_uml2_combinedfragment_instantiation(instance):
    assert isinstance(instance, UML2_CombinedFragment)

@given(instance=UML2_InteractionOccurrence_strategy)
@settings(max_examples=50)
def test_uml2_interactionoccurrence_instantiation(instance):
    assert isinstance(instance, UML2_InteractionOccurrence)

@given(instance=UML2_PackageMerge_strategy)
@settings(max_examples=50)
def test_uml2_packagemerge_instantiation(instance):
    assert isinstance(instance, UML2_PackageMerge)

@given(instance=UML2_ExecutionOccurrence_strategy)
@settings(max_examples=50)
def test_uml2_executionoccurrence_instantiation(instance):
    assert isinstance(instance, UML2_ExecutionOccurrence)

@given(instance=InteractionOccurrence_strategy)
@settings(max_examples=50)
def test_interactionoccurrence_instantiation(instance):
    assert isinstance(instance, InteractionOccurrence)

@given(instance=UML2_PartDecomposition_strategy)
@settings(max_examples=50)
def test_uml2_partdecomposition_instantiation(instance):
    assert isinstance(instance, UML2_PartDecomposition)

@given(instance=UML2_AddVariableValueAction_strategy)
@settings(max_examples=50)
def test_uml2_addvariablevalueaction_instantiation(instance):
    assert isinstance(instance, UML2_AddVariableValueAction)

@given(instance=UML2_ElementImport_strategy)
@settings(max_examples=50)
def test_uml2_elementimport_instantiation(instance):
    assert isinstance(instance, UML2_ElementImport)

@given(instance=UML2_FlowFinalNode_strategy)
@settings(max_examples=50)
def test_uml2_flowfinalnode_instantiation(instance):
    assert isinstance(instance, UML2_FlowFinalNode)

@given(instance=UML2_DurationInterval_strategy)
@settings(max_examples=50)
def test_uml2_durationinterval_instantiation(instance):
    assert isinstance(instance, UML2_DurationInterval)

@given(instance=UML2_ChangeTrigger_strategy)
@settings(max_examples=50)
def test_uml2_changetrigger_instantiation(instance):
    assert isinstance(instance, UML2_ChangeTrigger)

@given(instance=CallAction_strategy)
@settings(max_examples=50)
def test_callaction_instantiation(instance):
    assert isinstance(instance, CallAction)

@given(instance=UML2_CallBehaviorAction_strategy)
@settings(max_examples=50)
def test_uml2_callbehavioraction_instantiation(instance):
    assert isinstance(instance, UML2_CallBehaviorAction)

@given(instance=UML2_CallOperationAction_strategy)
@settings(max_examples=50)
def test_uml2_calloperationaction_instantiation(instance):
    assert isinstance(instance, UML2_CallOperationAction)

@given(instance=UML2_MessageTrigger_strategy)
@settings(max_examples=50)
def test_uml2_messagetrigger_instantiation(instance):
    assert isinstance(instance, UML2_MessageTrigger)

@given(instance=UML2_Gate_strategy)
@settings(max_examples=50)
def test_uml2_gate_instantiation(instance):
    assert isinstance(instance, UML2_Gate)

@given(instance=UML2_Enumeration_strategy)
@settings(max_examples=50)
def test_uml2_enumeration_instantiation(instance):
    assert isinstance(instance, UML2_Enumeration)

@given(instance=UML2_ProtocolConformance_strategy)
@settings(max_examples=50)
def test_uml2_protocolconformance_instantiation(instance):
    assert isinstance(instance, UML2_ProtocolConformance)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=UML2_FinalState_strategy)
@settings(max_examples=50)
def test_uml2_finalstate_instantiation(instance):
    assert isinstance(instance, UML2_FinalState)

@given(instance=UML2_StringExpression_strategy)
@settings(max_examples=50)
def test_uml2_stringexpression_instantiation(instance):
    assert isinstance(instance, UML2_StringExpression)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=UML2_Device_strategy)
@settings(max_examples=50)
def test_uml2_device_instantiation(instance):
    assert isinstance(instance, UML2_Device)

@given(instance=UML2_ExecutionEnvironment_strategy)
@settings(max_examples=50)
def test_uml2_executionenvironment_instantiation(instance):
    assert isinstance(instance, UML2_ExecutionEnvironment)

@given(instance=UML2_PackageImport_strategy)
@settings(max_examples=50)
def test_uml2_packageimport_instantiation(instance):
    assert isinstance(instance, UML2_PackageImport)

@given(instance=BehavioralFeature_strategy)
@settings(max_examples=50)
def test_behavioralfeature_instantiation(instance):
    assert isinstance(instance, BehavioralFeature)

@given(instance=UML2_Reception_strategy)
@settings(max_examples=50)
def test_uml2_reception_instantiation(instance):
    assert isinstance(instance, UML2_Reception)

@given(instance=ActivityEdge_strategy)
@settings(max_examples=50)
def test_activityedge_instantiation(instance):
    assert isinstance(instance, ActivityEdge)

@given(instance=UML2_ObjectFlow_strategy)
@settings(max_examples=50)
def test_uml2_objectflow_instantiation(instance):
    assert isinstance(instance, UML2_ObjectFlow)

@given(instance=UML2_ControlFlow_strategy)
@settings(max_examples=50)
def test_uml2_controlflow_instantiation(instance):
    assert isinstance(instance, UML2_ControlFlow)

@given(instance=LinkEndData_strategy)
@settings(max_examples=50)
def test_linkenddata_instantiation(instance):
    assert isinstance(instance, LinkEndData)

@given(instance=UML2_LinkEndCreationData_strategy)
@settings(max_examples=50)
def test_uml2_linkendcreationdata_instantiation(instance):
    assert isinstance(instance, UML2_LinkEndCreationData)

@given(instance=UML2_InteractionConstraint_strategy)
@settings(max_examples=50)
def test_uml2_interactionconstraint_instantiation(instance):
    assert isinstance(instance, UML2_InteractionConstraint)

@given(instance=ExecutableNode_strategy)
@settings(max_examples=50)
def test_executablenode_instantiation(instance):
    assert isinstance(instance, ExecutableNode)

@given(instance=UML2_Action_strategy)
@settings(max_examples=50)
def test_uml2_action_instantiation(instance):
    assert isinstance(instance, UML2_Action)

@given(instance=UML2_LoopNode_strategy)
@settings(max_examples=50)
def test_uml2_loopnode_instantiation(instance):
    assert isinstance(instance, UML2_LoopNode)

@given(instance=UML2_ConditionalNode_strategy)
@settings(max_examples=50)
def test_uml2_conditionalnode_instantiation(instance):
    assert isinstance(instance, UML2_ConditionalNode)

@given(instance=PackageImport_strategy)
@settings(max_examples=50)
def test_packageimport_instantiation(instance):
    assert isinstance(instance, PackageImport)

@given(instance=UML2_ProfileApplication_strategy)
@settings(max_examples=50)
def test_uml2_profileapplication_instantiation(instance):
    assert isinstance(instance, UML2_ProfileApplication)

@given(instance=UML2_TemplateBinding_strategy)
@settings(max_examples=50)
def test_uml2_templatebinding_instantiation(instance):
    assert isinstance(instance, UML2_TemplateBinding)

@given(instance=VariableAction_strategy)
@settings(max_examples=50)
def test_variableaction_instantiation(instance):
    assert isinstance(instance, VariableAction)

@given(instance=UML2_WriteVariableAction_strategy)
@settings(max_examples=50)
def test_uml2_writevariableaction_instantiation(instance):
    assert isinstance(instance, UML2_WriteVariableAction)

@given(instance=UML2_ReadVariableAction_strategy)
@settings(max_examples=50)
def test_uml2_readvariableaction_instantiation(instance):
    assert isinstance(instance, UML2_ReadVariableAction)

@given(instance=UML2_ClearVariableAction_strategy)
@settings(max_examples=50)
def test_uml2_clearvariableaction_instantiation(instance):
    assert isinstance(instance, UML2_ClearVariableAction)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=UML2_Connector_strategy)
@settings(max_examples=50)
def test_uml2_connector_instantiation(instance):
    assert isinstance(instance, UML2_Connector)

@given(instance=UML2_Generalization_strategy)
@settings(max_examples=50)
def test_uml2_generalization_instantiation(instance):
    assert isinstance(instance, UML2_Generalization)

@given(instance=PackageableElement_strategy)
@settings(max_examples=50)
def test_packageableelement_instantiation(instance):
    assert isinstance(instance, PackageableElement)

@given(instance=UML2_Constraint_strategy)
@settings(max_examples=50)
def test_uml2_constraint_instantiation(instance):
    assert isinstance(instance, UML2_Constraint)

@given(instance=UML2_Dependency_strategy)
@settings(max_examples=50)
def test_uml2_dependency_instantiation(instance):
    assert isinstance(instance, UML2_Dependency)

@given(instance=UML2_Type_strategy)
@settings(max_examples=50)
def test_uml2_type_instantiation(instance):
    assert isinstance(instance, UML2_Type)

@given(instance=UML2_InformationFlow_strategy)
@settings(max_examples=50)
def test_uml2_informationflow_instantiation(instance):
    assert isinstance(instance, UML2_InformationFlow)

@given(instance=UML2_GeneralizationSet_strategy)
@settings(max_examples=50)
def test_uml2_generalizationset_instantiation(instance):
    assert isinstance(instance, UML2_GeneralizationSet)

@given(instance=UML2_PrimitiveFunction_strategy)
@settings(max_examples=50)
def test_uml2_primitivefunction_instantiation(instance):
    assert isinstance(instance, UML2_PrimitiveFunction)

@given(instance=WriteLinkAction_strategy)
@settings(max_examples=50)
def test_writelinkaction_instantiation(instance):
    assert isinstance(instance, WriteLinkAction)

@given(instance=UML2_DestroyLinkAction_strategy)
@settings(max_examples=50)
def test_uml2_destroylinkaction_instantiation(instance):
    assert isinstance(instance, UML2_DestroyLinkAction)

@given(instance=UML2_CreateLinkAction_strategy)
@settings(max_examples=50)
def test_uml2_createlinkaction_instantiation(instance):
    assert isinstance(instance, UML2_CreateLinkAction)

@given(instance=MultiplicityElement_strategy)
@settings(max_examples=50)
def test_multiplicityelement_instantiation(instance):
    assert isinstance(instance, MultiplicityElement)

@given(instance=UML2_ConnectorEnd_strategy)
@settings(max_examples=50)
def test_uml2_connectorend_instantiation(instance):
    assert isinstance(instance, UML2_ConnectorEnd)

@given(instance=ObjectNode_strategy)
@settings(max_examples=50)
def test_objectnode_instantiation(instance):
    assert isinstance(instance, ObjectNode)

@given(instance=UML2_ActivityParameterNode_strategy)
@settings(max_examples=50)
def test_uml2_activityparameternode_instantiation(instance):
    assert isinstance(instance, UML2_ActivityParameterNode)

@given(instance=UML2_CentralBufferNode_strategy)
@settings(max_examples=50)
def test_uml2_centralbuffernode_instantiation(instance):
    assert isinstance(instance, UML2_CentralBufferNode)

@given(instance=UML2_ExpansionNode_strategy)
@settings(max_examples=50)
def test_uml2_expansionnode_instantiation(instance):
    assert isinstance(instance, UML2_ExpansionNode)

@given(instance=UML2_Pin_strategy)
@settings(max_examples=50)
def test_uml2_pin_instantiation(instance):
    assert isinstance(instance, UML2_Pin)

@given(instance=StructuredClassifier_strategy)
@settings(max_examples=50)
def test_structuredclassifier_instantiation(instance):
    assert isinstance(instance, StructuredClassifier)

@given(instance=UML2_EncapsulatedClassifier_strategy)
@settings(max_examples=50)
def test_uml2_encapsulatedclassifier_instantiation(instance):
    assert isinstance(instance, UML2_EncapsulatedClassifier)

@given(instance=IntervalConstraint_strategy)
@settings(max_examples=50)
def test_intervalconstraint_instantiation(instance):
    assert isinstance(instance, IntervalConstraint)

@given(instance=UML2_TimeConstraint_strategy)
@settings(max_examples=50)
def test_uml2_timeconstraint_instantiation(instance):
    assert isinstance(instance, UML2_TimeConstraint)

@given(instance=UML2_DurationConstraint_strategy)
@settings(max_examples=50)
def test_uml2_durationconstraint_instantiation(instance):
    assert isinstance(instance, UML2_DurationConstraint)

@given(instance=EventOccurrence_strategy)
@settings(max_examples=50)
def test_eventoccurrence_instantiation(instance):
    assert isinstance(instance, EventOccurrence)

@given(instance=UML2_Stop_strategy)
@settings(max_examples=50)
def test_uml2_stop_instantiation(instance):
    assert isinstance(instance, UML2_Stop)

@given(instance=LinkAction_strategy)
@settings(max_examples=50)
def test_linkaction_instantiation(instance):
    assert isinstance(instance, LinkAction)

@given(instance=UML2_WriteLinkAction_strategy)
@settings(max_examples=50)
def test_uml2_writelinkaction_instantiation(instance):
    assert isinstance(instance, UML2_WriteLinkAction)

@given(instance=UML2_ReadLinkAction_strategy)
@settings(max_examples=50)
def test_uml2_readlinkaction_instantiation(instance):
    assert isinstance(instance, UML2_ReadLinkAction)

@given(instance=Dependency_strategy)
@settings(max_examples=50)
def test_dependency_instantiation(instance):
    assert isinstance(instance, Dependency)

@given(instance=UML2_Deployment_strategy)
@settings(max_examples=50)
def test_uml2_deployment_instantiation(instance):
    assert isinstance(instance, UML2_Deployment)

@given(instance=UML2_Usage_strategy)
@settings(max_examples=50)
def test_uml2_usage_instantiation(instance):
    assert isinstance(instance, UML2_Usage)

@given(instance=UML2_Abstraction_strategy)
@settings(max_examples=50)
def test_uml2_abstraction_instantiation(instance):
    assert isinstance(instance, UML2_Abstraction)

@given(instance=UML2_Permission_strategy)
@settings(max_examples=50)
def test_uml2_permission_instantiation(instance):
    assert isinstance(instance, UML2_Permission)

@given(instance=Pin_strategy)
@settings(max_examples=50)
def test_pin_instantiation(instance):
    assert isinstance(instance, Pin)

@given(instance=ActivityGroup_strategy)
@settings(max_examples=50)
def test_activitygroup_instantiation(instance):
    assert isinstance(instance, ActivityGroup)

@given(instance=UML2_InterruptibleActivityRegion_strategy)
@settings(max_examples=50)
def test_uml2_interruptibleactivityregion_instantiation(instance):
    assert isinstance(instance, UML2_InterruptibleActivityRegion)

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=UML2_Pseudostate_strategy)
@settings(max_examples=50)
def test_uml2_pseudostate_instantiation(instance):
    assert isinstance(instance, UML2_Pseudostate)

@given(instance=UML2_ConnectionPointReference_strategy)
@settings(max_examples=50)
def test_uml2_connectionpointreference_instantiation(instance):
    assert isinstance(instance, UML2_ConnectionPointReference)

@given(instance=Namespace_strategy)
@settings(max_examples=50)
def test_namespace_instantiation(instance):
    assert isinstance(instance, Namespace)

@given(instance=UML2_Package_strategy)
@settings(max_examples=50)
def test_uml2_package_instantiation(instance):
    assert isinstance(instance, UML2_Package)

@given(instance=UML2_BehavioralFeature_strategy)
@settings(max_examples=50)
def test_uml2_behavioralfeature_instantiation(instance):
    assert isinstance(instance, UML2_BehavioralFeature)

@given(instance=UML2_InteractionOperand_strategy)
@settings(max_examples=50)
def test_uml2_interactionoperand_instantiation(instance):
    assert isinstance(instance, UML2_InteractionOperand)

@given(instance=CentralBufferNode_strategy)
@settings(max_examples=50)
def test_centralbuffernode_instantiation(instance):
    assert isinstance(instance, CentralBufferNode)

@given(instance=UML2_DataStoreNode_strategy)
@settings(max_examples=50)
def test_uml2_datastorenode_instantiation(instance):
    assert isinstance(instance, UML2_DataStoreNode)

@given(instance=WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, WriteStructuralFeatureAction)

@given(instance=UML2_RemoveStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_uml2_removestructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, UML2_RemoveStructuralFeatureValueAction)

@given(instance=UML2_DurationObservationAction_strategy)
@settings(max_examples=50)
def test_uml2_durationobservationaction_instantiation(instance):
    assert isinstance(instance, UML2_DurationObservationAction)

@given(instance=UML2_TimeObservationAction_strategy)
@settings(max_examples=50)
def test_uml2_timeobservationaction_instantiation(instance):
    assert isinstance(instance, UML2_TimeObservationAction)

@given(instance=UML2_AddStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_uml2_addstructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, UML2_AddStructuralFeatureValueAction)

@given(instance=UML2_Element_strategy)
@settings(max_examples=50)
def test_uml2_element_instantiation(instance):
    assert isinstance(instance, UML2_Element)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=UML2_StructuredClassifier_strategy)
@settings(max_examples=50)
def test_uml2_structuredclassifier_instantiation(instance):
    assert isinstance(instance, UML2_StructuredClassifier)

@given(instance=UML2_Artifact_strategy)
@settings(max_examples=50)
def test_uml2_artifact_instantiation(instance):
    assert isinstance(instance, UML2_Artifact)

@given(instance=UML2_BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_uml2_behavioredclassifier_instantiation(instance):
    assert isinstance(instance, UML2_BehavioredClassifier)

@given(instance=UML2_InformationItem_strategy)
@settings(max_examples=50)
def test_uml2_informationitem_instantiation(instance):
    assert isinstance(instance, UML2_InformationItem)

@given(instance=UML2_TemplateableClassifier_strategy)
@settings(max_examples=50)
def test_uml2_templateableclassifier_instantiation(instance):
    assert isinstance(instance, UML2_TemplateableClassifier)

@given(instance=UML2_Interface_strategy)
@settings(max_examples=50)
def test_uml2_interface_instantiation(instance):
    assert isinstance(instance, UML2_Interface)

@given(instance=UML2_Actor_strategy)
@settings(max_examples=50)
def test_uml2_actor_instantiation(instance):
    assert isinstance(instance, UML2_Actor)

@given(instance=UML2_DataType_strategy)
@settings(max_examples=50)
def test_uml2_datatype_instantiation(instance):
    assert isinstance(instance, UML2_DataType)

@given(instance=UML2_Signal_strategy)
@settings(max_examples=50)
def test_uml2_signal_instantiation(instance):
    assert isinstance(instance, UML2_Signal)

@given(instance=UML2_ParameterableClassifier_strategy)
@settings(max_examples=50)
def test_uml2_parameterableclassifier_instantiation(instance):
    assert isinstance(instance, UML2_ParameterableClassifier)

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=UML2_StateMachine_strategy)
@settings(max_examples=50)
def test_uml2_statemachine_instantiation(instance):
    assert isinstance(instance, UML2_StateMachine)

@given(instance=UML2_Interaction_strategy)
@settings(max_examples=50)
def test_uml2_interaction_instantiation(instance):
    assert isinstance(instance, UML2_Interaction)

@given(instance=UML2_Activity_strategy)
@settings(max_examples=50)
def test_uml2_activity_instantiation(instance):
    assert isinstance(instance, UML2_Activity)

@given(instance=RedefinableElement_strategy)
@settings(max_examples=50)
def test_redefinableelement_instantiation(instance):
    assert isinstance(instance, RedefinableElement)

@given(instance=UML2_Feature_strategy)
@settings(max_examples=50)
def test_uml2_feature_instantiation(instance):
    assert isinstance(instance, UML2_Feature)



@given(instance=UML2_Feature_strategy)
def test_uml2_feature_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original

@given(instance=UML2_State_strategy)
@settings(max_examples=50)
def test_uml2_state_instantiation(instance):
    assert isinstance(instance, UML2_State)

@given(instance=UML2_ActivityEdge_strategy)
@settings(max_examples=50)
def test_uml2_activityedge_instantiation(instance):
    assert isinstance(instance, UML2_ActivityEdge)

@given(instance=UML2_Region_strategy)
@settings(max_examples=50)
def test_uml2_region_instantiation(instance):
    assert isinstance(instance, UML2_Region)

@given(instance=UML2_RedefinableTemplateSignature_strategy)
@settings(max_examples=50)
def test_uml2_redefinabletemplatesignature_instantiation(instance):
    assert isinstance(instance, UML2_RedefinableTemplateSignature)

@given(instance=UML2_Classifier_strategy)
@settings(max_examples=50)
def test_uml2_classifier_instantiation(instance):
    assert isinstance(instance, UML2_Classifier)



@given(instance=UML2_Classifier_strategy)
def test_uml2_classifier_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=UML2_ExtensionPoint_strategy)
@settings(max_examples=50)
def test_uml2_extensionpoint_instantiation(instance):
    assert isinstance(instance, UML2_ExtensionPoint)

@given(instance=UML2_Transition_strategy)
@settings(max_examples=50)
def test_uml2_transition_instantiation(instance):
    assert isinstance(instance, UML2_Transition)

@given(instance=UML2_ActivityNode_strategy)
@settings(max_examples=50)
def test_uml2_activitynode_instantiation(instance):
    assert isinstance(instance, UML2_ActivityNode)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=UML2_Message_strategy)
@settings(max_examples=50)
def test_uml2_message_instantiation(instance):
    assert isinstance(instance, UML2_Message)

@given(instance=UML2_ActivityPartition_strategy)
@settings(max_examples=50)
def test_uml2_activitypartition_instantiation(instance):
    assert isinstance(instance, UML2_ActivityPartition)

@given(instance=UML2_Lifeline_strategy)
@settings(max_examples=50)
def test_uml2_lifeline_instantiation(instance):
    assert isinstance(instance, UML2_Lifeline)

@given(instance=UML2_RedefinableElement_strategy)
@settings(max_examples=50)
def test_uml2_redefinableelement_instantiation(instance):
    assert isinstance(instance, UML2_RedefinableElement)

@given(instance=UML2_InteractionFragment_strategy)
@settings(max_examples=50)
def test_uml2_interactionfragment_instantiation(instance):
    assert isinstance(instance, UML2_InteractionFragment)

@given(instance=UML2_DeployedArtifact_strategy)
@settings(max_examples=50)
def test_uml2_deployedartifact_instantiation(instance):
    assert isinstance(instance, UML2_DeployedArtifact)

@given(instance=UML2_Namespace_strategy)
@settings(max_examples=50)
def test_uml2_namespace_instantiation(instance):
    assert isinstance(instance, UML2_Namespace)

@given(instance=UML2_MessageEnd_strategy)
@settings(max_examples=50)
def test_uml2_messageend_instantiation(instance):
    assert isinstance(instance, UML2_MessageEnd)

@given(instance=UML2_TypedElement_strategy)
@settings(max_examples=50)
def test_uml2_typedelement_instantiation(instance):
    assert isinstance(instance, UML2_TypedElement)

@given(instance=UML2_DeploymentTarget_strategy)
@settings(max_examples=50)
def test_uml2_deploymenttarget_instantiation(instance):
    assert isinstance(instance, UML2_DeploymentTarget)

@given(instance=UML2_Include_strategy)
@settings(max_examples=50)
def test_uml2_include_instantiation(instance):
    assert isinstance(instance, UML2_Include)

@given(instance=UML2_Extend_strategy)
@settings(max_examples=50)
def test_uml2_extend_instantiation(instance):
    assert isinstance(instance, UML2_Extend)

@given(instance=UML2_ParameterSet_strategy)
@settings(max_examples=50)
def test_uml2_parameterset_instantiation(instance):
    assert isinstance(instance, UML2_ParameterSet)

@given(instance=UML2_Vertex_strategy)
@settings(max_examples=50)
def test_uml2_vertex_instantiation(instance):
    assert isinstance(instance, UML2_Vertex)

@given(instance=UML2_CollaborationOccurrence_strategy)
@settings(max_examples=50)
def test_uml2_collaborationoccurrence_instantiation(instance):
    assert isinstance(instance, UML2_CollaborationOccurrence)

@given(instance=UML2_GeneralOrdering_strategy)
@settings(max_examples=50)
def test_uml2_generalordering_instantiation(instance):
    assert isinstance(instance, UML2_GeneralOrdering)

@given(instance=UML2_Trigger_strategy)
@settings(max_examples=50)
def test_uml2_trigger_instantiation(instance):
    assert isinstance(instance, UML2_Trigger)

@given(instance=InvocationAction_strategy)
@settings(max_examples=50)
def test_invocationaction_instantiation(instance):
    assert isinstance(instance, InvocationAction)

@given(instance=UML2_CallAction_strategy)
@settings(max_examples=50)
def test_uml2_callaction_instantiation(instance):
    assert isinstance(instance, UML2_CallAction)

@given(instance=UML2_BroadcastSignalAction_strategy)
@settings(max_examples=50)
def test_uml2_broadcastsignalaction_instantiation(instance):
    assert isinstance(instance, UML2_BroadcastSignalAction)

@given(instance=UML2_SendSignalAction_strategy)
@settings(max_examples=50)
def test_uml2_sendsignalaction_instantiation(instance):
    assert isinstance(instance, UML2_SendSignalAction)

@given(instance=UML2_SendObjectAction_strategy)
@settings(max_examples=50)
def test_uml2_sendobjectaction_instantiation(instance):
    assert isinstance(instance, UML2_SendObjectAction)

@given(instance=Abstraction_strategy)
@settings(max_examples=50)
def test_abstraction_instantiation(instance):
    assert isinstance(instance, Abstraction)

@given(instance=UML2_Manifestation_strategy)
@settings(max_examples=50)
def test_uml2_manifestation_instantiation(instance):
    assert isinstance(instance, UML2_Manifestation)

@given(instance=UML2_Realization_strategy)
@settings(max_examples=50)
def test_uml2_realization_instantiation(instance):
    assert isinstance(instance, UML2_Realization)

@given(instance=MessageTrigger_strategy)
@settings(max_examples=50)
def test_messagetrigger_instantiation(instance):
    assert isinstance(instance, MessageTrigger)

@given(instance=UML2_SignalTrigger_strategy)
@settings(max_examples=50)
def test_uml2_signaltrigger_instantiation(instance):
    assert isinstance(instance, UML2_SignalTrigger)

@given(instance=UML2_CallTrigger_strategy)
@settings(max_examples=50)
def test_uml2_calltrigger_instantiation(instance):
    assert isinstance(instance, UML2_CallTrigger)

@given(instance=UML2_AnyTrigger_strategy)
@settings(max_examples=50)
def test_uml2_anytrigger_instantiation(instance):
    assert isinstance(instance, UML2_AnyTrigger)

@given(instance=Realization_strategy)
@settings(max_examples=50)
def test_realization_instantiation(instance):
    assert isinstance(instance, Realization)

@given(instance=UML2_Substitution_strategy)
@settings(max_examples=50)
def test_uml2_substitution_instantiation(instance):
    assert isinstance(instance, UML2_Substitution)

@given(instance=UML2_Implementation_strategy)
@settings(max_examples=50)
def test_uml2_implementation_instantiation(instance):
    assert isinstance(instance, UML2_Implementation)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=UML2_VariableAction_strategy)
@settings(max_examples=50)
def test_uml2_variableaction_instantiation(instance):
    assert isinstance(instance, UML2_VariableAction)

@given(instance=UML2_LinkAction_strategy)
@settings(max_examples=50)
def test_uml2_linkaction_instantiation(instance):
    assert isinstance(instance, UML2_LinkAction)

@given(instance=UML2_InvocationAction_strategy)
@settings(max_examples=50)
def test_uml2_invocationaction_instantiation(instance):
    assert isinstance(instance, UML2_InvocationAction)

@given(instance=UML2_ClearAssociationAction_strategy)
@settings(max_examples=50)
def test_uml2_clearassociationaction_instantiation(instance):
    assert isinstance(instance, UML2_ClearAssociationAction)

@given(instance=UML2_ReadLinkObjectEndAction_strategy)
@settings(max_examples=50)
def test_uml2_readlinkobjectendaction_instantiation(instance):
    assert isinstance(instance, UML2_ReadLinkObjectEndAction)

@given(instance=UML2_ReplyAction_strategy)
@settings(max_examples=50)
def test_uml2_replyaction_instantiation(instance):
    assert isinstance(instance, UML2_ReplyAction)

@given(instance=UML2_StartOwnedBehaviorAction_strategy)
@settings(max_examples=50)
def test_uml2_startownedbehavioraction_instantiation(instance):
    assert isinstance(instance, UML2_StartOwnedBehaviorAction)

@given(instance=UML2_CreateObjectAction_strategy)
@settings(max_examples=50)
def test_uml2_createobjectaction_instantiation(instance):
    assert isinstance(instance, UML2_CreateObjectAction)

@given(instance=UML2_RaiseExceptionAction_strategy)
@settings(max_examples=50)
def test_uml2_raiseexceptionaction_instantiation(instance):
    assert isinstance(instance, UML2_RaiseExceptionAction)

@given(instance=UML2_ReadExtentAction_strategy)
@settings(max_examples=50)
def test_uml2_readextentaction_instantiation(instance):
    assert isinstance(instance, UML2_ReadExtentAction)

@given(instance=UML2_AcceptEventAction_strategy)
@settings(max_examples=50)
def test_uml2_accepteventaction_instantiation(instance):
    assert isinstance(instance, UML2_AcceptEventAction)

@given(instance=UML2_ReadIsClassifiedObjectAction_strategy)
@settings(max_examples=50)
def test_uml2_readisclassifiedobjectaction_instantiation(instance):
    assert isinstance(instance, UML2_ReadIsClassifiedObjectAction)

@given(instance=UML2_StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_uml2_structuredactivitynode_instantiation(instance):
    assert isinstance(instance, UML2_StructuredActivityNode)

@given(instance=UML2_DestroyObjectAction_strategy)
@settings(max_examples=50)
def test_uml2_destroyobjectaction_instantiation(instance):
    assert isinstance(instance, UML2_DestroyObjectAction)

@given(instance=UML2_ReclassifyObjectAction_strategy)
@settings(max_examples=50)
def test_uml2_reclassifyobjectaction_instantiation(instance):
    assert isinstance(instance, UML2_ReclassifyObjectAction)

@given(instance=UML2_ApplyFunctionAction_strategy)
@settings(max_examples=50)
def test_uml2_applyfunctionaction_instantiation(instance):
    assert isinstance(instance, UML2_ApplyFunctionAction)

@given(instance=UML2_StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml2_structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, UML2_StructuralFeatureAction)

@given(instance=LiteralSpecification_strategy)
@settings(max_examples=50)
def test_literalspecification_instantiation(instance):
    assert isinstance(instance, LiteralSpecification)

@given(instance=UML2_LiteralNull_strategy)
@settings(max_examples=50)
def test_uml2_literalnull_instantiation(instance):
    assert isinstance(instance, UML2_LiteralNull)

@given(instance=UML2_LiteralInteger_strategy)
@settings(max_examples=50)
def test_uml2_literalinteger_instantiation(instance):
    assert isinstance(instance, UML2_LiteralInteger)

@given(instance=UML2_LiteralUnlimitedNatural_strategy)
@settings(max_examples=50)
def test_uml2_literalunlimitednatural_instantiation(instance):
    assert isinstance(instance, UML2_LiteralUnlimitedNatural)

@given(instance=UML2_LiteralBoolean_strategy)
@settings(max_examples=50)
def test_uml2_literalboolean_instantiation(instance):
    assert isinstance(instance, UML2_LiteralBoolean)

@given(instance=UML2_LiteralString_strategy)
@settings(max_examples=50)
def test_uml2_literalstring_instantiation(instance):
    assert isinstance(instance, UML2_LiteralString)

@given(instance=ActivityNode_strategy)
@settings(max_examples=50)
def test_activitynode_instantiation(instance):
    assert isinstance(instance, ActivityNode)

@given(instance=UML2_ControlNode_strategy)
@settings(max_examples=50)
def test_uml2_controlnode_instantiation(instance):
    assert isinstance(instance, UML2_ControlNode)

@given(instance=UML2_ExecutableNode_strategy)
@settings(max_examples=50)
def test_uml2_executablenode_instantiation(instance):
    assert isinstance(instance, UML2_ExecutableNode)

@given(instance=ControlNode_strategy)
@settings(max_examples=50)
def test_controlnode_instantiation(instance):
    assert isinstance(instance, ControlNode)

@given(instance=UML2_DecisionNode_strategy)
@settings(max_examples=50)
def test_uml2_decisionnode_instantiation(instance):
    assert isinstance(instance, UML2_DecisionNode)

@given(instance=UML2_MergeNode_strategy)
@settings(max_examples=50)
def test_uml2_mergenode_instantiation(instance):
    assert isinstance(instance, UML2_MergeNode)

@given(instance=UML2_InitialNode_strategy)
@settings(max_examples=50)
def test_uml2_initialnode_instantiation(instance):
    assert isinstance(instance, UML2_InitialNode)

@given(instance=UML2_ForkNode_strategy)
@settings(max_examples=50)
def test_uml2_forknode_instantiation(instance):
    assert isinstance(instance, UML2_ForkNode)

@given(instance=UML2_JoinNode_strategy)
@settings(max_examples=50)
def test_uml2_joinnode_instantiation(instance):
    assert isinstance(instance, UML2_JoinNode)

@given(instance=UML2_FinalNode_strategy)
@settings(max_examples=50)
def test_uml2_finalnode_instantiation(instance):
    assert isinstance(instance, UML2_FinalNode)

@given(instance=UML2_Association_strategy)
@settings(max_examples=50)
def test_uml2_association_instantiation(instance):
    assert isinstance(instance, UML2_Association)

@given(instance=DeploymentTarget_strategy)
@settings(max_examples=50)
def test_deploymenttarget_instantiation(instance):
    assert isinstance(instance, DeploymentTarget)

@given(instance=UML2_InstanceSpecification_strategy)
@settings(max_examples=50)
def test_uml2_instancespecification_instantiation(instance):
    assert isinstance(instance, UML2_InstanceSpecification)

@given(instance=ConnectableElement_strategy)
@settings(max_examples=50)
def test_connectableelement_instantiation(instance):
    assert isinstance(instance, ConnectableElement)

@given(instance=StructuralFeature_strategy)
@settings(max_examples=50)
def test_structuralfeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=UML2_Port_strategy)
@settings(max_examples=50)
def test_uml2_port_instantiation(instance):
    assert isinstance(instance, UML2_Port)

@given(instance=UML2_ExtensionEnd_strategy)
@settings(max_examples=50)
def test_uml2_extensionend_instantiation(instance):
    assert isinstance(instance, UML2_ExtensionEnd)

@given(instance=StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, StructuralFeatureAction)

@given(instance=UML2_ReadStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml2_readstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, UML2_ReadStructuralFeatureAction)

@given(instance=UML2_ClearStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml2_clearstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, UML2_ClearStructuralFeatureAction)

@given(instance=UML2_WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml2_writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, UML2_WriteStructuralFeatureAction)

@given(instance=UML2_ReadLinkObjectEndQualifierAction_strategy)
@settings(max_examples=50)
def test_uml2_readlinkobjectendqualifieraction_instantiation(instance):
    assert isinstance(instance, UML2_ReadLinkObjectEndQualifierAction)

@given(instance=UML2_InputPin_strategy)
@settings(max_examples=50)
def test_uml2_inputpin_instantiation(instance):
    assert isinstance(instance, UML2_InputPin)

@given(instance=UML2_TestIdentityAction_strategy)
@settings(max_examples=50)
def test_uml2_testidentityaction_instantiation(instance):
    assert isinstance(instance, UML2_TestIdentityAction)

@given(instance=Association_strategy)
@settings(max_examples=50)
def test_association_instantiation(instance):
    assert isinstance(instance, Association)

@given(instance=UML2_CommunicationPath_strategy)
@settings(max_examples=50)
def test_uml2_communicationpath_instantiation(instance):
    assert isinstance(instance, UML2_CommunicationPath)

@given(instance=UML2_Extension_strategy)
@settings(max_examples=50)
def test_uml2_extension_instantiation(instance):
    assert isinstance(instance, UML2_Extension)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=UML2_Stereotype_strategy)
@settings(max_examples=50)
def test_uml2_stereotype_instantiation(instance):
    assert isinstance(instance, UML2_Stereotype)

@given(instance=UML2_Component_strategy)
@settings(max_examples=50)
def test_uml2_component_instantiation(instance):
    assert isinstance(instance, UML2_Component)

@given(instance=UML2_Behavior_strategy)
@settings(max_examples=50)
def test_uml2_behavior_instantiation(instance):
    assert isinstance(instance, UML2_Behavior)

@given(instance=UML2_Node_strategy)
@settings(max_examples=50)
def test_uml2_node_instantiation(instance):
    assert isinstance(instance, UML2_Node)

@given(instance=UML2_AssociationClass_strategy)
@settings(max_examples=50)
def test_uml2_associationclass_instantiation(instance):
    assert isinstance(instance, UML2_AssociationClass)

@given(instance=UML2_OutputPin_strategy)
@settings(max_examples=50)
def test_uml2_outputpin_instantiation(instance):
    assert isinstance(instance, UML2_OutputPin)

@given(instance=UML2_ReadSelfAction_strategy)
@settings(max_examples=50)
def test_uml2_readselfaction_instantiation(instance):
    assert isinstance(instance, UML2_ReadSelfAction)

@given(instance=ParameterableElement_strategy)
@settings(max_examples=50)
def test_parameterableelement_instantiation(instance):
    assert isinstance(instance, ParameterableElement)

@given(instance=UML2_PackageableElement_strategy)
@settings(max_examples=50)
def test_uml2_packageableelement_instantiation(instance):
    assert isinstance(instance, UML2_PackageableElement)

@given(instance=UML2_ConnectableElement_strategy)
@settings(max_examples=50)
def test_uml2_connectableelement_instantiation(instance):
    assert isinstance(instance, UML2_ConnectableElement)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=UML2_StructuralFeature_strategy)
@settings(max_examples=50)
def test_uml2_structuralfeature_instantiation(instance):
    assert isinstance(instance, UML2_StructuralFeature)



@given(instance=UML2_StructuralFeature_strategy)
def test_uml2_structuralfeature_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original

@given(instance=UML2_Parameter_strategy)
@settings(max_examples=50)
def test_uml2_parameter_instantiation(instance):
    assert isinstance(instance, UML2_Parameter)



@given(instance=UML2_Parameter_strategy)
def test_uml2_parameter_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=UML2_Variable_strategy)
@settings(max_examples=50)
def test_uml2_variable_instantiation(instance):
    assert isinstance(instance, UML2_Variable)

@given(instance=UML2_ObjectNode_strategy)
@settings(max_examples=50)
def test_uml2_objectnode_instantiation(instance):
    assert isinstance(instance, UML2_ObjectNode)

@given(instance=UML2_Operation_strategy)
@settings(max_examples=50)
def test_uml2_operation_instantiation(instance):
    assert isinstance(instance, UML2_Operation)

@given(instance=UML2_ValueSpecification_strategy)
@settings(max_examples=50)
def test_uml2_valuespecification_instantiation(instance):
    assert isinstance(instance, UML2_ValueSpecification)

@given(instance=BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_behavioredclassifier_instantiation(instance):
    assert isinstance(instance, BehavioredClassifier)

@given(instance=UML2_Collaboration_strategy)
@settings(max_examples=50)
def test_uml2_collaboration_instantiation(instance):
    assert isinstance(instance, UML2_Collaboration)

@given(instance=UML2_Class_strategy)
@settings(max_examples=50)
def test_uml2_class_instantiation(instance):
    assert isinstance(instance, UML2_Class)



@given(instance=UML2_Class_strategy)
def test_uml2_class_isActive_setter(instance):
    original = instance.isActive
    instance.isActive = original
    assert instance.isActive == original

@given(instance=UML2_UseCase_strategy)
@settings(max_examples=50)
def test_uml2_usecase_instantiation(instance):
    assert isinstance(instance, UML2_UseCase)

@given(instance=ValueSpecification_strategy)
@settings(max_examples=50)
def test_valuespecification_instantiation(instance):
    assert isinstance(instance, ValueSpecification)

@given(instance=UML2_InstanceValue_strategy)
@settings(max_examples=50)
def test_uml2_instancevalue_instantiation(instance):
    assert isinstance(instance, UML2_InstanceValue)

@given(instance=UML2_LiteralSpecification_strategy)
@settings(max_examples=50)
def test_uml2_literalspecification_instantiation(instance):
    assert isinstance(instance, UML2_LiteralSpecification)

@given(instance=UML2_Duration_strategy)
@settings(max_examples=50)
def test_uml2_duration_instantiation(instance):
    assert isinstance(instance, UML2_Duration)

@given(instance=UML2_OpaqueExpression_strategy)
@settings(max_examples=50)
def test_uml2_opaqueexpression_instantiation(instance):
    assert isinstance(instance, UML2_OpaqueExpression)

@given(instance=UML2_TimeExpression_strategy)
@settings(max_examples=50)
def test_uml2_timeexpression_instantiation(instance):
    assert isinstance(instance, UML2_TimeExpression)

@given(instance=UML2_Interval_strategy)
@settings(max_examples=50)
def test_uml2_interval_instantiation(instance):
    assert isinstance(instance, UML2_Interval)

@given(instance=CreateLinkAction_strategy)
@settings(max_examples=50)
def test_createlinkaction_instantiation(instance):
    assert isinstance(instance, CreateLinkAction)

@given(instance=UML2_CreateLinkObjectAction_strategy)
@settings(max_examples=50)
def test_uml2_createlinkobjectaction_instantiation(instance):
    assert isinstance(instance, UML2_CreateLinkObjectAction)

@given(instance=UML2_Property_strategy)
@settings(max_examples=50)
def test_uml2_property_instantiation(instance):
    assert isinstance(instance, UML2_Property)



@given(instance=UML2_Property_strategy)
def test_uml2_property_aggregation_setter(instance):
    original = instance.aggregation
    instance.aggregation = original
    assert instance.aggregation == original



@given(instance=UML2_Property_strategy)
def test_uml2_property_isDerivedUnion_setter(instance):
    original = instance.isDerivedUnion
    instance.isDerivedUnion = original
    assert instance.isDerivedUnion == original



@given(instance=UML2_Property_strategy)
def test_uml2_property_isComposite_setter(instance):
    original = instance.isComposite
    instance.isComposite = original
    assert instance.isComposite == original



@given(instance=UML2_Property_strategy)
def test_uml2_property_isDerived_setter(instance):
    original = instance.isDerived
    instance.isDerived = original
    assert instance.isDerived == original

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=UML2_TemplateParameter_strategy)
@settings(max_examples=50)
def test_uml2_templateparameter_instantiation(instance):
    assert isinstance(instance, UML2_TemplateParameter)

@given(instance=UML2_ActivityGroup_strategy)
@settings(max_examples=50)
def test_uml2_activitygroup_instantiation(instance):
    assert isinstance(instance, UML2_ActivityGroup)

@given(instance=UML2_Clause_strategy)
@settings(max_examples=50)
def test_uml2_clause_instantiation(instance):
    assert isinstance(instance, UML2_Clause)

@given(instance=UML2_MultiplicityElement_strategy)
@settings(max_examples=50)
def test_uml2_multiplicityelement_instantiation(instance):
    assert isinstance(instance, UML2_MultiplicityElement)



@given(instance=UML2_MultiplicityElement_strategy)
def test_uml2_multiplicityelement_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original



@given(instance=UML2_MultiplicityElement_strategy)
def test_uml2_multiplicityelement_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original



@given(instance=UML2_MultiplicityElement_strategy)
def test_uml2_multiplicityelement_isOrdered_setter(instance):
    original = instance.isOrdered
    instance.isOrdered = original
    assert instance.isOrdered == original



@given(instance=UML2_MultiplicityElement_strategy)
def test_uml2_multiplicityelement_isUnique_setter(instance):
    original = instance.isUnique
    instance.isUnique = original
    assert instance.isUnique == original

@given(instance=UML2_ParameterableElement_strategy)
@settings(max_examples=50)
def test_uml2_parameterableelement_instantiation(instance):
    assert isinstance(instance, UML2_ParameterableElement)

@given(instance=UML2_Slot_strategy)
@settings(max_examples=50)
def test_uml2_slot_instantiation(instance):
    assert isinstance(instance, UML2_Slot)

@given(instance=UML2_LinkEndData_strategy)
@settings(max_examples=50)
def test_uml2_linkenddata_instantiation(instance):
    assert isinstance(instance, UML2_LinkEndData)

@given(instance=UML2_TemplateableElement_strategy)
@settings(max_examples=50)
def test_uml2_templateableelement_instantiation(instance):
    assert isinstance(instance, UML2_TemplateableElement)

@given(instance=UML2_TemplateSignature_strategy)
@settings(max_examples=50)
def test_uml2_templatesignature_instantiation(instance):
    assert isinstance(instance, UML2_TemplateSignature)

@given(instance=UML2_ExceptionHandler_strategy)
@settings(max_examples=50)
def test_uml2_exceptionhandler_instantiation(instance):
    assert isinstance(instance, UML2_ExceptionHandler)

@given(instance=UML2_TemplateParameterSubstitution_strategy)
@settings(max_examples=50)
def test_uml2_templateparametersubstitution_instantiation(instance):
    assert isinstance(instance, UML2_TemplateParameterSubstitution)

@given(instance=UML2_Relationship_strategy)
@settings(max_examples=50)
def test_uml2_relationship_instantiation(instance):
    assert isinstance(instance, UML2_Relationship)

@given(instance=UML2_QualifierValue_strategy)
@settings(max_examples=50)
def test_uml2_qualifiervalue_instantiation(instance):
    assert isinstance(instance, UML2_QualifierValue)
