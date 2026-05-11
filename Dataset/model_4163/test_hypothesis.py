import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    resource::Greeting,
    resource::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_resource::greeting_is_not_abstract():
    assert not inspect.isabstract(resource::Greeting)


def test_resource::greeting_constructor_exists():
    assert callable(resource::Greeting.__init__)


def test_resource::greeting_constructor_args():
    sig = inspect.signature(resource::Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_resource::greeting_has_name():
    assert hasattr(resource::Greeting, "name")
    descriptor = None
    for klass in resource::Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_resource::model_is_not_abstract():
    assert not inspect.isabstract(resource::Model)


def test_resource::model_constructor_exists():
    assert callable(resource::Model.__init__)


def test_resource::model_constructor_args():
    sig = inspect.signature(resource::Model.__init__)
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
resource::Greeting_strategy = st.builds(
    resource::Greeting,
    name=
        safe_text
)
resource::Model_strategy = st.builds(
    resource::Model,
)

@given(instance=resource::Greeting_strategy)
@settings(max_examples=50)
def test_resource::greeting_instantiation(instance):
    assert isinstance(instance, resource::Greeting)

@given(instance=resource::Greeting_strategy)
def test_resource::greeting_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=resource::Greeting_strategy)
def test_resource::greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=resource::Model_strategy)
@settings(max_examples=50)
def test_resource::model_instantiation(instance):
    assert isinstance(instance, resource::Model)
