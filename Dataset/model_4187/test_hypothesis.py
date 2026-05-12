import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    mDSL_Greeting,
    mDSL_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mdsl_greeting_is_not_abstract():
    assert not inspect.isabstract(mDSL_Greeting)


def test_mdsl_greeting_constructor_exists():
    assert callable(mDSL_Greeting.__init__)


def test_mdsl_greeting_constructor_args():
    sig = inspect.signature(mDSL_Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mdsl_greeting_has_name():
    assert hasattr(mDSL_Greeting, "name")
    descriptor = None
    for klass in mDSL_Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mdsl_model_is_not_abstract():
    assert not inspect.isabstract(mDSL_Model)


def test_mdsl_model_constructor_exists():
    assert callable(mDSL_Model.__init__)


def test_mdsl_model_constructor_args():
    sig = inspect.signature(mDSL_Model.__init__)
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
mDSL_Greeting_strategy = st.builds(
    mDSL_Greeting,
    name=
        safe_text
)
mDSL_Model_strategy = st.builds(
    mDSL_Model,
)

@given(instance=mDSL_Greeting_strategy)
@settings(max_examples=50)
def test_mdsl_greeting_instantiation(instance):
    assert isinstance(instance, mDSL_Greeting)



@given(instance=mDSL_Greeting_strategy)
def test_mdsl_greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mDSL_Model_strategy)
@settings(max_examples=50)
def test_mdsl_model_instantiation(instance):
    assert isinstance(instance, mDSL_Model)
