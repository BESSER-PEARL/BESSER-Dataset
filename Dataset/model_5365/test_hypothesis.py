import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    e_D,
    e_E,
    e_F,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_e_d_is_not_abstract():
    assert not inspect.isabstract(e_D)


def test_e_d_constructor_exists():
    assert callable(e_D.__init__)


def test_e_d_constructor_args():
    sig = inspect.signature(e_D.__init__)
    params = list(sig.parameters.keys())



def test_e_e_is_not_abstract():
    assert not inspect.isabstract(e_E)


def test_e_e_constructor_exists():
    assert callable(e_E.__init__)


def test_e_e_constructor_args():
    sig = inspect.signature(e_E.__init__)
    params = list(sig.parameters.keys())



def test_e_f_is_not_abstract():
    assert not inspect.isabstract(e_F)


def test_e_f_constructor_exists():
    assert callable(e_F.__init__)


def test_e_f_constructor_args():
    sig = inspect.signature(e_F.__init__)
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
e_D_strategy = st.builds(
    e_D,
)
e_E_strategy = st.builds(
    e_E,
)
e_F_strategy = st.builds(
    e_F,
)

@given(instance=e_D_strategy)
@settings(max_examples=50)
def test_e_d_instantiation(instance):
    assert isinstance(instance, e_D)

@given(instance=e_E_strategy)
@settings(max_examples=50)
def test_e_e_instantiation(instance):
    assert isinstance(instance, e_E)

@given(instance=e_F_strategy)
@settings(max_examples=50)
def test_e_f_instantiation(instance):
    assert isinstance(instance, e_F)
