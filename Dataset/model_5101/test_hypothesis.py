import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    testPackage::SecondClass,
    testPackage::FirstClass,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testpackage::secondclass_is_not_abstract():
    assert not inspect.isabstract(testPackage::SecondClass)


def test_testpackage::secondclass_constructor_exists():
    assert callable(testPackage::SecondClass.__init__)


def test_testpackage::secondclass_constructor_args():
    sig = inspect.signature(testPackage::SecondClass.__init__)
    params = list(sig.parameters.keys())



def test_testpackage::firstclass_is_not_abstract():
    assert not inspect.isabstract(testPackage::FirstClass)


def test_testpackage::firstclass_constructor_exists():
    assert callable(testPackage::FirstClass.__init__)


def test_testpackage::firstclass_constructor_args():
    sig = inspect.signature(testPackage::FirstClass.__init__)
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
testPackage::SecondClass_strategy = st.builds(
    testPackage::SecondClass,
)
testPackage::FirstClass_strategy = st.builds(
    testPackage::FirstClass,
)

@given(instance=testPackage::SecondClass_strategy)
@settings(max_examples=50)
def test_testpackage::secondclass_instantiation(instance):
    assert isinstance(instance, testPackage::SecondClass)

@given(instance=testPackage::FirstClass_strategy)
@settings(max_examples=50)
def test_testpackage::firstclass_instantiation(instance):
    assert isinstance(instance, testPackage::FirstClass)
