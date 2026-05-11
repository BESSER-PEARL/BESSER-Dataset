import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Action,
    essai::B,
    Kind,
    essai::A,
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



def test_essai::b_is_not_abstract():
    assert not inspect.isabstract(essai::B)


def test_essai::b_constructor_exists():
    assert callable(essai::B.__init__)


def test_essai::b_constructor_args():
    sig = inspect.signature(essai::B.__init__)
    params = list(sig.parameters.keys())



def test_kind_is_not_abstract():
    assert not inspect.isabstract(Kind)


def test_kind_constructor_exists():
    assert callable(Kind.__init__)


def test_kind_constructor_args():
    sig = inspect.signature(Kind.__init__)
    params = list(sig.parameters.keys())



def test_essai::a_is_not_abstract():
    assert not inspect.isabstract(essai::A)


def test_essai::a_constructor_exists():
    assert callable(essai::A.__init__)


def test_essai::a_constructor_args():
    sig = inspect.signature(essai::A.__init__)
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
essai::B_strategy = st.builds(
    essai::B,
)
Kind_strategy = st.builds(
    Kind,
)
essai::A_strategy = st.builds(
    essai::A,
)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=essai::B_strategy)
@settings(max_examples=50)
def test_essai::b_instantiation(instance):
    assert isinstance(instance, essai::B)

@given(instance=Kind_strategy)
@settings(max_examples=50)
def test_kind_instantiation(instance):
    assert isinstance(instance, Kind)

@given(instance=essai::A_strategy)
@settings(max_examples=50)
def test_essai::a_instantiation(instance):
    assert isinstance(instance, essai::A)
