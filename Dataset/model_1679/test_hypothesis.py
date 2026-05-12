import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    basic_RelatedTo,
    basic_Thing,
    basic_World,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_basic_relatedto_is_not_abstract():
    assert not inspect.isabstract(basic_RelatedTo)


def test_basic_relatedto_constructor_exists():
    assert callable(basic_RelatedTo.__init__)


def test_basic_relatedto_constructor_args():
    sig = inspect.signature(basic_RelatedTo.__init__)
    params = list(sig.parameters.keys())
    assert "since" in params, "Missing parameter 'since'"

def test_basic_relatedto_has_since():
    assert hasattr(basic_RelatedTo, "since")
    descriptor = None
    for klass in basic_RelatedTo.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
            break
    assert isinstance(descriptor, property)



def test_basic_thing_is_not_abstract():
    assert not inspect.isabstract(basic_Thing)


def test_basic_thing_constructor_exists():
    assert callable(basic_Thing.__init__)


def test_basic_thing_constructor_args():
    sig = inspect.signature(basic_Thing.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_basic_thing_has_id():
    assert hasattr(basic_Thing, "id")
    descriptor = None
    for klass in basic_Thing.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_basic_world_is_not_abstract():
    assert not inspect.isabstract(basic_World)


def test_basic_world_constructor_exists():
    assert callable(basic_World.__init__)


def test_basic_world_constructor_args():
    sig = inspect.signature(basic_World.__init__)
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
basic_RelatedTo_strategy = st.builds(
    basic_RelatedTo,
    since=
        safe_text
)
basic_Thing_strategy = st.builds(
    basic_Thing,
    id=
        st.integers()
)
basic_World_strategy = st.builds(
    basic_World,
)

@given(instance=basic_RelatedTo_strategy)
@settings(max_examples=50)
def test_basic_relatedto_instantiation(instance):
    assert isinstance(instance, basic_RelatedTo)



@given(instance=basic_RelatedTo_strategy)
def test_basic_relatedto_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original

@given(instance=basic_Thing_strategy)
@settings(max_examples=50)
def test_basic_thing_instantiation(instance):
    assert isinstance(instance, basic_Thing)



@given(instance=basic_Thing_strategy)
def test_basic_thing_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=basic_World_strategy)
@settings(max_examples=50)
def test_basic_world_instantiation(instance):
    assert isinstance(instance, basic_World)
