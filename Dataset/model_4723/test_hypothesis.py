import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    simpliC_Factor,
    simpliC_TFact,
    simpliC_EObject,
    Stmt,
    simpliC_Typedef,
    simpliC_Assign,
    simpliC_Block,
    simpliC_Args,
    simpliC_Decl,
    simpliC_Return,
    simpliC_Whilestmt,
    simpliC_Ifstmt,
    Factor,
    simpliC_IDuse,
    simpliC_ExprCall,
    simpliC_Expr,
    simpliC_Call,
    simpliC_Stmt,
    simpliC_Type,
    simpliC_Function,
    simpliC_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simplic_factor_is_not_abstract():
    assert not inspect.isabstract(simpliC_Factor)


def test_simplic_factor_constructor_exists():
    assert callable(simpliC_Factor.__init__)


def test_simplic_factor_constructor_args():
    sig = inspect.signature(simpliC_Factor.__init__)
    params = list(sig.parameters.keys())



def test_simplic_tfact_is_not_abstract():
    assert not inspect.isabstract(simpliC_TFact)


def test_simplic_tfact_constructor_exists():
    assert callable(simpliC_TFact.__init__)


def test_simplic_tfact_constructor_args():
    sig = inspect.signature(simpliC_TFact.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_simplic_tfact_has_op():
    assert hasattr(simpliC_TFact, "op")
    descriptor = None
    for klass in simpliC_TFact.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_simplic_eobject_is_not_abstract():
    assert not inspect.isabstract(simpliC_EObject)


def test_simplic_eobject_constructor_exists():
    assert callable(simpliC_EObject.__init__)


def test_simplic_eobject_constructor_args():
    sig = inspect.signature(simpliC_EObject.__init__)
    params = list(sig.parameters.keys())



def test_stmt_is_not_abstract():
    assert not inspect.isabstract(Stmt)


def test_stmt_constructor_exists():
    assert callable(Stmt.__init__)


def test_stmt_constructor_args():
    sig = inspect.signature(Stmt.__init__)
    params = list(sig.parameters.keys())



def test_simplic_typedef_is_not_abstract():
    assert not inspect.isabstract(simpliC_Typedef)


def test_simplic_typedef_constructor_exists():
    assert callable(simpliC_Typedef.__init__)


def test_simplic_typedef_constructor_args():
    sig = inspect.signature(simpliC_Typedef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplic_typedef_has_name():
    assert hasattr(simpliC_Typedef, "name")
    descriptor = None
    for klass in simpliC_Typedef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplic_assign_is_not_abstract():
    assert not inspect.isabstract(simpliC_Assign)


def test_simplic_assign_constructor_exists():
    assert callable(simpliC_Assign.__init__)


def test_simplic_assign_constructor_args():
    sig = inspect.signature(simpliC_Assign.__init__)
    params = list(sig.parameters.keys())
    assert "var" in params, "Missing parameter 'var'"

def test_simplic_assign_has_var():
    assert hasattr(simpliC_Assign, "var")
    descriptor = None
    for klass in simpliC_Assign.__mro__:
        if "var" in klass.__dict__:
            descriptor = klass.__dict__["var"]
            break
    assert isinstance(descriptor, property)



def test_simplic_block_is_not_abstract():
    assert not inspect.isabstract(simpliC_Block)


def test_simplic_block_constructor_exists():
    assert callable(simpliC_Block.__init__)


def test_simplic_block_constructor_args():
    sig = inspect.signature(simpliC_Block.__init__)
    params = list(sig.parameters.keys())



def test_simplic_args_is_not_abstract():
    assert not inspect.isabstract(simpliC_Args)


def test_simplic_args_constructor_exists():
    assert callable(simpliC_Args.__init__)


def test_simplic_args_constructor_args():
    sig = inspect.signature(simpliC_Args.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplic_args_has_name():
    assert hasattr(simpliC_Args, "name")
    descriptor = None
    for klass in simpliC_Args.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplic_decl_is_not_abstract():
    assert not inspect.isabstract(simpliC_Decl)


def test_simplic_decl_constructor_exists():
    assert callable(simpliC_Decl.__init__)


def test_simplic_decl_constructor_args():
    sig = inspect.signature(simpliC_Decl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplic_decl_has_name():
    assert hasattr(simpliC_Decl, "name")
    descriptor = None
    for klass in simpliC_Decl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplic_return_is_not_abstract():
    assert not inspect.isabstract(simpliC_Return)


def test_simplic_return_constructor_exists():
    assert callable(simpliC_Return.__init__)


def test_simplic_return_constructor_args():
    sig = inspect.signature(simpliC_Return.__init__)
    params = list(sig.parameters.keys())



def test_simplic_whilestmt_is_not_abstract():
    assert not inspect.isabstract(simpliC_Whilestmt)


def test_simplic_whilestmt_constructor_exists():
    assert callable(simpliC_Whilestmt.__init__)


def test_simplic_whilestmt_constructor_args():
    sig = inspect.signature(simpliC_Whilestmt.__init__)
    params = list(sig.parameters.keys())



def test_simplic_ifstmt_is_not_abstract():
    assert not inspect.isabstract(simpliC_Ifstmt)


def test_simplic_ifstmt_constructor_exists():
    assert callable(simpliC_Ifstmt.__init__)


def test_simplic_ifstmt_constructor_args():
    sig = inspect.signature(simpliC_Ifstmt.__init__)
    params = list(sig.parameters.keys())



def test_factor_is_not_abstract():
    assert not inspect.isabstract(Factor)


def test_factor_constructor_exists():
    assert callable(Factor.__init__)


def test_factor_constructor_args():
    sig = inspect.signature(Factor.__init__)
    params = list(sig.parameters.keys())



def test_simplic_iduse_is_not_abstract():
    assert not inspect.isabstract(simpliC_IDuse)


def test_simplic_iduse_constructor_exists():
    assert callable(simpliC_IDuse.__init__)


def test_simplic_iduse_constructor_args():
    sig = inspect.signature(simpliC_IDuse.__init__)
    params = list(sig.parameters.keys())



def test_simplic_exprcall_is_not_abstract():
    assert not inspect.isabstract(simpliC_ExprCall)


def test_simplic_exprcall_constructor_exists():
    assert callable(simpliC_ExprCall.__init__)


def test_simplic_exprcall_constructor_args():
    sig = inspect.signature(simpliC_ExprCall.__init__)
    params = list(sig.parameters.keys())



def test_simplic_expr_is_not_abstract():
    assert not inspect.isabstract(simpliC_Expr)


def test_simplic_expr_constructor_exists():
    assert callable(simpliC_Expr.__init__)


def test_simplic_expr_constructor_args():
    sig = inspect.signature(simpliC_Expr.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_simplic_expr_has_op():
    assert hasattr(simpliC_Expr, "op")
    descriptor = None
    for klass in simpliC_Expr.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_simplic_call_is_not_abstract():
    assert not inspect.isabstract(simpliC_Call)


def test_simplic_call_constructor_exists():
    assert callable(simpliC_Call.__init__)


def test_simplic_call_constructor_args():
    sig = inspect.signature(simpliC_Call.__init__)
    params = list(sig.parameters.keys())



def test_simplic_stmt_is_not_abstract():
    assert not inspect.isabstract(simpliC_Stmt)


def test_simplic_stmt_constructor_exists():
    assert callable(simpliC_Stmt.__init__)


def test_simplic_stmt_constructor_args():
    sig = inspect.signature(simpliC_Stmt.__init__)
    params = list(sig.parameters.keys())



def test_simplic_type_is_not_abstract():
    assert not inspect.isabstract(simpliC_Type)


def test_simplic_type_constructor_exists():
    assert callable(simpliC_Type.__init__)


def test_simplic_type_constructor_args():
    sig = inspect.signature(simpliC_Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplic_type_has_name():
    assert hasattr(simpliC_Type, "name")
    descriptor = None
    for klass in simpliC_Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplic_function_is_not_abstract():
    assert not inspect.isabstract(simpliC_Function)


def test_simplic_function_constructor_exists():
    assert callable(simpliC_Function.__init__)


def test_simplic_function_constructor_args():
    sig = inspect.signature(simpliC_Function.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplic_function_has_name():
    assert hasattr(simpliC_Function, "name")
    descriptor = None
    for klass in simpliC_Function.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplic_model_is_not_abstract():
    assert not inspect.isabstract(simpliC_Model)


def test_simplic_model_constructor_exists():
    assert callable(simpliC_Model.__init__)


def test_simplic_model_constructor_args():
    sig = inspect.signature(simpliC_Model.__init__)
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
simpliC_Factor_strategy = st.builds(
    simpliC_Factor,
)
simpliC_TFact_strategy = st.builds(
    simpliC_TFact,
    op=
        safe_text
)
simpliC_EObject_strategy = st.builds(
    simpliC_EObject,
)
Stmt_strategy = st.builds(
    Stmt,
)
simpliC_Typedef_strategy = st.builds(
    simpliC_Typedef,
    name=
        safe_text
)
simpliC_Assign_strategy = st.builds(
    simpliC_Assign,
    var=
        safe_text
)
simpliC_Block_strategy = st.builds(
    simpliC_Block,
)
simpliC_Args_strategy = st.builds(
    simpliC_Args,
    name=
        safe_text
)
simpliC_Decl_strategy = st.builds(
    simpliC_Decl,
    name=
        safe_text
)
simpliC_Return_strategy = st.builds(
    simpliC_Return,
)
simpliC_Whilestmt_strategy = st.builds(
    simpliC_Whilestmt,
)
simpliC_Ifstmt_strategy = st.builds(
    simpliC_Ifstmt,
)
Factor_strategy = st.builds(
    Factor,
)
simpliC_IDuse_strategy = st.builds(
    simpliC_IDuse,
)
simpliC_ExprCall_strategy = st.builds(
    simpliC_ExprCall,
)
simpliC_Expr_strategy = st.builds(
    simpliC_Expr,
    op=
        safe_text
)
simpliC_Call_strategy = st.builds(
    simpliC_Call,
)
simpliC_Stmt_strategy = st.builds(
    simpliC_Stmt,
)
simpliC_Type_strategy = st.builds(
    simpliC_Type,
    name=
        safe_text
)
simpliC_Function_strategy = st.builds(
    simpliC_Function,
    name=
        safe_text
)
simpliC_Model_strategy = st.builds(
    simpliC_Model,
)

@given(instance=simpliC_Factor_strategy)
@settings(max_examples=50)
def test_simplic_factor_instantiation(instance):
    assert isinstance(instance, simpliC_Factor)

@given(instance=simpliC_TFact_strategy)
@settings(max_examples=50)
def test_simplic_tfact_instantiation(instance):
    assert isinstance(instance, simpliC_TFact)



@given(instance=simpliC_TFact_strategy)
def test_simplic_tfact_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=simpliC_EObject_strategy)
@settings(max_examples=50)
def test_simplic_eobject_instantiation(instance):
    assert isinstance(instance, simpliC_EObject)

@given(instance=Stmt_strategy)
@settings(max_examples=50)
def test_stmt_instantiation(instance):
    assert isinstance(instance, Stmt)

@given(instance=simpliC_Typedef_strategy)
@settings(max_examples=50)
def test_simplic_typedef_instantiation(instance):
    assert isinstance(instance, simpliC_Typedef)



@given(instance=simpliC_Typedef_strategy)
def test_simplic_typedef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpliC_Assign_strategy)
@settings(max_examples=50)
def test_simplic_assign_instantiation(instance):
    assert isinstance(instance, simpliC_Assign)



@given(instance=simpliC_Assign_strategy)
def test_simplic_assign_var_setter(instance):
    original = instance.var
    instance.var = original
    assert instance.var == original

@given(instance=simpliC_Block_strategy)
@settings(max_examples=50)
def test_simplic_block_instantiation(instance):
    assert isinstance(instance, simpliC_Block)

@given(instance=simpliC_Args_strategy)
@settings(max_examples=50)
def test_simplic_args_instantiation(instance):
    assert isinstance(instance, simpliC_Args)



@given(instance=simpliC_Args_strategy)
def test_simplic_args_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpliC_Decl_strategy)
@settings(max_examples=50)
def test_simplic_decl_instantiation(instance):
    assert isinstance(instance, simpliC_Decl)



@given(instance=simpliC_Decl_strategy)
def test_simplic_decl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpliC_Return_strategy)
@settings(max_examples=50)
def test_simplic_return_instantiation(instance):
    assert isinstance(instance, simpliC_Return)

@given(instance=simpliC_Whilestmt_strategy)
@settings(max_examples=50)
def test_simplic_whilestmt_instantiation(instance):
    assert isinstance(instance, simpliC_Whilestmt)

@given(instance=simpliC_Ifstmt_strategy)
@settings(max_examples=50)
def test_simplic_ifstmt_instantiation(instance):
    assert isinstance(instance, simpliC_Ifstmt)

@given(instance=Factor_strategy)
@settings(max_examples=50)
def test_factor_instantiation(instance):
    assert isinstance(instance, Factor)

@given(instance=simpliC_IDuse_strategy)
@settings(max_examples=50)
def test_simplic_iduse_instantiation(instance):
    assert isinstance(instance, simpliC_IDuse)

@given(instance=simpliC_ExprCall_strategy)
@settings(max_examples=50)
def test_simplic_exprcall_instantiation(instance):
    assert isinstance(instance, simpliC_ExprCall)

@given(instance=simpliC_Expr_strategy)
@settings(max_examples=50)
def test_simplic_expr_instantiation(instance):
    assert isinstance(instance, simpliC_Expr)



@given(instance=simpliC_Expr_strategy)
def test_simplic_expr_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=simpliC_Call_strategy)
@settings(max_examples=50)
def test_simplic_call_instantiation(instance):
    assert isinstance(instance, simpliC_Call)

@given(instance=simpliC_Stmt_strategy)
@settings(max_examples=50)
def test_simplic_stmt_instantiation(instance):
    assert isinstance(instance, simpliC_Stmt)

@given(instance=simpliC_Type_strategy)
@settings(max_examples=50)
def test_simplic_type_instantiation(instance):
    assert isinstance(instance, simpliC_Type)



@given(instance=simpliC_Type_strategy)
def test_simplic_type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpliC_Function_strategy)
@settings(max_examples=50)
def test_simplic_function_instantiation(instance):
    assert isinstance(instance, simpliC_Function)



@given(instance=simpliC_Function_strategy)
def test_simplic_function_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpliC_Model_strategy)
@settings(max_examples=50)
def test_simplic_model_instantiation(instance):
    assert isinstance(instance, simpliC_Model)
