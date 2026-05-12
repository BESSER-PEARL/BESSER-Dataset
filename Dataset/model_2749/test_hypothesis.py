import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    B_RootB,
    B_B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_b_rootb_is_not_abstract():
    assert not inspect.isabstract(B_RootB)


def test_b_rootb_constructor_exists():
    assert callable(B_RootB.__init__)


def test_b_rootb_constructor_args():
    sig = inspect.signature(B_RootB.__init__)
    params = list(sig.parameters.keys())



def test_b_b_is_not_abstract():
    assert not inspect.isabstract(B_B)


def test_b_b_constructor_exists():
    assert callable(B_B.__init__)


def test_b_b_constructor_args():
    sig = inspect.signature(B_B.__init__)
    params = list(sig.parameters.keys())
    assert "b" in params, "Missing parameter 'b'"

def test_b_b_has_b():
    assert hasattr(B_B, "b")
    descriptor = None
    for klass in B_B.__mro__:
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
B_RootB_strategy = st.builds(
    B_RootB,
)
B_B_strategy = st.builds(
    B_B,
    b=
        st.integers()
)

@given(instance=B_RootB_strategy)
@settings(max_examples=50)
def test_b_rootb_instantiation(instance):
    assert isinstance(instance, B_RootB)

@given(instance=B_B_strategy)
@settings(max_examples=50)
def test_b_b_instantiation(instance):
    assert isinstance(instance, B_B)



@given(instance=B_B_strategy)
def test_b_b_b_setter(instance):
    original = instance.b
    instance.b = original
    assert instance.b == original
