import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    StructuredTree::NodeKind,
    StructuredTree::Tree,
    NodeKind,
    StructuredTree::LeafKind,
    StructuredTree::BranchKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_structuredtree::nodekind_is_not_abstract():
    assert not inspect.isabstract(StructuredTree::NodeKind)


def test_structuredtree::nodekind_constructor_exists():
    assert callable(StructuredTree::NodeKind.__init__)


def test_structuredtree::nodekind_constructor_args():
    sig = inspect.signature(StructuredTree::NodeKind.__init__)
    params = list(sig.parameters.keys())



def test_structuredtree::tree_is_not_abstract():
    assert not inspect.isabstract(StructuredTree::Tree)


def test_structuredtree::tree_constructor_exists():
    assert callable(StructuredTree::Tree.__init__)


def test_structuredtree::tree_constructor_args():
    sig = inspect.signature(StructuredTree::Tree.__init__)
    params = list(sig.parameters.keys())



def test_nodekind_is_not_abstract():
    assert not inspect.isabstract(NodeKind)


def test_nodekind_constructor_exists():
    assert callable(NodeKind.__init__)


def test_nodekind_constructor_args():
    sig = inspect.signature(NodeKind.__init__)
    params = list(sig.parameters.keys())



def test_structuredtree::leafkind_is_not_abstract():
    assert not inspect.isabstract(StructuredTree::LeafKind)


def test_structuredtree::leafkind_constructor_exists():
    assert callable(StructuredTree::LeafKind.__init__)


def test_structuredtree::leafkind_constructor_args():
    sig = inspect.signature(StructuredTree::LeafKind.__init__)
    params = list(sig.parameters.keys())



def test_structuredtree::branchkind_is_not_abstract():
    assert not inspect.isabstract(StructuredTree::BranchKind)


def test_structuredtree::branchkind_constructor_exists():
    assert callable(StructuredTree::BranchKind.__init__)


def test_structuredtree::branchkind_constructor_args():
    sig = inspect.signature(StructuredTree::BranchKind.__init__)
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
StructuredTree::NodeKind_strategy = st.builds(
    StructuredTree::NodeKind,
)
StructuredTree::Tree_strategy = st.builds(
    StructuredTree::Tree,
)
NodeKind_strategy = st.builds(
    NodeKind,
)
StructuredTree::LeafKind_strategy = st.builds(
    StructuredTree::LeafKind,
)
StructuredTree::BranchKind_strategy = st.builds(
    StructuredTree::BranchKind,
)

@given(instance=StructuredTree::NodeKind_strategy)
@settings(max_examples=50)
def test_structuredtree::nodekind_instantiation(instance):
    assert isinstance(instance, StructuredTree::NodeKind)

@given(instance=StructuredTree::Tree_strategy)
@settings(max_examples=50)
def test_structuredtree::tree_instantiation(instance):
    assert isinstance(instance, StructuredTree::Tree)

@given(instance=NodeKind_strategy)
@settings(max_examples=50)
def test_nodekind_instantiation(instance):
    assert isinstance(instance, NodeKind)

@given(instance=StructuredTree::LeafKind_strategy)
@settings(max_examples=50)
def test_structuredtree::leafkind_instantiation(instance):
    assert isinstance(instance, StructuredTree::LeafKind)

@given(instance=StructuredTree::BranchKind_strategy)
@settings(max_examples=50)
def test_structuredtree::branchkind_instantiation(instance):
    assert isinstance(instance, StructuredTree::BranchKind)
