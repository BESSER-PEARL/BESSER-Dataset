import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    PetriNet,
    PetriNets::Token,
    PetriNets::Transition,
    PetriNets::Place,
    PetriNets::PetriNet,
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



def test_petrinets::token_is_not_abstract():
    assert not inspect.isabstract(PetriNets::Token)


def test_petrinets::token_constructor_exists():
    assert callable(PetriNets::Token.__init__)


def test_petrinets::token_constructor_args():
    sig = inspect.signature(PetriNets::Token.__init__)
    params = list(sig.parameters.keys())



def test_petrinets::transition_is_not_abstract():
    assert not inspect.isabstract(PetriNets::Transition)


def test_petrinets::transition_constructor_exists():
    assert callable(PetriNets::Transition.__init__)


def test_petrinets::transition_constructor_args():
    sig = inspect.signature(PetriNets::Transition.__init__)
    params = list(sig.parameters.keys())



def test_petrinets::place_is_not_abstract():
    assert not inspect.isabstract(PetriNets::Place)


def test_petrinets::place_constructor_exists():
    assert callable(PetriNets::Place.__init__)


def test_petrinets::place_constructor_args():
    sig = inspect.signature(PetriNets::Place.__init__)
    params = list(sig.parameters.keys())
    assert "itokens" in params, "Missing parameter 'itokens'"

def test_petrinets::place_has_itokens():
    assert hasattr(PetriNets::Place, "itokens")
    descriptor = None
    for klass in PetriNets::Place.__mro__:
        if "itokens" in klass.__dict__:
            descriptor = klass.__dict__["itokens"]
            break
    assert isinstance(descriptor, property)



def test_petrinets::petrinet_is_not_abstract():
    assert not inspect.isabstract(PetriNets::PetriNet)


def test_petrinets::petrinet_constructor_exists():
    assert callable(PetriNets::PetriNet.__init__)


def test_petrinets::petrinet_constructor_args():
    sig = inspect.signature(PetriNets::PetriNet.__init__)
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
PetriNet_strategy = st.builds(
    PetriNet,
)
PetriNets::Token_strategy = st.builds(
    PetriNets::Token,
)
PetriNets::Transition_strategy = st.builds(
    PetriNets::Transition,
)
PetriNets::Place_strategy = st.builds(
    PetriNets::Place,
    itokens=
        st.integers()
)
PetriNets::PetriNet_strategy = st.builds(
    PetriNets::PetriNet,
)

@given(instance=PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet_instantiation(instance):
    assert isinstance(instance, PetriNet)

@given(instance=PetriNets::Token_strategy)
@settings(max_examples=50)
def test_petrinets::token_instantiation(instance):
    assert isinstance(instance, PetriNets::Token)

@given(instance=PetriNets::Transition_strategy)
@settings(max_examples=50)
def test_petrinets::transition_instantiation(instance):
    assert isinstance(instance, PetriNets::Transition)

@given(instance=PetriNets::Place_strategy)
@settings(max_examples=50)
def test_petrinets::place_instantiation(instance):
    assert isinstance(instance, PetriNets::Place)

@given(instance=PetriNets::Place_strategy)
def test_petrinets::place_itokens_type(instance):
    assert isinstance(instance.itokens, int)


@given(instance=PetriNets::Place_strategy)
def test_petrinets::place_itokens_setter(instance):
    original = instance.itokens
    instance.itokens = original
    assert instance.itokens == original

@given(instance=PetriNets::PetriNet_strategy)
@settings(max_examples=50)
def test_petrinets::petrinet_instantiation(instance):
    assert isinstance(instance, PetriNets::PetriNet)
