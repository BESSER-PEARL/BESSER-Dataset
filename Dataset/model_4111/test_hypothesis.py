import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Expr,
    wh_ExprTl,
    wh_ExprSym,
    wh_ExprCons,
    wh_ExprEq,
    wh_ExprAnd,
    wh_ExprList,
    wh_ExprHd,
    wh_ExprNot,
    wh_ExprSimple,
    wh_While,
    wh_For,
    wh_Affect,
    wh_Nop,
    wh_Expr,
    wh_If,
    wh_EObject,
    wh_Command,
    wh_ExprOr,
    wh_Commands,
    wh_Input,
    wh_Definition,
    wh_Function,
    wh_Program,
    wh_Wh,
    wh_Output,
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



def test_wh_exprtl_is_not_abstract():
    assert not inspect.isabstract(wh_ExprTl)


def test_wh_exprtl_constructor_exists():
    assert callable(wh_ExprTl.__init__)


def test_wh_exprtl_constructor_args():
    sig = inspect.signature(wh_ExprTl.__init__)
    params = list(sig.parameters.keys())



def test_wh_exprsym_is_not_abstract():
    assert not inspect.isabstract(wh_ExprSym)


def test_wh_exprsym_constructor_exists():
    assert callable(wh_ExprSym.__init__)


def test_wh_exprsym_constructor_args():
    sig = inspect.signature(wh_ExprSym.__init__)
    params = list(sig.parameters.keys())
    assert "arg1" in params, "Missing parameter 'arg1'"

def test_wh_exprsym_has_arg1():
    assert hasattr(wh_ExprSym, "arg1")
    descriptor = None
    for klass in wh_ExprSym.__mro__:
        if "arg1" in klass.__dict__:
            descriptor = klass.__dict__["arg1"]
            break
    assert isinstance(descriptor, property)



def test_wh_exprcons_is_not_abstract():
    assert not inspect.isabstract(wh_ExprCons)


def test_wh_exprcons_constructor_exists():
    assert callable(wh_ExprCons.__init__)


def test_wh_exprcons_constructor_args():
    sig = inspect.signature(wh_ExprCons.__init__)
    params = list(sig.parameters.keys())



def test_wh_expreq_is_not_abstract():
    assert not inspect.isabstract(wh_ExprEq)


def test_wh_expreq_constructor_exists():
    assert callable(wh_ExprEq.__init__)


def test_wh_expreq_constructor_args():
    sig = inspect.signature(wh_ExprEq.__init__)
    params = list(sig.parameters.keys())



def test_wh_exprand_is_not_abstract():
    assert not inspect.isabstract(wh_ExprAnd)


def test_wh_exprand_constructor_exists():
    assert callable(wh_ExprAnd.__init__)


def test_wh_exprand_constructor_args():
    sig = inspect.signature(wh_ExprAnd.__init__)
    params = list(sig.parameters.keys())



def test_wh_exprlist_is_not_abstract():
    assert not inspect.isabstract(wh_ExprList)


def test_wh_exprlist_constructor_exists():
    assert callable(wh_ExprList.__init__)


def test_wh_exprlist_constructor_args():
    sig = inspect.signature(wh_ExprList.__init__)
    params = list(sig.parameters.keys())



def test_wh_exprhd_is_not_abstract():
    assert not inspect.isabstract(wh_ExprHd)


def test_wh_exprhd_constructor_exists():
    assert callable(wh_ExprHd.__init__)


def test_wh_exprhd_constructor_args():
    sig = inspect.signature(wh_ExprHd.__init__)
    params = list(sig.parameters.keys())



def test_wh_exprnot_is_not_abstract():
    assert not inspect.isabstract(wh_ExprNot)


def test_wh_exprnot_constructor_exists():
    assert callable(wh_ExprNot.__init__)


def test_wh_exprnot_constructor_args():
    sig = inspect.signature(wh_ExprNot.__init__)
    params = list(sig.parameters.keys())



def test_wh_exprsimple_is_not_abstract():
    assert not inspect.isabstract(wh_ExprSimple)


def test_wh_exprsimple_constructor_exists():
    assert callable(wh_ExprSimple.__init__)


def test_wh_exprsimple_constructor_args():
    sig = inspect.signature(wh_ExprSimple.__init__)
    params = list(sig.parameters.keys())
    assert "sym" in params, "Missing parameter 'sym'"
    assert "str" in params, "Missing parameter 'str'"
    assert "varSimple" in params, "Missing parameter 'varSimple'"

def test_wh_exprsimple_has_sym():
    assert hasattr(wh_ExprSimple, "sym")
    descriptor = None
    for klass in wh_ExprSimple.__mro__:
        if "sym" in klass.__dict__:
            descriptor = klass.__dict__["sym"]
            break
    assert isinstance(descriptor, property)

def test_wh_exprsimple_has_str():
    assert hasattr(wh_ExprSimple, "str")
    descriptor = None
    for klass in wh_ExprSimple.__mro__:
        if "str" in klass.__dict__:
            descriptor = klass.__dict__["str"]
            break
    assert isinstance(descriptor, property)

def test_wh_exprsimple_has_varSimple():
    assert hasattr(wh_ExprSimple, "varSimple")
    descriptor = None
    for klass in wh_ExprSimple.__mro__:
        if "varSimple" in klass.__dict__:
            descriptor = klass.__dict__["varSimple"]
            break
    assert isinstance(descriptor, property)



def test_wh_while_is_not_abstract():
    assert not inspect.isabstract(wh_While)


def test_wh_while_constructor_exists():
    assert callable(wh_While.__init__)


def test_wh_while_constructor_args():
    sig = inspect.signature(wh_While.__init__)
    params = list(sig.parameters.keys())



def test_wh_for_is_not_abstract():
    assert not inspect.isabstract(wh_For)


def test_wh_for_constructor_exists():
    assert callable(wh_For.__init__)


def test_wh_for_constructor_args():
    sig = inspect.signature(wh_For.__init__)
    params = list(sig.parameters.keys())



def test_wh_affect_is_not_abstract():
    assert not inspect.isabstract(wh_Affect)


def test_wh_affect_constructor_exists():
    assert callable(wh_Affect.__init__)


def test_wh_affect_constructor_args():
    sig = inspect.signature(wh_Affect.__init__)
    params = list(sig.parameters.keys())
    assert "vars" in params, "Missing parameter 'vars'"

def test_wh_affect_has_vars():
    assert hasattr(wh_Affect, "vars")
    descriptor = None
    for klass in wh_Affect.__mro__:
        if "vars" in klass.__dict__:
            descriptor = klass.__dict__["vars"]
            break
    assert isinstance(descriptor, property)



def test_wh_nop_is_not_abstract():
    assert not inspect.isabstract(wh_Nop)


def test_wh_nop_constructor_exists():
    assert callable(wh_Nop.__init__)


def test_wh_nop_constructor_args():
    sig = inspect.signature(wh_Nop.__init__)
    params = list(sig.parameters.keys())
    assert "nop" in params, "Missing parameter 'nop'"

def test_wh_nop_has_nop():
    assert hasattr(wh_Nop, "nop")
    descriptor = None
    for klass in wh_Nop.__mro__:
        if "nop" in klass.__dict__:
            descriptor = klass.__dict__["nop"]
            break
    assert isinstance(descriptor, property)



def test_wh_expr_is_not_abstract():
    assert not inspect.isabstract(wh_Expr)


def test_wh_expr_constructor_exists():
    assert callable(wh_Expr.__init__)


def test_wh_expr_constructor_args():
    sig = inspect.signature(wh_Expr.__init__)
    params = list(sig.parameters.keys())



def test_wh_if_is_not_abstract():
    assert not inspect.isabstract(wh_If)


def test_wh_if_constructor_exists():
    assert callable(wh_If.__init__)


def test_wh_if_constructor_args():
    sig = inspect.signature(wh_If.__init__)
    params = list(sig.parameters.keys())



def test_wh_eobject_is_not_abstract():
    assert not inspect.isabstract(wh_EObject)


def test_wh_eobject_constructor_exists():
    assert callable(wh_EObject.__init__)


def test_wh_eobject_constructor_args():
    sig = inspect.signature(wh_EObject.__init__)
    params = list(sig.parameters.keys())



def test_wh_command_is_not_abstract():
    assert not inspect.isabstract(wh_Command)


def test_wh_command_constructor_exists():
    assert callable(wh_Command.__init__)


def test_wh_command_constructor_args():
    sig = inspect.signature(wh_Command.__init__)
    params = list(sig.parameters.keys())



def test_wh_expror_is_not_abstract():
    assert not inspect.isabstract(wh_ExprOr)


def test_wh_expror_constructor_exists():
    assert callable(wh_ExprOr.__init__)


def test_wh_expror_constructor_args():
    sig = inspect.signature(wh_ExprOr.__init__)
    params = list(sig.parameters.keys())



def test_wh_commands_is_not_abstract():
    assert not inspect.isabstract(wh_Commands)


def test_wh_commands_constructor_exists():
    assert callable(wh_Commands.__init__)


def test_wh_commands_constructor_args():
    sig = inspect.signature(wh_Commands.__init__)
    params = list(sig.parameters.keys())



def test_wh_input_is_not_abstract():
    assert not inspect.isabstract(wh_Input)


def test_wh_input_constructor_exists():
    assert callable(wh_Input.__init__)


def test_wh_input_constructor_args():
    sig = inspect.signature(wh_Input.__init__)
    params = list(sig.parameters.keys())
    assert "vars" in params, "Missing parameter 'vars'"

def test_wh_input_has_vars():
    assert hasattr(wh_Input, "vars")
    descriptor = None
    for klass in wh_Input.__mro__:
        if "vars" in klass.__dict__:
            descriptor = klass.__dict__["vars"]
            break
    assert isinstance(descriptor, property)



def test_wh_definition_is_not_abstract():
    assert not inspect.isabstract(wh_Definition)


def test_wh_definition_constructor_exists():
    assert callable(wh_Definition.__init__)


def test_wh_definition_constructor_args():
    sig = inspect.signature(wh_Definition.__init__)
    params = list(sig.parameters.keys())



def test_wh_function_is_not_abstract():
    assert not inspect.isabstract(wh_Function)


def test_wh_function_constructor_exists():
    assert callable(wh_Function.__init__)


def test_wh_function_constructor_args():
    sig = inspect.signature(wh_Function.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_wh_function_has_name():
    assert hasattr(wh_Function, "name")
    descriptor = None
    for klass in wh_Function.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_wh_program_is_not_abstract():
    assert not inspect.isabstract(wh_Program)


def test_wh_program_constructor_exists():
    assert callable(wh_Program.__init__)


def test_wh_program_constructor_args():
    sig = inspect.signature(wh_Program.__init__)
    params = list(sig.parameters.keys())



def test_wh_wh_is_not_abstract():
    assert not inspect.isabstract(wh_Wh)


def test_wh_wh_constructor_exists():
    assert callable(wh_Wh.__init__)


def test_wh_wh_constructor_args():
    sig = inspect.signature(wh_Wh.__init__)
    params = list(sig.parameters.keys())



def test_wh_output_is_not_abstract():
    assert not inspect.isabstract(wh_Output)


def test_wh_output_constructor_exists():
    assert callable(wh_Output.__init__)


def test_wh_output_constructor_args():
    sig = inspect.signature(wh_Output.__init__)
    params = list(sig.parameters.keys())
    assert "vars" in params, "Missing parameter 'vars'"

def test_wh_output_has_vars():
    assert hasattr(wh_Output, "vars")
    descriptor = None
    for klass in wh_Output.__mro__:
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
wh_ExprTl_strategy = st.builds(
    wh_ExprTl,
)
wh_ExprSym_strategy = st.builds(
    wh_ExprSym,
    arg1=
        safe_text
)
wh_ExprCons_strategy = st.builds(
    wh_ExprCons,
)
wh_ExprEq_strategy = st.builds(
    wh_ExprEq,
)
wh_ExprAnd_strategy = st.builds(
    wh_ExprAnd,
)
wh_ExprList_strategy = st.builds(
    wh_ExprList,
)
wh_ExprHd_strategy = st.builds(
    wh_ExprHd,
)
wh_ExprNot_strategy = st.builds(
    wh_ExprNot,
)
wh_ExprSimple_strategy = st.builds(
    wh_ExprSimple,
    sym=
        safe_text,
    str=
        safe_text,
    varSimple=
        safe_text
)
wh_While_strategy = st.builds(
    wh_While,
)
wh_For_strategy = st.builds(
    wh_For,
)
wh_Affect_strategy = st.builds(
    wh_Affect,
    vars=
        safe_text
)
wh_Nop_strategy = st.builds(
    wh_Nop,
    nop=
        safe_text
)
wh_Expr_strategy = st.builds(
    wh_Expr,
)
wh_If_strategy = st.builds(
    wh_If,
)
wh_EObject_strategy = st.builds(
    wh_EObject,
)
wh_Command_strategy = st.builds(
    wh_Command,
)
wh_ExprOr_strategy = st.builds(
    wh_ExprOr,
)
wh_Commands_strategy = st.builds(
    wh_Commands,
)
wh_Input_strategy = st.builds(
    wh_Input,
    vars=
        safe_text
)
wh_Definition_strategy = st.builds(
    wh_Definition,
)
wh_Function_strategy = st.builds(
    wh_Function,
    name=
        safe_text
)
wh_Program_strategy = st.builds(
    wh_Program,
)
wh_Wh_strategy = st.builds(
    wh_Wh,
)
wh_Output_strategy = st.builds(
    wh_Output,
    vars=
        safe_text
)

@given(instance=Expr_strategy)
@settings(max_examples=50)
def test_expr_instantiation(instance):
    assert isinstance(instance, Expr)

@given(instance=wh_ExprTl_strategy)
@settings(max_examples=50)
def test_wh_exprtl_instantiation(instance):
    assert isinstance(instance, wh_ExprTl)

@given(instance=wh_ExprSym_strategy)
@settings(max_examples=50)
def test_wh_exprsym_instantiation(instance):
    assert isinstance(instance, wh_ExprSym)



@given(instance=wh_ExprSym_strategy)
def test_wh_exprsym_arg1_setter(instance):
    original = instance.arg1
    instance.arg1 = original
    assert instance.arg1 == original

@given(instance=wh_ExprCons_strategy)
@settings(max_examples=50)
def test_wh_exprcons_instantiation(instance):
    assert isinstance(instance, wh_ExprCons)

@given(instance=wh_ExprEq_strategy)
@settings(max_examples=50)
def test_wh_expreq_instantiation(instance):
    assert isinstance(instance, wh_ExprEq)

@given(instance=wh_ExprAnd_strategy)
@settings(max_examples=50)
def test_wh_exprand_instantiation(instance):
    assert isinstance(instance, wh_ExprAnd)

@given(instance=wh_ExprList_strategy)
@settings(max_examples=50)
def test_wh_exprlist_instantiation(instance):
    assert isinstance(instance, wh_ExprList)

@given(instance=wh_ExprHd_strategy)
@settings(max_examples=50)
def test_wh_exprhd_instantiation(instance):
    assert isinstance(instance, wh_ExprHd)

@given(instance=wh_ExprNot_strategy)
@settings(max_examples=50)
def test_wh_exprnot_instantiation(instance):
    assert isinstance(instance, wh_ExprNot)

@given(instance=wh_ExprSimple_strategy)
@settings(max_examples=50)
def test_wh_exprsimple_instantiation(instance):
    assert isinstance(instance, wh_ExprSimple)



@given(instance=wh_ExprSimple_strategy)
def test_wh_exprsimple_sym_setter(instance):
    original = instance.sym
    instance.sym = original
    assert instance.sym == original



@given(instance=wh_ExprSimple_strategy)
def test_wh_exprsimple_str_setter(instance):
    original = instance.str
    instance.str = original
    assert instance.str == original



@given(instance=wh_ExprSimple_strategy)
def test_wh_exprsimple_varSimple_setter(instance):
    original = instance.varSimple
    instance.varSimple = original
    assert instance.varSimple == original

@given(instance=wh_While_strategy)
@settings(max_examples=50)
def test_wh_while_instantiation(instance):
    assert isinstance(instance, wh_While)

@given(instance=wh_For_strategy)
@settings(max_examples=50)
def test_wh_for_instantiation(instance):
    assert isinstance(instance, wh_For)

@given(instance=wh_Affect_strategy)
@settings(max_examples=50)
def test_wh_affect_instantiation(instance):
    assert isinstance(instance, wh_Affect)



@given(instance=wh_Affect_strategy)
def test_wh_affect_vars_setter(instance):
    original = instance.vars
    instance.vars = original
    assert instance.vars == original

@given(instance=wh_Nop_strategy)
@settings(max_examples=50)
def test_wh_nop_instantiation(instance):
    assert isinstance(instance, wh_Nop)



@given(instance=wh_Nop_strategy)
def test_wh_nop_nop_setter(instance):
    original = instance.nop
    instance.nop = original
    assert instance.nop == original

@given(instance=wh_Expr_strategy)
@settings(max_examples=50)
def test_wh_expr_instantiation(instance):
    assert isinstance(instance, wh_Expr)

@given(instance=wh_If_strategy)
@settings(max_examples=50)
def test_wh_if_instantiation(instance):
    assert isinstance(instance, wh_If)

@given(instance=wh_EObject_strategy)
@settings(max_examples=50)
def test_wh_eobject_instantiation(instance):
    assert isinstance(instance, wh_EObject)

@given(instance=wh_Command_strategy)
@settings(max_examples=50)
def test_wh_command_instantiation(instance):
    assert isinstance(instance, wh_Command)

@given(instance=wh_ExprOr_strategy)
@settings(max_examples=50)
def test_wh_expror_instantiation(instance):
    assert isinstance(instance, wh_ExprOr)

@given(instance=wh_Commands_strategy)
@settings(max_examples=50)
def test_wh_commands_instantiation(instance):
    assert isinstance(instance, wh_Commands)

@given(instance=wh_Input_strategy)
@settings(max_examples=50)
def test_wh_input_instantiation(instance):
    assert isinstance(instance, wh_Input)



@given(instance=wh_Input_strategy)
def test_wh_input_vars_setter(instance):
    original = instance.vars
    instance.vars = original
    assert instance.vars == original

@given(instance=wh_Definition_strategy)
@settings(max_examples=50)
def test_wh_definition_instantiation(instance):
    assert isinstance(instance, wh_Definition)

@given(instance=wh_Function_strategy)
@settings(max_examples=50)
def test_wh_function_instantiation(instance):
    assert isinstance(instance, wh_Function)



@given(instance=wh_Function_strategy)
def test_wh_function_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=wh_Program_strategy)
@settings(max_examples=50)
def test_wh_program_instantiation(instance):
    assert isinstance(instance, wh_Program)

@given(instance=wh_Wh_strategy)
@settings(max_examples=50)
def test_wh_wh_instantiation(instance):
    assert isinstance(instance, wh_Wh)

@given(instance=wh_Output_strategy)
@settings(max_examples=50)
def test_wh_output_instantiation(instance):
    assert isinstance(instance, wh_Output)



@given(instance=wh_Output_strategy)
def test_wh_output_vars_setter(instance):
    original = instance.vars
    instance.vars = original
    assert instance.vars == original
