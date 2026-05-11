import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ale1::RA2,
    ale1::RA1,
    ale1::A1,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ale1::ra2_is_not_abstract():
    assert not inspect.isabstract(ale1::RA2)


def test_ale1::ra2_constructor_exists():
    assert callable(ale1::RA2.__init__)


def test_ale1::ra2_constructor_args():
    sig = inspect.signature(ale1::RA2.__init__)
    params = list(sig.parameters.keys())



def test_ale1::ra1_is_not_abstract():
    assert not inspect.isabstract(ale1::RA1)


def test_ale1::ra1_constructor_exists():
    assert callable(ale1::RA1.__init__)


def test_ale1::ra1_constructor_args():
    sig = inspect.signature(ale1::RA1.__init__)
    params = list(sig.parameters.keys())



def test_ale1::a1_is_not_abstract():
    assert not inspect.isabstract(ale1::A1)


def test_ale1::a1_constructor_exists():
    assert callable(ale1::A1.__init__)


def test_ale1::a1_constructor_args():
    sig = inspect.signature(ale1::A1.__init__)
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
ale1::RA2_strategy = st.builds(
    ale1::RA2,
)
ale1::RA1_strategy = st.builds(
    ale1::RA1,
)
ale1::A1_strategy = st.builds(
    ale1::A1,
)

@given(instance=ale1::RA2_strategy)
@settings(max_examples=50)
def test_ale1::ra2_instantiation(instance):
    assert isinstance(instance, ale1::RA2)

@given(instance=ale1::RA1_strategy)
@settings(max_examples=50)
def test_ale1::ra1_instantiation(instance):
    assert isinstance(instance, ale1::RA1)

@given(instance=ale1::A1_strategy)
@settings(max_examples=50)
def test_ale1::a1_instantiation(instance):
    assert isinstance(instance, ale1::A1)
