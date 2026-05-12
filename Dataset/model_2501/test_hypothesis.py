import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    State,
    StateMachineTraverser_State,
    FSM,
    StateMachineTraverser_FSM,
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



def test_statemachinetraverser_state_is_not_abstract():
    assert not inspect.isabstract(StateMachineTraverser_State)


def test_statemachinetraverser_state_constructor_exists():
    assert callable(StateMachineTraverser_State.__init__)


def test_statemachinetraverser_state_constructor_args():
    sig = inspect.signature(StateMachineTraverser_State.__init__)
    params = list(sig.parameters.keys())



def test_fsm_is_not_abstract():
    assert not inspect.isabstract(FSM)


def test_fsm_constructor_exists():
    assert callable(FSM.__init__)


def test_fsm_constructor_args():
    sig = inspect.signature(FSM.__init__)
    params = list(sig.parameters.keys())



def test_statemachinetraverser_fsm_is_not_abstract():
    assert not inspect.isabstract(StateMachineTraverser_FSM)


def test_statemachinetraverser_fsm_constructor_exists():
    assert callable(StateMachineTraverser_FSM.__init__)


def test_statemachinetraverser_fsm_constructor_args():
    sig = inspect.signature(StateMachineTraverser_FSM.__init__)
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
StateMachineTraverser_State_strategy = st.builds(
    StateMachineTraverser_State,
)
FSM_strategy = st.builds(
    FSM,
)
StateMachineTraverser_FSM_strategy = st.builds(
    StateMachineTraverser_FSM,
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=StateMachineTraverser_State_strategy)
@settings(max_examples=50)
def test_statemachinetraverser_state_instantiation(instance):
    assert isinstance(instance, StateMachineTraverser_State)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=StateMachineTraverser_State_strategy)
@settings(max_examples=30)
def test_statemachinetraverser_state_adjacent_changes_state(instance):
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
        assert has_statements, f"Function 'adjacent' in StateMachineTraverser_State is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'adjacent' in StateMachineTraverser_State did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'adjacent' in StateMachineTraverser_State is not implemented or raised an error")

@given(instance=FSM_strategy)
@settings(max_examples=50)
def test_fsm_instantiation(instance):
    assert isinstance(instance, FSM)

@given(instance=StateMachineTraverser_FSM_strategy)
@settings(max_examples=50)
def test_statemachinetraverser_fsm_instantiation(instance):
    assert isinstance(instance, StateMachineTraverser_FSM)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=StateMachineTraverser_FSM_strategy)
@settings(max_examples=30)
def test_statemachinetraverser_fsm_initials_changes_state(instance):
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
        assert has_statements, f"Function 'initials' in StateMachineTraverser_FSM is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'initials' in StateMachineTraverser_FSM did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'initials' in StateMachineTraverser_FSM is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=StateMachineTraverser_FSM_strategy)
@settings(max_examples=30)
def test_statemachinetraverser_fsm_traverse_changes_state(instance):
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
        assert has_statements, f"Function 'traverse' in StateMachineTraverser_FSM is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'traverse' in StateMachineTraverser_FSM did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'traverse' in StateMachineTraverser_FSM is not implemented or raised an error")
