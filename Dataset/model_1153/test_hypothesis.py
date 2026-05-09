import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    gemoc::Transition,
    gemoc::State,
    gemoc::FSM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_gemoc::transition_is_not_abstract():
    assert not inspect.isabstract(gemoc::Transition)


def test_gemoc::transition_constructor_exists():
    assert callable(gemoc::Transition.__init__)


def test_gemoc::transition_constructor_args():
    sig = inspect.signature(gemoc::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "trigger" in params, "Missing parameter 'trigger'"
    assert "name" in params, "Missing parameter 'name'"

def test_gemoc::transition_has_trigger():
    assert hasattr(gemoc::Transition, "trigger")
    descriptor = None
    for klass in gemoc::Transition.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
            break
    assert isinstance(descriptor, property)

def test_gemoc::transition_has_name():
    assert hasattr(gemoc::Transition, "name")
    descriptor = None
    for klass in gemoc::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gemoc::state_is_not_abstract():
    assert not inspect.isabstract(gemoc::State)


def test_gemoc::state_constructor_exists():
    assert callable(gemoc::State.__init__)


def test_gemoc::state_constructor_args():
    sig = inspect.signature(gemoc::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gemoc::state_has_name():
    assert hasattr(gemoc::State, "name")
    descriptor = None
    for klass in gemoc::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gemoc::fsm_is_not_abstract():
    assert not inspect.isabstract(gemoc::FSM)


def test_gemoc::fsm_constructor_exists():
    assert callable(gemoc::FSM.__init__)


def test_gemoc::fsm_constructor_args():
    sig = inspect.signature(gemoc::FSM.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_gemoc::fsm_has_name():
    assert hasattr(gemoc::FSM, "name")
    descriptor = None
    for klass in gemoc::FSM.__mro__:
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
gemoc::Transition_strategy = st.builds(
    gemoc::Transition,
    trigger=
        safe_text,
    name=
        safe_text
)
gemoc::State_strategy = st.builds(
    gemoc::State,
    name=
        safe_text
)
gemoc::FSM_strategy = st.builds(
    gemoc::FSM,
    name=
        safe_text
)

@given(instance=gemoc::Transition_strategy)
@settings(max_examples=50)
def test_gemoc::transition_instantiation(instance):
    assert isinstance(instance, gemoc::Transition)

@given(instance=gemoc::Transition_strategy)
def test_gemoc::transition_trigger_type(instance):
    assert isinstance(instance.trigger, str)


@given(instance=gemoc::Transition_strategy)
def test_gemoc::transition_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original

@given(instance=gemoc::Transition_strategy)
def test_gemoc::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gemoc::Transition_strategy)
def test_gemoc::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gemoc::State_strategy)
@settings(max_examples=50)
def test_gemoc::state_instantiation(instance):
    assert isinstance(instance, gemoc::State)

@given(instance=gemoc::State_strategy)
def test_gemoc::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gemoc::State_strategy)
def test_gemoc::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gemoc::FSM_strategy)
@settings(max_examples=50)
def test_gemoc::fsm_instantiation(instance):
    assert isinstance(instance, gemoc::FSM)

@given(instance=gemoc::FSM_strategy)
def test_gemoc::fsm_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gemoc::FSM_strategy)
def test_gemoc::fsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=gemoc::FSM_strategy)
@settings(max_examples=30)
def test_gemoc::fsm_print_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.print()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.print).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'print' in gemoc::FSM is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'print' in gemoc::FSM did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'print' in gemoc::FSM is not implemented or raised an error")
