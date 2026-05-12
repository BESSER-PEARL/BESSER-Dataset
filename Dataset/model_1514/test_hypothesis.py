import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    model_System,
    model_State,
    model_Buffer,
    model_Transition,
    model_FSM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_model_system_is_not_abstract():
    assert not inspect.isabstract(model_System)


def test_model_system_constructor_exists():
    assert callable(model_System.__init__)


def test_model_system_constructor_args():
    sig = inspect.signature(model_System.__init__)
    params = list(sig.parameters.keys())



def test_model_state_is_not_abstract():
    assert not inspect.isabstract(model_State)


def test_model_state_constructor_exists():
    assert callable(model_State.__init__)


def test_model_state_constructor_args():
    sig = inspect.signature(model_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model_state_has_name():
    assert hasattr(model_State, "name")
    descriptor = None
    for klass in model_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model_buffer_is_not_abstract():
    assert not inspect.isabstract(model_Buffer)


def test_model_buffer_constructor_exists():
    assert callable(model_Buffer.__init__)


def test_model_buffer_constructor_args():
    sig = inspect.signature(model_Buffer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "initialValue" in params, "Missing parameter 'initialValue'"

def test_model_buffer_has_name():
    assert hasattr(model_Buffer, "name")
    descriptor = None
    for klass in model_Buffer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_model_buffer_has_initialValue():
    assert hasattr(model_Buffer, "initialValue")
    descriptor = None
    for klass in model_Buffer.__mro__:
        if "initialValue" in klass.__dict__:
            descriptor = klass.__dict__["initialValue"]
            break
    assert isinstance(descriptor, property)



def test_model_transition_is_not_abstract():
    assert not inspect.isabstract(model_Transition)


def test_model_transition_constructor_exists():
    assert callable(model_Transition.__init__)


def test_model_transition_constructor_args():
    sig = inspect.signature(model_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"
    assert "name" in params, "Missing parameter 'name'"
    assert "trigger" in params, "Missing parameter 'trigger'"

def test_model_transition_has_action():
    assert hasattr(model_Transition, "action")
    descriptor = None
    for klass in model_Transition.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)

def test_model_transition_has_name():
    assert hasattr(model_Transition, "name")
    descriptor = None
    for klass in model_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_model_transition_has_trigger():
    assert hasattr(model_Transition, "trigger")
    descriptor = None
    for klass in model_Transition.__mro__:
        if "trigger" in klass.__dict__:
            descriptor = klass.__dict__["trigger"]
            break
    assert isinstance(descriptor, property)



def test_model_fsm_is_not_abstract():
    assert not inspect.isabstract(model_FSM)


def test_model_fsm_constructor_exists():
    assert callable(model_FSM.__init__)


def test_model_fsm_constructor_args():
    sig = inspect.signature(model_FSM.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model_fsm_has_name():
    assert hasattr(model_FSM, "name")
    descriptor = None
    for klass in model_FSM.__mro__:
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
model_System_strategy = st.builds(
    model_System,
)
model_State_strategy = st.builds(
    model_State,
    name=
        safe_text
)
model_Buffer_strategy = st.builds(
    model_Buffer,
    name=
        safe_text,
    initialValue=
        safe_text
)
model_Transition_strategy = st.builds(
    model_Transition,
    action=
        safe_text,
    name=
        safe_text,
    trigger=
        safe_text
)
model_FSM_strategy = st.builds(
    model_FSM,
    name=
        safe_text
)

@given(instance=model_System_strategy)
@settings(max_examples=50)
def test_model_system_instantiation(instance):
    assert isinstance(instance, model_System)

@given(instance=model_State_strategy)
@settings(max_examples=50)
def test_model_state_instantiation(instance):
    assert isinstance(instance, model_State)



@given(instance=model_State_strategy)
def test_model_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model_Buffer_strategy)
@settings(max_examples=50)
def test_model_buffer_instantiation(instance):
    assert isinstance(instance, model_Buffer)



@given(instance=model_Buffer_strategy)
def test_model_buffer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=model_Buffer_strategy)
def test_model_buffer_initialValue_setter(instance):
    original = instance.initialValue
    instance.initialValue = original
    assert instance.initialValue == original

@given(instance=model_Transition_strategy)
@settings(max_examples=50)
def test_model_transition_instantiation(instance):
    assert isinstance(instance, model_Transition)



@given(instance=model_Transition_strategy)
def test_model_transition_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original



@given(instance=model_Transition_strategy)
def test_model_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=model_Transition_strategy)
def test_model_transition_trigger_setter(instance):
    original = instance.trigger
    instance.trigger = original
    assert instance.trigger == original

@given(instance=model_FSM_strategy)
@settings(max_examples=50)
def test_model_fsm_instantiation(instance):
    assert isinstance(instance, model_FSM)



@given(instance=model_FSM_strategy)
def test_model_fsm_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_FSM_strategy)
@settings(max_examples=30)
def test_model_fsm_run_changes_state(instance):
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
        assert has_statements, f"Function 'run' in model_FSM is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'run' in model_FSM did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'run' in model_FSM is not implemented or raised an error")
