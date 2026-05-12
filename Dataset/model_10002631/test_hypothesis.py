import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    T2,
    T,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_t2_is_not_abstract():
    assert not inspect.isabstract(T2)


def test_t2_constructor_exists():
    assert callable(T2.__init__)


def test_t2_constructor_args():
    sig = inspect.signature(T2.__init__)
    params = list(sig.parameters.keys())



def test_t_is_not_abstract():
    assert not inspect.isabstract(T)


def test_t_constructor_exists():
    assert callable(T.__init__)


def test_t_constructor_args():
    sig = inspect.signature(T.__init__)
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
T2_strategy = st.builds(
    T2,
)
T_strategy = st.builds(
    T,
)

@given(instance=T2_strategy)
@settings(max_examples=50)
def test_t2_instantiation(instance):
    assert isinstance(instance, T2)

@given(instance=T_strategy)
@settings(max_examples=50)
def test_t_instantiation(instance):
    assert isinstance(instance, T)
