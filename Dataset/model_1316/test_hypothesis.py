import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    metaModelStateMachine::Trigger,
    metaModelStateMachine::Guard,
    metaModelStateMachine::Transition,
    metaModelStateMachine::state,
    metaModelStateMachine::StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_metamodelstatemachine::trigger_is_not_abstract():
    assert not inspect.isabstract(metaModelStateMachine::Trigger)


def test_metamodelstatemachine::trigger_constructor_exists():
    assert callable(metaModelStateMachine::Trigger.__init__)


def test_metamodelstatemachine::trigger_constructor_args():
    sig = inspect.signature(metaModelStateMachine::Trigger.__init__)
    params = list(sig.parameters.keys())



def test_metamodelstatemachine::guard_is_not_abstract():
    assert not inspect.isabstract(metaModelStateMachine::Guard)


def test_metamodelstatemachine::guard_constructor_exists():
    assert callable(metaModelStateMachine::Guard.__init__)


def test_metamodelstatemachine::guard_constructor_args():
    sig = inspect.signature(metaModelStateMachine::Guard.__init__)
    params = list(sig.parameters.keys())



def test_metamodelstatemachine::transition_is_not_abstract():
    assert not inspect.isabstract(metaModelStateMachine::Transition)


def test_metamodelstatemachine::transition_constructor_exists():
    assert callable(metaModelStateMachine::Transition.__init__)


def test_metamodelstatemachine::transition_constructor_args():
    sig = inspect.signature(metaModelStateMachine::Transition.__init__)
    params = list(sig.parameters.keys())



def test_metamodelstatemachine::state_is_not_abstract():
    assert not inspect.isabstract(metaModelStateMachine::state)


def test_metamodelstatemachine::state_constructor_exists():
    assert callable(metaModelStateMachine::state.__init__)


def test_metamodelstatemachine::state_constructor_args():
    sig = inspect.signature(metaModelStateMachine::state.__init__)
    params = list(sig.parameters.keys())



def test_metamodelstatemachine::statemachine_is_not_abstract():
    assert not inspect.isabstract(metaModelStateMachine::StateMachine)


def test_metamodelstatemachine::statemachine_constructor_exists():
    assert callable(metaModelStateMachine::StateMachine.__init__)


def test_metamodelstatemachine::statemachine_constructor_args():
    sig = inspect.signature(metaModelStateMachine::StateMachine.__init__)
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
metaModelStateMachine::Trigger_strategy = st.builds(
    metaModelStateMachine::Trigger,
)
metaModelStateMachine::Guard_strategy = st.builds(
    metaModelStateMachine::Guard,
)
metaModelStateMachine::Transition_strategy = st.builds(
    metaModelStateMachine::Transition,
)
metaModelStateMachine::state_strategy = st.builds(
    metaModelStateMachine::state,
)
metaModelStateMachine::StateMachine_strategy = st.builds(
    metaModelStateMachine::StateMachine,
)

@given(instance=metaModelStateMachine::Trigger_strategy)
@settings(max_examples=50)
def test_metamodelstatemachine::trigger_instantiation(instance):
    assert isinstance(instance, metaModelStateMachine::Trigger)

@given(instance=metaModelStateMachine::Guard_strategy)
@settings(max_examples=50)
def test_metamodelstatemachine::guard_instantiation(instance):
    assert isinstance(instance, metaModelStateMachine::Guard)

@given(instance=metaModelStateMachine::Transition_strategy)
@settings(max_examples=50)
def test_metamodelstatemachine::transition_instantiation(instance):
    assert isinstance(instance, metaModelStateMachine::Transition)

@given(instance=metaModelStateMachine::state_strategy)
@settings(max_examples=50)
def test_metamodelstatemachine::state_instantiation(instance):
    assert isinstance(instance, metaModelStateMachine::state)

@given(instance=metaModelStateMachine::StateMachine_strategy)
@settings(max_examples=50)
def test_metamodelstatemachine::statemachine_instantiation(instance):
    assert isinstance(instance, metaModelStateMachine::StateMachine)
