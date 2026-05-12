import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    State,
    fMS_FinalState,
    fMS_InitState,
    fMS_Transition,
    fMS_State,
    fMS_FSM,
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



def test_fms_finalstate_is_not_abstract():
    assert not inspect.isabstract(fMS_FinalState)


def test_fms_finalstate_constructor_exists():
    assert callable(fMS_FinalState.__init__)


def test_fms_finalstate_constructor_args():
    sig = inspect.signature(fMS_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_fms_initstate_is_not_abstract():
    assert not inspect.isabstract(fMS_InitState)


def test_fms_initstate_constructor_exists():
    assert callable(fMS_InitState.__init__)


def test_fms_initstate_constructor_args():
    sig = inspect.signature(fMS_InitState.__init__)
    params = list(sig.parameters.keys())



def test_fms_transition_is_not_abstract():
    assert not inspect.isabstract(fMS_Transition)


def test_fms_transition_constructor_exists():
    assert callable(fMS_Transition.__init__)


def test_fms_transition_constructor_args():
    sig = inspect.signature(fMS_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fms_transition_has_name():
    assert hasattr(fMS_Transition, "name")
    descriptor = None
    for klass in fMS_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fms_state_is_not_abstract():
    assert not inspect.isabstract(fMS_State)


def test_fms_state_constructor_exists():
    assert callable(fMS_State.__init__)


def test_fms_state_constructor_args():
    sig = inspect.signature(fMS_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fms_state_has_name():
    assert hasattr(fMS_State, "name")
    descriptor = None
    for klass in fMS_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fms_fsm_is_not_abstract():
    assert not inspect.isabstract(fMS_FSM)


def test_fms_fsm_constructor_exists():
    assert callable(fMS_FSM.__init__)


def test_fms_fsm_constructor_args():
    sig = inspect.signature(fMS_FSM.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_fms_fsm_has_name():
    assert hasattr(fMS_FSM, "name")
    descriptor = None
    for klass in fMS_FSM.__mro__:
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
fMS_FinalState_strategy = st.builds(
    fMS_FinalState,
)
fMS_InitState_strategy = st.builds(
    fMS_InitState,
)
fMS_Transition_strategy = st.builds(
    fMS_Transition,
    name=
        safe_text
)
fMS_State_strategy = st.builds(
    fMS_State,
    name=
        safe_text
)
fMS_FSM_strategy = st.builds(
    fMS_FSM,
    name=
        safe_text
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=fMS_FinalState_strategy)
@settings(max_examples=50)
def test_fms_finalstate_instantiation(instance):
    assert isinstance(instance, fMS_FinalState)

@given(instance=fMS_InitState_strategy)
@settings(max_examples=50)
def test_fms_initstate_instantiation(instance):
    assert isinstance(instance, fMS_InitState)

@given(instance=fMS_Transition_strategy)
@settings(max_examples=50)
def test_fms_transition_instantiation(instance):
    assert isinstance(instance, fMS_Transition)



@given(instance=fMS_Transition_strategy)
def test_fms_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fMS_State_strategy)
@settings(max_examples=50)
def test_fms_state_instantiation(instance):
    assert isinstance(instance, fMS_State)



@given(instance=fMS_State_strategy)
def test_fms_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=fMS_FSM_strategy)
@settings(max_examples=50)
def test_fms_fsm_instantiation(instance):
    assert isinstance(instance, fMS_FSM)



@given(instance=fMS_FSM_strategy)
def test_fms_fsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
