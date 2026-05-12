import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    SuperClass,
    SuperSuperClass,
    testPackage_DerivedClass,
    testPackage_SuperClass,
    testPackage_SuperSuperClass,
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



def test_testpackage_derivedclass_is_not_abstract():
    assert not inspect.isabstract(testPackage_DerivedClass)


def test_testpackage_derivedclass_constructor_exists():
    assert callable(testPackage_DerivedClass.__init__)


def test_testpackage_derivedclass_constructor_args():
    sig = inspect.signature(testPackage_DerivedClass.__init__)
    params = list(sig.parameters.keys())



def test_testpackage_superclass_is_not_abstract():
    assert not inspect.isabstract(testPackage_SuperClass)


def test_testpackage_superclass_constructor_exists():
    assert callable(testPackage_SuperClass.__init__)


def test_testpackage_superclass_constructor_args():
    sig = inspect.signature(testPackage_SuperClass.__init__)
    params = list(sig.parameters.keys())



def test_testpackage_supersuperclass_is_not_abstract():
    assert not inspect.isabstract(testPackage_SuperSuperClass)


def test_testpackage_supersuperclass_constructor_exists():
    assert callable(testPackage_SuperSuperClass.__init__)


def test_testpackage_supersuperclass_constructor_args():
    sig = inspect.signature(testPackage_SuperSuperClass.__init__)
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
testPackage_DerivedClass_strategy = st.builds(
    testPackage_DerivedClass,
)
testPackage_SuperClass_strategy = st.builds(
    testPackage_SuperClass,
)
testPackage_SuperSuperClass_strategy = st.builds(
    testPackage_SuperSuperClass,
)

@given(instance=SuperClass_strategy)
@settings(max_examples=50)
def test_superclass_instantiation(instance):
    assert isinstance(instance, SuperClass)

@given(instance=SuperSuperClass_strategy)
@settings(max_examples=50)
def test_supersuperclass_instantiation(instance):
    assert isinstance(instance, SuperSuperClass)

@given(instance=testPackage_DerivedClass_strategy)
@settings(max_examples=50)
def test_testpackage_derivedclass_instantiation(instance):
    assert isinstance(instance, testPackage_DerivedClass)

@given(instance=testPackage_SuperClass_strategy)
@settings(max_examples=50)
def test_testpackage_superclass_instantiation(instance):
    assert isinstance(instance, testPackage_SuperClass)

@given(instance=testPackage_SuperSuperClass_strategy)
@settings(max_examples=50)
def test_testpackage_supersuperclass_instantiation(instance):
    assert isinstance(instance, testPackage_SuperSuperClass)
