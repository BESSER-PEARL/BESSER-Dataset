import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    astrans::B,
    astrans::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_astrans::b_is_not_abstract():
    assert not inspect.isabstract(astrans::B)


def test_astrans::b_constructor_exists():
    assert callable(astrans::B.__init__)


def test_astrans::b_constructor_args():
    sig = inspect.signature(astrans::B.__init__)
    params = list(sig.parameters.keys())



def test_astrans::a_is_not_abstract():
    assert not inspect.isabstract(astrans::A)


def test_astrans::a_constructor_exists():
    assert callable(astrans::A.__init__)


def test_astrans::a_constructor_args():
    sig = inspect.signature(astrans::A.__init__)
    params = list(sig.parameters.keys())
    assert "ra" in params, "Missing parameter 'ra'"

def test_astrans::a_has_ra():
    assert hasattr(astrans::A, "ra")
    descriptor = None
    for klass in astrans::A.__mro__:
        if "ra" in klass.__dict__:
            descriptor = klass.__dict__["ra"]
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
astrans::B_strategy = st.builds(
    astrans::B,
)
astrans::A_strategy = st.builds(
    astrans::A,
    ra=
        safe_text
)

@given(instance=astrans::B_strategy)
@settings(max_examples=50)
def test_astrans::b_instantiation(instance):
    assert isinstance(instance, astrans::B)

@given(instance=astrans::A_strategy)
@settings(max_examples=50)
def test_astrans::a_instantiation(instance):
    assert isinstance(instance, astrans::A)

@given(instance=astrans::A_strategy)
def test_astrans::a_ra_type(instance):
    assert isinstance(instance.ra, str)


@given(instance=astrans::A_strategy)
def test_astrans::a_ra_setter(instance):
    original = instance.ra
    instance.ra = original
    assert instance.ra == original
