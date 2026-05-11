import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    hExample::1::RHS::Y,
    hExample::1::RHS::X,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hexample::1::rhs::y_is_not_abstract():
    assert not inspect.isabstract(hExample::1::RHS::Y)


def test_hexample::1::rhs::y_constructor_exists():
    assert callable(hExample::1::RHS::Y.__init__)


def test_hexample::1::rhs::y_constructor_args():
    sig = inspect.signature(hExample::1::RHS::Y.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_hexample::1::rhs::y_has_label():
    assert hasattr(hExample::1::RHS::Y, "label")
    descriptor = None
    for klass in hExample::1::RHS::Y.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_hexample::1::rhs::x_is_not_abstract():
    assert not inspect.isabstract(hExample::1::RHS::X)


def test_hexample::1::rhs::x_constructor_exists():
    assert callable(hExample::1::RHS::X.__init__)


def test_hexample::1::rhs::x_constructor_args():
    sig = inspect.signature(hExample::1::RHS::X.__init__)
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
hExample::1::RHS::Y_strategy = st.builds(
    hExample::1::RHS::Y,
    label=
        safe_text
)
hExample::1::RHS::X_strategy = st.builds(
    hExample::1::RHS::X,
)

@given(instance=hExample::1::RHS::Y_strategy)
@settings(max_examples=50)
def test_hexample::1::rhs::y_instantiation(instance):
    assert isinstance(instance, hExample::1::RHS::Y)

@given(instance=hExample::1::RHS::Y_strategy)
def test_hexample::1::rhs::y_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=hExample::1::RHS::Y_strategy)
def test_hexample::1::rhs::y_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=hExample::1::RHS::X_strategy)
@settings(max_examples=50)
def test_hexample::1::rhs::x_instantiation(instance):
    assert isinstance(instance, hExample::1::RHS::X)
