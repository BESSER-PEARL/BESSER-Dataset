import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    e::F,
    e::D,
    e::E,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_e::f_is_not_abstract():
    assert not inspect.isabstract(e::F)


def test_e::f_constructor_exists():
    assert callable(e::F.__init__)


def test_e::f_constructor_args():
    sig = inspect.signature(e::F.__init__)
    params = list(sig.parameters.keys())



def test_e::d_is_not_abstract():
    assert not inspect.isabstract(e::D)


def test_e::d_constructor_exists():
    assert callable(e::D.__init__)


def test_e::d_constructor_args():
    sig = inspect.signature(e::D.__init__)
    params = list(sig.parameters.keys())



def test_e::e_is_not_abstract():
    assert not inspect.isabstract(e::E)


def test_e::e_constructor_exists():
    assert callable(e::E.__init__)


def test_e::e_constructor_args():
    sig = inspect.signature(e::E.__init__)
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
e::F_strategy = st.builds(
    e::F,
)
e::D_strategy = st.builds(
    e::D,
)
e::E_strategy = st.builds(
    e::E,
)

@given(instance=e::F_strategy)
@settings(max_examples=50)
def test_e::f_instantiation(instance):
    assert isinstance(instance, e::F)

@given(instance=e::D_strategy)
@settings(max_examples=50)
def test_e::d_instantiation(instance):
    assert isinstance(instance, e::D)

@given(instance=e::E_strategy)
@settings(max_examples=50)
def test_e::e_instantiation(instance):
    assert isinstance(instance, e::E)
