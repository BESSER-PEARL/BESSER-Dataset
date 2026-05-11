import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    myDslA::Greeting,
    myDslA::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsla::greeting_is_not_abstract():
    assert not inspect.isabstract(myDslA::Greeting)


def test_mydsla::greeting_constructor_exists():
    assert callable(myDslA::Greeting.__init__)


def test_mydsla::greeting_constructor_args():
    sig = inspect.signature(myDslA::Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsla::greeting_has_name():
    assert hasattr(myDslA::Greeting, "name")
    descriptor = None
    for klass in myDslA::Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsla::model_is_not_abstract():
    assert not inspect.isabstract(myDslA::Model)


def test_mydsla::model_constructor_exists():
    assert callable(myDslA::Model.__init__)


def test_mydsla::model_constructor_args():
    sig = inspect.signature(myDslA::Model.__init__)
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
myDslA::Greeting_strategy = st.builds(
    myDslA::Greeting,
    name=
        safe_text
)
myDslA::Model_strategy = st.builds(
    myDslA::Model,
)

@given(instance=myDslA::Greeting_strategy)
@settings(max_examples=50)
def test_mydsla::greeting_instantiation(instance):
    assert isinstance(instance, myDslA::Greeting)

@given(instance=myDslA::Greeting_strategy)
def test_mydsla::greeting_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDslA::Greeting_strategy)
def test_mydsla::greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDslA::Model_strategy)
@settings(max_examples=50)
def test_mydsla::model_instantiation(instance):
    assert isinstance(instance, myDslA::Model)
