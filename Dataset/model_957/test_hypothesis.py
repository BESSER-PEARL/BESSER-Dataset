import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ElementType,
    graph_NodeType,
    Element,
    graph_Edge,
    graph_Node,
    graph_ElementType,
    graph_Graph,
    graph_Element,
    graph_EdgeType,
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



def test_graph_nodetype_is_not_abstract():
    assert not inspect.isabstract(graph_NodeType)


def test_graph_nodetype_constructor_exists():
    assert callable(graph_NodeType.__init__)


def test_graph_nodetype_constructor_args():
    sig = inspect.signature(graph_NodeType.__init__)
    params = list(sig.parameters.keys())



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_graph_edge_is_not_abstract():
    assert not inspect.isabstract(graph_Edge)


def test_graph_edge_constructor_exists():
    assert callable(graph_Edge.__init__)


def test_graph_edge_constructor_args():
    sig = inspect.signature(graph_Edge.__init__)
    params = list(sig.parameters.keys())



def test_graph_node_is_not_abstract():
    assert not inspect.isabstract(graph_Node)


def test_graph_node_constructor_exists():
    assert callable(graph_Node.__init__)


def test_graph_node_constructor_args():
    sig = inspect.signature(graph_Node.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_graph_node_has_label():
    assert hasattr(graph_Node, "label")
    descriptor = None
    for klass in graph_Node.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_graph_elementtype_is_not_abstract():
    assert not inspect.isabstract(graph_ElementType)


def test_graph_elementtype_constructor_exists():
    assert callable(graph_ElementType.__init__)


def test_graph_elementtype_constructor_args():
    sig = inspect.signature(graph_ElementType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_graph_elementtype_has_name():
    assert hasattr(graph_ElementType, "name")
    descriptor = None
    for klass in graph_ElementType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_graph_graph_is_not_abstract():
    assert not inspect.isabstract(graph_Graph)


def test_graph_graph_constructor_exists():
    assert callable(graph_Graph.__init__)


def test_graph_graph_constructor_args():
    sig = inspect.signature(graph_Graph.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_graph_graph_has_name():
    assert hasattr(graph_Graph, "name")
    descriptor = None
    for klass in graph_Graph.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_graph_element_is_not_abstract():
    assert not inspect.isabstract(graph_Element)


def test_graph_element_constructor_exists():
    assert callable(graph_Element.__init__)


def test_graph_element_constructor_args():
    sig = inspect.signature(graph_Element.__init__)
    params = list(sig.parameters.keys())



def test_graph_edgetype_is_not_abstract():
    assert not inspect.isabstract(graph_EdgeType)


def test_graph_edgetype_constructor_exists():
    assert callable(graph_EdgeType.__init__)


def test_graph_edgetype_constructor_args():
    sig = inspect.signature(graph_EdgeType.__init__)
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
graph_NodeType_strategy = st.builds(
    graph_NodeType,
)
Element_strategy = st.builds(
    Element,
)
graph_Edge_strategy = st.builds(
    graph_Edge,
)
graph_Node_strategy = st.builds(
    graph_Node,
    label=
        safe_text
)
graph_ElementType_strategy = st.builds(
    graph_ElementType,
    name=
        safe_text
)
graph_Graph_strategy = st.builds(
    graph_Graph,
    name=
        safe_text
)
graph_Element_strategy = st.builds(
    graph_Element,
)
graph_EdgeType_strategy = st.builds(
    graph_EdgeType,
)

@given(instance=ElementType_strategy)
@settings(max_examples=50)
def test_elementtype_instantiation(instance):
    assert isinstance(instance, ElementType)

@given(instance=graph_NodeType_strategy)
@settings(max_examples=50)
def test_graph_nodetype_instantiation(instance):
    assert isinstance(instance, graph_NodeType)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=graph_Edge_strategy)
@settings(max_examples=50)
def test_graph_edge_instantiation(instance):
    assert isinstance(instance, graph_Edge)

@given(instance=graph_Node_strategy)
@settings(max_examples=50)
def test_graph_node_instantiation(instance):
    assert isinstance(instance, graph_Node)



@given(instance=graph_Node_strategy)
def test_graph_node_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=graph_ElementType_strategy)
@settings(max_examples=50)
def test_graph_elementtype_instantiation(instance):
    assert isinstance(instance, graph_ElementType)



@given(instance=graph_ElementType_strategy)
def test_graph_elementtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=graph_Graph_strategy)
@settings(max_examples=50)
def test_graph_graph_instantiation(instance):
    assert isinstance(instance, graph_Graph)



@given(instance=graph_Graph_strategy)
def test_graph_graph_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=graph_Element_strategy)
@settings(max_examples=50)
def test_graph_element_instantiation(instance):
    assert isinstance(instance, graph_Element)

@given(instance=graph_EdgeType_strategy)
@settings(max_examples=50)
def test_graph_edgetype_instantiation(instance):
    assert isinstance(instance, graph_EdgeType)
