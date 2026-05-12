import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    sm_StateMachine,
    sm_Variable,
    sm_State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sm_statemachine_is_not_abstract():
    assert not inspect.isabstract(sm_StateMachine)


def test_sm_statemachine_constructor_exists():
    assert callable(sm_StateMachine.__init__)


def test_sm_statemachine_constructor_args():
    sig = inspect.signature(sm_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_sm_variable_is_not_abstract():
    assert not inspect.isabstract(sm_Variable)


def test_sm_variable_constructor_exists():
    assert callable(sm_Variable.__init__)


def test_sm_variable_constructor_args():
    sig = inspect.signature(sm_Variable.__init__)
    params = list(sig.parameters.keys())



def test_sm_state_is_not_abstract():
    assert not inspect.isabstract(sm_State)


def test_sm_state_constructor_exists():
    assert callable(sm_State.__init__)


def test_sm_state_constructor_args():
    sig = inspect.signature(sm_State.__init__)
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
sm_StateMachine_strategy = st.builds(
    sm_StateMachine,
)
sm_Variable_strategy = st.builds(
    sm_Variable,
)
sm_State_strategy = st.builds(
    sm_State,
)

@given(instance=sm_StateMachine_strategy)
@settings(max_examples=50)
def test_sm_statemachine_instantiation(instance):
    assert isinstance(instance, sm_StateMachine)

@given(instance=sm_Variable_strategy)
@settings(max_examples=50)
def test_sm_variable_instantiation(instance):
    assert isinstance(instance, sm_Variable)

@given(instance=sm_State_strategy)
@settings(max_examples=50)
def test_sm_state_instantiation(instance):
    assert isinstance(instance, sm_State)
