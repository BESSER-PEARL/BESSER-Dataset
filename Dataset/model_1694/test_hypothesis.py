import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    helloworld::Thing,
    helloworld::World,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_helloworld::thing_is_not_abstract():
    assert not inspect.isabstract(helloworld::Thing)


def test_helloworld::thing_constructor_exists():
    assert callable(helloworld::Thing.__init__)


def test_helloworld::thing_constructor_args():
    sig = inspect.signature(helloworld::Thing.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_helloworld::thing_has_name():
    assert hasattr(helloworld::Thing, "name")
    descriptor = None
    for klass in helloworld::Thing.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_helloworld::world_is_not_abstract():
    assert not inspect.isabstract(helloworld::World)


def test_helloworld::world_constructor_exists():
    assert callable(helloworld::World.__init__)


def test_helloworld::world_constructor_args():
    sig = inspect.signature(helloworld::World.__init__)
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
helloworld::Thing_strategy = st.builds(
    helloworld::Thing,
    name=
        safe_text
)
helloworld::World_strategy = st.builds(
    helloworld::World,
)

@given(instance=helloworld::Thing_strategy)
@settings(max_examples=50)
def test_helloworld::thing_instantiation(instance):
    assert isinstance(instance, helloworld::Thing)

@given(instance=helloworld::Thing_strategy)
def test_helloworld::thing_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=helloworld::Thing_strategy)
def test_helloworld::thing_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=helloworld::World_strategy)
@settings(max_examples=50)
def test_helloworld::world_instantiation(instance):
    assert isinstance(instance, helloworld::World)
