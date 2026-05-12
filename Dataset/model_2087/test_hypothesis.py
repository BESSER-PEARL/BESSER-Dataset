import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    redblacktree2_Tree,
    redblacktree2_Node,
    Type,
    Color,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_redblacktree2_tree_is_not_abstract():
    assert not inspect.isabstract(redblacktree2_Tree)


def test_redblacktree2_tree_constructor_exists():
    assert callable(redblacktree2_Tree.__init__)


def test_redblacktree2_tree_constructor_args():
    sig = inspect.signature(redblacktree2_Tree.__init__)
    params = list(sig.parameters.keys())



def test_redblacktree2_node_is_not_abstract():
    assert not inspect.isabstract(redblacktree2_Node)


def test_redblacktree2_node_constructor_exists():
    assert callable(redblacktree2_Node.__init__)


def test_redblacktree2_node_constructor_args():
    sig = inspect.signature(redblacktree2_Node.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_redblacktree2_node_has_value():
    assert hasattr(redblacktree2_Node, "value")
    descriptor = None
    for klass in redblacktree2_Node.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_type_exists():
    # Check that the Enumeration exists
    assert Type is not None

def test_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Type]
    expected_literals = [
        "ROOT",
        "NODE",
        "LEAF",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Type"

def test_color_exists():
    # Check that the Enumeration exists
    assert Color is not None

def test_color_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Color]
    expected_literals = [
        "BLACK",
        "RED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Color"


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
redblacktree2_Tree_strategy = st.builds(
    redblacktree2_Tree,
)
redblacktree2_Node_strategy = st.builds(
    redblacktree2_Node,
    value=
        st.integers()
)

@given(instance=redblacktree2_Tree_strategy)
@settings(max_examples=50)
def test_redblacktree2_tree_instantiation(instance):
    assert isinstance(instance, redblacktree2_Tree)

@given(instance=redblacktree2_Node_strategy)
@settings(max_examples=50)
def test_redblacktree2_node_instantiation(instance):
    assert isinstance(instance, redblacktree2_Node)



@given(instance=redblacktree2_Node_strategy)
def test_redblacktree2_node_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original
