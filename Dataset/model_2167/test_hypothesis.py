import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    dag::Edge,
    dag::Vertex,
    dag::DAG,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dag::edge_is_not_abstract():
    assert not inspect.isabstract(dag::Edge)


def test_dag::edge_constructor_exists():
    assert callable(dag::Edge.__init__)


def test_dag::edge_constructor_args():
    sig = inspect.signature(dag::Edge.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_dag::edge_has_id():
    assert hasattr(dag::Edge, "id")
    descriptor = None
    for klass in dag::Edge.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_dag::vertex_is_not_abstract():
    assert not inspect.isabstract(dag::Vertex)


def test_dag::vertex_constructor_exists():
    assert callable(dag::Vertex.__init__)


def test_dag::vertex_constructor_args():
    sig = inspect.signature(dag::Vertex.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_dag::vertex_has_id():
    assert hasattr(dag::Vertex, "id")
    descriptor = None
    for klass in dag::Vertex.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_dag::dag_is_not_abstract():
    assert not inspect.isabstract(dag::DAG)


def test_dag::dag_constructor_exists():
    assert callable(dag::DAG.__init__)


def test_dag::dag_constructor_args():
    sig = inspect.signature(dag::DAG.__init__)
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
dag::Edge_strategy = st.builds(
    dag::Edge,
    id=
        safe_text
)
dag::Vertex_strategy = st.builds(
    dag::Vertex,
    id=
        safe_text
)
dag::DAG_strategy = st.builds(
    dag::DAG,
)

@given(instance=dag::Edge_strategy)
@settings(max_examples=50)
def test_dag::edge_instantiation(instance):
    assert isinstance(instance, dag::Edge)

@given(instance=dag::Edge_strategy)
def test_dag::edge_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=dag::Edge_strategy)
def test_dag::edge_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dag::Vertex_strategy)
@settings(max_examples=50)
def test_dag::vertex_instantiation(instance):
    assert isinstance(instance, dag::Vertex)

@given(instance=dag::Vertex_strategy)
def test_dag::vertex_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=dag::Vertex_strategy)
def test_dag::vertex_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=dag::DAG_strategy)
@settings(max_examples=50)
def test_dag::dag_instantiation(instance):
    assert isinstance(instance, dag::DAG)
