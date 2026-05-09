import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Node,
    petri::net::Place,
    petri::net::Transition,
    petri::net::Arc,
    petri::net::Node,
    petri::net::PetriNet,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_petri::net::place_is_not_abstract():
    assert not inspect.isabstract(petri::net::Place)


def test_petri::net::place_constructor_exists():
    assert callable(petri::net::Place.__init__)


def test_petri::net::place_constructor_args():
    sig = inspect.signature(petri::net::Place.__init__)
    params = list(sig.parameters.keys())



def test_petri::net::transition_is_not_abstract():
    assert not inspect.isabstract(petri::net::Transition)


def test_petri::net::transition_constructor_exists():
    assert callable(petri::net::Transition.__init__)


def test_petri::net::transition_constructor_args():
    sig = inspect.signature(petri::net::Transition.__init__)
    params = list(sig.parameters.keys())



def test_petri::net::arc_is_not_abstract():
    assert not inspect.isabstract(petri::net::Arc)


def test_petri::net::arc_constructor_exists():
    assert callable(petri::net::Arc.__init__)


def test_petri::net::arc_constructor_args():
    sig = inspect.signature(petri::net::Arc.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petri::net::arc_has_name():
    assert hasattr(petri::net::Arc, "name")
    descriptor = None
    for klass in petri::net::Arc.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petri::net::node_is_not_abstract():
    assert not inspect.isabstract(petri::net::Node)


def test_petri::net::node_constructor_exists():
    assert callable(petri::net::Node.__init__)


def test_petri::net::node_constructor_args():
    sig = inspect.signature(petri::net::Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petri::net::node_has_name():
    assert hasattr(petri::net::Node, "name")
    descriptor = None
    for klass in petri::net::Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petri::net::petrinet_is_not_abstract():
    assert not inspect.isabstract(petri::net::PetriNet)


def test_petri::net::petrinet_constructor_exists():
    assert callable(petri::net::PetriNet.__init__)


def test_petri::net::petrinet_constructor_args():
    sig = inspect.signature(petri::net::PetriNet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petri::net::petrinet_has_name():
    assert hasattr(petri::net::PetriNet, "name")
    descriptor = None
    for klass in petri::net::PetriNet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
Node_strategy = st.builds(
    Node,
)
petri::net::Place_strategy = st.builds(
    petri::net::Place,
)
petri::net::Transition_strategy = st.builds(
    petri::net::Transition,
)
petri::net::Arc_strategy = st.builds(
    petri::net::Arc,
    name=
        safe_text
)
petri::net::Node_strategy = st.builds(
    petri::net::Node,
    name=
        safe_text
)
petri::net::PetriNet_strategy = st.builds(
    petri::net::PetriNet,
    name=
        safe_text
)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=petri::net::Place_strategy)
@settings(max_examples=50)
def test_petri::net::place_instantiation(instance):
    assert isinstance(instance, petri::net::Place)

@given(instance=petri::net::Transition_strategy)
@settings(max_examples=50)
def test_petri::net::transition_instantiation(instance):
    assert isinstance(instance, petri::net::Transition)

@given(instance=petri::net::Arc_strategy)
@settings(max_examples=50)
def test_petri::net::arc_instantiation(instance):
    assert isinstance(instance, petri::net::Arc)

@given(instance=petri::net::Arc_strategy)
def test_petri::net::arc_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petri::net::Arc_strategy)
def test_petri::net::arc_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petri::net::Node_strategy)
@settings(max_examples=50)
def test_petri::net::node_instantiation(instance):
    assert isinstance(instance, petri::net::Node)

@given(instance=petri::net::Node_strategy)
def test_petri::net::node_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petri::net::Node_strategy)
def test_petri::net::node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=petri::net::PetriNet_strategy)
@settings(max_examples=50)
def test_petri::net::petrinet_instantiation(instance):
    assert isinstance(instance, petri::net::PetriNet)

@given(instance=petri::net::PetriNet_strategy)
def test_petri::net::petrinet_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=petri::net::PetriNet_strategy)
def test_petri::net::petrinet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
