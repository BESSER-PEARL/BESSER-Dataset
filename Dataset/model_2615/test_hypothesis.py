import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    GraphElement,
    grapho::GraphO,
    grapho::Edge,
    grapho::Node,
    grapho::GraphElement,
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



def test_grapho::grapho_is_not_abstract():
    assert not inspect.isabstract(grapho::GraphO)


def test_grapho::grapho_constructor_exists():
    assert callable(grapho::GraphO.__init__)


def test_grapho::grapho_constructor_args():
    sig = inspect.signature(grapho::GraphO.__init__)
    params = list(sig.parameters.keys())



def test_grapho::edge_is_not_abstract():
    assert not inspect.isabstract(grapho::Edge)


def test_grapho::edge_constructor_exists():
    assert callable(grapho::Edge.__init__)


def test_grapho::edge_constructor_args():
    sig = inspect.signature(grapho::Edge.__init__)
    params = list(sig.parameters.keys())
    assert "constraintRank" in params, "Missing parameter 'constraintRank'"
    assert "color" in params, "Missing parameter 'color'"
    assert "style" in params, "Missing parameter 'style'"

def test_grapho::edge_has_constraintRank():
    assert hasattr(grapho::Edge, "constraintRank")
    descriptor = None
    for klass in grapho::Edge.__mro__:
        if "constraintRank" in klass.__dict__:
            descriptor = klass.__dict__["constraintRank"]
            break
    assert isinstance(descriptor, property)

def test_grapho::edge_has_color():
    assert hasattr(grapho::Edge, "color")
    descriptor = None
    for klass in grapho::Edge.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_grapho::edge_has_style():
    assert hasattr(grapho::Edge, "style")
    descriptor = None
    for klass in grapho::Edge.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)



def test_grapho::node_is_not_abstract():
    assert not inspect.isabstract(grapho::Node)


def test_grapho::node_constructor_exists():
    assert callable(grapho::Node.__init__)


def test_grapho::node_constructor_args():
    sig = inspect.signature(grapho::Node.__init__)
    params = list(sig.parameters.keys())
    assert "shape" in params, "Missing parameter 'shape'"
    assert "color" in params, "Missing parameter 'color'"
    assert "style" in params, "Missing parameter 'style'"
    assert "label" in params, "Missing parameter 'label'"

def test_grapho::node_has_shape():
    assert hasattr(grapho::Node, "shape")
    descriptor = None
    for klass in grapho::Node.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)

def test_grapho::node_has_color():
    assert hasattr(grapho::Node, "color")
    descriptor = None
    for klass in grapho::Node.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_grapho::node_has_style():
    assert hasattr(grapho::Node, "style")
    descriptor = None
    for klass in grapho::Node.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_grapho::node_has_label():
    assert hasattr(grapho::Node, "label")
    descriptor = None
    for klass in grapho::Node.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_grapho::graphelement_is_not_abstract():
    assert not inspect.isabstract(grapho::GraphElement)


def test_grapho::graphelement_constructor_exists():
    assert callable(grapho::GraphElement.__init__)


def test_grapho::graphelement_constructor_args():
    sig = inspect.signature(grapho::GraphElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_grapho::graphelement_has_name():
    assert hasattr(grapho::GraphElement, "name")
    descriptor = None
    for klass in grapho::GraphElement.__mro__:
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
grapho::GraphO_strategy = st.builds(
    grapho::GraphO,
)
grapho::Edge_strategy = st.builds(
    grapho::Edge,
    constraintRank=
        st.booleans(),
    color=
        safe_text,
    style=
        safe_text
)
grapho::Node_strategy = st.builds(
    grapho::Node,
    shape=
        safe_text,
    color=
        safe_text,
    style=
        safe_text,
    label=
        safe_text
)
grapho::GraphElement_strategy = st.builds(
    grapho::GraphElement,
    name=
        safe_text
)

@given(instance=GraphElement_strategy)
@settings(max_examples=50)
def test_graphelement_instantiation(instance):
    assert isinstance(instance, GraphElement)

@given(instance=grapho::GraphO_strategy)
@settings(max_examples=50)
def test_grapho::grapho_instantiation(instance):
    assert isinstance(instance, grapho::GraphO)

@given(instance=grapho::Edge_strategy)
@settings(max_examples=50)
def test_grapho::edge_instantiation(instance):
    assert isinstance(instance, grapho::Edge)

@given(instance=grapho::Edge_strategy)
def test_grapho::edge_constraintRank_type(instance):
    assert isinstance(instance.constraintRank, bool)


@given(instance=grapho::Edge_strategy)
def test_grapho::edge_constraintRank_setter(instance):
    original = instance.constraintRank
    instance.constraintRank = original
    assert instance.constraintRank == original

@given(instance=grapho::Edge_strategy)
def test_grapho::edge_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=grapho::Edge_strategy)
def test_grapho::edge_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=grapho::Edge_strategy)
def test_grapho::edge_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=grapho::Edge_strategy)
def test_grapho::edge_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=grapho::Node_strategy)
@settings(max_examples=50)
def test_grapho::node_instantiation(instance):
    assert isinstance(instance, grapho::Node)

@given(instance=grapho::Node_strategy)
def test_grapho::node_shape_type(instance):
    assert isinstance(instance.shape, str)


@given(instance=grapho::Node_strategy)
def test_grapho::node_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original

@given(instance=grapho::Node_strategy)
def test_grapho::node_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=grapho::Node_strategy)
def test_grapho::node_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=grapho::Node_strategy)
def test_grapho::node_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=grapho::Node_strategy)
def test_grapho::node_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=grapho::Node_strategy)
def test_grapho::node_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=grapho::Node_strategy)
def test_grapho::node_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=grapho::GraphElement_strategy)
@settings(max_examples=50)
def test_grapho::graphelement_instantiation(instance):
    assert isinstance(instance, grapho::GraphElement)

@given(instance=grapho::GraphElement_strategy)
def test_grapho::graphelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=grapho::GraphElement_strategy)
def test_grapho::graphelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
