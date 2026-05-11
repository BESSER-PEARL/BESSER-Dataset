import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    xSampleDsl::Greeting,
    xSampleDsl::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_xsampledsl::greeting_is_not_abstract():
    assert not inspect.isabstract(xSampleDsl::Greeting)


def test_xsampledsl::greeting_constructor_exists():
    assert callable(xSampleDsl::Greeting.__init__)


def test_xsampledsl::greeting_constructor_args():
    sig = inspect.signature(xSampleDsl::Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_xsampledsl::greeting_has_name():
    assert hasattr(xSampleDsl::Greeting, "name")
    descriptor = None
    for klass in xSampleDsl::Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_xsampledsl::model_is_not_abstract():
    assert not inspect.isabstract(xSampleDsl::Model)


def test_xsampledsl::model_constructor_exists():
    assert callable(xSampleDsl::Model.__init__)


def test_xsampledsl::model_constructor_args():
    sig = inspect.signature(xSampleDsl::Model.__init__)
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
xSampleDsl::Greeting_strategy = st.builds(
    xSampleDsl::Greeting,
    name=
        safe_text
)
xSampleDsl::Model_strategy = st.builds(
    xSampleDsl::Model,
)

@given(instance=xSampleDsl::Greeting_strategy)
@settings(max_examples=50)
def test_xsampledsl::greeting_instantiation(instance):
    assert isinstance(instance, xSampleDsl::Greeting)

@given(instance=xSampleDsl::Greeting_strategy)
def test_xsampledsl::greeting_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=xSampleDsl::Greeting_strategy)
def test_xsampledsl::greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xSampleDsl::Model_strategy)
@settings(max_examples=50)
def test_xsampledsl::model_instantiation(instance):
    assert isinstance(instance, xSampleDsl::Model)
