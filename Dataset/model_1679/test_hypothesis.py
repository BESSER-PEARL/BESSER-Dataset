import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    basic::RelatedTo,
    basic::Thing,
    basic::World,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_basic::relatedto_is_not_abstract():
    assert not inspect.isabstract(basic::RelatedTo)


def test_basic::relatedto_constructor_exists():
    assert callable(basic::RelatedTo.__init__)


def test_basic::relatedto_constructor_args():
    sig = inspect.signature(basic::RelatedTo.__init__)
    params = list(sig.parameters.keys())
    assert "since" in params, "Missing parameter 'since'"

def test_basic::relatedto_has_since():
    assert hasattr(basic::RelatedTo, "since")
    descriptor = None
    for klass in basic::RelatedTo.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
            break
    assert isinstance(descriptor, property)



def test_basic::thing_is_not_abstract():
    assert not inspect.isabstract(basic::Thing)


def test_basic::thing_constructor_exists():
    assert callable(basic::Thing.__init__)


def test_basic::thing_constructor_args():
    sig = inspect.signature(basic::Thing.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_basic::thing_has_id():
    assert hasattr(basic::Thing, "id")
    descriptor = None
    for klass in basic::Thing.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_basic::world_is_not_abstract():
    assert not inspect.isabstract(basic::World)


def test_basic::world_constructor_exists():
    assert callable(basic::World.__init__)


def test_basic::world_constructor_args():
    sig = inspect.signature(basic::World.__init__)
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
basic::RelatedTo_strategy = st.builds(
    basic::RelatedTo,
    since=
        safe_text
)
basic::Thing_strategy = st.builds(
    basic::Thing,
    id=
        st.integers()
)
basic::World_strategy = st.builds(
    basic::World,
)

@given(instance=basic::RelatedTo_strategy)
@settings(max_examples=50)
def test_basic::relatedto_instantiation(instance):
    assert isinstance(instance, basic::RelatedTo)

@given(instance=basic::RelatedTo_strategy)
def test_basic::relatedto_since_type(instance):
    assert isinstance(instance.since, str)


@given(instance=basic::RelatedTo_strategy)
def test_basic::relatedto_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original

@given(instance=basic::Thing_strategy)
@settings(max_examples=50)
def test_basic::thing_instantiation(instance):
    assert isinstance(instance, basic::Thing)

@given(instance=basic::Thing_strategy)
def test_basic::thing_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=basic::Thing_strategy)
def test_basic::thing_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=basic::World_strategy)
@settings(max_examples=50)
def test_basic::world_instantiation(instance):
    assert isinstance(instance, basic::World)
