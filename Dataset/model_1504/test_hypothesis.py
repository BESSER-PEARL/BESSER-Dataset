import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    PetriNetMM0::Place,
    PetriNetMM0::Net,
    PetriNetMM0::Transition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinetmm0::place_is_not_abstract():
    assert not inspect.isabstract(PetriNetMM0::Place)


def test_petrinetmm0::place_constructor_exists():
    assert callable(PetriNetMM0::Place.__init__)


def test_petrinetmm0::place_constructor_args():
    sig = inspect.signature(PetriNetMM0::Place.__init__)
    params = list(sig.parameters.keys())



def test_petrinetmm0::net_is_not_abstract():
    assert not inspect.isabstract(PetriNetMM0::Net)


def test_petrinetmm0::net_constructor_exists():
    assert callable(PetriNetMM0::Net.__init__)


def test_petrinetmm0::net_constructor_args():
    sig = inspect.signature(PetriNetMM0::Net.__init__)
    params = list(sig.parameters.keys())



def test_petrinetmm0::transition_is_not_abstract():
    assert not inspect.isabstract(PetriNetMM0::Transition)


def test_petrinetmm0::transition_constructor_exists():
    assert callable(PetriNetMM0::Transition.__init__)


def test_petrinetmm0::transition_constructor_args():
    sig = inspect.signature(PetriNetMM0::Transition.__init__)
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
PetriNetMM0::Place_strategy = st.builds(
    PetriNetMM0::Place,
)
PetriNetMM0::Net_strategy = st.builds(
    PetriNetMM0::Net,
)
PetriNetMM0::Transition_strategy = st.builds(
    PetriNetMM0::Transition,
)

@given(instance=PetriNetMM0::Place_strategy)
@settings(max_examples=50)
def test_petrinetmm0::place_instantiation(instance):
    assert isinstance(instance, PetriNetMM0::Place)

@given(instance=PetriNetMM0::Net_strategy)
@settings(max_examples=50)
def test_petrinetmm0::net_instantiation(instance):
    assert isinstance(instance, PetriNetMM0::Net)

@given(instance=PetriNetMM0::Transition_strategy)
@settings(max_examples=50)
def test_petrinetmm0::transition_instantiation(instance):
    assert isinstance(instance, PetriNetMM0::Transition)
