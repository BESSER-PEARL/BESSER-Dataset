import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    StructuredActivityNode,
    ActivitiesProv_ExpansionRegion,
    ActivitiesProv_SequenceNode,
    ActivitiesProv_LoopNode,
    ActivitiesProv_ExceptionHandler,
    ExecutableNode,
    ActivitiesProv_ParameterSet,
    CentralBufferNode,
    ActivitiesProv_DataStoreNode,
    ActivitiesProv_Clause,
    ActivitiesProv_ConditionalNode,
    ActivityEdge,
    ActivitiesProv_ObjectFlow,
    ActivitiesProv_ControlFlow,
    ActivityGroup,
    ActivitiesProv_InterruptibleActivityRegion,
    ActivitiesProv_StructuredActivityNode,
    ActivitiesProv_ActivityPartition,
    ActivitiesProv_ActivityEdge,
    FinalNode,
    ActivitiesProv_FlowFinalNode,
    ControlNode,
    ActivitiesProv_FinalNode,
    ActivitiesProv_MergeNode,
    ActivitiesProv_DecisionNode,
    ActivitiesProv_InitialNode,
    ActivitiesProv_JoinNode,
    ActivitiesProv_ForkNode,
    ActivitiesProv_ActivityFinalNode,
    ObjectNode,
    ActivitiesProv_CentralBufferNode,
    ActivitiesProv_ExpansionNode,
    ActivitiesProv_ActivityParameterNode,
    ActivityNode,
    ActivitiesProv_ControlNode,
    ActivitiesProv_ExecutableNode,
    ActivitiesProv_ObjectNode,
    ActivitiesProv_ActivityGroup,
    ActivitiesProv_ActivityNode,
    ActivitiesProv_Activity,
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



def test_activitiesprov_expansionregion_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv_ExpansionRegion)


def test_activitiesprov_expansionregion_constructor_exists():
    assert callable(ActivitiesProv_ExpansionRegion.__init__)


def test_activitiesprov_expansionregion_constructor_args():
    sig = inspect.signature(ActivitiesProv_ExpansionRegion.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov_sequencenode_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv_SequenceNode)


def test_activitiesprov_sequencenode_constructor_exists():
    assert callable(ActivitiesProv_SequenceNode.__init__)


def test_activitiesprov_sequencenode_constructor_args():
    sig = inspect.signature(ActivitiesProv_SequenceNode.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov_loopnode_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv_LoopNode)


def test_activitiesprov_loopnode_constructor_exists():
    assert callable(ActivitiesProv_LoopNode.__init__)


def test_activitiesprov_loopnode_constructor_args():
    sig = inspect.signature(ActivitiesProv_LoopNode.__init__)
    params = list(sig.parameters.keys())
    assert "isTestedFirst" in params, "Missing parameter 'isTestedFirst'"

def test_activitiesprov_loopnode_has_isTestedFirst():
    assert hasattr(ActivitiesProv_LoopNode, "isTestedFirst")
    descriptor = None
    for klass in ActivitiesProv_LoopNode.__mro__:
        if "isTestedFirst" in klass.__dict__:
            descriptor = klass.__dict__["isTestedFirst"]
            break
    assert isinstance(descriptor, property)



def test_activitiesprov_exceptionhandler_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv_ExceptionHandler)


def test_activitiesprov_exceptionhandler_constructor_exists():
    assert callable(ActivitiesProv_ExceptionHandler.__init__)


def test_activitiesprov_exceptionhandler_constructor_args():
    sig = inspect.signature(ActivitiesProv_ExceptionHandler.__init__)
    params = list(sig.parameters.keys())



def test_executablenode_is_not_abstract():
    assert not inspect.isabstract(ExecutableNode)


def test_executablenode_constructor_exists():
    assert callable(ExecutableNode.__init__)


def test_executablenode_constructor_args():
    sig = inspect.signature(ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov_parameterset_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv_ParameterSet)


def test_activitiesprov_parameterset_constructor_exists():
    assert callable(ActivitiesProv_ParameterSet.__init__)


def test_activitiesprov_parameterset_constructor_args():
    sig = inspect.signature(ActivitiesProv_ParameterSet.__init__)
    params = list(sig.parameters.keys())



def test_centralbuffernode_is_not_abstract():
    assert not inspect.isabstract(CentralBufferNode)


def test_centralbuffernode_constructor_exists():
    assert callable(CentralBufferNode.__init__)


def test_centralbuffernode_constructor_args():
    sig = inspect.signature(CentralBufferNode.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov_datastorenode_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv_DataStoreNode)


def test_activitiesprov_datastorenode_constructor_exists():
    assert callable(ActivitiesProv_DataStoreNode.__init__)


def test_activitiesprov_datastorenode_constructor_args():
    sig = inspect.signature(ActivitiesProv_DataStoreNode.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov_clause_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv_Clause)


def test_activitiesprov_clause_constructor_exists():
    assert callable(ActivitiesProv_Clause.__init__)


def test_activitiesprov_clause_constructor_args():
    sig = inspect.signature(ActivitiesProv_Clause.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov_conditionalnode_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv_ConditionalNode)


def test_activitiesprov_conditionalnode_constructor_exists():
    assert callable(ActivitiesProv_ConditionalNode.__init__)


def test_activitiesprov_conditionalnode_constructor_args():
    sig = inspect.signature(ActivitiesProv_ConditionalNode.__init__)
    params = list(sig.parameters.keys())
    assert "isDeterminate" in params, "Missing parameter 'isDeterminate'"
    assert "isAssumed" in params, "Missing parameter 'isAssumed'"

def test_activitiesprov_conditionalnode_has_isDeterminate():
    assert hasattr(ActivitiesProv_ConditionalNode, "isDeterminate")
    descriptor = None
    for klass in ActivitiesProv_ConditionalNode.__mro__:
        if "isDeterminate" in klass.__dict__:
            descriptor = klass.__dict__["isDeterminate"]
            break
    assert isinstance(descriptor, property)

def test_activitiesprov_conditionalnode_has_isAssumed():
    assert hasattr(ActivitiesProv_ConditionalNode, "isAssumed")
    descriptor = None
    for klass in ActivitiesProv_ConditionalNode.__mro__:
        if "isAssumed" in klass.__dict__:
            descriptor = klass.__dict__["isAssumed"]
            break
    assert isinstance(descriptor, property)



def test_activityedge_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge)


def test_activityedge_constructor_exists():
    assert callable(ActivityEdge.__init__)


def test_activityedge_constructor_args():
    sig = inspect.signature(ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov_objectflow_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv_ObjectFlow)


def test_activitiesprov_objectflow_constructor_exists():
    assert callable(ActivitiesProv_ObjectFlow.__init__)


def test_activitiesprov_objectflow_constructor_args():
    sig = inspect.signature(ActivitiesProv_ObjectFlow.__init__)
    params = list(sig.parameters.keys())
    assert "isControlType" in params, "Missing parameter 'isControlType'"
    assert "isMulticast" in params, "Missing parameter 'isMulticast'"
    assert "isMultireceive" in params, "Missing parameter 'isMultireceive'"

def test_activitiesprov_objectflow_has_isControlType():
    assert hasattr(ActivitiesProv_ObjectFlow, "isControlType")
    descriptor = None
    for klass in ActivitiesProv_ObjectFlow.__mro__:
        if "isControlType" in klass.__dict__:
            descriptor = klass.__dict__["isControlType"]
            break
    assert isinstance(descriptor, property)

def test_activitiesprov_objectflow_has_isMulticast():
    assert hasattr(ActivitiesProv_ObjectFlow, "isMulticast")
    descriptor = None
    for klass in ActivitiesProv_ObjectFlow.__mro__:
        if "isMulticast" in klass.__dict__:
            descriptor = klass.__dict__["isMulticast"]
            break
    assert isinstance(descriptor, property)

def test_activitiesprov_objectflow_has_isMultireceive():
    assert hasattr(ActivitiesProv_ObjectFlow, "isMultireceive")
    descriptor = None
    for klass in ActivitiesProv_ObjectFlow.__mro__:
        if "isMultireceive" in klass.__dict__:
            descriptor = klass.__dict__["isMultireceive"]
            break
    assert isinstance(descriptor, property)



def test_activitiesprov_controlflow_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv_ControlFlow)


def test_activitiesprov_controlflow_constructor_exists():
    assert callable(ActivitiesProv_ControlFlow.__init__)


def test_activitiesprov_controlflow_constructor_args():
    sig = inspect.signature(ActivitiesProv_ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_activitygroup_is_not_abstract():
    assert not inspect.isabstract(ActivityGroup)


def test_activitygroup_constructor_exists():
    assert callable(ActivityGroup.__init__)


def test_activitygroup_constructor_args():
    sig = inspect.signature(ActivityGroup.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov_interruptibleactivityregion_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv_InterruptibleActivityRegion)


def test_activitiesprov_interruptibleactivityregion_constructor_exists():
    assert callable(ActivitiesProv_InterruptibleActivityRegion.__init__)


def test_activitiesprov_interruptibleactivityregion_constructor_args():
    sig = inspect.signature(ActivitiesProv_InterruptibleActivityRegion.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov_structuredactivitynode_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv_StructuredActivityNode)


def test_activitiesprov_structuredactivitynode_constructor_exists():
    assert callable(ActivitiesProv_StructuredActivityNode.__init__)


def test_activitiesprov_structuredactivitynode_constructor_args():
    sig = inspect.signature(ActivitiesProv_StructuredActivityNode.__init__)
    params = list(sig.parameters.keys())
    assert "mustIsolate" in params, "Missing parameter 'mustIsolate'"

def test_activitiesprov_structuredactivitynode_has_mustIsolate():
    assert hasattr(ActivitiesProv_StructuredActivityNode, "mustIsolate")
    descriptor = None
    for klass in ActivitiesProv_StructuredActivityNode.__mro__:
        if "mustIsolate" in klass.__dict__:
            descriptor = klass.__dict__["mustIsolate"]
            break
    assert isinstance(descriptor, property)



def test_activitiesprov_activitypartition_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv_ActivityPartition)


def test_activitiesprov_activitypartition_constructor_exists():
    assert callable(ActivitiesProv_ActivityPartition.__init__)


def test_activitiesprov_activitypartition_constructor_args():
    sig = inspect.signature(ActivitiesProv_ActivityPartition.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov_activityedge_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv_ActivityEdge)


def test_activitiesprov_activityedge_constructor_exists():
    assert callable(ActivitiesProv_ActivityEdge.__init__)


def test_activitiesprov_activityedge_constructor_args():
    sig = inspect.signature(ActivitiesProv_ActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_finalnode_is_not_abstract():
    assert not inspect.isabstract(FinalNode)


def test_finalnode_constructor_exists():
    assert callable(FinalNode.__init__)


def test_finalnode_constructor_args():
    sig = inspect.signature(FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov_flowfinalnode_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv_FlowFinalNode)


def test_activitiesprov_flowfinalnode_constructor_exists():
    assert callable(ActivitiesProv_FlowFinalNode.__init__)


def test_activitiesprov_flowfinalnode_constructor_args():
    sig = inspect.signature(ActivitiesProv_FlowFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_controlnode_is_not_abstract():
    assert not inspect.isabstract(ControlNode)


def test_controlnode_constructor_exists():
    assert callable(ControlNode.__init__)


def test_controlnode_constructor_args():
    sig = inspect.signature(ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov_finalnode_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv_FinalNode)


def test_activitiesprov_finalnode_constructor_exists():
    assert callable(ActivitiesProv_FinalNode.__init__)


def test_activitiesprov_finalnode_constructor_args():
    sig = inspect.signature(ActivitiesProv_FinalNode.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov_mergenode_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv_MergeNode)


def test_activitiesprov_mergenode_constructor_exists():
    assert callable(ActivitiesProv_MergeNode.__init__)


def test_activitiesprov_mergenode_constructor_args():
    sig = inspect.signature(ActivitiesProv_MergeNode.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov_decisionnode_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv_DecisionNode)


def test_activitiesprov_decisionnode_constructor_exists():
    assert callable(ActivitiesProv_DecisionNode.__init__)


def test_activitiesprov_decisionnode_constructor_args():
    sig = inspect.signature(ActivitiesProv_DecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov_initialnode_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv_InitialNode)


def test_activitiesprov_initialnode_constructor_exists():
    assert callable(ActivitiesProv_InitialNode.__init__)


def test_activitiesprov_initialnode_constructor_args():
    sig = inspect.signature(ActivitiesProv_InitialNode.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov_joinnode_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv_JoinNode)


def test_activitiesprov_joinnode_constructor_exists():
    assert callable(ActivitiesProv_JoinNode.__init__)


def test_activitiesprov_joinnode_constructor_args():
    sig = inspect.signature(ActivitiesProv_JoinNode.__init__)
    params = list(sig.parameters.keys())
    assert "isCombineDuplicate" in params, "Missing parameter 'isCombineDuplicate'"

def test_activitiesprov_joinnode_has_isCombineDuplicate():
    assert hasattr(ActivitiesProv_JoinNode, "isCombineDuplicate")
    descriptor = None
    for klass in ActivitiesProv_JoinNode.__mro__:
        if "isCombineDuplicate" in klass.__dict__:
            descriptor = klass.__dict__["isCombineDuplicate"]
            break
    assert isinstance(descriptor, property)



def test_activitiesprov_forknode_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv_ForkNode)


def test_activitiesprov_forknode_constructor_exists():
    assert callable(ActivitiesProv_ForkNode.__init__)


def test_activitiesprov_forknode_constructor_args():
    sig = inspect.signature(ActivitiesProv_ForkNode.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov_activityfinalnode_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv_ActivityFinalNode)


def test_activitiesprov_activityfinalnode_constructor_exists():
    assert callable(ActivitiesProv_ActivityFinalNode.__init__)


def test_activitiesprov_activityfinalnode_constructor_args():
    sig = inspect.signature(ActivitiesProv_ActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_objectnode_is_not_abstract():
    assert not inspect.isabstract(ObjectNode)


def test_objectnode_constructor_exists():
    assert callable(ObjectNode.__init__)


def test_objectnode_constructor_args():
    sig = inspect.signature(ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov_centralbuffernode_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv_CentralBufferNode)


def test_activitiesprov_centralbuffernode_constructor_exists():
    assert callable(ActivitiesProv_CentralBufferNode.__init__)


def test_activitiesprov_centralbuffernode_constructor_args():
    sig = inspect.signature(ActivitiesProv_CentralBufferNode.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov_expansionnode_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv_ExpansionNode)


def test_activitiesprov_expansionnode_constructor_exists():
    assert callable(ActivitiesProv_ExpansionNode.__init__)


def test_activitiesprov_expansionnode_constructor_args():
    sig = inspect.signature(ActivitiesProv_ExpansionNode.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov_activityparameternode_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv_ActivityParameterNode)


def test_activitiesprov_activityparameternode_constructor_exists():
    assert callable(ActivitiesProv_ActivityParameterNode.__init__)


def test_activitiesprov_activityparameternode_constructor_args():
    sig = inspect.signature(ActivitiesProv_ActivityParameterNode.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_is_not_abstract():
    assert not inspect.isabstract(ActivityNode)


def test_activitynode_constructor_exists():
    assert callable(ActivityNode.__init__)


def test_activitynode_constructor_args():
    sig = inspect.signature(ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov_controlnode_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv_ControlNode)


def test_activitiesprov_controlnode_constructor_exists():
    assert callable(ActivitiesProv_ControlNode.__init__)


def test_activitiesprov_controlnode_constructor_args():
    sig = inspect.signature(ActivitiesProv_ControlNode.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov_executablenode_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv_ExecutableNode)


def test_activitiesprov_executablenode_constructor_exists():
    assert callable(ActivitiesProv_ExecutableNode.__init__)


def test_activitiesprov_executablenode_constructor_args():
    sig = inspect.signature(ActivitiesProv_ExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov_objectnode_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv_ObjectNode)


def test_activitiesprov_objectnode_constructor_exists():
    assert callable(ActivitiesProv_ObjectNode.__init__)


def test_activitiesprov_objectnode_constructor_args():
    sig = inspect.signature(ActivitiesProv_ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov_activitygroup_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv_ActivityGroup)


def test_activitiesprov_activitygroup_constructor_exists():
    assert callable(ActivitiesProv_ActivityGroup.__init__)


def test_activitiesprov_activitygroup_constructor_args():
    sig = inspect.signature(ActivitiesProv_ActivityGroup.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov_activitynode_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv_ActivityNode)


def test_activitiesprov_activitynode_constructor_exists():
    assert callable(ActivitiesProv_ActivityNode.__init__)


def test_activitiesprov_activitynode_constructor_args():
    sig = inspect.signature(ActivitiesProv_ActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_activitiesprov_activity_is_not_abstract():
    assert not inspect.isabstract(ActivitiesProv_Activity)


def test_activitiesprov_activity_constructor_exists():
    assert callable(ActivitiesProv_Activity.__init__)


def test_activitiesprov_activity_constructor_args():
    sig = inspect.signature(ActivitiesProv_Activity.__init__)
    params = list(sig.parameters.keys())
    assert "isReadOnly" in params, "Missing parameter 'isReadOnly'"
    assert "isSingleExecution" in params, "Missing parameter 'isSingleExecution'"

def test_activitiesprov_activity_has_isReadOnly():
    assert hasattr(ActivitiesProv_Activity, "isReadOnly")
    descriptor = None
    for klass in ActivitiesProv_Activity.__mro__:
        if "isReadOnly" in klass.__dict__:
            descriptor = klass.__dict__["isReadOnly"]
            break
    assert isinstance(descriptor, property)

def test_activitiesprov_activity_has_isSingleExecution():
    assert hasattr(ActivitiesProv_Activity, "isSingleExecution")
    descriptor = None
    for klass in ActivitiesProv_Activity.__mro__:
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
ActivitiesProv_ExpansionRegion_strategy = st.builds(
    ActivitiesProv_ExpansionRegion,
)
ActivitiesProv_SequenceNode_strategy = st.builds(
    ActivitiesProv_SequenceNode,
)
ActivitiesProv_LoopNode_strategy = st.builds(
    ActivitiesProv_LoopNode,
    isTestedFirst=
        st.booleans()
)
ActivitiesProv_ExceptionHandler_strategy = st.builds(
    ActivitiesProv_ExceptionHandler,
)
ExecutableNode_strategy = st.builds(
    ExecutableNode,
)
ActivitiesProv_ParameterSet_strategy = st.builds(
    ActivitiesProv_ParameterSet,
)
CentralBufferNode_strategy = st.builds(
    CentralBufferNode,
)
ActivitiesProv_DataStoreNode_strategy = st.builds(
    ActivitiesProv_DataStoreNode,
)
ActivitiesProv_Clause_strategy = st.builds(
    ActivitiesProv_Clause,
)
ActivitiesProv_ConditionalNode_strategy = st.builds(
    ActivitiesProv_ConditionalNode,
    isDeterminate=
        st.booleans(),
    isAssumed=
        st.booleans()
)
ActivityEdge_strategy = st.builds(
    ActivityEdge,
)
ActivitiesProv_ObjectFlow_strategy = st.builds(
    ActivitiesProv_ObjectFlow,
    isControlType=
        st.booleans(),
    isMulticast=
        st.booleans(),
    isMultireceive=
        st.booleans()
)
ActivitiesProv_ControlFlow_strategy = st.builds(
    ActivitiesProv_ControlFlow,
)
ActivityGroup_strategy = st.builds(
    ActivityGroup,
)
ActivitiesProv_InterruptibleActivityRegion_strategy = st.builds(
    ActivitiesProv_InterruptibleActivityRegion,
)
ActivitiesProv_StructuredActivityNode_strategy = st.builds(
    ActivitiesProv_StructuredActivityNode,
    mustIsolate=
        st.booleans()
)
ActivitiesProv_ActivityPartition_strategy = st.builds(
    ActivitiesProv_ActivityPartition,
)
ActivitiesProv_ActivityEdge_strategy = st.builds(
    ActivitiesProv_ActivityEdge,
)
FinalNode_strategy = st.builds(
    FinalNode,
)
ActivitiesProv_FlowFinalNode_strategy = st.builds(
    ActivitiesProv_FlowFinalNode,
)
ControlNode_strategy = st.builds(
    ControlNode,
)
ActivitiesProv_FinalNode_strategy = st.builds(
    ActivitiesProv_FinalNode,
)
ActivitiesProv_MergeNode_strategy = st.builds(
    ActivitiesProv_MergeNode,
)
ActivitiesProv_DecisionNode_strategy = st.builds(
    ActivitiesProv_DecisionNode,
)
ActivitiesProv_InitialNode_strategy = st.builds(
    ActivitiesProv_InitialNode,
)
ActivitiesProv_JoinNode_strategy = st.builds(
    ActivitiesProv_JoinNode,
    isCombineDuplicate=
        st.booleans()
)
ActivitiesProv_ForkNode_strategy = st.builds(
    ActivitiesProv_ForkNode,
)
ActivitiesProv_ActivityFinalNode_strategy = st.builds(
    ActivitiesProv_ActivityFinalNode,
)
ObjectNode_strategy = st.builds(
    ObjectNode,
)
ActivitiesProv_CentralBufferNode_strategy = st.builds(
    ActivitiesProv_CentralBufferNode,
)
ActivitiesProv_ExpansionNode_strategy = st.builds(
    ActivitiesProv_ExpansionNode,
)
ActivitiesProv_ActivityParameterNode_strategy = st.builds(
    ActivitiesProv_ActivityParameterNode,
)
ActivityNode_strategy = st.builds(
    ActivityNode,
)
ActivitiesProv_ControlNode_strategy = st.builds(
    ActivitiesProv_ControlNode,
)
ActivitiesProv_ExecutableNode_strategy = st.builds(
    ActivitiesProv_ExecutableNode,
)
ActivitiesProv_ObjectNode_strategy = st.builds(
    ActivitiesProv_ObjectNode,
)
ActivitiesProv_ActivityGroup_strategy = st.builds(
    ActivitiesProv_ActivityGroup,
)
ActivitiesProv_ActivityNode_strategy = st.builds(
    ActivitiesProv_ActivityNode,
)
ActivitiesProv_Activity_strategy = st.builds(
    ActivitiesProv_Activity,
    isReadOnly=
        st.booleans(),
    isSingleExecution=
        st.booleans()
)

@given(instance=StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_structuredactivitynode_instantiation(instance):
    assert isinstance(instance, StructuredActivityNode)

@given(instance=ActivitiesProv_ExpansionRegion_strategy)
@settings(max_examples=50)
def test_activitiesprov_expansionregion_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_ExpansionRegion)

@given(instance=ActivitiesProv_SequenceNode_strategy)
@settings(max_examples=50)
def test_activitiesprov_sequencenode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_SequenceNode)

@given(instance=ActivitiesProv_LoopNode_strategy)
@settings(max_examples=50)
def test_activitiesprov_loopnode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_LoopNode)



@given(instance=ActivitiesProv_LoopNode_strategy)
def test_activitiesprov_loopnode_isTestedFirst_setter(instance):
    original = instance.isTestedFirst
    instance.isTestedFirst = original
    assert instance.isTestedFirst == original

@given(instance=ActivitiesProv_ExceptionHandler_strategy)
@settings(max_examples=50)
def test_activitiesprov_exceptionhandler_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_ExceptionHandler)

@given(instance=ExecutableNode_strategy)
@settings(max_examples=50)
def test_executablenode_instantiation(instance):
    assert isinstance(instance, ExecutableNode)

@given(instance=ActivitiesProv_ParameterSet_strategy)
@settings(max_examples=50)
def test_activitiesprov_parameterset_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_ParameterSet)

@given(instance=CentralBufferNode_strategy)
@settings(max_examples=50)
def test_centralbuffernode_instantiation(instance):
    assert isinstance(instance, CentralBufferNode)

@given(instance=ActivitiesProv_DataStoreNode_strategy)
@settings(max_examples=50)
def test_activitiesprov_datastorenode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_DataStoreNode)

@given(instance=ActivitiesProv_Clause_strategy)
@settings(max_examples=50)
def test_activitiesprov_clause_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_Clause)

@given(instance=ActivitiesProv_ConditionalNode_strategy)
@settings(max_examples=50)
def test_activitiesprov_conditionalnode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_ConditionalNode)



@given(instance=ActivitiesProv_ConditionalNode_strategy)
def test_activitiesprov_conditionalnode_isDeterminate_setter(instance):
    original = instance.isDeterminate
    instance.isDeterminate = original
    assert instance.isDeterminate == original



@given(instance=ActivitiesProv_ConditionalNode_strategy)
def test_activitiesprov_conditionalnode_isAssumed_setter(instance):
    original = instance.isAssumed
    instance.isAssumed = original
    assert instance.isAssumed == original

@given(instance=ActivityEdge_strategy)
@settings(max_examples=50)
def test_activityedge_instantiation(instance):
    assert isinstance(instance, ActivityEdge)

@given(instance=ActivitiesProv_ObjectFlow_strategy)
@settings(max_examples=50)
def test_activitiesprov_objectflow_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_ObjectFlow)



@given(instance=ActivitiesProv_ObjectFlow_strategy)
def test_activitiesprov_objectflow_isControlType_setter(instance):
    original = instance.isControlType
    instance.isControlType = original
    assert instance.isControlType == original



@given(instance=ActivitiesProv_ObjectFlow_strategy)
def test_activitiesprov_objectflow_isMulticast_setter(instance):
    original = instance.isMulticast
    instance.isMulticast = original
    assert instance.isMulticast == original



@given(instance=ActivitiesProv_ObjectFlow_strategy)
def test_activitiesprov_objectflow_isMultireceive_setter(instance):
    original = instance.isMultireceive
    instance.isMultireceive = original
    assert instance.isMultireceive == original

@given(instance=ActivitiesProv_ControlFlow_strategy)
@settings(max_examples=50)
def test_activitiesprov_controlflow_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_ControlFlow)

@given(instance=ActivityGroup_strategy)
@settings(max_examples=50)
def test_activitygroup_instantiation(instance):
    assert isinstance(instance, ActivityGroup)

@given(instance=ActivitiesProv_InterruptibleActivityRegion_strategy)
@settings(max_examples=50)
def test_activitiesprov_interruptibleactivityregion_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_InterruptibleActivityRegion)

@given(instance=ActivitiesProv_StructuredActivityNode_strategy)
@settings(max_examples=50)
def test_activitiesprov_structuredactivitynode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_StructuredActivityNode)



@given(instance=ActivitiesProv_StructuredActivityNode_strategy)
def test_activitiesprov_structuredactivitynode_mustIsolate_setter(instance):
    original = instance.mustIsolate
    instance.mustIsolate = original
    assert instance.mustIsolate == original

@given(instance=ActivitiesProv_ActivityPartition_strategy)
@settings(max_examples=50)
def test_activitiesprov_activitypartition_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_ActivityPartition)

@given(instance=ActivitiesProv_ActivityEdge_strategy)
@settings(max_examples=50)
def test_activitiesprov_activityedge_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_ActivityEdge)

@given(instance=FinalNode_strategy)
@settings(max_examples=50)
def test_finalnode_instantiation(instance):
    assert isinstance(instance, FinalNode)

@given(instance=ActivitiesProv_FlowFinalNode_strategy)
@settings(max_examples=50)
def test_activitiesprov_flowfinalnode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_FlowFinalNode)

@given(instance=ControlNode_strategy)
@settings(max_examples=50)
def test_controlnode_instantiation(instance):
    assert isinstance(instance, ControlNode)

@given(instance=ActivitiesProv_FinalNode_strategy)
@settings(max_examples=50)
def test_activitiesprov_finalnode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_FinalNode)

@given(instance=ActivitiesProv_MergeNode_strategy)
@settings(max_examples=50)
def test_activitiesprov_mergenode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_MergeNode)

@given(instance=ActivitiesProv_DecisionNode_strategy)
@settings(max_examples=50)
def test_activitiesprov_decisionnode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_DecisionNode)

@given(instance=ActivitiesProv_InitialNode_strategy)
@settings(max_examples=50)
def test_activitiesprov_initialnode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_InitialNode)

@given(instance=ActivitiesProv_JoinNode_strategy)
@settings(max_examples=50)
def test_activitiesprov_joinnode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_JoinNode)



@given(instance=ActivitiesProv_JoinNode_strategy)
def test_activitiesprov_joinnode_isCombineDuplicate_setter(instance):
    original = instance.isCombineDuplicate
    instance.isCombineDuplicate = original
    assert instance.isCombineDuplicate == original

@given(instance=ActivitiesProv_ForkNode_strategy)
@settings(max_examples=50)
def test_activitiesprov_forknode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_ForkNode)

@given(instance=ActivitiesProv_ActivityFinalNode_strategy)
@settings(max_examples=50)
def test_activitiesprov_activityfinalnode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_ActivityFinalNode)

@given(instance=ObjectNode_strategy)
@settings(max_examples=50)
def test_objectnode_instantiation(instance):
    assert isinstance(instance, ObjectNode)

@given(instance=ActivitiesProv_CentralBufferNode_strategy)
@settings(max_examples=50)
def test_activitiesprov_centralbuffernode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_CentralBufferNode)

@given(instance=ActivitiesProv_ExpansionNode_strategy)
@settings(max_examples=50)
def test_activitiesprov_expansionnode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_ExpansionNode)

@given(instance=ActivitiesProv_ActivityParameterNode_strategy)
@settings(max_examples=50)
def test_activitiesprov_activityparameternode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_ActivityParameterNode)

@given(instance=ActivityNode_strategy)
@settings(max_examples=50)
def test_activitynode_instantiation(instance):
    assert isinstance(instance, ActivityNode)

@given(instance=ActivitiesProv_ControlNode_strategy)
@settings(max_examples=50)
def test_activitiesprov_controlnode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_ControlNode)

@given(instance=ActivitiesProv_ExecutableNode_strategy)
@settings(max_examples=50)
def test_activitiesprov_executablenode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_ExecutableNode)

@given(instance=ActivitiesProv_ObjectNode_strategy)
@settings(max_examples=50)
def test_activitiesprov_objectnode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_ObjectNode)

@given(instance=ActivitiesProv_ActivityGroup_strategy)
@settings(max_examples=50)
def test_activitiesprov_activitygroup_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_ActivityGroup)

@given(instance=ActivitiesProv_ActivityNode_strategy)
@settings(max_examples=50)
def test_activitiesprov_activitynode_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_ActivityNode)

@given(instance=ActivitiesProv_Activity_strategy)
@settings(max_examples=50)
def test_activitiesprov_activity_instantiation(instance):
    assert isinstance(instance, ActivitiesProv_Activity)



@given(instance=ActivitiesProv_Activity_strategy)
def test_activitiesprov_activity_isReadOnly_setter(instance):
    original = instance.isReadOnly
    instance.isReadOnly = original
    assert instance.isReadOnly == original



@given(instance=ActivitiesProv_Activity_strategy)
def test_activitiesprov_activity_isSingleExecution_setter(instance):
    original = instance.isSingleExecution
    instance.isSingleExecution = original
    assert instance.isSingleExecution == original
