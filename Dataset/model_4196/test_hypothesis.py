import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    helloWorldDsl::Greeting,
    helloWorldDsl::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_helloworlddsl::greeting_is_not_abstract():
    assert not inspect.isabstract(helloWorldDsl::Greeting)


def test_helloworlddsl::greeting_constructor_exists():
    assert callable(helloWorldDsl::Greeting.__init__)


def test_helloworlddsl::greeting_constructor_args():
    sig = inspect.signature(helloWorldDsl::Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_helloworlddsl::greeting_has_name():
    assert hasattr(helloWorldDsl::Greeting, "name")
    descriptor = None
    for klass in helloWorldDsl::Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_helloworlddsl::model_is_not_abstract():
    assert not inspect.isabstract(helloWorldDsl::Model)


def test_helloworlddsl::model_constructor_exists():
    assert callable(helloWorldDsl::Model.__init__)


def test_helloworlddsl::model_constructor_args():
    sig = inspect.signature(helloWorldDsl::Model.__init__)
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
helloWorldDsl::Greeting_strategy = st.builds(
    helloWorldDsl::Greeting,
    name=
        safe_text
)
helloWorldDsl::Model_strategy = st.builds(
    helloWorldDsl::Model,
)

@given(instance=helloWorldDsl::Greeting_strategy)
@settings(max_examples=50)
def test_helloworlddsl::greeting_instantiation(instance):
    assert isinstance(instance, helloWorldDsl::Greeting)

@given(instance=helloWorldDsl::Greeting_strategy)
def test_helloworlddsl::greeting_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=helloWorldDsl::Greeting_strategy)
def test_helloworlddsl::greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=helloWorldDsl::Model_strategy)
@settings(max_examples=50)
def test_helloworlddsl::model_instantiation(instance):
    assert isinstance(instance, helloWorldDsl::Model)
