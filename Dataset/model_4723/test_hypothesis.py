import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    simpliC::Factor,
    simpliC::TFact,
    simpliC::EObject,
    Stmt,
    simpliC::Typedef,
    simpliC::Assign,
    simpliC::Block,
    simpliC::Args,
    simpliC::Decl,
    simpliC::Return,
    simpliC::Whilestmt,
    simpliC::Ifstmt,
    Factor,
    simpliC::IDuse,
    simpliC::ExprCall,
    simpliC::Expr,
    simpliC::Call,
    simpliC::Stmt,
    simpliC::Type,
    simpliC::Function,
    simpliC::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_simplic::factor_is_not_abstract():
    assert not inspect.isabstract(simpliC::Factor)


def test_simplic::factor_constructor_exists():
    assert callable(simpliC::Factor.__init__)


def test_simplic::factor_constructor_args():
    sig = inspect.signature(simpliC::Factor.__init__)
    params = list(sig.parameters.keys())



def test_simplic::tfact_is_not_abstract():
    assert not inspect.isabstract(simpliC::TFact)


def test_simplic::tfact_constructor_exists():
    assert callable(simpliC::TFact.__init__)


def test_simplic::tfact_constructor_args():
    sig = inspect.signature(simpliC::TFact.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_simplic::tfact_has_op():
    assert hasattr(simpliC::TFact, "op")
    descriptor = None
    for klass in simpliC::TFact.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_simplic::eobject_is_not_abstract():
    assert not inspect.isabstract(simpliC::EObject)


def test_simplic::eobject_constructor_exists():
    assert callable(simpliC::EObject.__init__)


def test_simplic::eobject_constructor_args():
    sig = inspect.signature(simpliC::EObject.__init__)
    params = list(sig.parameters.keys())



def test_stmt_is_not_abstract():
    assert not inspect.isabstract(Stmt)


def test_stmt_constructor_exists():
    assert callable(Stmt.__init__)


def test_stmt_constructor_args():
    sig = inspect.signature(Stmt.__init__)
    params = list(sig.parameters.keys())



def test_simplic::typedef_is_not_abstract():
    assert not inspect.isabstract(simpliC::Typedef)


def test_simplic::typedef_constructor_exists():
    assert callable(simpliC::Typedef.__init__)


def test_simplic::typedef_constructor_args():
    sig = inspect.signature(simpliC::Typedef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplic::typedef_has_name():
    assert hasattr(simpliC::Typedef, "name")
    descriptor = None
    for klass in simpliC::Typedef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplic::assign_is_not_abstract():
    assert not inspect.isabstract(simpliC::Assign)


def test_simplic::assign_constructor_exists():
    assert callable(simpliC::Assign.__init__)


def test_simplic::assign_constructor_args():
    sig = inspect.signature(simpliC::Assign.__init__)
    params = list(sig.parameters.keys())
    assert "var" in params, "Missing parameter 'var'"

def test_simplic::assign_has_var():
    assert hasattr(simpliC::Assign, "var")
    descriptor = None
    for klass in simpliC::Assign.__mro__:
        if "var" in klass.__dict__:
            descriptor = klass.__dict__["var"]
            break
    assert isinstance(descriptor, property)



def test_simplic::block_is_not_abstract():
    assert not inspect.isabstract(simpliC::Block)


def test_simplic::block_constructor_exists():
    assert callable(simpliC::Block.__init__)


def test_simplic::block_constructor_args():
    sig = inspect.signature(simpliC::Block.__init__)
    params = list(sig.parameters.keys())



def test_simplic::args_is_not_abstract():
    assert not inspect.isabstract(simpliC::Args)


def test_simplic::args_constructor_exists():
    assert callable(simpliC::Args.__init__)


def test_simplic::args_constructor_args():
    sig = inspect.signature(simpliC::Args.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplic::args_has_name():
    assert hasattr(simpliC::Args, "name")
    descriptor = None
    for klass in simpliC::Args.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplic::decl_is_not_abstract():
    assert not inspect.isabstract(simpliC::Decl)


def test_simplic::decl_constructor_exists():
    assert callable(simpliC::Decl.__init__)


def test_simplic::decl_constructor_args():
    sig = inspect.signature(simpliC::Decl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplic::decl_has_name():
    assert hasattr(simpliC::Decl, "name")
    descriptor = None
    for klass in simpliC::Decl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplic::return_is_not_abstract():
    assert not inspect.isabstract(simpliC::Return)


def test_simplic::return_constructor_exists():
    assert callable(simpliC::Return.__init__)


def test_simplic::return_constructor_args():
    sig = inspect.signature(simpliC::Return.__init__)
    params = list(sig.parameters.keys())



def test_simplic::whilestmt_is_not_abstract():
    assert not inspect.isabstract(simpliC::Whilestmt)


def test_simplic::whilestmt_constructor_exists():
    assert callable(simpliC::Whilestmt.__init__)


def test_simplic::whilestmt_constructor_args():
    sig = inspect.signature(simpliC::Whilestmt.__init__)
    params = list(sig.parameters.keys())



def test_simplic::ifstmt_is_not_abstract():
    assert not inspect.isabstract(simpliC::Ifstmt)


def test_simplic::ifstmt_constructor_exists():
    assert callable(simpliC::Ifstmt.__init__)


def test_simplic::ifstmt_constructor_args():
    sig = inspect.signature(simpliC::Ifstmt.__init__)
    params = list(sig.parameters.keys())



def test_factor_is_not_abstract():
    assert not inspect.isabstract(Factor)


def test_factor_constructor_exists():
    assert callable(Factor.__init__)


def test_factor_constructor_args():
    sig = inspect.signature(Factor.__init__)
    params = list(sig.parameters.keys())



def test_simplic::iduse_is_not_abstract():
    assert not inspect.isabstract(simpliC::IDuse)


def test_simplic::iduse_constructor_exists():
    assert callable(simpliC::IDuse.__init__)


def test_simplic::iduse_constructor_args():
    sig = inspect.signature(simpliC::IDuse.__init__)
    params = list(sig.parameters.keys())



def test_simplic::exprcall_is_not_abstract():
    assert not inspect.isabstract(simpliC::ExprCall)


def test_simplic::exprcall_constructor_exists():
    assert callable(simpliC::ExprCall.__init__)


def test_simplic::exprcall_constructor_args():
    sig = inspect.signature(simpliC::ExprCall.__init__)
    params = list(sig.parameters.keys())



def test_simplic::expr_is_not_abstract():
    assert not inspect.isabstract(simpliC::Expr)


def test_simplic::expr_constructor_exists():
    assert callable(simpliC::Expr.__init__)


def test_simplic::expr_constructor_args():
    sig = inspect.signature(simpliC::Expr.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_simplic::expr_has_op():
    assert hasattr(simpliC::Expr, "op")
    descriptor = None
    for klass in simpliC::Expr.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_simplic::call_is_not_abstract():
    assert not inspect.isabstract(simpliC::Call)


def test_simplic::call_constructor_exists():
    assert callable(simpliC::Call.__init__)


def test_simplic::call_constructor_args():
    sig = inspect.signature(simpliC::Call.__init__)
    params = list(sig.parameters.keys())



def test_simplic::stmt_is_not_abstract():
    assert not inspect.isabstract(simpliC::Stmt)


def test_simplic::stmt_constructor_exists():
    assert callable(simpliC::Stmt.__init__)


def test_simplic::stmt_constructor_args():
    sig = inspect.signature(simpliC::Stmt.__init__)
    params = list(sig.parameters.keys())



def test_simplic::type_is_not_abstract():
    assert not inspect.isabstract(simpliC::Type)


def test_simplic::type_constructor_exists():
    assert callable(simpliC::Type.__init__)


def test_simplic::type_constructor_args():
    sig = inspect.signature(simpliC::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplic::type_has_name():
    assert hasattr(simpliC::Type, "name")
    descriptor = None
    for klass in simpliC::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplic::function_is_not_abstract():
    assert not inspect.isabstract(simpliC::Function)


def test_simplic::function_constructor_exists():
    assert callable(simpliC::Function.__init__)


def test_simplic::function_constructor_args():
    sig = inspect.signature(simpliC::Function.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_simplic::function_has_name():
    assert hasattr(simpliC::Function, "name")
    descriptor = None
    for klass in simpliC::Function.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simplic::model_is_not_abstract():
    assert not inspect.isabstract(simpliC::Model)


def test_simplic::model_constructor_exists():
    assert callable(simpliC::Model.__init__)


def test_simplic::model_constructor_args():
    sig = inspect.signature(simpliC::Model.__init__)
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
simpliC::Factor_strategy = st.builds(
    simpliC::Factor,
)
simpliC::TFact_strategy = st.builds(
    simpliC::TFact,
    op=
        safe_text
)
simpliC::EObject_strategy = st.builds(
    simpliC::EObject,
)
Stmt_strategy = st.builds(
    Stmt,
)
simpliC::Typedef_strategy = st.builds(
    simpliC::Typedef,
    name=
        safe_text
)
simpliC::Assign_strategy = st.builds(
    simpliC::Assign,
    var=
        safe_text
)
simpliC::Block_strategy = st.builds(
    simpliC::Block,
)
simpliC::Args_strategy = st.builds(
    simpliC::Args,
    name=
        safe_text
)
simpliC::Decl_strategy = st.builds(
    simpliC::Decl,
    name=
        safe_text
)
simpliC::Return_strategy = st.builds(
    simpliC::Return,
)
simpliC::Whilestmt_strategy = st.builds(
    simpliC::Whilestmt,
)
simpliC::Ifstmt_strategy = st.builds(
    simpliC::Ifstmt,
)
Factor_strategy = st.builds(
    Factor,
)
simpliC::IDuse_strategy = st.builds(
    simpliC::IDuse,
)
simpliC::ExprCall_strategy = st.builds(
    simpliC::ExprCall,
)
simpliC::Expr_strategy = st.builds(
    simpliC::Expr,
    op=
        safe_text
)
simpliC::Call_strategy = st.builds(
    simpliC::Call,
)
simpliC::Stmt_strategy = st.builds(
    simpliC::Stmt,
)
simpliC::Type_strategy = st.builds(
    simpliC::Type,
    name=
        safe_text
)
simpliC::Function_strategy = st.builds(
    simpliC::Function,
    name=
        safe_text
)
simpliC::Model_strategy = st.builds(
    simpliC::Model,
)

@given(instance=simpliC::Factor_strategy)
@settings(max_examples=50)
def test_simplic::factor_instantiation(instance):
    assert isinstance(instance, simpliC::Factor)

@given(instance=simpliC::TFact_strategy)
@settings(max_examples=50)
def test_simplic::tfact_instantiation(instance):
    assert isinstance(instance, simpliC::TFact)

@given(instance=simpliC::TFact_strategy)
def test_simplic::tfact_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=simpliC::TFact_strategy)
def test_simplic::tfact_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=simpliC::EObject_strategy)
@settings(max_examples=50)
def test_simplic::eobject_instantiation(instance):
    assert isinstance(instance, simpliC::EObject)

@given(instance=Stmt_strategy)
@settings(max_examples=50)
def test_stmt_instantiation(instance):
    assert isinstance(instance, Stmt)

@given(instance=simpliC::Typedef_strategy)
@settings(max_examples=50)
def test_simplic::typedef_instantiation(instance):
    assert isinstance(instance, simpliC::Typedef)

@given(instance=simpliC::Typedef_strategy)
def test_simplic::typedef_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpliC::Typedef_strategy)
def test_simplic::typedef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpliC::Assign_strategy)
@settings(max_examples=50)
def test_simplic::assign_instantiation(instance):
    assert isinstance(instance, simpliC::Assign)

@given(instance=simpliC::Assign_strategy)
def test_simplic::assign_var_type(instance):
    assert isinstance(instance.var, str)


@given(instance=simpliC::Assign_strategy)
def test_simplic::assign_var_setter(instance):
    original = instance.var
    instance.var = original
    assert instance.var == original

@given(instance=simpliC::Block_strategy)
@settings(max_examples=50)
def test_simplic::block_instantiation(instance):
    assert isinstance(instance, simpliC::Block)

@given(instance=simpliC::Args_strategy)
@settings(max_examples=50)
def test_simplic::args_instantiation(instance):
    assert isinstance(instance, simpliC::Args)

@given(instance=simpliC::Args_strategy)
def test_simplic::args_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpliC::Args_strategy)
def test_simplic::args_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpliC::Decl_strategy)
@settings(max_examples=50)
def test_simplic::decl_instantiation(instance):
    assert isinstance(instance, simpliC::Decl)

@given(instance=simpliC::Decl_strategy)
def test_simplic::decl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpliC::Decl_strategy)
def test_simplic::decl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpliC::Return_strategy)
@settings(max_examples=50)
def test_simplic::return_instantiation(instance):
    assert isinstance(instance, simpliC::Return)

@given(instance=simpliC::Whilestmt_strategy)
@settings(max_examples=50)
def test_simplic::whilestmt_instantiation(instance):
    assert isinstance(instance, simpliC::Whilestmt)

@given(instance=simpliC::Ifstmt_strategy)
@settings(max_examples=50)
def test_simplic::ifstmt_instantiation(instance):
    assert isinstance(instance, simpliC::Ifstmt)

@given(instance=Factor_strategy)
@settings(max_examples=50)
def test_factor_instantiation(instance):
    assert isinstance(instance, Factor)

@given(instance=simpliC::IDuse_strategy)
@settings(max_examples=50)
def test_simplic::iduse_instantiation(instance):
    assert isinstance(instance, simpliC::IDuse)

@given(instance=simpliC::ExprCall_strategy)
@settings(max_examples=50)
def test_simplic::exprcall_instantiation(instance):
    assert isinstance(instance, simpliC::ExprCall)

@given(instance=simpliC::Expr_strategy)
@settings(max_examples=50)
def test_simplic::expr_instantiation(instance):
    assert isinstance(instance, simpliC::Expr)

@given(instance=simpliC::Expr_strategy)
def test_simplic::expr_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=simpliC::Expr_strategy)
def test_simplic::expr_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=simpliC::Call_strategy)
@settings(max_examples=50)
def test_simplic::call_instantiation(instance):
    assert isinstance(instance, simpliC::Call)

@given(instance=simpliC::Stmt_strategy)
@settings(max_examples=50)
def test_simplic::stmt_instantiation(instance):
    assert isinstance(instance, simpliC::Stmt)

@given(instance=simpliC::Type_strategy)
@settings(max_examples=50)
def test_simplic::type_instantiation(instance):
    assert isinstance(instance, simpliC::Type)

@given(instance=simpliC::Type_strategy)
def test_simplic::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpliC::Type_strategy)
def test_simplic::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpliC::Function_strategy)
@settings(max_examples=50)
def test_simplic::function_instantiation(instance):
    assert isinstance(instance, simpliC::Function)

@given(instance=simpliC::Function_strategy)
def test_simplic::function_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=simpliC::Function_strategy)
def test_simplic::function_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=simpliC::Model_strategy)
@settings(max_examples=50)
def test_simplic::model_instantiation(instance):
    assert isinstance(instance, simpliC::Model)
