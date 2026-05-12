import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    pnml_Element,
    pnml_PNMLDocument,
    Element,
    pnml_ArcPlace2Transition,
    pnml_NetElement,
    pnml_ArcTransition2Place,
    pnml_TransitionElement,
    pnml_PlaceElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_pnml_element_is_not_abstract():
    assert not inspect.isabstract(pnml_Element)


def test_pnml_element_constructor_exists():
    assert callable(pnml_Element.__init__)


def test_pnml_element_constructor_args():
    sig = inspect.signature(pnml_Element.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "id" in params, "Missing parameter 'id'"

def test_pnml_element_has_location():
    assert hasattr(pnml_Element, "location")
    descriptor = None
    for klass in pnml_Element.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_pnml_element_has_id():
    assert hasattr(pnml_Element, "id")
    descriptor = None
    for klass in pnml_Element.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_pnml_pnmldocument_is_not_abstract():
    assert not inspect.isabstract(pnml_PNMLDocument)


def test_pnml_pnmldocument_constructor_exists():
    assert callable(pnml_PNMLDocument.__init__)


def test_pnml_pnmldocument_constructor_args():
    sig = inspect.signature(pnml_PNMLDocument.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_pnml_pnmldocument_has_location():
    assert hasattr(pnml_PNMLDocument, "location")
    descriptor = None
    for klass in pnml_PNMLDocument.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_pnml_arcplace2transition_is_not_abstract():
    assert not inspect.isabstract(pnml_ArcPlace2Transition)


def test_pnml_arcplace2transition_constructor_exists():
    assert callable(pnml_ArcPlace2Transition.__init__)


def test_pnml_arcplace2transition_constructor_args():
    sig = inspect.signature(pnml_ArcPlace2Transition.__init__)
    params = list(sig.parameters.keys())



def test_pnml_netelement_is_not_abstract():
    assert not inspect.isabstract(pnml_NetElement)


def test_pnml_netelement_constructor_exists():
    assert callable(pnml_NetElement.__init__)


def test_pnml_netelement_constructor_args():
    sig = inspect.signature(pnml_NetElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pnml_netelement_has_name():
    assert hasattr(pnml_NetElement, "name")
    descriptor = None
    for klass in pnml_NetElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pnml_arctransition2place_is_not_abstract():
    assert not inspect.isabstract(pnml_ArcTransition2Place)


def test_pnml_arctransition2place_constructor_exists():
    assert callable(pnml_ArcTransition2Place.__init__)


def test_pnml_arctransition2place_constructor_args():
    sig = inspect.signature(pnml_ArcTransition2Place.__init__)
    params = list(sig.parameters.keys())



def test_pnml_transitionelement_is_not_abstract():
    assert not inspect.isabstract(pnml_TransitionElement)


def test_pnml_transitionelement_constructor_exists():
    assert callable(pnml_TransitionElement.__init__)


def test_pnml_transitionelement_constructor_args():
    sig = inspect.signature(pnml_TransitionElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_pnml_transitionelement_has_name():
    assert hasattr(pnml_TransitionElement, "name")
    descriptor = None
    for klass in pnml_TransitionElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_pnml_placeelement_is_not_abstract():
    assert not inspect.isabstract(pnml_PlaceElement)


def test_pnml_placeelement_constructor_exists():
    assert callable(pnml_PlaceElement.__init__)


def test_pnml_placeelement_constructor_args():
    sig = inspect.signature(pnml_PlaceElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "tokens" in params, "Missing parameter 'tokens'"

def test_pnml_placeelement_has_name():
    assert hasattr(pnml_PlaceElement, "name")
    descriptor = None
    for klass in pnml_PlaceElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_pnml_placeelement_has_tokens():
    assert hasattr(pnml_PlaceElement, "tokens")
    descriptor = None
    for klass in pnml_PlaceElement.__mro__:
        if "tokens" in klass.__dict__:
            descriptor = klass.__dict__["tokens"]
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
pnml_Element_strategy = st.builds(
    pnml_Element,
    location=
        safe_text,
    id=
        safe_text
)
pnml_PNMLDocument_strategy = st.builds(
    pnml_PNMLDocument,
    location=
        safe_text
)
Element_strategy = st.builds(
    Element,
)
pnml_ArcPlace2Transition_strategy = st.builds(
    pnml_ArcPlace2Transition,
)
pnml_NetElement_strategy = st.builds(
    pnml_NetElement,
    name=
        safe_text
)
pnml_ArcTransition2Place_strategy = st.builds(
    pnml_ArcTransition2Place,
)
pnml_TransitionElement_strategy = st.builds(
    pnml_TransitionElement,
    name=
        safe_text
)
pnml_PlaceElement_strategy = st.builds(
    pnml_PlaceElement,
    name=
        safe_text,
    tokens=
        st.integers()
)

@given(instance=pnml_Element_strategy)
@settings(max_examples=50)
def test_pnml_element_instantiation(instance):
    assert isinstance(instance, pnml_Element)



@given(instance=pnml_Element_strategy)
def test_pnml_element_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=pnml_Element_strategy)
def test_pnml_element_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=pnml_PNMLDocument_strategy)
@settings(max_examples=50)
def test_pnml_pnmldocument_instantiation(instance):
    assert isinstance(instance, pnml_PNMLDocument)



@given(instance=pnml_PNMLDocument_strategy)
def test_pnml_pnmldocument_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=pnml_ArcPlace2Transition_strategy)
@settings(max_examples=50)
def test_pnml_arcplace2transition_instantiation(instance):
    assert isinstance(instance, pnml_ArcPlace2Transition)

@given(instance=pnml_NetElement_strategy)
@settings(max_examples=50)
def test_pnml_netelement_instantiation(instance):
    assert isinstance(instance, pnml_NetElement)



@given(instance=pnml_NetElement_strategy)
def test_pnml_netelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pnml_ArcTransition2Place_strategy)
@settings(max_examples=50)
def test_pnml_arctransition2place_instantiation(instance):
    assert isinstance(instance, pnml_ArcTransition2Place)

@given(instance=pnml_TransitionElement_strategy)
@settings(max_examples=50)
def test_pnml_transitionelement_instantiation(instance):
    assert isinstance(instance, pnml_TransitionElement)



@given(instance=pnml_TransitionElement_strategy)
def test_pnml_transitionelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=pnml_PlaceElement_strategy)
@settings(max_examples=50)
def test_pnml_placeelement_instantiation(instance):
    assert isinstance(instance, pnml_PlaceElement)



@given(instance=pnml_PlaceElement_strategy)
def test_pnml_placeelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=pnml_PlaceElement_strategy)
def test_pnml_placeelement_tokens_setter(instance):
    original = instance.tokens
    instance.tokens = original
    assert instance.tokens == original
