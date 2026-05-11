import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    minimalB::B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_minimalb::b_is_not_abstract():
    assert not inspect.isabstract(minimalB::B)


def test_minimalb::b_constructor_exists():
    assert callable(minimalB::B.__init__)


def test_minimalb::b_constructor_args():
    sig = inspect.signature(minimalB::B.__init__)
    params = list(sig.parameters.keys())
    assert "b" in params, "Missing parameter 'b'"

def test_minimalb::b_has_b():
    assert hasattr(minimalB::B, "b")
    descriptor = None
    for klass in minimalB::B.__mro__:
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
minimalB::B_strategy = st.builds(
    minimalB::B,
    b=
        st.integers()
)

@given(instance=minimalB::B_strategy)
@settings(max_examples=50)
def test_minimalb::b_instantiation(instance):
    assert isinstance(instance, minimalB::B)

@given(instance=minimalB::B_strategy)
def test_minimalb::b_b_type(instance):
    assert isinstance(instance.b, int)


@given(instance=minimalB::B_strategy)
def test_minimalb::b_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original
