import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    petrinet::metamodel::Arc,
    Element,
    petrinet::metamodel::Place,
    petrinet::metamodel::Transition,
    petrinet::metamodel::PetriNet,
    petrinet::metamodel::Element,
    Arc,
    petrinet::metamodel::TransToPlaceArc,
    petrinet::metamodel::PlaceToTransArc,
    petrinet::metamodel::Rectangle,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinet::metamodel::arc_is_not_abstract():
    assert not inspect.isabstract(petrinet::metamodel::Arc)


def test_petrinet::metamodel::arc_constructor_exists():
    assert callable(petrinet::metamodel::Arc.__init__)


def test_petrinet::metamodel::arc_constructor_args():
    sig = inspect.signature(petrinet::metamodel::Arc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_petrinet::metamodel::arc_has_weight():
    assert hasattr(petrinet::metamodel::Arc, "weight")
    descriptor = None
    for klass in petrinet::metamodel::Arc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::metamodel::place_is_not_abstract():
    assert not inspect.isabstract(petrinet::metamodel::Place)


def test_petrinet::metamodel::place_constructor_exists():
    assert callable(petrinet::metamodel::Place.__init__)


def test_petrinet::metamodel::place_constructor_args():
    sig = inspect.signature(petrinet::metamodel::Place.__init__)
    params = list(sig.parameters.keys())
    assert "radius" in params, "Missing parameter 'radius'"
    assert "coordinates" in params, "Missing parameter 'coordinates'"
    assert "fill_colour" in params, "Missing parameter 'fill_colour'"

def test_petrinet::metamodel::place_has_radius():
    assert hasattr(petrinet::metamodel::Place, "radius")
    descriptor = None
    for klass in petrinet::metamodel::Place.__mro__:
        if "radius" in klass.__dict__:
            descriptor = klass.__dict__["radius"]
            break
    assert isinstance(descriptor, property)

def test_petrinet::metamodel::place_has_coordinates():
    assert hasattr(petrinet::metamodel::Place, "coordinates")
    descriptor = None
    for klass in petrinet::metamodel::Place.__mro__:
        if "coordinates" in klass.__dict__:
            descriptor = klass.__dict__["coordinates"]
            break
    assert isinstance(descriptor, property)

def test_petrinet::metamodel::place_has_fill_colour():
    assert hasattr(petrinet::metamodel::Place, "fill_colour")
    descriptor = None
    for klass in petrinet::metamodel::Place.__mro__:
        if "fill_colour" in klass.__dict__:
            descriptor = klass.__dict__["fill_colour"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::metamodel::transition_is_not_abstract():
    assert not inspect.isabstract(petrinet::metamodel::Transition)


def test_petrinet::metamodel::transition_constructor_exists():
    assert callable(petrinet::metamodel::Transition.__init__)


def test_petrinet::metamodel::transition_constructor_args():
    sig = inspect.signature(petrinet::metamodel::Transition.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::metamodel::petrinet_is_not_abstract():
    assert not inspect.isabstract(petrinet::metamodel::PetriNet)


def test_petrinet::metamodel::petrinet_constructor_exists():
    assert callable(petrinet::metamodel::PetriNet.__init__)


def test_petrinet::metamodel::petrinet_constructor_args():
    sig = inspect.signature(petrinet::metamodel::PetriNet.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::metamodel::element_is_not_abstract():
    assert not inspect.isabstract(petrinet::metamodel::Element)


def test_petrinet::metamodel::element_constructor_exists():
    assert callable(petrinet::metamodel::Element.__init__)


def test_petrinet::metamodel::element_constructor_args():
    sig = inspect.signature(petrinet::metamodel::Element.__init__)
    params = list(sig.parameters.keys())
    assert "comments" in params, "Missing parameter 'comments'"
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::metamodel::element_has_comments():
    assert hasattr(petrinet::metamodel::Element, "comments")
    descriptor = None
    for klass in petrinet::metamodel::Element.__mro__:
        if "comments" in klass.__dict__:
            descriptor = klass.__dict__["comments"]
            break
    assert isinstance(descriptor, property)

def test_petrinet::metamodel::element_has_name():
    assert hasattr(petrinet::metamodel::Element, "name")
    descriptor = None
    for klass in petrinet::metamodel::Element.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_arc_is_not_abstract():
    assert not inspect.isabstract(Arc)


def test_arc_constructor_exists():
    assert callable(Arc.__init__)


def test_arc_constructor_args():
    sig = inspect.signature(Arc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::metamodel::transtoplacearc_is_not_abstract():
    assert not inspect.isabstract(petrinet::metamodel::TransToPlaceArc)


def test_petrinet::metamodel::transtoplacearc_constructor_exists():
    assert callable(petrinet::metamodel::TransToPlaceArc.__init__)


def test_petrinet::metamodel::transtoplacearc_constructor_args():
    sig = inspect.signature(petrinet::metamodel::TransToPlaceArc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::metamodel::placetotransarc_is_not_abstract():
    assert not inspect.isabstract(petrinet::metamodel::PlaceToTransArc)


def test_petrinet::metamodel::placetotransarc_constructor_exists():
    assert callable(petrinet::metamodel::PlaceToTransArc.__init__)


def test_petrinet::metamodel::placetotransarc_constructor_args():
    sig = inspect.signature(petrinet::metamodel::PlaceToTransArc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::metamodel::rectangle_is_not_abstract():
    assert not inspect.isabstract(petrinet::metamodel::Rectangle)


def test_petrinet::metamodel::rectangle_constructor_exists():
    assert callable(petrinet::metamodel::Rectangle.__init__)


def test_petrinet::metamodel::rectangle_constructor_args():
    sig = inspect.signature(petrinet::metamodel::Rectangle.__init__)
    params = list(sig.parameters.keys())
    assert "start_end_coordinates" in params, "Missing parameter 'start_end_coordinates'"

def test_petrinet::metamodel::rectangle_has_start_end_coordinates():
    assert hasattr(petrinet::metamodel::Rectangle, "start_end_coordinates")
    descriptor = None
    for klass in petrinet::metamodel::Rectangle.__mro__:
        if "start_end_coordinates" in klass.__dict__:
            descriptor = klass.__dict__["start_end_coordinates"]
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
petrinet::metamodel::Arc_strategy = st.builds(
    petrinet::metamodel::Arc,
    weight=
        st.integers()
)
Element_strategy = st.builds(
    Element,
)
petrinet::metamodel::Place_strategy = st.builds(
    petrinet::metamodel::Place,
    radius=
        st.integers(),
    coordinates=
        st.integers(),
    fill_colour=
        safe_text
)
petrinet::metamodel::Transition_strategy = st.builds(
    petrinet::metamodel::Transition,
)
petrinet::metamodel::PetriNet_strategy = st.builds(
    petrinet::metamodel::PetriNet,
)
petrinet::metamodel::Element_strategy = st.builds(
    petrinet::metamodel::Element,
    comments=
        safe_text,
    name=
        safe_text
)
Arc_strategy = st.builds(
    Arc,
)
petrinet::metamodel::TransToPlaceArc_strategy = st.builds(
    petrinet::metamodel::TransToPlaceArc,
)
petrinet::metamodel::PlaceToTransArc_strategy = st.builds(
    petrinet::metamodel::PlaceToTransArc,
)
petrinet::metamodel::Rectangle_strategy = st.builds(
    petrinet::metamodel::Rectangle,
    start_end_coordinates=
        st.integers()
)

@given(instance=petrinet::metamodel::Arc_strategy)
@settings(max_examples=50)
def test_petrinet::metamodel::arc_instantiation(instance):
    assert isinstance(instance, petrinet::metamodel::Arc)

@given(instance=petrinet::metamodel::Arc_strategy)
def test_petrinet::metamodel::arc_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=petrinet::metamodel::Arc_strategy)
def test_petrinet::metamodel::arc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=petrinet::metamodel::Place_strategy)
@settings(max_examples=50)
def test_petrinet::metamodel::place_instantiation(instance):
    assert isinstance(instance, petrinet::metamodel::Place)

@given(instance=petrinet::metamodel::Place_strategy)
def test_petrinet::metamodel::place_radius_type(instance):
    assert isinstance(instance.radius, int)


@given(instance=petrinet::metamodel::Place_strategy)
def test_petrinet::metamodel::place_radius_setter(instance):
    original = instance.radius
    instance.radius = original
    assert instance.radius == original

@given(instance=petrinet::metamodel::Place_strategy)
def test_petrinet::metamodel::place_coordinates_type(instance):
    assert isinstance(instance.coordinates, int)


@given(instance=petrinet::metamodel::Place_strategy)
def test_petrinet::metamodel::place_coordinates_setter(instance):
    original = instance.coordinates
    instance.coordinates = original
    assert instance.coordinates == original

@given(instance=petrinet::metamodel::Place_strategy)
def test_petrinet::metamodel::place_fill_colour_type(instance):
    assert isinstance(instance.fill_colour, str)


@given(instance=petrinet::metamodel::Place_strategy)
def test_petrinet::metamodel::place_fill_colour_setter(instance):
    original = instance.fill_colour
    instance.fill_colour = original
    assert instance.fill_colour == original

@given(instance=petrinet::metamodel::Transition_strategy)
@settings(max_examples=50)
def test_petrinet::metamodel::transition_instantiation(instance):
    assert isinstance(instance, petrinet::metamodel::Transition)

@given(instance=petrinet::metamodel::PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet::metamodel::petrinet_instantiation(instance):
    assert isinstance(instance, petrinet::metamodel::PetriNet)

@given(instance=petrinet::metamodel::Element_strategy)
@settings(max_examples=50)
def test_petrinet::metamodel::element_instantiation(instance):
    assert isinstance(instance, petrinet::metamodel::Element)

@given(instance=petrinet::metamodel::Element_strategy)
def test_petrinet::metamodel::element_comments_type(instance):
    assert isinstance(instance.comments, str)


@given(instance=petrinet::metamodel::Element_strategy)
def test_petrinet::metamodel::element_comments_setter(instance):
    original = instance.comments
    instance.comments = original
    assert instance.comments == original

@given(instance=petrinet::metamodel::Element_strategy)
def test_petrinet::metamodel::element_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petrinet::metamodel::Element_strategy)
def test_petrinet::metamodel::element_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=petrinet::metamodel::TransToPlaceArc_strategy)
@settings(max_examples=50)
def test_petrinet::metamodel::transtoplacearc_instantiation(instance):
    assert isinstance(instance, petrinet::metamodel::TransToPlaceArc)

@given(instance=petrinet::metamodel::PlaceToTransArc_strategy)
@settings(max_examples=50)
def test_petrinet::metamodel::placetotransarc_instantiation(instance):
    assert isinstance(instance, petrinet::metamodel::PlaceToTransArc)

@given(instance=petrinet::metamodel::Rectangle_strategy)
@settings(max_examples=50)
def test_petrinet::metamodel::rectangle_instantiation(instance):
    assert isinstance(instance, petrinet::metamodel::Rectangle)

@given(instance=petrinet::metamodel::Rectangle_strategy)
def test_petrinet::metamodel::rectangle_start_end_coordinates_type(instance):
    assert isinstance(instance.start_end_coordinates, int)


@given(instance=petrinet::metamodel::Rectangle_strategy)
def test_petrinet::metamodel::rectangle_start_end_coordinates_setter(instance):
    original = instance.start_end_coordinates
    instance.start_end_coordinates = original
    assert instance.start_end_coordinates == original
