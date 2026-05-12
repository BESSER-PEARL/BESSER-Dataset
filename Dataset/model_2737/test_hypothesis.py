import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    AbcToNothing_C,
    AbcToNothing_classB,
    AbcToNothing_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abctonothing_c_is_not_abstract():
    assert not inspect.isabstract(AbcToNothing_C)


def test_abctonothing_c_constructor_exists():
    assert callable(AbcToNothing_C.__init__)


def test_abctonothing_c_constructor_args():
    sig = inspect.signature(AbcToNothing_C.__init__)
    params = list(sig.parameters.keys())



def test_abctonothing_classb_is_not_abstract():
    assert not inspect.isabstract(AbcToNothing_classB)


def test_abctonothing_classb_constructor_exists():
    assert callable(AbcToNothing_classB.__init__)


def test_abctonothing_classb_constructor_args():
    sig = inspect.signature(AbcToNothing_classB.__init__)
    params = list(sig.parameters.keys())



def test_abctonothing_a_is_not_abstract():
    assert not inspect.isabstract(AbcToNothing_A)


def test_abctonothing_a_constructor_exists():
    assert callable(AbcToNothing_A.__init__)


def test_abctonothing_a_constructor_args():
    sig = inspect.signature(AbcToNothing_A.__init__)
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
AbcToNothing_C_strategy = st.builds(
    AbcToNothing_C,
)
AbcToNothing_classB_strategy = st.builds(
    AbcToNothing_classB,
)
AbcToNothing_A_strategy = st.builds(
    AbcToNothing_A,
)

@given(instance=AbcToNothing_C_strategy)
@settings(max_examples=50)
def test_abctonothing_c_instantiation(instance):
    assert isinstance(instance, AbcToNothing_C)

@given(instance=AbcToNothing_classB_strategy)
@settings(max_examples=50)
def test_abctonothing_classb_instantiation(instance):
    assert isinstance(instance, AbcToNothing_classB)

@given(instance=AbcToNothing_A_strategy)
@settings(max_examples=50)
def test_abctonothing_a_instantiation(instance):
    assert isinstance(instance, AbcToNothing_A)
