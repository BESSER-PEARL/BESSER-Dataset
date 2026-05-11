import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    testSubpackages1::subpackage3::class4,
    testSubpackages2::root::class2,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testsubpackages1::subpackage3::class4_is_not_abstract():
    assert not inspect.isabstract(testSubpackages1::subpackage3::class4)


def test_testsubpackages1::subpackage3::class4_constructor_exists():
    assert callable(testSubpackages1::subpackage3::class4.__init__)


def test_testsubpackages1::subpackage3::class4_constructor_args():
    sig = inspect.signature(testSubpackages1::subpackage3::class4.__init__)
    params = list(sig.parameters.keys())



def test_testsubpackages2::root::class2_is_not_abstract():
    assert not inspect.isabstract(testSubpackages2::root::class2)


def test_testsubpackages2::root::class2_constructor_exists():
    assert callable(testSubpackages2::root::class2.__init__)


def test_testsubpackages2::root::class2_constructor_args():
    sig = inspect.signature(testSubpackages2::root::class2.__init__)
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
testSubpackages1::subpackage3::class4_strategy = st.builds(
    testSubpackages1::subpackage3::class4,
)
testSubpackages2::root::class2_strategy = st.builds(
    testSubpackages2::root::class2,
)

@given(instance=testSubpackages1::subpackage3::class4_strategy)
@settings(max_examples=50)
def test_testsubpackages1::subpackage3::class4_instantiation(instance):
    assert isinstance(instance, testSubpackages1::subpackage3::class4)

@given(instance=testSubpackages2::root::class2_strategy)
@settings(max_examples=50)
def test_testsubpackages2::root::class2_instantiation(instance):
    assert isinstance(instance, testSubpackages2::root::class2)
