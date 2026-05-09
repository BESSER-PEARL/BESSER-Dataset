import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Node,
    kiamaas::Leaf,
    kiamaas::Composite,
    kiamaas::Node,
    kiamaas::Top,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_kiamaas::leaf_is_not_abstract():
    assert not inspect.isabstract(kiamaas::Leaf)


def test_kiamaas::leaf_constructor_exists():
    assert callable(kiamaas::Leaf.__init__)


def test_kiamaas::leaf_constructor_args():
    sig = inspect.signature(kiamaas::Leaf.__init__)
    params = list(sig.parameters.keys())



def test_kiamaas::composite_is_not_abstract():
    assert not inspect.isabstract(kiamaas::Composite)


def test_kiamaas::composite_constructor_exists():
    assert callable(kiamaas::Composite.__init__)


def test_kiamaas::composite_constructor_args():
    sig = inspect.signature(kiamaas::Composite.__init__)
    params = list(sig.parameters.keys())



def test_kiamaas::node_is_not_abstract():
    assert not inspect.isabstract(kiamaas::Node)


def test_kiamaas::node_constructor_exists():
    assert callable(kiamaas::Node.__init__)


def test_kiamaas::node_constructor_args():
    sig = inspect.signature(kiamaas::Node.__init__)
    params = list(sig.parameters.keys())
    assert "depth" in params, "Missing parameter 'depth'"
    assert "height" in params, "Missing parameter 'height'"

def test_kiamaas::node_has_depth():
    assert hasattr(kiamaas::Node, "depth")
    descriptor = None
    for klass in kiamaas::Node.__mro__:
        if "depth" in klass.__dict__:
            descriptor = klass.__dict__["depth"]
            break
    assert isinstance(descriptor, property)

def test_kiamaas::node_has_height():
    assert hasattr(kiamaas::Node, "height")
    descriptor = None
    for klass in kiamaas::Node.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_kiamaas::top_is_not_abstract():
    assert not inspect.isabstract(kiamaas::Top)


def test_kiamaas::top_constructor_exists():
    assert callable(kiamaas::Top.__init__)


def test_kiamaas::top_constructor_args():
    sig = inspect.signature(kiamaas::Top.__init__)
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
Node_strategy = st.builds(
    Node,
)
kiamaas::Leaf_strategy = st.builds(
    kiamaas::Leaf,
)
kiamaas::Composite_strategy = st.builds(
    kiamaas::Composite,
)
kiamaas::Node_strategy = st.builds(
    kiamaas::Node,
    depth=
        safe_text,
    height=
        safe_text
)
kiamaas::Top_strategy = st.builds(
    kiamaas::Top,
)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=kiamaas::Leaf_strategy)
@settings(max_examples=50)
def test_kiamaas::leaf_instantiation(instance):
    assert isinstance(instance, kiamaas::Leaf)

@given(instance=kiamaas::Composite_strategy)
@settings(max_examples=50)
def test_kiamaas::composite_instantiation(instance):
    assert isinstance(instance, kiamaas::Composite)

@given(instance=kiamaas::Node_strategy)
@settings(max_examples=50)
def test_kiamaas::node_instantiation(instance):
    assert isinstance(instance, kiamaas::Node)

@given(instance=kiamaas::Node_strategy)
def test_kiamaas::node_depth_type(instance):
    assert isinstance(instance.depth, str)


@given(instance=kiamaas::Node_strategy)
def test_kiamaas::node_depth_setter(instance):
    original = instance.depth
    instance.depth = original
    assert instance.depth == original

@given(instance=kiamaas::Node_strategy)
def test_kiamaas::node_height_type(instance):
    assert isinstance(instance.height, str)


@given(instance=kiamaas::Node_strategy)
def test_kiamaas::node_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=kiamaas::Top_strategy)
@settings(max_examples=50)
def test_kiamaas::top_instantiation(instance):
    assert isinstance(instance, kiamaas::Top)
