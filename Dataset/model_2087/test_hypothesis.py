import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    redblacktree2::Tree,
    redblacktree2::Node,
    Color,
    Type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_redblacktree2::tree_is_not_abstract():
    assert not inspect.isabstract(redblacktree2::Tree)


def test_redblacktree2::tree_constructor_exists():
    assert callable(redblacktree2::Tree.__init__)


def test_redblacktree2::tree_constructor_args():
    sig = inspect.signature(redblacktree2::Tree.__init__)
    params = list(sig.parameters.keys())



def test_redblacktree2::node_is_not_abstract():
    assert not inspect.isabstract(redblacktree2::Node)


def test_redblacktree2::node_constructor_exists():
    assert callable(redblacktree2::Node.__init__)


def test_redblacktree2::node_constructor_args():
    sig = inspect.signature(redblacktree2::Node.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_redblacktree2::node_has_value():
    assert hasattr(redblacktree2::Node, "value")
    descriptor = None
    for klass in redblacktree2::Node.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

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

def test_type_exists():
    # Check that the Enumeration exists
    assert Type is not None

def test_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Type]
    expected_literals = [
        "NODE",
        "ROOT",
        "LEAF",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Type"


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
redblacktree2::Tree_strategy = st.builds(
    redblacktree2::Tree,
)
redblacktree2::Node_strategy = st.builds(
    redblacktree2::Node,
    value=
        st.integers()
)

@given(instance=redblacktree2::Tree_strategy)
@settings(max_examples=50)
def test_redblacktree2::tree_instantiation(instance):
    assert isinstance(instance, redblacktree2::Tree)

@given(instance=redblacktree2::Node_strategy)
@settings(max_examples=50)
def test_redblacktree2::node_instantiation(instance):
    assert isinstance(instance, redblacktree2::Node)

@given(instance=redblacktree2::Node_strategy)
def test_redblacktree2::node_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=redblacktree2::Node_strategy)
def test_redblacktree2::node_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original
