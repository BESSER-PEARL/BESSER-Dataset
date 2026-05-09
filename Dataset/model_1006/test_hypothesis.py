import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Statement,
    dot::Attribute,
    dot::Statement,
    dot::AttributeStatement,
    dot::Subgraph,
    dot::EdgeTarget,
    dot::EdgeStatement,
    dot::Port,
    dot::Node,
    dot::NodeStatement,
    dot::Graph,
    dot::GraphvizModel,
    GraphType,
    AttributeType,
    EdgeOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_dot::attribute_is_not_abstract():
    assert not inspect.isabstract(dot::Attribute)


def test_dot::attribute_constructor_exists():
    assert callable(dot::Attribute.__init__)


def test_dot::attribute_constructor_args():
    sig = inspect.signature(dot::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_dot::attribute_has_name():
    assert hasattr(dot::Attribute, "name")
    descriptor = None
    for klass in dot::Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dot::attribute_has_value():
    assert hasattr(dot::Attribute, "value")
    descriptor = None
    for klass in dot::Attribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dot::statement_is_not_abstract():
    assert not inspect.isabstract(dot::Statement)


def test_dot::statement_constructor_exists():
    assert callable(dot::Statement.__init__)


def test_dot::statement_constructor_args():
    sig = inspect.signature(dot::Statement.__init__)
    params = list(sig.parameters.keys())



def test_dot::attributestatement_is_not_abstract():
    assert not inspect.isabstract(dot::AttributeStatement)


def test_dot::attributestatement_constructor_exists():
    assert callable(dot::AttributeStatement.__init__)


def test_dot::attributestatement_constructor_args():
    sig = inspect.signature(dot::AttributeStatement.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_dot::attributestatement_has_type():
    assert hasattr(dot::AttributeStatement, "type")
    descriptor = None
    for klass in dot::AttributeStatement.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_dot::subgraph_is_not_abstract():
    assert not inspect.isabstract(dot::Subgraph)


def test_dot::subgraph_constructor_exists():
    assert callable(dot::Subgraph.__init__)


def test_dot::subgraph_constructor_args():
    sig = inspect.signature(dot::Subgraph.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dot::subgraph_has_name():
    assert hasattr(dot::Subgraph, "name")
    descriptor = None
    for klass in dot::Subgraph.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dot::edgetarget_is_not_abstract():
    assert not inspect.isabstract(dot::EdgeTarget)


def test_dot::edgetarget_constructor_exists():
    assert callable(dot::EdgeTarget.__init__)


def test_dot::edgetarget_constructor_args():
    sig = inspect.signature(dot::EdgeTarget.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_dot::edgetarget_has_operator():
    assert hasattr(dot::EdgeTarget, "operator")
    descriptor = None
    for klass in dot::EdgeTarget.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_dot::edgestatement_is_not_abstract():
    assert not inspect.isabstract(dot::EdgeStatement)


def test_dot::edgestatement_constructor_exists():
    assert callable(dot::EdgeStatement.__init__)


def test_dot::edgestatement_constructor_args():
    sig = inspect.signature(dot::EdgeStatement.__init__)
    params = list(sig.parameters.keys())



def test_dot::port_is_not_abstract():
    assert not inspect.isabstract(dot::Port)


def test_dot::port_constructor_exists():
    assert callable(dot::Port.__init__)


def test_dot::port_constructor_args():
    sig = inspect.signature(dot::Port.__init__)
    params = list(sig.parameters.keys())
    assert "compass_pt" in params, "Missing parameter 'compass_pt'"
    assert "name" in params, "Missing parameter 'name'"

def test_dot::port_has_compass_pt():
    assert hasattr(dot::Port, "compass_pt")
    descriptor = None
    for klass in dot::Port.__mro__:
        if "compass_pt" in klass.__dict__:
            descriptor = klass.__dict__["compass_pt"]
            break
    assert isinstance(descriptor, property)

def test_dot::port_has_name():
    assert hasattr(dot::Port, "name")
    descriptor = None
    for klass in dot::Port.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dot::node_is_not_abstract():
    assert not inspect.isabstract(dot::Node)


def test_dot::node_constructor_exists():
    assert callable(dot::Node.__init__)


def test_dot::node_constructor_args():
    sig = inspect.signature(dot::Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dot::node_has_name():
    assert hasattr(dot::Node, "name")
    descriptor = None
    for klass in dot::Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dot::nodestatement_is_not_abstract():
    assert not inspect.isabstract(dot::NodeStatement)


def test_dot::nodestatement_constructor_exists():
    assert callable(dot::NodeStatement.__init__)


def test_dot::nodestatement_constructor_args():
    sig = inspect.signature(dot::NodeStatement.__init__)
    params = list(sig.parameters.keys())



def test_dot::graph_is_not_abstract():
    assert not inspect.isabstract(dot::Graph)


def test_dot::graph_constructor_exists():
    assert callable(dot::Graph.__init__)


def test_dot::graph_constructor_args():
    sig = inspect.signature(dot::Graph.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "strict" in params, "Missing parameter 'strict'"
    assert "name" in params, "Missing parameter 'name'"

def test_dot::graph_has_type():
    assert hasattr(dot::Graph, "type")
    descriptor = None
    for klass in dot::Graph.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_dot::graph_has_strict():
    assert hasattr(dot::Graph, "strict")
    descriptor = None
    for klass in dot::Graph.__mro__:
        if "strict" in klass.__dict__:
            descriptor = klass.__dict__["strict"]
            break
    assert isinstance(descriptor, property)

def test_dot::graph_has_name():
    assert hasattr(dot::Graph, "name")
    descriptor = None
    for klass in dot::Graph.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dot::graphvizmodel_is_not_abstract():
    assert not inspect.isabstract(dot::GraphvizModel)


def test_dot::graphvizmodel_constructor_exists():
    assert callable(dot::GraphvizModel.__init__)


def test_dot::graphvizmodel_constructor_args():
    sig = inspect.signature(dot::GraphvizModel.__init__)
    params = list(sig.parameters.keys())

def test_graphtype_exists():
    # Check that the Enumeration exists
    assert GraphType is not None

def test_graphtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GraphType]
    expected_literals = [
        "digraph",
        "graph",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GraphType"

def test_attributetype_exists():
    # Check that the Enumeration exists
    assert AttributeType is not None

def test_attributetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AttributeType]
    expected_literals = [
        "node",
        "graph",
        "edge",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AttributeType"

def test_edgeoperator_exists():
    # Check that the Enumeration exists
    assert EdgeOperator is not None

def test_edgeoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EdgeOperator]
    expected_literals = [
        "directed",
        "undirected",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EdgeOperator"


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
Statement_strategy = st.builds(
    Statement,
)
dot::Attribute_strategy = st.builds(
    dot::Attribute,
    name=
        safe_text,
    value=
        safe_text
)
dot::Statement_strategy = st.builds(
    dot::Statement,
)
dot::AttributeStatement_strategy = st.builds(
    dot::AttributeStatement,
    type=
        safe_text
)
dot::Subgraph_strategy = st.builds(
    dot::Subgraph,
    name=
        safe_text
)
dot::EdgeTarget_strategy = st.builds(
    dot::EdgeTarget,
    operator=
        safe_text
)
dot::EdgeStatement_strategy = st.builds(
    dot::EdgeStatement,
)
dot::Port_strategy = st.builds(
    dot::Port,
    compass_pt=
        safe_text,
    name=
        safe_text
)
dot::Node_strategy = st.builds(
    dot::Node,
    name=
        safe_text
)
dot::NodeStatement_strategy = st.builds(
    dot::NodeStatement,
)
dot::Graph_strategy = st.builds(
    dot::Graph,
    type=
        safe_text,
    strict=
        st.booleans(),
    name=
        safe_text
)
dot::GraphvizModel_strategy = st.builds(
    dot::GraphvizModel,
)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=dot::Attribute_strategy)
@settings(max_examples=50)
def test_dot::attribute_instantiation(instance):
    assert isinstance(instance, dot::Attribute)

@given(instance=dot::Attribute_strategy)
def test_dot::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dot::Attribute_strategy)
def test_dot::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dot::Attribute_strategy)
def test_dot::attribute_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=dot::Attribute_strategy)
def test_dot::attribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=dot::Statement_strategy)
@settings(max_examples=50)
def test_dot::statement_instantiation(instance):
    assert isinstance(instance, dot::Statement)

@given(instance=dot::AttributeStatement_strategy)
@settings(max_examples=50)
def test_dot::attributestatement_instantiation(instance):
    assert isinstance(instance, dot::AttributeStatement)

@given(instance=dot::AttributeStatement_strategy)
def test_dot::attributestatement_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=dot::AttributeStatement_strategy)
def test_dot::attributestatement_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=dot::Subgraph_strategy)
@settings(max_examples=50)
def test_dot::subgraph_instantiation(instance):
    assert isinstance(instance, dot::Subgraph)

@given(instance=dot::Subgraph_strategy)
def test_dot::subgraph_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dot::Subgraph_strategy)
def test_dot::subgraph_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dot::EdgeTarget_strategy)
@settings(max_examples=50)
def test_dot::edgetarget_instantiation(instance):
    assert isinstance(instance, dot::EdgeTarget)

@given(instance=dot::EdgeTarget_strategy)
def test_dot::edgetarget_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=dot::EdgeTarget_strategy)
def test_dot::edgetarget_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=dot::EdgeStatement_strategy)
@settings(max_examples=50)
def test_dot::edgestatement_instantiation(instance):
    assert isinstance(instance, dot::EdgeStatement)

@given(instance=dot::Port_strategy)
@settings(max_examples=50)
def test_dot::port_instantiation(instance):
    assert isinstance(instance, dot::Port)

@given(instance=dot::Port_strategy)
def test_dot::port_compass_pt_type(instance):
    assert isinstance(instance.compass_pt, str)


@given(instance=dot::Port_strategy)
def test_dot::port_compass_pt_setter(instance):
    original = instance.compass_pt
    instance.compass_pt = original
    assert instance.compass_pt == original

@given(instance=dot::Port_strategy)
def test_dot::port_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dot::Port_strategy)
def test_dot::port_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dot::Node_strategy)
@settings(max_examples=50)
def test_dot::node_instantiation(instance):
    assert isinstance(instance, dot::Node)

@given(instance=dot::Node_strategy)
def test_dot::node_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dot::Node_strategy)
def test_dot::node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dot::NodeStatement_strategy)
@settings(max_examples=50)
def test_dot::nodestatement_instantiation(instance):
    assert isinstance(instance, dot::NodeStatement)

@given(instance=dot::Graph_strategy)
@settings(max_examples=50)
def test_dot::graph_instantiation(instance):
    assert isinstance(instance, dot::Graph)

@given(instance=dot::Graph_strategy)
def test_dot::graph_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=dot::Graph_strategy)
def test_dot::graph_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=dot::Graph_strategy)
def test_dot::graph_strict_type(instance):
    assert isinstance(instance.strict, bool)


@given(instance=dot::Graph_strategy)
def test_dot::graph_strict_setter(instance):
    original = instance.strict
    instance.strict = original
    assert instance.strict == original

@given(instance=dot::Graph_strategy)
def test_dot::graph_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dot::Graph_strategy)
def test_dot::graph_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dot::GraphvizModel_strategy)
@settings(max_examples=50)
def test_dot::graphvizmodel_instantiation(instance):
    assert isinstance(instance, dot::GraphvizModel)
