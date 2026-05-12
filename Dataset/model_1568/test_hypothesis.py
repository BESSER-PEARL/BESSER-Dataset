import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    graph_Edge,
    graph_Vertice,
    graph_Graph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_graph_edge_is_not_abstract():
    assert not inspect.isabstract(graph_Edge)


def test_graph_edge_constructor_exists():
    assert callable(graph_Edge.__init__)


def test_graph_edge_constructor_args():
    sig = inspect.signature(graph_Edge.__init__)
    params = list(sig.parameters.keys())



def test_graph_vertice_is_not_abstract():
    assert not inspect.isabstract(graph_Vertice)


def test_graph_vertice_constructor_exists():
    assert callable(graph_Vertice.__init__)


def test_graph_vertice_constructor_args():
    sig = inspect.signature(graph_Vertice.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_graph_vertice_has_label():
    assert hasattr(graph_Vertice, "label")
    descriptor = None
    for klass in graph_Vertice.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_graph_graph_is_not_abstract():
    assert not inspect.isabstract(graph_Graph)


def test_graph_graph_constructor_exists():
    assert callable(graph_Graph.__init__)


def test_graph_graph_constructor_args():
    sig = inspect.signature(graph_Graph.__init__)
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
graph_Edge_strategy = st.builds(
    graph_Edge,
)
graph_Vertice_strategy = st.builds(
    graph_Vertice,
    label=
        safe_text
)
graph_Graph_strategy = st.builds(
    graph_Graph,
)

@given(instance=graph_Edge_strategy)
@settings(max_examples=50)
def test_graph_edge_instantiation(instance):
    assert isinstance(instance, graph_Edge)

@given(instance=graph_Vertice_strategy)
@settings(max_examples=50)
def test_graph_vertice_instantiation(instance):
    assert isinstance(instance, graph_Vertice)



@given(instance=graph_Vertice_strategy)
def test_graph_vertice_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=graph_Graph_strategy)
@settings(max_examples=50)
def test_graph_graph_instantiation(instance):
    assert isinstance(instance, graph_Graph)
