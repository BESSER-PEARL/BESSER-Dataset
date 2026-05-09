import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    rel2rel::World,
    Thing,
    rel2rel::NamedElement,
    rel2rel::RelatedTo,
    NamedElement,
    rel2rel::Thing,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rel2rel::world_is_not_abstract():
    assert not inspect.isabstract(rel2rel::World)


def test_rel2rel::world_constructor_exists():
    assert callable(rel2rel::World.__init__)


def test_rel2rel::world_constructor_args():
    sig = inspect.signature(rel2rel::World.__init__)
    params = list(sig.parameters.keys())



def test_thing_is_not_abstract():
    assert not inspect.isabstract(Thing)


def test_thing_constructor_exists():
    assert callable(Thing.__init__)


def test_thing_constructor_args():
    sig = inspect.signature(Thing.__init__)
    params = list(sig.parameters.keys())



def test_rel2rel::namedelement_is_not_abstract():
    assert not inspect.isabstract(rel2rel::NamedElement)


def test_rel2rel::namedelement_constructor_exists():
    assert callable(rel2rel::NamedElement.__init__)


def test_rel2rel::namedelement_constructor_args():
    sig = inspect.signature(rel2rel::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rel2rel::namedelement_has_name():
    assert hasattr(rel2rel::NamedElement, "name")
    descriptor = None
    for klass in rel2rel::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rel2rel::relatedto_is_not_abstract():
    assert not inspect.isabstract(rel2rel::RelatedTo)


def test_rel2rel::relatedto_constructor_exists():
    assert callable(rel2rel::RelatedTo.__init__)


def test_rel2rel::relatedto_constructor_args():
    sig = inspect.signature(rel2rel::RelatedTo.__init__)
    params = list(sig.parameters.keys())
    assert "since" in params, "Missing parameter 'since'"

def test_rel2rel::relatedto_has_since():
    assert hasattr(rel2rel::RelatedTo, "since")
    descriptor = None
    for klass in rel2rel::RelatedTo.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_rel2rel::thing_is_not_abstract():
    assert not inspect.isabstract(rel2rel::Thing)


def test_rel2rel::thing_constructor_exists():
    assert callable(rel2rel::Thing.__init__)


def test_rel2rel::thing_constructor_args():
    sig = inspect.signature(rel2rel::Thing.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_rel2rel::thing_has_id():
    assert hasattr(rel2rel::Thing, "id")
    descriptor = None
    for klass in rel2rel::Thing.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
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
rel2rel::World_strategy = st.builds(
    rel2rel::World,
)
Thing_strategy = st.builds(
    Thing,
)
rel2rel::NamedElement_strategy = st.builds(
    rel2rel::NamedElement,
    name=
        safe_text
)
rel2rel::RelatedTo_strategy = st.builds(
    rel2rel::RelatedTo,
    since=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
rel2rel::Thing_strategy = st.builds(
    rel2rel::Thing,
    id=
        st.integers()
)

@given(instance=rel2rel::World_strategy)
@settings(max_examples=50)
def test_rel2rel::world_instantiation(instance):
    assert isinstance(instance, rel2rel::World)

@given(instance=Thing_strategy)
@settings(max_examples=50)
def test_thing_instantiation(instance):
    assert isinstance(instance, Thing)

@given(instance=rel2rel::NamedElement_strategy)
@settings(max_examples=50)
def test_rel2rel::namedelement_instantiation(instance):
    assert isinstance(instance, rel2rel::NamedElement)

@given(instance=rel2rel::NamedElement_strategy)
def test_rel2rel::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rel2rel::NamedElement_strategy)
def test_rel2rel::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rel2rel::RelatedTo_strategy)
@settings(max_examples=50)
def test_rel2rel::relatedto_instantiation(instance):
    assert isinstance(instance, rel2rel::RelatedTo)

@given(instance=rel2rel::RelatedTo_strategy)
def test_rel2rel::relatedto_since_type(instance):
    assert isinstance(instance.since, str)


@given(instance=rel2rel::RelatedTo_strategy)
def test_rel2rel::relatedto_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=rel2rel::Thing_strategy)
@settings(max_examples=50)
def test_rel2rel::thing_instantiation(instance):
    assert isinstance(instance, rel2rel::Thing)

@given(instance=rel2rel::Thing_strategy)
def test_rel2rel::thing_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=rel2rel::Thing_strategy)
def test_rel2rel::thing_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
