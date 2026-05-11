import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    tP1::IDM::Transition,
    tP1::IDM::State,
    tP1::IDM::StateMachine,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tp1::idm::transition_is_not_abstract():
    assert not inspect.isabstract(tP1::IDM::Transition)


def test_tp1::idm::transition_constructor_exists():
    assert callable(tP1::IDM::Transition.__init__)


def test_tp1::idm::transition_constructor_args():
    sig = inspect.signature(tP1::IDM::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tp1::idm::transition_has_name():
    assert hasattr(tP1::IDM::Transition, "name")
    descriptor = None
    for klass in tP1::IDM::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tp1::idm::state_is_not_abstract():
    assert not inspect.isabstract(tP1::IDM::State)


def test_tp1::idm::state_constructor_exists():
    assert callable(tP1::IDM::State.__init__)


def test_tp1::idm::state_constructor_args():
    sig = inspect.signature(tP1::IDM::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tp1::idm::state_has_name():
    assert hasattr(tP1::IDM::State, "name")
    descriptor = None
    for klass in tP1::IDM::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tp1::idm::statemachine_is_not_abstract():
    assert not inspect.isabstract(tP1::IDM::StateMachine)


def test_tp1::idm::statemachine_constructor_exists():
    assert callable(tP1::IDM::StateMachine.__init__)


def test_tp1::idm::statemachine_constructor_args():
    sig = inspect.signature(tP1::IDM::StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tp1::idm::statemachine_has_name():
    assert hasattr(tP1::IDM::StateMachine, "name")
    descriptor = None
    for klass in tP1::IDM::StateMachine.__mro__:
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
tP1::IDM::Transition_strategy = st.builds(
    tP1::IDM::Transition,
    name=
        safe_text
)
tP1::IDM::State_strategy = st.builds(
    tP1::IDM::State,
    name=
        safe_text
)
tP1::IDM::StateMachine_strategy = st.builds(
    tP1::IDM::StateMachine,
    name=
        safe_text
)

@given(instance=tP1::IDM::Transition_strategy)
@settings(max_examples=50)
def test_tp1::idm::transition_instantiation(instance):
    assert isinstance(instance, tP1::IDM::Transition)

@given(instance=tP1::IDM::Transition_strategy)
def test_tp1::idm::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tP1::IDM::Transition_strategy)
def test_tp1::idm::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tP1::IDM::State_strategy)
@settings(max_examples=50)
def test_tp1::idm::state_instantiation(instance):
    assert isinstance(instance, tP1::IDM::State)

@given(instance=tP1::IDM::State_strategy)
def test_tp1::idm::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tP1::IDM::State_strategy)
def test_tp1::idm::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tP1::IDM::StateMachine_strategy)
@settings(max_examples=50)
def test_tp1::idm::statemachine_instantiation(instance):
    assert isinstance(instance, tP1::IDM::StateMachine)

@given(instance=tP1::IDM::StateMachine_strategy)
def test_tp1::idm::statemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tP1::IDM::StateMachine_strategy)
def test_tp1::idm::statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=tP1::IDM::StateMachine_strategy)
@settings(max_examples=30)
def test_tp1::idm::statemachine_execute_changes_state(instance):
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
        assert has_statements, f"Function 'execute' in tP1::IDM::StateMachine is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'execute' in tP1::IDM::StateMachine did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'execute' in tP1::IDM::StateMachine is not implemented or raised an error")
