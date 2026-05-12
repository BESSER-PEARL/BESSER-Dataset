import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    metaModelStateMachine_Trigger,
    metaModelStateMachine_Guard,
    metaModelStateMachine_Transition,
    metaModelStateMachine_state,
    metaModelStateMachine_StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_metamodelstatemachine_trigger_is_not_abstract():
    assert not inspect.isabstract(metaModelStateMachine_Trigger)


def test_metamodelstatemachine_trigger_constructor_exists():
    assert callable(metaModelStateMachine_Trigger.__init__)


def test_metamodelstatemachine_trigger_constructor_args():
    sig = inspect.signature(metaModelStateMachine_Trigger.__init__)
    params = list(sig.parameters.keys())



def test_metamodelstatemachine_guard_is_not_abstract():
    assert not inspect.isabstract(metaModelStateMachine_Guard)


def test_metamodelstatemachine_guard_constructor_exists():
    assert callable(metaModelStateMachine_Guard.__init__)


def test_metamodelstatemachine_guard_constructor_args():
    sig = inspect.signature(metaModelStateMachine_Guard.__init__)
    params = list(sig.parameters.keys())



def test_metamodelstatemachine_transition_is_not_abstract():
    assert not inspect.isabstract(metaModelStateMachine_Transition)


def test_metamodelstatemachine_transition_constructor_exists():
    assert callable(metaModelStateMachine_Transition.__init__)


def test_metamodelstatemachine_transition_constructor_args():
    sig = inspect.signature(metaModelStateMachine_Transition.__init__)
    params = list(sig.parameters.keys())



def test_metamodelstatemachine_state_is_not_abstract():
    assert not inspect.isabstract(metaModelStateMachine_state)


def test_metamodelstatemachine_state_constructor_exists():
    assert callable(metaModelStateMachine_state.__init__)


def test_metamodelstatemachine_state_constructor_args():
    sig = inspect.signature(metaModelStateMachine_state.__init__)
    params = list(sig.parameters.keys())



def test_metamodelstatemachine_statemachine_is_not_abstract():
    assert not inspect.isabstract(metaModelStateMachine_StateMachine)


def test_metamodelstatemachine_statemachine_constructor_exists():
    assert callable(metaModelStateMachine_StateMachine.__init__)


def test_metamodelstatemachine_statemachine_constructor_args():
    sig = inspect.signature(metaModelStateMachine_StateMachine.__init__)
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
metaModelStateMachine_Trigger_strategy = st.builds(
    metaModelStateMachine_Trigger,
)
metaModelStateMachine_Guard_strategy = st.builds(
    metaModelStateMachine_Guard,
)
metaModelStateMachine_Transition_strategy = st.builds(
    metaModelStateMachine_Transition,
)
metaModelStateMachine_state_strategy = st.builds(
    metaModelStateMachine_state,
)
metaModelStateMachine_StateMachine_strategy = st.builds(
    metaModelStateMachine_StateMachine,
)

@given(instance=metaModelStateMachine_Trigger_strategy)
@settings(max_examples=50)
def test_metamodelstatemachine_trigger_instantiation(instance):
    assert isinstance(instance, metaModelStateMachine_Trigger)

@given(instance=metaModelStateMachine_Guard_strategy)
@settings(max_examples=50)
def test_metamodelstatemachine_guard_instantiation(instance):
    assert isinstance(instance, metaModelStateMachine_Guard)

@given(instance=metaModelStateMachine_Transition_strategy)
@settings(max_examples=50)
def test_metamodelstatemachine_transition_instantiation(instance):
    assert isinstance(instance, metaModelStateMachine_Transition)

@given(instance=metaModelStateMachine_state_strategy)
@settings(max_examples=50)
def test_metamodelstatemachine_state_instantiation(instance):
    assert isinstance(instance, metaModelStateMachine_state)

@given(instance=metaModelStateMachine_StateMachine_strategy)
@settings(max_examples=50)
def test_metamodelstatemachine_statemachine_instantiation(instance):
    assert isinstance(instance, metaModelStateMachine_StateMachine)
