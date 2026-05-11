import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    example4::Sirius::B,
    example4::Sirius::A,
    example4::Sirius::Element,
    example4::Sirius::Container,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_example4::sirius::b_is_not_abstract():
    assert not inspect.isabstract(example4::Sirius::B)


def test_example4::sirius::b_constructor_exists():
    assert callable(example4::Sirius::B.__init__)


def test_example4::sirius::b_constructor_args():
    sig = inspect.signature(example4::Sirius::B.__init__)
    params = list(sig.parameters.keys())



def test_example4::sirius::a_is_not_abstract():
    assert not inspect.isabstract(example4::Sirius::A)


def test_example4::sirius::a_constructor_exists():
    assert callable(example4::Sirius::A.__init__)


def test_example4::sirius::a_constructor_args():
    sig = inspect.signature(example4::Sirius::A.__init__)
    params = list(sig.parameters.keys())



def test_example4::sirius::element_is_not_abstract():
    assert not inspect.isabstract(example4::Sirius::Element)


def test_example4::sirius::element_constructor_exists():
    assert callable(example4::Sirius::Element.__init__)


def test_example4::sirius::element_constructor_args():
    sig = inspect.signature(example4::Sirius::Element.__init__)
    params = list(sig.parameters.keys())



def test_example4::sirius::container_is_not_abstract():
    assert not inspect.isabstract(example4::Sirius::Container)


def test_example4::sirius::container_constructor_exists():
    assert callable(example4::Sirius::Container.__init__)


def test_example4::sirius::container_constructor_args():
    sig = inspect.signature(example4::Sirius::Container.__init__)
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
example4::Sirius::B_strategy = st.builds(
    example4::Sirius::B,
)
example4::Sirius::A_strategy = st.builds(
    example4::Sirius::A,
)
example4::Sirius::Element_strategy = st.builds(
    example4::Sirius::Element,
)
example4::Sirius::Container_strategy = st.builds(
    example4::Sirius::Container,
)

@given(instance=example4::Sirius::B_strategy)
@settings(max_examples=50)
def test_example4::sirius::b_instantiation(instance):
    assert isinstance(instance, example4::Sirius::B)

@given(instance=example4::Sirius::A_strategy)
@settings(max_examples=50)
def test_example4::sirius::a_instantiation(instance):
    assert isinstance(instance, example4::Sirius::A)

@given(instance=example4::Sirius::Element_strategy)
@settings(max_examples=50)
def test_example4::sirius::element_instantiation(instance):
    assert isinstance(instance, example4::Sirius::Element)

@given(instance=example4::Sirius::Container_strategy)
@settings(max_examples=50)
def test_example4::sirius::container_instantiation(instance):
    assert isinstance(instance, example4::Sirius::Container)
