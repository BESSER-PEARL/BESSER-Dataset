import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    testLanguage::Greeting,
    testLanguage::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_testlanguage::greeting_is_not_abstract():
    assert not inspect.isabstract(testLanguage::Greeting)


def test_testlanguage::greeting_constructor_exists():
    assert callable(testLanguage::Greeting.__init__)


def test_testlanguage::greeting_constructor_args():
    sig = inspect.signature(testLanguage::Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_testlanguage::greeting_has_name():
    assert hasattr(testLanguage::Greeting, "name")
    descriptor = None
    for klass in testLanguage::Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_testlanguage::model_is_not_abstract():
    assert not inspect.isabstract(testLanguage::Model)


def test_testlanguage::model_constructor_exists():
    assert callable(testLanguage::Model.__init__)


def test_testlanguage::model_constructor_args():
    sig = inspect.signature(testLanguage::Model.__init__)
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
testLanguage::Greeting_strategy = st.builds(
    testLanguage::Greeting,
    name=
        safe_text
)
testLanguage::Model_strategy = st.builds(
    testLanguage::Model,
)

@given(instance=testLanguage::Greeting_strategy)
@settings(max_examples=50)
def test_testlanguage::greeting_instantiation(instance):
    assert isinstance(instance, testLanguage::Greeting)

@given(instance=testLanguage::Greeting_strategy)
def test_testlanguage::greeting_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=testLanguage::Greeting_strategy)
def test_testlanguage::greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=testLanguage::Model_strategy)
@settings(max_examples=50)
def test_testlanguage::model_instantiation(instance):
    assert isinstance(instance, testLanguage::Model)
