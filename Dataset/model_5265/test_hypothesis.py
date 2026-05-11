import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    E,
    A,
    astrans::B,
    astrans::A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_e_is_not_abstract():
    assert not inspect.isabstract(E)


def test_e_constructor_exists():
    assert callable(E.__init__)


def test_e_constructor_args():
    sig = inspect.signature(E.__init__)
    params = list(sig.parameters.keys())



def test_a_is_not_abstract():
    assert not inspect.isabstract(A)


def test_a_constructor_exists():
    assert callable(A.__init__)


def test_a_constructor_args():
    sig = inspect.signature(A.__init__)
    params = list(sig.parameters.keys())



def test_astrans::b_is_not_abstract():
    assert not inspect.isabstract(astrans::B)


def test_astrans::b_constructor_exists():
    assert callable(astrans::B.__init__)


def test_astrans::b_constructor_args():
    sig = inspect.signature(astrans::B.__init__)
    params = list(sig.parameters.keys())



def test_astrans::a_is_not_abstract():
    assert not inspect.isabstract(astrans::A)


def test_astrans::a_constructor_exists():
    assert callable(astrans::A.__init__)


def test_astrans::a_constructor_args():
    sig = inspect.signature(astrans::A.__init__)
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
E_strategy = st.builds(
    E,
)
A_strategy = st.builds(
    A,
)
astrans::B_strategy = st.builds(
    astrans::B,
)
astrans::A_strategy = st.builds(
    astrans::A,
)

@given(instance=E_strategy)
@settings(max_examples=50)
def test_e_instantiation(instance):
    assert isinstance(instance, E)

@given(instance=A_strategy)
@settings(max_examples=50)
def test_a_instantiation(instance):
    assert isinstance(instance, A)

@given(instance=astrans::B_strategy)
@settings(max_examples=50)
def test_astrans::b_instantiation(instance):
    assert isinstance(instance, astrans::B)

@given(instance=astrans::A_strategy)
@settings(max_examples=50)
def test_astrans::a_instantiation(instance):
    assert isinstance(instance, astrans::A)
