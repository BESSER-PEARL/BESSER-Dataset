import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    while_l_ExprNot,
    while_l_ExprSym,
    while_l_ExprTl,
    while_l_ExprHd,
    while_l_ExprList,
    while_l_While,
    while_l_For,
    while_l_Affect,
    while_l_Nop,
    while_l_Expr,
    while_l_If,
    while_l_EObject,
    while_l_ExprCons,
    while_l_ExprOr,
    while_l_ExprAnd,
    while_l_ExprSimple,
    while_l_ExprEq,
    while_l_Program,
    while_l_Wh,
    while_l_Command,
    while_l_Output,
    while_l_Commands,
    while_l_Input,
    while_l_Definition,
    while_l_Function,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_while_l_exprnot_is_not_abstract():
    assert not inspect.isabstract(while_l_ExprNot)


def test_while_l_exprnot_constructor_exists():
    assert callable(while_l_ExprNot.__init__)


def test_while_l_exprnot_constructor_args():
    sig = inspect.signature(while_l_ExprNot.__init__)
    params = list(sig.parameters.keys())



def test_while_l_exprsym_is_not_abstract():
    assert not inspect.isabstract(while_l_ExprSym)


def test_while_l_exprsym_constructor_exists():
    assert callable(while_l_ExprSym.__init__)


def test_while_l_exprsym_constructor_args():
    sig = inspect.signature(while_l_ExprSym.__init__)
    params = list(sig.parameters.keys())
    assert "arg1" in params, "Missing parameter 'arg1'"

def test_while_l_exprsym_has_arg1():
    assert hasattr(while_l_ExprSym, "arg1")
    descriptor = None
    for klass in while_l_ExprSym.__mro__:
        if "arg1" in klass.__dict__:
            descriptor = klass.__dict__["arg1"]
            break
    assert isinstance(descriptor, property)



def test_while_l_exprtl_is_not_abstract():
    assert not inspect.isabstract(while_l_ExprTl)


def test_while_l_exprtl_constructor_exists():
    assert callable(while_l_ExprTl.__init__)


def test_while_l_exprtl_constructor_args():
    sig = inspect.signature(while_l_ExprTl.__init__)
    params = list(sig.parameters.keys())



def test_while_l_exprhd_is_not_abstract():
    assert not inspect.isabstract(while_l_ExprHd)


def test_while_l_exprhd_constructor_exists():
    assert callable(while_l_ExprHd.__init__)


def test_while_l_exprhd_constructor_args():
    sig = inspect.signature(while_l_ExprHd.__init__)
    params = list(sig.parameters.keys())



def test_while_l_exprlist_is_not_abstract():
    assert not inspect.isabstract(while_l_ExprList)


def test_while_l_exprlist_constructor_exists():
    assert callable(while_l_ExprList.__init__)


def test_while_l_exprlist_constructor_args():
    sig = inspect.signature(while_l_ExprList.__init__)
    params = list(sig.parameters.keys())



def test_while_l_while_is_not_abstract():
    assert not inspect.isabstract(while_l_While)


def test_while_l_while_constructor_exists():
    assert callable(while_l_While.__init__)


def test_while_l_while_constructor_args():
    sig = inspect.signature(while_l_While.__init__)
    params = list(sig.parameters.keys())



def test_while_l_for_is_not_abstract():
    assert not inspect.isabstract(while_l_For)


def test_while_l_for_constructor_exists():
    assert callable(while_l_For.__init__)


def test_while_l_for_constructor_args():
    sig = inspect.signature(while_l_For.__init__)
    params = list(sig.parameters.keys())



def test_while_l_affect_is_not_abstract():
    assert not inspect.isabstract(while_l_Affect)


def test_while_l_affect_constructor_exists():
    assert callable(while_l_Affect.__init__)


def test_while_l_affect_constructor_args():
    sig = inspect.signature(while_l_Affect.__init__)
    params = list(sig.parameters.keys())
    assert "vars" in params, "Missing parameter 'vars'"

def test_while_l_affect_has_vars():
    assert hasattr(while_l_Affect, "vars")
    descriptor = None
    for klass in while_l_Affect.__mro__:
        if "vars" in klass.__dict__:
            descriptor = klass.__dict__["vars"]
            break
    assert isinstance(descriptor, property)



def test_while_l_nop_is_not_abstract():
    assert not inspect.isabstract(while_l_Nop)


def test_while_l_nop_constructor_exists():
    assert callable(while_l_Nop.__init__)


def test_while_l_nop_constructor_args():
    sig = inspect.signature(while_l_Nop.__init__)
    params = list(sig.parameters.keys())
    assert "nop" in params, "Missing parameter 'nop'"

def test_while_l_nop_has_nop():
    assert hasattr(while_l_Nop, "nop")
    descriptor = None
    for klass in while_l_Nop.__mro__:
        if "nop" in klass.__dict__:
            descriptor = klass.__dict__["nop"]
            break
    assert isinstance(descriptor, property)



def test_while_l_expr_is_not_abstract():
    assert not inspect.isabstract(while_l_Expr)


def test_while_l_expr_constructor_exists():
    assert callable(while_l_Expr.__init__)


def test_while_l_expr_constructor_args():
    sig = inspect.signature(while_l_Expr.__init__)
    params = list(sig.parameters.keys())



def test_while_l_if_is_not_abstract():
    assert not inspect.isabstract(while_l_If)


def test_while_l_if_constructor_exists():
    assert callable(while_l_If.__init__)


def test_while_l_if_constructor_args():
    sig = inspect.signature(while_l_If.__init__)
    params = list(sig.parameters.keys())



def test_while_l_eobject_is_not_abstract():
    assert not inspect.isabstract(while_l_EObject)


def test_while_l_eobject_constructor_exists():
    assert callable(while_l_EObject.__init__)


def test_while_l_eobject_constructor_args():
    sig = inspect.signature(while_l_EObject.__init__)
    params = list(sig.parameters.keys())



def test_while_l_exprcons_is_not_abstract():
    assert not inspect.isabstract(while_l_ExprCons)


def test_while_l_exprcons_constructor_exists():
    assert callable(while_l_ExprCons.__init__)


def test_while_l_exprcons_constructor_args():
    sig = inspect.signature(while_l_ExprCons.__init__)
    params = list(sig.parameters.keys())



def test_while_l_expror_is_not_abstract():
    assert not inspect.isabstract(while_l_ExprOr)


def test_while_l_expror_constructor_exists():
    assert callable(while_l_ExprOr.__init__)


def test_while_l_expror_constructor_args():
    sig = inspect.signature(while_l_ExprOr.__init__)
    params = list(sig.parameters.keys())



def test_while_l_exprand_is_not_abstract():
    assert not inspect.isabstract(while_l_ExprAnd)


def test_while_l_exprand_constructor_exists():
    assert callable(while_l_ExprAnd.__init__)


def test_while_l_exprand_constructor_args():
    sig = inspect.signature(while_l_ExprAnd.__init__)
    params = list(sig.parameters.keys())



def test_while_l_exprsimple_is_not_abstract():
    assert not inspect.isabstract(while_l_ExprSimple)


def test_while_l_exprsimple_constructor_exists():
    assert callable(while_l_ExprSimple.__init__)


def test_while_l_exprsimple_constructor_args():
    sig = inspect.signature(while_l_ExprSimple.__init__)
    params = list(sig.parameters.keys())
    assert "str" in params, "Missing parameter 'str'"
    assert "sym" in params, "Missing parameter 'sym'"
    assert "varSimple" in params, "Missing parameter 'varSimple'"
    assert "nameFunction" in params, "Missing parameter 'nameFunction'"

def test_while_l_exprsimple_has_str():
    assert hasattr(while_l_ExprSimple, "str")
    descriptor = None
    for klass in while_l_ExprSimple.__mro__:
        if "str" in klass.__dict__:
            descriptor = klass.__dict__["str"]
            break
    assert isinstance(descriptor, property)

def test_while_l_exprsimple_has_sym():
    assert hasattr(while_l_ExprSimple, "sym")
    descriptor = None
    for klass in while_l_ExprSimple.__mro__:
        if "sym" in klass.__dict__:
            descriptor = klass.__dict__["sym"]
            break
    assert isinstance(descriptor, property)

def test_while_l_exprsimple_has_varSimple():
    assert hasattr(while_l_ExprSimple, "varSimple")
    descriptor = None
    for klass in while_l_ExprSimple.__mro__:
        if "varSimple" in klass.__dict__:
            descriptor = klass.__dict__["varSimple"]
            break
    assert isinstance(descriptor, property)

def test_while_l_exprsimple_has_nameFunction():
    assert hasattr(while_l_ExprSimple, "nameFunction")
    descriptor = None
    for klass in while_l_ExprSimple.__mro__:
        if "nameFunction" in klass.__dict__:
            descriptor = klass.__dict__["nameFunction"]
            break
    assert isinstance(descriptor, property)



def test_while_l_expreq_is_not_abstract():
    assert not inspect.isabstract(while_l_ExprEq)


def test_while_l_expreq_constructor_exists():
    assert callable(while_l_ExprEq.__init__)


def test_while_l_expreq_constructor_args():
    sig = inspect.signature(while_l_ExprEq.__init__)
    params = list(sig.parameters.keys())



def test_while_l_program_is_not_abstract():
    assert not inspect.isabstract(while_l_Program)


def test_while_l_program_constructor_exists():
    assert callable(while_l_Program.__init__)


def test_while_l_program_constructor_args():
    sig = inspect.signature(while_l_Program.__init__)
    params = list(sig.parameters.keys())



def test_while_l_wh_is_not_abstract():
    assert not inspect.isabstract(while_l_Wh)


def test_while_l_wh_constructor_exists():
    assert callable(while_l_Wh.__init__)


def test_while_l_wh_constructor_args():
    sig = inspect.signature(while_l_Wh.__init__)
    params = list(sig.parameters.keys())



def test_while_l_command_is_not_abstract():
    assert not inspect.isabstract(while_l_Command)


def test_while_l_command_constructor_exists():
    assert callable(while_l_Command.__init__)


def test_while_l_command_constructor_args():
    sig = inspect.signature(while_l_Command.__init__)
    params = list(sig.parameters.keys())



def test_while_l_output_is_not_abstract():
    assert not inspect.isabstract(while_l_Output)


def test_while_l_output_constructor_exists():
    assert callable(while_l_Output.__init__)


def test_while_l_output_constructor_args():
    sig = inspect.signature(while_l_Output.__init__)
    params = list(sig.parameters.keys())
    assert "vars" in params, "Missing parameter 'vars'"

def test_while_l_output_has_vars():
    assert hasattr(while_l_Output, "vars")
    descriptor = None
    for klass in while_l_Output.__mro__:
        if "vars" in klass.__dict__:
            descriptor = klass.__dict__["vars"]
            break
    assert isinstance(descriptor, property)



def test_while_l_commands_is_not_abstract():
    assert not inspect.isabstract(while_l_Commands)


def test_while_l_commands_constructor_exists():
    assert callable(while_l_Commands.__init__)


def test_while_l_commands_constructor_args():
    sig = inspect.signature(while_l_Commands.__init__)
    params = list(sig.parameters.keys())



def test_while_l_input_is_not_abstract():
    assert not inspect.isabstract(while_l_Input)


def test_while_l_input_constructor_exists():
    assert callable(while_l_Input.__init__)


def test_while_l_input_constructor_args():
    sig = inspect.signature(while_l_Input.__init__)
    params = list(sig.parameters.keys())
    assert "vars" in params, "Missing parameter 'vars'"

def test_while_l_input_has_vars():
    assert hasattr(while_l_Input, "vars")
    descriptor = None
    for klass in while_l_Input.__mro__:
        if "vars" in klass.__dict__:
            descriptor = klass.__dict__["vars"]
            break
    assert isinstance(descriptor, property)



def test_while_l_definition_is_not_abstract():
    assert not inspect.isabstract(while_l_Definition)


def test_while_l_definition_constructor_exists():
    assert callable(while_l_Definition.__init__)


def test_while_l_definition_constructor_args():
    sig = inspect.signature(while_l_Definition.__init__)
    params = list(sig.parameters.keys())



def test_while_l_function_is_not_abstract():
    assert not inspect.isabstract(while_l_Function)


def test_while_l_function_constructor_exists():
    assert callable(while_l_Function.__init__)


def test_while_l_function_constructor_args():
    sig = inspect.signature(while_l_Function.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_while_l_function_has_name():
    assert hasattr(while_l_Function, "name")
    descriptor = None
    for klass in while_l_Function.__mro__:
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
while_l_ExprNot_strategy = st.builds(
    while_l_ExprNot,
)
while_l_ExprSym_strategy = st.builds(
    while_l_ExprSym,
    arg1=
        safe_text
)
while_l_ExprTl_strategy = st.builds(
    while_l_ExprTl,
)
while_l_ExprHd_strategy = st.builds(
    while_l_ExprHd,
)
while_l_ExprList_strategy = st.builds(
    while_l_ExprList,
)
while_l_While_strategy = st.builds(
    while_l_While,
)
while_l_For_strategy = st.builds(
    while_l_For,
)
while_l_Affect_strategy = st.builds(
    while_l_Affect,
    vars=
        safe_text
)
while_l_Nop_strategy = st.builds(
    while_l_Nop,
    nop=
        safe_text
)
while_l_Expr_strategy = st.builds(
    while_l_Expr,
)
while_l_If_strategy = st.builds(
    while_l_If,
)
while_l_EObject_strategy = st.builds(
    while_l_EObject,
)
while_l_ExprCons_strategy = st.builds(
    while_l_ExprCons,
)
while_l_ExprOr_strategy = st.builds(
    while_l_ExprOr,
)
while_l_ExprAnd_strategy = st.builds(
    while_l_ExprAnd,
)
while_l_ExprSimple_strategy = st.builds(
    while_l_ExprSimple,
    str=
        safe_text,
    sym=
        safe_text,
    varSimple=
        safe_text,
    nameFunction=
        safe_text
)
while_l_ExprEq_strategy = st.builds(
    while_l_ExprEq,
)
while_l_Program_strategy = st.builds(
    while_l_Program,
)
while_l_Wh_strategy = st.builds(
    while_l_Wh,
)
while_l_Command_strategy = st.builds(
    while_l_Command,
)
while_l_Output_strategy = st.builds(
    while_l_Output,
    vars=
        safe_text
)
while_l_Commands_strategy = st.builds(
    while_l_Commands,
)
while_l_Input_strategy = st.builds(
    while_l_Input,
    vars=
        safe_text
)
while_l_Definition_strategy = st.builds(
    while_l_Definition,
)
while_l_Function_strategy = st.builds(
    while_l_Function,
    name=
        safe_text
)

@given(instance=while_l_ExprNot_strategy)
@settings(max_examples=50)
def test_while_l_exprnot_instantiation(instance):
    assert isinstance(instance, while_l_ExprNot)

@given(instance=while_l_ExprSym_strategy)
@settings(max_examples=50)
def test_while_l_exprsym_instantiation(instance):
    assert isinstance(instance, while_l_ExprSym)



@given(instance=while_l_ExprSym_strategy)
def test_while_l_exprsym_arg1_setter(instance):
    original = instance.arg1
    instance.arg1 = original
    assert instance.arg1 == original

@given(instance=while_l_ExprTl_strategy)
@settings(max_examples=50)
def test_while_l_exprtl_instantiation(instance):
    assert isinstance(instance, while_l_ExprTl)

@given(instance=while_l_ExprHd_strategy)
@settings(max_examples=50)
def test_while_l_exprhd_instantiation(instance):
    assert isinstance(instance, while_l_ExprHd)

@given(instance=while_l_ExprList_strategy)
@settings(max_examples=50)
def test_while_l_exprlist_instantiation(instance):
    assert isinstance(instance, while_l_ExprList)

@given(instance=while_l_While_strategy)
@settings(max_examples=50)
def test_while_l_while_instantiation(instance):
    assert isinstance(instance, while_l_While)

@given(instance=while_l_For_strategy)
@settings(max_examples=50)
def test_while_l_for_instantiation(instance):
    assert isinstance(instance, while_l_For)

@given(instance=while_l_Affect_strategy)
@settings(max_examples=50)
def test_while_l_affect_instantiation(instance):
    assert isinstance(instance, while_l_Affect)



@given(instance=while_l_Affect_strategy)
def test_while_l_affect_vars_setter(instance):
    original = instance.vars
    instance.vars = original
    assert instance.vars == original

@given(instance=while_l_Nop_strategy)
@settings(max_examples=50)
def test_while_l_nop_instantiation(instance):
    assert isinstance(instance, while_l_Nop)



@given(instance=while_l_Nop_strategy)
def test_while_l_nop_nop_setter(instance):
    original = instance.nop
    instance.nop = original
    assert instance.nop == original

@given(instance=while_l_Expr_strategy)
@settings(max_examples=50)
def test_while_l_expr_instantiation(instance):
    assert isinstance(instance, while_l_Expr)

@given(instance=while_l_If_strategy)
@settings(max_examples=50)
def test_while_l_if_instantiation(instance):
    assert isinstance(instance, while_l_If)

@given(instance=while_l_EObject_strategy)
@settings(max_examples=50)
def test_while_l_eobject_instantiation(instance):
    assert isinstance(instance, while_l_EObject)

@given(instance=while_l_ExprCons_strategy)
@settings(max_examples=50)
def test_while_l_exprcons_instantiation(instance):
    assert isinstance(instance, while_l_ExprCons)

@given(instance=while_l_ExprOr_strategy)
@settings(max_examples=50)
def test_while_l_expror_instantiation(instance):
    assert isinstance(instance, while_l_ExprOr)

@given(instance=while_l_ExprAnd_strategy)
@settings(max_examples=50)
def test_while_l_exprand_instantiation(instance):
    assert isinstance(instance, while_l_ExprAnd)

@given(instance=while_l_ExprSimple_strategy)
@settings(max_examples=50)
def test_while_l_exprsimple_instantiation(instance):
    assert isinstance(instance, while_l_ExprSimple)



@given(instance=while_l_ExprSimple_strategy)
def test_while_l_exprsimple_str_setter(instance):
    original = instance.str
    instance.str = original
    assert instance.str == original



@given(instance=while_l_ExprSimple_strategy)
def test_while_l_exprsimple_sym_setter(instance):
    original = instance.sym
    instance.sym = original
    assert instance.sym == original



@given(instance=while_l_ExprSimple_strategy)
def test_while_l_exprsimple_varSimple_setter(instance):
    original = instance.varSimple
    instance.varSimple = original
    assert instance.varSimple == original



@given(instance=while_l_ExprSimple_strategy)
def test_while_l_exprsimple_nameFunction_setter(instance):
    original = instance.nameFunction
    instance.nameFunction = original
    assert instance.nameFunction == original

@given(instance=while_l_ExprEq_strategy)
@settings(max_examples=50)
def test_while_l_expreq_instantiation(instance):
    assert isinstance(instance, while_l_ExprEq)

@given(instance=while_l_Program_strategy)
@settings(max_examples=50)
def test_while_l_program_instantiation(instance):
    assert isinstance(instance, while_l_Program)

@given(instance=while_l_Wh_strategy)
@settings(max_examples=50)
def test_while_l_wh_instantiation(instance):
    assert isinstance(instance, while_l_Wh)

@given(instance=while_l_Command_strategy)
@settings(max_examples=50)
def test_while_l_command_instantiation(instance):
    assert isinstance(instance, while_l_Command)

@given(instance=while_l_Output_strategy)
@settings(max_examples=50)
def test_while_l_output_instantiation(instance):
    assert isinstance(instance, while_l_Output)



@given(instance=while_l_Output_strategy)
def test_while_l_output_vars_setter(instance):
    original = instance.vars
    instance.vars = original
    assert instance.vars == original

@given(instance=while_l_Commands_strategy)
@settings(max_examples=50)
def test_while_l_commands_instantiation(instance):
    assert isinstance(instance, while_l_Commands)

@given(instance=while_l_Input_strategy)
@settings(max_examples=50)
def test_while_l_input_instantiation(instance):
    assert isinstance(instance, while_l_Input)



@given(instance=while_l_Input_strategy)
def test_while_l_input_vars_setter(instance):
    original = instance.vars
    instance.vars = original
    assert instance.vars == original

@given(instance=while_l_Definition_strategy)
@settings(max_examples=50)
def test_while_l_definition_instantiation(instance):
    assert isinstance(instance, while_l_Definition)

@given(instance=while_l_Function_strategy)
@settings(max_examples=50)
def test_while_l_function_instantiation(instance):
    assert isinstance(instance, while_l_Function)



@given(instance=while_l_Function_strategy)
def test_while_l_function_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
