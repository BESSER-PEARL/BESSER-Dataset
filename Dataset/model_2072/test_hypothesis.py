import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    tree::Node,
    tree::Tree,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tree::node_is_not_abstract():
    assert not inspect.isabstract(tree::Node)


def test_tree::node_constructor_exists():
    assert callable(tree::Node.__init__)


def test_tree::node_constructor_args():
    sig = inspect.signature(tree::Node.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "data" in params, "Missing parameter 'data'"

def test_tree::node_has_label():
    assert hasattr(tree::Node, "label")
    descriptor = None
    for klass in tree::Node.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_tree::node_has_data():
    assert hasattr(tree::Node, "data")
    descriptor = None
    for klass in tree::Node.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)



def test_tree::tree_is_not_abstract():
    assert not inspect.isabstract(tree::Tree)


def test_tree::tree_constructor_exists():
    assert callable(tree::Tree.__init__)


def test_tree::tree_constructor_args():
    sig = inspect.signature(tree::Tree.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tree::tree_has_name():
    assert hasattr(tree::Tree, "name")
    descriptor = None
    for klass in tree::Tree.__mro__:
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
tree::Node_strategy = st.builds(
    tree::Node,
    label=
        safe_text,
    data=
        safe_text
)
tree::Tree_strategy = st.builds(
    tree::Tree,
    name=
        safe_text
)

@given(instance=tree::Node_strategy)
@settings(max_examples=50)
def test_tree::node_instantiation(instance):
    assert isinstance(instance, tree::Node)

@given(instance=tree::Node_strategy)
def test_tree::node_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=tree::Node_strategy)
def test_tree::node_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=tree::Node_strategy)
def test_tree::node_data_type(instance):
    assert isinstance(instance.data, str)


@given(instance=tree::Node_strategy)
def test_tree::node_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original

@given(instance=tree::Tree_strategy)
@settings(max_examples=50)
def test_tree::tree_instantiation(instance):
    assert isinstance(instance, tree::Tree)

@given(instance=tree::Tree_strategy)
def test_tree::tree_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tree::Tree_strategy)
def test_tree::tree_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
