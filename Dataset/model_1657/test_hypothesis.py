import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    NamedElement,
    simpleparts::RelatedTo,
    simpleparts::Thing,
    simpleparts::World,
    simpleparts::NamedElement,
    simpleparts::Piece,
    simpleparts::Item,
    simpleparts::Element,
    simpleparts::Part,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_simpleparts::relatedto_is_not_abstract():
    assert not inspect.isabstract(simpleparts::RelatedTo)


def test_simpleparts::relatedto_constructor_exists():
    assert callable(simpleparts::RelatedTo.__init__)


def test_simpleparts::relatedto_constructor_args():
    sig = inspect.signature(simpleparts::RelatedTo.__init__)
    params = list(sig.parameters.keys())
    assert "since" in params, "Missing parameter 'since'"

def test_simpleparts::relatedto_has_since():
    assert hasattr(simpleparts::RelatedTo, "since")
    descriptor = None
    for klass in simpleparts::RelatedTo.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
            break
    assert isinstance(descriptor, property)



def test_simpleparts::thing_is_not_abstract():
    assert not inspect.isabstract(simpleparts::Thing)


def test_simpleparts::thing_constructor_exists():
    assert callable(simpleparts::Thing.__init__)


def test_simpleparts::thing_constructor_args():
    sig = inspect.signature(simpleparts::Thing.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_simpleparts::thing_has_id():
    assert hasattr(simpleparts::Thing, "id")
    descriptor = None
    for klass in simpleparts::Thing.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_simpleparts::world_is_not_abstract():
    assert not inspect.isabstract(simpleparts::World)


def test_simpleparts::world_constructor_exists():
    assert callable(simpleparts::World.__init__)


def test_simpleparts::world_constructor_args():
    sig = inspect.signature(simpleparts::World.__init__)
    params = list(sig.parameters.keys())



def test_simpleparts::namedelement_is_not_abstract():
    assert not inspect.isabstract(simpleparts::NamedElement)


def test_simpleparts::namedelement_constructor_exists():
    assert callable(simpleparts::NamedElement.__init__)


def test_simpleparts::namedelement_constructor_args():
    sig = inspect.signature(simpleparts::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleparts::namedelement_has_name():
    assert hasattr(simpleparts::NamedElement, "name")
    descriptor = None
    for klass in simpleparts::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simpleparts::piece_is_not_abstract():
    assert not inspect.isabstract(simpleparts::Piece)


def test_simpleparts::piece_constructor_exists():
    assert callable(simpleparts::Piece.__init__)


def test_simpleparts::piece_constructor_args():
    sig = inspect.signature(simpleparts::Piece.__init__)
    params = list(sig.parameters.keys())



def test_simpleparts::item_is_not_abstract():
    assert not inspect.isabstract(simpleparts::Item)


def test_simpleparts::item_constructor_exists():
    assert callable(simpleparts::Item.__init__)


def test_simpleparts::item_constructor_args():
    sig = inspect.signature(simpleparts::Item.__init__)
    params = list(sig.parameters.keys())



def test_simpleparts::element_is_not_abstract():
    assert not inspect.isabstract(simpleparts::Element)


def test_simpleparts::element_constructor_exists():
    assert callable(simpleparts::Element.__init__)


def test_simpleparts::element_constructor_args():
    sig = inspect.signature(simpleparts::Element.__init__)
    params = list(sig.parameters.keys())



def test_simpleparts::part_is_not_abstract():
    assert not inspect.isabstract(simpleparts::Part)


def test_simpleparts::part_constructor_exists():
    assert callable(simpleparts::Part.__init__)


def test_simpleparts::part_constructor_args():
    sig = inspect.signature(simpleparts::Part.__init__)
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
NamedElement_strategy = st.builds(
    NamedElement,
)
simpleparts::RelatedTo_strategy = st.builds(
    simpleparts::RelatedTo,
    since=
        safe_text
)
simpleparts::Thing_strategy = st.builds(
    simpleparts::Thing,
    id=
        st.integers()
)
simpleparts::World_strategy = st.builds(
    simpleparts::World,
)
simpleparts::NamedElement_strategy = st.builds(
    simpleparts::NamedElement,
    name=
        safe_text
)
simpleparts::Piece_strategy = st.builds(
    simpleparts::Piece,
)
simpleparts::Item_strategy = st.builds(
    simpleparts::Item,
)
simpleparts::Element_strategy = st.builds(
    simpleparts::Element,
)
simpleparts::Part_strategy = st.builds(
    simpleparts::Part,
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=simpleparts::RelatedTo_strategy)
@settings(max_examples=50)
def test_simpleparts::relatedto_instantiation(instance):
    assert isinstance(instance, simpleparts::RelatedTo)

@given(instance=simpleparts::RelatedTo_strategy)
def test_simpleparts::relatedto_since_type(instance):
    assert isinstance(instance.since, str)


@given(instance=simpleparts::RelatedTo_strategy)
def test_simpleparts::relatedto_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original

@given(instance=simpleparts::Thing_strategy)
@settings(max_examples=50)
def test_simpleparts::thing_instantiation(instance):
    assert isinstance(instance, simpleparts::Thing)

@given(instance=simpleparts::Thing_strategy)
def test_simpleparts::thing_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=simpleparts::Thing_strategy)
def test_simpleparts::thing_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=simpleparts::World_strategy)
@settings(max_examples=50)
def test_simpleparts::world_instantiation(instance):
    assert isinstance(instance, simpleparts::World)

@given(instance=simpleparts::NamedElement_strategy)
@settings(max_examples=50)
def test_simpleparts::namedelement_instantiation(instance):
    assert isinstance(instance, simpleparts::NamedElement)

@given(instance=simpleparts::NamedElement_strategy)
def test_simpleparts::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpleparts::NamedElement_strategy)
def test_simpleparts::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpleparts::Piece_strategy)
@settings(max_examples=50)
def test_simpleparts::piece_instantiation(instance):
    assert isinstance(instance, simpleparts::Piece)

@given(instance=simpleparts::Item_strategy)
@settings(max_examples=50)
def test_simpleparts::item_instantiation(instance):
    assert isinstance(instance, simpleparts::Item)

@given(instance=simpleparts::Element_strategy)
@settings(max_examples=50)
def test_simpleparts::element_instantiation(instance):
    assert isinstance(instance, simpleparts::Element)

@given(instance=simpleparts::Part_strategy)
@settings(max_examples=50)
def test_simpleparts::part_instantiation(instance):
    assert isinstance(instance, simpleparts::Part)
