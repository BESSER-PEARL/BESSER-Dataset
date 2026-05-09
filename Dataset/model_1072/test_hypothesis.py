import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Arc,
    PetriNet::TransToPlaceArc,
    PetriNet::PlaceToTransArc,
    PetriNet::Arc,
    PetriNet::Transition,
    PetriNet::Place,
    PetriNet::PetriNet,
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



def test_petrinet::transtoplacearc_is_not_abstract():
    assert not inspect.isabstract(PetriNet::TransToPlaceArc)


def test_petrinet::transtoplacearc_constructor_exists():
    assert callable(PetriNet::TransToPlaceArc.__init__)


def test_petrinet::transtoplacearc_constructor_args():
    sig = inspect.signature(PetriNet::TransToPlaceArc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::placetotransarc_is_not_abstract():
    assert not inspect.isabstract(PetriNet::PlaceToTransArc)


def test_petrinet::placetotransarc_constructor_exists():
    assert callable(PetriNet::PlaceToTransArc.__init__)


def test_petrinet::placetotransarc_constructor_args():
    sig = inspect.signature(PetriNet::PlaceToTransArc.__init__)
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



def test_petrinet::petrinet_is_not_abstract():
    assert not inspect.isabstract(PetriNet::PetriNet)


def test_petrinet::petrinet_constructor_exists():
    assert callable(PetriNet::PetriNet.__init__)


def test_petrinet::petrinet_constructor_args():
    sig = inspect.signature(PetriNet::PetriNet.__init__)
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
PetriNet::TransToPlaceArc_strategy = st.builds(
    PetriNet::TransToPlaceArc,
)
PetriNet::PlaceToTransArc_strategy = st.builds(
    PetriNet::PlaceToTransArc,
)
PetriNet::Arc_strategy = st.builds(
    PetriNet::Arc,
    weight=
        st.integers()
)
PetriNet::Transition_strategy = st.builds(
    PetriNet::Transition,
)
PetriNet::Place_strategy = st.builds(
    PetriNet::Place,
)
PetriNet::PetriNet_strategy = st.builds(
    PetriNet::PetriNet,
)

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=PetriNet::TransToPlaceArc_strategy)
@settings(max_examples=50)
def test_petrinet::transtoplacearc_instantiation(instance):
    assert isinstance(instance, PetriNet::TransToPlaceArc)

@given(instance=PetriNet::PlaceToTransArc_strategy)
@settings(max_examples=50)
def test_petrinet::placetotransarc_instantiation(instance):
    assert isinstance(instance, PetriNet::PlaceToTransArc)

@given(instance=PetriNet::Arc_strategy)
@settings(max_examples=50)
def test_petrinet::arc_instantiation(instance):
    assert isinstance(instance, PetriNet::Arc)

@given(instance=PetriNet::Arc_strategy)
def test_petrinet::arc_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=PetriNet::Arc_strategy)
def test_petrinet::arc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=PetriNet::Transition_strategy)
@settings(max_examples=50)
def test_petrinet::transition_instantiation(instance):
    assert isinstance(instance, PetriNet::Transition)

@given(instance=PetriNet::Place_strategy)
@settings(max_examples=50)
def test_petrinet::place_instantiation(instance):
    assert isinstance(instance, PetriNet::Place)

@given(instance=PetriNet::PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet::petrinet_instantiation(instance):
    assert isinstance(instance, PetriNet::PetriNet)
