import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Arc,
    Element,
    petriNet::Place,
    NamedElement,
    petriNet::Element,
    petriNet::Arc,
    petriNet::PetriNet,
    petriNet::Transition,
    petriNet::PlaceToTransition,
    petriNet::TransitionToPlace,
    LocatedElement,
    petriNet::NamedElement,
    petriNet::LocatedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_arc_is_not_abstract():
    assert not inspect.isabstract(Arc)


def test_arc_constructor_exists():
    assert callable(Arc.__init__)


def test_arc_constructor_args():
    sig = inspect.signature(Arc.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::place_is_not_abstract():
    assert not inspect.isabstract(petriNet::Place)


def test_petrinet::place_constructor_exists():
    assert callable(petriNet::Place.__init__)


def test_petrinet::place_constructor_args():
    sig = inspect.signature(petriNet::Place.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::element_is_not_abstract():
    assert not inspect.isabstract(petriNet::Element)


def test_petrinet::element_constructor_exists():
    assert callable(petriNet::Element.__init__)


def test_petrinet::element_constructor_args():
    sig = inspect.signature(petriNet::Element.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::arc_is_not_abstract():
    assert not inspect.isabstract(petriNet::Arc)


def test_petrinet::arc_constructor_exists():
    assert callable(petriNet::Arc.__init__)


def test_petrinet::arc_constructor_args():
    sig = inspect.signature(petriNet::Arc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_petrinet::arc_has_weight():
    assert hasattr(petriNet::Arc, "weight")
    descriptor = None
    for klass in petriNet::Arc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::petrinet_is_not_abstract():
    assert not inspect.isabstract(petriNet::PetriNet)


def test_petrinet::petrinet_constructor_exists():
    assert callable(petriNet::PetriNet.__init__)


def test_petrinet::petrinet_constructor_args():
    sig = inspect.signature(petriNet::PetriNet.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::transition_is_not_abstract():
    assert not inspect.isabstract(petriNet::Transition)


def test_petrinet::transition_constructor_exists():
    assert callable(petriNet::Transition.__init__)


def test_petrinet::transition_constructor_args():
    sig = inspect.signature(petriNet::Transition.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::placetotransition_is_not_abstract():
    assert not inspect.isabstract(petriNet::PlaceToTransition)


def test_petrinet::placetotransition_constructor_exists():
    assert callable(petriNet::PlaceToTransition.__init__)


def test_petrinet::placetotransition_constructor_args():
    sig = inspect.signature(petriNet::PlaceToTransition.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::transitiontoplace_is_not_abstract():
    assert not inspect.isabstract(petriNet::TransitionToPlace)


def test_petrinet::transitiontoplace_constructor_exists():
    assert callable(petriNet::TransitionToPlace.__init__)


def test_petrinet::transitiontoplace_constructor_args():
    sig = inspect.signature(petriNet::TransitionToPlace.__init__)
    params = list(sig.parameters.keys())



def test_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::namedelement_is_not_abstract():
    assert not inspect.isabstract(petriNet::NamedElement)


def test_petrinet::namedelement_constructor_exists():
    assert callable(petriNet::NamedElement.__init__)


def test_petrinet::namedelement_constructor_args():
    sig = inspect.signature(petriNet::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::namedelement_has_name():
    assert hasattr(petriNet::NamedElement, "name")
    descriptor = None
    for klass in petriNet::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::locatedelement_is_not_abstract():
    assert not inspect.isabstract(petriNet::LocatedElement)


def test_petrinet::locatedelement_constructor_exists():
    assert callable(petriNet::LocatedElement.__init__)


def test_petrinet::locatedelement_constructor_args():
    sig = inspect.signature(petriNet::LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_petrinet::locatedelement_has_location():
    assert hasattr(petriNet::LocatedElement, "location")
    descriptor = None
    for klass in petriNet::LocatedElement.__mro__:
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
Arc_strategy = st.builds(
    Arc,
)
Element_strategy = st.builds(
    Element,
)
petriNet::Place_strategy = st.builds(
    petriNet::Place,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
petriNet::Element_strategy = st.builds(
    petriNet::Element,
)
petriNet::Arc_strategy = st.builds(
    petriNet::Arc,
    weight=
        st.integers()
)
petriNet::PetriNet_strategy = st.builds(
    petriNet::PetriNet,
)
petriNet::Transition_strategy = st.builds(
    petriNet::Transition,
)
petriNet::PlaceToTransition_strategy = st.builds(
    petriNet::PlaceToTransition,
)
petriNet::TransitionToPlace_strategy = st.builds(
    petriNet::TransitionToPlace,
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
petriNet::NamedElement_strategy = st.builds(
    petriNet::NamedElement,
    name=
        safe_text
)
petriNet::LocatedElement_strategy = st.builds(
    petriNet::LocatedElement,
    location=
        safe_text
)

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=petriNet::Place_strategy)
@settings(max_examples=50)
def test_petrinet::place_instantiation(instance):
    assert isinstance(instance, petriNet::Place)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=petriNet::Element_strategy)
@settings(max_examples=50)
def test_petrinet::element_instantiation(instance):
    assert isinstance(instance, petriNet::Element)

@given(instance=petriNet::Arc_strategy)
@settings(max_examples=50)
def test_petrinet::arc_instantiation(instance):
    assert isinstance(instance, petriNet::Arc)

@given(instance=petriNet::Arc_strategy)
def test_petrinet::arc_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=petriNet::Arc_strategy)
def test_petrinet::arc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=petriNet::PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet::petrinet_instantiation(instance):
    assert isinstance(instance, petriNet::PetriNet)

@given(instance=petriNet::Transition_strategy)
@settings(max_examples=50)
def test_petrinet::transition_instantiation(instance):
    assert isinstance(instance, petriNet::Transition)

@given(instance=petriNet::PlaceToTransition_strategy)
@settings(max_examples=50)
def test_petrinet::placetotransition_instantiation(instance):
    assert isinstance(instance, petriNet::PlaceToTransition)

@given(instance=petriNet::TransitionToPlace_strategy)
@settings(max_examples=50)
def test_petrinet::transitiontoplace_instantiation(instance):
    assert isinstance(instance, petriNet::TransitionToPlace)

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=petriNet::NamedElement_strategy)
@settings(max_examples=50)
def test_petrinet::namedelement_instantiation(instance):
    assert isinstance(instance, petriNet::NamedElement)

@given(instance=petriNet::NamedElement_strategy)
def test_petrinet::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petriNet::NamedElement_strategy)
def test_petrinet::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petriNet::LocatedElement_strategy)
@settings(max_examples=50)
def test_petrinet::locatedelement_instantiation(instance):
    assert isinstance(instance, petriNet::LocatedElement)

@given(instance=petriNet::LocatedElement_strategy)
def test_petrinet::locatedelement_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=petriNet::LocatedElement_strategy)
def test_petrinet::locatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original
