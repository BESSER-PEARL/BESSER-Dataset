import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    State,
    dsl_State,
    dsl_FSM,
    dsl_InitialState,
    dsl_Transition,
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



def test_dsl_state_is_not_abstract():
    assert not inspect.isabstract(dsl_State)


def test_dsl_state_constructor_exists():
    assert callable(dsl_State.__init__)


def test_dsl_state_constructor_args():
    sig = inspect.signature(dsl_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isFinal" in params, "Missing parameter 'isFinal'"

def test_dsl_state_has_name():
    assert hasattr(dsl_State, "name")
    descriptor = None
    for klass in dsl_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dsl_state_has_isFinal():
    assert hasattr(dsl_State, "isFinal")
    descriptor = None
    for klass in dsl_State.__mro__:
        if "isFinal" in klass.__dict__:
            descriptor = klass.__dict__["isFinal"]
            break
    assert isinstance(descriptor, property)



def test_dsl_fsm_is_not_abstract():
    assert not inspect.isabstract(dsl_FSM)


def test_dsl_fsm_constructor_exists():
    assert callable(dsl_FSM.__init__)


def test_dsl_fsm_constructor_args():
    sig = inspect.signature(dsl_FSM.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dsl_fsm_has_name():
    assert hasattr(dsl_FSM, "name")
    descriptor = None
    for klass in dsl_FSM.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dsl_initialstate_is_not_abstract():
    assert not inspect.isabstract(dsl_InitialState)


def test_dsl_initialstate_constructor_exists():
    assert callable(dsl_InitialState.__init__)


def test_dsl_initialstate_constructor_args():
    sig = inspect.signature(dsl_InitialState.__init__)
    params = list(sig.parameters.keys())



def test_dsl_transition_is_not_abstract():
    assert not inspect.isabstract(dsl_Transition)


def test_dsl_transition_constructor_exists():
    assert callable(dsl_Transition.__init__)


def test_dsl_transition_constructor_args():
    sig = inspect.signature(dsl_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "trigger" in params, "Missing parameter 'trigger'"

def test_dsl_transition_has_name():
    assert hasattr(dsl_Transition, "name")
    descriptor = None
    for klass in dsl_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dsl_transition_has_trigger():
    assert hasattr(dsl_Transition, "trigger")
    descriptor = None
    for klass in dsl_Transition.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
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
dsl_State_strategy = st.builds(
    dsl_State,
    name=
        safe_text,
    isFinal=
        st.booleans()
)
dsl_FSM_strategy = st.builds(
    dsl_FSM,
    name=
        safe_text
)
dsl_InitialState_strategy = st.builds(
    dsl_InitialState,
)
dsl_Transition_strategy = st.builds(
    dsl_Transition,
    name=
        safe_text,
    trigger=
        safe_text
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=dsl_State_strategy)
@settings(max_examples=50)
def test_dsl_state_instantiation(instance):
    assert isinstance(instance, dsl_State)



@given(instance=dsl_State_strategy)
def test_dsl_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=dsl_State_strategy)
def test_dsl_state_isFinal_setter(instance):
    original = instance.isFinal
    instance.isFinal = original
    assert instance.isFinal == original

@given(instance=dsl_FSM_strategy)
@settings(max_examples=50)
def test_dsl_fsm_instantiation(instance):
    assert isinstance(instance, dsl_FSM)



@given(instance=dsl_FSM_strategy)
def test_dsl_fsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dsl_InitialState_strategy)
@settings(max_examples=50)
def test_dsl_initialstate_instantiation(instance):
    assert isinstance(instance, dsl_InitialState)

@given(instance=dsl_Transition_strategy)
@settings(max_examples=50)
def test_dsl_transition_instantiation(instance):
    assert isinstance(instance, dsl_Transition)



@given(instance=dsl_Transition_strategy)
def test_dsl_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=dsl_Transition_strategy)
def test_dsl_transition_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original
