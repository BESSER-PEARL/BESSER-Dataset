import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    tree_Node,
    tree_Tree,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tree_node_is_not_abstract():
    assert not inspect.isabstract(tree_Node)


def test_tree_node_constructor_exists():
    assert callable(tree_Node.__init__)


def test_tree_node_constructor_args():
    sig = inspect.signature(tree_Node.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "data" in params, "Missing parameter 'data'"

def test_tree_node_has_label():
    assert hasattr(tree_Node, "label")
    descriptor = None
    for klass in tree_Node.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_tree_node_has_data():
    assert hasattr(tree_Node, "data")
    descriptor = None
    for klass in tree_Node.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)



def test_tree_tree_is_not_abstract():
    assert not inspect.isabstract(tree_Tree)


def test_tree_tree_constructor_exists():
    assert callable(tree_Tree.__init__)


def test_tree_tree_constructor_args():
    sig = inspect.signature(tree_Tree.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tree_tree_has_name():
    assert hasattr(tree_Tree, "name")
    descriptor = None
    for klass in tree_Tree.__mro__:
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
tree_Node_strategy = st.builds(
    tree_Node,
    label=
        safe_text,
    data=
        safe_text
)
tree_Tree_strategy = st.builds(
    tree_Tree,
    name=
        safe_text
)

@given(instance=tree_Node_strategy)
@settings(max_examples=50)
def test_tree_node_instantiation(instance):
    assert isinstance(instance, tree_Node)



@given(instance=tree_Node_strategy)
def test_tree_node_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=tree_Node_strategy)
def test_tree_node_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original

@given(instance=tree_Tree_strategy)
@settings(max_examples=50)
def test_tree_tree_instantiation(instance):
    assert isinstance(instance, tree_Tree)



@given(instance=tree_Tree_strategy)
def test_tree_tree_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
