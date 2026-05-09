import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    helloworld1::Thing,
    helloworld1::World,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_helloworld1::thing_is_not_abstract():
    assert not inspect.isabstract(helloworld1::Thing)


def test_helloworld1::thing_constructor_exists():
    assert callable(helloworld1::Thing.__init__)


def test_helloworld1::thing_constructor_args():
    sig = inspect.signature(helloworld1::Thing.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_helloworld1::thing_has_id():
    assert hasattr(helloworld1::Thing, "id")
    descriptor = None
    for klass in helloworld1::Thing.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_helloworld1::world_is_not_abstract():
    assert not inspect.isabstract(helloworld1::World)


def test_helloworld1::world_constructor_exists():
    assert callable(helloworld1::World.__init__)


def test_helloworld1::world_constructor_args():
    sig = inspect.signature(helloworld1::World.__init__)
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
helloworld1::Thing_strategy = st.builds(
    helloworld1::Thing,
    id=
        st.integers()
)
helloworld1::World_strategy = st.builds(
    helloworld1::World,
)

@given(instance=helloworld1::Thing_strategy)
@settings(max_examples=50)
def test_helloworld1::thing_instantiation(instance):
    assert isinstance(instance, helloworld1::Thing)

@given(instance=helloworld1::Thing_strategy)
def test_helloworld1::thing_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=helloworld1::Thing_strategy)
def test_helloworld1::thing_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=helloworld1::World_strategy)
@settings(max_examples=50)
def test_helloworld1::world_instantiation(instance):
    assert isinstance(instance, helloworld1::World)
