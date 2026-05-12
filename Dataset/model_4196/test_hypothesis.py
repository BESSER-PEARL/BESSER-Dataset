import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    helloWorldDsl_Greeting,
    helloWorldDsl_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_helloworlddsl_greeting_is_not_abstract():
    assert not inspect.isabstract(helloWorldDsl_Greeting)


def test_helloworlddsl_greeting_constructor_exists():
    assert callable(helloWorldDsl_Greeting.__init__)


def test_helloworlddsl_greeting_constructor_args():
    sig = inspect.signature(helloWorldDsl_Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_helloworlddsl_greeting_has_name():
    assert hasattr(helloWorldDsl_Greeting, "name")
    descriptor = None
    for klass in helloWorldDsl_Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_helloworlddsl_model_is_not_abstract():
    assert not inspect.isabstract(helloWorldDsl_Model)


def test_helloworlddsl_model_constructor_exists():
    assert callable(helloWorldDsl_Model.__init__)


def test_helloworlddsl_model_constructor_args():
    sig = inspect.signature(helloWorldDsl_Model.__init__)
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
helloWorldDsl_Greeting_strategy = st.builds(
    helloWorldDsl_Greeting,
    name=
        safe_text
)
helloWorldDsl_Model_strategy = st.builds(
    helloWorldDsl_Model,
)

@given(instance=helloWorldDsl_Greeting_strategy)
@settings(max_examples=50)
def test_helloworlddsl_greeting_instantiation(instance):
    assert isinstance(instance, helloWorldDsl_Greeting)



@given(instance=helloWorldDsl_Greeting_strategy)
def test_helloworlddsl_greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=helloWorldDsl_Model_strategy)
@settings(max_examples=50)
def test_helloworlddsl_model_instantiation(instance):
    assert isinstance(instance, helloWorldDsl_Model)
