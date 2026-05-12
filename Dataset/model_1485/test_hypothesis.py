import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Arc,
    petriNetEMF_TransitionToPlaceArc,
    petriNetEMF_PlaceToTransitionArc,
    petriNetEMF_Identification,
    Identification,
    petriNetEMF_Place,
    petriNetEMF_Arc,
    petriNetEMF_Transition,
    petriNetEMF_PetriNet,
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



def test_petrinetemf_transitiontoplacearc_is_not_abstract():
    assert not inspect.isabstract(petriNetEMF_TransitionToPlaceArc)


def test_petrinetemf_transitiontoplacearc_constructor_exists():
    assert callable(petriNetEMF_TransitionToPlaceArc.__init__)


def test_petrinetemf_transitiontoplacearc_constructor_args():
    sig = inspect.signature(petriNetEMF_TransitionToPlaceArc.__init__)
    params = list(sig.parameters.keys())



def test_petrinetemf_placetotransitionarc_is_not_abstract():
    assert not inspect.isabstract(petriNetEMF_PlaceToTransitionArc)


def test_petrinetemf_placetotransitionarc_constructor_exists():
    assert callable(petriNetEMF_PlaceToTransitionArc.__init__)


def test_petrinetemf_placetotransitionarc_constructor_args():
    sig = inspect.signature(petriNetEMF_PlaceToTransitionArc.__init__)
    params = list(sig.parameters.keys())



def test_petrinetemf_identification_is_not_abstract():
    assert not inspect.isabstract(petriNetEMF_Identification)


def test_petrinetemf_identification_constructor_exists():
    assert callable(petriNetEMF_Identification.__init__)


def test_petrinetemf_identification_constructor_args():
    sig = inspect.signature(petriNetEMF_Identification.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "ID" in params, "Missing parameter 'ID'"

def test_petrinetemf_identification_has_name():
    assert hasattr(petriNetEMF_Identification, "name")
    descriptor = None
    for klass in petriNetEMF_Identification.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_petrinetemf_identification_has_ID():
    assert hasattr(petriNetEMF_Identification, "ID")
    descriptor = None
    for klass in petriNetEMF_Identification.__mro__:
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



def test_petrinetemf_place_is_not_abstract():
    assert not inspect.isabstract(petriNetEMF_Place)


def test_petrinetemf_place_constructor_exists():
    assert callable(petriNetEMF_Place.__init__)


def test_petrinetemf_place_constructor_args():
    sig = inspect.signature(petriNetEMF_Place.__init__)
    params = list(sig.parameters.keys())



def test_petrinetemf_arc_is_not_abstract():
    assert not inspect.isabstract(petriNetEMF_Arc)


def test_petrinetemf_arc_constructor_exists():
    assert callable(petriNetEMF_Arc.__init__)


def test_petrinetemf_arc_constructor_args():
    sig = inspect.signature(petriNetEMF_Arc.__init__)
    params = list(sig.parameters.keys())



def test_petrinetemf_transition_is_not_abstract():
    assert not inspect.isabstract(petriNetEMF_Transition)


def test_petrinetemf_transition_constructor_exists():
    assert callable(petriNetEMF_Transition.__init__)


def test_petrinetemf_transition_constructor_args():
    sig = inspect.signature(petriNetEMF_Transition.__init__)
    params = list(sig.parameters.keys())



def test_petrinetemf_petrinet_is_not_abstract():
    assert not inspect.isabstract(petriNetEMF_PetriNet)


def test_petrinetemf_petrinet_constructor_exists():
    assert callable(petriNetEMF_PetriNet.__init__)


def test_petrinetemf_petrinet_constructor_args():
    sig = inspect.signature(petriNetEMF_PetriNet.__init__)
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
petriNetEMF_TransitionToPlaceArc_strategy = st.builds(
    petriNetEMF_TransitionToPlaceArc,
)
petriNetEMF_PlaceToTransitionArc_strategy = st.builds(
    petriNetEMF_PlaceToTransitionArc,
)
petriNetEMF_Identification_strategy = st.builds(
    petriNetEMF_Identification,
    name=
        safe_text,
    ID=
        safe_text
)
Identification_strategy = st.builds(
    Identification,
)
petriNetEMF_Place_strategy = st.builds(
    petriNetEMF_Place,
)
petriNetEMF_Arc_strategy = st.builds(
    petriNetEMF_Arc,
)
petriNetEMF_Transition_strategy = st.builds(
    petriNetEMF_Transition,
)
petriNetEMF_PetriNet_strategy = st.builds(
    petriNetEMF_PetriNet,
)

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=petriNetEMF_TransitionToPlaceArc_strategy)
@settings(max_examples=50)
def test_petrinetemf_transitiontoplacearc_instantiation(instance):
    assert isinstance(instance, petriNetEMF_TransitionToPlaceArc)

@given(instance=petriNetEMF_PlaceToTransitionArc_strategy)
@settings(max_examples=50)
def test_petrinetemf_placetotransitionarc_instantiation(instance):
    assert isinstance(instance, petriNetEMF_PlaceToTransitionArc)

@given(instance=petriNetEMF_Identification_strategy)
@settings(max_examples=50)
def test_petrinetemf_identification_instantiation(instance):
    assert isinstance(instance, petriNetEMF_Identification)



@given(instance=petriNetEMF_Identification_strategy)
def test_petrinetemf_identification_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=petriNetEMF_Identification_strategy)
def test_petrinetemf_identification_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=Identification_strategy)
@settings(max_examples=50)
def test_identification_instantiation(instance):
    assert isinstance(instance, Identification)

@given(instance=petriNetEMF_Place_strategy)
@settings(max_examples=50)
def test_petrinetemf_place_instantiation(instance):
    assert isinstance(instance, petriNetEMF_Place)

@given(instance=petriNetEMF_Arc_strategy)
@settings(max_examples=50)
def test_petrinetemf_arc_instantiation(instance):
    assert isinstance(instance, petriNetEMF_Arc)

@given(instance=petriNetEMF_Transition_strategy)
@settings(max_examples=50)
def test_petrinetemf_transition_instantiation(instance):
    assert isinstance(instance, petriNetEMF_Transition)

@given(instance=petriNetEMF_PetriNet_strategy)
@settings(max_examples=50)
def test_petrinetemf_petrinet_instantiation(instance):
    assert isinstance(instance, petriNetEMF_PetriNet)
