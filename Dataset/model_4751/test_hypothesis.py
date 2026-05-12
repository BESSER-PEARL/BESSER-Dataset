import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    TreeElement,
    edd_Leaf,
    edd_Node,
    edd_TreeElement,
    edd_EDD,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_treeelement_is_not_abstract():
    assert not inspect.isabstract(TreeElement)


def test_treeelement_constructor_exists():
    assert callable(TreeElement.__init__)


def test_treeelement_constructor_args():
    sig = inspect.signature(TreeElement.__init__)
    params = list(sig.parameters.keys())



def test_edd_leaf_is_not_abstract():
    assert not inspect.isabstract(edd_Leaf)


def test_edd_leaf_constructor_exists():
    assert callable(edd_Leaf.__init__)


def test_edd_leaf_constructor_args():
    sig = inspect.signature(edd_Leaf.__init__)
    params = list(sig.parameters.keys())



def test_edd_node_is_not_abstract():
    assert not inspect.isabstract(edd_Node)


def test_edd_node_constructor_exists():
    assert callable(edd_Node.__init__)


def test_edd_node_constructor_args():
    sig = inspect.signature(edd_Node.__init__)
    params = list(sig.parameters.keys())



def test_edd_treeelement_is_not_abstract():
    assert not inspect.isabstract(edd_TreeElement)


def test_edd_treeelement_constructor_exists():
    assert callable(edd_TreeElement.__init__)


def test_edd_treeelement_constructor_args():
    sig = inspect.signature(edd_TreeElement.__init__)
    params = list(sig.parameters.keys())
    assert "index" in params, "Missing parameter 'index'"
    assert "name" in params, "Missing parameter 'name'"

def test_edd_treeelement_has_index():
    assert hasattr(edd_TreeElement, "index")
    descriptor = None
    for klass in edd_TreeElement.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)

def test_edd_treeelement_has_name():
    assert hasattr(edd_TreeElement, "name")
    descriptor = None
    for klass in edd_TreeElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_edd_edd_is_not_abstract():
    assert not inspect.isabstract(edd_EDD)


def test_edd_edd_constructor_exists():
    assert callable(edd_EDD.__init__)


def test_edd_edd_constructor_args():
    sig = inspect.signature(edd_EDD.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_edd_edd_has_name():
    assert hasattr(edd_EDD, "name")
    descriptor = None
    for klass in edd_EDD.__mro__:
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
TreeElement_strategy = st.builds(
    TreeElement,
)
edd_Leaf_strategy = st.builds(
    edd_Leaf,
)
edd_Node_strategy = st.builds(
    edd_Node,
)
edd_TreeElement_strategy = st.builds(
    edd_TreeElement,
    index=
        safe_text,
    name=
        safe_text
)
edd_EDD_strategy = st.builds(
    edd_EDD,
    name=
        safe_text
)

@given(instance=TreeElement_strategy)
@settings(max_examples=50)
def test_treeelement_instantiation(instance):
    assert isinstance(instance, TreeElement)

@given(instance=edd_Leaf_strategy)
@settings(max_examples=50)
def test_edd_leaf_instantiation(instance):
    assert isinstance(instance, edd_Leaf)

@given(instance=edd_Node_strategy)
@settings(max_examples=50)
def test_edd_node_instantiation(instance):
    assert isinstance(instance, edd_Node)

@given(instance=edd_TreeElement_strategy)
@settings(max_examples=50)
def test_edd_treeelement_instantiation(instance):
    assert isinstance(instance, edd_TreeElement)



@given(instance=edd_TreeElement_strategy)
def test_edd_treeelement_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original



@given(instance=edd_TreeElement_strategy)
def test_edd_treeelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=edd_EDD_strategy)
@settings(max_examples=50)
def test_edd_edd_instantiation(instance):
    assert isinstance(instance, edd_EDD)



@given(instance=edd_EDD_strategy)
def test_edd_edd_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
