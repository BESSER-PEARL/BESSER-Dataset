import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    dfg_DfgEdge,
    dfg_DfgVertex,
    dfg_DfgGraph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_dfg_dfgedge_is_not_abstract():
    assert not inspect.isabstract(dfg_DfgEdge)


def test_dfg_dfgedge_constructor_exists():
    assert callable(dfg_DfgEdge.__init__)


def test_dfg_dfgedge_constructor_args():
    sig = inspect.signature(dfg_DfgEdge.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_dfg_dfgedge_has_label():
    assert hasattr(dfg_DfgEdge, "label")
    descriptor = None
    for klass in dfg_DfgEdge.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_dfg_dfgvertex_is_not_abstract():
    assert not inspect.isabstract(dfg_DfgVertex)


def test_dfg_dfgvertex_constructor_exists():
    assert callable(dfg_DfgVertex.__init__)


def test_dfg_dfgvertex_constructor_args():
    sig = inspect.signature(dfg_DfgVertex.__init__)
    params = list(sig.parameters.keys())
    assert "mappings" in params, "Missing parameter 'mappings'"

def test_dfg_dfgvertex_has_mappings():
    assert hasattr(dfg_DfgVertex, "mappings")
    descriptor = None
    for klass in dfg_DfgVertex.__mro__:
        if "mappings" in klass.__dict__:
            descriptor = klass.__dict__["mappings"]
            break
    assert isinstance(descriptor, property)



def test_dfg_dfggraph_is_not_abstract():
    assert not inspect.isabstract(dfg_DfgGraph)


def test_dfg_dfggraph_constructor_exists():
    assert callable(dfg_DfgGraph.__init__)


def test_dfg_dfggraph_constructor_args():
    sig = inspect.signature(dfg_DfgGraph.__init__)
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
dfg_DfgEdge_strategy = st.builds(
    dfg_DfgEdge,
    label=
        safe_text
)
dfg_DfgVertex_strategy = st.builds(
    dfg_DfgVertex,
    mappings=
        safe_text
)
dfg_DfgGraph_strategy = st.builds(
    dfg_DfgGraph,
)

@given(instance=dfg_DfgEdge_strategy)
@settings(max_examples=50)
def test_dfg_dfgedge_instantiation(instance):
    assert isinstance(instance, dfg_DfgEdge)



@given(instance=dfg_DfgEdge_strategy)
def test_dfg_dfgedge_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=dfg_DfgVertex_strategy)
@settings(max_examples=50)
def test_dfg_dfgvertex_instantiation(instance):
    assert isinstance(instance, dfg_DfgVertex)



@given(instance=dfg_DfgVertex_strategy)
def test_dfg_dfgvertex_mappings_setter(instance):
    original = instance.mappings
    instance.mappings = original
    assert instance.mappings == original

@given(instance=dfg_DfgGraph_strategy)
@settings(max_examples=50)
def test_dfg_dfggraph_instantiation(instance):
    assert isinstance(instance, dfg_DfgGraph)
