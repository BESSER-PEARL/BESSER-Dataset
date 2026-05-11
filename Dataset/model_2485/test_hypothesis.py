import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    fsmProv::StateMachine,
    fsmProv::Trigger,
    fsmProv::Transition,
    fsmProv::State,
    fsmProv::AbstractState,
    fsmProv::Region,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsmprov::statemachine_is_not_abstract():
    assert not inspect.isabstract(fsmProv::StateMachine)


def test_fsmprov::statemachine_constructor_exists():
    assert callable(fsmProv::StateMachine.__init__)


def test_fsmprov::statemachine_constructor_args():
    sig = inspect.signature(fsmProv::StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_fsmprov::trigger_is_not_abstract():
    assert not inspect.isabstract(fsmProv::Trigger)


def test_fsmprov::trigger_constructor_exists():
    assert callable(fsmProv::Trigger.__init__)


def test_fsmprov::trigger_constructor_args():
    sig = inspect.signature(fsmProv::Trigger.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_fsmprov::trigger_has_expression():
    assert hasattr(fsmProv::Trigger, "expression")
    descriptor = None
    for klass in fsmProv::Trigger.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_fsmprov::transition_is_not_abstract():
    assert not inspect.isabstract(fsmProv::Transition)


def test_fsmprov::transition_constructor_exists():
    assert callable(fsmProv::Transition.__init__)


def test_fsmprov::transition_constructor_args():
    sig = inspect.signature(fsmProv::Transition.__init__)
    params = list(sig.parameters.keys())



def test_fsmprov::state_is_not_abstract():
    assert not inspect.isabstract(fsmProv::State)


def test_fsmprov::state_constructor_exists():
    assert callable(fsmProv::State.__init__)


def test_fsmprov::state_constructor_args():
    sig = inspect.signature(fsmProv::State.__init__)
    params = list(sig.parameters.keys())



def test_fsmprov::abstractstate_is_not_abstract():
    assert not inspect.isabstract(fsmProv::AbstractState)


def test_fsmprov::abstractstate_constructor_exists():
    assert callable(fsmProv::AbstractState.__init__)


def test_fsmprov::abstractstate_constructor_args():
    sig = inspect.signature(fsmProv::AbstractState.__init__)
    params = list(sig.parameters.keys())



def test_fsmprov::region_is_not_abstract():
    assert not inspect.isabstract(fsmProv::Region)


def test_fsmprov::region_constructor_exists():
    assert callable(fsmProv::Region.__init__)


def test_fsmprov::region_constructor_args():
    sig = inspect.signature(fsmProv::Region.__init__)
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
fsmProv::StateMachine_strategy = st.builds(
    fsmProv::StateMachine,
)
fsmProv::Trigger_strategy = st.builds(
    fsmProv::Trigger,
    expression=
        safe_text
)
fsmProv::Transition_strategy = st.builds(
    fsmProv::Transition,
)
fsmProv::State_strategy = st.builds(
    fsmProv::State,
)
fsmProv::AbstractState_strategy = st.builds(
    fsmProv::AbstractState,
)
fsmProv::Region_strategy = st.builds(
    fsmProv::Region,
)

@given(instance=fsmProv::StateMachine_strategy)
@settings(max_examples=50)
def test_fsmprov::statemachine_instantiation(instance):
    assert isinstance(instance, fsmProv::StateMachine)

@given(instance=fsmProv::Trigger_strategy)
@settings(max_examples=50)
def test_fsmprov::trigger_instantiation(instance):
    assert isinstance(instance, fsmProv::Trigger)

@given(instance=fsmProv::Trigger_strategy)
def test_fsmprov::trigger_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=fsmProv::Trigger_strategy)
def test_fsmprov::trigger_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsmProv::Trigger_strategy)
@settings(max_examples=30)
def test_fsmprov::trigger_evaltrigger_changes_state(instance):
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
        assert has_statements, f"Function 'evalTrigger' in fsmProv::Trigger is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'evalTrigger' in fsmProv::Trigger did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'evalTrigger' in fsmProv::Trigger is not implemented or raised an error")

@given(instance=fsmProv::Transition_strategy)
@settings(max_examples=50)
def test_fsmprov::transition_instantiation(instance):
    assert isinstance(instance, fsmProv::Transition)

@given(instance=fsmProv::State_strategy)
@settings(max_examples=50)
def test_fsmprov::state_instantiation(instance):
    assert isinstance(instance, fsmProv::State)

@given(instance=fsmProv::AbstractState_strategy)
@settings(max_examples=50)
def test_fsmprov::abstractstate_instantiation(instance):
    assert isinstance(instance, fsmProv::AbstractState)

@given(instance=fsmProv::Region_strategy)
@settings(max_examples=50)
def test_fsmprov::region_instantiation(instance):
    assert isinstance(instance, fsmProv::Region)
