import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    dfg::DfgEdge,
    dfg::DfgVertex,
    dfg::DfgGraph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dfg::dfgedge_is_not_abstract():
    assert not inspect.isabstract(dfg::DfgEdge)


def test_dfg::dfgedge_constructor_exists():
    assert callable(dfg::DfgEdge.__init__)


def test_dfg::dfgedge_constructor_args():
    sig = inspect.signature(dfg::DfgEdge.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_dfg::dfgedge_has_label():
    assert hasattr(dfg::DfgEdge, "label")
    descriptor = None
    for klass in dfg::DfgEdge.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_dfg::dfgvertex_is_not_abstract():
    assert not inspect.isabstract(dfg::DfgVertex)


def test_dfg::dfgvertex_constructor_exists():
    assert callable(dfg::DfgVertex.__init__)


def test_dfg::dfgvertex_constructor_args():
    sig = inspect.signature(dfg::DfgVertex.__init__)
    params = list(sig.parameters.keys())
    assert "mappings" in params, "Missing parameter 'mappings'"

def test_dfg::dfgvertex_has_mappings():
    assert hasattr(dfg::DfgVertex, "mappings")
    descriptor = None
    for klass in dfg::DfgVertex.__mro__:
        if "mappings" in klass.__dict__:
            descriptor = klass.__dict__["mappings"]
            break
    assert isinstance(descriptor, property)



def test_dfg::dfggraph_is_not_abstract():
    assert not inspect.isabstract(dfg::DfgGraph)


def test_dfg::dfggraph_constructor_exists():
    assert callable(dfg::DfgGraph.__init__)


def test_dfg::dfggraph_constructor_args():
    sig = inspect.signature(dfg::DfgGraph.__init__)
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
dfg::DfgEdge_strategy = st.builds(
    dfg::DfgEdge,
    label=
        safe_text
)
dfg::DfgVertex_strategy = st.builds(
    dfg::DfgVertex,
    mappings=
        safe_text
)
dfg::DfgGraph_strategy = st.builds(
    dfg::DfgGraph,
)

@given(instance=dfg::DfgEdge_strategy)
@settings(max_examples=50)
def test_dfg::dfgedge_instantiation(instance):
    assert isinstance(instance, dfg::DfgEdge)

@given(instance=dfg::DfgEdge_strategy)
def test_dfg::dfgedge_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=dfg::DfgEdge_strategy)
def test_dfg::dfgedge_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=dfg::DfgVertex_strategy)
@settings(max_examples=50)
def test_dfg::dfgvertex_instantiation(instance):
    assert isinstance(instance, dfg::DfgVertex)

@given(instance=dfg::DfgVertex_strategy)
def test_dfg::dfgvertex_mappings_type(instance):
    assert isinstance(instance.mappings, str)


@given(instance=dfg::DfgVertex_strategy)
def test_dfg::dfgvertex_mappings_setter(instance):
    original = instance.mappings
    instance.mappings = original
    assert instance.mappings == original

@given(instance=dfg::DfgGraph_strategy)
@settings(max_examples=50)
def test_dfg::dfggraph_instantiation(instance):
    assert isinstance(instance, dfg::DfgGraph)
