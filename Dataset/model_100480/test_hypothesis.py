import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    tfsm_plaink3_NamedElement,
    Guard,
    tfsm_plaink3_EvaluateGuard,
    tfsm_plaink3_EventGuard,
    tfsm_plaink3_TemporalGuard,
    NamedElement,
    tfsm_plaink3_TimedSystem,
    tfsm_plaink3_Guard,
    tfsm_plaink3_Transition,
    tfsm_plaink3_FSMClock,
    tfsm_plaink3_FSMEvent,
    tfsm_plaink3_State,
    tfsm_plaink3_TFSM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tfsm_plaink3_namedelement_is_not_abstract():
    assert not inspect.isabstract(tfsm_plaink3_NamedElement)


def test_tfsm_plaink3_namedelement_constructor_exists():
    assert callable(tfsm_plaink3_NamedElement.__init__)


def test_tfsm_plaink3_namedelement_constructor_args():
    sig = inspect.signature(tfsm_plaink3_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tfsm_plaink3_namedelement_has_name():
    assert hasattr(tfsm_plaink3_NamedElement, "name")
    descriptor = None
    for klass in tfsm_plaink3_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_guard_is_not_abstract():
    assert not inspect.isabstract(Guard)


def test_guard_constructor_exists():
    assert callable(Guard.__init__)


def test_guard_constructor_args():
    sig = inspect.signature(Guard.__init__)
    params = list(sig.parameters.keys())



def test_tfsm_plaink3_evaluateguard_is_not_abstract():
    assert not inspect.isabstract(tfsm_plaink3_EvaluateGuard)


def test_tfsm_plaink3_evaluateguard_constructor_exists():
    assert callable(tfsm_plaink3_EvaluateGuard.__init__)


def test_tfsm_plaink3_evaluateguard_constructor_args():
    sig = inspect.signature(tfsm_plaink3_EvaluateGuard.__init__)
    params = list(sig.parameters.keys())
    assert "condition" in params, "Missing parameter 'condition'"

def test_tfsm_plaink3_evaluateguard_has_condition():
    assert hasattr(tfsm_plaink3_EvaluateGuard, "condition")
    descriptor = None
    for klass in tfsm_plaink3_EvaluateGuard.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)



def test_tfsm_plaink3_eventguard_is_not_abstract():
    assert not inspect.isabstract(tfsm_plaink3_EventGuard)


def test_tfsm_plaink3_eventguard_constructor_exists():
    assert callable(tfsm_plaink3_EventGuard.__init__)


def test_tfsm_plaink3_eventguard_constructor_args():
    sig = inspect.signature(tfsm_plaink3_EventGuard.__init__)
    params = list(sig.parameters.keys())



def test_tfsm_plaink3_temporalguard_is_not_abstract():
    assert not inspect.isabstract(tfsm_plaink3_TemporalGuard)


def test_tfsm_plaink3_temporalguard_constructor_exists():
    assert callable(tfsm_plaink3_TemporalGuard.__init__)


def test_tfsm_plaink3_temporalguard_constructor_args():
    sig = inspect.signature(tfsm_plaink3_TemporalGuard.__init__)
    params = list(sig.parameters.keys())
    assert "afterDuration" in params, "Missing parameter 'afterDuration'"

def test_tfsm_plaink3_temporalguard_has_afterDuration():
    assert hasattr(tfsm_plaink3_TemporalGuard, "afterDuration")
    descriptor = None
    for klass in tfsm_plaink3_TemporalGuard.__mro__:
        if "afterDuration" in klass.__dict__:
            descriptor = klass.__dict__["afterDuration"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_tfsm_plaink3_timedsystem_is_not_abstract():
    assert not inspect.isabstract(tfsm_plaink3_TimedSystem)


def test_tfsm_plaink3_timedsystem_constructor_exists():
    assert callable(tfsm_plaink3_TimedSystem.__init__)


def test_tfsm_plaink3_timedsystem_constructor_args():
    sig = inspect.signature(tfsm_plaink3_TimedSystem.__init__)
    params = list(sig.parameters.keys())



def test_tfsm_plaink3_guard_is_not_abstract():
    assert not inspect.isabstract(tfsm_plaink3_Guard)


def test_tfsm_plaink3_guard_constructor_exists():
    assert callable(tfsm_plaink3_Guard.__init__)


def test_tfsm_plaink3_guard_constructor_args():
    sig = inspect.signature(tfsm_plaink3_Guard.__init__)
    params = list(sig.parameters.keys())



def test_tfsm_plaink3_transition_is_not_abstract():
    assert not inspect.isabstract(tfsm_plaink3_Transition)


def test_tfsm_plaink3_transition_constructor_exists():
    assert callable(tfsm_plaink3_Transition.__init__)


def test_tfsm_plaink3_transition_constructor_args():
    sig = inspect.signature(tfsm_plaink3_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"

def test_tfsm_plaink3_transition_has_action():
    assert hasattr(tfsm_plaink3_Transition, "action")
    descriptor = None
    for klass in tfsm_plaink3_Transition.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)



def test_tfsm_plaink3_fsmclock_is_not_abstract():
    assert not inspect.isabstract(tfsm_plaink3_FSMClock)


def test_tfsm_plaink3_fsmclock_constructor_exists():
    assert callable(tfsm_plaink3_FSMClock.__init__)


def test_tfsm_plaink3_fsmclock_constructor_args():
    sig = inspect.signature(tfsm_plaink3_FSMClock.__init__)
    params = list(sig.parameters.keys())
    assert "numberOfTicks" in params, "Missing parameter 'numberOfTicks'"

def test_tfsm_plaink3_fsmclock_has_numberOfTicks():
    assert hasattr(tfsm_plaink3_FSMClock, "numberOfTicks")
    descriptor = None
    for klass in tfsm_plaink3_FSMClock.__mro__:
        if "numberOfTicks" in klass.__dict__:
            descriptor = klass.__dict__["numberOfTicks"]
            break
    assert isinstance(descriptor, property)



def test_tfsm_plaink3_fsmevent_is_not_abstract():
    assert not inspect.isabstract(tfsm_plaink3_FSMEvent)


def test_tfsm_plaink3_fsmevent_constructor_exists():
    assert callable(tfsm_plaink3_FSMEvent.__init__)


def test_tfsm_plaink3_fsmevent_constructor_args():
    sig = inspect.signature(tfsm_plaink3_FSMEvent.__init__)
    params = list(sig.parameters.keys())
    assert "isTriggered" in params, "Missing parameter 'isTriggered'"

def test_tfsm_plaink3_fsmevent_has_isTriggered():
    assert hasattr(tfsm_plaink3_FSMEvent, "isTriggered")
    descriptor = None
    for klass in tfsm_plaink3_FSMEvent.__mro__:
        if "isTriggered" in klass.__dict__:
            descriptor = klass.__dict__["isTriggered"]
            break
    assert isinstance(descriptor, property)



def test_tfsm_plaink3_state_is_not_abstract():
    assert not inspect.isabstract(tfsm_plaink3_State)


def test_tfsm_plaink3_state_constructor_exists():
    assert callable(tfsm_plaink3_State.__init__)


def test_tfsm_plaink3_state_constructor_args():
    sig = inspect.signature(tfsm_plaink3_State.__init__)
    params = list(sig.parameters.keys())



def test_tfsm_plaink3_tfsm_is_not_abstract():
    assert not inspect.isabstract(tfsm_plaink3_TFSM)


def test_tfsm_plaink3_tfsm_constructor_exists():
    assert callable(tfsm_plaink3_TFSM.__init__)


def test_tfsm_plaink3_tfsm_constructor_args():
    sig = inspect.signature(tfsm_plaink3_TFSM.__init__)
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
tfsm_plaink3_NamedElement_strategy = st.builds(
    tfsm_plaink3_NamedElement,
    name=
        safe_text
)
Guard_strategy = st.builds(
    Guard,
)
tfsm_plaink3_EvaluateGuard_strategy = st.builds(
    tfsm_plaink3_EvaluateGuard,
    condition=
        safe_text
)
tfsm_plaink3_EventGuard_strategy = st.builds(
    tfsm_plaink3_EventGuard,
)
tfsm_plaink3_TemporalGuard_strategy = st.builds(
    tfsm_plaink3_TemporalGuard,
    afterDuration=
        st.integers()
)
NamedElement_strategy = st.builds(
    NamedElement,
)
tfsm_plaink3_TimedSystem_strategy = st.builds(
    tfsm_plaink3_TimedSystem,
)
tfsm_plaink3_Guard_strategy = st.builds(
    tfsm_plaink3_Guard,
)
tfsm_plaink3_Transition_strategy = st.builds(
    tfsm_plaink3_Transition,
    action=
        safe_text
)
tfsm_plaink3_FSMClock_strategy = st.builds(
    tfsm_plaink3_FSMClock,
    numberOfTicks=
        safe_text
)
tfsm_plaink3_FSMEvent_strategy = st.builds(
    tfsm_plaink3_FSMEvent,
    isTriggered=
        st.booleans()
)
tfsm_plaink3_State_strategy = st.builds(
    tfsm_plaink3_State,
)
tfsm_plaink3_TFSM_strategy = st.builds(
    tfsm_plaink3_TFSM,
)

@given(instance=tfsm_plaink3_NamedElement_strategy)
@settings(max_examples=50)
def test_tfsm_plaink3_namedelement_instantiation(instance):
    assert isinstance(instance, tfsm_plaink3_NamedElement)



@given(instance=tfsm_plaink3_NamedElement_strategy)
def test_tfsm_plaink3_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Guard_strategy)
@settings(max_examples=50)
def test_guard_instantiation(instance):
    assert isinstance(instance, Guard)

@given(instance=tfsm_plaink3_EvaluateGuard_strategy)
@settings(max_examples=50)
def test_tfsm_plaink3_evaluateguard_instantiation(instance):
    assert isinstance(instance, tfsm_plaink3_EvaluateGuard)



@given(instance=tfsm_plaink3_EvaluateGuard_strategy)
def test_tfsm_plaink3_evaluateguard_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=tfsm_plaink3_EventGuard_strategy)
@settings(max_examples=50)
def test_tfsm_plaink3_eventguard_instantiation(instance):
    assert isinstance(instance, tfsm_plaink3_EventGuard)

@given(instance=tfsm_plaink3_TemporalGuard_strategy)
@settings(max_examples=50)
def test_tfsm_plaink3_temporalguard_instantiation(instance):
    assert isinstance(instance, tfsm_plaink3_TemporalGuard)



@given(instance=tfsm_plaink3_TemporalGuard_strategy)
def test_tfsm_plaink3_temporalguard_afterDuration_setter(instance):
    original = instance.afterDuration
    instance.afterDuration = original
    assert instance.afterDuration == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=tfsm_plaink3_TimedSystem_strategy)
@settings(max_examples=50)
def test_tfsm_plaink3_timedsystem_instantiation(instance):
    assert isinstance(instance, tfsm_plaink3_TimedSystem)

@given(instance=tfsm_plaink3_Guard_strategy)
@settings(max_examples=50)
def test_tfsm_plaink3_guard_instantiation(instance):
    assert isinstance(instance, tfsm_plaink3_Guard)

@given(instance=tfsm_plaink3_Transition_strategy)
@settings(max_examples=50)
def test_tfsm_plaink3_transition_instantiation(instance):
    assert isinstance(instance, tfsm_plaink3_Transition)



@given(instance=tfsm_plaink3_Transition_strategy)
def test_tfsm_plaink3_transition_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=tfsm_plaink3_FSMClock_strategy)
@settings(max_examples=50)
def test_tfsm_plaink3_fsmclock_instantiation(instance):
    assert isinstance(instance, tfsm_plaink3_FSMClock)



@given(instance=tfsm_plaink3_FSMClock_strategy)
def test_tfsm_plaink3_fsmclock_numberOfTicks_setter(instance):
    original = instance.numberOfTicks
    instance.numberOfTicks = original
    assert instance.numberOfTicks == original

@given(instance=tfsm_plaink3_FSMEvent_strategy)
@settings(max_examples=50)
def test_tfsm_plaink3_fsmevent_instantiation(instance):
    assert isinstance(instance, tfsm_plaink3_FSMEvent)



@given(instance=tfsm_plaink3_FSMEvent_strategy)
def test_tfsm_plaink3_fsmevent_isTriggered_setter(instance):
    original = instance.isTriggered
    instance.isTriggered = original
    assert instance.isTriggered == original

@given(instance=tfsm_plaink3_State_strategy)
@settings(max_examples=50)
def test_tfsm_plaink3_state_instantiation(instance):
    assert isinstance(instance, tfsm_plaink3_State)

@given(instance=tfsm_plaink3_TFSM_strategy)
@settings(max_examples=50)
def test_tfsm_plaink3_tfsm_instantiation(instance):
    assert isinstance(instance, tfsm_plaink3_TFSM)
