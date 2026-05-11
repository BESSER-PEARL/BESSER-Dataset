import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    declarationorder::S,
    S,
    declarationorder::Child,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_declarationorder::s_is_not_abstract():
    assert not inspect.isabstract(declarationorder::S)


def test_declarationorder::s_constructor_exists():
    assert callable(declarationorder::S.__init__)


def test_declarationorder::s_constructor_args():
    sig = inspect.signature(declarationorder::S.__init__)
    params = list(sig.parameters.keys())



def test_s_is_not_abstract():
    assert not inspect.isabstract(S)


def test_s_constructor_exists():
    assert callable(S.__init__)


def test_s_constructor_args():
    sig = inspect.signature(S.__init__)
    params = list(sig.parameters.keys())



def test_declarationorder::child_is_not_abstract():
    assert not inspect.isabstract(declarationorder::Child)


def test_declarationorder::child_constructor_exists():
    assert callable(declarationorder::Child.__init__)


def test_declarationorder::child_constructor_args():
    sig = inspect.signature(declarationorder::Child.__init__)
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
declarationorder::S_strategy = st.builds(
    declarationorder::S,
)
S_strategy = st.builds(
    S,
)
declarationorder::Child_strategy = st.builds(
    declarationorder::Child,
)

@given(instance=declarationorder::S_strategy)
@settings(max_examples=50)
def test_declarationorder::s_instantiation(instance):
    assert isinstance(instance, declarationorder::S)

@given(instance=S_strategy)
@settings(max_examples=50)
def test_s_instantiation(instance):
    assert isinstance(instance, S)

@given(instance=declarationorder::Child_strategy)
@settings(max_examples=50)
def test_declarationorder::child_instantiation(instance):
    assert isinstance(instance, declarationorder::Child)
