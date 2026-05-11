import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    AbcToNothing::C,
    AbcToNothing::classB,
    AbcToNothing::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abctonothing::c_is_not_abstract():
    assert not inspect.isabstract(AbcToNothing::C)


def test_abctonothing::c_constructor_exists():
    assert callable(AbcToNothing::C.__init__)


def test_abctonothing::c_constructor_args():
    sig = inspect.signature(AbcToNothing::C.__init__)
    params = list(sig.parameters.keys())



def test_abctonothing::classb_is_not_abstract():
    assert not inspect.isabstract(AbcToNothing::classB)


def test_abctonothing::classb_constructor_exists():
    assert callable(AbcToNothing::classB.__init__)


def test_abctonothing::classb_constructor_args():
    sig = inspect.signature(AbcToNothing::classB.__init__)
    params = list(sig.parameters.keys())



def test_abctonothing::a_is_not_abstract():
    assert not inspect.isabstract(AbcToNothing::A)


def test_abctonothing::a_constructor_exists():
    assert callable(AbcToNothing::A.__init__)


def test_abctonothing::a_constructor_args():
    sig = inspect.signature(AbcToNothing::A.__init__)
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
AbcToNothing::C_strategy = st.builds(
    AbcToNothing::C,
)
AbcToNothing::classB_strategy = st.builds(
    AbcToNothing::classB,
)
AbcToNothing::A_strategy = st.builds(
    AbcToNothing::A,
)

@given(instance=AbcToNothing::C_strategy)
@settings(max_examples=50)
def test_abctonothing::c_instantiation(instance):
    assert isinstance(instance, AbcToNothing::C)

@given(instance=AbcToNothing::classB_strategy)
@settings(max_examples=50)
def test_abctonothing::classb_instantiation(instance):
    assert isinstance(instance, AbcToNothing::classB)

@given(instance=AbcToNothing::A_strategy)
@settings(max_examples=50)
def test_abctonothing::a_instantiation(instance):
    assert isinstance(instance, AbcToNothing::A)
