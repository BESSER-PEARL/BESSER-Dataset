import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Element,
    graphdb_Property,
    graphdb_GraphElement,
    graphdb_Element,
    graphdb_Graph,
    GraphElement,
    graphdb_Edge,
    graphdb_Vertex,
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



def test_graphdb_property_is_not_abstract():
    assert not inspect.isabstract(graphdb_Property)


def test_graphdb_property_constructor_exists():
    assert callable(graphdb_Property.__init__)


def test_graphdb_property_constructor_args():
    sig = inspect.signature(graphdb_Property.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "key" in params, "Missing parameter 'key'"

def test_graphdb_property_has_type():
    assert hasattr(graphdb_Property, "type")
    descriptor = None
    for klass in graphdb_Property.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_graphdb_property_has_key():
    assert hasattr(graphdb_Property, "key")
    descriptor = None
    for klass in graphdb_Property.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_graphdb_graphelement_is_not_abstract():
    assert not inspect.isabstract(graphdb_GraphElement)


def test_graphdb_graphelement_constructor_exists():
    assert callable(graphdb_GraphElement.__init__)


def test_graphdb_graphelement_constructor_args():
    sig = inspect.signature(graphdb_GraphElement.__init__)
    params = list(sig.parameters.keys())



def test_graphdb_element_is_not_abstract():
    assert not inspect.isabstract(graphdb_Element)


def test_graphdb_element_constructor_exists():
    assert callable(graphdb_Element.__init__)


def test_graphdb_element_constructor_args():
    sig = inspect.signature(graphdb_Element.__init__)
    params = list(sig.parameters.keys())



def test_graphdb_graph_is_not_abstract():
    assert not inspect.isabstract(graphdb_Graph)


def test_graphdb_graph_constructor_exists():
    assert callable(graphdb_Graph.__init__)


def test_graphdb_graph_constructor_args():
    sig = inspect.signature(graphdb_Graph.__init__)
    params = list(sig.parameters.keys())
    assert "rawDatabase" in params, "Missing parameter 'rawDatabase'"

def test_graphdb_graph_has_rawDatabase():
    assert hasattr(graphdb_Graph, "rawDatabase")
    descriptor = None
    for klass in graphdb_Graph.__mro__:
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



def test_graphdb_edge_is_not_abstract():
    assert not inspect.isabstract(graphdb_Edge)


def test_graphdb_edge_constructor_exists():
    assert callable(graphdb_Edge.__init__)


def test_graphdb_edge_constructor_args():
    sig = inspect.signature(graphdb_Edge.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_graphdb_edge_has_name():
    assert hasattr(graphdb_Edge, "name")
    descriptor = None
    for klass in graphdb_Edge.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_graphdb_edge_has_type():
    assert hasattr(graphdb_Edge, "type")
    descriptor = None
    for klass in graphdb_Edge.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_graphdb_vertex_is_not_abstract():
    assert not inspect.isabstract(graphdb_Vertex)


def test_graphdb_vertex_constructor_exists():
    assert callable(graphdb_Vertex.__init__)


def test_graphdb_vertex_constructor_args():
    sig = inspect.signature(graphdb_Vertex.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "labels" in params, "Missing parameter 'labels'"

def test_graphdb_vertex_has_name():
    assert hasattr(graphdb_Vertex, "name")
    descriptor = None
    for klass in graphdb_Vertex.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_graphdb_vertex_has_labels():
    assert hasattr(graphdb_Vertex, "labels")
    descriptor = None
    for klass in graphdb_Vertex.__mro__:
        if "labels" in klass.__dict__:
            descriptor = klass.__dict__["labels"]
            break
    assert isinstance(descriptor, property)

def test_primitivetype_exists():
    # Check that the Enumeration exists
    assert PrimitiveType is not None

def test_primitivetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrimitiveType]
    expected_literals = [
        "Integer",
        "UmlToNoSQLID",
        "Object",
        "String",
        "Boolean",
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
graphdb_Property_strategy = st.builds(
    graphdb_Property,
    type=
        safe_text,
    key=
        safe_text
)
graphdb_GraphElement_strategy = st.builds(
    graphdb_GraphElement,
)
graphdb_Element_strategy = st.builds(
    graphdb_Element,
)
graphdb_Graph_strategy = st.builds(
    graphdb_Graph,
    rawDatabase=
        safe_text
)
GraphElement_strategy = st.builds(
    GraphElement,
)
graphdb_Edge_strategy = st.builds(
    graphdb_Edge,
    name=
        safe_text,
    type=
        safe_text
)
graphdb_Vertex_strategy = st.builds(
    graphdb_Vertex,
    name=
        safe_text,
    labels=
        safe_text
)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=graphdb_Property_strategy)
@settings(max_examples=50)
def test_graphdb_property_instantiation(instance):
    assert isinstance(instance, graphdb_Property)



@given(instance=graphdb_Property_strategy)
def test_graphdb_property_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=graphdb_Property_strategy)
def test_graphdb_property_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=graphdb_GraphElement_strategy)
@settings(max_examples=50)
def test_graphdb_graphelement_instantiation(instance):
    assert isinstance(instance, graphdb_GraphElement)

@given(instance=graphdb_Element_strategy)
@settings(max_examples=50)
def test_graphdb_element_instantiation(instance):
    assert isinstance(instance, graphdb_Element)

@given(instance=graphdb_Graph_strategy)
@settings(max_examples=50)
def test_graphdb_graph_instantiation(instance):
    assert isinstance(instance, graphdb_Graph)



@given(instance=graphdb_Graph_strategy)
def test_graphdb_graph_rawDatabase_setter(instance):
    original = instance.rawDatabase
    instance.rawDatabase = original
    assert instance.rawDatabase == original

@given(instance=GraphElement_strategy)
@settings(max_examples=50)
def test_graphelement_instantiation(instance):
    assert isinstance(instance, GraphElement)

@given(instance=graphdb_Edge_strategy)
@settings(max_examples=50)
def test_graphdb_edge_instantiation(instance):
    assert isinstance(instance, graphdb_Edge)



@given(instance=graphdb_Edge_strategy)
def test_graphdb_edge_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=graphdb_Edge_strategy)
def test_graphdb_edge_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=graphdb_Vertex_strategy)
@settings(max_examples=50)
def test_graphdb_vertex_instantiation(instance):
    assert isinstance(instance, graphdb_Vertex)



@given(instance=graphdb_Vertex_strategy)
def test_graphdb_vertex_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=graphdb_Vertex_strategy)
def test_graphdb_vertex_labels_setter(instance):
    original = instance.labels
    instance.labels = original
    assert instance.labels == original
