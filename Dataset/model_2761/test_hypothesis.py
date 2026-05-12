import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    D,
    case5_E,
    case5_B,
    case5_N,
    T,
    case5_D,
    case5_A,
    case5_T,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_d_is_not_abstract():
    assert not inspect.isabstract(D)


def test_d_constructor_exists():
    assert callable(D.__init__)


def test_d_constructor_args():
    sig = inspect.signature(D.__init__)
    params = list(sig.parameters.keys())



def test_case5_e_is_not_abstract():
    assert not inspect.isabstract(case5_E)


def test_case5_e_constructor_exists():
    assert callable(case5_E.__init__)


def test_case5_e_constructor_args():
    sig = inspect.signature(case5_E.__init__)
    params = list(sig.parameters.keys())



def test_case5_b_is_not_abstract():
    assert not inspect.isabstract(case5_B)


def test_case5_b_constructor_exists():
    assert callable(case5_B.__init__)


def test_case5_b_constructor_args():
    sig = inspect.signature(case5_B.__init__)
    params = list(sig.parameters.keys())



def test_case5_n_is_not_abstract():
    assert not inspect.isabstract(case5_N)


def test_case5_n_constructor_exists():
    assert callable(case5_N.__init__)


def test_case5_n_constructor_args():
    sig = inspect.signature(case5_N.__init__)
    params = list(sig.parameters.keys())



def test_t_is_not_abstract():
    assert not inspect.isabstract(T)


def test_t_constructor_exists():
    assert callable(T.__init__)


def test_t_constructor_args():
    sig = inspect.signature(T.__init__)
    params = list(sig.parameters.keys())



def test_case5_d_is_not_abstract():
    assert not inspect.isabstract(case5_D)


def test_case5_d_constructor_exists():
    assert callable(case5_D.__init__)


def test_case5_d_constructor_args():
    sig = inspect.signature(case5_D.__init__)
    params = list(sig.parameters.keys())



def test_case5_a_is_not_abstract():
    assert not inspect.isabstract(case5_A)


def test_case5_a_constructor_exists():
    assert callable(case5_A.__init__)


def test_case5_a_constructor_args():
    sig = inspect.signature(case5_A.__init__)
    params = list(sig.parameters.keys())



def test_case5_t_is_not_abstract():
    assert not inspect.isabstract(case5_T)


def test_case5_t_constructor_exists():
    assert callable(case5_T.__init__)


def test_case5_t_constructor_args():
    sig = inspect.signature(case5_T.__init__)
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
D_strategy = st.builds(
    D,
)
case5_E_strategy = st.builds(
    case5_E,
)
case5_B_strategy = st.builds(
    case5_B,
)
case5_N_strategy = st.builds(
    case5_N,
)
T_strategy = st.builds(
    T,
)
case5_D_strategy = st.builds(
    case5_D,
)
case5_A_strategy = st.builds(
    case5_A,
)
case5_T_strategy = st.builds(
    case5_T,
)

@given(instance=D_strategy)
@settings(max_examples=50)
def test_d_instantiation(instance):
    assert isinstance(instance, D)

@given(instance=case5_E_strategy)
@settings(max_examples=50)
def test_case5_e_instantiation(instance):
    assert isinstance(instance, case5_E)

@given(instance=case5_B_strategy)
@settings(max_examples=50)
def test_case5_b_instantiation(instance):
    assert isinstance(instance, case5_B)

@given(instance=case5_N_strategy)
@settings(max_examples=50)
def test_case5_n_instantiation(instance):
    assert isinstance(instance, case5_N)

@given(instance=T_strategy)
@settings(max_examples=50)
def test_t_instantiation(instance):
    assert isinstance(instance, T)

@given(instance=case5_D_strategy)
@settings(max_examples=50)
def test_case5_d_instantiation(instance):
    assert isinstance(instance, case5_D)

@given(instance=case5_A_strategy)
@settings(max_examples=50)
def test_case5_a_instantiation(instance):
    assert isinstance(instance, case5_A)

@given(instance=case5_T_strategy)
@settings(max_examples=50)
def test_case5_t_instantiation(instance):
    assert isinstance(instance, case5_T)
