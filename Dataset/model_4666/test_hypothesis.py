import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Lit,
    boolexp::Fals,
    boolexp::Tru,
    BinaryExp,
    boolexp::Or,
    boolexp::And,
    Exp,
    boolexp::Lit,
    boolexp::BinaryExp,
    boolexp::Exp,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_lit_is_not_abstract():
    assert not inspect.isabstract(Lit)


def test_lit_constructor_exists():
    assert callable(Lit.__init__)


def test_lit_constructor_args():
    sig = inspect.signature(Lit.__init__)
    params = list(sig.parameters.keys())



def test_boolexp::fals_is_not_abstract():
    assert not inspect.isabstract(boolexp::Fals)


def test_boolexp::fals_constructor_exists():
    assert callable(boolexp::Fals.__init__)


def test_boolexp::fals_constructor_args():
    sig = inspect.signature(boolexp::Fals.__init__)
    params = list(sig.parameters.keys())



def test_boolexp::tru_is_not_abstract():
    assert not inspect.isabstract(boolexp::Tru)


def test_boolexp::tru_constructor_exists():
    assert callable(boolexp::Tru.__init__)


def test_boolexp::tru_constructor_args():
    sig = inspect.signature(boolexp::Tru.__init__)
    params = list(sig.parameters.keys())



def test_binaryexp_is_not_abstract():
    assert not inspect.isabstract(BinaryExp)


def test_binaryexp_constructor_exists():
    assert callable(BinaryExp.__init__)


def test_binaryexp_constructor_args():
    sig = inspect.signature(BinaryExp.__init__)
    params = list(sig.parameters.keys())



def test_boolexp::or_is_not_abstract():
    assert not inspect.isabstract(boolexp::Or)


def test_boolexp::or_constructor_exists():
    assert callable(boolexp::Or.__init__)


def test_boolexp::or_constructor_args():
    sig = inspect.signature(boolexp::Or.__init__)
    params = list(sig.parameters.keys())



def test_boolexp::and_is_not_abstract():
    assert not inspect.isabstract(boolexp::And)


def test_boolexp::and_constructor_exists():
    assert callable(boolexp::And.__init__)


def test_boolexp::and_constructor_args():
    sig = inspect.signature(boolexp::And.__init__)
    params = list(sig.parameters.keys())



def test_exp_is_not_abstract():
    assert not inspect.isabstract(Exp)


def test_exp_constructor_exists():
    assert callable(Exp.__init__)


def test_exp_constructor_args():
    sig = inspect.signature(Exp.__init__)
    params = list(sig.parameters.keys())



def test_boolexp::lit_is_not_abstract():
    assert not inspect.isabstract(boolexp::Lit)


def test_boolexp::lit_constructor_exists():
    assert callable(boolexp::Lit.__init__)


def test_boolexp::lit_constructor_args():
    sig = inspect.signature(boolexp::Lit.__init__)
    params = list(sig.parameters.keys())



def test_boolexp::binaryexp_is_not_abstract():
    assert not inspect.isabstract(boolexp::BinaryExp)


def test_boolexp::binaryexp_constructor_exists():
    assert callable(boolexp::BinaryExp.__init__)


def test_boolexp::binaryexp_constructor_args():
    sig = inspect.signature(boolexp::BinaryExp.__init__)
    params = list(sig.parameters.keys())



def test_boolexp::exp_is_not_abstract():
    assert not inspect.isabstract(boolexp::Exp)


def test_boolexp::exp_constructor_exists():
    assert callable(boolexp::Exp.__init__)


def test_boolexp::exp_constructor_args():
    sig = inspect.signature(boolexp::Exp.__init__)
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
Lit_strategy = st.builds(
    Lit,
)
boolexp::Fals_strategy = st.builds(
    boolexp::Fals,
)
boolexp::Tru_strategy = st.builds(
    boolexp::Tru,
)
BinaryExp_strategy = st.builds(
    BinaryExp,
)
boolexp::Or_strategy = st.builds(
    boolexp::Or,
)
boolexp::And_strategy = st.builds(
    boolexp::And,
)
Exp_strategy = st.builds(
    Exp,
)
boolexp::Lit_strategy = st.builds(
    boolexp::Lit,
)
boolexp::BinaryExp_strategy = st.builds(
    boolexp::BinaryExp,
)
boolexp::Exp_strategy = st.builds(
    boolexp::Exp,
)

@given(instance=Lit_strategy)
@settings(max_examples=50)
def test_lit_instantiation(instance):
    assert isinstance(instance, Lit)

@given(instance=boolexp::Fals_strategy)
@settings(max_examples=50)
def test_boolexp::fals_instantiation(instance):
    assert isinstance(instance, boolexp::Fals)

@given(instance=boolexp::Tru_strategy)
@settings(max_examples=50)
def test_boolexp::tru_instantiation(instance):
    assert isinstance(instance, boolexp::Tru)

@given(instance=BinaryExp_strategy)
@settings(max_examples=50)
def test_binaryexp_instantiation(instance):
    assert isinstance(instance, BinaryExp)

@given(instance=boolexp::Or_strategy)
@settings(max_examples=50)
def test_boolexp::or_instantiation(instance):
    assert isinstance(instance, boolexp::Or)

@given(instance=boolexp::And_strategy)
@settings(max_examples=50)
def test_boolexp::and_instantiation(instance):
    assert isinstance(instance, boolexp::And)

@given(instance=Exp_strategy)
@settings(max_examples=50)
def test_exp_instantiation(instance):
    assert isinstance(instance, Exp)

@given(instance=boolexp::Lit_strategy)
@settings(max_examples=50)
def test_boolexp::lit_instantiation(instance):
    assert isinstance(instance, boolexp::Lit)

@given(instance=boolexp::BinaryExp_strategy)
@settings(max_examples=50)
def test_boolexp::binaryexp_instantiation(instance):
    assert isinstance(instance, boolexp::BinaryExp)

@given(instance=boolexp::Exp_strategy)
@settings(max_examples=50)
def test_boolexp::exp_instantiation(instance):
    assert isinstance(instance, boolexp::Exp)
