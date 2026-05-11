import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    sm::StateMachine,
    sm::Variable,
    sm::State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sm::statemachine_is_not_abstract():
    assert not inspect.isabstract(sm::StateMachine)


def test_sm::statemachine_constructor_exists():
    assert callable(sm::StateMachine.__init__)


def test_sm::statemachine_constructor_args():
    sig = inspect.signature(sm::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_sm::variable_is_not_abstract():
    assert not inspect.isabstract(sm::Variable)


def test_sm::variable_constructor_exists():
    assert callable(sm::Variable.__init__)


def test_sm::variable_constructor_args():
    sig = inspect.signature(sm::Variable.__init__)
    params = list(sig.parameters.keys())



def test_sm::state_is_not_abstract():
    assert not inspect.isabstract(sm::State)


def test_sm::state_constructor_exists():
    assert callable(sm::State.__init__)


def test_sm::state_constructor_args():
    sig = inspect.signature(sm::State.__init__)
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
sm::StateMachine_strategy = st.builds(
    sm::StateMachine,
)
sm::Variable_strategy = st.builds(
    sm::Variable,
)
sm::State_strategy = st.builds(
    sm::State,
)

@given(instance=sm::StateMachine_strategy)
@settings(max_examples=50)
def test_sm::statemachine_instantiation(instance):
    assert isinstance(instance, sm::StateMachine)

@given(instance=sm::Variable_strategy)
@settings(max_examples=50)
def test_sm::variable_instantiation(instance):
    assert isinstance(instance, sm::Variable)

@given(instance=sm::State_strategy)
@settings(max_examples=50)
def test_sm::state_instantiation(instance):
    assert isinstance(instance, sm::State)
