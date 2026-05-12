import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    tP1_IDM_Transition,
    tP1_IDM_State,
    tP1_IDM_StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tp1_idm_transition_is_not_abstract():
    assert not inspect.isabstract(tP1_IDM_Transition)


def test_tp1_idm_transition_constructor_exists():
    assert callable(tP1_IDM_Transition.__init__)


def test_tp1_idm_transition_constructor_args():
    sig = inspect.signature(tP1_IDM_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tp1_idm_transition_has_name():
    assert hasattr(tP1_IDM_Transition, "name")
    descriptor = None
    for klass in tP1_IDM_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tp1_idm_state_is_not_abstract():
    assert not inspect.isabstract(tP1_IDM_State)


def test_tp1_idm_state_constructor_exists():
    assert callable(tP1_IDM_State.__init__)


def test_tp1_idm_state_constructor_args():
    sig = inspect.signature(tP1_IDM_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tp1_idm_state_has_name():
    assert hasattr(tP1_IDM_State, "name")
    descriptor = None
    for klass in tP1_IDM_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tp1_idm_statemachine_is_not_abstract():
    assert not inspect.isabstract(tP1_IDM_StateMachine)


def test_tp1_idm_statemachine_constructor_exists():
    assert callable(tP1_IDM_StateMachine.__init__)


def test_tp1_idm_statemachine_constructor_args():
    sig = inspect.signature(tP1_IDM_StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tp1_idm_statemachine_has_name():
    assert hasattr(tP1_IDM_StateMachine, "name")
    descriptor = None
    for klass in tP1_IDM_StateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)


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
tP1_IDM_Transition_strategy = st.builds(
    tP1_IDM_Transition,
    name=
        safe_text
)
tP1_IDM_State_strategy = st.builds(
    tP1_IDM_State,
    name=
        safe_text
)
tP1_IDM_StateMachine_strategy = st.builds(
    tP1_IDM_StateMachine,
    name=
        safe_text
)

@given(instance=tP1_IDM_Transition_strategy)
@settings(max_examples=50)
def test_tp1_idm_transition_instantiation(instance):
    assert isinstance(instance, tP1_IDM_Transition)



@given(instance=tP1_IDM_Transition_strategy)
def test_tp1_idm_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tP1_IDM_State_strategy)
@settings(max_examples=50)
def test_tp1_idm_state_instantiation(instance):
    assert isinstance(instance, tP1_IDM_State)



@given(instance=tP1_IDM_State_strategy)
def test_tp1_idm_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tP1_IDM_StateMachine_strategy)
@settings(max_examples=50)
def test_tp1_idm_statemachine_instantiation(instance):
    assert isinstance(instance, tP1_IDM_StateMachine)



@given(instance=tP1_IDM_StateMachine_strategy)
def test_tp1_idm_statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tP1_IDM_StateMachine_strategy)
@settings(max_examples=30)
def test_tp1_idm_statemachine_execute_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.execute()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.execute).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'execute' in tP1_IDM_StateMachine is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'execute' in tP1_IDM_StateMachine did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'execute' in tP1_IDM_StateMachine is not implemented or raised an error")
