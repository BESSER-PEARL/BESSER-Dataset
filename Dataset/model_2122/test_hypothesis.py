import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    testSuite_Test,
    testSuite_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testsuite_test_is_not_abstract():
    assert not inspect.isabstract(testSuite_Test)


def test_testsuite_test_constructor_exists():
    assert callable(testSuite_Test.__init__)


def test_testsuite_test_constructor_args():
    sig = inspect.signature(testSuite_Test.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_testsuite_test_has_name():
    assert hasattr(testSuite_Test, "name")
    descriptor = None
    for klass in testSuite_Test.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_testsuite_model_is_not_abstract():
    assert not inspect.isabstract(testSuite_Model)


def test_testsuite_model_constructor_exists():
    assert callable(testSuite_Model.__init__)


def test_testsuite_model_constructor_args():
    sig = inspect.signature(testSuite_Model.__init__)
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
testSuite_Test_strategy = st.builds(
    testSuite_Test,
    name=
        safe_text
)
testSuite_Model_strategy = st.builds(
    testSuite_Model,
)

@given(instance=testSuite_Test_strategy)
@settings(max_examples=50)
def test_testsuite_test_instantiation(instance):
    assert isinstance(instance, testSuite_Test)



@given(instance=testSuite_Test_strategy)
def test_testsuite_test_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=testSuite_Model_strategy)
@settings(max_examples=50)
def test_testsuite_model_instantiation(instance):
    assert isinstance(instance, testSuite_Model)
