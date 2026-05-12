import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Node,
    graphEditor_Variablenode,
    graphEditor_Factornode,
    GraphElement,
    graphEditor_GraphElement,
    graphEditor_Message,
    graphEditor_Edge,
    graphEditor_Node,
    graphEditor_Graph,
    FunctionType,
    VariableType,
    MessageType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_grapheditor_variablenode_is_not_abstract():
    assert not inspect.isabstract(graphEditor_Variablenode)


def test_grapheditor_variablenode_constructor_exists():
    assert callable(graphEditor_Variablenode.__init__)


def test_grapheditor_variablenode_constructor_args():
    sig = inspect.signature(graphEditor_Variablenode.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"
    assert "type" in params, "Missing parameter 'type'"
    assert "isKnown" in params, "Missing parameter 'isKnown'"

def test_grapheditor_variablenode_has_values():
    assert hasattr(graphEditor_Variablenode, "values")
    descriptor = None
    for klass in graphEditor_Variablenode.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)

def test_grapheditor_variablenode_has_type():
    assert hasattr(graphEditor_Variablenode, "type")
    descriptor = None
    for klass in graphEditor_Variablenode.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_grapheditor_variablenode_has_isKnown():
    assert hasattr(graphEditor_Variablenode, "isKnown")
    descriptor = None
    for klass in graphEditor_Variablenode.__mro__:
        if "isKnown" in klass.__dict__:
            descriptor = klass.__dict__["isKnown"]
            break
    assert isinstance(descriptor, property)



def test_grapheditor_factornode_is_not_abstract():
    assert not inspect.isabstract(graphEditor_Factornode)


def test_grapheditor_factornode_constructor_exists():
    assert callable(graphEditor_Factornode.__init__)


def test_grapheditor_factornode_constructor_args():
    sig = inspect.signature(graphEditor_Factornode.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"
    assert "type" in params, "Missing parameter 'type'"

def test_grapheditor_factornode_has_values():
    assert hasattr(graphEditor_Factornode, "values")
    descriptor = None
    for klass in graphEditor_Factornode.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)

def test_grapheditor_factornode_has_type():
    assert hasattr(graphEditor_Factornode, "type")
    descriptor = None
    for klass in graphEditor_Factornode.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_graphelement_is_not_abstract():
    assert not inspect.isabstract(GraphElement)


def test_graphelement_constructor_exists():
    assert callable(GraphElement.__init__)


def test_graphelement_constructor_args():
    sig = inspect.signature(GraphElement.__init__)
    params = list(sig.parameters.keys())



def test_grapheditor_graphelement_is_not_abstract():
    assert not inspect.isabstract(graphEditor_GraphElement)


def test_grapheditor_graphelement_constructor_exists():
    assert callable(graphEditor_GraphElement.__init__)


def test_grapheditor_graphelement_constructor_args():
    sig = inspect.signature(graphEditor_GraphElement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_grapheditor_graphelement_has_id():
    assert hasattr(graphEditor_GraphElement, "id")
    descriptor = None
    for klass in graphEditor_GraphElement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_grapheditor_message_is_not_abstract():
    assert not inspect.isabstract(graphEditor_Message)


def test_grapheditor_message_constructor_exists():
    assert callable(graphEditor_Message.__init__)


def test_grapheditor_message_constructor_args():
    sig = inspect.signature(graphEditor_Message.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "count" in params, "Missing parameter 'count'"

def test_grapheditor_message_has_type():
    assert hasattr(graphEditor_Message, "type")
    descriptor = None
    for klass in graphEditor_Message.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_grapheditor_message_has_count():
    assert hasattr(graphEditor_Message, "count")
    descriptor = None
    for klass in graphEditor_Message.__mro__:
        if "count" in klass.__dict__:
            descriptor = klass.__dict__["count"]
            break
    assert isinstance(descriptor, property)



def test_grapheditor_edge_is_not_abstract():
    assert not inspect.isabstract(graphEditor_Edge)


def test_grapheditor_edge_constructor_exists():
    assert callable(graphEditor_Edge.__init__)


def test_grapheditor_edge_constructor_args():
    sig = inspect.signature(graphEditor_Edge.__init__)
    params = list(sig.parameters.keys())



def test_grapheditor_node_is_not_abstract():
    assert not inspect.isabstract(graphEditor_Node)


def test_grapheditor_node_constructor_exists():
    assert callable(graphEditor_Node.__init__)


def test_grapheditor_node_constructor_args():
    sig = inspect.signature(graphEditor_Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_grapheditor_node_has_name():
    assert hasattr(graphEditor_Node, "name")
    descriptor = None
    for klass in graphEditor_Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_grapheditor_graph_is_not_abstract():
    assert not inspect.isabstract(graphEditor_Graph)


def test_grapheditor_graph_constructor_exists():
    assert callable(graphEditor_Graph.__init__)


def test_grapheditor_graph_constructor_args():
    sig = inspect.signature(graphEditor_Graph.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "result" in params, "Missing parameter 'result'"

def test_grapheditor_graph_has_name():
    assert hasattr(graphEditor_Graph, "name")
    descriptor = None
    for klass in graphEditor_Graph.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_grapheditor_graph_has_result():
    assert hasattr(graphEditor_Graph, "result")
    descriptor = None
    for klass in graphEditor_Graph.__mro__:
        if "result" in klass.__dict__:
            descriptor = klass.__dict__["result"]
            break
    assert isinstance(descriptor, property)

def test_functiontype_exists():
    # Check that the Enumeration exists
    assert FunctionType is not None

def test_functiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FunctionType]
    expected_literals = [
        "Boolean",
        "Gausian",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FunctionType"

def test_variabletype_exists():
    # Check that the Enumeration exists
    assert VariableType is not None

def test_variabletype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in VariableType]
    expected_literals = [
        "Real",
        "Boolean",
        "Categorial",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in VariableType"

def test_messagetype_exists():
    # Check that the Enumeration exists
    assert MessageType is not None

def test_messagetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MessageType]
    expected_literals = [
        "VariableToFactor",
        "MarginalEdge",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MessageType"


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
Node_strategy = st.builds(
    Node,
)
graphEditor_Variablenode_strategy = st.builds(
    graphEditor_Variablenode,
    values=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    type=
        safe_text,
    isKnown=
        st.booleans()
)
graphEditor_Factornode_strategy = st.builds(
    graphEditor_Factornode,
    values=
        safe_text,
    type=
        safe_text
)
GraphElement_strategy = st.builds(
    GraphElement,
)
graphEditor_GraphElement_strategy = st.builds(
    graphEditor_GraphElement,
    id=
        safe_text
)
graphEditor_Message_strategy = st.builds(
    graphEditor_Message,
    type=
        safe_text,
    count=
        st.integers()
)
graphEditor_Edge_strategy = st.builds(
    graphEditor_Edge,
)
graphEditor_Node_strategy = st.builds(
    graphEditor_Node,
    name=
        safe_text
)
graphEditor_Graph_strategy = st.builds(
    graphEditor_Graph,
    name=
        safe_text,
    result=
        safe_text
)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=graphEditor_Variablenode_strategy)
@settings(max_examples=50)
def test_grapheditor_variablenode_instantiation(instance):
    assert isinstance(instance, graphEditor_Variablenode)



@given(instance=graphEditor_Variablenode_strategy)
def test_grapheditor_variablenode_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original



@given(instance=graphEditor_Variablenode_strategy)
def test_grapheditor_variablenode_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=graphEditor_Variablenode_strategy)
def test_grapheditor_variablenode_isKnown_setter(instance):
    original = instance.isKnown
    instance.isKnown = original
    assert instance.isKnown == original

@given(instance=graphEditor_Factornode_strategy)
@settings(max_examples=50)
def test_grapheditor_factornode_instantiation(instance):
    assert isinstance(instance, graphEditor_Factornode)



@given(instance=graphEditor_Factornode_strategy)
def test_grapheditor_factornode_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original



@given(instance=graphEditor_Factornode_strategy)
def test_grapheditor_factornode_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=GraphElement_strategy)
@settings(max_examples=50)
def test_graphelement_instantiation(instance):
    assert isinstance(instance, GraphElement)

@given(instance=graphEditor_GraphElement_strategy)
@settings(max_examples=50)
def test_grapheditor_graphelement_instantiation(instance):
    assert isinstance(instance, graphEditor_GraphElement)



@given(instance=graphEditor_GraphElement_strategy)
def test_grapheditor_graphelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=graphEditor_Message_strategy)
@settings(max_examples=50)
def test_grapheditor_message_instantiation(instance):
    assert isinstance(instance, graphEditor_Message)



@given(instance=graphEditor_Message_strategy)
def test_grapheditor_message_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=graphEditor_Message_strategy)
def test_grapheditor_message_count_setter(instance):
    original = instance.count
    instance.count = original
    assert instance.count == original

@given(instance=graphEditor_Edge_strategy)
@settings(max_examples=50)
def test_grapheditor_edge_instantiation(instance):
    assert isinstance(instance, graphEditor_Edge)

@given(instance=graphEditor_Node_strategy)
@settings(max_examples=50)
def test_grapheditor_node_instantiation(instance):
    assert isinstance(instance, graphEditor_Node)



@given(instance=graphEditor_Node_strategy)
def test_grapheditor_node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=graphEditor_Graph_strategy)
@settings(max_examples=50)
def test_grapheditor_graph_instantiation(instance):
    assert isinstance(instance, graphEditor_Graph)



@given(instance=graphEditor_Graph_strategy)
def test_grapheditor_graph_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=graphEditor_Graph_strategy)
def test_grapheditor_graph_result_setter(instance):
    original = instance.result
    instance.result = original
    assert instance.result == original
