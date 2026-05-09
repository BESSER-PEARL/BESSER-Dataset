import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    iupjwq::RelatedTo,
    iupjwq::Thing,
    iupjwq::World,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_iupjwq::relatedto_is_not_abstract():
    assert not inspect.isabstract(iupjwq::RelatedTo)


def test_iupjwq::relatedto_constructor_exists():
    assert callable(iupjwq::RelatedTo.__init__)


def test_iupjwq::relatedto_constructor_args():
    sig = inspect.signature(iupjwq::RelatedTo.__init__)
    params = list(sig.parameters.keys())
    assert "since" in params, "Missing parameter 'since'"

def test_iupjwq::relatedto_has_since():
    assert hasattr(iupjwq::RelatedTo, "since")
    descriptor = None
    for klass in iupjwq::RelatedTo.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
            break
    assert isinstance(descriptor, property)



def test_iupjwq::thing_is_not_abstract():
    assert not inspect.isabstract(iupjwq::Thing)


def test_iupjwq::thing_constructor_exists():
    assert callable(iupjwq::Thing.__init__)


def test_iupjwq::thing_constructor_args():
    sig = inspect.signature(iupjwq::Thing.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_iupjwq::thing_has_id():
    assert hasattr(iupjwq::Thing, "id")
    descriptor = None
    for klass in iupjwq::Thing.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_iupjwq::world_is_not_abstract():
    assert not inspect.isabstract(iupjwq::World)


def test_iupjwq::world_constructor_exists():
    assert callable(iupjwq::World.__init__)


def test_iupjwq::world_constructor_args():
    sig = inspect.signature(iupjwq::World.__init__)
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
iupjwq::RelatedTo_strategy = st.builds(
    iupjwq::RelatedTo,
    since=
        safe_text
)
iupjwq::Thing_strategy = st.builds(
    iupjwq::Thing,
    id=
        st.integers()
)
iupjwq::World_strategy = st.builds(
    iupjwq::World,
)

@given(instance=iupjwq::RelatedTo_strategy)
@settings(max_examples=50)
def test_iupjwq::relatedto_instantiation(instance):
    assert isinstance(instance, iupjwq::RelatedTo)

@given(instance=iupjwq::RelatedTo_strategy)
def test_iupjwq::relatedto_since_type(instance):
    assert isinstance(instance.since, str)


@given(instance=iupjwq::RelatedTo_strategy)
def test_iupjwq::relatedto_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original

@given(instance=iupjwq::Thing_strategy)
@settings(max_examples=50)
def test_iupjwq::thing_instantiation(instance):
    assert isinstance(instance, iupjwq::Thing)

@given(instance=iupjwq::Thing_strategy)
def test_iupjwq::thing_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=iupjwq::Thing_strategy)
def test_iupjwq::thing_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=iupjwq::World_strategy)
@settings(max_examples=50)
def test_iupjwq::world_instantiation(instance):
    assert isinstance(instance, iupjwq::World)
