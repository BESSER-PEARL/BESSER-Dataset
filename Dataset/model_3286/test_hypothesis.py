import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    traceability::Identifiable,
    traceability::GraphEndToEndTrace,
    traceability::Graph,
    traceability::EDFD,
    traceability::EDFDGraphTrace,
    traceability::EDFDToGraph,
    traceability::NamedEntity,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_traceability::identifiable_is_not_abstract():
    assert not inspect.isabstract(traceability::Identifiable)


def test_traceability::identifiable_constructor_exists():
    assert callable(traceability::Identifiable.__init__)


def test_traceability::identifiable_constructor_args():
    sig = inspect.signature(traceability::Identifiable.__init__)
    params = list(sig.parameters.keys())



def test_traceability::graphendtoendtrace_is_not_abstract():
    assert not inspect.isabstract(traceability::GraphEndToEndTrace)


def test_traceability::graphendtoendtrace_constructor_exists():
    assert callable(traceability::GraphEndToEndTrace.__init__)


def test_traceability::graphendtoendtrace_constructor_args():
    sig = inspect.signature(traceability::GraphEndToEndTrace.__init__)
    params = list(sig.parameters.keys())



def test_traceability::graph_is_not_abstract():
    assert not inspect.isabstract(traceability::Graph)


def test_traceability::graph_constructor_exists():
    assert callable(traceability::Graph.__init__)


def test_traceability::graph_constructor_args():
    sig = inspect.signature(traceability::Graph.__init__)
    params = list(sig.parameters.keys())



def test_traceability::edfd_is_not_abstract():
    assert not inspect.isabstract(traceability::EDFD)


def test_traceability::edfd_constructor_exists():
    assert callable(traceability::EDFD.__init__)


def test_traceability::edfd_constructor_args():
    sig = inspect.signature(traceability::EDFD.__init__)
    params = list(sig.parameters.keys())



def test_traceability::edfdgraphtrace_is_not_abstract():
    assert not inspect.isabstract(traceability::EDFDGraphTrace)


def test_traceability::edfdgraphtrace_constructor_exists():
    assert callable(traceability::EDFDGraphTrace.__init__)


def test_traceability::edfdgraphtrace_constructor_args():
    sig = inspect.signature(traceability::EDFDGraphTrace.__init__)
    params = list(sig.parameters.keys())



def test_traceability::edfdtograph_is_not_abstract():
    assert not inspect.isabstract(traceability::EDFDToGraph)


def test_traceability::edfdtograph_constructor_exists():
    assert callable(traceability::EDFDToGraph.__init__)


def test_traceability::edfdtograph_constructor_args():
    sig = inspect.signature(traceability::EDFDToGraph.__init__)
    params = list(sig.parameters.keys())



def test_traceability::namedentity_is_not_abstract():
    assert not inspect.isabstract(traceability::NamedEntity)


def test_traceability::namedentity_constructor_exists():
    assert callable(traceability::NamedEntity.__init__)


def test_traceability::namedentity_constructor_args():
    sig = inspect.signature(traceability::NamedEntity.__init__)
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
traceability::Identifiable_strategy = st.builds(
    traceability::Identifiable,
)
traceability::GraphEndToEndTrace_strategy = st.builds(
    traceability::GraphEndToEndTrace,
)
traceability::Graph_strategy = st.builds(
    traceability::Graph,
)
traceability::EDFD_strategy = st.builds(
    traceability::EDFD,
)
traceability::EDFDGraphTrace_strategy = st.builds(
    traceability::EDFDGraphTrace,
)
traceability::EDFDToGraph_strategy = st.builds(
    traceability::EDFDToGraph,
)
traceability::NamedEntity_strategy = st.builds(
    traceability::NamedEntity,
)

@given(instance=traceability::Identifiable_strategy)
@settings(max_examples=50)
def test_traceability::identifiable_instantiation(instance):
    assert isinstance(instance, traceability::Identifiable)

@given(instance=traceability::GraphEndToEndTrace_strategy)
@settings(max_examples=50)
def test_traceability::graphendtoendtrace_instantiation(instance):
    assert isinstance(instance, traceability::GraphEndToEndTrace)

@given(instance=traceability::Graph_strategy)
@settings(max_examples=50)
def test_traceability::graph_instantiation(instance):
    assert isinstance(instance, traceability::Graph)

@given(instance=traceability::EDFD_strategy)
@settings(max_examples=50)
def test_traceability::edfd_instantiation(instance):
    assert isinstance(instance, traceability::EDFD)

@given(instance=traceability::EDFDGraphTrace_strategy)
@settings(max_examples=50)
def test_traceability::edfdgraphtrace_instantiation(instance):
    assert isinstance(instance, traceability::EDFDGraphTrace)

@given(instance=traceability::EDFDToGraph_strategy)
@settings(max_examples=50)
def test_traceability::edfdtograph_instantiation(instance):
    assert isinstance(instance, traceability::EDFDToGraph)

@given(instance=traceability::NamedEntity_strategy)
@settings(max_examples=50)
def test_traceability::namedentity_instantiation(instance):
    assert isinstance(instance, traceability::NamedEntity)
