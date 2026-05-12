import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    graph_HasName,
    graph_Root,
    graph_Edge,
    HasName,
    graph_SubNode,
    graph_Node,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_graph_hasname_is_not_abstract():
    assert not inspect.isabstract(graph_HasName)


def test_graph_hasname_constructor_exists():
    assert callable(graph_HasName.__init__)


def test_graph_hasname_constructor_args():
    sig = inspect.signature(graph_HasName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_graph_hasname_has_name():
    assert hasattr(graph_HasName, "name")
    descriptor = None
    for klass in graph_HasName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_graph_root_is_not_abstract():
    assert not inspect.isabstract(graph_Root)


def test_graph_root_constructor_exists():
    assert callable(graph_Root.__init__)


def test_graph_root_constructor_args():
    sig = inspect.signature(graph_Root.__init__)
    params = list(sig.parameters.keys())



def test_graph_edge_is_not_abstract():
    assert not inspect.isabstract(graph_Edge)


def test_graph_edge_constructor_exists():
    assert callable(graph_Edge.__init__)


def test_graph_edge_constructor_args():
    sig = inspect.signature(graph_Edge.__init__)
    params = list(sig.parameters.keys())



def test_hasname_is_not_abstract():
    assert not inspect.isabstract(HasName)


def test_hasname_constructor_exists():
    assert callable(HasName.__init__)


def test_hasname_constructor_args():
    sig = inspect.signature(HasName.__init__)
    params = list(sig.parameters.keys())



def test_graph_subnode_is_not_abstract():
    assert not inspect.isabstract(graph_SubNode)


def test_graph_subnode_constructor_exists():
    assert callable(graph_SubNode.__init__)


def test_graph_subnode_constructor_args():
    sig = inspect.signature(graph_SubNode.__init__)
    params = list(sig.parameters.keys())



def test_graph_node_is_not_abstract():
    assert not inspect.isabstract(graph_Node)


def test_graph_node_constructor_exists():
    assert callable(graph_Node.__init__)


def test_graph_node_constructor_args():
    sig = inspect.signature(graph_Node.__init__)
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
graph_HasName_strategy = st.builds(
    graph_HasName,
    name=
        safe_text
)
graph_Root_strategy = st.builds(
    graph_Root,
)
graph_Edge_strategy = st.builds(
    graph_Edge,
)
HasName_strategy = st.builds(
    HasName,
)
graph_SubNode_strategy = st.builds(
    graph_SubNode,
)
graph_Node_strategy = st.builds(
    graph_Node,
)

@given(instance=graph_HasName_strategy)
@settings(max_examples=50)
def test_graph_hasname_instantiation(instance):
    assert isinstance(instance, graph_HasName)



@given(instance=graph_HasName_strategy)
def test_graph_hasname_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=graph_Root_strategy)
@settings(max_examples=50)
def test_graph_root_instantiation(instance):
    assert isinstance(instance, graph_Root)

@given(instance=graph_Edge_strategy)
@settings(max_examples=50)
def test_graph_edge_instantiation(instance):
    assert isinstance(instance, graph_Edge)

@given(instance=HasName_strategy)
@settings(max_examples=50)
def test_hasname_instantiation(instance):
    assert isinstance(instance, HasName)

@given(instance=graph_SubNode_strategy)
@settings(max_examples=50)
def test_graph_subnode_instantiation(instance):
    assert isinstance(instance, graph_SubNode)

@given(instance=graph_Node_strategy)
@settings(max_examples=50)
def test_graph_node_instantiation(instance):
    assert isinstance(instance, graph_Node)
