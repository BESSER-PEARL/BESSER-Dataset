import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    reneMartin_Greeting,
    reneMartin_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_renemartin_greeting_is_not_abstract():
    assert not inspect.isabstract(reneMartin_Greeting)


def test_renemartin_greeting_constructor_exists():
    assert callable(reneMartin_Greeting.__init__)


def test_renemartin_greeting_constructor_args():
    sig = inspect.signature(reneMartin_Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_renemartin_greeting_has_name():
    assert hasattr(reneMartin_Greeting, "name")
    descriptor = None
    for klass in reneMartin_Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_renemartin_model_is_not_abstract():
    assert not inspect.isabstract(reneMartin_Model)


def test_renemartin_model_constructor_exists():
    assert callable(reneMartin_Model.__init__)


def test_renemartin_model_constructor_args():
    sig = inspect.signature(reneMartin_Model.__init__)
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
reneMartin_Greeting_strategy = st.builds(
    reneMartin_Greeting,
    name=
        safe_text
)
reneMartin_Model_strategy = st.builds(
    reneMartin_Model,
)

@given(instance=reneMartin_Greeting_strategy)
@settings(max_examples=50)
def test_renemartin_greeting_instantiation(instance):
    assert isinstance(instance, reneMartin_Greeting)



@given(instance=reneMartin_Greeting_strategy)
def test_renemartin_greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=reneMartin_Model_strategy)
@settings(max_examples=50)
def test_renemartin_model_instantiation(instance):
    assert isinstance(instance, reneMartin_Model)
