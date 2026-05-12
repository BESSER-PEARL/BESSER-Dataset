import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    test_containmentwalker_dependency_subpackage_ClassInOtherPackage,
    test_containmentwalker_dependency_IsolatedClassInReachablePackage,
    ClassInOtherPackage,
    test_containmentwalker_dependency_Foo,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test_containmentwalker_dependency_subpackage_classinotherpackage_is_not_abstract():
    assert not inspect.isabstract(test_containmentwalker_dependency_subpackage_ClassInOtherPackage)


def test_test_containmentwalker_dependency_subpackage_classinotherpackage_constructor_exists():
    assert callable(test_containmentwalker_dependency_subpackage_ClassInOtherPackage.__init__)


def test_test_containmentwalker_dependency_subpackage_classinotherpackage_constructor_args():
    sig = inspect.signature(test_containmentwalker_dependency_subpackage_ClassInOtherPackage.__init__)
    params = list(sig.parameters.keys())



def test_test_containmentwalker_dependency_isolatedclassinreachablepackage_is_not_abstract():
    assert not inspect.isabstract(test_containmentwalker_dependency_IsolatedClassInReachablePackage)


def test_test_containmentwalker_dependency_isolatedclassinreachablepackage_constructor_exists():
    assert callable(test_containmentwalker_dependency_IsolatedClassInReachablePackage.__init__)


def test_test_containmentwalker_dependency_isolatedclassinreachablepackage_constructor_args():
    sig = inspect.signature(test_containmentwalker_dependency_IsolatedClassInReachablePackage.__init__)
    params = list(sig.parameters.keys())



def test_classinotherpackage_is_not_abstract():
    assert not inspect.isabstract(ClassInOtherPackage)


def test_classinotherpackage_constructor_exists():
    assert callable(ClassInOtherPackage.__init__)


def test_classinotherpackage_constructor_args():
    sig = inspect.signature(ClassInOtherPackage.__init__)
    params = list(sig.parameters.keys())



def test_test_containmentwalker_dependency_foo_is_not_abstract():
    assert not inspect.isabstract(test_containmentwalker_dependency_Foo)


def test_test_containmentwalker_dependency_foo_constructor_exists():
    assert callable(test_containmentwalker_dependency_Foo.__init__)


def test_test_containmentwalker_dependency_foo_constructor_args():
    sig = inspect.signature(test_containmentwalker_dependency_Foo.__init__)
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
test_containmentwalker_dependency_subpackage_ClassInOtherPackage_strategy = st.builds(
    test_containmentwalker_dependency_subpackage_ClassInOtherPackage,
)
test_containmentwalker_dependency_IsolatedClassInReachablePackage_strategy = st.builds(
    test_containmentwalker_dependency_IsolatedClassInReachablePackage,
)
ClassInOtherPackage_strategy = st.builds(
    ClassInOtherPackage,
)
test_containmentwalker_dependency_Foo_strategy = st.builds(
    test_containmentwalker_dependency_Foo,
)

@given(instance=test_containmentwalker_dependency_subpackage_ClassInOtherPackage_strategy)
@settings(max_examples=50)
def test_test_containmentwalker_dependency_subpackage_classinotherpackage_instantiation(instance):
    assert isinstance(instance, test_containmentwalker_dependency_subpackage_ClassInOtherPackage)

@given(instance=test_containmentwalker_dependency_IsolatedClassInReachablePackage_strategy)
@settings(max_examples=50)
def test_test_containmentwalker_dependency_isolatedclassinreachablepackage_instantiation(instance):
    assert isinstance(instance, test_containmentwalker_dependency_IsolatedClassInReachablePackage)

@given(instance=ClassInOtherPackage_strategy)
@settings(max_examples=50)
def test_classinotherpackage_instantiation(instance):
    assert isinstance(instance, ClassInOtherPackage)

@given(instance=test_containmentwalker_dependency_Foo_strategy)
@settings(max_examples=50)
def test_test_containmentwalker_dependency_foo_instantiation(instance):
    assert isinstance(instance, test_containmentwalker_dependency_Foo)
