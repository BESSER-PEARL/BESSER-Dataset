import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    hExamle_4_RHS_X,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hexamle_4_rhs_x_is_not_abstract():
    assert not inspect.isabstract(hExamle_4_RHS_X)


def test_hexamle_4_rhs_x_constructor_exists():
    assert callable(hExamle_4_RHS_X.__init__)


def test_hexamle_4_rhs_x_constructor_args():
    sig = inspect.signature(hExamle_4_RHS_X.__init__)
    params = list(sig.parameters.keys())
    assert "att1" in params, "Missing parameter 'att1'"

def test_hexamle_4_rhs_x_has_att1():
    assert hasattr(hExamle_4_RHS_X, "att1")
    descriptor = None
    for klass in hExamle_4_RHS_X.__mro__:
        if "att1" in klass.__dict__:
            descriptor = klass.__dict__["att1"]
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
hExamle_4_RHS_X_strategy = st.builds(
    hExamle_4_RHS_X,
    att1=
        safe_text
)

@given(instance=hExamle_4_RHS_X_strategy)
@settings(max_examples=50)
def test_hexamle_4_rhs_x_instantiation(instance):
    assert isinstance(instance, hExamle_4_RHS_X)



@given(instance=hExamle_4_RHS_X_strategy)
def test_hexamle_4_rhs_x_att1_setter(instance):
    original = instance.att1
    instance.att1 = original
    assert instance.att1 == original
