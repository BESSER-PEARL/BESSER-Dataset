import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    BinExp,
    boolexp_Or,
    boolexp_And,
    Exp,
    boolexp_Not,
    boolexp_Lit,
    boolexp_BinExp,
    boolexp_Exp,
    Lit,
    boolexp_Fals,
    boolexp_Tru,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_binexp_is_not_abstract():
    assert not inspect.isabstract(BinExp)


def test_binexp_constructor_exists():
    assert callable(BinExp.__init__)


def test_binexp_constructor_args():
    sig = inspect.signature(BinExp.__init__)
    params = list(sig.parameters.keys())



def test_boolexp_or_is_not_abstract():
    assert not inspect.isabstract(boolexp_Or)


def test_boolexp_or_constructor_exists():
    assert callable(boolexp_Or.__init__)


def test_boolexp_or_constructor_args():
    sig = inspect.signature(boolexp_Or.__init__)
    params = list(sig.parameters.keys())



def test_boolexp_and_is_not_abstract():
    assert not inspect.isabstract(boolexp_And)


def test_boolexp_and_constructor_exists():
    assert callable(boolexp_And.__init__)


def test_boolexp_and_constructor_args():
    sig = inspect.signature(boolexp_And.__init__)
    params = list(sig.parameters.keys())



def test_exp_is_not_abstract():
    assert not inspect.isabstract(Exp)


def test_exp_constructor_exists():
    assert callable(Exp.__init__)


def test_exp_constructor_args():
    sig = inspect.signature(Exp.__init__)
    params = list(sig.parameters.keys())



def test_boolexp_not_is_not_abstract():
    assert not inspect.isabstract(boolexp_Not)


def test_boolexp_not_constructor_exists():
    assert callable(boolexp_Not.__init__)


def test_boolexp_not_constructor_args():
    sig = inspect.signature(boolexp_Not.__init__)
    params = list(sig.parameters.keys())



def test_boolexp_lit_is_not_abstract():
    assert not inspect.isabstract(boolexp_Lit)


def test_boolexp_lit_constructor_exists():
    assert callable(boolexp_Lit.__init__)


def test_boolexp_lit_constructor_args():
    sig = inspect.signature(boolexp_Lit.__init__)
    params = list(sig.parameters.keys())



def test_boolexp_binexp_is_not_abstract():
    assert not inspect.isabstract(boolexp_BinExp)


def test_boolexp_binexp_constructor_exists():
    assert callable(boolexp_BinExp.__init__)


def test_boolexp_binexp_constructor_args():
    sig = inspect.signature(boolexp_BinExp.__init__)
    params = list(sig.parameters.keys())



def test_boolexp_exp_is_not_abstract():
    assert not inspect.isabstract(boolexp_Exp)


def test_boolexp_exp_constructor_exists():
    assert callable(boolexp_Exp.__init__)


def test_boolexp_exp_constructor_args():
    sig = inspect.signature(boolexp_Exp.__init__)
    params = list(sig.parameters.keys())



def test_lit_is_not_abstract():
    assert not inspect.isabstract(Lit)


def test_lit_constructor_exists():
    assert callable(Lit.__init__)


def test_lit_constructor_args():
    sig = inspect.signature(Lit.__init__)
    params = list(sig.parameters.keys())



def test_boolexp_fals_is_not_abstract():
    assert not inspect.isabstract(boolexp_Fals)


def test_boolexp_fals_constructor_exists():
    assert callable(boolexp_Fals.__init__)


def test_boolexp_fals_constructor_args():
    sig = inspect.signature(boolexp_Fals.__init__)
    params = list(sig.parameters.keys())



def test_boolexp_tru_is_not_abstract():
    assert not inspect.isabstract(boolexp_Tru)


def test_boolexp_tru_constructor_exists():
    assert callable(boolexp_Tru.__init__)


def test_boolexp_tru_constructor_args():
    sig = inspect.signature(boolexp_Tru.__init__)
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
BinExp_strategy = st.builds(
    BinExp,
)
boolexp_Or_strategy = st.builds(
    boolexp_Or,
)
boolexp_And_strategy = st.builds(
    boolexp_And,
)
Exp_strategy = st.builds(
    Exp,
)
boolexp_Not_strategy = st.builds(
    boolexp_Not,
)
boolexp_Lit_strategy = st.builds(
    boolexp_Lit,
)
boolexp_BinExp_strategy = st.builds(
    boolexp_BinExp,
)
boolexp_Exp_strategy = st.builds(
    boolexp_Exp,
)
Lit_strategy = st.builds(
    Lit,
)
boolexp_Fals_strategy = st.builds(
    boolexp_Fals,
)
boolexp_Tru_strategy = st.builds(
    boolexp_Tru,
)

@given(instance=BinExp_strategy)
@settings(max_examples=50)
def test_binexp_instantiation(instance):
    assert isinstance(instance, BinExp)

@given(instance=boolexp_Or_strategy)
@settings(max_examples=50)
def test_boolexp_or_instantiation(instance):
    assert isinstance(instance, boolexp_Or)

@given(instance=boolexp_And_strategy)
@settings(max_examples=50)
def test_boolexp_and_instantiation(instance):
    assert isinstance(instance, boolexp_And)

@given(instance=Exp_strategy)
@settings(max_examples=50)
def test_exp_instantiation(instance):
    assert isinstance(instance, Exp)

@given(instance=boolexp_Not_strategy)
@settings(max_examples=50)
def test_boolexp_not_instantiation(instance):
    assert isinstance(instance, boolexp_Not)

@given(instance=boolexp_Lit_strategy)
@settings(max_examples=50)
def test_boolexp_lit_instantiation(instance):
    assert isinstance(instance, boolexp_Lit)

@given(instance=boolexp_BinExp_strategy)
@settings(max_examples=50)
def test_boolexp_binexp_instantiation(instance):
    assert isinstance(instance, boolexp_BinExp)

@given(instance=boolexp_Exp_strategy)
@settings(max_examples=50)
def test_boolexp_exp_instantiation(instance):
    assert isinstance(instance, boolexp_Exp)

@given(instance=Lit_strategy)
@settings(max_examples=50)
def test_lit_instantiation(instance):
    assert isinstance(instance, Lit)

@given(instance=boolexp_Fals_strategy)
@settings(max_examples=50)
def test_boolexp_fals_instantiation(instance):
    assert isinstance(instance, boolexp_Fals)

@given(instance=boolexp_Tru_strategy)
@settings(max_examples=50)
def test_boolexp_tru_instantiation(instance):
    assert isinstance(instance, boolexp_Tru)
