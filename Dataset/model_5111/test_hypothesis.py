import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    SubType,
    SuperType,
    testPackage::SubType,
    testPackage::SubSubType,
    testPackage::SuperType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_subtype_is_not_abstract():
    assert not inspect.isabstract(SubType)


def test_subtype_constructor_exists():
    assert callable(SubType.__init__)


def test_subtype_constructor_args():
    sig = inspect.signature(SubType.__init__)
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



def test_testpackage::subsubtype_is_not_abstract():
    assert not inspect.isabstract(testPackage::SubSubType)


def test_testpackage::subsubtype_constructor_exists():
    assert callable(testPackage::SubSubType.__init__)


def test_testpackage::subsubtype_constructor_args():
    sig = inspect.signature(testPackage::SubSubType.__init__)
    params = list(sig.parameters.keys())



def test_testpackage::supertype_is_not_abstract():
    assert not inspect.isabstract(testPackage::SuperType)


def test_testpackage::supertype_constructor_exists():
    assert callable(testPackage::SuperType.__init__)


def test_testpackage::supertype_constructor_args():
    sig = inspect.signature(testPackage::SuperType.__init__)
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
SubType_strategy = st.builds(
    SubType,
)
SuperType_strategy = st.builds(
    SuperType,
)
testPackage::SubType_strategy = st.builds(
    testPackage::SubType,
)
testPackage::SubSubType_strategy = st.builds(
    testPackage::SubSubType,
)
testPackage::SuperType_strategy = st.builds(
    testPackage::SuperType,
)

@given(instance=SubType_strategy)
@settings(max_examples=50)
def test_subtype_instantiation(instance):
    assert isinstance(instance, SubType)

@given(instance=SuperType_strategy)
@settings(max_examples=50)
def test_supertype_instantiation(instance):
    assert isinstance(instance, SuperType)

@given(instance=testPackage::SubType_strategy)
@settings(max_examples=50)
def test_testpackage::subtype_instantiation(instance):
    assert isinstance(instance, testPackage::SubType)

@given(instance=testPackage::SubSubType_strategy)
@settings(max_examples=50)
def test_testpackage::subsubtype_instantiation(instance):
    assert isinstance(instance, testPackage::SubSubType)

@given(instance=testPackage::SuperType_strategy)
@settings(max_examples=50)
def test_testpackage::supertype_instantiation(instance):
    assert isinstance(instance, testPackage::SuperType)
