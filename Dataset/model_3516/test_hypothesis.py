import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    declarationorder_S,
    S,
    declarationorder_Child,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_declarationorder_s_is_not_abstract():
    assert not inspect.isabstract(declarationorder_S)


def test_declarationorder_s_constructor_exists():
    assert callable(declarationorder_S.__init__)


def test_declarationorder_s_constructor_args():
    sig = inspect.signature(declarationorder_S.__init__)
    params = list(sig.parameters.keys())



def test_s_is_not_abstract():
    assert not inspect.isabstract(S)


def test_s_constructor_exists():
    assert callable(S.__init__)


def test_s_constructor_args():
    sig = inspect.signature(S.__init__)
    params = list(sig.parameters.keys())



def test_declarationorder_child_is_not_abstract():
    assert not inspect.isabstract(declarationorder_Child)


def test_declarationorder_child_constructor_exists():
    assert callable(declarationorder_Child.__init__)


def test_declarationorder_child_constructor_args():
    sig = inspect.signature(declarationorder_Child.__init__)
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
declarationorder_S_strategy = st.builds(
    declarationorder_S,
)
S_strategy = st.builds(
    S,
)
declarationorder_Child_strategy = st.builds(
    declarationorder_Child,
)

@given(instance=declarationorder_S_strategy)
@settings(max_examples=50)
def test_declarationorder_s_instantiation(instance):
    assert isinstance(instance, declarationorder_S)

@given(instance=S_strategy)
@settings(max_examples=50)
def test_s_instantiation(instance):
    assert isinstance(instance, S)

@given(instance=declarationorder_Child_strategy)
@settings(max_examples=50)
def test_declarationorder_child_instantiation(instance):
    assert isinstance(instance, declarationorder_Child)
