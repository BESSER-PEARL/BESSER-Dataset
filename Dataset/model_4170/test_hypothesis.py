import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    docl::Greeting,
    docl::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_docl::greeting_is_not_abstract():
    assert not inspect.isabstract(docl::Greeting)


def test_docl::greeting_constructor_exists():
    assert callable(docl::Greeting.__init__)


def test_docl::greeting_constructor_args():
    sig = inspect.signature(docl::Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_docl::greeting_has_name():
    assert hasattr(docl::Greeting, "name")
    descriptor = None
    for klass in docl::Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_docl::model_is_not_abstract():
    assert not inspect.isabstract(docl::Model)


def test_docl::model_constructor_exists():
    assert callable(docl::Model.__init__)


def test_docl::model_constructor_args():
    sig = inspect.signature(docl::Model.__init__)
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
docl::Greeting_strategy = st.builds(
    docl::Greeting,
    name=
        safe_text
)
docl::Model_strategy = st.builds(
    docl::Model,
)

@given(instance=docl::Greeting_strategy)
@settings(max_examples=50)
def test_docl::greeting_instantiation(instance):
    assert isinstance(instance, docl::Greeting)

@given(instance=docl::Greeting_strategy)
def test_docl::greeting_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=docl::Greeting_strategy)
def test_docl::greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=docl::Model_strategy)
@settings(max_examples=50)
def test_docl::model_instantiation(instance):
    assert isinstance(instance, docl::Model)
