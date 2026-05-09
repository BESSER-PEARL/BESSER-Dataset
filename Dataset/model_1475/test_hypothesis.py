import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    NamedElement,
    Graph::GraphElement,
    Graph::Graph,
    Graph::NamedElement,
    GraphElement,
    Graph::DirectedArc,
    Graph::Node,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_graph::graphelement_is_not_abstract():
    assert not inspect.isabstract(Graph::GraphElement)


def test_graph::graphelement_constructor_exists():
    assert callable(Graph::GraphElement.__init__)


def test_graph::graphelement_constructor_args():
    sig = inspect.signature(Graph::GraphElement.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "label" in params, "Missing parameter 'label'"

def test_graph::graphelement_has_color():
    assert hasattr(Graph::GraphElement, "color")
    descriptor = None
    for klass in Graph::GraphElement.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_graph::graphelement_has_label():
    assert hasattr(Graph::GraphElement, "label")
    descriptor = None
    for klass in Graph::GraphElement.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_graph::graph_is_not_abstract():
    assert not inspect.isabstract(Graph::Graph)


def test_graph::graph_constructor_exists():
    assert callable(Graph::Graph.__init__)


def test_graph::graph_constructor_args():
    sig = inspect.signature(Graph::Graph.__init__)
    params = list(sig.parameters.keys())



def test_graph::namedelement_is_not_abstract():
    assert not inspect.isabstract(Graph::NamedElement)


def test_graph::namedelement_constructor_exists():
    assert callable(Graph::NamedElement.__init__)


def test_graph::namedelement_constructor_args():
    sig = inspect.signature(Graph::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_graph::namedelement_has_name():
    assert hasattr(Graph::NamedElement, "name")
    descriptor = None
    for klass in Graph::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_graphelement_is_not_abstract():
    assert not inspect.isabstract(GraphElement)


def test_graphelement_constructor_exists():
    assert callable(GraphElement.__init__)


def test_graphelement_constructor_args():
    sig = inspect.signature(GraphElement.__init__)
    params = list(sig.parameters.keys())



def test_graph::directedarc_is_not_abstract():
    assert not inspect.isabstract(Graph::DirectedArc)


def test_graph::directedarc_constructor_exists():
    assert callable(Graph::DirectedArc.__init__)


def test_graph::directedarc_constructor_args():
    sig = inspect.signature(Graph::DirectedArc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_graph::directedarc_has_weight():
    assert hasattr(Graph::DirectedArc, "weight")
    descriptor = None
    for klass in Graph::DirectedArc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_graph::node_is_not_abstract():
    assert not inspect.isabstract(Graph::Node)


def test_graph::node_constructor_exists():
    assert callable(Graph::Node.__init__)


def test_graph::node_constructor_args():
    sig = inspect.signature(Graph::Node.__init__)
    params = list(sig.parameters.keys())
    assert "shape" in params, "Missing parameter 'shape'"
    assert "style" in params, "Missing parameter 'style'"

def test_graph::node_has_shape():
    assert hasattr(Graph::Node, "shape")
    descriptor = None
    for klass in Graph::Node.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)

def test_graph::node_has_style():
    assert hasattr(Graph::Node, "style")
    descriptor = None
    for klass in Graph::Node.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
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
NamedElement_strategy = st.builds(
    NamedElement,
)
Graph::GraphElement_strategy = st.builds(
    Graph::GraphElement,
    color=
        safe_text,
    label=
        safe_text
)
Graph::Graph_strategy = st.builds(
    Graph::Graph,
)
Graph::NamedElement_strategy = st.builds(
    Graph::NamedElement,
    name=
        safe_text
)
GraphElement_strategy = st.builds(
    GraphElement,
)
Graph::DirectedArc_strategy = st.builds(
    Graph::DirectedArc,
    weight=
        st.integers()
)
Graph::Node_strategy = st.builds(
    Graph::Node,
    shape=
        safe_text,
    style=
        safe_text
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=Graph::GraphElement_strategy)
@settings(max_examples=50)
def test_graph::graphelement_instantiation(instance):
    assert isinstance(instance, Graph::GraphElement)

@given(instance=Graph::GraphElement_strategy)
def test_graph::graphelement_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=Graph::GraphElement_strategy)
def test_graph::graphelement_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=Graph::GraphElement_strategy)
def test_graph::graphelement_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=Graph::GraphElement_strategy)
def test_graph::graphelement_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=Graph::Graph_strategy)
@settings(max_examples=50)
def test_graph::graph_instantiation(instance):
    assert isinstance(instance, Graph::Graph)

@given(instance=Graph::NamedElement_strategy)
@settings(max_examples=50)
def test_graph::namedelement_instantiation(instance):
    assert isinstance(instance, Graph::NamedElement)

@given(instance=Graph::NamedElement_strategy)
def test_graph::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Graph::NamedElement_strategy)
def test_graph::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=GraphElement_strategy)
@settings(max_examples=50)
def test_graphelement_instantiation(instance):
    assert isinstance(instance, GraphElement)

@given(instance=Graph::DirectedArc_strategy)
@settings(max_examples=50)
def test_graph::directedarc_instantiation(instance):
    assert isinstance(instance, Graph::DirectedArc)

@given(instance=Graph::DirectedArc_strategy)
def test_graph::directedarc_weight_type(instance):
    assert isinstance(instance.weight, int)


@given(instance=Graph::DirectedArc_strategy)
def test_graph::directedarc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=Graph::Node_strategy)
@settings(max_examples=50)
def test_graph::node_instantiation(instance):
    assert isinstance(instance, Graph::Node)

@given(instance=Graph::Node_strategy)
def test_graph::node_shape_type(instance):
    assert isinstance(instance.shape, str)


@given(instance=Graph::Node_strategy)
def test_graph::node_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original

@given(instance=Graph::Node_strategy)
def test_graph::node_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=Graph::Node_strategy)
def test_graph::node_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original
