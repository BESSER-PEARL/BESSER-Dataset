import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    PetriNetMM0_Place,
    PetriNetMM0_Net,
    PetriNetMM0_Transition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinetmm0_place_is_not_abstract():
    assert not inspect.isabstract(PetriNetMM0_Place)


def test_petrinetmm0_place_constructor_exists():
    assert callable(PetriNetMM0_Place.__init__)


def test_petrinetmm0_place_constructor_args():
    sig = inspect.signature(PetriNetMM0_Place.__init__)
    params = list(sig.parameters.keys())



def test_petrinetmm0_net_is_not_abstract():
    assert not inspect.isabstract(PetriNetMM0_Net)


def test_petrinetmm0_net_constructor_exists():
    assert callable(PetriNetMM0_Net.__init__)


def test_petrinetmm0_net_constructor_args():
    sig = inspect.signature(PetriNetMM0_Net.__init__)
    params = list(sig.parameters.keys())



def test_petrinetmm0_transition_is_not_abstract():
    assert not inspect.isabstract(PetriNetMM0_Transition)


def test_petrinetmm0_transition_constructor_exists():
    assert callable(PetriNetMM0_Transition.__init__)


def test_petrinetmm0_transition_constructor_args():
    sig = inspect.signature(PetriNetMM0_Transition.__init__)
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
PetriNetMM0_Place_strategy = st.builds(
    PetriNetMM0_Place,
)
PetriNetMM0_Net_strategy = st.builds(
    PetriNetMM0_Net,
)
PetriNetMM0_Transition_strategy = st.builds(
    PetriNetMM0_Transition,
)

@given(instance=PetriNetMM0_Place_strategy)
@settings(max_examples=50)
def test_petrinetmm0_place_instantiation(instance):
    assert isinstance(instance, PetriNetMM0_Place)

@given(instance=PetriNetMM0_Net_strategy)
@settings(max_examples=50)
def test_petrinetmm0_net_instantiation(instance):
    assert isinstance(instance, PetriNetMM0_Net)

@given(instance=PetriNetMM0_Transition_strategy)
@settings(max_examples=50)
def test_petrinetmm0_transition_instantiation(instance):
    assert isinstance(instance, PetriNetMM0_Transition)
