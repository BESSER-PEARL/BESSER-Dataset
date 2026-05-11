import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    whileCpp::Vars,
    whileCpp::Output,
    whileCpp::Commands,
    whileCpp::Input,
    whileCpp::Definition,
    whileCpp::ExprNot,
    whileCpp::ExprEq,
    whileCpp::Expr,
    whileCpp::ExprOr,
    whileCpp::Cons,
    whileCpp::ExprAnd,
    whileCpp::ExprSimple,
    whileCpp::Function,
    whileCpp::Program,
    whileCpp::CommandForEach,
    whileCpp::CommandIf,
    whileCpp::CommandWhile,
    whileCpp::Exprs,
    whileCpp::Command,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_whilecpp::vars_is_not_abstract():
    assert not inspect.isabstract(whileCpp::Vars)


def test_whilecpp::vars_constructor_exists():
    assert callable(whileCpp::Vars.__init__)


def test_whilecpp::vars_constructor_args():
    sig = inspect.signature(whileCpp::Vars.__init__)
    params = list(sig.parameters.keys())
    assert "varGen" in params, "Missing parameter 'varGen'"

def test_whilecpp::vars_has_varGen():
    assert hasattr(whileCpp::Vars, "varGen")
    descriptor = None
    for klass in whileCpp::Vars.__mro__:
        if "varGen" in klass.__dict__:
            descriptor = klass.__dict__["varGen"]
            break
    assert isinstance(descriptor, property)



def test_whilecpp::output_is_not_abstract():
    assert not inspect.isabstract(whileCpp::Output)


def test_whilecpp::output_constructor_exists():
    assert callable(whileCpp::Output.__init__)


def test_whilecpp::output_constructor_args():
    sig = inspect.signature(whileCpp::Output.__init__)
    params = list(sig.parameters.keys())
    assert "varOut" in params, "Missing parameter 'varOut'"

def test_whilecpp::output_has_varOut():
    assert hasattr(whileCpp::Output, "varOut")
    descriptor = None
    for klass in whileCpp::Output.__mro__:
        if "varOut" in klass.__dict__:
            descriptor = klass.__dict__["varOut"]
            break
    assert isinstance(descriptor, property)



def test_whilecpp::commands_is_not_abstract():
    assert not inspect.isabstract(whileCpp::Commands)


def test_whilecpp::commands_constructor_exists():
    assert callable(whileCpp::Commands.__init__)


def test_whilecpp::commands_constructor_args():
    sig = inspect.signature(whileCpp::Commands.__init__)
    params = list(sig.parameters.keys())



def test_whilecpp::input_is_not_abstract():
    assert not inspect.isabstract(whileCpp::Input)


def test_whilecpp::input_constructor_exists():
    assert callable(whileCpp::Input.__init__)


def test_whilecpp::input_constructor_args():
    sig = inspect.signature(whileCpp::Input.__init__)
    params = list(sig.parameters.keys())
    assert "varIn" in params, "Missing parameter 'varIn'"

def test_whilecpp::input_has_varIn():
    assert hasattr(whileCpp::Input, "varIn")
    descriptor = None
    for klass in whileCpp::Input.__mro__:
        if "varIn" in klass.__dict__:
            descriptor = klass.__dict__["varIn"]
            break
    assert isinstance(descriptor, property)



def test_whilecpp::definition_is_not_abstract():
    assert not inspect.isabstract(whileCpp::Definition)


def test_whilecpp::definition_constructor_exists():
    assert callable(whileCpp::Definition.__init__)


def test_whilecpp::definition_constructor_args():
    sig = inspect.signature(whileCpp::Definition.__init__)
    params = list(sig.parameters.keys())



def test_whilecpp::exprnot_is_not_abstract():
    assert not inspect.isabstract(whileCpp::ExprNot)


def test_whilecpp::exprnot_constructor_exists():
    assert callable(whileCpp::ExprNot.__init__)


def test_whilecpp::exprnot_constructor_args():
    sig = inspect.signature(whileCpp::ExprNot.__init__)
    params = list(sig.parameters.keys())
    assert "not_" in params, "Missing parameter 'not_'"

def test_whilecpp::exprnot_has_not_():
    assert hasattr(whileCpp::ExprNot, "not_")
    descriptor = None
    for klass in whileCpp::ExprNot.__mro__:
        if "not_" in klass.__dict__:
            descriptor = klass.__dict__["not_"]
            break
    assert isinstance(descriptor, property)



def test_whilecpp::expreq_is_not_abstract():
    assert not inspect.isabstract(whileCpp::ExprEq)


def test_whilecpp::expreq_constructor_exists():
    assert callable(whileCpp::ExprEq.__init__)


def test_whilecpp::expreq_constructor_args():
    sig = inspect.signature(whileCpp::ExprEq.__init__)
    params = list(sig.parameters.keys())



def test_whilecpp::expr_is_not_abstract():
    assert not inspect.isabstract(whileCpp::Expr)


def test_whilecpp::expr_constructor_exists():
    assert callable(whileCpp::Expr.__init__)


def test_whilecpp::expr_constructor_args():
    sig = inspect.signature(whileCpp::Expr.__init__)
    params = list(sig.parameters.keys())



def test_whilecpp::expror_is_not_abstract():
    assert not inspect.isabstract(whileCpp::ExprOr)


def test_whilecpp::expror_constructor_exists():
    assert callable(whileCpp::ExprOr.__init__)


def test_whilecpp::expror_constructor_args():
    sig = inspect.signature(whileCpp::ExprOr.__init__)
    params = list(sig.parameters.keys())
    assert "exprOr" in params, "Missing parameter 'exprOr'"

def test_whilecpp::expror_has_exprOr():
    assert hasattr(whileCpp::ExprOr, "exprOr")
    descriptor = None
    for klass in whileCpp::ExprOr.__mro__:
        if "exprOr" in klass.__dict__:
            descriptor = klass.__dict__["exprOr"]
            break
    assert isinstance(descriptor, property)



def test_whilecpp::cons_is_not_abstract():
    assert not inspect.isabstract(whileCpp::Cons)


def test_whilecpp::cons_constructor_exists():
    assert callable(whileCpp::Cons.__init__)


def test_whilecpp::cons_constructor_args():
    sig = inspect.signature(whileCpp::Cons.__init__)
    params = list(sig.parameters.keys())
    assert "exprCons" in params, "Missing parameter 'exprCons'"

def test_whilecpp::cons_has_exprCons():
    assert hasattr(whileCpp::Cons, "exprCons")
    descriptor = None
    for klass in whileCpp::Cons.__mro__:
        if "exprCons" in klass.__dict__:
            descriptor = klass.__dict__["exprCons"]
            break
    assert isinstance(descriptor, property)



def test_whilecpp::exprand_is_not_abstract():
    assert not inspect.isabstract(whileCpp::ExprAnd)


def test_whilecpp::exprand_constructor_exists():
    assert callable(whileCpp::ExprAnd.__init__)


def test_whilecpp::exprand_constructor_args():
    sig = inspect.signature(whileCpp::ExprAnd.__init__)
    params = list(sig.parameters.keys())
    assert "exprAnd" in params, "Missing parameter 'exprAnd'"

def test_whilecpp::exprand_has_exprAnd():
    assert hasattr(whileCpp::ExprAnd, "exprAnd")
    descriptor = None
    for klass in whileCpp::ExprAnd.__mro__:
        if "exprAnd" in klass.__dict__:
            descriptor = klass.__dict__["exprAnd"]
            break
    assert isinstance(descriptor, property)



def test_whilecpp::exprsimple_is_not_abstract():
    assert not inspect.isabstract(whileCpp::ExprSimple)


def test_whilecpp::exprsimple_constructor_exists():
    assert callable(whileCpp::ExprSimple.__init__)


def test_whilecpp::exprsimple_constructor_args():
    sig = inspect.signature(whileCpp::ExprSimple.__init__)
    params = list(sig.parameters.keys())
    assert "vari" in params, "Missing parameter 'vari'"
    assert "nil" in params, "Missing parameter 'nil'"
    assert "exprHead" in params, "Missing parameter 'exprHead'"
    assert "symb" in params, "Missing parameter 'symb'"
    assert "nomSymb" in params, "Missing parameter 'nomSymb'"
    assert "exprTail" in params, "Missing parameter 'exprTail'"

def test_whilecpp::exprsimple_has_vari():
    assert hasattr(whileCpp::ExprSimple, "vari")
    descriptor = None
    for klass in whileCpp::ExprSimple.__mro__:
        if "vari" in klass.__dict__:
            descriptor = klass.__dict__["vari"]
            break
    assert isinstance(descriptor, property)

def test_whilecpp::exprsimple_has_nil():
    assert hasattr(whileCpp::ExprSimple, "nil")
    descriptor = None
    for klass in whileCpp::ExprSimple.__mro__:
        if "nil" in klass.__dict__:
            descriptor = klass.__dict__["nil"]
            break
    assert isinstance(descriptor, property)

def test_whilecpp::exprsimple_has_exprHead():
    assert hasattr(whileCpp::ExprSimple, "exprHead")
    descriptor = None
    for klass in whileCpp::ExprSimple.__mro__:
        if "exprHead" in klass.__dict__:
            descriptor = klass.__dict__["exprHead"]
            break
    assert isinstance(descriptor, property)

def test_whilecpp::exprsimple_has_symb():
    assert hasattr(whileCpp::ExprSimple, "symb")
    descriptor = None
    for klass in whileCpp::ExprSimple.__mro__:
        if "symb" in klass.__dict__:
            descriptor = klass.__dict__["symb"]
            break
    assert isinstance(descriptor, property)

def test_whilecpp::exprsimple_has_nomSymb():
    assert hasattr(whileCpp::ExprSimple, "nomSymb")
    descriptor = None
    for klass in whileCpp::ExprSimple.__mro__:
        if "nomSymb" in klass.__dict__:
            descriptor = klass.__dict__["nomSymb"]
            break
    assert isinstance(descriptor, property)

def test_whilecpp::exprsimple_has_exprTail():
    assert hasattr(whileCpp::ExprSimple, "exprTail")
    descriptor = None
    for klass in whileCpp::ExprSimple.__mro__:
        if "exprTail" in klass.__dict__:
            descriptor = klass.__dict__["exprTail"]
            break
    assert isinstance(descriptor, property)



def test_whilecpp::function_is_not_abstract():
    assert not inspect.isabstract(whileCpp::Function)


def test_whilecpp::function_constructor_exists():
    assert callable(whileCpp::Function.__init__)


def test_whilecpp::function_constructor_args():
    sig = inspect.signature(whileCpp::Function.__init__)
    params = list(sig.parameters.keys())
    assert "nom" in params, "Missing parameter 'nom'"

def test_whilecpp::function_has_nom():
    assert hasattr(whileCpp::Function, "nom")
    descriptor = None
    for klass in whileCpp::Function.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)



def test_whilecpp::program_is_not_abstract():
    assert not inspect.isabstract(whileCpp::Program)


def test_whilecpp::program_constructor_exists():
    assert callable(whileCpp::Program.__init__)


def test_whilecpp::program_constructor_args():
    sig = inspect.signature(whileCpp::Program.__init__)
    params = list(sig.parameters.keys())



def test_whilecpp::commandforeach_is_not_abstract():
    assert not inspect.isabstract(whileCpp::CommandForEach)


def test_whilecpp::commandforeach_constructor_exists():
    assert callable(whileCpp::CommandForEach.__init__)


def test_whilecpp::commandforeach_constructor_args():
    sig = inspect.signature(whileCpp::CommandForEach.__init__)
    params = list(sig.parameters.keys())



def test_whilecpp::commandif_is_not_abstract():
    assert not inspect.isabstract(whileCpp::CommandIf)


def test_whilecpp::commandif_constructor_exists():
    assert callable(whileCpp::CommandIf.__init__)


def test_whilecpp::commandif_constructor_args():
    sig = inspect.signature(whileCpp::CommandIf.__init__)
    params = list(sig.parameters.keys())



def test_whilecpp::commandwhile_is_not_abstract():
    assert not inspect.isabstract(whileCpp::CommandWhile)


def test_whilecpp::commandwhile_constructor_exists():
    assert callable(whileCpp::CommandWhile.__init__)


def test_whilecpp::commandwhile_constructor_args():
    sig = inspect.signature(whileCpp::CommandWhile.__init__)
    params = list(sig.parameters.keys())
    assert "w" in params, "Missing parameter 'w'"

def test_whilecpp::commandwhile_has_w():
    assert hasattr(whileCpp::CommandWhile, "w")
    descriptor = None
    for klass in whileCpp::CommandWhile.__mro__:
        if "w" in klass.__dict__:
            descriptor = klass.__dict__["w"]
            break
    assert isinstance(descriptor, property)



def test_whilecpp::exprs_is_not_abstract():
    assert not inspect.isabstract(whileCpp::Exprs)


def test_whilecpp::exprs_constructor_exists():
    assert callable(whileCpp::Exprs.__init__)


def test_whilecpp::exprs_constructor_args():
    sig = inspect.signature(whileCpp::Exprs.__init__)
    params = list(sig.parameters.keys())



def test_whilecpp::command_is_not_abstract():
    assert not inspect.isabstract(whileCpp::Command)


def test_whilecpp::command_constructor_exists():
    assert callable(whileCpp::Command.__init__)


def test_whilecpp::command_constructor_args():
    sig = inspect.signature(whileCpp::Command.__init__)
    params = list(sig.parameters.keys())
    assert "nop" in params, "Missing parameter 'nop'"

def test_whilecpp::command_has_nop():
    assert hasattr(whileCpp::Command, "nop")
    descriptor = None
    for klass in whileCpp::Command.__mro__:
        if "nop" in klass.__dict__:
            descriptor = klass.__dict__["nop"]
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
whileCpp::Vars_strategy = st.builds(
    whileCpp::Vars,
    varGen=
        safe_text
)
whileCpp::Output_strategy = st.builds(
    whileCpp::Output,
    varOut=
        safe_text
)
whileCpp::Commands_strategy = st.builds(
    whileCpp::Commands,
)
whileCpp::Input_strategy = st.builds(
    whileCpp::Input,
    varIn=
        safe_text
)
whileCpp::Definition_strategy = st.builds(
    whileCpp::Definition,
)
whileCpp::ExprNot_strategy = st.builds(
    whileCpp::ExprNot,
    not_=
        safe_text
)
whileCpp::ExprEq_strategy = st.builds(
    whileCpp::ExprEq,
)
whileCpp::Expr_strategy = st.builds(
    whileCpp::Expr,
)
whileCpp::ExprOr_strategy = st.builds(
    whileCpp::ExprOr,
    exprOr=
        safe_text
)
whileCpp::Cons_strategy = st.builds(
    whileCpp::Cons,
    exprCons=
        safe_text
)
whileCpp::ExprAnd_strategy = st.builds(
    whileCpp::ExprAnd,
    exprAnd=
        safe_text
)
whileCpp::ExprSimple_strategy = st.builds(
    whileCpp::ExprSimple,
    vari=
        safe_text,
    nil=
        safe_text,
    exprHead=
        safe_text,
    symb=
        safe_text,
    nomSymb=
        safe_text,
    exprTail=
        safe_text
)
whileCpp::Function_strategy = st.builds(
    whileCpp::Function,
    nom=
        safe_text
)
whileCpp::Program_strategy = st.builds(
    whileCpp::Program,
)
whileCpp::CommandForEach_strategy = st.builds(
    whileCpp::CommandForEach,
)
whileCpp::CommandIf_strategy = st.builds(
    whileCpp::CommandIf,
)
whileCpp::CommandWhile_strategy = st.builds(
    whileCpp::CommandWhile,
    w=
        safe_text
)
whileCpp::Exprs_strategy = st.builds(
    whileCpp::Exprs,
)
whileCpp::Command_strategy = st.builds(
    whileCpp::Command,
    nop=
        safe_text
)

@given(instance=whileCpp::Vars_strategy)
@settings(max_examples=50)
def test_whilecpp::vars_instantiation(instance):
    assert isinstance(instance, whileCpp::Vars)

@given(instance=whileCpp::Vars_strategy)
def test_whilecpp::vars_varGen_type(instance):
    assert isinstance(instance.varGen, str)


@given(instance=whileCpp::Vars_strategy)
def test_whilecpp::vars_varGen_setter(instance):
    original = instance.varGen
    instance.varGen = original
    assert instance.varGen == original

@given(instance=whileCpp::Output_strategy)
@settings(max_examples=50)
def test_whilecpp::output_instantiation(instance):
    assert isinstance(instance, whileCpp::Output)

@given(instance=whileCpp::Output_strategy)
def test_whilecpp::output_varOut_type(instance):
    assert isinstance(instance.varOut, str)


@given(instance=whileCpp::Output_strategy)
def test_whilecpp::output_varOut_setter(instance):
    original = instance.varOut
    instance.varOut = original
    assert instance.varOut == original

@given(instance=whileCpp::Commands_strategy)
@settings(max_examples=50)
def test_whilecpp::commands_instantiation(instance):
    assert isinstance(instance, whileCpp::Commands)

@given(instance=whileCpp::Input_strategy)
@settings(max_examples=50)
def test_whilecpp::input_instantiation(instance):
    assert isinstance(instance, whileCpp::Input)

@given(instance=whileCpp::Input_strategy)
def test_whilecpp::input_varIn_type(instance):
    assert isinstance(instance.varIn, str)


@given(instance=whileCpp::Input_strategy)
def test_whilecpp::input_varIn_setter(instance):
    original = instance.varIn
    instance.varIn = original
    assert instance.varIn == original

@given(instance=whileCpp::Definition_strategy)
@settings(max_examples=50)
def test_whilecpp::definition_instantiation(instance):
    assert isinstance(instance, whileCpp::Definition)

@given(instance=whileCpp::ExprNot_strategy)
@settings(max_examples=50)
def test_whilecpp::exprnot_instantiation(instance):
    assert isinstance(instance, whileCpp::ExprNot)

@given(instance=whileCpp::ExprNot_strategy)
def test_whilecpp::exprnot_not__type(instance):
    assert isinstance(instance.not_, str)


@given(instance=whileCpp::ExprNot_strategy)
def test_whilecpp::exprnot_not__setter(instance):
    original = instance.not_
    instance.not_ = original
    assert instance.not_ == original

@given(instance=whileCpp::ExprEq_strategy)
@settings(max_examples=50)
def test_whilecpp::expreq_instantiation(instance):
    assert isinstance(instance, whileCpp::ExprEq)

@given(instance=whileCpp::Expr_strategy)
@settings(max_examples=50)
def test_whilecpp::expr_instantiation(instance):
    assert isinstance(instance, whileCpp::Expr)

@given(instance=whileCpp::ExprOr_strategy)
@settings(max_examples=50)
def test_whilecpp::expror_instantiation(instance):
    assert isinstance(instance, whileCpp::ExprOr)

@given(instance=whileCpp::ExprOr_strategy)
def test_whilecpp::expror_exprOr_type(instance):
    assert isinstance(instance.exprOr, str)


@given(instance=whileCpp::ExprOr_strategy)
def test_whilecpp::expror_exprOr_setter(instance):
    original = instance.exprOr
    instance.exprOr = original
    assert instance.exprOr == original

@given(instance=whileCpp::Cons_strategy)
@settings(max_examples=50)
def test_whilecpp::cons_instantiation(instance):
    assert isinstance(instance, whileCpp::Cons)

@given(instance=whileCpp::Cons_strategy)
def test_whilecpp::cons_exprCons_type(instance):
    assert isinstance(instance.exprCons, str)


@given(instance=whileCpp::Cons_strategy)
def test_whilecpp::cons_exprCons_setter(instance):
    original = instance.exprCons
    instance.exprCons = original
    assert instance.exprCons == original

@given(instance=whileCpp::ExprAnd_strategy)
@settings(max_examples=50)
def test_whilecpp::exprand_instantiation(instance):
    assert isinstance(instance, whileCpp::ExprAnd)

@given(instance=whileCpp::ExprAnd_strategy)
def test_whilecpp::exprand_exprAnd_type(instance):
    assert isinstance(instance.exprAnd, str)


@given(instance=whileCpp::ExprAnd_strategy)
def test_whilecpp::exprand_exprAnd_setter(instance):
    original = instance.exprAnd
    instance.exprAnd = original
    assert instance.exprAnd == original

@given(instance=whileCpp::ExprSimple_strategy)
@settings(max_examples=50)
def test_whilecpp::exprsimple_instantiation(instance):
    assert isinstance(instance, whileCpp::ExprSimple)

@given(instance=whileCpp::ExprSimple_strategy)
def test_whilecpp::exprsimple_vari_type(instance):
    assert isinstance(instance.vari, str)


@given(instance=whileCpp::ExprSimple_strategy)
def test_whilecpp::exprsimple_vari_setter(instance):
    original = instance.vari
    instance.vari = original
    assert instance.vari == original

@given(instance=whileCpp::ExprSimple_strategy)
def test_whilecpp::exprsimple_nil_type(instance):
    assert isinstance(instance.nil, str)


@given(instance=whileCpp::ExprSimple_strategy)
def test_whilecpp::exprsimple_nil_setter(instance):
    original = instance.nil
    instance.nil = original
    assert instance.nil == original

@given(instance=whileCpp::ExprSimple_strategy)
def test_whilecpp::exprsimple_exprHead_type(instance):
    assert isinstance(instance.exprHead, str)


@given(instance=whileCpp::ExprSimple_strategy)
def test_whilecpp::exprsimple_exprHead_setter(instance):
    original = instance.exprHead
    instance.exprHead = original
    assert instance.exprHead == original

@given(instance=whileCpp::ExprSimple_strategy)
def test_whilecpp::exprsimple_symb_type(instance):
    assert isinstance(instance.symb, str)


@given(instance=whileCpp::ExprSimple_strategy)
def test_whilecpp::exprsimple_symb_setter(instance):
    original = instance.symb
    instance.symb = original
    assert instance.symb == original

@given(instance=whileCpp::ExprSimple_strategy)
def test_whilecpp::exprsimple_nomSymb_type(instance):
    assert isinstance(instance.nomSymb, str)


@given(instance=whileCpp::ExprSimple_strategy)
def test_whilecpp::exprsimple_nomSymb_setter(instance):
    original = instance.nomSymb
    instance.nomSymb = original
    assert instance.nomSymb == original

@given(instance=whileCpp::ExprSimple_strategy)
def test_whilecpp::exprsimple_exprTail_type(instance):
    assert isinstance(instance.exprTail, str)


@given(instance=whileCpp::ExprSimple_strategy)
def test_whilecpp::exprsimple_exprTail_setter(instance):
    original = instance.exprTail
    instance.exprTail = original
    assert instance.exprTail == original

@given(instance=whileCpp::Function_strategy)
@settings(max_examples=50)
def test_whilecpp::function_instantiation(instance):
    assert isinstance(instance, whileCpp::Function)

@given(instance=whileCpp::Function_strategy)
def test_whilecpp::function_nom_type(instance):
    assert isinstance(instance.nom, str)


@given(instance=whileCpp::Function_strategy)
def test_whilecpp::function_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original

@given(instance=whileCpp::Program_strategy)
@settings(max_examples=50)
def test_whilecpp::program_instantiation(instance):
    assert isinstance(instance, whileCpp::Program)

@given(instance=whileCpp::CommandForEach_strategy)
@settings(max_examples=50)
def test_whilecpp::commandforeach_instantiation(instance):
    assert isinstance(instance, whileCpp::CommandForEach)

@given(instance=whileCpp::CommandIf_strategy)
@settings(max_examples=50)
def test_whilecpp::commandif_instantiation(instance):
    assert isinstance(instance, whileCpp::CommandIf)

@given(instance=whileCpp::CommandWhile_strategy)
@settings(max_examples=50)
def test_whilecpp::commandwhile_instantiation(instance):
    assert isinstance(instance, whileCpp::CommandWhile)

@given(instance=whileCpp::CommandWhile_strategy)
def test_whilecpp::commandwhile_w_type(instance):
    assert isinstance(instance.w, str)


@given(instance=whileCpp::CommandWhile_strategy)
def test_whilecpp::commandwhile_w_setter(instance):
    original = instance.w
    instance.w = original
    assert instance.w == original

@given(instance=whileCpp::Exprs_strategy)
@settings(max_examples=50)
def test_whilecpp::exprs_instantiation(instance):
    assert isinstance(instance, whileCpp::Exprs)

@given(instance=whileCpp::Command_strategy)
@settings(max_examples=50)
def test_whilecpp::command_instantiation(instance):
    assert isinstance(instance, whileCpp::Command)

@given(instance=whileCpp::Command_strategy)
def test_whilecpp::command_nop_type(instance):
    assert isinstance(instance.nop, str)


@given(instance=whileCpp::Command_strategy)
def test_whilecpp::command_nop_setter(instance):
    original = instance.nop
    instance.nop = original
    assert instance.nop == original
