import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    helloBuck_Greeting,
    helloBuck_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hellobuck_greeting_is_not_abstract():
    assert not inspect.isabstract(helloBuck_Greeting)


def test_hellobuck_greeting_constructor_exists():
    assert callable(helloBuck_Greeting.__init__)


def test_hellobuck_greeting_constructor_args():
    sig = inspect.signature(helloBuck_Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hellobuck_greeting_has_name():
    assert hasattr(helloBuck_Greeting, "name")
    descriptor = None
    for klass in helloBuck_Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hellobuck_model_is_not_abstract():
    assert not inspect.isabstract(helloBuck_Model)


def test_hellobuck_model_constructor_exists():
    assert callable(helloBuck_Model.__init__)


def test_hellobuck_model_constructor_args():
    sig = inspect.signature(helloBuck_Model.__init__)
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
helloBuck_Greeting_strategy = st.builds(
    helloBuck_Greeting,
    name=
        safe_text
)
helloBuck_Model_strategy = st.builds(
    helloBuck_Model,
)

@given(instance=helloBuck_Greeting_strategy)
@settings(max_examples=50)
def test_hellobuck_greeting_instantiation(instance):
    assert isinstance(instance, helloBuck_Greeting)



@given(instance=helloBuck_Greeting_strategy)
def test_hellobuck_greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=helloBuck_Model_strategy)
@settings(max_examples=50)
def test_hellobuck_model_instantiation(instance):
    assert isinstance(instance, helloBuck_Model)
