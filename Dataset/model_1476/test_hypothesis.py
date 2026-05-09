import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    mgraph::MEdge,
    mgraph::MNode,
    mgraph::MGraph,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_mgraph::medge_is_not_abstract():
    assert not inspect.isabstract(mgraph::MEdge)


def test_mgraph::medge_constructor_exists():
    assert callable(mgraph::MEdge.__init__)


def test_mgraph::medge_constructor_args():
    sig = inspect.signature(mgraph::MEdge.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mgraph::medge_has_name():
    assert hasattr(mgraph::MEdge, "name")
    descriptor = None
    for klass in mgraph::MEdge.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mgraph::mnode_is_not_abstract():
    assert not inspect.isabstract(mgraph::MNode)


def test_mgraph::mnode_constructor_exists():
    assert callable(mgraph::MNode.__init__)


def test_mgraph::mnode_constructor_args():
    sig = inspect.signature(mgraph::MNode.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mgraph::mnode_has_name():
    assert hasattr(mgraph::MNode, "name")
    descriptor = None
    for klass in mgraph::MNode.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mgraph::mgraph_is_not_abstract():
    assert not inspect.isabstract(mgraph::MGraph)


def test_mgraph::mgraph_constructor_exists():
    assert callable(mgraph::MGraph.__init__)


def test_mgraph::mgraph_constructor_args():
    sig = inspect.signature(mgraph::MGraph.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mgraph::mgraph_has_name():
    assert hasattr(mgraph::MGraph, "name")
    descriptor = None
    for klass in mgraph::MGraph.__mro__:
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
mgraph::MEdge_strategy = st.builds(
    mgraph::MEdge,
    name=
        safe_text
)
mgraph::MNode_strategy = st.builds(
    mgraph::MNode,
    name=
        safe_text
)
mgraph::MGraph_strategy = st.builds(
    mgraph::MGraph,
    name=
        safe_text
)

@given(instance=mgraph::MEdge_strategy)
@settings(max_examples=50)
def test_mgraph::medge_instantiation(instance):
    assert isinstance(instance, mgraph::MEdge)

@given(instance=mgraph::MEdge_strategy)
def test_mgraph::medge_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mgraph::MEdge_strategy)
def test_mgraph::medge_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mgraph::MNode_strategy)
@settings(max_examples=50)
def test_mgraph::mnode_instantiation(instance):
    assert isinstance(instance, mgraph::MNode)

@given(instance=mgraph::MNode_strategy)
def test_mgraph::mnode_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mgraph::MNode_strategy)
def test_mgraph::mnode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=mgraph::MGraph_strategy)
@settings(max_examples=50)
def test_mgraph::mgraph_instantiation(instance):
    assert isinstance(instance, mgraph::MGraph)

@given(instance=mgraph::MGraph_strategy)
def test_mgraph::mgraph_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mgraph::MGraph_strategy)
def test_mgraph::mgraph_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
