import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    PetriNets::Token,
    Node,
    PetriNets::Place,
    PetriNets::Transition,
    Object,
    PetriNets::Arc,
    PetriNets::Node,
    PetriNets::Object,
    PetriNets::PetriNet,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_petrinets::token_is_not_abstract():
    assert not inspect.isabstract(PetriNets::Token)


def test_petrinets::token_constructor_exists():
    assert callable(PetriNets::Token.__init__)


def test_petrinets::token_constructor_args():
    sig = inspect.signature(PetriNets::Token.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_petrinets::place_is_not_abstract():
    assert not inspect.isabstract(PetriNets::Place)


def test_petrinets::place_constructor_exists():
    assert callable(PetriNets::Place.__init__)


def test_petrinets::place_constructor_args():
    sig = inspect.signature(PetriNets::Place.__init__)
    params = list(sig.parameters.keys())
    assert "capacity" in params, "Missing parameter 'capacity'"

def test_petrinets::place_has_capacity():
    assert hasattr(PetriNets::Place, "capacity")
    descriptor = None
    for klass in PetriNets::Place.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
            break
    assert isinstance(descriptor, property)



def test_petrinets::transition_is_not_abstract():
    assert not inspect.isabstract(PetriNets::Transition)


def test_petrinets::transition_constructor_exists():
    assert callable(PetriNets::Transition.__init__)


def test_petrinets::transition_constructor_args():
    sig = inspect.signature(PetriNets::Transition.__init__)
    params = list(sig.parameters.keys())



def test_object_is_not_abstract():
    assert not inspect.isabstract(Object)


def test_object_constructor_exists():
    assert callable(Object.__init__)


def test_object_constructor_args():
    sig = inspect.signature(Object.__init__)
    params = list(sig.parameters.keys())



def test_petrinets::arc_is_not_abstract():
    assert not inspect.isabstract(PetriNets::Arc)


def test_petrinets::arc_constructor_exists():
    assert callable(PetriNets::Arc.__init__)


def test_petrinets::arc_constructor_args():
    sig = inspect.signature(PetriNets::Arc.__init__)
    params = list(sig.parameters.keys())



def test_petrinets::node_is_not_abstract():
    assert not inspect.isabstract(PetriNets::Node)


def test_petrinets::node_constructor_exists():
    assert callable(PetriNets::Node.__init__)


def test_petrinets::node_constructor_args():
    sig = inspect.signature(PetriNets::Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_petrinets::node_has_name():
    assert hasattr(PetriNets::Node, "name")
    descriptor = None
    for klass in PetriNets::Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_petrinets::object_is_not_abstract():
    assert not inspect.isabstract(PetriNets::Object)


def test_petrinets::object_constructor_exists():
    assert callable(PetriNets::Object.__init__)


def test_petrinets::object_constructor_args():
    sig = inspect.signature(PetriNets::Object.__init__)
    params = list(sig.parameters.keys())



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
PetriNets::Token_strategy = st.builds(
    PetriNets::Token,
)
Node_strategy = st.builds(
    Node,
)
PetriNets::Place_strategy = st.builds(
    PetriNets::Place,
    capacity=
        st.integers()
)
PetriNets::Transition_strategy = st.builds(
    PetriNets::Transition,
)
Object_strategy = st.builds(
    Object,
)
PetriNets::Arc_strategy = st.builds(
    PetriNets::Arc,
)
PetriNets::Node_strategy = st.builds(
    PetriNets::Node,
    name=
        safe_text
)
PetriNets::Object_strategy = st.builds(
    PetriNets::Object,
)
PetriNets::PetriNet_strategy = st.builds(
    PetriNets::PetriNet,
)

@given(instance=PetriNets::Token_strategy)
@settings(max_examples=50)
def test_petrinets::token_instantiation(instance):
    assert isinstance(instance, PetriNets::Token)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=PetriNets::Place_strategy)
@settings(max_examples=50)
def test_petrinets::place_instantiation(instance):
    assert isinstance(instance, PetriNets::Place)

@given(instance=PetriNets::Place_strategy)
def test_petrinets::place_capacity_type(instance):
    assert isinstance(instance.capacity, int)


@given(instance=PetriNets::Place_strategy)
def test_petrinets::place_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original

@given(instance=PetriNets::Transition_strategy)
@settings(max_examples=50)
def test_petrinets::transition_instantiation(instance):
    assert isinstance(instance, PetriNets::Transition)

@given(instance=Object_strategy)
@settings(max_examples=50)
def test_object_instantiation(instance):
    assert isinstance(instance, Object)

@given(instance=PetriNets::Arc_strategy)
@settings(max_examples=50)
def test_petrinets::arc_instantiation(instance):
    assert isinstance(instance, PetriNets::Arc)

@given(instance=PetriNets::Node_strategy)
@settings(max_examples=50)
def test_petrinets::node_instantiation(instance):
    assert isinstance(instance, PetriNets::Node)

@given(instance=PetriNets::Node_strategy)
def test_petrinets::node_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=PetriNets::Node_strategy)
def test_petrinets::node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=PetriNets::Object_strategy)
@settings(max_examples=50)
def test_petrinets::object_instantiation(instance):
    assert isinstance(instance, PetriNets::Object)

@given(instance=PetriNets::PetriNet_strategy)
@settings(max_examples=50)
def test_petrinets::petrinet_instantiation(instance):
    assert isinstance(instance, PetriNets::PetriNet)
