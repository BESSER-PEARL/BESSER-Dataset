import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    sexec_StateCase,
    Trace,
    sexec_TraceStateEntered,
    sexec_ReactionFired,
    sexec_TraceStateExited,
    sexec_TraceBeginRunCycle,
    sexec_TraceReactionWillFire,
    sexec_TraceEndRunCycle,
    sexec_TraceNodeExecuted,
    Check,
    sexec_CheckRef,
    sexec_Expression,
    Step,
    sexec_UnscheduleTimeEvent,
    sexec_HistoryEntry,
    sexec_StateSwitch,
    sexec_ExitState,
    sexec_Call,
    sexec_Execution,
    sexec_ScheduleTimeEvent,
    sexec_EnterState,
    sexec_SaveHistory,
    sexec_Trace,
    sexec_Check,
    Event,
    sexec_TimeEvent,
    ExecutionNode,
    sexec_ExecutionExit,
    sexec_ExecutionEntry,
    sexec_ExecutionChoice,
    sexec_ExecutionSynchronization,
    ExecutionScope,
    ScopedElement,
    sexec_ExecutionFlow,
    NamedElement,
    MappedElement,
    sexec_ExecutionScope,
    sexec_Step,
    sexec_StateVector,
    sexec_ExecutionRegion,
    sexec_ExecutionNode,
    sexec_ExecutionState,
    sexec_EObject,
    sexec_MappedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sexec_statecase_is_not_abstract():
    assert not inspect.isabstract(sexec_StateCase)


def test_sexec_statecase_constructor_exists():
    assert callable(sexec_StateCase.__init__)


def test_sexec_statecase_constructor_args():
    sig = inspect.signature(sexec_StateCase.__init__)
    params = list(sig.parameters.keys())



def test_trace_is_not_abstract():
    assert not inspect.isabstract(Trace)


def test_trace_constructor_exists():
    assert callable(Trace.__init__)


def test_trace_constructor_args():
    sig = inspect.signature(Trace.__init__)
    params = list(sig.parameters.keys())



def test_sexec_tracestateentered_is_not_abstract():
    assert not inspect.isabstract(sexec_TraceStateEntered)


def test_sexec_tracestateentered_constructor_exists():
    assert callable(sexec_TraceStateEntered.__init__)


def test_sexec_tracestateentered_constructor_args():
    sig = inspect.signature(sexec_TraceStateEntered.__init__)
    params = list(sig.parameters.keys())



def test_sexec_reactionfired_is_not_abstract():
    assert not inspect.isabstract(sexec_ReactionFired)


def test_sexec_reactionfired_constructor_exists():
    assert callable(sexec_ReactionFired.__init__)


def test_sexec_reactionfired_constructor_args():
    sig = inspect.signature(sexec_ReactionFired.__init__)
    params = list(sig.parameters.keys())



def test_sexec_tracestateexited_is_not_abstract():
    assert not inspect.isabstract(sexec_TraceStateExited)


def test_sexec_tracestateexited_constructor_exists():
    assert callable(sexec_TraceStateExited.__init__)


def test_sexec_tracestateexited_constructor_args():
    sig = inspect.signature(sexec_TraceStateExited.__init__)
    params = list(sig.parameters.keys())



def test_sexec_tracebeginruncycle_is_not_abstract():
    assert not inspect.isabstract(sexec_TraceBeginRunCycle)


def test_sexec_tracebeginruncycle_constructor_exists():
    assert callable(sexec_TraceBeginRunCycle.__init__)


def test_sexec_tracebeginruncycle_constructor_args():
    sig = inspect.signature(sexec_TraceBeginRunCycle.__init__)
    params = list(sig.parameters.keys())



def test_sexec_tracereactionwillfire_is_not_abstract():
    assert not inspect.isabstract(sexec_TraceReactionWillFire)


def test_sexec_tracereactionwillfire_constructor_exists():
    assert callable(sexec_TraceReactionWillFire.__init__)


def test_sexec_tracereactionwillfire_constructor_args():
    sig = inspect.signature(sexec_TraceReactionWillFire.__init__)
    params = list(sig.parameters.keys())



def test_sexec_traceendruncycle_is_not_abstract():
    assert not inspect.isabstract(sexec_TraceEndRunCycle)


def test_sexec_traceendruncycle_constructor_exists():
    assert callable(sexec_TraceEndRunCycle.__init__)


def test_sexec_traceendruncycle_constructor_args():
    sig = inspect.signature(sexec_TraceEndRunCycle.__init__)
    params = list(sig.parameters.keys())



def test_sexec_tracenodeexecuted_is_not_abstract():
    assert not inspect.isabstract(sexec_TraceNodeExecuted)


def test_sexec_tracenodeexecuted_constructor_exists():
    assert callable(sexec_TraceNodeExecuted.__init__)


def test_sexec_tracenodeexecuted_constructor_args():
    sig = inspect.signature(sexec_TraceNodeExecuted.__init__)
    params = list(sig.parameters.keys())



def test_check_is_not_abstract():
    assert not inspect.isabstract(Check)


def test_check_constructor_exists():
    assert callable(Check.__init__)


def test_check_constructor_args():
    sig = inspect.signature(Check.__init__)
    params = list(sig.parameters.keys())



def test_sexec_checkref_is_not_abstract():
    assert not inspect.isabstract(sexec_CheckRef)


def test_sexec_checkref_constructor_exists():
    assert callable(sexec_CheckRef.__init__)


def test_sexec_checkref_constructor_args():
    sig = inspect.signature(sexec_CheckRef.__init__)
    params = list(sig.parameters.keys())



def test_sexec_expression_is_not_abstract():
    assert not inspect.isabstract(sexec_Expression)


def test_sexec_expression_constructor_exists():
    assert callable(sexec_Expression.__init__)


def test_sexec_expression_constructor_args():
    sig = inspect.signature(sexec_Expression.__init__)
    params = list(sig.parameters.keys())



def test_step_is_not_abstract():
    assert not inspect.isabstract(Step)


def test_step_constructor_exists():
    assert callable(Step.__init__)


def test_step_constructor_args():
    sig = inspect.signature(Step.__init__)
    params = list(sig.parameters.keys())



def test_sexec_unscheduletimeevent_is_not_abstract():
    assert not inspect.isabstract(sexec_UnscheduleTimeEvent)


def test_sexec_unscheduletimeevent_constructor_exists():
    assert callable(sexec_UnscheduleTimeEvent.__init__)


def test_sexec_unscheduletimeevent_constructor_args():
    sig = inspect.signature(sexec_UnscheduleTimeEvent.__init__)
    params = list(sig.parameters.keys())



def test_sexec_historyentry_is_not_abstract():
    assert not inspect.isabstract(sexec_HistoryEntry)


def test_sexec_historyentry_constructor_exists():
    assert callable(sexec_HistoryEntry.__init__)


def test_sexec_historyentry_constructor_args():
    sig = inspect.signature(sexec_HistoryEntry.__init__)
    params = list(sig.parameters.keys())
    assert "deep" in params, "Missing parameter 'deep'"

def test_sexec_historyentry_has_deep():
    assert hasattr(sexec_HistoryEntry, "deep")
    descriptor = None
    for klass in sexec_HistoryEntry.__mro__:
        if "deep" in klass.__dict__:
            descriptor = klass.__dict__["deep"]
            break
    assert isinstance(descriptor, property)



def test_sexec_stateswitch_is_not_abstract():
    assert not inspect.isabstract(sexec_StateSwitch)


def test_sexec_stateswitch_constructor_exists():
    assert callable(sexec_StateSwitch.__init__)


def test_sexec_stateswitch_constructor_args():
    sig = inspect.signature(sexec_StateSwitch.__init__)
    params = list(sig.parameters.keys())
    assert "stateConfigurationIdx" in params, "Missing parameter 'stateConfigurationIdx'"

def test_sexec_stateswitch_has_stateConfigurationIdx():
    assert hasattr(sexec_StateSwitch, "stateConfigurationIdx")
    descriptor = None
    for klass in sexec_StateSwitch.__mro__:
        if "stateConfigurationIdx" in klass.__dict__:
            descriptor = klass.__dict__["stateConfigurationIdx"]
            break
    assert isinstance(descriptor, property)



def test_sexec_exitstate_is_not_abstract():
    assert not inspect.isabstract(sexec_ExitState)


def test_sexec_exitstate_constructor_exists():
    assert callable(sexec_ExitState.__init__)


def test_sexec_exitstate_constructor_args():
    sig = inspect.signature(sexec_ExitState.__init__)
    params = list(sig.parameters.keys())



def test_sexec_call_is_not_abstract():
    assert not inspect.isabstract(sexec_Call)


def test_sexec_call_constructor_exists():
    assert callable(sexec_Call.__init__)


def test_sexec_call_constructor_args():
    sig = inspect.signature(sexec_Call.__init__)
    params = list(sig.parameters.keys())



def test_sexec_execution_is_not_abstract():
    assert not inspect.isabstract(sexec_Execution)


def test_sexec_execution_constructor_exists():
    assert callable(sexec_Execution.__init__)


def test_sexec_execution_constructor_args():
    sig = inspect.signature(sexec_Execution.__init__)
    params = list(sig.parameters.keys())



def test_sexec_scheduletimeevent_is_not_abstract():
    assert not inspect.isabstract(sexec_ScheduleTimeEvent)


def test_sexec_scheduletimeevent_constructor_exists():
    assert callable(sexec_ScheduleTimeEvent.__init__)


def test_sexec_scheduletimeevent_constructor_args():
    sig = inspect.signature(sexec_ScheduleTimeEvent.__init__)
    params = list(sig.parameters.keys())



def test_sexec_enterstate_is_not_abstract():
    assert not inspect.isabstract(sexec_EnterState)


def test_sexec_enterstate_constructor_exists():
    assert callable(sexec_EnterState.__init__)


def test_sexec_enterstate_constructor_args():
    sig = inspect.signature(sexec_EnterState.__init__)
    params = list(sig.parameters.keys())



def test_sexec_savehistory_is_not_abstract():
    assert not inspect.isabstract(sexec_SaveHistory)


def test_sexec_savehistory_constructor_exists():
    assert callable(sexec_SaveHistory.__init__)


def test_sexec_savehistory_constructor_args():
    sig = inspect.signature(sexec_SaveHistory.__init__)
    params = list(sig.parameters.keys())
    assert "deep" in params, "Missing parameter 'deep'"

def test_sexec_savehistory_has_deep():
    assert hasattr(sexec_SaveHistory, "deep")
    descriptor = None
    for klass in sexec_SaveHistory.__mro__:
        if "deep" in klass.__dict__:
            descriptor = klass.__dict__["deep"]
            break
    assert isinstance(descriptor, property)



def test_sexec_trace_is_not_abstract():
    assert not inspect.isabstract(sexec_Trace)


def test_sexec_trace_constructor_exists():
    assert callable(sexec_Trace.__init__)


def test_sexec_trace_constructor_args():
    sig = inspect.signature(sexec_Trace.__init__)
    params = list(sig.parameters.keys())



def test_sexec_check_is_not_abstract():
    assert not inspect.isabstract(sexec_Check)


def test_sexec_check_constructor_exists():
    assert callable(sexec_Check.__init__)


def test_sexec_check_constructor_args():
    sig = inspect.signature(sexec_Check.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_sexec_timeevent_is_not_abstract():
    assert not inspect.isabstract(sexec_TimeEvent)


def test_sexec_timeevent_constructor_exists():
    assert callable(sexec_TimeEvent.__init__)


def test_sexec_timeevent_constructor_args():
    sig = inspect.signature(sexec_TimeEvent.__init__)
    params = list(sig.parameters.keys())
    assert "periodic" in params, "Missing parameter 'periodic'"

def test_sexec_timeevent_has_periodic():
    assert hasattr(sexec_TimeEvent, "periodic")
    descriptor = None
    for klass in sexec_TimeEvent.__mro__:
        if "periodic" in klass.__dict__:
            descriptor = klass.__dict__["periodic"]
            break
    assert isinstance(descriptor, property)



def test_executionnode_is_not_abstract():
    assert not inspect.isabstract(ExecutionNode)


def test_executionnode_constructor_exists():
    assert callable(ExecutionNode.__init__)


def test_executionnode_constructor_args():
    sig = inspect.signature(ExecutionNode.__init__)
    params = list(sig.parameters.keys())



def test_sexec_executionexit_is_not_abstract():
    assert not inspect.isabstract(sexec_ExecutionExit)


def test_sexec_executionexit_constructor_exists():
    assert callable(sexec_ExecutionExit.__init__)


def test_sexec_executionexit_constructor_args():
    sig = inspect.signature(sexec_ExecutionExit.__init__)
    params = list(sig.parameters.keys())



def test_sexec_executionentry_is_not_abstract():
    assert not inspect.isabstract(sexec_ExecutionEntry)


def test_sexec_executionentry_constructor_exists():
    assert callable(sexec_ExecutionEntry.__init__)


def test_sexec_executionentry_constructor_args():
    sig = inspect.signature(sexec_ExecutionEntry.__init__)
    params = list(sig.parameters.keys())



def test_sexec_executionchoice_is_not_abstract():
    assert not inspect.isabstract(sexec_ExecutionChoice)


def test_sexec_executionchoice_constructor_exists():
    assert callable(sexec_ExecutionChoice.__init__)


def test_sexec_executionchoice_constructor_args():
    sig = inspect.signature(sexec_ExecutionChoice.__init__)
    params = list(sig.parameters.keys())



def test_sexec_executionsynchronization_is_not_abstract():
    assert not inspect.isabstract(sexec_ExecutionSynchronization)


def test_sexec_executionsynchronization_constructor_exists():
    assert callable(sexec_ExecutionSynchronization.__init__)


def test_sexec_executionsynchronization_constructor_args():
    sig = inspect.signature(sexec_ExecutionSynchronization.__init__)
    params = list(sig.parameters.keys())



def test_executionscope_is_not_abstract():
    assert not inspect.isabstract(ExecutionScope)


def test_executionscope_constructor_exists():
    assert callable(ExecutionScope.__init__)


def test_executionscope_constructor_args():
    sig = inspect.signature(ExecutionScope.__init__)
    params = list(sig.parameters.keys())



def test_scopedelement_is_not_abstract():
    assert not inspect.isabstract(ScopedElement)


def test_scopedelement_constructor_exists():
    assert callable(ScopedElement.__init__)


def test_scopedelement_constructor_args():
    sig = inspect.signature(ScopedElement.__init__)
    params = list(sig.parameters.keys())



def test_sexec_executionflow_is_not_abstract():
    assert not inspect.isabstract(sexec_ExecutionFlow)


def test_sexec_executionflow_constructor_exists():
    assert callable(sexec_ExecutionFlow.__init__)


def test_sexec_executionflow_constructor_args():
    sig = inspect.signature(sexec_ExecutionFlow.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_mappedelement_is_not_abstract():
    assert not inspect.isabstract(MappedElement)


def test_mappedelement_constructor_exists():
    assert callable(MappedElement.__init__)


def test_mappedelement_constructor_args():
    sig = inspect.signature(MappedElement.__init__)
    params = list(sig.parameters.keys())



def test_sexec_executionscope_is_not_abstract():
    assert not inspect.isabstract(sexec_ExecutionScope)


def test_sexec_executionscope_constructor_exists():
    assert callable(sexec_ExecutionScope.__init__)


def test_sexec_executionscope_constructor_args():
    sig = inspect.signature(sexec_ExecutionScope.__init__)
    params = list(sig.parameters.keys())



def test_sexec_step_is_not_abstract():
    assert not inspect.isabstract(sexec_Step)


def test_sexec_step_constructor_exists():
    assert callable(sexec_Step.__init__)


def test_sexec_step_constructor_args():
    sig = inspect.signature(sexec_Step.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_sexec_step_has_comment():
    assert hasattr(sexec_Step, "comment")
    descriptor = None
    for klass in sexec_Step.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_sexec_statevector_is_not_abstract():
    assert not inspect.isabstract(sexec_StateVector)


def test_sexec_statevector_constructor_exists():
    assert callable(sexec_StateVector.__init__)


def test_sexec_statevector_constructor_args():
    sig = inspect.signature(sexec_StateVector.__init__)
    params = list(sig.parameters.keys())
    assert "offset" in params, "Missing parameter 'offset'"
    assert "size" in params, "Missing parameter 'size'"

def test_sexec_statevector_has_offset():
    assert hasattr(sexec_StateVector, "offset")
    descriptor = None
    for klass in sexec_StateVector.__mro__:
        if "offset" in klass.__dict__:
            descriptor = klass.__dict__["offset"]
            break
    assert isinstance(descriptor, property)

def test_sexec_statevector_has_size():
    assert hasattr(sexec_StateVector, "size")
    descriptor = None
    for klass in sexec_StateVector.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_sexec_executionregion_is_not_abstract():
    assert not inspect.isabstract(sexec_ExecutionRegion)


def test_sexec_executionregion_constructor_exists():
    assert callable(sexec_ExecutionRegion.__init__)


def test_sexec_executionregion_constructor_args():
    sig = inspect.signature(sexec_ExecutionRegion.__init__)
    params = list(sig.parameters.keys())



def test_sexec_executionnode_is_not_abstract():
    assert not inspect.isabstract(sexec_ExecutionNode)


def test_sexec_executionnode_constructor_exists():
    assert callable(sexec_ExecutionNode.__init__)


def test_sexec_executionnode_constructor_args():
    sig = inspect.signature(sexec_ExecutionNode.__init__)
    params = list(sig.parameters.keys())
    assert "simpleName" in params, "Missing parameter 'simpleName'"

def test_sexec_executionnode_has_simpleName():
    assert hasattr(sexec_ExecutionNode, "simpleName")
    descriptor = None
    for klass in sexec_ExecutionNode.__mro__:
        if "simpleName" in klass.__dict__:
            descriptor = klass.__dict__["simpleName"]
            break
    assert isinstance(descriptor, property)



def test_sexec_executionstate_is_not_abstract():
    assert not inspect.isabstract(sexec_ExecutionState)


def test_sexec_executionstate_constructor_exists():
    assert callable(sexec_ExecutionState.__init__)


def test_sexec_executionstate_constructor_args():
    sig = inspect.signature(sexec_ExecutionState.__init__)
    params = list(sig.parameters.keys())
    assert "leaf" in params, "Missing parameter 'leaf'"

def test_sexec_executionstate_has_leaf():
    assert hasattr(sexec_ExecutionState, "leaf")
    descriptor = None
    for klass in sexec_ExecutionState.__mro__:
        if "leaf" in klass.__dict__:
            descriptor = klass.__dict__["leaf"]
            break
    assert isinstance(descriptor, property)



def test_sexec_eobject_is_not_abstract():
    assert not inspect.isabstract(sexec_EObject)


def test_sexec_eobject_constructor_exists():
    assert callable(sexec_EObject.__init__)


def test_sexec_eobject_constructor_args():
    sig = inspect.signature(sexec_EObject.__init__)
    params = list(sig.parameters.keys())



def test_sexec_mappedelement_is_not_abstract():
    assert not inspect.isabstract(sexec_MappedElement)


def test_sexec_mappedelement_constructor_exists():
    assert callable(sexec_MappedElement.__init__)


def test_sexec_mappedelement_constructor_args():
    sig = inspect.signature(sexec_MappedElement.__init__)
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
sexec_StateCase_strategy = st.builds(
    sexec_StateCase,
)
Trace_strategy = st.builds(
    Trace,
)
sexec_TraceStateEntered_strategy = st.builds(
    sexec_TraceStateEntered,
)
sexec_ReactionFired_strategy = st.builds(
    sexec_ReactionFired,
)
sexec_TraceStateExited_strategy = st.builds(
    sexec_TraceStateExited,
)
sexec_TraceBeginRunCycle_strategy = st.builds(
    sexec_TraceBeginRunCycle,
)
sexec_TraceReactionWillFire_strategy = st.builds(
    sexec_TraceReactionWillFire,
)
sexec_TraceEndRunCycle_strategy = st.builds(
    sexec_TraceEndRunCycle,
)
sexec_TraceNodeExecuted_strategy = st.builds(
    sexec_TraceNodeExecuted,
)
Check_strategy = st.builds(
    Check,
)
sexec_CheckRef_strategy = st.builds(
    sexec_CheckRef,
)
sexec_Expression_strategy = st.builds(
    sexec_Expression,
)
Step_strategy = st.builds(
    Step,
)
sexec_UnscheduleTimeEvent_strategy = st.builds(
    sexec_UnscheduleTimeEvent,
)
sexec_HistoryEntry_strategy = st.builds(
    sexec_HistoryEntry,
    deep=
        st.booleans()
)
sexec_StateSwitch_strategy = st.builds(
    sexec_StateSwitch,
    stateConfigurationIdx=
        st.integers()
)
sexec_ExitState_strategy = st.builds(
    sexec_ExitState,
)
sexec_Call_strategy = st.builds(
    sexec_Call,
)
sexec_Execution_strategy = st.builds(
    sexec_Execution,
)
sexec_ScheduleTimeEvent_strategy = st.builds(
    sexec_ScheduleTimeEvent,
)
sexec_EnterState_strategy = st.builds(
    sexec_EnterState,
)
sexec_SaveHistory_strategy = st.builds(
    sexec_SaveHistory,
    deep=
        st.booleans()
)
sexec_Trace_strategy = st.builds(
    sexec_Trace,
)
sexec_Check_strategy = st.builds(
    sexec_Check,
)
Event_strategy = st.builds(
    Event,
)
sexec_TimeEvent_strategy = st.builds(
    sexec_TimeEvent,
    periodic=
        st.booleans()
)
ExecutionNode_strategy = st.builds(
    ExecutionNode,
)
sexec_ExecutionExit_strategy = st.builds(
    sexec_ExecutionExit,
)
sexec_ExecutionEntry_strategy = st.builds(
    sexec_ExecutionEntry,
)
sexec_ExecutionChoice_strategy = st.builds(
    sexec_ExecutionChoice,
)
sexec_ExecutionSynchronization_strategy = st.builds(
    sexec_ExecutionSynchronization,
)
ExecutionScope_strategy = st.builds(
    ExecutionScope,
)
ScopedElement_strategy = st.builds(
    ScopedElement,
)
sexec_ExecutionFlow_strategy = st.builds(
    sexec_ExecutionFlow,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
MappedElement_strategy = st.builds(
    MappedElement,
)
sexec_ExecutionScope_strategy = st.builds(
    sexec_ExecutionScope,
)
sexec_Step_strategy = st.builds(
    sexec_Step,
    comment=
        safe_text
)
sexec_StateVector_strategy = st.builds(
    sexec_StateVector,
    offset=
        st.integers(),
    size=
        st.integers()
)
sexec_ExecutionRegion_strategy = st.builds(
    sexec_ExecutionRegion,
)
sexec_ExecutionNode_strategy = st.builds(
    sexec_ExecutionNode,
    simpleName=
        safe_text
)
sexec_ExecutionState_strategy = st.builds(
    sexec_ExecutionState,
    leaf=
        st.booleans()
)
sexec_EObject_strategy = st.builds(
    sexec_EObject,
)
sexec_MappedElement_strategy = st.builds(
    sexec_MappedElement,
)

@given(instance=sexec_StateCase_strategy)
@settings(max_examples=50)
def test_sexec_statecase_instantiation(instance):
    assert isinstance(instance, sexec_StateCase)

@given(instance=Trace_strategy)
@settings(max_examples=50)
def test_trace_instantiation(instance):
    assert isinstance(instance, Trace)

@given(instance=sexec_TraceStateEntered_strategy)
@settings(max_examples=50)
def test_sexec_tracestateentered_instantiation(instance):
    assert isinstance(instance, sexec_TraceStateEntered)

@given(instance=sexec_ReactionFired_strategy)
@settings(max_examples=50)
def test_sexec_reactionfired_instantiation(instance):
    assert isinstance(instance, sexec_ReactionFired)

@given(instance=sexec_TraceStateExited_strategy)
@settings(max_examples=50)
def test_sexec_tracestateexited_instantiation(instance):
    assert isinstance(instance, sexec_TraceStateExited)

@given(instance=sexec_TraceBeginRunCycle_strategy)
@settings(max_examples=50)
def test_sexec_tracebeginruncycle_instantiation(instance):
    assert isinstance(instance, sexec_TraceBeginRunCycle)

@given(instance=sexec_TraceReactionWillFire_strategy)
@settings(max_examples=50)
def test_sexec_tracereactionwillfire_instantiation(instance):
    assert isinstance(instance, sexec_TraceReactionWillFire)

@given(instance=sexec_TraceEndRunCycle_strategy)
@settings(max_examples=50)
def test_sexec_traceendruncycle_instantiation(instance):
    assert isinstance(instance, sexec_TraceEndRunCycle)

@given(instance=sexec_TraceNodeExecuted_strategy)
@settings(max_examples=50)
def test_sexec_tracenodeexecuted_instantiation(instance):
    assert isinstance(instance, sexec_TraceNodeExecuted)

@given(instance=Check_strategy)
@settings(max_examples=50)
def test_check_instantiation(instance):
    assert isinstance(instance, Check)

@given(instance=sexec_CheckRef_strategy)
@settings(max_examples=50)
def test_sexec_checkref_instantiation(instance):
    assert isinstance(instance, sexec_CheckRef)

@given(instance=sexec_Expression_strategy)
@settings(max_examples=50)
def test_sexec_expression_instantiation(instance):
    assert isinstance(instance, sexec_Expression)

@given(instance=Step_strategy)
@settings(max_examples=50)
def test_step_instantiation(instance):
    assert isinstance(instance, Step)

@given(instance=sexec_UnscheduleTimeEvent_strategy)
@settings(max_examples=50)
def test_sexec_unscheduletimeevent_instantiation(instance):
    assert isinstance(instance, sexec_UnscheduleTimeEvent)

@given(instance=sexec_HistoryEntry_strategy)
@settings(max_examples=50)
def test_sexec_historyentry_instantiation(instance):
    assert isinstance(instance, sexec_HistoryEntry)



@given(instance=sexec_HistoryEntry_strategy)
def test_sexec_historyentry_deep_setter(instance):
    original = instance.deep
    instance.deep = original
    assert instance.deep == original

@given(instance=sexec_StateSwitch_strategy)
@settings(max_examples=50)
def test_sexec_stateswitch_instantiation(instance):
    assert isinstance(instance, sexec_StateSwitch)



@given(instance=sexec_StateSwitch_strategy)
def test_sexec_stateswitch_stateConfigurationIdx_setter(instance):
    original = instance.stateConfigurationIdx
    instance.stateConfigurationIdx = original
    assert instance.stateConfigurationIdx == original

@given(instance=sexec_ExitState_strategy)
@settings(max_examples=50)
def test_sexec_exitstate_instantiation(instance):
    assert isinstance(instance, sexec_ExitState)

@given(instance=sexec_Call_strategy)
@settings(max_examples=50)
def test_sexec_call_instantiation(instance):
    assert isinstance(instance, sexec_Call)

@given(instance=sexec_Execution_strategy)
@settings(max_examples=50)
def test_sexec_execution_instantiation(instance):
    assert isinstance(instance, sexec_Execution)

@given(instance=sexec_ScheduleTimeEvent_strategy)
@settings(max_examples=50)
def test_sexec_scheduletimeevent_instantiation(instance):
    assert isinstance(instance, sexec_ScheduleTimeEvent)

@given(instance=sexec_EnterState_strategy)
@settings(max_examples=50)
def test_sexec_enterstate_instantiation(instance):
    assert isinstance(instance, sexec_EnterState)

@given(instance=sexec_SaveHistory_strategy)
@settings(max_examples=50)
def test_sexec_savehistory_instantiation(instance):
    assert isinstance(instance, sexec_SaveHistory)



@given(instance=sexec_SaveHistory_strategy)
def test_sexec_savehistory_deep_setter(instance):
    original = instance.deep
    instance.deep = original
    assert instance.deep == original

@given(instance=sexec_Trace_strategy)
@settings(max_examples=50)
def test_sexec_trace_instantiation(instance):
    assert isinstance(instance, sexec_Trace)

@given(instance=sexec_Check_strategy)
@settings(max_examples=50)
def test_sexec_check_instantiation(instance):
    assert isinstance(instance, sexec_Check)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=sexec_TimeEvent_strategy)
@settings(max_examples=50)
def test_sexec_timeevent_instantiation(instance):
    assert isinstance(instance, sexec_TimeEvent)



@given(instance=sexec_TimeEvent_strategy)
def test_sexec_timeevent_periodic_setter(instance):
    original = instance.periodic
    instance.periodic = original
    assert instance.periodic == original

@given(instance=ExecutionNode_strategy)
@settings(max_examples=50)
def test_executionnode_instantiation(instance):
    assert isinstance(instance, ExecutionNode)

@given(instance=sexec_ExecutionExit_strategy)
@settings(max_examples=50)
def test_sexec_executionexit_instantiation(instance):
    assert isinstance(instance, sexec_ExecutionExit)

@given(instance=sexec_ExecutionEntry_strategy)
@settings(max_examples=50)
def test_sexec_executionentry_instantiation(instance):
    assert isinstance(instance, sexec_ExecutionEntry)

@given(instance=sexec_ExecutionChoice_strategy)
@settings(max_examples=50)
def test_sexec_executionchoice_instantiation(instance):
    assert isinstance(instance, sexec_ExecutionChoice)

@given(instance=sexec_ExecutionSynchronization_strategy)
@settings(max_examples=50)
def test_sexec_executionsynchronization_instantiation(instance):
    assert isinstance(instance, sexec_ExecutionSynchronization)

@given(instance=ExecutionScope_strategy)
@settings(max_examples=50)
def test_executionscope_instantiation(instance):
    assert isinstance(instance, ExecutionScope)

@given(instance=ScopedElement_strategy)
@settings(max_examples=50)
def test_scopedelement_instantiation(instance):
    assert isinstance(instance, ScopedElement)

@given(instance=sexec_ExecutionFlow_strategy)
@settings(max_examples=50)
def test_sexec_executionflow_instantiation(instance):
    assert isinstance(instance, sexec_ExecutionFlow)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=MappedElement_strategy)
@settings(max_examples=50)
def test_mappedelement_instantiation(instance):
    assert isinstance(instance, MappedElement)

@given(instance=sexec_ExecutionScope_strategy)
@settings(max_examples=50)
def test_sexec_executionscope_instantiation(instance):
    assert isinstance(instance, sexec_ExecutionScope)

@given(instance=sexec_Step_strategy)
@settings(max_examples=50)
def test_sexec_step_instantiation(instance):
    assert isinstance(instance, sexec_Step)



@given(instance=sexec_Step_strategy)
def test_sexec_step_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=sexec_StateVector_strategy)
@settings(max_examples=50)
def test_sexec_statevector_instantiation(instance):
    assert isinstance(instance, sexec_StateVector)



@given(instance=sexec_StateVector_strategy)
def test_sexec_statevector_offset_setter(instance):
    original = instance.offset
    instance.offset = original
    assert instance.offset == original



@given(instance=sexec_StateVector_strategy)
def test_sexec_statevector_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=sexec_ExecutionRegion_strategy)
@settings(max_examples=50)
def test_sexec_executionregion_instantiation(instance):
    assert isinstance(instance, sexec_ExecutionRegion)

@given(instance=sexec_ExecutionNode_strategy)
@settings(max_examples=50)
def test_sexec_executionnode_instantiation(instance):
    assert isinstance(instance, sexec_ExecutionNode)



@given(instance=sexec_ExecutionNode_strategy)
def test_sexec_executionnode_simpleName_setter(instance):
    original = instance.simpleName
    instance.simpleName = original
    assert instance.simpleName == original

@given(instance=sexec_ExecutionState_strategy)
@settings(max_examples=50)
def test_sexec_executionstate_instantiation(instance):
    assert isinstance(instance, sexec_ExecutionState)



@given(instance=sexec_ExecutionState_strategy)
def test_sexec_executionstate_leaf_setter(instance):
    original = instance.leaf
    instance.leaf = original
    assert instance.leaf == original

@given(instance=sexec_EObject_strategy)
@settings(max_examples=50)
def test_sexec_eobject_instantiation(instance):
    assert isinstance(instance, sexec_EObject)

@given(instance=sexec_MappedElement_strategy)
@settings(max_examples=50)
def test_sexec_mappedelement_instantiation(instance):
    assert isinstance(instance, sexec_MappedElement)
