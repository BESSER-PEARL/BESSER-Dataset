import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Basic::C,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_basic::c_is_not_abstract():
    assert not inspect.isabstract(Basic::C)


def test_basic::c_constructor_exists():
    assert callable(Basic::C.__init__)


def test_basic::c_constructor_args():
    sig = inspect.signature(Basic::C.__init__)
    params = list(sig.parameters.keys())
    assert "b" in params, "Missing parameter 'b'"
    assert "a" in params, "Missing parameter 'a'"

def test_basic::c_has_b():
    assert hasattr(Basic::C, "b")
    descriptor = None
    for klass in Basic::C.__mro__:
        if "b" in klass.__dict__:
            descriptor = klass.__dict__["b"]
            break
    assert isinstance(descriptor, property)

def test_basic::c_has_a():
    assert hasattr(Basic::C, "a")
    descriptor = None
    for klass in Basic::C.__mro__:
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
Basic::C_strategy = st.builds(
    Basic::C,
    b=
        st.integers(),
    a=
        st.integers()
)

@given(instance=Basic::C_strategy)
@settings(max_examples=50)
def test_basic::c_instantiation(instance):
    assert isinstance(instance, Basic::C)

@given(instance=Basic::C_strategy)
def test_basic::c_b_type(instance):
    assert isinstance(instance.b, int)


@given(instance=Basic::C_strategy)
def test_basic::c_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original

@given(instance=Basic::C_strategy)
def test_basic::c_a_type(instance):
    assert isinstance(instance.a, int)


@given(instance=Basic::C_strategy)
def test_basic::c_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original
