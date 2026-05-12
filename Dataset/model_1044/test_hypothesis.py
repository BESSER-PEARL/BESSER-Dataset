import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    State,
    sample_Finalstate,
    sample_Initstate,
    sample_Transition,
    sample_FSM,
    sample_State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_sample_finalstate_is_not_abstract():
    assert not inspect.isabstract(sample_Finalstate)


def test_sample_finalstate_constructor_exists():
    assert callable(sample_Finalstate.__init__)


def test_sample_finalstate_constructor_args():
    sig = inspect.signature(sample_Finalstate.__init__)
    params = list(sig.parameters.keys())



def test_sample_initstate_is_not_abstract():
    assert not inspect.isabstract(sample_Initstate)


def test_sample_initstate_constructor_exists():
    assert callable(sample_Initstate.__init__)


def test_sample_initstate_constructor_args():
    sig = inspect.signature(sample_Initstate.__init__)
    params = list(sig.parameters.keys())



def test_sample_transition_is_not_abstract():
    assert not inspect.isabstract(sample_Transition)


def test_sample_transition_constructor_exists():
    assert callable(sample_Transition.__init__)


def test_sample_transition_constructor_args():
    sig = inspect.signature(sample_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "trigger" in params, "Missing parameter 'trigger'"
    assert "name" in params, "Missing parameter 'name'"

def test_sample_transition_has_trigger():
    assert hasattr(sample_Transition, "trigger")
    descriptor = None
    for klass in sample_Transition.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
            break
    assert isinstance(descriptor, property)

def test_sample_transition_has_name():
    assert hasattr(sample_Transition, "name")
    descriptor = None
    for klass in sample_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sample_fsm_is_not_abstract():
    assert not inspect.isabstract(sample_FSM)


def test_sample_fsm_constructor_exists():
    assert callable(sample_FSM.__init__)


def test_sample_fsm_constructor_args():
    sig = inspect.signature(sample_FSM.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sample_fsm_has_name():
    assert hasattr(sample_FSM, "name")
    descriptor = None
    for klass in sample_FSM.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sample_state_is_not_abstract():
    assert not inspect.isabstract(sample_State)


def test_sample_state_constructor_exists():
    assert callable(sample_State.__init__)


def test_sample_state_constructor_args():
    sig = inspect.signature(sample_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sample_state_has_name():
    assert hasattr(sample_State, "name")
    descriptor = None
    for klass in sample_State.__mro__:
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
State_strategy = st.builds(
    State,
)
sample_Finalstate_strategy = st.builds(
    sample_Finalstate,
)
sample_Initstate_strategy = st.builds(
    sample_Initstate,
)
sample_Transition_strategy = st.builds(
    sample_Transition,
    trigger=
        safe_text,
    name=
        safe_text
)
sample_FSM_strategy = st.builds(
    sample_FSM,
    name=
        safe_text
)
sample_State_strategy = st.builds(
    sample_State,
    name=
        safe_text
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=sample_Finalstate_strategy)
@settings(max_examples=50)
def test_sample_finalstate_instantiation(instance):
    assert isinstance(instance, sample_Finalstate)

@given(instance=sample_Initstate_strategy)
@settings(max_examples=50)
def test_sample_initstate_instantiation(instance):
    assert isinstance(instance, sample_Initstate)

@given(instance=sample_Transition_strategy)
@settings(max_examples=50)
def test_sample_transition_instantiation(instance):
    assert isinstance(instance, sample_Transition)



@given(instance=sample_Transition_strategy)
def test_sample_transition_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original



@given(instance=sample_Transition_strategy)
def test_sample_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sample_FSM_strategy)
@settings(max_examples=50)
def test_sample_fsm_instantiation(instance):
    assert isinstance(instance, sample_FSM)



@given(instance=sample_FSM_strategy)
def test_sample_fsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sample_State_strategy)
@settings(max_examples=50)
def test_sample_state_instantiation(instance):
    assert isinstance(instance, sample_State)



@given(instance=sample_State_strategy)
def test_sample_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
