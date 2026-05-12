import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    model_Transition,
    model_State,
    model_FSM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model_transition_is_not_abstract():
    assert not inspect.isabstract(model_Transition)


def test_model_transition_constructor_exists():
    assert callable(model_Transition.__init__)


def test_model_transition_constructor_args():
    sig = inspect.signature(model_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"
    assert "trigger" in params, "Missing parameter 'trigger'"
    assert "name" in params, "Missing parameter 'name'"

def test_model_transition_has_action():
    assert hasattr(model_Transition, "action")
    descriptor = None
    for klass in model_Transition.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)

def test_model_transition_has_trigger():
    assert hasattr(model_Transition, "trigger")
    descriptor = None
    for klass in model_Transition.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
            break
    assert isinstance(descriptor, property)

def test_model_transition_has_name():
    assert hasattr(model_Transition, "name")
    descriptor = None
    for klass in model_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model_state_is_not_abstract():
    assert not inspect.isabstract(model_State)


def test_model_state_constructor_exists():
    assert callable(model_State.__init__)


def test_model_state_constructor_args():
    sig = inspect.signature(model_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model_state_has_name():
    assert hasattr(model_State, "name")
    descriptor = None
    for klass in model_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model_fsm_is_not_abstract():
    assert not inspect.isabstract(model_FSM)


def test_model_fsm_constructor_exists():
    assert callable(model_FSM.__init__)


def test_model_fsm_constructor_args():
    sig = inspect.signature(model_FSM.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model_fsm_has_name():
    assert hasattr(model_FSM, "name")
    descriptor = None
    for klass in model_FSM.__mro__:
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
model_Transition_strategy = st.builds(
    model_Transition,
    action=
        safe_text,
    trigger=
        safe_text,
    name=
        safe_text
)
model_State_strategy = st.builds(
    model_State,
    name=
        safe_text
)
model_FSM_strategy = st.builds(
    model_FSM,
    name=
        safe_text
)

@given(instance=model_Transition_strategy)
@settings(max_examples=50)
def test_model_transition_instantiation(instance):
    assert isinstance(instance, model_Transition)



@given(instance=model_Transition_strategy)
def test_model_transition_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original



@given(instance=model_Transition_strategy)
def test_model_transition_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original



@given(instance=model_Transition_strategy)
def test_model_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model_State_strategy)
@settings(max_examples=50)
def test_model_state_instantiation(instance):
    assert isinstance(instance, model_State)



@given(instance=model_State_strategy)
def test_model_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model_FSM_strategy)
@settings(max_examples=50)
def test_model_fsm_instantiation(instance):
    assert isinstance(instance, model_FSM)



@given(instance=model_FSM_strategy)
def test_model_fsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
