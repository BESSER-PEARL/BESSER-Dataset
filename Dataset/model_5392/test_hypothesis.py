import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Action,
    essai_B,
    Kind,
    essai_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_essai_b_is_not_abstract():
    assert not inspect.isabstract(essai_B)


def test_essai_b_constructor_exists():
    assert callable(essai_B.__init__)


def test_essai_b_constructor_args():
    sig = inspect.signature(essai_B.__init__)
    params = list(sig.parameters.keys())



def test_kind_is_not_abstract():
    assert not inspect.isabstract(Kind)


def test_kind_constructor_exists():
    assert callable(Kind.__init__)


def test_kind_constructor_args():
    sig = inspect.signature(Kind.__init__)
    params = list(sig.parameters.keys())



def test_essai_a_is_not_abstract():
    assert not inspect.isabstract(essai_A)


def test_essai_a_constructor_exists():
    assert callable(essai_A.__init__)


def test_essai_a_constructor_args():
    sig = inspect.signature(essai_A.__init__)
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
Action_strategy = st.builds(
    Action,
)
essai_B_strategy = st.builds(
    essai_B,
)
Kind_strategy = st.builds(
    Kind,
)
essai_A_strategy = st.builds(
    essai_A,
)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=essai_B_strategy)
@settings(max_examples=50)
def test_essai_b_instantiation(instance):
    assert isinstance(instance, essai_B)

@given(instance=Kind_strategy)
@settings(max_examples=50)
def test_kind_instantiation(instance):
    assert isinstance(instance, Kind)

@given(instance=essai_A_strategy)
@settings(max_examples=50)
def test_essai_a_instantiation(instance):
    assert isinstance(instance, essai_A)
