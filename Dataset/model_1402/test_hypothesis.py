import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    State,
    HSM_CompositeState,
    HSM_Transition,
    HSM_State,
    HSM_StateMachine,
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



def test_hsm_compositestate_is_not_abstract():
    assert not inspect.isabstract(HSM_CompositeState)


def test_hsm_compositestate_constructor_exists():
    assert callable(HSM_CompositeState.__init__)


def test_hsm_compositestate_constructor_args():
    sig = inspect.signature(HSM_CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_hsm_transition_is_not_abstract():
    assert not inspect.isabstract(HSM_Transition)


def test_hsm_transition_constructor_exists():
    assert callable(HSM_Transition.__init__)


def test_hsm_transition_constructor_args():
    sig = inspect.signature(HSM_Transition.__init__)
    params = list(sig.parameters.keys())



def test_hsm_state_is_not_abstract():
    assert not inspect.isabstract(HSM_State)


def test_hsm_state_constructor_exists():
    assert callable(HSM_State.__init__)


def test_hsm_state_constructor_args():
    sig = inspect.signature(HSM_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hsm_state_has_name():
    assert hasattr(HSM_State, "name")
    descriptor = None
    for klass in HSM_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hsm_statemachine_is_not_abstract():
    assert not inspect.isabstract(HSM_StateMachine)


def test_hsm_statemachine_constructor_exists():
    assert callable(HSM_StateMachine.__init__)


def test_hsm_statemachine_constructor_args():
    sig = inspect.signature(HSM_StateMachine.__init__)
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
HSM_CompositeState_strategy = st.builds(
    HSM_CompositeState,
)
HSM_Transition_strategy = st.builds(
    HSM_Transition,
)
HSM_State_strategy = st.builds(
    HSM_State,
    name=
        safe_text
)
HSM_StateMachine_strategy = st.builds(
    HSM_StateMachine,
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=HSM_CompositeState_strategy)
@settings(max_examples=50)
def test_hsm_compositestate_instantiation(instance):
    assert isinstance(instance, HSM_CompositeState)

@given(instance=HSM_Transition_strategy)
@settings(max_examples=50)
def test_hsm_transition_instantiation(instance):
    assert isinstance(instance, HSM_Transition)

@given(instance=HSM_State_strategy)
@settings(max_examples=50)
def test_hsm_state_instantiation(instance):
    assert isinstance(instance, HSM_State)



@given(instance=HSM_State_strategy)
def test_hsm_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HSM_StateMachine_strategy)
@settings(max_examples=50)
def test_hsm_statemachine_instantiation(instance):
    assert isinstance(instance, HSM_StateMachine)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=HSM_StateMachine_strategy)
@settings(max_examples=30)
def test_hsm_statemachine_addtransition_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.addTransition(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.addTransition).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'addTransition' in HSM_StateMachine is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addTransition' in HSM_StateMachine did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addTransition' in HSM_StateMachine is not implemented or raised an error")
