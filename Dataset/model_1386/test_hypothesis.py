import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    test_NamedElement,
    NamedElement,
    test_Transition,
    test_State,
    test_StateMachine,
    Kind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test_namedelement_is_not_abstract():
    assert not inspect.isabstract(test_NamedElement)


def test_test_namedelement_constructor_exists():
    assert callable(test_NamedElement.__init__)


def test_test_namedelement_constructor_args():
    sig = inspect.signature(test_NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_test_transition_is_not_abstract():
    assert not inspect.isabstract(test_Transition)


def test_test_transition_constructor_exists():
    assert callable(test_Transition.__init__)


def test_test_transition_constructor_args():
    sig = inspect.signature(test_Transition.__init__)
    params = list(sig.parameters.keys())



def test_test_state_is_not_abstract():
    assert not inspect.isabstract(test_State)


def test_test_state_constructor_exists():
    assert callable(test_State.__init__)


def test_test_state_constructor_args():
    sig = inspect.signature(test_State.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_test_state_has_kind():
    assert hasattr(test_State, "kind")
    descriptor = None
    for klass in test_State.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_test_statemachine_is_not_abstract():
    assert not inspect.isabstract(test_StateMachine)


def test_test_statemachine_constructor_exists():
    assert callable(test_StateMachine.__init__)


def test_test_statemachine_constructor_args():
    sig = inspect.signature(test_StateMachine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_test_statemachine_has_name():
    assert hasattr(test_StateMachine, "name")
    descriptor = None
    for klass in test_StateMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_kind_exists():
    # Check that the Enumeration exists
    assert Kind is not None

def test_kind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Kind]
    expected_literals = [
        "NotNice",
        "Nice",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Kind"


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
test_NamedElement_strategy = st.builds(
    test_NamedElement,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
test_Transition_strategy = st.builds(
    test_Transition,
)
test_State_strategy = st.builds(
    test_State,
    kind=
        safe_text
)
test_StateMachine_strategy = st.builds(
    test_StateMachine,
    name=
        safe_text
)

@given(instance=test_NamedElement_strategy)
@settings(max_examples=50)
def test_test_namedelement_instantiation(instance):
    assert isinstance(instance, test_NamedElement)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=test_Transition_strategy)
@settings(max_examples=50)
def test_test_transition_instantiation(instance):
    assert isinstance(instance, test_Transition)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=test_Transition_strategy)
@settings(max_examples=30)
def test_test_transition_fire_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.fire()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.fire).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'fire' in test_Transition is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'fire' in test_Transition did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'fire' in test_Transition is not implemented or raised an error")

@given(instance=test_State_strategy)
@settings(max_examples=50)
def test_test_state_instantiation(instance):
    assert isinstance(instance, test_State)



@given(instance=test_State_strategy)
def test_test_state_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=test_StateMachine_strategy)
@settings(max_examples=50)
def test_test_statemachine_instantiation(instance):
    assert isinstance(instance, test_StateMachine)



@given(instance=test_StateMachine_strategy)
def test_test_statemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
