import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    pascal_Greeting,
    pascal_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_pascal_greeting_is_not_abstract():
    assert not inspect.isabstract(pascal_Greeting)


def test_pascal_greeting_constructor_exists():
    assert callable(pascal_Greeting.__init__)


def test_pascal_greeting_constructor_args():
    sig = inspect.signature(pascal_Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pascal_greeting_has_name():
    assert hasattr(pascal_Greeting, "name")
    descriptor = None
    for klass in pascal_Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pascal_model_is_not_abstract():
    assert not inspect.isabstract(pascal_Model)


def test_pascal_model_constructor_exists():
    assert callable(pascal_Model.__init__)


def test_pascal_model_constructor_args():
    sig = inspect.signature(pascal_Model.__init__)
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
pascal_Greeting_strategy = st.builds(
    pascal_Greeting,
    name=
        safe_text
)
pascal_Model_strategy = st.builds(
    pascal_Model,
)

@given(instance=pascal_Greeting_strategy)
@settings(max_examples=50)
def test_pascal_greeting_instantiation(instance):
    assert isinstance(instance, pascal_Greeting)



@given(instance=pascal_Greeting_strategy)
def test_pascal_greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pascal_Model_strategy)
@settings(max_examples=50)
def test_pascal_model_instantiation(instance):
    assert isinstance(instance, pascal_Model)
