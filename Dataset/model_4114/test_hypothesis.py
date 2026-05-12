import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    py_ExprEq,
    py_ExprNot,
    py_ExprSym,
    py_ExprTl,
    py_ExprHd,
    py_ExprList,
    py_LExpr,
    py_ExprCons,
    py_ExprOr,
    py_While,
    py_Foreach,
    py_For,
    py_Affect,
    py_Nop,
    py_Expr,
    py_If,
    py_EObject,
    py_ExprAnd,
    py_ExprSimple,
    py_Input,
    py_Definition,
    py_FunctionP,
    py_Program,
    py_Wh,
    py_Command,
    py_Output,
    py_Commands,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_py_expreq_is_not_abstract():
    assert not inspect.isabstract(py_ExprEq)


def test_py_expreq_constructor_exists():
    assert callable(py_ExprEq.__init__)


def test_py_expreq_constructor_args():
    sig = inspect.signature(py_ExprEq.__init__)
    params = list(sig.parameters.keys())



def test_py_exprnot_is_not_abstract():
    assert not inspect.isabstract(py_ExprNot)


def test_py_exprnot_constructor_exists():
    assert callable(py_ExprNot.__init__)


def test_py_exprnot_constructor_args():
    sig = inspect.signature(py_ExprNot.__init__)
    params = list(sig.parameters.keys())



def test_py_exprsym_is_not_abstract():
    assert not inspect.isabstract(py_ExprSym)


def test_py_exprsym_constructor_exists():
    assert callable(py_ExprSym.__init__)


def test_py_exprsym_constructor_args():
    sig = inspect.signature(py_ExprSym.__init__)
    params = list(sig.parameters.keys())
    assert "arg1" in params, "Missing parameter 'arg1'"

def test_py_exprsym_has_arg1():
    assert hasattr(py_ExprSym, "arg1")
    descriptor = None
    for klass in py_ExprSym.__mro__:
        if "arg1" in klass.__dict__:
            descriptor = klass.__dict__["arg1"]
            break
    assert isinstance(descriptor, property)



def test_py_exprtl_is_not_abstract():
    assert not inspect.isabstract(py_ExprTl)


def test_py_exprtl_constructor_exists():
    assert callable(py_ExprTl.__init__)


def test_py_exprtl_constructor_args():
    sig = inspect.signature(py_ExprTl.__init__)
    params = list(sig.parameters.keys())



def test_py_exprhd_is_not_abstract():
    assert not inspect.isabstract(py_ExprHd)


def test_py_exprhd_constructor_exists():
    assert callable(py_ExprHd.__init__)


def test_py_exprhd_constructor_args():
    sig = inspect.signature(py_ExprHd.__init__)
    params = list(sig.parameters.keys())



def test_py_exprlist_is_not_abstract():
    assert not inspect.isabstract(py_ExprList)


def test_py_exprlist_constructor_exists():
    assert callable(py_ExprList.__init__)


def test_py_exprlist_constructor_args():
    sig = inspect.signature(py_ExprList.__init__)
    params = list(sig.parameters.keys())



def test_py_lexpr_is_not_abstract():
    assert not inspect.isabstract(py_LExpr)


def test_py_lexpr_constructor_exists():
    assert callable(py_LExpr.__init__)


def test_py_lexpr_constructor_args():
    sig = inspect.signature(py_LExpr.__init__)
    params = list(sig.parameters.keys())



def test_py_exprcons_is_not_abstract():
    assert not inspect.isabstract(py_ExprCons)


def test_py_exprcons_constructor_exists():
    assert callable(py_ExprCons.__init__)


def test_py_exprcons_constructor_args():
    sig = inspect.signature(py_ExprCons.__init__)
    params = list(sig.parameters.keys())



def test_py_expror_is_not_abstract():
    assert not inspect.isabstract(py_ExprOr)


def test_py_expror_constructor_exists():
    assert callable(py_ExprOr.__init__)


def test_py_expror_constructor_args():
    sig = inspect.signature(py_ExprOr.__init__)
    params = list(sig.parameters.keys())



def test_py_while_is_not_abstract():
    assert not inspect.isabstract(py_While)


def test_py_while_constructor_exists():
    assert callable(py_While.__init__)


def test_py_while_constructor_args():
    sig = inspect.signature(py_While.__init__)
    params = list(sig.parameters.keys())



def test_py_foreach_is_not_abstract():
    assert not inspect.isabstract(py_Foreach)


def test_py_foreach_constructor_exists():
    assert callable(py_Foreach.__init__)


def test_py_foreach_constructor_args():
    sig = inspect.signature(py_Foreach.__init__)
    params = list(sig.parameters.keys())
    assert "var" in params, "Missing parameter 'var'"

def test_py_foreach_has_var():
    assert hasattr(py_Foreach, "var")
    descriptor = None
    for klass in py_Foreach.__mro__:
        if "var" in klass.__dict__:
            descriptor = klass.__dict__["var"]
            break
    assert isinstance(descriptor, property)



def test_py_for_is_not_abstract():
    assert not inspect.isabstract(py_For)


def test_py_for_constructor_exists():
    assert callable(py_For.__init__)


def test_py_for_constructor_args():
    sig = inspect.signature(py_For.__init__)
    params = list(sig.parameters.keys())



def test_py_affect_is_not_abstract():
    assert not inspect.isabstract(py_Affect)


def test_py_affect_constructor_exists():
    assert callable(py_Affect.__init__)


def test_py_affect_constructor_args():
    sig = inspect.signature(py_Affect.__init__)
    params = list(sig.parameters.keys())
    assert "vars" in params, "Missing parameter 'vars'"

def test_py_affect_has_vars():
    assert hasattr(py_Affect, "vars")
    descriptor = None
    for klass in py_Affect.__mro__:
        if "vars" in klass.__dict__:
            descriptor = klass.__dict__["vars"]
            break
    assert isinstance(descriptor, property)



def test_py_nop_is_not_abstract():
    assert not inspect.isabstract(py_Nop)


def test_py_nop_constructor_exists():
    assert callable(py_Nop.__init__)


def test_py_nop_constructor_args():
    sig = inspect.signature(py_Nop.__init__)
    params = list(sig.parameters.keys())
    assert "nop" in params, "Missing parameter 'nop'"

def test_py_nop_has_nop():
    assert hasattr(py_Nop, "nop")
    descriptor = None
    for klass in py_Nop.__mro__:
        if "nop" in klass.__dict__:
            descriptor = klass.__dict__["nop"]
            break
    assert isinstance(descriptor, property)



def test_py_expr_is_not_abstract():
    assert not inspect.isabstract(py_Expr)


def test_py_expr_constructor_exists():
    assert callable(py_Expr.__init__)


def test_py_expr_constructor_args():
    sig = inspect.signature(py_Expr.__init__)
    params = list(sig.parameters.keys())



def test_py_if_is_not_abstract():
    assert not inspect.isabstract(py_If)


def test_py_if_constructor_exists():
    assert callable(py_If.__init__)


def test_py_if_constructor_args():
    sig = inspect.signature(py_If.__init__)
    params = list(sig.parameters.keys())



def test_py_eobject_is_not_abstract():
    assert not inspect.isabstract(py_EObject)


def test_py_eobject_constructor_exists():
    assert callable(py_EObject.__init__)


def test_py_eobject_constructor_args():
    sig = inspect.signature(py_EObject.__init__)
    params = list(sig.parameters.keys())



def test_py_exprand_is_not_abstract():
    assert not inspect.isabstract(py_ExprAnd)


def test_py_exprand_constructor_exists():
    assert callable(py_ExprAnd.__init__)


def test_py_exprand_constructor_args():
    sig = inspect.signature(py_ExprAnd.__init__)
    params = list(sig.parameters.keys())



def test_py_exprsimple_is_not_abstract():
    assert not inspect.isabstract(py_ExprSimple)


def test_py_exprsimple_constructor_exists():
    assert callable(py_ExprSimple.__init__)


def test_py_exprsimple_constructor_args():
    sig = inspect.signature(py_ExprSimple.__init__)
    params = list(sig.parameters.keys())
    assert "str" in params, "Missing parameter 'str'"
    assert "sym" in params, "Missing parameter 'sym'"
    assert "varSimple" in params, "Missing parameter 'varSimple'"

def test_py_exprsimple_has_str():
    assert hasattr(py_ExprSimple, "str")
    descriptor = None
    for klass in py_ExprSimple.__mro__:
        if "str" in klass.__dict__:
            descriptor = klass.__dict__["str"]
            break
    assert isinstance(descriptor, property)

def test_py_exprsimple_has_sym():
    assert hasattr(py_ExprSimple, "sym")
    descriptor = None
    for klass in py_ExprSimple.__mro__:
        if "sym" in klass.__dict__:
            descriptor = klass.__dict__["sym"]
            break
    assert isinstance(descriptor, property)

def test_py_exprsimple_has_varSimple():
    assert hasattr(py_ExprSimple, "varSimple")
    descriptor = None
    for klass in py_ExprSimple.__mro__:
        if "varSimple" in klass.__dict__:
            descriptor = klass.__dict__["varSimple"]
            break
    assert isinstance(descriptor, property)



def test_py_input_is_not_abstract():
    assert not inspect.isabstract(py_Input)


def test_py_input_constructor_exists():
    assert callable(py_Input.__init__)


def test_py_input_constructor_args():
    sig = inspect.signature(py_Input.__init__)
    params = list(sig.parameters.keys())
    assert "vars" in params, "Missing parameter 'vars'"

def test_py_input_has_vars():
    assert hasattr(py_Input, "vars")
    descriptor = None
    for klass in py_Input.__mro__:
        if "vars" in klass.__dict__:
            descriptor = klass.__dict__["vars"]
            break
    assert isinstance(descriptor, property)



def test_py_definition_is_not_abstract():
    assert not inspect.isabstract(py_Definition)


def test_py_definition_constructor_exists():
    assert callable(py_Definition.__init__)


def test_py_definition_constructor_args():
    sig = inspect.signature(py_Definition.__init__)
    params = list(sig.parameters.keys())



def test_py_functionp_is_not_abstract():
    assert not inspect.isabstract(py_FunctionP)


def test_py_functionp_constructor_exists():
    assert callable(py_FunctionP.__init__)


def test_py_functionp_constructor_args():
    sig = inspect.signature(py_FunctionP.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_py_functionp_has_name():
    assert hasattr(py_FunctionP, "name")
    descriptor = None
    for klass in py_FunctionP.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_py_program_is_not_abstract():
    assert not inspect.isabstract(py_Program)


def test_py_program_constructor_exists():
    assert callable(py_Program.__init__)


def test_py_program_constructor_args():
    sig = inspect.signature(py_Program.__init__)
    params = list(sig.parameters.keys())



def test_py_wh_is_not_abstract():
    assert not inspect.isabstract(py_Wh)


def test_py_wh_constructor_exists():
    assert callable(py_Wh.__init__)


def test_py_wh_constructor_args():
    sig = inspect.signature(py_Wh.__init__)
    params = list(sig.parameters.keys())



def test_py_command_is_not_abstract():
    assert not inspect.isabstract(py_Command)


def test_py_command_constructor_exists():
    assert callable(py_Command.__init__)


def test_py_command_constructor_args():
    sig = inspect.signature(py_Command.__init__)
    params = list(sig.parameters.keys())



def test_py_output_is_not_abstract():
    assert not inspect.isabstract(py_Output)


def test_py_output_constructor_exists():
    assert callable(py_Output.__init__)


def test_py_output_constructor_args():
    sig = inspect.signature(py_Output.__init__)
    params = list(sig.parameters.keys())
    assert "vars" in params, "Missing parameter 'vars'"

def test_py_output_has_vars():
    assert hasattr(py_Output, "vars")
    descriptor = None
    for klass in py_Output.__mro__:
        if "vars" in klass.__dict__:
            descriptor = klass.__dict__["vars"]
            break
    assert isinstance(descriptor, property)



def test_py_commands_is_not_abstract():
    assert not inspect.isabstract(py_Commands)


def test_py_commands_constructor_exists():
    assert callable(py_Commands.__init__)


def test_py_commands_constructor_args():
    sig = inspect.signature(py_Commands.__init__)
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
py_ExprEq_strategy = st.builds(
    py_ExprEq,
)
py_ExprNot_strategy = st.builds(
    py_ExprNot,
)
py_ExprSym_strategy = st.builds(
    py_ExprSym,
    arg1=
        safe_text
)
py_ExprTl_strategy = st.builds(
    py_ExprTl,
)
py_ExprHd_strategy = st.builds(
    py_ExprHd,
)
py_ExprList_strategy = st.builds(
    py_ExprList,
)
py_LExpr_strategy = st.builds(
    py_LExpr,
)
py_ExprCons_strategy = st.builds(
    py_ExprCons,
)
py_ExprOr_strategy = st.builds(
    py_ExprOr,
)
py_While_strategy = st.builds(
    py_While,
)
py_Foreach_strategy = st.builds(
    py_Foreach,
    var=
        safe_text
)
py_For_strategy = st.builds(
    py_For,
)
py_Affect_strategy = st.builds(
    py_Affect,
    vars=
        safe_text
)
py_Nop_strategy = st.builds(
    py_Nop,
    nop=
        safe_text
)
py_Expr_strategy = st.builds(
    py_Expr,
)
py_If_strategy = st.builds(
    py_If,
)
py_EObject_strategy = st.builds(
    py_EObject,
)
py_ExprAnd_strategy = st.builds(
    py_ExprAnd,
)
py_ExprSimple_strategy = st.builds(
    py_ExprSimple,
    str=
        safe_text,
    sym=
        safe_text,
    varSimple=
        safe_text
)
py_Input_strategy = st.builds(
    py_Input,
    vars=
        safe_text
)
py_Definition_strategy = st.builds(
    py_Definition,
)
py_FunctionP_strategy = st.builds(
    py_FunctionP,
    name=
        safe_text
)
py_Program_strategy = st.builds(
    py_Program,
)
py_Wh_strategy = st.builds(
    py_Wh,
)
py_Command_strategy = st.builds(
    py_Command,
)
py_Output_strategy = st.builds(
    py_Output,
    vars=
        safe_text
)
py_Commands_strategy = st.builds(
    py_Commands,
)

@given(instance=py_ExprEq_strategy)
@settings(max_examples=50)
def test_py_expreq_instantiation(instance):
    assert isinstance(instance, py_ExprEq)

@given(instance=py_ExprNot_strategy)
@settings(max_examples=50)
def test_py_exprnot_instantiation(instance):
    assert isinstance(instance, py_ExprNot)

@given(instance=py_ExprSym_strategy)
@settings(max_examples=50)
def test_py_exprsym_instantiation(instance):
    assert isinstance(instance, py_ExprSym)



@given(instance=py_ExprSym_strategy)
def test_py_exprsym_arg1_setter(instance):
    original = instance.arg1
    instance.arg1 = original
    assert instance.arg1 == original

@given(instance=py_ExprTl_strategy)
@settings(max_examples=50)
def test_py_exprtl_instantiation(instance):
    assert isinstance(instance, py_ExprTl)

@given(instance=py_ExprHd_strategy)
@settings(max_examples=50)
def test_py_exprhd_instantiation(instance):
    assert isinstance(instance, py_ExprHd)

@given(instance=py_ExprList_strategy)
@settings(max_examples=50)
def test_py_exprlist_instantiation(instance):
    assert isinstance(instance, py_ExprList)

@given(instance=py_LExpr_strategy)
@settings(max_examples=50)
def test_py_lexpr_instantiation(instance):
    assert isinstance(instance, py_LExpr)

@given(instance=py_ExprCons_strategy)
@settings(max_examples=50)
def test_py_exprcons_instantiation(instance):
    assert isinstance(instance, py_ExprCons)

@given(instance=py_ExprOr_strategy)
@settings(max_examples=50)
def test_py_expror_instantiation(instance):
    assert isinstance(instance, py_ExprOr)

@given(instance=py_While_strategy)
@settings(max_examples=50)
def test_py_while_instantiation(instance):
    assert isinstance(instance, py_While)

@given(instance=py_Foreach_strategy)
@settings(max_examples=50)
def test_py_foreach_instantiation(instance):
    assert isinstance(instance, py_Foreach)



@given(instance=py_Foreach_strategy)
def test_py_foreach_var_setter(instance):
    original = instance.var
    instance.var = original
    assert instance.var == original

@given(instance=py_For_strategy)
@settings(max_examples=50)
def test_py_for_instantiation(instance):
    assert isinstance(instance, py_For)

@given(instance=py_Affect_strategy)
@settings(max_examples=50)
def test_py_affect_instantiation(instance):
    assert isinstance(instance, py_Affect)



@given(instance=py_Affect_strategy)
def test_py_affect_vars_setter(instance):
    original = instance.vars
    instance.vars = original
    assert instance.vars == original

@given(instance=py_Nop_strategy)
@settings(max_examples=50)
def test_py_nop_instantiation(instance):
    assert isinstance(instance, py_Nop)



@given(instance=py_Nop_strategy)
def test_py_nop_nop_setter(instance):
    original = instance.nop
    instance.nop = original
    assert instance.nop == original

@given(instance=py_Expr_strategy)
@settings(max_examples=50)
def test_py_expr_instantiation(instance):
    assert isinstance(instance, py_Expr)

@given(instance=py_If_strategy)
@settings(max_examples=50)
def test_py_if_instantiation(instance):
    assert isinstance(instance, py_If)

@given(instance=py_EObject_strategy)
@settings(max_examples=50)
def test_py_eobject_instantiation(instance):
    assert isinstance(instance, py_EObject)

@given(instance=py_ExprAnd_strategy)
@settings(max_examples=50)
def test_py_exprand_instantiation(instance):
    assert isinstance(instance, py_ExprAnd)

@given(instance=py_ExprSimple_strategy)
@settings(max_examples=50)
def test_py_exprsimple_instantiation(instance):
    assert isinstance(instance, py_ExprSimple)



@given(instance=py_ExprSimple_strategy)
def test_py_exprsimple_str_setter(instance):
    original = instance.str
    instance.str = original
    assert instance.str == original



@given(instance=py_ExprSimple_strategy)
def test_py_exprsimple_sym_setter(instance):
    original = instance.sym
    instance.sym = original
    assert instance.sym == original



@given(instance=py_ExprSimple_strategy)
def test_py_exprsimple_varSimple_setter(instance):
    original = instance.varSimple
    instance.varSimple = original
    assert instance.varSimple == original

@given(instance=py_Input_strategy)
@settings(max_examples=50)
def test_py_input_instantiation(instance):
    assert isinstance(instance, py_Input)



@given(instance=py_Input_strategy)
def test_py_input_vars_setter(instance):
    original = instance.vars
    instance.vars = original
    assert instance.vars == original

@given(instance=py_Definition_strategy)
@settings(max_examples=50)
def test_py_definition_instantiation(instance):
    assert isinstance(instance, py_Definition)

@given(instance=py_FunctionP_strategy)
@settings(max_examples=50)
def test_py_functionp_instantiation(instance):
    assert isinstance(instance, py_FunctionP)



@given(instance=py_FunctionP_strategy)
def test_py_functionp_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=py_Program_strategy)
@settings(max_examples=50)
def test_py_program_instantiation(instance):
    assert isinstance(instance, py_Program)

@given(instance=py_Wh_strategy)
@settings(max_examples=50)
def test_py_wh_instantiation(instance):
    assert isinstance(instance, py_Wh)

@given(instance=py_Command_strategy)
@settings(max_examples=50)
def test_py_command_instantiation(instance):
    assert isinstance(instance, py_Command)

@given(instance=py_Output_strategy)
@settings(max_examples=50)
def test_py_output_instantiation(instance):
    assert isinstance(instance, py_Output)



@given(instance=py_Output_strategy)
def test_py_output_vars_setter(instance):
    original = instance.vars
    instance.vars = original
    assert instance.vars == original

@given(instance=py_Commands_strategy)
@settings(max_examples=50)
def test_py_commands_instantiation(instance):
    assert isinstance(instance, py_Commands)
