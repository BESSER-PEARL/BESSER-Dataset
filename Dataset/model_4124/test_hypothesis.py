import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    langage::while::ExprEq,
    langage::while::ExprAnd,
    langage::while::ExprSimple,
    langage::while::ExprNot,
    langage::while::ExprOr,
    langage::while::LExpr,
    langage::while::Foreach,
    langage::while::If,
    langage::while::For,
    langage::while::While,
    langage::while::Assign,
    langage::while::Command,
    langage::while::VAR,
    langage::while::Output,
    langage::while::Expr,
    langage::while::Exprs,
    langage::while::Vars,
    langage::while::Ifconfort,
    langage::while::Commands,
    langage::while::Input,
    langage::while::Definition,
    langage::while::SYMB,
    langage::while::Function,
    langage::while::Program,
    langage::while::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_langage::while::expreq_is_not_abstract():
    assert not inspect.isabstract(langage::while::ExprEq)


def test_langage::while::expreq_constructor_exists():
    assert callable(langage::while::ExprEq.__init__)


def test_langage::while::expreq_constructor_args():
    sig = inspect.signature(langage::while::ExprEq.__init__)
    params = list(sig.parameters.keys())



def test_langage::while::exprand_is_not_abstract():
    assert not inspect.isabstract(langage::while::ExprAnd)


def test_langage::while::exprand_constructor_exists():
    assert callable(langage::while::ExprAnd.__init__)


def test_langage::while::exprand_constructor_args():
    sig = inspect.signature(langage::while::ExprAnd.__init__)
    params = list(sig.parameters.keys())



def test_langage::while::exprsimple_is_not_abstract():
    assert not inspect.isabstract(langage::while::ExprSimple)


def test_langage::while::exprsimple_constructor_exists():
    assert callable(langage::while::ExprSimple.__init__)


def test_langage::while::exprsimple_constructor_args():
    sig = inspect.signature(langage::while::ExprSimple.__init__)
    params = list(sig.parameters.keys())
    assert "nil" in params, "Missing parameter 'nil'"
    assert "mot" in params, "Missing parameter 'mot'"

def test_langage::while::exprsimple_has_nil():
    assert hasattr(langage::while::ExprSimple, "nil")
    descriptor = None
    for klass in langage::while::ExprSimple.__mro__:
        if "nil" in klass.__dict__:
            descriptor = klass.__dict__["nil"]
            break
    assert isinstance(descriptor, property)

def test_langage::while::exprsimple_has_mot():
    assert hasattr(langage::while::ExprSimple, "mot")
    descriptor = None
    for klass in langage::while::ExprSimple.__mro__:
        if "mot" in klass.__dict__:
            descriptor = klass.__dict__["mot"]
            break
    assert isinstance(descriptor, property)



def test_langage::while::exprnot_is_not_abstract():
    assert not inspect.isabstract(langage::while::ExprNot)


def test_langage::while::exprnot_constructor_exists():
    assert callable(langage::while::ExprNot.__init__)


def test_langage::while::exprnot_constructor_args():
    sig = inspect.signature(langage::while::ExprNot.__init__)
    params = list(sig.parameters.keys())



def test_langage::while::expror_is_not_abstract():
    assert not inspect.isabstract(langage::while::ExprOr)


def test_langage::while::expror_constructor_exists():
    assert callable(langage::while::ExprOr.__init__)


def test_langage::while::expror_constructor_args():
    sig = inspect.signature(langage::while::ExprOr.__init__)
    params = list(sig.parameters.keys())



def test_langage::while::lexpr_is_not_abstract():
    assert not inspect.isabstract(langage::while::LExpr)


def test_langage::while::lexpr_constructor_exists():
    assert callable(langage::while::LExpr.__init__)


def test_langage::while::lexpr_constructor_args():
    sig = inspect.signature(langage::while::LExpr.__init__)
    params = list(sig.parameters.keys())



def test_langage::while::foreach_is_not_abstract():
    assert not inspect.isabstract(langage::while::Foreach)


def test_langage::while::foreach_constructor_exists():
    assert callable(langage::while::Foreach.__init__)


def test_langage::while::foreach_constructor_args():
    sig = inspect.signature(langage::while::Foreach.__init__)
    params = list(sig.parameters.keys())



def test_langage::while::if_is_not_abstract():
    assert not inspect.isabstract(langage::while::If)


def test_langage::while::if_constructor_exists():
    assert callable(langage::while::If.__init__)


def test_langage::while::if_constructor_args():
    sig = inspect.signature(langage::while::If.__init__)
    params = list(sig.parameters.keys())



def test_langage::while::for_is_not_abstract():
    assert not inspect.isabstract(langage::while::For)


def test_langage::while::for_constructor_exists():
    assert callable(langage::while::For.__init__)


def test_langage::while::for_constructor_args():
    sig = inspect.signature(langage::while::For.__init__)
    params = list(sig.parameters.keys())



def test_langage::while::while_is_not_abstract():
    assert not inspect.isabstract(langage::while::While)


def test_langage::while::while_constructor_exists():
    assert callable(langage::while::While.__init__)


def test_langage::while::while_constructor_args():
    sig = inspect.signature(langage::while::While.__init__)
    params = list(sig.parameters.keys())



def test_langage::while::assign_is_not_abstract():
    assert not inspect.isabstract(langage::while::Assign)


def test_langage::while::assign_constructor_exists():
    assert callable(langage::while::Assign.__init__)


def test_langage::while::assign_constructor_args():
    sig = inspect.signature(langage::while::Assign.__init__)
    params = list(sig.parameters.keys())



def test_langage::while::command_is_not_abstract():
    assert not inspect.isabstract(langage::while::Command)


def test_langage::while::command_constructor_exists():
    assert callable(langage::while::Command.__init__)


def test_langage::while::command_constructor_args():
    sig = inspect.signature(langage::while::Command.__init__)
    params = list(sig.parameters.keys())
    assert "nop" in params, "Missing parameter 'nop'"

def test_langage::while::command_has_nop():
    assert hasattr(langage::while::Command, "nop")
    descriptor = None
    for klass in langage::while::Command.__mro__:
        if "nop" in klass.__dict__:
            descriptor = klass.__dict__["nop"]
            break
    assert isinstance(descriptor, property)



def test_langage::while::var_is_not_abstract():
    assert not inspect.isabstract(langage::while::VAR)


def test_langage::while::var_constructor_exists():
    assert callable(langage::while::VAR.__init__)


def test_langage::while::var_constructor_args():
    sig = inspect.signature(langage::while::VAR.__init__)
    params = list(sig.parameters.keys())
    assert "bv" in params, "Missing parameter 'bv'"
    assert "cf" in params, "Missing parameter 'cf'"

def test_langage::while::var_has_bv():
    assert hasattr(langage::while::VAR, "bv")
    descriptor = None
    for klass in langage::while::VAR.__mro__:
        if "bv" in klass.__dict__:
            descriptor = klass.__dict__["bv"]
            break
    assert isinstance(descriptor, property)

def test_langage::while::var_has_cf():
    assert hasattr(langage::while::VAR, "cf")
    descriptor = None
    for klass in langage::while::VAR.__mro__:
        if "cf" in klass.__dict__:
            descriptor = klass.__dict__["cf"]
            break
    assert isinstance(descriptor, property)



def test_langage::while::output_is_not_abstract():
    assert not inspect.isabstract(langage::while::Output)


def test_langage::while::output_constructor_exists():
    assert callable(langage::while::Output.__init__)


def test_langage::while::output_constructor_args():
    sig = inspect.signature(langage::while::Output.__init__)
    params = list(sig.parameters.keys())



def test_langage::while::expr_is_not_abstract():
    assert not inspect.isabstract(langage::while::Expr)


def test_langage::while::expr_constructor_exists():
    assert callable(langage::while::Expr.__init__)


def test_langage::while::expr_constructor_args():
    sig = inspect.signature(langage::while::Expr.__init__)
    params = list(sig.parameters.keys())



def test_langage::while::exprs_is_not_abstract():
    assert not inspect.isabstract(langage::while::Exprs)


def test_langage::while::exprs_constructor_exists():
    assert callable(langage::while::Exprs.__init__)


def test_langage::while::exprs_constructor_args():
    sig = inspect.signature(langage::while::Exprs.__init__)
    params = list(sig.parameters.keys())



def test_langage::while::vars_is_not_abstract():
    assert not inspect.isabstract(langage::while::Vars)


def test_langage::while::vars_constructor_exists():
    assert callable(langage::while::Vars.__init__)


def test_langage::while::vars_constructor_args():
    sig = inspect.signature(langage::while::Vars.__init__)
    params = list(sig.parameters.keys())



def test_langage::while::ifconfort_is_not_abstract():
    assert not inspect.isabstract(langage::while::Ifconfort)


def test_langage::while::ifconfort_constructor_exists():
    assert callable(langage::while::Ifconfort.__init__)


def test_langage::while::ifconfort_constructor_args():
    sig = inspect.signature(langage::while::Ifconfort.__init__)
    params = list(sig.parameters.keys())



def test_langage::while::commands_is_not_abstract():
    assert not inspect.isabstract(langage::while::Commands)


def test_langage::while::commands_constructor_exists():
    assert callable(langage::while::Commands.__init__)


def test_langage::while::commands_constructor_args():
    sig = inspect.signature(langage::while::Commands.__init__)
    params = list(sig.parameters.keys())



def test_langage::while::input_is_not_abstract():
    assert not inspect.isabstract(langage::while::Input)


def test_langage::while::input_constructor_exists():
    assert callable(langage::while::Input.__init__)


def test_langage::while::input_constructor_args():
    sig = inspect.signature(langage::while::Input.__init__)
    params = list(sig.parameters.keys())



def test_langage::while::definition_is_not_abstract():
    assert not inspect.isabstract(langage::while::Definition)


def test_langage::while::definition_constructor_exists():
    assert callable(langage::while::Definition.__init__)


def test_langage::while::definition_constructor_args():
    sig = inspect.signature(langage::while::Definition.__init__)
    params = list(sig.parameters.keys())



def test_langage::while::symb_is_not_abstract():
    assert not inspect.isabstract(langage::while::SYMB)


def test_langage::while::symb_constructor_exists():
    assert callable(langage::while::SYMB.__init__)


def test_langage::while::symb_constructor_args():
    sig = inspect.signature(langage::while::SYMB.__init__)
    params = list(sig.parameters.keys())
    assert "bs" in params, "Missing parameter 'bs'"
    assert "cf" in params, "Missing parameter 'cf'"

def test_langage::while::symb_has_bs():
    assert hasattr(langage::while::SYMB, "bs")
    descriptor = None
    for klass in langage::while::SYMB.__mro__:
        if "bs" in klass.__dict__:
            descriptor = klass.__dict__["bs"]
            break
    assert isinstance(descriptor, property)

def test_langage::while::symb_has_cf():
    assert hasattr(langage::while::SYMB, "cf")
    descriptor = None
    for klass in langage::while::SYMB.__mro__:
        if "cf" in klass.__dict__:
            descriptor = klass.__dict__["cf"]
            break
    assert isinstance(descriptor, property)



def test_langage::while::function_is_not_abstract():
    assert not inspect.isabstract(langage::while::Function)


def test_langage::while::function_constructor_exists():
    assert callable(langage::while::Function.__init__)


def test_langage::while::function_constructor_args():
    sig = inspect.signature(langage::while::Function.__init__)
    params = list(sig.parameters.keys())



def test_langage::while::program_is_not_abstract():
    assert not inspect.isabstract(langage::while::Program)


def test_langage::while::program_constructor_exists():
    assert callable(langage::while::Program.__init__)


def test_langage::while::program_constructor_args():
    sig = inspect.signature(langage::while::Program.__init__)
    params = list(sig.parameters.keys())
    assert "u" in params, "Missing parameter 'u'"

def test_langage::while::program_has_u():
    assert hasattr(langage::while::Program, "u")
    descriptor = None
    for klass in langage::while::Program.__mro__:
        if "u" in klass.__dict__:
            descriptor = klass.__dict__["u"]
            break
    assert isinstance(descriptor, property)



def test_langage::while::model_is_not_abstract():
    assert not inspect.isabstract(langage::while::Model)


def test_langage::while::model_constructor_exists():
    assert callable(langage::while::Model.__init__)


def test_langage::while::model_constructor_args():
    sig = inspect.signature(langage::while::Model.__init__)
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
langage::while::ExprEq_strategy = st.builds(
    langage::while::ExprEq,
)
langage::while::ExprAnd_strategy = st.builds(
    langage::while::ExprAnd,
)
langage::while::ExprSimple_strategy = st.builds(
    langage::while::ExprSimple,
    nil=
        safe_text,
    mot=
        safe_text
)
langage::while::ExprNot_strategy = st.builds(
    langage::while::ExprNot,
)
langage::while::ExprOr_strategy = st.builds(
    langage::while::ExprOr,
)
langage::while::LExpr_strategy = st.builds(
    langage::while::LExpr,
)
langage::while::Foreach_strategy = st.builds(
    langage::while::Foreach,
)
langage::while::If_strategy = st.builds(
    langage::while::If,
)
langage::while::For_strategy = st.builds(
    langage::while::For,
)
langage::while::While_strategy = st.builds(
    langage::while::While,
)
langage::while::Assign_strategy = st.builds(
    langage::while::Assign,
)
langage::while::Command_strategy = st.builds(
    langage::while::Command,
    nop=
        safe_text
)
langage::while::VAR_strategy = st.builds(
    langage::while::VAR,
    bv=
        safe_text,
    cf=
        safe_text
)
langage::while::Output_strategy = st.builds(
    langage::while::Output,
)
langage::while::Expr_strategy = st.builds(
    langage::while::Expr,
)
langage::while::Exprs_strategy = st.builds(
    langage::while::Exprs,
)
langage::while::Vars_strategy = st.builds(
    langage::while::Vars,
)
langage::while::Ifconfort_strategy = st.builds(
    langage::while::Ifconfort,
)
langage::while::Commands_strategy = st.builds(
    langage::while::Commands,
)
langage::while::Input_strategy = st.builds(
    langage::while::Input,
)
langage::while::Definition_strategy = st.builds(
    langage::while::Definition,
)
langage::while::SYMB_strategy = st.builds(
    langage::while::SYMB,
    bs=
        safe_text,
    cf=
        safe_text
)
langage::while::Function_strategy = st.builds(
    langage::while::Function,
)
langage::while::Program_strategy = st.builds(
    langage::while::Program,
    u=
        safe_text
)
langage::while::Model_strategy = st.builds(
    langage::while::Model,
)

@given(instance=langage::while::ExprEq_strategy)
@settings(max_examples=50)
def test_langage::while::expreq_instantiation(instance):
    assert isinstance(instance, langage::while::ExprEq)

@given(instance=langage::while::ExprAnd_strategy)
@settings(max_examples=50)
def test_langage::while::exprand_instantiation(instance):
    assert isinstance(instance, langage::while::ExprAnd)

@given(instance=langage::while::ExprSimple_strategy)
@settings(max_examples=50)
def test_langage::while::exprsimple_instantiation(instance):
    assert isinstance(instance, langage::while::ExprSimple)

@given(instance=langage::while::ExprSimple_strategy)
def test_langage::while::exprsimple_nil_type(instance):
    assert isinstance(instance.nil, str)


@given(instance=langage::while::ExprSimple_strategy)
def test_langage::while::exprsimple_nil_setter(instance):
    original = instance.nil
    instance.nil = original
    assert instance.nil == original

@given(instance=langage::while::ExprSimple_strategy)
def test_langage::while::exprsimple_mot_type(instance):
    assert isinstance(instance.mot, str)


@given(instance=langage::while::ExprSimple_strategy)
def test_langage::while::exprsimple_mot_setter(instance):
    original = instance.mot
    instance.mot = original
    assert instance.mot == original

@given(instance=langage::while::ExprNot_strategy)
@settings(max_examples=50)
def test_langage::while::exprnot_instantiation(instance):
    assert isinstance(instance, langage::while::ExprNot)

@given(instance=langage::while::ExprOr_strategy)
@settings(max_examples=50)
def test_langage::while::expror_instantiation(instance):
    assert isinstance(instance, langage::while::ExprOr)

@given(instance=langage::while::LExpr_strategy)
@settings(max_examples=50)
def test_langage::while::lexpr_instantiation(instance):
    assert isinstance(instance, langage::while::LExpr)

@given(instance=langage::while::Foreach_strategy)
@settings(max_examples=50)
def test_langage::while::foreach_instantiation(instance):
    assert isinstance(instance, langage::while::Foreach)

@given(instance=langage::while::If_strategy)
@settings(max_examples=50)
def test_langage::while::if_instantiation(instance):
    assert isinstance(instance, langage::while::If)

@given(instance=langage::while::For_strategy)
@settings(max_examples=50)
def test_langage::while::for_instantiation(instance):
    assert isinstance(instance, langage::while::For)

@given(instance=langage::while::While_strategy)
@settings(max_examples=50)
def test_langage::while::while_instantiation(instance):
    assert isinstance(instance, langage::while::While)

@given(instance=langage::while::Assign_strategy)
@settings(max_examples=50)
def test_langage::while::assign_instantiation(instance):
    assert isinstance(instance, langage::while::Assign)

@given(instance=langage::while::Command_strategy)
@settings(max_examples=50)
def test_langage::while::command_instantiation(instance):
    assert isinstance(instance, langage::while::Command)

@given(instance=langage::while::Command_strategy)
def test_langage::while::command_nop_type(instance):
    assert isinstance(instance.nop, str)


@given(instance=langage::while::Command_strategy)
def test_langage::while::command_nop_setter(instance):
    original = instance.nop
    instance.nop = original
    assert instance.nop == original

@given(instance=langage::while::VAR_strategy)
@settings(max_examples=50)
def test_langage::while::var_instantiation(instance):
    assert isinstance(instance, langage::while::VAR)

@given(instance=langage::while::VAR_strategy)
def test_langage::while::var_bv_type(instance):
    assert isinstance(instance.bv, str)


@given(instance=langage::while::VAR_strategy)
def test_langage::while::var_bv_setter(instance):
    original = instance.bv
    instance.bv = original
    assert instance.bv == original

@given(instance=langage::while::VAR_strategy)
def test_langage::while::var_cf_type(instance):
    assert isinstance(instance.cf, str)


@given(instance=langage::while::VAR_strategy)
def test_langage::while::var_cf_setter(instance):
    original = instance.cf
    instance.cf = original
    assert instance.cf == original

@given(instance=langage::while::Output_strategy)
@settings(max_examples=50)
def test_langage::while::output_instantiation(instance):
    assert isinstance(instance, langage::while::Output)

@given(instance=langage::while::Expr_strategy)
@settings(max_examples=50)
def test_langage::while::expr_instantiation(instance):
    assert isinstance(instance, langage::while::Expr)

@given(instance=langage::while::Exprs_strategy)
@settings(max_examples=50)
def test_langage::while::exprs_instantiation(instance):
    assert isinstance(instance, langage::while::Exprs)

@given(instance=langage::while::Vars_strategy)
@settings(max_examples=50)
def test_langage::while::vars_instantiation(instance):
    assert isinstance(instance, langage::while::Vars)

@given(instance=langage::while::Ifconfort_strategy)
@settings(max_examples=50)
def test_langage::while::ifconfort_instantiation(instance):
    assert isinstance(instance, langage::while::Ifconfort)

@given(instance=langage::while::Commands_strategy)
@settings(max_examples=50)
def test_langage::while::commands_instantiation(instance):
    assert isinstance(instance, langage::while::Commands)

@given(instance=langage::while::Input_strategy)
@settings(max_examples=50)
def test_langage::while::input_instantiation(instance):
    assert isinstance(instance, langage::while::Input)

@given(instance=langage::while::Definition_strategy)
@settings(max_examples=50)
def test_langage::while::definition_instantiation(instance):
    assert isinstance(instance, langage::while::Definition)

@given(instance=langage::while::SYMB_strategy)
@settings(max_examples=50)
def test_langage::while::symb_instantiation(instance):
    assert isinstance(instance, langage::while::SYMB)

@given(instance=langage::while::SYMB_strategy)
def test_langage::while::symb_bs_type(instance):
    assert isinstance(instance.bs, str)


@given(instance=langage::while::SYMB_strategy)
def test_langage::while::symb_bs_setter(instance):
    original = instance.bs
    instance.bs = original
    assert instance.bs == original

@given(instance=langage::while::SYMB_strategy)
def test_langage::while::symb_cf_type(instance):
    assert isinstance(instance.cf, str)


@given(instance=langage::while::SYMB_strategy)
def test_langage::while::symb_cf_setter(instance):
    original = instance.cf
    instance.cf = original
    assert instance.cf == original

@given(instance=langage::while::Function_strategy)
@settings(max_examples=50)
def test_langage::while::function_instantiation(instance):
    assert isinstance(instance, langage::while::Function)

@given(instance=langage::while::Program_strategy)
@settings(max_examples=50)
def test_langage::while::program_instantiation(instance):
    assert isinstance(instance, langage::while::Program)

@given(instance=langage::while::Program_strategy)
def test_langage::while::program_u_type(instance):
    assert isinstance(instance.u, str)


@given(instance=langage::while::Program_strategy)
def test_langage::while::program_u_setter(instance):
    original = instance.u
    instance.u = original
    assert instance.u == original

@given(instance=langage::while::Model_strategy)
@settings(max_examples=50)
def test_langage::while::model_instantiation(instance):
    assert isinstance(instance, langage::while::Model)
