import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    StructuredActivityNode,
    ActivitiesProv::ExpansionRegion,
    ActivitiesProv::SequenceNode,
    ActivitiesProv::LoopNode,
    ActivitiesProv::ExceptionHandler,
    ExecutableNode,
    ActivitiesProv::ParameterSet,
    CentralBufferNode,
    ActivitiesProv::DataStoreNode,
    ActivitiesProv::Clause,
    ActivitiesProv::ConditionalNode,
    ActivityEdge,
    ActivitiesProv::ObjectFlow,
    ActivitiesProv::ControlFlow,
    ActivityGroup,
    ActivitiesProv::InterruptibleActivityRegion,
    ActivitiesProv::StructuredActivityNode,
    ActivitiesProv::ActivityPartition,
    ActivitiesProv::ActivityEdge,
    FinalNode,
    ActivitiesProv::FlowFinalNode,
    ControlNode,
    ActivitiesProv::FinalNode,
    ActivitiesProv::MergeNode,
    ActivitiesProv::DecisionNode,
    ActivitiesProv::ForkNode,
    ActivitiesProv::InitialNode,
    ActivitiesProv::JoinNode,
    ActivitiesProv::ActivityFinalNode,
    ObjectNode,
    ActivitiesProv::ExpansionNode,
    ActivitiesProv::CentralBufferNode,
    ActivitiesProv::ActivityParameterNode,
    ActivityNode,
    ActivitiesProv::ControlNode,
    ActivitiesProv::ExecutableNode,
    ActivitiesProv::ObjectNode,
    ActivitiesProv::ActivityGroup,
    ActivitiesProv::ActivityNode,
    ActivitiesProv::Activity,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(StructuredActivityNode)


def test_structuredactivitynode_constructor_exists():
    assert callable(StructuredActivityNode.__init__)


def test_structuredactivitynode_constructor_args():
    sig = inspect.signature(StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov::expansionregion_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv::ExpansionRegion)


def test_activitiesprov::expansionregion_constructor_exists():
    assert callable(ActivitiesProv::ExpansionRegion.__init__)


def test_activitiesprov::expansionregion_constructor_args():
    sig = inspect.signature(ActivitiesProv::ExpansionRegion.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov::sequencenode_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv::SequenceNode)


def test_activitiesprov::sequencenode_constructor_exists():
    assert callable(ActivitiesProv::SequenceNode.__init__)


def test_activitiesprov::sequencenode_constructor_args():
    sig = inspect.signature(ActivitiesProv::SequenceNode.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov::loopnode_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv::LoopNode)


def test_activitiesprov::loopnode_constructor_exists():
    assert callable(ActivitiesProv::LoopNode.__init__)


def test_activitiesprov::loopnode_constructor_args():
    sig = inspect.signature(ActivitiesProv::LoopNode.__init__)
    params = list(sig.parameters.keys())
    assert "isTestedFirst" in params, "Missing parameter 'isTestedFirst'"

def test_activitiesprov::loopnode_has_isTestedFirst():
    assert hasattr(ActivitiesProv::LoopNode, "isTestedFirst")
    descriptor = None
    for klass in ActivitiesProv::LoopNode.__mro__:
        if "isTestedFirst" in klass.__dict__:
            descriptor = klass.__dict__["isTestedFirst"]
            break
    assert isinstance(descriptor, property)



def test_activitiesprov::exceptionhandler_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv::ExceptionHandler)


def test_activitiesprov::exceptionhandler_constructor_exists():
    assert callable(ActivitiesProv::ExceptionHandler.__init__)


def test_activitiesprov::exceptionhandler_constructor_args():
    sig = inspect.signature(ActivitiesProv::ExceptionHandler.__init__)
    params = list(sig.parameters.keys())



def test_executablenode_is_not_abstract():
    assert not inspect.isabstract(ExecutableNode)


def test_executablenode_constructor_exists():
    assert callable(ExecutableNode.__init__)


def test_executablenode_constructor_args():
    sig = inspect.signature(ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov::parameterset_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv::ParameterSet)


def test_activitiesprov::parameterset_constructor_exists():
    assert callable(ActivitiesProv::ParameterSet.__init__)


def test_activitiesprov::parameterset_constructor_args():
    sig = inspect.signature(ActivitiesProv::ParameterSet.__init__)
    params = list(sig.parameters.keys())



def test_centralbuffernode_is_not_abstract():
    assert not inspect.isabstract(CentralBufferNode)


def test_centralbuffernode_constructor_exists():
    assert callable(CentralBufferNode.__init__)


def test_centralbuffernode_constructor_args():
    sig = inspect.signature(CentralBufferNode.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov::datastorenode_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv::DataStoreNode)


def test_activitiesprov::datastorenode_constructor_exists():
    assert callable(ActivitiesProv::DataStoreNode.__init__)


def test_activitiesprov::datastorenode_constructor_args():
    sig = inspect.signature(ActivitiesProv::DataStoreNode.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov::clause_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv::Clause)


def test_activitiesprov::clause_constructor_exists():
    assert callable(ActivitiesProv::Clause.__init__)


def test_activitiesprov::clause_constructor_args():
    sig = inspect.signature(ActivitiesProv::Clause.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov::conditionalnode_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv::ConditionalNode)


def test_activitiesprov::conditionalnode_constructor_exists():
    assert callable(ActivitiesProv::ConditionalNode.__init__)


def test_activitiesprov::conditionalnode_constructor_args():
    sig = inspect.signature(ActivitiesProv::ConditionalNode.__init__)
    params = list(sig.parameters.keys())
    assert "isAssumed" in params, "Missing parameter 'isAssumed'"
    assert "isDeterminate" in params, "Missing parameter 'isDeterminate'"

def test_activitiesprov::conditionalnode_has_isAssumed():
    assert hasattr(ActivitiesProv::ConditionalNode, "isAssumed")
    descriptor = None
    for klass in ActivitiesProv::ConditionalNode.__mro__:
        if "isAssumed" in klass.__dict__:
            descriptor = klass.__dict__["isAssumed"]
            break
    assert isinstance(descriptor, property)

def test_activitiesprov::conditionalnode_has_isDeterminate():
    assert hasattr(ActivitiesProv::ConditionalNode, "isDeterminate")
    descriptor = None
    for klass in ActivitiesProv::ConditionalNode.__mro__:
        if "isDeterminate" in klass.__dict__:
            descriptor = klass.__dict__["isDeterminate"]
            break
    assert isinstance(descriptor, property)



def test_activityedge_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge)


def test_activityedge_constructor_exists():
    assert callable(ActivityEdge.__init__)


def test_activityedge_constructor_args():
    sig = inspect.signature(ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov::objectflow_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv::ObjectFlow)


def test_activitiesprov::objectflow_constructor_exists():
    assert callable(ActivitiesProv::ObjectFlow.__init__)


def test_activitiesprov::objectflow_constructor_args():
    sig = inspect.signature(ActivitiesProv::ObjectFlow.__init__)
    params = list(sig.parameters.keys())
    assert "isMulticast" in params, "Missing parameter 'isMulticast'"
    assert "isControlType" in params, "Missing parameter 'isControlType'"
    assert "isMultireceive" in params, "Missing parameter 'isMultireceive'"

def test_activitiesprov::objectflow_has_isMulticast():
    assert hasattr(ActivitiesProv::ObjectFlow, "isMulticast")
    descriptor = None
    for klass in ActivitiesProv::ObjectFlow.__mro__:
        if "isMulticast" in klass.__dict__:
            descriptor = klass.__dict__["isMulticast"]
            break
    assert isinstance(descriptor, property)

def test_activitiesprov::objectflow_has_isControlType():
    assert hasattr(ActivitiesProv::ObjectFlow, "isControlType")
    descriptor = None
    for klass in ActivitiesProv::ObjectFlow.__mro__:
        if "isControlType" in klass.__dict__:
            descriptor = klass.__dict__["isControlType"]
            break
    assert isinstance(descriptor, property)

def test_activitiesprov::objectflow_has_isMultireceive():
    assert hasattr(ActivitiesProv::ObjectFlow, "isMultireceive")
    descriptor = None
    for klass in ActivitiesProv::ObjectFlow.__mro__:
        if "isMultireceive" in klass.__dict__:
            descriptor = klass.__dict__["isMultireceive"]
            break
    assert isinstance(descriptor, property)



def test_activitiesprov::controlflow_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv::ControlFlow)


def test_activitiesprov::controlflow_constructor_exists():
    assert callable(ActivitiesProv::ControlFlow.__init__)


def test_activitiesprov::controlflow_constructor_args():
    sig = inspect.signature(ActivitiesProv::ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_activitygroup_is_not_abstract():
    assert not inspect.isabstract(ActivityGroup)


def test_activitygroup_constructor_exists():
    assert callable(ActivityGroup.__init__)


def test_activitygroup_constructor_args():
    sig = inspect.signature(ActivityGroup.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov::interruptibleactivityregion_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv::InterruptibleActivityRegion)


def test_activitiesprov::interruptibleactivityregion_constructor_exists():
    assert callable(ActivitiesProv::InterruptibleActivityRegion.__init__)


def test_activitiesprov::interruptibleactivityregion_constructor_args():
    sig = inspect.signature(ActivitiesProv::InterruptibleActivityRegion.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov::structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv::StructuredActivityNode)


def test_activitiesprov::structuredactivitynode_constructor_exists():
    assert callable(ActivitiesProv::StructuredActivityNode.__init__)


def test_activitiesprov::structuredactivitynode_constructor_args():
    sig = inspect.signature(ActivitiesProv::StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())
    assert "mustIsolate" in params, "Missing parameter 'mustIsolate'"

def test_activitiesprov::structuredactivitynode_has_mustIsolate():
    assert hasattr(ActivitiesProv::StructuredActivityNode, "mustIsolate")
    descriptor = None
    for klass in ActivitiesProv::StructuredActivityNode.__mro__:
        if "mustIsolate" in klass.__dict__:
            descriptor = klass.__dict__["mustIsolate"]
            break
    assert isinstance(descriptor, property)



def test_activitiesprov::activitypartition_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv::ActivityPartition)


def test_activitiesprov::activitypartition_constructor_exists():
    assert callable(ActivitiesProv::ActivityPartition.__init__)


def test_activitiesprov::activitypartition_constructor_args():
    sig = inspect.signature(ActivitiesProv::ActivityPartition.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov::activityedge_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv::ActivityEdge)


def test_activitiesprov::activityedge_constructor_exists():
    assert callable(ActivitiesProv::ActivityEdge.__init__)


def test_activitiesprov::activityedge_constructor_args():
    sig = inspect.signature(ActivitiesProv::ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_finalnode_is_not_abstract():
    assert not inspect.isabstract(FinalNode)


def test_finalnode_constructor_exists():
    assert callable(FinalNode.__init__)


def test_finalnode_constructor_args():
    sig = inspect.signature(FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov::flowfinalnode_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv::FlowFinalNode)


def test_activitiesprov::flowfinalnode_constructor_exists():
    assert callable(ActivitiesProv::FlowFinalNode.__init__)


def test_activitiesprov::flowfinalnode_constructor_args():
    sig = inspect.signature(ActivitiesProv::FlowFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_controlnode_is_not_abstract():
    assert not inspect.isabstract(ControlNode)


def test_controlnode_constructor_exists():
    assert callable(ControlNode.__init__)


def test_controlnode_constructor_args():
    sig = inspect.signature(ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov::finalnode_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv::FinalNode)


def test_activitiesprov::finalnode_constructor_exists():
    assert callable(ActivitiesProv::FinalNode.__init__)


def test_activitiesprov::finalnode_constructor_args():
    sig = inspect.signature(ActivitiesProv::FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov::mergenode_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv::MergeNode)


def test_activitiesprov::mergenode_constructor_exists():
    assert callable(ActivitiesProv::MergeNode.__init__)


def test_activitiesprov::mergenode_constructor_args():
    sig = inspect.signature(ActivitiesProv::MergeNode.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov::decisionnode_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv::DecisionNode)


def test_activitiesprov::decisionnode_constructor_exists():
    assert callable(ActivitiesProv::DecisionNode.__init__)


def test_activitiesprov::decisionnode_constructor_args():
    sig = inspect.signature(ActivitiesProv::DecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov::forknode_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv::ForkNode)


def test_activitiesprov::forknode_constructor_exists():
    assert callable(ActivitiesProv::ForkNode.__init__)


def test_activitiesprov::forknode_constructor_args():
    sig = inspect.signature(ActivitiesProv::ForkNode.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov::initialnode_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv::InitialNode)


def test_activitiesprov::initialnode_constructor_exists():
    assert callable(ActivitiesProv::InitialNode.__init__)


def test_activitiesprov::initialnode_constructor_args():
    sig = inspect.signature(ActivitiesProv::InitialNode.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov::joinnode_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv::JoinNode)


def test_activitiesprov::joinnode_constructor_exists():
    assert callable(ActivitiesProv::JoinNode.__init__)


def test_activitiesprov::joinnode_constructor_args():
    sig = inspect.signature(ActivitiesProv::JoinNode.__init__)
    params = list(sig.parameters.keys())
    assert "isCombineDuplicate" in params, "Missing parameter 'isCombineDuplicate'"

def test_activitiesprov::joinnode_has_isCombineDuplicate():
    assert hasattr(ActivitiesProv::JoinNode, "isCombineDuplicate")
    descriptor = None
    for klass in ActivitiesProv::JoinNode.__mro__:
        if "isCombineDuplicate" in klass.__dict__:
            descriptor = klass.__dict__["isCombineDuplicate"]
            break
    assert isinstance(descriptor, property)



def test_activitiesprov::activityfinalnode_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv::ActivityFinalNode)


def test_activitiesprov::activityfinalnode_constructor_exists():
    assert callable(ActivitiesProv::ActivityFinalNode.__init__)


def test_activitiesprov::activityfinalnode_constructor_args():
    sig = inspect.signature(ActivitiesProv::ActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_objectnode_is_not_abstract():
    assert not inspect.isabstract(ObjectNode)


def test_objectnode_constructor_exists():
    assert callable(ObjectNode.__init__)


def test_objectnode_constructor_args():
    sig = inspect.signature(ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov::expansionnode_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv::ExpansionNode)


def test_activitiesprov::expansionnode_constructor_exists():
    assert callable(ActivitiesProv::ExpansionNode.__init__)


def test_activitiesprov::expansionnode_constructor_args():
    sig = inspect.signature(ActivitiesProv::ExpansionNode.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov::centralbuffernode_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv::CentralBufferNode)


def test_activitiesprov::centralbuffernode_constructor_exists():
    assert callable(ActivitiesProv::CentralBufferNode.__init__)


def test_activitiesprov::centralbuffernode_constructor_args():
    sig = inspect.signature(ActivitiesProv::CentralBufferNode.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov::activityparameternode_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv::ActivityParameterNode)


def test_activitiesprov::activityparameternode_constructor_exists():
    assert callable(ActivitiesProv::ActivityParameterNode.__init__)


def test_activitiesprov::activityparameternode_constructor_args():
    sig = inspect.signature(ActivitiesProv::ActivityParameterNode.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_is_not_abstract():
    assert not inspect.isabstract(ActivityNode)


def test_activitynode_constructor_exists():
    assert callable(ActivityNode.__init__)


def test_activitynode_constructor_args():
    sig = inspect.signature(ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov::controlnode_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv::ControlNode)


def test_activitiesprov::controlnode_constructor_exists():
    assert callable(ActivitiesProv::ControlNode.__init__)


def test_activitiesprov::controlnode_constructor_args():
    sig = inspect.signature(ActivitiesProv::ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov::executablenode_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv::ExecutableNode)


def test_activitiesprov::executablenode_constructor_exists():
    assert callable(ActivitiesProv::ExecutableNode.__init__)


def test_activitiesprov::executablenode_constructor_args():
    sig = inspect.signature(ActivitiesProv::ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov::objectnode_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv::ObjectNode)


def test_activitiesprov::objectnode_constructor_exists():
    assert callable(ActivitiesProv::ObjectNode.__init__)


def test_activitiesprov::objectnode_constructor_args():
    sig = inspect.signature(ActivitiesProv::ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov::activitygroup_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv::ActivityGroup)


def test_activitiesprov::activitygroup_constructor_exists():
    assert callable(ActivitiesProv::ActivityGroup.__init__)


def test_activitiesprov::activitygroup_constructor_args():
    sig = inspect.signature(ActivitiesProv::ActivityGroup.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov::activitynode_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv::ActivityNode)


def test_activitiesprov::activitynode_constructor_exists():
    assert callable(ActivitiesProv::ActivityNode.__init__)


def test_activitiesprov::activitynode_constructor_args():
    sig = inspect.signature(ActivitiesProv::ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov::activity_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv::Activity)


def test_activitiesprov::activity_constructor_exists():
    assert callable(ActivitiesProv::Activity.__init__)


def test_activitiesprov::activity_constructor_args():
    sig = inspect.signature(ActivitiesProv::Activity.__init__)
    params = list(sig.parameters.keys())
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"
    assert "isSingleExecution" in params, "Missing parameter 'isSingleExecution'"

def test_activitiesprov::activity_has_isReadOnly():
    assert hasattr(ActivitiesProv::Activity, "isReadOnly")
    descriptor = None
    for klass in ActivitiesProv::Activity.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)

def test_activitiesprov::activity_has_isSingleExecution():
    assert hasattr(ActivitiesProv::Activity, "isSingleExecution")
    descriptor = None
    for klass in ActivitiesProv::Activity.__mro__:
        if "isSingleExecution" in klass.__dict__:
            descriptor = klass.__dict__["isSingleExecution"]
            break
    assert isinstance(descriptor, property)


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
StructuredActivityNode_strategy = st.builds(
    StructuredActivityNode,
)
ActivitiesProv::ExpansionRegion_strategy = st.builds(
    ActivitiesProv::ExpansionRegion,
)
ActivitiesProv::SequenceNode_strategy = st.builds(
    ActivitiesProv::SequenceNode,
)
ActivitiesProv::LoopNode_strategy = st.builds(
    ActivitiesProv::LoopNode,
    isTestedFirst=
        st.booleans()
)
ActivitiesProv::ExceptionHandler_strategy = st.builds(
    ActivitiesProv::ExceptionHandler,
)
ExecutableNode_strategy = st.builds(
    ExecutableNode,
)
ActivitiesProv::ParameterSet_strategy = st.builds(
    ActivitiesProv::ParameterSet,
)
CentralBufferNode_strategy = st.builds(
    CentralBufferNode,
)
ActivitiesProv::DataStoreNode_strategy = st.builds(
    ActivitiesProv::DataStoreNode,
)
ActivitiesProv::Clause_strategy = st.builds(
    ActivitiesProv::Clause,
)
ActivitiesProv::ConditionalNode_strategy = st.builds(
    ActivitiesProv::ConditionalNode,
    isAssumed=
        st.booleans(),
    isDeterminate=
        st.booleans()
)
ActivityEdge_strategy = st.builds(
    ActivityEdge,
)
ActivitiesProv::ObjectFlow_strategy = st.builds(
    ActivitiesProv::ObjectFlow,
    isMulticast=
        st.booleans(),
    isControlType=
        st.booleans(),
    isMultireceive=
        st.booleans()
)
ActivitiesProv::ControlFlow_strategy = st.builds(
    ActivitiesProv::ControlFlow,
)
ActivityGroup_strategy = st.builds(
    ActivityGroup,
)
ActivitiesProv::InterruptibleActivityRegion_strategy = st.builds(
    ActivitiesProv::InterruptibleActivityRegion,
)
ActivitiesProv::StructuredActivityNode_strategy = st.builds(
    ActivitiesProv::StructuredActivityNode,
    mustIsolate=
        st.booleans()
)
ActivitiesProv::ActivityPartition_strategy = st.builds(
    ActivitiesProv::ActivityPartition,
)
ActivitiesProv::ActivityEdge_strategy = st.builds(
    ActivitiesProv::ActivityEdge,
)
FinalNode_strategy = st.builds(
    FinalNode,
)
ActivitiesProv::FlowFinalNode_strategy = st.builds(
    ActivitiesProv::FlowFinalNode,
)
ControlNode_strategy = st.builds(
    ControlNode,
)
ActivitiesProv::FinalNode_strategy = st.builds(
    ActivitiesProv::FinalNode,
)
ActivitiesProv::MergeNode_strategy = st.builds(
    ActivitiesProv::MergeNode,
)
ActivitiesProv::DecisionNode_strategy = st.builds(
    ActivitiesProv::DecisionNode,
)
ActivitiesProv::ForkNode_strategy = st.builds(
    ActivitiesProv::ForkNode,
)
ActivitiesProv::InitialNode_strategy = st.builds(
    ActivitiesProv::InitialNode,
)
ActivitiesProv::JoinNode_strategy = st.builds(
    ActivitiesProv::JoinNode,
    isCombineDuplicate=
        st.booleans()
)
ActivitiesProv::ActivityFinalNode_strategy = st.builds(
    ActivitiesProv::ActivityFinalNode,
)
ObjectNode_strategy = st.builds(
    ObjectNode,
)
ActivitiesProv::ExpansionNode_strategy = st.builds(
    ActivitiesProv::ExpansionNode,
)
ActivitiesProv::CentralBufferNode_strategy = st.builds(
    ActivitiesProv::CentralBufferNode,
)
ActivitiesProv::ActivityParameterNode_strategy = st.builds(
    ActivitiesProv::ActivityParameterNode,
)
ActivityNode_strategy = st.builds(
    ActivityNode,
)
ActivitiesProv::ControlNode_strategy = st.builds(
    ActivitiesProv::ControlNode,
)
ActivitiesProv::ExecutableNode_strategy = st.builds(
    ActivitiesProv::ExecutableNode,
)
ActivitiesProv::ObjectNode_strategy = st.builds(
    ActivitiesProv::ObjectNode,
)
ActivitiesProv::ActivityGroup_strategy = st.builds(
    ActivitiesProv::ActivityGroup,
)
ActivitiesProv::ActivityNode_strategy = st.builds(
    ActivitiesProv::ActivityNode,
)
ActivitiesProv::Activity_strategy = st.builds(
    ActivitiesProv::Activity,
    isReadOnly=
        st.booleans(),
    isSingleExecution=
        st.booleans()
)

@given(instance=StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_structuredactivitynode_instantiation(instance):
    assert isinstance(instance, StructuredActivityNode)

@given(instance=ActivitiesProv::ExpansionRegion_strategy)
@settings(max_examples=50)
def test_activitiesprov::expansionregion_instantiation(instance):
    assert isinstance(instance, ActivitiesProv::ExpansionRegion)

@given(instance=ActivitiesProv::SequenceNode_strategy)
@settings(max_examples=50)
def test_activitiesprov::sequencenode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv::SequenceNode)

@given(instance=ActivitiesProv::LoopNode_strategy)
@settings(max_examples=50)
def test_activitiesprov::loopnode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv::LoopNode)

@given(instance=ActivitiesProv::LoopNode_strategy)
def test_activitiesprov::loopnode_isTestedFirst_type(instance):
    assert isinstance(instance.isTestedFirst, bool)


@given(instance=ActivitiesProv::LoopNode_strategy)
def test_activitiesprov::loopnode_isTestedFirst_setter(instance):
    original = instance.isTestedFirst
    instance.isTestedFirst = original
    assert instance.isTestedFirst == original

@given(instance=ActivitiesProv::ExceptionHandler_strategy)
@settings(max_examples=50)
def test_activitiesprov::exceptionhandler_instantiation(instance):
    assert isinstance(instance, ActivitiesProv::ExceptionHandler)

@given(instance=ExecutableNode_strategy)
@settings(max_examples=50)
def test_executablenode_instantiation(instance):
    assert isinstance(instance, ExecutableNode)

@given(instance=ActivitiesProv::ParameterSet_strategy)
@settings(max_examples=50)
def test_activitiesprov::parameterset_instantiation(instance):
    assert isinstance(instance, ActivitiesProv::ParameterSet)

@given(instance=CentralBufferNode_strategy)
@settings(max_examples=50)
def test_centralbuffernode_instantiation(instance):
    assert isinstance(instance, CentralBufferNode)

@given(instance=ActivitiesProv::DataStoreNode_strategy)
@settings(max_examples=50)
def test_activitiesprov::datastorenode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv::DataStoreNode)

@given(instance=ActivitiesProv::Clause_strategy)
@settings(max_examples=50)
def test_activitiesprov::clause_instantiation(instance):
    assert isinstance(instance, ActivitiesProv::Clause)

@given(instance=ActivitiesProv::ConditionalNode_strategy)
@settings(max_examples=50)
def test_activitiesprov::conditionalnode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv::ConditionalNode)

@given(instance=ActivitiesProv::ConditionalNode_strategy)
def test_activitiesprov::conditionalnode_isAssumed_type(instance):
    assert isinstance(instance.isAssumed, bool)


@given(instance=ActivitiesProv::ConditionalNode_strategy)
def test_activitiesprov::conditionalnode_isAssumed_setter(instance):
    original = instance.isAssumed
    instance.isAssumed = original
    assert instance.isAssumed == original

@given(instance=ActivitiesProv::ConditionalNode_strategy)
def test_activitiesprov::conditionalnode_isDeterminate_type(instance):
    assert isinstance(instance.isDeterminate, bool)


@given(instance=ActivitiesProv::ConditionalNode_strategy)
def test_activitiesprov::conditionalnode_isDeterminate_setter(instance):
    original = instance.isDeterminate
    instance.isDeterminate = original
    assert instance.isDeterminate == original

@given(instance=ActivityEdge_strategy)
@settings(max_examples=50)
def test_activityedge_instantiation(instance):
    assert isinstance(instance, ActivityEdge)

@given(instance=ActivitiesProv::ObjectFlow_strategy)
@settings(max_examples=50)
def test_activitiesprov::objectflow_instantiation(instance):
    assert isinstance(instance, ActivitiesProv::ObjectFlow)

@given(instance=ActivitiesProv::ObjectFlow_strategy)
def test_activitiesprov::objectflow_isMulticast_type(instance):
    assert isinstance(instance.isMulticast, bool)


@given(instance=ActivitiesProv::ObjectFlow_strategy)
def test_activitiesprov::objectflow_isMulticast_setter(instance):
    original = instance.isMulticast
    instance.isMulticast = original
    assert instance.isMulticast == original

@given(instance=ActivitiesProv::ObjectFlow_strategy)
def test_activitiesprov::objectflow_isControlType_type(instance):
    assert isinstance(instance.isControlType, bool)


@given(instance=ActivitiesProv::ObjectFlow_strategy)
def test_activitiesprov::objectflow_isControlType_setter(instance):
    original = instance.isControlType
    instance.isControlType = original
    assert instance.isControlType == original

@given(instance=ActivitiesProv::ObjectFlow_strategy)
def test_activitiesprov::objectflow_isMultireceive_type(instance):
    assert isinstance(instance.isMultireceive, bool)


@given(instance=ActivitiesProv::ObjectFlow_strategy)
def test_activitiesprov::objectflow_isMultireceive_setter(instance):
    original = instance.isMultireceive
    instance.isMultireceive = original
    assert instance.isMultireceive == original

@given(instance=ActivitiesProv::ControlFlow_strategy)
@settings(max_examples=50)
def test_activitiesprov::controlflow_instantiation(instance):
    assert isinstance(instance, ActivitiesProv::ControlFlow)

@given(instance=ActivityGroup_strategy)
@settings(max_examples=50)
def test_activitygroup_instantiation(instance):
    assert isinstance(instance, ActivityGroup)

@given(instance=ActivitiesProv::InterruptibleActivityRegion_strategy)
@settings(max_examples=50)
def test_activitiesprov::interruptibleactivityregion_instantiation(instance):
    assert isinstance(instance, ActivitiesProv::InterruptibleActivityRegion)

@given(instance=ActivitiesProv::StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_activitiesprov::structuredactivitynode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv::StructuredActivityNode)

@given(instance=ActivitiesProv::StructuredActivityNode_strategy)
def test_activitiesprov::structuredactivitynode_mustIsolate_type(instance):
    assert isinstance(instance.mustIsolate, bool)


@given(instance=ActivitiesProv::StructuredActivityNode_strategy)
def test_activitiesprov::structuredactivitynode_mustIsolate_setter(instance):
    original = instance.mustIsolate
    instance.mustIsolate = original
    assert instance.mustIsolate == original

@given(instance=ActivitiesProv::ActivityPartition_strategy)
@settings(max_examples=50)
def test_activitiesprov::activitypartition_instantiation(instance):
    assert isinstance(instance, ActivitiesProv::ActivityPartition)

@given(instance=ActivitiesProv::ActivityEdge_strategy)
@settings(max_examples=50)
def test_activitiesprov::activityedge_instantiation(instance):
    assert isinstance(instance, ActivitiesProv::ActivityEdge)

@given(instance=FinalNode_strategy)
@settings(max_examples=50)
def test_finalnode_instantiation(instance):
    assert isinstance(instance, FinalNode)

@given(instance=ActivitiesProv::FlowFinalNode_strategy)
@settings(max_examples=50)
def test_activitiesprov::flowfinalnode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv::FlowFinalNode)

@given(instance=ControlNode_strategy)
@settings(max_examples=50)
def test_controlnode_instantiation(instance):
    assert isinstance(instance, ControlNode)

@given(instance=ActivitiesProv::FinalNode_strategy)
@settings(max_examples=50)
def test_activitiesprov::finalnode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv::FinalNode)

@given(instance=ActivitiesProv::MergeNode_strategy)
@settings(max_examples=50)
def test_activitiesprov::mergenode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv::MergeNode)

@given(instance=ActivitiesProv::DecisionNode_strategy)
@settings(max_examples=50)
def test_activitiesprov::decisionnode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv::DecisionNode)

@given(instance=ActivitiesProv::ForkNode_strategy)
@settings(max_examples=50)
def test_activitiesprov::forknode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv::ForkNode)

@given(instance=ActivitiesProv::InitialNode_strategy)
@settings(max_examples=50)
def test_activitiesprov::initialnode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv::InitialNode)

@given(instance=ActivitiesProv::JoinNode_strategy)
@settings(max_examples=50)
def test_activitiesprov::joinnode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv::JoinNode)

@given(instance=ActivitiesProv::JoinNode_strategy)
def test_activitiesprov::joinnode_isCombineDuplicate_type(instance):
    assert isinstance(instance.isCombineDuplicate, bool)


@given(instance=ActivitiesProv::JoinNode_strategy)
def test_activitiesprov::joinnode_isCombineDuplicate_setter(instance):
    original = instance.isCombineDuplicate
    instance.isCombineDuplicate = original
    assert instance.isCombineDuplicate == original

@given(instance=ActivitiesProv::ActivityFinalNode_strategy)
@settings(max_examples=50)
def test_activitiesprov::activityfinalnode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv::ActivityFinalNode)

@given(instance=ObjectNode_strategy)
@settings(max_examples=50)
def test_objectnode_instantiation(instance):
    assert isinstance(instance, ObjectNode)

@given(instance=ActivitiesProv::ExpansionNode_strategy)
@settings(max_examples=50)
def test_activitiesprov::expansionnode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv::ExpansionNode)

@given(instance=ActivitiesProv::CentralBufferNode_strategy)
@settings(max_examples=50)
def test_activitiesprov::centralbuffernode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv::CentralBufferNode)

@given(instance=ActivitiesProv::ActivityParameterNode_strategy)
@settings(max_examples=50)
def test_activitiesprov::activityparameternode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv::ActivityParameterNode)

@given(instance=ActivityNode_strategy)
@settings(max_examples=50)
def test_activitynode_instantiation(instance):
    assert isinstance(instance, ActivityNode)

@given(instance=ActivitiesProv::ControlNode_strategy)
@settings(max_examples=50)
def test_activitiesprov::controlnode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv::ControlNode)

@given(instance=ActivitiesProv::ExecutableNode_strategy)
@settings(max_examples=50)
def test_activitiesprov::executablenode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv::ExecutableNode)

@given(instance=ActivitiesProv::ObjectNode_strategy)
@settings(max_examples=50)
def test_activitiesprov::objectnode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv::ObjectNode)

@given(instance=ActivitiesProv::ActivityGroup_strategy)
@settings(max_examples=50)
def test_activitiesprov::activitygroup_instantiation(instance):
    assert isinstance(instance, ActivitiesProv::ActivityGroup)

@given(instance=ActivitiesProv::ActivityNode_strategy)
@settings(max_examples=50)
def test_activitiesprov::activitynode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv::ActivityNode)

@given(instance=ActivitiesProv::Activity_strategy)
@settings(max_examples=50)
def test_activitiesprov::activity_instantiation(instance):
    assert isinstance(instance, ActivitiesProv::Activity)

@given(instance=ActivitiesProv::Activity_strategy)
def test_activitiesprov::activity_isReadOnly_type(instance):
    assert isinstance(instance.isReadOnly, bool)


@given(instance=ActivitiesProv::Activity_strategy)
def test_activitiesprov::activity_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original

@given(instance=ActivitiesProv::Activity_strategy)
def test_activitiesprov::activity_isSingleExecution_type(instance):
    assert isinstance(instance.isSingleExecution, bool)


@given(instance=ActivitiesProv::Activity_strategy)
def test_activitiesprov::activity_isSingleExecution_setter(instance):
    original = instance.isSingleExecution
    instance.isSingleExecution = original
    assert instance.isSingleExecution == original
