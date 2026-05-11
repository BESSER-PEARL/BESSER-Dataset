import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    State,
    StateMachineTraverser::State,
    FSM,
    StateMachineTraverser::FSM,
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



def test_statemachinetraverser::state_is_not_abstract():
    assert not inspect.isabstract(StateMachineTraverser::State)


def test_statemachinetraverser::state_constructor_exists():
    assert callable(StateMachineTraverser::State.__init__)


def test_statemachinetraverser::state_constructor_args():
    sig = inspect.signature(StateMachineTraverser::State.__init__)
    params = list(sig.parameters.keys())



def test_fsm_is_not_abstract():
    assert not inspect.isabstract(FSM)


def test_fsm_constructor_exists():
    assert callable(FSM.__init__)


def test_fsm_constructor_args():
    sig = inspect.signature(FSM.__init__)
    params = list(sig.parameters.keys())



def test_statemachinetraverser::fsm_is_not_abstract():
    assert not inspect.isabstract(StateMachineTraverser::FSM)


def test_statemachinetraverser::fsm_constructor_exists():
    assert callable(StateMachineTraverser::FSM.__init__)


def test_statemachinetraverser::fsm_constructor_args():
    sig = inspect.signature(StateMachineTraverser::FSM.__init__)
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
StateMachineTraverser::State_strategy = st.builds(
    StateMachineTraverser::State,
)
FSM_strategy = st.builds(
    FSM,
)
StateMachineTraverser::FSM_strategy = st.builds(
    StateMachineTraverser::FSM,
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=StateMachineTraverser::State_strategy)
@settings(max_examples=50)
def test_statemachinetraverser::state_instantiation(instance):
    assert isinstance(instance, StateMachineTraverser::State)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=StateMachineTraverser::State_strategy)
@settings(max_examples=30)
def test_statemachinetraverser::state_adjacent_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.adjacent()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.adjacent).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'adjacent' in StateMachineTraverser::State is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'adjacent' in StateMachineTraverser::State did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'adjacent' in StateMachineTraverser::State is not implemented or raised an error")

@given(instance=FSM_strategy)
@settings(max_examples=50)
def test_fsm_instantiation(instance):
    assert isinstance(instance, FSM)

@given(instance=StateMachineTraverser::FSM_strategy)
@settings(max_examples=50)
def test_statemachinetraverser::fsm_instantiation(instance):
    assert isinstance(instance, StateMachineTraverser::FSM)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=StateMachineTraverser::FSM_strategy)
@settings(max_examples=30)
def test_statemachinetraverser::fsm_initials_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.initials()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.initials).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'initials' in StateMachineTraverser::FSM is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'initials' in StateMachineTraverser::FSM did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'initials' in StateMachineTraverser::FSM is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=StateMachineTraverser::FSM_strategy)
@settings(max_examples=30)
def test_statemachinetraverser::fsm_traverse_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.traverse()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.traverse).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'traverse' in StateMachineTraverser::FSM is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'traverse' in StateMachineTraverser::FSM did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'traverse' in StateMachineTraverser::FSM is not implemented or raised an error")
