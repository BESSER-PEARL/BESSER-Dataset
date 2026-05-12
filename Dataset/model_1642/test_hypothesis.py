import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    kwcs_TopCS,
    TreeCS,
    kwcs_LeafCS,
    kwcs_BinCS,
    kwcs_TreeCS,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_kwcs_topcs_is_not_abstract():
    assert not inspect.isabstract(kwcs_TopCS)


def test_kwcs_topcs_constructor_exists():
    assert callable(kwcs_TopCS.__init__)


def test_kwcs_topcs_constructor_args():
    sig = inspect.signature(kwcs_TopCS.__init__)
    params = list(sig.parameters.keys())



def test_treecs_is_not_abstract():
    assert not inspect.isabstract(TreeCS)


def test_treecs_constructor_exists():
    assert callable(TreeCS.__init__)


def test_treecs_constructor_args():
    sig = inspect.signature(TreeCS.__init__)
    params = list(sig.parameters.keys())



def test_kwcs_leafcs_is_not_abstract():
    assert not inspect.isabstract(kwcs_LeafCS)


def test_kwcs_leafcs_constructor_exists():
    assert callable(kwcs_LeafCS.__init__)


def test_kwcs_leafcs_constructor_args():
    sig = inspect.signature(kwcs_LeafCS.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_kwcs_leafcs_has_val():
    assert hasattr(kwcs_LeafCS, "val")
    descriptor = None
    for klass in kwcs_LeafCS.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_kwcs_bincs_is_not_abstract():
    assert not inspect.isabstract(kwcs_BinCS)


def test_kwcs_bincs_constructor_exists():
    assert callable(kwcs_BinCS.__init__)


def test_kwcs_bincs_constructor_args():
    sig = inspect.signature(kwcs_BinCS.__init__)
    params = list(sig.parameters.keys())



def test_kwcs_treecs_is_not_abstract():
    assert not inspect.isabstract(kwcs_TreeCS)


def test_kwcs_treecs_constructor_exists():
    assert callable(kwcs_TreeCS.__init__)


def test_kwcs_treecs_constructor_args():
    sig = inspect.signature(kwcs_TreeCS.__init__)
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
kwcs_TopCS_strategy = st.builds(
    kwcs_TopCS,
)
TreeCS_strategy = st.builds(
    TreeCS,
)
kwcs_LeafCS_strategy = st.builds(
    kwcs_LeafCS,
    val=
        st.integers()
)
kwcs_BinCS_strategy = st.builds(
    kwcs_BinCS,
)
kwcs_TreeCS_strategy = st.builds(
    kwcs_TreeCS,
)

@given(instance=kwcs_TopCS_strategy)
@settings(max_examples=50)
def test_kwcs_topcs_instantiation(instance):
    assert isinstance(instance, kwcs_TopCS)

@given(instance=TreeCS_strategy)
@settings(max_examples=50)
def test_treecs_instantiation(instance):
    assert isinstance(instance, TreeCS)

@given(instance=kwcs_LeafCS_strategy)
@settings(max_examples=50)
def test_kwcs_leafcs_instantiation(instance):
    assert isinstance(instance, kwcs_LeafCS)



@given(instance=kwcs_LeafCS_strategy)
def test_kwcs_leafcs_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=kwcs_BinCS_strategy)
@settings(max_examples=50)
def test_kwcs_bincs_instantiation(instance):
    assert isinstance(instance, kwcs_BinCS)

@given(instance=kwcs_TreeCS_strategy)
@settings(max_examples=50)
def test_kwcs_treecs_instantiation(instance):
    assert isinstance(instance, kwcs_TreeCS)
