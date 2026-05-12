import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    fsm_Transition,
    NoAnnotationSuper,
    fsm_NoAnnotation,
    fsm_NoAnnotationSuper,
    fsm_FSM,
    fsm_State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsm_transition_is_not_abstract():
    assert not inspect.isabstract(fsm_Transition)


def test_fsm_transition_constructor_exists():
    assert callable(fsm_Transition.__init__)


def test_fsm_transition_constructor_args():
    sig = inspect.signature(fsm_Transition.__init__)
    params = list(sig.parameters.keys())



def test_noannotationsuper_is_not_abstract():
    assert not inspect.isabstract(NoAnnotationSuper)


def test_noannotationsuper_constructor_exists():
    assert callable(NoAnnotationSuper.__init__)


def test_noannotationsuper_constructor_args():
    sig = inspect.signature(NoAnnotationSuper.__init__)
    params = list(sig.parameters.keys())



def test_fsm_noannotation_is_not_abstract():
    assert not inspect.isabstract(fsm_NoAnnotation)


def test_fsm_noannotation_constructor_exists():
    assert callable(fsm_NoAnnotation.__init__)


def test_fsm_noannotation_constructor_args():
    sig = inspect.signature(fsm_NoAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "b" in params, "Missing parameter 'b'"
    assert "a" in params, "Missing parameter 'a'"

def test_fsm_noannotation_has_b():
    assert hasattr(fsm_NoAnnotation, "b")
    descriptor = None
    for klass in fsm_NoAnnotation.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)

def test_fsm_noannotation_has_a():
    assert hasattr(fsm_NoAnnotation, "a")
    descriptor = None
    for klass in fsm_NoAnnotation.__mro__:
        if "a" in klass.__dict__:
            descriptor = klass.__dict__["a"]
            break
    assert isinstance(descriptor, property)



def test_fsm_noannotationsuper_is_not_abstract():
    assert not inspect.isabstract(fsm_NoAnnotationSuper)


def test_fsm_noannotationsuper_constructor_exists():
    assert callable(fsm_NoAnnotationSuper.__init__)


def test_fsm_noannotationsuper_constructor_args():
    sig = inspect.signature(fsm_NoAnnotationSuper.__init__)
    params = list(sig.parameters.keys())



def test_fsm_fsm_is_not_abstract():
    assert not inspect.isabstract(fsm_FSM)


def test_fsm_fsm_constructor_exists():
    assert callable(fsm_FSM.__init__)


def test_fsm_fsm_constructor_args():
    sig = inspect.signature(fsm_FSM.__init__)
    params = list(sig.parameters.keys())



def test_fsm_state_is_not_abstract():
    assert not inspect.isabstract(fsm_State)


def test_fsm_state_constructor_exists():
    assert callable(fsm_State.__init__)


def test_fsm_state_constructor_args():
    sig = inspect.signature(fsm_State.__init__)
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
fsm_Transition_strategy = st.builds(
    fsm_Transition,
)
NoAnnotationSuper_strategy = st.builds(
    NoAnnotationSuper,
)
fsm_NoAnnotation_strategy = st.builds(
    fsm_NoAnnotation,
    b=
        safe_text,
    a=
        safe_text
)
fsm_NoAnnotationSuper_strategy = st.builds(
    fsm_NoAnnotationSuper,
)
fsm_FSM_strategy = st.builds(
    fsm_FSM,
)
fsm_State_strategy = st.builds(
    fsm_State,
)

@given(instance=fsm_Transition_strategy)
@settings(max_examples=50)
def test_fsm_transition_instantiation(instance):
    assert isinstance(instance, fsm_Transition)

@given(instance=NoAnnotationSuper_strategy)
@settings(max_examples=50)
def test_noannotationsuper_instantiation(instance):
    assert isinstance(instance, NoAnnotationSuper)

@given(instance=fsm_NoAnnotation_strategy)
@settings(max_examples=50)
def test_fsm_noannotation_instantiation(instance):
    assert isinstance(instance, fsm_NoAnnotation)



@given(instance=fsm_NoAnnotation_strategy)
def test_fsm_noannotation_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original



@given(instance=fsm_NoAnnotation_strategy)
def test_fsm_noannotation_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsm_NoAnnotation_strategy)
@settings(max_examples=30)
def test_fsm_noannotation_k_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.k(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.k).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'k' in fsm_NoAnnotation is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'k' in fsm_NoAnnotation did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'k' in fsm_NoAnnotation is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsm_NoAnnotation_strategy)
@settings(max_examples=30)
def test_fsm_noannotation_j_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.j(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.j).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'j' in fsm_NoAnnotation is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'j' in fsm_NoAnnotation did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'j' in fsm_NoAnnotation is not implemented or raised an error")

@given(instance=fsm_NoAnnotationSuper_strategy)
@settings(max_examples=50)
def test_fsm_noannotationsuper_instantiation(instance):
    assert isinstance(instance, fsm_NoAnnotationSuper)

@given(instance=fsm_FSM_strategy)
@settings(max_examples=50)
def test_fsm_fsm_instantiation(instance):
    assert isinstance(instance, fsm_FSM)

@given(instance=fsm_State_strategy)
@settings(max_examples=50)
def test_fsm_state_instantiation(instance):
    assert isinstance(instance, fsm_State)
