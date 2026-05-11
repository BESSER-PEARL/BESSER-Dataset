import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    java::Greeting,
    java::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_java::greeting_is_not_abstract():
    assert not inspect.isabstract(java::Greeting)


def test_java::greeting_constructor_exists():
    assert callable(java::Greeting.__init__)


def test_java::greeting_constructor_args():
    sig = inspect.signature(java::Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_java::greeting_has_name():
    assert hasattr(java::Greeting, "name")
    descriptor = None
    for klass in java::Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_java::model_is_not_abstract():
    assert not inspect.isabstract(java::Model)


def test_java::model_constructor_exists():
    assert callable(java::Model.__init__)


def test_java::model_constructor_args():
    sig = inspect.signature(java::Model.__init__)
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
java::Greeting_strategy = st.builds(
    java::Greeting,
    name=
        safe_text
)
java::Model_strategy = st.builds(
    java::Model,
)

@given(instance=java::Greeting_strategy)
@settings(max_examples=50)
def test_java::greeting_instantiation(instance):
    assert isinstance(instance, java::Greeting)

@given(instance=java::Greeting_strategy)
def test_java::greeting_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=java::Greeting_strategy)
def test_java::greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=java::Model_strategy)
@settings(max_examples=50)
def test_java::model_instantiation(instance):
    assert isinstance(instance, java::Model)
