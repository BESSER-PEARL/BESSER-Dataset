import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    tree_Node,
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
    assert "name" in params, "Missing parameter 'name'"

def test_tree_node_has_name():
    assert hasattr(tree_Node, "name")
    descriptor = None
    for klass in tree_Node.__mro__:
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
    name=
        safe_text
)

@given(instance=tree_Node_strategy)
@settings(max_examples=50)
def test_tree_node_instantiation(instance):
    assert isinstance(instance, tree_Node)



@given(instance=tree_Node_strategy)
def test_tree_node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
