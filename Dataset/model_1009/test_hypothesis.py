import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    fsm_tp_Transition,
    fsm_tp_State,
    fsm_tp_FSM,
    State,
    fsm_tp_InitialState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsm_tp_transition_is_not_abstract():
    assert not inspect.isabstract(fsm_tp_Transition)


def test_fsm_tp_transition_constructor_exists():
    assert callable(fsm_tp_Transition.__init__)


def test_fsm_tp_transition_constructor_args():
    sig = inspect.signature(fsm_tp_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "trigger" in params, "Missing parameter 'trigger'"
    assert "name" in params, "Missing parameter 'name'"

def test_fsm_tp_transition_has_trigger():
    assert hasattr(fsm_tp_Transition, "trigger")
    descriptor = None
    for klass in fsm_tp_Transition.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
            break
    assert isinstance(descriptor, property)

def test_fsm_tp_transition_has_name():
    assert hasattr(fsm_tp_Transition, "name")
    descriptor = None
    for klass in fsm_tp_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsm_tp_state_is_not_abstract():
    assert not inspect.isabstract(fsm_tp_State)


def test_fsm_tp_state_constructor_exists():
    assert callable(fsm_tp_State.__init__)


def test_fsm_tp_state_constructor_args():
    sig = inspect.signature(fsm_tp_State.__init__)
    params = list(sig.parameters.keys())
    assert "isFinal" in params, "Missing parameter 'isFinal'"
    assert "name" in params, "Missing parameter 'name'"

def test_fsm_tp_state_has_isFinal():
    assert hasattr(fsm_tp_State, "isFinal")
    descriptor = None
    for klass in fsm_tp_State.__mro__:
        if "isFinal" in klass.__dict__:
            descriptor = klass.__dict__["isFinal"]
            break
    assert isinstance(descriptor, property)

def test_fsm_tp_state_has_name():
    assert hasattr(fsm_tp_State, "name")
    descriptor = None
    for klass in fsm_tp_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsm_tp_fsm_is_not_abstract():
    assert not inspect.isabstract(fsm_tp_FSM)


def test_fsm_tp_fsm_constructor_exists():
    assert callable(fsm_tp_FSM.__init__)


def test_fsm_tp_fsm_constructor_args():
    sig = inspect.signature(fsm_tp_FSM.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fsm_tp_fsm_has_name():
    assert hasattr(fsm_tp_FSM, "name")
    descriptor = None
    for klass in fsm_tp_FSM.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_fsm_tp_initialstate_is_not_abstract():
    assert not inspect.isabstract(fsm_tp_InitialState)


def test_fsm_tp_initialstate_constructor_exists():
    assert callable(fsm_tp_InitialState.__init__)


def test_fsm_tp_initialstate_constructor_args():
    sig = inspect.signature(fsm_tp_InitialState.__init__)
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
fsm_tp_Transition_strategy = st.builds(
    fsm_tp_Transition,
    trigger=
        safe_text,
    name=
        safe_text
)
fsm_tp_State_strategy = st.builds(
    fsm_tp_State,
    isFinal=
        st.booleans(),
    name=
        safe_text
)
fsm_tp_FSM_strategy = st.builds(
    fsm_tp_FSM,
    name=
        safe_text
)
State_strategy = st.builds(
    State,
)
fsm_tp_InitialState_strategy = st.builds(
    fsm_tp_InitialState,
)

@given(instance=fsm_tp_Transition_strategy)
@settings(max_examples=50)
def test_fsm_tp_transition_instantiation(instance):
    assert isinstance(instance, fsm_tp_Transition)



@given(instance=fsm_tp_Transition_strategy)
def test_fsm_tp_transition_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original



@given(instance=fsm_tp_Transition_strategy)
def test_fsm_tp_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsm_tp_State_strategy)
@settings(max_examples=50)
def test_fsm_tp_state_instantiation(instance):
    assert isinstance(instance, fsm_tp_State)



@given(instance=fsm_tp_State_strategy)
def test_fsm_tp_state_isFinal_setter(instance):
    original = instance.isFinal
    instance.isFinal = original
    assert instance.isFinal == original



@given(instance=fsm_tp_State_strategy)
def test_fsm_tp_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fsm_tp_FSM_strategy)
@settings(max_examples=50)
def test_fsm_tp_fsm_instantiation(instance):
    assert isinstance(instance, fsm_tp_FSM)



@given(instance=fsm_tp_FSM_strategy)
def test_fsm_tp_fsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=fsm_tp_InitialState_strategy)
@settings(max_examples=50)
def test_fsm_tp_initialstate_instantiation(instance):
    assert isinstance(instance, fsm_tp_InitialState)
