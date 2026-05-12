import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    test_AbstractTest,
    test_Tests,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test_abstracttest_is_not_abstract():
    assert not inspect.isabstract(test_AbstractTest)


def test_test_abstracttest_constructor_exists():
    assert callable(test_AbstractTest.__init__)


def test_test_abstracttest_constructor_args():
    sig = inspect.signature(test_AbstractTest.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_test_abstracttest_has_text():
    assert hasattr(test_AbstractTest, "text")
    descriptor = None
    for klass in test_AbstractTest.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_test_tests_is_not_abstract():
    assert not inspect.isabstract(test_Tests)


def test_test_tests_constructor_exists():
    assert callable(test_Tests.__init__)


def test_test_tests_constructor_args():
    sig = inspect.signature(test_Tests.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_test_tests_has_name():
    assert hasattr(test_Tests, "name")
    descriptor = None
    for klass in test_Tests.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
test_AbstractTest_strategy = st.builds(
    test_AbstractTest,
    text=
        safe_text
)
test_Tests_strategy = st.builds(
    test_Tests,
    name=
        safe_text
)

@given(instance=test_AbstractTest_strategy)
@settings(max_examples=50)
def test_test_abstracttest_instantiation(instance):
    assert isinstance(instance, test_AbstractTest)



@given(instance=test_AbstractTest_strategy)
def test_test_abstracttest_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=test_Tests_strategy)
@settings(max_examples=50)
def test_test_tests_instantiation(instance):
    assert isinstance(instance, test_Tests)



@given(instance=test_Tests_strategy)
def test_test_tests_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
