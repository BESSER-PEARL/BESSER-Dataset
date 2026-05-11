import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    B::RootB,
    B::B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_b::rootb_is_not_abstract():
    assert not inspect.isabstract(B::RootB)


def test_b::rootb_constructor_exists():
    assert callable(B::RootB.__init__)


def test_b::rootb_constructor_args():
    sig = inspect.signature(B::RootB.__init__)
    params = list(sig.parameters.keys())



def test_b::b_is_not_abstract():
    assert not inspect.isabstract(B::B)


def test_b::b_constructor_exists():
    assert callable(B::B.__init__)


def test_b::b_constructor_args():
    sig = inspect.signature(B::B.__init__)
    params = list(sig.parameters.keys())
    assert "b" in params, "Missing parameter 'b'"

def test_b::b_has_b():
    assert hasattr(B::B, "b")
    descriptor = None
    for klass in B::B.__mro__:
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
B::RootB_strategy = st.builds(
    B::RootB,
)
B::B_strategy = st.builds(
    B::B,
    b=
        st.integers()
)

@given(instance=B::RootB_strategy)
@settings(max_examples=50)
def test_b::rootb_instantiation(instance):
    assert isinstance(instance, B::RootB)

@given(instance=B::B_strategy)
@settings(max_examples=50)
def test_b::b_instantiation(instance):
    assert isinstance(instance, B::B)

@given(instance=B::B_strategy)
def test_b::b_b_type(instance):
    assert isinstance(instance.b, int)


@given(instance=B::B_strategy)
def test_b::b_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original
