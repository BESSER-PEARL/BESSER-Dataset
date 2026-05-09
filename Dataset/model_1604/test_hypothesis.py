import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Edge,
    PetrinetDSL::TPEdge,
    PetrinetDSL::PTEdge,
    Node,
    PetrinetDSL::Place,
    PetrinetDSL::Transition,
    PetrinetDSL::Token,
    Petrinet,
    PetrinetDSL::Edge,
    PetrinetDSL::Node,
    PetrinetDSL::Petrinet,
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



def test_petrinetdsl::tpedge_is_not_abstract():
    assert not inspect.isabstract(PetrinetDSL::TPEdge)


def test_petrinetdsl::tpedge_constructor_exists():
    assert callable(PetrinetDSL::TPEdge.__init__)


def test_petrinetdsl::tpedge_constructor_args():
    sig = inspect.signature(PetrinetDSL::TPEdge.__init__)
    params = list(sig.parameters.keys())



def test_petrinetdsl::ptedge_is_not_abstract():
    assert not inspect.isabstract(PetrinetDSL::PTEdge)


def test_petrinetdsl::ptedge_constructor_exists():
    assert callable(PetrinetDSL::PTEdge.__init__)


def test_petrinetdsl::ptedge_constructor_args():
    sig = inspect.signature(PetrinetDSL::PTEdge.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_petrinetdsl::place_is_not_abstract():
    assert not inspect.isabstract(PetrinetDSL::Place)


def test_petrinetdsl::place_constructor_exists():
    assert callable(PetrinetDSL::Place.__init__)


def test_petrinetdsl::place_constructor_args():
    sig = inspect.signature(PetrinetDSL::Place.__init__)
    params = list(sig.parameters.keys())



def test_petrinetdsl::transition_is_not_abstract():
    assert not inspect.isabstract(PetrinetDSL::Transition)


def test_petrinetdsl::transition_constructor_exists():
    assert callable(PetrinetDSL::Transition.__init__)


def test_petrinetdsl::transition_constructor_args():
    sig = inspect.signature(PetrinetDSL::Transition.__init__)
    params = list(sig.parameters.keys())



def test_petrinetdsl::token_is_not_abstract():
    assert not inspect.isabstract(PetrinetDSL::Token)


def test_petrinetdsl::token_constructor_exists():
    assert callable(PetrinetDSL::Token.__init__)


def test_petrinetdsl::token_constructor_args():
    sig = inspect.signature(PetrinetDSL::Token.__init__)
    params = list(sig.parameters.keys())



def test_petrinet_is_not_abstract():
    assert not inspect.isabstract(Petrinet)


def test_petrinet_constructor_exists():
    assert callable(Petrinet.__init__)


def test_petrinet_constructor_args():
    sig = inspect.signature(Petrinet.__init__)
    params = list(sig.parameters.keys())



def test_petrinetdsl::edge_is_not_abstract():
    assert not inspect.isabstract(PetrinetDSL::Edge)


def test_petrinetdsl::edge_constructor_exists():
    assert callable(PetrinetDSL::Edge.__init__)


def test_petrinetdsl::edge_constructor_args():
    sig = inspect.signature(PetrinetDSL::Edge.__init__)
    params = list(sig.parameters.keys())



def test_petrinetdsl::node_is_not_abstract():
    assert not inspect.isabstract(PetrinetDSL::Node)


def test_petrinetdsl::node_constructor_exists():
    assert callable(PetrinetDSL::Node.__init__)


def test_petrinetdsl::node_constructor_args():
    sig = inspect.signature(PetrinetDSL::Node.__init__)
    params = list(sig.parameters.keys())



def test_petrinetdsl::petrinet_is_not_abstract():
    assert not inspect.isabstract(PetrinetDSL::Petrinet)


def test_petrinetdsl::petrinet_constructor_exists():
    assert callable(PetrinetDSL::Petrinet.__init__)


def test_petrinetdsl::petrinet_constructor_args():
    sig = inspect.signature(PetrinetDSL::Petrinet.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"

def test_petrinetdsl::petrinet_has_description():
    assert hasattr(PetrinetDSL::Petrinet, "description")
    descriptor = None
    for klass in PetrinetDSL::Petrinet.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_petrinetdsl::petrinet_has_name():
    assert hasattr(PetrinetDSL::Petrinet, "name")
    descriptor = None
    for klass in PetrinetDSL::Petrinet.__mro__:
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
Edge_strategy = st.builds(
    Edge,
)
PetrinetDSL::TPEdge_strategy = st.builds(
    PetrinetDSL::TPEdge,
)
PetrinetDSL::PTEdge_strategy = st.builds(
    PetrinetDSL::PTEdge,
)
Node_strategy = st.builds(
    Node,
)
PetrinetDSL::Place_strategy = st.builds(
    PetrinetDSL::Place,
)
PetrinetDSL::Transition_strategy = st.builds(
    PetrinetDSL::Transition,
)
PetrinetDSL::Token_strategy = st.builds(
    PetrinetDSL::Token,
)
Petrinet_strategy = st.builds(
    Petrinet,
)
PetrinetDSL::Edge_strategy = st.builds(
    PetrinetDSL::Edge,
)
PetrinetDSL::Node_strategy = st.builds(
    PetrinetDSL::Node,
)
PetrinetDSL::Petrinet_strategy = st.builds(
    PetrinetDSL::Petrinet,
    description=
        safe_text,
    name=
        safe_text
)

@given(instance=Edge_strategy)
@settings(max_examples=50)
def test_edge_instantiation(instance):
    assert isinstance(instance, Edge)

@given(instance=PetrinetDSL::TPEdge_strategy)
@settings(max_examples=50)
def test_petrinetdsl::tpedge_instantiation(instance):
    assert isinstance(instance, PetrinetDSL::TPEdge)

@given(instance=PetrinetDSL::PTEdge_strategy)
@settings(max_examples=50)
def test_petrinetdsl::ptedge_instantiation(instance):
    assert isinstance(instance, PetrinetDSL::PTEdge)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=PetrinetDSL::Place_strategy)
@settings(max_examples=50)
def test_petrinetdsl::place_instantiation(instance):
    assert isinstance(instance, PetrinetDSL::Place)

@given(instance=PetrinetDSL::Transition_strategy)
@settings(max_examples=50)
def test_petrinetdsl::transition_instantiation(instance):
    assert isinstance(instance, PetrinetDSL::Transition)

@given(instance=PetrinetDSL::Token_strategy)
@settings(max_examples=50)
def test_petrinetdsl::token_instantiation(instance):
    assert isinstance(instance, PetrinetDSL::Token)

@given(instance=Petrinet_strategy)
@settings(max_examples=50)
def test_petrinet_instantiation(instance):
    assert isinstance(instance, Petrinet)

@given(instance=PetrinetDSL::Edge_strategy)
@settings(max_examples=50)
def test_petrinetdsl::edge_instantiation(instance):
    assert isinstance(instance, PetrinetDSL::Edge)

@given(instance=PetrinetDSL::Node_strategy)
@settings(max_examples=50)
def test_petrinetdsl::node_instantiation(instance):
    assert isinstance(instance, PetrinetDSL::Node)

@given(instance=PetrinetDSL::Petrinet_strategy)
@settings(max_examples=50)
def test_petrinetdsl::petrinet_instantiation(instance):
    assert isinstance(instance, PetrinetDSL::Petrinet)

@given(instance=PetrinetDSL::Petrinet_strategy)
def test_petrinetdsl::petrinet_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=PetrinetDSL::Petrinet_strategy)
def test_petrinetdsl::petrinet_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=PetrinetDSL::Petrinet_strategy)
def test_petrinetdsl::petrinet_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=PetrinetDSL::Petrinet_strategy)
def test_petrinetdsl::petrinet_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
