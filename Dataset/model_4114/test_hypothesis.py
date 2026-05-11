import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    py::ExprEq,
    py::ExprNot,
    py::ExprSym,
    py::ExprTl,
    py::ExprHd,
    py::ExprList,
    py::LExpr,
    py::ExprCons,
    py::ExprOr,
    py::While,
    py::Foreach,
    py::For,
    py::Affect,
    py::Nop,
    py::Expr,
    py::If,
    py::EObject,
    py::ExprAnd,
    py::ExprSimple,
    py::Input,
    py::Definition,
    py::FunctionP,
    py::Program,
    py::Wh,
    py::Command,
    py::Output,
    py::Commands,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_py::expreq_is_not_abstract():
    assert not inspect.isabstract(py::ExprEq)


def test_py::expreq_constructor_exists():
    assert callable(py::ExprEq.__init__)


def test_py::expreq_constructor_args():
    sig = inspect.signature(py::ExprEq.__init__)
    params = list(sig.parameters.keys())



def test_py::exprnot_is_not_abstract():
    assert not inspect.isabstract(py::ExprNot)


def test_py::exprnot_constructor_exists():
    assert callable(py::ExprNot.__init__)


def test_py::exprnot_constructor_args():
    sig = inspect.signature(py::ExprNot.__init__)
    params = list(sig.parameters.keys())



def test_py::exprsym_is_not_abstract():
    assert not inspect.isabstract(py::ExprSym)


def test_py::exprsym_constructor_exists():
    assert callable(py::ExprSym.__init__)


def test_py::exprsym_constructor_args():
    sig = inspect.signature(py::ExprSym.__init__)
    params = list(sig.parameters.keys())
    assert "arg1" in params, "Missing parameter 'arg1'"

def test_py::exprsym_has_arg1():
    assert hasattr(py::ExprSym, "arg1")
    descriptor = None
    for klass in py::ExprSym.__mro__:
        if "arg1" in klass.__dict__:
            descriptor = klass.__dict__["arg1"]
            break
    assert isinstance(descriptor, property)



def test_py::exprtl_is_not_abstract():
    assert not inspect.isabstract(py::ExprTl)


def test_py::exprtl_constructor_exists():
    assert callable(py::ExprTl.__init__)


def test_py::exprtl_constructor_args():
    sig = inspect.signature(py::ExprTl.__init__)
    params = list(sig.parameters.keys())



def test_py::exprhd_is_not_abstract():
    assert not inspect.isabstract(py::ExprHd)


def test_py::exprhd_constructor_exists():
    assert callable(py::ExprHd.__init__)


def test_py::exprhd_constructor_args():
    sig = inspect.signature(py::ExprHd.__init__)
    params = list(sig.parameters.keys())



def test_py::exprlist_is_not_abstract():
    assert not inspect.isabstract(py::ExprList)


def test_py::exprlist_constructor_exists():
    assert callable(py::ExprList.__init__)


def test_py::exprlist_constructor_args():
    sig = inspect.signature(py::ExprList.__init__)
    params = list(sig.parameters.keys())



def test_py::lexpr_is_not_abstract():
    assert not inspect.isabstract(py::LExpr)


def test_py::lexpr_constructor_exists():
    assert callable(py::LExpr.__init__)


def test_py::lexpr_constructor_args():
    sig = inspect.signature(py::LExpr.__init__)
    params = list(sig.parameters.keys())



def test_py::exprcons_is_not_abstract():
    assert not inspect.isabstract(py::ExprCons)


def test_py::exprcons_constructor_exists():
    assert callable(py::ExprCons.__init__)


def test_py::exprcons_constructor_args():
    sig = inspect.signature(py::ExprCons.__init__)
    params = list(sig.parameters.keys())



def test_py::expror_is_not_abstract():
    assert not inspect.isabstract(py::ExprOr)


def test_py::expror_constructor_exists():
    assert callable(py::ExprOr.__init__)


def test_py::expror_constructor_args():
    sig = inspect.signature(py::ExprOr.__init__)
    params = list(sig.parameters.keys())



def test_py::while_is_not_abstract():
    assert not inspect.isabstract(py::While)


def test_py::while_constructor_exists():
    assert callable(py::While.__init__)


def test_py::while_constructor_args():
    sig = inspect.signature(py::While.__init__)
    params = list(sig.parameters.keys())



def test_py::foreach_is_not_abstract():
    assert not inspect.isabstract(py::Foreach)


def test_py::foreach_constructor_exists():
    assert callable(py::Foreach.__init__)


def test_py::foreach_constructor_args():
    sig = inspect.signature(py::Foreach.__init__)
    params = list(sig.parameters.keys())
    assert "var" in params, "Missing parameter 'var'"

def test_py::foreach_has_var():
    assert hasattr(py::Foreach, "var")
    descriptor = None
    for klass in py::Foreach.__mro__:
        if "var" in klass.__dict__:
            descriptor = klass.__dict__["var"]
            break
    assert isinstance(descriptor, property)



def test_py::for_is_not_abstract():
    assert not inspect.isabstract(py::For)


def test_py::for_constructor_exists():
    assert callable(py::For.__init__)


def test_py::for_constructor_args():
    sig = inspect.signature(py::For.__init__)
    params = list(sig.parameters.keys())



def test_py::affect_is_not_abstract():
    assert not inspect.isabstract(py::Affect)


def test_py::affect_constructor_exists():
    assert callable(py::Affect.__init__)


def test_py::affect_constructor_args():
    sig = inspect.signature(py::Affect.__init__)
    params = list(sig.parameters.keys())
    assert "vars" in params, "Missing parameter 'vars'"

def test_py::affect_has_vars():
    assert hasattr(py::Affect, "vars")
    descriptor = None
    for klass in py::Affect.__mro__:
        if "vars" in klass.__dict__:
            descriptor = klass.__dict__["vars"]
            break
    assert isinstance(descriptor, property)



def test_py::nop_is_not_abstract():
    assert not inspect.isabstract(py::Nop)


def test_py::nop_constructor_exists():
    assert callable(py::Nop.__init__)


def test_py::nop_constructor_args():
    sig = inspect.signature(py::Nop.__init__)
    params = list(sig.parameters.keys())
    assert "nop" in params, "Missing parameter 'nop'"

def test_py::nop_has_nop():
    assert hasattr(py::Nop, "nop")
    descriptor = None
    for klass in py::Nop.__mro__:
        if "nop" in klass.__dict__:
            descriptor = klass.__dict__["nop"]
            break
    assert isinstance(descriptor, property)



def test_py::expr_is_not_abstract():
    assert not inspect.isabstract(py::Expr)


def test_py::expr_constructor_exists():
    assert callable(py::Expr.__init__)


def test_py::expr_constructor_args():
    sig = inspect.signature(py::Expr.__init__)
    params = list(sig.parameters.keys())



def test_py::if_is_not_abstract():
    assert not inspect.isabstract(py::If)


def test_py::if_constructor_exists():
    assert callable(py::If.__init__)


def test_py::if_constructor_args():
    sig = inspect.signature(py::If.__init__)
    params = list(sig.parameters.keys())



def test_py::eobject_is_not_abstract():
    assert not inspect.isabstract(py::EObject)


def test_py::eobject_constructor_exists():
    assert callable(py::EObject.__init__)


def test_py::eobject_constructor_args():
    sig = inspect.signature(py::EObject.__init__)
    params = list(sig.parameters.keys())



def test_py::exprand_is_not_abstract():
    assert not inspect.isabstract(py::ExprAnd)


def test_py::exprand_constructor_exists():
    assert callable(py::ExprAnd.__init__)


def test_py::exprand_constructor_args():
    sig = inspect.signature(py::ExprAnd.__init__)
    params = list(sig.parameters.keys())



def test_py::exprsimple_is_not_abstract():
    assert not inspect.isabstract(py::ExprSimple)


def test_py::exprsimple_constructor_exists():
    assert callable(py::ExprSimple.__init__)


def test_py::exprsimple_constructor_args():
    sig = inspect.signature(py::ExprSimple.__init__)
    params = list(sig.parameters.keys())
    assert "varSimple" in params, "Missing parameter 'varSimple'"
    assert "sym" in params, "Missing parameter 'sym'"
    assert "str" in params, "Missing parameter 'str'"

def test_py::exprsimple_has_varSimple():
    assert hasattr(py::ExprSimple, "varSimple")
    descriptor = None
    for klass in py::ExprSimple.__mro__:
        if "varSimple" in klass.__dict__:
            descriptor = klass.__dict__["varSimple"]
            break
    assert isinstance(descriptor, property)

def test_py::exprsimple_has_sym():
    assert hasattr(py::ExprSimple, "sym")
    descriptor = None
    for klass in py::ExprSimple.__mro__:
        if "sym" in klass.__dict__:
            descriptor = klass.__dict__["sym"]
            break
    assert isinstance(descriptor, property)

def test_py::exprsimple_has_str():
    assert hasattr(py::ExprSimple, "str")
    descriptor = None
    for klass in py::ExprSimple.__mro__:
        if "str" in klass.__dict__:
            descriptor = klass.__dict__["str"]
            break
    assert isinstance(descriptor, property)



def test_py::input_is_not_abstract():
    assert not inspect.isabstract(py::Input)


def test_py::input_constructor_exists():
    assert callable(py::Input.__init__)


def test_py::input_constructor_args():
    sig = inspect.signature(py::Input.__init__)
    params = list(sig.parameters.keys())
    assert "vars" in params, "Missing parameter 'vars'"

def test_py::input_has_vars():
    assert hasattr(py::Input, "vars")
    descriptor = None
    for klass in py::Input.__mro__:
        if "vars" in klass.__dict__:
            descriptor = klass.__dict__["vars"]
            break
    assert isinstance(descriptor, property)



def test_py::definition_is_not_abstract():
    assert not inspect.isabstract(py::Definition)


def test_py::definition_constructor_exists():
    assert callable(py::Definition.__init__)


def test_py::definition_constructor_args():
    sig = inspect.signature(py::Definition.__init__)
    params = list(sig.parameters.keys())



def test_py::functionp_is_not_abstract():
    assert not inspect.isabstract(py::FunctionP)


def test_py::functionp_constructor_exists():
    assert callable(py::FunctionP.__init__)


def test_py::functionp_constructor_args():
    sig = inspect.signature(py::FunctionP.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_py::functionp_has_name():
    assert hasattr(py::FunctionP, "name")
    descriptor = None
    for klass in py::FunctionP.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_py::program_is_not_abstract():
    assert not inspect.isabstract(py::Program)


def test_py::program_constructor_exists():
    assert callable(py::Program.__init__)


def test_py::program_constructor_args():
    sig = inspect.signature(py::Program.__init__)
    params = list(sig.parameters.keys())



def test_py::wh_is_not_abstract():
    assert not inspect.isabstract(py::Wh)


def test_py::wh_constructor_exists():
    assert callable(py::Wh.__init__)


def test_py::wh_constructor_args():
    sig = inspect.signature(py::Wh.__init__)
    params = list(sig.parameters.keys())



def test_py::command_is_not_abstract():
    assert not inspect.isabstract(py::Command)


def test_py::command_constructor_exists():
    assert callable(py::Command.__init__)


def test_py::command_constructor_args():
    sig = inspect.signature(py::Command.__init__)
    params = list(sig.parameters.keys())



def test_py::output_is_not_abstract():
    assert not inspect.isabstract(py::Output)


def test_py::output_constructor_exists():
    assert callable(py::Output.__init__)


def test_py::output_constructor_args():
    sig = inspect.signature(py::Output.__init__)
    params = list(sig.parameters.keys())
    assert "vars" in params, "Missing parameter 'vars'"

def test_py::output_has_vars():
    assert hasattr(py::Output, "vars")
    descriptor = None
    for klass in py::Output.__mro__:
        if "vars" in klass.__dict__:
            descriptor = klass.__dict__["vars"]
            break
    assert isinstance(descriptor, property)



def test_py::commands_is_not_abstract():
    assert not inspect.isabstract(py::Commands)


def test_py::commands_constructor_exists():
    assert callable(py::Commands.__init__)


def test_py::commands_constructor_args():
    sig = inspect.signature(py::Commands.__init__)
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
py::ExprEq_strategy = st.builds(
    py::ExprEq,
)
py::ExprNot_strategy = st.builds(
    py::ExprNot,
)
py::ExprSym_strategy = st.builds(
    py::ExprSym,
    arg1=
        safe_text
)
py::ExprTl_strategy = st.builds(
    py::ExprTl,
)
py::ExprHd_strategy = st.builds(
    py::ExprHd,
)
py::ExprList_strategy = st.builds(
    py::ExprList,
)
py::LExpr_strategy = st.builds(
    py::LExpr,
)
py::ExprCons_strategy = st.builds(
    py::ExprCons,
)
py::ExprOr_strategy = st.builds(
    py::ExprOr,
)
py::While_strategy = st.builds(
    py::While,
)
py::Foreach_strategy = st.builds(
    py::Foreach,
    var=
        safe_text
)
py::For_strategy = st.builds(
    py::For,
)
py::Affect_strategy = st.builds(
    py::Affect,
    vars=
        safe_text
)
py::Nop_strategy = st.builds(
    py::Nop,
    nop=
        safe_text
)
py::Expr_strategy = st.builds(
    py::Expr,
)
py::If_strategy = st.builds(
    py::If,
)
py::EObject_strategy = st.builds(
    py::EObject,
)
py::ExprAnd_strategy = st.builds(
    py::ExprAnd,
)
py::ExprSimple_strategy = st.builds(
    py::ExprSimple,
    varSimple=
        safe_text,
    sym=
        safe_text,
    str=
        safe_text
)
py::Input_strategy = st.builds(
    py::Input,
    vars=
        safe_text
)
py::Definition_strategy = st.builds(
    py::Definition,
)
py::FunctionP_strategy = st.builds(
    py::FunctionP,
    name=
        safe_text
)
py::Program_strategy = st.builds(
    py::Program,
)
py::Wh_strategy = st.builds(
    py::Wh,
)
py::Command_strategy = st.builds(
    py::Command,
)
py::Output_strategy = st.builds(
    py::Output,
    vars=
        safe_text
)
py::Commands_strategy = st.builds(
    py::Commands,
)

@given(instance=py::ExprEq_strategy)
@settings(max_examples=50)
def test_py::expreq_instantiation(instance):
    assert isinstance(instance, py::ExprEq)

@given(instance=py::ExprNot_strategy)
@settings(max_examples=50)
def test_py::exprnot_instantiation(instance):
    assert isinstance(instance, py::ExprNot)

@given(instance=py::ExprSym_strategy)
@settings(max_examples=50)
def test_py::exprsym_instantiation(instance):
    assert isinstance(instance, py::ExprSym)

@given(instance=py::ExprSym_strategy)
def test_py::exprsym_arg1_type(instance):
    assert isinstance(instance.arg1, str)


@given(instance=py::ExprSym_strategy)
def test_py::exprsym_arg1_setter(instance):
    original = instance.arg1
    instance.arg1 = original
    assert instance.arg1 == original

@given(instance=py::ExprTl_strategy)
@settings(max_examples=50)
def test_py::exprtl_instantiation(instance):
    assert isinstance(instance, py::ExprTl)

@given(instance=py::ExprHd_strategy)
@settings(max_examples=50)
def test_py::exprhd_instantiation(instance):
    assert isinstance(instance, py::ExprHd)

@given(instance=py::ExprList_strategy)
@settings(max_examples=50)
def test_py::exprlist_instantiation(instance):
    assert isinstance(instance, py::ExprList)

@given(instance=py::LExpr_strategy)
@settings(max_examples=50)
def test_py::lexpr_instantiation(instance):
    assert isinstance(instance, py::LExpr)

@given(instance=py::ExprCons_strategy)
@settings(max_examples=50)
def test_py::exprcons_instantiation(instance):
    assert isinstance(instance, py::ExprCons)

@given(instance=py::ExprOr_strategy)
@settings(max_examples=50)
def test_py::expror_instantiation(instance):
    assert isinstance(instance, py::ExprOr)

@given(instance=py::While_strategy)
@settings(max_examples=50)
def test_py::while_instantiation(instance):
    assert isinstance(instance, py::While)

@given(instance=py::Foreach_strategy)
@settings(max_examples=50)
def test_py::foreach_instantiation(instance):
    assert isinstance(instance, py::Foreach)

@given(instance=py::Foreach_strategy)
def test_py::foreach_var_type(instance):
    assert isinstance(instance.var, str)


@given(instance=py::Foreach_strategy)
def test_py::foreach_var_setter(instance):
    original = instance.var
    instance.var = original
    assert instance.var == original

@given(instance=py::For_strategy)
@settings(max_examples=50)
def test_py::for_instantiation(instance):
    assert isinstance(instance, py::For)

@given(instance=py::Affect_strategy)
@settings(max_examples=50)
def test_py::affect_instantiation(instance):
    assert isinstance(instance, py::Affect)

@given(instance=py::Affect_strategy)
def test_py::affect_vars_type(instance):
    assert isinstance(instance.vars, str)


@given(instance=py::Affect_strategy)
def test_py::affect_vars_setter(instance):
    original = instance.vars
    instance.vars = original
    assert instance.vars == original

@given(instance=py::Nop_strategy)
@settings(max_examples=50)
def test_py::nop_instantiation(instance):
    assert isinstance(instance, py::Nop)

@given(instance=py::Nop_strategy)
def test_py::nop_nop_type(instance):
    assert isinstance(instance.nop, str)


@given(instance=py::Nop_strategy)
def test_py::nop_nop_setter(instance):
    original = instance.nop
    instance.nop = original
    assert instance.nop == original

@given(instance=py::Expr_strategy)
@settings(max_examples=50)
def test_py::expr_instantiation(instance):
    assert isinstance(instance, py::Expr)

@given(instance=py::If_strategy)
@settings(max_examples=50)
def test_py::if_instantiation(instance):
    assert isinstance(instance, py::If)

@given(instance=py::EObject_strategy)
@settings(max_examples=50)
def test_py::eobject_instantiation(instance):
    assert isinstance(instance, py::EObject)

@given(instance=py::ExprAnd_strategy)
@settings(max_examples=50)
def test_py::exprand_instantiation(instance):
    assert isinstance(instance, py::ExprAnd)

@given(instance=py::ExprSimple_strategy)
@settings(max_examples=50)
def test_py::exprsimple_instantiation(instance):
    assert isinstance(instance, py::ExprSimple)

@given(instance=py::ExprSimple_strategy)
def test_py::exprsimple_varSimple_type(instance):
    assert isinstance(instance.varSimple, str)


@given(instance=py::ExprSimple_strategy)
def test_py::exprsimple_varSimple_setter(instance):
    original = instance.varSimple
    instance.varSimple = original
    assert instance.varSimple == original

@given(instance=py::ExprSimple_strategy)
def test_py::exprsimple_sym_type(instance):
    assert isinstance(instance.sym, str)


@given(instance=py::ExprSimple_strategy)
def test_py::exprsimple_sym_setter(instance):
    original = instance.sym
    instance.sym = original
    assert instance.sym == original

@given(instance=py::ExprSimple_strategy)
def test_py::exprsimple_str_type(instance):
    assert isinstance(instance.str, str)


@given(instance=py::ExprSimple_strategy)
def test_py::exprsimple_str_setter(instance):
    original = instance.str
    instance.str = original
    assert instance.str == original

@given(instance=py::Input_strategy)
@settings(max_examples=50)
def test_py::input_instantiation(instance):
    assert isinstance(instance, py::Input)

@given(instance=py::Input_strategy)
def test_py::input_vars_type(instance):
    assert isinstance(instance.vars, str)


@given(instance=py::Input_strategy)
def test_py::input_vars_setter(instance):
    original = instance.vars
    instance.vars = original
    assert instance.vars == original

@given(instance=py::Definition_strategy)
@settings(max_examples=50)
def test_py::definition_instantiation(instance):
    assert isinstance(instance, py::Definition)

@given(instance=py::FunctionP_strategy)
@settings(max_examples=50)
def test_py::functionp_instantiation(instance):
    assert isinstance(instance, py::FunctionP)

@given(instance=py::FunctionP_strategy)
def test_py::functionp_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=py::FunctionP_strategy)
def test_py::functionp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=py::Program_strategy)
@settings(max_examples=50)
def test_py::program_instantiation(instance):
    assert isinstance(instance, py::Program)

@given(instance=py::Wh_strategy)
@settings(max_examples=50)
def test_py::wh_instantiation(instance):
    assert isinstance(instance, py::Wh)

@given(instance=py::Command_strategy)
@settings(max_examples=50)
def test_py::command_instantiation(instance):
    assert isinstance(instance, py::Command)

@given(instance=py::Output_strategy)
@settings(max_examples=50)
def test_py::output_instantiation(instance):
    assert isinstance(instance, py::Output)

@given(instance=py::Output_strategy)
def test_py::output_vars_type(instance):
    assert isinstance(instance.vars, str)


@given(instance=py::Output_strategy)
def test_py::output_vars_setter(instance):
    original = instance.vars
    instance.vars = original
    assert instance.vars == original

@given(instance=py::Commands_strategy)
@settings(max_examples=50)
def test_py::commands_instantiation(instance):
    assert isinstance(instance, py::Commands)
