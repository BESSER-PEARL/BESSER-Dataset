import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    pnml::Element,
    Element,
    pnml::ArcTransition2Place,
    pnml::TransitionElement,
    pnml::PlaceElement,
    pnml::ArcPlace2Transition,
    pnml::NetElement,
    pnml::PNMLDocument,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_pnml::element_is_not_abstract():
    assert not inspect.isabstract(pnml::Element)


def test_pnml::element_constructor_exists():
    assert callable(pnml::Element.__init__)


def test_pnml::element_constructor_args():
    sig = inspect.signature(pnml::Element.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "id" in params, "Missing parameter 'id'"

def test_pnml::element_has_location():
    assert hasattr(pnml::Element, "location")
    descriptor = None
    for klass in pnml::Element.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_pnml::element_has_id():
    assert hasattr(pnml::Element, "id")
    descriptor = None
    for klass in pnml::Element.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_pnml::arctransition2place_is_not_abstract():
    assert not inspect.isabstract(pnml::ArcTransition2Place)


def test_pnml::arctransition2place_constructor_exists():
    assert callable(pnml::ArcTransition2Place.__init__)


def test_pnml::arctransition2place_constructor_args():
    sig = inspect.signature(pnml::ArcTransition2Place.__init__)
    params = list(sig.parameters.keys())



def test_pnml::transitionelement_is_not_abstract():
    assert not inspect.isabstract(pnml::TransitionElement)


def test_pnml::transitionelement_constructor_exists():
    assert callable(pnml::TransitionElement.__init__)


def test_pnml::transitionelement_constructor_args():
    sig = inspect.signature(pnml::TransitionElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pnml::transitionelement_has_name():
    assert hasattr(pnml::TransitionElement, "name")
    descriptor = None
    for klass in pnml::TransitionElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pnml::placeelement_is_not_abstract():
    assert not inspect.isabstract(pnml::PlaceElement)


def test_pnml::placeelement_constructor_exists():
    assert callable(pnml::PlaceElement.__init__)


def test_pnml::placeelement_constructor_args():
    sig = inspect.signature(pnml::PlaceElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "tokens" in params, "Missing parameter 'tokens'"

def test_pnml::placeelement_has_name():
    assert hasattr(pnml::PlaceElement, "name")
    descriptor = None
    for klass in pnml::PlaceElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_pnml::placeelement_has_tokens():
    assert hasattr(pnml::PlaceElement, "tokens")
    descriptor = None
    for klass in pnml::PlaceElement.__mro__:
        if "tokens" in klass.__dict__:
            descriptor = klass.__dict__["tokens"]
            break
    assert isinstance(descriptor, property)



def test_pnml::arcplace2transition_is_not_abstract():
    assert not inspect.isabstract(pnml::ArcPlace2Transition)


def test_pnml::arcplace2transition_constructor_exists():
    assert callable(pnml::ArcPlace2Transition.__init__)


def test_pnml::arcplace2transition_constructor_args():
    sig = inspect.signature(pnml::ArcPlace2Transition.__init__)
    params = list(sig.parameters.keys())



def test_pnml::netelement_is_not_abstract():
    assert not inspect.isabstract(pnml::NetElement)


def test_pnml::netelement_constructor_exists():
    assert callable(pnml::NetElement.__init__)


def test_pnml::netelement_constructor_args():
    sig = inspect.signature(pnml::NetElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pnml::netelement_has_name():
    assert hasattr(pnml::NetElement, "name")
    descriptor = None
    for klass in pnml::NetElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pnml::pnmldocument_is_not_abstract():
    assert not inspect.isabstract(pnml::PNMLDocument)


def test_pnml::pnmldocument_constructor_exists():
    assert callable(pnml::PNMLDocument.__init__)


def test_pnml::pnmldocument_constructor_args():
    sig = inspect.signature(pnml::PNMLDocument.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_pnml::pnmldocument_has_location():
    assert hasattr(pnml::PNMLDocument, "location")
    descriptor = None
    for klass in pnml::PNMLDocument.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
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
pnml::Element_strategy = st.builds(
    pnml::Element,
    location=
        safe_text,
    id=
        safe_text
)
Element_strategy = st.builds(
    Element,
)
pnml::ArcTransition2Place_strategy = st.builds(
    pnml::ArcTransition2Place,
)
pnml::TransitionElement_strategy = st.builds(
    pnml::TransitionElement,
    name=
        safe_text
)
pnml::PlaceElement_strategy = st.builds(
    pnml::PlaceElement,
    name=
        safe_text,
    tokens=
        st.integers()
)
pnml::ArcPlace2Transition_strategy = st.builds(
    pnml::ArcPlace2Transition,
)
pnml::NetElement_strategy = st.builds(
    pnml::NetElement,
    name=
        safe_text
)
pnml::PNMLDocument_strategy = st.builds(
    pnml::PNMLDocument,
    location=
        safe_text
)

@given(instance=pnml::Element_strategy)
@settings(max_examples=50)
def test_pnml::element_instantiation(instance):
    assert isinstance(instance, pnml::Element)

@given(instance=pnml::Element_strategy)
def test_pnml::element_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=pnml::Element_strategy)
def test_pnml::element_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=pnml::Element_strategy)
def test_pnml::element_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=pnml::Element_strategy)
def test_pnml::element_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=pnml::ArcTransition2Place_strategy)
@settings(max_examples=50)
def test_pnml::arctransition2place_instantiation(instance):
    assert isinstance(instance, pnml::ArcTransition2Place)

@given(instance=pnml::TransitionElement_strategy)
@settings(max_examples=50)
def test_pnml::transitionelement_instantiation(instance):
    assert isinstance(instance, pnml::TransitionElement)

@given(instance=pnml::TransitionElement_strategy)
def test_pnml::transitionelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=pnml::TransitionElement_strategy)
def test_pnml::transitionelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pnml::PlaceElement_strategy)
@settings(max_examples=50)
def test_pnml::placeelement_instantiation(instance):
    assert isinstance(instance, pnml::PlaceElement)

@given(instance=pnml::PlaceElement_strategy)
def test_pnml::placeelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=pnml::PlaceElement_strategy)
def test_pnml::placeelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pnml::PlaceElement_strategy)
def test_pnml::placeelement_tokens_type(instance):
    assert isinstance(instance.tokens, int)


@given(instance=pnml::PlaceElement_strategy)
def test_pnml::placeelement_tokens_setter(instance):
    original = instance.tokens
    instance.tokens = original
    assert instance.tokens == original

@given(instance=pnml::ArcPlace2Transition_strategy)
@settings(max_examples=50)
def test_pnml::arcplace2transition_instantiation(instance):
    assert isinstance(instance, pnml::ArcPlace2Transition)

@given(instance=pnml::NetElement_strategy)
@settings(max_examples=50)
def test_pnml::netelement_instantiation(instance):
    assert isinstance(instance, pnml::NetElement)

@given(instance=pnml::NetElement_strategy)
def test_pnml::netelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=pnml::NetElement_strategy)
def test_pnml::netelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pnml::PNMLDocument_strategy)
@settings(max_examples=50)
def test_pnml::pnmldocument_instantiation(instance):
    assert isinstance(instance, pnml::PNMLDocument)

@given(instance=pnml::PNMLDocument_strategy)
def test_pnml::pnmldocument_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=pnml::PNMLDocument_strategy)
def test_pnml::pnmldocument_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original
