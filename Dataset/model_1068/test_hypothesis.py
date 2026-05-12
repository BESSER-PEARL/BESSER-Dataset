import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    PetriNet,
    Arc,
    PetriNet_TransitionToPlace,
    Element,
    NamedElement,
    PetriNet_Element,
    PetriNet_PetriNet,
    LocatedElement,
    PetriNet_NamedElement,
    Transition,
    Place,
    PetriNet_PlaceToTransition,
    PetriNet_Arc,
    PetriNet_Transition,
    PlaceToTransition,
    TransitionToPlace,
    PetriNet_Place,
    PetriNet_LocatedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinet_is_not_abstract():
    assert not inspect.isabstract(PetriNet)


def test_petrinet_constructor_exists():
    assert callable(PetriNet.__init__)


def test_petrinet_constructor_args():
    sig = inspect.signature(PetriNet.__init__)
    params = list(sig.parameters.keys())



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



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_element_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Element)


def test_petrinet_element_constructor_exists():
    assert callable(PetriNet_Element.__init__)


def test_petrinet_element_constructor_args():
    sig = inspect.signature(PetriNet_Element.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_petrinet_is_not_abstract():
    assert not inspect.isabstract(PetriNet_PetriNet)


def test_petrinet_petrinet_constructor_exists():
    assert callable(PetriNet_PetriNet.__init__)


def test_petrinet_petrinet_constructor_args():
    sig = inspect.signature(PetriNet_PetriNet.__init__)
    params = list(sig.parameters.keys())



def test_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_namedelement_is_not_abstract():
    assert not inspect.isabstract(PetriNet_NamedElement)


def test_petrinet_namedelement_constructor_exists():
    assert callable(PetriNet_NamedElement.__init__)


def test_petrinet_namedelement_constructor_args():
    sig = inspect.signature(PetriNet_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet_namedelement_has_name():
    assert hasattr(PetriNet_NamedElement, "name")
    descriptor = None
    for klass in PetriNet_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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



def test_petrinet_placetotransition_is_not_abstract():
    assert not inspect.isabstract(PetriNet_PlaceToTransition)


def test_petrinet_placetotransition_constructor_exists():
    assert callable(PetriNet_PlaceToTransition.__init__)


def test_petrinet_placetotransition_constructor_args():
    sig = inspect.signature(PetriNet_PlaceToTransition.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_arc_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Arc)


def test_petrinet_arc_constructor_exists():
    assert callable(PetriNet_Arc.__init__)


def test_petrinet_arc_constructor_args():
    sig = inspect.signature(PetriNet_Arc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_petrinet_arc_has_weight():
    assert hasattr(PetriNet_Arc, "weight")
    descriptor = None
    for klass in PetriNet_Arc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_petrinet_transition_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Transition)


def test_petrinet_transition_constructor_exists():
    assert callable(PetriNet_Transition.__init__)


def test_petrinet_transition_constructor_args():
    sig = inspect.signature(PetriNet_Transition.__init__)
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



def test_petrinet_place_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Place)


def test_petrinet_place_constructor_exists():
    assert callable(PetriNet_Place.__init__)


def test_petrinet_place_constructor_args():
    sig = inspect.signature(PetriNet_Place.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_locatedelement_is_not_abstract():
    assert not inspect.isabstract(PetriNet_LocatedElement)


def test_petrinet_locatedelement_constructor_exists():
    assert callable(PetriNet_LocatedElement.__init__)


def test_petrinet_locatedelement_constructor_args():
    sig = inspect.signature(PetriNet_LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_petrinet_locatedelement_has_location():
    assert hasattr(PetriNet_LocatedElement, "location")
    descriptor = None
    for klass in PetriNet_LocatedElement.__mro__:
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
PetriNet_strategy = st.builds(
    PetriNet,
)
Arc_strategy = st.builds(
    Arc,
)
PetriNet_TransitionToPlace_strategy = st.builds(
    PetriNet_TransitionToPlace,
)
Element_strategy = st.builds(
    Element,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
PetriNet_Element_strategy = st.builds(
    PetriNet_Element,
)
PetriNet_PetriNet_strategy = st.builds(
    PetriNet_PetriNet,
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
PetriNet_NamedElement_strategy = st.builds(
    PetriNet_NamedElement,
    name=
        safe_text
)
Transition_strategy = st.builds(
    Transition,
)
Place_strategy = st.builds(
    Place,
)
PetriNet_PlaceToTransition_strategy = st.builds(
    PetriNet_PlaceToTransition,
)
PetriNet_Arc_strategy = st.builds(
    PetriNet_Arc,
    weight=
        st.integers()
)
PetriNet_Transition_strategy = st.builds(
    PetriNet_Transition,
)
PlaceToTransition_strategy = st.builds(
    PlaceToTransition,
)
TransitionToPlace_strategy = st.builds(
    TransitionToPlace,
)
PetriNet_Place_strategy = st.builds(
    PetriNet_Place,
)
PetriNet_LocatedElement_strategy = st.builds(
    PetriNet_LocatedElement,
    location=
        safe_text
)

@given(instance=PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet_instantiation(instance):
    assert isinstance(instance, PetriNet)

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=PetriNet_TransitionToPlace_strategy)
@settings(max_examples=50)
def test_petrinet_transitiontoplace_instantiation(instance):
    assert isinstance(instance, PetriNet_TransitionToPlace)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=PetriNet_Element_strategy)
@settings(max_examples=50)
def test_petrinet_element_instantiation(instance):
    assert isinstance(instance, PetriNet_Element)

@given(instance=PetriNet_PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet_petrinet_instantiation(instance):
    assert isinstance(instance, PetriNet_PetriNet)

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=PetriNet_NamedElement_strategy)
@settings(max_examples=50)
def test_petrinet_namedelement_instantiation(instance):
    assert isinstance(instance, PetriNet_NamedElement)



@given(instance=PetriNet_NamedElement_strategy)
def test_petrinet_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=Place_strategy)
@settings(max_examples=50)
def test_place_instantiation(instance):
    assert isinstance(instance, Place)

@given(instance=PetriNet_PlaceToTransition_strategy)
@settings(max_examples=50)
def test_petrinet_placetotransition_instantiation(instance):
    assert isinstance(instance, PetriNet_PlaceToTransition)

@given(instance=PetriNet_Arc_strategy)
@settings(max_examples=50)
def test_petrinet_arc_instantiation(instance):
    assert isinstance(instance, PetriNet_Arc)



@given(instance=PetriNet_Arc_strategy)
def test_petrinet_arc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=PetriNet_Transition_strategy)
@settings(max_examples=50)
def test_petrinet_transition_instantiation(instance):
    assert isinstance(instance, PetriNet_Transition)

@given(instance=PlaceToTransition_strategy)
@settings(max_examples=50)
def test_placetotransition_instantiation(instance):
    assert isinstance(instance, PlaceToTransition)

@given(instance=TransitionToPlace_strategy)
@settings(max_examples=50)
def test_transitiontoplace_instantiation(instance):
    assert isinstance(instance, TransitionToPlace)

@given(instance=PetriNet_Place_strategy)
@settings(max_examples=50)
def test_petrinet_place_instantiation(instance):
    assert isinstance(instance, PetriNet_Place)

@given(instance=PetriNet_LocatedElement_strategy)
@settings(max_examples=50)
def test_petrinet_locatedelement_instantiation(instance):
    assert isinstance(instance, PetriNet_LocatedElement)



@given(instance=PetriNet_LocatedElement_strategy)
def test_petrinet_locatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original
