import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    while::Exp,
    Exp,
    while::VarExp,
    while::BinaryExp,
    BoolExp,
    BinaryExp,
    while::NEqExp,
    while::AndExp,
    while::EqExp,
    while::BoolExp,
    Statement,
    while::Assignment,
    while::Ret,
    while::If,
    while::While,
    while::Val,
    while::Var,
    while::Statement,
    while::Program,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_while::exp_is_not_abstract():
    assert not inspect.isabstract(while::Exp)


def test_while::exp_constructor_exists():
    assert callable(while::Exp.__init__)


def test_while::exp_constructor_args():
    sig = inspect.signature(while::Exp.__init__)
    params = list(sig.parameters.keys())



def test_exp_is_not_abstract():
    assert not inspect.isabstract(Exp)


def test_exp_constructor_exists():
    assert callable(Exp.__init__)


def test_exp_constructor_args():
    sig = inspect.signature(Exp.__init__)
    params = list(sig.parameters.keys())



def test_while::varexp_is_not_abstract():
    assert not inspect.isabstract(while::VarExp)


def test_while::varexp_constructor_exists():
    assert callable(while::VarExp.__init__)


def test_while::varexp_constructor_args():
    sig = inspect.signature(while::VarExp.__init__)
    params = list(sig.parameters.keys())



def test_while::binaryexp_is_not_abstract():
    assert not inspect.isabstract(while::BinaryExp)


def test_while::binaryexp_constructor_exists():
    assert callable(while::BinaryExp.__init__)


def test_while::binaryexp_constructor_args():
    sig = inspect.signature(while::BinaryExp.__init__)
    params = list(sig.parameters.keys())



def test_boolexp_is_not_abstract():
    assert not inspect.isabstract(BoolExp)


def test_boolexp_constructor_exists():
    assert callable(BoolExp.__init__)


def test_boolexp_constructor_args():
    sig = inspect.signature(BoolExp.__init__)
    params = list(sig.parameters.keys())



def test_binaryexp_is_not_abstract():
    assert not inspect.isabstract(BinaryExp)


def test_binaryexp_constructor_exists():
    assert callable(BinaryExp.__init__)


def test_binaryexp_constructor_args():
    sig = inspect.signature(BinaryExp.__init__)
    params = list(sig.parameters.keys())



def test_while::neqexp_is_not_abstract():
    assert not inspect.isabstract(while::NEqExp)


def test_while::neqexp_constructor_exists():
    assert callable(while::NEqExp.__init__)


def test_while::neqexp_constructor_args():
    sig = inspect.signature(while::NEqExp.__init__)
    params = list(sig.parameters.keys())



def test_while::andexp_is_not_abstract():
    assert not inspect.isabstract(while::AndExp)


def test_while::andexp_constructor_exists():
    assert callable(while::AndExp.__init__)


def test_while::andexp_constructor_args():
    sig = inspect.signature(while::AndExp.__init__)
    params = list(sig.parameters.keys())



def test_while::eqexp_is_not_abstract():
    assert not inspect.isabstract(while::EqExp)


def test_while::eqexp_constructor_exists():
    assert callable(while::EqExp.__init__)


def test_while::eqexp_constructor_args():
    sig = inspect.signature(while::EqExp.__init__)
    params = list(sig.parameters.keys())



def test_while::boolexp_is_not_abstract():
    assert not inspect.isabstract(while::BoolExp)


def test_while::boolexp_constructor_exists():
    assert callable(while::BoolExp.__init__)


def test_while::boolexp_constructor_args():
    sig = inspect.signature(while::BoolExp.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_while::assignment_is_not_abstract():
    assert not inspect.isabstract(while::Assignment)


def test_while::assignment_constructor_exists():
    assert callable(while::Assignment.__init__)


def test_while::assignment_constructor_args():
    sig = inspect.signature(while::Assignment.__init__)
    params = list(sig.parameters.keys())



def test_while::ret_is_not_abstract():
    assert not inspect.isabstract(while::Ret)


def test_while::ret_constructor_exists():
    assert callable(while::Ret.__init__)


def test_while::ret_constructor_args():
    sig = inspect.signature(while::Ret.__init__)
    params = list(sig.parameters.keys())



def test_while::if_is_not_abstract():
    assert not inspect.isabstract(while::If)


def test_while::if_constructor_exists():
    assert callable(while::If.__init__)


def test_while::if_constructor_args():
    sig = inspect.signature(while::If.__init__)
    params = list(sig.parameters.keys())



def test_while::while_is_not_abstract():
    assert not inspect.isabstract(while::While)


def test_while::while_constructor_exists():
    assert callable(while::While.__init__)


def test_while::while_constructor_args():
    sig = inspect.signature(while::While.__init__)
    params = list(sig.parameters.keys())



def test_while::val_is_not_abstract():
    assert not inspect.isabstract(while::Val)


def test_while::val_constructor_exists():
    assert callable(while::Val.__init__)


def test_while::val_constructor_args():
    sig = inspect.signature(while::Val.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_while::val_has_id():
    assert hasattr(while::Val, "id")
    descriptor = None
    for klass in while::Val.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_while::var_is_not_abstract():
    assert not inspect.isabstract(while::Var)


def test_while::var_constructor_exists():
    assert callable(while::Var.__init__)


def test_while::var_constructor_args():
    sig = inspect.signature(while::Var.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_while::var_has_id():
    assert hasattr(while::Var, "id")
    descriptor = None
    for klass in while::Var.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_while::statement_is_not_abstract():
    assert not inspect.isabstract(while::Statement)


def test_while::statement_constructor_exists():
    assert callable(while::Statement.__init__)


def test_while::statement_constructor_args():
    sig = inspect.signature(while::Statement.__init__)
    params = list(sig.parameters.keys())



def test_while::program_is_not_abstract():
    assert not inspect.isabstract(while::Program)


def test_while::program_constructor_exists():
    assert callable(while::Program.__init__)


def test_while::program_constructor_args():
    sig = inspect.signature(while::Program.__init__)
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
while::Exp_strategy = st.builds(
    while::Exp,
)
Exp_strategy = st.builds(
    Exp,
)
while::VarExp_strategy = st.builds(
    while::VarExp,
)
while::BinaryExp_strategy = st.builds(
    while::BinaryExp,
)
BoolExp_strategy = st.builds(
    BoolExp,
)
BinaryExp_strategy = st.builds(
    BinaryExp,
)
while::NEqExp_strategy = st.builds(
    while::NEqExp,
)
while::AndExp_strategy = st.builds(
    while::AndExp,
)
while::EqExp_strategy = st.builds(
    while::EqExp,
)
while::BoolExp_strategy = st.builds(
    while::BoolExp,
)
Statement_strategy = st.builds(
    Statement,
)
while::Assignment_strategy = st.builds(
    while::Assignment,
)
while::Ret_strategy = st.builds(
    while::Ret,
)
while::If_strategy = st.builds(
    while::If,
)
while::While_strategy = st.builds(
    while::While,
)
while::Val_strategy = st.builds(
    while::Val,
    id=
        safe_text
)
while::Var_strategy = st.builds(
    while::Var,
    id=
        safe_text
)
while::Statement_strategy = st.builds(
    while::Statement,
)
while::Program_strategy = st.builds(
    while::Program,
)

@given(instance=while::Exp_strategy)
@settings(max_examples=50)
def test_while::exp_instantiation(instance):
    assert isinstance(instance, while::Exp)

@given(instance=Exp_strategy)
@settings(max_examples=50)
def test_exp_instantiation(instance):
    assert isinstance(instance, Exp)

@given(instance=while::VarExp_strategy)
@settings(max_examples=50)
def test_while::varexp_instantiation(instance):
    assert isinstance(instance, while::VarExp)

@given(instance=while::BinaryExp_strategy)
@settings(max_examples=50)
def test_while::binaryexp_instantiation(instance):
    assert isinstance(instance, while::BinaryExp)

@given(instance=BoolExp_strategy)
@settings(max_examples=50)
def test_boolexp_instantiation(instance):
    assert isinstance(instance, BoolExp)

@given(instance=BinaryExp_strategy)
@settings(max_examples=50)
def test_binaryexp_instantiation(instance):
    assert isinstance(instance, BinaryExp)

@given(instance=while::NEqExp_strategy)
@settings(max_examples=50)
def test_while::neqexp_instantiation(instance):
    assert isinstance(instance, while::NEqExp)

@given(instance=while::AndExp_strategy)
@settings(max_examples=50)
def test_while::andexp_instantiation(instance):
    assert isinstance(instance, while::AndExp)

@given(instance=while::EqExp_strategy)
@settings(max_examples=50)
def test_while::eqexp_instantiation(instance):
    assert isinstance(instance, while::EqExp)

@given(instance=while::BoolExp_strategy)
@settings(max_examples=50)
def test_while::boolexp_instantiation(instance):
    assert isinstance(instance, while::BoolExp)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=while::Assignment_strategy)
@settings(max_examples=50)
def test_while::assignment_instantiation(instance):
    assert isinstance(instance, while::Assignment)

@given(instance=while::Ret_strategy)
@settings(max_examples=50)
def test_while::ret_instantiation(instance):
    assert isinstance(instance, while::Ret)

@given(instance=while::If_strategy)
@settings(max_examples=50)
def test_while::if_instantiation(instance):
    assert isinstance(instance, while::If)

@given(instance=while::While_strategy)
@settings(max_examples=50)
def test_while::while_instantiation(instance):
    assert isinstance(instance, while::While)

@given(instance=while::Val_strategy)
@settings(max_examples=50)
def test_while::val_instantiation(instance):
    assert isinstance(instance, while::Val)

@given(instance=while::Val_strategy)
def test_while::val_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=while::Val_strategy)
def test_while::val_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=while::Var_strategy)
@settings(max_examples=50)
def test_while::var_instantiation(instance):
    assert isinstance(instance, while::Var)

@given(instance=while::Var_strategy)
def test_while::var_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=while::Var_strategy)
def test_while::var_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=while::Statement_strategy)
@settings(max_examples=50)
def test_while::statement_instantiation(instance):
    assert isinstance(instance, while::Statement)

@given(instance=while::Program_strategy)
@settings(max_examples=50)
def test_while::program_instantiation(instance):
    assert isinstance(instance, while::Program)
