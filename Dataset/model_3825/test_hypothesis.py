import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Check,
    sexec::CheckRef,
    sexec::Expression,
    Step,
    sexec::Execution,
    sexec::Call,
    sexec::EnterState,
    sexec::ExitState,
    sexec::Check,
    Event,
    sexec::TimeEvent,
    ExecutionNode,
    sexec::ExecutionSynchronization,
    ExecutionScope,
    ScopedElement,
    sexec::ExecutionFlow,
    NamedElement,
    MappedElement,
    sexec::ExecutionScope,
    sexec::Step,
    sexec::StateVector,
    sexec::ExecutionRegion,
    sexec::ExecutionNode,
    sexec::ExecutionState,
    sexec::EObject,
    sexec::MappedElement,
    sexec::StateCase,
    sexec::StateSwitch,
    Trace,
    sexec::TraceReactionWillFire,
    sexec::ReactionFired,
    sexec::TraceStateEntered,
    sexec::TraceStateExited,
    sexec::TraceEndRunCycle,
    sexec::TraceBeginRunCycle,
    sexec::TraceNodeExecuted,
    sexec::Trace,
    sexec::HistoryEntry,
    sexec::SaveHistory,
    sexec::ExecutionChoice,
    sexec::ExecutionExit,
    sexec::ExecutionEntry,
    sexec::UnscheduleTimeEvent,
    sexec::ScheduleTimeEvent,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_check_is_not_abstract():
    assert not inspect.isabstract(Check)


def test_check_constructor_exists():
    assert callable(Check.__init__)


def test_check_constructor_args():
    sig = inspect.signature(Check.__init__)
    params = list(sig.parameters.keys())



def test_sexec::checkref_is_not_abstract():
    assert not inspect.isabstract(sexec::CheckRef)


def test_sexec::checkref_constructor_exists():
    assert callable(sexec::CheckRef.__init__)


def test_sexec::checkref_constructor_args():
    sig = inspect.signature(sexec::CheckRef.__init__)
    params = list(sig.parameters.keys())



def test_sexec::expression_is_not_abstract():
    assert not inspect.isabstract(sexec::Expression)


def test_sexec::expression_constructor_exists():
    assert callable(sexec::Expression.__init__)


def test_sexec::expression_constructor_args():
    sig = inspect.signature(sexec::Expression.__init__)
    params = list(sig.parameters.keys())



def test_step_is_not_abstract():
    assert not inspect.isabstract(Step)


def test_step_constructor_exists():
    assert callable(Step.__init__)


def test_step_constructor_args():
    sig = inspect.signature(Step.__init__)
    params = list(sig.parameters.keys())



def test_sexec::execution_is_not_abstract():
    assert not inspect.isabstract(sexec::Execution)


def test_sexec::execution_constructor_exists():
    assert callable(sexec::Execution.__init__)


def test_sexec::execution_constructor_args():
    sig = inspect.signature(sexec::Execution.__init__)
    params = list(sig.parameters.keys())



def test_sexec::call_is_not_abstract():
    assert not inspect.isabstract(sexec::Call)


def test_sexec::call_constructor_exists():
    assert callable(sexec::Call.__init__)


def test_sexec::call_constructor_args():
    sig = inspect.signature(sexec::Call.__init__)
    params = list(sig.parameters.keys())



def test_sexec::enterstate_is_not_abstract():
    assert not inspect.isabstract(sexec::EnterState)


def test_sexec::enterstate_constructor_exists():
    assert callable(sexec::EnterState.__init__)


def test_sexec::enterstate_constructor_args():
    sig = inspect.signature(sexec::EnterState.__init__)
    params = list(sig.parameters.keys())



def test_sexec::exitstate_is_not_abstract():
    assert not inspect.isabstract(sexec::ExitState)


def test_sexec::exitstate_constructor_exists():
    assert callable(sexec::ExitState.__init__)


def test_sexec::exitstate_constructor_args():
    sig = inspect.signature(sexec::ExitState.__init__)
    params = list(sig.parameters.keys())



def test_sexec::check_is_not_abstract():
    assert not inspect.isabstract(sexec::Check)


def test_sexec::check_constructor_exists():
    assert callable(sexec::Check.__init__)


def test_sexec::check_constructor_args():
    sig = inspect.signature(sexec::Check.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_sexec::timeevent_is_not_abstract():
    assert not inspect.isabstract(sexec::TimeEvent)


def test_sexec::timeevent_constructor_exists():
    assert callable(sexec::TimeEvent.__init__)


def test_sexec::timeevent_constructor_args():
    sig = inspect.signature(sexec::TimeEvent.__init__)
    params = list(sig.parameters.keys())
    assert "periodic" in params, "Missing parameter 'periodic'"

def test_sexec::timeevent_has_periodic():
    assert hasattr(sexec::TimeEvent, "periodic")
    descriptor = None
    for klass in sexec::TimeEvent.__mro__:
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



def test_sexec::executionsynchronization_is_not_abstract():
    assert not inspect.isabstract(sexec::ExecutionSynchronization)


def test_sexec::executionsynchronization_constructor_exists():
    assert callable(sexec::ExecutionSynchronization.__init__)


def test_sexec::executionsynchronization_constructor_args():
    sig = inspect.signature(sexec::ExecutionSynchronization.__init__)
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



def test_sexec::executionflow_is_not_abstract():
    assert not inspect.isabstract(sexec::ExecutionFlow)


def test_sexec::executionflow_constructor_exists():
    assert callable(sexec::ExecutionFlow.__init__)


def test_sexec::executionflow_constructor_args():
    sig = inspect.signature(sexec::ExecutionFlow.__init__)
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



def test_sexec::executionscope_is_not_abstract():
    assert not inspect.isabstract(sexec::ExecutionScope)


def test_sexec::executionscope_constructor_exists():
    assert callable(sexec::ExecutionScope.__init__)


def test_sexec::executionscope_constructor_args():
    sig = inspect.signature(sexec::ExecutionScope.__init__)
    params = list(sig.parameters.keys())



def test_sexec::step_is_not_abstract():
    assert not inspect.isabstract(sexec::Step)


def test_sexec::step_constructor_exists():
    assert callable(sexec::Step.__init__)


def test_sexec::step_constructor_args():
    sig = inspect.signature(sexec::Step.__init__)
    params = list(sig.parameters.keys())
    assert "comment" in params, "Missing parameter 'comment'"

def test_sexec::step_has_comment():
    assert hasattr(sexec::Step, "comment")
    descriptor = None
    for klass in sexec::Step.__mro__:
        if "comment" in klass.__dict__:
            descriptor = klass.__dict__["comment"]
            break
    assert isinstance(descriptor, property)



def test_sexec::statevector_is_not_abstract():
    assert not inspect.isabstract(sexec::StateVector)


def test_sexec::statevector_constructor_exists():
    assert callable(sexec::StateVector.__init__)


def test_sexec::statevector_constructor_args():
    sig = inspect.signature(sexec::StateVector.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "offset" in params, "Missing parameter 'offset'"

def test_sexec::statevector_has_size():
    assert hasattr(sexec::StateVector, "size")
    descriptor = None
    for klass in sexec::StateVector.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_sexec::statevector_has_offset():
    assert hasattr(sexec::StateVector, "offset")
    descriptor = None
    for klass in sexec::StateVector.__mro__:
        if "offset" in klass.__dict__:
            descriptor = klass.__dict__["offset"]
            break
    assert isinstance(descriptor, property)



def test_sexec::executionregion_is_not_abstract():
    assert not inspect.isabstract(sexec::ExecutionRegion)


def test_sexec::executionregion_constructor_exists():
    assert callable(sexec::ExecutionRegion.__init__)


def test_sexec::executionregion_constructor_args():
    sig = inspect.signature(sexec::ExecutionRegion.__init__)
    params = list(sig.parameters.keys())



def test_sexec::executionnode_is_not_abstract():
    assert not inspect.isabstract(sexec::ExecutionNode)


def test_sexec::executionnode_constructor_exists():
    assert callable(sexec::ExecutionNode.__init__)


def test_sexec::executionnode_constructor_args():
    sig = inspect.signature(sexec::ExecutionNode.__init__)
    params = list(sig.parameters.keys())
    assert "simpleName" in params, "Missing parameter 'simpleName'"

def test_sexec::executionnode_has_simpleName():
    assert hasattr(sexec::ExecutionNode, "simpleName")
    descriptor = None
    for klass in sexec::ExecutionNode.__mro__:
        if "simpleName" in klass.__dict__:
            descriptor = klass.__dict__["simpleName"]
            break
    assert isinstance(descriptor, property)



def test_sexec::executionstate_is_not_abstract():
    assert not inspect.isabstract(sexec::ExecutionState)


def test_sexec::executionstate_constructor_exists():
    assert callable(sexec::ExecutionState.__init__)


def test_sexec::executionstate_constructor_args():
    sig = inspect.signature(sexec::ExecutionState.__init__)
    params = list(sig.parameters.keys())
    assert "leaf" in params, "Missing parameter 'leaf'"

def test_sexec::executionstate_has_leaf():
    assert hasattr(sexec::ExecutionState, "leaf")
    descriptor = None
    for klass in sexec::ExecutionState.__mro__:
        if "leaf" in klass.__dict__:
            descriptor = klass.__dict__["leaf"]
            break
    assert isinstance(descriptor, property)



def test_sexec::eobject_is_not_abstract():
    assert not inspect.isabstract(sexec::EObject)


def test_sexec::eobject_constructor_exists():
    assert callable(sexec::EObject.__init__)


def test_sexec::eobject_constructor_args():
    sig = inspect.signature(sexec::EObject.__init__)
    params = list(sig.parameters.keys())



def test_sexec::mappedelement_is_not_abstract():
    assert not inspect.isabstract(sexec::MappedElement)


def test_sexec::mappedelement_constructor_exists():
    assert callable(sexec::MappedElement.__init__)


def test_sexec::mappedelement_constructor_args():
    sig = inspect.signature(sexec::MappedElement.__init__)
    params = list(sig.parameters.keys())



def test_sexec::statecase_is_not_abstract():
    assert not inspect.isabstract(sexec::StateCase)


def test_sexec::statecase_constructor_exists():
    assert callable(sexec::StateCase.__init__)


def test_sexec::statecase_constructor_args():
    sig = inspect.signature(sexec::StateCase.__init__)
    params = list(sig.parameters.keys())



def test_sexec::stateswitch_is_not_abstract():
    assert not inspect.isabstract(sexec::StateSwitch)


def test_sexec::stateswitch_constructor_exists():
    assert callable(sexec::StateSwitch.__init__)


def test_sexec::stateswitch_constructor_args():
    sig = inspect.signature(sexec::StateSwitch.__init__)
    params = list(sig.parameters.keys())
    assert "stateConfigurationIdx" in params, "Missing parameter 'stateConfigurationIdx'"

def test_sexec::stateswitch_has_stateConfigurationIdx():
    assert hasattr(sexec::StateSwitch, "stateConfigurationIdx")
    descriptor = None
    for klass in sexec::StateSwitch.__mro__:
        if "stateConfigurationIdx" in klass.__dict__:
            descriptor = klass.__dict__["stateConfigurationIdx"]
            break
    assert isinstance(descriptor, property)



def test_trace_is_not_abstract():
    assert not inspect.isabstract(Trace)


def test_trace_constructor_exists():
    assert callable(Trace.__init__)


def test_trace_constructor_args():
    sig = inspect.signature(Trace.__init__)
    params = list(sig.parameters.keys())



def test_sexec::tracereactionwillfire_is_not_abstract():
    assert not inspect.isabstract(sexec::TraceReactionWillFire)


def test_sexec::tracereactionwillfire_constructor_exists():
    assert callable(sexec::TraceReactionWillFire.__init__)


def test_sexec::tracereactionwillfire_constructor_args():
    sig = inspect.signature(sexec::TraceReactionWillFire.__init__)
    params = list(sig.parameters.keys())



def test_sexec::reactionfired_is_not_abstract():
    assert not inspect.isabstract(sexec::ReactionFired)


def test_sexec::reactionfired_constructor_exists():
    assert callable(sexec::ReactionFired.__init__)


def test_sexec::reactionfired_constructor_args():
    sig = inspect.signature(sexec::ReactionFired.__init__)
    params = list(sig.parameters.keys())



def test_sexec::tracestateentered_is_not_abstract():
    assert not inspect.isabstract(sexec::TraceStateEntered)


def test_sexec::tracestateentered_constructor_exists():
    assert callable(sexec::TraceStateEntered.__init__)


def test_sexec::tracestateentered_constructor_args():
    sig = inspect.signature(sexec::TraceStateEntered.__init__)
    params = list(sig.parameters.keys())



def test_sexec::tracestateexited_is_not_abstract():
    assert not inspect.isabstract(sexec::TraceStateExited)


def test_sexec::tracestateexited_constructor_exists():
    assert callable(sexec::TraceStateExited.__init__)


def test_sexec::tracestateexited_constructor_args():
    sig = inspect.signature(sexec::TraceStateExited.__init__)
    params = list(sig.parameters.keys())



def test_sexec::traceendruncycle_is_not_abstract():
    assert not inspect.isabstract(sexec::TraceEndRunCycle)


def test_sexec::traceendruncycle_constructor_exists():
    assert callable(sexec::TraceEndRunCycle.__init__)


def test_sexec::traceendruncycle_constructor_args():
    sig = inspect.signature(sexec::TraceEndRunCycle.__init__)
    params = list(sig.parameters.keys())



def test_sexec::tracebeginruncycle_is_not_abstract():
    assert not inspect.isabstract(sexec::TraceBeginRunCycle)


def test_sexec::tracebeginruncycle_constructor_exists():
    assert callable(sexec::TraceBeginRunCycle.__init__)


def test_sexec::tracebeginruncycle_constructor_args():
    sig = inspect.signature(sexec::TraceBeginRunCycle.__init__)
    params = list(sig.parameters.keys())



def test_sexec::tracenodeexecuted_is_not_abstract():
    assert not inspect.isabstract(sexec::TraceNodeExecuted)


def test_sexec::tracenodeexecuted_constructor_exists():
    assert callable(sexec::TraceNodeExecuted.__init__)


def test_sexec::tracenodeexecuted_constructor_args():
    sig = inspect.signature(sexec::TraceNodeExecuted.__init__)
    params = list(sig.parameters.keys())



def test_sexec::trace_is_not_abstract():
    assert not inspect.isabstract(sexec::Trace)


def test_sexec::trace_constructor_exists():
    assert callable(sexec::Trace.__init__)


def test_sexec::trace_constructor_args():
    sig = inspect.signature(sexec::Trace.__init__)
    params = list(sig.parameters.keys())



def test_sexec::historyentry_is_not_abstract():
    assert not inspect.isabstract(sexec::HistoryEntry)


def test_sexec::historyentry_constructor_exists():
    assert callable(sexec::HistoryEntry.__init__)


def test_sexec::historyentry_constructor_args():
    sig = inspect.signature(sexec::HistoryEntry.__init__)
    params = list(sig.parameters.keys())
    assert "deep" in params, "Missing parameter 'deep'"

def test_sexec::historyentry_has_deep():
    assert hasattr(sexec::HistoryEntry, "deep")
    descriptor = None
    for klass in sexec::HistoryEntry.__mro__:
        if "deep" in klass.__dict__:
            descriptor = klass.__dict__["deep"]
            break
    assert isinstance(descriptor, property)



def test_sexec::savehistory_is_not_abstract():
    assert not inspect.isabstract(sexec::SaveHistory)


def test_sexec::savehistory_constructor_exists():
    assert callable(sexec::SaveHistory.__init__)


def test_sexec::savehistory_constructor_args():
    sig = inspect.signature(sexec::SaveHistory.__init__)
    params = list(sig.parameters.keys())
    assert "deep" in params, "Missing parameter 'deep'"

def test_sexec::savehistory_has_deep():
    assert hasattr(sexec::SaveHistory, "deep")
    descriptor = None
    for klass in sexec::SaveHistory.__mro__:
        if "deep" in klass.__dict__:
            descriptor = klass.__dict__["deep"]
            break
    assert isinstance(descriptor, property)



def test_sexec::executionchoice_is_not_abstract():
    assert not inspect.isabstract(sexec::ExecutionChoice)


def test_sexec::executionchoice_constructor_exists():
    assert callable(sexec::ExecutionChoice.__init__)


def test_sexec::executionchoice_constructor_args():
    sig = inspect.signature(sexec::ExecutionChoice.__init__)
    params = list(sig.parameters.keys())



def test_sexec::executionexit_is_not_abstract():
    assert not inspect.isabstract(sexec::ExecutionExit)


def test_sexec::executionexit_constructor_exists():
    assert callable(sexec::ExecutionExit.__init__)


def test_sexec::executionexit_constructor_args():
    sig = inspect.signature(sexec::ExecutionExit.__init__)
    params = list(sig.parameters.keys())



def test_sexec::executionentry_is_not_abstract():
    assert not inspect.isabstract(sexec::ExecutionEntry)


def test_sexec::executionentry_constructor_exists():
    assert callable(sexec::ExecutionEntry.__init__)


def test_sexec::executionentry_constructor_args():
    sig = inspect.signature(sexec::ExecutionEntry.__init__)
    params = list(sig.parameters.keys())



def test_sexec::unscheduletimeevent_is_not_abstract():
    assert not inspect.isabstract(sexec::UnscheduleTimeEvent)


def test_sexec::unscheduletimeevent_constructor_exists():
    assert callable(sexec::UnscheduleTimeEvent.__init__)


def test_sexec::unscheduletimeevent_constructor_args():
    sig = inspect.signature(sexec::UnscheduleTimeEvent.__init__)
    params = list(sig.parameters.keys())



def test_sexec::scheduletimeevent_is_not_abstract():
    assert not inspect.isabstract(sexec::ScheduleTimeEvent)


def test_sexec::scheduletimeevent_constructor_exists():
    assert callable(sexec::ScheduleTimeEvent.__init__)


def test_sexec::scheduletimeevent_constructor_args():
    sig = inspect.signature(sexec::ScheduleTimeEvent.__init__)
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
Check_strategy = st.builds(
    Check,
)
sexec::CheckRef_strategy = st.builds(
    sexec::CheckRef,
)
sexec::Expression_strategy = st.builds(
    sexec::Expression,
)
Step_strategy = st.builds(
    Step,
)
sexec::Execution_strategy = st.builds(
    sexec::Execution,
)
sexec::Call_strategy = st.builds(
    sexec::Call,
)
sexec::EnterState_strategy = st.builds(
    sexec::EnterState,
)
sexec::ExitState_strategy = st.builds(
    sexec::ExitState,
)
sexec::Check_strategy = st.builds(
    sexec::Check,
)
Event_strategy = st.builds(
    Event,
)
sexec::TimeEvent_strategy = st.builds(
    sexec::TimeEvent,
    periodic=
        st.booleans()
)
ExecutionNode_strategy = st.builds(
    ExecutionNode,
)
sexec::ExecutionSynchronization_strategy = st.builds(
    sexec::ExecutionSynchronization,
)
ExecutionScope_strategy = st.builds(
    ExecutionScope,
)
ScopedElement_strategy = st.builds(
    ScopedElement,
)
sexec::ExecutionFlow_strategy = st.builds(
    sexec::ExecutionFlow,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
MappedElement_strategy = st.builds(
    MappedElement,
)
sexec::ExecutionScope_strategy = st.builds(
    sexec::ExecutionScope,
)
sexec::Step_strategy = st.builds(
    sexec::Step,
    comment=
        safe_text
)
sexec::StateVector_strategy = st.builds(
    sexec::StateVector,
    size=
        st.integers(),
    offset=
        st.integers()
)
sexec::ExecutionRegion_strategy = st.builds(
    sexec::ExecutionRegion,
)
sexec::ExecutionNode_strategy = st.builds(
    sexec::ExecutionNode,
    simpleName=
        safe_text
)
sexec::ExecutionState_strategy = st.builds(
    sexec::ExecutionState,
    leaf=
        st.booleans()
)
sexec::EObject_strategy = st.builds(
    sexec::EObject,
)
sexec::MappedElement_strategy = st.builds(
    sexec::MappedElement,
)
sexec::StateCase_strategy = st.builds(
    sexec::StateCase,
)
sexec::StateSwitch_strategy = st.builds(
    sexec::StateSwitch,
    stateConfigurationIdx=
        st.integers()
)
Trace_strategy = st.builds(
    Trace,
)
sexec::TraceReactionWillFire_strategy = st.builds(
    sexec::TraceReactionWillFire,
)
sexec::ReactionFired_strategy = st.builds(
    sexec::ReactionFired,
)
sexec::TraceStateEntered_strategy = st.builds(
    sexec::TraceStateEntered,
)
sexec::TraceStateExited_strategy = st.builds(
    sexec::TraceStateExited,
)
sexec::TraceEndRunCycle_strategy = st.builds(
    sexec::TraceEndRunCycle,
)
sexec::TraceBeginRunCycle_strategy = st.builds(
    sexec::TraceBeginRunCycle,
)
sexec::TraceNodeExecuted_strategy = st.builds(
    sexec::TraceNodeExecuted,
)
sexec::Trace_strategy = st.builds(
    sexec::Trace,
)
sexec::HistoryEntry_strategy = st.builds(
    sexec::HistoryEntry,
    deep=
        st.booleans()
)
sexec::SaveHistory_strategy = st.builds(
    sexec::SaveHistory,
    deep=
        st.booleans()
)
sexec::ExecutionChoice_strategy = st.builds(
    sexec::ExecutionChoice,
)
sexec::ExecutionExit_strategy = st.builds(
    sexec::ExecutionExit,
)
sexec::ExecutionEntry_strategy = st.builds(
    sexec::ExecutionEntry,
)
sexec::UnscheduleTimeEvent_strategy = st.builds(
    sexec::UnscheduleTimeEvent,
)
sexec::ScheduleTimeEvent_strategy = st.builds(
    sexec::ScheduleTimeEvent,
)

@given(instance=Check_strategy)
@settings(max_examples=50)
def test_check_instantiation(instance):
    assert isinstance(instance, Check)

@given(instance=sexec::CheckRef_strategy)
@settings(max_examples=50)
def test_sexec::checkref_instantiation(instance):
    assert isinstance(instance, sexec::CheckRef)

@given(instance=sexec::Expression_strategy)
@settings(max_examples=50)
def test_sexec::expression_instantiation(instance):
    assert isinstance(instance, sexec::Expression)

@given(instance=Step_strategy)
@settings(max_examples=50)
def test_step_instantiation(instance):
    assert isinstance(instance, Step)

@given(instance=sexec::Execution_strategy)
@settings(max_examples=50)
def test_sexec::execution_instantiation(instance):
    assert isinstance(instance, sexec::Execution)

@given(instance=sexec::Call_strategy)
@settings(max_examples=50)
def test_sexec::call_instantiation(instance):
    assert isinstance(instance, sexec::Call)

@given(instance=sexec::EnterState_strategy)
@settings(max_examples=50)
def test_sexec::enterstate_instantiation(instance):
    assert isinstance(instance, sexec::EnterState)

@given(instance=sexec::ExitState_strategy)
@settings(max_examples=50)
def test_sexec::exitstate_instantiation(instance):
    assert isinstance(instance, sexec::ExitState)

@given(instance=sexec::Check_strategy)
@settings(max_examples=50)
def test_sexec::check_instantiation(instance):
    assert isinstance(instance, sexec::Check)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=sexec::TimeEvent_strategy)
@settings(max_examples=50)
def test_sexec::timeevent_instantiation(instance):
    assert isinstance(instance, sexec::TimeEvent)

@given(instance=sexec::TimeEvent_strategy)
def test_sexec::timeevent_periodic_type(instance):
    assert isinstance(instance.periodic, bool)


@given(instance=sexec::TimeEvent_strategy)
def test_sexec::timeevent_periodic_setter(instance):
    original = instance.periodic
    instance.periodic = original
    assert instance.periodic == original

@given(instance=ExecutionNode_strategy)
@settings(max_examples=50)
def test_executionnode_instantiation(instance):
    assert isinstance(instance, ExecutionNode)

@given(instance=sexec::ExecutionSynchronization_strategy)
@settings(max_examples=50)
def test_sexec::executionsynchronization_instantiation(instance):
    assert isinstance(instance, sexec::ExecutionSynchronization)

@given(instance=ExecutionScope_strategy)
@settings(max_examples=50)
def test_executionscope_instantiation(instance):
    assert isinstance(instance, ExecutionScope)

@given(instance=ScopedElement_strategy)
@settings(max_examples=50)
def test_scopedelement_instantiation(instance):
    assert isinstance(instance, ScopedElement)

@given(instance=sexec::ExecutionFlow_strategy)
@settings(max_examples=50)
def test_sexec::executionflow_instantiation(instance):
    assert isinstance(instance, sexec::ExecutionFlow)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=MappedElement_strategy)
@settings(max_examples=50)
def test_mappedelement_instantiation(instance):
    assert isinstance(instance, MappedElement)

@given(instance=sexec::ExecutionScope_strategy)
@settings(max_examples=50)
def test_sexec::executionscope_instantiation(instance):
    assert isinstance(instance, sexec::ExecutionScope)

@given(instance=sexec::Step_strategy)
@settings(max_examples=50)
def test_sexec::step_instantiation(instance):
    assert isinstance(instance, sexec::Step)

@given(instance=sexec::Step_strategy)
def test_sexec::step_comment_type(instance):
    assert isinstance(instance.comment, str)


@given(instance=sexec::Step_strategy)
def test_sexec::step_comment_setter(instance):
    original = instance.comment
    instance.comment = original
    assert instance.comment == original

@given(instance=sexec::StateVector_strategy)
@settings(max_examples=50)
def test_sexec::statevector_instantiation(instance):
    assert isinstance(instance, sexec::StateVector)

@given(instance=sexec::StateVector_strategy)
def test_sexec::statevector_size_type(instance):
    assert isinstance(instance.size, int)


@given(instance=sexec::StateVector_strategy)
def test_sexec::statevector_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=sexec::StateVector_strategy)
def test_sexec::statevector_offset_type(instance):
    assert isinstance(instance.offset, int)


@given(instance=sexec::StateVector_strategy)
def test_sexec::statevector_offset_setter(instance):
    original = instance.offset
    instance.offset = original
    assert instance.offset == original

@given(instance=sexec::ExecutionRegion_strategy)
@settings(max_examples=50)
def test_sexec::executionregion_instantiation(instance):
    assert isinstance(instance, sexec::ExecutionRegion)

@given(instance=sexec::ExecutionNode_strategy)
@settings(max_examples=50)
def test_sexec::executionnode_instantiation(instance):
    assert isinstance(instance, sexec::ExecutionNode)

@given(instance=sexec::ExecutionNode_strategy)
def test_sexec::executionnode_simpleName_type(instance):
    assert isinstance(instance.simpleName, str)


@given(instance=sexec::ExecutionNode_strategy)
def test_sexec::executionnode_simpleName_setter(instance):
    original = instance.simpleName
    instance.simpleName = original
    assert instance.simpleName == original

@given(instance=sexec::ExecutionState_strategy)
@settings(max_examples=50)
def test_sexec::executionstate_instantiation(instance):
    assert isinstance(instance, sexec::ExecutionState)

@given(instance=sexec::ExecutionState_strategy)
def test_sexec::executionstate_leaf_type(instance):
    assert isinstance(instance.leaf, bool)


@given(instance=sexec::ExecutionState_strategy)
def test_sexec::executionstate_leaf_setter(instance):
    original = instance.leaf
    instance.leaf = original
    assert instance.leaf == original

@given(instance=sexec::EObject_strategy)
@settings(max_examples=50)
def test_sexec::eobject_instantiation(instance):
    assert isinstance(instance, sexec::EObject)

@given(instance=sexec::MappedElement_strategy)
@settings(max_examples=50)
def test_sexec::mappedelement_instantiation(instance):
    assert isinstance(instance, sexec::MappedElement)

@given(instance=sexec::StateCase_strategy)
@settings(max_examples=50)
def test_sexec::statecase_instantiation(instance):
    assert isinstance(instance, sexec::StateCase)

@given(instance=sexec::StateSwitch_strategy)
@settings(max_examples=50)
def test_sexec::stateswitch_instantiation(instance):
    assert isinstance(instance, sexec::StateSwitch)

@given(instance=sexec::StateSwitch_strategy)
def test_sexec::stateswitch_stateConfigurationIdx_type(instance):
    assert isinstance(instance.stateConfigurationIdx, int)


@given(instance=sexec::StateSwitch_strategy)
def test_sexec::stateswitch_stateConfigurationIdx_setter(instance):
    original = instance.stateConfigurationIdx
    instance.stateConfigurationIdx = original
    assert instance.stateConfigurationIdx == original

@given(instance=Trace_strategy)
@settings(max_examples=50)
def test_trace_instantiation(instance):
    assert isinstance(instance, Trace)

@given(instance=sexec::TraceReactionWillFire_strategy)
@settings(max_examples=50)
def test_sexec::tracereactionwillfire_instantiation(instance):
    assert isinstance(instance, sexec::TraceReactionWillFire)

@given(instance=sexec::ReactionFired_strategy)
@settings(max_examples=50)
def test_sexec::reactionfired_instantiation(instance):
    assert isinstance(instance, sexec::ReactionFired)

@given(instance=sexec::TraceStateEntered_strategy)
@settings(max_examples=50)
def test_sexec::tracestateentered_instantiation(instance):
    assert isinstance(instance, sexec::TraceStateEntered)

@given(instance=sexec::TraceStateExited_strategy)
@settings(max_examples=50)
def test_sexec::tracestateexited_instantiation(instance):
    assert isinstance(instance, sexec::TraceStateExited)

@given(instance=sexec::TraceEndRunCycle_strategy)
@settings(max_examples=50)
def test_sexec::traceendruncycle_instantiation(instance):
    assert isinstance(instance, sexec::TraceEndRunCycle)

@given(instance=sexec::TraceBeginRunCycle_strategy)
@settings(max_examples=50)
def test_sexec::tracebeginruncycle_instantiation(instance):
    assert isinstance(instance, sexec::TraceBeginRunCycle)

@given(instance=sexec::TraceNodeExecuted_strategy)
@settings(max_examples=50)
def test_sexec::tracenodeexecuted_instantiation(instance):
    assert isinstance(instance, sexec::TraceNodeExecuted)

@given(instance=sexec::Trace_strategy)
@settings(max_examples=50)
def test_sexec::trace_instantiation(instance):
    assert isinstance(instance, sexec::Trace)

@given(instance=sexec::HistoryEntry_strategy)
@settings(max_examples=50)
def test_sexec::historyentry_instantiation(instance):
    assert isinstance(instance, sexec::HistoryEntry)

@given(instance=sexec::HistoryEntry_strategy)
def test_sexec::historyentry_deep_type(instance):
    assert isinstance(instance.deep, bool)


@given(instance=sexec::HistoryEntry_strategy)
def test_sexec::historyentry_deep_setter(instance):
    original = instance.deep
    instance.deep = original
    assert instance.deep == original

@given(instance=sexec::SaveHistory_strategy)
@settings(max_examples=50)
def test_sexec::savehistory_instantiation(instance):
    assert isinstance(instance, sexec::SaveHistory)

@given(instance=sexec::SaveHistory_strategy)
def test_sexec::savehistory_deep_type(instance):
    assert isinstance(instance.deep, bool)


@given(instance=sexec::SaveHistory_strategy)
def test_sexec::savehistory_deep_setter(instance):
    original = instance.deep
    instance.deep = original
    assert instance.deep == original

@given(instance=sexec::ExecutionChoice_strategy)
@settings(max_examples=50)
def test_sexec::executionchoice_instantiation(instance):
    assert isinstance(instance, sexec::ExecutionChoice)

@given(instance=sexec::ExecutionExit_strategy)
@settings(max_examples=50)
def test_sexec::executionexit_instantiation(instance):
    assert isinstance(instance, sexec::ExecutionExit)

@given(instance=sexec::ExecutionEntry_strategy)
@settings(max_examples=50)
def test_sexec::executionentry_instantiation(instance):
    assert isinstance(instance, sexec::ExecutionEntry)

@given(instance=sexec::UnscheduleTimeEvent_strategy)
@settings(max_examples=50)
def test_sexec::unscheduletimeevent_instantiation(instance):
    assert isinstance(instance, sexec::UnscheduleTimeEvent)

@given(instance=sexec::ScheduleTimeEvent_strategy)
@settings(max_examples=50)
def test_sexec::scheduletimeevent_instantiation(instance):
    assert isinstance(instance, sexec::ScheduleTimeEvent)
