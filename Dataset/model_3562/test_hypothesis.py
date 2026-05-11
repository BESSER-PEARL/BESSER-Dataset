import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    BinExp,
    boolexp::Or,
    boolexp::And,
    Lit,
    boolexp::Fals,
    boolexp::Tru,
    Exp,
    boolexp::Not,
    boolexp::VarRef,
    boolexp::BinExp,
    boolexp::Exp,
    boolexp::Lit,
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



def test_exp_is_not_abstract():
    assert not inspect.isabstract(Exp)


def test_exp_constructor_exists():
    assert callable(Exp.__init__)


def test_exp_constructor_args():
    sig = inspect.signature(Exp.__init__)
    params = list(sig.parameters.keys())



def test_boolexp::not_is_not_abstract():
    assert not inspect.isabstract(boolexp::Not)


def test_boolexp::not_constructor_exists():
    assert callable(boolexp::Not.__init__)


def test_boolexp::not_constructor_args():
    sig = inspect.signature(boolexp::Not.__init__)
    params = list(sig.parameters.keys())



def test_boolexp::varref_is_not_abstract():
    assert not inspect.isabstract(boolexp::VarRef)


def test_boolexp::varref_constructor_exists():
    assert callable(boolexp::VarRef.__init__)


def test_boolexp::varref_constructor_args():
    sig = inspect.signature(boolexp::VarRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_boolexp::varref_has_name():
    assert hasattr(boolexp::VarRef, "name")
    descriptor = None
    for klass in boolexp::VarRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_boolexp::binexp_is_not_abstract():
    assert not inspect.isabstract(boolexp::BinExp)


def test_boolexp::binexp_constructor_exists():
    assert callable(boolexp::BinExp.__init__)


def test_boolexp::binexp_constructor_args():
    sig = inspect.signature(boolexp::BinExp.__init__)
    params = list(sig.parameters.keys())



def test_boolexp::exp_is_not_abstract():
    assert not inspect.isabstract(boolexp::Exp)


def test_boolexp::exp_constructor_exists():
    assert callable(boolexp::Exp.__init__)


def test_boolexp::exp_constructor_args():
    sig = inspect.signature(boolexp::Exp.__init__)
    params = list(sig.parameters.keys())



def test_boolexp::lit_is_not_abstract():
    assert not inspect.isabstract(boolexp::Lit)


def test_boolexp::lit_constructor_exists():
    assert callable(boolexp::Lit.__init__)


def test_boolexp::lit_constructor_args():
    sig = inspect.signature(boolexp::Lit.__init__)
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
boolexp::Or_strategy = st.builds(
    boolexp::Or,
)
boolexp::And_strategy = st.builds(
    boolexp::And,
)
Lit_strategy = st.builds(
    Lit,
)
boolexp::Fals_strategy = st.builds(
    boolexp::Fals,
)
boolexp::Tru_strategy = st.builds(
    boolexp::Tru,
)
Exp_strategy = st.builds(
    Exp,
)
boolexp::Not_strategy = st.builds(
    boolexp::Not,
)
boolexp::VarRef_strategy = st.builds(
    boolexp::VarRef,
    name=
        safe_text
)
boolexp::BinExp_strategy = st.builds(
    boolexp::BinExp,
)
boolexp::Exp_strategy = st.builds(
    boolexp::Exp,
)
boolexp::Lit_strategy = st.builds(
    boolexp::Lit,
)

@given(instance=BinExp_strategy)
@settings(max_examples=50)
def test_binexp_instantiation(instance):
    assert isinstance(instance, BinExp)

@given(instance=boolexp::Or_strategy)
@settings(max_examples=50)
def test_boolexp::or_instantiation(instance):
    assert isinstance(instance, boolexp::Or)

@given(instance=boolexp::And_strategy)
@settings(max_examples=50)
def test_boolexp::and_instantiation(instance):
    assert isinstance(instance, boolexp::And)

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

@given(instance=Exp_strategy)
@settings(max_examples=50)
def test_exp_instantiation(instance):
    assert isinstance(instance, Exp)

@given(instance=boolexp::Not_strategy)
@settings(max_examples=50)
def test_boolexp::not_instantiation(instance):
    assert isinstance(instance, boolexp::Not)

@given(instance=boolexp::VarRef_strategy)
@settings(max_examples=50)
def test_boolexp::varref_instantiation(instance):
    assert isinstance(instance, boolexp::VarRef)

@given(instance=boolexp::VarRef_strategy)
def test_boolexp::varref_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=boolexp::VarRef_strategy)
def test_boolexp::varref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=boolexp::BinExp_strategy)
@settings(max_examples=50)
def test_boolexp::binexp_instantiation(instance):
    assert isinstance(instance, boolexp::BinExp)

@given(instance=boolexp::Exp_strategy)
@settings(max_examples=50)
def test_boolexp::exp_instantiation(instance):
    assert isinstance(instance, boolexp::Exp)

@given(instance=boolexp::Lit_strategy)
@settings(max_examples=50)
def test_boolexp::lit_instantiation(instance):
    assert isinstance(instance, boolexp::Lit)
