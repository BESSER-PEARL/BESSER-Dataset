import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Arc,
    NamedElement,
    PetriNet::Element,
    PetriNet::PetriNet,
    LocatedElement,
    PetriNet::NamedElement,
    PetriNet::LocatedElement,
    PetriNet::PlaceToTransition,
    PetriNet::TransitionToPlace,
    Element,
    PetriNet::Transition,
    PetriNet::Place,
    PetriNet::Arc,
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



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::element_is_not_abstract():
    assert not inspect.isabstract(PetriNet::Element)


def test_petrinet::element_constructor_exists():
    assert callable(PetriNet::Element.__init__)


def test_petrinet::element_constructor_args():
    sig = inspect.signature(PetriNet::Element.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::petrinet_is_not_abstract():
    assert not inspect.isabstract(PetriNet::PetriNet)


def test_petrinet::petrinet_constructor_exists():
    assert callable(PetriNet::PetriNet.__init__)


def test_petrinet::petrinet_constructor_args():
    sig = inspect.signature(PetriNet::PetriNet.__init__)
    params = list(sig.parameters.keys())



def test_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::namedelement_is_not_abstract():
    assert not inspect.isabstract(PetriNet::NamedElement)


def test_petrinet::namedelement_constructor_exists():
    assert callable(PetriNet::NamedElement.__init__)


def test_petrinet::namedelement_constructor_args():
    sig = inspect.signature(PetriNet::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::namedelement_has_name():
    assert hasattr(PetriNet::NamedElement, "name")
    descriptor = None
    for klass in PetriNet::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::locatedelement_is_not_abstract():
    assert not inspect.isabstract(PetriNet::LocatedElement)


def test_petrinet::locatedelement_constructor_exists():
    assert callable(PetriNet::LocatedElement.__init__)


def test_petrinet::locatedelement_constructor_args():
    sig = inspect.signature(PetriNet::LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_petrinet::locatedelement_has_location():
    assert hasattr(PetriNet::LocatedElement, "location")
    descriptor = None
    for klass in PetriNet::LocatedElement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::placetotransition_is_not_abstract():
    assert not inspect.isabstract(PetriNet::PlaceToTransition)


def test_petrinet::placetotransition_constructor_exists():
    assert callable(PetriNet::PlaceToTransition.__init__)


def test_petrinet::placetotransition_constructor_args():
    sig = inspect.signature(PetriNet::PlaceToTransition.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::transitiontoplace_is_not_abstract():
    assert not inspect.isabstract(PetriNet::TransitionToPlace)


def test_petrinet::transitiontoplace_constructor_exists():
    assert callable(PetriNet::TransitionToPlace.__init__)


def test_petrinet::transitiontoplace_constructor_args():
    sig = inspect.signature(PetriNet::TransitionToPlace.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::transition_is_not_abstract():
    assert not inspect.isabstract(PetriNet::Transition)


def test_petrinet::transition_constructor_exists():
    assert callable(PetriNet::Transition.__init__)


def test_petrinet::transition_constructor_args():
    sig = inspect.signature(PetriNet::Transition.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::place_is_not_abstract():
    assert not inspect.isabstract(PetriNet::Place)


def test_petrinet::place_constructor_exists():
    assert callable(PetriNet::Place.__init__)


def test_petrinet::place_constructor_args():
    sig = inspect.signature(PetriNet::Place.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::arc_is_not_abstract():
    assert not inspect.isabstract(PetriNet::Arc)


def test_petrinet::arc_constructor_exists():
    assert callable(PetriNet::Arc.__init__)


def test_petrinet::arc_constructor_args():
    sig = inspect.signature(PetriNet::Arc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_petrinet::arc_has_weight():
    assert hasattr(PetriNet::Arc, "weight")
    descriptor = None
    for klass in PetriNet::Arc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
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
NamedElement_strategy = st.builds(
    NamedElement,
)
PetriNet::Element_strategy = st.builds(
    PetriNet::Element,
)
PetriNet::PetriNet_strategy = st.builds(
    PetriNet::PetriNet,
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
PetriNet::NamedElement_strategy = st.builds(
    PetriNet::NamedElement,
    name=
        safe_text
)
PetriNet::LocatedElement_strategy = st.builds(
    PetriNet::LocatedElement,
    location=
        safe_text
)
PetriNet::PlaceToTransition_strategy = st.builds(
    PetriNet::PlaceToTransition,
)
PetriNet::TransitionToPlace_strategy = st.builds(
    PetriNet::TransitionToPlace,
)
Element_strategy = st.builds(
    Element,
)
PetriNet::Transition_strategy = st.builds(
    PetriNet::Transition,
)
PetriNet::Place_strategy = st.builds(
    PetriNet::Place,
)
PetriNet::Arc_strategy = st.builds(
    PetriNet::Arc,
    weight=
        st.integers()
)

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=PetriNet::Element_strategy)
@settings(max_examples=50)
def test_petrinet::element_instantiation(instance):
    assert isinstance(instance, PetriNet::Element)

@given(instance=PetriNet::PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet::petrinet_instantiation(instance):
    assert isinstance(instance, PetriNet::PetriNet)

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=PetriNet::NamedElement_strategy)
@settings(max_examples=50)
def test_petrinet::namedelement_instantiation(instance):
    assert isinstance(instance, PetriNet::NamedElement)

@given(instance=PetriNet::NamedElement_strategy)
def test_petrinet::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=PetriNet::NamedElement_strategy)
def test_petrinet::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PetriNet::LocatedElement_strategy)
@settings(max_examples=50)
def test_petrinet::locatedelement_instantiation(instance):
    assert isinstance(instance, PetriNet::LocatedElement)

@given(instance=PetriNet::LocatedElement_strategy)
def test_petrinet::locatedelement_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=PetriNet::LocatedElement_strategy)
def test_petrinet::locatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=PetriNet::PlaceToTransition_strategy)
@settings(max_examples=50)
def test_petrinet::placetotransition_instantiation(instance):
    assert isinstance(instance, PetriNet::PlaceToTransition)

@given(instance=PetriNet::TransitionToPlace_strategy)
@settings(max_examples=50)
def test_petrinet::transitiontoplace_instantiation(instance):
    assert isinstance(instance, PetriNet::TransitionToPlace)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=PetriNet::Transition_strategy)
@settings(max_examples=50)
def test_petrinet::transition_instantiation(instance):
    assert isinstance(instance, PetriNet::Transition)

@given(instance=PetriNet::Place_strategy)
@settings(max_examples=50)
def test_petrinet::place_instantiation(instance):
    assert isinstance(instance, PetriNet::Place)

@given(instance=PetriNet::Arc_strategy)
@settings(max_examples=50)
def test_petrinet::arc_instantiation(instance):
    assert isinstance(instance, PetriNet::Arc)

@given(instance=PetriNet::Arc_strategy)
def test_petrinet::arc_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=PetriNet::Arc_strategy)
def test_petrinet::arc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original
