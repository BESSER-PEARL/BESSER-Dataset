import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    testPackage::SubClass,
    testPackage::SuperClass,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testpackage::subclass_is_not_abstract():
    assert not inspect.isabstract(testPackage::SubClass)


def test_testpackage::subclass_constructor_exists():
    assert callable(testPackage::SubClass.__init__)


def test_testpackage::subclass_constructor_args():
    sig = inspect.signature(testPackage::SubClass.__init__)
    params = list(sig.parameters.keys())



def test_testpackage::superclass_is_not_abstract():
    assert not inspect.isabstract(testPackage::SuperClass)


def test_testpackage::superclass_constructor_exists():
    assert callable(testPackage::SuperClass.__init__)


def test_testpackage::superclass_constructor_args():
    sig = inspect.signature(testPackage::SuperClass.__init__)
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
testPackage::SubClass_strategy = st.builds(
    testPackage::SubClass,
)
testPackage::SuperClass_strategy = st.builds(
    testPackage::SuperClass,
)

@given(instance=testPackage::SubClass_strategy)
@settings(max_examples=50)
def test_testpackage::subclass_instantiation(instance):
    assert isinstance(instance, testPackage::SubClass)

@given(instance=testPackage::SuperClass_strategy)
@settings(max_examples=50)
def test_testpackage::superclass_instantiation(instance):
    assert isinstance(instance, testPackage::SuperClass)
