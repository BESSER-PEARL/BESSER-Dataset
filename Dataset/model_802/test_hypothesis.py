import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    k3fsm_Transition,
    k3fsm_State,
    k3fsm_FSM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_k3fsm_transition_is_not_abstract():
    assert not inspect.isabstract(k3fsm_Transition)


def test_k3fsm_transition_constructor_exists():
    assert callable(k3fsm_Transition.__init__)


def test_k3fsm_transition_constructor_args():
    sig = inspect.signature(k3fsm_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "output" in params, "Missing parameter 'output'"
    assert "name" in params, "Missing parameter 'name'"
    assert "input" in params, "Missing parameter 'input'"

def test_k3fsm_transition_has_output():
    assert hasattr(k3fsm_Transition, "output")
    descriptor = None
    for klass in k3fsm_Transition.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)

def test_k3fsm_transition_has_name():
    assert hasattr(k3fsm_Transition, "name")
    descriptor = None
    for klass in k3fsm_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_k3fsm_transition_has_input():
    assert hasattr(k3fsm_Transition, "input")
    descriptor = None
    for klass in k3fsm_Transition.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)



def test_k3fsm_state_is_not_abstract():
    assert not inspect.isabstract(k3fsm_State)


def test_k3fsm_state_constructor_exists():
    assert callable(k3fsm_State.__init__)


def test_k3fsm_state_constructor_args():
    sig = inspect.signature(k3fsm_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_k3fsm_state_has_name():
    assert hasattr(k3fsm_State, "name")
    descriptor = None
    for klass in k3fsm_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_k3fsm_fsm_is_not_abstract():
    assert not inspect.isabstract(k3fsm_FSM)


def test_k3fsm_fsm_constructor_exists():
    assert callable(k3fsm_FSM.__init__)


def test_k3fsm_fsm_constructor_args():
    sig = inspect.signature(k3fsm_FSM.__init__)
    params = list(sig.parameters.keys())
    assert "unprocessedString" in params, "Missing parameter 'unprocessedString'"
    assert "producedString" in params, "Missing parameter 'producedString'"
    assert "name" in params, "Missing parameter 'name'"
    assert "consummedString" in params, "Missing parameter 'consummedString'"

def test_k3fsm_fsm_has_unprocessedString():
    assert hasattr(k3fsm_FSM, "unprocessedString")
    descriptor = None
    for klass in k3fsm_FSM.__mro__:
        if "unprocessedString" in klass.__dict__:
            descriptor = klass.__dict__["unprocessedString"]
            break
    assert isinstance(descriptor, property)

def test_k3fsm_fsm_has_producedString():
    assert hasattr(k3fsm_FSM, "producedString")
    descriptor = None
    for klass in k3fsm_FSM.__mro__:
        if "producedString" in klass.__dict__:
            descriptor = klass.__dict__["producedString"]
            break
    assert isinstance(descriptor, property)

def test_k3fsm_fsm_has_name():
    assert hasattr(k3fsm_FSM, "name")
    descriptor = None
    for klass in k3fsm_FSM.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_k3fsm_fsm_has_consummedString():
    assert hasattr(k3fsm_FSM, "consummedString")
    descriptor = None
    for klass in k3fsm_FSM.__mro__:
        if "consummedString" in klass.__dict__:
            descriptor = klass.__dict__["consummedString"]
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
k3fsm_Transition_strategy = st.builds(
    k3fsm_Transition,
    output=
        safe_text,
    name=
        safe_text,
    input=
        safe_text
)
k3fsm_State_strategy = st.builds(
    k3fsm_State,
    name=
        safe_text
)
k3fsm_FSM_strategy = st.builds(
    k3fsm_FSM,
    unprocessedString=
        safe_text,
    producedString=
        safe_text,
    name=
        safe_text,
    consummedString=
        safe_text
)

@given(instance=k3fsm_Transition_strategy)
@settings(max_examples=50)
def test_k3fsm_transition_instantiation(instance):
    assert isinstance(instance, k3fsm_Transition)



@given(instance=k3fsm_Transition_strategy)
def test_k3fsm_transition_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original



@given(instance=k3fsm_Transition_strategy)
def test_k3fsm_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=k3fsm_Transition_strategy)
def test_k3fsm_transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original

@given(instance=k3fsm_State_strategy)
@settings(max_examples=50)
def test_k3fsm_state_instantiation(instance):
    assert isinstance(instance, k3fsm_State)



@given(instance=k3fsm_State_strategy)
def test_k3fsm_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=k3fsm_FSM_strategy)
@settings(max_examples=50)
def test_k3fsm_fsm_instantiation(instance):
    assert isinstance(instance, k3fsm_FSM)



@given(instance=k3fsm_FSM_strategy)
def test_k3fsm_fsm_unprocessedString_setter(instance):
    original = instance.unprocessedString
    instance.unprocessedString = original
    assert instance.unprocessedString == original



@given(instance=k3fsm_FSM_strategy)
def test_k3fsm_fsm_producedString_setter(instance):
    original = instance.producedString
    instance.producedString = original
    assert instance.producedString == original



@given(instance=k3fsm_FSM_strategy)
def test_k3fsm_fsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=k3fsm_FSM_strategy)
def test_k3fsm_fsm_consummedString_setter(instance):
    original = instance.consummedString
    instance.consummedString = original
    assert instance.consummedString == original
