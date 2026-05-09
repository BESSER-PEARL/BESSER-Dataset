import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    PetriNet::PTArc,
    PetriNet::Net,
    PetriNet::Place,
    PetriNet::Transition,
    PetriNet::TPArc,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinet::ptarc_is_not_abstract():
    assert not inspect.isabstract(PetriNet::PTArc)


def test_petrinet::ptarc_constructor_exists():
    assert callable(PetriNet::PTArc.__init__)


def test_petrinet::ptarc_constructor_args():
    sig = inspect.signature(PetriNet::PTArc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::net_is_not_abstract():
    assert not inspect.isabstract(PetriNet::Net)


def test_petrinet::net_constructor_exists():
    assert callable(PetriNet::Net.__init__)


def test_petrinet::net_constructor_args():
    sig = inspect.signature(PetriNet::Net.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::place_is_not_abstract():
    assert not inspect.isabstract(PetriNet::Place)


def test_petrinet::place_constructor_exists():
    assert callable(PetriNet::Place.__init__)


def test_petrinet::place_constructor_args():
    sig = inspect.signature(PetriNet::Place.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::transition_is_not_abstract():
    assert not inspect.isabstract(PetriNet::Transition)


def test_petrinet::transition_constructor_exists():
    assert callable(PetriNet::Transition.__init__)


def test_petrinet::transition_constructor_args():
    sig = inspect.signature(PetriNet::Transition.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::tparc_is_not_abstract():
    assert not inspect.isabstract(PetriNet::TPArc)


def test_petrinet::tparc_constructor_exists():
    assert callable(PetriNet::TPArc.__init__)


def test_petrinet::tparc_constructor_args():
    sig = inspect.signature(PetriNet::TPArc.__init__)
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
PetriNet::PTArc_strategy = st.builds(
    PetriNet::PTArc,
)
PetriNet::Net_strategy = st.builds(
    PetriNet::Net,
)
PetriNet::Place_strategy = st.builds(
    PetriNet::Place,
)
PetriNet::Transition_strategy = st.builds(
    PetriNet::Transition,
)
PetriNet::TPArc_strategy = st.builds(
    PetriNet::TPArc,
)

@given(instance=PetriNet::PTArc_strategy)
@settings(max_examples=50)
def test_petrinet::ptarc_instantiation(instance):
    assert isinstance(instance, PetriNet::PTArc)

@given(instance=PetriNet::Net_strategy)
@settings(max_examples=50)
def test_petrinet::net_instantiation(instance):
    assert isinstance(instance, PetriNet::Net)

@given(instance=PetriNet::Place_strategy)
@settings(max_examples=50)
def test_petrinet::place_instantiation(instance):
    assert isinstance(instance, PetriNet::Place)

@given(instance=PetriNet::Transition_strategy)
@settings(max_examples=50)
def test_petrinet::transition_instantiation(instance):
    assert isinstance(instance, PetriNet::Transition)

@given(instance=PetriNet::TPArc_strategy)
@settings(max_examples=50)
def test_petrinet::tparc_instantiation(instance):
    assert isinstance(instance, PetriNet::TPArc)
