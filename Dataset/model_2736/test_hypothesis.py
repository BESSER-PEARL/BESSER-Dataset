import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Abc_C,
    Abc_classB,
    Abc_A,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_abc_c_is_not_abstract():
    assert not inspect.isabstract(Abc_C)


def test_abc_c_constructor_exists():
    assert callable(Abc_C.__init__)


def test_abc_c_constructor_args():
    sig = inspect.signature(Abc_C.__init__)
    params = list(sig.parameters.keys())



def test_abc_classb_is_not_abstract():
    assert not inspect.isabstract(Abc_classB)


def test_abc_classb_constructor_exists():
    assert callable(Abc_classB.__init__)


def test_abc_classb_constructor_args():
    sig = inspect.signature(Abc_classB.__init__)
    params = list(sig.parameters.keys())



def test_abc_a_is_not_abstract():
    assert not inspect.isabstract(Abc_A)


def test_abc_a_constructor_exists():
    assert callable(Abc_A.__init__)


def test_abc_a_constructor_args():
    sig = inspect.signature(Abc_A.__init__)
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
Abc_C_strategy = st.builds(
    Abc_C,
)
Abc_classB_strategy = st.builds(
    Abc_classB,
)
Abc_A_strategy = st.builds(
    Abc_A,
)

@given(instance=Abc_C_strategy)
@settings(max_examples=50)
def test_abc_c_instantiation(instance):
    assert isinstance(instance, Abc_C)

@given(instance=Abc_classB_strategy)
@settings(max_examples=50)
def test_abc_classb_instantiation(instance):
    assert isinstance(instance, Abc_classB)

@given(instance=Abc_A_strategy)
@settings(max_examples=50)
def test_abc_a_instantiation(instance):
    assert isinstance(instance, Abc_A)
