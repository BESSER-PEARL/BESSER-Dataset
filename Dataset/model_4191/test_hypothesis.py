import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    reneMartin::Greeting,
    reneMartin::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_renemartin::greeting_is_not_abstract():
    assert not inspect.isabstract(reneMartin::Greeting)


def test_renemartin::greeting_constructor_exists():
    assert callable(reneMartin::Greeting.__init__)


def test_renemartin::greeting_constructor_args():
    sig = inspect.signature(reneMartin::Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_renemartin::greeting_has_name():
    assert hasattr(reneMartin::Greeting, "name")
    descriptor = None
    for klass in reneMartin::Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_renemartin::model_is_not_abstract():
    assert not inspect.isabstract(reneMartin::Model)


def test_renemartin::model_constructor_exists():
    assert callable(reneMartin::Model.__init__)


def test_renemartin::model_constructor_args():
    sig = inspect.signature(reneMartin::Model.__init__)
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
reneMartin::Greeting_strategy = st.builds(
    reneMartin::Greeting,
    name=
        safe_text
)
reneMartin::Model_strategy = st.builds(
    reneMartin::Model,
)

@given(instance=reneMartin::Greeting_strategy)
@settings(max_examples=50)
def test_renemartin::greeting_instantiation(instance):
    assert isinstance(instance, reneMartin::Greeting)

@given(instance=reneMartin::Greeting_strategy)
def test_renemartin::greeting_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=reneMartin::Greeting_strategy)
def test_renemartin::greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=reneMartin::Model_strategy)
@settings(max_examples=50)
def test_renemartin::model_instantiation(instance):
    assert isinstance(instance, reneMartin::Model)
