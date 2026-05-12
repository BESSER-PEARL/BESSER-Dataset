import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    compositefsm_State,
    compositefsm_FSM,
    compositefsm_Transition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_compositefsm_state_is_not_abstract():
    assert not inspect.isabstract(compositefsm_State)


def test_compositefsm_state_constructor_exists():
    assert callable(compositefsm_State.__init__)


def test_compositefsm_state_constructor_args():
    sig = inspect.signature(compositefsm_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_compositefsm_state_has_name():
    assert hasattr(compositefsm_State, "name")
    descriptor = None
    for klass in compositefsm_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_compositefsm_fsm_is_not_abstract():
    assert not inspect.isabstract(compositefsm_FSM)


def test_compositefsm_fsm_constructor_exists():
    assert callable(compositefsm_FSM.__init__)


def test_compositefsm_fsm_constructor_args():
    sig = inspect.signature(compositefsm_FSM.__init__)
    params = list(sig.parameters.keys())



def test_compositefsm_transition_is_not_abstract():
    assert not inspect.isabstract(compositefsm_Transition)


def test_compositefsm_transition_constructor_exists():
    assert callable(compositefsm_Transition.__init__)


def test_compositefsm_transition_constructor_args():
    sig = inspect.signature(compositefsm_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "input" in params, "Missing parameter 'input'"
    assert "output" in params, "Missing parameter 'output'"

def test_compositefsm_transition_has_input():
    assert hasattr(compositefsm_Transition, "input")
    descriptor = None
    for klass in compositefsm_Transition.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)

def test_compositefsm_transition_has_output():
    assert hasattr(compositefsm_Transition, "output")
    descriptor = None
    for klass in compositefsm_Transition.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
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
compositefsm_State_strategy = st.builds(
    compositefsm_State,
    name=
        safe_text
)
compositefsm_FSM_strategy = st.builds(
    compositefsm_FSM,
)
compositefsm_Transition_strategy = st.builds(
    compositefsm_Transition,
    input=
        safe_text,
    output=
        safe_text
)

@given(instance=compositefsm_State_strategy)
@settings(max_examples=50)
def test_compositefsm_state_instantiation(instance):
    assert isinstance(instance, compositefsm_State)



@given(instance=compositefsm_State_strategy)
def test_compositefsm_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=compositefsm_FSM_strategy)
@settings(max_examples=50)
def test_compositefsm_fsm_instantiation(instance):
    assert isinstance(instance, compositefsm_FSM)

@given(instance=compositefsm_Transition_strategy)
@settings(max_examples=50)
def test_compositefsm_transition_instantiation(instance):
    assert isinstance(instance, compositefsm_Transition)



@given(instance=compositefsm_Transition_strategy)
def test_compositefsm_transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original



@given(instance=compositefsm_Transition_strategy)
def test_compositefsm_transition_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original
