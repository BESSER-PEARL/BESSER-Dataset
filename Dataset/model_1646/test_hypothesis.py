import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Tree,
    kwas::Leaf,
    kwas::Bin,
    kwas::Tree,
    kwas::Top,
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



def test_kwas::leaf_is_not_abstract():
    assert not inspect.isabstract(kwas::Leaf)


def test_kwas::leaf_constructor_exists():
    assert callable(kwas::Leaf.__init__)


def test_kwas::leaf_constructor_args():
    sig = inspect.signature(kwas::Leaf.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_kwas::leaf_has_val():
    assert hasattr(kwas::Leaf, "val")
    descriptor = None
    for klass in kwas::Leaf.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_kwas::bin_is_not_abstract():
    assert not inspect.isabstract(kwas::Bin)


def test_kwas::bin_constructor_exists():
    assert callable(kwas::Bin.__init__)


def test_kwas::bin_constructor_args():
    sig = inspect.signature(kwas::Bin.__init__)
    params = list(sig.parameters.keys())



def test_kwas::tree_is_not_abstract():
    assert not inspect.isabstract(kwas::Tree)


def test_kwas::tree_constructor_exists():
    assert callable(kwas::Tree.__init__)


def test_kwas::tree_constructor_args():
    sig = inspect.signature(kwas::Tree.__init__)
    params = list(sig.parameters.keys())
    assert "valsI" in params, "Missing parameter 'valsI'"
    assert "labelI" in params, "Missing parameter 'labelI'"
    assert "labelS" in params, "Missing parameter 'labelS'"
    assert "valsS" in params, "Missing parameter 'valsS'"

def test_kwas::tree_has_valsI():
    assert hasattr(kwas::Tree, "valsI")
    descriptor = None
    for klass in kwas::Tree.__mro__:
        if "valsI" in klass.__dict__:
            descriptor = klass.__dict__["valsI"]
            break
    assert isinstance(descriptor, property)

def test_kwas::tree_has_labelI():
    assert hasattr(kwas::Tree, "labelI")
    descriptor = None
    for klass in kwas::Tree.__mro__:
        if "labelI" in klass.__dict__:
            descriptor = klass.__dict__["labelI"]
            break
    assert isinstance(descriptor, property)

def test_kwas::tree_has_labelS():
    assert hasattr(kwas::Tree, "labelS")
    descriptor = None
    for klass in kwas::Tree.__mro__:
        if "labelS" in klass.__dict__:
            descriptor = klass.__dict__["labelS"]
            break
    assert isinstance(descriptor, property)

def test_kwas::tree_has_valsS():
    assert hasattr(kwas::Tree, "valsS")
    descriptor = None
    for klass in kwas::Tree.__mro__:
        if "valsS" in klass.__dict__:
            descriptor = klass.__dict__["valsS"]
            break
    assert isinstance(descriptor, property)



def test_kwas::top_is_not_abstract():
    assert not inspect.isabstract(kwas::Top)


def test_kwas::top_constructor_exists():
    assert callable(kwas::Top.__init__)


def test_kwas::top_constructor_args():
    sig = inspect.signature(kwas::Top.__init__)
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
kwas::Leaf_strategy = st.builds(
    kwas::Leaf,
    val=
        st.integers()
)
kwas::Bin_strategy = st.builds(
    kwas::Bin,
)
kwas::Tree_strategy = st.builds(
    kwas::Tree,
    valsI=
        st.integers(),
    labelI=
        safe_text,
    labelS=
        safe_text,
    valsS=
        st.integers()
)
kwas::Top_strategy = st.builds(
    kwas::Top,
)

@given(instance=Tree_strategy)
@settings(max_examples=50)
def test_tree_instantiation(instance):
    assert isinstance(instance, Tree)

@given(instance=kwas::Leaf_strategy)
@settings(max_examples=50)
def test_kwas::leaf_instantiation(instance):
    assert isinstance(instance, kwas::Leaf)

@given(instance=kwas::Leaf_strategy)
def test_kwas::leaf_val_type(instance):
    assert isinstance(instance.val, int)


@given(instance=kwas::Leaf_strategy)
def test_kwas::leaf_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=kwas::Bin_strategy)
@settings(max_examples=50)
def test_kwas::bin_instantiation(instance):
    assert isinstance(instance, kwas::Bin)

@given(instance=kwas::Tree_strategy)
@settings(max_examples=50)
def test_kwas::tree_instantiation(instance):
    assert isinstance(instance, kwas::Tree)

@given(instance=kwas::Tree_strategy)
def test_kwas::tree_valsI_type(instance):
    assert isinstance(instance.valsI, int)


@given(instance=kwas::Tree_strategy)
def test_kwas::tree_valsI_setter(instance):
    original = instance.valsI
    instance.valsI = original
    assert instance.valsI == original

@given(instance=kwas::Tree_strategy)
def test_kwas::tree_labelI_type(instance):
    assert isinstance(instance.labelI, str)


@given(instance=kwas::Tree_strategy)
def test_kwas::tree_labelI_setter(instance):
    original = instance.labelI
    instance.labelI = original
    assert instance.labelI == original

@given(instance=kwas::Tree_strategy)
def test_kwas::tree_labelS_type(instance):
    assert isinstance(instance.labelS, str)


@given(instance=kwas::Tree_strategy)
def test_kwas::tree_labelS_setter(instance):
    original = instance.labelS
    instance.labelS = original
    assert instance.labelS == original

@given(instance=kwas::Tree_strategy)
def test_kwas::tree_valsS_type(instance):
    assert isinstance(instance.valsS, int)


@given(instance=kwas::Tree_strategy)
def test_kwas::tree_valsS_setter(instance):
    original = instance.valsS
    instance.valsS = original
    assert instance.valsS == original

@given(instance=kwas::Top_strategy)
@settings(max_examples=50)
def test_kwas::top_instantiation(instance):
    assert isinstance(instance, kwas::Top)
