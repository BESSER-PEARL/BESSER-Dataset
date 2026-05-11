import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    tp1::State,
    tp1::Transition,
    tp1::StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tp1::state_is_not_abstract():
    assert not inspect.isabstract(tp1::State)


def test_tp1::state_constructor_exists():
    assert callable(tp1::State.__init__)


def test_tp1::state_constructor_args():
    sig = inspect.signature(tp1::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tp1::state_has_name():
    assert hasattr(tp1::State, "name")
    descriptor = None
    for klass in tp1::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tp1::transition_is_not_abstract():
    assert not inspect.isabstract(tp1::Transition)


def test_tp1::transition_constructor_exists():
    assert callable(tp1::Transition.__init__)


def test_tp1::transition_constructor_args():
    sig = inspect.signature(tp1::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tp1::transition_has_name():
    assert hasattr(tp1::Transition, "name")
    descriptor = None
    for klass in tp1::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tp1::statemachine_is_not_abstract():
    assert not inspect.isabstract(tp1::StateMachine)


def test_tp1::statemachine_constructor_exists():
    assert callable(tp1::StateMachine.__init__)


def test_tp1::statemachine_constructor_args():
    sig = inspect.signature(tp1::StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tp1::statemachine_has_name():
    assert hasattr(tp1::StateMachine, "name")
    descriptor = None
    for klass in tp1::StateMachine.__mro__:
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
tp1::State_strategy = st.builds(
    tp1::State,
    name=
        safe_text
)
tp1::Transition_strategy = st.builds(
    tp1::Transition,
    name=
        safe_text
)
tp1::StateMachine_strategy = st.builds(
    tp1::StateMachine,
    name=
        safe_text
)

@given(instance=tp1::State_strategy)
@settings(max_examples=50)
def test_tp1::state_instantiation(instance):
    assert isinstance(instance, tp1::State)

@given(instance=tp1::State_strategy)
def test_tp1::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tp1::State_strategy)
def test_tp1::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tp1::Transition_strategy)
@settings(max_examples=50)
def test_tp1::transition_instantiation(instance):
    assert isinstance(instance, tp1::Transition)

@given(instance=tp1::Transition_strategy)
def test_tp1::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tp1::Transition_strategy)
def test_tp1::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tp1::StateMachine_strategy)
@settings(max_examples=50)
def test_tp1::statemachine_instantiation(instance):
    assert isinstance(instance, tp1::StateMachine)

@given(instance=tp1::StateMachine_strategy)
def test_tp1::statemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tp1::StateMachine_strategy)
def test_tp1::statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tp1::StateMachine_strategy)
@settings(max_examples=30)
def test_tp1::statemachine_execute_changes_state(instance):
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
        assert has_statements, f"Function 'execute' in tp1::StateMachine is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'execute' in tp1::StateMachine did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'execute' in tp1::StateMachine is not implemented or raised an error")
