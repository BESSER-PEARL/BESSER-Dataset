import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    graph3::Node,
    graph3::Graph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_graph3::node_is_not_abstract():
    assert not inspect.isabstract(graph3::Node)


def test_graph3::node_constructor_exists():
    assert callable(graph3::Node.__init__)


def test_graph3::node_constructor_args():
    sig = inspect.signature(graph3::Node.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_graph3::node_has_text():
    assert hasattr(graph3::Node, "text")
    descriptor = None
    for klass in graph3::Node.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_graph3::graph_is_not_abstract():
    assert not inspect.isabstract(graph3::Graph)


def test_graph3::graph_constructor_exists():
    assert callable(graph3::Graph.__init__)


def test_graph3::graph_constructor_args():
    sig = inspect.signature(graph3::Graph.__init__)
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
graph3::Node_strategy = st.builds(
    graph3::Node,
    text=
        safe_text
)
graph3::Graph_strategy = st.builds(
    graph3::Graph,
)

@given(instance=graph3::Node_strategy)
@settings(max_examples=50)
def test_graph3::node_instantiation(instance):
    assert isinstance(instance, graph3::Node)

@given(instance=graph3::Node_strategy)
def test_graph3::node_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=graph3::Node_strategy)
def test_graph3::node_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=graph3::Graph_strategy)
@settings(max_examples=50)
def test_graph3::graph_instantiation(instance):
    assert isinstance(instance, graph3::Graph)
