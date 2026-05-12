import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    hExample_1_LHS_B,
    hExample_1_LHS_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hexample_1_lhs_b_is_not_abstract():
    assert not inspect.isabstract(hExample_1_LHS_B)


def test_hexample_1_lhs_b_constructor_exists():
    assert callable(hExample_1_LHS_B.__init__)


def test_hexample_1_lhs_b_constructor_args():
    sig = inspect.signature(hExample_1_LHS_B.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hexample_1_lhs_b_has_name():
    assert hasattr(hExample_1_LHS_B, "name")
    descriptor = None
    for klass in hExample_1_LHS_B.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hexample_1_lhs_a_is_not_abstract():
    assert not inspect.isabstract(hExample_1_LHS_A)


def test_hexample_1_lhs_a_constructor_exists():
    assert callable(hExample_1_LHS_A.__init__)


def test_hexample_1_lhs_a_constructor_args():
    sig = inspect.signature(hExample_1_LHS_A.__init__)
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
hExample_1_LHS_B_strategy = st.builds(
    hExample_1_LHS_B,
    name=
        safe_text
)
hExample_1_LHS_A_strategy = st.builds(
    hExample_1_LHS_A,
)

@given(instance=hExample_1_LHS_B_strategy)
@settings(max_examples=50)
def test_hexample_1_lhs_b_instantiation(instance):
    assert isinstance(instance, hExample_1_LHS_B)



@given(instance=hExample_1_LHS_B_strategy)
def test_hexample_1_lhs_b_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=hExample_1_LHS_A_strategy)
@settings(max_examples=50)
def test_hexample_1_lhs_a_instantiation(instance):
    assert isinstance(instance, hExample_1_LHS_A)
