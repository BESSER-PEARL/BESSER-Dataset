import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    hExample_3_RHS_X,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hexample_3_rhs_x_is_not_abstract():
    assert not inspect.isabstract(hExample_3_RHS_X)


def test_hexample_3_rhs_x_constructor_exists():
    assert callable(hExample_3_RHS_X.__init__)


def test_hexample_3_rhs_x_constructor_args():
    sig = inspect.signature(hExample_3_RHS_X.__init__)
    params = list(sig.parameters.keys())
    assert "att2" in params, "Missing parameter 'att2'"
    assert "att1" in params, "Missing parameter 'att1'"

def test_hexample_3_rhs_x_has_att2():
    assert hasattr(hExample_3_RHS_X, "att2")
    descriptor = None
    for klass in hExample_3_RHS_X.__mro__:
        if "att2" in klass.__dict__:
            descriptor = klass.__dict__["att2"]
            break
    assert isinstance(descriptor, property)

def test_hexample_3_rhs_x_has_att1():
    assert hasattr(hExample_3_RHS_X, "att1")
    descriptor = None
    for klass in hExample_3_RHS_X.__mro__:
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
hExample_3_RHS_X_strategy = st.builds(
    hExample_3_RHS_X,
    att2=
        safe_text,
    att1=
        safe_text
)

@given(instance=hExample_3_RHS_X_strategy)
@settings(max_examples=50)
def test_hexample_3_rhs_x_instantiation(instance):
    assert isinstance(instance, hExample_3_RHS_X)



@given(instance=hExample_3_RHS_X_strategy)
def test_hexample_3_rhs_x_att2_setter(instance):
    original = instance.att2
    instance.att2 = original
    assert instance.att2 == original



@given(instance=hExample_3_RHS_X_strategy)
def test_hexample_3_rhs_x_att1_setter(instance):
    original = instance.att1
    instance.att1 = original
    assert instance.att1 == original
