import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    testPackage::Class1,
    testPackage::HubClass,
    testPackage::Class5,
    testPackage::Class4,
    testPackage::Class3,
    testPackage::Class2,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testpackage::class1_is_not_abstract():
    assert not inspect.isabstract(testPackage::Class1)


def test_testpackage::class1_constructor_exists():
    assert callable(testPackage::Class1.__init__)


def test_testpackage::class1_constructor_args():
    sig = inspect.signature(testPackage::Class1.__init__)
    params = list(sig.parameters.keys())



def test_testpackage::hubclass_is_not_abstract():
    assert not inspect.isabstract(testPackage::HubClass)


def test_testpackage::hubclass_constructor_exists():
    assert callable(testPackage::HubClass.__init__)


def test_testpackage::hubclass_constructor_args():
    sig = inspect.signature(testPackage::HubClass.__init__)
    params = list(sig.parameters.keys())



def test_testpackage::class5_is_not_abstract():
    assert not inspect.isabstract(testPackage::Class5)


def test_testpackage::class5_constructor_exists():
    assert callable(testPackage::Class5.__init__)


def test_testpackage::class5_constructor_args():
    sig = inspect.signature(testPackage::Class5.__init__)
    params = list(sig.parameters.keys())



def test_testpackage::class4_is_not_abstract():
    assert not inspect.isabstract(testPackage::Class4)


def test_testpackage::class4_constructor_exists():
    assert callable(testPackage::Class4.__init__)


def test_testpackage::class4_constructor_args():
    sig = inspect.signature(testPackage::Class4.__init__)
    params = list(sig.parameters.keys())



def test_testpackage::class3_is_not_abstract():
    assert not inspect.isabstract(testPackage::Class3)


def test_testpackage::class3_constructor_exists():
    assert callable(testPackage::Class3.__init__)


def test_testpackage::class3_constructor_args():
    sig = inspect.signature(testPackage::Class3.__init__)
    params = list(sig.parameters.keys())



def test_testpackage::class2_is_not_abstract():
    assert not inspect.isabstract(testPackage::Class2)


def test_testpackage::class2_constructor_exists():
    assert callable(testPackage::Class2.__init__)


def test_testpackage::class2_constructor_args():
    sig = inspect.signature(testPackage::Class2.__init__)
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
testPackage::Class1_strategy = st.builds(
    testPackage::Class1,
)
testPackage::HubClass_strategy = st.builds(
    testPackage::HubClass,
)
testPackage::Class5_strategy = st.builds(
    testPackage::Class5,
)
testPackage::Class4_strategy = st.builds(
    testPackage::Class4,
)
testPackage::Class3_strategy = st.builds(
    testPackage::Class3,
)
testPackage::Class2_strategy = st.builds(
    testPackage::Class2,
)

@given(instance=testPackage::Class1_strategy)
@settings(max_examples=50)
def test_testpackage::class1_instantiation(instance):
    assert isinstance(instance, testPackage::Class1)

@given(instance=testPackage::HubClass_strategy)
@settings(max_examples=50)
def test_testpackage::hubclass_instantiation(instance):
    assert isinstance(instance, testPackage::HubClass)

@given(instance=testPackage::Class5_strategy)
@settings(max_examples=50)
def test_testpackage::class5_instantiation(instance):
    assert isinstance(instance, testPackage::Class5)

@given(instance=testPackage::Class4_strategy)
@settings(max_examples=50)
def test_testpackage::class4_instantiation(instance):
    assert isinstance(instance, testPackage::Class4)

@given(instance=testPackage::Class3_strategy)
@settings(max_examples=50)
def test_testpackage::class3_instantiation(instance):
    assert isinstance(instance, testPackage::Class3)

@given(instance=testPackage::Class2_strategy)
@settings(max_examples=50)
def test_testpackage::class2_instantiation(instance):
    assert isinstance(instance, testPackage::Class2)
