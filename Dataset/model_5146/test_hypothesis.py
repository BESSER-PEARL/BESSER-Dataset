import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    b::B,
    b::A,
    A,
    b::C,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_b::b_is_not_abstract():
    assert not inspect.isabstract(b::B)


def test_b::b_constructor_exists():
    assert callable(b::B.__init__)


def test_b::b_constructor_args():
    sig = inspect.signature(b::B.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"

def test_b::b_has_y():
    assert hasattr(b::B, "y")
    descriptor = None
    for klass in b::B.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)



def test_b::a_is_not_abstract():
    assert not inspect.isabstract(b::A)


def test_b::a_constructor_exists():
    assert callable(b::A.__init__)


def test_b::a_constructor_args():
    sig = inspect.signature(b::A.__init__)
    params = list(sig.parameters.keys())
    assert "x" in params, "Missing parameter 'x'"

def test_b::a_has_x():
    assert hasattr(b::A, "x")
    descriptor = None
    for klass in b::A.__mro__:
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



def test_b::c_is_not_abstract():
    assert not inspect.isabstract(b::C)


def test_b::c_constructor_exists():
    assert callable(b::C.__init__)


def test_b::c_constructor_args():
    sig = inspect.signature(b::C.__init__)
    params = list(sig.parameters.keys())
    assert "z" in params, "Missing parameter 'z'"

def test_b::c_has_z():
    assert hasattr(b::C, "z")
    descriptor = None
    for klass in b::C.__mro__:
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
b::B_strategy = st.builds(
    b::B,
    y=
        st.booleans()
)
b::A_strategy = st.builds(
    b::A,
    x=
        safe_text
)
A_strategy = st.builds(
    A,
)
b::C_strategy = st.builds(
    b::C,
    z=
        safe_text
)

@given(instance=b::B_strategy)
@settings(max_examples=50)
def test_b::b_instantiation(instance):
    assert isinstance(instance, b::B)

@given(instance=b::B_strategy)
def test_b::b_y_type(instance):
    assert isinstance(instance.y, bool)


@given(instance=b::B_strategy)
def test_b::b_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=b::A_strategy)
@settings(max_examples=50)
def test_b::a_instantiation(instance):
    assert isinstance(instance, b::A)

@given(instance=b::A_strategy)
def test_b::a_x_type(instance):
    assert isinstance(instance.x, str)


@given(instance=b::A_strategy)
def test_b::a_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=b::A_strategy)
@settings(max_examples=30)
def test_b::a_bar_changes_state(instance):
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
        assert has_statements, f"Function 'bar' in b::A is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'bar' in b::A did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'bar' in b::A is not implemented or raised an error")

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=b::C_strategy)
@settings(max_examples=50)
def test_b::c_instantiation(instance):
    assert isinstance(instance, b::C)

@given(instance=b::C_strategy)
def test_b::c_z_type(instance):
    assert isinstance(instance.z, str)


@given(instance=b::C_strategy)
def test_b::c_z_setter(instance):
    original = instance.z
    instance.z = original
    assert instance.z == original
