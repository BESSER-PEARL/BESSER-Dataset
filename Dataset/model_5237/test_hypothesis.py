import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Basic4::C,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_basic4::c_is_not_abstract():
    assert not inspect.isabstract(Basic4::C)


def test_basic4::c_constructor_exists():
    assert callable(Basic4::C.__init__)


def test_basic4::c_constructor_args():
    sig = inspect.signature(Basic4::C.__init__)
    params = list(sig.parameters.keys())
    assert "a" in params, "Missing parameter 'a'"
    assert "c" in params, "Missing parameter 'c'"
    assert "d" in params, "Missing parameter 'd'"
    assert "b" in params, "Missing parameter 'b'"

def test_basic4::c_has_a():
    assert hasattr(Basic4::C, "a")
    descriptor = None
    for klass in Basic4::C.__mro__:
        if "a" in klass.__dict__:
            descriptor = klass.__dict__["a"]
            break
    assert isinstance(descriptor, property)

def test_basic4::c_has_c():
    assert hasattr(Basic4::C, "c")
    descriptor = None
    for klass in Basic4::C.__mro__:
        if "c" in klass.__dict__:
            descriptor = klass.__dict__["c"]
            break
    assert isinstance(descriptor, property)

def test_basic4::c_has_d():
    assert hasattr(Basic4::C, "d")
    descriptor = None
    for klass in Basic4::C.__mro__:
        if "d" in klass.__dict__:
            descriptor = klass.__dict__["d"]
            break
    assert isinstance(descriptor, property)

def test_basic4::c_has_b():
    assert hasattr(Basic4::C, "b")
    descriptor = None
    for klass in Basic4::C.__mro__:
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
Basic4::C_strategy = st.builds(
    Basic4::C,
    a=
        st.booleans(),
    c=
        st.booleans(),
    d=
        st.booleans(),
    b=
        st.booleans()
)

@given(instance=Basic4::C_strategy)
@settings(max_examples=50)
def test_basic4::c_instantiation(instance):
    assert isinstance(instance, Basic4::C)

@given(instance=Basic4::C_strategy)
def test_basic4::c_a_type(instance):
    assert isinstance(instance.a, bool)


@given(instance=Basic4::C_strategy)
def test_basic4::c_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original

@given(instance=Basic4::C_strategy)
def test_basic4::c_c_type(instance):
    assert isinstance(instance.c, bool)


@given(instance=Basic4::C_strategy)
def test_basic4::c_c_setter(instance):
    original = instance.c
    instance.c = original
    assert instance.c == original

@given(instance=Basic4::C_strategy)
def test_basic4::c_d_type(instance):
    assert isinstance(instance.d, bool)


@given(instance=Basic4::C_strategy)
def test_basic4::c_d_setter(instance):
    original = instance.d
    instance.d = original
    assert instance.d == original

@given(instance=Basic4::C_strategy)
def test_basic4::c_b_type(instance):
    assert isinstance(instance.b, bool)


@given(instance=Basic4::C_strategy)
def test_basic4::c_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original
