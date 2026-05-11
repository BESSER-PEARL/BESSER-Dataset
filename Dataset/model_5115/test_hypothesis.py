import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    SuperClass,
    SuperSuperClass,
    testPackage::DerivedClass,
    testPackage::SuperClass,
    testPackage::SuperSuperClass,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_superclass_is_not_abstract():
    assert not inspect.isabstract(SuperClass)


def test_superclass_constructor_exists():
    assert callable(SuperClass.__init__)


def test_superclass_constructor_args():
    sig = inspect.signature(SuperClass.__init__)
    params = list(sig.parameters.keys())



def test_supersuperclass_is_not_abstract():
    assert not inspect.isabstract(SuperSuperClass)


def test_supersuperclass_constructor_exists():
    assert callable(SuperSuperClass.__init__)


def test_supersuperclass_constructor_args():
    sig = inspect.signature(SuperSuperClass.__init__)
    params = list(sig.parameters.keys())



def test_testpackage::derivedclass_is_not_abstract():
    assert not inspect.isabstract(testPackage::DerivedClass)


def test_testpackage::derivedclass_constructor_exists():
    assert callable(testPackage::DerivedClass.__init__)


def test_testpackage::derivedclass_constructor_args():
    sig = inspect.signature(testPackage::DerivedClass.__init__)
    params = list(sig.parameters.keys())



def test_testpackage::superclass_is_not_abstract():
    assert not inspect.isabstract(testPackage::SuperClass)


def test_testpackage::superclass_constructor_exists():
    assert callable(testPackage::SuperClass.__init__)


def test_testpackage::superclass_constructor_args():
    sig = inspect.signature(testPackage::SuperClass.__init__)
    params = list(sig.parameters.keys())



def test_testpackage::supersuperclass_is_not_abstract():
    assert not inspect.isabstract(testPackage::SuperSuperClass)


def test_testpackage::supersuperclass_constructor_exists():
    assert callable(testPackage::SuperSuperClass.__init__)


def test_testpackage::supersuperclass_constructor_args():
    sig = inspect.signature(testPackage::SuperSuperClass.__init__)
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
SuperClass_strategy = st.builds(
    SuperClass,
)
SuperSuperClass_strategy = st.builds(
    SuperSuperClass,
)
testPackage::DerivedClass_strategy = st.builds(
    testPackage::DerivedClass,
)
testPackage::SuperClass_strategy = st.builds(
    testPackage::SuperClass,
)
testPackage::SuperSuperClass_strategy = st.builds(
    testPackage::SuperSuperClass,
)

@given(instance=SuperClass_strategy)
@settings(max_examples=50)
def test_superclass_instantiation(instance):
    assert isinstance(instance, SuperClass)

@given(instance=SuperSuperClass_strategy)
@settings(max_examples=50)
def test_supersuperclass_instantiation(instance):
    assert isinstance(instance, SuperSuperClass)

@given(instance=testPackage::DerivedClass_strategy)
@settings(max_examples=50)
def test_testpackage::derivedclass_instantiation(instance):
    assert isinstance(instance, testPackage::DerivedClass)

@given(instance=testPackage::SuperClass_strategy)
@settings(max_examples=50)
def test_testpackage::superclass_instantiation(instance):
    assert isinstance(instance, testPackage::SuperClass)

@given(instance=testPackage::SuperSuperClass_strategy)
@settings(max_examples=50)
def test_testpackage::supersuperclass_instantiation(instance):
    assert isinstance(instance, testPackage::SuperSuperClass)
