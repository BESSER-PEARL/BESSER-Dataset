import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    myDsl2::Greeting,
    myDsl2::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl2::greeting_is_not_abstract():
    assert not inspect.isabstract(myDsl2::Greeting)


def test_mydsl2::greeting_constructor_exists():
    assert callable(myDsl2::Greeting.__init__)


def test_mydsl2::greeting_constructor_args():
    sig = inspect.signature(myDsl2::Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl2::greeting_has_name():
    assert hasattr(myDsl2::Greeting, "name")
    descriptor = None
    for klass in myDsl2::Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl2::model_is_not_abstract():
    assert not inspect.isabstract(myDsl2::Model)


def test_mydsl2::model_constructor_exists():
    assert callable(myDsl2::Model.__init__)


def test_mydsl2::model_constructor_args():
    sig = inspect.signature(myDsl2::Model.__init__)
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
myDsl2::Greeting_strategy = st.builds(
    myDsl2::Greeting,
    name=
        safe_text
)
myDsl2::Model_strategy = st.builds(
    myDsl2::Model,
)

@given(instance=myDsl2::Greeting_strategy)
@settings(max_examples=50)
def test_mydsl2::greeting_instantiation(instance):
    assert isinstance(instance, myDsl2::Greeting)

@given(instance=myDsl2::Greeting_strategy)
def test_mydsl2::greeting_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl2::Greeting_strategy)
def test_mydsl2::greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl2::Model_strategy)
@settings(max_examples=50)
def test_mydsl2::model_instantiation(instance):
    assert isinstance(instance, myDsl2::Model)
