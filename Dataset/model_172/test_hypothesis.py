import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Edge,
    petri::Edge,
    petri::EdgeToPlace,
    petri::EdgeToTransition,
    petri::Place,
    petri::Transition,
    petri::PetriNet,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_edge_is_not_abstract():
    assert not inspect.isabstract(Edge)


def test_edge_constructor_exists():
    assert callable(Edge.__init__)


def test_edge_constructor_args():
    sig = inspect.signature(Edge.__init__)
    params = list(sig.parameters.keys())



def test_petri::edge_is_not_abstract():
    assert not inspect.isabstract(petri::Edge)


def test_petri::edge_constructor_exists():
    assert callable(petri::Edge.__init__)


def test_petri::edge_constructor_args():
    sig = inspect.signature(petri::Edge.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_petri::edge_has_weight():
    assert hasattr(petri::Edge, "weight")
    descriptor = None
    for klass in petri::Edge.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_petri::edgetoplace_is_not_abstract():
    assert not inspect.isabstract(petri::EdgeToPlace)


def test_petri::edgetoplace_constructor_exists():
    assert callable(petri::EdgeToPlace.__init__)


def test_petri::edgetoplace_constructor_args():
    sig = inspect.signature(petri::EdgeToPlace.__init__)
    params = list(sig.parameters.keys())



def test_petri::edgetotransition_is_not_abstract():
    assert not inspect.isabstract(petri::EdgeToTransition)


def test_petri::edgetotransition_constructor_exists():
    assert callable(petri::EdgeToTransition.__init__)


def test_petri::edgetotransition_constructor_args():
    sig = inspect.signature(petri::EdgeToTransition.__init__)
    params = list(sig.parameters.keys())



def test_petri::place_is_not_abstract():
    assert not inspect.isabstract(petri::Place)


def test_petri::place_constructor_exists():
    assert callable(petri::Place.__init__)


def test_petri::place_constructor_args():
    sig = inspect.signature(petri::Place.__init__)
    params = list(sig.parameters.keys())
    assert "token" in params, "Missing parameter 'token'"

def test_petri::place_has_token():
    assert hasattr(petri::Place, "token")
    descriptor = None
    for klass in petri::Place.__mro__:
        if "token" in klass.__dict__:
            descriptor = klass.__dict__["token"]
            break
    assert isinstance(descriptor, property)



def test_petri::transition_is_not_abstract():
    assert not inspect.isabstract(petri::Transition)


def test_petri::transition_constructor_exists():
    assert callable(petri::Transition.__init__)


def test_petri::transition_constructor_args():
    sig = inspect.signature(petri::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "token" in params, "Missing parameter 'token'"

def test_petri::transition_has_token():
    assert hasattr(petri::Transition, "token")
    descriptor = None
    for klass in petri::Transition.__mro__:
        if "token" in klass.__dict__:
            descriptor = klass.__dict__["token"]
            break
    assert isinstance(descriptor, property)



def test_petri::petrinet_is_not_abstract():
    assert not inspect.isabstract(petri::PetriNet)


def test_petri::petrinet_constructor_exists():
    assert callable(petri::PetriNet.__init__)


def test_petri::petrinet_constructor_args():
    sig = inspect.signature(petri::PetriNet.__init__)
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
Edge_strategy = st.builds(
    Edge,
)
petri::Edge_strategy = st.builds(
    petri::Edge,
    weight=
        st.integers()
)
petri::EdgeToPlace_strategy = st.builds(
    petri::EdgeToPlace,
)
petri::EdgeToTransition_strategy = st.builds(
    petri::EdgeToTransition,
)
petri::Place_strategy = st.builds(
    petri::Place,
    token=
        st.integers()
)
petri::Transition_strategy = st.builds(
    petri::Transition,
    token=
        st.integers()
)
petri::PetriNet_strategy = st.builds(
    petri::PetriNet,
)

@given(instance=Edge_strategy)
@settings(max_examples=50)
def test_edge_instantiation(instance):
    assert isinstance(instance, Edge)

@given(instance=petri::Edge_strategy)
@settings(max_examples=50)
def test_petri::edge_instantiation(instance):
    assert isinstance(instance, petri::Edge)

@given(instance=petri::Edge_strategy)
def test_petri::edge_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=petri::Edge_strategy)
def test_petri::edge_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=petri::EdgeToPlace_strategy)
@settings(max_examples=50)
def test_petri::edgetoplace_instantiation(instance):
    assert isinstance(instance, petri::EdgeToPlace)

@given(instance=petri::EdgeToTransition_strategy)
@settings(max_examples=50)
def test_petri::edgetotransition_instantiation(instance):
    assert isinstance(instance, petri::EdgeToTransition)

@given(instance=petri::Place_strategy)
@settings(max_examples=50)
def test_petri::place_instantiation(instance):
    assert isinstance(instance, petri::Place)

@given(instance=petri::Place_strategy)
def test_petri::place_token_type(instance):
    assert isinstance(instance.token, int)


@given(instance=petri::Place_strategy)
def test_petri::place_token_setter(instance):
    original = instance.token
    instance.token = original
    assert instance.token == original

@given(instance=petri::Transition_strategy)
@settings(max_examples=50)
def test_petri::transition_instantiation(instance):
    assert isinstance(instance, petri::Transition)

@given(instance=petri::Transition_strategy)
def test_petri::transition_token_type(instance):
    assert isinstance(instance.token, int)


@given(instance=petri::Transition_strategy)
def test_petri::transition_token_setter(instance):
    original = instance.token
    instance.token = original
    assert instance.token == original

@given(instance=petri::PetriNet_strategy)
@settings(max_examples=50)
def test_petri::petrinet_instantiation(instance):
    assert isinstance(instance, petri::PetriNet)
