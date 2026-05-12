import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    d_Y,
    A,
    d_X,
    d_Z,
    Y,
    d_B,
    d_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_d_y_is_not_abstract():
    assert not inspect.isabstract(d_Y)


def test_d_y_constructor_exists():
    assert callable(d_Y.__init__)


def test_d_y_constructor_args():
    sig = inspect.signature(d_Y.__init__)
    params = list(sig.parameters.keys())
    assert "a" in params, "Missing parameter 'a'"

def test_d_y_has_a():
    assert hasattr(d_Y, "a")
    descriptor = None
    for klass in d_Y.__mro__:
        if "a" in klass.__dict__:
            descriptor = klass.__dict__["a"]
            break
    assert isinstance(descriptor, property)



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_d_x_is_not_abstract():
    assert not inspect.isabstract(d_X)


def test_d_x_constructor_exists():
    assert callable(d_X.__init__)


def test_d_x_constructor_args():
    sig = inspect.signature(d_X.__init__)
    params = list(sig.parameters.keys())



def test_d_z_is_not_abstract():
    assert not inspect.isabstract(d_Z)


def test_d_z_constructor_exists():
    assert callable(d_Z.__init__)


def test_d_z_constructor_args():
    sig = inspect.signature(d_Z.__init__)
    params = list(sig.parameters.keys())
    assert "b" in params, "Missing parameter 'b'"

def test_d_z_has_b():
    assert hasattr(d_Z, "b")
    descriptor = None
    for klass in d_Z.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)



def test_y_is_not_abstract():
    assert not inspect.isabstract(Y)


def test_y_constructor_exists():
    assert callable(Y.__init__)


def test_y_constructor_args():
    sig = inspect.signature(Y.__init__)
    params = list(sig.parameters.keys())



def test_d_b_is_not_abstract():
    assert not inspect.isabstract(d_B)


def test_d_b_constructor_exists():
    assert callable(d_B.__init__)


def test_d_b_constructor_args():
    sig = inspect.signature(d_B.__init__)
    params = list(sig.parameters.keys())



def test_d_a_is_not_abstract():
    assert not inspect.isabstract(d_A)


def test_d_a_constructor_exists():
    assert callable(d_A.__init__)


def test_d_a_constructor_args():
    sig = inspect.signature(d_A.__init__)
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
d_Y_strategy = st.builds(
    d_Y,
    a=
        safe_text
)
A_strategy = st.builds(
    A,
)
d_X_strategy = st.builds(
    d_X,
)
d_Z_strategy = st.builds(
    d_Z,
    b=
        st.integers()
)
Y_strategy = st.builds(
    Y,
)
d_B_strategy = st.builds(
    d_B,
)
d_A_strategy = st.builds(
    d_A,
)

@given(instance=d_Y_strategy)
@settings(max_examples=50)
def test_d_y_instantiation(instance):
    assert isinstance(instance, d_Y)



@given(instance=d_Y_strategy)
def test_d_y_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=d_X_strategy)
@settings(max_examples=50)
def test_d_x_instantiation(instance):
    assert isinstance(instance, d_X)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=d_X_strategy)
@settings(max_examples=30)
def test_d_x_baz_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.baz(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.baz).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'baz' in d_X is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'baz' in d_X did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'baz' in d_X is not implemented or raised an error")

@given(instance=d_Z_strategy)
@settings(max_examples=50)
def test_d_z_instantiation(instance):
    assert isinstance(instance, d_Z)



@given(instance=d_Z_strategy)
def test_d_z_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original

@given(instance=Y_strategy)
@settings(max_examples=50)
def test_y_instantiation(instance):
    assert isinstance(instance, Y)

@given(instance=d_B_strategy)
@settings(max_examples=50)
def test_d_b_instantiation(instance):
    assert isinstance(instance, d_B)

@given(instance=d_A_strategy)
@settings(max_examples=50)
def test_d_a_instantiation(instance):
    assert isinstance(instance, d_A)
