import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    tfsm::plaink3::NamedElement,
    Guard,
    tfsm::plaink3::EventGuard,
    tfsm::plaink3::EvaluateGuard,
    tfsm::plaink3::TemporalGuard,
    NamedElement,
    tfsm::plaink3::Transition,
    tfsm::plaink3::State,
    tfsm::plaink3::FSMClock,
    tfsm::plaink3::TimedSystem,
    tfsm::plaink3::Guard,
    tfsm::plaink3::FSMEvent,
    tfsm::plaink3::TFSM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tfsm::plaink3::namedelement_is_not_abstract():
    assert not inspect.isabstract(tfsm::plaink3::NamedElement)


def test_tfsm::plaink3::namedelement_constructor_exists():
    assert callable(tfsm::plaink3::NamedElement.__init__)


def test_tfsm::plaink3::namedelement_constructor_args():
    sig = inspect.signature(tfsm::plaink3::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tfsm::plaink3::namedelement_has_name():
    assert hasattr(tfsm::plaink3::NamedElement, "name")
    descriptor = None
    for klass in tfsm::plaink3::NamedElement.__mro__:
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



def test_tfsm::plaink3::eventguard_is_not_abstract():
    assert not inspect.isabstract(tfsm::plaink3::EventGuard)


def test_tfsm::plaink3::eventguard_constructor_exists():
    assert callable(tfsm::plaink3::EventGuard.__init__)


def test_tfsm::plaink3::eventguard_constructor_args():
    sig = inspect.signature(tfsm::plaink3::EventGuard.__init__)
    params = list(sig.parameters.keys())



def test_tfsm::plaink3::evaluateguard_is_not_abstract():
    assert not inspect.isabstract(tfsm::plaink3::EvaluateGuard)


def test_tfsm::plaink3::evaluateguard_constructor_exists():
    assert callable(tfsm::plaink3::EvaluateGuard.__init__)


def test_tfsm::plaink3::evaluateguard_constructor_args():
    sig = inspect.signature(tfsm::plaink3::EvaluateGuard.__init__)
    params = list(sig.parameters.keys())
    assert "condition" in params, "Missing parameter 'condition'"

def test_tfsm::plaink3::evaluateguard_has_condition():
    assert hasattr(tfsm::plaink3::EvaluateGuard, "condition")
    descriptor = None
    for klass in tfsm::plaink3::EvaluateGuard.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)



def test_tfsm::plaink3::temporalguard_is_not_abstract():
    assert not inspect.isabstract(tfsm::plaink3::TemporalGuard)


def test_tfsm::plaink3::temporalguard_constructor_exists():
    assert callable(tfsm::plaink3::TemporalGuard.__init__)


def test_tfsm::plaink3::temporalguard_constructor_args():
    sig = inspect.signature(tfsm::plaink3::TemporalGuard.__init__)
    params = list(sig.parameters.keys())
    assert "afterDuration" in params, "Missing parameter 'afterDuration'"

def test_tfsm::plaink3::temporalguard_has_afterDuration():
    assert hasattr(tfsm::plaink3::TemporalGuard, "afterDuration")
    descriptor = None
    for klass in tfsm::plaink3::TemporalGuard.__mro__:
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



def test_tfsm::plaink3::transition_is_not_abstract():
    assert not inspect.isabstract(tfsm::plaink3::Transition)


def test_tfsm::plaink3::transition_constructor_exists():
    assert callable(tfsm::plaink3::Transition.__init__)


def test_tfsm::plaink3::transition_constructor_args():
    sig = inspect.signature(tfsm::plaink3::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"

def test_tfsm::plaink3::transition_has_action():
    assert hasattr(tfsm::plaink3::Transition, "action")
    descriptor = None
    for klass in tfsm::plaink3::Transition.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)



def test_tfsm::plaink3::state_is_not_abstract():
    assert not inspect.isabstract(tfsm::plaink3::State)


def test_tfsm::plaink3::state_constructor_exists():
    assert callable(tfsm::plaink3::State.__init__)


def test_tfsm::plaink3::state_constructor_args():
    sig = inspect.signature(tfsm::plaink3::State.__init__)
    params = list(sig.parameters.keys())



def test_tfsm::plaink3::fsmclock_is_not_abstract():
    assert not inspect.isabstract(tfsm::plaink3::FSMClock)


def test_tfsm::plaink3::fsmclock_constructor_exists():
    assert callable(tfsm::plaink3::FSMClock.__init__)


def test_tfsm::plaink3::fsmclock_constructor_args():
    sig = inspect.signature(tfsm::plaink3::FSMClock.__init__)
    params = list(sig.parameters.keys())
    assert "numberOfTicks" in params, "Missing parameter 'numberOfTicks'"

def test_tfsm::plaink3::fsmclock_has_numberOfTicks():
    assert hasattr(tfsm::plaink3::FSMClock, "numberOfTicks")
    descriptor = None
    for klass in tfsm::plaink3::FSMClock.__mro__:
        if "numberOfTicks" in klass.__dict__:
            descriptor = klass.__dict__["numberOfTicks"]
            break
    assert isinstance(descriptor, property)



def test_tfsm::plaink3::timedsystem_is_not_abstract():
    assert not inspect.isabstract(tfsm::plaink3::TimedSystem)


def test_tfsm::plaink3::timedsystem_constructor_exists():
    assert callable(tfsm::plaink3::TimedSystem.__init__)


def test_tfsm::plaink3::timedsystem_constructor_args():
    sig = inspect.signature(tfsm::plaink3::TimedSystem.__init__)
    params = list(sig.parameters.keys())



def test_tfsm::plaink3::guard_is_not_abstract():
    assert not inspect.isabstract(tfsm::plaink3::Guard)


def test_tfsm::plaink3::guard_constructor_exists():
    assert callable(tfsm::plaink3::Guard.__init__)


def test_tfsm::plaink3::guard_constructor_args():
    sig = inspect.signature(tfsm::plaink3::Guard.__init__)
    params = list(sig.parameters.keys())



def test_tfsm::plaink3::fsmevent_is_not_abstract():
    assert not inspect.isabstract(tfsm::plaink3::FSMEvent)


def test_tfsm::plaink3::fsmevent_constructor_exists():
    assert callable(tfsm::plaink3::FSMEvent.__init__)


def test_tfsm::plaink3::fsmevent_constructor_args():
    sig = inspect.signature(tfsm::plaink3::FSMEvent.__init__)
    params = list(sig.parameters.keys())
    assert "isTriggered" in params, "Missing parameter 'isTriggered'"

def test_tfsm::plaink3::fsmevent_has_isTriggered():
    assert hasattr(tfsm::plaink3::FSMEvent, "isTriggered")
    descriptor = None
    for klass in tfsm::plaink3::FSMEvent.__mro__:
        if "isTriggered" in klass.__dict__:
            descriptor = klass.__dict__["isTriggered"]
            break
    assert isinstance(descriptor, property)



def test_tfsm::plaink3::tfsm_is_not_abstract():
    assert not inspect.isabstract(tfsm::plaink3::TFSM)


def test_tfsm::plaink3::tfsm_constructor_exists():
    assert callable(tfsm::plaink3::TFSM.__init__)


def test_tfsm::plaink3::tfsm_constructor_args():
    sig = inspect.signature(tfsm::plaink3::TFSM.__init__)
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
tfsm::plaink3::NamedElement_strategy = st.builds(
    tfsm::plaink3::NamedElement,
    name=
        safe_text
)
Guard_strategy = st.builds(
    Guard,
)
tfsm::plaink3::EventGuard_strategy = st.builds(
    tfsm::plaink3::EventGuard,
)
tfsm::plaink3::EvaluateGuard_strategy = st.builds(
    tfsm::plaink3::EvaluateGuard,
    condition=
        safe_text
)
tfsm::plaink3::TemporalGuard_strategy = st.builds(
    tfsm::plaink3::TemporalGuard,
    afterDuration=
        st.integers()
)
NamedElement_strategy = st.builds(
    NamedElement,
)
tfsm::plaink3::Transition_strategy = st.builds(
    tfsm::plaink3::Transition,
    action=
        safe_text
)
tfsm::plaink3::State_strategy = st.builds(
    tfsm::plaink3::State,
)
tfsm::plaink3::FSMClock_strategy = st.builds(
    tfsm::plaink3::FSMClock,
    numberOfTicks=
        safe_text
)
tfsm::plaink3::TimedSystem_strategy = st.builds(
    tfsm::plaink3::TimedSystem,
)
tfsm::plaink3::Guard_strategy = st.builds(
    tfsm::plaink3::Guard,
)
tfsm::plaink3::FSMEvent_strategy = st.builds(
    tfsm::plaink3::FSMEvent,
    isTriggered=
        st.booleans()
)
tfsm::plaink3::TFSM_strategy = st.builds(
    tfsm::plaink3::TFSM,
)

@given(instance=tfsm::plaink3::NamedElement_strategy)
@settings(max_examples=50)
def test_tfsm::plaink3::namedelement_instantiation(instance):
    assert isinstance(instance, tfsm::plaink3::NamedElement)

@given(instance=tfsm::plaink3::NamedElement_strategy)
def test_tfsm::plaink3::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tfsm::plaink3::NamedElement_strategy)
def test_tfsm::plaink3::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Guard_strategy)
@settings(max_examples=50)
def test_guard_instantiation(instance):
    assert isinstance(instance, Guard)

@given(instance=tfsm::plaink3::EventGuard_strategy)
@settings(max_examples=50)
def test_tfsm::plaink3::eventguard_instantiation(instance):
    assert isinstance(instance, tfsm::plaink3::EventGuard)

@given(instance=tfsm::plaink3::EvaluateGuard_strategy)
@settings(max_examples=50)
def test_tfsm::plaink3::evaluateguard_instantiation(instance):
    assert isinstance(instance, tfsm::plaink3::EvaluateGuard)

@given(instance=tfsm::plaink3::EvaluateGuard_strategy)
def test_tfsm::plaink3::evaluateguard_condition_type(instance):
    assert isinstance(instance.condition, str)


@given(instance=tfsm::plaink3::EvaluateGuard_strategy)
def test_tfsm::plaink3::evaluateguard_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=tfsm::plaink3::TemporalGuard_strategy)
@settings(max_examples=50)
def test_tfsm::plaink3::temporalguard_instantiation(instance):
    assert isinstance(instance, tfsm::plaink3::TemporalGuard)

@given(instance=tfsm::plaink3::TemporalGuard_strategy)
def test_tfsm::plaink3::temporalguard_afterDuration_type(instance):
    assert isinstance(instance.afterDuration, int)


@given(instance=tfsm::plaink3::TemporalGuard_strategy)
def test_tfsm::plaink3::temporalguard_afterDuration_setter(instance):
    original = instance.afterDuration
    instance.afterDuration = original
    assert instance.afterDuration == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=tfsm::plaink3::Transition_strategy)
@settings(max_examples=50)
def test_tfsm::plaink3::transition_instantiation(instance):
    assert isinstance(instance, tfsm::plaink3::Transition)

@given(instance=tfsm::plaink3::Transition_strategy)
def test_tfsm::plaink3::transition_action_type(instance):
    assert isinstance(instance.action, str)


@given(instance=tfsm::plaink3::Transition_strategy)
def test_tfsm::plaink3::transition_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=tfsm::plaink3::State_strategy)
@settings(max_examples=50)
def test_tfsm::plaink3::state_instantiation(instance):
    assert isinstance(instance, tfsm::plaink3::State)

@given(instance=tfsm::plaink3::FSMClock_strategy)
@settings(max_examples=50)
def test_tfsm::plaink3::fsmclock_instantiation(instance):
    assert isinstance(instance, tfsm::plaink3::FSMClock)

@given(instance=tfsm::plaink3::FSMClock_strategy)
def test_tfsm::plaink3::fsmclock_numberOfTicks_type(instance):
    assert isinstance(instance.numberOfTicks, str)


@given(instance=tfsm::plaink3::FSMClock_strategy)
def test_tfsm::plaink3::fsmclock_numberOfTicks_setter(instance):
    original = instance.numberOfTicks
    instance.numberOfTicks = original
    assert instance.numberOfTicks == original

@given(instance=tfsm::plaink3::TimedSystem_strategy)
@settings(max_examples=50)
def test_tfsm::plaink3::timedsystem_instantiation(instance):
    assert isinstance(instance, tfsm::plaink3::TimedSystem)

@given(instance=tfsm::plaink3::Guard_strategy)
@settings(max_examples=50)
def test_tfsm::plaink3::guard_instantiation(instance):
    assert isinstance(instance, tfsm::plaink3::Guard)

@given(instance=tfsm::plaink3::FSMEvent_strategy)
@settings(max_examples=50)
def test_tfsm::plaink3::fsmevent_instantiation(instance):
    assert isinstance(instance, tfsm::plaink3::FSMEvent)

@given(instance=tfsm::plaink3::FSMEvent_strategy)
def test_tfsm::plaink3::fsmevent_isTriggered_type(instance):
    assert isinstance(instance.isTriggered, bool)


@given(instance=tfsm::plaink3::FSMEvent_strategy)
def test_tfsm::plaink3::fsmevent_isTriggered_setter(instance):
    original = instance.isTriggered
    instance.isTriggered = original
    assert instance.isTriggered == original

@given(instance=tfsm::plaink3::TFSM_strategy)
@settings(max_examples=50)
def test_tfsm::plaink3::tfsm_instantiation(instance):
    assert isinstance(instance, tfsm::plaink3::TFSM)
