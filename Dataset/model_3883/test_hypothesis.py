import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    graph_G,
    Node,
    graph_Boundary,
    graph_Center,
    graph_Node,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_graph_g_is_not_abstract():
    assert not inspect.isabstract(graph_G)


def test_graph_g_constructor_exists():
    assert callable(graph_G.__init__)


def test_graph_g_constructor_args():
    sig = inspect.signature(graph_G.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_graph_boundary_is_not_abstract():
    assert not inspect.isabstract(graph_Boundary)


def test_graph_boundary_constructor_exists():
    assert callable(graph_Boundary.__init__)


def test_graph_boundary_constructor_args():
    sig = inspect.signature(graph_Boundary.__init__)
    params = list(sig.parameters.keys())



def test_graph_center_is_not_abstract():
    assert not inspect.isabstract(graph_Center)


def test_graph_center_constructor_exists():
    assert callable(graph_Center.__init__)


def test_graph_center_constructor_args():
    sig = inspect.signature(graph_Center.__init__)
    params = list(sig.parameters.keys())



def test_graph_node_is_not_abstract():
    assert not inspect.isabstract(graph_Node)


def test_graph_node_constructor_exists():
    assert callable(graph_Node.__init__)


def test_graph_node_constructor_args():
    sig = inspect.signature(graph_Node.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_graph_node_has_id():
    assert hasattr(graph_Node, "id")
    descriptor = None
    for klass in graph_Node.__mro__:
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
graph_G_strategy = st.builds(
    graph_G,
)
Node_strategy = st.builds(
    Node,
)
graph_Boundary_strategy = st.builds(
    graph_Boundary,
)
graph_Center_strategy = st.builds(
    graph_Center,
)
graph_Node_strategy = st.builds(
    graph_Node,
    id=
        safe_text
)

@given(instance=graph_G_strategy)
@settings(max_examples=50)
def test_graph_g_instantiation(instance):
    assert isinstance(instance, graph_G)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=graph_Boundary_strategy)
@settings(max_examples=50)
def test_graph_boundary_instantiation(instance):
    assert isinstance(instance, graph_Boundary)

@given(instance=graph_Center_strategy)
@settings(max_examples=50)
def test_graph_center_instantiation(instance):
    assert isinstance(instance, graph_Center)

@given(instance=graph_Node_strategy)
@settings(max_examples=50)
def test_graph_node_instantiation(instance):
    assert isinstance(instance, graph_Node)



@given(instance=graph_Node_strategy)
def test_graph_node_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
