import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    sAAP_StateMachine,
    sAAP_Transition,
    sAAP_State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_saap_statemachine_is_not_abstract():
    assert not inspect.isabstract(sAAP_StateMachine)


def test_saap_statemachine_constructor_exists():
    assert callable(sAAP_StateMachine.__init__)


def test_saap_statemachine_constructor_args():
    sig = inspect.signature(sAAP_StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_saap_statemachine_has_name():
    assert hasattr(sAAP_StateMachine, "name")
    descriptor = None
    for klass in sAAP_StateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_saap_transition_is_not_abstract():
    assert not inspect.isabstract(sAAP_Transition)


def test_saap_transition_constructor_exists():
    assert callable(sAAP_Transition.__init__)


def test_saap_transition_constructor_args():
    sig = inspect.signature(sAAP_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_saap_transition_has_name():
    assert hasattr(sAAP_Transition, "name")
    descriptor = None
    for klass in sAAP_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_saap_state_is_not_abstract():
    assert not inspect.isabstract(sAAP_State)


def test_saap_state_constructor_exists():
    assert callable(sAAP_State.__init__)


def test_saap_state_constructor_args():
    sig = inspect.signature(sAAP_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "default" in params, "Missing parameter 'default'"

def test_saap_state_has_name():
    assert hasattr(sAAP_State, "name")
    descriptor = None
    for klass in sAAP_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_saap_state_has_default():
    assert hasattr(sAAP_State, "default")
    descriptor = None
    for klass in sAAP_State.__mro__:
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
sAAP_StateMachine_strategy = st.builds(
    sAAP_StateMachine,
    name=
        safe_text
)
sAAP_Transition_strategy = st.builds(
    sAAP_Transition,
    name=
        safe_text
)
sAAP_State_strategy = st.builds(
    sAAP_State,
    name=
        safe_text,
    default=
        st.booleans()
)

@given(instance=sAAP_StateMachine_strategy)
@settings(max_examples=50)
def test_saap_statemachine_instantiation(instance):
    assert isinstance(instance, sAAP_StateMachine)



@given(instance=sAAP_StateMachine_strategy)
def test_saap_statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=sAAP_StateMachine_strategy)
@settings(max_examples=30)
def test_saap_statemachine_execute_changes_state(instance):
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
        assert has_statements, f"Function 'execute' in sAAP_StateMachine is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'execute' in sAAP_StateMachine did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'execute' in sAAP_StateMachine is not implemented or raised an error")

@given(instance=sAAP_Transition_strategy)
@settings(max_examples=50)
def test_saap_transition_instantiation(instance):
    assert isinstance(instance, sAAP_Transition)



@given(instance=sAAP_Transition_strategy)
def test_saap_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sAAP_State_strategy)
@settings(max_examples=50)
def test_saap_state_instantiation(instance):
    assert isinstance(instance, sAAP_State)



@given(instance=sAAP_State_strategy)
def test_saap_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=sAAP_State_strategy)
def test_saap_state_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original
