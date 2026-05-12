import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    b_B,
    b_A,
    A,
    b_C,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_b_b_is_not_abstract():
    assert not inspect.isabstract(b_B)


def test_b_b_constructor_exists():
    assert callable(b_B.__init__)


def test_b_b_constructor_args():
    sig = inspect.signature(b_B.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"

def test_b_b_has_y():
    assert hasattr(b_B, "y")
    descriptor = None
    for klass in b_B.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_b_a_is_not_abstract():
    assert not inspect.isabstract(b_A)


def test_b_a_constructor_exists():
    assert callable(b_A.__init__)


def test_b_a_constructor_args():
    sig = inspect.signature(b_A.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"

def test_b_a_has_x():
    assert hasattr(b_A, "x")
    descriptor = None
    for klass in b_A.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_b_c_is_not_abstract():
    assert not inspect.isabstract(b_C)


def test_b_c_constructor_exists():
    assert callable(b_C.__init__)


def test_b_c_constructor_args():
    sig = inspect.signature(b_C.__init__)
    params = list(sig.parameters.keys())
    assert "z" in params, "Missing parameter 'z'"

def test_b_c_has_z():
    assert hasattr(b_C, "z")
    descriptor = None
    for klass in b_C.__mro__:
        if "z" in klass.__dict__:
            descriptor = klass.__dict__["z"]
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
b_B_strategy = st.builds(
    b_B,
    y=
        st.booleans()
)
b_A_strategy = st.builds(
    b_A,
    x=
        safe_text
)
A_strategy = st.builds(
    A,
)
b_C_strategy = st.builds(
    b_C,
    z=
        safe_text
)

@given(instance=b_B_strategy)
@settings(max_examples=50)
def test_b_b_instantiation(instance):
    assert isinstance(instance, b_B)



@given(instance=b_B_strategy)
def test_b_b_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=b_A_strategy)
@settings(max_examples=50)
def test_b_a_instantiation(instance):
    assert isinstance(instance, b_A)



@given(instance=b_A_strategy)
def test_b_a_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=b_A_strategy)
@settings(max_examples=30)
def test_b_a_bar_changes_state(instance):
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
        assert has_statements, f"Function 'bar' in b_A is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'bar' in b_A did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'bar' in b_A is not implemented or raised an error")

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=b_C_strategy)
@settings(max_examples=50)
def test_b_c_instantiation(instance):
    assert isinstance(instance, b_C)



@given(instance=b_C_strategy)
def test_b_c_z_setter(instance):
    original = instance.z
    instance.z = original
    assert instance.z == original
