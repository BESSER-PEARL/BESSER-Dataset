import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    simpleTG_A,
    simpleTG_Container,
    simpleTG_C,
    simpleTG_B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simpletg_a_is_not_abstract():
    assert not inspect.isabstract(simpleTG_A)


def test_simpletg_a_constructor_exists():
    assert callable(simpleTG_A.__init__)


def test_simpletg_a_constructor_args():
    sig = inspect.signature(simpleTG_A.__init__)
    params = list(sig.parameters.keys())



def test_simpletg_container_is_not_abstract():
    assert not inspect.isabstract(simpleTG_Container)


def test_simpletg_container_constructor_exists():
    assert callable(simpleTG_Container.__init__)


def test_simpletg_container_constructor_args():
    sig = inspect.signature(simpleTG_Container.__init__)
    params = list(sig.parameters.keys())



def test_simpletg_c_is_not_abstract():
    assert not inspect.isabstract(simpleTG_C)


def test_simpletg_c_constructor_exists():
    assert callable(simpleTG_C.__init__)


def test_simpletg_c_constructor_args():
    sig = inspect.signature(simpleTG_C.__init__)
    params = list(sig.parameters.keys())



def test_simpletg_b_is_not_abstract():
    assert not inspect.isabstract(simpleTG_B)


def test_simpletg_b_constructor_exists():
    assert callable(simpleTG_B.__init__)


def test_simpletg_b_constructor_args():
    sig = inspect.signature(simpleTG_B.__init__)
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
simpleTG_A_strategy = st.builds(
    simpleTG_A,
)
simpleTG_Container_strategy = st.builds(
    simpleTG_Container,
)
simpleTG_C_strategy = st.builds(
    simpleTG_C,
)
simpleTG_B_strategy = st.builds(
    simpleTG_B,
)

@given(instance=simpleTG_A_strategy)
@settings(max_examples=50)
def test_simpletg_a_instantiation(instance):
    assert isinstance(instance, simpleTG_A)

@given(instance=simpleTG_Container_strategy)
@settings(max_examples=50)
def test_simpletg_container_instantiation(instance):
    assert isinstance(instance, simpleTG_Container)

@given(instance=simpleTG_C_strategy)
@settings(max_examples=50)
def test_simpletg_c_instantiation(instance):
    assert isinstance(instance, simpleTG_C)

@given(instance=simpleTG_B_strategy)
@settings(max_examples=50)
def test_simpletg_b_instantiation(instance):
    assert isinstance(instance, simpleTG_B)
