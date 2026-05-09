import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Arc,
    petriNetEMF::TransitionToPlaceArc,
    petriNetEMF::PlaceToTransitionArc,
    petriNetEMF::Identification,
    Identification,
    petriNetEMF::Place,
    petriNetEMF::Transition,
    petriNetEMF::Arc,
    petriNetEMF::PetriNet,
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



def test_petrinetemf::transitiontoplacearc_is_not_abstract():
    assert not inspect.isabstract(petriNetEMF::TransitionToPlaceArc)


def test_petrinetemf::transitiontoplacearc_constructor_exists():
    assert callable(petriNetEMF::TransitionToPlaceArc.__init__)


def test_petrinetemf::transitiontoplacearc_constructor_args():
    sig = inspect.signature(petriNetEMF::TransitionToPlaceArc.__init__)
    params = list(sig.parameters.keys())



def test_petrinetemf::placetotransitionarc_is_not_abstract():
    assert not inspect.isabstract(petriNetEMF::PlaceToTransitionArc)


def test_petrinetemf::placetotransitionarc_constructor_exists():
    assert callable(petriNetEMF::PlaceToTransitionArc.__init__)


def test_petrinetemf::placetotransitionarc_constructor_args():
    sig = inspect.signature(petriNetEMF::PlaceToTransitionArc.__init__)
    params = list(sig.parameters.keys())



def test_petrinetemf::identification_is_not_abstract():
    assert not inspect.isabstract(petriNetEMF::Identification)


def test_petrinetemf::identification_constructor_exists():
    assert callable(petriNetEMF::Identification.__init__)


def test_petrinetemf::identification_constructor_args():
    sig = inspect.signature(petriNetEMF::Identification.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "ID" in params, "Missing parameter 'ID'"

def test_petrinetemf::identification_has_name():
    assert hasattr(petriNetEMF::Identification, "name")
    descriptor = None
    for klass in petriNetEMF::Identification.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_petrinetemf::identification_has_ID():
    assert hasattr(petriNetEMF::Identification, "ID")
    descriptor = None
    for klass in petriNetEMF::Identification.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_identification_is_not_abstract():
    assert not inspect.isabstract(Identification)


def test_identification_constructor_exists():
    assert callable(Identification.__init__)


def test_identification_constructor_args():
    sig = inspect.signature(Identification.__init__)
    params = list(sig.parameters.keys())



def test_petrinetemf::place_is_not_abstract():
    assert not inspect.isabstract(petriNetEMF::Place)


def test_petrinetemf::place_constructor_exists():
    assert callable(petriNetEMF::Place.__init__)


def test_petrinetemf::place_constructor_args():
    sig = inspect.signature(petriNetEMF::Place.__init__)
    params = list(sig.parameters.keys())



def test_petrinetemf::transition_is_not_abstract():
    assert not inspect.isabstract(petriNetEMF::Transition)


def test_petrinetemf::transition_constructor_exists():
    assert callable(petriNetEMF::Transition.__init__)


def test_petrinetemf::transition_constructor_args():
    sig = inspect.signature(petriNetEMF::Transition.__init__)
    params = list(sig.parameters.keys())



def test_petrinetemf::arc_is_not_abstract():
    assert not inspect.isabstract(petriNetEMF::Arc)


def test_petrinetemf::arc_constructor_exists():
    assert callable(petriNetEMF::Arc.__init__)


def test_petrinetemf::arc_constructor_args():
    sig = inspect.signature(petriNetEMF::Arc.__init__)
    params = list(sig.parameters.keys())



def test_petrinetemf::petrinet_is_not_abstract():
    assert not inspect.isabstract(petriNetEMF::PetriNet)


def test_petrinetemf::petrinet_constructor_exists():
    assert callable(petriNetEMF::PetriNet.__init__)


def test_petrinetemf::petrinet_constructor_args():
    sig = inspect.signature(petriNetEMF::PetriNet.__init__)
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
petriNetEMF::TransitionToPlaceArc_strategy = st.builds(
    petriNetEMF::TransitionToPlaceArc,
)
petriNetEMF::PlaceToTransitionArc_strategy = st.builds(
    petriNetEMF::PlaceToTransitionArc,
)
petriNetEMF::Identification_strategy = st.builds(
    petriNetEMF::Identification,
    name=
        safe_text,
    ID=
        safe_text
)
Identification_strategy = st.builds(
    Identification,
)
petriNetEMF::Place_strategy = st.builds(
    petriNetEMF::Place,
)
petriNetEMF::Transition_strategy = st.builds(
    petriNetEMF::Transition,
)
petriNetEMF::Arc_strategy = st.builds(
    petriNetEMF::Arc,
)
petriNetEMF::PetriNet_strategy = st.builds(
    petriNetEMF::PetriNet,
)

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=petriNetEMF::TransitionToPlaceArc_strategy)
@settings(max_examples=50)
def test_petrinetemf::transitiontoplacearc_instantiation(instance):
    assert isinstance(instance, petriNetEMF::TransitionToPlaceArc)

@given(instance=petriNetEMF::PlaceToTransitionArc_strategy)
@settings(max_examples=50)
def test_petrinetemf::placetotransitionarc_instantiation(instance):
    assert isinstance(instance, petriNetEMF::PlaceToTransitionArc)

@given(instance=petriNetEMF::Identification_strategy)
@settings(max_examples=50)
def test_petrinetemf::identification_instantiation(instance):
    assert isinstance(instance, petriNetEMF::Identification)

@given(instance=petriNetEMF::Identification_strategy)
def test_petrinetemf::identification_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petriNetEMF::Identification_strategy)
def test_petrinetemf::identification_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petriNetEMF::Identification_strategy)
def test_petrinetemf::identification_ID_type(instance):
    assert isinstance(instance.ID, str)


@given(instance=petriNetEMF::Identification_strategy)
def test_petrinetemf::identification_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=Identification_strategy)
@settings(max_examples=50)
def test_identification_instantiation(instance):
    assert isinstance(instance, Identification)

@given(instance=petriNetEMF::Place_strategy)
@settings(max_examples=50)
def test_petrinetemf::place_instantiation(instance):
    assert isinstance(instance, petriNetEMF::Place)

@given(instance=petriNetEMF::Transition_strategy)
@settings(max_examples=50)
def test_petrinetemf::transition_instantiation(instance):
    assert isinstance(instance, petriNetEMF::Transition)

@given(instance=petriNetEMF::Arc_strategy)
@settings(max_examples=50)
def test_petrinetemf::arc_instantiation(instance):
    assert isinstance(instance, petriNetEMF::Arc)

@given(instance=petriNetEMF::PetriNet_strategy)
@settings(max_examples=50)
def test_petrinetemf::petrinet_instantiation(instance):
    assert isinstance(instance, petriNetEMF::PetriNet)
