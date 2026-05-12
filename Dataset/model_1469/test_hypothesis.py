import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    graph3_Graph,
    graph3_Node,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_graph3_graph_is_not_abstract():
    assert not inspect.isabstract(graph3_Graph)


def test_graph3_graph_constructor_exists():
    assert callable(graph3_Graph.__init__)


def test_graph3_graph_constructor_args():
    sig = inspect.signature(graph3_Graph.__init__)
    params = list(sig.parameters.keys())



def test_graph3_node_is_not_abstract():
    assert not inspect.isabstract(graph3_Node)


def test_graph3_node_constructor_exists():
    assert callable(graph3_Node.__init__)


def test_graph3_node_constructor_args():
    sig = inspect.signature(graph3_Node.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_graph3_node_has_text():
    assert hasattr(graph3_Node, "text")
    descriptor = None
    for klass in graph3_Node.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
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
graph3_Graph_strategy = st.builds(
    graph3_Graph,
)
graph3_Node_strategy = st.builds(
    graph3_Node,
    text=
        safe_text
)

@given(instance=graph3_Graph_strategy)
@settings(max_examples=50)
def test_graph3_graph_instantiation(instance):
    assert isinstance(instance, graph3_Graph)

@given(instance=graph3_Node_strategy)
@settings(max_examples=50)
def test_graph3_node_instantiation(instance):
    assert isinstance(instance, graph3_Node)



@given(instance=graph3_Node_strategy)
def test_graph3_node_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original
