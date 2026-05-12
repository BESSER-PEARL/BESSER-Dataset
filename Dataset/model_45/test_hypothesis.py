import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Arc,
    Element,
    petriNet_Place,
    NamedElement,
    petriNet_Element,
    petriNet_Arc,
    petriNet_PetriNet,
    petriNet_Transition,
    petriNet_PlaceToTransition,
    petriNet_TransitionToPlace,
    LocatedElement,
    petriNet_NamedElement,
    petriNet_LocatedElement,
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



def test_petrinet_place_is_not_abstract():
    assert not inspect.isabstract(petriNet_Place)


def test_petrinet_place_constructor_exists():
    assert callable(petriNet_Place.__init__)


def test_petrinet_place_constructor_args():
    sig = inspect.signature(petriNet_Place.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_element_is_not_abstract():
    assert not inspect.isabstract(petriNet_Element)


def test_petrinet_element_constructor_exists():
    assert callable(petriNet_Element.__init__)


def test_petrinet_element_constructor_args():
    sig = inspect.signature(petriNet_Element.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_arc_is_not_abstract():
    assert not inspect.isabstract(petriNet_Arc)


def test_petrinet_arc_constructor_exists():
    assert callable(petriNet_Arc.__init__)


def test_petrinet_arc_constructor_args():
    sig = inspect.signature(petriNet_Arc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_petrinet_arc_has_weight():
    assert hasattr(petriNet_Arc, "weight")
    descriptor = None
    for klass in petriNet_Arc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_petrinet_is_not_abstract():
    assert not inspect.isabstract(petriNet_PetriNet)


def test_petrinet_petrinet_constructor_exists():
    assert callable(petriNet_PetriNet.__init__)


def test_petrinet_petrinet_constructor_args():
    sig = inspect.signature(petriNet_PetriNet.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_transition_is_not_abstract():
    assert not inspect.isabstract(petriNet_Transition)


def test_petrinet_transition_constructor_exists():
    assert callable(petriNet_Transition.__init__)


def test_petrinet_transition_constructor_args():
    sig = inspect.signature(petriNet_Transition.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_placetotransition_is_not_abstract():
    assert not inspect.isabstract(petriNet_PlaceToTransition)


def test_petrinet_placetotransition_constructor_exists():
    assert callable(petriNet_PlaceToTransition.__init__)


def test_petrinet_placetotransition_constructor_args():
    sig = inspect.signature(petriNet_PlaceToTransition.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_transitiontoplace_is_not_abstract():
    assert not inspect.isabstract(petriNet_TransitionToPlace)


def test_petrinet_transitiontoplace_constructor_exists():
    assert callable(petriNet_TransitionToPlace.__init__)


def test_petrinet_transitiontoplace_constructor_args():
    sig = inspect.signature(petriNet_TransitionToPlace.__init__)
    params = list(sig.parameters.keys())



def test_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_namedelement_is_not_abstract():
    assert not inspect.isabstract(petriNet_NamedElement)


def test_petrinet_namedelement_constructor_exists():
    assert callable(petriNet_NamedElement.__init__)


def test_petrinet_namedelement_constructor_args():
    sig = inspect.signature(petriNet_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet_namedelement_has_name():
    assert hasattr(petriNet_NamedElement, "name")
    descriptor = None
    for klass in petriNet_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_locatedelement_is_not_abstract():
    assert not inspect.isabstract(petriNet_LocatedElement)


def test_petrinet_locatedelement_constructor_exists():
    assert callable(petriNet_LocatedElement.__init__)


def test_petrinet_locatedelement_constructor_args():
    sig = inspect.signature(petriNet_LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_petrinet_locatedelement_has_location():
    assert hasattr(petriNet_LocatedElement, "location")
    descriptor = None
    for klass in petriNet_LocatedElement.__mro__:
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
petriNet_Place_strategy = st.builds(
    petriNet_Place,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
petriNet_Element_strategy = st.builds(
    petriNet_Element,
)
petriNet_Arc_strategy = st.builds(
    petriNet_Arc,
    weight=
        st.integers()
)
petriNet_PetriNet_strategy = st.builds(
    petriNet_PetriNet,
)
petriNet_Transition_strategy = st.builds(
    petriNet_Transition,
)
petriNet_PlaceToTransition_strategy = st.builds(
    petriNet_PlaceToTransition,
)
petriNet_TransitionToPlace_strategy = st.builds(
    petriNet_TransitionToPlace,
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
petriNet_NamedElement_strategy = st.builds(
    petriNet_NamedElement,
    name=
        safe_text
)
petriNet_LocatedElement_strategy = st.builds(
    petriNet_LocatedElement,
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

@given(instance=petriNet_Place_strategy)
@settings(max_examples=50)
def test_petrinet_place_instantiation(instance):
    assert isinstance(instance, petriNet_Place)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=petriNet_Element_strategy)
@settings(max_examples=50)
def test_petrinet_element_instantiation(instance):
    assert isinstance(instance, petriNet_Element)

@given(instance=petriNet_Arc_strategy)
@settings(max_examples=50)
def test_petrinet_arc_instantiation(instance):
    assert isinstance(instance, petriNet_Arc)



@given(instance=petriNet_Arc_strategy)
def test_petrinet_arc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=petriNet_PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet_petrinet_instantiation(instance):
    assert isinstance(instance, petriNet_PetriNet)

@given(instance=petriNet_Transition_strategy)
@settings(max_examples=50)
def test_petrinet_transition_instantiation(instance):
    assert isinstance(instance, petriNet_Transition)

@given(instance=petriNet_PlaceToTransition_strategy)
@settings(max_examples=50)
def test_petrinet_placetotransition_instantiation(instance):
    assert isinstance(instance, petriNet_PlaceToTransition)

@given(instance=petriNet_TransitionToPlace_strategy)
@settings(max_examples=50)
def test_petrinet_transitiontoplace_instantiation(instance):
    assert isinstance(instance, petriNet_TransitionToPlace)

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=petriNet_NamedElement_strategy)
@settings(max_examples=50)
def test_petrinet_namedelement_instantiation(instance):
    assert isinstance(instance, petriNet_NamedElement)



@given(instance=petriNet_NamedElement_strategy)
def test_petrinet_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petriNet_LocatedElement_strategy)
@settings(max_examples=50)
def test_petrinet_locatedelement_instantiation(instance):
    assert isinstance(instance, petriNet_LocatedElement)



@given(instance=petriNet_LocatedElement_strategy)
def test_petrinet_locatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original
