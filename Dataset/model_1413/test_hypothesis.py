import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    NHSM_Transition,
    NHSM_State,
    NHSM_StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_nhsm_transition_is_not_abstract():
    assert not inspect.isabstract(NHSM_Transition)


def test_nhsm_transition_constructor_exists():
    assert callable(NHSM_Transition.__init__)


def test_nhsm_transition_constructor_args():
    sig = inspect.signature(NHSM_Transition.__init__)
    params = list(sig.parameters.keys())



def test_nhsm_state_is_not_abstract():
    assert not inspect.isabstract(NHSM_State)


def test_nhsm_state_constructor_exists():
    assert callable(NHSM_State.__init__)


def test_nhsm_state_constructor_args():
    sig = inspect.signature(NHSM_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_nhsm_state_has_name():
    assert hasattr(NHSM_State, "name")
    descriptor = None
    for klass in NHSM_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_nhsm_statemachine_is_not_abstract():
    assert not inspect.isabstract(NHSM_StateMachine)


def test_nhsm_statemachine_constructor_exists():
    assert callable(NHSM_StateMachine.__init__)


def test_nhsm_statemachine_constructor_args():
    sig = inspect.signature(NHSM_StateMachine.__init__)
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
NHSM_Transition_strategy = st.builds(
    NHSM_Transition,
)
NHSM_State_strategy = st.builds(
    NHSM_State,
    name=
        safe_text
)
NHSM_StateMachine_strategy = st.builds(
    NHSM_StateMachine,
)

@given(instance=NHSM_Transition_strategy)
@settings(max_examples=50)
def test_nhsm_transition_instantiation(instance):
    assert isinstance(instance, NHSM_Transition)

@given(instance=NHSM_State_strategy)
@settings(max_examples=50)
def test_nhsm_state_instantiation(instance):
    assert isinstance(instance, NHSM_State)



@given(instance=NHSM_State_strategy)
def test_nhsm_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NHSM_StateMachine_strategy)
@settings(max_examples=50)
def test_nhsm_statemachine_instantiation(instance):
    assert isinstance(instance, NHSM_StateMachine)
