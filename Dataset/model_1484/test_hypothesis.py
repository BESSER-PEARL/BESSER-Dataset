import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    graph::GraphIntf,
    graph::Graph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_graph::graphintf_is_not_abstract():
    assert not inspect.isabstract(graph::GraphIntf)


def test_graph::graphintf_constructor_exists():
    assert callable(graph::GraphIntf.__init__)


def test_graph::graphintf_constructor_args():
    sig = inspect.signature(graph::GraphIntf.__init__)
    params = list(sig.parameters.keys())



def test_graph::graph_is_not_abstract():
    assert not inspect.isabstract(graph::Graph)


def test_graph::graph_constructor_exists():
    assert callable(graph::Graph.__init__)


def test_graph::graph_constructor_args():
    sig = inspect.signature(graph::Graph.__init__)
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
graph::GraphIntf_strategy = st.builds(
    graph::GraphIntf,
)
graph::Graph_strategy = st.builds(
    graph::Graph,
)

@given(instance=graph::GraphIntf_strategy)
@settings(max_examples=50)
def test_graph::graphintf_instantiation(instance):
    assert isinstance(instance, graph::GraphIntf)

@given(instance=graph::Graph_strategy)
@settings(max_examples=50)
def test_graph::graph_instantiation(instance):
    assert isinstance(instance, graph::Graph)
