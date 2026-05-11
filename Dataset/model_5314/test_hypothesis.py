import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    hExample::1::LHS::B,
    hExample::1::LHS::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hexample::1::lhs::b_is_not_abstract():
    assert not inspect.isabstract(hExample::1::LHS::B)


def test_hexample::1::lhs::b_constructor_exists():
    assert callable(hExample::1::LHS::B.__init__)


def test_hexample::1::lhs::b_constructor_args():
    sig = inspect.signature(hExample::1::LHS::B.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hexample::1::lhs::b_has_name():
    assert hasattr(hExample::1::LHS::B, "name")
    descriptor = None
    for klass in hExample::1::LHS::B.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hexample::1::lhs::a_is_not_abstract():
    assert not inspect.isabstract(hExample::1::LHS::A)


def test_hexample::1::lhs::a_constructor_exists():
    assert callable(hExample::1::LHS::A.__init__)


def test_hexample::1::lhs::a_constructor_args():
    sig = inspect.signature(hExample::1::LHS::A.__init__)
    params = list(sig.parameters.keys())


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
hExample::1::LHS::B_strategy = st.builds(
    hExample::1::LHS::B,
    name=
        safe_text
)
hExample::1::LHS::A_strategy = st.builds(
    hExample::1::LHS::A,
)

@given(instance=hExample::1::LHS::B_strategy)
@settings(max_examples=50)
def test_hexample::1::lhs::b_instantiation(instance):
    assert isinstance(instance, hExample::1::LHS::B)

@given(instance=hExample::1::LHS::B_strategy)
def test_hexample::1::lhs::b_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=hExample::1::LHS::B_strategy)
def test_hexample::1::lhs::b_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=hExample::1::LHS::A_strategy)
@settings(max_examples=50)
def test_hexample::1::lhs::a_instantiation(instance):
    assert isinstance(instance, hExample::1::LHS::A)
