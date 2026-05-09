import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Node,
    petrinet::Place,
    petrinet::Transition,
    petrinet::PetriNet,
    Identifyable,
    petrinet::Arc,
    petrinet::Node,
    petrinet::Identifyable,
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



def test_petrinet::place_is_not_abstract():
    assert not inspect.isabstract(petrinet::Place)


def test_petrinet::place_constructor_exists():
    assert callable(petrinet::Place.__init__)


def test_petrinet::place_constructor_args():
    sig = inspect.signature(petrinet::Place.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::transition_is_not_abstract():
    assert not inspect.isabstract(petrinet::Transition)


def test_petrinet::transition_constructor_exists():
    assert callable(petrinet::Transition.__init__)


def test_petrinet::transition_constructor_args():
    sig = inspect.signature(petrinet::Transition.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::petrinet_is_not_abstract():
    assert not inspect.isabstract(petrinet::PetriNet)


def test_petrinet::petrinet_constructor_exists():
    assert callable(petrinet::PetriNet.__init__)


def test_petrinet::petrinet_constructor_args():
    sig = inspect.signature(petrinet::PetriNet.__init__)
    params = list(sig.parameters.keys())



def test_identifyable_is_not_abstract():
    assert not inspect.isabstract(Identifyable)


def test_identifyable_constructor_exists():
    assert callable(Identifyable.__init__)


def test_identifyable_constructor_args():
    sig = inspect.signature(Identifyable.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::arc_is_not_abstract():
    assert not inspect.isabstract(petrinet::Arc)


def test_petrinet::arc_constructor_exists():
    assert callable(petrinet::Arc.__init__)


def test_petrinet::arc_constructor_args():
    sig = inspect.signature(petrinet::Arc.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::node_is_not_abstract():
    assert not inspect.isabstract(petrinet::Node)


def test_petrinet::node_constructor_exists():
    assert callable(petrinet::Node.__init__)


def test_petrinet::node_constructor_args():
    sig = inspect.signature(petrinet::Node.__init__)
    params = list(sig.parameters.keys())



def test_petrinet::identifyable_is_not_abstract():
    assert not inspect.isabstract(petrinet::Identifyable)


def test_petrinet::identifyable_constructor_exists():
    assert callable(petrinet::Identifyable.__init__)


def test_petrinet::identifyable_constructor_args():
    sig = inspect.signature(petrinet::Identifyable.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_petrinet::identifyable_has_id():
    assert hasattr(petrinet::Identifyable, "id")
    descriptor = None
    for klass in petrinet::Identifyable.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
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
petrinet::Place_strategy = st.builds(
    petrinet::Place,
)
petrinet::Transition_strategy = st.builds(
    petrinet::Transition,
)
petrinet::PetriNet_strategy = st.builds(
    petrinet::PetriNet,
)
Identifyable_strategy = st.builds(
    Identifyable,
)
petrinet::Arc_strategy = st.builds(
    petrinet::Arc,
)
petrinet::Node_strategy = st.builds(
    petrinet::Node,
)
petrinet::Identifyable_strategy = st.builds(
    petrinet::Identifyable,
    id=
        safe_text
)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=petrinet::Place_strategy)
@settings(max_examples=50)
def test_petrinet::place_instantiation(instance):
    assert isinstance(instance, petrinet::Place)

@given(instance=petrinet::Transition_strategy)
@settings(max_examples=50)
def test_petrinet::transition_instantiation(instance):
    assert isinstance(instance, petrinet::Transition)

@given(instance=petrinet::PetriNet_strategy)
@settings(max_examples=50)
def test_petrinet::petrinet_instantiation(instance):
    assert isinstance(instance, petrinet::PetriNet)

@given(instance=Identifyable_strategy)
@settings(max_examples=50)
def test_identifyable_instantiation(instance):
    assert isinstance(instance, Identifyable)

@given(instance=petrinet::Arc_strategy)
@settings(max_examples=50)
def test_petrinet::arc_instantiation(instance):
    assert isinstance(instance, petrinet::Arc)

@given(instance=petrinet::Node_strategy)
@settings(max_examples=50)
def test_petrinet::node_instantiation(instance):
    assert isinstance(instance, petrinet::Node)

@given(instance=petrinet::Identifyable_strategy)
@settings(max_examples=50)
def test_petrinet::identifyable_instantiation(instance):
    assert isinstance(instance, petrinet::Identifyable)

@given(instance=petrinet::Identifyable_strategy)
def test_petrinet::identifyable_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=petrinet::Identifyable_strategy)
def test_petrinet::identifyable_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
