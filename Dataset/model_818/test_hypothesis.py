import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    fsmSample_Action,
    fsmSample_Transition,
    fsmSample_State,
    fsmSample_FSM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsmsample_action_is_not_abstract():
    assert not inspect.isabstract(fsmSample_Action)


def test_fsmsample_action_constructor_exists():
    assert callable(fsmSample_Action.__init__)


def test_fsmsample_action_constructor_args():
    sig = inspect.signature(fsmSample_Action.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsmsample_action_has_name():
    assert hasattr(fsmSample_Action, "name")
    descriptor = None
    for klass in fsmSample_Action.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsmsample_transition_is_not_abstract():
    assert not inspect.isabstract(fsmSample_Transition)


def test_fsmsample_transition_constructor_exists():
    assert callable(fsmSample_Transition.__init__)


def test_fsmsample_transition_constructor_args():
    sig = inspect.signature(fsmSample_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "output" in params, "Missing parameter 'output'"
    assert "input" in params, "Missing parameter 'input'"

def test_fsmsample_transition_has_output():
    assert hasattr(fsmSample_Transition, "output")
    descriptor = None
    for klass in fsmSample_Transition.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)

def test_fsmsample_transition_has_input():
    assert hasattr(fsmSample_Transition, "input")
    descriptor = None
    for klass in fsmSample_Transition.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)



def test_fsmsample_state_is_not_abstract():
    assert not inspect.isabstract(fsmSample_State)


def test_fsmsample_state_constructor_exists():
    assert callable(fsmSample_State.__init__)


def test_fsmsample_state_constructor_args():
    sig = inspect.signature(fsmSample_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsmsample_state_has_name():
    assert hasattr(fsmSample_State, "name")
    descriptor = None
    for klass in fsmSample_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsmsample_fsm_is_not_abstract():
    assert not inspect.isabstract(fsmSample_FSM)


def test_fsmsample_fsm_constructor_exists():
    assert callable(fsmSample_FSM.__init__)


def test_fsmsample_fsm_constructor_args():
    sig = inspect.signature(fsmSample_FSM.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsmsample_fsm_has_name():
    assert hasattr(fsmSample_FSM, "name")
    descriptor = None
    for klass in fsmSample_FSM.__mro__:
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
fsmSample_Action_strategy = st.builds(
    fsmSample_Action,
    name=
        safe_text
)
fsmSample_Transition_strategy = st.builds(
    fsmSample_Transition,
    output=
        safe_text,
    input=
        safe_text
)
fsmSample_State_strategy = st.builds(
    fsmSample_State,
    name=
        safe_text
)
fsmSample_FSM_strategy = st.builds(
    fsmSample_FSM,
    name=
        safe_text
)

@given(instance=fsmSample_Action_strategy)
@settings(max_examples=50)
def test_fsmsample_action_instantiation(instance):
    assert isinstance(instance, fsmSample_Action)



@given(instance=fsmSample_Action_strategy)
def test_fsmsample_action_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsmSample_Transition_strategy)
@settings(max_examples=50)
def test_fsmsample_transition_instantiation(instance):
    assert isinstance(instance, fsmSample_Transition)



@given(instance=fsmSample_Transition_strategy)
def test_fsmsample_transition_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original



@given(instance=fsmSample_Transition_strategy)
def test_fsmsample_transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original

@given(instance=fsmSample_State_strategy)
@settings(max_examples=50)
def test_fsmsample_state_instantiation(instance):
    assert isinstance(instance, fsmSample_State)



@given(instance=fsmSample_State_strategy)
def test_fsmsample_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsmSample_FSM_strategy)
@settings(max_examples=50)
def test_fsmsample_fsm_instantiation(instance):
    assert isinstance(instance, fsmSample_FSM)



@given(instance=fsmSample_FSM_strategy)
def test_fsmsample_fsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
