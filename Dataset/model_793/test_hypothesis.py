import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    timedfsm_FSM,
    timedfsm_Transition,
    timedfsm_State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_timedfsm_fsm_is_not_abstract():
    assert not inspect.isabstract(timedfsm_FSM)


def test_timedfsm_fsm_constructor_exists():
    assert callable(timedfsm_FSM.__init__)


def test_timedfsm_fsm_constructor_args():
    sig = inspect.signature(timedfsm_FSM.__init__)
    params = list(sig.parameters.keys())



def test_timedfsm_transition_is_not_abstract():
    assert not inspect.isabstract(timedfsm_Transition)


def test_timedfsm_transition_constructor_exists():
    assert callable(timedfsm_Transition.__init__)


def test_timedfsm_transition_constructor_args():
    sig = inspect.signature(timedfsm_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "input" in params, "Missing parameter 'input'"
    assert "waitingTime" in params, "Missing parameter 'waitingTime'"
    assert "output" in params, "Missing parameter 'output'"

def test_timedfsm_transition_has_input():
    assert hasattr(timedfsm_Transition, "input")
    descriptor = None
    for klass in timedfsm_Transition.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)

def test_timedfsm_transition_has_waitingTime():
    assert hasattr(timedfsm_Transition, "waitingTime")
    descriptor = None
    for klass in timedfsm_Transition.__mro__:
        if "waitingTime" in klass.__dict__:
            descriptor = klass.__dict__["waitingTime"]
            break
    assert isinstance(descriptor, property)

def test_timedfsm_transition_has_output():
    assert hasattr(timedfsm_Transition, "output")
    descriptor = None
    for klass in timedfsm_Transition.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)



def test_timedfsm_state_is_not_abstract():
    assert not inspect.isabstract(timedfsm_State)


def test_timedfsm_state_constructor_exists():
    assert callable(timedfsm_State.__init__)


def test_timedfsm_state_constructor_args():
    sig = inspect.signature(timedfsm_State.__init__)
    params = list(sig.parameters.keys())
    assert "waitingTime" in params, "Missing parameter 'waitingTime'"
    assert "name" in params, "Missing parameter 'name'"

def test_timedfsm_state_has_waitingTime():
    assert hasattr(timedfsm_State, "waitingTime")
    descriptor = None
    for klass in timedfsm_State.__mro__:
        if "waitingTime" in klass.__dict__:
            descriptor = klass.__dict__["waitingTime"]
            break
    assert isinstance(descriptor, property)

def test_timedfsm_state_has_name():
    assert hasattr(timedfsm_State, "name")
    descriptor = None
    for klass in timedfsm_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
timedfsm_FSM_strategy = st.builds(
    timedfsm_FSM,
)
timedfsm_Transition_strategy = st.builds(
    timedfsm_Transition,
    input=
        safe_text,
    waitingTime=
        st.integers(),
    output=
        safe_text
)
timedfsm_State_strategy = st.builds(
    timedfsm_State,
    waitingTime=
        st.integers(),
    name=
        safe_text
)

@given(instance=timedfsm_FSM_strategy)
@settings(max_examples=50)
def test_timedfsm_fsm_instantiation(instance):
    assert isinstance(instance, timedfsm_FSM)

@given(instance=timedfsm_Transition_strategy)
@settings(max_examples=50)
def test_timedfsm_transition_instantiation(instance):
    assert isinstance(instance, timedfsm_Transition)



@given(instance=timedfsm_Transition_strategy)
def test_timedfsm_transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original



@given(instance=timedfsm_Transition_strategy)
def test_timedfsm_transition_waitingTime_setter(instance):
    original = instance.waitingTime
    instance.waitingTime = original
    assert instance.waitingTime == original



@given(instance=timedfsm_Transition_strategy)
def test_timedfsm_transition_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original

@given(instance=timedfsm_State_strategy)
@settings(max_examples=50)
def test_timedfsm_state_instantiation(instance):
    assert isinstance(instance, timedfsm_State)



@given(instance=timedfsm_State_strategy)
def test_timedfsm_state_waitingTime_setter(instance):
    original = instance.waitingTime
    instance.waitingTime = original
    assert instance.waitingTime == original



@given(instance=timedfsm_State_strategy)
def test_timedfsm_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
