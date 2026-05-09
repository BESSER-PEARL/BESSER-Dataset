import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    basic2::Thing,
    basic2::World,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_basic2::thing_is_not_abstract():
    assert not inspect.isabstract(basic2::Thing)


def test_basic2::thing_constructor_exists():
    assert callable(basic2::Thing.__init__)


def test_basic2::thing_constructor_args():
    sig = inspect.signature(basic2::Thing.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_basic2::thing_has_id():
    assert hasattr(basic2::Thing, "id")
    descriptor = None
    for klass in basic2::Thing.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_basic2::world_is_not_abstract():
    assert not inspect.isabstract(basic2::World)


def test_basic2::world_constructor_exists():
    assert callable(basic2::World.__init__)


def test_basic2::world_constructor_args():
    sig = inspect.signature(basic2::World.__init__)
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
basic2::Thing_strategy = st.builds(
    basic2::Thing,
    id=
        st.integers()
)
basic2::World_strategy = st.builds(
    basic2::World,
)

@given(instance=basic2::Thing_strategy)
@settings(max_examples=50)
def test_basic2::thing_instantiation(instance):
    assert isinstance(instance, basic2::Thing)

@given(instance=basic2::Thing_strategy)
def test_basic2::thing_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=basic2::Thing_strategy)
def test_basic2::thing_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=basic2::World_strategy)
@settings(max_examples=50)
def test_basic2::world_instantiation(instance):
    assert isinstance(instance, basic2::World)
