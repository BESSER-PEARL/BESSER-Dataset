import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Edge,
    petri_Edge,
    petri_EdgeToPlace,
    petri_EdgeToTransition,
    petri_Place,
    petri_Transition,
    petri_PetriNet,
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



def test_petri_edge_is_not_abstract():
    assert not inspect.isabstract(petri_Edge)


def test_petri_edge_constructor_exists():
    assert callable(petri_Edge.__init__)


def test_petri_edge_constructor_args():
    sig = inspect.signature(petri_Edge.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_petri_edge_has_weight():
    assert hasattr(petri_Edge, "weight")
    descriptor = None
    for klass in petri_Edge.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_petri_edgetoplace_is_not_abstract():
    assert not inspect.isabstract(petri_EdgeToPlace)


def test_petri_edgetoplace_constructor_exists():
    assert callable(petri_EdgeToPlace.__init__)


def test_petri_edgetoplace_constructor_args():
    sig = inspect.signature(petri_EdgeToPlace.__init__)
    params = list(sig.parameters.keys())



def test_petri_edgetotransition_is_not_abstract():
    assert not inspect.isabstract(petri_EdgeToTransition)


def test_petri_edgetotransition_constructor_exists():
    assert callable(petri_EdgeToTransition.__init__)


def test_petri_edgetotransition_constructor_args():
    sig = inspect.signature(petri_EdgeToTransition.__init__)
    params = list(sig.parameters.keys())



def test_petri_place_is_not_abstract():
    assert not inspect.isabstract(petri_Place)


def test_petri_place_constructor_exists():
    assert callable(petri_Place.__init__)


def test_petri_place_constructor_args():
    sig = inspect.signature(petri_Place.__init__)
    params = list(sig.parameters.keys())
    assert "token" in params, "Missing parameter 'token'"

def test_petri_place_has_token():
    assert hasattr(petri_Place, "token")
    descriptor = None
    for klass in petri_Place.__mro__:
        if "token" in klass.__dict__:
            descriptor = klass.__dict__["token"]
            break
    assert isinstance(descriptor, property)



def test_petri_transition_is_not_abstract():
    assert not inspect.isabstract(petri_Transition)


def test_petri_transition_constructor_exists():
    assert callable(petri_Transition.__init__)


def test_petri_transition_constructor_args():
    sig = inspect.signature(petri_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "token" in params, "Missing parameter 'token'"

def test_petri_transition_has_token():
    assert hasattr(petri_Transition, "token")
    descriptor = None
    for klass in petri_Transition.__mro__:
        if "token" in klass.__dict__:
            descriptor = klass.__dict__["token"]
            break
    assert isinstance(descriptor, property)



def test_petri_petrinet_is_not_abstract():
    assert not inspect.isabstract(petri_PetriNet)


def test_petri_petrinet_constructor_exists():
    assert callable(petri_PetriNet.__init__)


def test_petri_petrinet_constructor_args():
    sig = inspect.signature(petri_PetriNet.__init__)
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
petri_Edge_strategy = st.builds(
    petri_Edge,
    weight=
        st.integers()
)
petri_EdgeToPlace_strategy = st.builds(
    petri_EdgeToPlace,
)
petri_EdgeToTransition_strategy = st.builds(
    petri_EdgeToTransition,
)
petri_Place_strategy = st.builds(
    petri_Place,
    token=
        st.integers()
)
petri_Transition_strategy = st.builds(
    petri_Transition,
    token=
        st.integers()
)
petri_PetriNet_strategy = st.builds(
    petri_PetriNet,
)

@given(instance=Edge_strategy)
@settings(max_examples=50)
def test_edge_instantiation(instance):
    assert isinstance(instance, Edge)

@given(instance=petri_Edge_strategy)
@settings(max_examples=50)
def test_petri_edge_instantiation(instance):
    assert isinstance(instance, petri_Edge)



@given(instance=petri_Edge_strategy)
def test_petri_edge_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=petri_EdgeToPlace_strategy)
@settings(max_examples=50)
def test_petri_edgetoplace_instantiation(instance):
    assert isinstance(instance, petri_EdgeToPlace)

@given(instance=petri_EdgeToTransition_strategy)
@settings(max_examples=50)
def test_petri_edgetotransition_instantiation(instance):
    assert isinstance(instance, petri_EdgeToTransition)

@given(instance=petri_Place_strategy)
@settings(max_examples=50)
def test_petri_place_instantiation(instance):
    assert isinstance(instance, petri_Place)



@given(instance=petri_Place_strategy)
def test_petri_place_token_setter(instance):
    original = instance.token
    instance.token = original
    assert instance.token == original

@given(instance=petri_Transition_strategy)
@settings(max_examples=50)
def test_petri_transition_instantiation(instance):
    assert isinstance(instance, petri_Transition)



@given(instance=petri_Transition_strategy)
def test_petri_transition_token_setter(instance):
    original = instance.token
    instance.token = original
    assert instance.token == original

@given(instance=petri_PetriNet_strategy)
@settings(max_examples=50)
def test_petri_petrinet_instantiation(instance):
    assert isinstance(instance, petri_PetriNet)
