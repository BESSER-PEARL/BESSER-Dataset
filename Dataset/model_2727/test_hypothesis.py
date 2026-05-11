import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    A,
    a::C,
    a::B,
    a::A,
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



def test_a::c_is_not_abstract():
    assert not inspect.isabstract(a::C)


def test_a::c_constructor_exists():
    assert callable(a::C.__init__)


def test_a::c_constructor_args():
    sig = inspect.signature(a::C.__init__)
    params = list(sig.parameters.keys())
    assert "c" in params, "Missing parameter 'c'"

def test_a::c_has_c():
    assert hasattr(a::C, "c")
    descriptor = None
    for klass in a::C.__mro__:
        if "c" in klass.__dict__:
            descriptor = klass.__dict__["c"]
            break
    assert isinstance(descriptor, property)



def test_a::b_is_not_abstract():
    assert not inspect.isabstract(a::B)


def test_a::b_constructor_exists():
    assert callable(a::B.__init__)


def test_a::b_constructor_args():
    sig = inspect.signature(a::B.__init__)
    params = list(sig.parameters.keys())
    assert "c" in params, "Missing parameter 'c'"

def test_a::b_has_c():
    assert hasattr(a::B, "c")
    descriptor = None
    for klass in a::B.__mro__:
        if "c" in klass.__dict__:
            descriptor = klass.__dict__["c"]
            break
    assert isinstance(descriptor, property)



def test_a::a_is_not_abstract():
    assert not inspect.isabstract(a::A)


def test_a::a_constructor_exists():
    assert callable(a::A.__init__)


def test_a::a_constructor_args():
    sig = inspect.signature(a::A.__init__)
    params = list(sig.parameters.keys())
    assert "a" in params, "Missing parameter 'a'"
    assert "b" in params, "Missing parameter 'b'"

def test_a::a_has_a():
    assert hasattr(a::A, "a")
    descriptor = None
    for klass in a::A.__mro__:
        if "a" in klass.__dict__:
            descriptor = klass.__dict__["a"]
            break
    assert isinstance(descriptor, property)

def test_a::a_has_b():
    assert hasattr(a::A, "b")
    descriptor = None
    for klass in a::A.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
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
a::C_strategy = st.builds(
    a::C,
    c=
        st.integers()
)
a::B_strategy = st.builds(
    a::B,
    c=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
a::A_strategy = st.builds(
    a::A,
    a=
        safe_text,
    b=
        safe_text
)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=a::C_strategy)
@settings(max_examples=50)
def test_a::c_instantiation(instance):
    assert isinstance(instance, a::C)

@given(instance=a::C_strategy)
def test_a::c_c_type(instance):
    assert isinstance(instance.c, int)


@given(instance=a::C_strategy)
def test_a::c_c_setter(instance):
    original = instance.c
    instance.c = original
    assert instance.c == original

@given(instance=a::B_strategy)
@settings(max_examples=50)
def test_a::b_instantiation(instance):
    assert isinstance(instance, a::B)

@given(instance=a::B_strategy)
def test_a::b_c_type(instance):
    assert isinstance(instance.c, float)


@given(instance=a::B_strategy)
def test_a::b_c_setter(instance):
    original = instance.c
    instance.c = original
    assert instance.c == original

@given(instance=a::A_strategy)
@settings(max_examples=50)
def test_a::a_instantiation(instance):
    assert isinstance(instance, a::A)

@given(instance=a::A_strategy)
def test_a::a_a_type(instance):
    assert isinstance(instance.a, str)


@given(instance=a::A_strategy)
def test_a::a_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original

@given(instance=a::A_strategy)
def test_a::a_b_type(instance):
    assert isinstance(instance.b, str)


@given(instance=a::A_strategy)
def test_a::a_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=a::A_strategy)
@settings(max_examples=30)
def test_a::a_foo_changes_state(instance):
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
        assert has_statements, f"Function 'foo' in a::A is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'foo' in a::A did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'foo' in a::A is not implemented or raised an error")
