import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Element,
    GraphML::Graph,
    GraphML::Key,
    Data,
    Edge,
    GraphML::Node,
    EndPoint,
    GraphML::HyperEdge,
    Port,
    Node,
    GraphML::Edge,
    Graph,
    Key,
    LocatedElement,
    GraphML::Element,
    GraphML::Data,
    GraphML::Port,
    GraphML::EndPoint,
    GraphML::Root,
    GraphML::LocatedElement,
    AttrType,
    ElemType,
    EdgeType,
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



def test_graphml::graph_is_not_abstract():
    assert not inspect.isabstract(GraphML::Graph)


def test_graphml::graph_constructor_exists():
    assert callable(GraphML::Graph.__init__)


def test_graphml::graph_constructor_args():
    sig = inspect.signature(GraphML::Graph.__init__)
    params = list(sig.parameters.keys())
    assert "edgeDefault" in params, "Missing parameter 'edgeDefault'"

def test_graphml::graph_has_edgeDefault():
    assert hasattr(GraphML::Graph, "edgeDefault")
    descriptor = None
    for klass in GraphML::Graph.__mro__:
        if "edgeDefault" in klass.__dict__:
            descriptor = klass.__dict__["edgeDefault"]
            break
    assert isinstance(descriptor, property)



def test_graphml::key_is_not_abstract():
    assert not inspect.isabstract(GraphML::Key)


def test_graphml::key_constructor_exists():
    assert callable(GraphML::Key.__init__)


def test_graphml::key_constructor_args():
    sig = inspect.signature(GraphML::Key.__init__)
    params = list(sig.parameters.keys())
    assert "for_" in params, "Missing parameter 'for_'"
    assert "type" in params, "Missing parameter 'type'"
    assert "attrName" in params, "Missing parameter 'attrName'"
    assert "defValue" in params, "Missing parameter 'defValue'"

def test_graphml::key_has_for_():
    assert hasattr(GraphML::Key, "for_")
    descriptor = None
    for klass in GraphML::Key.__mro__:
        if "for_" in klass.__dict__:
            descriptor = klass.__dict__["for_"]
            break
    assert isinstance(descriptor, property)

def test_graphml::key_has_type():
    assert hasattr(GraphML::Key, "type")
    descriptor = None
    for klass in GraphML::Key.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_graphml::key_has_attrName():
    assert hasattr(GraphML::Key, "attrName")
    descriptor = None
    for klass in GraphML::Key.__mro__:
        if "attrName" in klass.__dict__:
            descriptor = klass.__dict__["attrName"]
            break
    assert isinstance(descriptor, property)

def test_graphml::key_has_defValue():
    assert hasattr(GraphML::Key, "defValue")
    descriptor = None
    for klass in GraphML::Key.__mro__:
        if "defValue" in klass.__dict__:
            descriptor = klass.__dict__["defValue"]
            break
    assert isinstance(descriptor, property)



def test_data_is_not_abstract():
    assert not inspect.isabstract(Data)


def test_data_constructor_exists():
    assert callable(Data.__init__)


def test_data_constructor_args():
    sig = inspect.signature(Data.__init__)
    params = list(sig.parameters.keys())



def test_edge_is_not_abstract():
    assert not inspect.isabstract(Edge)


def test_edge_constructor_exists():
    assert callable(Edge.__init__)


def test_edge_constructor_args():
    sig = inspect.signature(Edge.__init__)
    params = list(sig.parameters.keys())



def test_graphml::node_is_not_abstract():
    assert not inspect.isabstract(GraphML::Node)


def test_graphml::node_constructor_exists():
    assert callable(GraphML::Node.__init__)


def test_graphml::node_constructor_args():
    sig = inspect.signature(GraphML::Node.__init__)
    params = list(sig.parameters.keys())



def test_endpoint_is_not_abstract():
    assert not inspect.isabstract(EndPoint)


def test_endpoint_constructor_exists():
    assert callable(EndPoint.__init__)


def test_endpoint_constructor_args():
    sig = inspect.signature(EndPoint.__init__)
    params = list(sig.parameters.keys())



def test_graphml::hyperedge_is_not_abstract():
    assert not inspect.isabstract(GraphML::HyperEdge)


def test_graphml::hyperedge_constructor_exists():
    assert callable(GraphML::HyperEdge.__init__)


def test_graphml::hyperedge_constructor_args():
    sig = inspect.signature(GraphML::HyperEdge.__init__)
    params = list(sig.parameters.keys())



def test_port_is_not_abstract():
    assert not inspect.isabstract(Port)


def test_port_constructor_exists():
    assert callable(Port.__init__)


def test_port_constructor_args():
    sig = inspect.signature(Port.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_graphml::edge_is_not_abstract():
    assert not inspect.isabstract(GraphML::Edge)


def test_graphml::edge_constructor_exists():
    assert callable(GraphML::Edge.__init__)


def test_graphml::edge_constructor_args():
    sig = inspect.signature(GraphML::Edge.__init__)
    params = list(sig.parameters.keys())
    assert "directed" in params, "Missing parameter 'directed'"

def test_graphml::edge_has_directed():
    assert hasattr(GraphML::Edge, "directed")
    descriptor = None
    for klass in GraphML::Edge.__mro__:
        if "directed" in klass.__dict__:
            descriptor = klass.__dict__["directed"]
            break
    assert isinstance(descriptor, property)



def test_graph_is_not_abstract():
    assert not inspect.isabstract(Graph)


def test_graph_constructor_exists():
    assert callable(Graph.__init__)


def test_graph_constructor_args():
    sig = inspect.signature(Graph.__init__)
    params = list(sig.parameters.keys())



def test_key_is_not_abstract():
    assert not inspect.isabstract(Key)


def test_key_constructor_exists():
    assert callable(Key.__init__)


def test_key_constructor_args():
    sig = inspect.signature(Key.__init__)
    params = list(sig.parameters.keys())



def test_locatedelement_is_not_abstract():
    assert not inspect.isabstract(LocatedElement)


def test_locatedelement_constructor_exists():
    assert callable(LocatedElement.__init__)


def test_locatedelement_constructor_args():
    sig = inspect.signature(LocatedElement.__init__)
    params = list(sig.parameters.keys())



def test_graphml::element_is_not_abstract():
    assert not inspect.isabstract(GraphML::Element)


def test_graphml::element_constructor_exists():
    assert callable(GraphML::Element.__init__)


def test_graphml::element_constructor_args():
    sig = inspect.signature(GraphML::Element.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_graphml::element_has_id():
    assert hasattr(GraphML::Element, "id")
    descriptor = None
    for klass in GraphML::Element.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_graphml::data_is_not_abstract():
    assert not inspect.isabstract(GraphML::Data)


def test_graphml::data_constructor_exists():
    assert callable(GraphML::Data.__init__)


def test_graphml::data_constructor_args():
    sig = inspect.signature(GraphML::Data.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_graphml::data_has_key():
    assert hasattr(GraphML::Data, "key")
    descriptor = None
    for klass in GraphML::Data.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_graphml::data_has_value():
    assert hasattr(GraphML::Data, "value")
    descriptor = None
    for klass in GraphML::Data.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_graphml::port_is_not_abstract():
    assert not inspect.isabstract(GraphML::Port)


def test_graphml::port_constructor_exists():
    assert callable(GraphML::Port.__init__)


def test_graphml::port_constructor_args():
    sig = inspect.signature(GraphML::Port.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_graphml::port_has_name():
    assert hasattr(GraphML::Port, "name")
    descriptor = None
    for klass in GraphML::Port.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_graphml::endpoint_is_not_abstract():
    assert not inspect.isabstract(GraphML::EndPoint)


def test_graphml::endpoint_constructor_exists():
    assert callable(GraphML::EndPoint.__init__)


def test_graphml::endpoint_constructor_args():
    sig = inspect.signature(GraphML::EndPoint.__init__)
    params = list(sig.parameters.keys())



def test_graphml::root_is_not_abstract():
    assert not inspect.isabstract(GraphML::Root)


def test_graphml::root_constructor_exists():
    assert callable(GraphML::Root.__init__)


def test_graphml::root_constructor_args():
    sig = inspect.signature(GraphML::Root.__init__)
    params = list(sig.parameters.keys())



def test_graphml::locatedelement_is_not_abstract():
    assert not inspect.isabstract(GraphML::LocatedElement)


def test_graphml::locatedelement_constructor_exists():
    assert callable(GraphML::LocatedElement.__init__)


def test_graphml::locatedelement_constructor_args():
    sig = inspect.signature(GraphML::LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "commentsAfter" in params, "Missing parameter 'commentsAfter'"
    assert "location" in params, "Missing parameter 'location'"
    assert "commentsBefore" in params, "Missing parameter 'commentsBefore'"

def test_graphml::locatedelement_has_commentsAfter():
    assert hasattr(GraphML::LocatedElement, "commentsAfter")
    descriptor = None
    for klass in GraphML::LocatedElement.__mro__:
        if "commentsAfter" in klass.__dict__:
            descriptor = klass.__dict__["commentsAfter"]
            break
    assert isinstance(descriptor, property)

def test_graphml::locatedelement_has_location():
    assert hasattr(GraphML::LocatedElement, "location")
    descriptor = None
    for klass in GraphML::LocatedElement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_graphml::locatedelement_has_commentsBefore():
    assert hasattr(GraphML::LocatedElement, "commentsBefore")
    descriptor = None
    for klass in GraphML::LocatedElement.__mro__:
        if "commentsBefore" in klass.__dict__:
            descriptor = klass.__dict__["commentsBefore"]
            break
    assert isinstance(descriptor, property)

def test_attrtype_exists():
    # Check that the Enumeration exists
    assert AttrType is not None

def test_attrtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AttrType]
    expected_literals = [
        "string",
        "integer",
        "double",
        "boolean",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AttrType"

def test_elemtype_exists():
    # Check that the Enumeration exists
    assert ElemType is not None

def test_elemtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ElemType]
    expected_literals = [
        "node",
        "graph",
        "edge",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ElemType"

def test_edgetype_exists():
    # Check that the Enumeration exists
    assert EdgeType is not None

def test_edgetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EdgeType]
    expected_literals = [
        "undirected",
        "directed",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EdgeType"


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
GraphML::Graph_strategy = st.builds(
    GraphML::Graph,
    edgeDefault=
        safe_text
)
GraphML::Key_strategy = st.builds(
    GraphML::Key,
    for_=
        safe_text,
    type=
        safe_text,
    attrName=
        safe_text,
    defValue=
        safe_text
)
Data_strategy = st.builds(
    Data,
)
Edge_strategy = st.builds(
    Edge,
)
GraphML::Node_strategy = st.builds(
    GraphML::Node,
)
EndPoint_strategy = st.builds(
    EndPoint,
)
GraphML::HyperEdge_strategy = st.builds(
    GraphML::HyperEdge,
)
Port_strategy = st.builds(
    Port,
)
Node_strategy = st.builds(
    Node,
)
GraphML::Edge_strategy = st.builds(
    GraphML::Edge,
    directed=
        safe_text
)
Graph_strategy = st.builds(
    Graph,
)
Key_strategy = st.builds(
    Key,
)
LocatedElement_strategy = st.builds(
    LocatedElement,
)
GraphML::Element_strategy = st.builds(
    GraphML::Element,
    id=
        safe_text
)
GraphML::Data_strategy = st.builds(
    GraphML::Data,
    key=
        safe_text,
    value=
        safe_text
)
GraphML::Port_strategy = st.builds(
    GraphML::Port,
    name=
        safe_text
)
GraphML::EndPoint_strategy = st.builds(
    GraphML::EndPoint,
)
GraphML::Root_strategy = st.builds(
    GraphML::Root,
)
GraphML::LocatedElement_strategy = st.builds(
    GraphML::LocatedElement,
    commentsAfter=
        safe_text,
    location=
        safe_text,
    commentsBefore=
        safe_text
)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=GraphML::Graph_strategy)
@settings(max_examples=50)
def test_graphml::graph_instantiation(instance):
    assert isinstance(instance, GraphML::Graph)

@given(instance=GraphML::Graph_strategy)
def test_graphml::graph_edgeDefault_type(instance):
    assert isinstance(instance.edgeDefault, str)


@given(instance=GraphML::Graph_strategy)
def test_graphml::graph_edgeDefault_setter(instance):
    original = instance.edgeDefault
    instance.edgeDefault = original
    assert instance.edgeDefault == original

@given(instance=GraphML::Key_strategy)
@settings(max_examples=50)
def test_graphml::key_instantiation(instance):
    assert isinstance(instance, GraphML::Key)

@given(instance=GraphML::Key_strategy)
def test_graphml::key_for__type(instance):
    assert isinstance(instance.for_, str)


@given(instance=GraphML::Key_strategy)
def test_graphml::key_for__setter(instance):
    original = instance.for_
    instance.for_ = original
    assert instance.for_ == original

@given(instance=GraphML::Key_strategy)
def test_graphml::key_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=GraphML::Key_strategy)
def test_graphml::key_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=GraphML::Key_strategy)
def test_graphml::key_attrName_type(instance):
    assert isinstance(instance.attrName, str)


@given(instance=GraphML::Key_strategy)
def test_graphml::key_attrName_setter(instance):
    original = instance.attrName
    instance.attrName = original
    assert instance.attrName == original

@given(instance=GraphML::Key_strategy)
def test_graphml::key_defValue_type(instance):
    assert isinstance(instance.defValue, str)


@given(instance=GraphML::Key_strategy)
def test_graphml::key_defValue_setter(instance):
    original = instance.defValue
    instance.defValue = original
    assert instance.defValue == original

@given(instance=Data_strategy)
@settings(max_examples=50)
def test_data_instantiation(instance):
    assert isinstance(instance, Data)

@given(instance=Edge_strategy)
@settings(max_examples=50)
def test_edge_instantiation(instance):
    assert isinstance(instance, Edge)

@given(instance=GraphML::Node_strategy)
@settings(max_examples=50)
def test_graphml::node_instantiation(instance):
    assert isinstance(instance, GraphML::Node)

@given(instance=EndPoint_strategy)
@settings(max_examples=50)
def test_endpoint_instantiation(instance):
    assert isinstance(instance, EndPoint)

@given(instance=GraphML::HyperEdge_strategy)
@settings(max_examples=50)
def test_graphml::hyperedge_instantiation(instance):
    assert isinstance(instance, GraphML::HyperEdge)

@given(instance=Port_strategy)
@settings(max_examples=50)
def test_port_instantiation(instance):
    assert isinstance(instance, Port)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=GraphML::Edge_strategy)
@settings(max_examples=50)
def test_graphml::edge_instantiation(instance):
    assert isinstance(instance, GraphML::Edge)

@given(instance=GraphML::Edge_strategy)
def test_graphml::edge_directed_type(instance):
    assert isinstance(instance.directed, str)


@given(instance=GraphML::Edge_strategy)
def test_graphml::edge_directed_setter(instance):
    original = instance.directed
    instance.directed = original
    assert instance.directed == original

@given(instance=Graph_strategy)
@settings(max_examples=50)
def test_graph_instantiation(instance):
    assert isinstance(instance, Graph)

@given(instance=Key_strategy)
@settings(max_examples=50)
def test_key_instantiation(instance):
    assert isinstance(instance, Key)

@given(instance=LocatedElement_strategy)
@settings(max_examples=50)
def test_locatedelement_instantiation(instance):
    assert isinstance(instance, LocatedElement)

@given(instance=GraphML::Element_strategy)
@settings(max_examples=50)
def test_graphml::element_instantiation(instance):
    assert isinstance(instance, GraphML::Element)

@given(instance=GraphML::Element_strategy)
def test_graphml::element_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=GraphML::Element_strategy)
def test_graphml::element_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=GraphML::Data_strategy)
@settings(max_examples=50)
def test_graphml::data_instantiation(instance):
    assert isinstance(instance, GraphML::Data)

@given(instance=GraphML::Data_strategy)
def test_graphml::data_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=GraphML::Data_strategy)
def test_graphml::data_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=GraphML::Data_strategy)
def test_graphml::data_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=GraphML::Data_strategy)
def test_graphml::data_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=GraphML::Port_strategy)
@settings(max_examples=50)
def test_graphml::port_instantiation(instance):
    assert isinstance(instance, GraphML::Port)

@given(instance=GraphML::Port_strategy)
def test_graphml::port_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=GraphML::Port_strategy)
def test_graphml::port_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=GraphML::EndPoint_strategy)
@settings(max_examples=50)
def test_graphml::endpoint_instantiation(instance):
    assert isinstance(instance, GraphML::EndPoint)

@given(instance=GraphML::Root_strategy)
@settings(max_examples=50)
def test_graphml::root_instantiation(instance):
    assert isinstance(instance, GraphML::Root)

@given(instance=GraphML::LocatedElement_strategy)
@settings(max_examples=50)
def test_graphml::locatedelement_instantiation(instance):
    assert isinstance(instance, GraphML::LocatedElement)

@given(instance=GraphML::LocatedElement_strategy)
def test_graphml::locatedelement_commentsAfter_type(instance):
    assert isinstance(instance.commentsAfter, str)


@given(instance=GraphML::LocatedElement_strategy)
def test_graphml::locatedelement_commentsAfter_setter(instance):
    original = instance.commentsAfter
    instance.commentsAfter = original
    assert instance.commentsAfter == original

@given(instance=GraphML::LocatedElement_strategy)
def test_graphml::locatedelement_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=GraphML::LocatedElement_strategy)
def test_graphml::locatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=GraphML::LocatedElement_strategy)
def test_graphml::locatedelement_commentsBefore_type(instance):
    assert isinstance(instance.commentsBefore, str)


@given(instance=GraphML::LocatedElement_strategy)
def test_graphml::locatedelement_commentsBefore_setter(instance):
    original = instance.commentsBefore
    instance.commentsBefore = original
    assert instance.commentsBefore == original
