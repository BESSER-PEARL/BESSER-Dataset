import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Guard,
    tfsm_EvaluateGuard,
    tfsm_EventGuard,
    tfsm_TemporalGuard,
    tfsm_NamedElement,
    NamedElement,
    tfsm_FSMEvent,
    tfsm_Transition,
    tfsm_FSMClock,
    tfsm_State,
    tfsm_TimedSystem,
    tfsm_TFSM,
    tfsm_Guard,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_guard_is_not_abstract():
    assert not inspect.isabstract(Guard)


def test_guard_constructor_exists():
    assert callable(Guard.__init__)


def test_guard_constructor_args():
    sig = inspect.signature(Guard.__init__)
    params = list(sig.parameters.keys())



def test_tfsm_evaluateguard_is_not_abstract():
    assert not inspect.isabstract(tfsm_EvaluateGuard)


def test_tfsm_evaluateguard_constructor_exists():
    assert callable(tfsm_EvaluateGuard.__init__)


def test_tfsm_evaluateguard_constructor_args():
    sig = inspect.signature(tfsm_EvaluateGuard.__init__)
    params = list(sig.parameters.keys())
    assert "condition" in params, "Missing parameter 'condition'"

def test_tfsm_evaluateguard_has_condition():
    assert hasattr(tfsm_EvaluateGuard, "condition")
    descriptor = None
    for klass in tfsm_EvaluateGuard.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)



def test_tfsm_eventguard_is_not_abstract():
    assert not inspect.isabstract(tfsm_EventGuard)


def test_tfsm_eventguard_constructor_exists():
    assert callable(tfsm_EventGuard.__init__)


def test_tfsm_eventguard_constructor_args():
    sig = inspect.signature(tfsm_EventGuard.__init__)
    params = list(sig.parameters.keys())



def test_tfsm_temporalguard_is_not_abstract():
    assert not inspect.isabstract(tfsm_TemporalGuard)


def test_tfsm_temporalguard_constructor_exists():
    assert callable(tfsm_TemporalGuard.__init__)


def test_tfsm_temporalguard_constructor_args():
    sig = inspect.signature(tfsm_TemporalGuard.__init__)
    params = list(sig.parameters.keys())
    assert "afterDuration" in params, "Missing parameter 'afterDuration'"

def test_tfsm_temporalguard_has_afterDuration():
    assert hasattr(tfsm_TemporalGuard, "afterDuration")
    descriptor = None
    for klass in tfsm_TemporalGuard.__mro__:
        if "afterDuration" in klass.__dict__:
            descriptor = klass.__dict__["afterDuration"]
            break
    assert isinstance(descriptor, property)



def test_tfsm_namedelement_is_not_abstract():
    assert not inspect.isabstract(tfsm_NamedElement)


def test_tfsm_namedelement_constructor_exists():
    assert callable(tfsm_NamedElement.__init__)


def test_tfsm_namedelement_constructor_args():
    sig = inspect.signature(tfsm_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tfsm_namedelement_has_name():
    assert hasattr(tfsm_NamedElement, "name")
    descriptor = None
    for klass in tfsm_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_tfsm_fsmevent_is_not_abstract():
    assert not inspect.isabstract(tfsm_FSMEvent)


def test_tfsm_fsmevent_constructor_exists():
    assert callable(tfsm_FSMEvent.__init__)


def test_tfsm_fsmevent_constructor_args():
    sig = inspect.signature(tfsm_FSMEvent.__init__)
    params = list(sig.parameters.keys())



def test_tfsm_transition_is_not_abstract():
    assert not inspect.isabstract(tfsm_Transition)


def test_tfsm_transition_constructor_exists():
    assert callable(tfsm_Transition.__init__)


def test_tfsm_transition_constructor_args():
    sig = inspect.signature(tfsm_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"

def test_tfsm_transition_has_action():
    assert hasattr(tfsm_Transition, "action")
    descriptor = None
    for klass in tfsm_Transition.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)



def test_tfsm_fsmclock_is_not_abstract():
    assert not inspect.isabstract(tfsm_FSMClock)


def test_tfsm_fsmclock_constructor_exists():
    assert callable(tfsm_FSMClock.__init__)


def test_tfsm_fsmclock_constructor_args():
    sig = inspect.signature(tfsm_FSMClock.__init__)
    params = list(sig.parameters.keys())



def test_tfsm_state_is_not_abstract():
    assert not inspect.isabstract(tfsm_State)


def test_tfsm_state_constructor_exists():
    assert callable(tfsm_State.__init__)


def test_tfsm_state_constructor_args():
    sig = inspect.signature(tfsm_State.__init__)
    params = list(sig.parameters.keys())



def test_tfsm_timedsystem_is_not_abstract():
    assert not inspect.isabstract(tfsm_TimedSystem)


def test_tfsm_timedsystem_constructor_exists():
    assert callable(tfsm_TimedSystem.__init__)


def test_tfsm_timedsystem_constructor_args():
    sig = inspect.signature(tfsm_TimedSystem.__init__)
    params = list(sig.parameters.keys())



def test_tfsm_tfsm_is_not_abstract():
    assert not inspect.isabstract(tfsm_TFSM)


def test_tfsm_tfsm_constructor_exists():
    assert callable(tfsm_TFSM.__init__)


def test_tfsm_tfsm_constructor_args():
    sig = inspect.signature(tfsm_TFSM.__init__)
    params = list(sig.parameters.keys())



def test_tfsm_guard_is_not_abstract():
    assert not inspect.isabstract(tfsm_Guard)


def test_tfsm_guard_constructor_exists():
    assert callable(tfsm_Guard.__init__)


def test_tfsm_guard_constructor_args():
    sig = inspect.signature(tfsm_Guard.__init__)
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
Guard_strategy = st.builds(
    Guard,
)
tfsm_EvaluateGuard_strategy = st.builds(
    tfsm_EvaluateGuard,
    condition=
        safe_text
)
tfsm_EventGuard_strategy = st.builds(
    tfsm_EventGuard,
)
tfsm_TemporalGuard_strategy = st.builds(
    tfsm_TemporalGuard,
    afterDuration=
        st.integers()
)
tfsm_NamedElement_strategy = st.builds(
    tfsm_NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
tfsm_FSMEvent_strategy = st.builds(
    tfsm_FSMEvent,
)
tfsm_Transition_strategy = st.builds(
    tfsm_Transition,
    action=
        safe_text
)
tfsm_FSMClock_strategy = st.builds(
    tfsm_FSMClock,
)
tfsm_State_strategy = st.builds(
    tfsm_State,
)
tfsm_TimedSystem_strategy = st.builds(
    tfsm_TimedSystem,
)
tfsm_TFSM_strategy = st.builds(
    tfsm_TFSM,
)
tfsm_Guard_strategy = st.builds(
    tfsm_Guard,
)

@given(instance=Guard_strategy)
@settings(max_examples=50)
def test_guard_instantiation(instance):
    assert isinstance(instance, Guard)

@given(instance=tfsm_EvaluateGuard_strategy)
@settings(max_examples=50)
def test_tfsm_evaluateguard_instantiation(instance):
    assert isinstance(instance, tfsm_EvaluateGuard)



@given(instance=tfsm_EvaluateGuard_strategy)
def test_tfsm_evaluateguard_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=tfsm_EventGuard_strategy)
@settings(max_examples=50)
def test_tfsm_eventguard_instantiation(instance):
    assert isinstance(instance, tfsm_EventGuard)

@given(instance=tfsm_TemporalGuard_strategy)
@settings(max_examples=50)
def test_tfsm_temporalguard_instantiation(instance):
    assert isinstance(instance, tfsm_TemporalGuard)



@given(instance=tfsm_TemporalGuard_strategy)
def test_tfsm_temporalguard_afterDuration_setter(instance):
    original = instance.afterDuration
    instance.afterDuration = original
    assert instance.afterDuration == original

@given(instance=tfsm_NamedElement_strategy)
@settings(max_examples=50)
def test_tfsm_namedelement_instantiation(instance):
    assert isinstance(instance, tfsm_NamedElement)



@given(instance=tfsm_NamedElement_strategy)
def test_tfsm_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=tfsm_FSMEvent_strategy)
@settings(max_examples=50)
def test_tfsm_fsmevent_instantiation(instance):
    assert isinstance(instance, tfsm_FSMEvent)

@given(instance=tfsm_Transition_strategy)
@settings(max_examples=50)
def test_tfsm_transition_instantiation(instance):
    assert isinstance(instance, tfsm_Transition)



@given(instance=tfsm_Transition_strategy)
def test_tfsm_transition_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=tfsm_FSMClock_strategy)
@settings(max_examples=50)
def test_tfsm_fsmclock_instantiation(instance):
    assert isinstance(instance, tfsm_FSMClock)

@given(instance=tfsm_State_strategy)
@settings(max_examples=50)
def test_tfsm_state_instantiation(instance):
    assert isinstance(instance, tfsm_State)

@given(instance=tfsm_TimedSystem_strategy)
@settings(max_examples=50)
def test_tfsm_timedsystem_instantiation(instance):
    assert isinstance(instance, tfsm_TimedSystem)

@given(instance=tfsm_TFSM_strategy)
@settings(max_examples=50)
def test_tfsm_tfsm_instantiation(instance):
    assert isinstance(instance, tfsm_TFSM)

@given(instance=tfsm_Guard_strategy)
@settings(max_examples=50)
def test_tfsm_guard_instantiation(instance):
    assert isinstance(instance, tfsm_Guard)
