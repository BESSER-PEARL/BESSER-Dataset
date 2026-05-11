import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    test::containmentwalker::dependency::subpackage::ClassInOtherPackage,
    test::containmentwalker::dependency::IsolatedClassInReachablePackage,
    ClassInOtherPackage,
    test::containmentwalker::dependency::Foo,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test::containmentwalker::dependency::subpackage::classinotherpackage_is_not_abstract():
    assert not inspect.isabstract(test::containmentwalker::dependency::subpackage::ClassInOtherPackage)


def test_test::containmentwalker::dependency::subpackage::classinotherpackage_constructor_exists():
    assert callable(test::containmentwalker::dependency::subpackage::ClassInOtherPackage.__init__)


def test_test::containmentwalker::dependency::subpackage::classinotherpackage_constructor_args():
    sig = inspect.signature(test::containmentwalker::dependency::subpackage::ClassInOtherPackage.__init__)
    params = list(sig.parameters.keys())



def test_test::containmentwalker::dependency::isolatedclassinreachablepackage_is_not_abstract():
    assert not inspect.isabstract(test::containmentwalker::dependency::IsolatedClassInReachablePackage)


def test_test::containmentwalker::dependency::isolatedclassinreachablepackage_constructor_exists():
    assert callable(test::containmentwalker::dependency::IsolatedClassInReachablePackage.__init__)


def test_test::containmentwalker::dependency::isolatedclassinreachablepackage_constructor_args():
    sig = inspect.signature(test::containmentwalker::dependency::IsolatedClassInReachablePackage.__init__)
    params = list(sig.parameters.keys())



def test_classinotherpackage_is_not_abstract():
    assert not inspect.isabstract(ClassInOtherPackage)


def test_classinotherpackage_constructor_exists():
    assert callable(ClassInOtherPackage.__init__)


def test_classinotherpackage_constructor_args():
    sig = inspect.signature(ClassInOtherPackage.__init__)
    params = list(sig.parameters.keys())



def test_test::containmentwalker::dependency::foo_is_not_abstract():
    assert not inspect.isabstract(test::containmentwalker::dependency::Foo)


def test_test::containmentwalker::dependency::foo_constructor_exists():
    assert callable(test::containmentwalker::dependency::Foo.__init__)


def test_test::containmentwalker::dependency::foo_constructor_args():
    sig = inspect.signature(test::containmentwalker::dependency::Foo.__init__)
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
test::containmentwalker::dependency::subpackage::ClassInOtherPackage_strategy = st.builds(
    test::containmentwalker::dependency::subpackage::ClassInOtherPackage,
)
test::containmentwalker::dependency::IsolatedClassInReachablePackage_strategy = st.builds(
    test::containmentwalker::dependency::IsolatedClassInReachablePackage,
)
ClassInOtherPackage_strategy = st.builds(
    ClassInOtherPackage,
)
test::containmentwalker::dependency::Foo_strategy = st.builds(
    test::containmentwalker::dependency::Foo,
)

@given(instance=test::containmentwalker::dependency::subpackage::ClassInOtherPackage_strategy)
@settings(max_examples=50)
def test_test::containmentwalker::dependency::subpackage::classinotherpackage_instantiation(instance):
    assert isinstance(instance, test::containmentwalker::dependency::subpackage::ClassInOtherPackage)

@given(instance=test::containmentwalker::dependency::IsolatedClassInReachablePackage_strategy)
@settings(max_examples=50)
def test_test::containmentwalker::dependency::isolatedclassinreachablepackage_instantiation(instance):
    assert isinstance(instance, test::containmentwalker::dependency::IsolatedClassInReachablePackage)

@given(instance=ClassInOtherPackage_strategy)
@settings(max_examples=50)
def test_classinotherpackage_instantiation(instance):
    assert isinstance(instance, ClassInOtherPackage)

@given(instance=test::containmentwalker::dependency::Foo_strategy)
@settings(max_examples=50)
def test_test::containmentwalker::dependency::foo_instantiation(instance):
    assert isinstance(instance, test::containmentwalker::dependency::Foo)
