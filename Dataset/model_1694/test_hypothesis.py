import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    helloworld_Thing,
    helloworld_World,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_helloworld_thing_is_not_abstract():
    assert not inspect.isabstract(helloworld_Thing)


def test_helloworld_thing_constructor_exists():
    assert callable(helloworld_Thing.__init__)


def test_helloworld_thing_constructor_args():
    sig = inspect.signature(helloworld_Thing.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_helloworld_thing_has_name():
    assert hasattr(helloworld_Thing, "name")
    descriptor = None
    for klass in helloworld_Thing.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_helloworld_world_is_not_abstract():
    assert not inspect.isabstract(helloworld_World)


def test_helloworld_world_constructor_exists():
    assert callable(helloworld_World.__init__)


def test_helloworld_world_constructor_args():
    sig = inspect.signature(helloworld_World.__init__)
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
helloworld_Thing_strategy = st.builds(
    helloworld_Thing,
    name=
        safe_text
)
helloworld_World_strategy = st.builds(
    helloworld_World,
)

@given(instance=helloworld_Thing_strategy)
@settings(max_examples=50)
def test_helloworld_thing_instantiation(instance):
    assert isinstance(instance, helloworld_Thing)



@given(instance=helloworld_Thing_strategy)
def test_helloworld_thing_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=helloworld_World_strategy)
@settings(max_examples=50)
def test_helloworld_world_instantiation(instance):
    assert isinstance(instance, helloworld_World)
