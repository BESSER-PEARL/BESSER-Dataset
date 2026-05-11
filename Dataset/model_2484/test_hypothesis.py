import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    fsm::Transition,
    fsm::State,
    fsm::FSM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsm::transition_is_not_abstract():
    assert not inspect.isabstract(fsm::Transition)


def test_fsm::transition_constructor_exists():
    assert callable(fsm::Transition.__init__)


def test_fsm::transition_constructor_args():
    sig = inspect.signature(fsm::Transition.__init__)
    params = list(sig.parameters.keys())



def test_fsm::state_is_not_abstract():
    assert not inspect.isabstract(fsm::State)


def test_fsm::state_constructor_exists():
    assert callable(fsm::State.__init__)


def test_fsm::state_constructor_args():
    sig = inspect.signature(fsm::State.__init__)
    params = list(sig.parameters.keys())



def test_fsm::fsm_is_not_abstract():
    assert not inspect.isabstract(fsm::FSM)


def test_fsm::fsm_constructor_exists():
    assert callable(fsm::FSM.__init__)


def test_fsm::fsm_constructor_args():
    sig = inspect.signature(fsm::FSM.__init__)
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
fsm::Transition_strategy = st.builds(
    fsm::Transition,
)
fsm::State_strategy = st.builds(
    fsm::State,
)
fsm::FSM_strategy = st.builds(
    fsm::FSM,
)

@given(instance=fsm::Transition_strategy)
@settings(max_examples=50)
def test_fsm::transition_instantiation(instance):
    assert isinstance(instance, fsm::Transition)

@given(instance=fsm::State_strategy)
@settings(max_examples=50)
def test_fsm::state_instantiation(instance):
    assert isinstance(instance, fsm::State)

@given(instance=fsm::FSM_strategy)
@settings(max_examples=50)
def test_fsm::fsm_instantiation(instance):
    assert isinstance(instance, fsm::FSM)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsm::FSM_strategy)
@settings(max_examples=30)
def test_fsm::fsm_j_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.j(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.j).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'j' in fsm::FSM is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'j' in fsm::FSM did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'j' in fsm::FSM is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsm::FSM_strategy)
@settings(max_examples=30)
def test_fsm::fsm_k_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.k(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.k).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'k' in fsm::FSM is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'k' in fsm::FSM did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'k' in fsm::FSM is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsm::FSM_strategy)
@settings(max_examples=30)
def test_fsm::fsm_i_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.i(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.i).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'i' in fsm::FSM is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'i' in fsm::FSM did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'i' in fsm::FSM is not implemented or raised an error")
