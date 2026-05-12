import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    root_nested_NestedTest,
    NestedTest,
    root_RootTest,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_root_nested_nestedtest_is_not_abstract():
    assert not inspect.isabstract(root_nested_NestedTest)


def test_root_nested_nestedtest_constructor_exists():
    assert callable(root_nested_NestedTest.__init__)


def test_root_nested_nestedtest_constructor_args():
    sig = inspect.signature(root_nested_NestedTest.__init__)
    params = list(sig.parameters.keys())



def test_nestedtest_is_not_abstract():
    assert not inspect.isabstract(NestedTest)


def test_nestedtest_constructor_exists():
    assert callable(NestedTest.__init__)


def test_nestedtest_constructor_args():
    sig = inspect.signature(NestedTest.__init__)
    params = list(sig.parameters.keys())



def test_root_roottest_is_not_abstract():
    assert not inspect.isabstract(root_RootTest)


def test_root_roottest_constructor_exists():
    assert callable(root_RootTest.__init__)


def test_root_roottest_constructor_args():
    sig = inspect.signature(root_RootTest.__init__)
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
root_nested_NestedTest_strategy = st.builds(
    root_nested_NestedTest,
)
NestedTest_strategy = st.builds(
    NestedTest,
)
root_RootTest_strategy = st.builds(
    root_RootTest,
)

@given(instance=root_nested_NestedTest_strategy)
@settings(max_examples=50)
def test_root_nested_nestedtest_instantiation(instance):
    assert isinstance(instance, root_nested_NestedTest)

@given(instance=NestedTest_strategy)
@settings(max_examples=50)
def test_nestedtest_instantiation(instance):
    assert isinstance(instance, NestedTest)

@given(instance=root_RootTest_strategy)
@settings(max_examples=50)
def test_root_roottest_instantiation(instance):
    assert isinstance(instance, root_RootTest)
