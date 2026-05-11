import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Lit,
    boolExpEnv::Tru,
    Exp,
    boolExpEnv::Lit,
    boolExpEnv::BinExp,
    boolExpEnv::VarRef,
    BinExp,
    boolExpEnv::Or,
    boolExpEnv::And,
    boolExpEnv::Not,
    boolExpEnv::Fals,
    boolExpEnv::Exp,
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



def test_boolexpenv::tru_is_not_abstract():
    assert not inspect.isabstract(boolExpEnv::Tru)


def test_boolexpenv::tru_constructor_exists():
    assert callable(boolExpEnv::Tru.__init__)


def test_boolexpenv::tru_constructor_args():
    sig = inspect.signature(boolExpEnv::Tru.__init__)
    params = list(sig.parameters.keys())



def test_exp_is_not_abstract():
    assert not inspect.isabstract(Exp)


def test_exp_constructor_exists():
    assert callable(Exp.__init__)


def test_exp_constructor_args():
    sig = inspect.signature(Exp.__init__)
    params = list(sig.parameters.keys())



def test_boolexpenv::lit_is_not_abstract():
    assert not inspect.isabstract(boolExpEnv::Lit)


def test_boolexpenv::lit_constructor_exists():
    assert callable(boolExpEnv::Lit.__init__)


def test_boolexpenv::lit_constructor_args():
    sig = inspect.signature(boolExpEnv::Lit.__init__)
    params = list(sig.parameters.keys())



def test_boolexpenv::binexp_is_not_abstract():
    assert not inspect.isabstract(boolExpEnv::BinExp)


def test_boolexpenv::binexp_constructor_exists():
    assert callable(boolExpEnv::BinExp.__init__)


def test_boolexpenv::binexp_constructor_args():
    sig = inspect.signature(boolExpEnv::BinExp.__init__)
    params = list(sig.parameters.keys())



def test_boolexpenv::varref_is_not_abstract():
    assert not inspect.isabstract(boolExpEnv::VarRef)


def test_boolexpenv::varref_constructor_exists():
    assert callable(boolExpEnv::VarRef.__init__)


def test_boolexpenv::varref_constructor_args():
    sig = inspect.signature(boolExpEnv::VarRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_boolexpenv::varref_has_name():
    assert hasattr(boolExpEnv::VarRef, "name")
    descriptor = None
    for klass in boolExpEnv::VarRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_binexp_is_not_abstract():
    assert not inspect.isabstract(BinExp)


def test_binexp_constructor_exists():
    assert callable(BinExp.__init__)


def test_binexp_constructor_args():
    sig = inspect.signature(BinExp.__init__)
    params = list(sig.parameters.keys())



def test_boolexpenv::or_is_not_abstract():
    assert not inspect.isabstract(boolExpEnv::Or)


def test_boolexpenv::or_constructor_exists():
    assert callable(boolExpEnv::Or.__init__)


def test_boolexpenv::or_constructor_args():
    sig = inspect.signature(boolExpEnv::Or.__init__)
    params = list(sig.parameters.keys())



def test_boolexpenv::and_is_not_abstract():
    assert not inspect.isabstract(boolExpEnv::And)


def test_boolexpenv::and_constructor_exists():
    assert callable(boolExpEnv::And.__init__)


def test_boolexpenv::and_constructor_args():
    sig = inspect.signature(boolExpEnv::And.__init__)
    params = list(sig.parameters.keys())



def test_boolexpenv::not_is_not_abstract():
    assert not inspect.isabstract(boolExpEnv::Not)


def test_boolexpenv::not_constructor_exists():
    assert callable(boolExpEnv::Not.__init__)


def test_boolexpenv::not_constructor_args():
    sig = inspect.signature(boolExpEnv::Not.__init__)
    params = list(sig.parameters.keys())



def test_boolexpenv::fals_is_not_abstract():
    assert not inspect.isabstract(boolExpEnv::Fals)


def test_boolexpenv::fals_constructor_exists():
    assert callable(boolExpEnv::Fals.__init__)


def test_boolexpenv::fals_constructor_args():
    sig = inspect.signature(boolExpEnv::Fals.__init__)
    params = list(sig.parameters.keys())



def test_boolexpenv::exp_is_not_abstract():
    assert not inspect.isabstract(boolExpEnv::Exp)


def test_boolexpenv::exp_constructor_exists():
    assert callable(boolExpEnv::Exp.__init__)


def test_boolexpenv::exp_constructor_args():
    sig = inspect.signature(boolExpEnv::Exp.__init__)
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
boolExpEnv::Tru_strategy = st.builds(
    boolExpEnv::Tru,
)
Exp_strategy = st.builds(
    Exp,
)
boolExpEnv::Lit_strategy = st.builds(
    boolExpEnv::Lit,
)
boolExpEnv::BinExp_strategy = st.builds(
    boolExpEnv::BinExp,
)
boolExpEnv::VarRef_strategy = st.builds(
    boolExpEnv::VarRef,
    name=
        safe_text
)
BinExp_strategy = st.builds(
    BinExp,
)
boolExpEnv::Or_strategy = st.builds(
    boolExpEnv::Or,
)
boolExpEnv::And_strategy = st.builds(
    boolExpEnv::And,
)
boolExpEnv::Not_strategy = st.builds(
    boolExpEnv::Not,
)
boolExpEnv::Fals_strategy = st.builds(
    boolExpEnv::Fals,
)
boolExpEnv::Exp_strategy = st.builds(
    boolExpEnv::Exp,
)

@given(instance=Lit_strategy)
@settings(max_examples=50)
def test_lit_instantiation(instance):
    assert isinstance(instance, Lit)

@given(instance=boolExpEnv::Tru_strategy)
@settings(max_examples=50)
def test_boolexpenv::tru_instantiation(instance):
    assert isinstance(instance, boolExpEnv::Tru)

@given(instance=Exp_strategy)
@settings(max_examples=50)
def test_exp_instantiation(instance):
    assert isinstance(instance, Exp)

@given(instance=boolExpEnv::Lit_strategy)
@settings(max_examples=50)
def test_boolexpenv::lit_instantiation(instance):
    assert isinstance(instance, boolExpEnv::Lit)

@given(instance=boolExpEnv::BinExp_strategy)
@settings(max_examples=50)
def test_boolexpenv::binexp_instantiation(instance):
    assert isinstance(instance, boolExpEnv::BinExp)

@given(instance=boolExpEnv::VarRef_strategy)
@settings(max_examples=50)
def test_boolexpenv::varref_instantiation(instance):
    assert isinstance(instance, boolExpEnv::VarRef)

@given(instance=boolExpEnv::VarRef_strategy)
def test_boolexpenv::varref_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=boolExpEnv::VarRef_strategy)
def test_boolexpenv::varref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=BinExp_strategy)
@settings(max_examples=50)
def test_binexp_instantiation(instance):
    assert isinstance(instance, BinExp)

@given(instance=boolExpEnv::Or_strategy)
@settings(max_examples=50)
def test_boolexpenv::or_instantiation(instance):
    assert isinstance(instance, boolExpEnv::Or)

@given(instance=boolExpEnv::And_strategy)
@settings(max_examples=50)
def test_boolexpenv::and_instantiation(instance):
    assert isinstance(instance, boolExpEnv::And)

@given(instance=boolExpEnv::Not_strategy)
@settings(max_examples=50)
def test_boolexpenv::not_instantiation(instance):
    assert isinstance(instance, boolExpEnv::Not)

@given(instance=boolExpEnv::Fals_strategy)
@settings(max_examples=50)
def test_boolexpenv::fals_instantiation(instance):
    assert isinstance(instance, boolExpEnv::Fals)

@given(instance=boolExpEnv::Exp_strategy)
@settings(max_examples=50)
def test_boolexpenv::exp_instantiation(instance):
    assert isinstance(instance, boolExpEnv::Exp)
