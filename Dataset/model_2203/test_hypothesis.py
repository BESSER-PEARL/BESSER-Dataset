import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    TreeElement,
    MMTree::Leaf,
    MMTree::Node,
    MMTree::TreeElement,
    LeafSize,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_treeelement_is_not_abstract():
    assert not inspect.isabstract(TreeElement)


def test_treeelement_constructor_exists():
    assert callable(TreeElement.__init__)


def test_treeelement_constructor_args():
    sig = inspect.signature(TreeElement.__init__)
    params = list(sig.parameters.keys())



def test_mmtree::leaf_is_not_abstract():
    assert not inspect.isabstract(MMTree::Leaf)


def test_mmtree::leaf_constructor_exists():
    assert callable(MMTree::Leaf.__init__)


def test_mmtree::leaf_constructor_args():
    sig = inspect.signature(MMTree::Leaf.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"

def test_mmtree::leaf_has_size():
    assert hasattr(MMTree::Leaf, "size")
    descriptor = None
    for klass in MMTree::Leaf.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_mmtree::node_is_not_abstract():
    assert not inspect.isabstract(MMTree::Node)


def test_mmtree::node_constructor_exists():
    assert callable(MMTree::Node.__init__)


def test_mmtree::node_constructor_args():
    sig = inspect.signature(MMTree::Node.__init__)
    params = list(sig.parameters.keys())



def test_mmtree::treeelement_is_not_abstract():
    assert not inspect.isabstract(MMTree::TreeElement)


def test_mmtree::treeelement_constructor_exists():
    assert callable(MMTree::TreeElement.__init__)


def test_mmtree::treeelement_constructor_args():
    sig = inspect.signature(MMTree::TreeElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mmtree::treeelement_has_name():
    assert hasattr(MMTree::TreeElement, "name")
    descriptor = None
    for klass in MMTree::TreeElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_leafsize_exists():
    # Check that the Enumeration exists
    assert LeafSize is not None

def test_leafsize_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LeafSize]
    expected_literals = [
        "medium",
        "big",
        "small",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LeafSize"


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
TreeElement_strategy = st.builds(
    TreeElement,
)
MMTree::Leaf_strategy = st.builds(
    MMTree::Leaf,
    size=
        safe_text
)
MMTree::Node_strategy = st.builds(
    MMTree::Node,
)
MMTree::TreeElement_strategy = st.builds(
    MMTree::TreeElement,
    name=
        safe_text
)

@given(instance=TreeElement_strategy)
@settings(max_examples=50)
def test_treeelement_instantiation(instance):
    assert isinstance(instance, TreeElement)

@given(instance=MMTree::Leaf_strategy)
@settings(max_examples=50)
def test_mmtree::leaf_instantiation(instance):
    assert isinstance(instance, MMTree::Leaf)

@given(instance=MMTree::Leaf_strategy)
def test_mmtree::leaf_size_type(instance):
    assert isinstance(instance.size, str)


@given(instance=MMTree::Leaf_strategy)
def test_mmtree::leaf_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=MMTree::Node_strategy)
@settings(max_examples=50)
def test_mmtree::node_instantiation(instance):
    assert isinstance(instance, MMTree::Node)

@given(instance=MMTree::TreeElement_strategy)
@settings(max_examples=50)
def test_mmtree::treeelement_instantiation(instance):
    assert isinstance(instance, MMTree::TreeElement)

@given(instance=MMTree::TreeElement_strategy)
def test_mmtree::treeelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=MMTree::TreeElement_strategy)
def test_mmtree::treeelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
