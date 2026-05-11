import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    SimpleTree::NodeKind,
    SimpleTree::Tree,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simpletree::nodekind_is_not_abstract():
    assert not inspect.isabstract(SimpleTree::NodeKind)


def test_simpletree::nodekind_constructor_exists():
    assert callable(SimpleTree::NodeKind.__init__)


def test_simpletree::nodekind_constructor_args():
    sig = inspect.signature(SimpleTree::NodeKind.__init__)
    params = list(sig.parameters.keys())



def test_simpletree::tree_is_not_abstract():
    assert not inspect.isabstract(SimpleTree::Tree)


def test_simpletree::tree_constructor_exists():
    assert callable(SimpleTree::Tree.__init__)


def test_simpletree::tree_constructor_args():
    sig = inspect.signature(SimpleTree::Tree.__init__)
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
SimpleTree::NodeKind_strategy = st.builds(
    SimpleTree::NodeKind,
)
SimpleTree::Tree_strategy = st.builds(
    SimpleTree::Tree,
)

@given(instance=SimpleTree::NodeKind_strategy)
@settings(max_examples=50)
def test_simpletree::nodekind_instantiation(instance):
    assert isinstance(instance, SimpleTree::NodeKind)

@given(instance=SimpleTree::Tree_strategy)
@settings(max_examples=50)
def test_simpletree::tree_instantiation(instance):
    assert isinstance(instance, SimpleTree::Tree)
