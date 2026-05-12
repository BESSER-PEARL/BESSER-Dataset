import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Element,
    GraphML_Graph,
    GraphML_Key,
    Data,
    Edge,
    GraphML_Node,
    EndPoint,
    GraphML_HyperEdge,
    Port,
    Node,
    GraphML_Edge,
    Graph,
    Key,
    LocatedElement,
    GraphML_Element,
    GraphML_EndPoint,
    GraphML_Data,
    GraphML_Port,
    GraphML_Root,
    GraphML_LocatedElement,
    ElemType,
    AttrType,
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



def test_graphml_graph_is_not_abstract():
    assert not inspect.isabstract(GraphML_Graph)


def test_graphml_graph_constructor_exists():
    assert callable(GraphML_Graph.__init__)


def test_graphml_graph_constructor_args():
    sig = inspect.signature(GraphML_Graph.__init__)
    params = list(sig.parameters.keys())
    assert "edgeDefault" in params, "Missing parameter 'edgeDefault'"

def test_graphml_graph_has_edgeDefault():
    assert hasattr(GraphML_Graph, "edgeDefault")
    descriptor = None
    for klass in GraphML_Graph.__mro__:
        if "edgeDefault" in klass.__dict__:
            descriptor = klass.__dict__["edgeDefault"]
            break
    assert isinstance(descriptor, property)



def test_graphml_key_is_not_abstract():
    assert not inspect.isabstract(GraphML_Key)


def test_graphml_key_constructor_exists():
    assert callable(GraphML_Key.__init__)


def test_graphml_key_constructor_args():
    sig = inspect.signature(GraphML_Key.__init__)
    params = list(sig.parameters.keys())
    assert "defValue" in params, "Missing parameter 'defValue'"
    assert "attrName" in params, "Missing parameter 'attrName'"
    assert "for_" in params, "Missing parameter 'for_'"
    assert "type" in params, "Missing parameter 'type'"

def test_graphml_key_has_defValue():
    assert hasattr(GraphML_Key, "defValue")
    descriptor = None
    for klass in GraphML_Key.__mro__:
        if "defValue" in klass.__dict__:
            descriptor = klass.__dict__["defValue"]
            break
    assert isinstance(descriptor, property)

def test_graphml_key_has_attrName():
    assert hasattr(GraphML_Key, "attrName")
    descriptor = None
    for klass in GraphML_Key.__mro__:
        if "attrName" in klass.__dict__:
            descriptor = klass.__dict__["attrName"]
            break
    assert isinstance(descriptor, property)

def test_graphml_key_has_for_():
    assert hasattr(GraphML_Key, "for_")
    descriptor = None
    for klass in GraphML_Key.__mro__:
        if "for_" in klass.__dict__:
            descriptor = klass.__dict__["for_"]
            break
    assert isinstance(descriptor, property)

def test_graphml_key_has_type():
    assert hasattr(GraphML_Key, "type")
    descriptor = None
    for klass in GraphML_Key.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
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



def test_graphml_node_is_not_abstract():
    assert not inspect.isabstract(GraphML_Node)


def test_graphml_node_constructor_exists():
    assert callable(GraphML_Node.__init__)


def test_graphml_node_constructor_args():
    sig = inspect.signature(GraphML_Node.__init__)
    params = list(sig.parameters.keys())



def test_endpoint_is_not_abstract():
    assert not inspect.isabstract(EndPoint)


def test_endpoint_constructor_exists():
    assert callable(EndPoint.__init__)


def test_endpoint_constructor_args():
    sig = inspect.signature(EndPoint.__init__)
    params = list(sig.parameters.keys())



def test_graphml_hyperedge_is_not_abstract():
    assert not inspect.isabstract(GraphML_HyperEdge)


def test_graphml_hyperedge_constructor_exists():
    assert callable(GraphML_HyperEdge.__init__)


def test_graphml_hyperedge_constructor_args():
    sig = inspect.signature(GraphML_HyperEdge.__init__)
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



def test_graphml_edge_is_not_abstract():
    assert not inspect.isabstract(GraphML_Edge)


def test_graphml_edge_constructor_exists():
    assert callable(GraphML_Edge.__init__)


def test_graphml_edge_constructor_args():
    sig = inspect.signature(GraphML_Edge.__init__)
    params = list(sig.parameters.keys())
    assert "directed" in params, "Missing parameter 'directed'"

def test_graphml_edge_has_directed():
    assert hasattr(GraphML_Edge, "directed")
    descriptor = None
    for klass in GraphML_Edge.__mro__:
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



def test_graphml_element_is_not_abstract():
    assert not inspect.isabstract(GraphML_Element)


def test_graphml_element_constructor_exists():
    assert callable(GraphML_Element.__init__)


def test_graphml_element_constructor_args():
    sig = inspect.signature(GraphML_Element.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_graphml_element_has_id():
    assert hasattr(GraphML_Element, "id")
    descriptor = None
    for klass in GraphML_Element.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_graphml_endpoint_is_not_abstract():
    assert not inspect.isabstract(GraphML_EndPoint)


def test_graphml_endpoint_constructor_exists():
    assert callable(GraphML_EndPoint.__init__)


def test_graphml_endpoint_constructor_args():
    sig = inspect.signature(GraphML_EndPoint.__init__)
    params = list(sig.parameters.keys())



def test_graphml_data_is_not_abstract():
    assert not inspect.isabstract(GraphML_Data)


def test_graphml_data_constructor_exists():
    assert callable(GraphML_Data.__init__)


def test_graphml_data_constructor_args():
    sig = inspect.signature(GraphML_Data.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_graphml_data_has_key():
    assert hasattr(GraphML_Data, "key")
    descriptor = None
    for klass in GraphML_Data.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_graphml_data_has_value():
    assert hasattr(GraphML_Data, "value")
    descriptor = None
    for klass in GraphML_Data.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_graphml_port_is_not_abstract():
    assert not inspect.isabstract(GraphML_Port)


def test_graphml_port_constructor_exists():
    assert callable(GraphML_Port.__init__)


def test_graphml_port_constructor_args():
    sig = inspect.signature(GraphML_Port.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_graphml_port_has_name():
    assert hasattr(GraphML_Port, "name")
    descriptor = None
    for klass in GraphML_Port.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_graphml_root_is_not_abstract():
    assert not inspect.isabstract(GraphML_Root)


def test_graphml_root_constructor_exists():
    assert callable(GraphML_Root.__init__)


def test_graphml_root_constructor_args():
    sig = inspect.signature(GraphML_Root.__init__)
    params = list(sig.parameters.keys())



def test_graphml_locatedelement_is_not_abstract():
    assert not inspect.isabstract(GraphML_LocatedElement)


def test_graphml_locatedelement_constructor_exists():
    assert callable(GraphML_LocatedElement.__init__)


def test_graphml_locatedelement_constructor_args():
    sig = inspect.signature(GraphML_LocatedElement.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"
    assert "commentsBefore" in params, "Missing parameter 'commentsBefore'"
    assert "commentsAfter" in params, "Missing parameter 'commentsAfter'"

def test_graphml_locatedelement_has_location():
    assert hasattr(GraphML_LocatedElement, "location")
    descriptor = None
    for klass in GraphML_LocatedElement.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_graphml_locatedelement_has_commentsBefore():
    assert hasattr(GraphML_LocatedElement, "commentsBefore")
    descriptor = None
    for klass in GraphML_LocatedElement.__mro__:
        if "commentsBefore" in klass.__dict__:
            descriptor = klass.__dict__["commentsBefore"]
            break
    assert isinstance(descriptor, property)

def test_graphml_locatedelement_has_commentsAfter():
    assert hasattr(GraphML_LocatedElement, "commentsAfter")
    descriptor = None
    for klass in GraphML_LocatedElement.__mro__:
        if "commentsAfter" in klass.__dict__:
            descriptor = klass.__dict__["commentsAfter"]
            break
    assert isinstance(descriptor, property)

def test_elemtype_exists():
    # Check that the Enumeration exists
    assert ElemType is not None

def test_elemtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ElemType]
    expected_literals = [
        "edge",
        "node",
        "graph",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ElemType"

def test_attrtype_exists():
    # Check that the Enumeration exists
    assert AttrType is not None

def test_attrtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AttrType]
    expected_literals = [
        "integer",
        "boolean",
        "string",
        "double",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AttrType"

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
GraphML_Graph_strategy = st.builds(
    GraphML_Graph,
    edgeDefault=
        safe_text
)
GraphML_Key_strategy = st.builds(
    GraphML_Key,
    defValue=
        safe_text,
    attrName=
        safe_text,
    for_=
        safe_text,
    type=
        safe_text
)
Data_strategy = st.builds(
    Data,
)
Edge_strategy = st.builds(
    Edge,
)
GraphML_Node_strategy = st.builds(
    GraphML_Node,
)
EndPoint_strategy = st.builds(
    EndPoint,
)
GraphML_HyperEdge_strategy = st.builds(
    GraphML_HyperEdge,
)
Port_strategy = st.builds(
    Port,
)
Node_strategy = st.builds(
    Node,
)
GraphML_Edge_strategy = st.builds(
    GraphML_Edge,
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
GraphML_Element_strategy = st.builds(
    GraphML_Element,
    id=
        safe_text
)
GraphML_EndPoint_strategy = st.builds(
    GraphML_EndPoint,
)
GraphML_Data_strategy = st.builds(
    GraphML_Data,
    key=
        safe_text,
    value=
        safe_text
)
GraphML_Port_strategy = st.builds(
    GraphML_Port,
    name=
        safe_text
)
GraphML_Root_strategy = st.builds(
    GraphML_Root,
)
GraphML_LocatedElement_strategy = st.builds(
    GraphML_LocatedElement,
    location=
        safe_text,
    commentsBefore=
        safe_text,
    commentsAfter=
        safe_text
)

@given(instance=Element_strategy)
@settings(max_examples=50)
def test_element_instantiation(instance):
    assert isinstance(instance, Element)

@given(instance=GraphML_Graph_strategy)
@settings(max_examples=50)
def test_graphml_graph_instantiation(instance):
    assert isinstance(instance, GraphML_Graph)



@given(instance=GraphML_Graph_strategy)
def test_graphml_graph_edgeDefault_setter(instance):
    original = instance.edgeDefault
    instance.edgeDefault = original
    assert instance.edgeDefault == original

@given(instance=GraphML_Key_strategy)
@settings(max_examples=50)
def test_graphml_key_instantiation(instance):
    assert isinstance(instance, GraphML_Key)



@given(instance=GraphML_Key_strategy)
def test_graphml_key_defValue_setter(instance):
    original = instance.defValue
    instance.defValue = original
    assert instance.defValue == original



@given(instance=GraphML_Key_strategy)
def test_graphml_key_attrName_setter(instance):
    original = instance.attrName
    instance.attrName = original
    assert instance.attrName == original



@given(instance=GraphML_Key_strategy)
def test_graphml_key_for__setter(instance):
    original = instance.for_
    instance.for_ = original
    assert instance.for_ == original



@given(instance=GraphML_Key_strategy)
def test_graphml_key_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Data_strategy)
@settings(max_examples=50)
def test_data_instantiation(instance):
    assert isinstance(instance, Data)

@given(instance=Edge_strategy)
@settings(max_examples=50)
def test_edge_instantiation(instance):
    assert isinstance(instance, Edge)

@given(instance=GraphML_Node_strategy)
@settings(max_examples=50)
def test_graphml_node_instantiation(instance):
    assert isinstance(instance, GraphML_Node)

@given(instance=EndPoint_strategy)
@settings(max_examples=50)
def test_endpoint_instantiation(instance):
    assert isinstance(instance, EndPoint)

@given(instance=GraphML_HyperEdge_strategy)
@settings(max_examples=50)
def test_graphml_hyperedge_instantiation(instance):
    assert isinstance(instance, GraphML_HyperEdge)

@given(instance=Port_strategy)
@settings(max_examples=50)
def test_port_instantiation(instance):
    assert isinstance(instance, Port)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=GraphML_Edge_strategy)
@settings(max_examples=50)
def test_graphml_edge_instantiation(instance):
    assert isinstance(instance, GraphML_Edge)



@given(instance=GraphML_Edge_strategy)
def test_graphml_edge_directed_setter(instance):
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

@given(instance=GraphML_Element_strategy)
@settings(max_examples=50)
def test_graphml_element_instantiation(instance):
    assert isinstance(instance, GraphML_Element)



@given(instance=GraphML_Element_strategy)
def test_graphml_element_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=GraphML_EndPoint_strategy)
@settings(max_examples=50)
def test_graphml_endpoint_instantiation(instance):
    assert isinstance(instance, GraphML_EndPoint)

@given(instance=GraphML_Data_strategy)
@settings(max_examples=50)
def test_graphml_data_instantiation(instance):
    assert isinstance(instance, GraphML_Data)



@given(instance=GraphML_Data_strategy)
def test_graphml_data_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=GraphML_Data_strategy)
def test_graphml_data_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=GraphML_Port_strategy)
@settings(max_examples=50)
def test_graphml_port_instantiation(instance):
    assert isinstance(instance, GraphML_Port)



@given(instance=GraphML_Port_strategy)
def test_graphml_port_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=GraphML_Root_strategy)
@settings(max_examples=50)
def test_graphml_root_instantiation(instance):
    assert isinstance(instance, GraphML_Root)

@given(instance=GraphML_LocatedElement_strategy)
@settings(max_examples=50)
def test_graphml_locatedelement_instantiation(instance):
    assert isinstance(instance, GraphML_LocatedElement)



@given(instance=GraphML_LocatedElement_strategy)
def test_graphml_locatedelement_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=GraphML_LocatedElement_strategy)
def test_graphml_locatedelement_commentsBefore_setter(instance):
    original = instance.commentsBefore
    instance.commentsBefore = original
    assert instance.commentsBefore == original



@given(instance=GraphML_LocatedElement_strategy)
def test_graphml_locatedelement_commentsAfter_setter(instance):
    original = instance.commentsAfter
    instance.commentsAfter = original
    assert instance.commentsAfter == original
