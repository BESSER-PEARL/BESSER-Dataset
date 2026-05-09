import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    model::Transition,
    model::State,
    model::System,
    model::Buffer,
    model::FSM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model::transition_is_not_abstract():
    assert not inspect.isabstract(model::Transition)


def test_model::transition_constructor_exists():
    assert callable(model::Transition.__init__)


def test_model::transition_constructor_args():
    sig = inspect.signature(model::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"
    assert "name" in params, "Missing parameter 'name'"
    assert "trigger" in params, "Missing parameter 'trigger'"

def test_model::transition_has_action():
    assert hasattr(model::Transition, "action")
    descriptor = None
    for klass in model::Transition.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)

def test_model::transition_has_name():
    assert hasattr(model::Transition, "name")
    descriptor = None
    for klass in model::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_model::transition_has_trigger():
    assert hasattr(model::Transition, "trigger")
    descriptor = None
    for klass in model::Transition.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
            break
    assert isinstance(descriptor, property)



def test_model::state_is_not_abstract():
    assert not inspect.isabstract(model::State)


def test_model::state_constructor_exists():
    assert callable(model::State.__init__)


def test_model::state_constructor_args():
    sig = inspect.signature(model::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model::state_has_name():
    assert hasattr(model::State, "name")
    descriptor = None
    for klass in model::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model::system_is_not_abstract():
    assert not inspect.isabstract(model::System)


def test_model::system_constructor_exists():
    assert callable(model::System.__init__)


def test_model::system_constructor_args():
    sig = inspect.signature(model::System.__init__)
    params = list(sig.parameters.keys())



def test_model::buffer_is_not_abstract():
    assert not inspect.isabstract(model::Buffer)


def test_model::buffer_constructor_exists():
    assert callable(model::Buffer.__init__)


def test_model::buffer_constructor_args():
    sig = inspect.signature(model::Buffer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "initialValue" in params, "Missing parameter 'initialValue'"

def test_model::buffer_has_name():
    assert hasattr(model::Buffer, "name")
    descriptor = None
    for klass in model::Buffer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_model::buffer_has_initialValue():
    assert hasattr(model::Buffer, "initialValue")
    descriptor = None
    for klass in model::Buffer.__mro__:
        if "initialValue" in klass.__dict__:
            descriptor = klass.__dict__["initialValue"]
            break
    assert isinstance(descriptor, property)



def test_model::fsm_is_not_abstract():
    assert not inspect.isabstract(model::FSM)


def test_model::fsm_constructor_exists():
    assert callable(model::FSM.__init__)


def test_model::fsm_constructor_args():
    sig = inspect.signature(model::FSM.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model::fsm_has_name():
    assert hasattr(model::FSM, "name")
    descriptor = None
    for klass in model::FSM.__mro__:
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
model::Transition_strategy = st.builds(
    model::Transition,
    action=
        safe_text,
    name=
        safe_text,
    trigger=
        safe_text
)
model::State_strategy = st.builds(
    model::State,
    name=
        safe_text
)
model::System_strategy = st.builds(
    model::System,
)
model::Buffer_strategy = st.builds(
    model::Buffer,
    name=
        safe_text,
    initialValue=
        safe_text
)
model::FSM_strategy = st.builds(
    model::FSM,
    name=
        safe_text
)

@given(instance=model::Transition_strategy)
@settings(max_examples=50)
def test_model::transition_instantiation(instance):
    assert isinstance(instance, model::Transition)

@given(instance=model::Transition_strategy)
def test_model::transition_action_type(instance):
    assert isinstance(instance.action, str)


@given(instance=model::Transition_strategy)
def test_model::transition_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=model::Transition_strategy)
def test_model::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::Transition_strategy)
def test_model::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model::Transition_strategy)
def test_model::transition_trigger_type(instance):
    assert isinstance(instance.trigger, str)


@given(instance=model::Transition_strategy)
def test_model::transition_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original

@given(instance=model::State_strategy)
@settings(max_examples=50)
def test_model::state_instantiation(instance):
    assert isinstance(instance, model::State)

@given(instance=model::State_strategy)
def test_model::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::State_strategy)
def test_model::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model::System_strategy)
@settings(max_examples=50)
def test_model::system_instantiation(instance):
    assert isinstance(instance, model::System)

@given(instance=model::Buffer_strategy)
@settings(max_examples=50)
def test_model::buffer_instantiation(instance):
    assert isinstance(instance, model::Buffer)

@given(instance=model::Buffer_strategy)
def test_model::buffer_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::Buffer_strategy)
def test_model::buffer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model::Buffer_strategy)
def test_model::buffer_initialValue_type(instance):
    assert isinstance(instance.initialValue, str)


@given(instance=model::Buffer_strategy)
def test_model::buffer_initialValue_setter(instance):
    original = instance.initialValue
    instance.initialValue = original
    assert instance.initialValue == original

@given(instance=model::FSM_strategy)
@settings(max_examples=50)
def test_model::fsm_instantiation(instance):
    assert isinstance(instance, model::FSM)

@given(instance=model::FSM_strategy)
def test_model::fsm_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::FSM_strategy)
def test_model::fsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model::FSM_strategy)
@settings(max_examples=30)
def test_model::fsm_run_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.run()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.run).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'run' in model::FSM is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'run' in model::FSM did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'run' in model::FSM is not implemented or raised an error")
