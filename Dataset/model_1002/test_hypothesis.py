import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Node,
    graphEditor::Variablenode,
    graphEditor::Factornode,
    GraphElement,
    graphEditor::GraphElement,
    graphEditor::Message,
    graphEditor::Edge,
    graphEditor::Node,
    graphEditor::Graph,
    FunctionType,
    MessageType,
    VariableType,
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



def test_grapheditor::variablenode_is_not_abstract():
    assert not inspect.isabstract(graphEditor::Variablenode)


def test_grapheditor::variablenode_constructor_exists():
    assert callable(graphEditor::Variablenode.__init__)


def test_grapheditor::variablenode_constructor_args():
    sig = inspect.signature(graphEditor::Variablenode.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "values" in params, "Missing parameter 'values'"
    assert "isKnown" in params, "Missing parameter 'isKnown'"

def test_grapheditor::variablenode_has_type():
    assert hasattr(graphEditor::Variablenode, "type")
    descriptor = None
    for klass in graphEditor::Variablenode.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_grapheditor::variablenode_has_values():
    assert hasattr(graphEditor::Variablenode, "values")
    descriptor = None
    for klass in graphEditor::Variablenode.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)

def test_grapheditor::variablenode_has_isKnown():
    assert hasattr(graphEditor::Variablenode, "isKnown")
    descriptor = None
    for klass in graphEditor::Variablenode.__mro__:
        if "isKnown" in klass.__dict__:
            descriptor = klass.__dict__["isKnown"]
            break
    assert isinstance(descriptor, property)



def test_grapheditor::factornode_is_not_abstract():
    assert not inspect.isabstract(graphEditor::Factornode)


def test_grapheditor::factornode_constructor_exists():
    assert callable(graphEditor::Factornode.__init__)


def test_grapheditor::factornode_constructor_args():
    sig = inspect.signature(graphEditor::Factornode.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "values" in params, "Missing parameter 'values'"

def test_grapheditor::factornode_has_type():
    assert hasattr(graphEditor::Factornode, "type")
    descriptor = None
    for klass in graphEditor::Factornode.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_grapheditor::factornode_has_values():
    assert hasattr(graphEditor::Factornode, "values")
    descriptor = None
    for klass in graphEditor::Factornode.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_graphelement_is_not_abstract():
    assert not inspect.isabstract(GraphElement)


def test_graphelement_constructor_exists():
    assert callable(GraphElement.__init__)


def test_graphelement_constructor_args():
    sig = inspect.signature(GraphElement.__init__)
    params = list(sig.parameters.keys())



def test_grapheditor::graphelement_is_not_abstract():
    assert not inspect.isabstract(graphEditor::GraphElement)


def test_grapheditor::graphelement_constructor_exists():
    assert callable(graphEditor::GraphElement.__init__)


def test_grapheditor::graphelement_constructor_args():
    sig = inspect.signature(graphEditor::GraphElement.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_grapheditor::graphelement_has_id():
    assert hasattr(graphEditor::GraphElement, "id")
    descriptor = None
    for klass in graphEditor::GraphElement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_grapheditor::message_is_not_abstract():
    assert not inspect.isabstract(graphEditor::Message)


def test_grapheditor::message_constructor_exists():
    assert callable(graphEditor::Message.__init__)


def test_grapheditor::message_constructor_args():
    sig = inspect.signature(graphEditor::Message.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "count" in params, "Missing parameter 'count'"

def test_grapheditor::message_has_type():
    assert hasattr(graphEditor::Message, "type")
    descriptor = None
    for klass in graphEditor::Message.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_grapheditor::message_has_count():
    assert hasattr(graphEditor::Message, "count")
    descriptor = None
    for klass in graphEditor::Message.__mro__:
        if "count" in klass.__dict__:
            descriptor = klass.__dict__["count"]
            break
    assert isinstance(descriptor, property)



def test_grapheditor::edge_is_not_abstract():
    assert not inspect.isabstract(graphEditor::Edge)


def test_grapheditor::edge_constructor_exists():
    assert callable(graphEditor::Edge.__init__)


def test_grapheditor::edge_constructor_args():
    sig = inspect.signature(graphEditor::Edge.__init__)
    params = list(sig.parameters.keys())



def test_grapheditor::node_is_not_abstract():
    assert not inspect.isabstract(graphEditor::Node)


def test_grapheditor::node_constructor_exists():
    assert callable(graphEditor::Node.__init__)


def test_grapheditor::node_constructor_args():
    sig = inspect.signature(graphEditor::Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_grapheditor::node_has_name():
    assert hasattr(graphEditor::Node, "name")
    descriptor = None
    for klass in graphEditor::Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_grapheditor::graph_is_not_abstract():
    assert not inspect.isabstract(graphEditor::Graph)


def test_grapheditor::graph_constructor_exists():
    assert callable(graphEditor::Graph.__init__)


def test_grapheditor::graph_constructor_args():
    sig = inspect.signature(graphEditor::Graph.__init__)
    params = list(sig.parameters.keys())
    assert "result" in params, "Missing parameter 'result'"
    assert "name" in params, "Missing parameter 'name'"

def test_grapheditor::graph_has_result():
    assert hasattr(graphEditor::Graph, "result")
    descriptor = None
    for klass in graphEditor::Graph.__mro__:
        if "result" in klass.__dict__:
            descriptor = klass.__dict__["result"]
            break
    assert isinstance(descriptor, property)

def test_grapheditor::graph_has_name():
    assert hasattr(graphEditor::Graph, "name")
    descriptor = None
    for klass in graphEditor::Graph.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_functiontype_exists():
    # Check that the Enumeration exists
    assert FunctionType is not None

def test_functiontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FunctionType]
    expected_literals = [
        "Gausian",
        "Boolean",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FunctionType"

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
graphEditor::Variablenode_strategy = st.builds(
    graphEditor::Variablenode,
    type=
        safe_text,
    values=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    isKnown=
        st.booleans()
)
graphEditor::Factornode_strategy = st.builds(
    graphEditor::Factornode,
    type=
        safe_text,
    values=
        safe_text
)
GraphElement_strategy = st.builds(
    GraphElement,
)
graphEditor::GraphElement_strategy = st.builds(
    graphEditor::GraphElement,
    id=
        safe_text
)
graphEditor::Message_strategy = st.builds(
    graphEditor::Message,
    type=
        safe_text,
    count=
        st.integers()
)
graphEditor::Edge_strategy = st.builds(
    graphEditor::Edge,
)
graphEditor::Node_strategy = st.builds(
    graphEditor::Node,
    name=
        safe_text
)
graphEditor::Graph_strategy = st.builds(
    graphEditor::Graph,
    result=
        safe_text,
    name=
        safe_text
)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=graphEditor::Variablenode_strategy)
@settings(max_examples=50)
def test_grapheditor::variablenode_instantiation(instance):
    assert isinstance(instance, graphEditor::Variablenode)

@given(instance=graphEditor::Variablenode_strategy)
def test_grapheditor::variablenode_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=graphEditor::Variablenode_strategy)
def test_grapheditor::variablenode_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=graphEditor::Variablenode_strategy)
def test_grapheditor::variablenode_values_type(instance):
    assert isinstance(instance.values, float)


@given(instance=graphEditor::Variablenode_strategy)
def test_grapheditor::variablenode_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=graphEditor::Variablenode_strategy)
def test_grapheditor::variablenode_isKnown_type(instance):
    assert isinstance(instance.isKnown, bool)


@given(instance=graphEditor::Variablenode_strategy)
def test_grapheditor::variablenode_isKnown_setter(instance):
    original = instance.isKnown
    instance.isKnown = original
    assert instance.isKnown == original

@given(instance=graphEditor::Factornode_strategy)
@settings(max_examples=50)
def test_grapheditor::factornode_instantiation(instance):
    assert isinstance(instance, graphEditor::Factornode)

@given(instance=graphEditor::Factornode_strategy)
def test_grapheditor::factornode_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=graphEditor::Factornode_strategy)
def test_grapheditor::factornode_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=graphEditor::Factornode_strategy)
def test_grapheditor::factornode_values_type(instance):
    assert isinstance(instance.values, str)


@given(instance=graphEditor::Factornode_strategy)
def test_grapheditor::factornode_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=GraphElement_strategy)
@settings(max_examples=50)
def test_graphelement_instantiation(instance):
    assert isinstance(instance, GraphElement)

@given(instance=graphEditor::GraphElement_strategy)
@settings(max_examples=50)
def test_grapheditor::graphelement_instantiation(instance):
    assert isinstance(instance, graphEditor::GraphElement)

@given(instance=graphEditor::GraphElement_strategy)
def test_grapheditor::graphelement_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=graphEditor::GraphElement_strategy)
def test_grapheditor::graphelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=graphEditor::Message_strategy)
@settings(max_examples=50)
def test_grapheditor::message_instantiation(instance):
    assert isinstance(instance, graphEditor::Message)

@given(instance=graphEditor::Message_strategy)
def test_grapheditor::message_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=graphEditor::Message_strategy)
def test_grapheditor::message_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=graphEditor::Message_strategy)
def test_grapheditor::message_count_type(instance):
    assert isinstance(instance.count, int)


@given(instance=graphEditor::Message_strategy)
def test_grapheditor::message_count_setter(instance):
    original = instance.count
    instance.count = original
    assert instance.count == original

@given(instance=graphEditor::Edge_strategy)
@settings(max_examples=50)
def test_grapheditor::edge_instantiation(instance):
    assert isinstance(instance, graphEditor::Edge)

@given(instance=graphEditor::Node_strategy)
@settings(max_examples=50)
def test_grapheditor::node_instantiation(instance):
    assert isinstance(instance, graphEditor::Node)

@given(instance=graphEditor::Node_strategy)
def test_grapheditor::node_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=graphEditor::Node_strategy)
def test_grapheditor::node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=graphEditor::Graph_strategy)
@settings(max_examples=50)
def test_grapheditor::graph_instantiation(instance):
    assert isinstance(instance, graphEditor::Graph)

@given(instance=graphEditor::Graph_strategy)
def test_grapheditor::graph_result_type(instance):
    assert isinstance(instance.result, str)


@given(instance=graphEditor::Graph_strategy)
def test_grapheditor::graph_result_setter(instance):
    original = instance.result
    instance.result = original
    assert instance.result == original

@given(instance=graphEditor::Graph_strategy)
def test_grapheditor::graph_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=graphEditor::Graph_strategy)
def test_grapheditor::graph_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
