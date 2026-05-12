import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    petrinet_metamodel_Arc,
    Element,
    petrinet_metamodel_Transition,
    petrinet_metamodel_Place,
    petrinet_metamodel_PetriNet,
    petrinet_metamodel_Element,
    Arc,
    petrinet_metamodel_PlaceToTransArc,
    petrinet_metamodel_TransToPlaceArc,
    petrinet_metamodel_Rectangle,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinet_metamodel_arc_is_not_abstract():
    assert not inspect.isabstract(petrinet_metamodel_Arc)


def test_petrinet_metamodel_arc_constructor_exists():
    assert callable(petrinet_metamodel_Arc.__init__)


def test_petrinet_metamodel_arc_constructor_args():
    sig = inspect.signature(petrinet_metamodel_Arc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_petrinet_metamodel_arc_has_weight():
    assert hasattr(petrinet_metamodel_Arc, "weight")
    descriptor = None
    for klass in petrinet_metamodel_Arc.__mro__:
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



def test_petrinet_metamodel_transition_is_not_abstract():
    assert not inspect.isabstract(petrinet_metamodel_Transition)


def test_petrinet_metamodel_transition_constructor_exists():
    assert callable(petrinet_metamodel_Transition.__init__)


def test_petrinet_metamodel_transition_constructor_args():
    sig = inspect.signature(petrinet_metamodel_Transition.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_metamodel_place_is_not_abstract():
    assert not inspect.isabstract(petrinet_metamodel_Place)


def test_petrinet_metamodel_place_constructor_exists():
    assert callable(petrinet_metamodel_Place.__init__)


def test_petrinet_metamodel_place_constructor_args():
    sig = inspect.signature(petrinet_metamodel_Place.__init__)
    params = list(sig.parameters.keys())
    assert "fill_colour" in params, "Missing parameter 'fill_colour'"
    assert "radius" in params, "Missing parameter 'radius'"
    assert "coordinates" in params, "Missing parameter 'coordinates'"

def test_petrinet_metamodel_place_has_fill_colour():
    assert hasattr(petrinet_metamodel_Place, "fill_colour")
    descriptor = None
    for klass in petrinet_metamodel_Place.__mro__:
        if "fill_colour" in klass.__dict__:
            descriptor = klass.__dict__["fill_colour"]
            break
    assert isinstance(descriptor, property)

def test_petrinet_metamodel_place_has_radius():
    assert hasattr(petrinet_metamodel_Place, "radius")
    descriptor = None
    for klass in petrinet_metamodel_Place.__mro__:
        if "radius" in klass.__dict__:
            descriptor = klass.__dict__["radius"]
            break
    assert isinstance(descriptor, property)

def test_petrinet_metamodel_place_has_coordinates():
    assert hasattr(petrinet_metamodel_Place, "coordinates")
    descriptor = None
    for klass in petrinet_metamodel_Place.__mro__:
        if "coordinates" in klass.__dict__:
            descriptor = klass.__dict__["coordinates"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_metamodel_petrinet_is_not_abstract():
    assert not inspect.isabstract(petrinet_metamodel_PetriNet)


def test_petrinet_metamodel_petrinet_constructor_exists():
    assert callable(petrinet_metamodel_PetriNet.__init__)


def test_petrinet_metamodel_petrinet_constructor_args():
    sig = inspect.signature(petrinet_metamodel_PetriNet.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_metamodel_element_is_not_abstract():
    assert not inspect.isabstract(petrinet_metamodel_Element)


def test_petrinet_metamodel_element_constructor_exists():
    assert callable(petrinet_metamodel_Element.__init__)


def test_petrinet_metamodel_element_constructor_args():
    sig = inspect.signature(petrinet_metamodel_Element.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "comments" in params, "Missing parameter 'comments'"

def test_petrinet_metamodel_element_has_name():
    assert hasattr(petrinet_metamodel_Element, "name")
    descriptor = None
    for klass in petrinet_metamodel_Element.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_petrinet_metamodel_element_has_comments():
    assert hasattr(petrinet_metamodel_Element, "comments")
    descriptor = None
    for klass in petrinet_metamodel_Element.__mro__:
        if "comments" in klass.__dict__:
            descriptor = klass.__dict__["comments"]
            break
    assert isinstance(descriptor, property)



def test_arc_is_not_abstract():
    assert not inspect.isabstract(Arc)


def test_arc_constructor_exists():
    assert callable(Arc.__init__)


def test_arc_constructor_args():
    sig = inspect.signature(Arc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_metamodel_placetotransarc_is_not_abstract():
    assert not inspect.isabstract(petrinet_metamodel_PlaceToTransArc)


def test_petrinet_metamodel_placetotransarc_constructor_exists():
    assert callable(petrinet_metamodel_PlaceToTransArc.__init__)


def test_petrinet_metamodel_placetotransarc_constructor_args():
    sig = inspect.signature(petrinet_metamodel_PlaceToTransArc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_metamodel_transtoplacearc_is_not_abstract():
    assert not inspect.isabstract(petrinet_metamodel_TransToPlaceArc)


def test_petrinet_metamodel_transtoplacearc_constructor_exists():
    assert callable(petrinet_metamodel_TransToPlaceArc.__init__)


def test_petrinet_metamodel_transtoplacearc_constructor_args():
    sig = inspect.signature(petrinet_metamodel_TransToPlaceArc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_metamodel_rectangle_is_not_abstract():
    assert not inspect.isabstract(petrinet_metamodel_Rectangle)


def test_petrinet_metamodel_rectangle_constructor_exists():
    assert callable(petrinet_metamodel_Rectangle.__init__)


def test_petrinet_metamodel_rectangle_constructor_args():
    sig = inspect.signature(petrinet_metamodel_Rectangle.__init__)
    params = list(sig.parameters.keys())
    assert "start_end_coordinates" in params, "Missing parameter 'start_end_coordinates'"

def test_petrinet_metamodel_rectangle_has_start_end_coordinates():
    assert hasattr(petrinet_metamodel_Rectangle, "start_end_coordinates")
    descriptor = None
    for klass in petrinet_metamodel_Rectangle.__mro__:
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
petrinet_metamodel_Arc_strategy = st.builds(
    petrinet_metamodel_Arc,
    weight=
        st.integers()
)
Element_strategy = st.builds(
    Element,
)
petrinet_metamodel_Transition_strategy = st.builds(
    petrinet_metamodel_Transition,
)
petrinet_metamodel_Place_strategy = st.builds(
    petrinet_metamodel_Place,
    fill_colour=
        safe_text,
    radius=
        st.integers(),
    coordinates=
        st.integers()
)
petrinet_metamodel_PetriNet_strategy = st.builds(
    petrinet_metamodel_PetriNet,
)
petrinet_metamodel_Element_strategy = st.builds(
    petrinet_metamodel_Element,
    name=
        safe_text,
    comments=
        safe_text
)
Arc_strategy = st.builds(
    Arc,
)
petrinet_metamodel_PlaceToTransArc_strategy = st.builds(
    petrinet_metamodel_PlaceToTransArc,
)
petrinet_metamodel_TransToPlaceArc_strategy = st.builds(
    petrinet_metamodel_TransToPlaceArc,
)
petrinet_metamodel_Rectangle_strategy = st.builds(
    petrinet_metamodel_Rectangle,
    start_end_coordinates=
        st.integers()
)

@given(instance=petrinet_metamodel_Arc_strategy)
@settings(max_examples=50)
def test_petrinet_metamodel_arc_instantiation(instance):
    assert isinstance(instance, petrinet_metamodel_Arc)



@given(instance=petrinet_metamodel_Arc_strategy)
def test_petrinet_metamodel_arc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=petrinet_metamodel_Transition_strategy)
@settings(max_examples=50)
def test_petrinet_metamodel_transition_instantiation(instance):
    assert isinstance(instance, petrinet_metamodel_Transition)

@given(instance=petrinet_metamodel_Place_strategy)
@settings(max_examples=50)
def test_petrinet_metamodel_place_instantiation(instance):
    assert isinstance(instance, petrinet_metamodel_Place)



@given(instance=petrinet_metamodel_Place_strategy)
def test_petrinet_metamodel_place_fill_colour_setter(instance):
    original = instance.fill_colour
    instance.fill_colour = original
    assert instance.fill_colour == original



@given(instance=petrinet_metamodel_Place_strategy)
def test_petrinet_metamodel_place_radius_setter(instance):
    original = instance.radius
    instance.radius = original
    assert instance.radius == original



@given(instance=petrinet_metamodel_Place_strategy)
def test_petrinet_metamodel_place_coordinates_setter(instance):
    original = instance.coordinates
    instance.coordinates = original
    assert instance.coordinates == original

@given(instance=petrinet_metamodel_PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet_metamodel_petrinet_instantiation(instance):
    assert isinstance(instance, petrinet_metamodel_PetriNet)

@given(instance=petrinet_metamodel_Element_strategy)
@settings(max_examples=50)
def test_petrinet_metamodel_element_instantiation(instance):
    assert isinstance(instance, petrinet_metamodel_Element)



@given(instance=petrinet_metamodel_Element_strategy)
def test_petrinet_metamodel_element_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=petrinet_metamodel_Element_strategy)
def test_petrinet_metamodel_element_comments_setter(instance):
    original = instance.comments
    instance.comments = original
    assert instance.comments == original

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=petrinet_metamodel_PlaceToTransArc_strategy)
@settings(max_examples=50)
def test_petrinet_metamodel_placetotransarc_instantiation(instance):
    assert isinstance(instance, petrinet_metamodel_PlaceToTransArc)

@given(instance=petrinet_metamodel_TransToPlaceArc_strategy)
@settings(max_examples=50)
def test_petrinet_metamodel_transtoplacearc_instantiation(instance):
    assert isinstance(instance, petrinet_metamodel_TransToPlaceArc)

@given(instance=petrinet_metamodel_Rectangle_strategy)
@settings(max_examples=50)
def test_petrinet_metamodel_rectangle_instantiation(instance):
    assert isinstance(instance, petrinet_metamodel_Rectangle)



@given(instance=petrinet_metamodel_Rectangle_strategy)
def test_petrinet_metamodel_rectangle_start_end_coordinates_setter(instance):
    original = instance.start_end_coordinates
    instance.start_end_coordinates = original
    assert instance.start_end_coordinates == original
