import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    helloworld1_Thing,
    helloworld1_World,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_helloworld1_thing_is_not_abstract():
    assert not inspect.isabstract(helloworld1_Thing)


def test_helloworld1_thing_constructor_exists():
    assert callable(helloworld1_Thing.__init__)


def test_helloworld1_thing_constructor_args():
    sig = inspect.signature(helloworld1_Thing.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_helloworld1_thing_has_id():
    assert hasattr(helloworld1_Thing, "id")
    descriptor = None
    for klass in helloworld1_Thing.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_helloworld1_world_is_not_abstract():
    assert not inspect.isabstract(helloworld1_World)


def test_helloworld1_world_constructor_exists():
    assert callable(helloworld1_World.__init__)


def test_helloworld1_world_constructor_args():
    sig = inspect.signature(helloworld1_World.__init__)
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
helloworld1_Thing_strategy = st.builds(
    helloworld1_Thing,
    id=
        st.integers()
)
helloworld1_World_strategy = st.builds(
    helloworld1_World,
)

@given(instance=helloworld1_Thing_strategy)
@settings(max_examples=50)
def test_helloworld1_thing_instantiation(instance):
    assert isinstance(instance, helloworld1_Thing)



@given(instance=helloworld1_Thing_strategy)
def test_helloworld1_thing_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=helloworld1_World_strategy)
@settings(max_examples=50)
def test_helloworld1_world_instantiation(instance):
    assert isinstance(instance, helloworld1_World)
