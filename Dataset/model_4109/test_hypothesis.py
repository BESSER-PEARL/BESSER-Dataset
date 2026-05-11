import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    wh::ExprNot,
    wh::ExprOr,
    wh::ExprAnd,
    wh::ListExpr,
    wh::Cons,
    wh::ExprSimple,
    wh::ExprEq,
    wh::If,
    wh::While,
    wh::For,
    wh::Expr,
    wh::Foreach,
    wh::EObject,
    wh::Command,
    wh::Exprs,
    wh::Vars,
    wh::Affect,
    wh::Nop,
    wh::Definition,
    wh::Program,
    wh::Wh,
    wh::Output,
    wh::Commands,
    wh::Input,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_wh::exprnot_is_not_abstract():
    assert not inspect.isabstract(wh::ExprNot)


def test_wh::exprnot_constructor_exists():
    assert callable(wh::ExprNot.__init__)


def test_wh::exprnot_constructor_args():
    sig = inspect.signature(wh::ExprNot.__init__)
    params = list(sig.parameters.keys())
    assert "not_" in params, "Missing parameter 'not_'"

def test_wh::exprnot_has_not_():
    assert hasattr(wh::ExprNot, "not_")
    descriptor = None
    for klass in wh::ExprNot.__mro__:
        if "not_" in klass.__dict__:
            descriptor = klass.__dict__["not_"]
            break
    assert isinstance(descriptor, property)



def test_wh::expror_is_not_abstract():
    assert not inspect.isabstract(wh::ExprOr)


def test_wh::expror_constructor_exists():
    assert callable(wh::ExprOr.__init__)


def test_wh::expror_constructor_args():
    sig = inspect.signature(wh::ExprOr.__init__)
    params = list(sig.parameters.keys())



def test_wh::exprand_is_not_abstract():
    assert not inspect.isabstract(wh::ExprAnd)


def test_wh::exprand_constructor_exists():
    assert callable(wh::ExprAnd.__init__)


def test_wh::exprand_constructor_args():
    sig = inspect.signature(wh::ExprAnd.__init__)
    params = list(sig.parameters.keys())



def test_wh::listexpr_is_not_abstract():
    assert not inspect.isabstract(wh::ListExpr)


def test_wh::listexpr_constructor_exists():
    assert callable(wh::ListExpr.__init__)


def test_wh::listexpr_constructor_args():
    sig = inspect.signature(wh::ListExpr.__init__)
    params = list(sig.parameters.keys())



def test_wh::cons_is_not_abstract():
    assert not inspect.isabstract(wh::Cons)


def test_wh::cons_constructor_exists():
    assert callable(wh::Cons.__init__)


def test_wh::cons_constructor_args():
    sig = inspect.signature(wh::Cons.__init__)
    params = list(sig.parameters.keys())



def test_wh::exprsimple_is_not_abstract():
    assert not inspect.isabstract(wh::ExprSimple)


def test_wh::exprsimple_constructor_exists():
    assert callable(wh::ExprSimple.__init__)


def test_wh::exprsimple_constructor_args():
    sig = inspect.signature(wh::ExprSimple.__init__)
    params = list(sig.parameters.keys())
    assert "str" in params, "Missing parameter 'str'"
    assert "strSymb" in params, "Missing parameter 'strSymb'"

def test_wh::exprsimple_has_str():
    assert hasattr(wh::ExprSimple, "str")
    descriptor = None
    for klass in wh::ExprSimple.__mro__:
        if "str" in klass.__dict__:
            descriptor = klass.__dict__["str"]
            break
    assert isinstance(descriptor, property)

def test_wh::exprsimple_has_strSymb():
    assert hasattr(wh::ExprSimple, "strSymb")
    descriptor = None
    for klass in wh::ExprSimple.__mro__:
        if "strSymb" in klass.__dict__:
            descriptor = klass.__dict__["strSymb"]
            break
    assert isinstance(descriptor, property)



def test_wh::expreq_is_not_abstract():
    assert not inspect.isabstract(wh::ExprEq)


def test_wh::expreq_constructor_exists():
    assert callable(wh::ExprEq.__init__)


def test_wh::expreq_constructor_args():
    sig = inspect.signature(wh::ExprEq.__init__)
    params = list(sig.parameters.keys())



def test_wh::if_is_not_abstract():
    assert not inspect.isabstract(wh::If)


def test_wh::if_constructor_exists():
    assert callable(wh::If.__init__)


def test_wh::if_constructor_args():
    sig = inspect.signature(wh::If.__init__)
    params = list(sig.parameters.keys())



def test_wh::while_is_not_abstract():
    assert not inspect.isabstract(wh::While)


def test_wh::while_constructor_exists():
    assert callable(wh::While.__init__)


def test_wh::while_constructor_args():
    sig = inspect.signature(wh::While.__init__)
    params = list(sig.parameters.keys())



def test_wh::for_is_not_abstract():
    assert not inspect.isabstract(wh::For)


def test_wh::for_constructor_exists():
    assert callable(wh::For.__init__)


def test_wh::for_constructor_args():
    sig = inspect.signature(wh::For.__init__)
    params = list(sig.parameters.keys())



def test_wh::expr_is_not_abstract():
    assert not inspect.isabstract(wh::Expr)


def test_wh::expr_constructor_exists():
    assert callable(wh::Expr.__init__)


def test_wh::expr_constructor_args():
    sig = inspect.signature(wh::Expr.__init__)
    params = list(sig.parameters.keys())



def test_wh::foreach_is_not_abstract():
    assert not inspect.isabstract(wh::Foreach)


def test_wh::foreach_constructor_exists():
    assert callable(wh::Foreach.__init__)


def test_wh::foreach_constructor_args():
    sig = inspect.signature(wh::Foreach.__init__)
    params = list(sig.parameters.keys())



def test_wh::eobject_is_not_abstract():
    assert not inspect.isabstract(wh::EObject)


def test_wh::eobject_constructor_exists():
    assert callable(wh::EObject.__init__)


def test_wh::eobject_constructor_args():
    sig = inspect.signature(wh::EObject.__init__)
    params = list(sig.parameters.keys())



def test_wh::command_is_not_abstract():
    assert not inspect.isabstract(wh::Command)


def test_wh::command_constructor_exists():
    assert callable(wh::Command.__init__)


def test_wh::command_constructor_args():
    sig = inspect.signature(wh::Command.__init__)
    params = list(sig.parameters.keys())



def test_wh::exprs_is_not_abstract():
    assert not inspect.isabstract(wh::Exprs)


def test_wh::exprs_constructor_exists():
    assert callable(wh::Exprs.__init__)


def test_wh::exprs_constructor_args():
    sig = inspect.signature(wh::Exprs.__init__)
    params = list(sig.parameters.keys())



def test_wh::vars_is_not_abstract():
    assert not inspect.isabstract(wh::Vars)


def test_wh::vars_constructor_exists():
    assert callable(wh::Vars.__init__)


def test_wh::vars_constructor_args():
    sig = inspect.signature(wh::Vars.__init__)
    params = list(sig.parameters.keys())
    assert "vars" in params, "Missing parameter 'vars'"

def test_wh::vars_has_vars():
    assert hasattr(wh::Vars, "vars")
    descriptor = None
    for klass in wh::Vars.__mro__:
        if "vars" in klass.__dict__:
            descriptor = klass.__dict__["vars"]
            break
    assert isinstance(descriptor, property)



def test_wh::affect_is_not_abstract():
    assert not inspect.isabstract(wh::Affect)


def test_wh::affect_constructor_exists():
    assert callable(wh::Affect.__init__)


def test_wh::affect_constructor_args():
    sig = inspect.signature(wh::Affect.__init__)
    params = list(sig.parameters.keys())



def test_wh::nop_is_not_abstract():
    assert not inspect.isabstract(wh::Nop)


def test_wh::nop_constructor_exists():
    assert callable(wh::Nop.__init__)


def test_wh::nop_constructor_args():
    sig = inspect.signature(wh::Nop.__init__)
    params = list(sig.parameters.keys())
    assert "nop" in params, "Missing parameter 'nop'"

def test_wh::nop_has_nop():
    assert hasattr(wh::Nop, "nop")
    descriptor = None
    for klass in wh::Nop.__mro__:
        if "nop" in klass.__dict__:
            descriptor = klass.__dict__["nop"]
            break
    assert isinstance(descriptor, property)



def test_wh::definition_is_not_abstract():
    assert not inspect.isabstract(wh::Definition)


def test_wh::definition_constructor_exists():
    assert callable(wh::Definition.__init__)


def test_wh::definition_constructor_args():
    sig = inspect.signature(wh::Definition.__init__)
    params = list(sig.parameters.keys())



def test_wh::program_is_not_abstract():
    assert not inspect.isabstract(wh::Program)


def test_wh::program_constructor_exists():
    assert callable(wh::Program.__init__)


def test_wh::program_constructor_args():
    sig = inspect.signature(wh::Program.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_wh::program_has_name():
    assert hasattr(wh::Program, "name")
    descriptor = None
    for klass in wh::Program.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_wh::wh_is_not_abstract():
    assert not inspect.isabstract(wh::Wh)


def test_wh::wh_constructor_exists():
    assert callable(wh::Wh.__init__)


def test_wh::wh_constructor_args():
    sig = inspect.signature(wh::Wh.__init__)
    params = list(sig.parameters.keys())



def test_wh::output_is_not_abstract():
    assert not inspect.isabstract(wh::Output)


def test_wh::output_constructor_exists():
    assert callable(wh::Output.__init__)


def test_wh::output_constructor_args():
    sig = inspect.signature(wh::Output.__init__)
    params = list(sig.parameters.keys())
    assert "vars" in params, "Missing parameter 'vars'"

def test_wh::output_has_vars():
    assert hasattr(wh::Output, "vars")
    descriptor = None
    for klass in wh::Output.__mro__:
        if "vars" in klass.__dict__:
            descriptor = klass.__dict__["vars"]
            break
    assert isinstance(descriptor, property)



def test_wh::commands_is_not_abstract():
    assert not inspect.isabstract(wh::Commands)


def test_wh::commands_constructor_exists():
    assert callable(wh::Commands.__init__)


def test_wh::commands_constructor_args():
    sig = inspect.signature(wh::Commands.__init__)
    params = list(sig.parameters.keys())



def test_wh::input_is_not_abstract():
    assert not inspect.isabstract(wh::Input)


def test_wh::input_constructor_exists():
    assert callable(wh::Input.__init__)


def test_wh::input_constructor_args():
    sig = inspect.signature(wh::Input.__init__)
    params = list(sig.parameters.keys())
    assert "vars" in params, "Missing parameter 'vars'"

def test_wh::input_has_vars():
    assert hasattr(wh::Input, "vars")
    descriptor = None
    for klass in wh::Input.__mro__:
        if "vars" in klass.__dict__:
            descriptor = klass.__dict__["vars"]
            break
    assert isinstance(descriptor, property)


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
wh::ExprNot_strategy = st.builds(
    wh::ExprNot,
    not_=
        safe_text
)
wh::ExprOr_strategy = st.builds(
    wh::ExprOr,
)
wh::ExprAnd_strategy = st.builds(
    wh::ExprAnd,
)
wh::ListExpr_strategy = st.builds(
    wh::ListExpr,
)
wh::Cons_strategy = st.builds(
    wh::Cons,
)
wh::ExprSimple_strategy = st.builds(
    wh::ExprSimple,
    str=
        safe_text,
    strSymb=
        safe_text
)
wh::ExprEq_strategy = st.builds(
    wh::ExprEq,
)
wh::If_strategy = st.builds(
    wh::If,
)
wh::While_strategy = st.builds(
    wh::While,
)
wh::For_strategy = st.builds(
    wh::For,
)
wh::Expr_strategy = st.builds(
    wh::Expr,
)
wh::Foreach_strategy = st.builds(
    wh::Foreach,
)
wh::EObject_strategy = st.builds(
    wh::EObject,
)
wh::Command_strategy = st.builds(
    wh::Command,
)
wh::Exprs_strategy = st.builds(
    wh::Exprs,
)
wh::Vars_strategy = st.builds(
    wh::Vars,
    vars=
        safe_text
)
wh::Affect_strategy = st.builds(
    wh::Affect,
)
wh::Nop_strategy = st.builds(
    wh::Nop,
    nop=
        safe_text
)
wh::Definition_strategy = st.builds(
    wh::Definition,
)
wh::Program_strategy = st.builds(
    wh::Program,
    name=
        safe_text
)
wh::Wh_strategy = st.builds(
    wh::Wh,
)
wh::Output_strategy = st.builds(
    wh::Output,
    vars=
        safe_text
)
wh::Commands_strategy = st.builds(
    wh::Commands,
)
wh::Input_strategy = st.builds(
    wh::Input,
    vars=
        safe_text
)

@given(instance=wh::ExprNot_strategy)
@settings(max_examples=50)
def test_wh::exprnot_instantiation(instance):
    assert isinstance(instance, wh::ExprNot)

@given(instance=wh::ExprNot_strategy)
def test_wh::exprnot_not__type(instance):
    assert isinstance(instance.not_, str)


@given(instance=wh::ExprNot_strategy)
def test_wh::exprnot_not__setter(instance):
    original = instance.not_
    instance.not_ = original
    assert instance.not_ == original

@given(instance=wh::ExprOr_strategy)
@settings(max_examples=50)
def test_wh::expror_instantiation(instance):
    assert isinstance(instance, wh::ExprOr)

@given(instance=wh::ExprAnd_strategy)
@settings(max_examples=50)
def test_wh::exprand_instantiation(instance):
    assert isinstance(instance, wh::ExprAnd)

@given(instance=wh::ListExpr_strategy)
@settings(max_examples=50)
def test_wh::listexpr_instantiation(instance):
    assert isinstance(instance, wh::ListExpr)

@given(instance=wh::Cons_strategy)
@settings(max_examples=50)
def test_wh::cons_instantiation(instance):
    assert isinstance(instance, wh::Cons)

@given(instance=wh::ExprSimple_strategy)
@settings(max_examples=50)
def test_wh::exprsimple_instantiation(instance):
    assert isinstance(instance, wh::ExprSimple)

@given(instance=wh::ExprSimple_strategy)
def test_wh::exprsimple_str_type(instance):
    assert isinstance(instance.str, str)


@given(instance=wh::ExprSimple_strategy)
def test_wh::exprsimple_str_setter(instance):
    original = instance.str
    instance.str = original
    assert instance.str == original

@given(instance=wh::ExprSimple_strategy)
def test_wh::exprsimple_strSymb_type(instance):
    assert isinstance(instance.strSymb, str)


@given(instance=wh::ExprSimple_strategy)
def test_wh::exprsimple_strSymb_setter(instance):
    original = instance.strSymb
    instance.strSymb = original
    assert instance.strSymb == original

@given(instance=wh::ExprEq_strategy)
@settings(max_examples=50)
def test_wh::expreq_instantiation(instance):
    assert isinstance(instance, wh::ExprEq)

@given(instance=wh::If_strategy)
@settings(max_examples=50)
def test_wh::if_instantiation(instance):
    assert isinstance(instance, wh::If)

@given(instance=wh::While_strategy)
@settings(max_examples=50)
def test_wh::while_instantiation(instance):
    assert isinstance(instance, wh::While)

@given(instance=wh::For_strategy)
@settings(max_examples=50)
def test_wh::for_instantiation(instance):
    assert isinstance(instance, wh::For)

@given(instance=wh::Expr_strategy)
@settings(max_examples=50)
def test_wh::expr_instantiation(instance):
    assert isinstance(instance, wh::Expr)

@given(instance=wh::Foreach_strategy)
@settings(max_examples=50)
def test_wh::foreach_instantiation(instance):
    assert isinstance(instance, wh::Foreach)

@given(instance=wh::EObject_strategy)
@settings(max_examples=50)
def test_wh::eobject_instantiation(instance):
    assert isinstance(instance, wh::EObject)

@given(instance=wh::Command_strategy)
@settings(max_examples=50)
def test_wh::command_instantiation(instance):
    assert isinstance(instance, wh::Command)

@given(instance=wh::Exprs_strategy)
@settings(max_examples=50)
def test_wh::exprs_instantiation(instance):
    assert isinstance(instance, wh::Exprs)

@given(instance=wh::Vars_strategy)
@settings(max_examples=50)
def test_wh::vars_instantiation(instance):
    assert isinstance(instance, wh::Vars)

@given(instance=wh::Vars_strategy)
def test_wh::vars_vars_type(instance):
    assert isinstance(instance.vars, str)


@given(instance=wh::Vars_strategy)
def test_wh::vars_vars_setter(instance):
    original = instance.vars
    instance.vars = original
    assert instance.vars == original

@given(instance=wh::Affect_strategy)
@settings(max_examples=50)
def test_wh::affect_instantiation(instance):
    assert isinstance(instance, wh::Affect)

@given(instance=wh::Nop_strategy)
@settings(max_examples=50)
def test_wh::nop_instantiation(instance):
    assert isinstance(instance, wh::Nop)

@given(instance=wh::Nop_strategy)
def test_wh::nop_nop_type(instance):
    assert isinstance(instance.nop, str)


@given(instance=wh::Nop_strategy)
def test_wh::nop_nop_setter(instance):
    original = instance.nop
    instance.nop = original
    assert instance.nop == original

@given(instance=wh::Definition_strategy)
@settings(max_examples=50)
def test_wh::definition_instantiation(instance):
    assert isinstance(instance, wh::Definition)

@given(instance=wh::Program_strategy)
@settings(max_examples=50)
def test_wh::program_instantiation(instance):
    assert isinstance(instance, wh::Program)

@given(instance=wh::Program_strategy)
def test_wh::program_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=wh::Program_strategy)
def test_wh::program_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=wh::Wh_strategy)
@settings(max_examples=50)
def test_wh::wh_instantiation(instance):
    assert isinstance(instance, wh::Wh)

@given(instance=wh::Output_strategy)
@settings(max_examples=50)
def test_wh::output_instantiation(instance):
    assert isinstance(instance, wh::Output)

@given(instance=wh::Output_strategy)
def test_wh::output_vars_type(instance):
    assert isinstance(instance.vars, str)


@given(instance=wh::Output_strategy)
def test_wh::output_vars_setter(instance):
    original = instance.vars
    instance.vars = original
    assert instance.vars == original

@given(instance=wh::Commands_strategy)
@settings(max_examples=50)
def test_wh::commands_instantiation(instance):
    assert isinstance(instance, wh::Commands)

@given(instance=wh::Input_strategy)
@settings(max_examples=50)
def test_wh::input_instantiation(instance):
    assert isinstance(instance, wh::Input)

@given(instance=wh::Input_strategy)
def test_wh::input_vars_type(instance):
    assert isinstance(instance.vars, str)


@given(instance=wh::Input_strategy)
def test_wh::input_vars_setter(instance):
    original = instance.vars
    instance.vars = original
    assert instance.vars == original
