import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ElementType,
    graph::NodeType,
    Element,
    graph::Edge,
    graph::Node,
    graph::ElementType,
    graph::Graph,
    graph::Element,
    graph::EdgeType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_elementtype_is_not_abstract():
    assert not inspect.isabstract(ElementType)


def test_elementtype_constructor_exists():
    assert callable(ElementType.__init__)


def test_elementtype_constructor_args():
    sig = inspect.signature(ElementType.__init__)
    params = list(sig.parameters.keys())



def test_graph::nodetype_is_not_abstract():
    assert not inspect.isabstract(graph::NodeType)


def test_graph::nodetype_constructor_exists():
    assert callable(graph::NodeType.__init__)


def test_graph::nodetype_constructor_args():
    sig = inspect.signature(graph::NodeType.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_graph::edge_is_not_abstract():
    assert not inspect.isabstract(graph::Edge)


def test_graph::edge_constructor_exists():
    assert callable(graph::Edge.__init__)


def test_graph::edge_constructor_args():
    sig = inspect.signature(graph::Edge.__init__)
    params = list(sig.parameters.keys())



def test_graph::node_is_not_abstract():
    assert not inspect.isabstract(graph::Node)


def test_graph::node_constructor_exists():
    assert callable(graph::Node.__init__)


def test_graph::node_constructor_args():
    sig = inspect.signature(graph::Node.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_graph::node_has_label():
    assert hasattr(graph::Node, "label")
    descriptor = None
    for klass in graph::Node.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_graph::elementtype_is_not_abstract():
    assert not inspect.isabstract(graph::ElementType)


def test_graph::elementtype_constructor_exists():
    assert callable(graph::ElementType.__init__)


def test_graph::elementtype_constructor_args():
    sig = inspect.signature(graph::ElementType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_graph::elementtype_has_name():
    assert hasattr(graph::ElementType, "name")
    descriptor = None
    for klass in graph::ElementType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_graph::graph_is_not_abstract():
    assert not inspect.isabstract(graph::Graph)


def test_graph::graph_constructor_exists():
    assert callable(graph::Graph.__init__)


def test_graph::graph_constructor_args():
    sig = inspect.signature(graph::Graph.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_graph::graph_has_name():
    assert hasattr(graph::Graph, "name")
    descriptor = None
    for klass in graph::Graph.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_graph::element_is_not_abstract():
    assert not inspect.isabstract(graph::Element)


def test_graph::element_constructor_exists():
    assert callable(graph::Element.__init__)


def test_graph::element_constructor_args():
    sig = inspect.signature(graph::Element.__init__)
    params = list(sig.parameters.keys())



def test_graph::edgetype_is_not_abstract():
    assert not inspect.isabstract(graph::EdgeType)


def test_graph::edgetype_constructor_exists():
    assert callable(graph::EdgeType.__init__)


def test_graph::edgetype_constructor_args():
    sig = inspect.signature(graph::EdgeType.__init__)
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
ElementType_strategy = st.builds(
    ElementType,
)
graph::NodeType_strategy = st.builds(
    graph::NodeType,
)
Element_strategy = st.builds(
    Element,
)
graph::Edge_strategy = st.builds(
    graph::Edge,
)
graph::Node_strategy = st.builds(
    graph::Node,
    label=
        safe_text
)
graph::ElementType_strategy = st.builds(
    graph::ElementType,
    name=
        safe_text
)
graph::Graph_strategy = st.builds(
    graph::Graph,
    name=
        safe_text
)
graph::Element_strategy = st.builds(
    graph::Element,
)
graph::EdgeType_strategy = st.builds(
    graph::EdgeType,
)

@given(instance=ElementType_strategy)
@settings(max_examples=50)
def test_elementtype_instantiation(instance):
    assert isinstance(instance, ElementType)

@given(instance=graph::NodeType_strategy)
@settings(max_examples=50)
def test_graph::nodetype_instantiation(instance):
    assert isinstance(instance, graph::NodeType)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=graph::Edge_strategy)
@settings(max_examples=50)
def test_graph::edge_instantiation(instance):
    assert isinstance(instance, graph::Edge)

@given(instance=graph::Node_strategy)
@settings(max_examples=50)
def test_graph::node_instantiation(instance):
    assert isinstance(instance, graph::Node)

@given(instance=graph::Node_strategy)
def test_graph::node_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=graph::Node_strategy)
def test_graph::node_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=graph::ElementType_strategy)
@settings(max_examples=50)
def test_graph::elementtype_instantiation(instance):
    assert isinstance(instance, graph::ElementType)

@given(instance=graph::ElementType_strategy)
def test_graph::elementtype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=graph::ElementType_strategy)
def test_graph::elementtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=graph::Graph_strategy)
@settings(max_examples=50)
def test_graph::graph_instantiation(instance):
    assert isinstance(instance, graph::Graph)

@given(instance=graph::Graph_strategy)
def test_graph::graph_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=graph::Graph_strategy)
def test_graph::graph_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=graph::Element_strategy)
@settings(max_examples=50)
def test_graph::element_instantiation(instance):
    assert isinstance(instance, graph::Element)

@given(instance=graph::EdgeType_strategy)
@settings(max_examples=50)
def test_graph::edgetype_instantiation(instance):
    assert isinstance(instance, graph::EdgeType)
