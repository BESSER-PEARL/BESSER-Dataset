import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    PetriNet_PTArc,
    PetriNet_Net,
    PetriNet_Place,
    PetriNet_Transition,
    PetriNet_TPArc,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinet_ptarc_is_not_abstract():
    assert not inspect.isabstract(PetriNet_PTArc)


def test_petrinet_ptarc_constructor_exists():
    assert callable(PetriNet_PTArc.__init__)


def test_petrinet_ptarc_constructor_args():
    sig = inspect.signature(PetriNet_PTArc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_net_is_not_abstract():
    assert not inspect.isabstract(PetriNet_Net)


def test_petrinet_net_constructor_exists():
    assert callable(PetriNet_Net.__init__)


def test_petrinet_net_constructor_args():
    sig = inspect.signature(PetriNet_Net.__init__)
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



def test_petrinet_tparc_is_not_abstract():
    assert not inspect.isabstract(PetriNet_TPArc)


def test_petrinet_tparc_constructor_exists():
    assert callable(PetriNet_TPArc.__init__)


def test_petrinet_tparc_constructor_args():
    sig = inspect.signature(PetriNet_TPArc.__init__)
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
PetriNet_PTArc_strategy = st.builds(
    PetriNet_PTArc,
)
PetriNet_Net_strategy = st.builds(
    PetriNet_Net,
)
PetriNet_Place_strategy = st.builds(
    PetriNet_Place,
)
PetriNet_Transition_strategy = st.builds(
    PetriNet_Transition,
)
PetriNet_TPArc_strategy = st.builds(
    PetriNet_TPArc,
)

@given(instance=PetriNet_PTArc_strategy)
@settings(max_examples=50)
def test_petrinet_ptarc_instantiation(instance):
    assert isinstance(instance, PetriNet_PTArc)

@given(instance=PetriNet_Net_strategy)
@settings(max_examples=50)
def test_petrinet_net_instantiation(instance):
    assert isinstance(instance, PetriNet_Net)

@given(instance=PetriNet_Place_strategy)
@settings(max_examples=50)
def test_petrinet_place_instantiation(instance):
    assert isinstance(instance, PetriNet_Place)

@given(instance=PetriNet_Transition_strategy)
@settings(max_examples=50)
def test_petrinet_transition_instantiation(instance):
    assert isinstance(instance, PetriNet_Transition)

@given(instance=PetriNet_TPArc_strategy)
@settings(max_examples=50)
def test_petrinet_tparc_instantiation(instance):
    assert isinstance(instance, PetriNet_TPArc)
