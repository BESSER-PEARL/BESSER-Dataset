import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    timedfsm::Transition,
    timedfsm::State,
    timedfsm::FSM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_timedfsm::transition_is_not_abstract():
    assert not inspect.isabstract(timedfsm::Transition)


def test_timedfsm::transition_constructor_exists():
    assert callable(timedfsm::Transition.__init__)


def test_timedfsm::transition_constructor_args():
    sig = inspect.signature(timedfsm::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "input" in params, "Missing parameter 'input'"
    assert "waitingTime" in params, "Missing parameter 'waitingTime'"
    assert "output" in params, "Missing parameter 'output'"

def test_timedfsm::transition_has_input():
    assert hasattr(timedfsm::Transition, "input")
    descriptor = None
    for klass in timedfsm::Transition.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)

def test_timedfsm::transition_has_waitingTime():
    assert hasattr(timedfsm::Transition, "waitingTime")
    descriptor = None
    for klass in timedfsm::Transition.__mro__:
        if "waitingTime" in klass.__dict__:
            descriptor = klass.__dict__["waitingTime"]
            break
    assert isinstance(descriptor, property)

def test_timedfsm::transition_has_output():
    assert hasattr(timedfsm::Transition, "output")
    descriptor = None
    for klass in timedfsm::Transition.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)



def test_timedfsm::state_is_not_abstract():
    assert not inspect.isabstract(timedfsm::State)


def test_timedfsm::state_constructor_exists():
    assert callable(timedfsm::State.__init__)


def test_timedfsm::state_constructor_args():
    sig = inspect.signature(timedfsm::State.__init__)
    params = list(sig.parameters.keys())
    assert "waitingTime" in params, "Missing parameter 'waitingTime'"
    assert "name" in params, "Missing parameter 'name'"

def test_timedfsm::state_has_waitingTime():
    assert hasattr(timedfsm::State, "waitingTime")
    descriptor = None
    for klass in timedfsm::State.__mro__:
        if "waitingTime" in klass.__dict__:
            descriptor = klass.__dict__["waitingTime"]
            break
    assert isinstance(descriptor, property)

def test_timedfsm::state_has_name():
    assert hasattr(timedfsm::State, "name")
    descriptor = None
    for klass in timedfsm::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_timedfsm::fsm_is_not_abstract():
    assert not inspect.isabstract(timedfsm::FSM)


def test_timedfsm::fsm_constructor_exists():
    assert callable(timedfsm::FSM.__init__)


def test_timedfsm::fsm_constructor_args():
    sig = inspect.signature(timedfsm::FSM.__init__)
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
timedfsm::Transition_strategy = st.builds(
    timedfsm::Transition,
    input=
        safe_text,
    waitingTime=
        st.integers(),
    output=
        safe_text
)
timedfsm::State_strategy = st.builds(
    timedfsm::State,
    waitingTime=
        st.integers(),
    name=
        safe_text
)
timedfsm::FSM_strategy = st.builds(
    timedfsm::FSM,
)

@given(instance=timedfsm::Transition_strategy)
@settings(max_examples=50)
def test_timedfsm::transition_instantiation(instance):
    assert isinstance(instance, timedfsm::Transition)

@given(instance=timedfsm::Transition_strategy)
def test_timedfsm::transition_input_type(instance):
    assert isinstance(instance.input, str)


@given(instance=timedfsm::Transition_strategy)
def test_timedfsm::transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original

@given(instance=timedfsm::Transition_strategy)
def test_timedfsm::transition_waitingTime_type(instance):
    assert isinstance(instance.waitingTime, int)


@given(instance=timedfsm::Transition_strategy)
def test_timedfsm::transition_waitingTime_setter(instance):
    original = instance.waitingTime
    instance.waitingTime = original
    assert instance.waitingTime == original

@given(instance=timedfsm::Transition_strategy)
def test_timedfsm::transition_output_type(instance):
    assert isinstance(instance.output, str)


@given(instance=timedfsm::Transition_strategy)
def test_timedfsm::transition_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original

@given(instance=timedfsm::State_strategy)
@settings(max_examples=50)
def test_timedfsm::state_instantiation(instance):
    assert isinstance(instance, timedfsm::State)

@given(instance=timedfsm::State_strategy)
def test_timedfsm::state_waitingTime_type(instance):
    assert isinstance(instance.waitingTime, int)


@given(instance=timedfsm::State_strategy)
def test_timedfsm::state_waitingTime_setter(instance):
    original = instance.waitingTime
    instance.waitingTime = original
    assert instance.waitingTime == original

@given(instance=timedfsm::State_strategy)
def test_timedfsm::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=timedfsm::State_strategy)
def test_timedfsm::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=timedfsm::FSM_strategy)
@settings(max_examples=50)
def test_timedfsm::fsm_instantiation(instance):
    assert isinstance(instance, timedfsm::FSM)
