import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    SubType,
    SuperType,
    testPackage_SubType,
    testPackage_SubSubType,
    testPackage_SuperType,
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



def test_testpackage_subtype_is_not_abstract():
    assert not inspect.isabstract(testPackage_SubType)


def test_testpackage_subtype_constructor_exists():
    assert callable(testPackage_SubType.__init__)


def test_testpackage_subtype_constructor_args():
    sig = inspect.signature(testPackage_SubType.__init__)
    params = list(sig.parameters.keys())



def test_testpackage_subsubtype_is_not_abstract():
    assert not inspect.isabstract(testPackage_SubSubType)


def test_testpackage_subsubtype_constructor_exists():
    assert callable(testPackage_SubSubType.__init__)


def test_testpackage_subsubtype_constructor_args():
    sig = inspect.signature(testPackage_SubSubType.__init__)
    params = list(sig.parameters.keys())



def test_testpackage_supertype_is_not_abstract():
    assert not inspect.isabstract(testPackage_SuperType)


def test_testpackage_supertype_constructor_exists():
    assert callable(testPackage_SuperType.__init__)


def test_testpackage_supertype_constructor_args():
    sig = inspect.signature(testPackage_SuperType.__init__)
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
testPackage_SubType_strategy = st.builds(
    testPackage_SubType,
)
testPackage_SubSubType_strategy = st.builds(
    testPackage_SubSubType,
)
testPackage_SuperType_strategy = st.builds(
    testPackage_SuperType,
)

@given(instance=SubType_strategy)
@settings(max_examples=50)
def test_subtype_instantiation(instance):
    assert isinstance(instance, SubType)

@given(instance=SuperType_strategy)
@settings(max_examples=50)
def test_supertype_instantiation(instance):
    assert isinstance(instance, SuperType)

@given(instance=testPackage_SubType_strategy)
@settings(max_examples=50)
def test_testpackage_subtype_instantiation(instance):
    assert isinstance(instance, testPackage_SubType)

@given(instance=testPackage_SubSubType_strategy)
@settings(max_examples=50)
def test_testpackage_subsubtype_instantiation(instance):
    assert isinstance(instance, testPackage_SubSubType)

@given(instance=testPackage_SuperType_strategy)
@settings(max_examples=50)
def test_testpackage_supertype_instantiation(instance):
    assert isinstance(instance, testPackage_SuperType)
