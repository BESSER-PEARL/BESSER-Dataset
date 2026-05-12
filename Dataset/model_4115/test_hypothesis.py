import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    whileCpp_ExprNot,
    whileCpp_ExprEq,
    whileCpp_Expr,
    whileCpp_ExprOr,
    whileCpp_Cons,
    whileCpp_ExprAnd,
    whileCpp_ExprSimple,
    whileCpp_Function,
    whileCpp_Program,
    whileCpp_CommandForEach,
    whileCpp_CommandIf,
    whileCpp_CommandWhile,
    whileCpp_Exprs,
    whileCpp_Command,
    whileCpp_Vars,
    whileCpp_Output,
    whileCpp_Commands,
    whileCpp_Input,
    whileCpp_Definition,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_whilecpp_exprnot_is_not_abstract():
    assert not inspect.isabstract(whileCpp_ExprNot)


def test_whilecpp_exprnot_constructor_exists():
    assert callable(whileCpp_ExprNot.__init__)


def test_whilecpp_exprnot_constructor_args():
    sig = inspect.signature(whileCpp_ExprNot.__init__)
    params = list(sig.parameters.keys())
    assert "not_" in params, "Missing parameter 'not_'"

def test_whilecpp_exprnot_has_not_():
    assert hasattr(whileCpp_ExprNot, "not_")
    descriptor = None
    for klass in whileCpp_ExprNot.__mro__:
        if "not_" in klass.__dict__:
            descriptor = klass.__dict__["not_"]
            break
    assert isinstance(descriptor, property)



def test_whilecpp_expreq_is_not_abstract():
    assert not inspect.isabstract(whileCpp_ExprEq)


def test_whilecpp_expreq_constructor_exists():
    assert callable(whileCpp_ExprEq.__init__)


def test_whilecpp_expreq_constructor_args():
    sig = inspect.signature(whileCpp_ExprEq.__init__)
    params = list(sig.parameters.keys())



def test_whilecpp_expr_is_not_abstract():
    assert not inspect.isabstract(whileCpp_Expr)


def test_whilecpp_expr_constructor_exists():
    assert callable(whileCpp_Expr.__init__)


def test_whilecpp_expr_constructor_args():
    sig = inspect.signature(whileCpp_Expr.__init__)
    params = list(sig.parameters.keys())



def test_whilecpp_expror_is_not_abstract():
    assert not inspect.isabstract(whileCpp_ExprOr)


def test_whilecpp_expror_constructor_exists():
    assert callable(whileCpp_ExprOr.__init__)


def test_whilecpp_expror_constructor_args():
    sig = inspect.signature(whileCpp_ExprOr.__init__)
    params = list(sig.parameters.keys())
    assert "exprOr" in params, "Missing parameter 'exprOr'"

def test_whilecpp_expror_has_exprOr():
    assert hasattr(whileCpp_ExprOr, "exprOr")
    descriptor = None
    for klass in whileCpp_ExprOr.__mro__:
        if "exprOr" in klass.__dict__:
            descriptor = klass.__dict__["exprOr"]
            break
    assert isinstance(descriptor, property)



def test_whilecpp_cons_is_not_abstract():
    assert not inspect.isabstract(whileCpp_Cons)


def test_whilecpp_cons_constructor_exists():
    assert callable(whileCpp_Cons.__init__)


def test_whilecpp_cons_constructor_args():
    sig = inspect.signature(whileCpp_Cons.__init__)
    params = list(sig.parameters.keys())
    assert "exprCons" in params, "Missing parameter 'exprCons'"

def test_whilecpp_cons_has_exprCons():
    assert hasattr(whileCpp_Cons, "exprCons")
    descriptor = None
    for klass in whileCpp_Cons.__mro__:
        if "exprCons" in klass.__dict__:
            descriptor = klass.__dict__["exprCons"]
            break
    assert isinstance(descriptor, property)



def test_whilecpp_exprand_is_not_abstract():
    assert not inspect.isabstract(whileCpp_ExprAnd)


def test_whilecpp_exprand_constructor_exists():
    assert callable(whileCpp_ExprAnd.__init__)


def test_whilecpp_exprand_constructor_args():
    sig = inspect.signature(whileCpp_ExprAnd.__init__)
    params = list(sig.parameters.keys())
    assert "exprAnd" in params, "Missing parameter 'exprAnd'"

def test_whilecpp_exprand_has_exprAnd():
    assert hasattr(whileCpp_ExprAnd, "exprAnd")
    descriptor = None
    for klass in whileCpp_ExprAnd.__mro__:
        if "exprAnd" in klass.__dict__:
            descriptor = klass.__dict__["exprAnd"]
            break
    assert isinstance(descriptor, property)



def test_whilecpp_exprsimple_is_not_abstract():
    assert not inspect.isabstract(whileCpp_ExprSimple)


def test_whilecpp_exprsimple_constructor_exists():
    assert callable(whileCpp_ExprSimple.__init__)


def test_whilecpp_exprsimple_constructor_args():
    sig = inspect.signature(whileCpp_ExprSimple.__init__)
    params = list(sig.parameters.keys())
    assert "vari" in params, "Missing parameter 'vari'"
    assert "exprTail" in params, "Missing parameter 'exprTail'"
    assert "nomSymb" in params, "Missing parameter 'nomSymb'"
    assert "exprHead" in params, "Missing parameter 'exprHead'"
    assert "nil" in params, "Missing parameter 'nil'"
    assert "symb" in params, "Missing parameter 'symb'"

def test_whilecpp_exprsimple_has_vari():
    assert hasattr(whileCpp_ExprSimple, "vari")
    descriptor = None
    for klass in whileCpp_ExprSimple.__mro__:
        if "vari" in klass.__dict__:
            descriptor = klass.__dict__["vari"]
            break
    assert isinstance(descriptor, property)

def test_whilecpp_exprsimple_has_exprTail():
    assert hasattr(whileCpp_ExprSimple, "exprTail")
    descriptor = None
    for klass in whileCpp_ExprSimple.__mro__:
        if "exprTail" in klass.__dict__:
            descriptor = klass.__dict__["exprTail"]
            break
    assert isinstance(descriptor, property)

def test_whilecpp_exprsimple_has_nomSymb():
    assert hasattr(whileCpp_ExprSimple, "nomSymb")
    descriptor = None
    for klass in whileCpp_ExprSimple.__mro__:
        if "nomSymb" in klass.__dict__:
            descriptor = klass.__dict__["nomSymb"]
            break
    assert isinstance(descriptor, property)

def test_whilecpp_exprsimple_has_exprHead():
    assert hasattr(whileCpp_ExprSimple, "exprHead")
    descriptor = None
    for klass in whileCpp_ExprSimple.__mro__:
        if "exprHead" in klass.__dict__:
            descriptor = klass.__dict__["exprHead"]
            break
    assert isinstance(descriptor, property)

def test_whilecpp_exprsimple_has_nil():
    assert hasattr(whileCpp_ExprSimple, "nil")
    descriptor = None
    for klass in whileCpp_ExprSimple.__mro__:
        if "nil" in klass.__dict__:
            descriptor = klass.__dict__["nil"]
            break
    assert isinstance(descriptor, property)

def test_whilecpp_exprsimple_has_symb():
    assert hasattr(whileCpp_ExprSimple, "symb")
    descriptor = None
    for klass in whileCpp_ExprSimple.__mro__:
        if "symb" in klass.__dict__:
            descriptor = klass.__dict__["symb"]
            break
    assert isinstance(descriptor, property)



def test_whilecpp_function_is_not_abstract():
    assert not inspect.isabstract(whileCpp_Function)


def test_whilecpp_function_constructor_exists():
    assert callable(whileCpp_Function.__init__)


def test_whilecpp_function_constructor_args():
    sig = inspect.signature(whileCpp_Function.__init__)
    params = list(sig.parameters.keys())
    assert "nom" in params, "Missing parameter 'nom'"

def test_whilecpp_function_has_nom():
    assert hasattr(whileCpp_Function, "nom")
    descriptor = None
    for klass in whileCpp_Function.__mro__:
        if "nom" in klass.__dict__:
            descriptor = klass.__dict__["nom"]
            break
    assert isinstance(descriptor, property)



def test_whilecpp_program_is_not_abstract():
    assert not inspect.isabstract(whileCpp_Program)


def test_whilecpp_program_constructor_exists():
    assert callable(whileCpp_Program.__init__)


def test_whilecpp_program_constructor_args():
    sig = inspect.signature(whileCpp_Program.__init__)
    params = list(sig.parameters.keys())



def test_whilecpp_commandforeach_is_not_abstract():
    assert not inspect.isabstract(whileCpp_CommandForEach)


def test_whilecpp_commandforeach_constructor_exists():
    assert callable(whileCpp_CommandForEach.__init__)


def test_whilecpp_commandforeach_constructor_args():
    sig = inspect.signature(whileCpp_CommandForEach.__init__)
    params = list(sig.parameters.keys())



def test_whilecpp_commandif_is_not_abstract():
    assert not inspect.isabstract(whileCpp_CommandIf)


def test_whilecpp_commandif_constructor_exists():
    assert callable(whileCpp_CommandIf.__init__)


def test_whilecpp_commandif_constructor_args():
    sig = inspect.signature(whileCpp_CommandIf.__init__)
    params = list(sig.parameters.keys())



def test_whilecpp_commandwhile_is_not_abstract():
    assert not inspect.isabstract(whileCpp_CommandWhile)


def test_whilecpp_commandwhile_constructor_exists():
    assert callable(whileCpp_CommandWhile.__init__)


def test_whilecpp_commandwhile_constructor_args():
    sig = inspect.signature(whileCpp_CommandWhile.__init__)
    params = list(sig.parameters.keys())
    assert "w" in params, "Missing parameter 'w'"

def test_whilecpp_commandwhile_has_w():
    assert hasattr(whileCpp_CommandWhile, "w")
    descriptor = None
    for klass in whileCpp_CommandWhile.__mro__:
        if "w" in klass.__dict__:
            descriptor = klass.__dict__["w"]
            break
    assert isinstance(descriptor, property)



def test_whilecpp_exprs_is_not_abstract():
    assert not inspect.isabstract(whileCpp_Exprs)


def test_whilecpp_exprs_constructor_exists():
    assert callable(whileCpp_Exprs.__init__)


def test_whilecpp_exprs_constructor_args():
    sig = inspect.signature(whileCpp_Exprs.__init__)
    params = list(sig.parameters.keys())



def test_whilecpp_command_is_not_abstract():
    assert not inspect.isabstract(whileCpp_Command)


def test_whilecpp_command_constructor_exists():
    assert callable(whileCpp_Command.__init__)


def test_whilecpp_command_constructor_args():
    sig = inspect.signature(whileCpp_Command.__init__)
    params = list(sig.parameters.keys())
    assert "nop" in params, "Missing parameter 'nop'"

def test_whilecpp_command_has_nop():
    assert hasattr(whileCpp_Command, "nop")
    descriptor = None
    for klass in whileCpp_Command.__mro__:
        if "nop" in klass.__dict__:
            descriptor = klass.__dict__["nop"]
            break
    assert isinstance(descriptor, property)



def test_whilecpp_vars_is_not_abstract():
    assert not inspect.isabstract(whileCpp_Vars)


def test_whilecpp_vars_constructor_exists():
    assert callable(whileCpp_Vars.__init__)


def test_whilecpp_vars_constructor_args():
    sig = inspect.signature(whileCpp_Vars.__init__)
    params = list(sig.parameters.keys())
    assert "varGen" in params, "Missing parameter 'varGen'"

def test_whilecpp_vars_has_varGen():
    assert hasattr(whileCpp_Vars, "varGen")
    descriptor = None
    for klass in whileCpp_Vars.__mro__:
        if "varGen" in klass.__dict__:
            descriptor = klass.__dict__["varGen"]
            break
    assert isinstance(descriptor, property)



def test_whilecpp_output_is_not_abstract():
    assert not inspect.isabstract(whileCpp_Output)


def test_whilecpp_output_constructor_exists():
    assert callable(whileCpp_Output.__init__)


def test_whilecpp_output_constructor_args():
    sig = inspect.signature(whileCpp_Output.__init__)
    params = list(sig.parameters.keys())
    assert "varOut" in params, "Missing parameter 'varOut'"

def test_whilecpp_output_has_varOut():
    assert hasattr(whileCpp_Output, "varOut")
    descriptor = None
    for klass in whileCpp_Output.__mro__:
        if "varOut" in klass.__dict__:
            descriptor = klass.__dict__["varOut"]
            break
    assert isinstance(descriptor, property)



def test_whilecpp_commands_is_not_abstract():
    assert not inspect.isabstract(whileCpp_Commands)


def test_whilecpp_commands_constructor_exists():
    assert callable(whileCpp_Commands.__init__)


def test_whilecpp_commands_constructor_args():
    sig = inspect.signature(whileCpp_Commands.__init__)
    params = list(sig.parameters.keys())



def test_whilecpp_input_is_not_abstract():
    assert not inspect.isabstract(whileCpp_Input)


def test_whilecpp_input_constructor_exists():
    assert callable(whileCpp_Input.__init__)


def test_whilecpp_input_constructor_args():
    sig = inspect.signature(whileCpp_Input.__init__)
    params = list(sig.parameters.keys())
    assert "varIn" in params, "Missing parameter 'varIn'"

def test_whilecpp_input_has_varIn():
    assert hasattr(whileCpp_Input, "varIn")
    descriptor = None
    for klass in whileCpp_Input.__mro__:
        if "varIn" in klass.__dict__:
            descriptor = klass.__dict__["varIn"]
            break
    assert isinstance(descriptor, property)



def test_whilecpp_definition_is_not_abstract():
    assert not inspect.isabstract(whileCpp_Definition)


def test_whilecpp_definition_constructor_exists():
    assert callable(whileCpp_Definition.__init__)


def test_whilecpp_definition_constructor_args():
    sig = inspect.signature(whileCpp_Definition.__init__)
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
whileCpp_ExprNot_strategy = st.builds(
    whileCpp_ExprNot,
    not_=
        safe_text
)
whileCpp_ExprEq_strategy = st.builds(
    whileCpp_ExprEq,
)
whileCpp_Expr_strategy = st.builds(
    whileCpp_Expr,
)
whileCpp_ExprOr_strategy = st.builds(
    whileCpp_ExprOr,
    exprOr=
        safe_text
)
whileCpp_Cons_strategy = st.builds(
    whileCpp_Cons,
    exprCons=
        safe_text
)
whileCpp_ExprAnd_strategy = st.builds(
    whileCpp_ExprAnd,
    exprAnd=
        safe_text
)
whileCpp_ExprSimple_strategy = st.builds(
    whileCpp_ExprSimple,
    vari=
        safe_text,
    exprTail=
        safe_text,
    nomSymb=
        safe_text,
    exprHead=
        safe_text,
    nil=
        safe_text,
    symb=
        safe_text
)
whileCpp_Function_strategy = st.builds(
    whileCpp_Function,
    nom=
        safe_text
)
whileCpp_Program_strategy = st.builds(
    whileCpp_Program,
)
whileCpp_CommandForEach_strategy = st.builds(
    whileCpp_CommandForEach,
)
whileCpp_CommandIf_strategy = st.builds(
    whileCpp_CommandIf,
)
whileCpp_CommandWhile_strategy = st.builds(
    whileCpp_CommandWhile,
    w=
        safe_text
)
whileCpp_Exprs_strategy = st.builds(
    whileCpp_Exprs,
)
whileCpp_Command_strategy = st.builds(
    whileCpp_Command,
    nop=
        safe_text
)
whileCpp_Vars_strategy = st.builds(
    whileCpp_Vars,
    varGen=
        safe_text
)
whileCpp_Output_strategy = st.builds(
    whileCpp_Output,
    varOut=
        safe_text
)
whileCpp_Commands_strategy = st.builds(
    whileCpp_Commands,
)
whileCpp_Input_strategy = st.builds(
    whileCpp_Input,
    varIn=
        safe_text
)
whileCpp_Definition_strategy = st.builds(
    whileCpp_Definition,
)

@given(instance=whileCpp_ExprNot_strategy)
@settings(max_examples=50)
def test_whilecpp_exprnot_instantiation(instance):
    assert isinstance(instance, whileCpp_ExprNot)



@given(instance=whileCpp_ExprNot_strategy)
def test_whilecpp_exprnot_not__setter(instance):
    original = instance.not_
    instance.not_ = original
    assert instance.not_ == original

@given(instance=whileCpp_ExprEq_strategy)
@settings(max_examples=50)
def test_whilecpp_expreq_instantiation(instance):
    assert isinstance(instance, whileCpp_ExprEq)

@given(instance=whileCpp_Expr_strategy)
@settings(max_examples=50)
def test_whilecpp_expr_instantiation(instance):
    assert isinstance(instance, whileCpp_Expr)

@given(instance=whileCpp_ExprOr_strategy)
@settings(max_examples=50)
def test_whilecpp_expror_instantiation(instance):
    assert isinstance(instance, whileCpp_ExprOr)



@given(instance=whileCpp_ExprOr_strategy)
def test_whilecpp_expror_exprOr_setter(instance):
    original = instance.exprOr
    instance.exprOr = original
    assert instance.exprOr == original

@given(instance=whileCpp_Cons_strategy)
@settings(max_examples=50)
def test_whilecpp_cons_instantiation(instance):
    assert isinstance(instance, whileCpp_Cons)



@given(instance=whileCpp_Cons_strategy)
def test_whilecpp_cons_exprCons_setter(instance):
    original = instance.exprCons
    instance.exprCons = original
    assert instance.exprCons == original

@given(instance=whileCpp_ExprAnd_strategy)
@settings(max_examples=50)
def test_whilecpp_exprand_instantiation(instance):
    assert isinstance(instance, whileCpp_ExprAnd)



@given(instance=whileCpp_ExprAnd_strategy)
def test_whilecpp_exprand_exprAnd_setter(instance):
    original = instance.exprAnd
    instance.exprAnd = original
    assert instance.exprAnd == original

@given(instance=whileCpp_ExprSimple_strategy)
@settings(max_examples=50)
def test_whilecpp_exprsimple_instantiation(instance):
    assert isinstance(instance, whileCpp_ExprSimple)



@given(instance=whileCpp_ExprSimple_strategy)
def test_whilecpp_exprsimple_vari_setter(instance):
    original = instance.vari
    instance.vari = original
    assert instance.vari == original



@given(instance=whileCpp_ExprSimple_strategy)
def test_whilecpp_exprsimple_exprTail_setter(instance):
    original = instance.exprTail
    instance.exprTail = original
    assert instance.exprTail == original



@given(instance=whileCpp_ExprSimple_strategy)
def test_whilecpp_exprsimple_nomSymb_setter(instance):
    original = instance.nomSymb
    instance.nomSymb = original
    assert instance.nomSymb == original



@given(instance=whileCpp_ExprSimple_strategy)
def test_whilecpp_exprsimple_exprHead_setter(instance):
    original = instance.exprHead
    instance.exprHead = original
    assert instance.exprHead == original



@given(instance=whileCpp_ExprSimple_strategy)
def test_whilecpp_exprsimple_nil_setter(instance):
    original = instance.nil
    instance.nil = original
    assert instance.nil == original



@given(instance=whileCpp_ExprSimple_strategy)
def test_whilecpp_exprsimple_symb_setter(instance):
    original = instance.symb
    instance.symb = original
    assert instance.symb == original

@given(instance=whileCpp_Function_strategy)
@settings(max_examples=50)
def test_whilecpp_function_instantiation(instance):
    assert isinstance(instance, whileCpp_Function)



@given(instance=whileCpp_Function_strategy)
def test_whilecpp_function_nom_setter(instance):
    original = instance.nom
    instance.nom = original
    assert instance.nom == original

@given(instance=whileCpp_Program_strategy)
@settings(max_examples=50)
def test_whilecpp_program_instantiation(instance):
    assert isinstance(instance, whileCpp_Program)

@given(instance=whileCpp_CommandForEach_strategy)
@settings(max_examples=50)
def test_whilecpp_commandforeach_instantiation(instance):
    assert isinstance(instance, whileCpp_CommandForEach)

@given(instance=whileCpp_CommandIf_strategy)
@settings(max_examples=50)
def test_whilecpp_commandif_instantiation(instance):
    assert isinstance(instance, whileCpp_CommandIf)

@given(instance=whileCpp_CommandWhile_strategy)
@settings(max_examples=50)
def test_whilecpp_commandwhile_instantiation(instance):
    assert isinstance(instance, whileCpp_CommandWhile)



@given(instance=whileCpp_CommandWhile_strategy)
def test_whilecpp_commandwhile_w_setter(instance):
    original = instance.w
    instance.w = original
    assert instance.w == original

@given(instance=whileCpp_Exprs_strategy)
@settings(max_examples=50)
def test_whilecpp_exprs_instantiation(instance):
    assert isinstance(instance, whileCpp_Exprs)

@given(instance=whileCpp_Command_strategy)
@settings(max_examples=50)
def test_whilecpp_command_instantiation(instance):
    assert isinstance(instance, whileCpp_Command)



@given(instance=whileCpp_Command_strategy)
def test_whilecpp_command_nop_setter(instance):
    original = instance.nop
    instance.nop = original
    assert instance.nop == original

@given(instance=whileCpp_Vars_strategy)
@settings(max_examples=50)
def test_whilecpp_vars_instantiation(instance):
    assert isinstance(instance, whileCpp_Vars)



@given(instance=whileCpp_Vars_strategy)
def test_whilecpp_vars_varGen_setter(instance):
    original = instance.varGen
    instance.varGen = original
    assert instance.varGen == original

@given(instance=whileCpp_Output_strategy)
@settings(max_examples=50)
def test_whilecpp_output_instantiation(instance):
    assert isinstance(instance, whileCpp_Output)



@given(instance=whileCpp_Output_strategy)
def test_whilecpp_output_varOut_setter(instance):
    original = instance.varOut
    instance.varOut = original
    assert instance.varOut == original

@given(instance=whileCpp_Commands_strategy)
@settings(max_examples=50)
def test_whilecpp_commands_instantiation(instance):
    assert isinstance(instance, whileCpp_Commands)

@given(instance=whileCpp_Input_strategy)
@settings(max_examples=50)
def test_whilecpp_input_instantiation(instance):
    assert isinstance(instance, whileCpp_Input)



@given(instance=whileCpp_Input_strategy)
def test_whilecpp_input_varIn_setter(instance):
    original = instance.varIn
    instance.varIn = original
    assert instance.varIn == original

@given(instance=whileCpp_Definition_strategy)
@settings(max_examples=50)
def test_whilecpp_definition_instantiation(instance):
    assert isinstance(instance, whileCpp_Definition)
