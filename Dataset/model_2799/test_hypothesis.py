import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Tree_Node,
    Tree_Storage,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tree_node_is_not_abstract():
    assert not inspect.isabstract(Tree_Node)


def test_tree_node_constructor_exists():
    assert callable(Tree_Node.__init__)


def test_tree_node_constructor_args():
    sig = inspect.signature(Tree_Node.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_tree_node_has_value():
    assert hasattr(Tree_Node, "value")
    descriptor = None
    for klass in Tree_Node.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_tree_storage_is_not_abstract():
    assert not inspect.isabstract(Tree_Storage)


def test_tree_storage_constructor_exists():
    assert callable(Tree_Storage.__init__)


def test_tree_storage_constructor_args():
    sig = inspect.signature(Tree_Storage.__init__)
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
Tree_Node_strategy = st.builds(
    Tree_Node,
    value=
        st.integers()
)
Tree_Storage_strategy = st.builds(
    Tree_Storage,
)

@given(instance=Tree_Node_strategy)
@settings(max_examples=50)
def test_tree_node_instantiation(instance):
    assert isinstance(instance, Tree_Node)



@given(instance=Tree_Node_strategy)
def test_tree_node_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Tree_Storage_strategy)
@settings(max_examples=50)
def test_tree_storage_instantiation(instance):
    assert isinstance(instance, Tree_Storage)
