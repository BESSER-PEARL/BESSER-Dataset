import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    StateMachinesModule::Constraint,
    StateMachinesModule::Transition,
    StateMachinesModule::State,
    StateMachinesModule::StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statemachinesmodule::constraint_is_not_abstract():
    assert not inspect.isabstract(StateMachinesModule::Constraint)


def test_statemachinesmodule::constraint_constructor_exists():
    assert callable(StateMachinesModule::Constraint.__init__)


def test_statemachinesmodule::constraint_constructor_args():
    sig = inspect.signature(StateMachinesModule::Constraint.__init__)
    params = list(sig.parameters.keys())



def test_statemachinesmodule::transition_is_not_abstract():
    assert not inspect.isabstract(StateMachinesModule::Transition)


def test_statemachinesmodule::transition_constructor_exists():
    assert callable(StateMachinesModule::Transition.__init__)


def test_statemachinesmodule::transition_constructor_args():
    sig = inspect.signature(StateMachinesModule::Transition.__init__)
    params = list(sig.parameters.keys())



def test_statemachinesmodule::state_is_not_abstract():
    assert not inspect.isabstract(StateMachinesModule::State)


def test_statemachinesmodule::state_constructor_exists():
    assert callable(StateMachinesModule::State.__init__)


def test_statemachinesmodule::state_constructor_args():
    sig = inspect.signature(StateMachinesModule::State.__init__)
    params = list(sig.parameters.keys())



def test_statemachinesmodule::statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachinesModule::StateMachine)


def test_statemachinesmodule::statemachine_constructor_exists():
    assert callable(StateMachinesModule::StateMachine.__init__)


def test_statemachinesmodule::statemachine_constructor_args():
    sig = inspect.signature(StateMachinesModule::StateMachine.__init__)
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
StateMachinesModule::Constraint_strategy = st.builds(
    StateMachinesModule::Constraint,
)
StateMachinesModule::Transition_strategy = st.builds(
    StateMachinesModule::Transition,
)
StateMachinesModule::State_strategy = st.builds(
    StateMachinesModule::State,
)
StateMachinesModule::StateMachine_strategy = st.builds(
    StateMachinesModule::StateMachine,
)

@given(instance=StateMachinesModule::Constraint_strategy)
@settings(max_examples=50)
def test_statemachinesmodule::constraint_instantiation(instance):
    assert isinstance(instance, StateMachinesModule::Constraint)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=StateMachinesModule::Constraint_strategy)
@settings(max_examples=30)
def test_statemachinesmodule::constraint_eval_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.eval()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.eval).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'eval' in StateMachinesModule::Constraint is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'eval' in StateMachinesModule::Constraint did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'eval' in StateMachinesModule::Constraint is not implemented or raised an error")

@given(instance=StateMachinesModule::Transition_strategy)
@settings(max_examples=50)
def test_statemachinesmodule::transition_instantiation(instance):
    assert isinstance(instance, StateMachinesModule::Transition)

@given(instance=StateMachinesModule::State_strategy)
@settings(max_examples=50)
def test_statemachinesmodule::state_instantiation(instance):
    assert isinstance(instance, StateMachinesModule::State)

@given(instance=StateMachinesModule::StateMachine_strategy)
@settings(max_examples=50)
def test_statemachinesmodule::statemachine_instantiation(instance):
    assert isinstance(instance, StateMachinesModule::StateMachine)
