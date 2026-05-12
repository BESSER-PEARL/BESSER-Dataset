import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    wh_ExprEq,
    wh_ExprNot,
    wh_ExprOr,
    wh_ExprAnd,
    wh_ListExpr,
    wh_Cons,
    wh_ExprSimple,
    wh_Expr,
    wh_Exprs,
    wh_Vars,
    wh_Affect,
    wh_Nop,
    wh_EObject,
    wh_Command,
    wh_Output,
    wh_Input,
    wh_Definition,
    wh_Program,
    wh_Wh,
    wh_Commands,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_wh_expreq_is_not_abstract():
    assert not inspect.isabstract(wh_ExprEq)


def test_wh_expreq_constructor_exists():
    assert callable(wh_ExprEq.__init__)


def test_wh_expreq_constructor_args():
    sig = inspect.signature(wh_ExprEq.__init__)
    params = list(sig.parameters.keys())



def test_wh_exprnot_is_not_abstract():
    assert not inspect.isabstract(wh_ExprNot)


def test_wh_exprnot_constructor_exists():
    assert callable(wh_ExprNot.__init__)


def test_wh_exprnot_constructor_args():
    sig = inspect.signature(wh_ExprNot.__init__)
    params = list(sig.parameters.keys())
    assert "not_" in params, "Missing parameter 'not_'"

def test_wh_exprnot_has_not_():
    assert hasattr(wh_ExprNot, "not_")
    descriptor = None
    for klass in wh_ExprNot.__mro__:
        if "not_" in klass.__dict__:
            descriptor = klass.__dict__["not_"]
            break
    assert isinstance(descriptor, property)



def test_wh_expror_is_not_abstract():
    assert not inspect.isabstract(wh_ExprOr)


def test_wh_expror_constructor_exists():
    assert callable(wh_ExprOr.__init__)


def test_wh_expror_constructor_args():
    sig = inspect.signature(wh_ExprOr.__init__)
    params = list(sig.parameters.keys())



def test_wh_exprand_is_not_abstract():
    assert not inspect.isabstract(wh_ExprAnd)


def test_wh_exprand_constructor_exists():
    assert callable(wh_ExprAnd.__init__)


def test_wh_exprand_constructor_args():
    sig = inspect.signature(wh_ExprAnd.__init__)
    params = list(sig.parameters.keys())



def test_wh_listexpr_is_not_abstract():
    assert not inspect.isabstract(wh_ListExpr)


def test_wh_listexpr_constructor_exists():
    assert callable(wh_ListExpr.__init__)


def test_wh_listexpr_constructor_args():
    sig = inspect.signature(wh_ListExpr.__init__)
    params = list(sig.parameters.keys())



def test_wh_cons_is_not_abstract():
    assert not inspect.isabstract(wh_Cons)


def test_wh_cons_constructor_exists():
    assert callable(wh_Cons.__init__)


def test_wh_cons_constructor_args():
    sig = inspect.signature(wh_Cons.__init__)
    params = list(sig.parameters.keys())



def test_wh_exprsimple_is_not_abstract():
    assert not inspect.isabstract(wh_ExprSimple)


def test_wh_exprsimple_constructor_exists():
    assert callable(wh_ExprSimple.__init__)


def test_wh_exprsimple_constructor_args():
    sig = inspect.signature(wh_ExprSimple.__init__)
    params = list(sig.parameters.keys())
    assert "str" in params, "Missing parameter 'str'"

def test_wh_exprsimple_has_str():
    assert hasattr(wh_ExprSimple, "str")
    descriptor = None
    for klass in wh_ExprSimple.__mro__:
        if "str" in klass.__dict__:
            descriptor = klass.__dict__["str"]
            break
    assert isinstance(descriptor, property)



def test_wh_expr_is_not_abstract():
    assert not inspect.isabstract(wh_Expr)


def test_wh_expr_constructor_exists():
    assert callable(wh_Expr.__init__)


def test_wh_expr_constructor_args():
    sig = inspect.signature(wh_Expr.__init__)
    params = list(sig.parameters.keys())



def test_wh_exprs_is_not_abstract():
    assert not inspect.isabstract(wh_Exprs)


def test_wh_exprs_constructor_exists():
    assert callable(wh_Exprs.__init__)


def test_wh_exprs_constructor_args():
    sig = inspect.signature(wh_Exprs.__init__)
    params = list(sig.parameters.keys())



def test_wh_vars_is_not_abstract():
    assert not inspect.isabstract(wh_Vars)


def test_wh_vars_constructor_exists():
    assert callable(wh_Vars.__init__)


def test_wh_vars_constructor_args():
    sig = inspect.signature(wh_Vars.__init__)
    params = list(sig.parameters.keys())
    assert "vars" in params, "Missing parameter 'vars'"

def test_wh_vars_has_vars():
    assert hasattr(wh_Vars, "vars")
    descriptor = None
    for klass in wh_Vars.__mro__:
        if "vars" in klass.__dict__:
            descriptor = klass.__dict__["vars"]
            break
    assert isinstance(descriptor, property)



def test_wh_affect_is_not_abstract():
    assert not inspect.isabstract(wh_Affect)


def test_wh_affect_constructor_exists():
    assert callable(wh_Affect.__init__)


def test_wh_affect_constructor_args():
    sig = inspect.signature(wh_Affect.__init__)
    params = list(sig.parameters.keys())



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



def test_wh_program_is_not_abstract():
    assert not inspect.isabstract(wh_Program)


def test_wh_program_constructor_exists():
    assert callable(wh_Program.__init__)


def test_wh_program_constructor_args():
    sig = inspect.signature(wh_Program.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_wh_program_has_name():
    assert hasattr(wh_Program, "name")
    descriptor = None
    for klass in wh_Program.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_wh_wh_is_not_abstract():
    assert not inspect.isabstract(wh_Wh)


def test_wh_wh_constructor_exists():
    assert callable(wh_Wh.__init__)


def test_wh_wh_constructor_args():
    sig = inspect.signature(wh_Wh.__init__)
    params = list(sig.parameters.keys())



def test_wh_commands_is_not_abstract():
    assert not inspect.isabstract(wh_Commands)


def test_wh_commands_constructor_exists():
    assert callable(wh_Commands.__init__)


def test_wh_commands_constructor_args():
    sig = inspect.signature(wh_Commands.__init__)
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
wh_ExprEq_strategy = st.builds(
    wh_ExprEq,
)
wh_ExprNot_strategy = st.builds(
    wh_ExprNot,
    not_=
        safe_text
)
wh_ExprOr_strategy = st.builds(
    wh_ExprOr,
)
wh_ExprAnd_strategy = st.builds(
    wh_ExprAnd,
)
wh_ListExpr_strategy = st.builds(
    wh_ListExpr,
)
wh_Cons_strategy = st.builds(
    wh_Cons,
)
wh_ExprSimple_strategy = st.builds(
    wh_ExprSimple,
    str=
        safe_text
)
wh_Expr_strategy = st.builds(
    wh_Expr,
)
wh_Exprs_strategy = st.builds(
    wh_Exprs,
)
wh_Vars_strategy = st.builds(
    wh_Vars,
    vars=
        safe_text
)
wh_Affect_strategy = st.builds(
    wh_Affect,
)
wh_Nop_strategy = st.builds(
    wh_Nop,
    nop=
        safe_text
)
wh_EObject_strategy = st.builds(
    wh_EObject,
)
wh_Command_strategy = st.builds(
    wh_Command,
)
wh_Output_strategy = st.builds(
    wh_Output,
    vars=
        safe_text
)
wh_Input_strategy = st.builds(
    wh_Input,
    vars=
        safe_text
)
wh_Definition_strategy = st.builds(
    wh_Definition,
)
wh_Program_strategy = st.builds(
    wh_Program,
    name=
        safe_text
)
wh_Wh_strategy = st.builds(
    wh_Wh,
)
wh_Commands_strategy = st.builds(
    wh_Commands,
)

@given(instance=wh_ExprEq_strategy)
@settings(max_examples=50)
def test_wh_expreq_instantiation(instance):
    assert isinstance(instance, wh_ExprEq)

@given(instance=wh_ExprNot_strategy)
@settings(max_examples=50)
def test_wh_exprnot_instantiation(instance):
    assert isinstance(instance, wh_ExprNot)



@given(instance=wh_ExprNot_strategy)
def test_wh_exprnot_not__setter(instance):
    original = instance.not_
    instance.not_ = original
    assert instance.not_ == original

@given(instance=wh_ExprOr_strategy)
@settings(max_examples=50)
def test_wh_expror_instantiation(instance):
    assert isinstance(instance, wh_ExprOr)

@given(instance=wh_ExprAnd_strategy)
@settings(max_examples=50)
def test_wh_exprand_instantiation(instance):
    assert isinstance(instance, wh_ExprAnd)

@given(instance=wh_ListExpr_strategy)
@settings(max_examples=50)
def test_wh_listexpr_instantiation(instance):
    assert isinstance(instance, wh_ListExpr)

@given(instance=wh_Cons_strategy)
@settings(max_examples=50)
def test_wh_cons_instantiation(instance):
    assert isinstance(instance, wh_Cons)

@given(instance=wh_ExprSimple_strategy)
@settings(max_examples=50)
def test_wh_exprsimple_instantiation(instance):
    assert isinstance(instance, wh_ExprSimple)



@given(instance=wh_ExprSimple_strategy)
def test_wh_exprsimple_str_setter(instance):
    original = instance.str
    instance.str = original
    assert instance.str == original

@given(instance=wh_Expr_strategy)
@settings(max_examples=50)
def test_wh_expr_instantiation(instance):
    assert isinstance(instance, wh_Expr)

@given(instance=wh_Exprs_strategy)
@settings(max_examples=50)
def test_wh_exprs_instantiation(instance):
    assert isinstance(instance, wh_Exprs)

@given(instance=wh_Vars_strategy)
@settings(max_examples=50)
def test_wh_vars_instantiation(instance):
    assert isinstance(instance, wh_Vars)



@given(instance=wh_Vars_strategy)
def test_wh_vars_vars_setter(instance):
    original = instance.vars
    instance.vars = original
    assert instance.vars == original

@given(instance=wh_Affect_strategy)
@settings(max_examples=50)
def test_wh_affect_instantiation(instance):
    assert isinstance(instance, wh_Affect)

@given(instance=wh_Nop_strategy)
@settings(max_examples=50)
def test_wh_nop_instantiation(instance):
    assert isinstance(instance, wh_Nop)



@given(instance=wh_Nop_strategy)
def test_wh_nop_nop_setter(instance):
    original = instance.nop
    instance.nop = original
    assert instance.nop == original

@given(instance=wh_EObject_strategy)
@settings(max_examples=50)
def test_wh_eobject_instantiation(instance):
    assert isinstance(instance, wh_EObject)

@given(instance=wh_Command_strategy)
@settings(max_examples=50)
def test_wh_command_instantiation(instance):
    assert isinstance(instance, wh_Command)

@given(instance=wh_Output_strategy)
@settings(max_examples=50)
def test_wh_output_instantiation(instance):
    assert isinstance(instance, wh_Output)



@given(instance=wh_Output_strategy)
def test_wh_output_vars_setter(instance):
    original = instance.vars
    instance.vars = original
    assert instance.vars == original

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

@given(instance=wh_Program_strategy)
@settings(max_examples=50)
def test_wh_program_instantiation(instance):
    assert isinstance(instance, wh_Program)



@given(instance=wh_Program_strategy)
def test_wh_program_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=wh_Wh_strategy)
@settings(max_examples=50)
def test_wh_wh_instantiation(instance):
    assert isinstance(instance, wh_Wh)

@given(instance=wh_Commands_strategy)
@settings(max_examples=50)
def test_wh_commands_instantiation(instance):
    assert isinstance(instance, wh_Commands)
