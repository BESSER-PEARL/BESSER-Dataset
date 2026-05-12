import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    GraphElement,
    Graph_DirectedArc,
    Graph_Node,
    NamedElement,
    Graph_GraphElement,
    Graph_Graph,
    Graph_NamedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_graphelement_is_not_abstract():
    assert not inspect.isabstract(GraphElement)


def test_graphelement_constructor_exists():
    assert callable(GraphElement.__init__)


def test_graphelement_constructor_args():
    sig = inspect.signature(GraphElement.__init__)
    params = list(sig.parameters.keys())



def test_graph_directedarc_is_not_abstract():
    assert not inspect.isabstract(Graph_DirectedArc)


def test_graph_directedarc_constructor_exists():
    assert callable(Graph_DirectedArc.__init__)


def test_graph_directedarc_constructor_args():
    sig = inspect.signature(Graph_DirectedArc.__init__)
    params = list(sig.parameters.keys())
    assert "weight" in params, "Missing parameter 'weight'"

def test_graph_directedarc_has_weight():
    assert hasattr(Graph_DirectedArc, "weight")
    descriptor = None
    for klass in Graph_DirectedArc.__mro__:
        if "weight" in klass.__dict__:
            descriptor = klass.__dict__["weight"]
            break
    assert isinstance(descriptor, property)



def test_graph_node_is_not_abstract():
    assert not inspect.isabstract(Graph_Node)


def test_graph_node_constructor_exists():
    assert callable(Graph_Node.__init__)


def test_graph_node_constructor_args():
    sig = inspect.signature(Graph_Node.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "shape" in params, "Missing parameter 'shape'"

def test_graph_node_has_style():
    assert hasattr(Graph_Node, "style")
    descriptor = None
    for klass in Graph_Node.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_graph_node_has_shape():
    assert hasattr(Graph_Node, "shape")
    descriptor = None
    for klass in Graph_Node.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_graph_graphelement_is_not_abstract():
    assert not inspect.isabstract(Graph_GraphElement)


def test_graph_graphelement_constructor_exists():
    assert callable(Graph_GraphElement.__init__)


def test_graph_graphelement_constructor_args():
    sig = inspect.signature(Graph_GraphElement.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "color" in params, "Missing parameter 'color'"

def test_graph_graphelement_has_label():
    assert hasattr(Graph_GraphElement, "label")
    descriptor = None
    for klass in Graph_GraphElement.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_graph_graphelement_has_color():
    assert hasattr(Graph_GraphElement, "color")
    descriptor = None
    for klass in Graph_GraphElement.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_graph_graph_is_not_abstract():
    assert not inspect.isabstract(Graph_Graph)


def test_graph_graph_constructor_exists():
    assert callable(Graph_Graph.__init__)


def test_graph_graph_constructor_args():
    sig = inspect.signature(Graph_Graph.__init__)
    params = list(sig.parameters.keys())



def test_graph_namedelement_is_not_abstract():
    assert not inspect.isabstract(Graph_NamedElement)


def test_graph_namedelement_constructor_exists():
    assert callable(Graph_NamedElement.__init__)


def test_graph_namedelement_constructor_args():
    sig = inspect.signature(Graph_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_graph_namedelement_has_name():
    assert hasattr(Graph_NamedElement, "name")
    descriptor = None
    for klass in Graph_NamedElement.__mro__:
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
GraphElement_strategy = st.builds(
    GraphElement,
)
Graph_DirectedArc_strategy = st.builds(
    Graph_DirectedArc,
    weight=
        st.integers()
)
Graph_Node_strategy = st.builds(
    Graph_Node,
    style=
        safe_text,
    shape=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
Graph_GraphElement_strategy = st.builds(
    Graph_GraphElement,
    label=
        safe_text,
    color=
        safe_text
)
Graph_Graph_strategy = st.builds(
    Graph_Graph,
)
Graph_NamedElement_strategy = st.builds(
    Graph_NamedElement,
    name=
        safe_text
)

@given(instance=GraphElement_strategy)
@settings(max_examples=50)
def test_graphelement_instantiation(instance):
    assert isinstance(instance, GraphElement)

@given(instance=Graph_DirectedArc_strategy)
@settings(max_examples=50)
def test_graph_directedarc_instantiation(instance):
    assert isinstance(instance, Graph_DirectedArc)



@given(instance=Graph_DirectedArc_strategy)
def test_graph_directedarc_weight_setter(instance):
    original = instance.weight
    instance.weight = original
    assert instance.weight == original

@given(instance=Graph_Node_strategy)
@settings(max_examples=50)
def test_graph_node_instantiation(instance):
    assert isinstance(instance, Graph_Node)



@given(instance=Graph_Node_strategy)
def test_graph_node_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=Graph_Node_strategy)
def test_graph_node_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=Graph_GraphElement_strategy)
@settings(max_examples=50)
def test_graph_graphelement_instantiation(instance):
    assert isinstance(instance, Graph_GraphElement)



@given(instance=Graph_GraphElement_strategy)
def test_graph_graphelement_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=Graph_GraphElement_strategy)
def test_graph_graphelement_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=Graph_Graph_strategy)
@settings(max_examples=50)
def test_graph_graph_instantiation(instance):
    assert isinstance(instance, Graph_Graph)

@given(instance=Graph_NamedElement_strategy)
@settings(max_examples=50)
def test_graph_namedelement_instantiation(instance):
    assert isinstance(instance, Graph_NamedElement)



@given(instance=Graph_NamedElement_strategy)
def test_graph_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
