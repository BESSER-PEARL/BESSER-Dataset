import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    State,
    HSM_FinalState,
    HSM_InitialState,
    HSM_CompositeState,
    HSM_State,
    HSM_StateMachine,
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



def test_hsm_finalstate_is_not_abstract():
    assert not inspect.isabstract(HSM_FinalState)


def test_hsm_finalstate_constructor_exists():
    assert callable(HSM_FinalState.__init__)


def test_hsm_finalstate_constructor_args():
    sig = inspect.signature(HSM_FinalState.__init__)
    params = list(sig.parameters.keys())



def test_hsm_initialstate_is_not_abstract():
    assert not inspect.isabstract(HSM_InitialState)


def test_hsm_initialstate_constructor_exists():
    assert callable(HSM_InitialState.__init__)


def test_hsm_initialstate_constructor_args():
    sig = inspect.signature(HSM_InitialState.__init__)
    params = list(sig.parameters.keys())



def test_hsm_compositestate_is_not_abstract():
    assert not inspect.isabstract(HSM_CompositeState)


def test_hsm_compositestate_constructor_exists():
    assert callable(HSM_CompositeState.__init__)


def test_hsm_compositestate_constructor_args():
    sig = inspect.signature(HSM_CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_hsm_state_is_not_abstract():
    assert not inspect.isabstract(HSM_State)


def test_hsm_state_constructor_exists():
    assert callable(HSM_State.__init__)


def test_hsm_state_constructor_args():
    sig = inspect.signature(HSM_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hsm_state_has_name():
    assert hasattr(HSM_State, "name")
    descriptor = None
    for klass in HSM_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hsm_statemachine_is_not_abstract():
    assert not inspect.isabstract(HSM_StateMachine)


def test_hsm_statemachine_constructor_exists():
    assert callable(HSM_StateMachine.__init__)


def test_hsm_statemachine_constructor_args():
    sig = inspect.signature(HSM_StateMachine.__init__)
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
State_strategy = st.builds(
    State,
)
HSM_FinalState_strategy = st.builds(
    HSM_FinalState,
)
HSM_InitialState_strategy = st.builds(
    HSM_InitialState,
)
HSM_CompositeState_strategy = st.builds(
    HSM_CompositeState,
)
HSM_State_strategy = st.builds(
    HSM_State,
    name=
        safe_text
)
HSM_StateMachine_strategy = st.builds(
    HSM_StateMachine,
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=HSM_FinalState_strategy)
@settings(max_examples=50)
def test_hsm_finalstate_instantiation(instance):
    assert isinstance(instance, HSM_FinalState)

@given(instance=HSM_InitialState_strategy)
@settings(max_examples=50)
def test_hsm_initialstate_instantiation(instance):
    assert isinstance(instance, HSM_InitialState)

@given(instance=HSM_CompositeState_strategy)
@settings(max_examples=50)
def test_hsm_compositestate_instantiation(instance):
    assert isinstance(instance, HSM_CompositeState)

@given(instance=HSM_State_strategy)
@settings(max_examples=50)
def test_hsm_state_instantiation(instance):
    assert isinstance(instance, HSM_State)



@given(instance=HSM_State_strategy)
def test_hsm_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HSM_StateMachine_strategy)
@settings(max_examples=50)
def test_hsm_statemachine_instantiation(instance):
    assert isinstance(instance, HSM_StateMachine)
