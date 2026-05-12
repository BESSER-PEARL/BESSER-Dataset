import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    PetriNet::Movement,
    Token,
    PetriNet::Marking,
    PetriNet::Token,
    Movement,
    Transition,
    Place,
    PlaceToTransition,
    TransitionToPlace,
    Marking,
    PetriNet::Execution,
    Execution,
    Arc,
    PetriNet::TransitionToPlace,
    PetriNet::PlaceToTransition,
    Element,
    PetriNet::Transition,
    NamedElement,
    PetriNet::Arc,
    PetriNet::PetriNet,
    LocatedElement,
    PetriNet::NamedElement,
    PetriNet::LocatedElement,
    PetriNet::Place,
    PetriNet,
    PetriNet::Element,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinet::movement_is_not_abstract():
    assert not inspect.isabstract(PetriNet::Movement)


def test_petrinet::movement_constructor_exists():
    assert callable(PetriNet::Movement.__init__)


def test_petrinet::movement_constructor_args():
    sig = inspect.signature(PetriNet::Movement.__init__)
    params = list(sig.parameters.keys())



def test_token_is_not_abstract():
    assert not inspect.isabstract(Token)


def test_token_constructor_exists():
    assert callable(Token.__init__)


def test_token_constructor_args():
    sig = inspect.signature(Token.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::marking_is_not_abstract():
    assert not inspect.isabstract(PetriNet::Marking)


def test_petrinet::marking_constructor_exists():
    assert callable(PetriNet::Marking.__init__)


def test_petrinet::marking_constructor_args():
    sig = inspect.signature(PetriNet::Marking.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::token_is_not_abstract():
    assert not inspect.isabstract(PetriNet::Token)


def test_petrinet::token_constructor_exists():
    assert callable(PetriNet::Token.__init__)


def test_petrinet::token_constructor_args():
    sig = inspect.signature(PetriNet::Token.__init__)
    params = list(sig.parameters.keys())



def test_movement_is_not_abstract():
    assert not inspect.isabstract(Movement)


def test_movement_constructor_exists():
    assert callable(Movement.__init__)


def test_movement_constructor_args():
    sig = inspect.signature(Movement.__init__)
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



def test_marking_is_not_abstract():
    assert not inspect.isabstract(Marking)


def test_marking_constructor_exists():
    assert callable(Marking.__init__)


def test_marking_constructor_args():
    sig = inspect.signature(Marking.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::execution_is_not_abstract():
    assert not inspect.isabstract(PetriNet::Execution)


def test_petrinet::execution_constructor_exists():
    assert callable(PetriNet::Execution.__init__)


def test_petrinet::execution_constructor_args():
    sig = inspect.signature(PetriNet::Execution.__init__)
    params = list(sig.parameters.keys())



def test_execution_is_not_abstract():
    assert not inspect.isabstract(Execution)


def test_execution_constructor_exists():
    assert callable(Execution.__init__)


def test_execution_constructor_args():
    sig = inspect.signature(Execution.__init__)
    params = list(sig.parameters.keys())



def test_arc_is_not_abstract():
    assert not inspect.isabstract(Arc)


def test_arc_constructor_exists():
    assert callable(Arc.__init__)


def test_arc_constructor_args():
    sig = inspect.signature(Arc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::transitiontoplace_is_not_abstract():
    assert not inspect.isabstract(PetriNet::TransitionToPlace)


def test_petrinet::transitiontoplace_constructor_exists():
    assert callable(PetriNet::TransitionToPlace.__init__)


def test_petrinet::transitiontoplace_constructor_args():
    sig = inspect.signature(PetriNet::TransitionToPlace.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::placetotransition_is_not_abstract():
    assert not inspect.isabstract(PetriNet::PlaceToTransition)


def test_petrinet::placetotransition_constructor_exists():
    assert callable(PetriNet::PlaceToTransition.__init__)


def test_petrinet::placetotransition_constructor_args():
    sig = inspect.signature(PetriNet::PlaceToTransition.__init__)
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



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
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



def test_petrinet::place_is_not_abstract():
    assert not inspect.isabstract(PetriNet::Place)


def test_petrinet::place_constructor_exists():
    assert callable(PetriNet::Place.__init__)


def test_petrinet::place_constructor_args():
    sig = inspect.signature(PetriNet::Place.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_is_not_abstract():
    assert not inspect.isabstract(PetriNet)


def test_petrinet_constructor_exists():
    assert callable(PetriNet.__init__)


def test_petrinet_constructor_args():
    sig = inspect.signature(PetriNet.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::element_is_not_abstract():
    assert not inspect.isabstract(PetriNet::Element)


def test_petrinet::element_constructor_exists():
    assert callable(PetriNet::Element.__init__)


def test_petrinet::element_constructor_args():
    sig = inspect.signature(PetriNet::Element.__init__)
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
PetriNet::Movement_strategy = st.builds(
    PetriNet::Movement,
)
Token_strategy = st.builds(
    Token,
)
PetriNet::Marking_strategy = st.builds(
    PetriNet::Marking,
)
PetriNet::Token_strategy = st.builds(
    PetriNet::Token,
)
Movement_strategy = st.builds(
    Movement,
)
Transition_strategy = st.builds(
    Transition,
)
Place_strategy = st.builds(
    Place,
)
PlaceToTransition_strategy = st.builds(
    PlaceToTransition,
)
TransitionToPlace_strategy = st.builds(
    TransitionToPlace,
)
Marking_strategy = st.builds(
    Marking,
)
PetriNet::Execution_strategy = st.builds(
    PetriNet::Execution,
)
Execution_strategy = st.builds(
    Execution,
)
Arc_strategy = st.builds(
    Arc,
)
PetriNet::TransitionToPlace_strategy = st.builds(
    PetriNet::TransitionToPlace,
)
PetriNet::PlaceToTransition_strategy = st.builds(
    PetriNet::PlaceToTransition,
)
Element_strategy = st.builds(
    Element,
)
PetriNet::Transition_strategy = st.builds(
    PetriNet::Transition,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
PetriNet::Arc_strategy = st.builds(
    PetriNet::Arc,
    weight=
        safe_text
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
PetriNet::Place_strategy = st.builds(
    PetriNet::Place,
)
PetriNet_strategy = st.builds(
    PetriNet,
)
PetriNet::Element_strategy = st.builds(
    PetriNet::Element,
)

@given(instance=PetriNet::Movement_strategy)
@settings(max_examples=50)
def test_petrinet::movement_instantiation(instance):
    assert isinstance(instance, PetriNet::Movement)

@given(instance=Token_strategy)
@settings(max_examples=50)
def test_token_instantiation(instance):
    assert isinstance(instance, Token)

@given(instance=PetriNet::Marking_strategy)
@settings(max_examples=50)
def test_petrinet::marking_instantiation(instance):
    assert isinstance(instance, PetriNet::Marking)

@given(instance=PetriNet::Token_strategy)
@settings(max_examples=50)
def test_petrinet::token_instantiation(instance):
    assert isinstance(instance, PetriNet::Token)

@given(instance=Movement_strategy)
@settings(max_examples=50)
def test_movement_instantiation(instance):
    assert isinstance(instance, Movement)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=Place_strategy)
@settings(max_examples=50)
def test_place_instantiation(instance):
    assert isinstance(instance, Place)

@given(instance=PlaceToTransition_strategy)
@settings(max_examples=50)
def test_placetotransition_instantiation(instance):
    assert isinstance(instance, PlaceToTransition)

@given(instance=TransitionToPlace_strategy)
@settings(max_examples=50)
def test_transitiontoplace_instantiation(instance):
    assert isinstance(instance, TransitionToPlace)

@given(instance=Marking_strategy)
@settings(max_examples=50)
def test_marking_instantiation(instance):
    assert isinstance(instance, Marking)

@given(instance=PetriNet::Execution_strategy)
@settings(max_examples=50)
def test_petrinet::execution_instantiation(instance):
    assert isinstance(instance, PetriNet::Execution)

@given(instance=Execution_strategy)
@settings(max_examples=50)
def test_execution_instantiation(instance):
    assert isinstance(instance, Execution)

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=PetriNet::TransitionToPlace_strategy)
@settings(max_examples=50)
def test_petrinet::transitiontoplace_instantiation(instance):
    assert isinstance(instance, PetriNet::TransitionToPlace)

@given(instance=PetriNet::PlaceToTransition_strategy)
@settings(max_examples=50)
def test_petrinet::placetotransition_instantiation(instance):
    assert isinstance(instance, PetriNet::PlaceToTransition)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=PetriNet::Transition_strategy)
@settings(max_examples=50)
def test_petrinet::transition_instantiation(instance):
    assert isinstance(instance, PetriNet::Transition)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

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

@given(instance=PetriNet::Place_strategy)
@settings(max_examples=50)
def test_petrinet::place_instantiation(instance):
    assert isinstance(instance, PetriNet::Place)

@given(instance=PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet_instantiation(instance):
    assert isinstance(instance, PetriNet)

@given(instance=PetriNet::Element_strategy)
@settings(max_examples=50)
def test_petrinet::element_instantiation(instance):
    assert isinstance(instance, PetriNet::Element)
