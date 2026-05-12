import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Exp,
    boolexp_BinaryExp,
    boolexp_Exp,
    Lit,
    boolexp_Fals,
    boolexp_Tru,
    BinaryExp,
    boolexp_Or,
    boolexp_And,
    boolexp_Lit,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_exp_is_not_abstract():
    assert not inspect.isabstract(Exp)


def test_exp_constructor_exists():
    assert callable(Exp.__init__)


def test_exp_constructor_args():
    sig = inspect.signature(Exp.__init__)
    params = list(sig.parameters.keys())



def test_boolexp_binaryexp_is_not_abstract():
    assert not inspect.isabstract(boolexp_BinaryExp)


def test_boolexp_binaryexp_constructor_exists():
    assert callable(boolexp_BinaryExp.__init__)


def test_boolexp_binaryexp_constructor_args():
    sig = inspect.signature(boolexp_BinaryExp.__init__)
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



def test_binaryexp_is_not_abstract():
    assert not inspect.isabstract(BinaryExp)


def test_binaryexp_constructor_exists():
    assert callable(BinaryExp.__init__)


def test_binaryexp_constructor_args():
    sig = inspect.signature(BinaryExp.__init__)
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



def test_boolexp_lit_is_not_abstract():
    assert not inspect.isabstract(boolexp_Lit)


def test_boolexp_lit_constructor_exists():
    assert callable(boolexp_Lit.__init__)


def test_boolexp_lit_constructor_args():
    sig = inspect.signature(boolexp_Lit.__init__)
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
Exp_strategy = st.builds(
    Exp,
)
boolexp_BinaryExp_strategy = st.builds(
    boolexp_BinaryExp,
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
BinaryExp_strategy = st.builds(
    BinaryExp,
)
boolexp_Or_strategy = st.builds(
    boolexp_Or,
)
boolexp_And_strategy = st.builds(
    boolexp_And,
)
boolexp_Lit_strategy = st.builds(
    boolexp_Lit,
)

@given(instance=Exp_strategy)
@settings(max_examples=50)
def test_exp_instantiation(instance):
    assert isinstance(instance, Exp)

@given(instance=boolexp_BinaryExp_strategy)
@settings(max_examples=50)
def test_boolexp_binaryexp_instantiation(instance):
    assert isinstance(instance, boolexp_BinaryExp)

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

@given(instance=BinaryExp_strategy)
@settings(max_examples=50)
def test_binaryexp_instantiation(instance):
    assert isinstance(instance, BinaryExp)

@given(instance=boolexp_Or_strategy)
@settings(max_examples=50)
def test_boolexp_or_instantiation(instance):
    assert isinstance(instance, boolexp_Or)

@given(instance=boolexp_And_strategy)
@settings(max_examples=50)
def test_boolexp_and_instantiation(instance):
    assert isinstance(instance, boolexp_And)

@given(instance=boolexp_Lit_strategy)
@settings(max_examples=50)
def test_boolexp_lit_instantiation(instance):
    assert isinstance(instance, boolexp_Lit)
