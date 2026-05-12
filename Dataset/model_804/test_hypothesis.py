import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    kfsm_Action,
    kfsm_Transition,
    kfsm_State,
    kfsm_FSM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_kfsm_action_is_not_abstract():
    assert not inspect.isabstract(kfsm_Action)


def test_kfsm_action_constructor_exists():
    assert callable(kfsm_Action.__init__)


def test_kfsm_action_constructor_args():
    sig = inspect.signature(kfsm_Action.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_kfsm_action_has_id():
    assert hasattr(kfsm_Action, "id")
    descriptor = None
    for klass in kfsm_Action.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_kfsm_transition_is_not_abstract():
    assert not inspect.isabstract(kfsm_Transition)


def test_kfsm_transition_constructor_exists():
    assert callable(kfsm_Transition.__init__)


def test_kfsm_transition_constructor_args():
    sig = inspect.signature(kfsm_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "output" in params, "Missing parameter 'output'"
    assert "input" in params, "Missing parameter 'input'"

def test_kfsm_transition_has_output():
    assert hasattr(kfsm_Transition, "output")
    descriptor = None
    for klass in kfsm_Transition.__mro__:
        if "output" in klass.__dict__:
            descriptor = klass.__dict__["output"]
            break
    assert isinstance(descriptor, property)

def test_kfsm_transition_has_input():
    assert hasattr(kfsm_Transition, "input")
    descriptor = None
    for klass in kfsm_Transition.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)



def test_kfsm_state_is_not_abstract():
    assert not inspect.isabstract(kfsm_State)


def test_kfsm_state_constructor_exists():
    assert callable(kfsm_State.__init__)


def test_kfsm_state_constructor_args():
    sig = inspect.signature(kfsm_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_kfsm_state_has_name():
    assert hasattr(kfsm_State, "name")
    descriptor = None
    for klass in kfsm_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_kfsm_fsm_is_not_abstract():
    assert not inspect.isabstract(kfsm_FSM)


def test_kfsm_fsm_constructor_exists():
    assert callable(kfsm_FSM.__init__)


def test_kfsm_fsm_constructor_args():
    sig = inspect.signature(kfsm_FSM.__init__)
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
kfsm_Action_strategy = st.builds(
    kfsm_Action,
    id=
        safe_text
)
kfsm_Transition_strategy = st.builds(
    kfsm_Transition,
    output=
        safe_text,
    input=
        safe_text
)
kfsm_State_strategy = st.builds(
    kfsm_State,
    name=
        safe_text
)
kfsm_FSM_strategy = st.builds(
    kfsm_FSM,
)

@given(instance=kfsm_Action_strategy)
@settings(max_examples=50)
def test_kfsm_action_instantiation(instance):
    assert isinstance(instance, kfsm_Action)



@given(instance=kfsm_Action_strategy)
def test_kfsm_action_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=kfsm_Transition_strategy)
@settings(max_examples=50)
def test_kfsm_transition_instantiation(instance):
    assert isinstance(instance, kfsm_Transition)



@given(instance=kfsm_Transition_strategy)
def test_kfsm_transition_output_setter(instance):
    original = instance.output
    instance.output = original
    assert instance.output == original



@given(instance=kfsm_Transition_strategy)
def test_kfsm_transition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original

@given(instance=kfsm_State_strategy)
@settings(max_examples=50)
def test_kfsm_state_instantiation(instance):
    assert isinstance(instance, kfsm_State)



@given(instance=kfsm_State_strategy)
def test_kfsm_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=kfsm_FSM_strategy)
@settings(max_examples=50)
def test_kfsm_fsm_instantiation(instance):
    assert isinstance(instance, kfsm_FSM)
