import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    F,
    target::H,
    target::G,
    target::F,
    target::E,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_f_is_not_abstract():
    assert not inspect.isabstract(F)


def test_f_constructor_exists():
    assert callable(F.__init__)


def test_f_constructor_args():
    sig = inspect.signature(F.__init__)
    params = list(sig.parameters.keys())



def test_target::h_is_not_abstract():
    assert not inspect.isabstract(target::H)


def test_target::h_constructor_exists():
    assert callable(target::H.__init__)


def test_target::h_constructor_args():
    sig = inspect.signature(target::H.__init__)
    params = list(sig.parameters.keys())



def test_target::g_is_not_abstract():
    assert not inspect.isabstract(target::G)


def test_target::g_constructor_exists():
    assert callable(target::G.__init__)


def test_target::g_constructor_args():
    sig = inspect.signature(target::G.__init__)
    params = list(sig.parameters.keys())



def test_target::f_is_not_abstract():
    assert not inspect.isabstract(target::F)


def test_target::f_constructor_exists():
    assert callable(target::F.__init__)


def test_target::f_constructor_args():
    sig = inspect.signature(target::F.__init__)
    params = list(sig.parameters.keys())



def test_target::e_is_not_abstract():
    assert not inspect.isabstract(target::E)


def test_target::e_constructor_exists():
    assert callable(target::E.__init__)


def test_target::e_constructor_args():
    sig = inspect.signature(target::E.__init__)
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
F_strategy = st.builds(
    F,
)
target::H_strategy = st.builds(
    target::H,
)
target::G_strategy = st.builds(
    target::G,
)
target::F_strategy = st.builds(
    target::F,
)
target::E_strategy = st.builds(
    target::E,
)

@given(instance=F_strategy)
@settings(max_examples=50)
def test_f_instantiation(instance):
    assert isinstance(instance, F)

@given(instance=target::H_strategy)
@settings(max_examples=50)
def test_target::h_instantiation(instance):
    assert isinstance(instance, target::H)

@given(instance=target::G_strategy)
@settings(max_examples=50)
def test_target::g_instantiation(instance):
    assert isinstance(instance, target::G)

@given(instance=target::F_strategy)
@settings(max_examples=50)
def test_target::f_instantiation(instance):
    assert isinstance(instance, target::F)

@given(instance=target::E_strategy)
@settings(max_examples=50)
def test_target::e_instantiation(instance):
    assert isinstance(instance, target::E)
