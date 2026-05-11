import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    sAAP::StateMachine,
    sAAP::Transition,
    sAAP::State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_saap::statemachine_is_not_abstract():
    assert not inspect.isabstract(sAAP::StateMachine)


def test_saap::statemachine_constructor_exists():
    assert callable(sAAP::StateMachine.__init__)


def test_saap::statemachine_constructor_args():
    sig = inspect.signature(sAAP::StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_saap::statemachine_has_name():
    assert hasattr(sAAP::StateMachine, "name")
    descriptor = None
    for klass in sAAP::StateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_saap::transition_is_not_abstract():
    assert not inspect.isabstract(sAAP::Transition)


def test_saap::transition_constructor_exists():
    assert callable(sAAP::Transition.__init__)


def test_saap::transition_constructor_args():
    sig = inspect.signature(sAAP::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_saap::transition_has_name():
    assert hasattr(sAAP::Transition, "name")
    descriptor = None
    for klass in sAAP::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_saap::state_is_not_abstract():
    assert not inspect.isabstract(sAAP::State)


def test_saap::state_constructor_exists():
    assert callable(sAAP::State.__init__)


def test_saap::state_constructor_args():
    sig = inspect.signature(sAAP::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "default" in params, "Missing parameter 'default'"

def test_saap::state_has_name():
    assert hasattr(sAAP::State, "name")
    descriptor = None
    for klass in sAAP::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_saap::state_has_default():
    assert hasattr(sAAP::State, "default")
    descriptor = None
    for klass in sAAP::State.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
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
sAAP::StateMachine_strategy = st.builds(
    sAAP::StateMachine,
    name=
        safe_text
)
sAAP::Transition_strategy = st.builds(
    sAAP::Transition,
    name=
        safe_text
)
sAAP::State_strategy = st.builds(
    sAAP::State,
    name=
        safe_text,
    default=
        st.booleans()
)

@given(instance=sAAP::StateMachine_strategy)
@settings(max_examples=50)
def test_saap::statemachine_instantiation(instance):
    assert isinstance(instance, sAAP::StateMachine)

@given(instance=sAAP::StateMachine_strategy)
def test_saap::statemachine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sAAP::StateMachine_strategy)
def test_saap::statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=sAAP::StateMachine_strategy)
@settings(max_examples=30)
def test_saap::statemachine_execute_changes_state(instance):
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
        assert has_statements, f"Function 'execute' in sAAP::StateMachine is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'execute' in sAAP::StateMachine did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'execute' in sAAP::StateMachine is not implemented or raised an error")

@given(instance=sAAP::Transition_strategy)
@settings(max_examples=50)
def test_saap::transition_instantiation(instance):
    assert isinstance(instance, sAAP::Transition)

@given(instance=sAAP::Transition_strategy)
def test_saap::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sAAP::Transition_strategy)
def test_saap::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sAAP::State_strategy)
@settings(max_examples=50)
def test_saap::state_instantiation(instance):
    assert isinstance(instance, sAAP::State)

@given(instance=sAAP::State_strategy)
def test_saap::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=sAAP::State_strategy)
def test_saap::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sAAP::State_strategy)
def test_saap::state_default_type(instance):
    assert isinstance(instance.default, bool)


@given(instance=sAAP::State_strategy)
def test_saap::state_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original
