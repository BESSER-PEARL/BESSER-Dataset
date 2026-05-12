import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    testPackage_SecondClass,
    testPackage_FirstClass,
    SecondClass,
    testPackage_SecondSubClass,
    FirstClass,
    testPackage_FirstSubClass,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testpackage_secondclass_is_not_abstract():
    assert not inspect.isabstract(testPackage_SecondClass)


def test_testpackage_secondclass_constructor_exists():
    assert callable(testPackage_SecondClass.__init__)


def test_testpackage_secondclass_constructor_args():
    sig = inspect.signature(testPackage_SecondClass.__init__)
    params = list(sig.parameters.keys())



def test_testpackage_firstclass_is_not_abstract():
    assert not inspect.isabstract(testPackage_FirstClass)


def test_testpackage_firstclass_constructor_exists():
    assert callable(testPackage_FirstClass.__init__)


def test_testpackage_firstclass_constructor_args():
    sig = inspect.signature(testPackage_FirstClass.__init__)
    params = list(sig.parameters.keys())



def test_secondclass_is_not_abstract():
    assert not inspect.isabstract(SecondClass)


def test_secondclass_constructor_exists():
    assert callable(SecondClass.__init__)


def test_secondclass_constructor_args():
    sig = inspect.signature(SecondClass.__init__)
    params = list(sig.parameters.keys())



def test_testpackage_secondsubclass_is_not_abstract():
    assert not inspect.isabstract(testPackage_SecondSubClass)


def test_testpackage_secondsubclass_constructor_exists():
    assert callable(testPackage_SecondSubClass.__init__)


def test_testpackage_secondsubclass_constructor_args():
    sig = inspect.signature(testPackage_SecondSubClass.__init__)
    params = list(sig.parameters.keys())



def test_firstclass_is_not_abstract():
    assert not inspect.isabstract(FirstClass)


def test_firstclass_constructor_exists():
    assert callable(FirstClass.__init__)


def test_firstclass_constructor_args():
    sig = inspect.signature(FirstClass.__init__)
    params = list(sig.parameters.keys())



def test_testpackage_firstsubclass_is_not_abstract():
    assert not inspect.isabstract(testPackage_FirstSubClass)


def test_testpackage_firstsubclass_constructor_exists():
    assert callable(testPackage_FirstSubClass.__init__)


def test_testpackage_firstsubclass_constructor_args():
    sig = inspect.signature(testPackage_FirstSubClass.__init__)
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
testPackage_SecondClass_strategy = st.builds(
    testPackage_SecondClass,
)
testPackage_FirstClass_strategy = st.builds(
    testPackage_FirstClass,
)
SecondClass_strategy = st.builds(
    SecondClass,
)
testPackage_SecondSubClass_strategy = st.builds(
    testPackage_SecondSubClass,
)
FirstClass_strategy = st.builds(
    FirstClass,
)
testPackage_FirstSubClass_strategy = st.builds(
    testPackage_FirstSubClass,
)

@given(instance=testPackage_SecondClass_strategy)
@settings(max_examples=50)
def test_testpackage_secondclass_instantiation(instance):
    assert isinstance(instance, testPackage_SecondClass)

@given(instance=testPackage_FirstClass_strategy)
@settings(max_examples=50)
def test_testpackage_firstclass_instantiation(instance):
    assert isinstance(instance, testPackage_FirstClass)

@given(instance=SecondClass_strategy)
@settings(max_examples=50)
def test_secondclass_instantiation(instance):
    assert isinstance(instance, SecondClass)

@given(instance=testPackage_SecondSubClass_strategy)
@settings(max_examples=50)
def test_testpackage_secondsubclass_instantiation(instance):
    assert isinstance(instance, testPackage_SecondSubClass)

@given(instance=FirstClass_strategy)
@settings(max_examples=50)
def test_firstclass_instantiation(instance):
    assert isinstance(instance, FirstClass)

@given(instance=testPackage_FirstSubClass_strategy)
@settings(max_examples=50)
def test_testpackage_firstsubclass_instantiation(instance):
    assert isinstance(instance, testPackage_FirstSubClass)
