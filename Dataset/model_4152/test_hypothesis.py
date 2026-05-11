import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    greetings::Greeting,
    greetings::GreetingsModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_greetings::greeting_is_not_abstract():
    assert not inspect.isabstract(greetings::Greeting)


def test_greetings::greeting_constructor_exists():
    assert callable(greetings::Greeting.__init__)


def test_greetings::greeting_constructor_args():
    sig = inspect.signature(greetings::Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_greetings::greeting_has_name():
    assert hasattr(greetings::Greeting, "name")
    descriptor = None
    for klass in greetings::Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_greetings::greetingsmodel_is_not_abstract():
    assert not inspect.isabstract(greetings::GreetingsModel)


def test_greetings::greetingsmodel_constructor_exists():
    assert callable(greetings::GreetingsModel.__init__)


def test_greetings::greetingsmodel_constructor_args():
    sig = inspect.signature(greetings::GreetingsModel.__init__)
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
greetings::Greeting_strategy = st.builds(
    greetings::Greeting,
    name=
        safe_text
)
greetings::GreetingsModel_strategy = st.builds(
    greetings::GreetingsModel,
)

@given(instance=greetings::Greeting_strategy)
@settings(max_examples=50)
def test_greetings::greeting_instantiation(instance):
    assert isinstance(instance, greetings::Greeting)

@given(instance=greetings::Greeting_strategy)
def test_greetings::greeting_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=greetings::Greeting_strategy)
def test_greetings::greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=greetings::GreetingsModel_strategy)
@settings(max_examples=50)
def test_greetings::greetingsmodel_instantiation(instance):
    assert isinstance(instance, greetings::GreetingsModel)
