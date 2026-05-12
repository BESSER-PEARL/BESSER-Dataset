import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    mgraph_MEdge,
    mgraph_MNode,
    mgraph_MGraph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mgraph_medge_is_not_abstract():
    assert not inspect.isabstract(mgraph_MEdge)


def test_mgraph_medge_constructor_exists():
    assert callable(mgraph_MEdge.__init__)


def test_mgraph_medge_constructor_args():
    sig = inspect.signature(mgraph_MEdge.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mgraph_medge_has_name():
    assert hasattr(mgraph_MEdge, "name")
    descriptor = None
    for klass in mgraph_MEdge.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mgraph_mnode_is_not_abstract():
    assert not inspect.isabstract(mgraph_MNode)


def test_mgraph_mnode_constructor_exists():
    assert callable(mgraph_MNode.__init__)


def test_mgraph_mnode_constructor_args():
    sig = inspect.signature(mgraph_MNode.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mgraph_mnode_has_name():
    assert hasattr(mgraph_MNode, "name")
    descriptor = None
    for klass in mgraph_MNode.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mgraph_mgraph_is_not_abstract():
    assert not inspect.isabstract(mgraph_MGraph)


def test_mgraph_mgraph_constructor_exists():
    assert callable(mgraph_MGraph.__init__)


def test_mgraph_mgraph_constructor_args():
    sig = inspect.signature(mgraph_MGraph.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mgraph_mgraph_has_name():
    assert hasattr(mgraph_MGraph, "name")
    descriptor = None
    for klass in mgraph_MGraph.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
mgraph_MEdge_strategy = st.builds(
    mgraph_MEdge,
    name=
        safe_text
)
mgraph_MNode_strategy = st.builds(
    mgraph_MNode,
    name=
        safe_text
)
mgraph_MGraph_strategy = st.builds(
    mgraph_MGraph,
    name=
        safe_text
)

@given(instance=mgraph_MEdge_strategy)
@settings(max_examples=50)
def test_mgraph_medge_instantiation(instance):
    assert isinstance(instance, mgraph_MEdge)



@given(instance=mgraph_MEdge_strategy)
def test_mgraph_medge_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mgraph_MNode_strategy)
@settings(max_examples=50)
def test_mgraph_mnode_instantiation(instance):
    assert isinstance(instance, mgraph_MNode)



@given(instance=mgraph_MNode_strategy)
def test_mgraph_mnode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mgraph_MGraph_strategy)
@settings(max_examples=50)
def test_mgraph_mgraph_instantiation(instance):
    assert isinstance(instance, mgraph_MGraph)



@given(instance=mgraph_MGraph_strategy)
def test_mgraph_mgraph_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
