import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    root::nested::NestedTest,
    NestedTest,
    root::RootTest,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_root::nested::nestedtest_is_not_abstract():
    assert not inspect.isabstract(root::nested::NestedTest)


def test_root::nested::nestedtest_constructor_exists():
    assert callable(root::nested::NestedTest.__init__)


def test_root::nested::nestedtest_constructor_args():
    sig = inspect.signature(root::nested::NestedTest.__init__)
    params = list(sig.parameters.keys())



def test_nestedtest_is_not_abstract():
    assert not inspect.isabstract(NestedTest)


def test_nestedtest_constructor_exists():
    assert callable(NestedTest.__init__)


def test_nestedtest_constructor_args():
    sig = inspect.signature(NestedTest.__init__)
    params = list(sig.parameters.keys())



def test_root::roottest_is_not_abstract():
    assert not inspect.isabstract(root::RootTest)


def test_root::roottest_constructor_exists():
    assert callable(root::RootTest.__init__)


def test_root::roottest_constructor_args():
    sig = inspect.signature(root::RootTest.__init__)
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
root::nested::NestedTest_strategy = st.builds(
    root::nested::NestedTest,
)
NestedTest_strategy = st.builds(
    NestedTest,
)
root::RootTest_strategy = st.builds(
    root::RootTest,
)

@given(instance=root::nested::NestedTest_strategy)
@settings(max_examples=50)
def test_root::nested::nestedtest_instantiation(instance):
    assert isinstance(instance, root::nested::NestedTest)

@given(instance=NestedTest_strategy)
@settings(max_examples=50)
def test_nestedtest_instantiation(instance):
    assert isinstance(instance, NestedTest)

@given(instance=root::RootTest_strategy)
@settings(max_examples=50)
def test_root::roottest_instantiation(instance):
    assert isinstance(instance, root::RootTest)
