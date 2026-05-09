import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    TreeCS,
    kwcs::LeafCS,
    kwcs::BinCS,
    kwcs::TreeCS,
    kwcs::TopCS,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_treecs_is_not_abstract():
    assert not inspect.isabstract(TreeCS)


def test_treecs_constructor_exists():
    assert callable(TreeCS.__init__)


def test_treecs_constructor_args():
    sig = inspect.signature(TreeCS.__init__)
    params = list(sig.parameters.keys())



def test_kwcs::leafcs_is_not_abstract():
    assert not inspect.isabstract(kwcs::LeafCS)


def test_kwcs::leafcs_constructor_exists():
    assert callable(kwcs::LeafCS.__init__)


def test_kwcs::leafcs_constructor_args():
    sig = inspect.signature(kwcs::LeafCS.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_kwcs::leafcs_has_val():
    assert hasattr(kwcs::LeafCS, "val")
    descriptor = None
    for klass in kwcs::LeafCS.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_kwcs::bincs_is_not_abstract():
    assert not inspect.isabstract(kwcs::BinCS)


def test_kwcs::bincs_constructor_exists():
    assert callable(kwcs::BinCS.__init__)


def test_kwcs::bincs_constructor_args():
    sig = inspect.signature(kwcs::BinCS.__init__)
    params = list(sig.parameters.keys())



def test_kwcs::treecs_is_not_abstract():
    assert not inspect.isabstract(kwcs::TreeCS)


def test_kwcs::treecs_constructor_exists():
    assert callable(kwcs::TreeCS.__init__)


def test_kwcs::treecs_constructor_args():
    sig = inspect.signature(kwcs::TreeCS.__init__)
    params = list(sig.parameters.keys())



def test_kwcs::topcs_is_not_abstract():
    assert not inspect.isabstract(kwcs::TopCS)


def test_kwcs::topcs_constructor_exists():
    assert callable(kwcs::TopCS.__init__)


def test_kwcs::topcs_constructor_args():
    sig = inspect.signature(kwcs::TopCS.__init__)
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
TreeCS_strategy = st.builds(
    TreeCS,
)
kwcs::LeafCS_strategy = st.builds(
    kwcs::LeafCS,
    val=
        st.integers()
)
kwcs::BinCS_strategy = st.builds(
    kwcs::BinCS,
)
kwcs::TreeCS_strategy = st.builds(
    kwcs::TreeCS,
)
kwcs::TopCS_strategy = st.builds(
    kwcs::TopCS,
)

@given(instance=TreeCS_strategy)
@settings(max_examples=50)
def test_treecs_instantiation(instance):
    assert isinstance(instance, TreeCS)

@given(instance=kwcs::LeafCS_strategy)
@settings(max_examples=50)
def test_kwcs::leafcs_instantiation(instance):
    assert isinstance(instance, kwcs::LeafCS)

@given(instance=kwcs::LeafCS_strategy)
def test_kwcs::leafcs_val_type(instance):
    assert isinstance(instance.val, int)


@given(instance=kwcs::LeafCS_strategy)
def test_kwcs::leafcs_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=kwcs::BinCS_strategy)
@settings(max_examples=50)
def test_kwcs::bincs_instantiation(instance):
    assert isinstance(instance, kwcs::BinCS)

@given(instance=kwcs::TreeCS_strategy)
@settings(max_examples=50)
def test_kwcs::treecs_instantiation(instance):
    assert isinstance(instance, kwcs::TreeCS)

@given(instance=kwcs::TopCS_strategy)
@settings(max_examples=50)
def test_kwcs::topcs_instantiation(instance):
    assert isinstance(instance, kwcs::TopCS)
