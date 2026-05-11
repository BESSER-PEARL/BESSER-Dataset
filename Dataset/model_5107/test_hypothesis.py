import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    testPackage::SecondClass,
    testPackage::FirstClass,
    SecondClass,
    testPackage::SecondSubClass,
    FirstClass,
    testPackage::FirstSubClass,
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



def test_secondclass_is_not_abstract():
    assert not inspect.isabstract(SecondClass)


def test_secondclass_constructor_exists():
    assert callable(SecondClass.__init__)


def test_secondclass_constructor_args():
    sig = inspect.signature(SecondClass.__init__)
    params = list(sig.parameters.keys())



def test_testpackage::secondsubclass_is_not_abstract():
    assert not inspect.isabstract(testPackage::SecondSubClass)


def test_testpackage::secondsubclass_constructor_exists():
    assert callable(testPackage::SecondSubClass.__init__)


def test_testpackage::secondsubclass_constructor_args():
    sig = inspect.signature(testPackage::SecondSubClass.__init__)
    params = list(sig.parameters.keys())



def test_firstclass_is_not_abstract():
    assert not inspect.isabstract(FirstClass)


def test_firstclass_constructor_exists():
    assert callable(FirstClass.__init__)


def test_firstclass_constructor_args():
    sig = inspect.signature(FirstClass.__init__)
    params = list(sig.parameters.keys())



def test_testpackage::firstsubclass_is_not_abstract():
    assert not inspect.isabstract(testPackage::FirstSubClass)


def test_testpackage::firstsubclass_constructor_exists():
    assert callable(testPackage::FirstSubClass.__init__)


def test_testpackage::firstsubclass_constructor_args():
    sig = inspect.signature(testPackage::FirstSubClass.__init__)
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
SecondClass_strategy = st.builds(
    SecondClass,
)
testPackage::SecondSubClass_strategy = st.builds(
    testPackage::SecondSubClass,
)
FirstClass_strategy = st.builds(
    FirstClass,
)
testPackage::FirstSubClass_strategy = st.builds(
    testPackage::FirstSubClass,
)

@given(instance=testPackage::SecondClass_strategy)
@settings(max_examples=50)
def test_testpackage::secondclass_instantiation(instance):
    assert isinstance(instance, testPackage::SecondClass)

@given(instance=testPackage::FirstClass_strategy)
@settings(max_examples=50)
def test_testpackage::firstclass_instantiation(instance):
    assert isinstance(instance, testPackage::FirstClass)

@given(instance=SecondClass_strategy)
@settings(max_examples=50)
def test_secondclass_instantiation(instance):
    assert isinstance(instance, SecondClass)

@given(instance=testPackage::SecondSubClass_strategy)
@settings(max_examples=50)
def test_testpackage::secondsubclass_instantiation(instance):
    assert isinstance(instance, testPackage::SecondSubClass)

@given(instance=FirstClass_strategy)
@settings(max_examples=50)
def test_firstclass_instantiation(instance):
    assert isinstance(instance, FirstClass)

@given(instance=testPackage::FirstSubClass_strategy)
@settings(max_examples=50)
def test_testpackage::firstsubclass_instantiation(instance):
    assert isinstance(instance, testPackage::FirstSubClass)
