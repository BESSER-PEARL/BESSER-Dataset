import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ConnectableElement,
    Association,
    TemplateParameter,
    CentralBufferNode,
    VariableAction,
    WriteStructuralFeatureAction,
    StateMachine,
    MessageTrigger,
    DirectedRelationship,
    DeploymentTarget,
    PackageableElement,
    Class,
    OpaqueExpression,
    InteractionFragment,
    Behavior,
    Trigger,
    IntervalConstraint,
    LiteralSpecification,
    WriteVariableAction,
    TemplateableElement,
    EncapsulatedClassifier,
    UML2WithID_Element,
    State,
    Transition,
    AcceptEventAction,
    InputPin,
    Constraint,
    Artifact,
    CreateLinkAction,
    ActivityGroup,
    StructuralFeatureAction,
    StructuralFeature,
    StructuredClassifier,
    BehavioredClassifier,
    Realization,
    PackageImport,
    DataType,
    Relationship,
    InvocationAction,
    InstanceSpecification,
    EventOccurrence,
    Node,
    ExecutableNode,
    StructuredActivityNode,
    Feature,
    Type,
    LinkEndData,
    Dependency,
    ValueSpecification,
    Abstraction,
    Package,
    ActivityEdge,
    ObjectNode,
    LinkAction,
    Action,
    CallAction,
    InteractionOccurrence,
    ActivityNode,
    Vertex,
    Namespace,
    TemplateSignature,
    Interval,
    Pin,
    Property,
    ParameterableElement,
    MultiplicityElement,
    TypedElement,
    BehavioralFeature,
    FinalNode,
    WriteLinkAction,
    ControlNode,
    DeployedArtifact,
    Classifier,
    NamedElement,
    RedefinableElement,
    Element,
    UML2WithID_Pin,
    UML2WithID_Port,
    UML2WithID_Realization,
    UML2WithID_CreateLinkObjectAction,
    UML2WithID_ConnectableElementTemplateParameter,
    UML2WithID_AddVariableValueAction,
    UML2WithID_IntervalConstraint,
    UML2WithID_InitialNode,
    UML2WithID_Model,
    UML2WithID_ActivityGroup,
    UML2WithID_InteractionOperand,
    UML2WithID_ReplyAction,
    UML2WithID_Node,
    UML2WithID_TimeExpression,
    UML2WithID_Stereotype,
    UML2WithID_NamedElement,
    UML2WithID_DeploymentSpecification,
    UML2WithID_Clause,
    UML2WithID_EnumerationLiteral,
    UML2WithID_CreateLinkAction,
    UML2WithID_Action,
    UML2WithID_ControlFlow,
    UML2WithID_TimeConstraint,
    UML2WithID_InvocationAction,
    UML2WithID_TestIdentityAction,
    UML2WithID_Generalization,
    UML2WithID_Property,
    UML2WithID_ExecutableNode,
    UML2WithID_Namespace,
    UML2WithID_Extension,
    UML2WithID_TemplateParameter,
    UML2WithID_ExceptionHandler,
    UML2WithID_ActivityNode,
    UML2WithID_Activity,
    UML2WithID_EncapsulatedClassifier,
    UML2WithID_Stop,
    UML2WithID_OutputPin,
    UML2WithID_InstanceValue,
    UML2WithID_MergeNode,
    UML2WithID_ChangeTrigger,
    UML2WithID_DestroyObjectAction,
    UML2WithID_Region,
    UML2WithID_InterruptibleActivityRegion,
    UML2WithID_Implementation,
    UML2WithID_Extend,
    UML2WithID_SendSignalAction,
    UML2WithID_Interaction,
    UML2WithID_Reception,
    UML2WithID_CallBehaviorAction,
    UML2WithID_RedefinableTemplateSignature,
    UML2WithID_InstanceSpecification,
    UML2WithID_StructuralFeatureAction,
    UML2WithID_PackageableElement,
    UML2WithID_PrimitiveType,
    UML2WithID_BehavioralFeature,
    UML2WithID_ControlNode,
    UML2WithID_Association,
    UML2WithID_JoinNode,
    UML2WithID_Deployment,
    UML2WithID_FinalState,
    UML2WithID_Component,
    UML2WithID_StateMachine,
    UML2WithID_StateInvariant,
    UML2WithID_ExpansionRegion,
    UML2WithID_CallAction,
    UML2WithID_ObjectNode,
    UML2WithID_OpaqueExpression,
    UML2WithID_GeneralOrdering,
    UML2WithID_RaiseExceptionAction,
    UML2WithID_Variable,
    UML2WithID_ReadLinkObjectEndAction,
    UML2WithID_ClearAssociationAction,
    UML2WithID_DirectedRelationship,
    UML2WithID_Usage,
    UML2WithID_LiteralString,
    UML2WithID_TemplateableElement,
    UML2WithID_StartOwnedBehaviorAction,
    UML2WithID_DeployedArtifact,
    UML2WithID_LiteralInteger,
    UML2WithID_StructuredActivityNode,
    UML2WithID_ReadLinkAction,
    UML2WithID_Vertex,
    UML2WithID_LiteralUnlimitedNatural,
    UML2WithID_DataType,
    UML2WithID_LoopNode,
    UML2WithID_Transition,
    UML2WithID_ProtocolTransition,
    UML2WithID_UseCase,
    UML2WithID_ParameterableClassifier,
    UML2WithID_TimeInterval,
    UML2WithID_ProtocolConformance,
    UML2WithID_Operation,
    UML2WithID_InteractionFragment,
    UML2WithID_Slot,
    UML2WithID_RedefinableElement,
    UML2WithID_ReadLinkObjectEndQualifierAction,
    UML2WithID_VariableAction,
    UML2WithID_ActivityFinalNode,
    UML2WithID_Interval,
    UML2WithID_LinkEndCreationData,
    UML2WithID_ReadExtentAction,
    UML2WithID_Pseudostate,
    UML2WithID_DestroyLinkAction,
    UML2WithID_FlowFinalNode,
    UML2WithID_ClearStructuralFeatureAction,
    UML2WithID_CombinedFragment,
    UML2WithID_Continuation,
    UML2WithID_ForkNode,
    UML2WithID_Relationship,
    UML2WithID_AssociationClass,
    UML2WithID_ProtocolStateMachine,
    UML2WithID_ActivityEdge,
    UML2WithID_Signal,
    UML2WithID_DurationObservationAction,
    UML2WithID_Permission,
    UML2WithID_Artifact,
    UML2WithID_ReadStructuralFeatureAction,
    UML2WithID_MessageEnd,
    UML2WithID_CallTrigger,
    UML2WithID_Comment,
    UML2WithID_DurationConstraint,
    UML2WithID_ValueSpecification,
    UML2WithID_Parameter,
    UML2WithID_ActivityPartition,
    UML2WithID_AnyTrigger,
    UML2WithID_TemplateBinding,
    UML2WithID_Constraint,
    UML2WithID_Enumeration,
    UML2WithID_BehavioredClassifier,
    UML2WithID_RemoveVariableValueAction,
    UML2WithID_LiteralNull,
    UML2WithID_ConnectableElement,
    UML2WithID_TimeObservationAction,
    UML2WithID_Class,
    UML2WithID_LinkEndData,
    UML2WithID_TimeTrigger,
    UML2WithID_Type,
    UML2WithID_StringExpression,
    UML2WithID_CallOperationAction,
    UML2WithID_CentralBufferNode,
    UML2WithID_ParameterableElement,
    UML2WithID_ProfileApplication,
    UML2WithID_ExpansionNode,
    UML2WithID_Collaboration,
    UML2WithID_State,
    UML2WithID_ConnectorEnd,
    UML2WithID_Include,
    UML2WithID_Profile,
    UML2WithID_Duration,
    UML2WithID_PackageImport,
    UML2WithID_Interface,
    UML2WithID_ExecutionOccurrence,
    UML2WithID_ReclassifyObjectAction,
    UML2WithID_MessageTrigger,
    UML2WithID_Substitution,
    UML2WithID_InputPin,
    UML2WithID_Expression,
    UML2WithID_ValuePin,
    UML2WithID_QualifierValue,
    UML2WithID_CollaborationOccurrence,
    UML2WithID_CreateObjectAction,
    UML2WithID_TemplateSignature,
    UML2WithID_Abstraction,
    UML2WithID_Trigger,
    UML2WithID_Connector,
    UML2WithID_LiteralBoolean,
    UML2WithID_BroadcastSignalAction,
    UML2WithID_ObjectFlow,
    UML2WithID_PackageMerge,
    UML2WithID_LinkAction,
    UML2WithID_FinalNode,
    UML2WithID_ExecutionEnvironment,
    UML2WithID_Message,
    UML2WithID_DataStoreNode,
    UML2WithID_ClassifierTemplateParameter,
    UML2WithID_ClearVariableAction,
    UML2WithID_Manifestation,
    UML2WithID_InteractionConstraint,
    UML2WithID_CommunicationPath,
    UML2WithID_Actor,
    UML2WithID_ExtensionEnd,
    UML2WithID_GeneralizationSet,
    UML2WithID_StructuralFeature,
    UML2WithID_TemplateableClassifier,
    UML2WithID_Device,
    UML2WithID_PrimitiveFunction,
    UML2WithID_ConnectionPointReference,
    UML2WithID_PartDecomposition,
    UML2WithID_ReadSelfAction,
    UML2WithID_MultiplicityElement,
    UML2WithID_DurationInterval,
    UML2WithID_AcceptEventAction,
    UML2WithID_SignalTrigger,
    UML2WithID_SendObjectAction,
    UML2WithID_WriteStructuralFeatureAction,
    UML2WithID_Lifeline,
    UML2WithID_ReadVariableAction,
    UML2WithID_LiteralSpecification,
    UML2WithID_DecisionNode,
    UML2WithID_DeploymentTarget,
    UML2WithID_ReadIsClassifiedObjectAction,
    UML2WithID_Package,
    UML2WithID_TypedElement,
    UML2WithID_InformationFlow,
    UML2WithID_InteractionOccurrence,
    UML2WithID_ActivityParameterNode,
    UML2WithID_WriteLinkAction,
    UML2WithID_ElementImport,
    UML2WithID_TemplateParameterSubstitution,
    UML2WithID_RemoveStructuralFeatureValueAction,
    UML2WithID_StructuredClassifier,
    UML2WithID_OperationTemplateParameter,
    UML2WithID_ConditionalNode,
    UML2WithID_AcceptCallAction,
    UML2WithID_Feature,
    UML2WithID_WriteVariableAction,
    UML2WithID_Behavior,
    UML2WithID_InformationItem,
    UML2WithID_Dependency,
    UML2WithID_Classifier,
    UML2WithID_ApplyFunctionAction,
    UML2WithID_ExtensionPoint,
    UML2WithID_AddStructuralFeatureValueAction,
    UML2WithID_ParameterSet,
    MessageEnd,
    UML2WithID_EventOccurrence,
    UML2WithID_Gate,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_connectableelement_is_not_abstract():
    assert not inspect.isabstract(ConnectableElement)


def test_connectableelement_constructor_exists():
    assert callable(ConnectableElement.__init__)


def test_connectableelement_constructor_args():
    sig = inspect.signature(ConnectableElement.__init__)
    params = list(sig.parameters.keys())



def test_association_is_not_abstract():
    assert not inspect.isabstract(Association)


def test_association_constructor_exists():
    assert callable(Association.__init__)


def test_association_constructor_args():
    sig = inspect.signature(Association.__init__)
    params = list(sig.parameters.keys())



def test_templateparameter_is_not_abstract():
    assert not inspect.isabstract(TemplateParameter)


def test_templateparameter_constructor_exists():
    assert callable(TemplateParameter.__init__)


def test_templateparameter_constructor_args():
    sig = inspect.signature(TemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_centralbuffernode_is_not_abstract():
    assert not inspect.isabstract(CentralBufferNode)


def test_centralbuffernode_constructor_exists():
    assert callable(CentralBufferNode.__init__)


def test_centralbuffernode_constructor_args():
    sig = inspect.signature(CentralBufferNode.__init__)
    params = list(sig.parameters.keys())



def test_variableaction_is_not_abstract():
    assert not inspect.isabstract(VariableAction)


def test_variableaction_constructor_exists():
    assert callable(VariableAction.__init__)


def test_variableaction_constructor_args():
    sig = inspect.signature(VariableAction.__init__)
    params = list(sig.parameters.keys())



def test_writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(WriteStructuralFeatureAction)


def test_writestructuralfeatureaction_constructor_exists():
    assert callable(WriteStructuralFeatureAction.__init__)


def test_writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachine)


def test_statemachine_constructor_exists():
    assert callable(StateMachine.__init__)


def test_statemachine_constructor_args():
    sig = inspect.signature(StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_messagetrigger_is_not_abstract():
    assert not inspect.isabstract(MessageTrigger)


def test_messagetrigger_constructor_exists():
    assert callable(MessageTrigger.__init__)


def test_messagetrigger_constructor_args():
    sig = inspect.signature(MessageTrigger.__init__)
    params = list(sig.parameters.keys())



def test_directedrelationship_is_not_abstract():
    assert not inspect.isabstract(DirectedRelationship)


def test_directedrelationship_constructor_exists():
    assert callable(DirectedRelationship.__init__)


def test_directedrelationship_constructor_args():
    sig = inspect.signature(DirectedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_deploymenttarget_is_not_abstract():
    assert not inspect.isabstract(DeploymentTarget)


def test_deploymenttarget_constructor_exists():
    assert callable(DeploymentTarget.__init__)


def test_deploymenttarget_constructor_args():
    sig = inspect.signature(DeploymentTarget.__init__)
    params = list(sig.parameters.keys())



def test_packageableelement_is_not_abstract():
    assert not inspect.isabstract(PackageableElement)


def test_packageableelement_constructor_exists():
    assert callable(PackageableElement.__init__)


def test_packageableelement_constructor_args():
    sig = inspect.signature(PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(OpaqueExpression)


def test_opaqueexpression_constructor_exists():
    assert callable(OpaqueExpression.__init__)


def test_opaqueexpression_constructor_args():
    sig = inspect.signature(OpaqueExpression.__init__)
    params = list(sig.parameters.keys())



def test_interactionfragment_is_not_abstract():
    assert not inspect.isabstract(InteractionFragment)


def test_interactionfragment_constructor_exists():
    assert callable(InteractionFragment.__init__)


def test_interactionfragment_constructor_args():
    sig = inspect.signature(InteractionFragment.__init__)
    params = list(sig.parameters.keys())



def test_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
    params = list(sig.parameters.keys())



def test_trigger_is_not_abstract():
    assert not inspect.isabstract(Trigger)


def test_trigger_constructor_exists():
    assert callable(Trigger.__init__)


def test_trigger_constructor_args():
    sig = inspect.signature(Trigger.__init__)
    params = list(sig.parameters.keys())



def test_intervalconstraint_is_not_abstract():
    assert not inspect.isabstract(IntervalConstraint)


def test_intervalconstraint_constructor_exists():
    assert callable(IntervalConstraint.__init__)


def test_intervalconstraint_constructor_args():
    sig = inspect.signature(IntervalConstraint.__init__)
    params = list(sig.parameters.keys())



def test_literalspecification_is_not_abstract():
    assert not inspect.isabstract(LiteralSpecification)


def test_literalspecification_constructor_exists():
    assert callable(LiteralSpecification.__init__)


def test_literalspecification_constructor_args():
    sig = inspect.signature(LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_writevariableaction_is_not_abstract():
    assert not inspect.isabstract(WriteVariableAction)


def test_writevariableaction_constructor_exists():
    assert callable(WriteVariableAction.__init__)


def test_writevariableaction_constructor_args():
    sig = inspect.signature(WriteVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_templateableelement_is_not_abstract():
    assert not inspect.isabstract(TemplateableElement)


def test_templateableelement_constructor_exists():
    assert callable(TemplateableElement.__init__)


def test_templateableelement_constructor_args():
    sig = inspect.signature(TemplateableElement.__init__)
    params = list(sig.parameters.keys())



def test_encapsulatedclassifier_is_not_abstract():
    assert not inspect.isabstract(EncapsulatedClassifier)


def test_encapsulatedclassifier_constructor_exists():
    assert callable(EncapsulatedClassifier.__init__)


def test_encapsulatedclassifier_constructor_args():
    sig = inspect.signature(EncapsulatedClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_element_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Element)


def test_uml2withid_element_constructor_exists():
    assert callable(UML2WithID_Element.__init__)


def test_uml2withid_element_constructor_args():
    sig = inspect.signature(UML2WithID_Element.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"

def test_uml2withid_element_has_ID():
    assert hasattr(UML2WithID_Element, "ID")
    descriptor = None
    for klass in UML2WithID_Element.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_accepteventaction_is_not_abstract():
    assert not inspect.isabstract(AcceptEventAction)


def test_accepteventaction_constructor_exists():
    assert callable(AcceptEventAction.__init__)


def test_accepteventaction_constructor_args():
    sig = inspect.signature(AcceptEventAction.__init__)
    params = list(sig.parameters.keys())



def test_inputpin_is_not_abstract():
    assert not inspect.isabstract(InputPin)


def test_inputpin_constructor_exists():
    assert callable(InputPin.__init__)


def test_inputpin_constructor_args():
    sig = inspect.signature(InputPin.__init__)
    params = list(sig.parameters.keys())



def test_constraint_is_not_abstract():
    assert not inspect.isabstract(Constraint)


def test_constraint_constructor_exists():
    assert callable(Constraint.__init__)


def test_constraint_constructor_args():
    sig = inspect.signature(Constraint.__init__)
    params = list(sig.parameters.keys())



def test_artifact_is_not_abstract():
    assert not inspect.isabstract(Artifact)


def test_artifact_constructor_exists():
    assert callable(Artifact.__init__)


def test_artifact_constructor_args():
    sig = inspect.signature(Artifact.__init__)
    params = list(sig.parameters.keys())



def test_createlinkaction_is_not_abstract():
    assert not inspect.isabstract(CreateLinkAction)


def test_createlinkaction_constructor_exists():
    assert callable(CreateLinkAction.__init__)


def test_createlinkaction_constructor_args():
    sig = inspect.signature(CreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_activitygroup_is_not_abstract():
    assert not inspect.isabstract(ActivityGroup)


def test_activitygroup_constructor_exists():
    assert callable(ActivityGroup.__init__)


def test_activitygroup_constructor_args():
    sig = inspect.signature(ActivityGroup.__init__)
    params = list(sig.parameters.keys())



def test_structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(StructuralFeatureAction)


def test_structuralfeatureaction_constructor_exists():
    assert callable(StructuralFeatureAction.__init__)


def test_structuralfeatureaction_constructor_args():
    sig = inspect.signature(StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(StructuralFeature)


def test_structuralfeature_constructor_exists():
    assert callable(StructuralFeature.__init__)


def test_structuralfeature_constructor_args():
    sig = inspect.signature(StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_structuredclassifier_is_not_abstract():
    assert not inspect.isabstract(StructuredClassifier)


def test_structuredclassifier_constructor_exists():
    assert callable(StructuredClassifier.__init__)


def test_structuredclassifier_constructor_args():
    sig = inspect.signature(StructuredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(BehavioredClassifier)


def test_behavioredclassifier_constructor_exists():
    assert callable(BehavioredClassifier.__init__)


def test_behavioredclassifier_constructor_args():
    sig = inspect.signature(BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_realization_is_not_abstract():
    assert not inspect.isabstract(Realization)


def test_realization_constructor_exists():
    assert callable(Realization.__init__)


def test_realization_constructor_args():
    sig = inspect.signature(Realization.__init__)
    params = list(sig.parameters.keys())



def test_packageimport_is_not_abstract():
    assert not inspect.isabstract(PackageImport)


def test_packageimport_constructor_exists():
    assert callable(PackageImport.__init__)


def test_packageimport_constructor_args():
    sig = inspect.signature(PackageImport.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_relationship_is_not_abstract():
    assert not inspect.isabstract(Relationship)


def test_relationship_constructor_exists():
    assert callable(Relationship.__init__)


def test_relationship_constructor_args():
    sig = inspect.signature(Relationship.__init__)
    params = list(sig.parameters.keys())



def test_invocationaction_is_not_abstract():
    assert not inspect.isabstract(InvocationAction)


def test_invocationaction_constructor_exists():
    assert callable(InvocationAction.__init__)


def test_invocationaction_constructor_args():
    sig = inspect.signature(InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_instancespecification_is_not_abstract():
    assert not inspect.isabstract(InstanceSpecification)


def test_instancespecification_constructor_exists():
    assert callable(InstanceSpecification.__init__)


def test_instancespecification_constructor_args():
    sig = inspect.signature(InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_eventoccurrence_is_not_abstract():
    assert not inspect.isabstract(EventOccurrence)


def test_eventoccurrence_constructor_exists():
    assert callable(EventOccurrence.__init__)


def test_eventoccurrence_constructor_args():
    sig = inspect.signature(EventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_executablenode_is_not_abstract():
    assert not inspect.isabstract(ExecutableNode)


def test_executablenode_constructor_exists():
    assert callable(ExecutableNode.__init__)


def test_executablenode_constructor_args():
    sig = inspect.signature(ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(StructuredActivityNode)


def test_structuredactivitynode_constructor_exists():
    assert callable(StructuredActivityNode.__init__)


def test_structuredactivitynode_constructor_args():
    sig = inspect.signature(StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_linkenddata_is_not_abstract():
    assert not inspect.isabstract(LinkEndData)


def test_linkenddata_constructor_exists():
    assert callable(LinkEndData.__init__)


def test_linkenddata_constructor_args():
    sig = inspect.signature(LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_dependency_is_not_abstract():
    assert not inspect.isabstract(Dependency)


def test_dependency_constructor_exists():
    assert callable(Dependency.__init__)


def test_dependency_constructor_args():
    sig = inspect.signature(Dependency.__init__)
    params = list(sig.parameters.keys())



def test_valuespecification_is_not_abstract():
    assert not inspect.isabstract(ValueSpecification)


def test_valuespecification_constructor_exists():
    assert callable(ValueSpecification.__init__)


def test_valuespecification_constructor_args():
    sig = inspect.signature(ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_abstraction_is_not_abstract():
    assert not inspect.isabstract(Abstraction)


def test_abstraction_constructor_exists():
    assert callable(Abstraction.__init__)


def test_abstraction_constructor_args():
    sig = inspect.signature(Abstraction.__init__)
    params = list(sig.parameters.keys())



def test_package_is_not_abstract():
    assert not inspect.isabstract(Package)


def test_package_constructor_exists():
    assert callable(Package.__init__)


def test_package_constructor_args():
    sig = inspect.signature(Package.__init__)
    params = list(sig.parameters.keys())



def test_activityedge_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge)


def test_activityedge_constructor_exists():
    assert callable(ActivityEdge.__init__)


def test_activityedge_constructor_args():
    sig = inspect.signature(ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_objectnode_is_not_abstract():
    assert not inspect.isabstract(ObjectNode)


def test_objectnode_constructor_exists():
    assert callable(ObjectNode.__init__)


def test_objectnode_constructor_args():
    sig = inspect.signature(ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_linkaction_is_not_abstract():
    assert not inspect.isabstract(LinkAction)


def test_linkaction_constructor_exists():
    assert callable(LinkAction.__init__)


def test_linkaction_constructor_args():
    sig = inspect.signature(LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_callaction_is_not_abstract():
    assert not inspect.isabstract(CallAction)


def test_callaction_constructor_exists():
    assert callable(CallAction.__init__)


def test_callaction_constructor_args():
    sig = inspect.signature(CallAction.__init__)
    params = list(sig.parameters.keys())



def test_interactionoccurrence_is_not_abstract():
    assert not inspect.isabstract(InteractionOccurrence)


def test_interactionoccurrence_constructor_exists():
    assert callable(InteractionOccurrence.__init__)


def test_interactionoccurrence_constructor_args():
    sig = inspect.signature(InteractionOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_is_not_abstract():
    assert not inspect.isabstract(ActivityNode)


def test_activitynode_constructor_exists():
    assert callable(ActivityNode.__init__)


def test_activitynode_constructor_args():
    sig = inspect.signature(ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_vertex_is_not_abstract():
    assert not inspect.isabstract(Vertex)


def test_vertex_constructor_exists():
    assert callable(Vertex.__init__)


def test_vertex_constructor_args():
    sig = inspect.signature(Vertex.__init__)
    params = list(sig.parameters.keys())



def test_namespace_is_not_abstract():
    assert not inspect.isabstract(Namespace)


def test_namespace_constructor_exists():
    assert callable(Namespace.__init__)


def test_namespace_constructor_args():
    sig = inspect.signature(Namespace.__init__)
    params = list(sig.parameters.keys())



def test_templatesignature_is_not_abstract():
    assert not inspect.isabstract(TemplateSignature)


def test_templatesignature_constructor_exists():
    assert callable(TemplateSignature.__init__)


def test_templatesignature_constructor_args():
    sig = inspect.signature(TemplateSignature.__init__)
    params = list(sig.parameters.keys())



def test_interval_is_not_abstract():
    assert not inspect.isabstract(Interval)


def test_interval_constructor_exists():
    assert callable(Interval.__init__)


def test_interval_constructor_args():
    sig = inspect.signature(Interval.__init__)
    params = list(sig.parameters.keys())



def test_pin_is_not_abstract():
    assert not inspect.isabstract(Pin)


def test_pin_constructor_exists():
    assert callable(Pin.__init__)


def test_pin_constructor_args():
    sig = inspect.signature(Pin.__init__)
    params = list(sig.parameters.keys())



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_parameterableelement_is_not_abstract():
    assert not inspect.isabstract(ParameterableElement)


def test_parameterableelement_constructor_exists():
    assert callable(ParameterableElement.__init__)


def test_parameterableelement_constructor_args():
    sig = inspect.signature(ParameterableElement.__init__)
    params = list(sig.parameters.keys())



def test_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(MultiplicityElement)


def test_multiplicityelement_constructor_exists():
    assert callable(MultiplicityElement.__init__)


def test_multiplicityelement_constructor_args():
    sig = inspect.signature(MultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(BehavioralFeature)


def test_behavioralfeature_constructor_exists():
    assert callable(BehavioralFeature.__init__)


def test_behavioralfeature_constructor_args():
    sig = inspect.signature(BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_finalnode_is_not_abstract():
    assert not inspect.isabstract(FinalNode)


def test_finalnode_constructor_exists():
    assert callable(FinalNode.__init__)


def test_finalnode_constructor_args():
    sig = inspect.signature(FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_writelinkaction_is_not_abstract():
    assert not inspect.isabstract(WriteLinkAction)


def test_writelinkaction_constructor_exists():
    assert callable(WriteLinkAction.__init__)


def test_writelinkaction_constructor_args():
    sig = inspect.signature(WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_controlnode_is_not_abstract():
    assert not inspect.isabstract(ControlNode)


def test_controlnode_constructor_exists():
    assert callable(ControlNode.__init__)


def test_controlnode_constructor_args():
    sig = inspect.signature(ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_deployedartifact_is_not_abstract():
    assert not inspect.isabstract(DeployedArtifact)


def test_deployedartifact_constructor_exists():
    assert callable(DeployedArtifact.__init__)


def test_deployedartifact_constructor_args():
    sig = inspect.signature(DeployedArtifact.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_redefinableelement_is_not_abstract():
    assert not inspect.isabstract(RedefinableElement)


def test_redefinableelement_constructor_exists():
    assert callable(RedefinableElement.__init__)


def test_redefinableelement_constructor_args():
    sig = inspect.signature(RedefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_pin_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Pin)


def test_uml2withid_pin_constructor_exists():
    assert callable(UML2WithID_Pin.__init__)


def test_uml2withid_pin_constructor_args():
    sig = inspect.signature(UML2WithID_Pin.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_port_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Port)


def test_uml2withid_port_constructor_exists():
    assert callable(UML2WithID_Port.__init__)


def test_uml2withid_port_constructor_args():
    sig = inspect.signature(UML2WithID_Port.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_realization_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Realization)


def test_uml2withid_realization_constructor_exists():
    assert callable(UML2WithID_Realization.__init__)


def test_uml2withid_realization_constructor_args():
    sig = inspect.signature(UML2WithID_Realization.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_createlinkobjectaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_CreateLinkObjectAction)


def test_uml2withid_createlinkobjectaction_constructor_exists():
    assert callable(UML2WithID_CreateLinkObjectAction.__init__)


def test_uml2withid_createlinkobjectaction_constructor_args():
    sig = inspect.signature(UML2WithID_CreateLinkObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_connectableelementtemplateparameter_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ConnectableElementTemplateParameter)


def test_uml2withid_connectableelementtemplateparameter_constructor_exists():
    assert callable(UML2WithID_ConnectableElementTemplateParameter.__init__)


def test_uml2withid_connectableelementtemplateparameter_constructor_args():
    sig = inspect.signature(UML2WithID_ConnectableElementTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_addvariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_AddVariableValueAction)


def test_uml2withid_addvariablevalueaction_constructor_exists():
    assert callable(UML2WithID_AddVariableValueAction.__init__)


def test_uml2withid_addvariablevalueaction_constructor_args():
    sig = inspect.signature(UML2WithID_AddVariableValueAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_intervalconstraint_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_IntervalConstraint)


def test_uml2withid_intervalconstraint_constructor_exists():
    assert callable(UML2WithID_IntervalConstraint.__init__)


def test_uml2withid_intervalconstraint_constructor_args():
    sig = inspect.signature(UML2WithID_IntervalConstraint.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_initialnode_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_InitialNode)


def test_uml2withid_initialnode_constructor_exists():
    assert callable(UML2WithID_InitialNode.__init__)


def test_uml2withid_initialnode_constructor_args():
    sig = inspect.signature(UML2WithID_InitialNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_model_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Model)


def test_uml2withid_model_constructor_exists():
    assert callable(UML2WithID_Model.__init__)


def test_uml2withid_model_constructor_args():
    sig = inspect.signature(UML2WithID_Model.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_activitygroup_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ActivityGroup)


def test_uml2withid_activitygroup_constructor_exists():
    assert callable(UML2WithID_ActivityGroup.__init__)


def test_uml2withid_activitygroup_constructor_args():
    sig = inspect.signature(UML2WithID_ActivityGroup.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_interactionoperand_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_InteractionOperand)


def test_uml2withid_interactionoperand_constructor_exists():
    assert callable(UML2WithID_InteractionOperand.__init__)


def test_uml2withid_interactionoperand_constructor_args():
    sig = inspect.signature(UML2WithID_InteractionOperand.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_replyaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ReplyAction)


def test_uml2withid_replyaction_constructor_exists():
    assert callable(UML2WithID_ReplyAction.__init__)


def test_uml2withid_replyaction_constructor_args():
    sig = inspect.signature(UML2WithID_ReplyAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_node_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Node)


def test_uml2withid_node_constructor_exists():
    assert callable(UML2WithID_Node.__init__)


def test_uml2withid_node_constructor_args():
    sig = inspect.signature(UML2WithID_Node.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_timeexpression_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_TimeExpression)


def test_uml2withid_timeexpression_constructor_exists():
    assert callable(UML2WithID_TimeExpression.__init__)


def test_uml2withid_timeexpression_constructor_args():
    sig = inspect.signature(UML2WithID_TimeExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_stereotype_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Stereotype)


def test_uml2withid_stereotype_constructor_exists():
    assert callable(UML2WithID_Stereotype.__init__)


def test_uml2withid_stereotype_constructor_args():
    sig = inspect.signature(UML2WithID_Stereotype.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_namedelement_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_NamedElement)


def test_uml2withid_namedelement_constructor_exists():
    assert callable(UML2WithID_NamedElement.__init__)


def test_uml2withid_namedelement_constructor_args():
    sig = inspect.signature(UML2WithID_NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_deploymentspecification_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_DeploymentSpecification)


def test_uml2withid_deploymentspecification_constructor_exists():
    assert callable(UML2WithID_DeploymentSpecification.__init__)


def test_uml2withid_deploymentspecification_constructor_args():
    sig = inspect.signature(UML2WithID_DeploymentSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_clause_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Clause)


def test_uml2withid_clause_constructor_exists():
    assert callable(UML2WithID_Clause.__init__)


def test_uml2withid_clause_constructor_args():
    sig = inspect.signature(UML2WithID_Clause.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_enumerationliteral_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_EnumerationLiteral)


def test_uml2withid_enumerationliteral_constructor_exists():
    assert callable(UML2WithID_EnumerationLiteral.__init__)


def test_uml2withid_enumerationliteral_constructor_args():
    sig = inspect.signature(UML2WithID_EnumerationLiteral.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_createlinkaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_CreateLinkAction)


def test_uml2withid_createlinkaction_constructor_exists():
    assert callable(UML2WithID_CreateLinkAction.__init__)


def test_uml2withid_createlinkaction_constructor_args():
    sig = inspect.signature(UML2WithID_CreateLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_action_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Action)


def test_uml2withid_action_constructor_exists():
    assert callable(UML2WithID_Action.__init__)


def test_uml2withid_action_constructor_args():
    sig = inspect.signature(UML2WithID_Action.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_controlflow_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ControlFlow)


def test_uml2withid_controlflow_constructor_exists():
    assert callable(UML2WithID_ControlFlow.__init__)


def test_uml2withid_controlflow_constructor_args():
    sig = inspect.signature(UML2WithID_ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_timeconstraint_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_TimeConstraint)


def test_uml2withid_timeconstraint_constructor_exists():
    assert callable(UML2WithID_TimeConstraint.__init__)


def test_uml2withid_timeconstraint_constructor_args():
    sig = inspect.signature(UML2WithID_TimeConstraint.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_invocationaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_InvocationAction)


def test_uml2withid_invocationaction_constructor_exists():
    assert callable(UML2WithID_InvocationAction.__init__)


def test_uml2withid_invocationaction_constructor_args():
    sig = inspect.signature(UML2WithID_InvocationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_testidentityaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_TestIdentityAction)


def test_uml2withid_testidentityaction_constructor_exists():
    assert callable(UML2WithID_TestIdentityAction.__init__)


def test_uml2withid_testidentityaction_constructor_args():
    sig = inspect.signature(UML2WithID_TestIdentityAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_generalization_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Generalization)


def test_uml2withid_generalization_constructor_exists():
    assert callable(UML2WithID_Generalization.__init__)


def test_uml2withid_generalization_constructor_args():
    sig = inspect.signature(UML2WithID_Generalization.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_property_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Property)


def test_uml2withid_property_constructor_exists():
    assert callable(UML2WithID_Property.__init__)


def test_uml2withid_property_constructor_args():
    sig = inspect.signature(UML2WithID_Property.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_executablenode_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ExecutableNode)


def test_uml2withid_executablenode_constructor_exists():
    assert callable(UML2WithID_ExecutableNode.__init__)


def test_uml2withid_executablenode_constructor_args():
    sig = inspect.signature(UML2WithID_ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_namespace_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Namespace)


def test_uml2withid_namespace_constructor_exists():
    assert callable(UML2WithID_Namespace.__init__)


def test_uml2withid_namespace_constructor_args():
    sig = inspect.signature(UML2WithID_Namespace.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_extension_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Extension)


def test_uml2withid_extension_constructor_exists():
    assert callable(UML2WithID_Extension.__init__)


def test_uml2withid_extension_constructor_args():
    sig = inspect.signature(UML2WithID_Extension.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_templateparameter_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_TemplateParameter)


def test_uml2withid_templateparameter_constructor_exists():
    assert callable(UML2WithID_TemplateParameter.__init__)


def test_uml2withid_templateparameter_constructor_args():
    sig = inspect.signature(UML2WithID_TemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_exceptionhandler_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ExceptionHandler)


def test_uml2withid_exceptionhandler_constructor_exists():
    assert callable(UML2WithID_ExceptionHandler.__init__)


def test_uml2withid_exceptionhandler_constructor_args():
    sig = inspect.signature(UML2WithID_ExceptionHandler.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_activitynode_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ActivityNode)


def test_uml2withid_activitynode_constructor_exists():
    assert callable(UML2WithID_ActivityNode.__init__)


def test_uml2withid_activitynode_constructor_args():
    sig = inspect.signature(UML2WithID_ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_activity_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Activity)


def test_uml2withid_activity_constructor_exists():
    assert callable(UML2WithID_Activity.__init__)


def test_uml2withid_activity_constructor_args():
    sig = inspect.signature(UML2WithID_Activity.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_encapsulatedclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_EncapsulatedClassifier)


def test_uml2withid_encapsulatedclassifier_constructor_exists():
    assert callable(UML2WithID_EncapsulatedClassifier.__init__)


def test_uml2withid_encapsulatedclassifier_constructor_args():
    sig = inspect.signature(UML2WithID_EncapsulatedClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_stop_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Stop)


def test_uml2withid_stop_constructor_exists():
    assert callable(UML2WithID_Stop.__init__)


def test_uml2withid_stop_constructor_args():
    sig = inspect.signature(UML2WithID_Stop.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_outputpin_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_OutputPin)


def test_uml2withid_outputpin_constructor_exists():
    assert callable(UML2WithID_OutputPin.__init__)


def test_uml2withid_outputpin_constructor_args():
    sig = inspect.signature(UML2WithID_OutputPin.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_instancevalue_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_InstanceValue)


def test_uml2withid_instancevalue_constructor_exists():
    assert callable(UML2WithID_InstanceValue.__init__)


def test_uml2withid_instancevalue_constructor_args():
    sig = inspect.signature(UML2WithID_InstanceValue.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_mergenode_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_MergeNode)


def test_uml2withid_mergenode_constructor_exists():
    assert callable(UML2WithID_MergeNode.__init__)


def test_uml2withid_mergenode_constructor_args():
    sig = inspect.signature(UML2WithID_MergeNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_changetrigger_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ChangeTrigger)


def test_uml2withid_changetrigger_constructor_exists():
    assert callable(UML2WithID_ChangeTrigger.__init__)


def test_uml2withid_changetrigger_constructor_args():
    sig = inspect.signature(UML2WithID_ChangeTrigger.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_destroyobjectaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_DestroyObjectAction)


def test_uml2withid_destroyobjectaction_constructor_exists():
    assert callable(UML2WithID_DestroyObjectAction.__init__)


def test_uml2withid_destroyobjectaction_constructor_args():
    sig = inspect.signature(UML2WithID_DestroyObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_region_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Region)


def test_uml2withid_region_constructor_exists():
    assert callable(UML2WithID_Region.__init__)


def test_uml2withid_region_constructor_args():
    sig = inspect.signature(UML2WithID_Region.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_interruptibleactivityregion_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_InterruptibleActivityRegion)


def test_uml2withid_interruptibleactivityregion_constructor_exists():
    assert callable(UML2WithID_InterruptibleActivityRegion.__init__)


def test_uml2withid_interruptibleactivityregion_constructor_args():
    sig = inspect.signature(UML2WithID_InterruptibleActivityRegion.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_implementation_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Implementation)


def test_uml2withid_implementation_constructor_exists():
    assert callable(UML2WithID_Implementation.__init__)


def test_uml2withid_implementation_constructor_args():
    sig = inspect.signature(UML2WithID_Implementation.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_extend_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Extend)


def test_uml2withid_extend_constructor_exists():
    assert callable(UML2WithID_Extend.__init__)


def test_uml2withid_extend_constructor_args():
    sig = inspect.signature(UML2WithID_Extend.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_sendsignalaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_SendSignalAction)


def test_uml2withid_sendsignalaction_constructor_exists():
    assert callable(UML2WithID_SendSignalAction.__init__)


def test_uml2withid_sendsignalaction_constructor_args():
    sig = inspect.signature(UML2WithID_SendSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_interaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Interaction)


def test_uml2withid_interaction_constructor_exists():
    assert callable(UML2WithID_Interaction.__init__)


def test_uml2withid_interaction_constructor_args():
    sig = inspect.signature(UML2WithID_Interaction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_reception_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Reception)


def test_uml2withid_reception_constructor_exists():
    assert callable(UML2WithID_Reception.__init__)


def test_uml2withid_reception_constructor_args():
    sig = inspect.signature(UML2WithID_Reception.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_callbehavioraction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_CallBehaviorAction)


def test_uml2withid_callbehavioraction_constructor_exists():
    assert callable(UML2WithID_CallBehaviorAction.__init__)


def test_uml2withid_callbehavioraction_constructor_args():
    sig = inspect.signature(UML2WithID_CallBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_redefinabletemplatesignature_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_RedefinableTemplateSignature)


def test_uml2withid_redefinabletemplatesignature_constructor_exists():
    assert callable(UML2WithID_RedefinableTemplateSignature.__init__)


def test_uml2withid_redefinabletemplatesignature_constructor_args():
    sig = inspect.signature(UML2WithID_RedefinableTemplateSignature.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_instancespecification_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_InstanceSpecification)


def test_uml2withid_instancespecification_constructor_exists():
    assert callable(UML2WithID_InstanceSpecification.__init__)


def test_uml2withid_instancespecification_constructor_args():
    sig = inspect.signature(UML2WithID_InstanceSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_structuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_StructuralFeatureAction)


def test_uml2withid_structuralfeatureaction_constructor_exists():
    assert callable(UML2WithID_StructuralFeatureAction.__init__)


def test_uml2withid_structuralfeatureaction_constructor_args():
    sig = inspect.signature(UML2WithID_StructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_packageableelement_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_PackageableElement)


def test_uml2withid_packageableelement_constructor_exists():
    assert callable(UML2WithID_PackageableElement.__init__)


def test_uml2withid_packageableelement_constructor_args():
    sig = inspect.signature(UML2WithID_PackageableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_primitivetype_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_PrimitiveType)


def test_uml2withid_primitivetype_constructor_exists():
    assert callable(UML2WithID_PrimitiveType.__init__)


def test_uml2withid_primitivetype_constructor_args():
    sig = inspect.signature(UML2WithID_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_BehavioralFeature)


def test_uml2withid_behavioralfeature_constructor_exists():
    assert callable(UML2WithID_BehavioralFeature.__init__)


def test_uml2withid_behavioralfeature_constructor_args():
    sig = inspect.signature(UML2WithID_BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_controlnode_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ControlNode)


def test_uml2withid_controlnode_constructor_exists():
    assert callable(UML2WithID_ControlNode.__init__)


def test_uml2withid_controlnode_constructor_args():
    sig = inspect.signature(UML2WithID_ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_association_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Association)


def test_uml2withid_association_constructor_exists():
    assert callable(UML2WithID_Association.__init__)


def test_uml2withid_association_constructor_args():
    sig = inspect.signature(UML2WithID_Association.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_joinnode_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_JoinNode)


def test_uml2withid_joinnode_constructor_exists():
    assert callable(UML2WithID_JoinNode.__init__)


def test_uml2withid_joinnode_constructor_args():
    sig = inspect.signature(UML2WithID_JoinNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_deployment_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Deployment)


def test_uml2withid_deployment_constructor_exists():
    assert callable(UML2WithID_Deployment.__init__)


def test_uml2withid_deployment_constructor_args():
    sig = inspect.signature(UML2WithID_Deployment.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_finalstate_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_FinalState)


def test_uml2withid_finalstate_constructor_exists():
    assert callable(UML2WithID_FinalState.__init__)


def test_uml2withid_finalstate_constructor_args():
    sig = inspect.signature(UML2WithID_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_component_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Component)


def test_uml2withid_component_constructor_exists():
    assert callable(UML2WithID_Component.__init__)


def test_uml2withid_component_constructor_args():
    sig = inspect.signature(UML2WithID_Component.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_statemachine_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_StateMachine)


def test_uml2withid_statemachine_constructor_exists():
    assert callable(UML2WithID_StateMachine.__init__)


def test_uml2withid_statemachine_constructor_args():
    sig = inspect.signature(UML2WithID_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_stateinvariant_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_StateInvariant)


def test_uml2withid_stateinvariant_constructor_exists():
    assert callable(UML2WithID_StateInvariant.__init__)


def test_uml2withid_stateinvariant_constructor_args():
    sig = inspect.signature(UML2WithID_StateInvariant.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_expansionregion_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ExpansionRegion)


def test_uml2withid_expansionregion_constructor_exists():
    assert callable(UML2WithID_ExpansionRegion.__init__)


def test_uml2withid_expansionregion_constructor_args():
    sig = inspect.signature(UML2WithID_ExpansionRegion.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_callaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_CallAction)


def test_uml2withid_callaction_constructor_exists():
    assert callable(UML2WithID_CallAction.__init__)


def test_uml2withid_callaction_constructor_args():
    sig = inspect.signature(UML2WithID_CallAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_objectnode_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ObjectNode)


def test_uml2withid_objectnode_constructor_exists():
    assert callable(UML2WithID_ObjectNode.__init__)


def test_uml2withid_objectnode_constructor_args():
    sig = inspect.signature(UML2WithID_ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_OpaqueExpression)


def test_uml2withid_opaqueexpression_constructor_exists():
    assert callable(UML2WithID_OpaqueExpression.__init__)


def test_uml2withid_opaqueexpression_constructor_args():
    sig = inspect.signature(UML2WithID_OpaqueExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_generalordering_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_GeneralOrdering)


def test_uml2withid_generalordering_constructor_exists():
    assert callable(UML2WithID_GeneralOrdering.__init__)


def test_uml2withid_generalordering_constructor_args():
    sig = inspect.signature(UML2WithID_GeneralOrdering.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_raiseexceptionaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_RaiseExceptionAction)


def test_uml2withid_raiseexceptionaction_constructor_exists():
    assert callable(UML2WithID_RaiseExceptionAction.__init__)


def test_uml2withid_raiseexceptionaction_constructor_args():
    sig = inspect.signature(UML2WithID_RaiseExceptionAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_variable_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Variable)


def test_uml2withid_variable_constructor_exists():
    assert callable(UML2WithID_Variable.__init__)


def test_uml2withid_variable_constructor_args():
    sig = inspect.signature(UML2WithID_Variable.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_readlinkobjectendaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ReadLinkObjectEndAction)


def test_uml2withid_readlinkobjectendaction_constructor_exists():
    assert callable(UML2WithID_ReadLinkObjectEndAction.__init__)


def test_uml2withid_readlinkobjectendaction_constructor_args():
    sig = inspect.signature(UML2WithID_ReadLinkObjectEndAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_clearassociationaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ClearAssociationAction)


def test_uml2withid_clearassociationaction_constructor_exists():
    assert callable(UML2WithID_ClearAssociationAction.__init__)


def test_uml2withid_clearassociationaction_constructor_args():
    sig = inspect.signature(UML2WithID_ClearAssociationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_directedrelationship_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_DirectedRelationship)


def test_uml2withid_directedrelationship_constructor_exists():
    assert callable(UML2WithID_DirectedRelationship.__init__)


def test_uml2withid_directedrelationship_constructor_args():
    sig = inspect.signature(UML2WithID_DirectedRelationship.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_usage_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Usage)


def test_uml2withid_usage_constructor_exists():
    assert callable(UML2WithID_Usage.__init__)


def test_uml2withid_usage_constructor_args():
    sig = inspect.signature(UML2WithID_Usage.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_literalstring_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_LiteralString)


def test_uml2withid_literalstring_constructor_exists():
    assert callable(UML2WithID_LiteralString.__init__)


def test_uml2withid_literalstring_constructor_args():
    sig = inspect.signature(UML2WithID_LiteralString.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_templateableelement_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_TemplateableElement)


def test_uml2withid_templateableelement_constructor_exists():
    assert callable(UML2WithID_TemplateableElement.__init__)


def test_uml2withid_templateableelement_constructor_args():
    sig = inspect.signature(UML2WithID_TemplateableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_startownedbehavioraction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_StartOwnedBehaviorAction)


def test_uml2withid_startownedbehavioraction_constructor_exists():
    assert callable(UML2WithID_StartOwnedBehaviorAction.__init__)


def test_uml2withid_startownedbehavioraction_constructor_args():
    sig = inspect.signature(UML2WithID_StartOwnedBehaviorAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_deployedartifact_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_DeployedArtifact)


def test_uml2withid_deployedartifact_constructor_exists():
    assert callable(UML2WithID_DeployedArtifact.__init__)


def test_uml2withid_deployedartifact_constructor_args():
    sig = inspect.signature(UML2WithID_DeployedArtifact.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_literalinteger_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_LiteralInteger)


def test_uml2withid_literalinteger_constructor_exists():
    assert callable(UML2WithID_LiteralInteger.__init__)


def test_uml2withid_literalinteger_constructor_args():
    sig = inspect.signature(UML2WithID_LiteralInteger.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_StructuredActivityNode)


def test_uml2withid_structuredactivitynode_constructor_exists():
    assert callable(UML2WithID_StructuredActivityNode.__init__)


def test_uml2withid_structuredactivitynode_constructor_args():
    sig = inspect.signature(UML2WithID_StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_readlinkaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ReadLinkAction)


def test_uml2withid_readlinkaction_constructor_exists():
    assert callable(UML2WithID_ReadLinkAction.__init__)


def test_uml2withid_readlinkaction_constructor_args():
    sig = inspect.signature(UML2WithID_ReadLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_vertex_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Vertex)


def test_uml2withid_vertex_constructor_exists():
    assert callable(UML2WithID_Vertex.__init__)


def test_uml2withid_vertex_constructor_args():
    sig = inspect.signature(UML2WithID_Vertex.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_literalunlimitednatural_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_LiteralUnlimitedNatural)


def test_uml2withid_literalunlimitednatural_constructor_exists():
    assert callable(UML2WithID_LiteralUnlimitedNatural.__init__)


def test_uml2withid_literalunlimitednatural_constructor_args():
    sig = inspect.signature(UML2WithID_LiteralUnlimitedNatural.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_datatype_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_DataType)


def test_uml2withid_datatype_constructor_exists():
    assert callable(UML2WithID_DataType.__init__)


def test_uml2withid_datatype_constructor_args():
    sig = inspect.signature(UML2WithID_DataType.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_loopnode_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_LoopNode)


def test_uml2withid_loopnode_constructor_exists():
    assert callable(UML2WithID_LoopNode.__init__)


def test_uml2withid_loopnode_constructor_args():
    sig = inspect.signature(UML2WithID_LoopNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_transition_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Transition)


def test_uml2withid_transition_constructor_exists():
    assert callable(UML2WithID_Transition.__init__)


def test_uml2withid_transition_constructor_args():
    sig = inspect.signature(UML2WithID_Transition.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_protocoltransition_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ProtocolTransition)


def test_uml2withid_protocoltransition_constructor_exists():
    assert callable(UML2WithID_ProtocolTransition.__init__)


def test_uml2withid_protocoltransition_constructor_args():
    sig = inspect.signature(UML2WithID_ProtocolTransition.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_usecase_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_UseCase)


def test_uml2withid_usecase_constructor_exists():
    assert callable(UML2WithID_UseCase.__init__)


def test_uml2withid_usecase_constructor_args():
    sig = inspect.signature(UML2WithID_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_parameterableclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ParameterableClassifier)


def test_uml2withid_parameterableclassifier_constructor_exists():
    assert callable(UML2WithID_ParameterableClassifier.__init__)


def test_uml2withid_parameterableclassifier_constructor_args():
    sig = inspect.signature(UML2WithID_ParameterableClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_timeinterval_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_TimeInterval)


def test_uml2withid_timeinterval_constructor_exists():
    assert callable(UML2WithID_TimeInterval.__init__)


def test_uml2withid_timeinterval_constructor_args():
    sig = inspect.signature(UML2WithID_TimeInterval.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_protocolconformance_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ProtocolConformance)


def test_uml2withid_protocolconformance_constructor_exists():
    assert callable(UML2WithID_ProtocolConformance.__init__)


def test_uml2withid_protocolconformance_constructor_args():
    sig = inspect.signature(UML2WithID_ProtocolConformance.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_operation_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Operation)


def test_uml2withid_operation_constructor_exists():
    assert callable(UML2WithID_Operation.__init__)


def test_uml2withid_operation_constructor_args():
    sig = inspect.signature(UML2WithID_Operation.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_interactionfragment_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_InteractionFragment)


def test_uml2withid_interactionfragment_constructor_exists():
    assert callable(UML2WithID_InteractionFragment.__init__)


def test_uml2withid_interactionfragment_constructor_args():
    sig = inspect.signature(UML2WithID_InteractionFragment.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_slot_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Slot)


def test_uml2withid_slot_constructor_exists():
    assert callable(UML2WithID_Slot.__init__)


def test_uml2withid_slot_constructor_args():
    sig = inspect.signature(UML2WithID_Slot.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_redefinableelement_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_RedefinableElement)


def test_uml2withid_redefinableelement_constructor_exists():
    assert callable(UML2WithID_RedefinableElement.__init__)


def test_uml2withid_redefinableelement_constructor_args():
    sig = inspect.signature(UML2WithID_RedefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_readlinkobjectendqualifieraction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ReadLinkObjectEndQualifierAction)


def test_uml2withid_readlinkobjectendqualifieraction_constructor_exists():
    assert callable(UML2WithID_ReadLinkObjectEndQualifierAction.__init__)


def test_uml2withid_readlinkobjectendqualifieraction_constructor_args():
    sig = inspect.signature(UML2WithID_ReadLinkObjectEndQualifierAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_variableaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_VariableAction)


def test_uml2withid_variableaction_constructor_exists():
    assert callable(UML2WithID_VariableAction.__init__)


def test_uml2withid_variableaction_constructor_args():
    sig = inspect.signature(UML2WithID_VariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_activityfinalnode_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ActivityFinalNode)


def test_uml2withid_activityfinalnode_constructor_exists():
    assert callable(UML2WithID_ActivityFinalNode.__init__)


def test_uml2withid_activityfinalnode_constructor_args():
    sig = inspect.signature(UML2WithID_ActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_interval_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Interval)


def test_uml2withid_interval_constructor_exists():
    assert callable(UML2WithID_Interval.__init__)


def test_uml2withid_interval_constructor_args():
    sig = inspect.signature(UML2WithID_Interval.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_linkendcreationdata_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_LinkEndCreationData)


def test_uml2withid_linkendcreationdata_constructor_exists():
    assert callable(UML2WithID_LinkEndCreationData.__init__)


def test_uml2withid_linkendcreationdata_constructor_args():
    sig = inspect.signature(UML2WithID_LinkEndCreationData.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_readextentaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ReadExtentAction)


def test_uml2withid_readextentaction_constructor_exists():
    assert callable(UML2WithID_ReadExtentAction.__init__)


def test_uml2withid_readextentaction_constructor_args():
    sig = inspect.signature(UML2WithID_ReadExtentAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_pseudostate_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Pseudostate)


def test_uml2withid_pseudostate_constructor_exists():
    assert callable(UML2WithID_Pseudostate.__init__)


def test_uml2withid_pseudostate_constructor_args():
    sig = inspect.signature(UML2WithID_Pseudostate.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_destroylinkaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_DestroyLinkAction)


def test_uml2withid_destroylinkaction_constructor_exists():
    assert callable(UML2WithID_DestroyLinkAction.__init__)


def test_uml2withid_destroylinkaction_constructor_args():
    sig = inspect.signature(UML2WithID_DestroyLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_flowfinalnode_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_FlowFinalNode)


def test_uml2withid_flowfinalnode_constructor_exists():
    assert callable(UML2WithID_FlowFinalNode.__init__)


def test_uml2withid_flowfinalnode_constructor_args():
    sig = inspect.signature(UML2WithID_FlowFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_clearstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ClearStructuralFeatureAction)


def test_uml2withid_clearstructuralfeatureaction_constructor_exists():
    assert callable(UML2WithID_ClearStructuralFeatureAction.__init__)


def test_uml2withid_clearstructuralfeatureaction_constructor_args():
    sig = inspect.signature(UML2WithID_ClearStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_combinedfragment_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_CombinedFragment)


def test_uml2withid_combinedfragment_constructor_exists():
    assert callable(UML2WithID_CombinedFragment.__init__)


def test_uml2withid_combinedfragment_constructor_args():
    sig = inspect.signature(UML2WithID_CombinedFragment.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_continuation_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Continuation)


def test_uml2withid_continuation_constructor_exists():
    assert callable(UML2WithID_Continuation.__init__)


def test_uml2withid_continuation_constructor_args():
    sig = inspect.signature(UML2WithID_Continuation.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_forknode_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ForkNode)


def test_uml2withid_forknode_constructor_exists():
    assert callable(UML2WithID_ForkNode.__init__)


def test_uml2withid_forknode_constructor_args():
    sig = inspect.signature(UML2WithID_ForkNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_relationship_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Relationship)


def test_uml2withid_relationship_constructor_exists():
    assert callable(UML2WithID_Relationship.__init__)


def test_uml2withid_relationship_constructor_args():
    sig = inspect.signature(UML2WithID_Relationship.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_associationclass_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_AssociationClass)


def test_uml2withid_associationclass_constructor_exists():
    assert callable(UML2WithID_AssociationClass.__init__)


def test_uml2withid_associationclass_constructor_args():
    sig = inspect.signature(UML2WithID_AssociationClass.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_protocolstatemachine_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ProtocolStateMachine)


def test_uml2withid_protocolstatemachine_constructor_exists():
    assert callable(UML2WithID_ProtocolStateMachine.__init__)


def test_uml2withid_protocolstatemachine_constructor_args():
    sig = inspect.signature(UML2WithID_ProtocolStateMachine.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_activityedge_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ActivityEdge)


def test_uml2withid_activityedge_constructor_exists():
    assert callable(UML2WithID_ActivityEdge.__init__)


def test_uml2withid_activityedge_constructor_args():
    sig = inspect.signature(UML2WithID_ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_signal_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Signal)


def test_uml2withid_signal_constructor_exists():
    assert callable(UML2WithID_Signal.__init__)


def test_uml2withid_signal_constructor_args():
    sig = inspect.signature(UML2WithID_Signal.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_durationobservationaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_DurationObservationAction)


def test_uml2withid_durationobservationaction_constructor_exists():
    assert callable(UML2WithID_DurationObservationAction.__init__)


def test_uml2withid_durationobservationaction_constructor_args():
    sig = inspect.signature(UML2WithID_DurationObservationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_permission_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Permission)


def test_uml2withid_permission_constructor_exists():
    assert callable(UML2WithID_Permission.__init__)


def test_uml2withid_permission_constructor_args():
    sig = inspect.signature(UML2WithID_Permission.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_artifact_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Artifact)


def test_uml2withid_artifact_constructor_exists():
    assert callable(UML2WithID_Artifact.__init__)


def test_uml2withid_artifact_constructor_args():
    sig = inspect.signature(UML2WithID_Artifact.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_readstructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ReadStructuralFeatureAction)


def test_uml2withid_readstructuralfeatureaction_constructor_exists():
    assert callable(UML2WithID_ReadStructuralFeatureAction.__init__)


def test_uml2withid_readstructuralfeatureaction_constructor_args():
    sig = inspect.signature(UML2WithID_ReadStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_messageend_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_MessageEnd)


def test_uml2withid_messageend_constructor_exists():
    assert callable(UML2WithID_MessageEnd.__init__)


def test_uml2withid_messageend_constructor_args():
    sig = inspect.signature(UML2WithID_MessageEnd.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_calltrigger_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_CallTrigger)


def test_uml2withid_calltrigger_constructor_exists():
    assert callable(UML2WithID_CallTrigger.__init__)


def test_uml2withid_calltrigger_constructor_args():
    sig = inspect.signature(UML2WithID_CallTrigger.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_comment_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Comment)


def test_uml2withid_comment_constructor_exists():
    assert callable(UML2WithID_Comment.__init__)


def test_uml2withid_comment_constructor_args():
    sig = inspect.signature(UML2WithID_Comment.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_durationconstraint_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_DurationConstraint)


def test_uml2withid_durationconstraint_constructor_exists():
    assert callable(UML2WithID_DurationConstraint.__init__)


def test_uml2withid_durationconstraint_constructor_args():
    sig = inspect.signature(UML2WithID_DurationConstraint.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_valuespecification_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ValueSpecification)


def test_uml2withid_valuespecification_constructor_exists():
    assert callable(UML2WithID_ValueSpecification.__init__)


def test_uml2withid_valuespecification_constructor_args():
    sig = inspect.signature(UML2WithID_ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_parameter_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Parameter)


def test_uml2withid_parameter_constructor_exists():
    assert callable(UML2WithID_Parameter.__init__)


def test_uml2withid_parameter_constructor_args():
    sig = inspect.signature(UML2WithID_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_activitypartition_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ActivityPartition)


def test_uml2withid_activitypartition_constructor_exists():
    assert callable(UML2WithID_ActivityPartition.__init__)


def test_uml2withid_activitypartition_constructor_args():
    sig = inspect.signature(UML2WithID_ActivityPartition.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_anytrigger_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_AnyTrigger)


def test_uml2withid_anytrigger_constructor_exists():
    assert callable(UML2WithID_AnyTrigger.__init__)


def test_uml2withid_anytrigger_constructor_args():
    sig = inspect.signature(UML2WithID_AnyTrigger.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_templatebinding_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_TemplateBinding)


def test_uml2withid_templatebinding_constructor_exists():
    assert callable(UML2WithID_TemplateBinding.__init__)


def test_uml2withid_templatebinding_constructor_args():
    sig = inspect.signature(UML2WithID_TemplateBinding.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_constraint_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Constraint)


def test_uml2withid_constraint_constructor_exists():
    assert callable(UML2WithID_Constraint.__init__)


def test_uml2withid_constraint_constructor_args():
    sig = inspect.signature(UML2WithID_Constraint.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_enumeration_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Enumeration)


def test_uml2withid_enumeration_constructor_exists():
    assert callable(UML2WithID_Enumeration.__init__)


def test_uml2withid_enumeration_constructor_args():
    sig = inspect.signature(UML2WithID_Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_BehavioredClassifier)


def test_uml2withid_behavioredclassifier_constructor_exists():
    assert callable(UML2WithID_BehavioredClassifier.__init__)


def test_uml2withid_behavioredclassifier_constructor_args():
    sig = inspect.signature(UML2WithID_BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_removevariablevalueaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_RemoveVariableValueAction)


def test_uml2withid_removevariablevalueaction_constructor_exists():
    assert callable(UML2WithID_RemoveVariableValueAction.__init__)


def test_uml2withid_removevariablevalueaction_constructor_args():
    sig = inspect.signature(UML2WithID_RemoveVariableValueAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_literalnull_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_LiteralNull)


def test_uml2withid_literalnull_constructor_exists():
    assert callable(UML2WithID_LiteralNull.__init__)


def test_uml2withid_literalnull_constructor_args():
    sig = inspect.signature(UML2WithID_LiteralNull.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_connectableelement_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ConnectableElement)


def test_uml2withid_connectableelement_constructor_exists():
    assert callable(UML2WithID_ConnectableElement.__init__)


def test_uml2withid_connectableelement_constructor_args():
    sig = inspect.signature(UML2WithID_ConnectableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_timeobservationaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_TimeObservationAction)


def test_uml2withid_timeobservationaction_constructor_exists():
    assert callable(UML2WithID_TimeObservationAction.__init__)


def test_uml2withid_timeobservationaction_constructor_args():
    sig = inspect.signature(UML2WithID_TimeObservationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_class_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Class)


def test_uml2withid_class_constructor_exists():
    assert callable(UML2WithID_Class.__init__)


def test_uml2withid_class_constructor_args():
    sig = inspect.signature(UML2WithID_Class.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_linkenddata_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_LinkEndData)


def test_uml2withid_linkenddata_constructor_exists():
    assert callable(UML2WithID_LinkEndData.__init__)


def test_uml2withid_linkenddata_constructor_args():
    sig = inspect.signature(UML2WithID_LinkEndData.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_timetrigger_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_TimeTrigger)


def test_uml2withid_timetrigger_constructor_exists():
    assert callable(UML2WithID_TimeTrigger.__init__)


def test_uml2withid_timetrigger_constructor_args():
    sig = inspect.signature(UML2WithID_TimeTrigger.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_type_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Type)


def test_uml2withid_type_constructor_exists():
    assert callable(UML2WithID_Type.__init__)


def test_uml2withid_type_constructor_args():
    sig = inspect.signature(UML2WithID_Type.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_stringexpression_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_StringExpression)


def test_uml2withid_stringexpression_constructor_exists():
    assert callable(UML2WithID_StringExpression.__init__)


def test_uml2withid_stringexpression_constructor_args():
    sig = inspect.signature(UML2WithID_StringExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_calloperationaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_CallOperationAction)


def test_uml2withid_calloperationaction_constructor_exists():
    assert callable(UML2WithID_CallOperationAction.__init__)


def test_uml2withid_calloperationaction_constructor_args():
    sig = inspect.signature(UML2WithID_CallOperationAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_centralbuffernode_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_CentralBufferNode)


def test_uml2withid_centralbuffernode_constructor_exists():
    assert callable(UML2WithID_CentralBufferNode.__init__)


def test_uml2withid_centralbuffernode_constructor_args():
    sig = inspect.signature(UML2WithID_CentralBufferNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_parameterableelement_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ParameterableElement)


def test_uml2withid_parameterableelement_constructor_exists():
    assert callable(UML2WithID_ParameterableElement.__init__)


def test_uml2withid_parameterableelement_constructor_args():
    sig = inspect.signature(UML2WithID_ParameterableElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_profileapplication_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ProfileApplication)


def test_uml2withid_profileapplication_constructor_exists():
    assert callable(UML2WithID_ProfileApplication.__init__)


def test_uml2withid_profileapplication_constructor_args():
    sig = inspect.signature(UML2WithID_ProfileApplication.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_expansionnode_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ExpansionNode)


def test_uml2withid_expansionnode_constructor_exists():
    assert callable(UML2WithID_ExpansionNode.__init__)


def test_uml2withid_expansionnode_constructor_args():
    sig = inspect.signature(UML2WithID_ExpansionNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_collaboration_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Collaboration)


def test_uml2withid_collaboration_constructor_exists():
    assert callable(UML2WithID_Collaboration.__init__)


def test_uml2withid_collaboration_constructor_args():
    sig = inspect.signature(UML2WithID_Collaboration.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_state_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_State)


def test_uml2withid_state_constructor_exists():
    assert callable(UML2WithID_State.__init__)


def test_uml2withid_state_constructor_args():
    sig = inspect.signature(UML2WithID_State.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_connectorend_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ConnectorEnd)


def test_uml2withid_connectorend_constructor_exists():
    assert callable(UML2WithID_ConnectorEnd.__init__)


def test_uml2withid_connectorend_constructor_args():
    sig = inspect.signature(UML2WithID_ConnectorEnd.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_include_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Include)


def test_uml2withid_include_constructor_exists():
    assert callable(UML2WithID_Include.__init__)


def test_uml2withid_include_constructor_args():
    sig = inspect.signature(UML2WithID_Include.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_profile_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Profile)


def test_uml2withid_profile_constructor_exists():
    assert callable(UML2WithID_Profile.__init__)


def test_uml2withid_profile_constructor_args():
    sig = inspect.signature(UML2WithID_Profile.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_duration_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Duration)


def test_uml2withid_duration_constructor_exists():
    assert callable(UML2WithID_Duration.__init__)


def test_uml2withid_duration_constructor_args():
    sig = inspect.signature(UML2WithID_Duration.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_packageimport_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_PackageImport)


def test_uml2withid_packageimport_constructor_exists():
    assert callable(UML2WithID_PackageImport.__init__)


def test_uml2withid_packageimport_constructor_args():
    sig = inspect.signature(UML2WithID_PackageImport.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_interface_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Interface)


def test_uml2withid_interface_constructor_exists():
    assert callable(UML2WithID_Interface.__init__)


def test_uml2withid_interface_constructor_args():
    sig = inspect.signature(UML2WithID_Interface.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_executionoccurrence_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ExecutionOccurrence)


def test_uml2withid_executionoccurrence_constructor_exists():
    assert callable(UML2WithID_ExecutionOccurrence.__init__)


def test_uml2withid_executionoccurrence_constructor_args():
    sig = inspect.signature(UML2WithID_ExecutionOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_reclassifyobjectaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ReclassifyObjectAction)


def test_uml2withid_reclassifyobjectaction_constructor_exists():
    assert callable(UML2WithID_ReclassifyObjectAction.__init__)


def test_uml2withid_reclassifyobjectaction_constructor_args():
    sig = inspect.signature(UML2WithID_ReclassifyObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_messagetrigger_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_MessageTrigger)


def test_uml2withid_messagetrigger_constructor_exists():
    assert callable(UML2WithID_MessageTrigger.__init__)


def test_uml2withid_messagetrigger_constructor_args():
    sig = inspect.signature(UML2WithID_MessageTrigger.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_substitution_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Substitution)


def test_uml2withid_substitution_constructor_exists():
    assert callable(UML2WithID_Substitution.__init__)


def test_uml2withid_substitution_constructor_args():
    sig = inspect.signature(UML2WithID_Substitution.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_inputpin_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_InputPin)


def test_uml2withid_inputpin_constructor_exists():
    assert callable(UML2WithID_InputPin.__init__)


def test_uml2withid_inputpin_constructor_args():
    sig = inspect.signature(UML2WithID_InputPin.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_expression_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Expression)


def test_uml2withid_expression_constructor_exists():
    assert callable(UML2WithID_Expression.__init__)


def test_uml2withid_expression_constructor_args():
    sig = inspect.signature(UML2WithID_Expression.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_valuepin_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ValuePin)


def test_uml2withid_valuepin_constructor_exists():
    assert callable(UML2WithID_ValuePin.__init__)


def test_uml2withid_valuepin_constructor_args():
    sig = inspect.signature(UML2WithID_ValuePin.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_qualifiervalue_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_QualifierValue)


def test_uml2withid_qualifiervalue_constructor_exists():
    assert callable(UML2WithID_QualifierValue.__init__)


def test_uml2withid_qualifiervalue_constructor_args():
    sig = inspect.signature(UML2WithID_QualifierValue.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_collaborationoccurrence_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_CollaborationOccurrence)


def test_uml2withid_collaborationoccurrence_constructor_exists():
    assert callable(UML2WithID_CollaborationOccurrence.__init__)


def test_uml2withid_collaborationoccurrence_constructor_args():
    sig = inspect.signature(UML2WithID_CollaborationOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_createobjectaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_CreateObjectAction)


def test_uml2withid_createobjectaction_constructor_exists():
    assert callable(UML2WithID_CreateObjectAction.__init__)


def test_uml2withid_createobjectaction_constructor_args():
    sig = inspect.signature(UML2WithID_CreateObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_templatesignature_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_TemplateSignature)


def test_uml2withid_templatesignature_constructor_exists():
    assert callable(UML2WithID_TemplateSignature.__init__)


def test_uml2withid_templatesignature_constructor_args():
    sig = inspect.signature(UML2WithID_TemplateSignature.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_abstraction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Abstraction)


def test_uml2withid_abstraction_constructor_exists():
    assert callable(UML2WithID_Abstraction.__init__)


def test_uml2withid_abstraction_constructor_args():
    sig = inspect.signature(UML2WithID_Abstraction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_trigger_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Trigger)


def test_uml2withid_trigger_constructor_exists():
    assert callable(UML2WithID_Trigger.__init__)


def test_uml2withid_trigger_constructor_args():
    sig = inspect.signature(UML2WithID_Trigger.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_connector_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Connector)


def test_uml2withid_connector_constructor_exists():
    assert callable(UML2WithID_Connector.__init__)


def test_uml2withid_connector_constructor_args():
    sig = inspect.signature(UML2WithID_Connector.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_literalboolean_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_LiteralBoolean)


def test_uml2withid_literalboolean_constructor_exists():
    assert callable(UML2WithID_LiteralBoolean.__init__)


def test_uml2withid_literalboolean_constructor_args():
    sig = inspect.signature(UML2WithID_LiteralBoolean.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_broadcastsignalaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_BroadcastSignalAction)


def test_uml2withid_broadcastsignalaction_constructor_exists():
    assert callable(UML2WithID_BroadcastSignalAction.__init__)


def test_uml2withid_broadcastsignalaction_constructor_args():
    sig = inspect.signature(UML2WithID_BroadcastSignalAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_objectflow_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ObjectFlow)


def test_uml2withid_objectflow_constructor_exists():
    assert callable(UML2WithID_ObjectFlow.__init__)


def test_uml2withid_objectflow_constructor_args():
    sig = inspect.signature(UML2WithID_ObjectFlow.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_packagemerge_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_PackageMerge)


def test_uml2withid_packagemerge_constructor_exists():
    assert callable(UML2WithID_PackageMerge.__init__)


def test_uml2withid_packagemerge_constructor_args():
    sig = inspect.signature(UML2WithID_PackageMerge.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_linkaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_LinkAction)


def test_uml2withid_linkaction_constructor_exists():
    assert callable(UML2WithID_LinkAction.__init__)


def test_uml2withid_linkaction_constructor_args():
    sig = inspect.signature(UML2WithID_LinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_finalnode_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_FinalNode)


def test_uml2withid_finalnode_constructor_exists():
    assert callable(UML2WithID_FinalNode.__init__)


def test_uml2withid_finalnode_constructor_args():
    sig = inspect.signature(UML2WithID_FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_executionenvironment_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ExecutionEnvironment)


def test_uml2withid_executionenvironment_constructor_exists():
    assert callable(UML2WithID_ExecutionEnvironment.__init__)


def test_uml2withid_executionenvironment_constructor_args():
    sig = inspect.signature(UML2WithID_ExecutionEnvironment.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_message_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Message)


def test_uml2withid_message_constructor_exists():
    assert callable(UML2WithID_Message.__init__)


def test_uml2withid_message_constructor_args():
    sig = inspect.signature(UML2WithID_Message.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_datastorenode_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_DataStoreNode)


def test_uml2withid_datastorenode_constructor_exists():
    assert callable(UML2WithID_DataStoreNode.__init__)


def test_uml2withid_datastorenode_constructor_args():
    sig = inspect.signature(UML2WithID_DataStoreNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_classifiertemplateparameter_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ClassifierTemplateParameter)


def test_uml2withid_classifiertemplateparameter_constructor_exists():
    assert callable(UML2WithID_ClassifierTemplateParameter.__init__)


def test_uml2withid_classifiertemplateparameter_constructor_args():
    sig = inspect.signature(UML2WithID_ClassifierTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_clearvariableaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ClearVariableAction)


def test_uml2withid_clearvariableaction_constructor_exists():
    assert callable(UML2WithID_ClearVariableAction.__init__)


def test_uml2withid_clearvariableaction_constructor_args():
    sig = inspect.signature(UML2WithID_ClearVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_manifestation_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Manifestation)


def test_uml2withid_manifestation_constructor_exists():
    assert callable(UML2WithID_Manifestation.__init__)


def test_uml2withid_manifestation_constructor_args():
    sig = inspect.signature(UML2WithID_Manifestation.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_interactionconstraint_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_InteractionConstraint)


def test_uml2withid_interactionconstraint_constructor_exists():
    assert callable(UML2WithID_InteractionConstraint.__init__)


def test_uml2withid_interactionconstraint_constructor_args():
    sig = inspect.signature(UML2WithID_InteractionConstraint.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_communicationpath_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_CommunicationPath)


def test_uml2withid_communicationpath_constructor_exists():
    assert callable(UML2WithID_CommunicationPath.__init__)


def test_uml2withid_communicationpath_constructor_args():
    sig = inspect.signature(UML2WithID_CommunicationPath.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_actor_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Actor)


def test_uml2withid_actor_constructor_exists():
    assert callable(UML2WithID_Actor.__init__)


def test_uml2withid_actor_constructor_args():
    sig = inspect.signature(UML2WithID_Actor.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_extensionend_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ExtensionEnd)


def test_uml2withid_extensionend_constructor_exists():
    assert callable(UML2WithID_ExtensionEnd.__init__)


def test_uml2withid_extensionend_constructor_args():
    sig = inspect.signature(UML2WithID_ExtensionEnd.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_generalizationset_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_GeneralizationSet)


def test_uml2withid_generalizationset_constructor_exists():
    assert callable(UML2WithID_GeneralizationSet.__init__)


def test_uml2withid_generalizationset_constructor_args():
    sig = inspect.signature(UML2WithID_GeneralizationSet.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_StructuralFeature)


def test_uml2withid_structuralfeature_constructor_exists():
    assert callable(UML2WithID_StructuralFeature.__init__)


def test_uml2withid_structuralfeature_constructor_args():
    sig = inspect.signature(UML2WithID_StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_templateableclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_TemplateableClassifier)


def test_uml2withid_templateableclassifier_constructor_exists():
    assert callable(UML2WithID_TemplateableClassifier.__init__)


def test_uml2withid_templateableclassifier_constructor_args():
    sig = inspect.signature(UML2WithID_TemplateableClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_device_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Device)


def test_uml2withid_device_constructor_exists():
    assert callable(UML2WithID_Device.__init__)


def test_uml2withid_device_constructor_args():
    sig = inspect.signature(UML2WithID_Device.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_primitivefunction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_PrimitiveFunction)


def test_uml2withid_primitivefunction_constructor_exists():
    assert callable(UML2WithID_PrimitiveFunction.__init__)


def test_uml2withid_primitivefunction_constructor_args():
    sig = inspect.signature(UML2WithID_PrimitiveFunction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_connectionpointreference_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ConnectionPointReference)


def test_uml2withid_connectionpointreference_constructor_exists():
    assert callable(UML2WithID_ConnectionPointReference.__init__)


def test_uml2withid_connectionpointreference_constructor_args():
    sig = inspect.signature(UML2WithID_ConnectionPointReference.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_partdecomposition_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_PartDecomposition)


def test_uml2withid_partdecomposition_constructor_exists():
    assert callable(UML2WithID_PartDecomposition.__init__)


def test_uml2withid_partdecomposition_constructor_args():
    sig = inspect.signature(UML2WithID_PartDecomposition.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_readselfaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ReadSelfAction)


def test_uml2withid_readselfaction_constructor_exists():
    assert callable(UML2WithID_ReadSelfAction.__init__)


def test_uml2withid_readselfaction_constructor_args():
    sig = inspect.signature(UML2WithID_ReadSelfAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_MultiplicityElement)


def test_uml2withid_multiplicityelement_constructor_exists():
    assert callable(UML2WithID_MultiplicityElement.__init__)


def test_uml2withid_multiplicityelement_constructor_args():
    sig = inspect.signature(UML2WithID_MultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_durationinterval_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_DurationInterval)


def test_uml2withid_durationinterval_constructor_exists():
    assert callable(UML2WithID_DurationInterval.__init__)


def test_uml2withid_durationinterval_constructor_args():
    sig = inspect.signature(UML2WithID_DurationInterval.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_accepteventaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_AcceptEventAction)


def test_uml2withid_accepteventaction_constructor_exists():
    assert callable(UML2WithID_AcceptEventAction.__init__)


def test_uml2withid_accepteventaction_constructor_args():
    sig = inspect.signature(UML2WithID_AcceptEventAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_signaltrigger_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_SignalTrigger)


def test_uml2withid_signaltrigger_constructor_exists():
    assert callable(UML2WithID_SignalTrigger.__init__)


def test_uml2withid_signaltrigger_constructor_args():
    sig = inspect.signature(UML2WithID_SignalTrigger.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_sendobjectaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_SendObjectAction)


def test_uml2withid_sendobjectaction_constructor_exists():
    assert callable(UML2WithID_SendObjectAction.__init__)


def test_uml2withid_sendobjectaction_constructor_args():
    sig = inspect.signature(UML2WithID_SendObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_writestructuralfeatureaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_WriteStructuralFeatureAction)


def test_uml2withid_writestructuralfeatureaction_constructor_exists():
    assert callable(UML2WithID_WriteStructuralFeatureAction.__init__)


def test_uml2withid_writestructuralfeatureaction_constructor_args():
    sig = inspect.signature(UML2WithID_WriteStructuralFeatureAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_lifeline_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Lifeline)


def test_uml2withid_lifeline_constructor_exists():
    assert callable(UML2WithID_Lifeline.__init__)


def test_uml2withid_lifeline_constructor_args():
    sig = inspect.signature(UML2WithID_Lifeline.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_readvariableaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ReadVariableAction)


def test_uml2withid_readvariableaction_constructor_exists():
    assert callable(UML2WithID_ReadVariableAction.__init__)


def test_uml2withid_readvariableaction_constructor_args():
    sig = inspect.signature(UML2WithID_ReadVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_literalspecification_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_LiteralSpecification)


def test_uml2withid_literalspecification_constructor_exists():
    assert callable(UML2WithID_LiteralSpecification.__init__)


def test_uml2withid_literalspecification_constructor_args():
    sig = inspect.signature(UML2WithID_LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_decisionnode_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_DecisionNode)


def test_uml2withid_decisionnode_constructor_exists():
    assert callable(UML2WithID_DecisionNode.__init__)


def test_uml2withid_decisionnode_constructor_args():
    sig = inspect.signature(UML2WithID_DecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_deploymenttarget_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_DeploymentTarget)


def test_uml2withid_deploymenttarget_constructor_exists():
    assert callable(UML2WithID_DeploymentTarget.__init__)


def test_uml2withid_deploymenttarget_constructor_args():
    sig = inspect.signature(UML2WithID_DeploymentTarget.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_readisclassifiedobjectaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ReadIsClassifiedObjectAction)


def test_uml2withid_readisclassifiedobjectaction_constructor_exists():
    assert callable(UML2WithID_ReadIsClassifiedObjectAction.__init__)


def test_uml2withid_readisclassifiedobjectaction_constructor_args():
    sig = inspect.signature(UML2WithID_ReadIsClassifiedObjectAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_package_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Package)


def test_uml2withid_package_constructor_exists():
    assert callable(UML2WithID_Package.__init__)


def test_uml2withid_package_constructor_args():
    sig = inspect.signature(UML2WithID_Package.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_typedelement_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_TypedElement)


def test_uml2withid_typedelement_constructor_exists():
    assert callable(UML2WithID_TypedElement.__init__)


def test_uml2withid_typedelement_constructor_args():
    sig = inspect.signature(UML2WithID_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_informationflow_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_InformationFlow)


def test_uml2withid_informationflow_constructor_exists():
    assert callable(UML2WithID_InformationFlow.__init__)


def test_uml2withid_informationflow_constructor_args():
    sig = inspect.signature(UML2WithID_InformationFlow.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_interactionoccurrence_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_InteractionOccurrence)


def test_uml2withid_interactionoccurrence_constructor_exists():
    assert callable(UML2WithID_InteractionOccurrence.__init__)


def test_uml2withid_interactionoccurrence_constructor_args():
    sig = inspect.signature(UML2WithID_InteractionOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_activityparameternode_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ActivityParameterNode)


def test_uml2withid_activityparameternode_constructor_exists():
    assert callable(UML2WithID_ActivityParameterNode.__init__)


def test_uml2withid_activityparameternode_constructor_args():
    sig = inspect.signature(UML2WithID_ActivityParameterNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_writelinkaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_WriteLinkAction)


def test_uml2withid_writelinkaction_constructor_exists():
    assert callable(UML2WithID_WriteLinkAction.__init__)


def test_uml2withid_writelinkaction_constructor_args():
    sig = inspect.signature(UML2WithID_WriteLinkAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_elementimport_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ElementImport)


def test_uml2withid_elementimport_constructor_exists():
    assert callable(UML2WithID_ElementImport.__init__)


def test_uml2withid_elementimport_constructor_args():
    sig = inspect.signature(UML2WithID_ElementImport.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_templateparametersubstitution_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_TemplateParameterSubstitution)


def test_uml2withid_templateparametersubstitution_constructor_exists():
    assert callable(UML2WithID_TemplateParameterSubstitution.__init__)


def test_uml2withid_templateparametersubstitution_constructor_args():
    sig = inspect.signature(UML2WithID_TemplateParameterSubstitution.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_removestructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_RemoveStructuralFeatureValueAction)


def test_uml2withid_removestructuralfeaturevalueaction_constructor_exists():
    assert callable(UML2WithID_RemoveStructuralFeatureValueAction.__init__)


def test_uml2withid_removestructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(UML2WithID_RemoveStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_structuredclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_StructuredClassifier)


def test_uml2withid_structuredclassifier_constructor_exists():
    assert callable(UML2WithID_StructuredClassifier.__init__)


def test_uml2withid_structuredclassifier_constructor_args():
    sig = inspect.signature(UML2WithID_StructuredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_operationtemplateparameter_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_OperationTemplateParameter)


def test_uml2withid_operationtemplateparameter_constructor_exists():
    assert callable(UML2WithID_OperationTemplateParameter.__init__)


def test_uml2withid_operationtemplateparameter_constructor_args():
    sig = inspect.signature(UML2WithID_OperationTemplateParameter.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_conditionalnode_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ConditionalNode)


def test_uml2withid_conditionalnode_constructor_exists():
    assert callable(UML2WithID_ConditionalNode.__init__)


def test_uml2withid_conditionalnode_constructor_args():
    sig = inspect.signature(UML2WithID_ConditionalNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_acceptcallaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_AcceptCallAction)


def test_uml2withid_acceptcallaction_constructor_exists():
    assert callable(UML2WithID_AcceptCallAction.__init__)


def test_uml2withid_acceptcallaction_constructor_args():
    sig = inspect.signature(UML2WithID_AcceptCallAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_feature_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Feature)


def test_uml2withid_feature_constructor_exists():
    assert callable(UML2WithID_Feature.__init__)


def test_uml2withid_feature_constructor_args():
    sig = inspect.signature(UML2WithID_Feature.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_writevariableaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_WriteVariableAction)


def test_uml2withid_writevariableaction_constructor_exists():
    assert callable(UML2WithID_WriteVariableAction.__init__)


def test_uml2withid_writevariableaction_constructor_args():
    sig = inspect.signature(UML2WithID_WriteVariableAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_behavior_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Behavior)


def test_uml2withid_behavior_constructor_exists():
    assert callable(UML2WithID_Behavior.__init__)


def test_uml2withid_behavior_constructor_args():
    sig = inspect.signature(UML2WithID_Behavior.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_informationitem_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_InformationItem)


def test_uml2withid_informationitem_constructor_exists():
    assert callable(UML2WithID_InformationItem.__init__)


def test_uml2withid_informationitem_constructor_args():
    sig = inspect.signature(UML2WithID_InformationItem.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_dependency_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Dependency)


def test_uml2withid_dependency_constructor_exists():
    assert callable(UML2WithID_Dependency.__init__)


def test_uml2withid_dependency_constructor_args():
    sig = inspect.signature(UML2WithID_Dependency.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_classifier_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Classifier)


def test_uml2withid_classifier_constructor_exists():
    assert callable(UML2WithID_Classifier.__init__)


def test_uml2withid_classifier_constructor_args():
    sig = inspect.signature(UML2WithID_Classifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_applyfunctionaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ApplyFunctionAction)


def test_uml2withid_applyfunctionaction_constructor_exists():
    assert callable(UML2WithID_ApplyFunctionAction.__init__)


def test_uml2withid_applyfunctionaction_constructor_args():
    sig = inspect.signature(UML2WithID_ApplyFunctionAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_extensionpoint_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ExtensionPoint)


def test_uml2withid_extensionpoint_constructor_exists():
    assert callable(UML2WithID_ExtensionPoint.__init__)


def test_uml2withid_extensionpoint_constructor_args():
    sig = inspect.signature(UML2WithID_ExtensionPoint.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_addstructuralfeaturevalueaction_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_AddStructuralFeatureValueAction)


def test_uml2withid_addstructuralfeaturevalueaction_constructor_exists():
    assert callable(UML2WithID_AddStructuralFeatureValueAction.__init__)


def test_uml2withid_addstructuralfeaturevalueaction_constructor_args():
    sig = inspect.signature(UML2WithID_AddStructuralFeatureValueAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_parameterset_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_ParameterSet)


def test_uml2withid_parameterset_constructor_exists():
    assert callable(UML2WithID_ParameterSet.__init__)


def test_uml2withid_parameterset_constructor_args():
    sig = inspect.signature(UML2WithID_ParameterSet.__init__)
    params = list(sig.parameters.keys())



def test_messageend_is_not_abstract():
    assert not inspect.isabstract(MessageEnd)


def test_messageend_constructor_exists():
    assert callable(MessageEnd.__init__)


def test_messageend_constructor_args():
    sig = inspect.signature(MessageEnd.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_eventoccurrence_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_EventOccurrence)


def test_uml2withid_eventoccurrence_constructor_exists():
    assert callable(UML2WithID_EventOccurrence.__init__)


def test_uml2withid_eventoccurrence_constructor_args():
    sig = inspect.signature(UML2WithID_EventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_uml2withid_gate_is_not_abstract():
    assert not inspect.isabstract(UML2WithID_Gate)


def test_uml2withid_gate_constructor_exists():
    assert callable(UML2WithID_Gate.__init__)


def test_uml2withid_gate_constructor_args():
    sig = inspect.signature(UML2WithID_Gate.__init__)
    params = list(sig.parameters.keys())


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
ConnectableElement_strategy = st.builds(
    ConnectableElement,
)
Association_strategy = st.builds(
    Association,
)
TemplateParameter_strategy = st.builds(
    TemplateParameter,
)
CentralBufferNode_strategy = st.builds(
    CentralBufferNode,
)
VariableAction_strategy = st.builds(
    VariableAction,
)
WriteStructuralFeatureAction_strategy = st.builds(
    WriteStructuralFeatureAction,
)
StateMachine_strategy = st.builds(
    StateMachine,
)
MessageTrigger_strategy = st.builds(
    MessageTrigger,
)
DirectedRelationship_strategy = st.builds(
    DirectedRelationship,
)
DeploymentTarget_strategy = st.builds(
    DeploymentTarget,
)
PackageableElement_strategy = st.builds(
    PackageableElement,
)
Class_strategy = st.builds(
    Class,
)
OpaqueExpression_strategy = st.builds(
    OpaqueExpression,
)
InteractionFragment_strategy = st.builds(
    InteractionFragment,
)
Behavior_strategy = st.builds(
    Behavior,
)
Trigger_strategy = st.builds(
    Trigger,
)
IntervalConstraint_strategy = st.builds(
    IntervalConstraint,
)
LiteralSpecification_strategy = st.builds(
    LiteralSpecification,
)
WriteVariableAction_strategy = st.builds(
    WriteVariableAction,
)
TemplateableElement_strategy = st.builds(
    TemplateableElement,
)
EncapsulatedClassifier_strategy = st.builds(
    EncapsulatedClassifier,
)
UML2WithID_Element_strategy = st.builds(
    UML2WithID_Element,
    ID=
        safe_text
)
State_strategy = st.builds(
    State,
)
Transition_strategy = st.builds(
    Transition,
)
AcceptEventAction_strategy = st.builds(
    AcceptEventAction,
)
InputPin_strategy = st.builds(
    InputPin,
)
Constraint_strategy = st.builds(
    Constraint,
)
Artifact_strategy = st.builds(
    Artifact,
)
CreateLinkAction_strategy = st.builds(
    CreateLinkAction,
)
ActivityGroup_strategy = st.builds(
    ActivityGroup,
)
StructuralFeatureAction_strategy = st.builds(
    StructuralFeatureAction,
)
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
StructuredClassifier_strategy = st.builds(
    StructuredClassifier,
)
BehavioredClassifier_strategy = st.builds(
    BehavioredClassifier,
)
Realization_strategy = st.builds(
    Realization,
)
PackageImport_strategy = st.builds(
    PackageImport,
)
DataType_strategy = st.builds(
    DataType,
)
Relationship_strategy = st.builds(
    Relationship,
)
InvocationAction_strategy = st.builds(
    InvocationAction,
)
InstanceSpecification_strategy = st.builds(
    InstanceSpecification,
)
EventOccurrence_strategy = st.builds(
    EventOccurrence,
)
Node_strategy = st.builds(
    Node,
)
ExecutableNode_strategy = st.builds(
    ExecutableNode,
)
StructuredActivityNode_strategy = st.builds(
    StructuredActivityNode,
)
Feature_strategy = st.builds(
    Feature,
)
Type_strategy = st.builds(
    Type,
)
LinkEndData_strategy = st.builds(
    LinkEndData,
)
Dependency_strategy = st.builds(
    Dependency,
)
ValueSpecification_strategy = st.builds(
    ValueSpecification,
)
Abstraction_strategy = st.builds(
    Abstraction,
)
Package_strategy = st.builds(
    Package,
)
ActivityEdge_strategy = st.builds(
    ActivityEdge,
)
ObjectNode_strategy = st.builds(
    ObjectNode,
)
LinkAction_strategy = st.builds(
    LinkAction,
)
Action_strategy = st.builds(
    Action,
)
CallAction_strategy = st.builds(
    CallAction,
)
InteractionOccurrence_strategy = st.builds(
    InteractionOccurrence,
)
ActivityNode_strategy = st.builds(
    ActivityNode,
)
Vertex_strategy = st.builds(
    Vertex,
)
Namespace_strategy = st.builds(
    Namespace,
)
TemplateSignature_strategy = st.builds(
    TemplateSignature,
)
Interval_strategy = st.builds(
    Interval,
)
Pin_strategy = st.builds(
    Pin,
)
Property_strategy = st.builds(
    Property,
)
ParameterableElement_strategy = st.builds(
    ParameterableElement,
)
MultiplicityElement_strategy = st.builds(
    MultiplicityElement,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
BehavioralFeature_strategy = st.builds(
    BehavioralFeature,
)
FinalNode_strategy = st.builds(
    FinalNode,
)
WriteLinkAction_strategy = st.builds(
    WriteLinkAction,
)
ControlNode_strategy = st.builds(
    ControlNode,
)
DeployedArtifact_strategy = st.builds(
    DeployedArtifact,
)
Classifier_strategy = st.builds(
    Classifier,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
RedefinableElement_strategy = st.builds(
    RedefinableElement,
)
Element_strategy = st.builds(
    Element,
)
UML2WithID_Pin_strategy = st.builds(
    UML2WithID_Pin,
)
UML2WithID_Port_strategy = st.builds(
    UML2WithID_Port,
)
UML2WithID_Realization_strategy = st.builds(
    UML2WithID_Realization,
)
UML2WithID_CreateLinkObjectAction_strategy = st.builds(
    UML2WithID_CreateLinkObjectAction,
)
UML2WithID_ConnectableElementTemplateParameter_strategy = st.builds(
    UML2WithID_ConnectableElementTemplateParameter,
)
UML2WithID_AddVariableValueAction_strategy = st.builds(
    UML2WithID_AddVariableValueAction,
)
UML2WithID_IntervalConstraint_strategy = st.builds(
    UML2WithID_IntervalConstraint,
)
UML2WithID_InitialNode_strategy = st.builds(
    UML2WithID_InitialNode,
)
UML2WithID_Model_strategy = st.builds(
    UML2WithID_Model,
)
UML2WithID_ActivityGroup_strategy = st.builds(
    UML2WithID_ActivityGroup,
)
UML2WithID_InteractionOperand_strategy = st.builds(
    UML2WithID_InteractionOperand,
)
UML2WithID_ReplyAction_strategy = st.builds(
    UML2WithID_ReplyAction,
)
UML2WithID_Node_strategy = st.builds(
    UML2WithID_Node,
)
UML2WithID_TimeExpression_strategy = st.builds(
    UML2WithID_TimeExpression,
)
UML2WithID_Stereotype_strategy = st.builds(
    UML2WithID_Stereotype,
)
UML2WithID_NamedElement_strategy = st.builds(
    UML2WithID_NamedElement,
)
UML2WithID_DeploymentSpecification_strategy = st.builds(
    UML2WithID_DeploymentSpecification,
)
UML2WithID_Clause_strategy = st.builds(
    UML2WithID_Clause,
)
UML2WithID_EnumerationLiteral_strategy = st.builds(
    UML2WithID_EnumerationLiteral,
)
UML2WithID_CreateLinkAction_strategy = st.builds(
    UML2WithID_CreateLinkAction,
)
UML2WithID_Action_strategy = st.builds(
    UML2WithID_Action,
)
UML2WithID_ControlFlow_strategy = st.builds(
    UML2WithID_ControlFlow,
)
UML2WithID_TimeConstraint_strategy = st.builds(
    UML2WithID_TimeConstraint,
)
UML2WithID_InvocationAction_strategy = st.builds(
    UML2WithID_InvocationAction,
)
UML2WithID_TestIdentityAction_strategy = st.builds(
    UML2WithID_TestIdentityAction,
)
UML2WithID_Generalization_strategy = st.builds(
    UML2WithID_Generalization,
)
UML2WithID_Property_strategy = st.builds(
    UML2WithID_Property,
)
UML2WithID_ExecutableNode_strategy = st.builds(
    UML2WithID_ExecutableNode,
)
UML2WithID_Namespace_strategy = st.builds(
    UML2WithID_Namespace,
)
UML2WithID_Extension_strategy = st.builds(
    UML2WithID_Extension,
)
UML2WithID_TemplateParameter_strategy = st.builds(
    UML2WithID_TemplateParameter,
)
UML2WithID_ExceptionHandler_strategy = st.builds(
    UML2WithID_ExceptionHandler,
)
UML2WithID_ActivityNode_strategy = st.builds(
    UML2WithID_ActivityNode,
)
UML2WithID_Activity_strategy = st.builds(
    UML2WithID_Activity,
)
UML2WithID_EncapsulatedClassifier_strategy = st.builds(
    UML2WithID_EncapsulatedClassifier,
)
UML2WithID_Stop_strategy = st.builds(
    UML2WithID_Stop,
)
UML2WithID_OutputPin_strategy = st.builds(
    UML2WithID_OutputPin,
)
UML2WithID_InstanceValue_strategy = st.builds(
    UML2WithID_InstanceValue,
)
UML2WithID_MergeNode_strategy = st.builds(
    UML2WithID_MergeNode,
)
UML2WithID_ChangeTrigger_strategy = st.builds(
    UML2WithID_ChangeTrigger,
)
UML2WithID_DestroyObjectAction_strategy = st.builds(
    UML2WithID_DestroyObjectAction,
)
UML2WithID_Region_strategy = st.builds(
    UML2WithID_Region,
)
UML2WithID_InterruptibleActivityRegion_strategy = st.builds(
    UML2WithID_InterruptibleActivityRegion,
)
UML2WithID_Implementation_strategy = st.builds(
    UML2WithID_Implementation,
)
UML2WithID_Extend_strategy = st.builds(
    UML2WithID_Extend,
)
UML2WithID_SendSignalAction_strategy = st.builds(
    UML2WithID_SendSignalAction,
)
UML2WithID_Interaction_strategy = st.builds(
    UML2WithID_Interaction,
)
UML2WithID_Reception_strategy = st.builds(
    UML2WithID_Reception,
)
UML2WithID_CallBehaviorAction_strategy = st.builds(
    UML2WithID_CallBehaviorAction,
)
UML2WithID_RedefinableTemplateSignature_strategy = st.builds(
    UML2WithID_RedefinableTemplateSignature,
)
UML2WithID_InstanceSpecification_strategy = st.builds(
    UML2WithID_InstanceSpecification,
)
UML2WithID_StructuralFeatureAction_strategy = st.builds(
    UML2WithID_StructuralFeatureAction,
)
UML2WithID_PackageableElement_strategy = st.builds(
    UML2WithID_PackageableElement,
)
UML2WithID_PrimitiveType_strategy = st.builds(
    UML2WithID_PrimitiveType,
)
UML2WithID_BehavioralFeature_strategy = st.builds(
    UML2WithID_BehavioralFeature,
)
UML2WithID_ControlNode_strategy = st.builds(
    UML2WithID_ControlNode,
)
UML2WithID_Association_strategy = st.builds(
    UML2WithID_Association,
)
UML2WithID_JoinNode_strategy = st.builds(
    UML2WithID_JoinNode,
)
UML2WithID_Deployment_strategy = st.builds(
    UML2WithID_Deployment,
)
UML2WithID_FinalState_strategy = st.builds(
    UML2WithID_FinalState,
)
UML2WithID_Component_strategy = st.builds(
    UML2WithID_Component,
)
UML2WithID_StateMachine_strategy = st.builds(
    UML2WithID_StateMachine,
)
UML2WithID_StateInvariant_strategy = st.builds(
    UML2WithID_StateInvariant,
)
UML2WithID_ExpansionRegion_strategy = st.builds(
    UML2WithID_ExpansionRegion,
)
UML2WithID_CallAction_strategy = st.builds(
    UML2WithID_CallAction,
)
UML2WithID_ObjectNode_strategy = st.builds(
    UML2WithID_ObjectNode,
)
UML2WithID_OpaqueExpression_strategy = st.builds(
    UML2WithID_OpaqueExpression,
)
UML2WithID_GeneralOrdering_strategy = st.builds(
    UML2WithID_GeneralOrdering,
)
UML2WithID_RaiseExceptionAction_strategy = st.builds(
    UML2WithID_RaiseExceptionAction,
)
UML2WithID_Variable_strategy = st.builds(
    UML2WithID_Variable,
)
UML2WithID_ReadLinkObjectEndAction_strategy = st.builds(
    UML2WithID_ReadLinkObjectEndAction,
)
UML2WithID_ClearAssociationAction_strategy = st.builds(
    UML2WithID_ClearAssociationAction,
)
UML2WithID_DirectedRelationship_strategy = st.builds(
    UML2WithID_DirectedRelationship,
)
UML2WithID_Usage_strategy = st.builds(
    UML2WithID_Usage,
)
UML2WithID_LiteralString_strategy = st.builds(
    UML2WithID_LiteralString,
)
UML2WithID_TemplateableElement_strategy = st.builds(
    UML2WithID_TemplateableElement,
)
UML2WithID_StartOwnedBehaviorAction_strategy = st.builds(
    UML2WithID_StartOwnedBehaviorAction,
)
UML2WithID_DeployedArtifact_strategy = st.builds(
    UML2WithID_DeployedArtifact,
)
UML2WithID_LiteralInteger_strategy = st.builds(
    UML2WithID_LiteralInteger,
)
UML2WithID_StructuredActivityNode_strategy = st.builds(
    UML2WithID_StructuredActivityNode,
)
UML2WithID_ReadLinkAction_strategy = st.builds(
    UML2WithID_ReadLinkAction,
)
UML2WithID_Vertex_strategy = st.builds(
    UML2WithID_Vertex,
)
UML2WithID_LiteralUnlimitedNatural_strategy = st.builds(
    UML2WithID_LiteralUnlimitedNatural,
)
UML2WithID_DataType_strategy = st.builds(
    UML2WithID_DataType,
)
UML2WithID_LoopNode_strategy = st.builds(
    UML2WithID_LoopNode,
)
UML2WithID_Transition_strategy = st.builds(
    UML2WithID_Transition,
)
UML2WithID_ProtocolTransition_strategy = st.builds(
    UML2WithID_ProtocolTransition,
)
UML2WithID_UseCase_strategy = st.builds(
    UML2WithID_UseCase,
)
UML2WithID_ParameterableClassifier_strategy = st.builds(
    UML2WithID_ParameterableClassifier,
)
UML2WithID_TimeInterval_strategy = st.builds(
    UML2WithID_TimeInterval,
)
UML2WithID_ProtocolConformance_strategy = st.builds(
    UML2WithID_ProtocolConformance,
)
UML2WithID_Operation_strategy = st.builds(
    UML2WithID_Operation,
)
UML2WithID_InteractionFragment_strategy = st.builds(
    UML2WithID_InteractionFragment,
)
UML2WithID_Slot_strategy = st.builds(
    UML2WithID_Slot,
)
UML2WithID_RedefinableElement_strategy = st.builds(
    UML2WithID_RedefinableElement,
)
UML2WithID_ReadLinkObjectEndQualifierAction_strategy = st.builds(
    UML2WithID_ReadLinkObjectEndQualifierAction,
)
UML2WithID_VariableAction_strategy = st.builds(
    UML2WithID_VariableAction,
)
UML2WithID_ActivityFinalNode_strategy = st.builds(
    UML2WithID_ActivityFinalNode,
)
UML2WithID_Interval_strategy = st.builds(
    UML2WithID_Interval,
)
UML2WithID_LinkEndCreationData_strategy = st.builds(
    UML2WithID_LinkEndCreationData,
)
UML2WithID_ReadExtentAction_strategy = st.builds(
    UML2WithID_ReadExtentAction,
)
UML2WithID_Pseudostate_strategy = st.builds(
    UML2WithID_Pseudostate,
)
UML2WithID_DestroyLinkAction_strategy = st.builds(
    UML2WithID_DestroyLinkAction,
)
UML2WithID_FlowFinalNode_strategy = st.builds(
    UML2WithID_FlowFinalNode,
)
UML2WithID_ClearStructuralFeatureAction_strategy = st.builds(
    UML2WithID_ClearStructuralFeatureAction,
)
UML2WithID_CombinedFragment_strategy = st.builds(
    UML2WithID_CombinedFragment,
)
UML2WithID_Continuation_strategy = st.builds(
    UML2WithID_Continuation,
)
UML2WithID_ForkNode_strategy = st.builds(
    UML2WithID_ForkNode,
)
UML2WithID_Relationship_strategy = st.builds(
    UML2WithID_Relationship,
)
UML2WithID_AssociationClass_strategy = st.builds(
    UML2WithID_AssociationClass,
)
UML2WithID_ProtocolStateMachine_strategy = st.builds(
    UML2WithID_ProtocolStateMachine,
)
UML2WithID_ActivityEdge_strategy = st.builds(
    UML2WithID_ActivityEdge,
)
UML2WithID_Signal_strategy = st.builds(
    UML2WithID_Signal,
)
UML2WithID_DurationObservationAction_strategy = st.builds(
    UML2WithID_DurationObservationAction,
)
UML2WithID_Permission_strategy = st.builds(
    UML2WithID_Permission,
)
UML2WithID_Artifact_strategy = st.builds(
    UML2WithID_Artifact,
)
UML2WithID_ReadStructuralFeatureAction_strategy = st.builds(
    UML2WithID_ReadStructuralFeatureAction,
)
UML2WithID_MessageEnd_strategy = st.builds(
    UML2WithID_MessageEnd,
)
UML2WithID_CallTrigger_strategy = st.builds(
    UML2WithID_CallTrigger,
)
UML2WithID_Comment_strategy = st.builds(
    UML2WithID_Comment,
)
UML2WithID_DurationConstraint_strategy = st.builds(
    UML2WithID_DurationConstraint,
)
UML2WithID_ValueSpecification_strategy = st.builds(
    UML2WithID_ValueSpecification,
)
UML2WithID_Parameter_strategy = st.builds(
    UML2WithID_Parameter,
)
UML2WithID_ActivityPartition_strategy = st.builds(
    UML2WithID_ActivityPartition,
)
UML2WithID_AnyTrigger_strategy = st.builds(
    UML2WithID_AnyTrigger,
)
UML2WithID_TemplateBinding_strategy = st.builds(
    UML2WithID_TemplateBinding,
)
UML2WithID_Constraint_strategy = st.builds(
    UML2WithID_Constraint,
)
UML2WithID_Enumeration_strategy = st.builds(
    UML2WithID_Enumeration,
)
UML2WithID_BehavioredClassifier_strategy = st.builds(
    UML2WithID_BehavioredClassifier,
)
UML2WithID_RemoveVariableValueAction_strategy = st.builds(
    UML2WithID_RemoveVariableValueAction,
)
UML2WithID_LiteralNull_strategy = st.builds(
    UML2WithID_LiteralNull,
)
UML2WithID_ConnectableElement_strategy = st.builds(
    UML2WithID_ConnectableElement,
)
UML2WithID_TimeObservationAction_strategy = st.builds(
    UML2WithID_TimeObservationAction,
)
UML2WithID_Class_strategy = st.builds(
    UML2WithID_Class,
)
UML2WithID_LinkEndData_strategy = st.builds(
    UML2WithID_LinkEndData,
)
UML2WithID_TimeTrigger_strategy = st.builds(
    UML2WithID_TimeTrigger,
)
UML2WithID_Type_strategy = st.builds(
    UML2WithID_Type,
)
UML2WithID_StringExpression_strategy = st.builds(
    UML2WithID_StringExpression,
)
UML2WithID_CallOperationAction_strategy = st.builds(
    UML2WithID_CallOperationAction,
)
UML2WithID_CentralBufferNode_strategy = st.builds(
    UML2WithID_CentralBufferNode,
)
UML2WithID_ParameterableElement_strategy = st.builds(
    UML2WithID_ParameterableElement,
)
UML2WithID_ProfileApplication_strategy = st.builds(
    UML2WithID_ProfileApplication,
)
UML2WithID_ExpansionNode_strategy = st.builds(
    UML2WithID_ExpansionNode,
)
UML2WithID_Collaboration_strategy = st.builds(
    UML2WithID_Collaboration,
)
UML2WithID_State_strategy = st.builds(
    UML2WithID_State,
)
UML2WithID_ConnectorEnd_strategy = st.builds(
    UML2WithID_ConnectorEnd,
)
UML2WithID_Include_strategy = st.builds(
    UML2WithID_Include,
)
UML2WithID_Profile_strategy = st.builds(
    UML2WithID_Profile,
)
UML2WithID_Duration_strategy = st.builds(
    UML2WithID_Duration,
)
UML2WithID_PackageImport_strategy = st.builds(
    UML2WithID_PackageImport,
)
UML2WithID_Interface_strategy = st.builds(
    UML2WithID_Interface,
)
UML2WithID_ExecutionOccurrence_strategy = st.builds(
    UML2WithID_ExecutionOccurrence,
)
UML2WithID_ReclassifyObjectAction_strategy = st.builds(
    UML2WithID_ReclassifyObjectAction,
)
UML2WithID_MessageTrigger_strategy = st.builds(
    UML2WithID_MessageTrigger,
)
UML2WithID_Substitution_strategy = st.builds(
    UML2WithID_Substitution,
)
UML2WithID_InputPin_strategy = st.builds(
    UML2WithID_InputPin,
)
UML2WithID_Expression_strategy = st.builds(
    UML2WithID_Expression,
)
UML2WithID_ValuePin_strategy = st.builds(
    UML2WithID_ValuePin,
)
UML2WithID_QualifierValue_strategy = st.builds(
    UML2WithID_QualifierValue,
)
UML2WithID_CollaborationOccurrence_strategy = st.builds(
    UML2WithID_CollaborationOccurrence,
)
UML2WithID_CreateObjectAction_strategy = st.builds(
    UML2WithID_CreateObjectAction,
)
UML2WithID_TemplateSignature_strategy = st.builds(
    UML2WithID_TemplateSignature,
)
UML2WithID_Abstraction_strategy = st.builds(
    UML2WithID_Abstraction,
)
UML2WithID_Trigger_strategy = st.builds(
    UML2WithID_Trigger,
)
UML2WithID_Connector_strategy = st.builds(
    UML2WithID_Connector,
)
UML2WithID_LiteralBoolean_strategy = st.builds(
    UML2WithID_LiteralBoolean,
)
UML2WithID_BroadcastSignalAction_strategy = st.builds(
    UML2WithID_BroadcastSignalAction,
)
UML2WithID_ObjectFlow_strategy = st.builds(
    UML2WithID_ObjectFlow,
)
UML2WithID_PackageMerge_strategy = st.builds(
    UML2WithID_PackageMerge,
)
UML2WithID_LinkAction_strategy = st.builds(
    UML2WithID_LinkAction,
)
UML2WithID_FinalNode_strategy = st.builds(
    UML2WithID_FinalNode,
)
UML2WithID_ExecutionEnvironment_strategy = st.builds(
    UML2WithID_ExecutionEnvironment,
)
UML2WithID_Message_strategy = st.builds(
    UML2WithID_Message,
)
UML2WithID_DataStoreNode_strategy = st.builds(
    UML2WithID_DataStoreNode,
)
UML2WithID_ClassifierTemplateParameter_strategy = st.builds(
    UML2WithID_ClassifierTemplateParameter,
)
UML2WithID_ClearVariableAction_strategy = st.builds(
    UML2WithID_ClearVariableAction,
)
UML2WithID_Manifestation_strategy = st.builds(
    UML2WithID_Manifestation,
)
UML2WithID_InteractionConstraint_strategy = st.builds(
    UML2WithID_InteractionConstraint,
)
UML2WithID_CommunicationPath_strategy = st.builds(
    UML2WithID_CommunicationPath,
)
UML2WithID_Actor_strategy = st.builds(
    UML2WithID_Actor,
)
UML2WithID_ExtensionEnd_strategy = st.builds(
    UML2WithID_ExtensionEnd,
)
UML2WithID_GeneralizationSet_strategy = st.builds(
    UML2WithID_GeneralizationSet,
)
UML2WithID_StructuralFeature_strategy = st.builds(
    UML2WithID_StructuralFeature,
)
UML2WithID_TemplateableClassifier_strategy = st.builds(
    UML2WithID_TemplateableClassifier,
)
UML2WithID_Device_strategy = st.builds(
    UML2WithID_Device,
)
UML2WithID_PrimitiveFunction_strategy = st.builds(
    UML2WithID_PrimitiveFunction,
)
UML2WithID_ConnectionPointReference_strategy = st.builds(
    UML2WithID_ConnectionPointReference,
)
UML2WithID_PartDecomposition_strategy = st.builds(
    UML2WithID_PartDecomposition,
)
UML2WithID_ReadSelfAction_strategy = st.builds(
    UML2WithID_ReadSelfAction,
)
UML2WithID_MultiplicityElement_strategy = st.builds(
    UML2WithID_MultiplicityElement,
)
UML2WithID_DurationInterval_strategy = st.builds(
    UML2WithID_DurationInterval,
)
UML2WithID_AcceptEventAction_strategy = st.builds(
    UML2WithID_AcceptEventAction,
)
UML2WithID_SignalTrigger_strategy = st.builds(
    UML2WithID_SignalTrigger,
)
UML2WithID_SendObjectAction_strategy = st.builds(
    UML2WithID_SendObjectAction,
)
UML2WithID_WriteStructuralFeatureAction_strategy = st.builds(
    UML2WithID_WriteStructuralFeatureAction,
)
UML2WithID_Lifeline_strategy = st.builds(
    UML2WithID_Lifeline,
)
UML2WithID_ReadVariableAction_strategy = st.builds(
    UML2WithID_ReadVariableAction,
)
UML2WithID_LiteralSpecification_strategy = st.builds(
    UML2WithID_LiteralSpecification,
)
UML2WithID_DecisionNode_strategy = st.builds(
    UML2WithID_DecisionNode,
)
UML2WithID_DeploymentTarget_strategy = st.builds(
    UML2WithID_DeploymentTarget,
)
UML2WithID_ReadIsClassifiedObjectAction_strategy = st.builds(
    UML2WithID_ReadIsClassifiedObjectAction,
)
UML2WithID_Package_strategy = st.builds(
    UML2WithID_Package,
)
UML2WithID_TypedElement_strategy = st.builds(
    UML2WithID_TypedElement,
)
UML2WithID_InformationFlow_strategy = st.builds(
    UML2WithID_InformationFlow,
)
UML2WithID_InteractionOccurrence_strategy = st.builds(
    UML2WithID_InteractionOccurrence,
)
UML2WithID_ActivityParameterNode_strategy = st.builds(
    UML2WithID_ActivityParameterNode,
)
UML2WithID_WriteLinkAction_strategy = st.builds(
    UML2WithID_WriteLinkAction,
)
UML2WithID_ElementImport_strategy = st.builds(
    UML2WithID_ElementImport,
)
UML2WithID_TemplateParameterSubstitution_strategy = st.builds(
    UML2WithID_TemplateParameterSubstitution,
)
UML2WithID_RemoveStructuralFeatureValueAction_strategy = st.builds(
    UML2WithID_RemoveStructuralFeatureValueAction,
)
UML2WithID_StructuredClassifier_strategy = st.builds(
    UML2WithID_StructuredClassifier,
)
UML2WithID_OperationTemplateParameter_strategy = st.builds(
    UML2WithID_OperationTemplateParameter,
)
UML2WithID_ConditionalNode_strategy = st.builds(
    UML2WithID_ConditionalNode,
)
UML2WithID_AcceptCallAction_strategy = st.builds(
    UML2WithID_AcceptCallAction,
)
UML2WithID_Feature_strategy = st.builds(
    UML2WithID_Feature,
)
UML2WithID_WriteVariableAction_strategy = st.builds(
    UML2WithID_WriteVariableAction,
)
UML2WithID_Behavior_strategy = st.builds(
    UML2WithID_Behavior,
)
UML2WithID_InformationItem_strategy = st.builds(
    UML2WithID_InformationItem,
)
UML2WithID_Dependency_strategy = st.builds(
    UML2WithID_Dependency,
)
UML2WithID_Classifier_strategy = st.builds(
    UML2WithID_Classifier,
)
UML2WithID_ApplyFunctionAction_strategy = st.builds(
    UML2WithID_ApplyFunctionAction,
)
UML2WithID_ExtensionPoint_strategy = st.builds(
    UML2WithID_ExtensionPoint,
)
UML2WithID_AddStructuralFeatureValueAction_strategy = st.builds(
    UML2WithID_AddStructuralFeatureValueAction,
)
UML2WithID_ParameterSet_strategy = st.builds(
    UML2WithID_ParameterSet,
)
MessageEnd_strategy = st.builds(
    MessageEnd,
)
UML2WithID_EventOccurrence_strategy = st.builds(
    UML2WithID_EventOccurrence,
)
UML2WithID_Gate_strategy = st.builds(
    UML2WithID_Gate,
)

@given(instance=ConnectableElement_strategy)
@settings(max_examples=50)
def test_connectableelement_instantiation(instance):
    assert isinstance(instance, ConnectableElement)

@given(instance=Association_strategy)
@settings(max_examples=50)
def test_association_instantiation(instance):
    assert isinstance(instance, Association)

@given(instance=TemplateParameter_strategy)
@settings(max_examples=50)
def test_templateparameter_instantiation(instance):
    assert isinstance(instance, TemplateParameter)

@given(instance=CentralBufferNode_strategy)
@settings(max_examples=50)
def test_centralbuffernode_instantiation(instance):
    assert isinstance(instance, CentralBufferNode)

@given(instance=VariableAction_strategy)
@settings(max_examples=50)
def test_variableaction_instantiation(instance):
    assert isinstance(instance, VariableAction)

@given(instance=WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, WriteStructuralFeatureAction)

@given(instance=StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_instantiation(instance):
    assert isinstance(instance, StateMachine)

@given(instance=MessageTrigger_strategy)
@settings(max_examples=50)
def test_messagetrigger_instantiation(instance):
    assert isinstance(instance, MessageTrigger)

@given(instance=DirectedRelationship_strategy)
@settings(max_examples=50)
def test_directedrelationship_instantiation(instance):
    assert isinstance(instance, DirectedRelationship)

@given(instance=DeploymentTarget_strategy)
@settings(max_examples=50)
def test_deploymenttarget_instantiation(instance):
    assert isinstance(instance, DeploymentTarget)

@given(instance=PackageableElement_strategy)
@settings(max_examples=50)
def test_packageableelement_instantiation(instance):
    assert isinstance(instance, PackageableElement)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=OpaqueExpression_strategy)
@settings(max_examples=50)
def test_opaqueexpression_instantiation(instance):
    assert isinstance(instance, OpaqueExpression)

@given(instance=InteractionFragment_strategy)
@settings(max_examples=50)
def test_interactionfragment_instantiation(instance):
    assert isinstance(instance, InteractionFragment)

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=Trigger_strategy)
@settings(max_examples=50)
def test_trigger_instantiation(instance):
    assert isinstance(instance, Trigger)

@given(instance=IntervalConstraint_strategy)
@settings(max_examples=50)
def test_intervalconstraint_instantiation(instance):
    assert isinstance(instance, IntervalConstraint)

@given(instance=LiteralSpecification_strategy)
@settings(max_examples=50)
def test_literalspecification_instantiation(instance):
    assert isinstance(instance, LiteralSpecification)

@given(instance=WriteVariableAction_strategy)
@settings(max_examples=50)
def test_writevariableaction_instantiation(instance):
    assert isinstance(instance, WriteVariableAction)

@given(instance=TemplateableElement_strategy)
@settings(max_examples=50)
def test_templateableelement_instantiation(instance):
    assert isinstance(instance, TemplateableElement)

@given(instance=EncapsulatedClassifier_strategy)
@settings(max_examples=50)
def test_encapsulatedclassifier_instantiation(instance):
    assert isinstance(instance, EncapsulatedClassifier)

@given(instance=UML2WithID_Element_strategy)
@settings(max_examples=50)
def test_uml2withid_element_instantiation(instance):
    assert isinstance(instance, UML2WithID_Element)



@given(instance=UML2WithID_Element_strategy)
def test_uml2withid_element_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=AcceptEventAction_strategy)
@settings(max_examples=50)
def test_accepteventaction_instantiation(instance):
    assert isinstance(instance, AcceptEventAction)

@given(instance=InputPin_strategy)
@settings(max_examples=50)
def test_inputpin_instantiation(instance):
    assert isinstance(instance, InputPin)

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=Artifact_strategy)
@settings(max_examples=50)
def test_artifact_instantiation(instance):
    assert isinstance(instance, Artifact)

@given(instance=CreateLinkAction_strategy)
@settings(max_examples=50)
def test_createlinkaction_instantiation(instance):
    assert isinstance(instance, CreateLinkAction)

@given(instance=ActivityGroup_strategy)
@settings(max_examples=50)
def test_activitygroup_instantiation(instance):
    assert isinstance(instance, ActivityGroup)

@given(instance=StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, StructuralFeatureAction)

@given(instance=StructuralFeature_strategy)
@settings(max_examples=50)
def test_structuralfeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)

@given(instance=StructuredClassifier_strategy)
@settings(max_examples=50)
def test_structuredclassifier_instantiation(instance):
    assert isinstance(instance, StructuredClassifier)

@given(instance=BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_behavioredclassifier_instantiation(instance):
    assert isinstance(instance, BehavioredClassifier)

@given(instance=Realization_strategy)
@settings(max_examples=50)
def test_realization_instantiation(instance):
    assert isinstance(instance, Realization)

@given(instance=PackageImport_strategy)
@settings(max_examples=50)
def test_packageimport_instantiation(instance):
    assert isinstance(instance, PackageImport)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=Relationship_strategy)
@settings(max_examples=50)
def test_relationship_instantiation(instance):
    assert isinstance(instance, Relationship)

@given(instance=InvocationAction_strategy)
@settings(max_examples=50)
def test_invocationaction_instantiation(instance):
    assert isinstance(instance, InvocationAction)

@given(instance=InstanceSpecification_strategy)
@settings(max_examples=50)
def test_instancespecification_instantiation(instance):
    assert isinstance(instance, InstanceSpecification)

@given(instance=EventOccurrence_strategy)
@settings(max_examples=50)
def test_eventoccurrence_instantiation(instance):
    assert isinstance(instance, EventOccurrence)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=ExecutableNode_strategy)
@settings(max_examples=50)
def test_executablenode_instantiation(instance):
    assert isinstance(instance, ExecutableNode)

@given(instance=StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_structuredactivitynode_instantiation(instance):
    assert isinstance(instance, StructuredActivityNode)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=LinkEndData_strategy)
@settings(max_examples=50)
def test_linkenddata_instantiation(instance):
    assert isinstance(instance, LinkEndData)

@given(instance=Dependency_strategy)
@settings(max_examples=50)
def test_dependency_instantiation(instance):
    assert isinstance(instance, Dependency)

@given(instance=ValueSpecification_strategy)
@settings(max_examples=50)
def test_valuespecification_instantiation(instance):
    assert isinstance(instance, ValueSpecification)

@given(instance=Abstraction_strategy)
@settings(max_examples=50)
def test_abstraction_instantiation(instance):
    assert isinstance(instance, Abstraction)

@given(instance=Package_strategy)
@settings(max_examples=50)
def test_package_instantiation(instance):
    assert isinstance(instance, Package)

@given(instance=ActivityEdge_strategy)
@settings(max_examples=50)
def test_activityedge_instantiation(instance):
    assert isinstance(instance, ActivityEdge)

@given(instance=ObjectNode_strategy)
@settings(max_examples=50)
def test_objectnode_instantiation(instance):
    assert isinstance(instance, ObjectNode)

@given(instance=LinkAction_strategy)
@settings(max_examples=50)
def test_linkaction_instantiation(instance):
    assert isinstance(instance, LinkAction)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=CallAction_strategy)
@settings(max_examples=50)
def test_callaction_instantiation(instance):
    assert isinstance(instance, CallAction)

@given(instance=InteractionOccurrence_strategy)
@settings(max_examples=50)
def test_interactionoccurrence_instantiation(instance):
    assert isinstance(instance, InteractionOccurrence)

@given(instance=ActivityNode_strategy)
@settings(max_examples=50)
def test_activitynode_instantiation(instance):
    assert isinstance(instance, ActivityNode)

@given(instance=Vertex_strategy)
@settings(max_examples=50)
def test_vertex_instantiation(instance):
    assert isinstance(instance, Vertex)

@given(instance=Namespace_strategy)
@settings(max_examples=50)
def test_namespace_instantiation(instance):
    assert isinstance(instance, Namespace)

@given(instance=TemplateSignature_strategy)
@settings(max_examples=50)
def test_templatesignature_instantiation(instance):
    assert isinstance(instance, TemplateSignature)

@given(instance=Interval_strategy)
@settings(max_examples=50)
def test_interval_instantiation(instance):
    assert isinstance(instance, Interval)

@given(instance=Pin_strategy)
@settings(max_examples=50)
def test_pin_instantiation(instance):
    assert isinstance(instance, Pin)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=ParameterableElement_strategy)
@settings(max_examples=50)
def test_parameterableelement_instantiation(instance):
    assert isinstance(instance, ParameterableElement)

@given(instance=MultiplicityElement_strategy)
@settings(max_examples=50)
def test_multiplicityelement_instantiation(instance):
    assert isinstance(instance, MultiplicityElement)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=BehavioralFeature_strategy)
@settings(max_examples=50)
def test_behavioralfeature_instantiation(instance):
    assert isinstance(instance, BehavioralFeature)

@given(instance=FinalNode_strategy)
@settings(max_examples=50)
def test_finalnode_instantiation(instance):
    assert isinstance(instance, FinalNode)

@given(instance=WriteLinkAction_strategy)
@settings(max_examples=50)
def test_writelinkaction_instantiation(instance):
    assert isinstance(instance, WriteLinkAction)

@given(instance=ControlNode_strategy)
@settings(max_examples=50)
def test_controlnode_instantiation(instance):
    assert isinstance(instance, ControlNode)

@given(instance=DeployedArtifact_strategy)
@settings(max_examples=50)
def test_deployedartifact_instantiation(instance):
    assert isinstance(instance, DeployedArtifact)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=RedefinableElement_strategy)
@settings(max_examples=50)
def test_redefinableelement_instantiation(instance):
    assert isinstance(instance, RedefinableElement)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=UML2WithID_Pin_strategy)
@settings(max_examples=50)
def test_uml2withid_pin_instantiation(instance):
    assert isinstance(instance, UML2WithID_Pin)

@given(instance=UML2WithID_Port_strategy)
@settings(max_examples=50)
def test_uml2withid_port_instantiation(instance):
    assert isinstance(instance, UML2WithID_Port)

@given(instance=UML2WithID_Realization_strategy)
@settings(max_examples=50)
def test_uml2withid_realization_instantiation(instance):
    assert isinstance(instance, UML2WithID_Realization)

@given(instance=UML2WithID_CreateLinkObjectAction_strategy)
@settings(max_examples=50)
def test_uml2withid_createlinkobjectaction_instantiation(instance):
    assert isinstance(instance, UML2WithID_CreateLinkObjectAction)

@given(instance=UML2WithID_ConnectableElementTemplateParameter_strategy)
@settings(max_examples=50)
def test_uml2withid_connectableelementtemplateparameter_instantiation(instance):
    assert isinstance(instance, UML2WithID_ConnectableElementTemplateParameter)

@given(instance=UML2WithID_AddVariableValueAction_strategy)
@settings(max_examples=50)
def test_uml2withid_addvariablevalueaction_instantiation(instance):
    assert isinstance(instance, UML2WithID_AddVariableValueAction)

@given(instance=UML2WithID_IntervalConstraint_strategy)
@settings(max_examples=50)
def test_uml2withid_intervalconstraint_instantiation(instance):
    assert isinstance(instance, UML2WithID_IntervalConstraint)

@given(instance=UML2WithID_InitialNode_strategy)
@settings(max_examples=50)
def test_uml2withid_initialnode_instantiation(instance):
    assert isinstance(instance, UML2WithID_InitialNode)

@given(instance=UML2WithID_Model_strategy)
@settings(max_examples=50)
def test_uml2withid_model_instantiation(instance):
    assert isinstance(instance, UML2WithID_Model)

@given(instance=UML2WithID_ActivityGroup_strategy)
@settings(max_examples=50)
def test_uml2withid_activitygroup_instantiation(instance):
    assert isinstance(instance, UML2WithID_ActivityGroup)

@given(instance=UML2WithID_InteractionOperand_strategy)
@settings(max_examples=50)
def test_uml2withid_interactionoperand_instantiation(instance):
    assert isinstance(instance, UML2WithID_InteractionOperand)

@given(instance=UML2WithID_ReplyAction_strategy)
@settings(max_examples=50)
def test_uml2withid_replyaction_instantiation(instance):
    assert isinstance(instance, UML2WithID_ReplyAction)

@given(instance=UML2WithID_Node_strategy)
@settings(max_examples=50)
def test_uml2withid_node_instantiation(instance):
    assert isinstance(instance, UML2WithID_Node)

@given(instance=UML2WithID_TimeExpression_strategy)
@settings(max_examples=50)
def test_uml2withid_timeexpression_instantiation(instance):
    assert isinstance(instance, UML2WithID_TimeExpression)

@given(instance=UML2WithID_Stereotype_strategy)
@settings(max_examples=50)
def test_uml2withid_stereotype_instantiation(instance):
    assert isinstance(instance, UML2WithID_Stereotype)

@given(instance=UML2WithID_NamedElement_strategy)
@settings(max_examples=50)
def test_uml2withid_namedelement_instantiation(instance):
    assert isinstance(instance, UML2WithID_NamedElement)

@given(instance=UML2WithID_DeploymentSpecification_strategy)
@settings(max_examples=50)
def test_uml2withid_deploymentspecification_instantiation(instance):
    assert isinstance(instance, UML2WithID_DeploymentSpecification)

@given(instance=UML2WithID_Clause_strategy)
@settings(max_examples=50)
def test_uml2withid_clause_instantiation(instance):
    assert isinstance(instance, UML2WithID_Clause)

@given(instance=UML2WithID_EnumerationLiteral_strategy)
@settings(max_examples=50)
def test_uml2withid_enumerationliteral_instantiation(instance):
    assert isinstance(instance, UML2WithID_EnumerationLiteral)

@given(instance=UML2WithID_CreateLinkAction_strategy)
@settings(max_examples=50)
def test_uml2withid_createlinkaction_instantiation(instance):
    assert isinstance(instance, UML2WithID_CreateLinkAction)

@given(instance=UML2WithID_Action_strategy)
@settings(max_examples=50)
def test_uml2withid_action_instantiation(instance):
    assert isinstance(instance, UML2WithID_Action)

@given(instance=UML2WithID_ControlFlow_strategy)
@settings(max_examples=50)
def test_uml2withid_controlflow_instantiation(instance):
    assert isinstance(instance, UML2WithID_ControlFlow)

@given(instance=UML2WithID_TimeConstraint_strategy)
@settings(max_examples=50)
def test_uml2withid_timeconstraint_instantiation(instance):
    assert isinstance(instance, UML2WithID_TimeConstraint)

@given(instance=UML2WithID_InvocationAction_strategy)
@settings(max_examples=50)
def test_uml2withid_invocationaction_instantiation(instance):
    assert isinstance(instance, UML2WithID_InvocationAction)

@given(instance=UML2WithID_TestIdentityAction_strategy)
@settings(max_examples=50)
def test_uml2withid_testidentityaction_instantiation(instance):
    assert isinstance(instance, UML2WithID_TestIdentityAction)

@given(instance=UML2WithID_Generalization_strategy)
@settings(max_examples=50)
def test_uml2withid_generalization_instantiation(instance):
    assert isinstance(instance, UML2WithID_Generalization)

@given(instance=UML2WithID_Property_strategy)
@settings(max_examples=50)
def test_uml2withid_property_instantiation(instance):
    assert isinstance(instance, UML2WithID_Property)

@given(instance=UML2WithID_ExecutableNode_strategy)
@settings(max_examples=50)
def test_uml2withid_executablenode_instantiation(instance):
    assert isinstance(instance, UML2WithID_ExecutableNode)

@given(instance=UML2WithID_Namespace_strategy)
@settings(max_examples=50)
def test_uml2withid_namespace_instantiation(instance):
    assert isinstance(instance, UML2WithID_Namespace)

@given(instance=UML2WithID_Extension_strategy)
@settings(max_examples=50)
def test_uml2withid_extension_instantiation(instance):
    assert isinstance(instance, UML2WithID_Extension)

@given(instance=UML2WithID_TemplateParameter_strategy)
@settings(max_examples=50)
def test_uml2withid_templateparameter_instantiation(instance):
    assert isinstance(instance, UML2WithID_TemplateParameter)

@given(instance=UML2WithID_ExceptionHandler_strategy)
@settings(max_examples=50)
def test_uml2withid_exceptionhandler_instantiation(instance):
    assert isinstance(instance, UML2WithID_ExceptionHandler)

@given(instance=UML2WithID_ActivityNode_strategy)
@settings(max_examples=50)
def test_uml2withid_activitynode_instantiation(instance):
    assert isinstance(instance, UML2WithID_ActivityNode)

@given(instance=UML2WithID_Activity_strategy)
@settings(max_examples=50)
def test_uml2withid_activity_instantiation(instance):
    assert isinstance(instance, UML2WithID_Activity)

@given(instance=UML2WithID_EncapsulatedClassifier_strategy)
@settings(max_examples=50)
def test_uml2withid_encapsulatedclassifier_instantiation(instance):
    assert isinstance(instance, UML2WithID_EncapsulatedClassifier)

@given(instance=UML2WithID_Stop_strategy)
@settings(max_examples=50)
def test_uml2withid_stop_instantiation(instance):
    assert isinstance(instance, UML2WithID_Stop)

@given(instance=UML2WithID_OutputPin_strategy)
@settings(max_examples=50)
def test_uml2withid_outputpin_instantiation(instance):
    assert isinstance(instance, UML2WithID_OutputPin)

@given(instance=UML2WithID_InstanceValue_strategy)
@settings(max_examples=50)
def test_uml2withid_instancevalue_instantiation(instance):
    assert isinstance(instance, UML2WithID_InstanceValue)

@given(instance=UML2WithID_MergeNode_strategy)
@settings(max_examples=50)
def test_uml2withid_mergenode_instantiation(instance):
    assert isinstance(instance, UML2WithID_MergeNode)

@given(instance=UML2WithID_ChangeTrigger_strategy)
@settings(max_examples=50)
def test_uml2withid_changetrigger_instantiation(instance):
    assert isinstance(instance, UML2WithID_ChangeTrigger)

@given(instance=UML2WithID_DestroyObjectAction_strategy)
@settings(max_examples=50)
def test_uml2withid_destroyobjectaction_instantiation(instance):
    assert isinstance(instance, UML2WithID_DestroyObjectAction)

@given(instance=UML2WithID_Region_strategy)
@settings(max_examples=50)
def test_uml2withid_region_instantiation(instance):
    assert isinstance(instance, UML2WithID_Region)

@given(instance=UML2WithID_InterruptibleActivityRegion_strategy)
@settings(max_examples=50)
def test_uml2withid_interruptibleactivityregion_instantiation(instance):
    assert isinstance(instance, UML2WithID_InterruptibleActivityRegion)

@given(instance=UML2WithID_Implementation_strategy)
@settings(max_examples=50)
def test_uml2withid_implementation_instantiation(instance):
    assert isinstance(instance, UML2WithID_Implementation)

@given(instance=UML2WithID_Extend_strategy)
@settings(max_examples=50)
def test_uml2withid_extend_instantiation(instance):
    assert isinstance(instance, UML2WithID_Extend)

@given(instance=UML2WithID_SendSignalAction_strategy)
@settings(max_examples=50)
def test_uml2withid_sendsignalaction_instantiation(instance):
    assert isinstance(instance, UML2WithID_SendSignalAction)

@given(instance=UML2WithID_Interaction_strategy)
@settings(max_examples=50)
def test_uml2withid_interaction_instantiation(instance):
    assert isinstance(instance, UML2WithID_Interaction)

@given(instance=UML2WithID_Reception_strategy)
@settings(max_examples=50)
def test_uml2withid_reception_instantiation(instance):
    assert isinstance(instance, UML2WithID_Reception)

@given(instance=UML2WithID_CallBehaviorAction_strategy)
@settings(max_examples=50)
def test_uml2withid_callbehavioraction_instantiation(instance):
    assert isinstance(instance, UML2WithID_CallBehaviorAction)

@given(instance=UML2WithID_RedefinableTemplateSignature_strategy)
@settings(max_examples=50)
def test_uml2withid_redefinabletemplatesignature_instantiation(instance):
    assert isinstance(instance, UML2WithID_RedefinableTemplateSignature)

@given(instance=UML2WithID_InstanceSpecification_strategy)
@settings(max_examples=50)
def test_uml2withid_instancespecification_instantiation(instance):
    assert isinstance(instance, UML2WithID_InstanceSpecification)

@given(instance=UML2WithID_StructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml2withid_structuralfeatureaction_instantiation(instance):
    assert isinstance(instance, UML2WithID_StructuralFeatureAction)

@given(instance=UML2WithID_PackageableElement_strategy)
@settings(max_examples=50)
def test_uml2withid_packageableelement_instantiation(instance):
    assert isinstance(instance, UML2WithID_PackageableElement)

@given(instance=UML2WithID_PrimitiveType_strategy)
@settings(max_examples=50)
def test_uml2withid_primitivetype_instantiation(instance):
    assert isinstance(instance, UML2WithID_PrimitiveType)

@given(instance=UML2WithID_BehavioralFeature_strategy)
@settings(max_examples=50)
def test_uml2withid_behavioralfeature_instantiation(instance):
    assert isinstance(instance, UML2WithID_BehavioralFeature)

@given(instance=UML2WithID_ControlNode_strategy)
@settings(max_examples=50)
def test_uml2withid_controlnode_instantiation(instance):
    assert isinstance(instance, UML2WithID_ControlNode)

@given(instance=UML2WithID_Association_strategy)
@settings(max_examples=50)
def test_uml2withid_association_instantiation(instance):
    assert isinstance(instance, UML2WithID_Association)

@given(instance=UML2WithID_JoinNode_strategy)
@settings(max_examples=50)
def test_uml2withid_joinnode_instantiation(instance):
    assert isinstance(instance, UML2WithID_JoinNode)

@given(instance=UML2WithID_Deployment_strategy)
@settings(max_examples=50)
def test_uml2withid_deployment_instantiation(instance):
    assert isinstance(instance, UML2WithID_Deployment)

@given(instance=UML2WithID_FinalState_strategy)
@settings(max_examples=50)
def test_uml2withid_finalstate_instantiation(instance):
    assert isinstance(instance, UML2WithID_FinalState)

@given(instance=UML2WithID_Component_strategy)
@settings(max_examples=50)
def test_uml2withid_component_instantiation(instance):
    assert isinstance(instance, UML2WithID_Component)

@given(instance=UML2WithID_StateMachine_strategy)
@settings(max_examples=50)
def test_uml2withid_statemachine_instantiation(instance):
    assert isinstance(instance, UML2WithID_StateMachine)

@given(instance=UML2WithID_StateInvariant_strategy)
@settings(max_examples=50)
def test_uml2withid_stateinvariant_instantiation(instance):
    assert isinstance(instance, UML2WithID_StateInvariant)

@given(instance=UML2WithID_ExpansionRegion_strategy)
@settings(max_examples=50)
def test_uml2withid_expansionregion_instantiation(instance):
    assert isinstance(instance, UML2WithID_ExpansionRegion)

@given(instance=UML2WithID_CallAction_strategy)
@settings(max_examples=50)
def test_uml2withid_callaction_instantiation(instance):
    assert isinstance(instance, UML2WithID_CallAction)

@given(instance=UML2WithID_ObjectNode_strategy)
@settings(max_examples=50)
def test_uml2withid_objectnode_instantiation(instance):
    assert isinstance(instance, UML2WithID_ObjectNode)

@given(instance=UML2WithID_OpaqueExpression_strategy)
@settings(max_examples=50)
def test_uml2withid_opaqueexpression_instantiation(instance):
    assert isinstance(instance, UML2WithID_OpaqueExpression)

@given(instance=UML2WithID_GeneralOrdering_strategy)
@settings(max_examples=50)
def test_uml2withid_generalordering_instantiation(instance):
    assert isinstance(instance, UML2WithID_GeneralOrdering)

@given(instance=UML2WithID_RaiseExceptionAction_strategy)
@settings(max_examples=50)
def test_uml2withid_raiseexceptionaction_instantiation(instance):
    assert isinstance(instance, UML2WithID_RaiseExceptionAction)

@given(instance=UML2WithID_Variable_strategy)
@settings(max_examples=50)
def test_uml2withid_variable_instantiation(instance):
    assert isinstance(instance, UML2WithID_Variable)

@given(instance=UML2WithID_ReadLinkObjectEndAction_strategy)
@settings(max_examples=50)
def test_uml2withid_readlinkobjectendaction_instantiation(instance):
    assert isinstance(instance, UML2WithID_ReadLinkObjectEndAction)

@given(instance=UML2WithID_ClearAssociationAction_strategy)
@settings(max_examples=50)
def test_uml2withid_clearassociationaction_instantiation(instance):
    assert isinstance(instance, UML2WithID_ClearAssociationAction)

@given(instance=UML2WithID_DirectedRelationship_strategy)
@settings(max_examples=50)
def test_uml2withid_directedrelationship_instantiation(instance):
    assert isinstance(instance, UML2WithID_DirectedRelationship)

@given(instance=UML2WithID_Usage_strategy)
@settings(max_examples=50)
def test_uml2withid_usage_instantiation(instance):
    assert isinstance(instance, UML2WithID_Usage)

@given(instance=UML2WithID_LiteralString_strategy)
@settings(max_examples=50)
def test_uml2withid_literalstring_instantiation(instance):
    assert isinstance(instance, UML2WithID_LiteralString)

@given(instance=UML2WithID_TemplateableElement_strategy)
@settings(max_examples=50)
def test_uml2withid_templateableelement_instantiation(instance):
    assert isinstance(instance, UML2WithID_TemplateableElement)

@given(instance=UML2WithID_StartOwnedBehaviorAction_strategy)
@settings(max_examples=50)
def test_uml2withid_startownedbehavioraction_instantiation(instance):
    assert isinstance(instance, UML2WithID_StartOwnedBehaviorAction)

@given(instance=UML2WithID_DeployedArtifact_strategy)
@settings(max_examples=50)
def test_uml2withid_deployedartifact_instantiation(instance):
    assert isinstance(instance, UML2WithID_DeployedArtifact)

@given(instance=UML2WithID_LiteralInteger_strategy)
@settings(max_examples=50)
def test_uml2withid_literalinteger_instantiation(instance):
    assert isinstance(instance, UML2WithID_LiteralInteger)

@given(instance=UML2WithID_StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_uml2withid_structuredactivitynode_instantiation(instance):
    assert isinstance(instance, UML2WithID_StructuredActivityNode)

@given(instance=UML2WithID_ReadLinkAction_strategy)
@settings(max_examples=50)
def test_uml2withid_readlinkaction_instantiation(instance):
    assert isinstance(instance, UML2WithID_ReadLinkAction)

@given(instance=UML2WithID_Vertex_strategy)
@settings(max_examples=50)
def test_uml2withid_vertex_instantiation(instance):
    assert isinstance(instance, UML2WithID_Vertex)

@given(instance=UML2WithID_LiteralUnlimitedNatural_strategy)
@settings(max_examples=50)
def test_uml2withid_literalunlimitednatural_instantiation(instance):
    assert isinstance(instance, UML2WithID_LiteralUnlimitedNatural)

@given(instance=UML2WithID_DataType_strategy)
@settings(max_examples=50)
def test_uml2withid_datatype_instantiation(instance):
    assert isinstance(instance, UML2WithID_DataType)

@given(instance=UML2WithID_LoopNode_strategy)
@settings(max_examples=50)
def test_uml2withid_loopnode_instantiation(instance):
    assert isinstance(instance, UML2WithID_LoopNode)

@given(instance=UML2WithID_Transition_strategy)
@settings(max_examples=50)
def test_uml2withid_transition_instantiation(instance):
    assert isinstance(instance, UML2WithID_Transition)

@given(instance=UML2WithID_ProtocolTransition_strategy)
@settings(max_examples=50)
def test_uml2withid_protocoltransition_instantiation(instance):
    assert isinstance(instance, UML2WithID_ProtocolTransition)

@given(instance=UML2WithID_UseCase_strategy)
@settings(max_examples=50)
def test_uml2withid_usecase_instantiation(instance):
    assert isinstance(instance, UML2WithID_UseCase)

@given(instance=UML2WithID_ParameterableClassifier_strategy)
@settings(max_examples=50)
def test_uml2withid_parameterableclassifier_instantiation(instance):
    assert isinstance(instance, UML2WithID_ParameterableClassifier)

@given(instance=UML2WithID_TimeInterval_strategy)
@settings(max_examples=50)
def test_uml2withid_timeinterval_instantiation(instance):
    assert isinstance(instance, UML2WithID_TimeInterval)

@given(instance=UML2WithID_ProtocolConformance_strategy)
@settings(max_examples=50)
def test_uml2withid_protocolconformance_instantiation(instance):
    assert isinstance(instance, UML2WithID_ProtocolConformance)

@given(instance=UML2WithID_Operation_strategy)
@settings(max_examples=50)
def test_uml2withid_operation_instantiation(instance):
    assert isinstance(instance, UML2WithID_Operation)

@given(instance=UML2WithID_InteractionFragment_strategy)
@settings(max_examples=50)
def test_uml2withid_interactionfragment_instantiation(instance):
    assert isinstance(instance, UML2WithID_InteractionFragment)

@given(instance=UML2WithID_Slot_strategy)
@settings(max_examples=50)
def test_uml2withid_slot_instantiation(instance):
    assert isinstance(instance, UML2WithID_Slot)

@given(instance=UML2WithID_RedefinableElement_strategy)
@settings(max_examples=50)
def test_uml2withid_redefinableelement_instantiation(instance):
    assert isinstance(instance, UML2WithID_RedefinableElement)

@given(instance=UML2WithID_ReadLinkObjectEndQualifierAction_strategy)
@settings(max_examples=50)
def test_uml2withid_readlinkobjectendqualifieraction_instantiation(instance):
    assert isinstance(instance, UML2WithID_ReadLinkObjectEndQualifierAction)

@given(instance=UML2WithID_VariableAction_strategy)
@settings(max_examples=50)
def test_uml2withid_variableaction_instantiation(instance):
    assert isinstance(instance, UML2WithID_VariableAction)

@given(instance=UML2WithID_ActivityFinalNode_strategy)
@settings(max_examples=50)
def test_uml2withid_activityfinalnode_instantiation(instance):
    assert isinstance(instance, UML2WithID_ActivityFinalNode)

@given(instance=UML2WithID_Interval_strategy)
@settings(max_examples=50)
def test_uml2withid_interval_instantiation(instance):
    assert isinstance(instance, UML2WithID_Interval)

@given(instance=UML2WithID_LinkEndCreationData_strategy)
@settings(max_examples=50)
def test_uml2withid_linkendcreationdata_instantiation(instance):
    assert isinstance(instance, UML2WithID_LinkEndCreationData)

@given(instance=UML2WithID_ReadExtentAction_strategy)
@settings(max_examples=50)
def test_uml2withid_readextentaction_instantiation(instance):
    assert isinstance(instance, UML2WithID_ReadExtentAction)

@given(instance=UML2WithID_Pseudostate_strategy)
@settings(max_examples=50)
def test_uml2withid_pseudostate_instantiation(instance):
    assert isinstance(instance, UML2WithID_Pseudostate)

@given(instance=UML2WithID_DestroyLinkAction_strategy)
@settings(max_examples=50)
def test_uml2withid_destroylinkaction_instantiation(instance):
    assert isinstance(instance, UML2WithID_DestroyLinkAction)

@given(instance=UML2WithID_FlowFinalNode_strategy)
@settings(max_examples=50)
def test_uml2withid_flowfinalnode_instantiation(instance):
    assert isinstance(instance, UML2WithID_FlowFinalNode)

@given(instance=UML2WithID_ClearStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml2withid_clearstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, UML2WithID_ClearStructuralFeatureAction)

@given(instance=UML2WithID_CombinedFragment_strategy)
@settings(max_examples=50)
def test_uml2withid_combinedfragment_instantiation(instance):
    assert isinstance(instance, UML2WithID_CombinedFragment)

@given(instance=UML2WithID_Continuation_strategy)
@settings(max_examples=50)
def test_uml2withid_continuation_instantiation(instance):
    assert isinstance(instance, UML2WithID_Continuation)

@given(instance=UML2WithID_ForkNode_strategy)
@settings(max_examples=50)
def test_uml2withid_forknode_instantiation(instance):
    assert isinstance(instance, UML2WithID_ForkNode)

@given(instance=UML2WithID_Relationship_strategy)
@settings(max_examples=50)
def test_uml2withid_relationship_instantiation(instance):
    assert isinstance(instance, UML2WithID_Relationship)

@given(instance=UML2WithID_AssociationClass_strategy)
@settings(max_examples=50)
def test_uml2withid_associationclass_instantiation(instance):
    assert isinstance(instance, UML2WithID_AssociationClass)

@given(instance=UML2WithID_ProtocolStateMachine_strategy)
@settings(max_examples=50)
def test_uml2withid_protocolstatemachine_instantiation(instance):
    assert isinstance(instance, UML2WithID_ProtocolStateMachine)

@given(instance=UML2WithID_ActivityEdge_strategy)
@settings(max_examples=50)
def test_uml2withid_activityedge_instantiation(instance):
    assert isinstance(instance, UML2WithID_ActivityEdge)

@given(instance=UML2WithID_Signal_strategy)
@settings(max_examples=50)
def test_uml2withid_signal_instantiation(instance):
    assert isinstance(instance, UML2WithID_Signal)

@given(instance=UML2WithID_DurationObservationAction_strategy)
@settings(max_examples=50)
def test_uml2withid_durationobservationaction_instantiation(instance):
    assert isinstance(instance, UML2WithID_DurationObservationAction)

@given(instance=UML2WithID_Permission_strategy)
@settings(max_examples=50)
def test_uml2withid_permission_instantiation(instance):
    assert isinstance(instance, UML2WithID_Permission)

@given(instance=UML2WithID_Artifact_strategy)
@settings(max_examples=50)
def test_uml2withid_artifact_instantiation(instance):
    assert isinstance(instance, UML2WithID_Artifact)

@given(instance=UML2WithID_ReadStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml2withid_readstructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, UML2WithID_ReadStructuralFeatureAction)

@given(instance=UML2WithID_MessageEnd_strategy)
@settings(max_examples=50)
def test_uml2withid_messageend_instantiation(instance):
    assert isinstance(instance, UML2WithID_MessageEnd)

@given(instance=UML2WithID_CallTrigger_strategy)
@settings(max_examples=50)
def test_uml2withid_calltrigger_instantiation(instance):
    assert isinstance(instance, UML2WithID_CallTrigger)

@given(instance=UML2WithID_Comment_strategy)
@settings(max_examples=50)
def test_uml2withid_comment_instantiation(instance):
    assert isinstance(instance, UML2WithID_Comment)

@given(instance=UML2WithID_DurationConstraint_strategy)
@settings(max_examples=50)
def test_uml2withid_durationconstraint_instantiation(instance):
    assert isinstance(instance, UML2WithID_DurationConstraint)

@given(instance=UML2WithID_ValueSpecification_strategy)
@settings(max_examples=50)
def test_uml2withid_valuespecification_instantiation(instance):
    assert isinstance(instance, UML2WithID_ValueSpecification)

@given(instance=UML2WithID_Parameter_strategy)
@settings(max_examples=50)
def test_uml2withid_parameter_instantiation(instance):
    assert isinstance(instance, UML2WithID_Parameter)

@given(instance=UML2WithID_ActivityPartition_strategy)
@settings(max_examples=50)
def test_uml2withid_activitypartition_instantiation(instance):
    assert isinstance(instance, UML2WithID_ActivityPartition)

@given(instance=UML2WithID_AnyTrigger_strategy)
@settings(max_examples=50)
def test_uml2withid_anytrigger_instantiation(instance):
    assert isinstance(instance, UML2WithID_AnyTrigger)

@given(instance=UML2WithID_TemplateBinding_strategy)
@settings(max_examples=50)
def test_uml2withid_templatebinding_instantiation(instance):
    assert isinstance(instance, UML2WithID_TemplateBinding)

@given(instance=UML2WithID_Constraint_strategy)
@settings(max_examples=50)
def test_uml2withid_constraint_instantiation(instance):
    assert isinstance(instance, UML2WithID_Constraint)

@given(instance=UML2WithID_Enumeration_strategy)
@settings(max_examples=50)
def test_uml2withid_enumeration_instantiation(instance):
    assert isinstance(instance, UML2WithID_Enumeration)

@given(instance=UML2WithID_BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_uml2withid_behavioredclassifier_instantiation(instance):
    assert isinstance(instance, UML2WithID_BehavioredClassifier)

@given(instance=UML2WithID_RemoveVariableValueAction_strategy)
@settings(max_examples=50)
def test_uml2withid_removevariablevalueaction_instantiation(instance):
    assert isinstance(instance, UML2WithID_RemoveVariableValueAction)

@given(instance=UML2WithID_LiteralNull_strategy)
@settings(max_examples=50)
def test_uml2withid_literalnull_instantiation(instance):
    assert isinstance(instance, UML2WithID_LiteralNull)

@given(instance=UML2WithID_ConnectableElement_strategy)
@settings(max_examples=50)
def test_uml2withid_connectableelement_instantiation(instance):
    assert isinstance(instance, UML2WithID_ConnectableElement)

@given(instance=UML2WithID_TimeObservationAction_strategy)
@settings(max_examples=50)
def test_uml2withid_timeobservationaction_instantiation(instance):
    assert isinstance(instance, UML2WithID_TimeObservationAction)

@given(instance=UML2WithID_Class_strategy)
@settings(max_examples=50)
def test_uml2withid_class_instantiation(instance):
    assert isinstance(instance, UML2WithID_Class)

@given(instance=UML2WithID_LinkEndData_strategy)
@settings(max_examples=50)
def test_uml2withid_linkenddata_instantiation(instance):
    assert isinstance(instance, UML2WithID_LinkEndData)

@given(instance=UML2WithID_TimeTrigger_strategy)
@settings(max_examples=50)
def test_uml2withid_timetrigger_instantiation(instance):
    assert isinstance(instance, UML2WithID_TimeTrigger)

@given(instance=UML2WithID_Type_strategy)
@settings(max_examples=50)
def test_uml2withid_type_instantiation(instance):
    assert isinstance(instance, UML2WithID_Type)

@given(instance=UML2WithID_StringExpression_strategy)
@settings(max_examples=50)
def test_uml2withid_stringexpression_instantiation(instance):
    assert isinstance(instance, UML2WithID_StringExpression)

@given(instance=UML2WithID_CallOperationAction_strategy)
@settings(max_examples=50)
def test_uml2withid_calloperationaction_instantiation(instance):
    assert isinstance(instance, UML2WithID_CallOperationAction)

@given(instance=UML2WithID_CentralBufferNode_strategy)
@settings(max_examples=50)
def test_uml2withid_centralbuffernode_instantiation(instance):
    assert isinstance(instance, UML2WithID_CentralBufferNode)

@given(instance=UML2WithID_ParameterableElement_strategy)
@settings(max_examples=50)
def test_uml2withid_parameterableelement_instantiation(instance):
    assert isinstance(instance, UML2WithID_ParameterableElement)

@given(instance=UML2WithID_ProfileApplication_strategy)
@settings(max_examples=50)
def test_uml2withid_profileapplication_instantiation(instance):
    assert isinstance(instance, UML2WithID_ProfileApplication)

@given(instance=UML2WithID_ExpansionNode_strategy)
@settings(max_examples=50)
def test_uml2withid_expansionnode_instantiation(instance):
    assert isinstance(instance, UML2WithID_ExpansionNode)

@given(instance=UML2WithID_Collaboration_strategy)
@settings(max_examples=50)
def test_uml2withid_collaboration_instantiation(instance):
    assert isinstance(instance, UML2WithID_Collaboration)

@given(instance=UML2WithID_State_strategy)
@settings(max_examples=50)
def test_uml2withid_state_instantiation(instance):
    assert isinstance(instance, UML2WithID_State)

@given(instance=UML2WithID_ConnectorEnd_strategy)
@settings(max_examples=50)
def test_uml2withid_connectorend_instantiation(instance):
    assert isinstance(instance, UML2WithID_ConnectorEnd)

@given(instance=UML2WithID_Include_strategy)
@settings(max_examples=50)
def test_uml2withid_include_instantiation(instance):
    assert isinstance(instance, UML2WithID_Include)

@given(instance=UML2WithID_Profile_strategy)
@settings(max_examples=50)
def test_uml2withid_profile_instantiation(instance):
    assert isinstance(instance, UML2WithID_Profile)

@given(instance=UML2WithID_Duration_strategy)
@settings(max_examples=50)
def test_uml2withid_duration_instantiation(instance):
    assert isinstance(instance, UML2WithID_Duration)

@given(instance=UML2WithID_PackageImport_strategy)
@settings(max_examples=50)
def test_uml2withid_packageimport_instantiation(instance):
    assert isinstance(instance, UML2WithID_PackageImport)

@given(instance=UML2WithID_Interface_strategy)
@settings(max_examples=50)
def test_uml2withid_interface_instantiation(instance):
    assert isinstance(instance, UML2WithID_Interface)

@given(instance=UML2WithID_ExecutionOccurrence_strategy)
@settings(max_examples=50)
def test_uml2withid_executionoccurrence_instantiation(instance):
    assert isinstance(instance, UML2WithID_ExecutionOccurrence)

@given(instance=UML2WithID_ReclassifyObjectAction_strategy)
@settings(max_examples=50)
def test_uml2withid_reclassifyobjectaction_instantiation(instance):
    assert isinstance(instance, UML2WithID_ReclassifyObjectAction)

@given(instance=UML2WithID_MessageTrigger_strategy)
@settings(max_examples=50)
def test_uml2withid_messagetrigger_instantiation(instance):
    assert isinstance(instance, UML2WithID_MessageTrigger)

@given(instance=UML2WithID_Substitution_strategy)
@settings(max_examples=50)
def test_uml2withid_substitution_instantiation(instance):
    assert isinstance(instance, UML2WithID_Substitution)

@given(instance=UML2WithID_InputPin_strategy)
@settings(max_examples=50)
def test_uml2withid_inputpin_instantiation(instance):
    assert isinstance(instance, UML2WithID_InputPin)

@given(instance=UML2WithID_Expression_strategy)
@settings(max_examples=50)
def test_uml2withid_expression_instantiation(instance):
    assert isinstance(instance, UML2WithID_Expression)

@given(instance=UML2WithID_ValuePin_strategy)
@settings(max_examples=50)
def test_uml2withid_valuepin_instantiation(instance):
    assert isinstance(instance, UML2WithID_ValuePin)

@given(instance=UML2WithID_QualifierValue_strategy)
@settings(max_examples=50)
def test_uml2withid_qualifiervalue_instantiation(instance):
    assert isinstance(instance, UML2WithID_QualifierValue)

@given(instance=UML2WithID_CollaborationOccurrence_strategy)
@settings(max_examples=50)
def test_uml2withid_collaborationoccurrence_instantiation(instance):
    assert isinstance(instance, UML2WithID_CollaborationOccurrence)

@given(instance=UML2WithID_CreateObjectAction_strategy)
@settings(max_examples=50)
def test_uml2withid_createobjectaction_instantiation(instance):
    assert isinstance(instance, UML2WithID_CreateObjectAction)

@given(instance=UML2WithID_TemplateSignature_strategy)
@settings(max_examples=50)
def test_uml2withid_templatesignature_instantiation(instance):
    assert isinstance(instance, UML2WithID_TemplateSignature)

@given(instance=UML2WithID_Abstraction_strategy)
@settings(max_examples=50)
def test_uml2withid_abstraction_instantiation(instance):
    assert isinstance(instance, UML2WithID_Abstraction)

@given(instance=UML2WithID_Trigger_strategy)
@settings(max_examples=50)
def test_uml2withid_trigger_instantiation(instance):
    assert isinstance(instance, UML2WithID_Trigger)

@given(instance=UML2WithID_Connector_strategy)
@settings(max_examples=50)
def test_uml2withid_connector_instantiation(instance):
    assert isinstance(instance, UML2WithID_Connector)

@given(instance=UML2WithID_LiteralBoolean_strategy)
@settings(max_examples=50)
def test_uml2withid_literalboolean_instantiation(instance):
    assert isinstance(instance, UML2WithID_LiteralBoolean)

@given(instance=UML2WithID_BroadcastSignalAction_strategy)
@settings(max_examples=50)
def test_uml2withid_broadcastsignalaction_instantiation(instance):
    assert isinstance(instance, UML2WithID_BroadcastSignalAction)

@given(instance=UML2WithID_ObjectFlow_strategy)
@settings(max_examples=50)
def test_uml2withid_objectflow_instantiation(instance):
    assert isinstance(instance, UML2WithID_ObjectFlow)

@given(instance=UML2WithID_PackageMerge_strategy)
@settings(max_examples=50)
def test_uml2withid_packagemerge_instantiation(instance):
    assert isinstance(instance, UML2WithID_PackageMerge)

@given(instance=UML2WithID_LinkAction_strategy)
@settings(max_examples=50)
def test_uml2withid_linkaction_instantiation(instance):
    assert isinstance(instance, UML2WithID_LinkAction)

@given(instance=UML2WithID_FinalNode_strategy)
@settings(max_examples=50)
def test_uml2withid_finalnode_instantiation(instance):
    assert isinstance(instance, UML2WithID_FinalNode)

@given(instance=UML2WithID_ExecutionEnvironment_strategy)
@settings(max_examples=50)
def test_uml2withid_executionenvironment_instantiation(instance):
    assert isinstance(instance, UML2WithID_ExecutionEnvironment)

@given(instance=UML2WithID_Message_strategy)
@settings(max_examples=50)
def test_uml2withid_message_instantiation(instance):
    assert isinstance(instance, UML2WithID_Message)

@given(instance=UML2WithID_DataStoreNode_strategy)
@settings(max_examples=50)
def test_uml2withid_datastorenode_instantiation(instance):
    assert isinstance(instance, UML2WithID_DataStoreNode)

@given(instance=UML2WithID_ClassifierTemplateParameter_strategy)
@settings(max_examples=50)
def test_uml2withid_classifiertemplateparameter_instantiation(instance):
    assert isinstance(instance, UML2WithID_ClassifierTemplateParameter)

@given(instance=UML2WithID_ClearVariableAction_strategy)
@settings(max_examples=50)
def test_uml2withid_clearvariableaction_instantiation(instance):
    assert isinstance(instance, UML2WithID_ClearVariableAction)

@given(instance=UML2WithID_Manifestation_strategy)
@settings(max_examples=50)
def test_uml2withid_manifestation_instantiation(instance):
    assert isinstance(instance, UML2WithID_Manifestation)

@given(instance=UML2WithID_InteractionConstraint_strategy)
@settings(max_examples=50)
def test_uml2withid_interactionconstraint_instantiation(instance):
    assert isinstance(instance, UML2WithID_InteractionConstraint)

@given(instance=UML2WithID_CommunicationPath_strategy)
@settings(max_examples=50)
def test_uml2withid_communicationpath_instantiation(instance):
    assert isinstance(instance, UML2WithID_CommunicationPath)

@given(instance=UML2WithID_Actor_strategy)
@settings(max_examples=50)
def test_uml2withid_actor_instantiation(instance):
    assert isinstance(instance, UML2WithID_Actor)

@given(instance=UML2WithID_ExtensionEnd_strategy)
@settings(max_examples=50)
def test_uml2withid_extensionend_instantiation(instance):
    assert isinstance(instance, UML2WithID_ExtensionEnd)

@given(instance=UML2WithID_GeneralizationSet_strategy)
@settings(max_examples=50)
def test_uml2withid_generalizationset_instantiation(instance):
    assert isinstance(instance, UML2WithID_GeneralizationSet)

@given(instance=UML2WithID_StructuralFeature_strategy)
@settings(max_examples=50)
def test_uml2withid_structuralfeature_instantiation(instance):
    assert isinstance(instance, UML2WithID_StructuralFeature)

@given(instance=UML2WithID_TemplateableClassifier_strategy)
@settings(max_examples=50)
def test_uml2withid_templateableclassifier_instantiation(instance):
    assert isinstance(instance, UML2WithID_TemplateableClassifier)

@given(instance=UML2WithID_Device_strategy)
@settings(max_examples=50)
def test_uml2withid_device_instantiation(instance):
    assert isinstance(instance, UML2WithID_Device)

@given(instance=UML2WithID_PrimitiveFunction_strategy)
@settings(max_examples=50)
def test_uml2withid_primitivefunction_instantiation(instance):
    assert isinstance(instance, UML2WithID_PrimitiveFunction)

@given(instance=UML2WithID_ConnectionPointReference_strategy)
@settings(max_examples=50)
def test_uml2withid_connectionpointreference_instantiation(instance):
    assert isinstance(instance, UML2WithID_ConnectionPointReference)

@given(instance=UML2WithID_PartDecomposition_strategy)
@settings(max_examples=50)
def test_uml2withid_partdecomposition_instantiation(instance):
    assert isinstance(instance, UML2WithID_PartDecomposition)

@given(instance=UML2WithID_ReadSelfAction_strategy)
@settings(max_examples=50)
def test_uml2withid_readselfaction_instantiation(instance):
    assert isinstance(instance, UML2WithID_ReadSelfAction)

@given(instance=UML2WithID_MultiplicityElement_strategy)
@settings(max_examples=50)
def test_uml2withid_multiplicityelement_instantiation(instance):
    assert isinstance(instance, UML2WithID_MultiplicityElement)

@given(instance=UML2WithID_DurationInterval_strategy)
@settings(max_examples=50)
def test_uml2withid_durationinterval_instantiation(instance):
    assert isinstance(instance, UML2WithID_DurationInterval)

@given(instance=UML2WithID_AcceptEventAction_strategy)
@settings(max_examples=50)
def test_uml2withid_accepteventaction_instantiation(instance):
    assert isinstance(instance, UML2WithID_AcceptEventAction)

@given(instance=UML2WithID_SignalTrigger_strategy)
@settings(max_examples=50)
def test_uml2withid_signaltrigger_instantiation(instance):
    assert isinstance(instance, UML2WithID_SignalTrigger)

@given(instance=UML2WithID_SendObjectAction_strategy)
@settings(max_examples=50)
def test_uml2withid_sendobjectaction_instantiation(instance):
    assert isinstance(instance, UML2WithID_SendObjectAction)

@given(instance=UML2WithID_WriteStructuralFeatureAction_strategy)
@settings(max_examples=50)
def test_uml2withid_writestructuralfeatureaction_instantiation(instance):
    assert isinstance(instance, UML2WithID_WriteStructuralFeatureAction)

@given(instance=UML2WithID_Lifeline_strategy)
@settings(max_examples=50)
def test_uml2withid_lifeline_instantiation(instance):
    assert isinstance(instance, UML2WithID_Lifeline)

@given(instance=UML2WithID_ReadVariableAction_strategy)
@settings(max_examples=50)
def test_uml2withid_readvariableaction_instantiation(instance):
    assert isinstance(instance, UML2WithID_ReadVariableAction)

@given(instance=UML2WithID_LiteralSpecification_strategy)
@settings(max_examples=50)
def test_uml2withid_literalspecification_instantiation(instance):
    assert isinstance(instance, UML2WithID_LiteralSpecification)

@given(instance=UML2WithID_DecisionNode_strategy)
@settings(max_examples=50)
def test_uml2withid_decisionnode_instantiation(instance):
    assert isinstance(instance, UML2WithID_DecisionNode)

@given(instance=UML2WithID_DeploymentTarget_strategy)
@settings(max_examples=50)
def test_uml2withid_deploymenttarget_instantiation(instance):
    assert isinstance(instance, UML2WithID_DeploymentTarget)

@given(instance=UML2WithID_ReadIsClassifiedObjectAction_strategy)
@settings(max_examples=50)
def test_uml2withid_readisclassifiedobjectaction_instantiation(instance):
    assert isinstance(instance, UML2WithID_ReadIsClassifiedObjectAction)

@given(instance=UML2WithID_Package_strategy)
@settings(max_examples=50)
def test_uml2withid_package_instantiation(instance):
    assert isinstance(instance, UML2WithID_Package)

@given(instance=UML2WithID_TypedElement_strategy)
@settings(max_examples=50)
def test_uml2withid_typedelement_instantiation(instance):
    assert isinstance(instance, UML2WithID_TypedElement)

@given(instance=UML2WithID_InformationFlow_strategy)
@settings(max_examples=50)
def test_uml2withid_informationflow_instantiation(instance):
    assert isinstance(instance, UML2WithID_InformationFlow)

@given(instance=UML2WithID_InteractionOccurrence_strategy)
@settings(max_examples=50)
def test_uml2withid_interactionoccurrence_instantiation(instance):
    assert isinstance(instance, UML2WithID_InteractionOccurrence)

@given(instance=UML2WithID_ActivityParameterNode_strategy)
@settings(max_examples=50)
def test_uml2withid_activityparameternode_instantiation(instance):
    assert isinstance(instance, UML2WithID_ActivityParameterNode)

@given(instance=UML2WithID_WriteLinkAction_strategy)
@settings(max_examples=50)
def test_uml2withid_writelinkaction_instantiation(instance):
    assert isinstance(instance, UML2WithID_WriteLinkAction)

@given(instance=UML2WithID_ElementImport_strategy)
@settings(max_examples=50)
def test_uml2withid_elementimport_instantiation(instance):
    assert isinstance(instance, UML2WithID_ElementImport)

@given(instance=UML2WithID_TemplateParameterSubstitution_strategy)
@settings(max_examples=50)
def test_uml2withid_templateparametersubstitution_instantiation(instance):
    assert isinstance(instance, UML2WithID_TemplateParameterSubstitution)

@given(instance=UML2WithID_RemoveStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_uml2withid_removestructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, UML2WithID_RemoveStructuralFeatureValueAction)

@given(instance=UML2WithID_StructuredClassifier_strategy)
@settings(max_examples=50)
def test_uml2withid_structuredclassifier_instantiation(instance):
    assert isinstance(instance, UML2WithID_StructuredClassifier)

@given(instance=UML2WithID_OperationTemplateParameter_strategy)
@settings(max_examples=50)
def test_uml2withid_operationtemplateparameter_instantiation(instance):
    assert isinstance(instance, UML2WithID_OperationTemplateParameter)

@given(instance=UML2WithID_ConditionalNode_strategy)
@settings(max_examples=50)
def test_uml2withid_conditionalnode_instantiation(instance):
    assert isinstance(instance, UML2WithID_ConditionalNode)

@given(instance=UML2WithID_AcceptCallAction_strategy)
@settings(max_examples=50)
def test_uml2withid_acceptcallaction_instantiation(instance):
    assert isinstance(instance, UML2WithID_AcceptCallAction)

@given(instance=UML2WithID_Feature_strategy)
@settings(max_examples=50)
def test_uml2withid_feature_instantiation(instance):
    assert isinstance(instance, UML2WithID_Feature)

@given(instance=UML2WithID_WriteVariableAction_strategy)
@settings(max_examples=50)
def test_uml2withid_writevariableaction_instantiation(instance):
    assert isinstance(instance, UML2WithID_WriteVariableAction)

@given(instance=UML2WithID_Behavior_strategy)
@settings(max_examples=50)
def test_uml2withid_behavior_instantiation(instance):
    assert isinstance(instance, UML2WithID_Behavior)

@given(instance=UML2WithID_InformationItem_strategy)
@settings(max_examples=50)
def test_uml2withid_informationitem_instantiation(instance):
    assert isinstance(instance, UML2WithID_InformationItem)

@given(instance=UML2WithID_Dependency_strategy)
@settings(max_examples=50)
def test_uml2withid_dependency_instantiation(instance):
    assert isinstance(instance, UML2WithID_Dependency)

@given(instance=UML2WithID_Classifier_strategy)
@settings(max_examples=50)
def test_uml2withid_classifier_instantiation(instance):
    assert isinstance(instance, UML2WithID_Classifier)

@given(instance=UML2WithID_ApplyFunctionAction_strategy)
@settings(max_examples=50)
def test_uml2withid_applyfunctionaction_instantiation(instance):
    assert isinstance(instance, UML2WithID_ApplyFunctionAction)

@given(instance=UML2WithID_ExtensionPoint_strategy)
@settings(max_examples=50)
def test_uml2withid_extensionpoint_instantiation(instance):
    assert isinstance(instance, UML2WithID_ExtensionPoint)

@given(instance=UML2WithID_AddStructuralFeatureValueAction_strategy)
@settings(max_examples=50)
def test_uml2withid_addstructuralfeaturevalueaction_instantiation(instance):
    assert isinstance(instance, UML2WithID_AddStructuralFeatureValueAction)

@given(instance=UML2WithID_ParameterSet_strategy)
@settings(max_examples=50)
def test_uml2withid_parameterset_instantiation(instance):
    assert isinstance(instance, UML2WithID_ParameterSet)

@given(instance=MessageEnd_strategy)
@settings(max_examples=50)
def test_messageend_instantiation(instance):
    assert isinstance(instance, MessageEnd)

@given(instance=UML2WithID_EventOccurrence_strategy)
@settings(max_examples=50)
def test_uml2withid_eventoccurrence_instantiation(instance):
    assert isinstance(instance, UML2WithID_EventOccurrence)

@given(instance=UML2WithID_Gate_strategy)
@settings(max_examples=50)
def test_uml2withid_gate_instantiation(instance):
    assert isinstance(instance, UML2WithID_Gate)
