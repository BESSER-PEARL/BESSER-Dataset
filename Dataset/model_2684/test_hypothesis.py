import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    simpleTG::A,
    simpleTG::Container,
    simpleTG::C,
    simpleTG::B,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simpletg::a_is_not_abstract():
    assert not inspect.isabstract(simpleTG::A)


def test_simpletg::a_constructor_exists():
    assert callable(simpleTG::A.__init__)


def test_simpletg::a_constructor_args():
    sig = inspect.signature(simpleTG::A.__init__)
    params = list(sig.parameters.keys())



def test_simpletg::container_is_not_abstract():
    assert not inspect.isabstract(simpleTG::Container)


def test_simpletg::container_constructor_exists():
    assert callable(simpleTG::Container.__init__)


def test_simpletg::container_constructor_args():
    sig = inspect.signature(simpleTG::Container.__init__)
    params = list(sig.parameters.keys())



def test_simpletg::c_is_not_abstract():
    assert not inspect.isabstract(simpleTG::C)


def test_simpletg::c_constructor_exists():
    assert callable(simpleTG::C.__init__)


def test_simpletg::c_constructor_args():
    sig = inspect.signature(simpleTG::C.__init__)
    params = list(sig.parameters.keys())



def test_simpletg::b_is_not_abstract():
    assert not inspect.isabstract(simpleTG::B)


def test_simpletg::b_constructor_exists():
    assert callable(simpleTG::B.__init__)


def test_simpletg::b_constructor_args():
    sig = inspect.signature(simpleTG::B.__init__)
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
simpleTG::A_strategy = st.builds(
    simpleTG::A,
)
simpleTG::Container_strategy = st.builds(
    simpleTG::Container,
)
simpleTG::C_strategy = st.builds(
    simpleTG::C,
)
simpleTG::B_strategy = st.builds(
    simpleTG::B,
)

@given(instance=simpleTG::A_strategy)
@settings(max_examples=50)
def test_simpletg::a_instantiation(instance):
    assert isinstance(instance, simpleTG::A)

@given(instance=simpleTG::Container_strategy)
@settings(max_examples=50)
def test_simpletg::container_instantiation(instance):
    assert isinstance(instance, simpleTG::Container)

@given(instance=simpleTG::C_strategy)
@settings(max_examples=50)
def test_simpletg::c_instantiation(instance):
    assert isinstance(instance, simpleTG::C)

@given(instance=simpleTG::B_strategy)
@settings(max_examples=50)
def test_simpletg::b_instantiation(instance):
    assert isinstance(instance, simpleTG::B)
