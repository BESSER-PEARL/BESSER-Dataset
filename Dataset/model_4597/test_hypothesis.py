import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    edgeRHS,
    dot_edgeRHS_subgraph,
    dot_edgeRHS_node,
    dot_a_list,
    dot_attr_list,
    dot_edgeRHS,
    dot_node_id,
    dot_graph,
    dot_graphvizmodel,
    stmt,
    dot_attribute,
    dot_attr_stmt,
    dot_edge_stmt_subgraph,
    dot_subgraph,
    dot_node_stmt,
    dot_edge_stmt_node,
    dot_stmt,
    attributetype,
    edgeop,
    graphtype,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_edgerhs_is_not_abstract():
    assert not inspect.isabstract(edgeRHS)


def test_edgerhs_constructor_exists():
    assert callable(edgeRHS.__init__)


def test_edgerhs_constructor_args():
    sig = inspect.signature(edgeRHS.__init__)
    params = list(sig.parameters.keys())



def test_dot_edgerhs_subgraph_is_not_abstract():
    assert not inspect.isabstract(dot_edgeRHS_subgraph)


def test_dot_edgerhs_subgraph_constructor_exists():
    assert callable(dot_edgeRHS_subgraph.__init__)


def test_dot_edgerhs_subgraph_constructor_args():
    sig = inspect.signature(dot_edgeRHS_subgraph.__init__)
    params = list(sig.parameters.keys())



def test_dot_edgerhs_node_is_not_abstract():
    assert not inspect.isabstract(dot_edgeRHS_node)


def test_dot_edgerhs_node_constructor_exists():
    assert callable(dot_edgeRHS_node.__init__)


def test_dot_edgerhs_node_constructor_args():
    sig = inspect.signature(dot_edgeRHS_node.__init__)
    params = list(sig.parameters.keys())



def test_dot_a_list_is_not_abstract():
    assert not inspect.isabstract(dot_a_list)


def test_dot_a_list_constructor_exists():
    assert callable(dot_a_list.__init__)


def test_dot_a_list_constructor_args():
    sig = inspect.signature(dot_a_list.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_dot_a_list_has_name():
    assert hasattr(dot_a_list, "name")
    descriptor = None
    for klass in dot_a_list.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dot_a_list_has_value():
    assert hasattr(dot_a_list, "value")
    descriptor = None
    for klass in dot_a_list.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dot_attr_list_is_not_abstract():
    assert not inspect.isabstract(dot_attr_list)


def test_dot_attr_list_constructor_exists():
    assert callable(dot_attr_list.__init__)


def test_dot_attr_list_constructor_args():
    sig = inspect.signature(dot_attr_list.__init__)
    params = list(sig.parameters.keys())



def test_dot_edgerhs_is_not_abstract():
    assert not inspect.isabstract(dot_edgeRHS)


def test_dot_edgerhs_constructor_exists():
    assert callable(dot_edgeRHS.__init__)


def test_dot_edgerhs_constructor_args():
    sig = inspect.signature(dot_edgeRHS.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_dot_edgerhs_has_op():
    assert hasattr(dot_edgeRHS, "op")
    descriptor = None
    for klass in dot_edgeRHS.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_dot_node_id_is_not_abstract():
    assert not inspect.isabstract(dot_node_id)


def test_dot_node_id_constructor_exists():
    assert callable(dot_node_id.__init__)


def test_dot_node_id_constructor_args():
    sig = inspect.signature(dot_node_id.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dot_node_id_has_name():
    assert hasattr(dot_node_id, "name")
    descriptor = None
    for klass in dot_node_id.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dot_graph_is_not_abstract():
    assert not inspect.isabstract(dot_graph)


def test_dot_graph_constructor_exists():
    assert callable(dot_graph.__init__)


def test_dot_graph_constructor_args():
    sig = inspect.signature(dot_graph.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"
    assert "strict" in params, "Missing parameter 'strict'"

def test_dot_graph_has_name():
    assert hasattr(dot_graph, "name")
    descriptor = None
    for klass in dot_graph.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dot_graph_has_type():
    assert hasattr(dot_graph, "type")
    descriptor = None
    for klass in dot_graph.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_dot_graph_has_strict():
    assert hasattr(dot_graph, "strict")
    descriptor = None
    for klass in dot_graph.__mro__:
        if "strict" in klass.__dict__:
            descriptor = klass.__dict__["strict"]
            break
    assert isinstance(descriptor, property)



def test_dot_graphvizmodel_is_not_abstract():
    assert not inspect.isabstract(dot_graphvizmodel)


def test_dot_graphvizmodel_constructor_exists():
    assert callable(dot_graphvizmodel.__init__)


def test_dot_graphvizmodel_constructor_args():
    sig = inspect.signature(dot_graphvizmodel.__init__)
    params = list(sig.parameters.keys())



def test_stmt_is_not_abstract():
    assert not inspect.isabstract(stmt)


def test_stmt_constructor_exists():
    assert callable(stmt.__init__)


def test_stmt_constructor_args():
    sig = inspect.signature(stmt.__init__)
    params = list(sig.parameters.keys())



def test_dot_attribute_is_not_abstract():
    assert not inspect.isabstract(dot_attribute)


def test_dot_attribute_constructor_exists():
    assert callable(dot_attribute.__init__)


def test_dot_attribute_constructor_args():
    sig = inspect.signature(dot_attribute.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_dot_attribute_has_value():
    assert hasattr(dot_attribute, "value")
    descriptor = None
    for klass in dot_attribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_dot_attribute_has_name():
    assert hasattr(dot_attribute, "name")
    descriptor = None
    for klass in dot_attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dot_attr_stmt_is_not_abstract():
    assert not inspect.isabstract(dot_attr_stmt)


def test_dot_attr_stmt_constructor_exists():
    assert callable(dot_attr_stmt.__init__)


def test_dot_attr_stmt_constructor_args():
    sig = inspect.signature(dot_attr_stmt.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_dot_attr_stmt_has_type():
    assert hasattr(dot_attr_stmt, "type")
    descriptor = None
    for klass in dot_attr_stmt.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_dot_edge_stmt_subgraph_is_not_abstract():
    assert not inspect.isabstract(dot_edge_stmt_subgraph)


def test_dot_edge_stmt_subgraph_constructor_exists():
    assert callable(dot_edge_stmt_subgraph.__init__)


def test_dot_edge_stmt_subgraph_constructor_args():
    sig = inspect.signature(dot_edge_stmt_subgraph.__init__)
    params = list(sig.parameters.keys())



def test_dot_subgraph_is_not_abstract():
    assert not inspect.isabstract(dot_subgraph)


def test_dot_subgraph_constructor_exists():
    assert callable(dot_subgraph.__init__)


def test_dot_subgraph_constructor_args():
    sig = inspect.signature(dot_subgraph.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dot_subgraph_has_name():
    assert hasattr(dot_subgraph, "name")
    descriptor = None
    for klass in dot_subgraph.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dot_node_stmt_is_not_abstract():
    assert not inspect.isabstract(dot_node_stmt)


def test_dot_node_stmt_constructor_exists():
    assert callable(dot_node_stmt.__init__)


def test_dot_node_stmt_constructor_args():
    sig = inspect.signature(dot_node_stmt.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dot_node_stmt_has_name():
    assert hasattr(dot_node_stmt, "name")
    descriptor = None
    for klass in dot_node_stmt.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dot_edge_stmt_node_is_not_abstract():
    assert not inspect.isabstract(dot_edge_stmt_node)


def test_dot_edge_stmt_node_constructor_exists():
    assert callable(dot_edge_stmt_node.__init__)


def test_dot_edge_stmt_node_constructor_args():
    sig = inspect.signature(dot_edge_stmt_node.__init__)
    params = list(sig.parameters.keys())



def test_dot_stmt_is_not_abstract():
    assert not inspect.isabstract(dot_stmt)


def test_dot_stmt_constructor_exists():
    assert callable(dot_stmt.__init__)


def test_dot_stmt_constructor_args():
    sig = inspect.signature(dot_stmt.__init__)
    params = list(sig.parameters.keys())

def test_attributetype_exists():
    # Check that the Enumeration exists
    assert attributetype is not None

def test_attributetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in attributetype]
    expected_literals = [
        "node",
        "edge",
        "graph",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in attributetype"

def test_edgeop_exists():
    # Check that the Enumeration exists
    assert edgeop is not None

def test_edgeop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in edgeop]
    expected_literals = [
        "undirected",
        "directed",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in edgeop"

def test_graphtype_exists():
    # Check that the Enumeration exists
    assert graphtype is not None

def test_graphtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in graphtype]
    expected_literals = [
        "graph",
        "digraph",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in graphtype"


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
edgeRHS_strategy = st.builds(
    edgeRHS,
)
dot_edgeRHS_subgraph_strategy = st.builds(
    dot_edgeRHS_subgraph,
)
dot_edgeRHS_node_strategy = st.builds(
    dot_edgeRHS_node,
)
dot_a_list_strategy = st.builds(
    dot_a_list,
    name=
        safe_text,
    value=
        safe_text
)
dot_attr_list_strategy = st.builds(
    dot_attr_list,
)
dot_edgeRHS_strategy = st.builds(
    dot_edgeRHS,
    op=
        safe_text
)
dot_node_id_strategy = st.builds(
    dot_node_id,
    name=
        safe_text
)
dot_graph_strategy = st.builds(
    dot_graph,
    name=
        safe_text,
    type=
        safe_text,
    strict=
        st.booleans()
)
dot_graphvizmodel_strategy = st.builds(
    dot_graphvizmodel,
)
stmt_strategy = st.builds(
    stmt,
)
dot_attribute_strategy = st.builds(
    dot_attribute,
    value=
        safe_text,
    name=
        safe_text
)
dot_attr_stmt_strategy = st.builds(
    dot_attr_stmt,
    type=
        safe_text
)
dot_edge_stmt_subgraph_strategy = st.builds(
    dot_edge_stmt_subgraph,
)
dot_subgraph_strategy = st.builds(
    dot_subgraph,
    name=
        safe_text
)
dot_node_stmt_strategy = st.builds(
    dot_node_stmt,
    name=
        safe_text
)
dot_edge_stmt_node_strategy = st.builds(
    dot_edge_stmt_node,
)
dot_stmt_strategy = st.builds(
    dot_stmt,
)

@given(instance=edgeRHS_strategy)
@settings(max_examples=50)
def test_edgerhs_instantiation(instance):
    assert isinstance(instance, edgeRHS)

@given(instance=dot_edgeRHS_subgraph_strategy)
@settings(max_examples=50)
def test_dot_edgerhs_subgraph_instantiation(instance):
    assert isinstance(instance, dot_edgeRHS_subgraph)

@given(instance=dot_edgeRHS_node_strategy)
@settings(max_examples=50)
def test_dot_edgerhs_node_instantiation(instance):
    assert isinstance(instance, dot_edgeRHS_node)

@given(instance=dot_a_list_strategy)
@settings(max_examples=50)
def test_dot_a_list_instantiation(instance):
    assert isinstance(instance, dot_a_list)



@given(instance=dot_a_list_strategy)
def test_dot_a_list_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=dot_a_list_strategy)
def test_dot_a_list_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=dot_attr_list_strategy)
@settings(max_examples=50)
def test_dot_attr_list_instantiation(instance):
    assert isinstance(instance, dot_attr_list)

@given(instance=dot_edgeRHS_strategy)
@settings(max_examples=50)
def test_dot_edgerhs_instantiation(instance):
    assert isinstance(instance, dot_edgeRHS)



@given(instance=dot_edgeRHS_strategy)
def test_dot_edgerhs_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=dot_node_id_strategy)
@settings(max_examples=50)
def test_dot_node_id_instantiation(instance):
    assert isinstance(instance, dot_node_id)



@given(instance=dot_node_id_strategy)
def test_dot_node_id_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dot_graph_strategy)
@settings(max_examples=50)
def test_dot_graph_instantiation(instance):
    assert isinstance(instance, dot_graph)



@given(instance=dot_graph_strategy)
def test_dot_graph_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=dot_graph_strategy)
def test_dot_graph_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=dot_graph_strategy)
def test_dot_graph_strict_setter(instance):
    original = instance.strict
    instance.strict = original
    assert instance.strict == original

@given(instance=dot_graphvizmodel_strategy)
@settings(max_examples=50)
def test_dot_graphvizmodel_instantiation(instance):
    assert isinstance(instance, dot_graphvizmodel)

@given(instance=stmt_strategy)
@settings(max_examples=50)
def test_stmt_instantiation(instance):
    assert isinstance(instance, stmt)

@given(instance=dot_attribute_strategy)
@settings(max_examples=50)
def test_dot_attribute_instantiation(instance):
    assert isinstance(instance, dot_attribute)



@given(instance=dot_attribute_strategy)
def test_dot_attribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=dot_attribute_strategy)
def test_dot_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dot_attr_stmt_strategy)
@settings(max_examples=50)
def test_dot_attr_stmt_instantiation(instance):
    assert isinstance(instance, dot_attr_stmt)



@given(instance=dot_attr_stmt_strategy)
def test_dot_attr_stmt_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=dot_edge_stmt_subgraph_strategy)
@settings(max_examples=50)
def test_dot_edge_stmt_subgraph_instantiation(instance):
    assert isinstance(instance, dot_edge_stmt_subgraph)

@given(instance=dot_subgraph_strategy)
@settings(max_examples=50)
def test_dot_subgraph_instantiation(instance):
    assert isinstance(instance, dot_subgraph)



@given(instance=dot_subgraph_strategy)
def test_dot_subgraph_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dot_node_stmt_strategy)
@settings(max_examples=50)
def test_dot_node_stmt_instantiation(instance):
    assert isinstance(instance, dot_node_stmt)



@given(instance=dot_node_stmt_strategy)
def test_dot_node_stmt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dot_edge_stmt_node_strategy)
@settings(max_examples=50)
def test_dot_edge_stmt_node_instantiation(instance):
    assert isinstance(instance, dot_edge_stmt_node)

@given(instance=dot_stmt_strategy)
@settings(max_examples=50)
def test_dot_stmt_instantiation(instance):
    assert isinstance(instance, dot_stmt)
