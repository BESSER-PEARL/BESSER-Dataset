import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    OverlappingTree::NodeKind,
    OverlappingTree::Tree,
    OverlappingTree::Child,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_overlappingtree::nodekind_is_not_abstract():
    assert not inspect.isabstract(OverlappingTree::NodeKind)


def test_overlappingtree::nodekind_constructor_exists():
    assert callable(OverlappingTree::NodeKind.__init__)


def test_overlappingtree::nodekind_constructor_args():
    sig = inspect.signature(OverlappingTree::NodeKind.__init__)
    params = list(sig.parameters.keys())



def test_overlappingtree::tree_is_not_abstract():
    assert not inspect.isabstract(OverlappingTree::Tree)


def test_overlappingtree::tree_constructor_exists():
    assert callable(OverlappingTree::Tree.__init__)


def test_overlappingtree::tree_constructor_args():
    sig = inspect.signature(OverlappingTree::Tree.__init__)
    params = list(sig.parameters.keys())



def test_overlappingtree::child_is_not_abstract():
    assert not inspect.isabstract(OverlappingTree::Child)


def test_overlappingtree::child_constructor_exists():
    assert callable(OverlappingTree::Child.__init__)


def test_overlappingtree::child_constructor_args():
    sig = inspect.signature(OverlappingTree::Child.__init__)
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
OverlappingTree::NodeKind_strategy = st.builds(
    OverlappingTree::NodeKind,
)
OverlappingTree::Tree_strategy = st.builds(
    OverlappingTree::Tree,
)
OverlappingTree::Child_strategy = st.builds(
    OverlappingTree::Child,
)

@given(instance=OverlappingTree::NodeKind_strategy)
@settings(max_examples=50)
def test_overlappingtree::nodekind_instantiation(instance):
    assert isinstance(instance, OverlappingTree::NodeKind)

@given(instance=OverlappingTree::Tree_strategy)
@settings(max_examples=50)
def test_overlappingtree::tree_instantiation(instance):
    assert isinstance(instance, OverlappingTree::Tree)

@given(instance=OverlappingTree::Child_strategy)
@settings(max_examples=50)
def test_overlappingtree::child_instantiation(instance):
    assert isinstance(instance, OverlappingTree::Child)
