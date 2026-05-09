import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    tree::Edge,
    tree::Node,
    tree::Diagram,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tree::edge_is_not_abstract():
    assert not inspect.isabstract(tree::Edge)


def test_tree::edge_constructor_exists():
    assert callable(tree::Edge.__init__)


def test_tree::edge_constructor_args():
    sig = inspect.signature(tree::Edge.__init__)
    params = list(sig.parameters.keys())



def test_tree::node_is_not_abstract():
    assert not inspect.isabstract(tree::Node)


def test_tree::node_constructor_exists():
    assert callable(tree::Node.__init__)


def test_tree::node_constructor_args():
    sig = inspect.signature(tree::Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tree::node_has_name():
    assert hasattr(tree::Node, "name")
    descriptor = None
    for klass in tree::Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tree::diagram_is_not_abstract():
    assert not inspect.isabstract(tree::Diagram)


def test_tree::diagram_constructor_exists():
    assert callable(tree::Diagram.__init__)


def test_tree::diagram_constructor_args():
    sig = inspect.signature(tree::Diagram.__init__)
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
tree::Edge_strategy = st.builds(
    tree::Edge,
)
tree::Node_strategy = st.builds(
    tree::Node,
    name=
        safe_text
)
tree::Diagram_strategy = st.builds(
    tree::Diagram,
)

@given(instance=tree::Edge_strategy)
@settings(max_examples=50)
def test_tree::edge_instantiation(instance):
    assert isinstance(instance, tree::Edge)

@given(instance=tree::Node_strategy)
@settings(max_examples=50)
def test_tree::node_instantiation(instance):
    assert isinstance(instance, tree::Node)

@given(instance=tree::Node_strategy)
def test_tree::node_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tree::Node_strategy)
def test_tree::node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tree::Diagram_strategy)
@settings(max_examples=50)
def test_tree::diagram_instantiation(instance):
    assert isinstance(instance, tree::Diagram)
