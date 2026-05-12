import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Node,
    kiamaas_Leaf,
    kiamaas_Composite,
    kiamaas_Node,
    kiamaas_Top,
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



def test_kiamaas_leaf_is_not_abstract():
    assert not inspect.isabstract(kiamaas_Leaf)


def test_kiamaas_leaf_constructor_exists():
    assert callable(kiamaas_Leaf.__init__)


def test_kiamaas_leaf_constructor_args():
    sig = inspect.signature(kiamaas_Leaf.__init__)
    params = list(sig.parameters.keys())



def test_kiamaas_composite_is_not_abstract():
    assert not inspect.isabstract(kiamaas_Composite)


def test_kiamaas_composite_constructor_exists():
    assert callable(kiamaas_Composite.__init__)


def test_kiamaas_composite_constructor_args():
    sig = inspect.signature(kiamaas_Composite.__init__)
    params = list(sig.parameters.keys())



def test_kiamaas_node_is_not_abstract():
    assert not inspect.isabstract(kiamaas_Node)


def test_kiamaas_node_constructor_exists():
    assert callable(kiamaas_Node.__init__)


def test_kiamaas_node_constructor_args():
    sig = inspect.signature(kiamaas_Node.__init__)
    params = list(sig.parameters.keys())
    assert "depth" in params, "Missing parameter 'depth'"
    assert "height" in params, "Missing parameter 'height'"

def test_kiamaas_node_has_depth():
    assert hasattr(kiamaas_Node, "depth")
    descriptor = None
    for klass in kiamaas_Node.__mro__:
        if "depth" in klass.__dict__:
            descriptor = klass.__dict__["depth"]
            break
    assert isinstance(descriptor, property)

def test_kiamaas_node_has_height():
    assert hasattr(kiamaas_Node, "height")
    descriptor = None
    for klass in kiamaas_Node.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_kiamaas_top_is_not_abstract():
    assert not inspect.isabstract(kiamaas_Top)


def test_kiamaas_top_constructor_exists():
    assert callable(kiamaas_Top.__init__)


def test_kiamaas_top_constructor_args():
    sig = inspect.signature(kiamaas_Top.__init__)
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
kiamaas_Leaf_strategy = st.builds(
    kiamaas_Leaf,
)
kiamaas_Composite_strategy = st.builds(
    kiamaas_Composite,
)
kiamaas_Node_strategy = st.builds(
    kiamaas_Node,
    depth=
        safe_text,
    height=
        safe_text
)
kiamaas_Top_strategy = st.builds(
    kiamaas_Top,
)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=kiamaas_Leaf_strategy)
@settings(max_examples=50)
def test_kiamaas_leaf_instantiation(instance):
    assert isinstance(instance, kiamaas_Leaf)

@given(instance=kiamaas_Composite_strategy)
@settings(max_examples=50)
def test_kiamaas_composite_instantiation(instance):
    assert isinstance(instance, kiamaas_Composite)

@given(instance=kiamaas_Node_strategy)
@settings(max_examples=50)
def test_kiamaas_node_instantiation(instance):
    assert isinstance(instance, kiamaas_Node)



@given(instance=kiamaas_Node_strategy)
def test_kiamaas_node_depth_setter(instance):
    original = instance.depth
    instance.depth = original
    assert instance.depth == original



@given(instance=kiamaas_Node_strategy)
def test_kiamaas_node_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=kiamaas_Top_strategy)
@settings(max_examples=50)
def test_kiamaas_top_instantiation(instance):
    assert isinstance(instance, kiamaas_Top)
