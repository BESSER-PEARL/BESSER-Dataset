import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    PetriNet::NonReferencedClass,
    PetriNet::Arc,
    PetriNet,
    PlaceToTransArc,
    TransToPlaceArc,
    Arc,
    PetriNet::PlaceToTransArc,
    Transition,
    Place,
    Element,
    PetriNet::Transition,
    PetriNet::Place,
    PetriNet::PetriNet,
    PetriNet::Element,
    PetriNet::TransToPlaceArc,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinet::nonreferencedclass_is_not_abstract():
    assert not inspect.isabstract(PetriNet::NonReferencedClass)


def test_petrinet::nonreferencedclass_constructor_exists():
    assert callable(PetriNet::NonReferencedClass.__init__)


def test_petrinet::nonreferencedclass_constructor_args():
    sig = inspect.signature(PetriNet::NonReferencedClass.__init__)
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



def test_petrinet_is_not_abstract():
    assert not inspect.isabstract(PetriNet)


def test_petrinet_constructor_exists():
    assert callable(PetriNet.__init__)


def test_petrinet_constructor_args():
    sig = inspect.signature(PetriNet.__init__)
    params = list(sig.parameters.keys())



def test_placetotransarc_is_not_abstract():
    assert not inspect.isabstract(PlaceToTransArc)


def test_placetotransarc_constructor_exists():
    assert callable(PlaceToTransArc.__init__)


def test_placetotransarc_constructor_args():
    sig = inspect.signature(PlaceToTransArc.__init__)
    params = list(sig.parameters.keys())



def test_transtoplacearc_is_not_abstract():
    assert not inspect.isabstract(TransToPlaceArc)


def test_transtoplacearc_constructor_exists():
    assert callable(TransToPlaceArc.__init__)


def test_transtoplacearc_constructor_args():
    sig = inspect.signature(TransToPlaceArc.__init__)
    params = list(sig.parameters.keys())



def test_arc_is_not_abstract():
    assert not inspect.isabstract(Arc)


def test_arc_constructor_exists():
    assert callable(Arc.__init__)


def test_arc_constructor_args():
    sig = inspect.signature(Arc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::placetotransarc_is_not_abstract():
    assert not inspect.isabstract(PetriNet::PlaceToTransArc)


def test_petrinet::placetotransarc_constructor_exists():
    assert callable(PetriNet::PlaceToTransArc.__init__)


def test_petrinet::placetotransarc_constructor_args():
    sig = inspect.signature(PetriNet::PlaceToTransArc.__init__)
    params = list(sig.parameters.keys())



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
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::place_has_name():
    assert hasattr(PetriNet::Place, "name")
    descriptor = None
    for klass in PetriNet::Place.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::petrinet_is_not_abstract():
    assert not inspect.isabstract(PetriNet::PetriNet)


def test_petrinet::petrinet_constructor_exists():
    assert callable(PetriNet::PetriNet.__init__)


def test_petrinet::petrinet_constructor_args():
    sig = inspect.signature(PetriNet::PetriNet.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::element_is_not_abstract():
    assert not inspect.isabstract(PetriNet::Element)


def test_petrinet::element_constructor_exists():
    assert callable(PetriNet::Element.__init__)


def test_petrinet::element_constructor_args():
    sig = inspect.signature(PetriNet::Element.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::transtoplacearc_is_not_abstract():
    assert not inspect.isabstract(PetriNet::TransToPlaceArc)


def test_petrinet::transtoplacearc_constructor_exists():
    assert callable(PetriNet::TransToPlaceArc.__init__)


def test_petrinet::transtoplacearc_constructor_args():
    sig = inspect.signature(PetriNet::TransToPlaceArc.__init__)
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
PetriNet::NonReferencedClass_strategy = st.builds(
    PetriNet::NonReferencedClass,
)
PetriNet::Arc_strategy = st.builds(
    PetriNet::Arc,
    weight=
        safe_text
)
PetriNet_strategy = st.builds(
    PetriNet,
)
PlaceToTransArc_strategy = st.builds(
    PlaceToTransArc,
)
TransToPlaceArc_strategy = st.builds(
    TransToPlaceArc,
)
Arc_strategy = st.builds(
    Arc,
)
PetriNet::PlaceToTransArc_strategy = st.builds(
    PetriNet::PlaceToTransArc,
)
Transition_strategy = st.builds(
    Transition,
)
Place_strategy = st.builds(
    Place,
)
Element_strategy = st.builds(
    Element,
)
PetriNet::Transition_strategy = st.builds(
    PetriNet::Transition,
)
PetriNet::Place_strategy = st.builds(
    PetriNet::Place,
    name=
        safe_text
)
PetriNet::PetriNet_strategy = st.builds(
    PetriNet::PetriNet,
)
PetriNet::Element_strategy = st.builds(
    PetriNet::Element,
)
PetriNet::TransToPlaceArc_strategy = st.builds(
    PetriNet::TransToPlaceArc,
)

@given(instance=PetriNet::NonReferencedClass_strategy)
@settings(max_examples=50)
def test_petrinet::nonreferencedclass_instantiation(instance):
    assert isinstance(instance, PetriNet::NonReferencedClass)

@given(instance=PetriNet::Arc_strategy)
@settings(max_examples=50)
def test_petrinet::arc_instantiation(instance):
    assert isinstance(instance, PetriNet::Arc)

@given(instance=PetriNet::Arc_strategy)
def test_petrinet::arc_weight_type(instance):
    assert isinstance(instance.weight, str)


@given(instance=PetriNet::Arc_strategy)
def test_petrinet::arc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet_instantiation(instance):
    assert isinstance(instance, PetriNet)

@given(instance=PlaceToTransArc_strategy)
@settings(max_examples=50)
def test_placetotransarc_instantiation(instance):
    assert isinstance(instance, PlaceToTransArc)

@given(instance=TransToPlaceArc_strategy)
@settings(max_examples=50)
def test_transtoplacearc_instantiation(instance):
    assert isinstance(instance, TransToPlaceArc)

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=PetriNet::PlaceToTransArc_strategy)
@settings(max_examples=50)
def test_petrinet::placetotransarc_instantiation(instance):
    assert isinstance(instance, PetriNet::PlaceToTransArc)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=Place_strategy)
@settings(max_examples=50)
def test_place_instantiation(instance):
    assert isinstance(instance, Place)

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

@given(instance=PetriNet::Place_strategy)
def test_petrinet::place_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=PetriNet::Place_strategy)
def test_petrinet::place_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PetriNet::PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet::petrinet_instantiation(instance):
    assert isinstance(instance, PetriNet::PetriNet)

@given(instance=PetriNet::Element_strategy)
@settings(max_examples=50)
def test_petrinet::element_instantiation(instance):
    assert isinstance(instance, PetriNet::Element)

@given(instance=PetriNet::TransToPlaceArc_strategy)
@settings(max_examples=50)
def test_petrinet::transtoplacearc_instantiation(instance):
    assert isinstance(instance, PetriNet::TransToPlaceArc)
