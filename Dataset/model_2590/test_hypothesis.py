import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    testSubpackages1::root::testSubpackages1::subpackage2::class3,
    testSubpackages1::root::testSubpackages1::subpackage3::class4,
    testSubpackages1::root::testSubpackages1::subpackage1::class2,
    class3,
    testSubpackages1::root::class1,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testsubpackages1::root::testsubpackages1::subpackage2::class3_is_not_abstract():
    assert not inspect.isabstract(testSubpackages1::root::testSubpackages1::subpackage2::class3)


def test_testsubpackages1::root::testsubpackages1::subpackage2::class3_constructor_exists():
    assert callable(testSubpackages1::root::testSubpackages1::subpackage2::class3.__init__)


def test_testsubpackages1::root::testsubpackages1::subpackage2::class3_constructor_args():
    sig = inspect.signature(testSubpackages1::root::testSubpackages1::subpackage2::class3.__init__)
    params = list(sig.parameters.keys())



def test_testsubpackages1::root::testsubpackages1::subpackage3::class4_is_not_abstract():
    assert not inspect.isabstract(testSubpackages1::root::testSubpackages1::subpackage3::class4)


def test_testsubpackages1::root::testsubpackages1::subpackage3::class4_constructor_exists():
    assert callable(testSubpackages1::root::testSubpackages1::subpackage3::class4.__init__)


def test_testsubpackages1::root::testsubpackages1::subpackage3::class4_constructor_args():
    sig = inspect.signature(testSubpackages1::root::testSubpackages1::subpackage3::class4.__init__)
    params = list(sig.parameters.keys())



def test_testsubpackages1::root::testsubpackages1::subpackage1::class2_is_not_abstract():
    assert not inspect.isabstract(testSubpackages1::root::testSubpackages1::subpackage1::class2)


def test_testsubpackages1::root::testsubpackages1::subpackage1::class2_constructor_exists():
    assert callable(testSubpackages1::root::testSubpackages1::subpackage1::class2.__init__)


def test_testsubpackages1::root::testsubpackages1::subpackage1::class2_constructor_args():
    sig = inspect.signature(testSubpackages1::root::testSubpackages1::subpackage1::class2.__init__)
    params = list(sig.parameters.keys())



def test_class3_is_not_abstract():
    assert not inspect.isabstract(class3)


def test_class3_constructor_exists():
    assert callable(class3.__init__)


def test_class3_constructor_args():
    sig = inspect.signature(class3.__init__)
    params = list(sig.parameters.keys())



def test_testsubpackages1::root::class1_is_not_abstract():
    assert not inspect.isabstract(testSubpackages1::root::class1)


def test_testsubpackages1::root::class1_constructor_exists():
    assert callable(testSubpackages1::root::class1.__init__)


def test_testsubpackages1::root::class1_constructor_args():
    sig = inspect.signature(testSubpackages1::root::class1.__init__)
    params = list(sig.parameters.keys())
    assert "a" in params, "Missing parameter 'a'"

def test_testsubpackages1::root::class1_has_a():
    assert hasattr(testSubpackages1::root::class1, "a")
    descriptor = None
    for klass in testSubpackages1::root::class1.__mro__:
        if "a" in klass.__dict__:
            descriptor = klass.__dict__["a"]
            break
    assert isinstance(descriptor, property)


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
testSubpackages1::root::testSubpackages1::subpackage2::class3_strategy = st.builds(
    testSubpackages1::root::testSubpackages1::subpackage2::class3,
)
testSubpackages1::root::testSubpackages1::subpackage3::class4_strategy = st.builds(
    testSubpackages1::root::testSubpackages1::subpackage3::class4,
)
testSubpackages1::root::testSubpackages1::subpackage1::class2_strategy = st.builds(
    testSubpackages1::root::testSubpackages1::subpackage1::class2,
)
class3_strategy = st.builds(
    class3,
)
testSubpackages1::root::class1_strategy = st.builds(
    testSubpackages1::root::class1,
    a=
        st.dates()
)

@given(instance=testSubpackages1::root::testSubpackages1::subpackage2::class3_strategy)
@settings(max_examples=50)
def test_testsubpackages1::root::testsubpackages1::subpackage2::class3_instantiation(instance):
    assert isinstance(instance, testSubpackages1::root::testSubpackages1::subpackage2::class3)

@given(instance=testSubpackages1::root::testSubpackages1::subpackage3::class4_strategy)
@settings(max_examples=50)
def test_testsubpackages1::root::testsubpackages1::subpackage3::class4_instantiation(instance):
    assert isinstance(instance, testSubpackages1::root::testSubpackages1::subpackage3::class4)

@given(instance=testSubpackages1::root::testSubpackages1::subpackage1::class2_strategy)
@settings(max_examples=50)
def test_testsubpackages1::root::testsubpackages1::subpackage1::class2_instantiation(instance):
    assert isinstance(instance, testSubpackages1::root::testSubpackages1::subpackage1::class2)

@given(instance=class3_strategy)
@settings(max_examples=50)
def test_class3_instantiation(instance):
    assert isinstance(instance, class3)

@given(instance=testSubpackages1::root::class1_strategy)
@settings(max_examples=50)
def test_testsubpackages1::root::class1_instantiation(instance):
    assert isinstance(instance, testSubpackages1::root::class1)

@given(instance=testSubpackages1::root::class1_strategy)
def test_testsubpackages1::root::class1_a_type(instance):
    assert isinstance(instance.a, date)


@given(instance=testSubpackages1::root::class1_strategy)
def test_testsubpackages1::root::class1_a_setter(instance):
    original = instance.a
    instance.a = original
    assert instance.a == original
