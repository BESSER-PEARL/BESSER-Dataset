import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    simpleb::B1,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simpleb::b1_is_not_abstract():
    assert not inspect.isabstract(simpleb::B1)


def test_simpleb::b1_constructor_exists():
    assert callable(simpleb::B1.__init__)


def test_simpleb::b1_constructor_args():
    sig = inspect.signature(simpleb::B1.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleb::b1_has_name():
    assert hasattr(simpleb::B1, "name")
    descriptor = None
    for klass in simpleb::B1.__mro__:
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
simpleb::B1_strategy = st.builds(
    simpleb::B1,
    name=
        safe_text
)

@given(instance=simpleb::B1_strategy)
@settings(max_examples=50)
def test_simpleb::b1_instantiation(instance):
    assert isinstance(instance, simpleb::B1)

@given(instance=simpleb::B1_strategy)
def test_simpleb::b1_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpleb::B1_strategy)
def test_simpleb::b1_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
