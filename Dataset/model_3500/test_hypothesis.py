import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    while_Exp,
    Exp,
    while_VarExp,
    while_BinaryExp,
    BoolExp,
    BinaryExp,
    while_NEqExp,
    while_AndExp,
    while_EqExp,
    while_BoolExp,
    Statement,
    while_Ret,
    while_Assignment,
    while_If,
    while_While,
    while_Val,
    while_Var,
    while_Statement,
    while_Program,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_while_exp_is_not_abstract():
    assert not inspect.isabstract(while_Exp)


def test_while_exp_constructor_exists():
    assert callable(while_Exp.__init__)


def test_while_exp_constructor_args():
    sig = inspect.signature(while_Exp.__init__)
    params = list(sig.parameters.keys())



def test_exp_is_not_abstract():
    assert not inspect.isabstract(Exp)


def test_exp_constructor_exists():
    assert callable(Exp.__init__)


def test_exp_constructor_args():
    sig = inspect.signature(Exp.__init__)
    params = list(sig.parameters.keys())



def test_while_varexp_is_not_abstract():
    assert not inspect.isabstract(while_VarExp)


def test_while_varexp_constructor_exists():
    assert callable(while_VarExp.__init__)


def test_while_varexp_constructor_args():
    sig = inspect.signature(while_VarExp.__init__)
    params = list(sig.parameters.keys())



def test_while_binaryexp_is_not_abstract():
    assert not inspect.isabstract(while_BinaryExp)


def test_while_binaryexp_constructor_exists():
    assert callable(while_BinaryExp.__init__)


def test_while_binaryexp_constructor_args():
    sig = inspect.signature(while_BinaryExp.__init__)
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



def test_while_neqexp_is_not_abstract():
    assert not inspect.isabstract(while_NEqExp)


def test_while_neqexp_constructor_exists():
    assert callable(while_NEqExp.__init__)


def test_while_neqexp_constructor_args():
    sig = inspect.signature(while_NEqExp.__init__)
    params = list(sig.parameters.keys())



def test_while_andexp_is_not_abstract():
    assert not inspect.isabstract(while_AndExp)


def test_while_andexp_constructor_exists():
    assert callable(while_AndExp.__init__)


def test_while_andexp_constructor_args():
    sig = inspect.signature(while_AndExp.__init__)
    params = list(sig.parameters.keys())



def test_while_eqexp_is_not_abstract():
    assert not inspect.isabstract(while_EqExp)


def test_while_eqexp_constructor_exists():
    assert callable(while_EqExp.__init__)


def test_while_eqexp_constructor_args():
    sig = inspect.signature(while_EqExp.__init__)
    params = list(sig.parameters.keys())



def test_while_boolexp_is_not_abstract():
    assert not inspect.isabstract(while_BoolExp)


def test_while_boolexp_constructor_exists():
    assert callable(while_BoolExp.__init__)


def test_while_boolexp_constructor_args():
    sig = inspect.signature(while_BoolExp.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_while_ret_is_not_abstract():
    assert not inspect.isabstract(while_Ret)


def test_while_ret_constructor_exists():
    assert callable(while_Ret.__init__)


def test_while_ret_constructor_args():
    sig = inspect.signature(while_Ret.__init__)
    params = list(sig.parameters.keys())



def test_while_assignment_is_not_abstract():
    assert not inspect.isabstract(while_Assignment)


def test_while_assignment_constructor_exists():
    assert callable(while_Assignment.__init__)


def test_while_assignment_constructor_args():
    sig = inspect.signature(while_Assignment.__init__)
    params = list(sig.parameters.keys())



def test_while_if_is_not_abstract():
    assert not inspect.isabstract(while_If)


def test_while_if_constructor_exists():
    assert callable(while_If.__init__)


def test_while_if_constructor_args():
    sig = inspect.signature(while_If.__init__)
    params = list(sig.parameters.keys())



def test_while_while_is_not_abstract():
    assert not inspect.isabstract(while_While)


def test_while_while_constructor_exists():
    assert callable(while_While.__init__)


def test_while_while_constructor_args():
    sig = inspect.signature(while_While.__init__)
    params = list(sig.parameters.keys())



def test_while_val_is_not_abstract():
    assert not inspect.isabstract(while_Val)


def test_while_val_constructor_exists():
    assert callable(while_Val.__init__)


def test_while_val_constructor_args():
    sig = inspect.signature(while_Val.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_while_val_has_id():
    assert hasattr(while_Val, "id")
    descriptor = None
    for klass in while_Val.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_while_var_is_not_abstract():
    assert not inspect.isabstract(while_Var)


def test_while_var_constructor_exists():
    assert callable(while_Var.__init__)


def test_while_var_constructor_args():
    sig = inspect.signature(while_Var.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_while_var_has_id():
    assert hasattr(while_Var, "id")
    descriptor = None
    for klass in while_Var.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_while_statement_is_not_abstract():
    assert not inspect.isabstract(while_Statement)


def test_while_statement_constructor_exists():
    assert callable(while_Statement.__init__)


def test_while_statement_constructor_args():
    sig = inspect.signature(while_Statement.__init__)
    params = list(sig.parameters.keys())



def test_while_program_is_not_abstract():
    assert not inspect.isabstract(while_Program)


def test_while_program_constructor_exists():
    assert callable(while_Program.__init__)


def test_while_program_constructor_args():
    sig = inspect.signature(while_Program.__init__)
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
while_Exp_strategy = st.builds(
    while_Exp,
)
Exp_strategy = st.builds(
    Exp,
)
while_VarExp_strategy = st.builds(
    while_VarExp,
)
while_BinaryExp_strategy = st.builds(
    while_BinaryExp,
)
BoolExp_strategy = st.builds(
    BoolExp,
)
BinaryExp_strategy = st.builds(
    BinaryExp,
)
while_NEqExp_strategy = st.builds(
    while_NEqExp,
)
while_AndExp_strategy = st.builds(
    while_AndExp,
)
while_EqExp_strategy = st.builds(
    while_EqExp,
)
while_BoolExp_strategy = st.builds(
    while_BoolExp,
)
Statement_strategy = st.builds(
    Statement,
)
while_Ret_strategy = st.builds(
    while_Ret,
)
while_Assignment_strategy = st.builds(
    while_Assignment,
)
while_If_strategy = st.builds(
    while_If,
)
while_While_strategy = st.builds(
    while_While,
)
while_Val_strategy = st.builds(
    while_Val,
    id=
        safe_text
)
while_Var_strategy = st.builds(
    while_Var,
    id=
        safe_text
)
while_Statement_strategy = st.builds(
    while_Statement,
)
while_Program_strategy = st.builds(
    while_Program,
)

@given(instance=while_Exp_strategy)
@settings(max_examples=50)
def test_while_exp_instantiation(instance):
    assert isinstance(instance, while_Exp)

@given(instance=Exp_strategy)
@settings(max_examples=50)
def test_exp_instantiation(instance):
    assert isinstance(instance, Exp)

@given(instance=while_VarExp_strategy)
@settings(max_examples=50)
def test_while_varexp_instantiation(instance):
    assert isinstance(instance, while_VarExp)

@given(instance=while_BinaryExp_strategy)
@settings(max_examples=50)
def test_while_binaryexp_instantiation(instance):
    assert isinstance(instance, while_BinaryExp)

@given(instance=BoolExp_strategy)
@settings(max_examples=50)
def test_boolexp_instantiation(instance):
    assert isinstance(instance, BoolExp)

@given(instance=BinaryExp_strategy)
@settings(max_examples=50)
def test_binaryexp_instantiation(instance):
    assert isinstance(instance, BinaryExp)

@given(instance=while_NEqExp_strategy)
@settings(max_examples=50)
def test_while_neqexp_instantiation(instance):
    assert isinstance(instance, while_NEqExp)

@given(instance=while_AndExp_strategy)
@settings(max_examples=50)
def test_while_andexp_instantiation(instance):
    assert isinstance(instance, while_AndExp)

@given(instance=while_EqExp_strategy)
@settings(max_examples=50)
def test_while_eqexp_instantiation(instance):
    assert isinstance(instance, while_EqExp)

@given(instance=while_BoolExp_strategy)
@settings(max_examples=50)
def test_while_boolexp_instantiation(instance):
    assert isinstance(instance, while_BoolExp)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=while_Ret_strategy)
@settings(max_examples=50)
def test_while_ret_instantiation(instance):
    assert isinstance(instance, while_Ret)

@given(instance=while_Assignment_strategy)
@settings(max_examples=50)
def test_while_assignment_instantiation(instance):
    assert isinstance(instance, while_Assignment)

@given(instance=while_If_strategy)
@settings(max_examples=50)
def test_while_if_instantiation(instance):
    assert isinstance(instance, while_If)

@given(instance=while_While_strategy)
@settings(max_examples=50)
def test_while_while_instantiation(instance):
    assert isinstance(instance, while_While)

@given(instance=while_Val_strategy)
@settings(max_examples=50)
def test_while_val_instantiation(instance):
    assert isinstance(instance, while_Val)



@given(instance=while_Val_strategy)
def test_while_val_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=while_Var_strategy)
@settings(max_examples=50)
def test_while_var_instantiation(instance):
    assert isinstance(instance, while_Var)



@given(instance=while_Var_strategy)
def test_while_var_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=while_Statement_strategy)
@settings(max_examples=50)
def test_while_statement_instantiation(instance):
    assert isinstance(instance, while_Statement)

@given(instance=while_Program_strategy)
@settings(max_examples=50)
def test_while_program_instantiation(instance):
    assert isinstance(instance, while_Program)
