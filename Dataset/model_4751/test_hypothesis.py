import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    TreeElement,
    edd::Leaf,
    edd::Node,
    edd::TreeElement,
    edd::EDD,
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



def test_edd::leaf_is_not_abstract():
    assert not inspect.isabstract(edd::Leaf)


def test_edd::leaf_constructor_exists():
    assert callable(edd::Leaf.__init__)


def test_edd::leaf_constructor_args():
    sig = inspect.signature(edd::Leaf.__init__)
    params = list(sig.parameters.keys())



def test_edd::node_is_not_abstract():
    assert not inspect.isabstract(edd::Node)


def test_edd::node_constructor_exists():
    assert callable(edd::Node.__init__)


def test_edd::node_constructor_args():
    sig = inspect.signature(edd::Node.__init__)
    params = list(sig.parameters.keys())



def test_edd::treeelement_is_not_abstract():
    assert not inspect.isabstract(edd::TreeElement)


def test_edd::treeelement_constructor_exists():
    assert callable(edd::TreeElement.__init__)


def test_edd::treeelement_constructor_args():
    sig = inspect.signature(edd::TreeElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "index" in params, "Missing parameter 'index'"

def test_edd::treeelement_has_name():
    assert hasattr(edd::TreeElement, "name")
    descriptor = None
    for klass in edd::TreeElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_edd::treeelement_has_index():
    assert hasattr(edd::TreeElement, "index")
    descriptor = None
    for klass in edd::TreeElement.__mro__:
        if "index" in klass.__dict__:
            descriptor = klass.__dict__["index"]
            break
    assert isinstance(descriptor, property)



def test_edd::edd_is_not_abstract():
    assert not inspect.isabstract(edd::EDD)


def test_edd::edd_constructor_exists():
    assert callable(edd::EDD.__init__)


def test_edd::edd_constructor_args():
    sig = inspect.signature(edd::EDD.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_edd::edd_has_name():
    assert hasattr(edd::EDD, "name")
    descriptor = None
    for klass in edd::EDD.__mro__:
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
edd::Leaf_strategy = st.builds(
    edd::Leaf,
)
edd::Node_strategy = st.builds(
    edd::Node,
)
edd::TreeElement_strategy = st.builds(
    edd::TreeElement,
    name=
        safe_text,
    index=
        safe_text
)
edd::EDD_strategy = st.builds(
    edd::EDD,
    name=
        safe_text
)

@given(instance=TreeElement_strategy)
@settings(max_examples=50)
def test_treeelement_instantiation(instance):
    assert isinstance(instance, TreeElement)

@given(instance=edd::Leaf_strategy)
@settings(max_examples=50)
def test_edd::leaf_instantiation(instance):
    assert isinstance(instance, edd::Leaf)

@given(instance=edd::Node_strategy)
@settings(max_examples=50)
def test_edd::node_instantiation(instance):
    assert isinstance(instance, edd::Node)

@given(instance=edd::TreeElement_strategy)
@settings(max_examples=50)
def test_edd::treeelement_instantiation(instance):
    assert isinstance(instance, edd::TreeElement)

@given(instance=edd::TreeElement_strategy)
def test_edd::treeelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=edd::TreeElement_strategy)
def test_edd::treeelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=edd::TreeElement_strategy)
def test_edd::treeelement_index_type(instance):
    assert isinstance(instance.index, str)


@given(instance=edd::TreeElement_strategy)
def test_edd::treeelement_index_setter(instance):
    original = instance.index
    instance.index = original
    assert instance.index == original

@given(instance=edd::EDD_strategy)
@settings(max_examples=50)
def test_edd::edd_instantiation(instance):
    assert isinstance(instance, edd::EDD)

@given(instance=edd::EDD_strategy)
def test_edd::edd_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=edd::EDD_strategy)
def test_edd::edd_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
