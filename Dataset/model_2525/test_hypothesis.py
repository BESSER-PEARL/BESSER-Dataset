import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    rulegen_C,
    rulegen_B,
    rulegen_A,
    rulegen_Context,
    rulegen_D,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rulegen_c_is_not_abstract():
    assert not inspect.isabstract(rulegen_C)


def test_rulegen_c_constructor_exists():
    assert callable(rulegen_C.__init__)


def test_rulegen_c_constructor_args():
    sig = inspect.signature(rulegen_C.__init__)
    params = list(sig.parameters.keys())



def test_rulegen_b_is_not_abstract():
    assert not inspect.isabstract(rulegen_B)


def test_rulegen_b_constructor_exists():
    assert callable(rulegen_B.__init__)


def test_rulegen_b_constructor_args():
    sig = inspect.signature(rulegen_B.__init__)
    params = list(sig.parameters.keys())



def test_rulegen_a_is_not_abstract():
    assert not inspect.isabstract(rulegen_A)


def test_rulegen_a_constructor_exists():
    assert callable(rulegen_A.__init__)


def test_rulegen_a_constructor_args():
    sig = inspect.signature(rulegen_A.__init__)
    params = list(sig.parameters.keys())



def test_rulegen_context_is_not_abstract():
    assert not inspect.isabstract(rulegen_Context)


def test_rulegen_context_constructor_exists():
    assert callable(rulegen_Context.__init__)


def test_rulegen_context_constructor_args():
    sig = inspect.signature(rulegen_Context.__init__)
    params = list(sig.parameters.keys())



def test_rulegen_d_is_not_abstract():
    assert not inspect.isabstract(rulegen_D)


def test_rulegen_d_constructor_exists():
    assert callable(rulegen_D.__init__)


def test_rulegen_d_constructor_args():
    sig = inspect.signature(rulegen_D.__init__)
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
rulegen_C_strategy = st.builds(
    rulegen_C,
)
rulegen_B_strategy = st.builds(
    rulegen_B,
)
rulegen_A_strategy = st.builds(
    rulegen_A,
)
rulegen_Context_strategy = st.builds(
    rulegen_Context,
)
rulegen_D_strategy = st.builds(
    rulegen_D,
)

@given(instance=rulegen_C_strategy)
@settings(max_examples=50)
def test_rulegen_c_instantiation(instance):
    assert isinstance(instance, rulegen_C)

@given(instance=rulegen_B_strategy)
@settings(max_examples=50)
def test_rulegen_b_instantiation(instance):
    assert isinstance(instance, rulegen_B)

@given(instance=rulegen_A_strategy)
@settings(max_examples=50)
def test_rulegen_a_instantiation(instance):
    assert isinstance(instance, rulegen_A)

@given(instance=rulegen_Context_strategy)
@settings(max_examples=50)
def test_rulegen_context_instantiation(instance):
    assert isinstance(instance, rulegen_Context)

@given(instance=rulegen_D_strategy)
@settings(max_examples=50)
def test_rulegen_d_instantiation(instance):
    assert isinstance(instance, rulegen_D)
