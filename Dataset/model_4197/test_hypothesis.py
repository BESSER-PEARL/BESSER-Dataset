import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    xSampleDsl_Greeting,
    xSampleDsl_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_xsampledsl_greeting_is_not_abstract():
    assert not inspect.isabstract(xSampleDsl_Greeting)


def test_xsampledsl_greeting_constructor_exists():
    assert callable(xSampleDsl_Greeting.__init__)


def test_xsampledsl_greeting_constructor_args():
    sig = inspect.signature(xSampleDsl_Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_xsampledsl_greeting_has_name():
    assert hasattr(xSampleDsl_Greeting, "name")
    descriptor = None
    for klass in xSampleDsl_Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_xsampledsl_model_is_not_abstract():
    assert not inspect.isabstract(xSampleDsl_Model)


def test_xsampledsl_model_constructor_exists():
    assert callable(xSampleDsl_Model.__init__)


def test_xsampledsl_model_constructor_args():
    sig = inspect.signature(xSampleDsl_Model.__init__)
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
xSampleDsl_Greeting_strategy = st.builds(
    xSampleDsl_Greeting,
    name=
        safe_text
)
xSampleDsl_Model_strategy = st.builds(
    xSampleDsl_Model,
)

@given(instance=xSampleDsl_Greeting_strategy)
@settings(max_examples=50)
def test_xsampledsl_greeting_instantiation(instance):
    assert isinstance(instance, xSampleDsl_Greeting)



@given(instance=xSampleDsl_Greeting_strategy)
def test_xsampledsl_greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xSampleDsl_Model_strategy)
@settings(max_examples=50)
def test_xsampledsl_model_instantiation(instance):
    assert isinstance(instance, xSampleDsl_Model)
