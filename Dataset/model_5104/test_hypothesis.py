import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    testPackage::SuperType,
    testPackage::AnotherType2,
    SuperType,
    testPackage::SubType,
    testPackage::AnotherType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testpackage::supertype_is_not_abstract():
    assert not inspect.isabstract(testPackage::SuperType)


def test_testpackage::supertype_constructor_exists():
    assert callable(testPackage::SuperType.__init__)


def test_testpackage::supertype_constructor_args():
    sig = inspect.signature(testPackage::SuperType.__init__)
    params = list(sig.parameters.keys())



def test_testpackage::anothertype2_is_not_abstract():
    assert not inspect.isabstract(testPackage::AnotherType2)


def test_testpackage::anothertype2_constructor_exists():
    assert callable(testPackage::AnotherType2.__init__)


def test_testpackage::anothertype2_constructor_args():
    sig = inspect.signature(testPackage::AnotherType2.__init__)
    params = list(sig.parameters.keys())



def test_supertype_is_not_abstract():
    assert not inspect.isabstract(SuperType)


def test_supertype_constructor_exists():
    assert callable(SuperType.__init__)


def test_supertype_constructor_args():
    sig = inspect.signature(SuperType.__init__)
    params = list(sig.parameters.keys())



def test_testpackage::subtype_is_not_abstract():
    assert not inspect.isabstract(testPackage::SubType)


def test_testpackage::subtype_constructor_exists():
    assert callable(testPackage::SubType.__init__)


def test_testpackage::subtype_constructor_args():
    sig = inspect.signature(testPackage::SubType.__init__)
    params = list(sig.parameters.keys())



def test_testpackage::anothertype_is_not_abstract():
    assert not inspect.isabstract(testPackage::AnotherType)


def test_testpackage::anothertype_constructor_exists():
    assert callable(testPackage::AnotherType.__init__)


def test_testpackage::anothertype_constructor_args():
    sig = inspect.signature(testPackage::AnotherType.__init__)
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
testPackage::SuperType_strategy = st.builds(
    testPackage::SuperType,
)
testPackage::AnotherType2_strategy = st.builds(
    testPackage::AnotherType2,
)
SuperType_strategy = st.builds(
    SuperType,
)
testPackage::SubType_strategy = st.builds(
    testPackage::SubType,
)
testPackage::AnotherType_strategy = st.builds(
    testPackage::AnotherType,
)

@given(instance=testPackage::SuperType_strategy)
@settings(max_examples=50)
def test_testpackage::supertype_instantiation(instance):
    assert isinstance(instance, testPackage::SuperType)

@given(instance=testPackage::AnotherType2_strategy)
@settings(max_examples=50)
def test_testpackage::anothertype2_instantiation(instance):
    assert isinstance(instance, testPackage::AnotherType2)

@given(instance=SuperType_strategy)
@settings(max_examples=50)
def test_supertype_instantiation(instance):
    assert isinstance(instance, SuperType)

@given(instance=testPackage::SubType_strategy)
@settings(max_examples=50)
def test_testpackage::subtype_instantiation(instance):
    assert isinstance(instance, testPackage::SubType)

@given(instance=testPackage::AnotherType_strategy)
@settings(max_examples=50)
def test_testpackage::anothertype_instantiation(instance):
    assert isinstance(instance, testPackage::AnotherType)
