import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    GraphElement,
    Dot_DirectedArc,
    Dot_Node,
    NamedElement,
    Dot_GraphElement,
    Dot_Graph,
    Dot_NamedElement,
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



def test_dot_directedarc_is_not_abstract():
    assert not inspect.isabstract(Dot_DirectedArc)


def test_dot_directedarc_constructor_exists():
    assert callable(Dot_DirectedArc.__init__)


def test_dot_directedarc_constructor_args():
    sig = inspect.signature(Dot_DirectedArc.__init__)
    params = list(sig.parameters.keys())



def test_dot_node_is_not_abstract():
    assert not inspect.isabstract(Dot_Node)


def test_dot_node_constructor_exists():
    assert callable(Dot_Node.__init__)


def test_dot_node_constructor_args():
    sig = inspect.signature(Dot_Node.__init__)
    params = list(sig.parameters.keys())
    assert "shape" in params, "Missing parameter 'shape'"
    assert "style" in params, "Missing parameter 'style'"

def test_dot_node_has_shape():
    assert hasattr(Dot_Node, "shape")
    descriptor = None
    for klass in Dot_Node.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)

def test_dot_node_has_style():
    assert hasattr(Dot_Node, "style")
    descriptor = None
    for klass in Dot_Node.__mro__:
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



def test_dot_graphelement_is_not_abstract():
    assert not inspect.isabstract(Dot_GraphElement)


def test_dot_graphelement_constructor_exists():
    assert callable(Dot_GraphElement.__init__)


def test_dot_graphelement_constructor_args():
    sig = inspect.signature(Dot_GraphElement.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "label" in params, "Missing parameter 'label'"

def test_dot_graphelement_has_color():
    assert hasattr(Dot_GraphElement, "color")
    descriptor = None
    for klass in Dot_GraphElement.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_dot_graphelement_has_label():
    assert hasattr(Dot_GraphElement, "label")
    descriptor = None
    for klass in Dot_GraphElement.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_dot_graph_is_not_abstract():
    assert not inspect.isabstract(Dot_Graph)


def test_dot_graph_constructor_exists():
    assert callable(Dot_Graph.__init__)


def test_dot_graph_constructor_args():
    sig = inspect.signature(Dot_Graph.__init__)
    params = list(sig.parameters.keys())



def test_dot_namedelement_is_not_abstract():
    assert not inspect.isabstract(Dot_NamedElement)


def test_dot_namedelement_constructor_exists():
    assert callable(Dot_NamedElement.__init__)


def test_dot_namedelement_constructor_args():
    sig = inspect.signature(Dot_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dot_namedelement_has_name():
    assert hasattr(Dot_NamedElement, "name")
    descriptor = None
    for klass in Dot_NamedElement.__mro__:
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
Dot_DirectedArc_strategy = st.builds(
    Dot_DirectedArc,
)
Dot_Node_strategy = st.builds(
    Dot_Node,
    shape=
        safe_text,
    style=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
Dot_GraphElement_strategy = st.builds(
    Dot_GraphElement,
    color=
        safe_text,
    label=
        safe_text
)
Dot_Graph_strategy = st.builds(
    Dot_Graph,
)
Dot_NamedElement_strategy = st.builds(
    Dot_NamedElement,
    name=
        safe_text
)

@given(instance=GraphElement_strategy)
@settings(max_examples=50)
def test_graphelement_instantiation(instance):
    assert isinstance(instance, GraphElement)

@given(instance=Dot_DirectedArc_strategy)
@settings(max_examples=50)
def test_dot_directedarc_instantiation(instance):
    assert isinstance(instance, Dot_DirectedArc)

@given(instance=Dot_Node_strategy)
@settings(max_examples=50)
def test_dot_node_instantiation(instance):
    assert isinstance(instance, Dot_Node)



@given(instance=Dot_Node_strategy)
def test_dot_node_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original



@given(instance=Dot_Node_strategy)
def test_dot_node_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=Dot_GraphElement_strategy)
@settings(max_examples=50)
def test_dot_graphelement_instantiation(instance):
    assert isinstance(instance, Dot_GraphElement)



@given(instance=Dot_GraphElement_strategy)
def test_dot_graphelement_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=Dot_GraphElement_strategy)
def test_dot_graphelement_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=Dot_Graph_strategy)
@settings(max_examples=50)
def test_dot_graph_instantiation(instance):
    assert isinstance(instance, Dot_Graph)

@given(instance=Dot_NamedElement_strategy)
@settings(max_examples=50)
def test_dot_namedelement_instantiation(instance):
    assert isinstance(instance, Dot_NamedElement)



@given(instance=Dot_NamedElement_strategy)
def test_dot_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
