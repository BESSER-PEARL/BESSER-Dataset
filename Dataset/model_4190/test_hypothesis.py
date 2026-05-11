import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    evlDSL::Greeting,
    evlDSL::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_evldsl::greeting_is_not_abstract():
    assert not inspect.isabstract(evlDSL::Greeting)


def test_evldsl::greeting_constructor_exists():
    assert callable(evlDSL::Greeting.__init__)


def test_evldsl::greeting_constructor_args():
    sig = inspect.signature(evlDSL::Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_evldsl::greeting_has_name():
    assert hasattr(evlDSL::Greeting, "name")
    descriptor = None
    for klass in evlDSL::Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_evldsl::model_is_not_abstract():
    assert not inspect.isabstract(evlDSL::Model)


def test_evldsl::model_constructor_exists():
    assert callable(evlDSL::Model.__init__)


def test_evldsl::model_constructor_args():
    sig = inspect.signature(evlDSL::Model.__init__)
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
evlDSL::Greeting_strategy = st.builds(
    evlDSL::Greeting,
    name=
        safe_text
)
evlDSL::Model_strategy = st.builds(
    evlDSL::Model,
)

@given(instance=evlDSL::Greeting_strategy)
@settings(max_examples=50)
def test_evldsl::greeting_instantiation(instance):
    assert isinstance(instance, evlDSL::Greeting)

@given(instance=evlDSL::Greeting_strategy)
def test_evldsl::greeting_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=evlDSL::Greeting_strategy)
def test_evldsl::greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=evlDSL::Model_strategy)
@settings(max_examples=50)
def test_evldsl::model_instantiation(instance):
    assert isinstance(instance, evlDSL::Model)
