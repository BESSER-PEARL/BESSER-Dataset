import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    target_F,
    target_E,
    F,
    target_H,
    target_G,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_target_f_is_not_abstract():
    assert not inspect.isabstract(target_F)


def test_target_f_constructor_exists():
    assert callable(target_F.__init__)


def test_target_f_constructor_args():
    sig = inspect.signature(target_F.__init__)
    params = list(sig.parameters.keys())



def test_target_e_is_not_abstract():
    assert not inspect.isabstract(target_E)


def test_target_e_constructor_exists():
    assert callable(target_E.__init__)


def test_target_e_constructor_args():
    sig = inspect.signature(target_E.__init__)
    params = list(sig.parameters.keys())



def test_f_is_not_abstract():
    assert not inspect.isabstract(F)


def test_f_constructor_exists():
    assert callable(F.__init__)


def test_f_constructor_args():
    sig = inspect.signature(F.__init__)
    params = list(sig.parameters.keys())



def test_target_h_is_not_abstract():
    assert not inspect.isabstract(target_H)


def test_target_h_constructor_exists():
    assert callable(target_H.__init__)


def test_target_h_constructor_args():
    sig = inspect.signature(target_H.__init__)
    params = list(sig.parameters.keys())



def test_target_g_is_not_abstract():
    assert not inspect.isabstract(target_G)


def test_target_g_constructor_exists():
    assert callable(target_G.__init__)


def test_target_g_constructor_args():
    sig = inspect.signature(target_G.__init__)
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
target_F_strategy = st.builds(
    target_F,
)
target_E_strategy = st.builds(
    target_E,
)
F_strategy = st.builds(
    F,
)
target_H_strategy = st.builds(
    target_H,
)
target_G_strategy = st.builds(
    target_G,
)

@given(instance=target_F_strategy)
@settings(max_examples=50)
def test_target_f_instantiation(instance):
    assert isinstance(instance, target_F)

@given(instance=target_E_strategy)
@settings(max_examples=50)
def test_target_e_instantiation(instance):
    assert isinstance(instance, target_E)

@given(instance=F_strategy)
@settings(max_examples=50)
def test_f_instantiation(instance):
    assert isinstance(instance, F)

@given(instance=target_H_strategy)
@settings(max_examples=50)
def test_target_h_instantiation(instance):
    assert isinstance(instance, target_H)

@given(instance=target_G_strategy)
@settings(max_examples=50)
def test_target_g_instantiation(instance):
    assert isinstance(instance, target_G)
