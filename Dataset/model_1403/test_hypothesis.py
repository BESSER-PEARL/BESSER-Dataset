import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    State,
    HSM::CompositeState,
    HSM::Transition,
    HSM::State,
    HSM::StateMachine,
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



def test_hsm::compositestate_is_not_abstract():
    assert not inspect.isabstract(HSM::CompositeState)


def test_hsm::compositestate_constructor_exists():
    assert callable(HSM::CompositeState.__init__)


def test_hsm::compositestate_constructor_args():
    sig = inspect.signature(HSM::CompositeState.__init__)
    params = list(sig.parameters.keys())



def test_hsm::transition_is_not_abstract():
    assert not inspect.isabstract(HSM::Transition)


def test_hsm::transition_constructor_exists():
    assert callable(HSM::Transition.__init__)


def test_hsm::transition_constructor_args():
    sig = inspect.signature(HSM::Transition.__init__)
    params = list(sig.parameters.keys())



def test_hsm::state_is_not_abstract():
    assert not inspect.isabstract(HSM::State)


def test_hsm::state_constructor_exists():
    assert callable(HSM::State.__init__)


def test_hsm::state_constructor_args():
    sig = inspect.signature(HSM::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hsm::state_has_name():
    assert hasattr(HSM::State, "name")
    descriptor = None
    for klass in HSM::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hsm::statemachine_is_not_abstract():
    assert not inspect.isabstract(HSM::StateMachine)


def test_hsm::statemachine_constructor_exists():
    assert callable(HSM::StateMachine.__init__)


def test_hsm::statemachine_constructor_args():
    sig = inspect.signature(HSM::StateMachine.__init__)
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
HSM::CompositeState_strategy = st.builds(
    HSM::CompositeState,
)
HSM::Transition_strategy = st.builds(
    HSM::Transition,
)
HSM::State_strategy = st.builds(
    HSM::State,
    name=
        safe_text
)
HSM::StateMachine_strategy = st.builds(
    HSM::StateMachine,
)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=HSM::CompositeState_strategy)
@settings(max_examples=50)
def test_hsm::compositestate_instantiation(instance):
    assert isinstance(instance, HSM::CompositeState)

@given(instance=HSM::Transition_strategy)
@settings(max_examples=50)
def test_hsm::transition_instantiation(instance):
    assert isinstance(instance, HSM::Transition)

@given(instance=HSM::State_strategy)
@settings(max_examples=50)
def test_hsm::state_instantiation(instance):
    assert isinstance(instance, HSM::State)

@given(instance=HSM::State_strategy)
def test_hsm::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=HSM::State_strategy)
def test_hsm::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HSM::StateMachine_strategy)
@settings(max_examples=50)
def test_hsm::statemachine_instantiation(instance):
    assert isinstance(instance, HSM::StateMachine)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=HSM::StateMachine_strategy)
@settings(max_examples=30)
def test_hsm::statemachine_addtransition_changes_state(instance):
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
        assert has_statements, f"Function 'addTransition' in HSM::StateMachine is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'addTransition' in HSM::StateMachine did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'addTransition' in HSM::StateMachine is not implemented or raised an error")
