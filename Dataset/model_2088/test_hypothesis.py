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
    assert "anAttribute3" in params, "Missing parameter 'anAttribute3'"
    assert "anAttribute2" in params, "Missing parameter 'anAttribute2'"
    assert "name" in params, "Missing parameter 'name'"
    assert "anAttribute4" in params, "Missing parameter 'anAttribute4'"
    assert "anAttribute" in params, "Missing parameter 'anAttribute'"

def test_tree::node_has_anAttribute3():
    assert hasattr(tree::Node, "anAttribute3")
    descriptor = None
    for klass in tree::Node.__mro__:
        if "anAttribute3" in klass.__dict__:
            descriptor = klass.__dict__["anAttribute3"]
            break
    assert isinstance(descriptor, property)

def test_tree::node_has_anAttribute2():
    assert hasattr(tree::Node, "anAttribute2")
    descriptor = None
    for klass in tree::Node.__mro__:
        if "anAttribute2" in klass.__dict__:
            descriptor = klass.__dict__["anAttribute2"]
            break
    assert isinstance(descriptor, property)

def test_tree::node_has_name():
    assert hasattr(tree::Node, "name")
    descriptor = None
    for klass in tree::Node.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_tree::node_has_anAttribute4():
    assert hasattr(tree::Node, "anAttribute4")
    descriptor = None
    for klass in tree::Node.__mro__:
        if "anAttribute4" in klass.__dict__:
            descriptor = klass.__dict__["anAttribute4"]
            break
    assert isinstance(descriptor, property)

def test_tree::node_has_anAttribute():
    assert hasattr(tree::Node, "anAttribute")
    descriptor = None
    for klass in tree::Node.__mro__:
        if "anAttribute" in klass.__dict__:
            descriptor = klass.__dict__["anAttribute"]
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
    anAttribute3=
        st.integers(),
    anAttribute2=
        st.integers(),
    name=
        safe_text,
    anAttribute4=
        st.integers(),
    anAttribute=
        st.integers()
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
def test_tree::node_anAttribute3_type(instance):
    assert isinstance(instance.anAttribute3, int)


@given(instance=tree::Node_strategy)
def test_tree::node_anAttribute3_setter(instance):
    original = instance.anAttribute3
    instance.anAttribute3 = original
    assert instance.anAttribute3 == original

@given(instance=tree::Node_strategy)
def test_tree::node_anAttribute2_type(instance):
    assert isinstance(instance.anAttribute2, int)


@given(instance=tree::Node_strategy)
def test_tree::node_anAttribute2_setter(instance):
    original = instance.anAttribute2
    instance.anAttribute2 = original
    assert instance.anAttribute2 == original

@given(instance=tree::Node_strategy)
def test_tree::node_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tree::Node_strategy)
def test_tree::node_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tree::Node_strategy)
def test_tree::node_anAttribute4_type(instance):
    assert isinstance(instance.anAttribute4, int)


@given(instance=tree::Node_strategy)
def test_tree::node_anAttribute4_setter(instance):
    original = instance.anAttribute4
    instance.anAttribute4 = original
    assert instance.anAttribute4 == original

@given(instance=tree::Node_strategy)
def test_tree::node_anAttribute_type(instance):
    assert isinstance(instance.anAttribute, int)


@given(instance=tree::Node_strategy)
def test_tree::node_anAttribute_setter(instance):
    original = instance.anAttribute
    instance.anAttribute = original
    assert instance.anAttribute == original

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
