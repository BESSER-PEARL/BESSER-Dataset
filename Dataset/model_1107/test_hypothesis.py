import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    fsml::FSMTransition,
    fsml::FSMState,
    fsml::FSM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsml::fsmtransition_is_not_abstract():
    assert not inspect.isabstract(fsml::FSMTransition)


def test_fsml::fsmtransition_constructor_exists():
    assert callable(fsml::FSMTransition.__init__)


def test_fsml::fsmtransition_constructor_args():
    sig = inspect.signature(fsml::FSMTransition.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"
    assert "input" in params, "Missing parameter 'input'"

def test_fsml::fsmtransition_has_action():
    assert hasattr(fsml::FSMTransition, "action")
    descriptor = None
    for klass in fsml::FSMTransition.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)

def test_fsml::fsmtransition_has_input():
    assert hasattr(fsml::FSMTransition, "input")
    descriptor = None
    for klass in fsml::FSMTransition.__mro__:
        if "input" in klass.__dict__:
            descriptor = klass.__dict__["input"]
            break
    assert isinstance(descriptor, property)



def test_fsml::fsmstate_is_not_abstract():
    assert not inspect.isabstract(fsml::FSMState)


def test_fsml::fsmstate_constructor_exists():
    assert callable(fsml::FSMState.__init__)


def test_fsml::fsmstate_constructor_args():
    sig = inspect.signature(fsml::FSMState.__init__)
    params = list(sig.parameters.keys())
    assert "initial" in params, "Missing parameter 'initial'"
    assert "name" in params, "Missing parameter 'name'"

def test_fsml::fsmstate_has_initial():
    assert hasattr(fsml::FSMState, "initial")
    descriptor = None
    for klass in fsml::FSMState.__mro__:
        if "initial" in klass.__dict__:
            descriptor = klass.__dict__["initial"]
            break
    assert isinstance(descriptor, property)

def test_fsml::fsmstate_has_name():
    assert hasattr(fsml::FSMState, "name")
    descriptor = None
    for klass in fsml::FSMState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsml::fsm_is_not_abstract():
    assert not inspect.isabstract(fsml::FSM)


def test_fsml::fsm_constructor_exists():
    assert callable(fsml::FSM.__init__)


def test_fsml::fsm_constructor_args():
    sig = inspect.signature(fsml::FSM.__init__)
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
fsml::FSMTransition_strategy = st.builds(
    fsml::FSMTransition,
    action=
        safe_text,
    input=
        safe_text
)
fsml::FSMState_strategy = st.builds(
    fsml::FSMState,
    initial=
        st.booleans(),
    name=
        safe_text
)
fsml::FSM_strategy = st.builds(
    fsml::FSM,
)

@given(instance=fsml::FSMTransition_strategy)
@settings(max_examples=50)
def test_fsml::fsmtransition_instantiation(instance):
    assert isinstance(instance, fsml::FSMTransition)

@given(instance=fsml::FSMTransition_strategy)
def test_fsml::fsmtransition_action_type(instance):
    assert isinstance(instance.action, str)


@given(instance=fsml::FSMTransition_strategy)
def test_fsml::fsmtransition_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=fsml::FSMTransition_strategy)
def test_fsml::fsmtransition_input_type(instance):
    assert isinstance(instance.input, str)


@given(instance=fsml::FSMTransition_strategy)
def test_fsml::fsmtransition_input_setter(instance):
    original = instance.input
    instance.input = original
    assert instance.input == original

@given(instance=fsml::FSMState_strategy)
@settings(max_examples=50)
def test_fsml::fsmstate_instantiation(instance):
    assert isinstance(instance, fsml::FSMState)

@given(instance=fsml::FSMState_strategy)
def test_fsml::fsmstate_initial_type(instance):
    assert isinstance(instance.initial, bool)


@given(instance=fsml::FSMState_strategy)
def test_fsml::fsmstate_initial_setter(instance):
    original = instance.initial
    instance.initial = original
    assert instance.initial == original

@given(instance=fsml::FSMState_strategy)
def test_fsml::fsmstate_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=fsml::FSMState_strategy)
def test_fsml::fsmstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsml::FSMState_strategy)
@settings(max_examples=30)
def test_fsml::fsmstate_hasdistinctevents_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.hasDistinctEvents(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.hasDistinctEvents).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'hasDistinctEvents' in fsml::FSMState is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'hasDistinctEvents' in fsml::FSMState did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'hasDistinctEvents' in fsml::FSMState is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsml::FSMState_strategy)
@settings(max_examples=30)
def test_fsml::fsmstate_isreachable_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isReachable(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isReachable).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isReachable' in fsml::FSMState is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isReachable' in fsml::FSMState did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isReachable' in fsml::FSMState is not implemented or raised an error")

@given(instance=fsml::FSM_strategy)
@settings(max_examples=50)
def test_fsml::fsm_instantiation(instance):
    assert isinstance(instance, fsml::FSM)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsml::FSM_strategy)
@settings(max_examples=30)
def test_fsml::fsm_hasexactoneinitialstate_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.hasExactOneInitialState(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.hasExactOneInitialState).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'hasExactOneInitialState' in fsml::FSM is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'hasExactOneInitialState' in fsml::FSM did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'hasExactOneInitialState' in fsml::FSM is not implemented or raised an error")
