import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    tree::BigTree,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tree::bigtree_is_not_abstract():
    assert not inspect.isabstract(tree::BigTree)


def test_tree::bigtree_constructor_exists():
    assert callable(tree::BigTree.__init__)


def test_tree::bigtree_constructor_args():
    sig = inspect.signature(tree::BigTree.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tree::bigtree_has_name():
    assert hasattr(tree::BigTree, "name")
    descriptor = None
    for klass in tree::BigTree.__mro__:
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
tree::BigTree_strategy = st.builds(
    tree::BigTree,
    name=
        safe_text
)

@given(instance=tree::BigTree_strategy)
@settings(max_examples=50)
def test_tree::bigtree_instantiation(instance):
    assert isinstance(instance, tree::BigTree)

@given(instance=tree::BigTree_strategy)
def test_tree::bigtree_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tree::BigTree_strategy)
def test_tree::bigtree_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
