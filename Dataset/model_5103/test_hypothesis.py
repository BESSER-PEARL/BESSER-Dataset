import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    testPackage_Class1,
    testPackage_HubClass,
    testPackage_Class5,
    testPackage_Class4,
    testPackage_Class3,
    testPackage_Class2,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testpackage_class1_is_not_abstract():
    assert not inspect.isabstract(testPackage_Class1)


def test_testpackage_class1_constructor_exists():
    assert callable(testPackage_Class1.__init__)


def test_testpackage_class1_constructor_args():
    sig = inspect.signature(testPackage_Class1.__init__)
    params = list(sig.parameters.keys())



def test_testpackage_hubclass_is_not_abstract():
    assert not inspect.isabstract(testPackage_HubClass)


def test_testpackage_hubclass_constructor_exists():
    assert callable(testPackage_HubClass.__init__)


def test_testpackage_hubclass_constructor_args():
    sig = inspect.signature(testPackage_HubClass.__init__)
    params = list(sig.parameters.keys())



def test_testpackage_class5_is_not_abstract():
    assert not inspect.isabstract(testPackage_Class5)


def test_testpackage_class5_constructor_exists():
    assert callable(testPackage_Class5.__init__)


def test_testpackage_class5_constructor_args():
    sig = inspect.signature(testPackage_Class5.__init__)
    params = list(sig.parameters.keys())



def test_testpackage_class4_is_not_abstract():
    assert not inspect.isabstract(testPackage_Class4)


def test_testpackage_class4_constructor_exists():
    assert callable(testPackage_Class4.__init__)


def test_testpackage_class4_constructor_args():
    sig = inspect.signature(testPackage_Class4.__init__)
    params = list(sig.parameters.keys())



def test_testpackage_class3_is_not_abstract():
    assert not inspect.isabstract(testPackage_Class3)


def test_testpackage_class3_constructor_exists():
    assert callable(testPackage_Class3.__init__)


def test_testpackage_class3_constructor_args():
    sig = inspect.signature(testPackage_Class3.__init__)
    params = list(sig.parameters.keys())



def test_testpackage_class2_is_not_abstract():
    assert not inspect.isabstract(testPackage_Class2)


def test_testpackage_class2_constructor_exists():
    assert callable(testPackage_Class2.__init__)


def test_testpackage_class2_constructor_args():
    sig = inspect.signature(testPackage_Class2.__init__)
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
testPackage_Class1_strategy = st.builds(
    testPackage_Class1,
)
testPackage_HubClass_strategy = st.builds(
    testPackage_HubClass,
)
testPackage_Class5_strategy = st.builds(
    testPackage_Class5,
)
testPackage_Class4_strategy = st.builds(
    testPackage_Class4,
)
testPackage_Class3_strategy = st.builds(
    testPackage_Class3,
)
testPackage_Class2_strategy = st.builds(
    testPackage_Class2,
)

@given(instance=testPackage_Class1_strategy)
@settings(max_examples=50)
def test_testpackage_class1_instantiation(instance):
    assert isinstance(instance, testPackage_Class1)

@given(instance=testPackage_HubClass_strategy)
@settings(max_examples=50)
def test_testpackage_hubclass_instantiation(instance):
    assert isinstance(instance, testPackage_HubClass)

@given(instance=testPackage_Class5_strategy)
@settings(max_examples=50)
def test_testpackage_class5_instantiation(instance):
    assert isinstance(instance, testPackage_Class5)

@given(instance=testPackage_Class4_strategy)
@settings(max_examples=50)
def test_testpackage_class4_instantiation(instance):
    assert isinstance(instance, testPackage_Class4)

@given(instance=testPackage_Class3_strategy)
@settings(max_examples=50)
def test_testpackage_class3_instantiation(instance):
    assert isinstance(instance, testPackage_Class3)

@given(instance=testPackage_Class2_strategy)
@settings(max_examples=50)
def test_testpackage_class2_instantiation(instance):
    assert isinstance(instance, testPackage_Class2)
