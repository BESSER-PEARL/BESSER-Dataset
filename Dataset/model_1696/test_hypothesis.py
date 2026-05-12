import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    basic2_Thing,
    basic2_World,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_basic2_thing_is_not_abstract():
    assert not inspect.isabstract(basic2_Thing)


def test_basic2_thing_constructor_exists():
    assert callable(basic2_Thing.__init__)


def test_basic2_thing_constructor_args():
    sig = inspect.signature(basic2_Thing.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_basic2_thing_has_id():
    assert hasattr(basic2_Thing, "id")
    descriptor = None
    for klass in basic2_Thing.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_basic2_world_is_not_abstract():
    assert not inspect.isabstract(basic2_World)


def test_basic2_world_constructor_exists():
    assert callable(basic2_World.__init__)


def test_basic2_world_constructor_args():
    sig = inspect.signature(basic2_World.__init__)
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
basic2_Thing_strategy = st.builds(
    basic2_Thing,
    id=
        st.integers()
)
basic2_World_strategy = st.builds(
    basic2_World,
)

@given(instance=basic2_Thing_strategy)
@settings(max_examples=50)
def test_basic2_thing_instantiation(instance):
    assert isinstance(instance, basic2_Thing)



@given(instance=basic2_Thing_strategy)
def test_basic2_thing_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=basic2_World_strategy)
@settings(max_examples=50)
def test_basic2_world_instantiation(instance):
    assert isinstance(instance, basic2_World)
