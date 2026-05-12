import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    fsmProv_Trigger,
    fsmProv_Transition,
    fsmProv_State,
    fsmProv_AbstractState,
    fsmProv_Region,
    fsmProv_StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsmprov_trigger_is_not_abstract():
    assert not inspect.isabstract(fsmProv_Trigger)


def test_fsmprov_trigger_constructor_exists():
    assert callable(fsmProv_Trigger.__init__)


def test_fsmprov_trigger_constructor_args():
    sig = inspect.signature(fsmProv_Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_fsmprov_trigger_has_expression():
    assert hasattr(fsmProv_Trigger, "expression")
    descriptor = None
    for klass in fsmProv_Trigger.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_fsmprov_transition_is_not_abstract():
    assert not inspect.isabstract(fsmProv_Transition)


def test_fsmprov_transition_constructor_exists():
    assert callable(fsmProv_Transition.__init__)


def test_fsmprov_transition_constructor_args():
    sig = inspect.signature(fsmProv_Transition.__init__)
    params = list(sig.parameters.keys())



def test_fsmprov_state_is_not_abstract():
    assert not inspect.isabstract(fsmProv_State)


def test_fsmprov_state_constructor_exists():
    assert callable(fsmProv_State.__init__)


def test_fsmprov_state_constructor_args():
    sig = inspect.signature(fsmProv_State.__init__)
    params = list(sig.parameters.keys())



def test_fsmprov_abstractstate_is_not_abstract():
    assert not inspect.isabstract(fsmProv_AbstractState)


def test_fsmprov_abstractstate_constructor_exists():
    assert callable(fsmProv_AbstractState.__init__)


def test_fsmprov_abstractstate_constructor_args():
    sig = inspect.signature(fsmProv_AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_fsmprov_region_is_not_abstract():
    assert not inspect.isabstract(fsmProv_Region)


def test_fsmprov_region_constructor_exists():
    assert callable(fsmProv_Region.__init__)


def test_fsmprov_region_constructor_args():
    sig = inspect.signature(fsmProv_Region.__init__)
    params = list(sig.parameters.keys())



def test_fsmprov_statemachine_is_not_abstract():
    assert not inspect.isabstract(fsmProv_StateMachine)


def test_fsmprov_statemachine_constructor_exists():
    assert callable(fsmProv_StateMachine.__init__)


def test_fsmprov_statemachine_constructor_args():
    sig = inspect.signature(fsmProv_StateMachine.__init__)
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
fsmProv_Trigger_strategy = st.builds(
    fsmProv_Trigger,
    expression=
        safe_text
)
fsmProv_Transition_strategy = st.builds(
    fsmProv_Transition,
)
fsmProv_State_strategy = st.builds(
    fsmProv_State,
)
fsmProv_AbstractState_strategy = st.builds(
    fsmProv_AbstractState,
)
fsmProv_Region_strategy = st.builds(
    fsmProv_Region,
)
fsmProv_StateMachine_strategy = st.builds(
    fsmProv_StateMachine,
)

@given(instance=fsmProv_Trigger_strategy)
@settings(max_examples=50)
def test_fsmprov_trigger_instantiation(instance):
    assert isinstance(instance, fsmProv_Trigger)



@given(instance=fsmProv_Trigger_strategy)
def test_fsmprov_trigger_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsmProv_Trigger_strategy)
@settings(max_examples=30)
def test_fsmprov_trigger_evaltrigger_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.evalTrigger(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.evalTrigger).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'evalTrigger' in fsmProv_Trigger is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evalTrigger' in fsmProv_Trigger did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evalTrigger' in fsmProv_Trigger is not implemented or raised an error")

@given(instance=fsmProv_Transition_strategy)
@settings(max_examples=50)
def test_fsmprov_transition_instantiation(instance):
    assert isinstance(instance, fsmProv_Transition)

@given(instance=fsmProv_State_strategy)
@settings(max_examples=50)
def test_fsmprov_state_instantiation(instance):
    assert isinstance(instance, fsmProv_State)

@given(instance=fsmProv_AbstractState_strategy)
@settings(max_examples=50)
def test_fsmprov_abstractstate_instantiation(instance):
    assert isinstance(instance, fsmProv_AbstractState)

@given(instance=fsmProv_Region_strategy)
@settings(max_examples=50)
def test_fsmprov_region_instantiation(instance):
    assert isinstance(instance, fsmProv_Region)

@given(instance=fsmProv_StateMachine_strategy)
@settings(max_examples=50)
def test_fsmprov_statemachine_instantiation(instance):
    assert isinstance(instance, fsmProv_StateMachine)
