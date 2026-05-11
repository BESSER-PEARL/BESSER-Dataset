import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    rulegen::C,
    rulegen::B,
    rulegen::A,
    rulegen::Context,
    rulegen::D,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rulegen::c_is_not_abstract():
    assert not inspect.isabstract(rulegen::C)


def test_rulegen::c_constructor_exists():
    assert callable(rulegen::C.__init__)


def test_rulegen::c_constructor_args():
    sig = inspect.signature(rulegen::C.__init__)
    params = list(sig.parameters.keys())



def test_rulegen::b_is_not_abstract():
    assert not inspect.isabstract(rulegen::B)


def test_rulegen::b_constructor_exists():
    assert callable(rulegen::B.__init__)


def test_rulegen::b_constructor_args():
    sig = inspect.signature(rulegen::B.__init__)
    params = list(sig.parameters.keys())



def test_rulegen::a_is_not_abstract():
    assert not inspect.isabstract(rulegen::A)


def test_rulegen::a_constructor_exists():
    assert callable(rulegen::A.__init__)


def test_rulegen::a_constructor_args():
    sig = inspect.signature(rulegen::A.__init__)
    params = list(sig.parameters.keys())



def test_rulegen::context_is_not_abstract():
    assert not inspect.isabstract(rulegen::Context)


def test_rulegen::context_constructor_exists():
    assert callable(rulegen::Context.__init__)


def test_rulegen::context_constructor_args():
    sig = inspect.signature(rulegen::Context.__init__)
    params = list(sig.parameters.keys())



def test_rulegen::d_is_not_abstract():
    assert not inspect.isabstract(rulegen::D)


def test_rulegen::d_constructor_exists():
    assert callable(rulegen::D.__init__)


def test_rulegen::d_constructor_args():
    sig = inspect.signature(rulegen::D.__init__)
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
rulegen::C_strategy = st.builds(
    rulegen::C,
)
rulegen::B_strategy = st.builds(
    rulegen::B,
)
rulegen::A_strategy = st.builds(
    rulegen::A,
)
rulegen::Context_strategy = st.builds(
    rulegen::Context,
)
rulegen::D_strategy = st.builds(
    rulegen::D,
)

@given(instance=rulegen::C_strategy)
@settings(max_examples=50)
def test_rulegen::c_instantiation(instance):
    assert isinstance(instance, rulegen::C)

@given(instance=rulegen::B_strategy)
@settings(max_examples=50)
def test_rulegen::b_instantiation(instance):
    assert isinstance(instance, rulegen::B)

@given(instance=rulegen::A_strategy)
@settings(max_examples=50)
def test_rulegen::a_instantiation(instance):
    assert isinstance(instance, rulegen::A)

@given(instance=rulegen::Context_strategy)
@settings(max_examples=50)
def test_rulegen::context_instantiation(instance):
    assert isinstance(instance, rulegen::Context)

@given(instance=rulegen::D_strategy)
@settings(max_examples=50)
def test_rulegen::d_instantiation(instance):
    assert isinstance(instance, rulegen::D)
