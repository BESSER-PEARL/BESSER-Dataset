import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    g_Y,
    g_X,
    A,
    g_C,
    g_B,
    g_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_g_y_is_not_abstract():
    assert not inspect.isabstract(g_Y)


def test_g_y_constructor_exists():
    assert callable(g_Y.__init__)


def test_g_y_constructor_args():
    sig = inspect.signature(g_Y.__init__)
    params = list(sig.parameters.keys())
    assert "a" in params, "Missing parameter 'a'"

def test_g_y_has_a():
    assert hasattr(g_Y, "a")
    descriptor = None
    for klass in g_Y.__mro__:
        if "a" in klass.__dict__:
            descriptor = klass.__dict__["a"]
            break
    assert isinstance(descriptor, property)



def test_g_x_is_not_abstract():
    assert not inspect.isabstract(g_X)


def test_g_x_constructor_exists():
    assert callable(g_X.__init__)


def test_g_x_constructor_args():
    sig = inspect.signature(g_X.__init__)
    params = list(sig.parameters.keys())



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_g_c_is_not_abstract():
    assert not inspect.isabstract(g_C)


def test_g_c_constructor_exists():
    assert callable(g_C.__init__)


def test_g_c_constructor_args():
    sig = inspect.signature(g_C.__init__)
    params = list(sig.parameters.keys())
    assert "z" in params, "Missing parameter 'z'"

def test_g_c_has_z():
    assert hasattr(g_C, "z")
    descriptor = None
    for klass in g_C.__mro__:
        if "z" in klass.__dict__:
            descriptor = klass.__dict__["z"]
            break
    assert isinstance(descriptor, property)



def test_g_b_is_not_abstract():
    assert not inspect.isabstract(g_B)


def test_g_b_constructor_exists():
    assert callable(g_B.__init__)


def test_g_b_constructor_args():
    sig = inspect.signature(g_B.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"

def test_g_b_has_y():
    assert hasattr(g_B, "y")
    descriptor = None
    for klass in g_B.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_g_a_is_not_abstract():
    assert not inspect.isabstract(g_A)


def test_g_a_constructor_exists():
    assert callable(g_A.__init__)


def test_g_a_constructor_args():
    sig = inspect.signature(g_A.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"

def test_g_a_has_x():
    assert hasattr(g_A, "x")
    descriptor = None
    for klass in g_A.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
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
g_Y_strategy = st.builds(
    g_Y,
    a=
        safe_text
)
g_X_strategy = st.builds(
    g_X,
)
A_strategy = st.builds(
    A,
)
g_C_strategy = st.builds(
    g_C,
    z=
        safe_text
)
g_B_strategy = st.builds(
    g_B,
    y=
        st.booleans()
)
g_A_strategy = st.builds(
    g_A,
    x=
        safe_text
)

@given(instance=g_Y_strategy)
@settings(max_examples=50)
def test_g_y_instantiation(instance):
    assert isinstance(instance, g_Y)



@given(instance=g_Y_strategy)
def test_g_y_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original

@given(instance=g_X_strategy)
@settings(max_examples=50)
def test_g_x_instantiation(instance):
    assert isinstance(instance, g_X)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=g_X_strategy)
@settings(max_examples=30)
def test_g_x_foo_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.foo()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.foo).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'foo' in g_X is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'foo' in g_X did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'foo' in g_X is not implemented or raised an error")

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=g_C_strategy)
@settings(max_examples=50)
def test_g_c_instantiation(instance):
    assert isinstance(instance, g_C)



@given(instance=g_C_strategy)
def test_g_c_z_setter(instance):
    original = instance.z
    instance.z = original
    assert instance.z == original

@given(instance=g_B_strategy)
@settings(max_examples=50)
def test_g_b_instantiation(instance):
    assert isinstance(instance, g_B)



@given(instance=g_B_strategy)
def test_g_b_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=g_A_strategy)
@settings(max_examples=50)
def test_g_a_instantiation(instance):
    assert isinstance(instance, g_A)



@given(instance=g_A_strategy)
def test_g_a_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=g_A_strategy)
@settings(max_examples=30)
def test_g_a_bar_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.bar()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.bar).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'bar' in g_A is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'bar' in g_A did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'bar' in g_A is not implemented or raised an error")
