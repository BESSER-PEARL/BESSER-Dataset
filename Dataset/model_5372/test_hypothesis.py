import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    hExample_1_RHS_Y,
    hExample_1_RHS_X,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hexample_1_rhs_y_is_not_abstract():
    assert not inspect.isabstract(hExample_1_RHS_Y)


def test_hexample_1_rhs_y_constructor_exists():
    assert callable(hExample_1_RHS_Y.__init__)


def test_hexample_1_rhs_y_constructor_args():
    sig = inspect.signature(hExample_1_RHS_Y.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_hexample_1_rhs_y_has_label():
    assert hasattr(hExample_1_RHS_Y, "label")
    descriptor = None
    for klass in hExample_1_RHS_Y.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_hexample_1_rhs_x_is_not_abstract():
    assert not inspect.isabstract(hExample_1_RHS_X)


def test_hexample_1_rhs_x_constructor_exists():
    assert callable(hExample_1_RHS_X.__init__)


def test_hexample_1_rhs_x_constructor_args():
    sig = inspect.signature(hExample_1_RHS_X.__init__)
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
hExample_1_RHS_Y_strategy = st.builds(
    hExample_1_RHS_Y,
    label=
        safe_text
)
hExample_1_RHS_X_strategy = st.builds(
    hExample_1_RHS_X,
)

@given(instance=hExample_1_RHS_Y_strategy)
@settings(max_examples=50)
def test_hexample_1_rhs_y_instantiation(instance):
    assert isinstance(instance, hExample_1_RHS_Y)



@given(instance=hExample_1_RHS_Y_strategy)
def test_hexample_1_rhs_y_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=hExample_1_RHS_X_strategy)
@settings(max_examples=50)
def test_hexample_1_rhs_x_instantiation(instance):
    assert isinstance(instance, hExample_1_RHS_X)
