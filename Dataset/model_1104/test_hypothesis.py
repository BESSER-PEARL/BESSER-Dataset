import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Arc,
    evoPetrinet::TransitionToPlace,
    evoPetrinet::PlaceToTransition,
    PlaceToTransition,
    TransitionToPlace,
    Element,
    evoPetrinet::Place,
    evoPetrinet::Transition,
    evoPetrinet::Arc,
    Transition,
    Place,
    LocatedElement,
    evoPetrinet::NamedElement,
    evoPetrinet::LocatedElement,
    PetriNet,
    evoPetrinet::PetriNetModel,
    NamedElement,
    evoPetrinet::Element,
    evoPetrinet::PetriNet,
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



def test_evopetrinet::transitiontoplace_is_not_abstract():
    assert not inspect.isabstract(evoPetrinet::TransitionToPlace)


def test_evopetrinet::transitiontoplace_constructor_exists():
    assert callable(evoPetrinet::TransitionToPlace.__init__)


def test_evopetrinet::transitiontoplace_constructor_args():
    sig = inspect.signature(evoPetrinet::TransitionToPlace.__init__)
    params = list(sig.parameters.keys())



def test_evopetrinet::placetotransition_is_not_abstract():
    assert not inspect.isabstract(evoPetrinet::PlaceToTransition)


def test_evopetrinet::placetotransition_constructor_exists():
    assert callable(evoPetrinet::PlaceToTransition.__init__)


def test_evopetrinet::placetotransition_constructor_args():
    sig = inspect.signature(evoPetrinet::PlaceToTransition.__init__)
    params = list(sig.parameters.keys())



def test_placetotransition_is_not_abstract():
    assert not inspect.isabstract(PlaceToTransition)


def test_placetotransition_constructor_exists():
    assert callable(PlaceToTransition.__init__)


def test_placetotransition_constructor_args():
    sig = inspect.signature(PlaceToTransition.__init__)
    params = list(sig.parameters.keys())



def test_transitiontoplace_is_not_abstract():
    assert not inspect.isabstract(TransitionToPlace)


def test_transitiontoplace_constructor_exists():
    assert callable(TransitionToPlace.__init__)


def test_transitiontoplace_constructor_args():
    sig = inspect.signature(TransitionToPlace.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_evopetrinet::place_is_not_abstract():
    assert not inspect.isabstract(evoPetrinet::Place)


def test_evopetrinet::place_constructor_exists():
    assert callable(evoPetrinet::Place.__init__)


def test_evopetrinet::place_constructor_args():
    sig = inspect.signature(evoPetrinet::Place.__init__)
    params = list(sig.parameters.keys())



def test_evopetrinet::transition_is_not_abstract():
    assert not inspect.isabstract(evoPetrinet::Transition)


def test_evopetrinet::transition_constructor_exists():
    assert callable(evoPetrinet::Transition.__init__)


def test_evopetrinet::transition_constructor_args():
    sig = inspect.signature(evoPetrinet::Transition.__init__)
    params = list(sig.parameters.keys())



def test_evopetrinet::arc_is_not_abstract():
    assert not inspect.isabstract(evoPetrinet::Arc)


def test_evopetrinet::arc_constructor_exists():
    assert callable(evoPetrinet::Arc.__init__)


def test_evopetrinet::arc_constructor_args():
    sig = inspect.signature(evoPetrinet::Arc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_evopetrinet::arc_has_weight():
    assert hasattr(evoPetrinet::Arc, "weight")
    descriptor = None
    for klass in evoPetrinet::Arc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_place_is_not_abstract():
    assert not inspect.isabstract(Place)


def test_place_constructor_exists():
    assert callable(Place.__init__)


def test_place_constructor_args():
    sig = inspect.signature(Place.__init__)
    params = list(sig.parameters.keys())



def test_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_evopetrinet::namedelement_is_not_abstract():
    assert not inspect.isabstract(evoPetrinet::NamedElement)


def test_evopetrinet::namedelement_constructor_exists():
    assert callable(evoPetrinet::NamedElement.__init__)


def test_evopetrinet::namedelement_constructor_args():
    sig = inspect.signature(evoPetrinet::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_evopetrinet::namedelement_has_name():
    assert hasattr(evoPetrinet::NamedElement, "name")
    descriptor = None
    for klass in evoPetrinet::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_evopetrinet::locatedelement_is_not_abstract():
    assert not inspect.isabstract(evoPetrinet::LocatedElement)


def test_evopetrinet::locatedelement_constructor_exists():
    assert callable(evoPetrinet::LocatedElement.__init__)


def test_evopetrinet::locatedelement_constructor_args():
    sig = inspect.signature(evoPetrinet::LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_evopetrinet::locatedelement_has_location():
    assert hasattr(evoPetrinet::LocatedElement, "location")
    descriptor = None
    for klass in evoPetrinet::LocatedElement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_is_not_abstract():
    assert not inspect.isabstract(PetriNet)


def test_petrinet_constructor_exists():
    assert callable(PetriNet.__init__)


def test_petrinet_constructor_args():
    sig = inspect.signature(PetriNet.__init__)
    params = list(sig.parameters.keys())



def test_evopetrinet::petrinetmodel_is_not_abstract():
    assert not inspect.isabstract(evoPetrinet::PetriNetModel)


def test_evopetrinet::petrinetmodel_constructor_exists():
    assert callable(evoPetrinet::PetriNetModel.__init__)


def test_evopetrinet::petrinetmodel_constructor_args():
    sig = inspect.signature(evoPetrinet::PetriNetModel.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_evopetrinet::element_is_not_abstract():
    assert not inspect.isabstract(evoPetrinet::Element)


def test_evopetrinet::element_constructor_exists():
    assert callable(evoPetrinet::Element.__init__)


def test_evopetrinet::element_constructor_args():
    sig = inspect.signature(evoPetrinet::Element.__init__)
    params = list(sig.parameters.keys())



def test_evopetrinet::petrinet_is_not_abstract():
    assert not inspect.isabstract(evoPetrinet::PetriNet)


def test_evopetrinet::petrinet_constructor_exists():
    assert callable(evoPetrinet::PetriNet.__init__)


def test_evopetrinet::petrinet_constructor_args():
    sig = inspect.signature(evoPetrinet::PetriNet.__init__)
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
Arc_strategy = st.builds(
    Arc,
)
evoPetrinet::TransitionToPlace_strategy = st.builds(
    evoPetrinet::TransitionToPlace,
)
evoPetrinet::PlaceToTransition_strategy = st.builds(
    evoPetrinet::PlaceToTransition,
)
PlaceToTransition_strategy = st.builds(
    PlaceToTransition,
)
TransitionToPlace_strategy = st.builds(
    TransitionToPlace,
)
Element_strategy = st.builds(
    Element,
)
evoPetrinet::Place_strategy = st.builds(
    evoPetrinet::Place,
)
evoPetrinet::Transition_strategy = st.builds(
    evoPetrinet::Transition,
)
evoPetrinet::Arc_strategy = st.builds(
    evoPetrinet::Arc,
    weight=
        safe_text
)
Transition_strategy = st.builds(
    Transition,
)
Place_strategy = st.builds(
    Place,
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
evoPetrinet::NamedElement_strategy = st.builds(
    evoPetrinet::NamedElement,
    name=
        safe_text
)
evoPetrinet::LocatedElement_strategy = st.builds(
    evoPetrinet::LocatedElement,
    location=
        safe_text
)
PetriNet_strategy = st.builds(
    PetriNet,
)
evoPetrinet::PetriNetModel_strategy = st.builds(
    evoPetrinet::PetriNetModel,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
evoPetrinet::Element_strategy = st.builds(
    evoPetrinet::Element,
)
evoPetrinet::PetriNet_strategy = st.builds(
    evoPetrinet::PetriNet,
)

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=evoPetrinet::TransitionToPlace_strategy)
@settings(max_examples=50)
def test_evopetrinet::transitiontoplace_instantiation(instance):
    assert isinstance(instance, evoPetrinet::TransitionToPlace)

@given(instance=evoPetrinet::PlaceToTransition_strategy)
@settings(max_examples=50)
def test_evopetrinet::placetotransition_instantiation(instance):
    assert isinstance(instance, evoPetrinet::PlaceToTransition)

@given(instance=PlaceToTransition_strategy)
@settings(max_examples=50)
def test_placetotransition_instantiation(instance):
    assert isinstance(instance, PlaceToTransition)

@given(instance=TransitionToPlace_strategy)
@settings(max_examples=50)
def test_transitiontoplace_instantiation(instance):
    assert isinstance(instance, TransitionToPlace)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=evoPetrinet::Place_strategy)
@settings(max_examples=50)
def test_evopetrinet::place_instantiation(instance):
    assert isinstance(instance, evoPetrinet::Place)

@given(instance=evoPetrinet::Transition_strategy)
@settings(max_examples=50)
def test_evopetrinet::transition_instantiation(instance):
    assert isinstance(instance, evoPetrinet::Transition)

@given(instance=evoPetrinet::Arc_strategy)
@settings(max_examples=50)
def test_evopetrinet::arc_instantiation(instance):
    assert isinstance(instance, evoPetrinet::Arc)

@given(instance=evoPetrinet::Arc_strategy)
def test_evopetrinet::arc_weight_type(instance):
    assert isinstance(instance.weight, str)


@given(instance=evoPetrinet::Arc_strategy)
def test_evopetrinet::arc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=Place_strategy)
@settings(max_examples=50)
def test_place_instantiation(instance):
    assert isinstance(instance, Place)

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=evoPetrinet::NamedElement_strategy)
@settings(max_examples=50)
def test_evopetrinet::namedelement_instantiation(instance):
    assert isinstance(instance, evoPetrinet::NamedElement)

@given(instance=evoPetrinet::NamedElement_strategy)
def test_evopetrinet::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=evoPetrinet::NamedElement_strategy)
def test_evopetrinet::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=evoPetrinet::LocatedElement_strategy)
@settings(max_examples=50)
def test_evopetrinet::locatedelement_instantiation(instance):
    assert isinstance(instance, evoPetrinet::LocatedElement)

@given(instance=evoPetrinet::LocatedElement_strategy)
def test_evopetrinet::locatedelement_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=evoPetrinet::LocatedElement_strategy)
def test_evopetrinet::locatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet_instantiation(instance):
    assert isinstance(instance, PetriNet)

@given(instance=evoPetrinet::PetriNetModel_strategy)
@settings(max_examples=50)
def test_evopetrinet::petrinetmodel_instantiation(instance):
    assert isinstance(instance, evoPetrinet::PetriNetModel)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=evoPetrinet::Element_strategy)
@settings(max_examples=50)
def test_evopetrinet::element_instantiation(instance):
    assert isinstance(instance, evoPetrinet::Element)

@given(instance=evoPetrinet::PetriNet_strategy)
@settings(max_examples=50)
def test_evopetrinet::petrinet_instantiation(instance):
    assert isinstance(instance, evoPetrinet::PetriNet)
