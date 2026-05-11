import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    while::l::ExprNot,
    while::l::ExprSym,
    while::l::ExprTl,
    while::l::ExprHd,
    while::l::ExprList,
    while::l::While,
    while::l::For,
    while::l::Affect,
    while::l::Nop,
    while::l::Expr,
    while::l::If,
    while::l::EObject,
    while::l::ExprCons,
    while::l::ExprOr,
    while::l::ExprAnd,
    while::l::ExprSimple,
    while::l::ExprEq,
    while::l::Program,
    while::l::Wh,
    while::l::Command,
    while::l::Output,
    while::l::Commands,
    while::l::Input,
    while::l::Definition,
    while::l::Function,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_while::l::exprnot_is_not_abstract():
    assert not inspect.isabstract(while::l::ExprNot)


def test_while::l::exprnot_constructor_exists():
    assert callable(while::l::ExprNot.__init__)


def test_while::l::exprnot_constructor_args():
    sig = inspect.signature(while::l::ExprNot.__init__)
    params = list(sig.parameters.keys())



def test_while::l::exprsym_is_not_abstract():
    assert not inspect.isabstract(while::l::ExprSym)


def test_while::l::exprsym_constructor_exists():
    assert callable(while::l::ExprSym.__init__)


def test_while::l::exprsym_constructor_args():
    sig = inspect.signature(while::l::ExprSym.__init__)
    params = list(sig.parameters.keys())
    assert "arg1" in params, "Missing parameter 'arg1'"

def test_while::l::exprsym_has_arg1():
    assert hasattr(while::l::ExprSym, "arg1")
    descriptor = None
    for klass in while::l::ExprSym.__mro__:
        if "arg1" in klass.__dict__:
            descriptor = klass.__dict__["arg1"]
            break
    assert isinstance(descriptor, property)



def test_while::l::exprtl_is_not_abstract():
    assert not inspect.isabstract(while::l::ExprTl)


def test_while::l::exprtl_constructor_exists():
    assert callable(while::l::ExprTl.__init__)


def test_while::l::exprtl_constructor_args():
    sig = inspect.signature(while::l::ExprTl.__init__)
    params = list(sig.parameters.keys())



def test_while::l::exprhd_is_not_abstract():
    assert not inspect.isabstract(while::l::ExprHd)


def test_while::l::exprhd_constructor_exists():
    assert callable(while::l::ExprHd.__init__)


def test_while::l::exprhd_constructor_args():
    sig = inspect.signature(while::l::ExprHd.__init__)
    params = list(sig.parameters.keys())



def test_while::l::exprlist_is_not_abstract():
    assert not inspect.isabstract(while::l::ExprList)


def test_while::l::exprlist_constructor_exists():
    assert callable(while::l::ExprList.__init__)


def test_while::l::exprlist_constructor_args():
    sig = inspect.signature(while::l::ExprList.__init__)
    params = list(sig.parameters.keys())



def test_while::l::while_is_not_abstract():
    assert not inspect.isabstract(while::l::While)


def test_while::l::while_constructor_exists():
    assert callable(while::l::While.__init__)


def test_while::l::while_constructor_args():
    sig = inspect.signature(while::l::While.__init__)
    params = list(sig.parameters.keys())



def test_while::l::for_is_not_abstract():
    assert not inspect.isabstract(while::l::For)


def test_while::l::for_constructor_exists():
    assert callable(while::l::For.__init__)


def test_while::l::for_constructor_args():
    sig = inspect.signature(while::l::For.__init__)
    params = list(sig.parameters.keys())



def test_while::l::affect_is_not_abstract():
    assert not inspect.isabstract(while::l::Affect)


def test_while::l::affect_constructor_exists():
    assert callable(while::l::Affect.__init__)


def test_while::l::affect_constructor_args():
    sig = inspect.signature(while::l::Affect.__init__)
    params = list(sig.parameters.keys())
    assert "vars" in params, "Missing parameter 'vars'"

def test_while::l::affect_has_vars():
    assert hasattr(while::l::Affect, "vars")
    descriptor = None
    for klass in while::l::Affect.__mro__:
        if "vars" in klass.__dict__:
            descriptor = klass.__dict__["vars"]
            break
    assert isinstance(descriptor, property)



def test_while::l::nop_is_not_abstract():
    assert not inspect.isabstract(while::l::Nop)


def test_while::l::nop_constructor_exists():
    assert callable(while::l::Nop.__init__)


def test_while::l::nop_constructor_args():
    sig = inspect.signature(while::l::Nop.__init__)
    params = list(sig.parameters.keys())
    assert "nop" in params, "Missing parameter 'nop'"

def test_while::l::nop_has_nop():
    assert hasattr(while::l::Nop, "nop")
    descriptor = None
    for klass in while::l::Nop.__mro__:
        if "nop" in klass.__dict__:
            descriptor = klass.__dict__["nop"]
            break
    assert isinstance(descriptor, property)



def test_while::l::expr_is_not_abstract():
    assert not inspect.isabstract(while::l::Expr)


def test_while::l::expr_constructor_exists():
    assert callable(while::l::Expr.__init__)


def test_while::l::expr_constructor_args():
    sig = inspect.signature(while::l::Expr.__init__)
    params = list(sig.parameters.keys())



def test_while::l::if_is_not_abstract():
    assert not inspect.isabstract(while::l::If)


def test_while::l::if_constructor_exists():
    assert callable(while::l::If.__init__)


def test_while::l::if_constructor_args():
    sig = inspect.signature(while::l::If.__init__)
    params = list(sig.parameters.keys())



def test_while::l::eobject_is_not_abstract():
    assert not inspect.isabstract(while::l::EObject)


def test_while::l::eobject_constructor_exists():
    assert callable(while::l::EObject.__init__)


def test_while::l::eobject_constructor_args():
    sig = inspect.signature(while::l::EObject.__init__)
    params = list(sig.parameters.keys())



def test_while::l::exprcons_is_not_abstract():
    assert not inspect.isabstract(while::l::ExprCons)


def test_while::l::exprcons_constructor_exists():
    assert callable(while::l::ExprCons.__init__)


def test_while::l::exprcons_constructor_args():
    sig = inspect.signature(while::l::ExprCons.__init__)
    params = list(sig.parameters.keys())



def test_while::l::expror_is_not_abstract():
    assert not inspect.isabstract(while::l::ExprOr)


def test_while::l::expror_constructor_exists():
    assert callable(while::l::ExprOr.__init__)


def test_while::l::expror_constructor_args():
    sig = inspect.signature(while::l::ExprOr.__init__)
    params = list(sig.parameters.keys())



def test_while::l::exprand_is_not_abstract():
    assert not inspect.isabstract(while::l::ExprAnd)


def test_while::l::exprand_constructor_exists():
    assert callable(while::l::ExprAnd.__init__)


def test_while::l::exprand_constructor_args():
    sig = inspect.signature(while::l::ExprAnd.__init__)
    params = list(sig.parameters.keys())



def test_while::l::exprsimple_is_not_abstract():
    assert not inspect.isabstract(while::l::ExprSimple)


def test_while::l::exprsimple_constructor_exists():
    assert callable(while::l::ExprSimple.__init__)


def test_while::l::exprsimple_constructor_args():
    sig = inspect.signature(while::l::ExprSimple.__init__)
    params = list(sig.parameters.keys())
    assert "str" in params, "Missing parameter 'str'"
    assert "sym" in params, "Missing parameter 'sym'"
    assert "varSimple" in params, "Missing parameter 'varSimple'"
    assert "nameFunction" in params, "Missing parameter 'nameFunction'"

def test_while::l::exprsimple_has_str():
    assert hasattr(while::l::ExprSimple, "str")
    descriptor = None
    for klass in while::l::ExprSimple.__mro__:
        if "str" in klass.__dict__:
            descriptor = klass.__dict__["str"]
            break
    assert isinstance(descriptor, property)

def test_while::l::exprsimple_has_sym():
    assert hasattr(while::l::ExprSimple, "sym")
    descriptor = None
    for klass in while::l::ExprSimple.__mro__:
        if "sym" in klass.__dict__:
            descriptor = klass.__dict__["sym"]
            break
    assert isinstance(descriptor, property)

def test_while::l::exprsimple_has_varSimple():
    assert hasattr(while::l::ExprSimple, "varSimple")
    descriptor = None
    for klass in while::l::ExprSimple.__mro__:
        if "varSimple" in klass.__dict__:
            descriptor = klass.__dict__["varSimple"]
            break
    assert isinstance(descriptor, property)

def test_while::l::exprsimple_has_nameFunction():
    assert hasattr(while::l::ExprSimple, "nameFunction")
    descriptor = None
    for klass in while::l::ExprSimple.__mro__:
        if "nameFunction" in klass.__dict__:
            descriptor = klass.__dict__["nameFunction"]
            break
    assert isinstance(descriptor, property)



def test_while::l::expreq_is_not_abstract():
    assert not inspect.isabstract(while::l::ExprEq)


def test_while::l::expreq_constructor_exists():
    assert callable(while::l::ExprEq.__init__)


def test_while::l::expreq_constructor_args():
    sig = inspect.signature(while::l::ExprEq.__init__)
    params = list(sig.parameters.keys())



def test_while::l::program_is_not_abstract():
    assert not inspect.isabstract(while::l::Program)


def test_while::l::program_constructor_exists():
    assert callable(while::l::Program.__init__)


def test_while::l::program_constructor_args():
    sig = inspect.signature(while::l::Program.__init__)
    params = list(sig.parameters.keys())



def test_while::l::wh_is_not_abstract():
    assert not inspect.isabstract(while::l::Wh)


def test_while::l::wh_constructor_exists():
    assert callable(while::l::Wh.__init__)


def test_while::l::wh_constructor_args():
    sig = inspect.signature(while::l::Wh.__init__)
    params = list(sig.parameters.keys())



def test_while::l::command_is_not_abstract():
    assert not inspect.isabstract(while::l::Command)


def test_while::l::command_constructor_exists():
    assert callable(while::l::Command.__init__)


def test_while::l::command_constructor_args():
    sig = inspect.signature(while::l::Command.__init__)
    params = list(sig.parameters.keys())



def test_while::l::output_is_not_abstract():
    assert not inspect.isabstract(while::l::Output)


def test_while::l::output_constructor_exists():
    assert callable(while::l::Output.__init__)


def test_while::l::output_constructor_args():
    sig = inspect.signature(while::l::Output.__init__)
    params = list(sig.parameters.keys())
    assert "vars" in params, "Missing parameter 'vars'"

def test_while::l::output_has_vars():
    assert hasattr(while::l::Output, "vars")
    descriptor = None
    for klass in while::l::Output.__mro__:
        if "vars" in klass.__dict__:
            descriptor = klass.__dict__["vars"]
            break
    assert isinstance(descriptor, property)



def test_while::l::commands_is_not_abstract():
    assert not inspect.isabstract(while::l::Commands)


def test_while::l::commands_constructor_exists():
    assert callable(while::l::Commands.__init__)


def test_while::l::commands_constructor_args():
    sig = inspect.signature(while::l::Commands.__init__)
    params = list(sig.parameters.keys())



def test_while::l::input_is_not_abstract():
    assert not inspect.isabstract(while::l::Input)


def test_while::l::input_constructor_exists():
    assert callable(while::l::Input.__init__)


def test_while::l::input_constructor_args():
    sig = inspect.signature(while::l::Input.__init__)
    params = list(sig.parameters.keys())
    assert "vars" in params, "Missing parameter 'vars'"

def test_while::l::input_has_vars():
    assert hasattr(while::l::Input, "vars")
    descriptor = None
    for klass in while::l::Input.__mro__:
        if "vars" in klass.__dict__:
            descriptor = klass.__dict__["vars"]
            break
    assert isinstance(descriptor, property)



def test_while::l::definition_is_not_abstract():
    assert not inspect.isabstract(while::l::Definition)


def test_while::l::definition_constructor_exists():
    assert callable(while::l::Definition.__init__)


def test_while::l::definition_constructor_args():
    sig = inspect.signature(while::l::Definition.__init__)
    params = list(sig.parameters.keys())



def test_while::l::function_is_not_abstract():
    assert not inspect.isabstract(while::l::Function)


def test_while::l::function_constructor_exists():
    assert callable(while::l::Function.__init__)


def test_while::l::function_constructor_args():
    sig = inspect.signature(while::l::Function.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_while::l::function_has_name():
    assert hasattr(while::l::Function, "name")
    descriptor = None
    for klass in while::l::Function.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
while::l::ExprNot_strategy = st.builds(
    while::l::ExprNot,
)
while::l::ExprSym_strategy = st.builds(
    while::l::ExprSym,
    arg1=
        safe_text
)
while::l::ExprTl_strategy = st.builds(
    while::l::ExprTl,
)
while::l::ExprHd_strategy = st.builds(
    while::l::ExprHd,
)
while::l::ExprList_strategy = st.builds(
    while::l::ExprList,
)
while::l::While_strategy = st.builds(
    while::l::While,
)
while::l::For_strategy = st.builds(
    while::l::For,
)
while::l::Affect_strategy = st.builds(
    while::l::Affect,
    vars=
        safe_text
)
while::l::Nop_strategy = st.builds(
    while::l::Nop,
    nop=
        safe_text
)
while::l::Expr_strategy = st.builds(
    while::l::Expr,
)
while::l::If_strategy = st.builds(
    while::l::If,
)
while::l::EObject_strategy = st.builds(
    while::l::EObject,
)
while::l::ExprCons_strategy = st.builds(
    while::l::ExprCons,
)
while::l::ExprOr_strategy = st.builds(
    while::l::ExprOr,
)
while::l::ExprAnd_strategy = st.builds(
    while::l::ExprAnd,
)
while::l::ExprSimple_strategy = st.builds(
    while::l::ExprSimple,
    str=
        safe_text,
    sym=
        safe_text,
    varSimple=
        safe_text,
    nameFunction=
        safe_text
)
while::l::ExprEq_strategy = st.builds(
    while::l::ExprEq,
)
while::l::Program_strategy = st.builds(
    while::l::Program,
)
while::l::Wh_strategy = st.builds(
    while::l::Wh,
)
while::l::Command_strategy = st.builds(
    while::l::Command,
)
while::l::Output_strategy = st.builds(
    while::l::Output,
    vars=
        safe_text
)
while::l::Commands_strategy = st.builds(
    while::l::Commands,
)
while::l::Input_strategy = st.builds(
    while::l::Input,
    vars=
        safe_text
)
while::l::Definition_strategy = st.builds(
    while::l::Definition,
)
while::l::Function_strategy = st.builds(
    while::l::Function,
    name=
        safe_text
)

@given(instance=while::l::ExprNot_strategy)
@settings(max_examples=50)
def test_while::l::exprnot_instantiation(instance):
    assert isinstance(instance, while::l::ExprNot)

@given(instance=while::l::ExprSym_strategy)
@settings(max_examples=50)
def test_while::l::exprsym_instantiation(instance):
    assert isinstance(instance, while::l::ExprSym)

@given(instance=while::l::ExprSym_strategy)
def test_while::l::exprsym_arg1_type(instance):
    assert isinstance(instance.arg1, str)


@given(instance=while::l::ExprSym_strategy)
def test_while::l::exprsym_arg1_setter(instance):
    original = instance.arg1
    instance.arg1 = original
    assert instance.arg1 == original

@given(instance=while::l::ExprTl_strategy)
@settings(max_examples=50)
def test_while::l::exprtl_instantiation(instance):
    assert isinstance(instance, while::l::ExprTl)

@given(instance=while::l::ExprHd_strategy)
@settings(max_examples=50)
def test_while::l::exprhd_instantiation(instance):
    assert isinstance(instance, while::l::ExprHd)

@given(instance=while::l::ExprList_strategy)
@settings(max_examples=50)
def test_while::l::exprlist_instantiation(instance):
    assert isinstance(instance, while::l::ExprList)

@given(instance=while::l::While_strategy)
@settings(max_examples=50)
def test_while::l::while_instantiation(instance):
    assert isinstance(instance, while::l::While)

@given(instance=while::l::For_strategy)
@settings(max_examples=50)
def test_while::l::for_instantiation(instance):
    assert isinstance(instance, while::l::For)

@given(instance=while::l::Affect_strategy)
@settings(max_examples=50)
def test_while::l::affect_instantiation(instance):
    assert isinstance(instance, while::l::Affect)

@given(instance=while::l::Affect_strategy)
def test_while::l::affect_vars_type(instance):
    assert isinstance(instance.vars, str)


@given(instance=while::l::Affect_strategy)
def test_while::l::affect_vars_setter(instance):
    original = instance.vars
    instance.vars = original
    assert instance.vars == original

@given(instance=while::l::Nop_strategy)
@settings(max_examples=50)
def test_while::l::nop_instantiation(instance):
    assert isinstance(instance, while::l::Nop)

@given(instance=while::l::Nop_strategy)
def test_while::l::nop_nop_type(instance):
    assert isinstance(instance.nop, str)


@given(instance=while::l::Nop_strategy)
def test_while::l::nop_nop_setter(instance):
    original = instance.nop
    instance.nop = original
    assert instance.nop == original

@given(instance=while::l::Expr_strategy)
@settings(max_examples=50)
def test_while::l::expr_instantiation(instance):
    assert isinstance(instance, while::l::Expr)

@given(instance=while::l::If_strategy)
@settings(max_examples=50)
def test_while::l::if_instantiation(instance):
    assert isinstance(instance, while::l::If)

@given(instance=while::l::EObject_strategy)
@settings(max_examples=50)
def test_while::l::eobject_instantiation(instance):
    assert isinstance(instance, while::l::EObject)

@given(instance=while::l::ExprCons_strategy)
@settings(max_examples=50)
def test_while::l::exprcons_instantiation(instance):
    assert isinstance(instance, while::l::ExprCons)

@given(instance=while::l::ExprOr_strategy)
@settings(max_examples=50)
def test_while::l::expror_instantiation(instance):
    assert isinstance(instance, while::l::ExprOr)

@given(instance=while::l::ExprAnd_strategy)
@settings(max_examples=50)
def test_while::l::exprand_instantiation(instance):
    assert isinstance(instance, while::l::ExprAnd)

@given(instance=while::l::ExprSimple_strategy)
@settings(max_examples=50)
def test_while::l::exprsimple_instantiation(instance):
    assert isinstance(instance, while::l::ExprSimple)

@given(instance=while::l::ExprSimple_strategy)
def test_while::l::exprsimple_str_type(instance):
    assert isinstance(instance.str, str)


@given(instance=while::l::ExprSimple_strategy)
def test_while::l::exprsimple_str_setter(instance):
    original = instance.str
    instance.str = original
    assert instance.str == original

@given(instance=while::l::ExprSimple_strategy)
def test_while::l::exprsimple_sym_type(instance):
    assert isinstance(instance.sym, str)


@given(instance=while::l::ExprSimple_strategy)
def test_while::l::exprsimple_sym_setter(instance):
    original = instance.sym
    instance.sym = original
    assert instance.sym == original

@given(instance=while::l::ExprSimple_strategy)
def test_while::l::exprsimple_varSimple_type(instance):
    assert isinstance(instance.varSimple, str)


@given(instance=while::l::ExprSimple_strategy)
def test_while::l::exprsimple_varSimple_setter(instance):
    original = instance.varSimple
    instance.varSimple = original
    assert instance.varSimple == original

@given(instance=while::l::ExprSimple_strategy)
def test_while::l::exprsimple_nameFunction_type(instance):
    assert isinstance(instance.nameFunction, str)


@given(instance=while::l::ExprSimple_strategy)
def test_while::l::exprsimple_nameFunction_setter(instance):
    original = instance.nameFunction
    instance.nameFunction = original
    assert instance.nameFunction == original

@given(instance=while::l::ExprEq_strategy)
@settings(max_examples=50)
def test_while::l::expreq_instantiation(instance):
    assert isinstance(instance, while::l::ExprEq)

@given(instance=while::l::Program_strategy)
@settings(max_examples=50)
def test_while::l::program_instantiation(instance):
    assert isinstance(instance, while::l::Program)

@given(instance=while::l::Wh_strategy)
@settings(max_examples=50)
def test_while::l::wh_instantiation(instance):
    assert isinstance(instance, while::l::Wh)

@given(instance=while::l::Command_strategy)
@settings(max_examples=50)
def test_while::l::command_instantiation(instance):
    assert isinstance(instance, while::l::Command)

@given(instance=while::l::Output_strategy)
@settings(max_examples=50)
def test_while::l::output_instantiation(instance):
    assert isinstance(instance, while::l::Output)

@given(instance=while::l::Output_strategy)
def test_while::l::output_vars_type(instance):
    assert isinstance(instance.vars, str)


@given(instance=while::l::Output_strategy)
def test_while::l::output_vars_setter(instance):
    original = instance.vars
    instance.vars = original
    assert instance.vars == original

@given(instance=while::l::Commands_strategy)
@settings(max_examples=50)
def test_while::l::commands_instantiation(instance):
    assert isinstance(instance, while::l::Commands)

@given(instance=while::l::Input_strategy)
@settings(max_examples=50)
def test_while::l::input_instantiation(instance):
    assert isinstance(instance, while::l::Input)

@given(instance=while::l::Input_strategy)
def test_while::l::input_vars_type(instance):
    assert isinstance(instance.vars, str)


@given(instance=while::l::Input_strategy)
def test_while::l::input_vars_setter(instance):
    original = instance.vars
    instance.vars = original
    assert instance.vars == original

@given(instance=while::l::Definition_strategy)
@settings(max_examples=50)
def test_while::l::definition_instantiation(instance):
    assert isinstance(instance, while::l::Definition)

@given(instance=while::l::Function_strategy)
@settings(max_examples=50)
def test_while::l::function_instantiation(instance):
    assert isinstance(instance, while::l::Function)

@given(instance=while::l::Function_strategy)
def test_while::l::function_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=while::l::Function_strategy)
def test_while::l::function_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
