import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    example4_Sirius_B,
    example4_Sirius_A,
    example4_Sirius_Element,
    example4_Sirius_Container,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_example4_sirius_b_is_not_abstract():
    assert not inspect.isabstract(example4_Sirius_B)


def test_example4_sirius_b_constructor_exists():
    assert callable(example4_Sirius_B.__init__)


def test_example4_sirius_b_constructor_args():
    sig = inspect.signature(example4_Sirius_B.__init__)
    params = list(sig.parameters.keys())



def test_example4_sirius_a_is_not_abstract():
    assert not inspect.isabstract(example4_Sirius_A)


def test_example4_sirius_a_constructor_exists():
    assert callable(example4_Sirius_A.__init__)


def test_example4_sirius_a_constructor_args():
    sig = inspect.signature(example4_Sirius_A.__init__)
    params = list(sig.parameters.keys())



def test_example4_sirius_element_is_not_abstract():
    assert not inspect.isabstract(example4_Sirius_Element)


def test_example4_sirius_element_constructor_exists():
    assert callable(example4_Sirius_Element.__init__)


def test_example4_sirius_element_constructor_args():
    sig = inspect.signature(example4_Sirius_Element.__init__)
    params = list(sig.parameters.keys())



def test_example4_sirius_container_is_not_abstract():
    assert not inspect.isabstract(example4_Sirius_Container)


def test_example4_sirius_container_constructor_exists():
    assert callable(example4_Sirius_Container.__init__)


def test_example4_sirius_container_constructor_args():
    sig = inspect.signature(example4_Sirius_Container.__init__)
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
example4_Sirius_B_strategy = st.builds(
    example4_Sirius_B,
)
example4_Sirius_A_strategy = st.builds(
    example4_Sirius_A,
)
example4_Sirius_Element_strategy = st.builds(
    example4_Sirius_Element,
)
example4_Sirius_Container_strategy = st.builds(
    example4_Sirius_Container,
)

@given(instance=example4_Sirius_B_strategy)
@settings(max_examples=50)
def test_example4_sirius_b_instantiation(instance):
    assert isinstance(instance, example4_Sirius_B)

@given(instance=example4_Sirius_A_strategy)
@settings(max_examples=50)
def test_example4_sirius_a_instantiation(instance):
    assert isinstance(instance, example4_Sirius_A)

@given(instance=example4_Sirius_Element_strategy)
@settings(max_examples=50)
def test_example4_sirius_element_instantiation(instance):
    assert isinstance(instance, example4_Sirius_Element)

@given(instance=example4_Sirius_Container_strategy)
@settings(max_examples=50)
def test_example4_sirius_container_instantiation(instance):
    assert isinstance(instance, example4_Sirius_Container)
