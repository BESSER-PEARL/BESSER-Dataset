import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    astrans_B,
    astrans_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_astrans_b_is_not_abstract():
    assert not inspect.isabstract(astrans_B)


def test_astrans_b_constructor_exists():
    assert callable(astrans_B.__init__)


def test_astrans_b_constructor_args():
    sig = inspect.signature(astrans_B.__init__)
    params = list(sig.parameters.keys())



def test_astrans_a_is_not_abstract():
    assert not inspect.isabstract(astrans_A)


def test_astrans_a_constructor_exists():
    assert callable(astrans_A.__init__)


def test_astrans_a_constructor_args():
    sig = inspect.signature(astrans_A.__init__)
    params = list(sig.parameters.keys())
    assert "ra" in params, "Missing parameter 'ra'"

def test_astrans_a_has_ra():
    assert hasattr(astrans_A, "ra")
    descriptor = None
    for klass in astrans_A.__mro__:
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
astrans_B_strategy = st.builds(
    astrans_B,
)
astrans_A_strategy = st.builds(
    astrans_A,
    ra=
        safe_text
)

@given(instance=astrans_B_strategy)
@settings(max_examples=50)
def test_astrans_b_instantiation(instance):
    assert isinstance(instance, astrans_B)

@given(instance=astrans_A_strategy)
@settings(max_examples=50)
def test_astrans_a_instantiation(instance):
    assert isinstance(instance, astrans_A)



@given(instance=astrans_A_strategy)
def test_astrans_a_ra_setter(instance):
    original = instance.ra
    instance.ra = original
    assert instance.ra == original
