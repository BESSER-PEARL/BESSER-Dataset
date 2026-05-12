import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Basic2_C,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_basic2_c_is_not_abstract():
    assert not inspect.isabstract(Basic2_C)


def test_basic2_c_constructor_exists():
    assert callable(Basic2_C.__init__)


def test_basic2_c_constructor_args():
    sig = inspect.signature(Basic2_C.__init__)
    params = list(sig.parameters.keys())
    assert "a" in params, "Missing parameter 'a'"
    assert "c" in params, "Missing parameter 'c'"
    assert "b" in params, "Missing parameter 'b'"

def test_basic2_c_has_a():
    assert hasattr(Basic2_C, "a")
    descriptor = None
    for klass in Basic2_C.__mro__:
        if "a" in klass.__dict__:
            descriptor = klass.__dict__["a"]
            break
    assert isinstance(descriptor, property)

def test_basic2_c_has_c():
    assert hasattr(Basic2_C, "c")
    descriptor = None
    for klass in Basic2_C.__mro__:
        if "c" in klass.__dict__:
            descriptor = klass.__dict__["c"]
            break
    assert isinstance(descriptor, property)

def test_basic2_c_has_b():
    assert hasattr(Basic2_C, "b")
    descriptor = None
    for klass in Basic2_C.__mro__:
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
Basic2_C_strategy = st.builds(
    Basic2_C,
    a=
        st.integers(),
    c=
        st.integers(),
    b=
        st.integers()
)

@given(instance=Basic2_C_strategy)
@settings(max_examples=50)
def test_basic2_c_instantiation(instance):
    assert isinstance(instance, Basic2_C)



@given(instance=Basic2_C_strategy)
def test_basic2_c_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original



@given(instance=Basic2_C_strategy)
def test_basic2_c_c_setter(instance):
    original = instance.c
    instance.c = original
    assert instance.c == original



@given(instance=Basic2_C_strategy)
def test_basic2_c_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original
