import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    graph::G,
    Node,
    graph::Boundary,
    graph::Center,
    graph::Node,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_graph::g_is_not_abstract():
    assert not inspect.isabstract(graph::G)


def test_graph::g_constructor_exists():
    assert callable(graph::G.__init__)


def test_graph::g_constructor_args():
    sig = inspect.signature(graph::G.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_graph::boundary_is_not_abstract():
    assert not inspect.isabstract(graph::Boundary)


def test_graph::boundary_constructor_exists():
    assert callable(graph::Boundary.__init__)


def test_graph::boundary_constructor_args():
    sig = inspect.signature(graph::Boundary.__init__)
    params = list(sig.parameters.keys())



def test_graph::center_is_not_abstract():
    assert not inspect.isabstract(graph::Center)


def test_graph::center_constructor_exists():
    assert callable(graph::Center.__init__)


def test_graph::center_constructor_args():
    sig = inspect.signature(graph::Center.__init__)
    params = list(sig.parameters.keys())



def test_graph::node_is_not_abstract():
    assert not inspect.isabstract(graph::Node)


def test_graph::node_constructor_exists():
    assert callable(graph::Node.__init__)


def test_graph::node_constructor_args():
    sig = inspect.signature(graph::Node.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_graph::node_has_id():
    assert hasattr(graph::Node, "id")
    descriptor = None
    for klass in graph::Node.__mro__:
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
graph::G_strategy = st.builds(
    graph::G,
)
Node_strategy = st.builds(
    Node,
)
graph::Boundary_strategy = st.builds(
    graph::Boundary,
)
graph::Center_strategy = st.builds(
    graph::Center,
)
graph::Node_strategy = st.builds(
    graph::Node,
    id=
        safe_text
)

@given(instance=graph::G_strategy)
@settings(max_examples=50)
def test_graph::g_instantiation(instance):
    assert isinstance(instance, graph::G)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=graph::Boundary_strategy)
@settings(max_examples=50)
def test_graph::boundary_instantiation(instance):
    assert isinstance(instance, graph::Boundary)

@given(instance=graph::Center_strategy)
@settings(max_examples=50)
def test_graph::center_instantiation(instance):
    assert isinstance(instance, graph::Center)

@given(instance=graph::Node_strategy)
@settings(max_examples=50)
def test_graph::node_instantiation(instance):
    assert isinstance(instance, graph::Node)

@given(instance=graph::Node_strategy)
def test_graph::node_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=graph::Node_strategy)
def test_graph::node_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
