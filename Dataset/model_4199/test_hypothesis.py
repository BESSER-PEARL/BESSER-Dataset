import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    myDsl::Greeting,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mydsl::greeting_is_not_abstract():
    assert not inspect.isabstract(myDsl::Greeting)


def test_mydsl::greeting_constructor_exists():
    assert callable(myDsl::Greeting.__init__)


def test_mydsl::greeting_constructor_args():
    sig = inspect.signature(myDsl::Greeting.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl::greeting_has_name():
    assert hasattr(myDsl::Greeting, "name")
    descriptor = None
    for klass in myDsl::Greeting.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)


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
myDsl::Greeting_strategy = st.builds(
    myDsl::Greeting,
    name=
        safe_text
)

@given(instance=myDsl::Greeting_strategy)
@settings(max_examples=50)
def test_mydsl::greeting_instantiation(instance):
    assert isinstance(instance, myDsl::Greeting)

@given(instance=myDsl::Greeting_strategy)
def test_mydsl::greeting_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=myDsl::Greeting_strategy)
def test_mydsl::greeting_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
