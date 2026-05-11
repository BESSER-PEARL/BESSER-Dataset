import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    root::container::border::node::3,
    root::container::border::node::2,
    root::container::border::node::1,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_root::container::border::node::3_is_not_abstract():
    assert not inspect.isabstract(root::container::border::node::3)


def test_root::container::border::node::3_constructor_exists():
    assert callable(root::container::border::node::3.__init__)


def test_root::container::border::node::3_constructor_args():
    sig = inspect.signature(root::container::border::node::3.__init__)
    params = list(sig.parameters.keys())



def test_root::container::border::node::2_is_not_abstract():
    assert not inspect.isabstract(root::container::border::node::2)


def test_root::container::border::node::2_constructor_exists():
    assert callable(root::container::border::node::2.__init__)


def test_root::container::border::node::2_constructor_args():
    sig = inspect.signature(root::container::border::node::2.__init__)
    params = list(sig.parameters.keys())



def test_root::container::border::node::1_is_not_abstract():
    assert not inspect.isabstract(root::container::border::node::1)


def test_root::container::border::node::1_constructor_exists():
    assert callable(root::container::border::node::1.__init__)


def test_root::container::border::node::1_constructor_args():
    sig = inspect.signature(root::container::border::node::1.__init__)
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
root::container::border::node::3_strategy = st.builds(
    root::container::border::node::3,
)
root::container::border::node::2_strategy = st.builds(
    root::container::border::node::2,
)
root::container::border::node::1_strategy = st.builds(
    root::container::border::node::1,
)

@given(instance=root::container::border::node::3_strategy)
@settings(max_examples=50)
def test_root::container::border::node::3_instantiation(instance):
    assert isinstance(instance, root::container::border::node::3)

@given(instance=root::container::border::node::2_strategy)
@settings(max_examples=50)
def test_root::container::border::node::2_instantiation(instance):
    assert isinstance(instance, root::container::border::node::2)

@given(instance=root::container::border::node::1_strategy)
@settings(max_examples=50)
def test_root::container::border::node::1_instantiation(instance):
    assert isinstance(instance, root::container::border::node::1)
