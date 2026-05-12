import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    dag_Edge,
    dag_Vertex,
    dag_DAG,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dag_edge_is_not_abstract():
    assert not inspect.isabstract(dag_Edge)


def test_dag_edge_constructor_exists():
    assert callable(dag_Edge.__init__)


def test_dag_edge_constructor_args():
    sig = inspect.signature(dag_Edge.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_dag_edge_has_id():
    assert hasattr(dag_Edge, "id")
    descriptor = None
    for klass in dag_Edge.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_dag_vertex_is_not_abstract():
    assert not inspect.isabstract(dag_Vertex)


def test_dag_vertex_constructor_exists():
    assert callable(dag_Vertex.__init__)


def test_dag_vertex_constructor_args():
    sig = inspect.signature(dag_Vertex.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_dag_vertex_has_id():
    assert hasattr(dag_Vertex, "id")
    descriptor = None
    for klass in dag_Vertex.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_dag_dag_is_not_abstract():
    assert not inspect.isabstract(dag_DAG)


def test_dag_dag_constructor_exists():
    assert callable(dag_DAG.__init__)


def test_dag_dag_constructor_args():
    sig = inspect.signature(dag_DAG.__init__)
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
dag_Edge_strategy = st.builds(
    dag_Edge,
    id=
        safe_text
)
dag_Vertex_strategy = st.builds(
    dag_Vertex,
    id=
        safe_text
)
dag_DAG_strategy = st.builds(
    dag_DAG,
)

@given(instance=dag_Edge_strategy)
@settings(max_examples=50)
def test_dag_edge_instantiation(instance):
    assert isinstance(instance, dag_Edge)



@given(instance=dag_Edge_strategy)
def test_dag_edge_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dag_Vertex_strategy)
@settings(max_examples=50)
def test_dag_vertex_instantiation(instance):
    assert isinstance(instance, dag_Vertex)



@given(instance=dag_Vertex_strategy)
def test_dag_vertex_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dag_DAG_strategy)
@settings(max_examples=50)
def test_dag_dag_instantiation(instance):
    assert isinstance(instance, dag_DAG)
