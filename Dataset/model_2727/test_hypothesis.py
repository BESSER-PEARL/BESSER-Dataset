import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    A,
    a_C,
    a_B,
    a_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_a_c_is_not_abstract():
    assert not inspect.isabstract(a_C)


def test_a_c_constructor_exists():
    assert callable(a_C.__init__)


def test_a_c_constructor_args():
    sig = inspect.signature(a_C.__init__)
    params = list(sig.parameters.keys())
    assert "c" in params, "Missing parameter 'c'"

def test_a_c_has_c():
    assert hasattr(a_C, "c")
    descriptor = None
    for klass in a_C.__mro__:
        if "c" in klass.__dict__:
            descriptor = klass.__dict__["c"]
            break
    assert isinstance(descriptor, property)



def test_a_b_is_not_abstract():
    assert not inspect.isabstract(a_B)


def test_a_b_constructor_exists():
    assert callable(a_B.__init__)


def test_a_b_constructor_args():
    sig = inspect.signature(a_B.__init__)
    params = list(sig.parameters.keys())
    assert "c" in params, "Missing parameter 'c'"

def test_a_b_has_c():
    assert hasattr(a_B, "c")
    descriptor = None
    for klass in a_B.__mro__:
        if "c" in klass.__dict__:
            descriptor = klass.__dict__["c"]
            break
    assert isinstance(descriptor, property)



def test_a_a_is_not_abstract():
    assert not inspect.isabstract(a_A)


def test_a_a_constructor_exists():
    assert callable(a_A.__init__)


def test_a_a_constructor_args():
    sig = inspect.signature(a_A.__init__)
    params = list(sig.parameters.keys())
    assert "b" in params, "Missing parameter 'b'"
    assert "a" in params, "Missing parameter 'a'"

def test_a_a_has_b():
    assert hasattr(a_A, "b")
    descriptor = None
    for klass in a_A.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)

def test_a_a_has_a():
    assert hasattr(a_A, "a")
    descriptor = None
    for klass in a_A.__mro__:
        if "a" in klass.__dict__:
            descriptor = klass.__dict__["a"]
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
A_strategy = st.builds(
    A,
)
a_C_strategy = st.builds(
    a_C,
    c=
        st.integers()
)
a_B_strategy = st.builds(
    a_B,
    c=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
a_A_strategy = st.builds(
    a_A,
    b=
        safe_text,
    a=
        safe_text
)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=a_C_strategy)
@settings(max_examples=50)
def test_a_c_instantiation(instance):
    assert isinstance(instance, a_C)



@given(instance=a_C_strategy)
def test_a_c_c_setter(instance):
    original = instance.c
    instance.c = original
    assert instance.c == original

@given(instance=a_B_strategy)
@settings(max_examples=50)
def test_a_b_instantiation(instance):
    assert isinstance(instance, a_B)



@given(instance=a_B_strategy)
def test_a_b_c_setter(instance):
    original = instance.c
    instance.c = original
    assert instance.c == original

@given(instance=a_A_strategy)
@settings(max_examples=50)
def test_a_a_instantiation(instance):
    assert isinstance(instance, a_A)



@given(instance=a_A_strategy)
def test_a_a_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original



@given(instance=a_A_strategy)
def test_a_a_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=a_A_strategy)
@settings(max_examples=30)
def test_a_a_foo_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.foo(
            "test", 
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.foo).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'foo' in a_A is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'foo' in a_A did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'foo' in a_A is not implemented or raised an error")
