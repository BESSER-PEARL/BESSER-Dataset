import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    myDsl2_Greeting,
    myDsl2_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl2_greeting_is_not_abstract():
    assert not inspect.isabstract(myDsl2_Greeting)


def test_mydsl2_greeting_constructor_exists():
    assert callable(myDsl2_Greeting.__init__)


def test_mydsl2_greeting_constructor_args():
    sig = inspect.signature(myDsl2_Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl2_greeting_has_name():
    assert hasattr(myDsl2_Greeting, "name")
    descriptor = None
    for klass in myDsl2_Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl2_model_is_not_abstract():
    assert not inspect.isabstract(myDsl2_Model)


def test_mydsl2_model_constructor_exists():
    assert callable(myDsl2_Model.__init__)


def test_mydsl2_model_constructor_args():
    sig = inspect.signature(myDsl2_Model.__init__)
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
myDsl2_Greeting_strategy = st.builds(
    myDsl2_Greeting,
    name=
        safe_text
)
myDsl2_Model_strategy = st.builds(
    myDsl2_Model,
)

@given(instance=myDsl2_Greeting_strategy)
@settings(max_examples=50)
def test_mydsl2_greeting_instantiation(instance):
    assert isinstance(instance, myDsl2_Greeting)



@given(instance=myDsl2_Greeting_strategy)
def test_mydsl2_greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl2_Model_strategy)
@settings(max_examples=50)
def test_mydsl2_model_instantiation(instance):
    assert isinstance(instance, myDsl2_Model)
