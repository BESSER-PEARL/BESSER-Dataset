import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Tree::Node,
    Tree::Storage,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tree::node_is_not_abstract():
    assert not inspect.isabstract(Tree::Node)


def test_tree::node_constructor_exists():
    assert callable(Tree::Node.__init__)


def test_tree::node_constructor_args():
    sig = inspect.signature(Tree::Node.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_tree::node_has_value():
    assert hasattr(Tree::Node, "value")
    descriptor = None
    for klass in Tree::Node.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_tree::storage_is_not_abstract():
    assert not inspect.isabstract(Tree::Storage)


def test_tree::storage_constructor_exists():
    assert callable(Tree::Storage.__init__)


def test_tree::storage_constructor_args():
    sig = inspect.signature(Tree::Storage.__init__)
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
Tree::Node_strategy = st.builds(
    Tree::Node,
    value=
        st.integers()
)
Tree::Storage_strategy = st.builds(
    Tree::Storage,
)

@given(instance=Tree::Node_strategy)
@settings(max_examples=50)
def test_tree::node_instantiation(instance):
    assert isinstance(instance, Tree::Node)

@given(instance=Tree::Node_strategy)
def test_tree::node_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=Tree::Node_strategy)
def test_tree::node_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Tree::Storage_strategy)
@settings(max_examples=50)
def test_tree::storage_instantiation(instance):
    assert isinstance(instance, Tree::Storage)
