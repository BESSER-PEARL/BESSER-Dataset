import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ExpansionRegion,
    ExpansionNode,
    Activities_ExtraStructuredActivities_Classifier,
    Classifier,
    Activities_CompleteStructuredActivities_InputPin,
    ExecutableNode,
    Clause,
    Activities_StructuredActivities_MultiplicityElement,
    Activities_StructuredActivities_OutputPin,
    StructuredActivities_MultiplicityElement,
    ExceptionHandler,
    IntermediateActivities_Feature,
    FundamentalActivities_Namespace,
    Activities_IntermediateActivities_BehavioralFeature,
    CentralBufferNode,
    Activities_IntermediateActivities_DataStoreNode,
    Activities_IntermediateActivities_State,
    Activities_IntermediateActivities_Constraint,
    Activities_IntermediateActivities_Element,
    FundamentalActivities_Action,
    FundamentalActivities_ActivityGroup,
    StructuredActivities_ExecutableNode,
    Activities_StructuredActivities_StructuredActivityNode,
    Activities_IntermediateActivities_Class,
    Activities_IntermediateActivities_Feature,
    FinalNode,
    Activities_IntermediateActivities_FlowFinalNode,
    State,
    Element,
    Activities_ExtraStructuredActivities_ExceptionHandler,
    Activities_StructuredActivities_Clause,
    Activities_IntermediateActivities_ValueSpecification,
    ObjectFlow,
    ControlNode,
    Activities_IntermediateActivities_ForkNode,
    Activities_IntermediateActivities_JoinNode,
    Activities_IntermediateActivities_FinalNode,
    Activities_IntermediateActivities_DecisionNode,
    Activities_IntermediateActivities_MergeNode,
    Activities_BasicActivities_InitialNode,
    IntermediateActivities_FinalNode,
    BasicActivities_ControlNode,
    Activities_BasicActivities_ActivityFinalNode,
    Activities_BasicActivities_Parameter,
    Parameter,
    ObjectNode,
    Activities_IntermediateActivities_CentralBufferNode,
    Activities_BasicActivities_ActivityParameterNode,
    Activities_ExtraStructuredActivities_ExpansionNode,
    Activities_BasicActivities_Pin,
    Activities_BasicActivities_TypedElement,
    BasicActivities_TypedElement,
    Activities_StructuredActivities_Variable,
    ValueSpecification,
    OutputPin,
    InputPin,
    Constraint,
    InterruptibleActivityRegion,
    FundamentalActivities_ActivityNode,
    Activities_BasicActivities_ObjectNode,
    RedefinableElement,
    Activities_BasicActivities_ActivityEdge,
    Activities_BasicActivities_RedefinableElement,
    Activities_FundamentalActivities_Namespace,
    Activity,
    NamedElement,
    Activities_IntermediateActivities_ParameterSet,
    Activities_FundamentalActivities_ActivityGroup,
    ActivityPartition,
    ActivityEdge,
    Activities_BasicActivities_ObjectFlow,
    Activities_BasicActivities_ControlFlow,
    ActivityGroup,
    Activities_IntermediateActivities_InterruptibleActivityRegion,
    Activities_IntermediateActivities_ActivityPartition,
    ActivityNode,
    Activities_BasicActivities_ControlNode,
    Activities_FundamentalActivities_Action,
    Activities_StructuredActivities_ExecutableNode,
    Behavior,
    Activities_FundamentalActivities_Activity,
    BasicActivities_RedefinableElement,
    FundamentalActivities_NamedElement,
    Activities_FundamentalActivities_ActivityNode,
    Activities_FundamentalActivities_NamedElement,
    ParameterSet,
    Class,
    Activities_FundamentalActivities_Behavior,
    Variable,
    StructuredActivityNode,
    Activities_ExtraStructuredActivities_ExpansionRegion,
    Activities_StructuredActivities_SequenceNode,
    Activities_StructuredActivities_LoopNode,
    Activities_StructuredActivities_ConditionalNode,
    ExpansionKind,
    ParameterEffectKind,
    ObjectNodeOrderingKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_expansionregion_is_not_abstract():
    assert not inspect.isabstract(ExpansionRegion)


def test_expansionregion_constructor_exists():
    assert callable(ExpansionRegion.__init__)


def test_expansionregion_constructor_args():
    sig = inspect.signature(ExpansionRegion.__init__)
    params = list(sig.parameters.keys())



def test_expansionnode_is_not_abstract():
    assert not inspect.isabstract(ExpansionNode)


def test_expansionnode_constructor_exists():
    assert callable(ExpansionNode.__init__)


def test_expansionnode_constructor_args():
    sig = inspect.signature(ExpansionNode.__init__)
    params = list(sig.parameters.keys())



def test_activities_extrastructuredactivities_classifier_is_not_abstract():
    assert not inspect.isabstract(Activities_ExtraStructuredActivities_Classifier)


def test_activities_extrastructuredactivities_classifier_constructor_exists():
    assert callable(Activities_ExtraStructuredActivities_Classifier.__init__)


def test_activities_extrastructuredactivities_classifier_constructor_args():
    sig = inspect.signature(Activities_ExtraStructuredActivities_Classifier.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_activities_completestructuredactivities_inputpin_is_not_abstract():
    assert not inspect.isabstract(Activities_CompleteStructuredActivities_InputPin)


def test_activities_completestructuredactivities_inputpin_constructor_exists():
    assert callable(Activities_CompleteStructuredActivities_InputPin.__init__)


def test_activities_completestructuredactivities_inputpin_constructor_args():
    sig = inspect.signature(Activities_CompleteStructuredActivities_InputPin.__init__)
    params = list(sig.parameters.keys())



def test_executablenode_is_not_abstract():
    assert not inspect.isabstract(ExecutableNode)


def test_executablenode_constructor_exists():
    assert callable(ExecutableNode.__init__)


def test_executablenode_constructor_args():
    sig = inspect.signature(ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_clause_is_not_abstract():
    assert not inspect.isabstract(Clause)


def test_clause_constructor_exists():
    assert callable(Clause.__init__)


def test_clause_constructor_args():
    sig = inspect.signature(Clause.__init__)
    params = list(sig.parameters.keys())



def test_activities_structuredactivities_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(Activities_StructuredActivities_MultiplicityElement)


def test_activities_structuredactivities_multiplicityelement_constructor_exists():
    assert callable(Activities_StructuredActivities_MultiplicityElement.__init__)


def test_activities_structuredactivities_multiplicityelement_constructor_args():
    sig = inspect.signature(Activities_StructuredActivities_MultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_activities_structuredactivities_outputpin_is_not_abstract():
    assert not inspect.isabstract(Activities_StructuredActivities_OutputPin)


def test_activities_structuredactivities_outputpin_constructor_exists():
    assert callable(Activities_StructuredActivities_OutputPin.__init__)


def test_activities_structuredactivities_outputpin_constructor_args():
    sig = inspect.signature(Activities_StructuredActivities_OutputPin.__init__)
    params = list(sig.parameters.keys())



def test_structuredactivities_multiplicityelement_is_not_abstract():
    assert not inspect.isabstract(StructuredActivities_MultiplicityElement)


def test_structuredactivities_multiplicityelement_constructor_exists():
    assert callable(StructuredActivities_MultiplicityElement.__init__)


def test_structuredactivities_multiplicityelement_constructor_args():
    sig = inspect.signature(StructuredActivities_MultiplicityElement.__init__)
    params = list(sig.parameters.keys())



def test_exceptionhandler_is_not_abstract():
    assert not inspect.isabstract(ExceptionHandler)


def test_exceptionhandler_constructor_exists():
    assert callable(ExceptionHandler.__init__)


def test_exceptionhandler_constructor_args():
    sig = inspect.signature(ExceptionHandler.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities_feature_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities_Feature)


def test_intermediateactivities_feature_constructor_exists():
    assert callable(IntermediateActivities_Feature.__init__)


def test_intermediateactivities_feature_constructor_args():
    sig = inspect.signature(IntermediateActivities_Feature.__init__)
    params = list(sig.parameters.keys())



def test_fundamentalactivities_namespace_is_not_abstract():
    assert not inspect.isabstract(FundamentalActivities_Namespace)


def test_fundamentalactivities_namespace_constructor_exists():
    assert callable(FundamentalActivities_Namespace.__init__)


def test_fundamentalactivities_namespace_constructor_args():
    sig = inspect.signature(FundamentalActivities_Namespace.__init__)
    params = list(sig.parameters.keys())



def test_activities_intermediateactivities_behavioralfeature_is_not_abstract():
    assert not inspect.isabstract(Activities_IntermediateActivities_BehavioralFeature)


def test_activities_intermediateactivities_behavioralfeature_constructor_exists():
    assert callable(Activities_IntermediateActivities_BehavioralFeature.__init__)


def test_activities_intermediateactivities_behavioralfeature_constructor_args():
    sig = inspect.signature(Activities_IntermediateActivities_BehavioralFeature.__init__)
    params = list(sig.parameters.keys())



def test_centralbuffernode_is_not_abstract():
    assert not inspect.isabstract(CentralBufferNode)


def test_centralbuffernode_constructor_exists():
    assert callable(CentralBufferNode.__init__)


def test_centralbuffernode_constructor_args():
    sig = inspect.signature(CentralBufferNode.__init__)
    params = list(sig.parameters.keys())



def test_activities_intermediateactivities_datastorenode_is_not_abstract():
    assert not inspect.isabstract(Activities_IntermediateActivities_DataStoreNode)


def test_activities_intermediateactivities_datastorenode_constructor_exists():
    assert callable(Activities_IntermediateActivities_DataStoreNode.__init__)


def test_activities_intermediateactivities_datastorenode_constructor_args():
    sig = inspect.signature(Activities_IntermediateActivities_DataStoreNode.__init__)
    params = list(sig.parameters.keys())



def test_activities_intermediateactivities_state_is_not_abstract():
    assert not inspect.isabstract(Activities_IntermediateActivities_State)


def test_activities_intermediateactivities_state_constructor_exists():
    assert callable(Activities_IntermediateActivities_State.__init__)


def test_activities_intermediateactivities_state_constructor_args():
    sig = inspect.signature(Activities_IntermediateActivities_State.__init__)
    params = list(sig.parameters.keys())



def test_activities_intermediateactivities_constraint_is_not_abstract():
    assert not inspect.isabstract(Activities_IntermediateActivities_Constraint)


def test_activities_intermediateactivities_constraint_constructor_exists():
    assert callable(Activities_IntermediateActivities_Constraint.__init__)


def test_activities_intermediateactivities_constraint_constructor_args():
    sig = inspect.signature(Activities_IntermediateActivities_Constraint.__init__)
    params = list(sig.parameters.keys())



def test_activities_intermediateactivities_element_is_not_abstract():
    assert not inspect.isabstract(Activities_IntermediateActivities_Element)


def test_activities_intermediateactivities_element_constructor_exists():
    assert callable(Activities_IntermediateActivities_Element.__init__)


def test_activities_intermediateactivities_element_constructor_args():
    sig = inspect.signature(Activities_IntermediateActivities_Element.__init__)
    params = list(sig.parameters.keys())



def test_fundamentalactivities_action_is_not_abstract():
    assert not inspect.isabstract(FundamentalActivities_Action)


def test_fundamentalactivities_action_constructor_exists():
    assert callable(FundamentalActivities_Action.__init__)


def test_fundamentalactivities_action_constructor_args():
    sig = inspect.signature(FundamentalActivities_Action.__init__)
    params = list(sig.parameters.keys())



def test_fundamentalactivities_activitygroup_is_not_abstract():
    assert not inspect.isabstract(FundamentalActivities_ActivityGroup)


def test_fundamentalactivities_activitygroup_constructor_exists():
    assert callable(FundamentalActivities_ActivityGroup.__init__)


def test_fundamentalactivities_activitygroup_constructor_args():
    sig = inspect.signature(FundamentalActivities_ActivityGroup.__init__)
    params = list(sig.parameters.keys())



def test_structuredactivities_executablenode_is_not_abstract():
    assert not inspect.isabstract(StructuredActivities_ExecutableNode)


def test_structuredactivities_executablenode_constructor_exists():
    assert callable(StructuredActivities_ExecutableNode.__init__)


def test_structuredactivities_executablenode_constructor_args():
    sig = inspect.signature(StructuredActivities_ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_activities_structuredactivities_structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(Activities_StructuredActivities_StructuredActivityNode)


def test_activities_structuredactivities_structuredactivitynode_constructor_exists():
    assert callable(Activities_StructuredActivities_StructuredActivityNode.__init__)


def test_activities_structuredactivities_structuredactivitynode_constructor_args():
    sig = inspect.signature(Activities_StructuredActivities_StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())
    assert "mustIsolate" in params, "Missing parameter 'mustIsolate'"

def test_activities_structuredactivities_structuredactivitynode_has_mustIsolate():
    assert hasattr(Activities_StructuredActivities_StructuredActivityNode, "mustIsolate")
    descriptor = None
    for klass in Activities_StructuredActivities_StructuredActivityNode.__mro__:
        if "mustIsolate" in klass.__dict__:
            descriptor = klass.__dict__["mustIsolate"]
            break
    assert isinstance(descriptor, property)



def test_activities_intermediateactivities_class_is_not_abstract():
    assert not inspect.isabstract(Activities_IntermediateActivities_Class)


def test_activities_intermediateactivities_class_constructor_exists():
    assert callable(Activities_IntermediateActivities_Class.__init__)


def test_activities_intermediateactivities_class_constructor_args():
    sig = inspect.signature(Activities_IntermediateActivities_Class.__init__)
    params = list(sig.parameters.keys())



def test_activities_intermediateactivities_feature_is_not_abstract():
    assert not inspect.isabstract(Activities_IntermediateActivities_Feature)


def test_activities_intermediateactivities_feature_constructor_exists():
    assert callable(Activities_IntermediateActivities_Feature.__init__)


def test_activities_intermediateactivities_feature_constructor_args():
    sig = inspect.signature(Activities_IntermediateActivities_Feature.__init__)
    params = list(sig.parameters.keys())



def test_finalnode_is_not_abstract():
    assert not inspect.isabstract(FinalNode)


def test_finalnode_constructor_exists():
    assert callable(FinalNode.__init__)


def test_finalnode_constructor_args():
    sig = inspect.signature(FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_activities_intermediateactivities_flowfinalnode_is_not_abstract():
    assert not inspect.isabstract(Activities_IntermediateActivities_FlowFinalNode)


def test_activities_intermediateactivities_flowfinalnode_constructor_exists():
    assert callable(Activities_IntermediateActivities_FlowFinalNode.__init__)


def test_activities_intermediateactivities_flowfinalnode_constructor_args():
    sig = inspect.signature(Activities_IntermediateActivities_FlowFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_activities_extrastructuredactivities_exceptionhandler_is_not_abstract():
    assert not inspect.isabstract(Activities_ExtraStructuredActivities_ExceptionHandler)


def test_activities_extrastructuredactivities_exceptionhandler_constructor_exists():
    assert callable(Activities_ExtraStructuredActivities_ExceptionHandler.__init__)


def test_activities_extrastructuredactivities_exceptionhandler_constructor_args():
    sig = inspect.signature(Activities_ExtraStructuredActivities_ExceptionHandler.__init__)
    params = list(sig.parameters.keys())



def test_activities_structuredactivities_clause_is_not_abstract():
    assert not inspect.isabstract(Activities_StructuredActivities_Clause)


def test_activities_structuredactivities_clause_constructor_exists():
    assert callable(Activities_StructuredActivities_Clause.__init__)


def test_activities_structuredactivities_clause_constructor_args():
    sig = inspect.signature(Activities_StructuredActivities_Clause.__init__)
    params = list(sig.parameters.keys())



def test_activities_intermediateactivities_valuespecification_is_not_abstract():
    assert not inspect.isabstract(Activities_IntermediateActivities_ValueSpecification)


def test_activities_intermediateactivities_valuespecification_constructor_exists():
    assert callable(Activities_IntermediateActivities_ValueSpecification.__init__)


def test_activities_intermediateactivities_valuespecification_constructor_args():
    sig = inspect.signature(Activities_IntermediateActivities_ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_objectflow_is_not_abstract():
    assert not inspect.isabstract(ObjectFlow)


def test_objectflow_constructor_exists():
    assert callable(ObjectFlow.__init__)


def test_objectflow_constructor_args():
    sig = inspect.signature(ObjectFlow.__init__)
    params = list(sig.parameters.keys())



def test_controlnode_is_not_abstract():
    assert not inspect.isabstract(ControlNode)


def test_controlnode_constructor_exists():
    assert callable(ControlNode.__init__)


def test_controlnode_constructor_args():
    sig = inspect.signature(ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_activities_intermediateactivities_forknode_is_not_abstract():
    assert not inspect.isabstract(Activities_IntermediateActivities_ForkNode)


def test_activities_intermediateactivities_forknode_constructor_exists():
    assert callable(Activities_IntermediateActivities_ForkNode.__init__)


def test_activities_intermediateactivities_forknode_constructor_args():
    sig = inspect.signature(Activities_IntermediateActivities_ForkNode.__init__)
    params = list(sig.parameters.keys())



def test_activities_intermediateactivities_joinnode_is_not_abstract():
    assert not inspect.isabstract(Activities_IntermediateActivities_JoinNode)


def test_activities_intermediateactivities_joinnode_constructor_exists():
    assert callable(Activities_IntermediateActivities_JoinNode.__init__)


def test_activities_intermediateactivities_joinnode_constructor_args():
    sig = inspect.signature(Activities_IntermediateActivities_JoinNode.__init__)
    params = list(sig.parameters.keys())
    assert "isCombineDuplicate" in params, "Missing parameter 'isCombineDuplicate'"

def test_activities_intermediateactivities_joinnode_has_isCombineDuplicate():
    assert hasattr(Activities_IntermediateActivities_JoinNode, "isCombineDuplicate")
    descriptor = None
    for klass in Activities_IntermediateActivities_JoinNode.__mro__:
        if "isCombineDuplicate" in klass.__dict__:
            descriptor = klass.__dict__["isCombineDuplicate"]
            break
    assert isinstance(descriptor, property)



def test_activities_intermediateactivities_finalnode_is_not_abstract():
    assert not inspect.isabstract(Activities_IntermediateActivities_FinalNode)


def test_activities_intermediateactivities_finalnode_constructor_exists():
    assert callable(Activities_IntermediateActivities_FinalNode.__init__)


def test_activities_intermediateactivities_finalnode_constructor_args():
    sig = inspect.signature(Activities_IntermediateActivities_FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_activities_intermediateactivities_decisionnode_is_not_abstract():
    assert not inspect.isabstract(Activities_IntermediateActivities_DecisionNode)


def test_activities_intermediateactivities_decisionnode_constructor_exists():
    assert callable(Activities_IntermediateActivities_DecisionNode.__init__)


def test_activities_intermediateactivities_decisionnode_constructor_args():
    sig = inspect.signature(Activities_IntermediateActivities_DecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_activities_intermediateactivities_mergenode_is_not_abstract():
    assert not inspect.isabstract(Activities_IntermediateActivities_MergeNode)


def test_activities_intermediateactivities_mergenode_constructor_exists():
    assert callable(Activities_IntermediateActivities_MergeNode.__init__)


def test_activities_intermediateactivities_mergenode_constructor_args():
    sig = inspect.signature(Activities_IntermediateActivities_MergeNode.__init__)
    params = list(sig.parameters.keys())



def test_activities_basicactivities_initialnode_is_not_abstract():
    assert not inspect.isabstract(Activities_BasicActivities_InitialNode)


def test_activities_basicactivities_initialnode_constructor_exists():
    assert callable(Activities_BasicActivities_InitialNode.__init__)


def test_activities_basicactivities_initialnode_constructor_args():
    sig = inspect.signature(Activities_BasicActivities_InitialNode.__init__)
    params = list(sig.parameters.keys())



def test_intermediateactivities_finalnode_is_not_abstract():
    assert not inspect.isabstract(IntermediateActivities_FinalNode)


def test_intermediateactivities_finalnode_constructor_exists():
    assert callable(IntermediateActivities_FinalNode.__init__)


def test_intermediateactivities_finalnode_constructor_args():
    sig = inspect.signature(IntermediateActivities_FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_basicactivities_controlnode_is_not_abstract():
    assert not inspect.isabstract(BasicActivities_ControlNode)


def test_basicactivities_controlnode_constructor_exists():
    assert callable(BasicActivities_ControlNode.__init__)


def test_basicactivities_controlnode_constructor_args():
    sig = inspect.signature(BasicActivities_ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_activities_basicactivities_activityfinalnode_is_not_abstract():
    assert not inspect.isabstract(Activities_BasicActivities_ActivityFinalNode)


def test_activities_basicactivities_activityfinalnode_constructor_exists():
    assert callable(Activities_BasicActivities_ActivityFinalNode.__init__)


def test_activities_basicactivities_activityfinalnode_constructor_args():
    sig = inspect.signature(Activities_BasicActivities_ActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_activities_basicactivities_parameter_is_not_abstract():
    assert not inspect.isabstract(Activities_BasicActivities_Parameter)


def test_activities_basicactivities_parameter_constructor_exists():
    assert callable(Activities_BasicActivities_Parameter.__init__)


def test_activities_basicactivities_parameter_constructor_args():
    sig = inspect.signature(Activities_BasicActivities_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "effect" in params, "Missing parameter 'effect'"
    assert "isException" in params, "Missing parameter 'isException'"
    assert "isStream" in params, "Missing parameter 'isStream'"

def test_activities_basicactivities_parameter_has_effect():
    assert hasattr(Activities_BasicActivities_Parameter, "effect")
    descriptor = None
    for klass in Activities_BasicActivities_Parameter.__mro__:
        if "effect" in klass.__dict__:
            descriptor = klass.__dict__["effect"]
            break
    assert isinstance(descriptor, property)

def test_activities_basicactivities_parameter_has_isException():
    assert hasattr(Activities_BasicActivities_Parameter, "isException")
    descriptor = None
    for klass in Activities_BasicActivities_Parameter.__mro__:
        if "isException" in klass.__dict__:
            descriptor = klass.__dict__["isException"]
            break
    assert isinstance(descriptor, property)

def test_activities_basicactivities_parameter_has_isStream():
    assert hasattr(Activities_BasicActivities_Parameter, "isStream")
    descriptor = None
    for klass in Activities_BasicActivities_Parameter.__mro__:
        if "isStream" in klass.__dict__:
            descriptor = klass.__dict__["isStream"]
            break
    assert isinstance(descriptor, property)



def test_parameter_is_not_abstract():
    assert not inspect.isabstract(Parameter)


def test_parameter_constructor_exists():
    assert callable(Parameter.__init__)


def test_parameter_constructor_args():
    sig = inspect.signature(Parameter.__init__)
    params = list(sig.parameters.keys())



def test_objectnode_is_not_abstract():
    assert not inspect.isabstract(ObjectNode)


def test_objectnode_constructor_exists():
    assert callable(ObjectNode.__init__)


def test_objectnode_constructor_args():
    sig = inspect.signature(ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_activities_intermediateactivities_centralbuffernode_is_not_abstract():
    assert not inspect.isabstract(Activities_IntermediateActivities_CentralBufferNode)


def test_activities_intermediateactivities_centralbuffernode_constructor_exists():
    assert callable(Activities_IntermediateActivities_CentralBufferNode.__init__)


def test_activities_intermediateactivities_centralbuffernode_constructor_args():
    sig = inspect.signature(Activities_IntermediateActivities_CentralBufferNode.__init__)
    params = list(sig.parameters.keys())



def test_activities_basicactivities_activityparameternode_is_not_abstract():
    assert not inspect.isabstract(Activities_BasicActivities_ActivityParameterNode)


def test_activities_basicactivities_activityparameternode_constructor_exists():
    assert callable(Activities_BasicActivities_ActivityParameterNode.__init__)


def test_activities_basicactivities_activityparameternode_constructor_args():
    sig = inspect.signature(Activities_BasicActivities_ActivityParameterNode.__init__)
    params = list(sig.parameters.keys())



def test_activities_extrastructuredactivities_expansionnode_is_not_abstract():
    assert not inspect.isabstract(Activities_ExtraStructuredActivities_ExpansionNode)


def test_activities_extrastructuredactivities_expansionnode_constructor_exists():
    assert callable(Activities_ExtraStructuredActivities_ExpansionNode.__init__)


def test_activities_extrastructuredactivities_expansionnode_constructor_args():
    sig = inspect.signature(Activities_ExtraStructuredActivities_ExpansionNode.__init__)
    params = list(sig.parameters.keys())



def test_activities_basicactivities_pin_is_not_abstract():
    assert not inspect.isabstract(Activities_BasicActivities_Pin)


def test_activities_basicactivities_pin_constructor_exists():
    assert callable(Activities_BasicActivities_Pin.__init__)


def test_activities_basicactivities_pin_constructor_args():
    sig = inspect.signature(Activities_BasicActivities_Pin.__init__)
    params = list(sig.parameters.keys())
    assert "isControl" in params, "Missing parameter 'isControl'"

def test_activities_basicactivities_pin_has_isControl():
    assert hasattr(Activities_BasicActivities_Pin, "isControl")
    descriptor = None
    for klass in Activities_BasicActivities_Pin.__mro__:
        if "isControl" in klass.__dict__:
            descriptor = klass.__dict__["isControl"]
            break
    assert isinstance(descriptor, property)



def test_activities_basicactivities_typedelement_is_not_abstract():
    assert not inspect.isabstract(Activities_BasicActivities_TypedElement)


def test_activities_basicactivities_typedelement_constructor_exists():
    assert callable(Activities_BasicActivities_TypedElement.__init__)


def test_activities_basicactivities_typedelement_constructor_args():
    sig = inspect.signature(Activities_BasicActivities_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_basicactivities_typedelement_is_not_abstract():
    assert not inspect.isabstract(BasicActivities_TypedElement)


def test_basicactivities_typedelement_constructor_exists():
    assert callable(BasicActivities_TypedElement.__init__)


def test_basicactivities_typedelement_constructor_args():
    sig = inspect.signature(BasicActivities_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_activities_structuredactivities_variable_is_not_abstract():
    assert not inspect.isabstract(Activities_StructuredActivities_Variable)


def test_activities_structuredactivities_variable_constructor_exists():
    assert callable(Activities_StructuredActivities_Variable.__init__)


def test_activities_structuredactivities_variable_constructor_args():
    sig = inspect.signature(Activities_StructuredActivities_Variable.__init__)
    params = list(sig.parameters.keys())



def test_valuespecification_is_not_abstract():
    assert not inspect.isabstract(ValueSpecification)


def test_valuespecification_constructor_exists():
    assert callable(ValueSpecification.__init__)


def test_valuespecification_constructor_args():
    sig = inspect.signature(ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_outputpin_is_not_abstract():
    assert not inspect.isabstract(OutputPin)


def test_outputpin_constructor_exists():
    assert callable(OutputPin.__init__)


def test_outputpin_constructor_args():
    sig = inspect.signature(OutputPin.__init__)
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



def test_interruptibleactivityregion_is_not_abstract():
    assert not inspect.isabstract(InterruptibleActivityRegion)


def test_interruptibleactivityregion_constructor_exists():
    assert callable(InterruptibleActivityRegion.__init__)


def test_interruptibleactivityregion_constructor_args():
    sig = inspect.signature(InterruptibleActivityRegion.__init__)
    params = list(sig.parameters.keys())



def test_fundamentalactivities_activitynode_is_not_abstract():
    assert not inspect.isabstract(FundamentalActivities_ActivityNode)


def test_fundamentalactivities_activitynode_constructor_exists():
    assert callable(FundamentalActivities_ActivityNode.__init__)


def test_fundamentalactivities_activitynode_constructor_args():
    sig = inspect.signature(FundamentalActivities_ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_activities_basicactivities_objectnode_is_not_abstract():
    assert not inspect.isabstract(Activities_BasicActivities_ObjectNode)


def test_activities_basicactivities_objectnode_constructor_exists():
    assert callable(Activities_BasicActivities_ObjectNode.__init__)


def test_activities_basicactivities_objectnode_constructor_args():
    sig = inspect.signature(Activities_BasicActivities_ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_redefinableelement_is_not_abstract():
    assert not inspect.isabstract(RedefinableElement)


def test_redefinableelement_constructor_exists():
    assert callable(RedefinableElement.__init__)


def test_redefinableelement_constructor_args():
    sig = inspect.signature(RedefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_activities_basicactivities_activityedge_is_not_abstract():
    assert not inspect.isabstract(Activities_BasicActivities_ActivityEdge)


def test_activities_basicactivities_activityedge_constructor_exists():
    assert callable(Activities_BasicActivities_ActivityEdge.__init__)


def test_activities_basicactivities_activityedge_constructor_args():
    sig = inspect.signature(Activities_BasicActivities_ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_activities_basicactivities_redefinableelement_is_not_abstract():
    assert not inspect.isabstract(Activities_BasicActivities_RedefinableElement)


def test_activities_basicactivities_redefinableelement_constructor_exists():
    assert callable(Activities_BasicActivities_RedefinableElement.__init__)


def test_activities_basicactivities_redefinableelement_constructor_args():
    sig = inspect.signature(Activities_BasicActivities_RedefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_activities_fundamentalactivities_namespace_is_not_abstract():
    assert not inspect.isabstract(Activities_FundamentalActivities_Namespace)


def test_activities_fundamentalactivities_namespace_constructor_exists():
    assert callable(Activities_FundamentalActivities_Namespace.__init__)


def test_activities_fundamentalactivities_namespace_constructor_args():
    sig = inspect.signature(Activities_FundamentalActivities_Namespace.__init__)
    params = list(sig.parameters.keys())



def test_activity_is_not_abstract():
    assert not inspect.isabstract(Activity)


def test_activity_constructor_exists():
    assert callable(Activity.__init__)


def test_activity_constructor_args():
    sig = inspect.signature(Activity.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_activities_intermediateactivities_parameterset_is_not_abstract():
    assert not inspect.isabstract(Activities_IntermediateActivities_ParameterSet)


def test_activities_intermediateactivities_parameterset_constructor_exists():
    assert callable(Activities_IntermediateActivities_ParameterSet.__init__)


def test_activities_intermediateactivities_parameterset_constructor_args():
    sig = inspect.signature(Activities_IntermediateActivities_ParameterSet.__init__)
    params = list(sig.parameters.keys())



def test_activities_fundamentalactivities_activitygroup_is_not_abstract():
    assert not inspect.isabstract(Activities_FundamentalActivities_ActivityGroup)


def test_activities_fundamentalactivities_activitygroup_constructor_exists():
    assert callable(Activities_FundamentalActivities_ActivityGroup.__init__)


def test_activities_fundamentalactivities_activitygroup_constructor_args():
    sig = inspect.signature(Activities_FundamentalActivities_ActivityGroup.__init__)
    params = list(sig.parameters.keys())



def test_activitypartition_is_not_abstract():
    assert not inspect.isabstract(ActivityPartition)


def test_activitypartition_constructor_exists():
    assert callable(ActivityPartition.__init__)


def test_activitypartition_constructor_args():
    sig = inspect.signature(ActivityPartition.__init__)
    params = list(sig.parameters.keys())



def test_activityedge_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge)


def test_activityedge_constructor_exists():
    assert callable(ActivityEdge.__init__)


def test_activityedge_constructor_args():
    sig = inspect.signature(ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_activities_basicactivities_objectflow_is_not_abstract():
    assert not inspect.isabstract(Activities_BasicActivities_ObjectFlow)


def test_activities_basicactivities_objectflow_constructor_exists():
    assert callable(Activities_BasicActivities_ObjectFlow.__init__)


def test_activities_basicactivities_objectflow_constructor_args():
    sig = inspect.signature(Activities_BasicActivities_ObjectFlow.__init__)
    params = list(sig.parameters.keys())
    assert "isMultireceive" in params, "Missing parameter 'isMultireceive'"
    assert "isControlType" in params, "Missing parameter 'isControlType'"
    assert "isMulticast" in params, "Missing parameter 'isMulticast'"
    assert "ordering" in params, "Missing parameter 'ordering'"

def test_activities_basicactivities_objectflow_has_isMultireceive():
    assert hasattr(Activities_BasicActivities_ObjectFlow, "isMultireceive")
    descriptor = None
    for klass in Activities_BasicActivities_ObjectFlow.__mro__:
        if "isMultireceive" in klass.__dict__:
            descriptor = klass.__dict__["isMultireceive"]
            break
    assert isinstance(descriptor, property)

def test_activities_basicactivities_objectflow_has_isControlType():
    assert hasattr(Activities_BasicActivities_ObjectFlow, "isControlType")
    descriptor = None
    for klass in Activities_BasicActivities_ObjectFlow.__mro__:
        if "isControlType" in klass.__dict__:
            descriptor = klass.__dict__["isControlType"]
            break
    assert isinstance(descriptor, property)

def test_activities_basicactivities_objectflow_has_isMulticast():
    assert hasattr(Activities_BasicActivities_ObjectFlow, "isMulticast")
    descriptor = None
    for klass in Activities_BasicActivities_ObjectFlow.__mro__:
        if "isMulticast" in klass.__dict__:
            descriptor = klass.__dict__["isMulticast"]
            break
    assert isinstance(descriptor, property)

def test_activities_basicactivities_objectflow_has_ordering():
    assert hasattr(Activities_BasicActivities_ObjectFlow, "ordering")
    descriptor = None
    for klass in Activities_BasicActivities_ObjectFlow.__mro__:
        if "ordering" in klass.__dict__:
            descriptor = klass.__dict__["ordering"]
            break
    assert isinstance(descriptor, property)



def test_activities_basicactivities_controlflow_is_not_abstract():
    assert not inspect.isabstract(Activities_BasicActivities_ControlFlow)


def test_activities_basicactivities_controlflow_constructor_exists():
    assert callable(Activities_BasicActivities_ControlFlow.__init__)


def test_activities_basicactivities_controlflow_constructor_args():
    sig = inspect.signature(Activities_BasicActivities_ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_activitygroup_is_not_abstract():
    assert not inspect.isabstract(ActivityGroup)


def test_activitygroup_constructor_exists():
    assert callable(ActivityGroup.__init__)


def test_activitygroup_constructor_args():
    sig = inspect.signature(ActivityGroup.__init__)
    params = list(sig.parameters.keys())



def test_activities_intermediateactivities_interruptibleactivityregion_is_not_abstract():
    assert not inspect.isabstract(Activities_IntermediateActivities_InterruptibleActivityRegion)


def test_activities_intermediateactivities_interruptibleactivityregion_constructor_exists():
    assert callable(Activities_IntermediateActivities_InterruptibleActivityRegion.__init__)


def test_activities_intermediateactivities_interruptibleactivityregion_constructor_args():
    sig = inspect.signature(Activities_IntermediateActivities_InterruptibleActivityRegion.__init__)
    params = list(sig.parameters.keys())



def test_activities_intermediateactivities_activitypartition_is_not_abstract():
    assert not inspect.isabstract(Activities_IntermediateActivities_ActivityPartition)


def test_activities_intermediateactivities_activitypartition_constructor_exists():
    assert callable(Activities_IntermediateActivities_ActivityPartition.__init__)


def test_activities_intermediateactivities_activitypartition_constructor_args():
    sig = inspect.signature(Activities_IntermediateActivities_ActivityPartition.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_is_not_abstract():
    assert not inspect.isabstract(ActivityNode)


def test_activitynode_constructor_exists():
    assert callable(ActivityNode.__init__)


def test_activitynode_constructor_args():
    sig = inspect.signature(ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_activities_basicactivities_controlnode_is_not_abstract():
    assert not inspect.isabstract(Activities_BasicActivities_ControlNode)


def test_activities_basicactivities_controlnode_constructor_exists():
    assert callable(Activities_BasicActivities_ControlNode.__init__)


def test_activities_basicactivities_controlnode_constructor_args():
    sig = inspect.signature(Activities_BasicActivities_ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_activities_fundamentalactivities_action_is_not_abstract():
    assert not inspect.isabstract(Activities_FundamentalActivities_Action)


def test_activities_fundamentalactivities_action_constructor_exists():
    assert callable(Activities_FundamentalActivities_Action.__init__)


def test_activities_fundamentalactivities_action_constructor_args():
    sig = inspect.signature(Activities_FundamentalActivities_Action.__init__)
    params = list(sig.parameters.keys())
    assert "isLocallyReentrant" in params, "Missing parameter 'isLocallyReentrant'"

def test_activities_fundamentalactivities_action_has_isLocallyReentrant():
    assert hasattr(Activities_FundamentalActivities_Action, "isLocallyReentrant")
    descriptor = None
    for klass in Activities_FundamentalActivities_Action.__mro__:
        if "isLocallyReentrant" in klass.__dict__:
            descriptor = klass.__dict__["isLocallyReentrant"]
            break
    assert isinstance(descriptor, property)



def test_activities_structuredactivities_executablenode_is_not_abstract():
    assert not inspect.isabstract(Activities_StructuredActivities_ExecutableNode)


def test_activities_structuredactivities_executablenode_constructor_exists():
    assert callable(Activities_StructuredActivities_ExecutableNode.__init__)


def test_activities_structuredactivities_executablenode_constructor_args():
    sig = inspect.signature(Activities_StructuredActivities_ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
    params = list(sig.parameters.keys())



def test_activities_fundamentalactivities_activity_is_not_abstract():
    assert not inspect.isabstract(Activities_FundamentalActivities_Activity)


def test_activities_fundamentalactivities_activity_constructor_exists():
    assert callable(Activities_FundamentalActivities_Activity.__init__)


def test_activities_fundamentalactivities_activity_constructor_args():
    sig = inspect.signature(Activities_FundamentalActivities_Activity.__init__)
    params = list(sig.parameters.keys())
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"
    assert "isSingleExecution" in params, "Missing parameter 'isSingleExecution'"

def test_activities_fundamentalactivities_activity_has_isReadOnly():
    assert hasattr(Activities_FundamentalActivities_Activity, "isReadOnly")
    descriptor = None
    for klass in Activities_FundamentalActivities_Activity.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)

def test_activities_fundamentalactivities_activity_has_isSingleExecution():
    assert hasattr(Activities_FundamentalActivities_Activity, "isSingleExecution")
    descriptor = None
    for klass in Activities_FundamentalActivities_Activity.__mro__:
        if "isSingleExecution" in klass.__dict__:
            descriptor = klass.__dict__["isSingleExecution"]
            break
    assert isinstance(descriptor, property)



def test_basicactivities_redefinableelement_is_not_abstract():
    assert not inspect.isabstract(BasicActivities_RedefinableElement)


def test_basicactivities_redefinableelement_constructor_exists():
    assert callable(BasicActivities_RedefinableElement.__init__)


def test_basicactivities_redefinableelement_constructor_args():
    sig = inspect.signature(BasicActivities_RedefinableElement.__init__)
    params = list(sig.parameters.keys())



def test_fundamentalactivities_namedelement_is_not_abstract():
    assert not inspect.isabstract(FundamentalActivities_NamedElement)


def test_fundamentalactivities_namedelement_constructor_exists():
    assert callable(FundamentalActivities_NamedElement.__init__)


def test_fundamentalactivities_namedelement_constructor_args():
    sig = inspect.signature(FundamentalActivities_NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_activities_fundamentalactivities_activitynode_is_not_abstract():
    assert not inspect.isabstract(Activities_FundamentalActivities_ActivityNode)


def test_activities_fundamentalactivities_activitynode_constructor_exists():
    assert callable(Activities_FundamentalActivities_ActivityNode.__init__)


def test_activities_fundamentalactivities_activitynode_constructor_args():
    sig = inspect.signature(Activities_FundamentalActivities_ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_activities_fundamentalactivities_namedelement_is_not_abstract():
    assert not inspect.isabstract(Activities_FundamentalActivities_NamedElement)


def test_activities_fundamentalactivities_namedelement_constructor_exists():
    assert callable(Activities_FundamentalActivities_NamedElement.__init__)


def test_activities_fundamentalactivities_namedelement_constructor_args():
    sig = inspect.signature(Activities_FundamentalActivities_NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_parameterset_is_not_abstract():
    assert not inspect.isabstract(ParameterSet)


def test_parameterset_constructor_exists():
    assert callable(ParameterSet.__init__)


def test_parameterset_constructor_args():
    sig = inspect.signature(ParameterSet.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_activities_fundamentalactivities_behavior_is_not_abstract():
    assert not inspect.isabstract(Activities_FundamentalActivities_Behavior)


def test_activities_fundamentalactivities_behavior_constructor_exists():
    assert callable(Activities_FundamentalActivities_Behavior.__init__)


def test_activities_fundamentalactivities_behavior_constructor_args():
    sig = inspect.signature(Activities_FundamentalActivities_Behavior.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(StructuredActivityNode)


def test_structuredactivitynode_constructor_exists():
    assert callable(StructuredActivityNode.__init__)


def test_structuredactivitynode_constructor_args():
    sig = inspect.signature(StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_activities_extrastructuredactivities_expansionregion_is_not_abstract():
    assert not inspect.isabstract(Activities_ExtraStructuredActivities_ExpansionRegion)


def test_activities_extrastructuredactivities_expansionregion_constructor_exists():
    assert callable(Activities_ExtraStructuredActivities_ExpansionRegion.__init__)


def test_activities_extrastructuredactivities_expansionregion_constructor_args():
    sig = inspect.signature(Activities_ExtraStructuredActivities_ExpansionRegion.__init__)
    params = list(sig.parameters.keys())
    assert "mode" in params, "Missing parameter 'mode'"

def test_activities_extrastructuredactivities_expansionregion_has_mode():
    assert hasattr(Activities_ExtraStructuredActivities_ExpansionRegion, "mode")
    descriptor = None
    for klass in Activities_ExtraStructuredActivities_ExpansionRegion.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)



def test_activities_structuredactivities_sequencenode_is_not_abstract():
    assert not inspect.isabstract(Activities_StructuredActivities_SequenceNode)


def test_activities_structuredactivities_sequencenode_constructor_exists():
    assert callable(Activities_StructuredActivities_SequenceNode.__init__)


def test_activities_structuredactivities_sequencenode_constructor_args():
    sig = inspect.signature(Activities_StructuredActivities_SequenceNode.__init__)
    params = list(sig.parameters.keys())



def test_activities_structuredactivities_loopnode_is_not_abstract():
    assert not inspect.isabstract(Activities_StructuredActivities_LoopNode)


def test_activities_structuredactivities_loopnode_constructor_exists():
    assert callable(Activities_StructuredActivities_LoopNode.__init__)


def test_activities_structuredactivities_loopnode_constructor_args():
    sig = inspect.signature(Activities_StructuredActivities_LoopNode.__init__)
    params = list(sig.parameters.keys())
    assert "isTestedFirst" in params, "Missing parameter 'isTestedFirst'"

def test_activities_structuredactivities_loopnode_has_isTestedFirst():
    assert hasattr(Activities_StructuredActivities_LoopNode, "isTestedFirst")
    descriptor = None
    for klass in Activities_StructuredActivities_LoopNode.__mro__:
        if "isTestedFirst" in klass.__dict__:
            descriptor = klass.__dict__["isTestedFirst"]
            break
    assert isinstance(descriptor, property)



def test_activities_structuredactivities_conditionalnode_is_not_abstract():
    assert not inspect.isabstract(Activities_StructuredActivities_ConditionalNode)


def test_activities_structuredactivities_conditionalnode_constructor_exists():
    assert callable(Activities_StructuredActivities_ConditionalNode.__init__)


def test_activities_structuredactivities_conditionalnode_constructor_args():
    sig = inspect.signature(Activities_StructuredActivities_ConditionalNode.__init__)
    params = list(sig.parameters.keys())
    assert "isDeterminate" in params, "Missing parameter 'isDeterminate'"
    assert "isAssumed" in params, "Missing parameter 'isAssumed'"

def test_activities_structuredactivities_conditionalnode_has_isDeterminate():
    assert hasattr(Activities_StructuredActivities_ConditionalNode, "isDeterminate")
    descriptor = None
    for klass in Activities_StructuredActivities_ConditionalNode.__mro__:
        if "isDeterminate" in klass.__dict__:
            descriptor = klass.__dict__["isDeterminate"]
            break
    assert isinstance(descriptor, property)

def test_activities_structuredactivities_conditionalnode_has_isAssumed():
    assert hasattr(Activities_StructuredActivities_ConditionalNode, "isAssumed")
    descriptor = None
    for klass in Activities_StructuredActivities_ConditionalNode.__mro__:
        if "isAssumed" in klass.__dict__:
            descriptor = klass.__dict__["isAssumed"]
            break
    assert isinstance(descriptor, property)

def test_expansionkind_exists():
    # Check that the Enumeration exists
    assert ExpansionKind is not None

def test_expansionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExpansionKind]
    expected_literals = [
        "parallel",
        "stream",
        "iterative",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExpansionKind"

def test_parametereffectkind_exists():
    # Check that the Enumeration exists
    assert ParameterEffectKind is not None

def test_parametereffectkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ParameterEffectKind]
    expected_literals = [
        "read",
        "delete",
        "create",
        "update",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ParameterEffectKind"

def test_objectnodeorderingkind_exists():
    # Check that the Enumeration exists
    assert ObjectNodeOrderingKind is not None

def test_objectnodeorderingkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ObjectNodeOrderingKind]
    expected_literals = [
        "LIFO",
        "FIFO",
        "ordered",
        "unordered",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ObjectNodeOrderingKind"


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
ExpansionRegion_strategy = st.builds(
    ExpansionRegion,
)
ExpansionNode_strategy = st.builds(
    ExpansionNode,
)
Activities_ExtraStructuredActivities_Classifier_strategy = st.builds(
    Activities_ExtraStructuredActivities_Classifier,
)
Classifier_strategy = st.builds(
    Classifier,
)
Activities_CompleteStructuredActivities_InputPin_strategy = st.builds(
    Activities_CompleteStructuredActivities_InputPin,
)
ExecutableNode_strategy = st.builds(
    ExecutableNode,
)
Clause_strategy = st.builds(
    Clause,
)
Activities_StructuredActivities_MultiplicityElement_strategy = st.builds(
    Activities_StructuredActivities_MultiplicityElement,
)
Activities_StructuredActivities_OutputPin_strategy = st.builds(
    Activities_StructuredActivities_OutputPin,
)
StructuredActivities_MultiplicityElement_strategy = st.builds(
    StructuredActivities_MultiplicityElement,
)
ExceptionHandler_strategy = st.builds(
    ExceptionHandler,
)
IntermediateActivities_Feature_strategy = st.builds(
    IntermediateActivities_Feature,
)
FundamentalActivities_Namespace_strategy = st.builds(
    FundamentalActivities_Namespace,
)
Activities_IntermediateActivities_BehavioralFeature_strategy = st.builds(
    Activities_IntermediateActivities_BehavioralFeature,
)
CentralBufferNode_strategy = st.builds(
    CentralBufferNode,
)
Activities_IntermediateActivities_DataStoreNode_strategy = st.builds(
    Activities_IntermediateActivities_DataStoreNode,
)
Activities_IntermediateActivities_State_strategy = st.builds(
    Activities_IntermediateActivities_State,
)
Activities_IntermediateActivities_Constraint_strategy = st.builds(
    Activities_IntermediateActivities_Constraint,
)
Activities_IntermediateActivities_Element_strategy = st.builds(
    Activities_IntermediateActivities_Element,
)
FundamentalActivities_Action_strategy = st.builds(
    FundamentalActivities_Action,
)
FundamentalActivities_ActivityGroup_strategy = st.builds(
    FundamentalActivities_ActivityGroup,
)
StructuredActivities_ExecutableNode_strategy = st.builds(
    StructuredActivities_ExecutableNode,
)
Activities_StructuredActivities_StructuredActivityNode_strategy = st.builds(
    Activities_StructuredActivities_StructuredActivityNode,
    mustIsolate=
        st.booleans()
)
Activities_IntermediateActivities_Class_strategy = st.builds(
    Activities_IntermediateActivities_Class,
)
Activities_IntermediateActivities_Feature_strategy = st.builds(
    Activities_IntermediateActivities_Feature,
)
FinalNode_strategy = st.builds(
    FinalNode,
)
Activities_IntermediateActivities_FlowFinalNode_strategy = st.builds(
    Activities_IntermediateActivities_FlowFinalNode,
)
State_strategy = st.builds(
    State,
)
Element_strategy = st.builds(
    Element,
)
Activities_ExtraStructuredActivities_ExceptionHandler_strategy = st.builds(
    Activities_ExtraStructuredActivities_ExceptionHandler,
)
Activities_StructuredActivities_Clause_strategy = st.builds(
    Activities_StructuredActivities_Clause,
)
Activities_IntermediateActivities_ValueSpecification_strategy = st.builds(
    Activities_IntermediateActivities_ValueSpecification,
)
ObjectFlow_strategy = st.builds(
    ObjectFlow,
)
ControlNode_strategy = st.builds(
    ControlNode,
)
Activities_IntermediateActivities_ForkNode_strategy = st.builds(
    Activities_IntermediateActivities_ForkNode,
)
Activities_IntermediateActivities_JoinNode_strategy = st.builds(
    Activities_IntermediateActivities_JoinNode,
    isCombineDuplicate=
        st.booleans()
)
Activities_IntermediateActivities_FinalNode_strategy = st.builds(
    Activities_IntermediateActivities_FinalNode,
)
Activities_IntermediateActivities_DecisionNode_strategy = st.builds(
    Activities_IntermediateActivities_DecisionNode,
)
Activities_IntermediateActivities_MergeNode_strategy = st.builds(
    Activities_IntermediateActivities_MergeNode,
)
Activities_BasicActivities_InitialNode_strategy = st.builds(
    Activities_BasicActivities_InitialNode,
)
IntermediateActivities_FinalNode_strategy = st.builds(
    IntermediateActivities_FinalNode,
)
BasicActivities_ControlNode_strategy = st.builds(
    BasicActivities_ControlNode,
)
Activities_BasicActivities_ActivityFinalNode_strategy = st.builds(
    Activities_BasicActivities_ActivityFinalNode,
)
Activities_BasicActivities_Parameter_strategy = st.builds(
    Activities_BasicActivities_Parameter,
    effect=
        safe_text,
    isException=
        st.booleans(),
    isStream=
        st.booleans()
)
Parameter_strategy = st.builds(
    Parameter,
)
ObjectNode_strategy = st.builds(
    ObjectNode,
)
Activities_IntermediateActivities_CentralBufferNode_strategy = st.builds(
    Activities_IntermediateActivities_CentralBufferNode,
)
Activities_BasicActivities_ActivityParameterNode_strategy = st.builds(
    Activities_BasicActivities_ActivityParameterNode,
)
Activities_ExtraStructuredActivities_ExpansionNode_strategy = st.builds(
    Activities_ExtraStructuredActivities_ExpansionNode,
)
Activities_BasicActivities_Pin_strategy = st.builds(
    Activities_BasicActivities_Pin,
    isControl=
        st.booleans()
)
Activities_BasicActivities_TypedElement_strategy = st.builds(
    Activities_BasicActivities_TypedElement,
)
BasicActivities_TypedElement_strategy = st.builds(
    BasicActivities_TypedElement,
)
Activities_StructuredActivities_Variable_strategy = st.builds(
    Activities_StructuredActivities_Variable,
)
ValueSpecification_strategy = st.builds(
    ValueSpecification,
)
OutputPin_strategy = st.builds(
    OutputPin,
)
InputPin_strategy = st.builds(
    InputPin,
)
Constraint_strategy = st.builds(
    Constraint,
)
InterruptibleActivityRegion_strategy = st.builds(
    InterruptibleActivityRegion,
)
FundamentalActivities_ActivityNode_strategy = st.builds(
    FundamentalActivities_ActivityNode,
)
Activities_BasicActivities_ObjectNode_strategy = st.builds(
    Activities_BasicActivities_ObjectNode,
)
RedefinableElement_strategy = st.builds(
    RedefinableElement,
)
Activities_BasicActivities_ActivityEdge_strategy = st.builds(
    Activities_BasicActivities_ActivityEdge,
)
Activities_BasicActivities_RedefinableElement_strategy = st.builds(
    Activities_BasicActivities_RedefinableElement,
)
Activities_FundamentalActivities_Namespace_strategy = st.builds(
    Activities_FundamentalActivities_Namespace,
)
Activity_strategy = st.builds(
    Activity,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
Activities_IntermediateActivities_ParameterSet_strategy = st.builds(
    Activities_IntermediateActivities_ParameterSet,
)
Activities_FundamentalActivities_ActivityGroup_strategy = st.builds(
    Activities_FundamentalActivities_ActivityGroup,
)
ActivityPartition_strategy = st.builds(
    ActivityPartition,
)
ActivityEdge_strategy = st.builds(
    ActivityEdge,
)
Activities_BasicActivities_ObjectFlow_strategy = st.builds(
    Activities_BasicActivities_ObjectFlow,
    isMultireceive=
        st.booleans(),
    isControlType=
        st.booleans(),
    isMulticast=
        st.booleans(),
    ordering=
        safe_text
)
Activities_BasicActivities_ControlFlow_strategy = st.builds(
    Activities_BasicActivities_ControlFlow,
)
ActivityGroup_strategy = st.builds(
    ActivityGroup,
)
Activities_IntermediateActivities_InterruptibleActivityRegion_strategy = st.builds(
    Activities_IntermediateActivities_InterruptibleActivityRegion,
)
Activities_IntermediateActivities_ActivityPartition_strategy = st.builds(
    Activities_IntermediateActivities_ActivityPartition,
)
ActivityNode_strategy = st.builds(
    ActivityNode,
)
Activities_BasicActivities_ControlNode_strategy = st.builds(
    Activities_BasicActivities_ControlNode,
)
Activities_FundamentalActivities_Action_strategy = st.builds(
    Activities_FundamentalActivities_Action,
    isLocallyReentrant=
        st.booleans()
)
Activities_StructuredActivities_ExecutableNode_strategy = st.builds(
    Activities_StructuredActivities_ExecutableNode,
)
Behavior_strategy = st.builds(
    Behavior,
)
Activities_FundamentalActivities_Activity_strategy = st.builds(
    Activities_FundamentalActivities_Activity,
    isReadOnly=
        st.booleans(),
    isSingleExecution=
        st.booleans()
)
BasicActivities_RedefinableElement_strategy = st.builds(
    BasicActivities_RedefinableElement,
)
FundamentalActivities_NamedElement_strategy = st.builds(
    FundamentalActivities_NamedElement,
)
Activities_FundamentalActivities_ActivityNode_strategy = st.builds(
    Activities_FundamentalActivities_ActivityNode,
)
Activities_FundamentalActivities_NamedElement_strategy = st.builds(
    Activities_FundamentalActivities_NamedElement,
)
ParameterSet_strategy = st.builds(
    ParameterSet,
)
Class_strategy = st.builds(
    Class,
)
Activities_FundamentalActivities_Behavior_strategy = st.builds(
    Activities_FundamentalActivities_Behavior,
)
Variable_strategy = st.builds(
    Variable,
)
StructuredActivityNode_strategy = st.builds(
    StructuredActivityNode,
)
Activities_ExtraStructuredActivities_ExpansionRegion_strategy = st.builds(
    Activities_ExtraStructuredActivities_ExpansionRegion,
    mode=
        safe_text
)
Activities_StructuredActivities_SequenceNode_strategy = st.builds(
    Activities_StructuredActivities_SequenceNode,
)
Activities_StructuredActivities_LoopNode_strategy = st.builds(
    Activities_StructuredActivities_LoopNode,
    isTestedFirst=
        st.booleans()
)
Activities_StructuredActivities_ConditionalNode_strategy = st.builds(
    Activities_StructuredActivities_ConditionalNode,
    isDeterminate=
        st.booleans(),
    isAssumed=
        st.booleans()
)

@given(instance=ExpansionRegion_strategy)
@settings(max_examples=50)
def test_expansionregion_instantiation(instance):
    assert isinstance(instance, ExpansionRegion)

@given(instance=ExpansionNode_strategy)
@settings(max_examples=50)
def test_expansionnode_instantiation(instance):
    assert isinstance(instance, ExpansionNode)

@given(instance=Activities_ExtraStructuredActivities_Classifier_strategy)
@settings(max_examples=50)
def test_activities_extrastructuredactivities_classifier_instantiation(instance):
    assert isinstance(instance, Activities_ExtraStructuredActivities_Classifier)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=Activities_CompleteStructuredActivities_InputPin_strategy)
@settings(max_examples=50)
def test_activities_completestructuredactivities_inputpin_instantiation(instance):
    assert isinstance(instance, Activities_CompleteStructuredActivities_InputPin)

@given(instance=ExecutableNode_strategy)
@settings(max_examples=50)
def test_executablenode_instantiation(instance):
    assert isinstance(instance, ExecutableNode)

@given(instance=Clause_strategy)
@settings(max_examples=50)
def test_clause_instantiation(instance):
    assert isinstance(instance, Clause)

@given(instance=Activities_StructuredActivities_MultiplicityElement_strategy)
@settings(max_examples=50)
def test_activities_structuredactivities_multiplicityelement_instantiation(instance):
    assert isinstance(instance, Activities_StructuredActivities_MultiplicityElement)

@given(instance=Activities_StructuredActivities_OutputPin_strategy)
@settings(max_examples=50)
def test_activities_structuredactivities_outputpin_instantiation(instance):
    assert isinstance(instance, Activities_StructuredActivities_OutputPin)

@given(instance=StructuredActivities_MultiplicityElement_strategy)
@settings(max_examples=50)
def test_structuredactivities_multiplicityelement_instantiation(instance):
    assert isinstance(instance, StructuredActivities_MultiplicityElement)

@given(instance=ExceptionHandler_strategy)
@settings(max_examples=50)
def test_exceptionhandler_instantiation(instance):
    assert isinstance(instance, ExceptionHandler)

@given(instance=IntermediateActivities_Feature_strategy)
@settings(max_examples=50)
def test_intermediateactivities_feature_instantiation(instance):
    assert isinstance(instance, IntermediateActivities_Feature)

@given(instance=FundamentalActivities_Namespace_strategy)
@settings(max_examples=50)
def test_fundamentalactivities_namespace_instantiation(instance):
    assert isinstance(instance, FundamentalActivities_Namespace)

@given(instance=Activities_IntermediateActivities_BehavioralFeature_strategy)
@settings(max_examples=50)
def test_activities_intermediateactivities_behavioralfeature_instantiation(instance):
    assert isinstance(instance, Activities_IntermediateActivities_BehavioralFeature)

@given(instance=CentralBufferNode_strategy)
@settings(max_examples=50)
def test_centralbuffernode_instantiation(instance):
    assert isinstance(instance, CentralBufferNode)

@given(instance=Activities_IntermediateActivities_DataStoreNode_strategy)
@settings(max_examples=50)
def test_activities_intermediateactivities_datastorenode_instantiation(instance):
    assert isinstance(instance, Activities_IntermediateActivities_DataStoreNode)

@given(instance=Activities_IntermediateActivities_State_strategy)
@settings(max_examples=50)
def test_activities_intermediateactivities_state_instantiation(instance):
    assert isinstance(instance, Activities_IntermediateActivities_State)

@given(instance=Activities_IntermediateActivities_Constraint_strategy)
@settings(max_examples=50)
def test_activities_intermediateactivities_constraint_instantiation(instance):
    assert isinstance(instance, Activities_IntermediateActivities_Constraint)

@given(instance=Activities_IntermediateActivities_Element_strategy)
@settings(max_examples=50)
def test_activities_intermediateactivities_element_instantiation(instance):
    assert isinstance(instance, Activities_IntermediateActivities_Element)

@given(instance=FundamentalActivities_Action_strategy)
@settings(max_examples=50)
def test_fundamentalactivities_action_instantiation(instance):
    assert isinstance(instance, FundamentalActivities_Action)

@given(instance=FundamentalActivities_ActivityGroup_strategy)
@settings(max_examples=50)
def test_fundamentalactivities_activitygroup_instantiation(instance):
    assert isinstance(instance, FundamentalActivities_ActivityGroup)

@given(instance=StructuredActivities_ExecutableNode_strategy)
@settings(max_examples=50)
def test_structuredactivities_executablenode_instantiation(instance):
    assert isinstance(instance, StructuredActivities_ExecutableNode)

@given(instance=Activities_StructuredActivities_StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_activities_structuredactivities_structuredactivitynode_instantiation(instance):
    assert isinstance(instance, Activities_StructuredActivities_StructuredActivityNode)



@given(instance=Activities_StructuredActivities_StructuredActivityNode_strategy)
def test_activities_structuredactivities_structuredactivitynode_mustIsolate_setter(instance):
    original = instance.mustIsolate
    instance.mustIsolate = original
    assert instance.mustIsolate == original

@given(instance=Activities_IntermediateActivities_Class_strategy)
@settings(max_examples=50)
def test_activities_intermediateactivities_class_instantiation(instance):
    assert isinstance(instance, Activities_IntermediateActivities_Class)

@given(instance=Activities_IntermediateActivities_Feature_strategy)
@settings(max_examples=50)
def test_activities_intermediateactivities_feature_instantiation(instance):
    assert isinstance(instance, Activities_IntermediateActivities_Feature)

@given(instance=FinalNode_strategy)
@settings(max_examples=50)
def test_finalnode_instantiation(instance):
    assert isinstance(instance, FinalNode)

@given(instance=Activities_IntermediateActivities_FlowFinalNode_strategy)
@settings(max_examples=50)
def test_activities_intermediateactivities_flowfinalnode_instantiation(instance):
    assert isinstance(instance, Activities_IntermediateActivities_FlowFinalNode)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=Activities_ExtraStructuredActivities_ExceptionHandler_strategy)
@settings(max_examples=50)
def test_activities_extrastructuredactivities_exceptionhandler_instantiation(instance):
    assert isinstance(instance, Activities_ExtraStructuredActivities_ExceptionHandler)

@given(instance=Activities_StructuredActivities_Clause_strategy)
@settings(max_examples=50)
def test_activities_structuredactivities_clause_instantiation(instance):
    assert isinstance(instance, Activities_StructuredActivities_Clause)

@given(instance=Activities_IntermediateActivities_ValueSpecification_strategy)
@settings(max_examples=50)
def test_activities_intermediateactivities_valuespecification_instantiation(instance):
    assert isinstance(instance, Activities_IntermediateActivities_ValueSpecification)

@given(instance=ObjectFlow_strategy)
@settings(max_examples=50)
def test_objectflow_instantiation(instance):
    assert isinstance(instance, ObjectFlow)

@given(instance=ControlNode_strategy)
@settings(max_examples=50)
def test_controlnode_instantiation(instance):
    assert isinstance(instance, ControlNode)

@given(instance=Activities_IntermediateActivities_ForkNode_strategy)
@settings(max_examples=50)
def test_activities_intermediateactivities_forknode_instantiation(instance):
    assert isinstance(instance, Activities_IntermediateActivities_ForkNode)

@given(instance=Activities_IntermediateActivities_JoinNode_strategy)
@settings(max_examples=50)
def test_activities_intermediateactivities_joinnode_instantiation(instance):
    assert isinstance(instance, Activities_IntermediateActivities_JoinNode)



@given(instance=Activities_IntermediateActivities_JoinNode_strategy)
def test_activities_intermediateactivities_joinnode_isCombineDuplicate_setter(instance):
    original = instance.isCombineDuplicate
    instance.isCombineDuplicate = original
    assert instance.isCombineDuplicate == original

@given(instance=Activities_IntermediateActivities_FinalNode_strategy)
@settings(max_examples=50)
def test_activities_intermediateactivities_finalnode_instantiation(instance):
    assert isinstance(instance, Activities_IntermediateActivities_FinalNode)

@given(instance=Activities_IntermediateActivities_DecisionNode_strategy)
@settings(max_examples=50)
def test_activities_intermediateactivities_decisionnode_instantiation(instance):
    assert isinstance(instance, Activities_IntermediateActivities_DecisionNode)

@given(instance=Activities_IntermediateActivities_MergeNode_strategy)
@settings(max_examples=50)
def test_activities_intermediateactivities_mergenode_instantiation(instance):
    assert isinstance(instance, Activities_IntermediateActivities_MergeNode)

@given(instance=Activities_BasicActivities_InitialNode_strategy)
@settings(max_examples=50)
def test_activities_basicactivities_initialnode_instantiation(instance):
    assert isinstance(instance, Activities_BasicActivities_InitialNode)

@given(instance=IntermediateActivities_FinalNode_strategy)
@settings(max_examples=50)
def test_intermediateactivities_finalnode_instantiation(instance):
    assert isinstance(instance, IntermediateActivities_FinalNode)

@given(instance=BasicActivities_ControlNode_strategy)
@settings(max_examples=50)
def test_basicactivities_controlnode_instantiation(instance):
    assert isinstance(instance, BasicActivities_ControlNode)

@given(instance=Activities_BasicActivities_ActivityFinalNode_strategy)
@settings(max_examples=50)
def test_activities_basicactivities_activityfinalnode_instantiation(instance):
    assert isinstance(instance, Activities_BasicActivities_ActivityFinalNode)

@given(instance=Activities_BasicActivities_Parameter_strategy)
@settings(max_examples=50)
def test_activities_basicactivities_parameter_instantiation(instance):
    assert isinstance(instance, Activities_BasicActivities_Parameter)



@given(instance=Activities_BasicActivities_Parameter_strategy)
def test_activities_basicactivities_parameter_effect_setter(instance):
    original = instance.effect
    instance.effect = original
    assert instance.effect == original



@given(instance=Activities_BasicActivities_Parameter_strategy)
def test_activities_basicactivities_parameter_isException_setter(instance):
    original = instance.isException
    instance.isException = original
    assert instance.isException == original



@given(instance=Activities_BasicActivities_Parameter_strategy)
def test_activities_basicactivities_parameter_isStream_setter(instance):
    original = instance.isStream
    instance.isStream = original
    assert instance.isStream == original

@given(instance=Parameter_strategy)
@settings(max_examples=50)
def test_parameter_instantiation(instance):
    assert isinstance(instance, Parameter)

@given(instance=ObjectNode_strategy)
@settings(max_examples=50)
def test_objectnode_instantiation(instance):
    assert isinstance(instance, ObjectNode)

@given(instance=Activities_IntermediateActivities_CentralBufferNode_strategy)
@settings(max_examples=50)
def test_activities_intermediateactivities_centralbuffernode_instantiation(instance):
    assert isinstance(instance, Activities_IntermediateActivities_CentralBufferNode)

@given(instance=Activities_BasicActivities_ActivityParameterNode_strategy)
@settings(max_examples=50)
def test_activities_basicactivities_activityparameternode_instantiation(instance):
    assert isinstance(instance, Activities_BasicActivities_ActivityParameterNode)

@given(instance=Activities_ExtraStructuredActivities_ExpansionNode_strategy)
@settings(max_examples=50)
def test_activities_extrastructuredactivities_expansionnode_instantiation(instance):
    assert isinstance(instance, Activities_ExtraStructuredActivities_ExpansionNode)

@given(instance=Activities_BasicActivities_Pin_strategy)
@settings(max_examples=50)
def test_activities_basicactivities_pin_instantiation(instance):
    assert isinstance(instance, Activities_BasicActivities_Pin)



@given(instance=Activities_BasicActivities_Pin_strategy)
def test_activities_basicactivities_pin_isControl_setter(instance):
    original = instance.isControl
    instance.isControl = original
    assert instance.isControl == original

@given(instance=Activities_BasicActivities_TypedElement_strategy)
@settings(max_examples=50)
def test_activities_basicactivities_typedelement_instantiation(instance):
    assert isinstance(instance, Activities_BasicActivities_TypedElement)

@given(instance=BasicActivities_TypedElement_strategy)
@settings(max_examples=50)
def test_basicactivities_typedelement_instantiation(instance):
    assert isinstance(instance, BasicActivities_TypedElement)

@given(instance=Activities_StructuredActivities_Variable_strategy)
@settings(max_examples=50)
def test_activities_structuredactivities_variable_instantiation(instance):
    assert isinstance(instance, Activities_StructuredActivities_Variable)

@given(instance=ValueSpecification_strategy)
@settings(max_examples=50)
def test_valuespecification_instantiation(instance):
    assert isinstance(instance, ValueSpecification)

@given(instance=OutputPin_strategy)
@settings(max_examples=50)
def test_outputpin_instantiation(instance):
    assert isinstance(instance, OutputPin)

@given(instance=InputPin_strategy)
@settings(max_examples=50)
def test_inputpin_instantiation(instance):
    assert isinstance(instance, InputPin)

@given(instance=Constraint_strategy)
@settings(max_examples=50)
def test_constraint_instantiation(instance):
    assert isinstance(instance, Constraint)

@given(instance=InterruptibleActivityRegion_strategy)
@settings(max_examples=50)
def test_interruptibleactivityregion_instantiation(instance):
    assert isinstance(instance, InterruptibleActivityRegion)

@given(instance=FundamentalActivities_ActivityNode_strategy)
@settings(max_examples=50)
def test_fundamentalactivities_activitynode_instantiation(instance):
    assert isinstance(instance, FundamentalActivities_ActivityNode)

@given(instance=Activities_BasicActivities_ObjectNode_strategy)
@settings(max_examples=50)
def test_activities_basicactivities_objectnode_instantiation(instance):
    assert isinstance(instance, Activities_BasicActivities_ObjectNode)

@given(instance=RedefinableElement_strategy)
@settings(max_examples=50)
def test_redefinableelement_instantiation(instance):
    assert isinstance(instance, RedefinableElement)

@given(instance=Activities_BasicActivities_ActivityEdge_strategy)
@settings(max_examples=50)
def test_activities_basicactivities_activityedge_instantiation(instance):
    assert isinstance(instance, Activities_BasicActivities_ActivityEdge)

@given(instance=Activities_BasicActivities_RedefinableElement_strategy)
@settings(max_examples=50)
def test_activities_basicactivities_redefinableelement_instantiation(instance):
    assert isinstance(instance, Activities_BasicActivities_RedefinableElement)

@given(instance=Activities_FundamentalActivities_Namespace_strategy)
@settings(max_examples=50)
def test_activities_fundamentalactivities_namespace_instantiation(instance):
    assert isinstance(instance, Activities_FundamentalActivities_Namespace)

@given(instance=Activity_strategy)
@settings(max_examples=50)
def test_activity_instantiation(instance):
    assert isinstance(instance, Activity)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=Activities_IntermediateActivities_ParameterSet_strategy)
@settings(max_examples=50)
def test_activities_intermediateactivities_parameterset_instantiation(instance):
    assert isinstance(instance, Activities_IntermediateActivities_ParameterSet)

@given(instance=Activities_FundamentalActivities_ActivityGroup_strategy)
@settings(max_examples=50)
def test_activities_fundamentalactivities_activitygroup_instantiation(instance):
    assert isinstance(instance, Activities_FundamentalActivities_ActivityGroup)

@given(instance=ActivityPartition_strategy)
@settings(max_examples=50)
def test_activitypartition_instantiation(instance):
    assert isinstance(instance, ActivityPartition)

@given(instance=ActivityEdge_strategy)
@settings(max_examples=50)
def test_activityedge_instantiation(instance):
    assert isinstance(instance, ActivityEdge)

@given(instance=Activities_BasicActivities_ObjectFlow_strategy)
@settings(max_examples=50)
def test_activities_basicactivities_objectflow_instantiation(instance):
    assert isinstance(instance, Activities_BasicActivities_ObjectFlow)



@given(instance=Activities_BasicActivities_ObjectFlow_strategy)
def test_activities_basicactivities_objectflow_isMultireceive_setter(instance):
    original = instance.isMultireceive
    instance.isMultireceive = original
    assert instance.isMultireceive == original



@given(instance=Activities_BasicActivities_ObjectFlow_strategy)
def test_activities_basicactivities_objectflow_isControlType_setter(instance):
    original = instance.isControlType
    instance.isControlType = original
    assert instance.isControlType == original



@given(instance=Activities_BasicActivities_ObjectFlow_strategy)
def test_activities_basicactivities_objectflow_isMulticast_setter(instance):
    original = instance.isMulticast
    instance.isMulticast = original
    assert instance.isMulticast == original



@given(instance=Activities_BasicActivities_ObjectFlow_strategy)
def test_activities_basicactivities_objectflow_ordering_setter(instance):
    original = instance.ordering
    instance.ordering = original
    assert instance.ordering == original

@given(instance=Activities_BasicActivities_ControlFlow_strategy)
@settings(max_examples=50)
def test_activities_basicactivities_controlflow_instantiation(instance):
    assert isinstance(instance, Activities_BasicActivities_ControlFlow)

@given(instance=ActivityGroup_strategy)
@settings(max_examples=50)
def test_activitygroup_instantiation(instance):
    assert isinstance(instance, ActivityGroup)

@given(instance=Activities_IntermediateActivities_InterruptibleActivityRegion_strategy)
@settings(max_examples=50)
def test_activities_intermediateactivities_interruptibleactivityregion_instantiation(instance):
    assert isinstance(instance, Activities_IntermediateActivities_InterruptibleActivityRegion)

@given(instance=Activities_IntermediateActivities_ActivityPartition_strategy)
@settings(max_examples=50)
def test_activities_intermediateactivities_activitypartition_instantiation(instance):
    assert isinstance(instance, Activities_IntermediateActivities_ActivityPartition)

@given(instance=ActivityNode_strategy)
@settings(max_examples=50)
def test_activitynode_instantiation(instance):
    assert isinstance(instance, ActivityNode)

@given(instance=Activities_BasicActivities_ControlNode_strategy)
@settings(max_examples=50)
def test_activities_basicactivities_controlnode_instantiation(instance):
    assert isinstance(instance, Activities_BasicActivities_ControlNode)

@given(instance=Activities_FundamentalActivities_Action_strategy)
@settings(max_examples=50)
def test_activities_fundamentalactivities_action_instantiation(instance):
    assert isinstance(instance, Activities_FundamentalActivities_Action)



@given(instance=Activities_FundamentalActivities_Action_strategy)
def test_activities_fundamentalactivities_action_isLocallyReentrant_setter(instance):
    original = instance.isLocallyReentrant
    instance.isLocallyReentrant = original
    assert instance.isLocallyReentrant == original

@given(instance=Activities_StructuredActivities_ExecutableNode_strategy)
@settings(max_examples=50)
def test_activities_structuredactivities_executablenode_instantiation(instance):
    assert isinstance(instance, Activities_StructuredActivities_ExecutableNode)

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=Activities_FundamentalActivities_Activity_strategy)
@settings(max_examples=50)
def test_activities_fundamentalactivities_activity_instantiation(instance):
    assert isinstance(instance, Activities_FundamentalActivities_Activity)



@given(instance=Activities_FundamentalActivities_Activity_strategy)
def test_activities_fundamentalactivities_activity_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original



@given(instance=Activities_FundamentalActivities_Activity_strategy)
def test_activities_fundamentalactivities_activity_isSingleExecution_setter(instance):
    original = instance.isSingleExecution
    instance.isSingleExecution = original
    assert instance.isSingleExecution == original

@given(instance=BasicActivities_RedefinableElement_strategy)
@settings(max_examples=50)
def test_basicactivities_redefinableelement_instantiation(instance):
    assert isinstance(instance, BasicActivities_RedefinableElement)

@given(instance=FundamentalActivities_NamedElement_strategy)
@settings(max_examples=50)
def test_fundamentalactivities_namedelement_instantiation(instance):
    assert isinstance(instance, FundamentalActivities_NamedElement)

@given(instance=Activities_FundamentalActivities_ActivityNode_strategy)
@settings(max_examples=50)
def test_activities_fundamentalactivities_activitynode_instantiation(instance):
    assert isinstance(instance, Activities_FundamentalActivities_ActivityNode)

@given(instance=Activities_FundamentalActivities_NamedElement_strategy)
@settings(max_examples=50)
def test_activities_fundamentalactivities_namedelement_instantiation(instance):
    assert isinstance(instance, Activities_FundamentalActivities_NamedElement)

@given(instance=ParameterSet_strategy)
@settings(max_examples=50)
def test_parameterset_instantiation(instance):
    assert isinstance(instance, ParameterSet)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=Activities_FundamentalActivities_Behavior_strategy)
@settings(max_examples=50)
def test_activities_fundamentalactivities_behavior_instantiation(instance):
    assert isinstance(instance, Activities_FundamentalActivities_Behavior)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_structuredactivitynode_instantiation(instance):
    assert isinstance(instance, StructuredActivityNode)

@given(instance=Activities_ExtraStructuredActivities_ExpansionRegion_strategy)
@settings(max_examples=50)
def test_activities_extrastructuredactivities_expansionregion_instantiation(instance):
    assert isinstance(instance, Activities_ExtraStructuredActivities_ExpansionRegion)



@given(instance=Activities_ExtraStructuredActivities_ExpansionRegion_strategy)
def test_activities_extrastructuredactivities_expansionregion_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original

@given(instance=Activities_StructuredActivities_SequenceNode_strategy)
@settings(max_examples=50)
def test_activities_structuredactivities_sequencenode_instantiation(instance):
    assert isinstance(instance, Activities_StructuredActivities_SequenceNode)

@given(instance=Activities_StructuredActivities_LoopNode_strategy)
@settings(max_examples=50)
def test_activities_structuredactivities_loopnode_instantiation(instance):
    assert isinstance(instance, Activities_StructuredActivities_LoopNode)



@given(instance=Activities_StructuredActivities_LoopNode_strategy)
def test_activities_structuredactivities_loopnode_isTestedFirst_setter(instance):
    original = instance.isTestedFirst
    instance.isTestedFirst = original
    assert instance.isTestedFirst == original

@given(instance=Activities_StructuredActivities_ConditionalNode_strategy)
@settings(max_examples=50)
def test_activities_structuredactivities_conditionalnode_instantiation(instance):
    assert isinstance(instance, Activities_StructuredActivities_ConditionalNode)



@given(instance=Activities_StructuredActivities_ConditionalNode_strategy)
def test_activities_structuredactivities_conditionalnode_isDeterminate_setter(instance):
    original = instance.isDeterminate
    instance.isDeterminate = original
    assert instance.isDeterminate == original



@given(instance=Activities_StructuredActivities_ConditionalNode_strategy)
def test_activities_structuredactivities_conditionalnode_isAssumed_setter(instance):
    original = instance.isAssumed
    instance.isAssumed = original
    assert instance.isAssumed == original
