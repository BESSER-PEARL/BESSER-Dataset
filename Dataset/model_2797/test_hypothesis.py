import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    tree::Node,
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
    assert "name" in params, "Missing parameter 'name'"

def test_tree::node_has_name():
    assert hasattr(tree::Node, "name")
    descriptor = None
    for klass in tree::Node.__mro__:
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
    name=
        safe_text
)

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
