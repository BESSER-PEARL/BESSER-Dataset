import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    DAG_Edge,
    DAG_Node,
    DAG_Revision,
    DAG_Graph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dag_edge_is_not_abstract():
    assert not inspect.isabstract(DAG_Edge)


def test_dag_edge_constructor_exists():
    assert callable(DAG_Edge.__init__)


def test_dag_edge_constructor_args():
    sig = inspect.signature(DAG_Edge.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "ID" in params, "Missing parameter 'ID'"

def test_dag_edge_has_name():
    assert hasattr(DAG_Edge, "name")
    descriptor = None
    for klass in DAG_Edge.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dag_edge_has_ID():
    assert hasattr(DAG_Edge, "ID")
    descriptor = None
    for klass in DAG_Edge.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_dag_node_is_not_abstract():
    assert not inspect.isabstract(DAG_Node)


def test_dag_node_constructor_exists():
    assert callable(DAG_Node.__init__)


def test_dag_node_constructor_args():
    sig = inspect.signature(DAG_Node.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"
    assert "name" in params, "Missing parameter 'name'"
    assert "ID" in params, "Missing parameter 'ID'"

def test_dag_node_has_level():
    assert hasattr(DAG_Node, "level")
    descriptor = None
    for klass in DAG_Node.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_dag_node_has_name():
    assert hasattr(DAG_Node, "name")
    descriptor = None
    for klass in DAG_Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dag_node_has_ID():
    assert hasattr(DAG_Node, "ID")
    descriptor = None
    for klass in DAG_Node.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_dag_revision_is_not_abstract():
    assert not inspect.isabstract(DAG_Revision)


def test_dag_revision_constructor_exists():
    assert callable(DAG_Revision.__init__)


def test_dag_revision_constructor_args():
    sig = inspect.signature(DAG_Revision.__init__)
    params = list(sig.parameters.keys())



def test_dag_graph_is_not_abstract():
    assert not inspect.isabstract(DAG_Graph)


def test_dag_graph_constructor_exists():
    assert callable(DAG_Graph.__init__)


def test_dag_graph_constructor_args():
    sig = inspect.signature(DAG_Graph.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dag_graph_has_name():
    assert hasattr(DAG_Graph, "name")
    descriptor = None
    for klass in DAG_Graph.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)


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
DAG_Edge_strategy = st.builds(
    DAG_Edge,
    name=
        safe_text,
    ID=
        st.integers()
)
DAG_Node_strategy = st.builds(
    DAG_Node,
    level=
        st.integers(),
    name=
        safe_text,
    ID=
        st.integers()
)
DAG_Revision_strategy = st.builds(
    DAG_Revision,
)
DAG_Graph_strategy = st.builds(
    DAG_Graph,
    name=
        safe_text
)

@given(instance=DAG_Edge_strategy)
@settings(max_examples=50)
def test_dag_edge_instantiation(instance):
    assert isinstance(instance, DAG_Edge)



@given(instance=DAG_Edge_strategy)
def test_dag_edge_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=DAG_Edge_strategy)
def test_dag_edge_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=DAG_Node_strategy)
@settings(max_examples=50)
def test_dag_node_instantiation(instance):
    assert isinstance(instance, DAG_Node)



@given(instance=DAG_Node_strategy)
def test_dag_node_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original



@given(instance=DAG_Node_strategy)
def test_dag_node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=DAG_Node_strategy)
def test_dag_node_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=DAG_Revision_strategy)
@settings(max_examples=50)
def test_dag_revision_instantiation(instance):
    assert isinstance(instance, DAG_Revision)

@given(instance=DAG_Graph_strategy)
@settings(max_examples=50)
def test_dag_graph_instantiation(instance):
    assert isinstance(instance, DAG_Graph)



@given(instance=DAG_Graph_strategy)
def test_dag_graph_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
