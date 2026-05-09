import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Guard,
    tfsm::EventGuard,
    tfsm::EvaluateGuard,
    tfsm::TemporalGuard,
    tfsm::NamedElement,
    NamedElement,
    tfsm::Transition,
    tfsm::FSMEvent,
    tfsm::State,
    tfsm::FSMClock,
    tfsm::TimedSystem,
    tfsm::TFSM,
    tfsm::Guard,
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



def test_tfsm::eventguard_is_not_abstract():
    assert not inspect.isabstract(tfsm::EventGuard)


def test_tfsm::eventguard_constructor_exists():
    assert callable(tfsm::EventGuard.__init__)


def test_tfsm::eventguard_constructor_args():
    sig = inspect.signature(tfsm::EventGuard.__init__)
    params = list(sig.parameters.keys())



def test_tfsm::evaluateguard_is_not_abstract():
    assert not inspect.isabstract(tfsm::EvaluateGuard)


def test_tfsm::evaluateguard_constructor_exists():
    assert callable(tfsm::EvaluateGuard.__init__)


def test_tfsm::evaluateguard_constructor_args():
    sig = inspect.signature(tfsm::EvaluateGuard.__init__)
    params = list(sig.parameters.keys())
    assert "condition" in params, "Missing parameter 'condition'"

def test_tfsm::evaluateguard_has_condition():
    assert hasattr(tfsm::EvaluateGuard, "condition")
    descriptor = None
    for klass in tfsm::EvaluateGuard.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)



def test_tfsm::temporalguard_is_not_abstract():
    assert not inspect.isabstract(tfsm::TemporalGuard)


def test_tfsm::temporalguard_constructor_exists():
    assert callable(tfsm::TemporalGuard.__init__)


def test_tfsm::temporalguard_constructor_args():
    sig = inspect.signature(tfsm::TemporalGuard.__init__)
    params = list(sig.parameters.keys())
    assert "afterDuration" in params, "Missing parameter 'afterDuration'"

def test_tfsm::temporalguard_has_afterDuration():
    assert hasattr(tfsm::TemporalGuard, "afterDuration")
    descriptor = None
    for klass in tfsm::TemporalGuard.__mro__:
        if "afterDuration" in klass.__dict__:
            descriptor = klass.__dict__["afterDuration"]
            break
    assert isinstance(descriptor, property)



def test_tfsm::namedelement_is_not_abstract():
    assert not inspect.isabstract(tfsm::NamedElement)


def test_tfsm::namedelement_constructor_exists():
    assert callable(tfsm::NamedElement.__init__)


def test_tfsm::namedelement_constructor_args():
    sig = inspect.signature(tfsm::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tfsm::namedelement_has_name():
    assert hasattr(tfsm::NamedElement, "name")
    descriptor = None
    for klass in tfsm::NamedElement.__mro__:
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



def test_tfsm::transition_is_not_abstract():
    assert not inspect.isabstract(tfsm::Transition)


def test_tfsm::transition_constructor_exists():
    assert callable(tfsm::Transition.__init__)


def test_tfsm::transition_constructor_args():
    sig = inspect.signature(tfsm::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"

def test_tfsm::transition_has_action():
    assert hasattr(tfsm::Transition, "action")
    descriptor = None
    for klass in tfsm::Transition.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)



def test_tfsm::fsmevent_is_not_abstract():
    assert not inspect.isabstract(tfsm::FSMEvent)


def test_tfsm::fsmevent_constructor_exists():
    assert callable(tfsm::FSMEvent.__init__)


def test_tfsm::fsmevent_constructor_args():
    sig = inspect.signature(tfsm::FSMEvent.__init__)
    params = list(sig.parameters.keys())



def test_tfsm::state_is_not_abstract():
    assert not inspect.isabstract(tfsm::State)


def test_tfsm::state_constructor_exists():
    assert callable(tfsm::State.__init__)


def test_tfsm::state_constructor_args():
    sig = inspect.signature(tfsm::State.__init__)
    params = list(sig.parameters.keys())



def test_tfsm::fsmclock_is_not_abstract():
    assert not inspect.isabstract(tfsm::FSMClock)


def test_tfsm::fsmclock_constructor_exists():
    assert callable(tfsm::FSMClock.__init__)


def test_tfsm::fsmclock_constructor_args():
    sig = inspect.signature(tfsm::FSMClock.__init__)
    params = list(sig.parameters.keys())



def test_tfsm::timedsystem_is_not_abstract():
    assert not inspect.isabstract(tfsm::TimedSystem)


def test_tfsm::timedsystem_constructor_exists():
    assert callable(tfsm::TimedSystem.__init__)


def test_tfsm::timedsystem_constructor_args():
    sig = inspect.signature(tfsm::TimedSystem.__init__)
    params = list(sig.parameters.keys())



def test_tfsm::tfsm_is_not_abstract():
    assert not inspect.isabstract(tfsm::TFSM)


def test_tfsm::tfsm_constructor_exists():
    assert callable(tfsm::TFSM.__init__)


def test_tfsm::tfsm_constructor_args():
    sig = inspect.signature(tfsm::TFSM.__init__)
    params = list(sig.parameters.keys())



def test_tfsm::guard_is_not_abstract():
    assert not inspect.isabstract(tfsm::Guard)


def test_tfsm::guard_constructor_exists():
    assert callable(tfsm::Guard.__init__)


def test_tfsm::guard_constructor_args():
    sig = inspect.signature(tfsm::Guard.__init__)
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
tfsm::EventGuard_strategy = st.builds(
    tfsm::EventGuard,
)
tfsm::EvaluateGuard_strategy = st.builds(
    tfsm::EvaluateGuard,
    condition=
        safe_text
)
tfsm::TemporalGuard_strategy = st.builds(
    tfsm::TemporalGuard,
    afterDuration=
        st.integers()
)
tfsm::NamedElement_strategy = st.builds(
    tfsm::NamedElement,
    name=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
tfsm::Transition_strategy = st.builds(
    tfsm::Transition,
    action=
        safe_text
)
tfsm::FSMEvent_strategy = st.builds(
    tfsm::FSMEvent,
)
tfsm::State_strategy = st.builds(
    tfsm::State,
)
tfsm::FSMClock_strategy = st.builds(
    tfsm::FSMClock,
)
tfsm::TimedSystem_strategy = st.builds(
    tfsm::TimedSystem,
)
tfsm::TFSM_strategy = st.builds(
    tfsm::TFSM,
)
tfsm::Guard_strategy = st.builds(
    tfsm::Guard,
)

@given(instance=Guard_strategy)
@settings(max_examples=50)
def test_guard_instantiation(instance):
    assert isinstance(instance, Guard)

@given(instance=tfsm::EventGuard_strategy)
@settings(max_examples=50)
def test_tfsm::eventguard_instantiation(instance):
    assert isinstance(instance, tfsm::EventGuard)

@given(instance=tfsm::EvaluateGuard_strategy)
@settings(max_examples=50)
def test_tfsm::evaluateguard_instantiation(instance):
    assert isinstance(instance, tfsm::EvaluateGuard)

@given(instance=tfsm::EvaluateGuard_strategy)
def test_tfsm::evaluateguard_condition_type(instance):
    assert isinstance(instance.condition, str)


@given(instance=tfsm::EvaluateGuard_strategy)
def test_tfsm::evaluateguard_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=tfsm::TemporalGuard_strategy)
@settings(max_examples=50)
def test_tfsm::temporalguard_instantiation(instance):
    assert isinstance(instance, tfsm::TemporalGuard)

@given(instance=tfsm::TemporalGuard_strategy)
def test_tfsm::temporalguard_afterDuration_type(instance):
    assert isinstance(instance.afterDuration, int)


@given(instance=tfsm::TemporalGuard_strategy)
def test_tfsm::temporalguard_afterDuration_setter(instance):
    original = instance.afterDuration
    instance.afterDuration = original
    assert instance.afterDuration == original

@given(instance=tfsm::NamedElement_strategy)
@settings(max_examples=50)
def test_tfsm::namedelement_instantiation(instance):
    assert isinstance(instance, tfsm::NamedElement)

@given(instance=tfsm::NamedElement_strategy)
def test_tfsm::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tfsm::NamedElement_strategy)
def test_tfsm::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=tfsm::Transition_strategy)
@settings(max_examples=50)
def test_tfsm::transition_instantiation(instance):
    assert isinstance(instance, tfsm::Transition)

@given(instance=tfsm::Transition_strategy)
def test_tfsm::transition_action_type(instance):
    assert isinstance(instance.action, str)


@given(instance=tfsm::Transition_strategy)
def test_tfsm::transition_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=tfsm::FSMEvent_strategy)
@settings(max_examples=50)
def test_tfsm::fsmevent_instantiation(instance):
    assert isinstance(instance, tfsm::FSMEvent)

@given(instance=tfsm::State_strategy)
@settings(max_examples=50)
def test_tfsm::state_instantiation(instance):
    assert isinstance(instance, tfsm::State)

@given(instance=tfsm::FSMClock_strategy)
@settings(max_examples=50)
def test_tfsm::fsmclock_instantiation(instance):
    assert isinstance(instance, tfsm::FSMClock)

@given(instance=tfsm::TimedSystem_strategy)
@settings(max_examples=50)
def test_tfsm::timedsystem_instantiation(instance):
    assert isinstance(instance, tfsm::TimedSystem)

@given(instance=tfsm::TFSM_strategy)
@settings(max_examples=50)
def test_tfsm::tfsm_instantiation(instance):
    assert isinstance(instance, tfsm::TFSM)

@given(instance=tfsm::Guard_strategy)
@settings(max_examples=50)
def test_tfsm::guard_instantiation(instance):
    assert isinstance(instance, tfsm::Guard)
