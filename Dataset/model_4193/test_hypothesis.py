import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    helloBuck::Greeting,
    helloBuck::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hellobuck::greeting_is_not_abstract():
    assert not inspect.isabstract(helloBuck::Greeting)


def test_hellobuck::greeting_constructor_exists():
    assert callable(helloBuck::Greeting.__init__)


def test_hellobuck::greeting_constructor_args():
    sig = inspect.signature(helloBuck::Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hellobuck::greeting_has_name():
    assert hasattr(helloBuck::Greeting, "name")
    descriptor = None
    for klass in helloBuck::Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hellobuck::model_is_not_abstract():
    assert not inspect.isabstract(helloBuck::Model)


def test_hellobuck::model_constructor_exists():
    assert callable(helloBuck::Model.__init__)


def test_hellobuck::model_constructor_args():
    sig = inspect.signature(helloBuck::Model.__init__)
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
helloBuck::Greeting_strategy = st.builds(
    helloBuck::Greeting,
    name=
        safe_text
)
helloBuck::Model_strategy = st.builds(
    helloBuck::Model,
)

@given(instance=helloBuck::Greeting_strategy)
@settings(max_examples=50)
def test_hellobuck::greeting_instantiation(instance):
    assert isinstance(instance, helloBuck::Greeting)

@given(instance=helloBuck::Greeting_strategy)
def test_hellobuck::greeting_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=helloBuck::Greeting_strategy)
def test_hellobuck::greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=helloBuck::Model_strategy)
@settings(max_examples=50)
def test_hellobuck::model_instantiation(instance):
    assert isinstance(instance, helloBuck::Model)
