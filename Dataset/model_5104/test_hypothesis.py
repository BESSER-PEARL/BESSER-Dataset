import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    testPackage_SuperType,
    testPackage_AnotherType2,
    SuperType,
    testPackage_SubType,
    testPackage_AnotherType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testpackage_supertype_is_not_abstract():
    assert not inspect.isabstract(testPackage_SuperType)


def test_testpackage_supertype_constructor_exists():
    assert callable(testPackage_SuperType.__init__)


def test_testpackage_supertype_constructor_args():
    sig = inspect.signature(testPackage_SuperType.__init__)
    params = list(sig.parameters.keys())



def test_testpackage_anothertype2_is_not_abstract():
    assert not inspect.isabstract(testPackage_AnotherType2)


def test_testpackage_anothertype2_constructor_exists():
    assert callable(testPackage_AnotherType2.__init__)


def test_testpackage_anothertype2_constructor_args():
    sig = inspect.signature(testPackage_AnotherType2.__init__)
    params = list(sig.parameters.keys())



def test_supertype_is_not_abstract():
    assert not inspect.isabstract(SuperType)


def test_supertype_constructor_exists():
    assert callable(SuperType.__init__)


def test_supertype_constructor_args():
    sig = inspect.signature(SuperType.__init__)
    params = list(sig.parameters.keys())



def test_testpackage_subtype_is_not_abstract():
    assert not inspect.isabstract(testPackage_SubType)


def test_testpackage_subtype_constructor_exists():
    assert callable(testPackage_SubType.__init__)


def test_testpackage_subtype_constructor_args():
    sig = inspect.signature(testPackage_SubType.__init__)
    params = list(sig.parameters.keys())



def test_testpackage_anothertype_is_not_abstract():
    assert not inspect.isabstract(testPackage_AnotherType)


def test_testpackage_anothertype_constructor_exists():
    assert callable(testPackage_AnotherType.__init__)


def test_testpackage_anothertype_constructor_args():
    sig = inspect.signature(testPackage_AnotherType.__init__)
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
testPackage_SuperType_strategy = st.builds(
    testPackage_SuperType,
)
testPackage_AnotherType2_strategy = st.builds(
    testPackage_AnotherType2,
)
SuperType_strategy = st.builds(
    SuperType,
)
testPackage_SubType_strategy = st.builds(
    testPackage_SubType,
)
testPackage_AnotherType_strategy = st.builds(
    testPackage_AnotherType,
)

@given(instance=testPackage_SuperType_strategy)
@settings(max_examples=50)
def test_testpackage_supertype_instantiation(instance):
    assert isinstance(instance, testPackage_SuperType)

@given(instance=testPackage_AnotherType2_strategy)
@settings(max_examples=50)
def test_testpackage_anothertype2_instantiation(instance):
    assert isinstance(instance, testPackage_AnotherType2)

@given(instance=SuperType_strategy)
@settings(max_examples=50)
def test_supertype_instantiation(instance):
    assert isinstance(instance, SuperType)

@given(instance=testPackage_SubType_strategy)
@settings(max_examples=50)
def test_testpackage_subtype_instantiation(instance):
    assert isinstance(instance, testPackage_SubType)

@given(instance=testPackage_AnotherType_strategy)
@settings(max_examples=50)
def test_testpackage_anothertype_instantiation(instance):
    assert isinstance(instance, testPackage_AnotherType)
