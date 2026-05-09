import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    tsm::TimeEvent,
    NamedElement,
    tsm::StateMachine,
    tsm::State,
    tsm::NamedElement,
    tsm::Transition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tsm::timeevent_is_not_abstract():
    assert not inspect.isabstract(tsm::TimeEvent)


def test_tsm::timeevent_constructor_exists():
    assert callable(tsm::TimeEvent.__init__)


def test_tsm::timeevent_constructor_args():
    sig = inspect.signature(tsm::TimeEvent.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"

def test_tsm::timeevent_has_time():
    assert hasattr(tsm::TimeEvent, "time")
    descriptor = None
    for klass in tsm::TimeEvent.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_tsm::statemachine_is_not_abstract():
    assert not inspect.isabstract(tsm::StateMachine)


def test_tsm::statemachine_constructor_exists():
    assert callable(tsm::StateMachine.__init__)


def test_tsm::statemachine_constructor_args():
    sig = inspect.signature(tsm::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_tsm::state_is_not_abstract():
    assert not inspect.isabstract(tsm::State)


def test_tsm::state_constructor_exists():
    assert callable(tsm::State.__init__)


def test_tsm::state_constructor_args():
    sig = inspect.signature(tsm::State.__init__)
    params = list(sig.parameters.keys())



def test_tsm::namedelement_is_not_abstract():
    assert not inspect.isabstract(tsm::NamedElement)


def test_tsm::namedelement_constructor_exists():
    assert callable(tsm::NamedElement.__init__)


def test_tsm::namedelement_constructor_args():
    sig = inspect.signature(tsm::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tsm::namedelement_has_name():
    assert hasattr(tsm::NamedElement, "name")
    descriptor = None
    for klass in tsm::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tsm::transition_is_not_abstract():
    assert not inspect.isabstract(tsm::Transition)


def test_tsm::transition_constructor_exists():
    assert callable(tsm::Transition.__init__)


def test_tsm::transition_constructor_args():
    sig = inspect.signature(tsm::Transition.__init__)
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
tsm::TimeEvent_strategy = st.builds(
    tsm::TimeEvent,
    time=
        st.integers()
)
NamedElement_strategy = st.builds(
    NamedElement,
)
tsm::StateMachine_strategy = st.builds(
    tsm::StateMachine,
)
tsm::State_strategy = st.builds(
    tsm::State,
)
tsm::NamedElement_strategy = st.builds(
    tsm::NamedElement,
    name=
        safe_text
)
tsm::Transition_strategy = st.builds(
    tsm::Transition,
)

@given(instance=tsm::TimeEvent_strategy)
@settings(max_examples=50)
def test_tsm::timeevent_instantiation(instance):
    assert isinstance(instance, tsm::TimeEvent)

@given(instance=tsm::TimeEvent_strategy)
def test_tsm::timeevent_time_type(instance):
    assert isinstance(instance.time, int)


@given(instance=tsm::TimeEvent_strategy)
def test_tsm::timeevent_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=tsm::StateMachine_strategy)
@settings(max_examples=50)
def test_tsm::statemachine_instantiation(instance):
    assert isinstance(instance, tsm::StateMachine)

@given(instance=tsm::State_strategy)
@settings(max_examples=50)
def test_tsm::state_instantiation(instance):
    assert isinstance(instance, tsm::State)

@given(instance=tsm::NamedElement_strategy)
@settings(max_examples=50)
def test_tsm::namedelement_instantiation(instance):
    assert isinstance(instance, tsm::NamedElement)

@given(instance=tsm::NamedElement_strategy)
def test_tsm::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tsm::NamedElement_strategy)
def test_tsm::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tsm::Transition_strategy)
@settings(max_examples=50)
def test_tsm::transition_instantiation(instance):
    assert isinstance(instance, tsm::Transition)
