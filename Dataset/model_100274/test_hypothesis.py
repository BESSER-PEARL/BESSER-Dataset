import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Arc,
    PetriNet::TPArc,
    PetriNet::PTArc,
    PetriNet::Arc,
    Transition,
    Place,
    PetriNet::Net,
    PetriNet::Transition,
    TPArc,
    PTArc,
    Net,
    PetriNet::Place,
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



def test_petrinet::tparc_is_not_abstract():
    assert not inspect.isabstract(PetriNet::TPArc)


def test_petrinet::tparc_constructor_exists():
    assert callable(PetriNet::TPArc.__init__)


def test_petrinet::tparc_constructor_args():
    sig = inspect.signature(PetriNet::TPArc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::ptarc_is_not_abstract():
    assert not inspect.isabstract(PetriNet::PTArc)


def test_petrinet::ptarc_constructor_exists():
    assert callable(PetriNet::PTArc.__init__)


def test_petrinet::ptarc_constructor_args():
    sig = inspect.signature(PetriNet::PTArc.__init__)
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



def test_petrinet::net_is_not_abstract():
    assert not inspect.isabstract(PetriNet::Net)


def test_petrinet::net_constructor_exists():
    assert callable(PetriNet::Net.__init__)


def test_petrinet::net_constructor_args():
    sig = inspect.signature(PetriNet::Net.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::transition_is_not_abstract():
    assert not inspect.isabstract(PetriNet::Transition)


def test_petrinet::transition_constructor_exists():
    assert callable(PetriNet::Transition.__init__)


def test_petrinet::transition_constructor_args():
    sig = inspect.signature(PetriNet::Transition.__init__)
    params = list(sig.parameters.keys())



def test_tparc_is_not_abstract():
    assert not inspect.isabstract(TPArc)


def test_tparc_constructor_exists():
    assert callable(TPArc.__init__)


def test_tparc_constructor_args():
    sig = inspect.signature(TPArc.__init__)
    params = list(sig.parameters.keys())



def test_ptarc_is_not_abstract():
    assert not inspect.isabstract(PTArc)


def test_ptarc_constructor_exists():
    assert callable(PTArc.__init__)


def test_ptarc_constructor_args():
    sig = inspect.signature(PTArc.__init__)
    params = list(sig.parameters.keys())



def test_net_is_not_abstract():
    assert not inspect.isabstract(Net)


def test_net_constructor_exists():
    assert callable(Net.__init__)


def test_net_constructor_args():
    sig = inspect.signature(Net.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::place_is_not_abstract():
    assert not inspect.isabstract(PetriNet::Place)


def test_petrinet::place_constructor_exists():
    assert callable(PetriNet::Place.__init__)


def test_petrinet::place_constructor_args():
    sig = inspect.signature(PetriNet::Place.__init__)
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
PetriNet::TPArc_strategy = st.builds(
    PetriNet::TPArc,
)
PetriNet::PTArc_strategy = st.builds(
    PetriNet::PTArc,
)
PetriNet::Arc_strategy = st.builds(
    PetriNet::Arc,
    weight=
        safe_text
)
Transition_strategy = st.builds(
    Transition,
)
Place_strategy = st.builds(
    Place,
)
PetriNet::Net_strategy = st.builds(
    PetriNet::Net,
)
PetriNet::Transition_strategy = st.builds(
    PetriNet::Transition,
)
TPArc_strategy = st.builds(
    TPArc,
)
PTArc_strategy = st.builds(
    PTArc,
)
Net_strategy = st.builds(
    Net,
)
PetriNet::Place_strategy = st.builds(
    PetriNet::Place,
)

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=PetriNet::TPArc_strategy)
@settings(max_examples=50)
def test_petrinet::tparc_instantiation(instance):
    assert isinstance(instance, PetriNet::TPArc)

@given(instance=PetriNet::PTArc_strategy)
@settings(max_examples=50)
def test_petrinet::ptarc_instantiation(instance):
    assert isinstance(instance, PetriNet::PTArc)

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

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=Place_strategy)
@settings(max_examples=50)
def test_place_instantiation(instance):
    assert isinstance(instance, Place)

@given(instance=PetriNet::Net_strategy)
@settings(max_examples=50)
def test_petrinet::net_instantiation(instance):
    assert isinstance(instance, PetriNet::Net)

@given(instance=PetriNet::Transition_strategy)
@settings(max_examples=50)
def test_petrinet::transition_instantiation(instance):
    assert isinstance(instance, PetriNet::Transition)

@given(instance=TPArc_strategy)
@settings(max_examples=50)
def test_tparc_instantiation(instance):
    assert isinstance(instance, TPArc)

@given(instance=PTArc_strategy)
@settings(max_examples=50)
def test_ptarc_instantiation(instance):
    assert isinstance(instance, PTArc)

@given(instance=Net_strategy)
@settings(max_examples=50)
def test_net_instantiation(instance):
    assert isinstance(instance, Net)

@given(instance=PetriNet::Place_strategy)
@settings(max_examples=50)
def test_petrinet::place_instantiation(instance):
    assert isinstance(instance, PetriNet::Place)
