import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Tree,
    kwas_Leaf,
    kwas_Bin,
    kwas_Tree,
    kwas_Top,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tree_is_not_abstract():
    assert not inspect.isabstract(Tree)


def test_tree_constructor_exists():
    assert callable(Tree.__init__)


def test_tree_constructor_args():
    sig = inspect.signature(Tree.__init__)
    params = list(sig.parameters.keys())



def test_kwas_leaf_is_not_abstract():
    assert not inspect.isabstract(kwas_Leaf)


def test_kwas_leaf_constructor_exists():
    assert callable(kwas_Leaf.__init__)


def test_kwas_leaf_constructor_args():
    sig = inspect.signature(kwas_Leaf.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_kwas_leaf_has_val():
    assert hasattr(kwas_Leaf, "val")
    descriptor = None
    for klass in kwas_Leaf.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_kwas_bin_is_not_abstract():
    assert not inspect.isabstract(kwas_Bin)


def test_kwas_bin_constructor_exists():
    assert callable(kwas_Bin.__init__)


def test_kwas_bin_constructor_args():
    sig = inspect.signature(kwas_Bin.__init__)
    params = list(sig.parameters.keys())



def test_kwas_tree_is_not_abstract():
    assert not inspect.isabstract(kwas_Tree)


def test_kwas_tree_constructor_exists():
    assert callable(kwas_Tree.__init__)


def test_kwas_tree_constructor_args():
    sig = inspect.signature(kwas_Tree.__init__)
    params = list(sig.parameters.keys())
    assert "labelS" in params, "Missing parameter 'labelS'"
    assert "valsS" in params, "Missing parameter 'valsS'"
    assert "valsI" in params, "Missing parameter 'valsI'"
    assert "labelI" in params, "Missing parameter 'labelI'"

def test_kwas_tree_has_labelS():
    assert hasattr(kwas_Tree, "labelS")
    descriptor = None
    for klass in kwas_Tree.__mro__:
        if "labelS" in klass.__dict__:
            descriptor = klass.__dict__["labelS"]
            break
    assert isinstance(descriptor, property)

def test_kwas_tree_has_valsS():
    assert hasattr(kwas_Tree, "valsS")
    descriptor = None
    for klass in kwas_Tree.__mro__:
        if "valsS" in klass.__dict__:
            descriptor = klass.__dict__["valsS"]
            break
    assert isinstance(descriptor, property)

def test_kwas_tree_has_valsI():
    assert hasattr(kwas_Tree, "valsI")
    descriptor = None
    for klass in kwas_Tree.__mro__:
        if "valsI" in klass.__dict__:
            descriptor = klass.__dict__["valsI"]
            break
    assert isinstance(descriptor, property)

def test_kwas_tree_has_labelI():
    assert hasattr(kwas_Tree, "labelI")
    descriptor = None
    for klass in kwas_Tree.__mro__:
        if "labelI" in klass.__dict__:
            descriptor = klass.__dict__["labelI"]
            break
    assert isinstance(descriptor, property)



def test_kwas_top_is_not_abstract():
    assert not inspect.isabstract(kwas_Top)


def test_kwas_top_constructor_exists():
    assert callable(kwas_Top.__init__)


def test_kwas_top_constructor_args():
    sig = inspect.signature(kwas_Top.__init__)
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
Tree_strategy = st.builds(
    Tree,
)
kwas_Leaf_strategy = st.builds(
    kwas_Leaf,
    val=
        st.integers()
)
kwas_Bin_strategy = st.builds(
    kwas_Bin,
)
kwas_Tree_strategy = st.builds(
    kwas_Tree,
    labelS=
        safe_text,
    valsS=
        st.integers(),
    valsI=
        st.integers(),
    labelI=
        safe_text
)
kwas_Top_strategy = st.builds(
    kwas_Top,
)

@given(instance=Tree_strategy)
@settings(max_examples=50)
def test_tree_instantiation(instance):
    assert isinstance(instance, Tree)

@given(instance=kwas_Leaf_strategy)
@settings(max_examples=50)
def test_kwas_leaf_instantiation(instance):
    assert isinstance(instance, kwas_Leaf)



@given(instance=kwas_Leaf_strategy)
def test_kwas_leaf_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=kwas_Bin_strategy)
@settings(max_examples=50)
def test_kwas_bin_instantiation(instance):
    assert isinstance(instance, kwas_Bin)

@given(instance=kwas_Tree_strategy)
@settings(max_examples=50)
def test_kwas_tree_instantiation(instance):
    assert isinstance(instance, kwas_Tree)



@given(instance=kwas_Tree_strategy)
def test_kwas_tree_labelS_setter(instance):
    original = instance.labelS
    instance.labelS = original
    assert instance.labelS == original



@given(instance=kwas_Tree_strategy)
def test_kwas_tree_valsS_setter(instance):
    original = instance.valsS
    instance.valsS = original
    assert instance.valsS == original



@given(instance=kwas_Tree_strategy)
def test_kwas_tree_valsI_setter(instance):
    original = instance.valsI
    instance.valsI = original
    assert instance.valsI == original



@given(instance=kwas_Tree_strategy)
def test_kwas_tree_labelI_setter(instance):
    original = instance.labelI
    instance.labelI = original
    assert instance.labelI == original

@given(instance=kwas_Top_strategy)
@settings(max_examples=50)
def test_kwas_top_instantiation(instance):
    assert isinstance(instance, kwas_Top)
