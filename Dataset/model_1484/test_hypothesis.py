import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    graph_GraphIntf,
    graph_Graph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_graph_graphintf_is_not_abstract():
    assert not inspect.isabstract(graph_GraphIntf)


def test_graph_graphintf_constructor_exists():
    assert callable(graph_GraphIntf.__init__)


def test_graph_graphintf_constructor_args():
    sig = inspect.signature(graph_GraphIntf.__init__)
    params = list(sig.parameters.keys())



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
graph_GraphIntf_strategy = st.builds(
    graph_GraphIntf,
)
graph_Graph_strategy = st.builds(
    graph_Graph,
)

@given(instance=graph_GraphIntf_strategy)
@settings(max_examples=50)
def test_graph_graphintf_instantiation(instance):
    assert isinstance(instance, graph_GraphIntf)

@given(instance=graph_Graph_strategy)
@settings(max_examples=50)
def test_graph_graph_instantiation(instance):
    assert isinstance(instance, graph_Graph)
