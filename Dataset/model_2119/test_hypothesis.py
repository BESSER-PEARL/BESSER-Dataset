import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    test::AbstractTest,
    test::Tests,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_test::abstracttest_is_not_abstract():
    assert not inspect.isabstract(test::AbstractTest)


def test_test::abstracttest_constructor_exists():
    assert callable(test::AbstractTest.__init__)


def test_test::abstracttest_constructor_args():
    sig = inspect.signature(test::AbstractTest.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_test::abstracttest_has_text():
    assert hasattr(test::AbstractTest, "text")
    descriptor = None
    for klass in test::AbstractTest.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_test::tests_is_not_abstract():
    assert not inspect.isabstract(test::Tests)


def test_test::tests_constructor_exists():
    assert callable(test::Tests.__init__)


def test_test::tests_constructor_args():
    sig = inspect.signature(test::Tests.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_test::tests_has_name():
    assert hasattr(test::Tests, "name")
    descriptor = None
    for klass in test::Tests.__mro__:
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
test::AbstractTest_strategy = st.builds(
    test::AbstractTest,
    text=
        safe_text
)
test::Tests_strategy = st.builds(
    test::Tests,
    name=
        safe_text
)

@given(instance=test::AbstractTest_strategy)
@settings(max_examples=50)
def test_test::abstracttest_instantiation(instance):
    assert isinstance(instance, test::AbstractTest)

@given(instance=test::AbstractTest_strategy)
def test_test::abstracttest_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=test::AbstractTest_strategy)
def test_test::abstracttest_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=test::Tests_strategy)
@settings(max_examples=50)
def test_test::tests_instantiation(instance):
    assert isinstance(instance, test::Tests)

@given(instance=test::Tests_strategy)
def test_test::tests_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=test::Tests_strategy)
def test_test::tests_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
