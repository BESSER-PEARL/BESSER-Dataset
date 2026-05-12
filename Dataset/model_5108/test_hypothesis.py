import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    testPackage_SubClass,
    testPackage_SuperClass,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testpackage_subclass_is_not_abstract():
    assert not inspect.isabstract(testPackage_SubClass)


def test_testpackage_subclass_constructor_exists():
    assert callable(testPackage_SubClass.__init__)


def test_testpackage_subclass_constructor_args():
    sig = inspect.signature(testPackage_SubClass.__init__)
    params = list(sig.parameters.keys())



def test_testpackage_superclass_is_not_abstract():
    assert not inspect.isabstract(testPackage_SuperClass)


def test_testpackage_superclass_constructor_exists():
    assert callable(testPackage_SuperClass.__init__)


def test_testpackage_superclass_constructor_args():
    sig = inspect.signature(testPackage_SuperClass.__init__)
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
testPackage_SubClass_strategy = st.builds(
    testPackage_SubClass,
)
testPackage_SuperClass_strategy = st.builds(
    testPackage_SuperClass,
)

@given(instance=testPackage_SubClass_strategy)
@settings(max_examples=50)
def test_testpackage_subclass_instantiation(instance):
    assert isinstance(instance, testPackage_SubClass)

@given(instance=testPackage_SuperClass_strategy)
@settings(max_examples=50)
def test_testpackage_superclass_instantiation(instance):
    assert isinstance(instance, testPackage_SuperClass)
