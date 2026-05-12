import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ABC_D,
    ABC_C,
    ABC_B,
    ABC_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abc_d_is_not_abstract():
    assert not inspect.isabstract(ABC_D)


def test_abc_d_constructor_exists():
    assert callable(ABC_D.__init__)


def test_abc_d_constructor_args():
    sig = inspect.signature(ABC_D.__init__)
    params = list(sig.parameters.keys())



def test_abc_c_is_not_abstract():
    assert not inspect.isabstract(ABC_C)


def test_abc_c_constructor_exists():
    assert callable(ABC_C.__init__)


def test_abc_c_constructor_args():
    sig = inspect.signature(ABC_C.__init__)
    params = list(sig.parameters.keys())



def test_abc_b_is_not_abstract():
    assert not inspect.isabstract(ABC_B)


def test_abc_b_constructor_exists():
    assert callable(ABC_B.__init__)


def test_abc_b_constructor_args():
    sig = inspect.signature(ABC_B.__init__)
    params = list(sig.parameters.keys())



def test_abc_a_is_not_abstract():
    assert not inspect.isabstract(ABC_A)


def test_abc_a_constructor_exists():
    assert callable(ABC_A.__init__)


def test_abc_a_constructor_args():
    sig = inspect.signature(ABC_A.__init__)
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
ABC_D_strategy = st.builds(
    ABC_D,
)
ABC_C_strategy = st.builds(
    ABC_C,
)
ABC_B_strategy = st.builds(
    ABC_B,
)
ABC_A_strategy = st.builds(
    ABC_A,
)

@given(instance=ABC_D_strategy)
@settings(max_examples=50)
def test_abc_d_instantiation(instance):
    assert isinstance(instance, ABC_D)

@given(instance=ABC_C_strategy)
@settings(max_examples=50)
def test_abc_c_instantiation(instance):
    assert isinstance(instance, ABC_C)

@given(instance=ABC_B_strategy)
@settings(max_examples=50)
def test_abc_b_instantiation(instance):
    assert isinstance(instance, ABC_B)

@given(instance=ABC_A_strategy)
@settings(max_examples=50)
def test_abc_a_instantiation(instance):
    assert isinstance(instance, ABC_A)
