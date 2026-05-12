import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Transition,
    Place,
    PetriNet_Arc,
    PetriNet_Element,
    Arc,
    PetriNet_TransitionToPlace,
    PetriNet_PlaceToTransition,
    Element,
    PetriNet_Place,
    PetriNet_Transition,
    EObject,
    PetriNet_PetriNet,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_petrinet_arc_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Arc)


def test_petrinet_arc_constructor_exists():
    assert callable(PetriNet_Arc.__init__)


def test_petrinet_arc_constructor_args():
    sig = inspect.signature(PetriNet_Arc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet_arc_has_weight():
    assert hasattr(PetriNet_Arc, "weight")
    descriptor = None
    for klass in PetriNet_Arc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)

def test_petrinet_arc_has_name():
    assert hasattr(PetriNet_Arc, "name")
    descriptor = None
    for klass in PetriNet_Arc.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_element_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Element)


def test_petrinet_element_constructor_exists():
    assert callable(PetriNet_Element.__init__)


def test_petrinet_element_constructor_args():
    sig = inspect.signature(PetriNet_Element.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet_element_has_name():
    assert hasattr(PetriNet_Element, "name")
    descriptor = None
    for klass in PetriNet_Element.__mro__:
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



def test_petrinet_transitiontoplace_is_not_abstract():
    assert not inspect.isabstract(PetriNet_TransitionToPlace)


def test_petrinet_transitiontoplace_constructor_exists():
    assert callable(PetriNet_TransitionToPlace.__init__)


def test_petrinet_transitiontoplace_constructor_args():
    sig = inspect.signature(PetriNet_TransitionToPlace.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_placetotransition_is_not_abstract():
    assert not inspect.isabstract(PetriNet_PlaceToTransition)


def test_petrinet_placetotransition_constructor_exists():
    assert callable(PetriNet_PlaceToTransition.__init__)


def test_petrinet_placetotransition_constructor_args():
    sig = inspect.signature(PetriNet_PlaceToTransition.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_place_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Place)


def test_petrinet_place_constructor_exists():
    assert callable(PetriNet_Place.__init__)


def test_petrinet_place_constructor_args():
    sig = inspect.signature(PetriNet_Place.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_transition_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Transition)


def test_petrinet_transition_constructor_exists():
    assert callable(PetriNet_Transition.__init__)


def test_petrinet_transition_constructor_args():
    sig = inspect.signature(PetriNet_Transition.__init__)
    params = list(sig.parameters.keys())



def test_eobject_is_not_abstract():
    assert not inspect.isabstract(EObject)


def test_eobject_constructor_exists():
    assert callable(EObject.__init__)


def test_eobject_constructor_args():
    sig = inspect.signature(EObject.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_petrinet_is_not_abstract():
    assert not inspect.isabstract(PetriNet_PetriNet)


def test_petrinet_petrinet_constructor_exists():
    assert callable(PetriNet_PetriNet.__init__)


def test_petrinet_petrinet_constructor_args():
    sig = inspect.signature(PetriNet_PetriNet.__init__)
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
Transition_strategy = st.builds(
    Transition,
)
Place_strategy = st.builds(
    Place,
)
PetriNet_Arc_strategy = st.builds(
    PetriNet_Arc,
    weight=
        safe_text,
    name=
        safe_text
)
PetriNet_Element_strategy = st.builds(
    PetriNet_Element,
    name=
        safe_text
)
Arc_strategy = st.builds(
    Arc,
)
PetriNet_TransitionToPlace_strategy = st.builds(
    PetriNet_TransitionToPlace,
)
PetriNet_PlaceToTransition_strategy = st.builds(
    PetriNet_PlaceToTransition,
)
Element_strategy = st.builds(
    Element,
)
PetriNet_Place_strategy = st.builds(
    PetriNet_Place,
)
PetriNet_Transition_strategy = st.builds(
    PetriNet_Transition,
)
EObject_strategy = st.builds(
    EObject,
)
PetriNet_PetriNet_strategy = st.builds(
    PetriNet_PetriNet,
)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=Place_strategy)
@settings(max_examples=50)
def test_place_instantiation(instance):
    assert isinstance(instance, Place)

@given(instance=PetriNet_Arc_strategy)
@settings(max_examples=50)
def test_petrinet_arc_instantiation(instance):
    assert isinstance(instance, PetriNet_Arc)



@given(instance=PetriNet_Arc_strategy)
def test_petrinet_arc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original



@given(instance=PetriNet_Arc_strategy)
def test_petrinet_arc_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PetriNet_Element_strategy)
@settings(max_examples=50)
def test_petrinet_element_instantiation(instance):
    assert isinstance(instance, PetriNet_Element)



@given(instance=PetriNet_Element_strategy)
def test_petrinet_element_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=PetriNet_TransitionToPlace_strategy)
@settings(max_examples=50)
def test_petrinet_transitiontoplace_instantiation(instance):
    assert isinstance(instance, PetriNet_TransitionToPlace)

@given(instance=PetriNet_PlaceToTransition_strategy)
@settings(max_examples=50)
def test_petrinet_placetotransition_instantiation(instance):
    assert isinstance(instance, PetriNet_PlaceToTransition)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=PetriNet_Place_strategy)
@settings(max_examples=50)
def test_petrinet_place_instantiation(instance):
    assert isinstance(instance, PetriNet_Place)

@given(instance=PetriNet_Transition_strategy)
@settings(max_examples=50)
def test_petrinet_transition_instantiation(instance):
    assert isinstance(instance, PetriNet_Transition)

@given(instance=EObject_strategy)
@settings(max_examples=50)
def test_eobject_instantiation(instance):
    assert isinstance(instance, EObject)

@given(instance=PetriNet_PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet_petrinet_instantiation(instance):
    assert isinstance(instance, PetriNet_PetriNet)
