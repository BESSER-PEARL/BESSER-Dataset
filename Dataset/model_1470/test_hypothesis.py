import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    graph_Edge,
    graph_Node,
    graph_GraphModel,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_graph_edge_is_not_abstract():
    assert not inspect.isabstract(graph_Edge)


def test_graph_edge_constructor_exists():
    assert callable(graph_Edge.__init__)


def test_graph_edge_constructor_args():
    sig = inspect.signature(graph_Edge.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_graph_edge_has_label():
    assert hasattr(graph_Edge, "label")
    descriptor = None
    for klass in graph_Edge.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_graph_node_is_not_abstract():
    assert not inspect.isabstract(graph_Node)


def test_graph_node_constructor_exists():
    assert callable(graph_Node.__init__)


def test_graph_node_constructor_args():
    sig = inspect.signature(graph_Node.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_graph_node_has_value():
    assert hasattr(graph_Node, "value")
    descriptor = None
    for klass in graph_Node.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_graph_graphmodel_is_not_abstract():
    assert not inspect.isabstract(graph_GraphModel)


def test_graph_graphmodel_constructor_exists():
    assert callable(graph_GraphModel.__init__)


def test_graph_graphmodel_constructor_args():
    sig = inspect.signature(graph_GraphModel.__init__)
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
graph_Edge_strategy = st.builds(
    graph_Edge,
    label=
        safe_text
)
graph_Node_strategy = st.builds(
    graph_Node,
    value=
        safe_text
)
graph_GraphModel_strategy = st.builds(
    graph_GraphModel,
)

@given(instance=graph_Edge_strategy)
@settings(max_examples=50)
def test_graph_edge_instantiation(instance):
    assert isinstance(instance, graph_Edge)



@given(instance=graph_Edge_strategy)
def test_graph_edge_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=graph_Node_strategy)
@settings(max_examples=50)
def test_graph_node_instantiation(instance):
    assert isinstance(instance, graph_Node)



@given(instance=graph_Node_strategy)
def test_graph_node_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=graph_GraphModel_strategy)
@settings(max_examples=50)
def test_graph_graphmodel_instantiation(instance):
    assert isinstance(instance, graph_GraphModel)
