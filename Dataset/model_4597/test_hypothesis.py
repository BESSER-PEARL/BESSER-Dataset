import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    edgeRHS,
    dot::edgeRHS::subgraph,
    dot::edgeRHS::node,
    dot::a::list,
    dot::attr::list,
    dot::edgeRHS,
    dot::node::id,
    dot::graph,
    dot::graphvizmodel,
    stmt,
    dot::node::stmt,
    dot::edge::stmt::subgraph,
    dot::subgraph,
    dot::attr::stmt,
    dot::attribute,
    dot::edge::stmt::node,
    dot::stmt,
    edgeop,
    graphtype,
    attributetype,
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



def test_dot::edgerhs::subgraph_is_not_abstract():
    assert not inspect.isabstract(dot::edgeRHS::subgraph)


def test_dot::edgerhs::subgraph_constructor_exists():
    assert callable(dot::edgeRHS::subgraph.__init__)


def test_dot::edgerhs::subgraph_constructor_args():
    sig = inspect.signature(dot::edgeRHS::subgraph.__init__)
    params = list(sig.parameters.keys())



def test_dot::edgerhs::node_is_not_abstract():
    assert not inspect.isabstract(dot::edgeRHS::node)


def test_dot::edgerhs::node_constructor_exists():
    assert callable(dot::edgeRHS::node.__init__)


def test_dot::edgerhs::node_constructor_args():
    sig = inspect.signature(dot::edgeRHS::node.__init__)
    params = list(sig.parameters.keys())



def test_dot::a::list_is_not_abstract():
    assert not inspect.isabstract(dot::a::list)


def test_dot::a::list_constructor_exists():
    assert callable(dot::a::list.__init__)


def test_dot::a::list_constructor_args():
    sig = inspect.signature(dot::a::list.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_dot::a::list_has_name():
    assert hasattr(dot::a::list, "name")
    descriptor = None
    for klass in dot::a::list.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dot::a::list_has_value():
    assert hasattr(dot::a::list, "value")
    descriptor = None
    for klass in dot::a::list.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dot::attr::list_is_not_abstract():
    assert not inspect.isabstract(dot::attr::list)


def test_dot::attr::list_constructor_exists():
    assert callable(dot::attr::list.__init__)


def test_dot::attr::list_constructor_args():
    sig = inspect.signature(dot::attr::list.__init__)
    params = list(sig.parameters.keys())



def test_dot::edgerhs_is_not_abstract():
    assert not inspect.isabstract(dot::edgeRHS)


def test_dot::edgerhs_constructor_exists():
    assert callable(dot::edgeRHS.__init__)


def test_dot::edgerhs_constructor_args():
    sig = inspect.signature(dot::edgeRHS.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_dot::edgerhs_has_op():
    assert hasattr(dot::edgeRHS, "op")
    descriptor = None
    for klass in dot::edgeRHS.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_dot::node::id_is_not_abstract():
    assert not inspect.isabstract(dot::node::id)


def test_dot::node::id_constructor_exists():
    assert callable(dot::node::id.__init__)


def test_dot::node::id_constructor_args():
    sig = inspect.signature(dot::node::id.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dot::node::id_has_name():
    assert hasattr(dot::node::id, "name")
    descriptor = None
    for klass in dot::node::id.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dot::graph_is_not_abstract():
    assert not inspect.isabstract(dot::graph)


def test_dot::graph_constructor_exists():
    assert callable(dot::graph.__init__)


def test_dot::graph_constructor_args():
    sig = inspect.signature(dot::graph.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "strict" in params, "Missing parameter 'strict'"
    assert "name" in params, "Missing parameter 'name'"

def test_dot::graph_has_type():
    assert hasattr(dot::graph, "type")
    descriptor = None
    for klass in dot::graph.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_dot::graph_has_strict():
    assert hasattr(dot::graph, "strict")
    descriptor = None
    for klass in dot::graph.__mro__:
        if "strict" in klass.__dict__:
            descriptor = klass.__dict__["strict"]
            break
    assert isinstance(descriptor, property)

def test_dot::graph_has_name():
    assert hasattr(dot::graph, "name")
    descriptor = None
    for klass in dot::graph.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dot::graphvizmodel_is_not_abstract():
    assert not inspect.isabstract(dot::graphvizmodel)


def test_dot::graphvizmodel_constructor_exists():
    assert callable(dot::graphvizmodel.__init__)


def test_dot::graphvizmodel_constructor_args():
    sig = inspect.signature(dot::graphvizmodel.__init__)
    params = list(sig.parameters.keys())



def test_stmt_is_not_abstract():
    assert not inspect.isabstract(stmt)


def test_stmt_constructor_exists():
    assert callable(stmt.__init__)


def test_stmt_constructor_args():
    sig = inspect.signature(stmt.__init__)
    params = list(sig.parameters.keys())



def test_dot::node::stmt_is_not_abstract():
    assert not inspect.isabstract(dot::node::stmt)


def test_dot::node::stmt_constructor_exists():
    assert callable(dot::node::stmt.__init__)


def test_dot::node::stmt_constructor_args():
    sig = inspect.signature(dot::node::stmt.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dot::node::stmt_has_name():
    assert hasattr(dot::node::stmt, "name")
    descriptor = None
    for klass in dot::node::stmt.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dot::edge::stmt::subgraph_is_not_abstract():
    assert not inspect.isabstract(dot::edge::stmt::subgraph)


def test_dot::edge::stmt::subgraph_constructor_exists():
    assert callable(dot::edge::stmt::subgraph.__init__)


def test_dot::edge::stmt::subgraph_constructor_args():
    sig = inspect.signature(dot::edge::stmt::subgraph.__init__)
    params = list(sig.parameters.keys())



def test_dot::subgraph_is_not_abstract():
    assert not inspect.isabstract(dot::subgraph)


def test_dot::subgraph_constructor_exists():
    assert callable(dot::subgraph.__init__)


def test_dot::subgraph_constructor_args():
    sig = inspect.signature(dot::subgraph.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dot::subgraph_has_name():
    assert hasattr(dot::subgraph, "name")
    descriptor = None
    for klass in dot::subgraph.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dot::attr::stmt_is_not_abstract():
    assert not inspect.isabstract(dot::attr::stmt)


def test_dot::attr::stmt_constructor_exists():
    assert callable(dot::attr::stmt.__init__)


def test_dot::attr::stmt_constructor_args():
    sig = inspect.signature(dot::attr::stmt.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_dot::attr::stmt_has_type():
    assert hasattr(dot::attr::stmt, "type")
    descriptor = None
    for klass in dot::attr::stmt.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_dot::attribute_is_not_abstract():
    assert not inspect.isabstract(dot::attribute)


def test_dot::attribute_constructor_exists():
    assert callable(dot::attribute.__init__)


def test_dot::attribute_constructor_args():
    sig = inspect.signature(dot::attribute.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_dot::attribute_has_value():
    assert hasattr(dot::attribute, "value")
    descriptor = None
    for klass in dot::attribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_dot::attribute_has_name():
    assert hasattr(dot::attribute, "name")
    descriptor = None
    for klass in dot::attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dot::edge::stmt::node_is_not_abstract():
    assert not inspect.isabstract(dot::edge::stmt::node)


def test_dot::edge::stmt::node_constructor_exists():
    assert callable(dot::edge::stmt::node.__init__)


def test_dot::edge::stmt::node_constructor_args():
    sig = inspect.signature(dot::edge::stmt::node.__init__)
    params = list(sig.parameters.keys())



def test_dot::stmt_is_not_abstract():
    assert not inspect.isabstract(dot::stmt)


def test_dot::stmt_constructor_exists():
    assert callable(dot::stmt.__init__)


def test_dot::stmt_constructor_args():
    sig = inspect.signature(dot::stmt.__init__)
    params = list(sig.parameters.keys())

def test_edgeop_exists():
    # Check that the Enumeration exists
    assert edgeop is not None

def test_edgeop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in edgeop]
    expected_literals = [
        "directed",
        "undirected",
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
dot::edgeRHS::subgraph_strategy = st.builds(
    dot::edgeRHS::subgraph,
)
dot::edgeRHS::node_strategy = st.builds(
    dot::edgeRHS::node,
)
dot::a::list_strategy = st.builds(
    dot::a::list,
    name=
        safe_text,
    value=
        safe_text
)
dot::attr::list_strategy = st.builds(
    dot::attr::list,
)
dot::edgeRHS_strategy = st.builds(
    dot::edgeRHS,
    op=
        safe_text
)
dot::node::id_strategy = st.builds(
    dot::node::id,
    name=
        safe_text
)
dot::graph_strategy = st.builds(
    dot::graph,
    type=
        safe_text,
    strict=
        st.booleans(),
    name=
        safe_text
)
dot::graphvizmodel_strategy = st.builds(
    dot::graphvizmodel,
)
stmt_strategy = st.builds(
    stmt,
)
dot::node::stmt_strategy = st.builds(
    dot::node::stmt,
    name=
        safe_text
)
dot::edge::stmt::subgraph_strategy = st.builds(
    dot::edge::stmt::subgraph,
)
dot::subgraph_strategy = st.builds(
    dot::subgraph,
    name=
        safe_text
)
dot::attr::stmt_strategy = st.builds(
    dot::attr::stmt,
    type=
        safe_text
)
dot::attribute_strategy = st.builds(
    dot::attribute,
    value=
        safe_text,
    name=
        safe_text
)
dot::edge::stmt::node_strategy = st.builds(
    dot::edge::stmt::node,
)
dot::stmt_strategy = st.builds(
    dot::stmt,
)

@given(instance=edgeRHS_strategy)
@settings(max_examples=50)
def test_edgerhs_instantiation(instance):
    assert isinstance(instance, edgeRHS)

@given(instance=dot::edgeRHS::subgraph_strategy)
@settings(max_examples=50)
def test_dot::edgerhs::subgraph_instantiation(instance):
    assert isinstance(instance, dot::edgeRHS::subgraph)

@given(instance=dot::edgeRHS::node_strategy)
@settings(max_examples=50)
def test_dot::edgerhs::node_instantiation(instance):
    assert isinstance(instance, dot::edgeRHS::node)

@given(instance=dot::a::list_strategy)
@settings(max_examples=50)
def test_dot::a::list_instantiation(instance):
    assert isinstance(instance, dot::a::list)

@given(instance=dot::a::list_strategy)
def test_dot::a::list_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dot::a::list_strategy)
def test_dot::a::list_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dot::a::list_strategy)
def test_dot::a::list_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=dot::a::list_strategy)
def test_dot::a::list_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=dot::attr::list_strategy)
@settings(max_examples=50)
def test_dot::attr::list_instantiation(instance):
    assert isinstance(instance, dot::attr::list)

@given(instance=dot::edgeRHS_strategy)
@settings(max_examples=50)
def test_dot::edgerhs_instantiation(instance):
    assert isinstance(instance, dot::edgeRHS)

@given(instance=dot::edgeRHS_strategy)
def test_dot::edgerhs_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=dot::edgeRHS_strategy)
def test_dot::edgerhs_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=dot::node::id_strategy)
@settings(max_examples=50)
def test_dot::node::id_instantiation(instance):
    assert isinstance(instance, dot::node::id)

@given(instance=dot::node::id_strategy)
def test_dot::node::id_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dot::node::id_strategy)
def test_dot::node::id_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dot::graph_strategy)
@settings(max_examples=50)
def test_dot::graph_instantiation(instance):
    assert isinstance(instance, dot::graph)

@given(instance=dot::graph_strategy)
def test_dot::graph_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=dot::graph_strategy)
def test_dot::graph_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=dot::graph_strategy)
def test_dot::graph_strict_type(instance):
    assert isinstance(instance.strict, bool)


@given(instance=dot::graph_strategy)
def test_dot::graph_strict_setter(instance):
    original = instance.strict
    instance.strict = original
    assert instance.strict == original

@given(instance=dot::graph_strategy)
def test_dot::graph_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dot::graph_strategy)
def test_dot::graph_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dot::graphvizmodel_strategy)
@settings(max_examples=50)
def test_dot::graphvizmodel_instantiation(instance):
    assert isinstance(instance, dot::graphvizmodel)

@given(instance=stmt_strategy)
@settings(max_examples=50)
def test_stmt_instantiation(instance):
    assert isinstance(instance, stmt)

@given(instance=dot::node::stmt_strategy)
@settings(max_examples=50)
def test_dot::node::stmt_instantiation(instance):
    assert isinstance(instance, dot::node::stmt)

@given(instance=dot::node::stmt_strategy)
def test_dot::node::stmt_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dot::node::stmt_strategy)
def test_dot::node::stmt_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dot::edge::stmt::subgraph_strategy)
@settings(max_examples=50)
def test_dot::edge::stmt::subgraph_instantiation(instance):
    assert isinstance(instance, dot::edge::stmt::subgraph)

@given(instance=dot::subgraph_strategy)
@settings(max_examples=50)
def test_dot::subgraph_instantiation(instance):
    assert isinstance(instance, dot::subgraph)

@given(instance=dot::subgraph_strategy)
def test_dot::subgraph_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dot::subgraph_strategy)
def test_dot::subgraph_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dot::attr::stmt_strategy)
@settings(max_examples=50)
def test_dot::attr::stmt_instantiation(instance):
    assert isinstance(instance, dot::attr::stmt)

@given(instance=dot::attr::stmt_strategy)
def test_dot::attr::stmt_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=dot::attr::stmt_strategy)
def test_dot::attr::stmt_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=dot::attribute_strategy)
@settings(max_examples=50)
def test_dot::attribute_instantiation(instance):
    assert isinstance(instance, dot::attribute)

@given(instance=dot::attribute_strategy)
def test_dot::attribute_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=dot::attribute_strategy)
def test_dot::attribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=dot::attribute_strategy)
def test_dot::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dot::attribute_strategy)
def test_dot::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dot::edge::stmt::node_strategy)
@settings(max_examples=50)
def test_dot::edge::stmt::node_instantiation(instance):
    assert isinstance(instance, dot::edge::stmt::node)

@given(instance=dot::stmt_strategy)
@settings(max_examples=50)
def test_dot::stmt_instantiation(instance):
    assert isinstance(instance, dot::stmt)
