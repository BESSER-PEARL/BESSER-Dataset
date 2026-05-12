import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    resource_Greeting,
    resource_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_resource_greeting_is_not_abstract():
    assert not inspect.isabstract(resource_Greeting)


def test_resource_greeting_constructor_exists():
    assert callable(resource_Greeting.__init__)


def test_resource_greeting_constructor_args():
    sig = inspect.signature(resource_Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_resource_greeting_has_name():
    assert hasattr(resource_Greeting, "name")
    descriptor = None
    for klass in resource_Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_resource_model_is_not_abstract():
    assert not inspect.isabstract(resource_Model)


def test_resource_model_constructor_exists():
    assert callable(resource_Model.__init__)


def test_resource_model_constructor_args():
    sig = inspect.signature(resource_Model.__init__)
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
resource_Greeting_strategy = st.builds(
    resource_Greeting,
    name=
        safe_text
)
resource_Model_strategy = st.builds(
    resource_Model,
)

@given(instance=resource_Greeting_strategy)
@settings(max_examples=50)
def test_resource_greeting_instantiation(instance):
    assert isinstance(instance, resource_Greeting)



@given(instance=resource_Greeting_strategy)
def test_resource_greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=resource_Model_strategy)
@settings(max_examples=50)
def test_resource_model_instantiation(instance):
    assert isinstance(instance, resource_Model)
