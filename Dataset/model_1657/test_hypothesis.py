import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    NamedElement,
    simpleparts_RelatedTo,
    simpleparts_Thing,
    simpleparts_World,
    simpleparts_NamedElement,
    simpleparts_Piece,
    simpleparts_Item,
    simpleparts_Element,
    simpleparts_Part,
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



def test_simpleparts_relatedto_is_not_abstract():
    assert not inspect.isabstract(simpleparts_RelatedTo)


def test_simpleparts_relatedto_constructor_exists():
    assert callable(simpleparts_RelatedTo.__init__)


def test_simpleparts_relatedto_constructor_args():
    sig = inspect.signature(simpleparts_RelatedTo.__init__)
    params = list(sig.parameters.keys())
    assert "since" in params, "Missing parameter 'since'"

def test_simpleparts_relatedto_has_since():
    assert hasattr(simpleparts_RelatedTo, "since")
    descriptor = None
    for klass in simpleparts_RelatedTo.__mro__:
        if "since" in klass.__dict__:
            descriptor = klass.__dict__["since"]
            break
    assert isinstance(descriptor, property)



def test_simpleparts_thing_is_not_abstract():
    assert not inspect.isabstract(simpleparts_Thing)


def test_simpleparts_thing_constructor_exists():
    assert callable(simpleparts_Thing.__init__)


def test_simpleparts_thing_constructor_args():
    sig = inspect.signature(simpleparts_Thing.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_simpleparts_thing_has_id():
    assert hasattr(simpleparts_Thing, "id")
    descriptor = None
    for klass in simpleparts_Thing.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_simpleparts_world_is_not_abstract():
    assert not inspect.isabstract(simpleparts_World)


def test_simpleparts_world_constructor_exists():
    assert callable(simpleparts_World.__init__)


def test_simpleparts_world_constructor_args():
    sig = inspect.signature(simpleparts_World.__init__)
    params = list(sig.parameters.keys())



def test_simpleparts_namedelement_is_not_abstract():
    assert not inspect.isabstract(simpleparts_NamedElement)


def test_simpleparts_namedelement_constructor_exists():
    assert callable(simpleparts_NamedElement.__init__)


def test_simpleparts_namedelement_constructor_args():
    sig = inspect.signature(simpleparts_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simpleparts_namedelement_has_name():
    assert hasattr(simpleparts_NamedElement, "name")
    descriptor = None
    for klass in simpleparts_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simpleparts_piece_is_not_abstract():
    assert not inspect.isabstract(simpleparts_Piece)


def test_simpleparts_piece_constructor_exists():
    assert callable(simpleparts_Piece.__init__)


def test_simpleparts_piece_constructor_args():
    sig = inspect.signature(simpleparts_Piece.__init__)
    params = list(sig.parameters.keys())



def test_simpleparts_item_is_not_abstract():
    assert not inspect.isabstract(simpleparts_Item)


def test_simpleparts_item_constructor_exists():
    assert callable(simpleparts_Item.__init__)


def test_simpleparts_item_constructor_args():
    sig = inspect.signature(simpleparts_Item.__init__)
    params = list(sig.parameters.keys())



def test_simpleparts_element_is_not_abstract():
    assert not inspect.isabstract(simpleparts_Element)


def test_simpleparts_element_constructor_exists():
    assert callable(simpleparts_Element.__init__)


def test_simpleparts_element_constructor_args():
    sig = inspect.signature(simpleparts_Element.__init__)
    params = list(sig.parameters.keys())



def test_simpleparts_part_is_not_abstract():
    assert not inspect.isabstract(simpleparts_Part)


def test_simpleparts_part_constructor_exists():
    assert callable(simpleparts_Part.__init__)


def test_simpleparts_part_constructor_args():
    sig = inspect.signature(simpleparts_Part.__init__)
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
simpleparts_RelatedTo_strategy = st.builds(
    simpleparts_RelatedTo,
    since=
        safe_text
)
simpleparts_Thing_strategy = st.builds(
    simpleparts_Thing,
    id=
        st.integers()
)
simpleparts_World_strategy = st.builds(
    simpleparts_World,
)
simpleparts_NamedElement_strategy = st.builds(
    simpleparts_NamedElement,
    name=
        safe_text
)
simpleparts_Piece_strategy = st.builds(
    simpleparts_Piece,
)
simpleparts_Item_strategy = st.builds(
    simpleparts_Item,
)
simpleparts_Element_strategy = st.builds(
    simpleparts_Element,
)
simpleparts_Part_strategy = st.builds(
    simpleparts_Part,
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=simpleparts_RelatedTo_strategy)
@settings(max_examples=50)
def test_simpleparts_relatedto_instantiation(instance):
    assert isinstance(instance, simpleparts_RelatedTo)



@given(instance=simpleparts_RelatedTo_strategy)
def test_simpleparts_relatedto_since_setter(instance):
    original = instance.since
    instance.since = original
    assert instance.since == original

@given(instance=simpleparts_Thing_strategy)
@settings(max_examples=50)
def test_simpleparts_thing_instantiation(instance):
    assert isinstance(instance, simpleparts_Thing)



@given(instance=simpleparts_Thing_strategy)
def test_simpleparts_thing_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=simpleparts_World_strategy)
@settings(max_examples=50)
def test_simpleparts_world_instantiation(instance):
    assert isinstance(instance, simpleparts_World)

@given(instance=simpleparts_NamedElement_strategy)
@settings(max_examples=50)
def test_simpleparts_namedelement_instantiation(instance):
    assert isinstance(instance, simpleparts_NamedElement)



@given(instance=simpleparts_NamedElement_strategy)
def test_simpleparts_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpleparts_Piece_strategy)
@settings(max_examples=50)
def test_simpleparts_piece_instantiation(instance):
    assert isinstance(instance, simpleparts_Piece)

@given(instance=simpleparts_Item_strategy)
@settings(max_examples=50)
def test_simpleparts_item_instantiation(instance):
    assert isinstance(instance, simpleparts_Item)

@given(instance=simpleparts_Element_strategy)
@settings(max_examples=50)
def test_simpleparts_element_instantiation(instance):
    assert isinstance(instance, simpleparts_Element)

@given(instance=simpleparts_Part_strategy)
@settings(max_examples=50)
def test_simpleparts_part_instantiation(instance):
    assert isinstance(instance, simpleparts_Part)
