import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Expr,
    wh::ExprCons,
    wh::ExprHd,
    wh::ExprSym,
    wh::ExprTl,
    wh::ExprAnd,
    wh::ExprList,
    wh::ExprEq,
    wh::ExprNot,
    wh::ExprSimple,
    wh::While,
    wh::For,
    wh::Affect,
    wh::Nop,
    wh::Expr,
    wh::If,
    wh::EObject,
    wh::Command,
    wh::ExprOr,
    wh::Commands,
    wh::Input,
    wh::Definition,
    wh::Function,
    wh::Program,
    wh::Wh,
    wh::Output,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_expr_is_not_abstract():
    assert not inspect.isabstract(Expr)


def test_expr_constructor_exists():
    assert callable(Expr.__init__)


def test_expr_constructor_args():
    sig = inspect.signature(Expr.__init__)
    params = list(sig.parameters.keys())



def test_wh::exprcons_is_not_abstract():
    assert not inspect.isabstract(wh::ExprCons)


def test_wh::exprcons_constructor_exists():
    assert callable(wh::ExprCons.__init__)


def test_wh::exprcons_constructor_args():
    sig = inspect.signature(wh::ExprCons.__init__)
    params = list(sig.parameters.keys())



def test_wh::exprhd_is_not_abstract():
    assert not inspect.isabstract(wh::ExprHd)


def test_wh::exprhd_constructor_exists():
    assert callable(wh::ExprHd.__init__)


def test_wh::exprhd_constructor_args():
    sig = inspect.signature(wh::ExprHd.__init__)
    params = list(sig.parameters.keys())



def test_wh::exprsym_is_not_abstract():
    assert not inspect.isabstract(wh::ExprSym)


def test_wh::exprsym_constructor_exists():
    assert callable(wh::ExprSym.__init__)


def test_wh::exprsym_constructor_args():
    sig = inspect.signature(wh::ExprSym.__init__)
    params = list(sig.parameters.keys())
    assert "arg1" in params, "Missing parameter 'arg1'"

def test_wh::exprsym_has_arg1():
    assert hasattr(wh::ExprSym, "arg1")
    descriptor = None
    for klass in wh::ExprSym.__mro__:
        if "arg1" in klass.__dict__:
            descriptor = klass.__dict__["arg1"]
            break
    assert isinstance(descriptor, property)



def test_wh::exprtl_is_not_abstract():
    assert not inspect.isabstract(wh::ExprTl)


def test_wh::exprtl_constructor_exists():
    assert callable(wh::ExprTl.__init__)


def test_wh::exprtl_constructor_args():
    sig = inspect.signature(wh::ExprTl.__init__)
    params = list(sig.parameters.keys())



def test_wh::exprand_is_not_abstract():
    assert not inspect.isabstract(wh::ExprAnd)


def test_wh::exprand_constructor_exists():
    assert callable(wh::ExprAnd.__init__)


def test_wh::exprand_constructor_args():
    sig = inspect.signature(wh::ExprAnd.__init__)
    params = list(sig.parameters.keys())



def test_wh::exprlist_is_not_abstract():
    assert not inspect.isabstract(wh::ExprList)


def test_wh::exprlist_constructor_exists():
    assert callable(wh::ExprList.__init__)


def test_wh::exprlist_constructor_args():
    sig = inspect.signature(wh::ExprList.__init__)
    params = list(sig.parameters.keys())



def test_wh::expreq_is_not_abstract():
    assert not inspect.isabstract(wh::ExprEq)


def test_wh::expreq_constructor_exists():
    assert callable(wh::ExprEq.__init__)


def test_wh::expreq_constructor_args():
    sig = inspect.signature(wh::ExprEq.__init__)
    params = list(sig.parameters.keys())



def test_wh::exprnot_is_not_abstract():
    assert not inspect.isabstract(wh::ExprNot)


def test_wh::exprnot_constructor_exists():
    assert callable(wh::ExprNot.__init__)


def test_wh::exprnot_constructor_args():
    sig = inspect.signature(wh::ExprNot.__init__)
    params = list(sig.parameters.keys())



def test_wh::exprsimple_is_not_abstract():
    assert not inspect.isabstract(wh::ExprSimple)


def test_wh::exprsimple_constructor_exists():
    assert callable(wh::ExprSimple.__init__)


def test_wh::exprsimple_constructor_args():
    sig = inspect.signature(wh::ExprSimple.__init__)
    params = list(sig.parameters.keys())
    assert "varSimple" in params, "Missing parameter 'varSimple'"
    assert "str" in params, "Missing parameter 'str'"
    assert "sym" in params, "Missing parameter 'sym'"

def test_wh::exprsimple_has_varSimple():
    assert hasattr(wh::ExprSimple, "varSimple")
    descriptor = None
    for klass in wh::ExprSimple.__mro__:
        if "varSimple" in klass.__dict__:
            descriptor = klass.__dict__["varSimple"]
            break
    assert isinstance(descriptor, property)

def test_wh::exprsimple_has_str():
    assert hasattr(wh::ExprSimple, "str")
    descriptor = None
    for klass in wh::ExprSimple.__mro__:
        if "str" in klass.__dict__:
            descriptor = klass.__dict__["str"]
            break
    assert isinstance(descriptor, property)

def test_wh::exprsimple_has_sym():
    assert hasattr(wh::ExprSimple, "sym")
    descriptor = None
    for klass in wh::ExprSimple.__mro__:
        if "sym" in klass.__dict__:
            descriptor = klass.__dict__["sym"]
            break
    assert isinstance(descriptor, property)



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



def test_wh::affect_is_not_abstract():
    assert not inspect.isabstract(wh::Affect)


def test_wh::affect_constructor_exists():
    assert callable(wh::Affect.__init__)


def test_wh::affect_constructor_args():
    sig = inspect.signature(wh::Affect.__init__)
    params = list(sig.parameters.keys())
    assert "vars" in params, "Missing parameter 'vars'"

def test_wh::affect_has_vars():
    assert hasattr(wh::Affect, "vars")
    descriptor = None
    for klass in wh::Affect.__mro__:
        if "vars" in klass.__dict__:
            descriptor = klass.__dict__["vars"]
            break
    assert isinstance(descriptor, property)



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



def test_wh::expr_is_not_abstract():
    assert not inspect.isabstract(wh::Expr)


def test_wh::expr_constructor_exists():
    assert callable(wh::Expr.__init__)


def test_wh::expr_constructor_args():
    sig = inspect.signature(wh::Expr.__init__)
    params = list(sig.parameters.keys())



def test_wh::if_is_not_abstract():
    assert not inspect.isabstract(wh::If)


def test_wh::if_constructor_exists():
    assert callable(wh::If.__init__)


def test_wh::if_constructor_args():
    sig = inspect.signature(wh::If.__init__)
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



def test_wh::expror_is_not_abstract():
    assert not inspect.isabstract(wh::ExprOr)


def test_wh::expror_constructor_exists():
    assert callable(wh::ExprOr.__init__)


def test_wh::expror_constructor_args():
    sig = inspect.signature(wh::ExprOr.__init__)
    params = list(sig.parameters.keys())



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



def test_wh::definition_is_not_abstract():
    assert not inspect.isabstract(wh::Definition)


def test_wh::definition_constructor_exists():
    assert callable(wh::Definition.__init__)


def test_wh::definition_constructor_args():
    sig = inspect.signature(wh::Definition.__init__)
    params = list(sig.parameters.keys())



def test_wh::function_is_not_abstract():
    assert not inspect.isabstract(wh::Function)


def test_wh::function_constructor_exists():
    assert callable(wh::Function.__init__)


def test_wh::function_constructor_args():
    sig = inspect.signature(wh::Function.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_wh::function_has_name():
    assert hasattr(wh::Function, "name")
    descriptor = None
    for klass in wh::Function.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_wh::program_is_not_abstract():
    assert not inspect.isabstract(wh::Program)


def test_wh::program_constructor_exists():
    assert callable(wh::Program.__init__)


def test_wh::program_constructor_args():
    sig = inspect.signature(wh::Program.__init__)
    params = list(sig.parameters.keys())



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
Expr_strategy = st.builds(
    Expr,
)
wh::ExprCons_strategy = st.builds(
    wh::ExprCons,
)
wh::ExprHd_strategy = st.builds(
    wh::ExprHd,
)
wh::ExprSym_strategy = st.builds(
    wh::ExprSym,
    arg1=
        safe_text
)
wh::ExprTl_strategy = st.builds(
    wh::ExprTl,
)
wh::ExprAnd_strategy = st.builds(
    wh::ExprAnd,
)
wh::ExprList_strategy = st.builds(
    wh::ExprList,
)
wh::ExprEq_strategy = st.builds(
    wh::ExprEq,
)
wh::ExprNot_strategy = st.builds(
    wh::ExprNot,
)
wh::ExprSimple_strategy = st.builds(
    wh::ExprSimple,
    varSimple=
        safe_text,
    str=
        safe_text,
    sym=
        safe_text
)
wh::While_strategy = st.builds(
    wh::While,
)
wh::For_strategy = st.builds(
    wh::For,
)
wh::Affect_strategy = st.builds(
    wh::Affect,
    vars=
        safe_text
)
wh::Nop_strategy = st.builds(
    wh::Nop,
    nop=
        safe_text
)
wh::Expr_strategy = st.builds(
    wh::Expr,
)
wh::If_strategy = st.builds(
    wh::If,
)
wh::EObject_strategy = st.builds(
    wh::EObject,
)
wh::Command_strategy = st.builds(
    wh::Command,
)
wh::ExprOr_strategy = st.builds(
    wh::ExprOr,
)
wh::Commands_strategy = st.builds(
    wh::Commands,
)
wh::Input_strategy = st.builds(
    wh::Input,
    vars=
        safe_text
)
wh::Definition_strategy = st.builds(
    wh::Definition,
)
wh::Function_strategy = st.builds(
    wh::Function,
    name=
        safe_text
)
wh::Program_strategy = st.builds(
    wh::Program,
)
wh::Wh_strategy = st.builds(
    wh::Wh,
)
wh::Output_strategy = st.builds(
    wh::Output,
    vars=
        safe_text
)

@given(instance=Expr_strategy)
@settings(max_examples=50)
def test_expr_instantiation(instance):
    assert isinstance(instance, Expr)

@given(instance=wh::ExprCons_strategy)
@settings(max_examples=50)
def test_wh::exprcons_instantiation(instance):
    assert isinstance(instance, wh::ExprCons)

@given(instance=wh::ExprHd_strategy)
@settings(max_examples=50)
def test_wh::exprhd_instantiation(instance):
    assert isinstance(instance, wh::ExprHd)

@given(instance=wh::ExprSym_strategy)
@settings(max_examples=50)
def test_wh::exprsym_instantiation(instance):
    assert isinstance(instance, wh::ExprSym)

@given(instance=wh::ExprSym_strategy)
def test_wh::exprsym_arg1_type(instance):
    assert isinstance(instance.arg1, str)


@given(instance=wh::ExprSym_strategy)
def test_wh::exprsym_arg1_setter(instance):
    original = instance.arg1
    instance.arg1 = original
    assert instance.arg1 == original

@given(instance=wh::ExprTl_strategy)
@settings(max_examples=50)
def test_wh::exprtl_instantiation(instance):
    assert isinstance(instance, wh::ExprTl)

@given(instance=wh::ExprAnd_strategy)
@settings(max_examples=50)
def test_wh::exprand_instantiation(instance):
    assert isinstance(instance, wh::ExprAnd)

@given(instance=wh::ExprList_strategy)
@settings(max_examples=50)
def test_wh::exprlist_instantiation(instance):
    assert isinstance(instance, wh::ExprList)

@given(instance=wh::ExprEq_strategy)
@settings(max_examples=50)
def test_wh::expreq_instantiation(instance):
    assert isinstance(instance, wh::ExprEq)

@given(instance=wh::ExprNot_strategy)
@settings(max_examples=50)
def test_wh::exprnot_instantiation(instance):
    assert isinstance(instance, wh::ExprNot)

@given(instance=wh::ExprSimple_strategy)
@settings(max_examples=50)
def test_wh::exprsimple_instantiation(instance):
    assert isinstance(instance, wh::ExprSimple)

@given(instance=wh::ExprSimple_strategy)
def test_wh::exprsimple_varSimple_type(instance):
    assert isinstance(instance.varSimple, str)


@given(instance=wh::ExprSimple_strategy)
def test_wh::exprsimple_varSimple_setter(instance):
    original = instance.varSimple
    instance.varSimple = original
    assert instance.varSimple == original

@given(instance=wh::ExprSimple_strategy)
def test_wh::exprsimple_str_type(instance):
    assert isinstance(instance.str, str)


@given(instance=wh::ExprSimple_strategy)
def test_wh::exprsimple_str_setter(instance):
    original = instance.str
    instance.str = original
    assert instance.str == original

@given(instance=wh::ExprSimple_strategy)
def test_wh::exprsimple_sym_type(instance):
    assert isinstance(instance.sym, str)


@given(instance=wh::ExprSimple_strategy)
def test_wh::exprsimple_sym_setter(instance):
    original = instance.sym
    instance.sym = original
    assert instance.sym == original

@given(instance=wh::While_strategy)
@settings(max_examples=50)
def test_wh::while_instantiation(instance):
    assert isinstance(instance, wh::While)

@given(instance=wh::For_strategy)
@settings(max_examples=50)
def test_wh::for_instantiation(instance):
    assert isinstance(instance, wh::For)

@given(instance=wh::Affect_strategy)
@settings(max_examples=50)
def test_wh::affect_instantiation(instance):
    assert isinstance(instance, wh::Affect)

@given(instance=wh::Affect_strategy)
def test_wh::affect_vars_type(instance):
    assert isinstance(instance.vars, str)


@given(instance=wh::Affect_strategy)
def test_wh::affect_vars_setter(instance):
    original = instance.vars
    instance.vars = original
    assert instance.vars == original

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

@given(instance=wh::Expr_strategy)
@settings(max_examples=50)
def test_wh::expr_instantiation(instance):
    assert isinstance(instance, wh::Expr)

@given(instance=wh::If_strategy)
@settings(max_examples=50)
def test_wh::if_instantiation(instance):
    assert isinstance(instance, wh::If)

@given(instance=wh::EObject_strategy)
@settings(max_examples=50)
def test_wh::eobject_instantiation(instance):
    assert isinstance(instance, wh::EObject)

@given(instance=wh::Command_strategy)
@settings(max_examples=50)
def test_wh::command_instantiation(instance):
    assert isinstance(instance, wh::Command)

@given(instance=wh::ExprOr_strategy)
@settings(max_examples=50)
def test_wh::expror_instantiation(instance):
    assert isinstance(instance, wh::ExprOr)

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

@given(instance=wh::Definition_strategy)
@settings(max_examples=50)
def test_wh::definition_instantiation(instance):
    assert isinstance(instance, wh::Definition)

@given(instance=wh::Function_strategy)
@settings(max_examples=50)
def test_wh::function_instantiation(instance):
    assert isinstance(instance, wh::Function)

@given(instance=wh::Function_strategy)
def test_wh::function_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=wh::Function_strategy)
def test_wh::function_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=wh::Program_strategy)
@settings(max_examples=50)
def test_wh::program_instantiation(instance):
    assert isinstance(instance, wh::Program)

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
