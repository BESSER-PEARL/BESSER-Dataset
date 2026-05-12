import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    m_pa_C,
    m_pa_B,
    m_pa_A,
    m_ToplevelClass,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_m_pa_c_is_not_abstract():
    assert not inspect.isabstract(m_pa_C)


def test_m_pa_c_constructor_exists():
    assert callable(m_pa_C.__init__)


def test_m_pa_c_constructor_args():
    sig = inspect.signature(m_pa_C.__init__)
    params = list(sig.parameters.keys())



def test_m_pa_b_is_not_abstract():
    assert not inspect.isabstract(m_pa_B)


def test_m_pa_b_constructor_exists():
    assert callable(m_pa_B.__init__)


def test_m_pa_b_constructor_args():
    sig = inspect.signature(m_pa_B.__init__)
    params = list(sig.parameters.keys())



def test_m_pa_a_is_not_abstract():
    assert not inspect.isabstract(m_pa_A)


def test_m_pa_a_constructor_exists():
    assert callable(m_pa_A.__init__)


def test_m_pa_a_constructor_args():
    sig = inspect.signature(m_pa_A.__init__)
    params = list(sig.parameters.keys())



def test_m_toplevelclass_is_not_abstract():
    assert not inspect.isabstract(m_ToplevelClass)


def test_m_toplevelclass_constructor_exists():
    assert callable(m_ToplevelClass.__init__)


def test_m_toplevelclass_constructor_args():
    sig = inspect.signature(m_ToplevelClass.__init__)
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
m_pa_C_strategy = st.builds(
    m_pa_C,
)
m_pa_B_strategy = st.builds(
    m_pa_B,
)
m_pa_A_strategy = st.builds(
    m_pa_A,
)
m_ToplevelClass_strategy = st.builds(
    m_ToplevelClass,
)

@given(instance=m_pa_C_strategy)
@settings(max_examples=50)
def test_m_pa_c_instantiation(instance):
    assert isinstance(instance, m_pa_C)

@given(instance=m_pa_B_strategy)
@settings(max_examples=50)
def test_m_pa_b_instantiation(instance):
    assert isinstance(instance, m_pa_B)

@given(instance=m_pa_A_strategy)
@settings(max_examples=50)
def test_m_pa_a_instantiation(instance):
    assert isinstance(instance, m_pa_A)

@given(instance=m_ToplevelClass_strategy)
@settings(max_examples=50)
def test_m_toplevelclass_instantiation(instance):
    assert isinstance(instance, m_ToplevelClass)
