import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    testSuite::Test,
    testSuite::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testsuite::test_is_not_abstract():
    assert not inspect.isabstract(testSuite::Test)


def test_testsuite::test_constructor_exists():
    assert callable(testSuite::Test.__init__)


def test_testsuite::test_constructor_args():
    sig = inspect.signature(testSuite::Test.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_testsuite::test_has_name():
    assert hasattr(testSuite::Test, "name")
    descriptor = None
    for klass in testSuite::Test.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_testsuite::model_is_not_abstract():
    assert not inspect.isabstract(testSuite::Model)


def test_testsuite::model_constructor_exists():
    assert callable(testSuite::Model.__init__)


def test_testsuite::model_constructor_args():
    sig = inspect.signature(testSuite::Model.__init__)
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
testSuite::Test_strategy = st.builds(
    testSuite::Test,
    name=
        safe_text
)
testSuite::Model_strategy = st.builds(
    testSuite::Model,
)

@given(instance=testSuite::Test_strategy)
@settings(max_examples=50)
def test_testsuite::test_instantiation(instance):
    assert isinstance(instance, testSuite::Test)

@given(instance=testSuite::Test_strategy)
def test_testsuite::test_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=testSuite::Test_strategy)
def test_testsuite::test_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=testSuite::Model_strategy)
@settings(max_examples=50)
def test_testsuite::model_instantiation(instance):
    assert isinstance(instance, testSuite::Model)
