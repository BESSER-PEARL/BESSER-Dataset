import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Element,
    graphdb::Property,
    graphdb::GraphElement,
    graphdb::Element,
    graphdb::Graph,
    GraphElement,
    graphdb::Vertex,
    graphdb::Edge,
    PrimitiveType,
    DatabaseKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_element_is_not_abstract():
    assert not inspect.isabstract(Element)


def test_element_constructor_exists():
    assert callable(Element.__init__)


def test_element_constructor_args():
    sig = inspect.signature(Element.__init__)
    params = list(sig.parameters.keys())



def test_graphdb::property_is_not_abstract():
    assert not inspect.isabstract(graphdb::Property)


def test_graphdb::property_constructor_exists():
    assert callable(graphdb::Property.__init__)


def test_graphdb::property_constructor_args():
    sig = inspect.signature(graphdb::Property.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "type" in params, "Missing parameter 'type'"

def test_graphdb::property_has_key():
    assert hasattr(graphdb::Property, "key")
    descriptor = None
    for klass in graphdb::Property.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_graphdb::property_has_type():
    assert hasattr(graphdb::Property, "type")
    descriptor = None
    for klass in graphdb::Property.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_graphdb::graphelement_is_not_abstract():
    assert not inspect.isabstract(graphdb::GraphElement)


def test_graphdb::graphelement_constructor_exists():
    assert callable(graphdb::GraphElement.__init__)


def test_graphdb::graphelement_constructor_args():
    sig = inspect.signature(graphdb::GraphElement.__init__)
    params = list(sig.parameters.keys())



def test_graphdb::element_is_not_abstract():
    assert not inspect.isabstract(graphdb::Element)


def test_graphdb::element_constructor_exists():
    assert callable(graphdb::Element.__init__)


def test_graphdb::element_constructor_args():
    sig = inspect.signature(graphdb::Element.__init__)
    params = list(sig.parameters.keys())



def test_graphdb::graph_is_not_abstract():
    assert not inspect.isabstract(graphdb::Graph)


def test_graphdb::graph_constructor_exists():
    assert callable(graphdb::Graph.__init__)


def test_graphdb::graph_constructor_args():
    sig = inspect.signature(graphdb::Graph.__init__)
    params = list(sig.parameters.keys())
    assert "rawDatabase" in params, "Missing parameter 'rawDatabase'"

def test_graphdb::graph_has_rawDatabase():
    assert hasattr(graphdb::Graph, "rawDatabase")
    descriptor = None
    for klass in graphdb::Graph.__mro__:
        if "rawDatabase" in klass.__dict__:
            descriptor = klass.__dict__["rawDatabase"]
            break
    assert isinstance(descriptor, property)



def test_graphelement_is_not_abstract():
    assert not inspect.isabstract(GraphElement)


def test_graphelement_constructor_exists():
    assert callable(GraphElement.__init__)


def test_graphelement_constructor_args():
    sig = inspect.signature(GraphElement.__init__)
    params = list(sig.parameters.keys())



def test_graphdb::vertex_is_not_abstract():
    assert not inspect.isabstract(graphdb::Vertex)


def test_graphdb::vertex_constructor_exists():
    assert callable(graphdb::Vertex.__init__)


def test_graphdb::vertex_constructor_args():
    sig = inspect.signature(graphdb::Vertex.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "labels" in params, "Missing parameter 'labels'"

def test_graphdb::vertex_has_name():
    assert hasattr(graphdb::Vertex, "name")
    descriptor = None
    for klass in graphdb::Vertex.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_graphdb::vertex_has_labels():
    assert hasattr(graphdb::Vertex, "labels")
    descriptor = None
    for klass in graphdb::Vertex.__mro__:
        if "labels" in klass.__dict__:
            descriptor = klass.__dict__["labels"]
            break
    assert isinstance(descriptor, property)



def test_graphdb::edge_is_not_abstract():
    assert not inspect.isabstract(graphdb::Edge)


def test_graphdb::edge_constructor_exists():
    assert callable(graphdb::Edge.__init__)


def test_graphdb::edge_constructor_args():
    sig = inspect.signature(graphdb::Edge.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_graphdb::edge_has_type():
    assert hasattr(graphdb::Edge, "type")
    descriptor = None
    for klass in graphdb::Edge.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_graphdb::edge_has_name():
    assert hasattr(graphdb::Edge, "name")
    descriptor = None
    for klass in graphdb::Edge.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_primitivetype_exists():
    # Check that the Enumeration exists
    assert PrimitiveType is not None

def test_primitivetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrimitiveType]
    expected_literals = [
        "UmlToNoSQLID",
        "Object",
        "Boolean",
        "String",
        "Integer",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrimitiveType"

def test_databasekind_exists():
    # Check that the Enumeration exists
    assert DatabaseKind is not None

def test_databasekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DatabaseKind]
    expected_literals = [
        "GREMLIN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DatabaseKind"


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
Element_strategy = st.builds(
    Element,
)
graphdb::Property_strategy = st.builds(
    graphdb::Property,
    key=
        safe_text,
    type=
        safe_text
)
graphdb::GraphElement_strategy = st.builds(
    graphdb::GraphElement,
)
graphdb::Element_strategy = st.builds(
    graphdb::Element,
)
graphdb::Graph_strategy = st.builds(
    graphdb::Graph,
    rawDatabase=
        safe_text
)
GraphElement_strategy = st.builds(
    GraphElement,
)
graphdb::Vertex_strategy = st.builds(
    graphdb::Vertex,
    name=
        safe_text,
    labels=
        safe_text
)
graphdb::Edge_strategy = st.builds(
    graphdb::Edge,
    type=
        safe_text,
    name=
        safe_text
)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=graphdb::Property_strategy)
@settings(max_examples=50)
def test_graphdb::property_instantiation(instance):
    assert isinstance(instance, graphdb::Property)

@given(instance=graphdb::Property_strategy)
def test_graphdb::property_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=graphdb::Property_strategy)
def test_graphdb::property_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=graphdb::Property_strategy)
def test_graphdb::property_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=graphdb::Property_strategy)
def test_graphdb::property_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=graphdb::GraphElement_strategy)
@settings(max_examples=50)
def test_graphdb::graphelement_instantiation(instance):
    assert isinstance(instance, graphdb::GraphElement)

@given(instance=graphdb::Element_strategy)
@settings(max_examples=50)
def test_graphdb::element_instantiation(instance):
    assert isinstance(instance, graphdb::Element)

@given(instance=graphdb::Graph_strategy)
@settings(max_examples=50)
def test_graphdb::graph_instantiation(instance):
    assert isinstance(instance, graphdb::Graph)

@given(instance=graphdb::Graph_strategy)
def test_graphdb::graph_rawDatabase_type(instance):
    assert isinstance(instance.rawDatabase, str)


@given(instance=graphdb::Graph_strategy)
def test_graphdb::graph_rawDatabase_setter(instance):
    original = instance.rawDatabase
    instance.rawDatabase = original
    assert instance.rawDatabase == original

@given(instance=GraphElement_strategy)
@settings(max_examples=50)
def test_graphelement_instantiation(instance):
    assert isinstance(instance, GraphElement)

@given(instance=graphdb::Vertex_strategy)
@settings(max_examples=50)
def test_graphdb::vertex_instantiation(instance):
    assert isinstance(instance, graphdb::Vertex)

@given(instance=graphdb::Vertex_strategy)
def test_graphdb::vertex_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=graphdb::Vertex_strategy)
def test_graphdb::vertex_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=graphdb::Vertex_strategy)
def test_graphdb::vertex_labels_type(instance):
    assert isinstance(instance.labels, str)


@given(instance=graphdb::Vertex_strategy)
def test_graphdb::vertex_labels_setter(instance):
    original = instance.labels
    instance.labels = original
    assert instance.labels == original

@given(instance=graphdb::Edge_strategy)
@settings(max_examples=50)
def test_graphdb::edge_instantiation(instance):
    assert isinstance(instance, graphdb::Edge)

@given(instance=graphdb::Edge_strategy)
def test_graphdb::edge_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=graphdb::Edge_strategy)
def test_graphdb::edge_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=graphdb::Edge_strategy)
def test_graphdb::edge_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=graphdb::Edge_strategy)
def test_graphdb::edge_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
