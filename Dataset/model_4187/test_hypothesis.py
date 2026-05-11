import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    mDSL::Greeting,
    mDSL::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mdsl::greeting_is_not_abstract():
    assert not inspect.isabstract(mDSL::Greeting)


def test_mdsl::greeting_constructor_exists():
    assert callable(mDSL::Greeting.__init__)


def test_mdsl::greeting_constructor_args():
    sig = inspect.signature(mDSL::Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mdsl::greeting_has_name():
    assert hasattr(mDSL::Greeting, "name")
    descriptor = None
    for klass in mDSL::Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mdsl::model_is_not_abstract():
    assert not inspect.isabstract(mDSL::Model)


def test_mdsl::model_constructor_exists():
    assert callable(mDSL::Model.__init__)


def test_mdsl::model_constructor_args():
    sig = inspect.signature(mDSL::Model.__init__)
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
mDSL::Greeting_strategy = st.builds(
    mDSL::Greeting,
    name=
        safe_text
)
mDSL::Model_strategy = st.builds(
    mDSL::Model,
)

@given(instance=mDSL::Greeting_strategy)
@settings(max_examples=50)
def test_mdsl::greeting_instantiation(instance):
    assert isinstance(instance, mDSL::Greeting)

@given(instance=mDSL::Greeting_strategy)
def test_mdsl::greeting_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mDSL::Greeting_strategy)
def test_mdsl::greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mDSL::Model_strategy)
@settings(max_examples=50)
def test_mdsl::model_instantiation(instance):
    assert isinstance(instance, mDSL::Model)
