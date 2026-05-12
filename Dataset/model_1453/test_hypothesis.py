import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    tree_Edge,
    tree_Node,
    tree_Diagram,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tree_edge_is_not_abstract():
    assert not inspect.isabstract(tree_Edge)


def test_tree_edge_constructor_exists():
    assert callable(tree_Edge.__init__)


def test_tree_edge_constructor_args():
    sig = inspect.signature(tree_Edge.__init__)
    params = list(sig.parameters.keys())



def test_tree_node_is_not_abstract():
    assert not inspect.isabstract(tree_Node)


def test_tree_node_constructor_exists():
    assert callable(tree_Node.__init__)


def test_tree_node_constructor_args():
    sig = inspect.signature(tree_Node.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tree_node_has_name():
    assert hasattr(tree_Node, "name")
    descriptor = None
    for klass in tree_Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tree_diagram_is_not_abstract():
    assert not inspect.isabstract(tree_Diagram)


def test_tree_diagram_constructor_exists():
    assert callable(tree_Diagram.__init__)


def test_tree_diagram_constructor_args():
    sig = inspect.signature(tree_Diagram.__init__)
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
tree_Edge_strategy = st.builds(
    tree_Edge,
)
tree_Node_strategy = st.builds(
    tree_Node,
    name=
        safe_text
)
tree_Diagram_strategy = st.builds(
    tree_Diagram,
)

@given(instance=tree_Edge_strategy)
@settings(max_examples=50)
def test_tree_edge_instantiation(instance):
    assert isinstance(instance, tree_Edge)

@given(instance=tree_Node_strategy)
@settings(max_examples=50)
def test_tree_node_instantiation(instance):
    assert isinstance(instance, tree_Node)



@given(instance=tree_Node_strategy)
def test_tree_node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tree_Diagram_strategy)
@settings(max_examples=50)
def test_tree_diagram_instantiation(instance):
    assert isinstance(instance, tree_Diagram)
