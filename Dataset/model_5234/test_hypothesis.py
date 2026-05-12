import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Basic_C,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_basic_c_is_not_abstract():
    assert not inspect.isabstract(Basic_C)


def test_basic_c_constructor_exists():
    assert callable(Basic_C.__init__)


def test_basic_c_constructor_args():
    sig = inspect.signature(Basic_C.__init__)
    params = list(sig.parameters.keys())
    assert "a" in params, "Missing parameter 'a'"
    assert "b" in params, "Missing parameter 'b'"

def test_basic_c_has_a():
    assert hasattr(Basic_C, "a")
    descriptor = None
    for klass in Basic_C.__mro__:
        if "a" in klass.__dict__:
            descriptor = klass.__dict__["a"]
            break
    assert isinstance(descriptor, property)

def test_basic_c_has_b():
    assert hasattr(Basic_C, "b")
    descriptor = None
    for klass in Basic_C.__mro__:
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
Basic_C_strategy = st.builds(
    Basic_C,
    a=
        st.integers(),
    b=
        st.integers()
)

@given(instance=Basic_C_strategy)
@settings(max_examples=50)
def test_basic_c_instantiation(instance):
    assert isinstance(instance, Basic_C)



@given(instance=Basic_C_strategy)
def test_basic_c_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original



@given(instance=Basic_C_strategy)
def test_basic_c_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original
