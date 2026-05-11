import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    GraphElement,
    Dot::DirectedArc,
    Dot::Node,
    NamedElement,
    Dot::GraphElement,
    Dot::Graph,
    Dot::NamedElement,
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



def test_dot::directedarc_is_not_abstract():
    assert not inspect.isabstract(Dot::DirectedArc)


def test_dot::directedarc_constructor_exists():
    assert callable(Dot::DirectedArc.__init__)


def test_dot::directedarc_constructor_args():
    sig = inspect.signature(Dot::DirectedArc.__init__)
    params = list(sig.parameters.keys())



def test_dot::node_is_not_abstract():
    assert not inspect.isabstract(Dot::Node)


def test_dot::node_constructor_exists():
    assert callable(Dot::Node.__init__)


def test_dot::node_constructor_args():
    sig = inspect.signature(Dot::Node.__init__)
    params = list(sig.parameters.keys())
    assert "shape" in params, "Missing parameter 'shape'"
    assert "style" in params, "Missing parameter 'style'"

def test_dot::node_has_shape():
    assert hasattr(Dot::Node, "shape")
    descriptor = None
    for klass in Dot::Node.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)

def test_dot::node_has_style():
    assert hasattr(Dot::Node, "style")
    descriptor = None
    for klass in Dot::Node.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_dot::graphelement_is_not_abstract():
    assert not inspect.isabstract(Dot::GraphElement)


def test_dot::graphelement_constructor_exists():
    assert callable(Dot::GraphElement.__init__)


def test_dot::graphelement_constructor_args():
    sig = inspect.signature(Dot::GraphElement.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "label" in params, "Missing parameter 'label'"

def test_dot::graphelement_has_color():
    assert hasattr(Dot::GraphElement, "color")
    descriptor = None
    for klass in Dot::GraphElement.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_dot::graphelement_has_label():
    assert hasattr(Dot::GraphElement, "label")
    descriptor = None
    for klass in Dot::GraphElement.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_dot::graph_is_not_abstract():
    assert not inspect.isabstract(Dot::Graph)


def test_dot::graph_constructor_exists():
    assert callable(Dot::Graph.__init__)


def test_dot::graph_constructor_args():
    sig = inspect.signature(Dot::Graph.__init__)
    params = list(sig.parameters.keys())



def test_dot::namedelement_is_not_abstract():
    assert not inspect.isabstract(Dot::NamedElement)


def test_dot::namedelement_constructor_exists():
    assert callable(Dot::NamedElement.__init__)


def test_dot::namedelement_constructor_args():
    sig = inspect.signature(Dot::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dot::namedelement_has_name():
    assert hasattr(Dot::NamedElement, "name")
    descriptor = None
    for klass in Dot::NamedElement.__mro__:
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
Dot::DirectedArc_strategy = st.builds(
    Dot::DirectedArc,
)
Dot::Node_strategy = st.builds(
    Dot::Node,
    shape=
        safe_text,
    style=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
Dot::GraphElement_strategy = st.builds(
    Dot::GraphElement,
    color=
        safe_text,
    label=
        safe_text
)
Dot::Graph_strategy = st.builds(
    Dot::Graph,
)
Dot::NamedElement_strategy = st.builds(
    Dot::NamedElement,
    name=
        safe_text
)

@given(instance=GraphElement_strategy)
@settings(max_examples=50)
def test_graphelement_instantiation(instance):
    assert isinstance(instance, GraphElement)

@given(instance=Dot::DirectedArc_strategy)
@settings(max_examples=50)
def test_dot::directedarc_instantiation(instance):
    assert isinstance(instance, Dot::DirectedArc)

@given(instance=Dot::Node_strategy)
@settings(max_examples=50)
def test_dot::node_instantiation(instance):
    assert isinstance(instance, Dot::Node)

@given(instance=Dot::Node_strategy)
def test_dot::node_shape_type(instance):
    assert isinstance(instance.shape, str)


@given(instance=Dot::Node_strategy)
def test_dot::node_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original

@given(instance=Dot::Node_strategy)
def test_dot::node_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=Dot::Node_strategy)
def test_dot::node_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=Dot::GraphElement_strategy)
@settings(max_examples=50)
def test_dot::graphelement_instantiation(instance):
    assert isinstance(instance, Dot::GraphElement)

@given(instance=Dot::GraphElement_strategy)
def test_dot::graphelement_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=Dot::GraphElement_strategy)
def test_dot::graphelement_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=Dot::GraphElement_strategy)
def test_dot::graphelement_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=Dot::GraphElement_strategy)
def test_dot::graphelement_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=Dot::Graph_strategy)
@settings(max_examples=50)
def test_dot::graph_instantiation(instance):
    assert isinstance(instance, Dot::Graph)

@given(instance=Dot::NamedElement_strategy)
@settings(max_examples=50)
def test_dot::namedelement_instantiation(instance):
    assert isinstance(instance, Dot::NamedElement)

@given(instance=Dot::NamedElement_strategy)
def test_dot::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Dot::NamedElement_strategy)
def test_dot::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
