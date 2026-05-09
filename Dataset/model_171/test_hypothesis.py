import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Arc,
    petrinet::TransitionPlaceArc,
    petrinet::PlaceTransitionArc,
    petrinet::Node,
    petrinet::Arc,
    petrinet::PetriNet,
    Node,
    petrinet::Transition,
    petrinet::Place,
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



def test_petrinet::transitionplacearc_is_not_abstract():
    assert not inspect.isabstract(petrinet::TransitionPlaceArc)


def test_petrinet::transitionplacearc_constructor_exists():
    assert callable(petrinet::TransitionPlaceArc.__init__)


def test_petrinet::transitionplacearc_constructor_args():
    sig = inspect.signature(petrinet::TransitionPlaceArc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::placetransitionarc_is_not_abstract():
    assert not inspect.isabstract(petrinet::PlaceTransitionArc)


def test_petrinet::placetransitionarc_constructor_exists():
    assert callable(petrinet::PlaceTransitionArc.__init__)


def test_petrinet::placetransitionarc_constructor_args():
    sig = inspect.signature(petrinet::PlaceTransitionArc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::node_is_not_abstract():
    assert not inspect.isabstract(petrinet::Node)


def test_petrinet::node_constructor_exists():
    assert callable(petrinet::Node.__init__)


def test_petrinet::node_constructor_args():
    sig = inspect.signature(petrinet::Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::node_has_name():
    assert hasattr(petrinet::Node, "name")
    descriptor = None
    for klass in petrinet::Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::arc_is_not_abstract():
    assert not inspect.isabstract(petrinet::Arc)


def test_petrinet::arc_constructor_exists():
    assert callable(petrinet::Arc.__init__)


def test_petrinet::arc_constructor_args():
    sig = inspect.signature(petrinet::Arc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_petrinet::arc_has_weight():
    assert hasattr(petrinet::Arc, "weight")
    descriptor = None
    for klass in petrinet::Arc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_petrinet::petrinet_is_not_abstract():
    assert not inspect.isabstract(petrinet::PetriNet)


def test_petrinet::petrinet_constructor_exists():
    assert callable(petrinet::PetriNet.__init__)


def test_petrinet::petrinet_constructor_args():
    sig = inspect.signature(petrinet::PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinet::petrinet_has_name():
    assert hasattr(petrinet::PetriNet, "name")
    descriptor = None
    for klass in petrinet::PetriNet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::transition_is_not_abstract():
    assert not inspect.isabstract(petrinet::Transition)


def test_petrinet::transition_constructor_exists():
    assert callable(petrinet::Transition.__init__)


def test_petrinet::transition_constructor_args():
    sig = inspect.signature(petrinet::Transition.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::place_is_not_abstract():
    assert not inspect.isabstract(petrinet::Place)


def test_petrinet::place_constructor_exists():
    assert callable(petrinet::Place.__init__)


def test_petrinet::place_constructor_args():
    sig = inspect.signature(petrinet::Place.__init__)
    params = list(sig.parameters.keys())
    assert "capacity" in params, "Missing parameter 'capacity'"
    assert "tokens" in params, "Missing parameter 'tokens'"

def test_petrinet::place_has_capacity():
    assert hasattr(petrinet::Place, "capacity")
    descriptor = None
    for klass in petrinet::Place.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
            break
    assert isinstance(descriptor, property)

def test_petrinet::place_has_tokens():
    assert hasattr(petrinet::Place, "tokens")
    descriptor = None
    for klass in petrinet::Place.__mro__:
        if "tokens" in klass.__dict__:
            descriptor = klass.__dict__["tokens"]
            break
    assert isinstance(descriptor, property)


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
petrinet::TransitionPlaceArc_strategy = st.builds(
    petrinet::TransitionPlaceArc,
)
petrinet::PlaceTransitionArc_strategy = st.builds(
    petrinet::PlaceTransitionArc,
)
petrinet::Node_strategy = st.builds(
    petrinet::Node,
    name=
        safe_text
)
petrinet::Arc_strategy = st.builds(
    petrinet::Arc,
    weight=
        st.integers()
)
petrinet::PetriNet_strategy = st.builds(
    petrinet::PetriNet,
    name=
        safe_text
)
Node_strategy = st.builds(
    Node,
)
petrinet::Transition_strategy = st.builds(
    petrinet::Transition,
)
petrinet::Place_strategy = st.builds(
    petrinet::Place,
    capacity=
        st.integers(),
    tokens=
        st.integers()
)

@given(instance=Arc_strategy)
@settings(max_examples=50)
def test_arc_instantiation(instance):
    assert isinstance(instance, Arc)

@given(instance=petrinet::TransitionPlaceArc_strategy)
@settings(max_examples=50)
def test_petrinet::transitionplacearc_instantiation(instance):
    assert isinstance(instance, petrinet::TransitionPlaceArc)

@given(instance=petrinet::PlaceTransitionArc_strategy)
@settings(max_examples=50)
def test_petrinet::placetransitionarc_instantiation(instance):
    assert isinstance(instance, petrinet::PlaceTransitionArc)

@given(instance=petrinet::Node_strategy)
@settings(max_examples=50)
def test_petrinet::node_instantiation(instance):
    assert isinstance(instance, petrinet::Node)

@given(instance=petrinet::Node_strategy)
def test_petrinet::node_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petrinet::Node_strategy)
def test_petrinet::node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petrinet::Arc_strategy)
@settings(max_examples=50)
def test_petrinet::arc_instantiation(instance):
    assert isinstance(instance, petrinet::Arc)

@given(instance=petrinet::Arc_strategy)
def test_petrinet::arc_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=petrinet::Arc_strategy)
def test_petrinet::arc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=petrinet::PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet::petrinet_instantiation(instance):
    assert isinstance(instance, petrinet::PetriNet)

@given(instance=petrinet::PetriNet_strategy)
def test_petrinet::petrinet_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petrinet::PetriNet_strategy)
def test_petrinet::petrinet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=petrinet::Transition_strategy)
@settings(max_examples=50)
def test_petrinet::transition_instantiation(instance):
    assert isinstance(instance, petrinet::Transition)

@given(instance=petrinet::Place_strategy)
@settings(max_examples=50)
def test_petrinet::place_instantiation(instance):
    assert isinstance(instance, petrinet::Place)

@given(instance=petrinet::Place_strategy)
def test_petrinet::place_capacity_type(instance):
    assert isinstance(instance.capacity, int)


@given(instance=petrinet::Place_strategy)
def test_petrinet::place_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original

@given(instance=petrinet::Place_strategy)
def test_petrinet::place_tokens_type(instance):
    assert isinstance(instance.tokens, int)


@given(instance=petrinet::Place_strategy)
def test_petrinet::place_tokens_setter(instance):
    original = instance.tokens
    instance.tokens = original
    assert instance.tokens == original
