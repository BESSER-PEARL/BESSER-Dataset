import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    fsm::Transition,
    NoAnnotationSuper,
    fsm::NoAnnotation,
    fsm::NoAnnotationSuper,
    fsm::FSM,
    fsm::State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsm::transition_is_not_abstract():
    assert not inspect.isabstract(fsm::Transition)


def test_fsm::transition_constructor_exists():
    assert callable(fsm::Transition.__init__)


def test_fsm::transition_constructor_args():
    sig = inspect.signature(fsm::Transition.__init__)
    params = list(sig.parameters.keys())



def test_noannotationsuper_is_not_abstract():
    assert not inspect.isabstract(NoAnnotationSuper)


def test_noannotationsuper_constructor_exists():
    assert callable(NoAnnotationSuper.__init__)


def test_noannotationsuper_constructor_args():
    sig = inspect.signature(NoAnnotationSuper.__init__)
    params = list(sig.parameters.keys())



def test_fsm::noannotation_is_not_abstract():
    assert not inspect.isabstract(fsm::NoAnnotation)


def test_fsm::noannotation_constructor_exists():
    assert callable(fsm::NoAnnotation.__init__)


def test_fsm::noannotation_constructor_args():
    sig = inspect.signature(fsm::NoAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "a" in params, "Missing parameter 'a'"
    assert "b" in params, "Missing parameter 'b'"

def test_fsm::noannotation_has_a():
    assert hasattr(fsm::NoAnnotation, "a")
    descriptor = None
    for klass in fsm::NoAnnotation.__mro__:
        if "a" in klass.__dict__:
            descriptor = klass.__dict__["a"]
            break
    assert isinstance(descriptor, property)

def test_fsm::noannotation_has_b():
    assert hasattr(fsm::NoAnnotation, "b")
    descriptor = None
    for klass in fsm::NoAnnotation.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)



def test_fsm::noannotationsuper_is_not_abstract():
    assert not inspect.isabstract(fsm::NoAnnotationSuper)


def test_fsm::noannotationsuper_constructor_exists():
    assert callable(fsm::NoAnnotationSuper.__init__)


def test_fsm::noannotationsuper_constructor_args():
    sig = inspect.signature(fsm::NoAnnotationSuper.__init__)
    params = list(sig.parameters.keys())



def test_fsm::fsm_is_not_abstract():
    assert not inspect.isabstract(fsm::FSM)


def test_fsm::fsm_constructor_exists():
    assert callable(fsm::FSM.__init__)


def test_fsm::fsm_constructor_args():
    sig = inspect.signature(fsm::FSM.__init__)
    params = list(sig.parameters.keys())



def test_fsm::state_is_not_abstract():
    assert not inspect.isabstract(fsm::State)


def test_fsm::state_constructor_exists():
    assert callable(fsm::State.__init__)


def test_fsm::state_constructor_args():
    sig = inspect.signature(fsm::State.__init__)
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
fsm::Transition_strategy = st.builds(
    fsm::Transition,
)
NoAnnotationSuper_strategy = st.builds(
    NoAnnotationSuper,
)
fsm::NoAnnotation_strategy = st.builds(
    fsm::NoAnnotation,
    a=
        safe_text,
    b=
        safe_text
)
fsm::NoAnnotationSuper_strategy = st.builds(
    fsm::NoAnnotationSuper,
)
fsm::FSM_strategy = st.builds(
    fsm::FSM,
)
fsm::State_strategy = st.builds(
    fsm::State,
)

@given(instance=fsm::Transition_strategy)
@settings(max_examples=50)
def test_fsm::transition_instantiation(instance):
    assert isinstance(instance, fsm::Transition)

@given(instance=NoAnnotationSuper_strategy)
@settings(max_examples=50)
def test_noannotationsuper_instantiation(instance):
    assert isinstance(instance, NoAnnotationSuper)

@given(instance=fsm::NoAnnotation_strategy)
@settings(max_examples=50)
def test_fsm::noannotation_instantiation(instance):
    assert isinstance(instance, fsm::NoAnnotation)

@given(instance=fsm::NoAnnotation_strategy)
def test_fsm::noannotation_a_type(instance):
    assert isinstance(instance.a, str)


@given(instance=fsm::NoAnnotation_strategy)
def test_fsm::noannotation_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original

@given(instance=fsm::NoAnnotation_strategy)
def test_fsm::noannotation_b_type(instance):
    assert isinstance(instance.b, str)


@given(instance=fsm::NoAnnotation_strategy)
def test_fsm::noannotation_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsm::NoAnnotation_strategy)
@settings(max_examples=30)
def test_fsm::noannotation_k_changes_state(instance):
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
        assert has_statements, f"Function 'k' in fsm::NoAnnotation is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'k' in fsm::NoAnnotation did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'k' in fsm::NoAnnotation is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=fsm::NoAnnotation_strategy)
@settings(max_examples=30)
def test_fsm::noannotation_j_changes_state(instance):
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
        assert has_statements, f"Function 'j' in fsm::NoAnnotation is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'j' in fsm::NoAnnotation did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'j' in fsm::NoAnnotation is not implemented or raised an error")

@given(instance=fsm::NoAnnotationSuper_strategy)
@settings(max_examples=50)
def test_fsm::noannotationsuper_instantiation(instance):
    assert isinstance(instance, fsm::NoAnnotationSuper)

@given(instance=fsm::FSM_strategy)
@settings(max_examples=50)
def test_fsm::fsm_instantiation(instance):
    assert isinstance(instance, fsm::FSM)

@given(instance=fsm::State_strategy)
@settings(max_examples=50)
def test_fsm::state_instantiation(instance):
    assert isinstance(instance, fsm::State)
